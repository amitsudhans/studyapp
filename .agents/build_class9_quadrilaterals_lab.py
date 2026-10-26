# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 10
4-GONS (QUADRILATERALS) (Competencies CG-4, C-4.2, C-7.3, CG-9)
Generates public/animations/class9-quadrilaterals.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_quadrilaterals_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-quadrilaterals.html"

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
    <title>NCERT Class 9 Mathematics • 4-gons (Quadrilaterals) Lab</title>
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
                        <span class="hidden md:inline-block px-2 py-0.5 rounded text-[11px] font-medium bg-slate-800 text-slate-400">CG-4 • C-4.2 • C-7.3 • CG-9</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-slate-100 flex items-center gap-2">
                        4-gons (Quadrilaterals) & Parallelograms Lab
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
                    <span id="slideCategory" class="text-slate-400 uppercase tracking-wider text-[10px]">Foundations</span>
                </div>
                <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white">Precise Definition & Anatomy of a 4-gon</h2>
                <p id="slideSubtitle" class="text-xs sm:text-sm text-slate-300 mt-1 font-medium">Non-Collinear Coplanar Points, Convex vs Concave Polygons & The 360° Angle Sum Theorem</p>
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
                        Welcome to 4-gons and Quadrilaterals! Let's explore how a simple diagonal reveals the secrets of parallelograms and the famous Midpoint Theorem.
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
                You have mastered 4-gon characterisations, all parallelogram theorems, central and reflection symmetries, the Midpoint Theorem and its converse, the 2:1 median centroid proof, Varignon's Theorem, coordinate geometry of midpoints, and universal plane tessellations!
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
                osc.frequency.setValueAtTime(520, audioSynthContext.currentTime);
                osc.frequency.exponentialRampToValueAtTime(1040, audioSynthContext.currentTime + 0.3);
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

        // Sim 1: 4-gon Builder & 360° Angle Sum
        function renderSim1(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Skew Vertex C (x):</label>
                            <input type="range" id="sim1_cx" min="280" max="520" value="440" class="w-28 accent-indigo-500">
                            <span id="sim1_cx_val" class="font-bold text-indigo-400">440</span>
                        </div>
                        <button id="sim1_diag_btn" class="px-3 py-1.5 rounded-lg bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 font-bold border border-indigo-500/40 text-xs transition">
                            Toggle Diagonal AC
                        </button>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim1_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim1_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Sum = ∠A + ∠B + ∠C + ∠D = (2 × 180°) = 360° (Always constant!)
                    </div>
                </div>
            `;

            let showDiag = true;
            const slider = document.getElementById('sim1_cx');
            const cxVal = document.getElementById('sim1_cx_val');
            const diagBtn = document.getElementById('sim1_diag_btn');
            const svg = document.getElementById('sim1_svg');
            const readout = document.getElementById('sim1_readout');

            function update() {
                const cx = parseFloat(slider.value);
                cxVal.textContent = cx;

                // Vertices
                const Ax = 140, Ay = 60;
                const Bx = 80, By = 220;
                const Cx = cx, Cy = 220;
                const Dx = 400, Dy = 80;

                let svgHtml = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                `;

                if (showDiag) {
                    svgHtml += `
                        <!-- Diagonal AC -->
                        <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4"/>
                        <!-- △ABC shade -->
                        <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(56, 189, 248, 0.15)"/>
                        <!-- △ACD shade -->
                        <polygon points="${Ax},${Ay} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.15)"/>
                        <text x="180" y="160" fill="#38bdf8" font-size="11" font-weight="bold">△ABC (180°)</text>
                        <text x="320" y="140" fill="#34d399" font-size="11" font-weight="bold">△ACD (180°)</text>
                    `;
                }

                // Vertices & Labels
                [ [Ax,Ay,'A'], [Bx,By,'B'], [Cx,Cy,'C'], [Dx,Dy,'D'] ].forEach(([x,y,l]) => {
                    svgHtml += `
                        <circle cx="${x}" cy="${y}" r="6" fill="#f8fafc" stroke="#6366f1" stroke-width="2"/>
                        <text x="${x + (x<250?-15:12)}" y="${y + (y<150?-8:15)}" fill="#f8fafc" font-size="12" font-weight="bold">${l}</text>
                    `;
                });

                svg.innerHTML = svgHtml;
            }

            slider.addEventListener('input', update);
            diagBtn.addEventListener('click', () => {
                showDiag = !showDiag;
                update();
            });
            update();
        }

        // Sim 2: Parallelogram Characterisation Tester
        function renderSim2(container) {
            const tests = [
                {
                    title: "1. Opposite Sides Parallel (Definition)",
                    desc: "AB ∥ CD and AD ∥ BC. Both pairs of opposite sides are parallel."
                },
                {
                    title: "2. Opposite Sides Equal (Theorem 8.2)",
                    desc: "AB = CD and AD = BC. Both pairs of opposite sides have identical lengths."
                },
                {
                    title: "3. Opposite Angles Equal (Theorem 8.4)",
                    desc: "∠A = ∠C and ∠B = ∠D. Both pairs of opposite angles are equal."
                },
                {
                    title: "4. Diagonals Bisect (Theorem 8.6)",
                    desc: "OA = OC and OB = OD. The diagonals share the exact same midpoint O."
                },
                {
                    title: "5. One Pair Equal & Parallel (Theorem 8.8)",
                    desc: "AB = CD and AB ∥ CD. One pair of opposite sides is both equal and parallel."
                }
            ];

            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Select Test:</span>
                        <select id="sim2_select" class="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2 py-1 text-xs font-bold">
                            ${tests.map((t, i) => `<option value="${i}">${t.title}</option>`).join('')}
                        </select>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim2_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim2_readout" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const select = document.getElementById('sim2_select');
            const svg = document.getElementById('sim2_svg');
            const readout = document.getElementById('sim2_readout');

            function update() {
                const idx = parseInt(select.value);
                const Ax = 180, Ay = 60;
                const Bx = 100, By = 220;
                const Cx = 420, Cy = 220;
                const Dx = 500, Dy = 60;
                const Ox = 300, Oy = 140;

                let svgHtml = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="3"/>
                    <text x="${Ax-15}" y="${Ay}" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                    <text x="${Bx-15}" y="${By+10}" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx+12}" y="${By+10}" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                    <text x="${Dx+12}" y="${Ay}" fill="#f8fafc" font-size="12" font-weight="bold">D</text>
                `;

                if (idx === 0) {
                    // Parallel arrows
                    svgHtml += `
                        <text x="260" y="50" fill="#38bdf8" font-size="12" font-weight="bold">AB ∥ CD ➔➔</text>
                        <text x="260" y="240" fill="#38bdf8" font-size="12" font-weight="bold">AB ∥ CD ➔➔</text>
                    `;
                } else if (idx === 1) {
                    svgHtml += `
                        <text x="340" y="50" fill="#fbbf24" font-size="12" font-weight="bold">L = 320</text>
                        <text x="260" y="240" fill="#fbbf24" font-size="12" font-weight="bold">L = 320</text>
                        <text x="120" y="140" fill="#f43f5e" font-size="12" font-weight="bold">W = 180</text>
                        <text x="470" y="140" fill="#f43f5e" font-size="12" font-weight="bold">W = 180</text>
                    `;
                } else if (idx === 2) {
                    svgHtml += `
                        <text x="190" y="90" fill="#38bdf8" font-size="12" font-weight="bold">∠A = 115°</text>
                        <text x="350" y="210" fill="#38bdf8" font-size="12" font-weight="bold">∠C = 115°</text>
                        <text x="130" y="200" fill="#fbbf24" font-size="12" font-weight="bold">∠B = 65°</text>
                        <text x="440" y="90" fill="#fbbf24" font-size="12" font-weight="bold">∠D = 65°</text>
                    `;
                } else if (idx === 3) {
                    svgHtml += `
                        <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                        <line x1="${Bx}" y1="${By}" x2="${Dx}" y2="${Dy}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                        <circle cx="${Ox}" cy="${Oy}" r="5" fill="#f8fafc"/>
                        <text x="${Ox+8}" y="${Oy-8}" fill="#f8fafc" font-size="11" font-weight="bold">O</text>
                        <text x="220" y="100" fill="#fbbf24" font-size="11">OA = OC</text>
                        <text x="360" y="180" fill="#38bdf8" font-size="11">OB = OD</text>
                    `;
                } else {
                    svgHtml += `
                        <line x1="${Ax}" y1="${Ay}" x2="${Dx}" y2="${Dy}" stroke="#f59e0b" stroke-width="5"/>
                        <line x1="${Bx}" y1="${By}" x2="${Cx}" y2="${Cy}" stroke="#f59e0b" stroke-width="5"/>
                        <text x="300" y="140" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">AB = CD AND AB ∥ CD</text>
                    `;
                }

                svg.innerHTML = svgHtml;
                readout.textContent = `✓ ${tests[idx].desc} ⇒ Guaranteed to be a Parallelogram!`;
            }

            select.addEventListener('change', update);
            update();
        }

        // Sim 3: Diagonal Partition & CPCTC Explorer
        function renderSim3(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 8.1: Diagonal Partition into 2 Congruent Triangles</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300">Separate Halves:</label>
                            <input type="range" id="sim3_sep" min="0" max="60" value="0" class="w-28 accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim3_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim3_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        △ABC ≅ △CDA by ASA ⇒ AB = CD and BC = DA by CPCTC!
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim3_sep');
            const svg = document.getElementById('sim3_svg');

            function update() {
                const s = parseFloat(slider.value);
                const Ax = 180, Ay = 60 - s;
                const Bx = 100 - s, By = 220;
                const Cx = 420, Cy = 220 + s;
                const Dx = 500 + s, Dy = 60;

                svg.innerHTML = `
                    <!-- Bottom Triangle △ABC -->
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Top Triangle △CDA -->
                    <polygon points="${Ax},${Ay} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>

                    <text x="210" y="170" fill="#a5b4fc" font-size="12" font-weight="bold">△ABC</text>
                    <text x="350" y="110" fill="#6ee7b7" font-size="12" font-weight="bold">△CDA</text>

                    <!-- Vertices -->
                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f8fafc"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#f8fafc"/>
                    <circle cx="${Cx}" cy="${Cy}" r="5" fill="#f8fafc"/>
                    <circle cx="${Dx}" cy="${Dy}" r="5" fill="#f8fafc"/>
                    <text x="${Ax-15}" y="${Ay}" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                    <text x="${Bx-15}" y="${By+10}" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx+12}" y="${Cy+10}" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                    <text x="${Dx+12}" y="${Dy}" fill="#f8fafc" font-size="12" font-weight="bold">D</text>
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 4: Opposite Angle Balancer & Supplementary Angle Wheel
        function renderSim4(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Angle ∠A:</label>
                            <input type="range" id="sim4_A" min="40" max="140" value="65" class="w-36 accent-indigo-500">
                            <span id="sim4_A_val" class="font-bold text-indigo-400">65°</span>
                        </div>
                        <span class="text-slate-400 font-mono text-[11px]">Theorem 8.4: ∠A = ∠C, ∠B = ∠D</span>
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

            const ASlider = document.getElementById('sim4_A');
            const AVal = document.getElementById('sim4_A_val');
            const svg = document.getElementById('sim4_svg');
            const readout = document.getElementById('sim4_readout');

            function update() {
                const angA = parseFloat(ASlider.value);
                const angB = 180 - angA;
                AVal.textContent = `${angA}°`;

                const rad = (angA * Math.PI) / 180;
                const L = 160;
                const H = 280;

                const Ax = 240, Ay = 60;
                const Bx = Ax - L * Math.cos(rad), By = Ay + L * Math.sin(rad);
                const Cx = Bx + 220, Cy = By;
                const Dx = Ax + 220, Dy = Ay;

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Angle labels -->
                    <text x="${Ax - 20}" y="${Ay + 25}" fill="#38bdf8" font-size="12" font-weight="bold">∠A = ${angA}°</text>
                    <text x="${Cx - 20}" y="${Cy - 15}" fill="#38bdf8" font-size="12" font-weight="bold">∠C = ${angA}°</text>
                    <text x="${Bx + 15}" y="${By - 15}" fill="#f59e0b" font-size="12" font-weight="bold">∠B = ${angB}°</text>
                    <text x="${Dx - 60}" y="${Dy + 25}" fill="#f59e0b" font-size="12" font-weight="bold">∠D = ${angB}°</text>
                `;

                readout.innerHTML = `
                    Opposite Angles Equal: <b>∠A = ∠C = ${angA}°</b> | <b>∠B = ∠D = ${angB}°</b>.<br>
                    Consecutive Angles Supplementary: ∠A + ∠B = ${angA}° + ${angB}° = <b>180°</b>.
                `;
            }

            ASlider.addEventListener('input', update);
            update();
        }

        // Sim 5: Diagonal Bisection & Mutual Midpoint Simulator
        function renderSim5(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 8.6: Diagonals Bisect Each Other at Point O</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300">Skew:</label>
                            <input type="range" id="sim5_skew" min="40" max="140" value="70" class="w-28 accent-indigo-500">
                        </div>
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

            const slider = document.getElementById('sim5_skew');
            const svg = document.getElementById('sim5_svg');
            const readout = document.getElementById('sim5_readout');

            function update() {
                const skew = parseFloat(slider.value);
                const rad = (skew * Math.PI) / 180;
                const Ax = 200, Ay = 60;
                const Bx = Ax - 140 * Math.cos(rad), By = Ay + 140 * Math.sin(rad);
                const Cx = Bx + 260, Cy = By;
                const Dx = Ax + 260, Dy = Ay;
                const Ox = (Ax + Cx) / 2, Oy = (Ay + Cy) / 2;

                const lenAC = Math.hypot(Cx - Ax, Cy - Ay);
                const lenBD = Math.hypot(Dx - Bx, Dy - By);

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Diagonals -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#f59e0b" stroke-width="2.5"/>
                    <line x1="${Bx}" y1="${By}" x2="${Dx}" y2="${Dy}" stroke="#38bdf8" stroke-width="2.5"/>

                    <circle cx="${Ox}" cy="${Oy}" r="6" fill="#f8fafc"/>
                    <text x="${Ox+8}" y="${Oy-8}" fill="#f8fafc" font-size="12" font-weight="bold">O</text>

                    <!-- Segment markings -->
                    <text x="${(Ax+Ox)/2 - 20}" y="${(Ay+Oy)/2}" fill="#fbbf24" font-size="11">OA = ${(lenAC/2).toFixed(1)}</text>
                    <text x="${(Cx+Ox)/2 + 10}" y="${(Cy+Oy)/2}" fill="#fbbf24" font-size="11">OC = ${(lenAC/2).toFixed(1)}</text>
                    <text x="${(Bx+Ox)/2 - 25}" y="${(By+Oy)/2}" fill="#38bdf8" font-size="11">OB = ${(lenBD/2).toFixed(1)}</text>
                    <text x="${(Dx+Ox)/2 + 10}" y="${(Dy+Oy)/2}" fill="#38bdf8" font-size="11">OD = ${(lenBD/2).toFixed(1)}</text>
                `;

                readout.innerHTML = `
                    OA = OC = ${(lenAC/2).toFixed(1)} cm | OB = OD = ${(lenBD/2).toFixed(1)} cm.<br>
                    Point O bisects BOTH diagonals simultaneously!
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 6: Special 4-gon Morphing Transformer
        function renderSim6(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Morph Shape:</span>
                        <div class="flex gap-1.5">
                            <button id="sim6_par" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition">Parallelogram</button>
                            <button id="sim6_rec" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Rectangle</button>
                            <button id="sim6_rho" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Rhombus</button>
                            <button id="sim6_squ" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Square</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim6_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim6_desc" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = "par";
            const parBtn = document.getElementById('sim6_par');
            const recBtn = document.getElementById('sim6_rec');
            const rhoBtn = document.getElementById('sim6_rho');
            const squBtn = document.getElementById('sim6_squ');
            const svg = document.getElementById('sim6_svg');
            const desc = document.getElementById('sim6_desc');

            function setMode(m) {
                mode = m;
                [parBtn, recBtn, rhoBtn, squBtn].forEach(b => {
                    b.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                });
                if (m === 'par') parBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";
                if (m === 'rec') recBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";
                if (m === 'rho') rhoBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";
                if (m === 'squ') squBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition";

                let Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;
                let info = "";

                if (m === 'par') {
                    Ax = 220; Ay = 70; Bx = 140; By = 210; Cx = 380; Cy = 210; Dx = 460; Dy = 70;
                    info = "General Parallelogram: Opposite sides equal & parallel. Diagonals bisect, but AC ≠ BD and AC ∡ BD.";
                } else if (m === 'rec') {
                    Ax = 160; Ay = 70; Bx = 160; By = 210; Cx = 440; Cy = 210; Dx = 440; Dy = 70;
                    info = "Rectangle: All angles = 90°. Diagonals are EQUAL in length (AC = BD)!";
                } else if (m === 'rho') {
                    Ax = 300; Ay = 50; Bx = 180; By = 140; Cx = 300; Cy = 230; Dx = 420; Dy = 140;
                    info = "Rhombus: All 4 sides equal. Diagonals are PERPENDICULAR bisectors (AC ⊥ BD)!";
                } else {
                    Ax = 210; Ay = 50; Bx = 210; By = 230; Cx = 390; Cy = 230; Dx = 390; Dy = 50;
                    info = "Square: Regular 4-gon! All sides equal, all angles = 90°, diagonals are BOTH equal AND perpendicular!";
                }

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                    <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                    <line x1="${Bx}" y1="${By}" x2="${Dx}" y2="${Dy}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                `;
                desc.textContent = info;
            }

            parBtn.addEventListener('click', () => setMode('par'));
            recBtn.addEventListener('click', () => setMode('rec'));
            rhoBtn.addEventListener('click', () => setMode('rho'));
            squBtn.addEventListener('click', () => setMode('squ'));
            setMode('par');
        }

        // Sim 7: 180° Half-Turn Central Symmetry Visualizer
        function renderSim7(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Half-Turn Rotation Angle:</label>
                            <input type="range" id="sim7_rot" min="0" max="180" value="0" class="w-36 accent-emerald-500">
                            <span id="sim7_rot_val" class="font-bold text-emerald-400">0°</span>
                        </div>
                        <span class="text-slate-400 font-mono text-[11px]">Center O = Point of Inversion</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Static Reference Outline -->
                            <polygon points="220,70 140,210 380,210 460,70" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
                            <!-- Center O -->
                            <circle cx="300" cy="140" r="5" fill="#f8fafc"/>
                            <text x="300" y="125" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Center O</text>

                            <!-- Rotating Parallelogram Group -->
                            <g id="sim7_group">
                                <polygon points="220,70 140,210 380,210 460,70" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>
                                <text x="215" y="60" fill="#a5b4fc" font-size="12" font-weight="bold">A</text>
                                <text x="125" y="220" fill="#6ee7b7" font-size="12" font-weight="bold">B</text>
                                <text x="390" y="220" fill="#fde68a" font-size="12" font-weight="bold">C</text>
                                <text x="470" y="60" fill="#fda4af" font-size="12" font-weight="bold">D</text>
                            </g>
                        </svg>
                    </div>

                    <div id="sim7_badge" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        Slide to rotate 180° around diagonal intersection point O.
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim7_rot');
            const rotVal = document.getElementById('sim7_rot_val');
            const group = document.getElementById('sim7_group');
            const badge = document.getElementById('sim7_badge');

            slider.addEventListener('input', () => {
                const rot = parseFloat(slider.value);
                rotVal.textContent = `${rot}°`;
                group.setAttribute('transform', `rotate(${rot}, 300, 140)`);

                if (rot === 180) {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-bold bg-emerald-950/60 border border-emerald-500 text-emerald-300';
                    badge.innerHTML = `✓ 180° HALF-TURN COMPLETE: The parallelogram maps precisely onto itself! A swaps with C, B swaps with D.`;
                } else {
                    badge.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-slate-900 border border-slate-800 text-slate-300';
                    badge.innerHTML = `Rotating by ${rot}° around Center O... (Stop at 180° for central symmetry!)`;
                }
            });
        }

        // Sim 8: 4-gon Symmetry Mirror & Rotation Analyzer
        function renderSim8(container) {
            const shapes = [
                { name: "General Parallelogram", lines: 0, order: 2, note: "0 Mirror Lines, Order-2 Rotational Symmetry (180°)." },
                { name: "Rectangle", lines: 2, order: 2, note: "2 Mirror Lines (joining opposite midpoints), Order-2 Rotational Symmetry." },
                { name: "Rhombus", lines: 2, order: 2, note: "2 Mirror Lines (the two diagonals), Order-2 Rotational Symmetry." },
                { name: "Square", lines: 4, order: 4, note: "4 Mirror Lines (2 diagonals + 2 midpoints), Order-4 Rotational Symmetry (90°)." },
                { name: "Kite", lines: 1, order: 1, note: "1 Mirror Line (main diagonal), Order-1 Rotational Symmetry." }
            ];

            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Select 4-gon:</span>
                        <select id="sim8_select" class="bg-slate-800 border border-slate-700 text-slate-200 rounded-lg px-2 py-1 text-xs font-bold">
                            ${shapes.map((s, i) => `<option value="${i}">${s.name}</option>`).join('')}
                        </select>
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

            const select = document.getElementById('sim8_select');
            const svg = document.getElementById('sim8_svg');
            const readout = document.getElementById('sim8_readout');

            function update() {
                const idx = parseInt(select.value);
                const s = shapes[idx];

                let svgHtml = "";
                if (idx === 0) {
                    svgHtml = `
                        <polygon points="220,70 140,210 380,210 460,70" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>
                        <circle cx="300" cy="140" r="5" fill="#f59e0b"/>
                        <text x="300" y="250" fill="#94a3b8" font-size="12" text-anchor="middle">No reflection axes exist!</text>
                    `;
                } else if (idx === 1) {
                    svgHtml = `
                        <polygon points="160,70 160,210 440,210 440,70" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="3"/>
                        <!-- 2 mirror lines -->
                        <line x1="300" y1="40" x2="300" y2="240" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,3"/>
                        <line x1="130" y1="140" x2="470" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,3"/>
                        <text x="300" y="260" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">2 Reflection Axes</text>
                    `;
                } else if (idx === 2) {
                    svgHtml = `
                        <polygon points="300,50 180,140 300,230 420,140" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                        <line x1="300" y1="30" x2="300" y2="250" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,3"/>
                        <line x1="160" y1="140" x2="440" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,3"/>
                        <text x="300" y="270" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">2 Reflection Axes (Diagonals)</text>
                    `;
                } else if (idx === 3) {
                    svgHtml = `
                        <polygon points="210,50 210,230 390,230 390,50" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="300" y1="30" x2="300" y2="250" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
                        <line x1="180" y1="140" x2="420" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,3"/>
                        <line x1="190" y1="30" x2="410" y2="250" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
                        <line x1="190" y1="250" x2="410" y2="30" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
                        <text x="300" y="270" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">4 Reflection Axes</text>
                    `;
                } else {
                    svgHtml = `
                        <polygon points="300,40 210,120 300,240 390,120" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="3"/>
                        <line x1="300" y1="20" x2="300" y2="260" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,3"/>
                        <text x="300" y="275" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">1 Reflection Axis (Main Diagonal)</text>
                    `;
                }

                svg.innerHTML = svgHtml;
                readout.textContent = s.note;
            }

            select.addEventListener('change', update);
            update();
        }

        // Sim 9: Midpoint Theorem Proof Animator
        function renderSim9(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Theorem 8.9 Proof Steps:</span>
                        <div class="flex gap-1.5">
                            <button id="sim9_s1" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition">1. Midpoints D, E</button>
                            <button id="sim9_s2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">2. Extend EF = DE</button>
                            <button id="sim9_s3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">3. BCFD Parallelogram</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim9_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim9_desc" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let step = 1;
            const b1 = document.getElementById('sim9_s1');
            const b2 = document.getElementById('sim9_s2');
            const b3 = document.getElementById('sim9_s3');
            const svg = document.getElementById('sim9_svg');
            const desc = document.getElementById('sim9_desc');

            function setStep(s) {
                step = s;
                [b1, b2, b3].forEach((b, i) => {
                    b.className = (i + 1 === s) ? "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold text-xs transition" : "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                });

                const Ax = 240, Ay = 50;
                const Bx = 100, By = 230;
                const Cx = 460, Cy = 230;
                const Dx = (Ax + Bx) / 2, Dy = (Ay + By) / 2;
                const Ex = (Ax + Cx) / 2, Ey = (Ay + Cy) / 2;
                const Fx = Ex + (Ex - Dx), Fy = Ey + (Ey - Dy);

                let svgHtml = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                    <text x="${Ax}" y="${Ay-10}" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                    <text x="${Bx-15}" y="${By+10}" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                    <text x="${Cx+10}" y="${By+10}" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                `;

                if (s === 1) {
                    svgHtml += `
                        <line x1="${Dx}" y1="${Dy}" x2="${Ex}" y2="${Ey}" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="${Dx}" cy="${Dy}" r="6" fill="#f59e0b"/>
                        <circle cx="${Ex}" cy="${Ey}" r="6" fill="#f59e0b"/>
                        <text x="${Dx-20}" y="${Dy}" fill="#fbbf24" font-size="12" font-weight="bold">D</text>
                        <text x="${Ex+10}" y="${Ey}" fill="#fbbf24" font-size="12" font-weight="bold">E</text>
                    `;
                    desc.textContent = "Step 1: D is midpoint of AB (AD=BD), E is midpoint of AC (AE=CE). Connect DE.";
                } else if (s === 2) {
                    svgHtml += `
                        <line x1="${Dx}" y1="${Dy}" x2="${Fx}" y2="${Fy}" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
                        <line x1="${Cx}" y1="${Cy}" x2="${Fx}" y2="${Fy}" stroke="#10b981" stroke-width="2.5"/>
                        <circle cx="${Fx}" cy="${Fy}" r="6" fill="#10b981"/>
                        <text x="${Fx+10}" y="${Fy}" fill="#6ee7b7" font-size="12" font-weight="bold">F</text>
                        <!-- Congruent pair -->
                        <polygon points="${Ax},${Ay} ${Dx},${Dy} ${Ex},${Ey}" fill="rgba(56, 189, 248, 0.3)"/>
                        <polygon points="${Cx},${Cy} ${Fx},${Fy} ${Ex},${Ey}" fill="rgba(16, 185, 129, 0.3)"/>
                        <text x="320" y="110" fill="#38bdf8" font-size="11">△ADE ≅ △CFE (SAS)</text>
                    `;
                    desc.textContent = "Step 2: Extend DE to F such that EF = DE. Join CF. By SAS, △ADE ≅ △CFE ⇒ AD = CF and AD ∥ CF.";
                } else {
                    svgHtml += `
                        <polygon points="${Bx},${By} ${Cx},${Cy} ${Fx},${Fy} ${Dx},${Dy}" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                        <text x="280" y="180" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">BCFD is a Parallelogram!</text>
                    `;
                    desc.textContent = "Step 3: Since BD = CF and BD ∥ CF, BCFD is a parallelogram! Hence DF ∥ BC and DE = 1/2 DF = 1/2 BC!";
                }

                svg.innerHTML = svgHtml;
            }

            b1.addEventListener('click', () => setStep(1));
            b2.addEventListener('click', () => setStep(2));
            b3.addEventListener('click', () => setStep(3));
            setStep(1);
        }

        // Sim 10: Converse Midpoint Simulator
        function renderSim10(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Position of Point D on AB:</label>
                            <input type="range" id="sim10_d" min="20" max="80" value="50" class="w-36 accent-emerald-500">
                            <span id="sim10_d_val" class="font-bold text-emerald-400">50% (Midpoint)</span>
                        </div>
                        <span class="text-slate-400 font-mono text-[11px]">Theorem 8.10</span>
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

            const slider = document.getElementById('sim10_d');
            const dVal = document.getElementById('sim10_d_val');
            const svg = document.getElementById('sim10_svg');
            const readout = document.getElementById('sim10_readout');

            function update() {
                const pct = parseFloat(slider.value) / 100;
                dVal.textContent = `${Math.round(pct * 100)}%${pct === 0.5 ? ' (Midpoint)' : ''}`;

                const Ax = 250, Ay = 50;
                const Bx = 100, By = 230;
                const Cx = 470, Cy = 230;

                const Dx = Ax + (Bx - Ax) * pct;
                const Dy = Ay + (By - Ay) * pct;
                const Ex = Ax + (Cx - Ax) * pct;
                const Ey = Ay + (Cy - Ay) * pct;

                svg.innerHTML = `
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Parallel line DE -->
                    <line x1="${Dx}" y1="${Dy}" x2="${Ex}" y2="${Ey}" stroke="#10b981" stroke-width="4"/>
                    <line x1="${Bx}" y1="${By}" x2="${Cx}" y2="${Cy}" stroke="#10b981" stroke-width="4"/>

                    <circle cx="${Dx}" cy="${Dy}" r="6" fill="#f59e0b"/>
                    <circle cx="${Ex}" cy="${Ey}" r="6" fill="#f59e0b"/>
                    <text x="${Dx-20}" y="${Dy}" fill="#fbbf24" font-size="12" font-weight="bold">D</text>
                    <text x="${Ex+10}" y="${Ey}" fill="#fbbf24" font-size="12" font-weight="bold">E</text>

                    <text x="300" y="250" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">DE ∥ BC</text>
                `;

                if (pct === 0.5) {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    readout.innerHTML = `✓ CONVERSE MIDPOINT THEOREM: D is the exact midpoint of AB ⇒ Line DE ∥ BC bisects AC at its exact midpoint E (AE = EC)!`;
                } else {
                    readout.className = 'p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-slate-900 border border-slate-800 text-slate-300';
                    readout.innerHTML = `D is at ${(pct*100).toFixed(0)}% of AB. Move slider to 50% for the exact midpoint!`;
                }
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 11: Centroid 2:1 Lever & Median Concurrency Visualizer
        function renderSim11(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Median Concurrency & The 2:1 Centroid Ratio</span>
                        <span class="text-indigo-400 font-mono font-bold">FEQP Parallelogram Proof</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Triangle ABC -->
                            <polygon points="280,40 100,230 480,230" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="3"/>
                            <!-- Medians -->
                            <line x1="280" y1="40" x2="290" y2="230" stroke="#f59e0b" stroke-width="2"/>
                            <line x1="100" y1="230" x2="380" y2="135" stroke="#38bdf8" stroke-width="2"/>
                            <line x1="480" y1="230" x2="190" y2="135" stroke="#10b981" stroke-width="2"/>

                            <!-- Centroid G -->
                            <circle cx="286.6" cy="166.6" r="7" fill="#f43f5e"/>
                            <text x="305" y="172" fill="#fda4af" font-size="14" font-weight="bold">G (Centroid)</text>

                            <!-- Labels -->
                            <text x="280" y="28" fill="#f8fafc" font-size="12" font-weight="bold">A</text>
                            <text x="80" y="240" fill="#f8fafc" font-size="12" font-weight="bold">B</text>
                            <text x="495" y="240" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
                            <text x="290" y="250" fill="#fbbf24" font-size="11">D (Midpoint BC)</text>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Centroid G divides each median: <b>AG : GD = 2 : 1</b> | <b>BG : GE = 2 : 1</b> | <b>CG : GF = 2 : 1</b>!
                    </div>
                </div>
            `;
        }

        // Sim 12: Varignon's Theorem Playground
        function renderSim12(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Distort Vertex C:</label>
                            <input type="range" id="sim12_c" min="320" max="520" value="450" class="w-32 accent-indigo-500">
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Varignon: Midpoints = Parallelogram</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim12_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim12_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim12_c');
            const svg = document.getElementById('sim12_svg');
            const readout = document.getElementById('sim12_readout');

            function update() {
                const cx = parseFloat(slider.value);
                const Ax = 140, Ay = 50;
                const Bx = 90, By = 220;
                const Cx = cx, Cy = 230;
                const Dx = 470, Dy = 80;

                const Px = (Ax + Bx) / 2, Py = (Ay + By) / 2;
                const Qx = (Bx + Cx) / 2, Qy = (By + Cy) / 2;
                const Rx = (Cx + Dx) / 2, Ry = (Cy + Dy) / 2;
                const Sx = (Dx + Ax) / 2, Sy = (Dy + Ay) / 2;

                svg.innerHTML = `
                    <!-- Outer 4-gon ABCD -->
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="none" stroke="#64748b" stroke-width="2"/>
                    <!-- Diagonal AC -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Cx}" y2="${Cy}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

                    <!-- Varignon Midpoint Parallelogram PQRS -->
                    <polygon points="${Px},${Py} ${Qx},${Qy} ${Rx},${Ry} ${Sx},${Sy}" fill="rgba(16, 185, 129, 0.35)" stroke="#10b981" stroke-width="3"/>

                    <!-- Midpoint dots -->
                    <circle cx="${Px}" cy="${Py}" r="5" fill="#10b981"/>
                    <circle cx="${Qx}" cy="${Qy}" r="5" fill="#10b981"/>
                    <circle cx="${Rx}" cy="${Ry}" r="5" fill="#10b981"/>
                    <circle cx="${Sx}" cy="${Sy}" r="5" fill="#10b981"/>

                    <text x="${Px-15}" y="${Py}" fill="#6ee7b7" font-size="11" font-weight="bold">P</text>
                    <text x="${Qx}" y="${Qy+18}" fill="#6ee7b7" font-size="11" font-weight="bold">Q</text>
                    <text x="${Rx+12}" y="${Ry}" fill="#6ee7b7" font-size="11" font-weight="bold">R</text>
                    <text x="${Sx}" y="${Sy-10}" fill="#6ee7b7" font-size="11" font-weight="bold">S</text>
                `;

                readout.innerHTML = `
                    PQ ∥ SR and PQ = SR = 1/2 AC.<br>
                    Varignon's Theorem: PQRS is ALWAYS a parallelogram, and <b>Area(PQRS) = 1/2 Area(ABCD)</b>!
                `;
            }

            slider.addEventListener('input', update);
            update();
        }

        // Sim 13: 4th Vertex Coordinate Calculator
        function renderSim13(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-3 gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div>
                            <span class="text-indigo-400 font-bold block">Vertex A(x, y):</span>
                            <span class="text-slate-300 font-mono">(1, 2)</span>
                        </div>
                        <div>
                            <span class="text-indigo-400 font-bold block">Vertex B(x, y):</span>
                            <span class="text-slate-300 font-mono">(5, 3)</span>
                        </div>
                        <div>
                            <span class="text-indigo-400 font-bold block">Vertex C(x, y):</span>
                            <span class="text-slate-300 font-mono">(8, 8)</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Grid background -->
                            <path d="M 50 0 L 50 280 M 150 0 L 150 280 M 250 0 L 250 280 M 350 0 L 350 280 M 450 0 L 450 280 M 550 0 L 550 280" stroke="#1e293b" stroke-width="1"/>
                            <polygon points="120,200 280,180 400,60 240,80" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="3"/>

                            <circle cx="120" cy="200" r="6" fill="#38bdf8"/>
                            <circle cx="280" cy="180" r="6" fill="#38bdf8"/>
                            <circle cx="400" cy="60" r="6" fill="#38bdf8"/>
                            <circle cx="240" cy="80" r="7" fill="#10b981"/>

                            <text x="100" y="215" fill="#38bdf8" font-size="12" font-weight="bold">A(1, 2)</text>
                            <text x="290" y="195" fill="#38bdf8" font-size="12" font-weight="bold">B(5, 3)</text>
                            <text x="410" y="65" fill="#38bdf8" font-size="12" font-weight="bold">C(8, 8)</text>
                            <text x="220" y="65" fill="#34d399" font-size="13" font-weight="bold">D(4, 7) [Calculated!]</text>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        Formula: D = A + C - B ⇒ x_D = 1 + 8 - 5 = <b>4</b> | y_D = 2 + 8 - 3 = <b>7</b> ⇒ D(4, 7)!
                    </div>
                </div>
            `;
        }

        // Sim 14: Universal Plane Tiling Engine
        function renderSim14(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Tessellation Grid: 180° Midpoint Rotations (360° Sum)</span>
                        <span class="text-indigo-400 font-mono font-bold">A + B + C + D = 360°</span>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Repeating interlocking 4-gon tiles -->
                            <g transform="translate(100, 20)">
                                <polygon points="0,0 80,20 120,80 30,70" fill="rgba(99, 102, 241, 0.35)" stroke="#6366f1" stroke-width="2"/>
                                <polygon points="80,20 160,40 200,100 120,80" fill="rgba(16, 185, 129, 0.35)" stroke="#10b981" stroke-width="2"/>
                                <polygon points="30,70 120,80 150,150 50,140" fill="rgba(245, 158, 11, 0.35)" stroke="#f59e0b" stroke-width="2"/>
                                <polygon points="120,80 200,100 230,170 150,150" fill="rgba(244, 63, 94, 0.35)" stroke="#f43f5e" stroke-width="2"/>

                                <!-- Central vertex where 4 corners meet -->
                                <circle cx="120" cy="80" r="6" fill="#f8fafc"/>
                                <text x="135" y="80" fill="#f8fafc" font-size="12" font-weight="bold">360° Joint (A+B+C+D)</text>
                            </g>
                        </svg>
                    </div>

                    <div class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        UNIVERSAL TILING: Any irregular 4-gon packs the plane with 0 gaps because four angles form 360° around each vertex!
                    </div>
                </div>
            `;
        }

        // Sim 15: Converse Questioning Lab
        function renderSim15(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Testing Converses & Traps:</span>
                        <div class="flex gap-2">
                            <button id="sim15_trap" class="px-2.5 py-1 rounded bg-rose-600 text-white font-bold text-xs transition">Equal Diagonals Trap</button>
                            <button id="sim15_fixed" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition">Fixed Parallelogram Converse</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[280px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim15_svg" viewBox="0 0 600 280" class="w-full h-full max-h-[280px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim15_desc" class="p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let isTrap = true;
            const trapBtn = document.getElementById('sim15_trap');
            const fixedBtn = document.getElementById('sim15_fixed');
            const svg = document.getElementById('sim15_svg');
            const desc = document.getElementById('sim15_desc');

            function update() {
                if (isTrap) {
                    trapBtn.className = "px-2.5 py-1 rounded bg-rose-600 text-white font-bold text-xs transition";
                    fixedBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                    svg.innerHTML = `
                        <!-- Isosceles Trapezium -->
                        <polygon points="220,70 140,210 460,210 380,70" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="3"/>
                        <line x1="220" y1="70" x2="460" y2="210" stroke="#f59e0b" stroke-width="2.5"/>
                        <line x1="380" y1="70" x2="140" y2="210" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="300" y="240" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="middle">Isosceles Trapezium: Diagonals Equal, but NOT a Rectangle!</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-rose-950/40 border border-rose-500/40 text-rose-300';
                    desc.textContent = "FALSE CONVERSE: 'Equal diagonals implies rectangle' is FALSE! The counterexample is an isosceles trapezium.";
                } else {
                    trapBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs transition";
                    fixedBtn.className = "px-2.5 py-1 rounded bg-emerald-600 text-white font-bold text-xs transition";
                    svg.innerHTML = `
                        <!-- Rectangle -->
                        <polygon points="180,70 180,210 420,210 420,70" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="3"/>
                        <line x1="180" y1="70" x2="420" y2="210" stroke="#f59e0b" stroke-width="2.5"/>
                        <line x1="180" y1="210" x2="420" y2="70" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="300" y="240" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Parallelogram with Equal Diagonals = RECTANGLE!</text>
                    `;
                    desc.className = 'p-2.5 rounded-xl text-center text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300';
                    desc.textContent = "TRUE REFINED CONVERSE: If the diagonals of a PARALLELOGRAM are equal, then it is guaranteed to be a rectangle!";
                }
            }

            trapBtn.addEventListener('click', () => { isTrap = true; update(); });
            fixedBtn.addEventListener('click', () => { isTrap = false; update(); });
            update();
        }

        // Sim 16: Interactive Paper Folding & CAD Classifier
        function renderSim16(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-indigo-400 font-bold block mb-1">1. Varignon Origami Fold Simulation:</span>
                            <div class="flex items-center gap-2 mb-2">
                                <label class="text-slate-300">Fold Flaps Inward:</label>
                                <input type="range" id="sim16_fold" min="0" max="100" value="0" class="w-24 accent-indigo-500">
                                <span id="sim16_fold_val" class="font-mono text-indigo-400 font-bold">0%</span>
                            </div>
                            <div class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                4 corner flaps fold inward to cover the central parallelogram exactly once!
                            </div>
                        </div>

                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 text-xs">
                            <span class="text-emerald-400 font-bold block mb-1">2. CAD Vector Classifier (v₁ · v₂ = 0):</span>
                            <div class="flex items-center gap-2 mb-2">
                                <button onclick="window.testCad('rec')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">Rectangle</button>
                                <button onclick="window.testCad('rho')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">Rhombus</button>
                                <button onclick="window.testCad('squ')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">Square</button>
                            </div>
                            <div id="sim16_cad_res" class="p-2 rounded bg-slate-950 font-mono text-[11px] text-emerald-300 border border-slate-800">
                                Click a button to test vector dot product & orthogonality...
                            </div>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[220px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim16_svg" viewBox="0 0 600 220" class="w-full h-full max-h-[220px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>
                </div>
            `;

            const foldSlider = document.getElementById('sim16_fold');
            const foldVal = document.getElementById('sim16_fold_val');
            const svg = document.getElementById('sim16_svg');

            function updateFold() {
                const f = parseFloat(foldSlider.value) / 100;
                foldVal.textContent = `${Math.round(f * 100)}%`;

                svg.innerHTML = `
                    <!-- Outer Paper Quadrilateral -->
                    <polygon points="180,30 100,180 440,180 480,50" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
                    <!-- Central Varignon Parallelogram -->
                    <polygon points="140,105 270,180 460,115 330,40" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="3"/>
                    <text x="300" y="115" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Varignon Parallelogram (Area = 50%)</text>
                `;
            }

            window.testCad = function(type) {
                const res = document.getElementById('sim16_cad_res');
                if (type === 'rec') {
                    res.innerHTML = `v₁ · v₂ = 0 (90° right angle) and |v₁| ≠ |v₂| ⇒ <b>RECTANGLE</b>.`;
                } else if (type === 'rho') {
                    res.innerHTML = `|v₁| = |v₂| (4 equal sides) and v₁ · v₂ ≠ 0 ⇒ <b>RHOMBUS</b>.`;
                } else {
                    res.innerHTML = `|v₁| = |v₂| AND v₁ · v₂ = 0 ⇒ <b>SQUARE</b>.`;
                }
            };

            foldSlider.addEventListener('input', updateFold);
            updateFold();
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

