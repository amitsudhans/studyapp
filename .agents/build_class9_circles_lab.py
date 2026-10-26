# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 11
CIRCLES (Competencies CG-4, C-7.3, CG-9)
Generates public/animations/class9-circles.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_circles_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-circles.html"

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
    <title>NCERT Class 9 Mathematics • Circles Laboratory</title>
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
                        <span class="hidden md:inline-block px-2 py-0.5 rounded text-[11px] font-medium bg-slate-800 text-slate-400">CG-4 • C-7.3 • CG-9</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-slate-100 flex items-center gap-2">
                        Circles: Chords, Arcs & Cyclic Theorems Lab
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
                <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white">Practical Applications, Wheels & Cultural Motifs</h2>
                <p id="slideSubtitle" class="text-xs sm:text-sm text-slate-300 mt-1 font-medium">Kinematic Rolling Resistance, Ancient Civilisation Inventions & Sacred Chakra Geometry</p>
            </div>

            <!-- Avatar & Teacher Speech Bubble -->
            <div class="flex items-center gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 max-w-md w-full shrink-0">
                <div id="avatarContainer" class="relative w-12 h-12 rounded-full bg-gradient-to-tr from-indigo-600 to-emerald-500 p-0.5 shrink-0 shadow-lg shadow-indigo-500/20">
                    <svg viewBox="0 0 100 100" class="w-full h-full rounded-full bg-slate-900">
                        <circle cx="50" cy="50" r="48" fill="#1e293b"/>
                        <path d="M25 55 C20 30 35 15 50 15 C65 15 80 30 75 55 C70 45 65 30 50 30 C35 30 30 45 25 55 Z" fill="#6366f1"/>
                        <circle cx="50" cy="50" r="26" fill="#fcd34d"/>
                        <circle cx="42" cy="48" r="7" fill="none" stroke="#0f172a" stroke-width="2.5"/>
                        <circle cx="58" cy="48" r="7" fill="none" stroke="#0f172a" stroke-width="2.5"/>
                        <line x1="49" y1="48" x2="51" y2="48" stroke="#0f172a" stroke-width="2.5"/>
                        <circle cx="42" cy="48" r="2.5" fill="#0f172a"/>
                        <circle cx="58" cy="48" r="2.5" fill="#0f172a"/>
                        <path d="M50 51 L48 55 L52 55" fill="none" stroke="#d97706" stroke-width="1.5" stroke-linecap="round"/>
                        <ellipse id="teacherMouth" cx="50" cy="63" rx="4" ry="1.5" fill="#991b1b"/>
                        <path d="M30 32 Q50 40 70 32 Q60 22 50 22 Q40 22 30 32 Z" fill="#4f46e5"/>
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
                        Welcome to Circles! The circle is arguably humanity's greatest discovery. Let's explore its geometry from rolling wheels to cyclic quadrilaterals.
                    </p>
                </div>
            </div>
        </div>

        <!-- Dynamic Content Body -->
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
                You have mastered circle definitions, chords and central angles, perpendicular bisectors, distance laws, the 2θ inscribed angle theorem, Thales' semicircle 90° theorem, concyclicity tests, and cyclic quadrilateral theorems!
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
                <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5">Mathematical Proof & Justification</div>
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
                osc.frequency.setValueAtTime(587.33, audioSynthContext.currentTime);
                osc.frequency.exponentialRampToValueAtTime(1174.66, audioSynthContext.currentTime + 0.3);
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

            if (currentSlideIndex === 19) {
                nextBtn.style.display = 'none';
                lastSlideNotice.classList.remove('hidden');
            } else {
                nextBtn.style.display = 'inline-flex';
                lastSlideNotice.classList.add('hidden');
            }

            if (currentSlideIndex < 16) {
                renderContentSlide(SLIDES_DATA[currentSlideIndex]);
            } else {
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

        // Sim 1: Wheel Rolling Kinematics & Ashoka Chakra 24-Spoke Generator
        function renderSim1(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Spokes Count:</label>
                            <input type="range" id="sim1_spokes" min="8" max="24" step="4" value="24" class="w-28 accent-indigo-500">
                            <span id="sim1_spokes_val" class="font-bold text-indigo-400 font-mono">24 (Ashoka Chakra)</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300">Roll Wheel:</label>
                            <input type="range" id="sim1_roll" min="0" max="360" value="0" class="w-28 accent-emerald-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim1_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim1_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Ashoka Chakra: 24 spokes evenly separated by 360° / 24 = 15° each!
                    </div>
                </div>
            `;

            const spokesSlider = document.getElementById('sim1_spokes');
            const rollSlider = document.getElementById('sim1_roll');
            const spokesVal = document.getElementById('sim1_spokes_val');
            const svg = document.getElementById('sim1_svg');
            const readout = document.getElementById('sim1_readout');

            function update() {
                const numSpokes = parseInt(spokesSlider.value);
                const roll = parseFloat(rollSlider.value);
                spokesVal.textContent = `${numSpokes}${numSpokes === 24 ? ' (Ashoka Chakra)' : ''}`;

                const Ox = 300, Oy = 140, R = 100;
                let spokesHtml = "";

                for (let i = 0; i < numSpokes; i++) {
                    const ang = ((i * 360 / numSpokes) + roll) * Math.PI / 180;
                    const x2 = Ox + R * Math.cos(ang);
                    const y2 = Oy + R * Math.sin(ang);
                    spokesHtml += `<line x1="${Ox}" y1="${Oy}" x2="${x2}" y2="${y2}" stroke="#38bdf8" stroke-width="2"/>`;
                }

                svg.innerHTML = `
                    <!-- Outer Rim -->
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="6"/>
                    <circle cx="${Ox}" cy="${Oy}" r="${R + 6}" fill="none" stroke="#4f46e5" stroke-width="2"/>
                    <!-- Spokes -->
                    ${spokesHtml}
                    <!-- Center Hub -->
                    <circle cx="${Ox}" cy="${Oy}" r="12" fill="#f59e0b" stroke="#f8fafc" stroke-width="2"/>
                `;

                readout.textContent = `Circle Spokes = ${numSpokes} | Angular separation = ${(360/numSpokes).toFixed(1)}° | Rotation = ${roll}°`;
            }

            spokesSlider.addEventListener('input', update);
            rollSlider.addEventListener('input', update);
            update();
        }

        // Sim 2: Circle Anatomy & Element Inspector
        function renderSim2(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Circle Anatomy Elements:</span>
                        <div class="flex gap-1.5">
                            <button id="sim2_btn_chord" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition">Chord & Segment</button>
                            <button id="sim2_btn_sector" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Sector (Radii)</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim2_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim2_desc" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = "chord";
            const chordBtn = document.getElementById('sim2_btn_chord');
            const sectorBtn = document.getElementById('sim2_btn_sector');
            const svg = document.getElementById('sim2_svg');
            const desc = document.getElementById('sim2_desc');

            function update() {
                const Ox = 300, Oy = 140, R = 100;
                const Ax = Ox - R * Math.cos(Math.PI / 4), Ay = Oy + R * Math.sin(Math.PI / 4);
                const Bx = Ox + R * Math.cos(Math.PI / 4), By = Oy + R * Math.sin(Math.PI / 4);

                if (mode === "chord") {
                    chordBtn.className = "px-2 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";
                    sectorBtn.className = "px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";

                    svg.innerHTML = `
                        <!-- Circle -->
                        <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                        <!-- Minor Segment fill -->
                        <path d="M ${Ax} ${By} A ${R} ${R} 0 0 0 ${Bx} ${By} Z" fill="rgba(244, 63, 94, 0.4)"/>
                        <!-- Chord AB -->
                        <line x1="${Ax}" y1="${Ay}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="4"/>

                        <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                        <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f59e0b"/>
                        <circle cx="${Bx}" cy="${By}" r="5" fill="#f59e0b"/>

                        <text x="${Ox}" y="${Oy - 10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">O (Centre)</text>
                        <text x="${Ax - 15}" y="${Ay + 10}" fill="#f59e0b" font-size="12" font-weight="bold">A</text>
                        <text x="${Bx + 15}" y="${By + 10}" fill="#f59e0b" font-size="12" font-weight="bold">B</text>

                        <text x="${Ox}" y="${Ay - 10}" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Chord AB</text>
                        <text x="${Ox}" y="${Ay + 35}" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">Minor Segment</text>
                    `;
                    desc.textContent = "CHORD & SEGMENT: Chord AB connects two points. The region enclosed between chord AB and arc AB is the Segment.";
                } else {
                    chordBtn.className = "px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                    sectorBtn.className = "px-2 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";

                    svg.innerHTML = `
                        <!-- Circle -->
                        <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                        <!-- Minor Sector fill -->
                        <path d="M ${Ox} ${Oy} L ${Ax} ${Ay} A ${R} ${R} 0 0 0 ${Bx} ${By} Z" fill="rgba(16, 185, 129, 0.35)"/>
                        <!-- Radii OA and OB -->
                        <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${Ay}" stroke="#10b981" stroke-width="3"/>
                        <line x1="${Ox}" y1="${Oy}" x2="${Bx}" y2="${By}" stroke="#10b981" stroke-width="3"/>

                        <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                        <text x="${Ox}" y="${Oy - 10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">O</text>
                        <text x="${(Ox+Ax)/2 - 15}" y="${(Oy+Ay)/2}" fill="#6ee7b7" font-size="11">Radius r</text>
                        <text x="${(Ox+Bx)/2 + 15}" y="${(Oy+By)/2}" fill="#6ee7b7" font-size="11">Radius r</text>
                        <text x="${Ox}" y="${Oy + 50}" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Sector AOB (Pie Slice)</text>
                    `;
                    desc.textContent = "SECTOR: Region enclosed between two radii OA, OB and their corresponding arc is a Sector.";
                }
            }

            chordBtn.addEventListener('click', () => { mode = "chord"; update(); });
            sectorBtn.addEventListener('click', () => { mode = "sector"; update(); });
            update();
        }

        // Sim 3: 3-Point Circumcircle & Perpendicular Bisectors
        function renderSim3(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem: Exactly 1 Unique Circle Passes Through 3 Non-Collinear Points</span>
                        <span class="text-emerald-400 font-mono text-[11px]">Perpendicular Bisectors Meet at O</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Circumcircle -->
                            <circle cx="300" cy="140" r="100" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="3"/>
                            <!-- Triangle ABC -->
                            <polygon points="230,68 215,198 396,168" fill="none" stroke="#f8fafc" stroke-width="2"/>

                            <!-- Perpendicular Bisectors -->
                            <line x1="160" y1="120" x2="440" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
                            <line x1="320" y1="50" x2="280" y2="230" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>

                            <!-- Circumcentre O -->
                            <circle cx="300" cy="140" r="6" fill="#10b981"/>
                            <text x="315" y="145" fill="#34d399" font-size="12" font-weight="bold">O (Circumcentre)</text>

                            <!-- Vertices -->
                            <circle cx="230" cy="68" r="6" fill="#f8fafc"/>
                            <circle cx="215" cy="198" r="6" fill="#f8fafc"/>
                            <circle cx="396" cy="168" r="6" fill="#f8fafc"/>

                            <text x="230" y="52" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                            <text x="195" y="210" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                            <text x="410" y="175" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        OA = OB = OC = R. The perpendicular bisectors intersect at a single unique point O!
                    </div>
                </div>
            `;
        }

        // Sim 4: Triangle Angle Morph & Circumcentre Migration
        function renderSim4(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Vertex Angle A:</label>
                            <input type="range" id="sim4_ang" min="45" max="135" value="60" class="w-36 accent-indigo-500">
                            <span id="sim4_ang_val" class="font-bold text-indigo-400 font-mono">60°</span>
                        </div>
                        <span id="sim4_type_badge" class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Acute Triangle</span>
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

            const slider = document.getElementById('sim4_ang');
            const angVal = document.getElementById('sim4_ang_val');
            const badge = document.getElementById('sim4_type_badge');
            const svg = document.getElementById('sim4_svg');
            const readout = document.getElementById('sim4_readout');

            function update() {
                const angA = parseFloat(slider.value);
                angVal.textContent = `${angA}°`;

                const Ox = 300, Oy = 140, R = 90;
                // Place B at 210°, C at 330°
                const Bx = Ox + R * Math.cos(210 * Math.PI / 180);
                const By = Oy - R * Math.sin(210 * Math.PI / 180);
                const Cx = Ox + R * Math.cos(330 * Math.PI / 180);
                const Cy = Oy - R * Math.sin(330 * Math.PI / 180);

                // Ax, Ay depends on angA
                const Ax = Ox, Ay = Oy - R;

                let status = "";
                if (angA < 90) {
                    badge.className = "px-2.5 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
                    badge.textContent = "Acute Triangle (Inside)";
                    status = "Circumcentre O lies strictly INSIDE the acute triangle.";
                } else if (angA === 90) {
                    badge.className = "px-2.5 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
                    badge.textContent = "Right Triangle (On Hypotenuse)";
                    status = "Circumcentre O lies EXACTLY on the midpoint of the hypotenuse!";
                } else {
                    badge.className = "px-2.5 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
                    badge.textContent = "Obtuse Triangle (Outside)";
                    status = "Circumcentre O lies strictly OUTSIDE in the exterior of the obtuse triangle.";
                }

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="2" stroke-dasharray="4,4"/>
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>

                    <circle cx="${Ox}" cy="${Oy}" r="6" fill="#10b981"/>
                    <text x="${Ox+10}" y="${Oy+10}" fill="#34d399" font-size="12" font-weight="bold">O</text>

                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f8fafc"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#f8fafc"/>
                    <circle cx="${Cx}" cy="${Cy}" r="5" fill="#f8fafc"/>

                    <text x="${Ax}" y="${Ay - 10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">A (${angA}°)</text>
                    <text x="${Bx - 15}" y="${By + 15}" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx + 15}" y="${Cy + 15}" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                `;

                readout.textContent = status;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 5: Chord Equalizer & Central Angle Subtended Dial
        function renderSim5(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Chord Length L:</label>
                            <input type="range" id="sim5_len" min="60" max="160" value="120" class="w-36 accent-indigo-500">
                            <span id="sim5_len_val" class="font-bold text-indigo-400 font-mono">120 mm</span>
                        </div>
                        <span class="text-slate-400 font-mono text-[11px]">Theorems 9.1 & 9.2</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim5_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim5_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim5_len');
            const lenVal = document.getElementById('sim5_len_val');
            const svg = document.getElementById('sim5_svg');
            const readout = document.getElementById('sim5_readout');

            function update() {
                const L = parseFloat(slider.value);
                lenVal.textContent = `${L} mm`;

                const Ox = 300, Oy = 140, R = 95;
                const theta = 2 * Math.asin(Math.min(1, (L / (2 * R))));
                const deg = (theta * 180 / Math.PI).toFixed(1);

                // Chord 1 (Right)
                const A1x = Ox + R * Math.cos(-theta/2), A1y = Oy + R * Math.sin(-theta/2);
                const B1x = Ox + R * Math.cos(theta/2), B1y = Oy + R * Math.sin(theta/2);

                // Chord 2 (Left)
                const A2x = Ox + R * Math.cos(Math.PI - theta/2), A2y = Oy + R * Math.sin(Math.PI - theta/2);
                const B2x = Ox + R * Math.cos(Math.PI + theta/2), B2y = Oy + R * Math.sin(Math.PI + theta/2);

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <!-- Sector 1 -->
                    <polygon points="${Ox},${Oy} ${A1x},${A1y} ${B1x},${B1y}" fill="rgba(16, 185, 129, 0.25)"/>
                    <line x1="${A1x}" y1="${A1y}" x2="${B1x}" y2="${B1y}" stroke="#10b981" stroke-width="4"/>
                    <!-- Sector 2 -->
                    <polygon points="${Ox},${Oy} ${A2x},${A2y} ${B2x},${B2y}" fill="rgba(56, 189, 248, 0.25)"/>
                    <line x1="${A2x}" y1="${A2y}" x2="${B2x}" y2="${B2y}" stroke="#38bdf8" stroke-width="4"/>

                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <text x="${Ox}" y="${Oy - 10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">O</text>

                    <text x="${Ox + 35}" y="${Oy + 5}" fill="#34d399" font-size="11" font-weight="bold">${deg}°</text>
                    <text x="${Ox - 55}" y="${Oy + 5}" fill="#38bdf8" font-size="11" font-weight="bold">${deg}°</text>
                `;

                readout.innerHTML = `
                    Theorem 9.1: Chord AB = CD (${L} mm) ⇒ Central angle ∠AOB = ∠COD = <b>${deg}°</b> (proven via SSS)!
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 6: Perpendicular from Centre Bisects Chord
        function renderSim6(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 9.3: Perpendicular OM ⊥ AB Bisects Chord AB (AM = MB)</span>
                        <span class="text-emerald-400 font-mono text-[11px]">RHS Congruence Proof</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Circle -->
                            <circle cx="300" cy="130" r="100" fill="none" stroke="#6366f1" stroke-width="3"/>
                            <!-- Chord AB -->
                            <line x1="220" y1="190" x2="380" y2="190" stroke="#f59e0b" stroke-width="4"/>
                            <!-- Perpendicular OM -->
                            <line x1="300" y1="130" x2="300" y2="190" stroke="#10b981" stroke-width="3"/>
                            <!-- Radii OA and OB -->
                            <line x1="300" y1="130" x2="220" y2="190" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                            <line x1="300" y1="130" x2="380" y2="190" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>

                            <!-- Right angle marker -->
                            <rect x="290" y="180" width="10" height="10" fill="none" stroke="#10b981" stroke-width="2"/>

                            <circle cx="300" cy="130" r="5" fill="#f8fafc"/>
                            <circle cx="300" cy="190" r="5" fill="#10b981"/>
                            <circle cx="220" cy="190" r="5" fill="#f59e0b"/>
                            <circle cx="380" cy="190" r="5" fill="#f59e0b"/>

                            <text x="300" y="118" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">O</text>
                            <text x="210" y="195" fill="#fbbf24" font-size="12" font-weight="bold">A</text>
                            <text x="390" y="195" fill="#fbbf24" font-size="12" font-weight="bold">B</text>
                            <text x="300" y="210" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">M (Midpoint)</text>

                            <text x="250" y="155" fill="#38bdf8" font-size="11">Radius r</text>
                            <text x="340" y="155" fill="#38bdf8" font-size="11">Radius r</text>
                            <text x="255" y="182" fill="#fbbf24" font-size="11">AM = 8</text>
                            <text x="335" y="182" fill="#fbbf24" font-size="11">MB = 8</text>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        △OMA ≅ △OMB by RHS ⇒ AM = MB (Midpoint confirmed!).
                    </div>
                </div>
            `;
        }

        // Sim 7: Chord Distance Slider & Pythagorean Calculator
        function renderSim7(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Distance d:</label>
                            <input type="range" id="sim7_d" min="0" max="95" value="60" class="w-36 accent-indigo-500">
                            <span id="sim7_d_val" class="font-bold text-indigo-400 font-mono">60 mm</span>
                        </div>
                        <span class="text-slate-400 font-mono text-[11px]">Radius r = 100 mm</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim7_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim7_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim7_d');
            const dVal = document.getElementById('sim7_d_val');
            const svg = document.getElementById('sim7_svg');
            const readout = document.getElementById('sim7_readout');

            function update() {
                const d = parseFloat(slider.value);
                dVal.textContent = `${d} mm`;

                const Ox = 300, Oy = 140, r = 100;
                const halfL = Math.sqrt(Math.max(0, r*r - d*d));
                const fullL = 2 * halfL;

                const chordY = Oy + d;
                const Ax = Ox - halfL, Bx = Ox + halfL;

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <!-- Chord AB -->
                    <line x1="${Ax}" y1="${chordY}" x2="${Bx}" y2="${chordY}" stroke="#f59e0b" stroke-width="4"/>
                    <!-- Distance segment OM -->
                    <line x1="${Ox}" y1="${Oy}" x2="${Ox}" y2="${chordY}" stroke="#10b981" stroke-width="3"/>
                    <!-- Radius OA -->
                    <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${chordY}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>

                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <circle cx="${Ox}" cy="${chordY}" r="5" fill="#10b981"/>

                    <text x="${Ox + 8}" y="${(Oy + chordY)/2}" fill="#34d399" font-size="11" font-weight="bold">d = ${d}</text>
                    <text x="${(Ox + Ax)/2 - 10}" y="${(Oy + chordY)/2 - 5}" fill="#38bdf8" font-size="11">r = 100</text>
                    <text x="${Ox}" y="${chordY + 18}" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">L = ${fullL.toFixed(1)} mm</text>
                `;

                readout.innerHTML = `
                    Pythagoras: r² = d² + (L/2)² ⇒ (L/2) = √(${r}² - ${d}²) = <b>${halfL.toFixed(1)} mm</b> ⇒ Total Chord L = <b>${fullL.toFixed(1)} mm</b>.
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 8: Equidistant Chords Balancer
        function renderSim8(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 9.5: Equal Chords Are Equidistant (d₁ = d₂)</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300">Distance d:</label>
                            <input type="range" id="sim8_d" min="20" max="80" value="50" class="w-28 accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim8_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim8_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim8_d');
            const svg = document.getElementById('sim8_svg');
            const readout = document.getElementById('sim8_readout');

            function update() {
                const d = parseFloat(slider.value);
                const Ox = 300, Oy = 140, r = 95;
                const halfL = Math.sqrt(Math.max(0, r*r - d*d));

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <!-- Chord 1 (Top) -->
                    <line x1="${Ox - halfL}" y1="${Oy - d}" x2="${Ox + halfL}" y2="${Oy - d}" stroke="#10b981" stroke-width="4"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Ox}" y2="${Oy - d}" stroke="#10b981" stroke-width="2"/>
                    <!-- Chord 2 (Bottom) -->
                    <line x1="${Ox - halfL}" y1="${Oy + d}" x2="${Ox + halfL}" y2="${Oy + d}" stroke="#38bdf8" stroke-width="4"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Ox}" y2="${Oy + d}" stroke="#38bdf8" stroke-width="2"/>

                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <text x="${Ox + 8}" y="${Oy - d/2}" fill="#34d399" font-size="11">d₁ = ${d}</text>
                    <text x="${Ox + 8}" y="${Oy + d/2 + 5}" fill="#38bdf8" font-size="11">d₂ = ${d}</text>
                `;

                readout.innerHTML = `
                    d₁ = d₂ = ${d} mm ⇒ Chord 1 = Chord 2 = <b>${(2 * halfL).toFixed(1)} mm</b> (Equal & Equidistant!).
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 9: Diameter as Longest Chord
        function renderSim9(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Move Chord to Centre (d):</label>
                            <input type="range" id="sim9_d" min="0" max="95" value="50" class="w-36 accent-indigo-500">
                            <span id="sim9_d_val" class="font-bold text-indigo-400 font-mono">50 mm</span>
                        </div>
                        <span id="sim9_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300">Regular Chord</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim9_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim9_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim9_d');
            const dVal = document.getElementById('sim9_d_val');
            const badge = document.getElementById('sim9_badge');
            const svg = document.getElementById('sim9_svg');
            const readout = document.getElementById('sim9_readout');

            function update() {
                const d = parseFloat(slider.value);
                dVal.textContent = `${d} mm`;

                const Ox = 300, Oy = 140, r = 100;
                const halfL = Math.sqrt(Math.max(0, r*r - d*d));
                const fullL = 2 * halfL;

                if (d === 0) {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
                    badge.textContent = "DIAMETER (MAXIMUM)";
                } else {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300";
                    badge.textContent = "Regular Chord";
                }

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <line x1="${Ox - halfL}" y1="${Oy + d}" x2="${Ox + halfL}" y2="${Oy + d}" stroke="${d === 0 ? '#10b981' : '#f59e0b'}" stroke-width="${d === 0 ? 5 : 3.5}"/>
                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <text x="${Ox}" y="${Oy - 10}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">O</text>
                    <text x="${Ox}" y="${Oy + d + 20}" fill="${d === 0 ? '#34d399' : '#fbbf24'}" font-size="13" font-weight="bold" text-anchor="middle">
                        ${d === 0 ? 'DIAMETER L = 200 mm' : `Chord L = ${fullL.toFixed(1)} mm`}
                    </text>
                `;

                if (d === 0) {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.innerHTML = `✓ MAXIMUM CHORD ACHIEVED: Distance d = 0 ⇒ The chord passes through the centre and becomes the DIAMETER (L = 2r = 200 mm)!`;
                } else {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300';
                    readout.innerHTML = `Distance d = ${d} mm ⇒ Chord length = ${fullL.toFixed(1)} mm. Slide to 0 to reach the maximum (diameter)!`;
                }
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 10: Inscribed Angle vs Central Angle (2θ vs θ)
        function renderSim10(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Move Point P on Circle:</label>
                            <input type="range" id="sim10_p_ang" min="30" max="150" value="90" class="w-36 accent-indigo-500">
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Theorem 9.7: ∠AOB = 2 × ∠APB</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim10_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim10_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim10_p_ang');
            const svg = document.getElementById('sim10_svg');
            const readout = document.getElementById('sim10_readout');

            function update() {
                const degP = parseFloat(slider.value);
                const Ox = 300, Oy = 140, R = 100;

                // Fixed arc AB at bottom: A at 220°, B at 320°
                const Ax = Ox + R * Math.cos(220 * Math.PI / 180);
                const Ay = Oy - R * Math.sin(220 * Math.PI / 180);
                const Bx = Ox + R * Math.cos(320 * Math.PI / 180);
                const By = Oy - R * Math.sin(320 * Math.PI / 180);

                // Central angle = 100 degrees
                const centralDeg = 100;
                const inscribedDeg = centralDeg / 2; // 50 degrees

                // Point P on top arc
                const radP = degP * Math.PI / 180;
                const Px = Ox + R * Math.cos(radP);
                const Py = Oy - R * Math.sin(radP);

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <!-- Central Angle Rays -->
                    <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${Ay}" stroke="#f59e0b" stroke-width="2.5"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="2.5"/>

                    <!-- Inscribed Angle Rays -->
                    <line x1="${Px}" y1="${Py}" x2="${Ax}" y2="${Ay}" stroke="#10b981" stroke-width="2.5"/>
                    <line x1="${Px}" y1="${Py}" x2="${Bx}" y2="${By}" stroke="#10b981" stroke-width="2.5"/>

                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <circle cx="${Px}" cy="${Py}" r="6" fill="#10b981"/>
                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f59e0b"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#f59e0b"/>

                    <text x="${Ox}" y="${Oy + 25}" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Central: 100°</text>
                    <text x="${Px}" y="${Py - 10}" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">P (${inscribedDeg}°)</text>
                    <text x="${Ax - 15}" y="${Ay + 10}" fill="#fbbf24" font-size="12" font-weight="bold">A</text>
                    <text x="${Bx + 15}" y="${By + 10}" fill="#fbbf24" font-size="12" font-weight="bold">B</text>
                `;

                readout.innerHTML = `
                    Inscribed Angle Theorem: Central Angle <b>∠AOB = 100°</b> = 2 × Inscribed Angle <b>∠APB = 50°</b>!
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 11: Same Segment Angle Glider
        function renderSim11(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Glide Point P along Arc:</label>
                            <input type="range" id="sim11_p" min="30" max="150" value="70" class="w-36 accent-emerald-500">
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Theorem 9.8</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim11_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim11_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Angles in the same segment are strictly identical!
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim11_p');
            const svg = document.getElementById('sim11_svg');

            function update() {
                const degP = parseFloat(slider.value);
                const Ox = 300, Oy = 140, R = 100;

                const Ax = Ox - R * Math.cos(Math.PI / 4), Ay = Oy + R * Math.sin(Math.PI / 4);
                const Bx = Ox + R * Math.cos(Math.PI / 4), By = Oy + R * Math.sin(Math.PI / 4);

                const radP = degP * Math.PI / 180;
                const Px = Ox + R * Math.cos(radP);
                const Py = Oy - R * Math.sin(radP);

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <line x1="${Ax}" y1="${Ay}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="3"/>

                    <!-- Inscribed rays from P -->
                    <line x1="${Px}" y1="${Py}" x2="${Ax}" y2="${Ay}" stroke="#10b981" stroke-width="2.5"/>
                    <line x1="${Px}" y1="${Py}" x2="${Bx}" y2="${By}" stroke="#10b981" stroke-width="2.5"/>

                    <circle cx="${Px}" cy="${Py}" r="6" fill="#10b981"/>
                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f59e0b"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#f59e0b"/>

                    <text x="${Px}" y="${Py - 10}" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">∠APB = 45.0° (Locked!)</text>
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 12: Thales' Semicircle 90° Explorer
        function renderSim12(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Point P on Semicircle:</label>
                            <input type="range" id="sim12_p" min="15" max="165" value="65" class="w-36 accent-emerald-500">
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Thales' Theorem: Always 90°</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim12_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim12_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Thales' Theorem: Angle in a semicircle is strictly 90°!
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim12_p');
            const svg = document.getElementById('sim12_svg');

            function update() {
                const deg = parseFloat(slider.value);
                const Ox = 300, Oy = 180, R = 110;

                const Ax = Ox - R, Ay = Oy;
                const Bx = Ox + R, By = Oy;

                const rad = deg * Math.PI / 180;
                const Px = Ox + R * Math.cos(rad);
                const Py = Oy - R * Math.sin(rad);

                svg.innerHTML = `
                    <!-- Semicircle Arc -->
                    <path d="M ${Ax} ${Ay} A ${R} ${R} 0 0 1 ${Bx} ${By}" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="3"/>
                    <!-- Diameter Base -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Bx}" y2="${By}" stroke="#38bdf8" stroke-width="4"/>

                    <line x1="${Px}" y1="${Py}" x2="${Ax}" y2="${Ay}" stroke="#f59e0b" stroke-width="2.5"/>
                    <line x1="${Px}" y1="${Py}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="2.5"/>

                    <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                    <circle cx="${Px}" cy="${Py}" r="6" fill="#f59e0b"/>

                    <text x="${Ox}" y="${Oy + 20}" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Diameter AB (Central Angle 180°)</text>
                    <text x="${Px}" y="${Py - 10}" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">∠APB = 90.0°</text>
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 13: 4-Point Concyclicity Detector
        function renderSim13(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Position of Point D:</label>
                            <input type="range" id="sim13_d" min="60" max="140" value="100" class="w-36 accent-indigo-500">
                        </div>
                        <span id="sim13_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300">Concyclic</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim13_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim13_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim13_d');
            const badge = document.getElementById('sim13_badge');
            const svg = document.getElementById('sim13_svg');
            const readout = document.getElementById('sim13_readout');

            function update() {
                const dVal = parseFloat(slider.value);
                const isConcyclic = (dVal === 100);

                if (isConcyclic) {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
                    badge.textContent = "✓ CONCYCLIC (All 4 on Circle)";
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.textContent = "∠ACB = ∠ADB = 50° on same side of AB ⇒ Points A, B, C, D are CONCYCLIC!";
                } else {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30";
                    badge.textContent = "✗ NOT Concyclic";
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    readout.textContent = "∠ACB ≠ ∠ADB. Point D does not lie on the circle through A, B, C.";
                }

                const Ox = 300, Oy = 140, R = 100;
                const Ax = 210, Ay = 190, Bx = 390, By = 190;
                const Cx = 250, Cy = 50;
                const Dx = 350, Dy = 50 + (100 - dVal);

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="${isConcyclic ? '#10b981' : '#64748b'}" stroke-width="${isConcyclic ? 3 : 1.5}" stroke-dasharray="${isConcyclic ? 'none' : '4,4'}"/>
                    <line x1="${Ax}" y1="${Ay}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="3"/>

                    <line x1="${Cx}" y1="${Cy}" x2="${Ax}" y2="${Ay}" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="${Cx}" y1="${Cy}" x2="${Bx}" y2="${By}" stroke="#38bdf8" stroke-width="2"/>

                    <line x1="${Dx}" y1="${Dy}" x2="${Ax}" y2="${Ay}" stroke="${isConcyclic ? '#10b981' : '#f43f5e'}" stroke-width="2"/>
                    <line x1="${Dx}" y1="${Dy}" x2="${Bx}" y2="${By}" stroke="${isConcyclic ? '#10b981' : '#f43f5e'}" stroke-width="2"/>

                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f8fafc"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#f8fafc"/>
                    <circle cx="${Cx}" cy="${Cy}" r="5" fill="#38bdf8"/>
                    <circle cx="${Dx}" cy="${Dy}" r="6" fill="${isConcyclic ? '#10b981' : '#f43f5e'}"/>

                    <text x="${Cx}" y="${Cy - 8}" fill="#38bdf8" font-size="11" font-weight="bold">C (50°)</text>
                    <text x="${Dx}" y="${Dy - 8}" fill="${isConcyclic ? '#34d399' : '#fda4af'}" font-size="11" font-weight="bold">D (${isConcyclic ? '50°' : (50 + (100 - dVal)/2).toFixed(1) + '°'})</text>
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 14: Cyclic Quadrilateral Opposite Angle Balancer
        function renderSim14(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Angle ∠A:</label>
                            <input type="range" id="sim14_A" min="50" max="130" value="75" class="w-36 accent-indigo-500">
                            <span id="sim14_A_val" class="font-bold text-indigo-400 font-mono">75°</span>
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Theorem 9.9: ∠A + ∠C = 180°</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim14_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim14_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim14_A');
            const AVal = document.getElementById('sim14_A_val');
            const svg = document.getElementById('sim14_svg');
            const readout = document.getElementById('sim14_readout');

            function update() {
                const angA = parseFloat(slider.value);
                const angC = 180 - angA;
                AVal.textContent = `${angA}°`;

                const Ox = 300, Oy = 140, R = 100;
                // Vertices
                const Ax = 230, Ay = 65;
                const Bx = 210, By = 190;
                const Cx = 380, Cy = 210;
                const Dx = 390, Dy = 85;

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>

                    <!-- Angle labels -->
                    <text x="${Ax - 5}" y="${Ay - 8}" fill="#38bdf8" font-size="12" font-weight="bold">A (${angA}°)</text>
                    <text x="${Cx + 5}" y="${Cy + 15}" fill="#38bdf8" font-size="12" font-weight="bold">C (${angC}°)</text>
                `;

                readout.innerHTML = `
                    Opposite Angles Supplementary: <b>∠A (${angA}°) + ∠C (${angC}°) = 180°</b>!
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 15: Special Cyclic Shapes & Ptolemy's Theorem
        function renderSim15(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Special Cyclic 4-gons:</span>
                        <div class="flex gap-1.5">
                            <button id="sim15_rec" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition">Cyclic Parallelogram (Rectangle)</button>
                            <button id="sim15_trap" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Cyclic Trapezium (Isosceles)</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim15_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim15_desc" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = "rec";
            const recBtn = document.getElementById('sim15_rec');
            const trapBtn = document.getElementById('sim15_trap');
            const svg = document.getElementById('sim15_svg');
            const desc = document.getElementById('sim15_desc');

            function update() {
                const Ox = 300, Oy = 140, R = 100;
                if (mode === "rec") {
                    recBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";
                    trapBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";

                    svg.innerHTML = `
                        <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                        <polygon points="220,80 220,200 380,200 380,80" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                        <text x="300" y="145" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">Every Cyclic Parallelogram is a RECTANGLE!</text>
                    `;
                    desc.textContent = "∠A = ∠C (parallelogram) and ∠A + ∠C = 180° (cyclic) ⇒ 2∠A = 180° ⇒ ∠A = 90° (Rectangle!).";
                } else {
                    recBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                    trapBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";

                    svg.innerHTML = `
                        <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                        <polygon points="250,60 210,210 390,210 350,60" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="3"/>
                        <text x="300" y="145" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">Every Cyclic Trapezium is ISOSCELES!</text>
                    `;
                    desc.textContent = "A cyclic trapezium ABCD with AB ∥ CD always has equal non-parallel legs (AD = BC) and equal diagonals.";
                }
            }

            recBtn.addEventListener('click', () => { mode = "rec"; update(); });
            trapBtn.addEventListener('click', () => { mode = "trap"; update(); });
            update();
        }

        // Sim 16: Interactive Algorithmic Circle Solver
        function renderSim16(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-indigo-400 font-bold block mb-1">1. Forward-Chaining Circle Engine:</span>
                            <div class="flex items-center gap-2 mb-2">
                                <label class="text-slate-300">Input Inscribed Angle:</label>
                                <input type="number" id="sim16_in" value="40" min="10" max="85" class="w-16 bg-slate-800 text-white px-2 py-1 rounded font-mono">
                                <button onclick="window.runCircleEngine()" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold">Solve</button>
                            </div>
                            <div id="sim16_res" class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                Output: Central Angle = 80°, Semicircle = 90°, Cyclic Opposite = 140°.
                            </div>
                        </div>

                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-emerald-400 font-bold block mb-1">2. Chord-Radius Solver (r² = d² + (L/2)²):</span>
                            <div class="flex items-center gap-2 mb-2">
                                <label class="text-slate-300">Radius r=10, Chord L=16 ⇒</label>
                                <span class="font-mono text-emerald-400 font-bold">d = 6 cm</span>
                            </div>
                            <div class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                d = √(10² - 8²) = √(100 - 64) = √36 = 6 cm!
                            </div>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[220px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 220" class="w-full h-full max-h-[220px]">
                            <circle cx="300" cy="110" r="80" fill="none" stroke="#6366f1" stroke-width="3"/>
                            <polygon points="240,60 230,160 370,160 360,60" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
                            <text x="300" y="115" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Rule-Based Forward Deduction</text>
                        </svg>
                    </div>
                </div>
            `;

            window.runCircleEngine = function() {
                const val = parseFloat(document.getElementById('sim16_in').value) || 40;
                const central = val * 2;
                const opp = 180 - val;
                document.getElementById('sim16_res').innerHTML = `
                    Deductions: Central Angle = <b>${central}°</b> (Theorem 9.7) | Cyclic Opposite Angle = <b>${opp}°</b> (Theorem 9.9)!
                `;
            };
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

