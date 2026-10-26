# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 9
TRIANGLES: CONGRUENCE THEOREMS (Competencies CG-4, C-4.1, C-7.3, CG-9)
Generates public/animations/class9-triangles-congruence.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_triangles_congruence_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-triangles-congruence.html"

# Ensure exp is duplicated to explanation for checkpoints
for s in SLIDES:
    for cp in s["checkpoints"]:
        cp["explanation"] = cp.get("exp", cp.get("explanation", ""))

def generate_html():
    slides_json = json.dumps(SLIDES)
    quizzes_json = json.dumps(QUIZZES)

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Mathematics • Triangles: Congruence Theorems Lab</title>
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
        @keyframes mouthMove {
            0%, 100% { transform: scaleY(0.2); }
            50% { transform: scaleY(1.1); }
        }
        .talking #teacherMouth {
            animation: mouthMove 0.22s infinite alternate ease-in-out;
            transform-origin: center bottom;
        }
        .glass-panel {
            background: rgba(15, 23, 42, 0.78);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        .glow-indigo {
            box-shadow: 0 0 25px -5px rgba(99, 102, 241, 0.35);
        }
        .glow-emerald {
            box-shadow: 0 0 25px -5px rgba(16, 185, 129, 0.35);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-indigo-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="border-b border-slate-800/80 bg-slate-900/80 backdrop-blur sticky top-0 z-40 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=mathematics&class=class9" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">
                    <i data-lucide="arrow-left" class="w-5 h-5"></i>
                </a>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">NCERT CLASS 9</span>
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">UNIT II: GEOMETRY</span>
                        <span class="hidden md:inline-block px-2 py-0.5 rounded text-[11px] font-medium bg-slate-800 text-slate-400">CG-4 • C-4.1 • C-7.3 • CG-9</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-slate-100 flex items-center gap-2">
                        Triangles: Congruence Theorems Lab
                    </h1>
                </div>
            </div>

            <!-- Slide Picker & Audio Controls -->
            <div class="flex items-center gap-2">
                <div class="relative">
                    <select id="slidePicker" class="bg-slate-800 border border-slate-700 text-slate-200 text-xs sm:text-sm rounded-lg px-2.5 py-1.5 pr-8 focus:ring-2 focus:ring-indigo-500 appearance-none font-medium">
                        <!-- Populated by JS -->
                    </select>
                    <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none"></i>
                </div>

                <button id="toggleAudioBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-600/90 hover:bg-indigo-600 text-white text-xs sm:text-sm font-semibold shadow-lg shadow-indigo-600/20 transition">
                    <i data-lucide="volume-2" id="audioIcon" class="w-4 h-4"></i>
                    <span id="audioStatusText" class="hidden sm:inline">Narration ON</span>
                </button>
            </div>
        </div>

        <!-- Global Progress Bar -->
        <div class="w-full bg-slate-800 h-1.5 mt-2 rounded-full overflow-hidden">
            <div id="slideProgressBar" class="bg-gradient-to-r from-indigo-500 via-sky-400 to-emerald-400 h-full transition-all duration-300" style="width: 5%;"></div>
        </div>
    </header>

    <!-- Main Workspace -->
    <main class="flex-1 max-w-7xl mx-auto w-full p-3 sm:p-5 flex flex-col gap-5">

        <!-- Slide Header Banner -->
        <div class="glass-panel rounded-2xl p-4 sm:p-5 flex flex-col md:flex-row md:items-center justify-between gap-4 border-l-4 border-l-indigo-500">
            <div>
                <div class="flex items-center gap-2 text-xs font-semibold text-indigo-400 mb-1">
                    <span id="slideBadge" class="px-2.5 py-0.5 rounded-full bg-indigo-500/10 border border-indigo-500/20">Slide 1 of 20</span>
                    <span id="slideCategory" class="text-slate-400 uppercase tracking-wider text-[10px]">Practical Applications</span>
                </div>
                <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white">Structural Rigidity of Triangles vs. Quadrilaterals</h2>
                <p id="slideSubtitle" class="text-xs sm:text-sm text-slate-300 mt-1 font-medium">Kinematic Degrees of Freedom, 3-Bar vs 4-Bar Linkages & Practical Truss Engineering</p>
            </div>

            <!-- Avatar & Teacher Speech Bubble -->
            <div class="flex items-center gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 max-w-md w-full shrink-0">
                <!-- SVG Avatar Prof. Sophia -->
                <div id="avatarContainer" class="relative w-12 h-12 rounded-full bg-gradient-to-tr from-indigo-600 to-emerald-500 p-0.5 shrink-0 shadow-lg shadow-indigo-500/20">
                    <svg viewBox="0 0 100 100" class="w-full h-full rounded-full bg-slate-900">
                        <circle cx="50" cy="50" r="48" fill="#1e293b"/>
                        <!-- Hair back -->
                        <path d="M25 55 C20 30 35 15 50 15 C65 15 80 30 75 55 C70 45 65 30 50 30 C35 30 30 45 25 55 Z" fill="#6366f1"/>
                        <!-- Head -->
                        <circle cx="50" cy="50" r="26" fill="#fcd34d"/>
                        <!-- Glasses -->
                        <circle cx="42" cy="48" r="7" fill="none" stroke="#0f172a" stroke-width="2.5"/>
                        <circle cx="58" cy="48" r="7" fill="none" stroke="#0f172a" stroke-width="2.5"/>
                        <line x1="49" y1="48" x2="51" y2="48" stroke="#0f172a" stroke-width="2.5"/>
                        <!-- Eyes -->
                        <circle cx="42" cy="48" r="2.5" fill="#0f172a"/>
                        <circle cx="58" cy="48" r="2.5" fill="#0f172a"/>
                        <!-- Nose -->
                        <path d="M50 51 L48 55 L52 55" fill="none" stroke="#d97706" stroke-width="1.5" stroke-linecap="round"/>
                        <!-- Mouth (Animated) -->
                        <ellipse id="teacherMouth" cx="50" cy="63" rx="4" ry="1.5" fill="#991b1b"/>
                        <!-- Hair Front Fringe -->
                        <path d="M30 32 Q50 40 70 32 Q60 22 50 22 Q40 22 30 32 Z" fill="#4f46e5"/>
                        <!-- Graduation Cap -->
                        <polygon points="50,10 82,24 50,32 18,24" fill="#0f172a"/>
                        <polygon points="50,11 78,24 50,31 22,24" fill="#1e1b4b"/>
                        <path d="M72 26 L76 38 L72 40" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
                    </svg>
                    <span id="speechIndicator" class="absolute -bottom-1 -right-1 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-slate-900 hidden"></span>
                </div>
                <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-bold text-indigo-300">Prof. Sophia</span>
                        <button id="replaySpeechBtn" class="text-[10px] text-slate-400 hover:text-white flex items-center gap-1">
                            <i data-lucide="rotate-ccw" class="w-3 h-3"></i> Replay
                        </button>
                    </div>
                    <p id="teacherSpeech" class="text-xs text-slate-300 line-clamp-3 italic mt-0.5 leading-snug">
                        Welcome to Triangles: Congruence Theorems! Let's explore how triangle rigidity forms the backbone of modern engineering.
                    </p>
                </div>
            </div>
        </div>

        <!-- Dynamic Content Body (Changes between Slides 1-16 and Quiz Slides 17-20) -->
        <div id="dynamicSlideContent" class="flex-1 flex flex-col gap-5">
            <!-- Injected by renderCurrentSlide() -->
        </div>

        <!-- Last Slide Notice Banner (Strictly required on Slide 20) -->
        <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-indigo-950/40 shadow-xl shadow-emerald-950/30">
            <div class="w-16 h-16 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mb-3">
                <i data-lucide="award" class="w-8 h-8"></i>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-white">Congratulations!</h3>
            <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
            <p class="text-xs sm:text-sm text-slate-400 max-w-xl mx-auto mt-2">
                You have mastered structural triangle rigidity, all 5 congruence conditions (SAS, ASA, AAS, SSS, RHS), Isosceles Pons Asinorum proofs, conditional propositions & converses, the Ambiguous Case of SSA, diagram fallacies, and computational truss engineering.
            </p>
            <div class="flex flex-wrap items-center justify-center gap-3 mt-4">
                <button onclick="jumpToSlide(0)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold flex items-center gap-2 transition">
                    <i data-lucide="rotate-ccw" class="w-4 h-4"></i> Restart from Slide 1
                </button>
                <a href="/multimedia?syllabus=ncert&subject=mathematics&class=class9" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/30 flex items-center gap-2 transition">
                    <i data-lucide="book-open" class="w-4 h-4"></i> Back to Mathematics Curriculum
                </a>
            </div>
        </div>

        <!-- Navigation Footer -->
        <footer class="glass-panel rounded-xl p-3 sm:p-4 flex items-center justify-between gap-4 mt-auto">
            <button id="prevBtn" class="flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs sm:text-sm font-semibold transition disabled:opacity-40 disabled:cursor-not-allowed">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                <span>Previous Slide</span>
            </button>

            <div class="flex items-center gap-3 text-xs sm:text-sm font-bold text-slate-400">
                <span id="slideIndicator">Slide 1 / 20</span>
            </div>

            <button id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs sm:text-sm font-bold shadow-lg shadow-indigo-600/20 transition">
                <span>Next Slide</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </footer>
    </main>

    <!-- Quiz Solution Pop-up Modal -->
    <div id="solutionModal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 hidden">
        <div class="glass-panel max-w-2xl w-full rounded-2xl border border-indigo-500/30 shadow-2xl p-6 relative max-h-[85vh] overflow-y-auto">
            <button id="closeSolutionBtn" class="absolute top-4 right-4 p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>

            <div class="flex items-center gap-2.5 text-xs font-bold text-emerald-400 mb-2">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                <span id="solutionModalBadge">Detailed Step-by-Step Solution</span>
            </div>

            <h3 id="solutionModalTitle" class="text-base sm:text-lg font-bold text-white mb-3">Question Statement</h3>

            <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 mb-4">
                <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Correct Answer</div>
                <div id="solutionModalAns" class="text-sm font-bold text-emerald-300">Option Text</div>
            </div>

            <div>
                <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5">Mathematical Justification & Proof</div>
                <div id="solutionModalBody" class="text-xs sm:text-sm text-slate-200 leading-relaxed font-mono bg-slate-950/60 p-4 rounded-xl border border-slate-800/80 whitespace-pre-wrap">
                    Solution text...
                </div>
            </div>

            <div class="mt-5 flex justify-end">
                <button onclick="closeModal()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition">
                    Got it, Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Application Logic Scripts -->
    <script>
        const SLIDES_DATA = __SLIDES_JSON__;
        const QUIZZES_DATA = __QUIZZES_JSON__;

        const totalSlides = 20;
        let currentSlideIndex = 0;
        let isAudioMuted = false;
        let currentUtterance = null;
        let audioSynthContext = null;

        // Elements
        const slidePicker = document.getElementById('slidePicker');
        const slideProgressBar = document.getElementById('slideProgressBar');
        const slideBadge = document.getElementById('slideBadge');
        const slideCategory = document.getElementById('slideCategory');
        const slideTitle = document.getElementById('slideTitle');
        const slideSubtitle = document.getElementById('slideSubtitle');
        const teacherSpeech = document.getElementById('teacherSpeech');
        const speechIndicator = document.getElementById('speechIndicator');
        const avatarContainer = document.getElementById('avatarContainer');
        const toggleAudioBtn = document.getElementById('toggleAudioBtn');
        const audioIcon = document.getElementById('audioIcon');
        const audioStatusText = document.getElementById('audioStatusText');
        const replaySpeechBtn = document.getElementById('replaySpeechBtn');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const slideIndicator = document.getElementById('slideIndicator');
        const dynamicSlideContent = document.getElementById('dynamicSlideContent');
        const lastSlideNotice = document.getElementById('lastSlideNotice');

        // Modal Elements
        const solutionModal = document.getElementById('solutionModal');
        const closeSolutionBtn = document.getElementById('closeSolutionBtn');
        const solutionModalTitle = document.getElementById('solutionModalTitle');
        const solutionModalAns = document.getElementById('solutionModalAns');
        const solutionModalBody = document.getElementById('solutionModalBody');

        // Initialize Slide Picker
        function initSlidePicker() {
            slidePicker.innerHTML = '';
            for (let i = 0; i < 16; i++) {
                const opt = document.createElement('option');
                opt.value = i;
                opt.textContent = `Slide ${i + 1}: ${SLIDES_DATA[i].title}`;
                slidePicker.appendChild(opt);
            }
            for (let i = 0; i < 4; i++) {
                const opt = document.createElement('option');
                opt.value = 16 + i;
                opt.textContent = `Slide ${17 + i}: ${QUIZZES_DATA[i].title}`;
                slidePicker.appendChild(opt);
            }
        }

        // Speech Narration
        function speakCurrentSlide(text) {
            if (isAudioMuted) return;
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                currentUtterance = new SpeechSynthesisUtterance(text);
                currentUtterance.rate = 1.0;
                currentUtterance.pitch = 1.05;
                currentUtterance.lang = 'en-US';

                currentUtterance.onstart = () => {
                    avatarContainer.classList.add('talking');
                    speechIndicator.classList.remove('hidden');
                };
                currentUtterance.onend = () => {
                    avatarContainer.classList.remove('talking');
                    speechIndicator.classList.add('hidden');
                };
                currentUtterance.onerror = () => {
                    avatarContainer.classList.remove('talking');
                    speechIndicator.classList.add('hidden');
                    playSynthesizedChime();
                };
                window.speechSynthesis.speak(currentUtterance);
            } else {
                playSynthesizedChime();
            }
        }

        function playSynthesizedChime() {
            try {
                if (!audioSynthContext) {
                    audioSynthContext = new (window.AudioContext || window.webkitAudioContext)();
                }
                const osc = audioSynthContext.createOscillator();
                const gain = audioSynthContext.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, audioSynthContext.currentTime);
                osc.frequency.exponentialRampToValueAtTime(880, audioSynthContext.currentTime + 0.3);
                gain.gain.setValueAtTime(0.1, audioSynthContext.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioSynthContext.currentTime + 0.3);
                osc.connect(gain);
                gain.connect(audioSynthContext.destination);
                osc.start();
                osc.stop(audioSynthContext.currentTime + 0.3);
            } catch (e) {}
        }

        function stopSpeaking() {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
            }
            avatarContainer.classList.remove('talking');
            speechIndicator.classList.add('hidden');
        }

        // Render Current Slide
        function renderCurrentSlide() {
            stopSpeaking();
            slidePicker.value = currentSlideIndex;
            slideProgressBar.style.width = `${((currentSlideIndex + 1) / totalSlides) * 100}%`;
            slideIndicator.textContent = `Slide ${currentSlideIndex + 1} / ${totalSlides}`;

            prevBtn.disabled = (currentSlideIndex === 0);

            // Handle slide 20 lastSlideNotice & nextBtn display
            if (currentSlideIndex === 19) {
                nextBtn.style.display = 'none';
                lastSlideNotice.classList.remove('hidden');
            } else {
                nextBtn.style.display = 'inline-flex';
                lastSlideNotice.classList.add('hidden');
            }

            if (currentSlideIndex < 16) {
                // Content Slide
                renderContentSlide(SLIDES_DATA[currentSlideIndex]);
            } else {
                // Quiz Slide (17 - 20)
                renderQuizSlide(QUIZZES_DATA[currentSlideIndex - 16]);
            }

            lucide.createIcons();
            if (window.renderMathInElement) {
                renderMathInElement(document.body);
            }
        }

        // Render Content Slide (1 - 16)
        function renderContentSlide(slide) {
            slideBadge.textContent = `Slide ${slide.id} of 20`;
            slideCategory.textContent = slide.category;
            slideTitle.textContent = slide.title;
            slideSubtitle.textContent = slide.subtitle;
            teacherSpeech.textContent = slide.narration;

            speakCurrentSlide(slide.narration);

            let keyPointsHtml = slide.key_points.map(pt => `
                <li class="flex items-start gap-2 text-xs sm:text-sm text-slate-300">
                    <i data-lucide="check" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                    <span>${pt}</span>
                </li>
            `).join('');

            let checkpointsHtml = slide.checkpoints.map((cp, qIdx) => `
                <div class="glass-card rounded-xl p-4 border border-slate-800" id="cp_card_${slide.id}_${qIdx}">
                    <div class="flex items-center gap-2 text-[11px] font-bold text-indigo-400 mb-2">
                        <i data-lucide="help-circle" class="w-3.5 h-3.5"></i> Checkpoint ${qIdx + 1}
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-slate-100 mb-3">${cp.q}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3">
                        ${cp.options.map((opt, oIdx) => `
                            <button onclick="checkCheckpointAnswer(${slide.id}, ${qIdx}, ${oIdx}, ${cp.ans})"
                                    id="cp_btn_${slide.id}_${qIdx}_${oIdx}"
                                    class="text-left px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800/90 text-xs text-slate-300 border border-slate-800 transition">
                                <span class="font-bold text-slate-400 mr-1.5">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
                            </button>
                        `).join('')}
                    </div>
                    <div id="cp_exp_${slide.id}_${qIdx}" class="hidden p-3 rounded-lg text-xs leading-relaxed"></div>
                </div>
            `).join('');

            dynamicSlideContent.innerHTML = `
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
                    <!-- Left Column: Summary & Concepts -->
                    <div class="lg:col-span-5 flex flex-col gap-4">
                        <div class="glass-panel rounded-2xl p-4 sm:p-5">
                            <h3 class="text-xs font-bold text-indigo-400 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                                <i data-lucide="book-marked" class="w-4 h-4"></i> Core Mathematical Foundation
                            </h3>
                            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-normal">${slide.summary}</p>

                            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mt-4 mb-2">Key Principles</h4>
                            <ul class="space-y-2">
                                ${keyPointsHtml}
                            </ul>
                        </div>

                        <!-- Checkpoints Box -->
                        <div class="glass-panel rounded-2xl p-4 sm:p-5 flex flex-col gap-3">
                            <h3 class="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
                                <i data-lucide="zap" class="w-4 h-4"></i> Interactive Checkpoint Questions
                            </h3>
                            ${checkpointsHtml}
                        </div>
                    </div>

                    <!-- Right Column: Interactive Simulator -->
                    <div class="lg:col-span-7 glass-panel rounded-2xl p-4 sm:p-5 flex flex-col">
                        <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
                            <div class="flex items-center gap-2">
                                <span class="p-1.5 rounded-lg bg-indigo-500/20 text-indigo-400">
                                    <i data-lucide="play" class="w-4 h-4"></i>
                                </span>
                                <span class="text-xs sm:text-sm font-bold text-slate-100">${slide.sim_title}</span>
                            </div>
                            <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Interactive Simulator</span>
                        </div>
                        <div id="simulatorContainer" class="flex-1 w-full min-h-[440px] flex flex-col justify-center">
                            <!-- Injected by renderSimulator(slide.id) -->
                        </div>
                    </div>
                </div>
            `;

            renderSimulator(slide.id);
        }

        // Render Quiz Slide (17 - 20)
        function renderQuizSlide(quiz) {
            slideBadge.textContent = `Slide ${quiz.slide_id} of 20`;
            slideCategory.textContent = quiz.category;
            slideTitle.textContent = quiz.title;
            slideSubtitle.textContent = quiz.subtitle;
            const quizNarration = `Welcome to ${quiz.title}! Challenge yourself with these 10 mastery questions. Test your understanding and click 'View Solution' for complete mathematical justifications.`;
            teacherSpeech.textContent = quizNarration;
            speakCurrentSlide(quizNarration);

            let questionsHtml = quiz.questions.map((q, idx) => `
                <div class="glass-card rounded-xl p-4 border border-slate-800" id="quiz_q_${quiz.slide_id}_${idx}">
                    <div class="flex items-center justify-between mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300">Question ${idx + 1} of 10</span>
                        <button onclick="openSolutionModal(${quiz.slide_id}, ${idx})"
                                class="px-2.5 py-1 rounded-lg bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 text-xs font-semibold flex items-center gap-1 border border-indigo-500/40 transition">
                            <i data-lucide="file-text" class="w-3.5 h-3.5"></i> View Solution
                        </button>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-slate-100 mb-3">${q.q}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        ${q.options.map((opt, oIdx) => `
                            <button onclick="checkQuizAnswer(${quiz.slide_id}, ${idx}, ${oIdx}, ${q.ans})"
                                    id="quiz_btn_${quiz.slide_id}_${idx}_${oIdx}"
                                    class="text-left px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-xs text-slate-300 border border-slate-800 transition">
                                <span class="font-bold text-slate-400 mr-1.5">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
                            </button>
                        `).join('')}
                    </div>
                    <div id="quiz_feedback_${quiz.slide_id}_${idx}" class="hidden p-2 rounded-lg text-xs font-semibold mt-2"></div>
                </div>
            `).join('');

            dynamicSlideContent.innerHTML = `
                <div class="glass-panel rounded-2xl p-4 sm:p-6 flex flex-col gap-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                        <div class="flex items-center gap-2">
                            <i data-lucide="trophy" class="w-5 h-5 text-amber-400"></i>
                            <h3 class="text-sm sm:text-base font-bold text-white">10-Question Mastery Assessment</h3>
                        </div>
                        <span class="text-xs text-slate-400 font-medium">Click on your answer, then inspect the popup solution</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        ${questionsHtml}
                    </div>
                </div>
            `;
        }

        // Checkpoint Handler
        window.checkCheckpointAnswer = function(slideId, qIdx, selectedIdx, correctIdx) {
            const expDiv = document.getElementById(`cp_exp_${slideId}_${qIdx}`);
            const slide = SLIDES_DATA.find(s => s.id === slideId);
            const cp = slide.checkpoints[qIdx];

            for (let i = 0; i < cp.options.length; i++) {
                const btn = document.getElementById(`cp_btn_${slideId}_${qIdx}_${i}`);
                btn.disabled = true;
                if (i === correctIdx) {
                    btn.classList.remove('bg-slate-900', 'text-slate-300', 'border-slate-800');
                    btn.classList.add('bg-emerald-900/60', 'text-emerald-200', 'border-emerald-500');
                } else if (i === selectedIdx && selectedIdx !== correctIdx) {
                    btn.classList.remove('bg-slate-900', 'text-slate-300', 'border-slate-800');
                    btn.classList.add('bg-rose-900/60', 'text-rose-200', 'border-rose-500');
                }
            }

            expDiv.classList.remove('hidden');
            if (selectedIdx === correctIdx) {
                expDiv.className = 'p-3 rounded-lg text-xs leading-relaxed bg-emerald-950/60 border border-emerald-500/40 text-emerald-200 mt-2';
                expDiv.innerHTML = `<span class="font-bold text-emerald-300">✓ Correct!</span> ${cp.explanation}`;
            } else {
                expDiv.className = 'p-3 rounded-lg text-xs leading-relaxed bg-rose-950/60 border border-rose-500/40 text-rose-200 mt-2';
                expDiv.innerHTML = `<span class="font-bold text-rose-300">✗ Incorrect.</span> ${cp.explanation}`;
            }
        };

        // Quiz Question Answer Handler
        window.checkQuizAnswer = function(quizSlideId, qIdx, selectedIdx, correctIdx) {
            const feedbackDiv = document.getElementById(`quiz_feedback_${quizSlideId}_${qIdx}`);
            const quiz = QUIZZES_DATA.find(q => q.slide_id === quizSlideId);
            const question = quiz.questions[qIdx];

            for (let i = 0; i < question.options.length; i++) {
                const btn = document.getElementById(`quiz_btn_${quizSlideId}_${qIdx}_${i}`);
                btn.disabled = true;
                if (i === correctIdx) {
                    btn.classList.remove('bg-slate-900', 'text-slate-300', 'border-slate-800');
                    btn.classList.add('bg-emerald-900/60', 'text-emerald-200', 'border-emerald-500');
                } else if (i === selectedIdx && selectedIdx !== correctIdx) {
                    btn.classList.remove('bg-slate-900', 'text-slate-300', 'border-slate-800');
                    btn.classList.add('bg-rose-900/60', 'text-rose-200', 'border-rose-500');
                }
            }

            feedbackDiv.classList.remove('hidden');
            if (selectedIdx === correctIdx) {
                feedbackDiv.className = 'p-2 rounded-lg text-xs font-semibold mt-2 bg-emerald-950/60 text-emerald-300 border border-emerald-500/40';
                feedbackDiv.innerHTML = `✓ Correct! Click 'View Solution' for the full mathematical proof.`;
            } else {
                feedbackDiv.className = 'p-2 rounded-lg text-xs font-semibold mt-2 bg-rose-950/60 text-rose-300 border border-rose-500/40';
                feedbackDiv.innerHTML = `✗ Incorrect. Click 'View Solution' to inspect the step-by-step reasoning.`;
            }
        };

        // Solution Modal Handler
        window.openSolutionModal = function(quizSlideId, qIdx) {
            const quiz = QUIZZES_DATA.find(q => q.slide_id === quizSlideId);
            const question = quiz.questions[qIdx];

            solutionModalTitle.textContent = `Q${qIdx + 1}: ${question.q}`;
            solutionModalAns.textContent = `${String.fromCharCode(65 + question.ans)}. ${question.options[question.ans]}`;
            solutionModalBody.textContent = question.exp;

            solutionModal.classList.remove('hidden');
            if (window.renderMathInElement) {
                renderMathInElement(solutionModal);
            }
        };

        window.closeModal = function() {
            solutionModal.classList.add('hidden');
        };

        closeSolutionBtn.addEventListener('click', closeModal);
        solutionModal.addEventListener('click', (e) => {
            if (e.target === solutionModal) closeModal();
        });

        // Navigation Handlers
        prevBtn.addEventListener('click', () => {
            if (currentSlideIndex > 0) {
                currentSlideIndex--;
                renderCurrentSlide();
            }
        });

        nextBtn.addEventListener('click', () => {
            if (currentSlideIndex < totalSlides - 1) {
                currentSlideIndex++;
                renderCurrentSlide();
            }
        });

        slidePicker.addEventListener('change', (e) => {
            currentSlideIndex = parseInt(e.target.value);
            renderCurrentSlide();
        });

        window.jumpToSlide = function(idx) {
            currentSlideIndex = idx;
            renderCurrentSlide();
        };

        toggleAudioBtn.addEventListener('click', () => {
            isAudioMuted = !isAudioMuted;
            if (isAudioMuted) {
                stopSpeaking();
                audioIcon.setAttribute('data-lucide', 'volume-x');
                audioStatusText.textContent = 'Narration OFF';
                toggleAudioBtn.classList.remove('bg-indigo-600/90', 'hover:bg-indigo-600');
                toggleAudioBtn.classList.add('bg-slate-800', 'hover:bg-slate-700', 'text-slate-400');
            } else {
                audioIcon.setAttribute('data-lucide', 'volume-2');
                audioStatusText.textContent = 'Narration ON';
                toggleAudioBtn.classList.add('bg-indigo-600/90', 'hover:bg-indigo-600');
                toggleAudioBtn.classList.remove('bg-slate-800', 'hover:bg-slate-700', 'text-slate-400');
                if (currentSlideIndex < 16) {
                    speakCurrentSlide(SLIDES_DATA[currentSlideIndex].narration);
                }
            }
            lucide.createIcons();
        });

        replaySpeechBtn.addEventListener('click', () => {
            if (currentSlideIndex < 16) {
                speakCurrentSlide(SLIDES_DATA[currentSlideIndex].narration);
            } else {
                speakCurrentSlide(QUIZZES_DATA[currentSlideIndex - 16].title);
            }
        });

        // ==========================================
        // 16 BESPOKE INTERACTIVE SVG SIMULATORS
        // ==========================================
        function renderSimulator(slideId) {
            const container = document.getElementById('simulatorContainer');
            if (!container) return;
            container.innerHTML = '';

            switch (slideId) {
                case 1: renderSim1(container); break;
                case 2: renderSim2(container); break;
                case 3: renderSim3(container); break;
                case 4: renderSim4(container); break;
                case 5: renderSim5(container); break;
                case 6: renderSim6(container); break;
                case 7: renderSim7(container); break;
                case 8: renderSim8(container); break;
                case 9: renderSim9(container); break;
                case 10: renderSim10(container); break;
                case 11: renderSim11(container); break;
                case 12: renderSim12(container); break;
                case 13: renderSim13(container); break;
                case 14: renderSim14(container); break;
                case 15: renderSim15(container); break;
                case 16: renderSim16(container); break;
                default:
                    container.innerHTML = `<div class="text-slate-400 text-sm">Simulator loading...</div>`;
            }
            lucide.createIcons();
            if (window.renderMathInElement) {
                renderMathInElement(container);
            }
        }

        // Sim 1: Structural Rigidity (3-Bar vs 4-Bar Linkage)
        function renderSim1(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between gap-3 text-xs bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Shear 4-Bar Quadrilateral Angle:</label>
                            <input type="range" id="sim1_angle" min="45" max="135" value="90" class="w-32 accent-indigo-500">
                            <span id="sim1_angle_val" class="font-mono text-indigo-400 font-bold">90°</span>
                        </div>
                        <button id="sim1_brace_btn" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 font-bold border border-emerald-500/40 text-xs transition">
                            + Add Diagonal Strut Brace
                        </button>
                    </div>

                    <div class="flex-1 min-h-[300px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim1_svg" viewBox="0 0 600 300" class="w-full h-full max-h-[300px]">
                            <!-- Left: 4-Bar Quadrilateral Linkage -->
                            <g id="sim1_quad_group"></g>
                            <!-- Right: 3-Bar Triangle Linkage -->
                            <g id="sim1_tri_group"></g>
                        </svg>
                    </div>

                    <div id="sim1_badge" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/30 text-rose-300">
                        ⚠ 4-Bar Linkage has 1 Degree of Freedom: Unstable, shears smoothly into a parallelogram without altering side lengths!
                    </div>
                </div>
            `;

            let hasBrace = false;
            const slider = document.getElementById('sim1_angle');
            const angleVal = document.getElementById('sim1_angle_val');
            const braceBtn = document.getElementById('sim1_brace_btn');
            const badge = document.getElementById('sim1_badge');
            const quadGroup = document.getElementById('sim1_quad_group');
            const triGroup = document.getElementById('sim1_tri_group');

            function update() {
                let thetaDeg = parseFloat(slider.value);
                if (hasBrace) {
                    thetaDeg = 90;
                    slider.value = 90;
                    slider.disabled = true;
                } else {
                    slider.disabled = false;
                }
                angleVal.textContent = `${thetaDeg}°`;
                const rad = (thetaDeg * Math.PI) / 180;

                // 4-bar geometry (Base A1(70,240), B1(210,240), side L=120)
                const xA = 70, yA = 240;
                const xB = 210, yB = 240;
                const L = 120;
                const xD = xA + L * Math.cos(rad);
                const yD = yA - L * Math.sin(rad);
                const xC = xB + L * Math.cos(rad);
                const yC = yB - L * Math.sin(rad);

                let quadHtml = `
                    <text x="140" y="30" text-anchor="middle" fill="#94a3b8" font-size="12" font-weight="bold">4-Bar Quadrilateral (Hinged Pins)</text>
                    <!-- Beams -->
                    <line x1="${xA}" y1="${yA}" x2="${xB}" y2="${yB}" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
                    <line x1="${xA}" y1="${yA}" x2="${xD}" y2="${yD}" stroke="#38bdf8" stroke-width="8" stroke-linecap="round"/>
                    <line x1="${xD}" y1="${yD}" x2="${xC}" y2="${yC}" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
                    <line x1="${xB}" y1="${yB}" x2="${xC}" y2="${yC}" stroke="#38bdf8" stroke-width="8" stroke-linecap="round"/>
                `;

                if (hasBrace) {
                    quadHtml += `
                        <line x1="${xA}" y1="${yA}" x2="${xC}" y2="${yC}" stroke="#10b981" stroke-width="6" stroke-dasharray="6,4" stroke-linecap="round"/>
                        <text x="${(xA+xC)/2}" y="${(yA+yC)/2 - 10}" fill="#10b981" font-size="11" font-weight="bold">Diagonal Brace</text>
                    `;
                }

                // Pins
                [ [xA,yA,'A'], [xB,yB,'B'], [xC,yC,'C'], [xD,yD,'D'] ].forEach(([x,y,l]) => {
                    quadHtml += `
                        <circle cx="${x}" cy="${y}" r="8" fill="#0f172a" stroke="#e2e8f0" stroke-width="3"/>
                        <text x="${x + (x<140?-15:15)}" y="${y + (y<150?-10:15)}" fill="#f8fafc" font-size="11" font-weight="bold">${l}</text>
                    `;
                });
                quadGroup.innerHTML = quadHtml;

                // Triangle 3-bar geometry (Base A2(370,240), B2(510,240), side L=140 equilateral)
                const tA = 370, tB = 510, tY = 240;
                const tMidX = (tA + tB) / 2;
                const tHeight = 140 * Math.sin(Math.PI / 3);
                const tC_x = tMidX;
                const tC_y = tY - tHeight;

                triGroup.innerHTML = `
                    <text x="440" y="30" text-anchor="middle" fill="#94a3b8" font-size="12" font-weight="bold">3-Bar Triangle (Hinged Pins)</text>
                    <line x1="${tA}" y1="${tY}" x2="${tB}" y2="${tY}" stroke="#10b981" stroke-width="8" stroke-linecap="round"/>
                    <line x1="${tA}" y1="${tY}" x2="${tC_x}" y2="${tC_y}" stroke="#10b981" stroke-width="8" stroke-linecap="round"/>
                    <line x1="${tB}" y1="${tY}" x2="${tC_x}" y2="${tC_y}" stroke="#10b981" stroke-width="8" stroke-linecap="round"/>
                    <circle cx="${tA}" cy="${tY}" r="8" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                    <circle cx="${tB}" cy="${tY}" r="8" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                    <circle cx="${tC_x}" cy="${tC_y}" r="8" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                    <text x="440" y="170" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">LOCKED RIGID (SSS)</text>
                    <text x="440" y="190" fill="#94a3b8" font-size="10" text-anchor="middle">0 Degrees of Freedom</text>
                `;

                if (hasBrace) {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    badge.innerHTML = `✓ RIGID! The diagonal strut partitions the frame into 2 triangles. By SSS, the angles are locked!`;
                    braceBtn.textContent = '✕ Remove Diagonal Strut';
                    braceBtn.className = 'px-3 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 font-bold border border-rose-500/40 text-xs transition';
                } else {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/30 text-rose-300';
                    badge.innerHTML = `⚠ 4-Bar Linkage has 1 Degree of Freedom: Unstable, shears smoothly into a parallelogram without altering side lengths!`;
                    braceBtn.textContent = '+ Add Diagonal Strut Brace';
                    braceBtn.className = 'px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 font-bold border border-emerald-500/40 text-xs transition';
                }
            }

            slider.addEventListener('input', update);
            braceBtn.addEventListener('click', () => {
                hasBrace = !hasBrace;
                update();
            });
            update();
        }

        // Sim 2: Superposition & Rigid Transformations
        function renderSim2(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Translate X:</label>
                            <input type="range" id="sim2_tx" min="-80" max="80" value="50" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Translate Y:</label>
                            <input type="range" id="sim2_ty" min="-60" max="60" value="-30" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Rotate θ:</label>
                            <input type="range" id="sim2_rot" min="0" max="360" value="45" class="w-full accent-indigo-500">
                        </div>
                        <div class="flex items-end">
                            <button id="sim2_snap" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                                Auto-Superimpose
                            </button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[300px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 300" class="w-full h-full max-h-[300px]">
                            <!-- Target Triangle △ABC (Fixed) -->
                            <polygon points="250,70 190,230 330,230" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3" stroke-dasharray="4,3"/>
                            <text x="250" y="55" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">A</text>
                            <text x="175" y="245" fill="#a5b4fc" font-size="12" font-weight="bold">B</text>
                            <text x="340" y="245" fill="#a5b4fc" font-size="12" font-weight="bold">C</text>

                            <!-- Movable Triangle △DEF -->
                            <g id="sim2_movable_group">
                                <polygon points="250,70 190,230 330,230" fill="rgba(245, 158, 11, 0.35)" stroke="#f59e0b" stroke-width="3"/>
                                <text x="250" y="55" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">D</text>
                                <text x="175" y="245" fill="#fde68a" font-size="12" font-weight="bold">E</text>
                                <text x="340" y="245" fill="#fde68a" font-size="12" font-weight="bold">F</text>
                            </g>
                        </svg>
                    </div>

                    <div id="sim2_badge" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        Adjust Translation and Rotation until △DEF coincides completely with △ABC.
                    </div>
                </div>
            `;

            const txSlider = document.getElementById('sim2_tx');
            const tySlider = document.getElementById('sim2_ty');
            const rotSlider = document.getElementById('sim2_rot');
            const snapBtn = document.getElementById('sim2_snap');
            const movableGroup = document.getElementById('sim2_movable_group');
            const badge = document.getElementById('sim2_badge');

            function update() {
                const tx = parseFloat(txSlider.value);
                const ty = parseFloat(tySlider.value);
                const rot = parseFloat(rotSlider.value);

                // Pivot is centroid (256, 176)
                movableGroup.setAttribute('transform', `translate(${tx}, ${ty}) rotate(${rot}, 256, 176)`);

                const dist = Math.hypot(tx, ty);
                const angDiff = Math.abs(rot % 360);

                if (dist < 5 && (angDiff < 5 || angDiff > 355)) {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-bold bg-emerald-950/60 border border-emerald-500 text-emerald-300';
                    badge.innerHTML = `✓ PERFECT SUPERPOSITION! Both triangles coincide completely: △ABC ≅ △DEF (Same Shape & Same Size!)`;
                } else {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-amber-950/40 border border-amber-500/30 text-amber-300';
                    badge.innerHTML = `Distance Offset: ${dist.toFixed(1)} px | Rotation Offset: ${angDiff.toFixed(0)}° (Keep adjusting!)`;
                }
            }

            txSlider.addEventListener('input', update);
            tySlider.addEventListener('input', update);
            rotSlider.addEventListener('input', update);

            snapBtn.addEventListener('click', () => {
                txSlider.value = 0;
                tySlider.value = 0;
                rotSlider.value = 0;
                update();
            });

            update();
        }

        // Sim 3: Vertex Correspondence & CPCTC Mapper
        function renderSim3(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Select Correspondence Mapping:</span>
                        <select id="sim3_select" class="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2 py-1 text-xs font-bold">
                            <option value="correct">A↔D, B↔E, C↔F (Correct: △ABC ≅ △DEF)</option>
                            <option value="scrambled">A↔E, B↔D, C↔F (Incorrect: △ABC ≅ △EDF)</option>
                        </select>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Triangle ABC -->
                            <g id="sim3_tri1"></g>
                            <!-- Triangle DEF -->
                            <g id="sim3_tri2"></g>
                        </svg>
                    </div>

                    <div id="sim3_matrix" class="grid grid-cols-2 gap-2 text-xs font-mono bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const select = document.getElementById('sim3_select');
            const tri1 = document.getElementById('sim3_tri1');
            const tri2 = document.getElementById('sim3_tri2');
            const matrix = document.getElementById('sim3_matrix');

            function update() {
                const isCorrect = (select.value === 'correct');

                tri1.innerHTML = `
                    <polygon points="150,50 70,220 230,220" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                    <circle cx="150" cy="50" r="7" fill="#6366f1"/>
                    <circle cx="70" cy="220" r="7" fill="#10b981"/>
                    <circle cx="230" cy="220" r="7" fill="#f59e0b"/>
                    <text x="150" y="35" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">A</text>
                    <text x="50" y="235" fill="#6ee7b7" font-size="13" font-weight="bold">B</text>
                    <text x="245" y="235" fill="#fde68a" font-size="13" font-weight="bold">C</text>
                    <text x="150" y="150" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">△ABC</text>
                `;

                const dColor = isCorrect ? "#6366f1" : "#10b981";
                const eColor = isCorrect ? "#10b981" : "#6366f1";
                const dLabel = isCorrect ? "D" : "E";
                const eLabel = isCorrect ? "E" : "D";

                tri2.innerHTML = `
                    <polygon points="450,50 370,220 530,220" fill="rgba(16, 185, 129, 0.2)" stroke="${isCorrect ? '#10b981' : '#f43f5e'}" stroke-width="3"/>
                    <circle cx="450" cy="50" r="7" fill="${dColor}"/>
                    <circle cx="370" cy="220" r="7" fill="${eColor}"/>
                    <circle cx="530" cy="220" r="7" fill="#f59e0b"/>
                    <text x="450" y="35" fill="#e2e8f0" font-size="13" font-weight="bold" text-anchor="middle">${dLabel}</text>
                    <text x="350" y="235" fill="#e2e8f0" font-size="13" font-weight="bold">${eLabel}</text>
                    <text x="545" y="235" fill="#fde68a" font-size="13" font-weight="bold">F</text>
                    <text x="450" y="150" fill="${isCorrect ? '#6ee7b7' : '#fda4af'}" font-size="12" font-weight="bold" text-anchor="middle">
                        ${isCorrect ? '△DEF (Congruent)' : '△EDF (Mismatch!)'}
                    </text>
                `;

                if (isCorrect) {
                    matrix.innerHTML = `
                        <div>
                            <span class="text-indigo-400 font-bold">Corresponding Sides:</span><br>
                            • AB = DE<br>• BC = EF<br>• CA = FD
                        </div>
                        <div>
                            <span class="text-emerald-400 font-bold">Corresponding Angles (CPCTC):</span><br>
                            • ∠A = ∠D<br>• ∠B = ∠E<br>• ∠C = ∠F
                        </div>
                    `;
                } else {
                    matrix.innerHTML = `
                        <div class="col-span-2 text-rose-300">
                            ⚠ FAILS CPCTC! Writing △ABC ≅ △EDF incorrectly claims side AB = ED and ∠A = ∠E, which violates actual geometric correspondence!
                        </div>
                    `;
                }
            }

            select.addEventListener('change', update);
            update();
        }

        // Sim 4: SAS Constructor & Superposition
        function renderSim4(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-3 gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Side c (AB): <span id="sim4_c_val" class="text-indigo-400 font-bold">120</span></label>
                            <input type="range" id="sim4_c" min="70" max="160" value="120" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Included ∠A: <span id="sim4_A_val" class="text-indigo-400 font-bold">55°</span></label>
                            <input type="range" id="sim4_A" min="30" max="110" value="55" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Side b (AC): <span id="sim4_b_val" class="text-indigo-400 font-bold">140</span></label>
                            <input type="range" id="sim4_b" min="80" max="170" value="140" class="w-full accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim4_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim4_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const cSlider = document.getElementById('sim4_c');
            const ASlider = document.getElementById('sim4_A');
            const bSlider = document.getElementById('sim4_b');
            const cVal = document.getElementById('sim4_c_val');
            const AVal = document.getElementById('sim4_A_val');
            const bVal = document.getElementById('sim4_b_val');
            const svg = document.getElementById('sim4_svg');
            const readout = document.getElementById('sim4_readout');

            function update() {
                const c = parseFloat(cSlider.value);
                const angA = parseFloat(ASlider.value);
                const b = parseFloat(bSlider.value);
                cVal.textContent = c;
                AVal.textContent = `${angA}°`;
                bVal.textContent = b;

                const rad = (angA * Math.PI) / 180;
                const Ax = 180, Ay = 220;
                const Bx = Ax + c, By = Ay;
                const Cx = Ax + b * Math.cos(rad);
                const Cy = Ay - b * Math.sin(rad);

                const thirdSide_a = Math.hypot(Cx - Bx, Cy - By);

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Angle Arc at A -->
                    <path d="M${Ax + 30},${Ay} A30,30 0 0,0 ${Ax + 30 * Math.cos(rad)},${Ay - 30 * Math.sin(rad)}" fill="none" stroke="#f59e0b" stroke-width="3"/>
                    <text x="${Ax + 45}" y="${Ay - 12}" fill="#fbbf24" font-size="11" font-weight="bold">${angA}°</text>

                    <!-- Side Labels -->
                    <text x="${(Ax+Bx)/2}" y="${Ay + 20}" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">c = ${c}</text>
                    <text x="${(Ax+Cx)/2 - 20}" y="${(Ay+Cy)/2}" fill="#38bdf8" font-size="12" font-weight="bold">b = ${b}</text>
                    <text x="${(Bx+Cx)/2 + 20}" y="${(By+Cy)/2}" fill="#10b981" font-size="12" font-weight="bold">Locked a = ${thirdSide_a.toFixed(1)}</text>

                    <!-- Vertices -->
                    <circle cx="${Ax}" cy="${Ay}" r="6" fill="#f59e0b"/>
                    <circle cx="${Bx}" cy="${By}" r="6" fill="#6366f1"/>
                    <circle cx="${Cx}" cy="${Cy}" r="6" fill="#6366f1"/>
                    <text x="${Ax-15}" y="${Ay+15}" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                    <text x="${Bx+10}" y="${By+15}" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx}" y="${Cy-10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">C</text>
                `;

                readout.innerHTML = `
                    <span class="text-emerald-400 font-bold">SAS Principle:</span> Once Side b (${b}), Side c (${c}), and Included ∠A (${angA}°) are fixed, the third side a (${thirdSide_a.toFixed(1)}) and other angles are 100% locked!
                `;
            }

            cSlider.addEventListener('input', update);
            ASlider.addEventListener('input', update);
            bSlider.addEventListener('input', update);
            update();
        }

        // Sim 5: ASA 3-Case Deductive Proof Visualizer
        function renderSim5(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 7.1 Deductive Cases:</span>
                        <div class="flex gap-2">
                            <button id="sim5_case1" class="px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold text-xs transition">Case 1: AB = DE</button>
                            <button id="sim5_case2" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition">Case 2: AB > DE</button>
                            <button id="sim5_case3" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition">Case 3: AB < DE</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim5_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim5_desc" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let currentCase = 1;
            const btn1 = document.getElementById('sim5_case1');
            const btn2 = document.getElementById('sim5_case2');
            const btn3 = document.getElementById('sim5_case3');
            const svg = document.getElementById('sim5_svg');
            const desc = document.getElementById('sim5_desc');

            function setCase(c) {
                currentCase = c;
                [btn1, btn2, btn3].forEach((b, i) => {
                    if (i + 1 === c) {
                        b.className = 'px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold text-xs transition';
                    } else {
                        b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition';
                    }
                });

                if (c === 1) {
                    svg.innerHTML = `
                        <!-- △ABC -->
                        <polygon points="120,60 60,220 220,220" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                        <text x="120" y="45" fill="#a5b4fc" font-size="12" font-weight="bold">A</text>
                        <text x="45" y="235" fill="#a5b4fc" font-size="12" font-weight="bold">B</text>
                        <text x="230" y="235" fill="#a5b4fc" font-size="12" font-weight="bold">C</text>

                        <!-- △DEF -->
                        <polygon points="440,60 380,220 540,220" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                        <text x="440" y="45" fill="#6ee7b7" font-size="12" font-weight="bold">D</text>
                        <text x="365" y="235" fill="#6ee7b7" font-size="12" font-weight="bold">E</text>
                        <text x="550" y="235" fill="#6ee7b7" font-size="12" font-weight="bold">F</text>

                        <text x="300" y="150" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">△ABC ≅ △DEF by SAS Axiom!</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    desc.textContent = "Case 1: If AB = DE, then △ABC ≅ △DEF directly by SAS (AB=DE, ∠B=∠E, BC=EF).";
                } else if (c === 2) {
                    svg.innerHTML = `
                        <!-- △ABC with point P -->
                        <polygon points="120,40 60,220 220,220" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Sub-triangle PBC -->
                        <polygon points="90,130 60,220 220,220" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="3"/>
                        <line x1="90" y1="130" x2="220" y2="220" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>

                        <circle cx="90" cy="130" r="5" fill="#f43f5e"/>
                        <text x="70" y="135" fill="#f43f5e" font-size="12" font-weight="bold">P</text>
                        <text x="120" y="30" fill="#a5b4fc" font-size="12" font-weight="bold">A</text>
                        <text x="45" y="235" fill="#a5b4fc" font-size="12" font-weight="bold">B</text>
                        <text x="230" y="235" fill="#a5b4fc" font-size="12" font-weight="bold">C</text>

                        <!-- △DEF -->
                        <polygon points="440,110 380,220 540,220" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                        <text x="440" y="95" fill="#6ee7b7" font-size="12" font-weight="bold">D</text>
                        <text x="365" y="235" fill="#6ee7b7" font-size="12" font-weight="bold">E</text>
                        <text x="550" y="235" fill="#6ee7b7" font-size="12" font-weight="bold">F</text>

                        <text x="300" y="170" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">Contradiction: ∠PCB = ∠ACB!</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    desc.textContent = "Case 2 (Contradiction): If AB > DE, choosing PB = DE forces ∠PCB = ∠F = ∠ACB. A part cannot equal the whole! Hence AB cannot be greater than DE.";
                } else {
                    svg.innerHTML = `
                        <!-- △ABC -->
                        <polygon points="120,110 60,220 220,220" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                        <!-- △DEF with point M -->
                        <polygon points="440,40 380,220 540,220" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2"/>
                        <polygon points="410,130 380,220 540,220" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="3"/>
                        <text x="440" y="30" fill="#6ee7b7" font-size="12" font-weight="bold">D</text>
                        <text x="390" y="135" fill="#f43f5e" font-size="12" font-weight="bold">M</text>
                        <text x="300" y="170" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">Symmetric Contradiction!</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    desc.textContent = "Case 3 (Contradiction): Symmetrically, AB < DE forces ∠MEF = ∠DEF, another impossible contradiction. Therefore, AB MUST equal DE!";
                }
            }

            btn1.addEventListener('click', () => setCase(1));
            btn2.addEventListener('click', () => setCase(2));
            btn3.addEventListener('click', () => setCase(3));
            setCase(1);
        }

        // Sim 6: AAS to ASA Converter
        function renderSim6(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 gap-3 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Angle ∠A: <span id="sim6_A_val" class="text-indigo-400 font-bold">50°</span></label>
                            <input type="range" id="sim6_A" min="30" max="85" value="50" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Angle ∠B: <span id="sim6_B_val" class="text-indigo-400 font-bold">65°</span></label>
                            <input type="range" id="sim6_B" min="30" max="85" value="65" class="w-full accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim6_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim6_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const ASlider = document.getElementById('sim6_A');
            const BSlider = document.getElementById('sim6_B');
            const AVal = document.getElementById('sim6_A_val');
            const BVal = document.getElementById('sim6_B_val');
            const svg = document.getElementById('sim6_svg');
            const readout = document.getElementById('sim6_readout');

            function update() {
                const angA = parseFloat(ASlider.value);
                const angB = parseFloat(BSlider.value);
                const angC = 180 - (angA + angB);
                AVal.textContent = `${angA}°`;
                BVal.textContent = `${angB}°`;

                // Geometry
                const Bx = 150, By = 220;
                const Cx = 450, Cy = 220;
                const L = 300;
                const radB = (angB * Math.PI) / 180;
                const radC = (angC * Math.PI) / 180;

                // Ax, Ay from ray intersection
                const tanB = Math.tan(radB);
                const tanC = Math.tan(radC);
                const Ax = (Bx * tanB + Cx * tanC) / (tanB + tanC);
                const Ay = By - (tanB * tanC * (Cx - Bx)) / (tanB + tanC);

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Base BC (Non-included side for A & B) -->
                    <line x1="${Bx}" y1="${By}" x2="${Cx}" y2="${Cy}" stroke="#10b981" stroke-width="5"/>
                    <text x="300" y="${By + 20}" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Non-included Side BC = 10 cm</text>

                    <!-- Vertices -->
                    <circle cx="${Ax}" cy="${Ay}" r="6" fill="#f59e0b"/>
                    <circle cx="${Bx}" cy="${By}" r="6" fill="#38bdf8"/>
                    <circle cx="${Cx}" cy="${Cy}" r="6" fill="#10b981"/>

                    <text x="${Ax}" y="${Ay - 10}" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">A (${angA}°)</text>
                    <text x="${Bx - 20}" y="${By + 15}" fill="#38bdf8" font-size="12" font-weight="bold">B (${angB}°)</text>
                    <text x="${Cx + 15}" y="${Cy + 15}" fill="#34d399" font-size="12" font-weight="bold">C (${angC}°)</text>
                `;

                readout.innerHTML = `
                    Angle Sum Theorem: ∠C = 180° - (${angA}° + ${angB}°) = <b>${angC}°</b>.<br>
                    Side BC is now the INCLUDED side between ∠B and newly derived ∠C, instantly turning AAS into ASA!
                `;
            }

            ASlider.addEventListener('input', update);
            BSlider.addEventListener('input', update);
            update();
        }

        // Sim 7: SSS Compass Arc Intersection & Rigidity Lab
        function renderSim7(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 gap-3 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Radius from B (c = AB): <span id="sim7_c_val" class="text-indigo-400 font-bold">140</span></label>
                            <input type="range" id="sim7_c" min="80" max="220" value="140" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Radius from C (b = AC): <span id="sim7_b_val" class="text-indigo-400 font-bold">150</span></label>
                            <input type="range" id="sim7_b" min="80" max="220" value="150" class="w-full accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim7_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim7_readout" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const cSlider = document.getElementById('sim7_c');
            const bSlider = document.getElementById('sim7_b');
            const cVal = document.getElementById('sim7_c_val');
            const bVal = document.getElementById('sim7_b_val');
            const svg = document.getElementById('sim7_svg');
            const readout = document.getElementById('sim7_readout');

            function update() {
                const c = parseFloat(cSlider.value);
                const b = parseFloat(bSlider.value);
                cVal.textContent = c;
                bVal.textContent = b;

                const Bx = 180, By = 210;
                const Cx = 420, Cy = 210;
                const a = Cx - Bx; // 240

                let svgHtml = `
                    <!-- Base BC -->
                    <line x1="${Bx}" y1="${By}" x2="${Cx}" y2="${Cy}" stroke="#64748b" stroke-width="6"/>
                    <circle cx="${Bx}" cy="${By}" r="6" fill="#38bdf8"/>
                    <circle cx="${Cx}" cy="${Cy}" r="6" fill="#10b981"/>
                    <text x="${Bx-15}" y="${By+15}" fill="#38bdf8" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx+15}" y="${By+15}" fill="#10b981" font-size="12" font-weight="bold">C</text>
                    <text x="300" y="${By+20}" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Base a = 240</text>

                    <!-- Compass Arcs -->
                    <circle cx="${Bx}" cy="${By}" r="${c}" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                    <circle cx="${Cx}" cy="${Cy}" r="${b}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
                `;

                if (b + c <= a) {
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    readout.textContent = `⚠ Triangle Inequality Violated! b + c (${b + c}) ≤ a (${a}). Arcs do not intersect; no triangle can form.`;
                } else if (Math.abs(b - c) >= a) {
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    readout.textContent = `⚠ One circle lies completely inside the other; no intersection exists!`;
                } else {
                    // Unique intersection in upper half plane
                    const d = a;
                    const x = (d*d - b*b + c*c) / (2*d);
                    const y = Math.sqrt(Math.max(0, c*c - x*x));
                    const Ax = Bx + x;
                    const Ay = By - y;

                    svgHtml += `
                        <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="3"/>
                        <circle cx="${Ax}" cy="${Ay}" r="7" fill="#f59e0b"/>
                        <text x="${Ax}" y="${Ay-10}" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">A (Unique Intersection)</text>
                    `;
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.innerHTML = `✓ Two circles intersect at exactly ONE point in the upper half-plane. Hence 3 sides lock a UNIQUE triangle (SSS)!`;
                }
            }

            cSlider.addEventListener('input', update);
            bSlider.addEventListener('input', update);
            update();
        }

        // Sim 8: RHS Pythagorean Lock & Back-to-Back Isosceles Visualizer
        function renderSim8(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Hypotenuse h: <span id="sim8_h_val" class="text-indigo-400 font-bold">170</span></label>
                            <input type="range" id="sim8_h" min="130" max="220" value="170" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Common Leg b: <span id="sim8_b_val" class="text-indigo-400 font-bold">80</span></label>
                            <input type="range" id="sim8_b" min="50" max="110" value="80" class="w-full accent-indigo-500">
                        </div>
                        <div class="flex items-end">
                            <button id="sim8_reflect" class="w-full py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition">
                                Reflect & Join Back-to-Back
                            </button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim8_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim8_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let isReflected = false;
            const hSlider = document.getElementById('sim8_h');
            const bSlider = document.getElementById('sim8_b');
            const hVal = document.getElementById('sim8_h_val');
            const bVal = document.getElementById('sim8_b_val');
            const reflectBtn = document.getElementById('sim8_reflect');
            const svg = document.getElementById('sim8_svg');
            const readout = document.getElementById('sim8_readout');

            function update() {
                const h = parseFloat(hSlider.value);
                const b = parseFloat(bSlider.value);
                hVal.textContent = h;
                bVal.textContent = b;

                // a = sqrt(h^2 - b^2)
                const a = Math.sqrt(Math.max(0, h*h - b*b));

                const midX = 300, midY = 220;
                const topY = midY - a;

                let svgHtml = `
                    <!-- Right Triangle 1 (Left) -->
                    <polygon points="${midX},${topY} ${midX - b},${midY} ${midX},${midY}" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="3"/>
                    <rect x="${midX - 15}" y="${midY - 15}" width="15" height="15" fill="none" stroke="#f59e0b" stroke-width="2"/>
                    <text x="${midX - b/2 - 20}" y="${(midY+topY)/2}" fill="#38bdf8" font-size="11" font-weight="bold">h = ${h}</text>
                    <text x="${midX - b/2}" y="${midY + 18}" fill="#94a3b8" font-size="11" font-weight="bold">b = ${b}</text>
                    <line x1="${midX}" y1="${topY}" x2="${midX}" y2="${midY}" stroke="#10b981" stroke-width="4"/>
                    <text x="${midX + 8}" y="${(midY+topY)/2}" fill="#10b981" font-size="11" font-weight="bold">a = ${a.toFixed(1)}</text>
                `;

                if (isReflected) {
                    svgHtml += `
                        <!-- Reflected Right Triangle 2 (Right) -->
                        <polygon points="${midX},${topY} ${midX + b},${midY} ${midX},${midY}" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>
                        <rect x="${midX}" y="${midY - 15}" width="15" height="15" fill="none" stroke="#f59e0b" stroke-width="2"/>
                        <text x="${midX + b/2 + 10}" y="${(midY+topY)/2}" fill="#34d399" font-size="11" font-weight="bold">h = ${h}</text>
                        <text x="${midX + b/2}" y="${midY + 18}" fill="#94a3b8" font-size="11" font-weight="bold">b = ${b}</text>
                        <text x="300" y="35" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">Large Isosceles Triangle Formed!</text>
                    `;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.innerHTML = `✓ Back-to-Back Isosceles Proof: Legs both equal h (${h}), so base angles are equal. Hence triangles are congruent by AAS/SSS!`;
                    reflectBtn.textContent = 'Separate Triangles';
                } else {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300';
                    readout.innerHTML = `Pythagoras Lock: a = √(h² - b²) = √(${h}² - ${b}²) = <b>${a.toFixed(1)}</b>. Third side is locked, reducing RHS to SSS!`;
                    reflectBtn.textContent = 'Reflect & Join Back-to-Back';
                }

                svg.innerHTML = svgHtml;
            }

            hSlider.addEventListener('input', update);
            bSlider.addEventListener('input', update);
            reflectBtn.addEventListener('click', () => {
                isReflected = !isReflected;
                update();
            });
            update();
        }

        // Sim 9: Pons Asinorum / Isosceles Triangle Folding Proof
        function renderSim9(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Vertex Angle ∠A:</label>
                            <input type="range" id="sim9_A" min="30" max="100" value="48" class="w-32 accent-indigo-500">
                            <span id="sim9_A_val" class="font-bold text-indigo-400">48°</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Fold Bisector AD:</label>
                            <input type="range" id="sim9_fold" min="0" max="100" value="0" class="w-32 accent-emerald-500">
                            <span id="sim9_fold_val" class="font-bold text-emerald-400">0%</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim9_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim9_readout" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const ASlider = document.getElementById('sim9_A');
            const foldSlider = document.getElementById('sim9_fold');
            const AVal = document.getElementById('sim9_A_val');
            const foldVal = document.getElementById('sim9_fold_val');
            const svg = document.getElementById('sim9_svg');
            const readout = document.getElementById('sim9_readout');

            function update() {
                const angA = parseFloat(ASlider.value);
                const fold = parseFloat(foldSlider.value) / 100;
                AVal.textContent = `${angA}°`;
                foldVal.textContent = `${Math.round(fold * 100)}%`;

                const baseAng = (180 - angA) / 2;
                const Ax = 300, Ay = 50;
                const L = 180;
                const halfRad = ((angA / 2) * Math.PI) / 180;

                const originalBx = Ax - L * Math.sin(halfRad);
                const originalBy = Ay + L * Math.cos(halfRad);
                const Cx = Ax + L * Math.sin(halfRad);
                const Cy = Ay + L * Math.cos(halfRad);
                const Dx = Ax, Dy = originalBy;

                // Folding left vertex B toward right vertex C across AD
                const Bx = originalBx + (Cx - originalBx) * fold;
                const By = originalBy;

                svg.innerHTML = `
                    <!-- Right Half △ACD (Fixed) -->
                    <polygon points="${Ax},${Ay} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                    <!-- Left Half △ABD (Folds) -->
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Dx},${Dy}" fill="rgba(99, 102, 241, 0.35)" stroke="#6366f1" stroke-width="3"/>

                    <!-- Angle Bisector AD -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Dx}" y2="${Dy}" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>

                    <!-- Vertices -->
                    <circle cx="${Ax}" cy="${Ay}" r="6" fill="#f59e0b"/>
                    <circle cx="${Bx}" cy="${By}" r="6" fill="#6366f1"/>
                    <circle cx="${Cx}" cy="${Cy}" r="6" fill="#10b981"/>
                    <circle cx="${Dx}" cy="${Dy}" r="5" fill="#94a3b8"/>

                    <text x="${Ax}" y="${Ay - 10}" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">A</text>
                    <text x="${Bx - 15}" y="${By + 15}" fill="#a5b4fc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx + 15}" y="${Cy + 15}" fill="#6ee7b7" font-size="12" font-weight="bold">C</text>
                    <text x="${Dx}" y="${Dy + 18}" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">D</text>

                    <!-- Angle markers -->
                    <text x="${Ax - 25}" y="${Ay + 35}" fill="#a5b4fc" font-size="10">${(angA/2).toFixed(1)}°</text>
                    <text x="${Ax + 10}" y="${Ay + 35}" fill="#6ee7b7" font-size="10">${(angA/2).toFixed(1)}°</text>
                `;

                if (fold > 0.95) {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.innerHTML = `✓ COMPLETE SUPERPOSITION! △ABD ≅ △ACD by SAS. Therefore base angles ∠B and ∠C match identically: <b>∠B = ∠C = ${baseAng.toFixed(1)}°</b>!`;
                } else {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300';
                    readout.innerHTML = `Theorem 7.2 (Pons Asinorum): In △ABC, AB = AC. Angle bisector AD divides the triangle into two congruent halves. Base angles: <b>${baseAng.toFixed(1)}°</b>.`;
                }
            }

            ASlider.addEventListener('input', update);
            foldSlider.addEventListener('input', update);
            update();
        }

        // Sim 10: Proposition Builder & Truth Value Tester
        function renderSim10(container) {
            const presets = [
                {
                    title: "Equilateral ⇒ Isosceles",
                    p: "A triangle is equilateral",
                    q: "The triangle is isosceles",
                    isTrue: true,
                    note: "TRUE: Every triangle with 3 equal sides has at least 2 equal sides (P ⊆ Q)."
                },
                {
                    title: "Right Angles ⇒ Square",
                    p: "A quadrilateral has 4 right angles",
                    q: "The quadrilateral is a square",
                    isTrue: false,
                    note: "FALSE: A non-square rectangle satisfies P but not Q (Counterexample)."
                },
                {
                    title: "Equal Sides ⇒ Congruent",
                    p: "Two triangles have 3 pairs of equal sides",
                    q: "The two triangles are congruent",
                    isTrue: true,
                    note: "TRUE: By the SSS Congruence Theorem 7.4 (P ⊆ Q)."
                }
            ];

            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Select Geometric Proposition:</span>
                        <select id="sim10_select" class="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2 py-1 text-xs font-bold">
                            ${presets.map((p, i) => `<option value="${i}">${p.title}</option>`).join('')}
                        </select>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim10_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Euler Diagrams -->
                        </svg>
                    </div>

                    <div id="sim10_desc" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const select = document.getElementById('sim10_select');
            const svg = document.getElementById('sim10_svg');
            const desc = document.getElementById('sim10_desc');

            function update() {
                const item = presets[parseInt(select.value)];
                if (item.isTrue) {
                    svg.innerHTML = `
                        <!-- Outer Set Q (Conclusion) -->
                        <ellipse cx="300" cy="140" rx="200" ry="110" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                        <text x="300" y="55" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">Conclusion Set Q: "${item.q}"</text>

                        <!-- Inner Set P (Hypothesis) -->
                        <ellipse cx="300" cy="155" rx="100" ry="65" fill="rgba(16, 185, 129, 0.35)" stroke="#10b981" stroke-width="3"/>
                        <text x="300" y="155" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Hypothesis P: "${item.p}"</text>

                        <text x="300" y="270" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">P ⊆ Q (P is a subset of Q ⇒ P IMPLIES Q IS VALID)</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                } else {
                    svg.innerHTML = `
                        <!-- Set P -->
                        <ellipse cx="230" cy="140" rx="130" ry="85" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="3"/>
                        <text x="170" y="140" fill="#fda4af" font-size="12" font-weight="bold" text-anchor="middle">P: "${item.p}"</text>

                        <!-- Set Q -->
                        <ellipse cx="370" cy="140" rx="130" ry="85" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                        <text x="430" y="140" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Q: "${item.q}"</text>

                        <!-- Counterexample in P - Q -->
                        <circle cx="160" cy="170" r="6" fill="#f43f5e"/>
                        <text x="160" y="195" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Counterexample!</text>

                        <text x="300" y="270" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">P ⊄ Q (Counterexamples exist ⇒ Proposition FAILS)</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                }
                desc.textContent = item.note;
            }

            select.addEventListener('change', update);
            update();
        }

        // Sim 11: Converse Swapper Machine
        function renderSim11(container) {
            const pairs = [
                {
                    name: "Isosceles Sides vs Angles",
                    p: "AB = AC in △ABC",
                    q: "∠B = ∠C in △ABC",
                    pTrue: true,
                    qTrue: true,
                    isBiconditional: true,
                    note: "Biconditional: Theorems 7.2 and 7.3 form a true converse pair (AB = AC ⇔ ∠B = ∠C)."
                },
                {
                    name: "Linear Pair vs 180° Sum",
                    p: "Two adjacent angles form a linear pair",
                    q: "The sum of the two angles is 180°",
                    pTrue: true,
                    qTrue: true,
                    isBiconditional: true,
                    note: "Biconditional: Axiom 6.1 and Axiom 6.2 form a true converse pair."
                },
                {
                    name: "Square vs Right Angles",
                    p: "Quadrilateral ABCD is a square",
                    q: "Quadrilateral ABCD has 4 right angles",
                    pTrue: true,
                    qTrue: false,
                    isBiconditional: false,
                    note: "One-Way: All squares have 4 right angles, but non-square rectangles prove the converse is FALSE!"
                }
            ];

            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <select id="sim11_select" class="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2 py-1 text-xs font-bold">
                            ${pairs.map((p, i) => `<option value="${i}">${p.name}</option>`).join('')}
                        </select>
                        <button id="sim11_swap" class="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1 transition">
                            <i data-lucide="repeat" class="w-3.5 h-3.5"></i> Swap to Converse
                        </button>
                    </div>

                    <div class="flex-1 min-h-[260px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-4 flex flex-col items-center justify-center gap-4">
                        <div id="sim11_mode" class="text-xs font-bold text-indigo-400 uppercase tracking-widest">Original Conditional: P ⇒ Q</div>

                        <div class="flex items-center gap-3 w-full max-w-lg">
                            <div id="sim11_card_left" class="flex-1 p-4 rounded-xl bg-slate-900 border border-indigo-500/40 text-center font-bold text-sm text-indigo-200 shadow-lg">
                                Hypothesis P
                            </div>
                            <div class="text-2xl text-indigo-400 font-bold">➔</div>
                            <div id="sim11_card_right" class="flex-1 p-4 rounded-xl bg-slate-900 border border-emerald-500/40 text-center font-bold text-sm text-emerald-200 shadow-lg">
                                Conclusion Q
                            </div>
                        </div>

                        <div id="sim11_badge" class="px-4 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                            Status: Valid Implication
                        </div>
                    </div>

                    <div id="sim11_note" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let isConverse = false;
            const select = document.getElementById('sim11_select');
            const swapBtn = document.getElementById('sim11_swap');
            const mode = document.getElementById('sim11_mode');
            const leftCard = document.getElementById('sim11_card_left');
            const rightCard = document.getElementById('sim11_card_right');
            const badge = document.getElementById('sim11_badge');
            const note = document.getElementById('sim11_note');

            function update() {
                const item = pairs[parseInt(select.value)];
                if (!isConverse) {
                    mode.textContent = "Original Conditional Statement: (If P, then Q)";
                    leftCard.innerHTML = `<span class="text-[10px] text-slate-400 block mb-1">HYPOTHESIS P</span>${item.p}`;
                    rightCard.innerHTML = `<span class="text-[10px] text-slate-400 block mb-1">CONCLUSION Q</span>${item.q}`;
                    badge.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
                    badge.textContent = "✓ Original Statement is TRUE";
                } else {
                    mode.textContent = "Converse Statement: (If Q, then P)";
                    leftCard.innerHTML = `<span class="text-[10px] text-slate-400 block mb-1">HYPOTHESIS Q</span>${item.q}`;
                    rightCard.innerHTML = `<span class="text-[10px] text-slate-400 block mb-1">CONCLUSION P</span>${item.p}`;
                    if (item.qTrue) {
                        badge.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
                        badge.textContent = "✓ Converse is ALSO TRUE (Biconditional P ⇔ Q)";
                    } else {
                        badge.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30";
                        badge.textContent = "✗ Converse is FALSE! Counterexamples exist";
                    }
                }
                note.textContent = item.note;
                lucide.createIcons();
            }

            select.addEventListener('change', () => {
                isConverse = false;
                update();
            });
            swapBtn.addEventListener('click', () => {
                isConverse = !isConverse;
                update();
            });
            update();
        }

        // Sim 12: Counterexample Generator & Refuter
        function renderSim12(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Equal Area ≠ Congruence (Counterexample Generator):</span>
                        <span class="text-indigo-400 font-mono font-bold">Target Area = 24 cm²</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Triangle 1: Base 8, Height 6 (Area = 24) -->
                            <polygon points="120,70 50,210 210,210" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                            <line x1="120" y1="70" x2="120" y2="210" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                            <text x="130" y="140" fill="#fbbf24" font-size="11">h = 6</text>
                            <text x="130" y="230" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Base = 8</text>
                            <text x="130" y="180" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Area = 24 cm²</text>
                            <text x="130" y="35" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">△₁ (Sides: 7.6, 6.7, 8)</text>

                            <!-- Triangle 2: Base 12, Height 4 (Area = 24) -->
                            <polygon points="450,110 330,210 570,210" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="3"/>
                            <line x1="450" y1="110" x2="450" y2="210" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                            <text x="460" y="160" fill="#fbbf24" font-size="11">h = 4</text>
                            <text x="450" y="230" fill="#fda4af" font-size="12" font-weight="bold" text-anchor="middle">Base = 12</text>
                            <text x="450" y="180" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Area = 24 cm²</text>
                            <text x="450" y="35" fill="#fda4af" font-size="12" font-weight="bold" text-anchor="middle">△₂ (Sides: 12.6, 4.5, 12)</text>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300">
                        DECISIVE COUNTEREXAMPLE: Both triangles have identical area (24 cm²), but completely unequal side lengths! Thus, the converse ("Equal Area ⇒ Congruence") is completely FALSE!
                    </div>
                </div>
            `;
        }

        // Sim 13: The SSA Swinging Pendulum Simulator (The Ambiguous Case)
        function renderSim13(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Adjacent Side b: <span id="sim13_b_val" class="text-indigo-400 font-bold">180</span></label>
                            <input type="range" id="sim13_b" min="140" max="220" value="180" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Swinging Side a: <span id="sim13_a_val" class="text-indigo-400 font-bold">120</span></label>
                            <input type="range" id="sim13_a" min="70" max="210" value="120" class="w-full accent-indigo-500">
                        </div>
                        <div class="flex items-end">
                            <button id="sim13_toggle_tri" class="w-full py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition">
                                Toggle Acute / Obtuse
                            </button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim13_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim13_readout" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let showObtuse = false;
            const bSlider = document.getElementById('sim13_b');
            const aSlider = document.getElementById('sim13_a');
            const bVal = document.getElementById('sim13_b_val');
            const aVal = document.getElementById('sim13_a_val');
            const toggleBtn = document.getElementById('sim13_toggle_tri');
            const svg = document.getElementById('sim13_svg');
            const readout = document.getElementById('sim13_readout');

            function update() {
                const b = parseFloat(bSlider.value);
                const a = parseFloat(aSlider.value);
                bVal.textContent = b;
                aVal.textContent = a;

                const angA = 30; // 30 degrees
                const radA = (angA * Math.PI) / 180;
                const h = b * Math.sin(radA);

                const Ax = 100, Ay = 220;
                const Cx = Ax + b * Math.cos(radA);
                const Cy = Ay - b * Math.sin(radA);

                let svgHtml = `
                    <!-- Ground Base Ray from A -->
                    <line x1="${Ax}" y1="${Ay}" x2="560" y2="${Ay}" stroke="#64748b" stroke-width="4"/>
                    <!-- Side b (AC) -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#38bdf8" stroke-width="4"/>
                    <text x="${(Ax+Cx)/2 - 15}" y="${(Ay+Cy)/2 - 5}" fill="#38bdf8" font-size="12" font-weight="bold">b = ${b}</text>

                    <!-- Altitude h -->
                    <line x1="${Cx}" y1="${Cy}" x2="${Cx}" y2="${Ay}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                    <text x="${Cx + 8}" y="${(Cy+Ay)/2}" fill="#fbbf24" font-size="11">h = ${h.toFixed(1)}</text>

                    <!-- Swinging Circle Arc from C -->
                    <circle cx="${Cx}" cy="${Cy}" r="${a}" fill="none" stroke="rgba(244, 63, 94, 0.4)" stroke-width="2" stroke-dasharray="4,4"/>

                    <circle cx="${Ax}" cy="${Ay}" r="6" fill="#38bdf8"/>
                    <circle cx="${Cx}" cy="${Cy}" r="6" fill="#38bdf8"/>
                    <text x="${Ax-15}" y="${Ay+15}" fill="#f8fafc" font-size="12" font-weight="bold">A (30°)</text>
                    <text x="${Cx}" y="${Cy-10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">C</text>
                `;

                if (a < h) {
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    readout.textContent = `⚠ a (${a}) < Altitude h (${h.toFixed(1)}): Side a cannot reach the ground ray! NO triangle exists.`;
                } else if (Math.abs(a - h) < 1) {
                    svgHtml += `
                        <polygon points="${Ax},${Ay} ${Cx},${Cy} ${Cx},${Ay}" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>
                    `;
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.textContent = `✓ a = h: Exactly 1 Right Triangle formed (This is the RHS Theorem!).`;
                } else if (a >= b) {
                    const Bx = Cx + Math.sqrt(a*a - h*h);
                    svgHtml += `
                        <polygon points="${Ax},${Ay} ${Cx},${Cy} ${Bx},${Ay}" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>
                        <circle cx="${Bx}" cy="${Ay}" r="6" fill="#10b981"/>
                        <text x="${Bx}" y="${Ay+18}" fill="#6ee7b7" font-size="12" font-weight="bold">B</text>
                    `;
                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.textContent = `✓ a (${a}) ≥ b (${b}): Only 1 intersection on the forward ray (Opposite side is longest). Unique triangle!`;
                } else {
                    // Ambiguous case: 2 intersections B1 and B2
                    const offset = Math.sqrt(a*a - h*h);
                    const B1 = Cx - offset; // Obtuse
                    const B2 = Cx + offset; // Acute

                    if (showObtuse) {
                        svgHtml += `
                            <polygon points="${Ax},${Ay} ${Cx},${Cy} ${B1},${Ay}" fill="rgba(244, 63, 94, 0.35)" stroke="#f43f5e" stroke-width="3"/>
                            <circle cx="${B1}" cy="${Ay}" r="6" fill="#f43f5e"/>
                            <text x="${B1 - 10}" y="${Ay+18}" fill="#fda4af" font-size="12" font-weight="bold">B₁ (Obtuse △)</text>
                        `;
                    } else {
                        svgHtml += `
                            <polygon points="${Ax},${Ay} ${Cx},${Cy} ${B2},${Ay}" fill="rgba(99, 102, 241, 0.35)" stroke="#6366f1" stroke-width="3"/>
                            <circle cx="${B2}" cy="${Ay}" r="6" fill="#6366f1"/>
                            <text x="${B2 + 5}" y="${Ay+18}" fill="#a5b4fc" font-size="12" font-weight="bold">B₂ (Acute △)</text>
                        `;
                    }

                    svg.innerHTML = svgHtml;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-amber-950/40 border border-amber-500/40 text-amber-300';
                    readout.innerHTML = `⚠ AMBIGUOUS CASE: h (${h.toFixed(1)}) < a (${a}) < b (${b}). TWO non-congruent triangles exist! (Toggle above to inspect both). SSA fails!`;
                }
            }

            bSlider.addEventListener('input', update);
            aSlider.addEventListener('input', update);
            toggleBtn.addEventListener('click', () => {
                showObtuse = !showObtuse;
                update();
            });
            update();
        }

        // Sim 14: Valid SSA Situations
        function renderSim14(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-2 gap-3 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <label class="text-slate-300 font-semibold block">Angle ∠A: <span id="sim14_A_val" class="text-indigo-400 font-bold">90°</span></label>
                            <input type="range" id="sim14_A" min="30" max="120" value="90" class="w-full accent-indigo-500">
                        </div>
                        <div>
                            <label class="text-slate-300 font-semibold block">Side Ratio a/b: <span id="sim14_ratio_val" class="text-indigo-400 font-bold">1.20</span></label>
                            <input type="range" id="sim14_ratio" min="40" max="160" value="120" class="w-full accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim14_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim14_badge" class="p-2.5 rounded-xl text-center text-xs font-bold bg-emerald-950/40 border border-emerald-500 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const ASlider = document.getElementById('sim14_A');
            const ratioSlider = document.getElementById('sim14_ratio');
            const AVal = document.getElementById('sim14_A_val');
            const ratioVal = document.getElementById('sim14_ratio_val');
            const svg = document.getElementById('sim14_svg');
            const badge = document.getElementById('sim14_badge');

            function update() {
                const angA = parseFloat(ASlider.value);
                const ratio = parseFloat(ratioSlider.value) / 100;
                AVal.textContent = `${angA}°`;
                ratioVal.textContent = ratio.toFixed(2);

                const b = 150;
                const a = b * ratio;
                const rad = (angA * Math.PI) / 180;
                const sinA = Math.sin(rad);

                let status = "";
                let badgeClass = "";

                if (angA === 90 && ratio >= 1.0) {
                    status = "✓ VALID RHS THEOREM: Right angle + Hypotenuse ensures 100% unique triangle!";
                    badgeClass = "bg-emerald-950/60 border-emerald-500 text-emerald-300";
                } else if (angA > 90 && ratio > 1.0) {
                    status = "✓ VALID OBTUSE CASE: Angle > 90° and a > b yields exactly 1 unique triangle!";
                    badgeClass = "bg-emerald-950/60 border-emerald-500 text-emerald-300";
                } else if (ratio >= 1.0) {
                    status = "✓ VALID LONGEST SIDE: a ≥ b ensures only 1 intersection on the forward ray!";
                    badgeClass = "bg-emerald-950/60 border-emerald-500 text-emerald-300";
                } else if (ratio < sinA) {
                    status = "✗ IMPOSSIBLE: a < b·sin(A). The side is too short to reach the base ray!";
                    badgeClass = "bg-rose-950/60 border-rose-500 text-rose-300";
                } else {
                    status = "⚠ AMBIGUOUS CASE: b·sin(A) < a < b. TWO non-congruent triangles possible. SSA FAILS!";
                    badgeClass = "bg-amber-950/60 border-amber-500 text-amber-300";
                }

                badge.className = `p-2.5 rounded-xl text-center text-xs font-bold border ${badgeClass}`;
                badge.textContent = status;

                // Visual Representation
                svg.innerHTML = `
                    <line x1="120" y1="210" x2="520" y2="210" stroke="#64748b" stroke-width="4"/>
                    <line x1="120" y1="210" x2="${120 + b * Math.cos(rad)}" y2="${210 - b * Math.sin(rad)}" stroke="#38bdf8" stroke-width="4"/>
                    <circle cx="120" cy="210" r="6" fill="#38bdf8"/>
                    <text x="100" y="225" fill="#f8fafc" font-size="12" font-weight="bold">A (${angA}°)</text>
                    <text x="300" y="80" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">b = 150, a = ${a.toFixed(1)} (Ratio: ${ratio.toFixed(2)})</text>
                `;
            }

            ASlider.addEventListener('input', update);
            ratioSlider.addEventListener('input', update);
            update();
        }

        // Sim 15: Lewis Carroll's Fallacy
        function renderSim15(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Diagram Deception Inspector:</span>
                        <div class="flex gap-2">
                            <button id="sim15_fake" class="px-3 py-1.5 rounded-lg bg-rose-600 text-white font-bold text-xs transition">
                                Deceptive Sketch (Point Inside)
                            </button>
                            <button id="sim15_real" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition">
                                Accurate Construction (Point Outside)
                            </button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim15_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim15_readout" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let isAccurate = false;
            const fakeBtn = document.getElementById('sim15_fake');
            const realBtn = document.getElementById('sim15_real');
            const svg = document.getElementById('sim15_svg');
            const readout = document.getElementById('sim15_readout');

            function update() {
                if (!isAccurate) {
                    fakeBtn.className = "px-3 py-1.5 rounded-lg bg-rose-600 text-white font-bold text-xs transition";
                    realBtn.className = "px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition";
                    svg.innerHTML = `
                        <!-- Scalene Triangle ABC -->
                        <polygon points="260,50 140,210 460,210" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="3"/>
                        <text x="260" y="35" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                        <text x="125" y="225" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                        <text x="470" y="225" fill="#f8fafc" font-size="12" font-weight="bold">C</text>

                        <!-- False Inside Point O -->
                        <line x1="260" y1="50" x2="290" y2="150" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                        <line x1="300" y1="210" x2="300" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                        <circle cx="295" cy="145" r="6" fill="#f43f5e"/>
                        <text x="315" y="148" fill="#fda4af" font-size="12" font-weight="bold">False Point O (Inside!)</text>

                        <text x="300" y="260" fill="#fda4af" font-size="12" font-weight="bold" text-anchor="middle">
                            Deceptive hand sketch falsely places O inside, erroneously proving AB = AC!
                        </text>
                    `;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    readout.textContent = "LEWIS CARROLL FALLACY: Assuming the intersection point O lies inside the triangle leads to a false proof that all triangles are isosceles!";
                } else {
                    fakeBtn.className = "px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold text-xs transition";
                    realBtn.className = "px-3 py-1.5 rounded-lg bg-emerald-600 text-white font-bold text-xs transition";
                    svg.innerHTML = `
                        <!-- Scalene Triangle ABC -->
                        <polygon points="260,50 140,200 460,200" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="3"/>
                        <!-- Circumcircle -->
                        <circle cx="300" cy="140" r="120" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

                        <!-- Angle Bisector extending OUTSIDE -->
                        <line x1="260" y1="50" x2="300" y2="260" stroke="#f59e0b" stroke-width="2"/>
                        <!-- Perpendicular Bisector extending OUTSIDE -->
                        <line x1="300" y1="200" x2="300" y2="260" stroke="#38bdf8" stroke-width="2"/>

                        <!-- True Point O (Outside on Circumcircle!) -->
                        <circle cx="300" cy="260" r="7" fill="#10b981"/>
                        <text x="300" y="278" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">True Point O (Outside on Circumcircle!)</text>
                    `;
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.textContent = "ACCURATE CONTRUCTION: Point O lies strictly OUTSIDE the triangle on its circumcircle. The false proof collapses completely!";
                }
            }

            fakeBtn.addEventListener('click', () => { isAccurate = false; update(); });
            realBtn.addEventListener('click', () => { isAccurate = true; update(); });
            update();
        }

        // Sim 16: Algorithmic Congruence Decision Tree & Truss Solver
        function renderSim16(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <!-- Section A: Congruence Solver -->
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-indigo-400 font-bold block mb-2">1. Congruence Decision Engine:</span>
                            <div class="grid grid-cols-3 gap-1.5 mb-2">
                                <button onclick="window.runDecision('SSS')" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono font-bold text-xs transition">SSS</button>
                                <button onclick="window.runDecision('SAS')" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono font-bold text-xs transition">SAS</button>
                                <button onclick="window.runDecision('ASA')" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono font-bold text-xs transition">ASA</button>
                                <button onclick="window.runDecision('AAS')" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono font-bold text-xs transition">AAS</button>
                                <button onclick="window.runDecision('RHS')" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 font-mono font-bold text-xs transition">RHS</button>
                                <button onclick="window.runDecision('SSA')" class="px-2 py-1.5 rounded bg-rose-900/50 hover:bg-rose-900 text-rose-300 font-mono font-bold text-xs transition">SSA</button>
                            </div>
                            <div id="sim16_engine_res" class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                Select a criterion above to trace the decision pipeline...
                            </div>
                        </div>

                        <!-- Section B: Truss Rigidity Solver -->
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-emerald-400 font-bold block mb-1">2. Maxwell Truss Rigidity Solver (m = 2j - 3):</span>
                            <div class="flex items-center gap-2 mb-2">
                                <label class="text-slate-300">Joints (j):</label>
                                <input type="range" id="sim16_j" min="3" max="8" value="5" class="w-24 accent-emerald-500">
                                <span id="sim16_j_val" class="font-mono text-emerald-400 font-bold">5</span>
                            </div>
                            <div id="sim16_truss_res" class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                Required member bars: m = 2(5) - 3 = 7 bars.
                            </div>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[220px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim16_svg" viewBox="0 0 600 220" class="w-full h-full max-h-[220px]">
                            <!-- Truss visualizer -->
                        </svg>
                    </div>
                </div>
            `;

            window.runDecision = function(code) {
                const res = document.getElementById('sim16_engine_res');
                if (code === 'SSS') {
                    res.innerHTML = `<span class="text-emerald-400">✓ SSS Theorem:</span> 3 Sides Equal ⇒ Triangles are Congruent.`;
                } else if (code === 'SAS') {
                    res.innerHTML = `<span class="text-emerald-400">✓ SAS Axiom:</span> 2 Sides + Included Angle ⇒ Congruent.`;
                } else if (code === 'ASA' || code === 'AAS') {
                    res.innerHTML = `<span class="text-emerald-400">✓ ${code} Criterion:</span> 2 Angles + Side ⇒ Congruent via 180° Sum.`;
                } else if (code === 'RHS') {
                    res.innerHTML = `<span class="text-emerald-400">✓ RHS Theorem:</span> Right Angle + Hypotenuse ⇒ Congruent (Pythagoras Lock).`;
                } else if (code === 'SSA') {
                    res.innerHTML = `<span class="text-rose-400">⚠ Ambiguous SSA:</span> 2 Sides + Non-included Angle ⇒ Congruence FAILS in general!`;
                }
            };

            const jSlider = document.getElementById('sim16_j');
            const jVal = document.getElementById('sim16_j_val');
            const trussRes = document.getElementById('sim16_truss_res');
            const svg = document.getElementById('sim16_svg');

            function updateTruss() {
                const j = parseInt(jSlider.value);
                jVal.textContent = j;
                const m = 2 * j - 3;
                trussRes.innerHTML = `Maxwell Rigidity: j = ${j} joints requires <b>m = ${m} member bars</b> arranged in interconnected triangles!`;

                // Draw a simple Warren truss with j joints
                let svgHtml = `<text x="300" y="25" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Warren Planar Truss (j = ${j}, m = ${m})</text>`;
                const startX = 100, stepX = 400 / Math.max(2, j - 2);

                for (let i = 0; i < j; i++) {
                    const isTop = (i % 2 === 1);
                    const px = startX + (i * stepX * 0.5);
                    const py = isTop ? 70 : 170;
                    svgHtml += `<circle cx="${px}" cy="${py}" r="6" fill="#10b981"/>`;
                }

                // Connect with triangulation lines
                svgHtml += `
                    <line x1="100" y1="170" x2="500" y2="170" stroke="#10b981" stroke-width="4"/>
                    <line x1="150" y1="70" x2="450" y2="70" stroke="#10b981" stroke-width="4"/>
                    <line x1="100" y1="170" x2="150" y2="70" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="150" y1="70" x2="200" y2="170" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="200" y1="170" x2="250" y2="70" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="250" y1="70" x2="300" y2="170" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="300" y1="170" x2="350" y2="70" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="350" y1="70" x2="400" y2="170" stroke="#38bdf8" stroke-width="3"/>
                `;
                svg.innerHTML = svgHtml;
            }

            jSlider.addEventListener('input', updateTruss);
            updateTruss();
        }

        // Initialize application on load
        window.addEventListener('DOMContentLoaded', () => {
            initSlidePicker();
            renderCurrentSlide();
        });
    </script>
</body>
</html>
"""

    html = html_template.replace("__SLIDES_JSON__", slides_json).replace("__QUIZZES_JSON__", quizzes_json)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated: {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH)} bytes")

if __name__ == '__main__':
    generate_html()

