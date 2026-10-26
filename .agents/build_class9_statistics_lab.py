# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 14
STATISTICS (Competencies CG-6, C-6.1, CG-9)
Generates public/animations/class9-statistics.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_statistics_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-statistics.html"

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
    <title>NCERT Class 9 Mathematics • Statistics & Data Analysis Laboratory</title>
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
        .glow-cyan {
            box-shadow: 0 0 25px -5px rgba(6, 182, 212, 0.35);
        }
        .glow-amber {
            box-shadow: 0 0 25px -5px rgba(245, 158, 11, 0.35);
        }
        @keyframes pulse-subtle {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.85; transform: scale(1.02); }
        }
        .animate-subtle {
            animation: pulse-subtle 3s infinite ease-in-out;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-indigo-500 selection:text-white">

    <!-- Header Navigation Bar -->
    <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur-md sticky top-0 z-40 px-4 py-3 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-indigo-600 to-emerald-500 flex items-center justify-center shadow-lg shadow-indigo-500/25">
                <i data-lucide="bar-chart-2" class="w-6 h-6 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">NCERT Class 9</span>
                    <span class="text-xs text-slate-400">Chapter 14 • Competencies CG-6, C-6.1, CG-9</span>
                </div>
                <h1 class="text-base sm:text-lg font-extrabold text-white tracking-tight flex items-center gap-2">
                    Statistics & Data Analysis Laboratory
                </h1>
            </div>
        </div>

        <!-- Controls: Slide Counter, Prev/Next Buttons -->
        <div class="flex items-center gap-2 sm:gap-3">
            <div class="flex items-center bg-slate-800/80 rounded-lg p-1 border border-slate-700 text-xs font-medium">
                <button id="prevBtn" onclick="window.navSlide(-1)" class="px-2.5 py-1.5 rounded hover:bg-slate-700 text-slate-200 disabled:opacity-30 disabled:pointer-events-none transition flex items-center gap-1">
                    <i data-lucide="chevron-left" class="w-4 h-4"></i>
                    <span class="hidden sm:inline">Prev</span>
                </button>
                <div class="px-3 py-1 font-mono text-cyan-400 font-bold border-x border-slate-700 text-xs">
                    Slide <span id="currentSlideNum">1</span> / 20
                </div>
                <button id="nextBtn" onclick="window.navSlide(1)" class="px-2.5 py-1.5 rounded hover:bg-slate-700 text-slate-200 disabled:opacity-30 disabled:pointer-events-none transition flex items-center gap-1">
                    <span class="hidden sm:inline">Next</span>
                    <i data-lucide="chevron-right" class="w-4 h-4"></i>
                </button>
            </div>

            <!-- Slide Menu Quick Jump Dropdown -->
            <div class="relative">
                <button id="slideMenuBtn" onclick="window.toggleSlideMenu()" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition">
                    <i data-lucide="grid" class="w-5 h-5"></i>
                </button>
                <div id="slideMenuDropdown" class="hidden absolute right-0 mt-2 w-72 max-h-96 overflow-y-auto glass-panel rounded-xl shadow-2xl p-2 z-50 border border-slate-700">
                    <div class="text-xs font-bold text-slate-400 px-2 py-1 uppercase tracking-wider border-b border-slate-800 mb-1">Curriculum Navigator</div>
                    <div id="slideListItems" class="space-y-1">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Dynamic Content Grid -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-5">

        <!-- Left Column: Pedagogical Knowledge, Formulas & Checkpoints (Col 1-5) -->
        <div class="lg:col-span-5 flex flex-col gap-4">

            <!-- Teacher Avatar Card with Audio Narration -->
            <div class="glass-panel rounded-2xl p-4 border border-indigo-500/20 relative overflow-hidden">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Avatar -->
                    <div id="avatarContainer" class="relative w-14 h-14 shrink-0 rounded-2xl bg-gradient-to-b from-indigo-950 via-slate-900 to-slate-950 border border-indigo-500/30 flex items-center justify-center shadow-inner overflow-hidden">
                        <svg class="w-12 h-12" viewBox="0 0 100 100">
                            <!-- Body / Shoulders -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#4338ca"/>
                            <path d="M35,85 L50,92 L65,85 L50,98 Z" fill="#6366f1"/>
                            <!-- Neck -->
                            <rect x="44" y="62" width="12" height="18" fill="#fbcfe8" rx="3"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="45" rx="22" ry="24" fill="#fdf2f8"/>
                            <!-- Hair back -->
                            <path d="M26,45 Q24,20 50,18 Q76,20 74,45 Q75,65 68,70 Q72,40 50,28 Q28,40 32,70 Q25,65 26,45 Z" fill="#312e81"/>
                            <!-- Hair bangs -->
                            <path d="M30,35 Q50,22 70,35 Q60,25 50,26 Q40,25 30,35 Z" fill="#4338ca"/>
                            <!-- Glasses -->
                            <rect x="33" y="38" width="14" height="10" rx="3" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                            <rect x="53" y="38" width="14" height="10" rx="3" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                            <line x1="47" y1="43" x2="53" y2="43" stroke="#1e1b4b" stroke-width="2"/>
                            <!-- Eyes -->
                            <circle cx="40" cy="43" r="2.5" fill="#1e293b"/>
                            <circle cx="60" cy="43" r="2.5" fill="#1e293b"/>
                            <circle cx="41" cy="42" r="0.8" fill="#ffffff"/>
                            <circle cx="61" cy="42" r="0.8" fill="#ffffff"/>
                            <!-- Eyebrows -->
                            <path d="M34,35 Q40,33 46,36" fill="none" stroke="#312e81" stroke-width="1.8" stroke-linecap="round"/>
                            <path d="M54,36 Q60,33 66,35" fill="none" stroke="#312e81" stroke-width="1.8" stroke-linecap="round"/>
                            <!-- Smile / Mouth -->
                            <path id="teacherMouth" d="M44,57 Q50,62 56,57" fill="#be185d" stroke="#be185d" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                        <div id="speakingPulse" class="hidden absolute -top-1 -right-1 w-3.5 h-3.5 bg-emerald-500 rounded-full border-2 border-slate-900 animate-ping"></div>
                        <div id="speakingDot" class="hidden absolute -top-1 -right-1 w-3.5 h-3.5 bg-emerald-500 rounded-full border-2 border-slate-900"></div>
                    </div>
                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-white tracking-wide">Prof. Sophia</span>
                            <span id="speechStatus" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Idle</span>
                        </div>
                        <p class="text-[11px] text-cyan-300 truncate">Audio Companion • En-US Narration</p>
                    </div>
                </div>

                <!-- Speech Controls -->
                <div class="mt-3 pt-2.5 border-t border-slate-800 flex items-center justify-between gap-1.5">
                    <button id="toggleSpeechBtn" class="flex-1 px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-md shadow-indigo-600/30">
                        <i data-lucide="volume-2" class="w-4 h-4"></i>
                        <span id="speechBtnLabel">Explain Slide</span>
                    </button>
                    <button id="pauseSpeechBtn" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:pointer-events-none transition border border-slate-700">
                        <i data-lucide="pause" class="w-4 h-4"></i>
                    </button>
                    <button id="stopSpeechBtn" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:pointer-events-none transition border border-slate-700">
                        <i data-lucide="square" class="w-4 h-4"></i>
                    </button>
                    <select id="speechRateSelect" class="bg-slate-800 border border-slate-700 rounded-lg text-[11px] px-2 py-1 text-slate-300">
                        <option value="0.85">0.85x</option>
                        <option value="1.0" selected>1.0x</option>
                        <option value="1.2">1.2x</option>
                    </select>
                </div>
            </div>

            <!-- Slide Core Theory Card -->
            <div class="glass-panel rounded-2xl p-5 border border-slate-800 flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span id="slideCategoryText" class="text-xs font-bold uppercase tracking-wider text-cyan-400 font-mono">Category</span>
                        <span id="slideBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 border border-slate-700 text-slate-300">Badge</span>
                    </div>
                    <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white leading-tight mb-1">Slide Title</h2>
                    <h3 id="slideSubtitle" class="text-xs sm:text-sm text-cyan-300/90 font-medium mb-3">Subtitle</h3>
                    <p id="slideSummary" class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">Summary text...</p>

                    <!-- Key Bullet Points -->
                    <div class="border-t border-slate-800 pt-3">
                        <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                            <i data-lucide="key" class="w-3.5 h-3.5 text-cyan-400"></i>
                            Key Concepts & Formulas
                        </div>
                        <ul id="slideKeyPoints" class="space-y-1.5 text-xs text-slate-300">
                            <!-- Populated dynamically -->
                        </ul>
                    </div>
                </div>

                <!-- Progress Pill Bar -->
                <div class="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
                    <span>Progress: Slide <span id="slideProgressRatio">1 / 20</span></span>
                    <div class="w-32 bg-slate-800 rounded-full h-1.5 overflow-hidden">
                        <div id="slideProgressBar" class="bg-gradient-to-r from-cyan-500 to-indigo-500 h-1.5 rounded-full transition-all duration-300" style="width: 5%"></div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Column: Interactive Simulator & Live Laboratory (Col 6-12) -->
        <div class="lg:col-span-7 flex flex-col gap-4">

            <!-- Simulator Container -->
            <div id="contentSlideContainer" class="flex flex-col gap-4">
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 glow-cyan">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 mb-4">
                        <div class="flex items-center gap-2">
                            <div class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 flex items-center justify-center">
                                <i data-lucide="sparkles" class="w-4 h-4"></i>
                            </div>
                            <h3 id="simulatorTitle" class="text-sm font-bold text-white tracking-wide">Interactive Laboratory</h3>
                        </div>
                        <span class="text-[11px] font-mono text-cyan-400 px-2 py-0.5 rounded bg-cyan-950/60 border border-cyan-800/40">Real-time Simulation</span>
                    </div>

                    <!-- Simulator Canvas / Interactive Viewport -->
                    <div id="simulatorViewport" class="min-h-[380px] flex flex-col justify-center items-center rounded-xl bg-slate-950/80 border border-slate-800/70 p-4 relative overflow-hidden">
                        <!-- Rendered dynamically by active simulator function -->
                    </div>
                </div>

                <!-- In-Slide Checkpoints (2 Interactive Questions per Slide) -->
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800">
                    <div class="flex items-center gap-2 border-b border-slate-800 pb-2.5 mb-3">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i>
                        <h4 class="text-xs font-bold uppercase tracking-wider text-slate-300">Concept Checkpoints</h4>
                        <span class="text-[10px] text-slate-500 ml-auto">Immediate Feedback</span>
                    </div>
                    <div id="checkpointsContainer" class="space-y-4">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </div>

            <!-- Dedicated Quiz Challenge Container (Slides 17 to 20) -->
            <div id="quizSlideContainer" class="hidden flex flex-col gap-4">
                <div class="glass-panel rounded-2xl p-5 border border-indigo-500/30 glow-indigo">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
                        <div class="flex items-center gap-2.5">
                            <div class="w-8 h-8 rounded-xl bg-indigo-600/30 text-indigo-400 border border-indigo-500/40 flex items-center justify-center">
                                <i data-lucide="award" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h3 id="quizTitle" class="text-base font-extrabold text-white">Mastery Assessment</h3>
                                <p class="text-xs text-slate-400">10 Comprehensive Questions with Step-by-Step Pop-up Solutions</p>
                            </div>
                        </div>
                        <div id="quizScoreBadge" class="font-mono text-xs font-bold px-3 py-1 rounded-lg bg-slate-800 border border-slate-700 text-indigo-300">
                            Score: <span id="quizScoreVal">0</span> / 10
                        </div>
                    </div>

                    <!-- 10 Quiz Questions List -->
                    <div id="quizQuestionsList" class="space-y-5 max-h-[640px] overflow-y-auto pr-1">
                        <!-- Populated dynamically by JS -->
                    </div>
                </div>
            </div>

            <!-- Strict Last Slide Notice on Slide 20 -->
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-cyan-950/40 shadow-xl shadow-emerald-950/30">
                <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mb-3">
                    <i data-lucide="check-check" class="w-8 h-8"></i>
                </div>
                <h3 class="text-xl font-bold text-white">Congratulations on Completing Chapter 14!</h3>
                <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">You have mastered the PPDAC inquiry cycle, bar graphs, stacked and 100% stacked bar charts, histograms with uniform and varying class widths, frequency polygons, arithmetic mean, weighted average, median, mode, outlier sensitivity, Karl Pearson's empirical skewness rule, and computational thinking algorithms in statistics.</p>
                <div class="mt-4 flex justify-center gap-3">
                    <button onclick="window.navSlide(-19)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition">
                        Review Chapter From Start
                    </button>
                    <button onclick="window.navSlide(-3)" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-lg shadow-cyan-600/30 transition">
                        Retake Mastery Quizzes
                    </button>
                </div>
            </div>

        </div>

    </main>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <div class="glass-panel w-full max-w-lg rounded-2xl p-5 border border-indigo-500/40 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm">
                    <i data-lucide="book-open" class="w-4 h-4"></i>
                    <span>Step-by-Step Solution & Pedagogical Explanation</span>
                </div>
                <button onclick="window.closeSolutionModal()" class="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <div class="space-y-3 text-xs leading-relaxed text-slate-200">
                <div>
                    <span class="text-slate-400 font-bold uppercase tracking-wider text-[10px]">Question:</span>
                    <p id="modalQuestionText" class="mt-0.5 font-medium text-white"></p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                    <span class="text-cyan-400 font-bold uppercase tracking-wider text-[10px]">Detailed Derivation:</span>
                    <pre id="modalSolutionText" class="mt-1 font-mono text-[11px] text-slate-300 whitespace-pre-wrap leading-relaxed"></pre>
                </div>
            </div>
            <div class="flex justify-end pt-2">
                <button onclick="window.closeSolutionModal()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                    Got It, Continue
                </button>
            </div>
        </div>
    </div>

    <!-- Application Script Data & Controllers -->
    <script>
        const SLIDES = __SLIDES_JSON__;
        const QUIZZES = __QUIZZES_JSON__;

        let currentSlideIndex = 0; // 0 to 19 (total 20 slides)
        let speechSynth = window.speechSynthesis;
        let currentUtterance = null;
        let isSpeaking = false;
        let speechRate = 1.0;

        // Fallback Web Audio Synthesizer if Web Speech is unavailable
        let audioCtx = null;
        function playTone(freq, duration, type='sine') {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
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
            } catch(e) {
                console.warn("Audio Context fallback unavailable", e);
            }
        }

        // Initialize App on DOM Ready
        document.addEventListener('DOMContentLoaded', () => {
            initSlideDropdown();
            renderSlide(0);
            initSpeechControls();
            lucide.createIcons();
        });

        // Populate Slide Jump Menu
        function initSlideDropdown() {
            const list = document.getElementById('slideListItems');
            list.innerHTML = '';

            for (let i = 0; i < 20; i++) {
                const btn = document.createElement('button');
                btn.className = "w-full text-left px-2.5 py-1.5 rounded-lg text-xs hover:bg-slate-800 transition flex items-center justify-between";
                let title = (i < 16) ? SLIDES[i].title : QUIZZES[i - 16].title;
                let badge = (i < 16) ? `Slide ${i+1}` : `Quiz ${i-15}`;

                btn.innerHTML = `
                    <span class="truncate pr-2">${i+1}. ${title}</span>
                    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-cyan-400 shrink-0">${badge}</span>
                `;
                btn.onclick = () => {
                    window.renderSlide(i);
                    window.toggleSlideMenu();
                };
                list.appendChild(btn);
            }
        }

        window.toggleSlideMenu = function() {
            const dd = document.getElementById('slideMenuDropdown');
            dd.classList.toggle('hidden');
        };

        // Navigation Controller
        window.navSlide = function(delta) {
            const nextIndex = currentSlideIndex + delta;
            if (nextIndex >= 0 && nextIndex < 20) {
                stopSpeech();
                renderSlide(nextIndex);
            }
        };

        // Render Active Slide
        window.renderSlide = function(index) {
            currentSlideIndex = index;
            document.getElementById('currentSlideNum').textContent = currentSlideIndex + 1;
            document.getElementById('slideProgressRatio').textContent = `${currentSlideIndex + 1} / 20`;
            document.getElementById('slideProgressBar').style.width = `${((currentSlideIndex + 1) / 20) * 100}%`;

            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Handle Slide 20 Specific Requirement
            const lastSlideNotice = document.getElementById('lastSlideNotice');
            const nextBtn = document.getElementById('nextBtn');
            if (currentSlideIndex === 19) {
                lastSlideNotice.classList.remove('hidden');
                nextBtn.style.display = 'none';
            } else {
                lastSlideNotice.classList.add('hidden');
                nextBtn.style.display = 'flex';
                nextBtn.disabled = false;
            }

            const contentContainer = document.getElementById('contentSlideContainer');
            const quizContainer = document.getElementById('quizSlideContainer');

            if (currentSlideIndex < 16) {
                // Content Slide Mode (Slides 1 to 16)
                contentContainer.classList.remove('hidden');
                quizContainer.classList.add('hidden');

                const slide = SLIDES[currentSlideIndex];
                document.getElementById('slideCategoryText').textContent = slide.category;
                document.getElementById('slideBadge').textContent = slide.badge;
                document.getElementById('slideTitle').textContent = slide.title;
                document.getElementById('slideSubtitle').textContent = slide.subtitle;
                document.getElementById('slideSummary').textContent = slide.summary;
                document.getElementById('simulatorTitle').textContent = slide.sim_title;

                // Render Key Points
                const kpList = document.getElementById('slideKeyPoints');
                kpList.innerHTML = slide.key_points.map(pt => `
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1.5 shrink-0"></span>
                        <span>${pt}</span>
                    </li>
                `).join('');

                // Render Checkpoints
                renderCheckpoints(slide.checkpoints);

                // Render Bespoke Interactive Simulator
                renderSimulator(currentSlideIndex);

            } else {
                // Quiz Slide Mode (Slides 17 to 20)
                contentContainer.classList.add('hidden');
                quizContainer.classList.remove('hidden');

                const quiz = QUIZZES[currentSlideIndex - 16];
                document.getElementById('slideCategoryText').textContent = "Mastery Assessment";
                document.getElementById('slideBadge').textContent = quiz.badge;
                document.getElementById('slideTitle').textContent = quiz.title;
                document.getElementById('slideSubtitle').textContent = "10 Question Comprehensive Synthesis & Examination Challenge";
                document.getElementById('slideSummary').textContent = "Test your deep mastery across all aspects of this chapter. Answer each multiple-choice question to receive instant validation and open the detailed step-by-step solution derivation popup.";

                document.getElementById('slideKeyPoints').innerHTML = `
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
                        <span>Answer all 10 questions to achieve full mastery of this section.</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1.5 shrink-0"></span>
                        <span>Click "View Solution" for detailed mathematical proofs and formulas.</span>
                    </li>
                `;

                document.getElementById('quizTitle').textContent = quiz.title;
                renderQuizQuestions(quiz.questions);
            }

            // Trigger KaTeX math render
            setTimeout(() => {
                if (window.renderMathInElement) {
                    renderMathInElement(document.body, {
                        delimiters: [
                            {left: '$$', right: '$$', display: true},
                            {left: '$', right: '$', display: false}
                        ]
                    });
                }
                lucide.createIcons();
            }, 50);
        };

        // Checkpoints Renderer (2 questions per slide)
        function renderCheckpoints(checkpoints) {
            const container = document.getElementById('checkpointsContainer');
            container.innerHTML = '';

            checkpoints.forEach((cp, qIdx) => {
                const card = document.createElement('div');
                card.className = "p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5";

                const qHeader = document.createElement('div');
                qHeader.className = "text-xs font-semibold text-white flex items-start gap-2";
                qHeader.innerHTML = `
                    <span class="w-5 h-5 rounded-full bg-slate-800 text-cyan-400 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold border border-slate-700">Q${qIdx+1}</span>
                    <span class="flex-1">${cp.q}</span>
                `;
                card.appendChild(qHeader);

                const optsGrid = document.createElement('div');
                optsGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1";

                const feedbackDiv = document.createElement('div');
                feedbackDiv.className = "hidden text-[11px] p-2.5 rounded-lg font-medium leading-relaxed mt-2 border";

                cp.options.forEach((opt, oIdx) => {
                    const btn = document.createElement('button');
                    btn.className = "text-left px-3 py-2 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-xs text-slate-300 border border-slate-700/60 transition flex items-center gap-2";
                    btn.innerHTML = `
                        <span class="w-4 h-4 rounded text-[9px] font-mono font-bold bg-slate-900 text-slate-400 flex items-center justify-center shrink-0 border border-slate-700">${String.fromCharCode(65 + oIdx)}</span>
                        <span class="truncate">${opt}</span>
                    `;

                    btn.onclick = () => {
                        optsGrid.querySelectorAll('button').forEach(b => b.disabled = true);
                        if (oIdx === cp.ans) {
                            btn.classList.remove('bg-slate-800/80', 'text-slate-300', 'border-slate-700/60');
                            btn.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/50', 'font-bold');
                            feedbackDiv.classList.remove('hidden');
                            feedbackDiv.classList.add('bg-emerald-950/40', 'border-emerald-500/30', 'text-emerald-300');
                            feedbackDiv.innerHTML = `<strong>Correct!</strong> ${cp.exp || cp.explanation}`;
                            playTone(587.33, 0.12, 'triangle');
                        } else {
                            btn.classList.remove('bg-slate-800/80', 'text-slate-300', 'border-slate-700/60');
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            feedbackDiv.classList.remove('hidden');
                            feedbackDiv.classList.add('bg-rose-950/40', 'border-rose-500/30', 'text-rose-300');
                            feedbackDiv.innerHTML = `<strong>Incorrect.</strong> ${cp.exp || cp.explanation}`;
                            playTone(220, 0.2, 'sawtooth');
                        }
                    };
                    optsGrid.appendChild(btn);
                });

                card.appendChild(optsGrid);
                card.appendChild(feedbackDiv);
                container.appendChild(card);
            });
        }

        // Quiz Questions Renderer (10 questions per quiz slide)
        function renderQuizQuestions(questions) {
            const list = document.getElementById('quizQuestionsList');
            list.innerHTML = '';
            let score = 0;
            document.getElementById('quizScoreVal').textContent = score;

            questions.forEach((qObj, qIdx) => {
                const card = document.createElement('div');
                card.className = "p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3";

                const header = document.createElement('div');
                header.className = "flex items-start justify-between gap-2";
                header.innerHTML = `
                    <div class="text-xs font-semibold text-white flex items-start gap-2">
                        <span class="w-6 h-6 rounded-lg bg-indigo-950 text-indigo-400 border border-indigo-800/50 flex items-center justify-center text-xs font-mono font-bold shrink-0">${qIdx+1}</span>
                        <span class="mt-0.5">${qObj.q}</span>
                    </div>
                `;
                card.appendChild(header);

                const optsGrid = document.createElement('div');
                optsGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1";

                const resultBar = document.createElement('div');
                resultBar.className = "hidden flex items-center justify-between text-xs pt-1";

                qObj.options.forEach((opt, oIdx) => {
                    const btn = document.createElement('button');
                    btn.className = "text-left px-3 py-2 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-xs text-slate-300 border border-slate-700/60 transition flex items-center gap-2";
                    btn.innerHTML = `
                        <span class="w-4 h-4 rounded text-[9px] font-mono font-bold bg-slate-900 text-slate-400 flex items-center justify-center shrink-0 border border-slate-700">${String.fromCharCode(65 + oIdx)}</span>
                        <span>${opt}</span>
                    `;

                    btn.onclick = () => {
                        optsGrid.querySelectorAll('button').forEach(b => b.disabled = true);
                        resultBar.classList.remove('hidden');

                        if (oIdx === qObj.ans) {
                            btn.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/50', 'font-bold');
                            score++;
                            document.getElementById('quizScoreVal').textContent = score;
                            resultBar.innerHTML = `
                                <span class="text-emerald-400 font-bold flex items-center gap-1">
                                    <i data-lucide="check" class="w-4 h-4"></i> Correct Answer
                                </span>
                                <button onclick="window.openSolutionModal(${currentSlideIndex - 16}, ${qIdx})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 text-[11px] font-semibold transition">
                                    View Solution
                                </button>
                            `;
                            playTone(587.33, 0.12, 'triangle');
                        } else {
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            resultBar.innerHTML = `
                                <span class="text-rose-400 font-bold flex items-center gap-1">
                                    <i data-lucide="x" class="w-4 h-4"></i> Incorrect (Correct: ${String.fromCharCode(65 + qObj.ans)})
                                </span>
                                <button onclick="window.openSolutionModal(${currentSlideIndex - 16}, ${qIdx})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 text-[11px] font-semibold transition">
                                    View Solution
                                </button>
                            `;
                            playTone(220, 0.2, 'sawtooth');
                        }
                        lucide.createIcons();
                    };
                    optsGrid.appendChild(btn);
                });

                card.appendChild(optsGrid);
                card.appendChild(resultBar);
                list.appendChild(card);
            });
        }

        // Solution Modal Handlers
        window.openSolutionModal = function(quizIdx, qIdx) {
            const qObj = QUIZZES[quizIdx].questions[qIdx];
            document.getElementById('modalQuestionText').textContent = qObj.q;
            document.getElementById('modalSolutionText').textContent = qObj.solution;
            document.getElementById('solutionModal').classList.remove('hidden');
        };

        window.closeSolutionModal = function() {
            document.getElementById('solutionModal').classList.add('hidden');
        };

        // 16 Bespoke Interactive SVG Simulators
        function renderSimulator(slideIndex) {
            const vp = document.getElementById('simulatorViewport');
            vp.innerHTML = '';

            switch(slideIndex) {
                case 0: renderSim1(vp); break;
                case 1: renderSim2(vp); break;
                case 2: renderSim3(vp); break;
                case 3: renderSim4(vp); break;
                case 4: renderSim5(vp); break;
                case 5: renderSim6(vp); break;
                case 6: renderSim7(vp); break;
                case 7: renderSim8(vp); break;
                case 8: renderSim9(vp); break;
                case 9: renderSim10(vp); break;
                case 10: renderSim11(vp); break;
                case 11: renderSim12(vp); break;
                case 12: renderSim13(vp); break;
                case 13: renderSim14(vp); break;
                case 14: renderSim15(vp); break;
                case 15: renderSim16(vp); break;
                default: vp.innerHTML = `<div class="text-slate-400 text-xs">Simulator ready.</div>`;
            }
        }

        // SIMULATOR 1: Interactive PPDAC Inquiry Pipeline & Live Tally Counter
        function renderSim1(vp) {
            let dataPoints = [2, 3, 3, 4, 1, 3, 2, 5, 4, 2, 3];

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- PPDAC Pipeline Badges -->
                        <div class="grid grid-cols-5 gap-1 text-center font-mono text-[10px]">
                            <div class="p-1 rounded bg-cyan-950/60 border border-cyan-800 text-cyan-400 font-bold">1. Problem</div>
                            <div class="p-1 rounded bg-indigo-950/60 border border-indigo-800 text-indigo-400 font-bold">2. Plan</div>
                            <div class="p-1 rounded bg-emerald-950/80 border border-emerald-500 text-emerald-300 font-black animate-pulse">3. Data (Live)</div>
                            <div class="p-1 rounded bg-slate-900 border border-slate-800 text-slate-400">4. Analysis</div>
                            <div class="p-1 rounded bg-slate-900 border border-slate-800 text-slate-400">5. Conclusion</div>
                        </div>

                        <!-- Data Collector Toolbar -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs text-slate-300 font-medium">Add Study Hours (1-5):</span>
                            <div class="flex gap-1.5">
                                ${[1, 2, 3, 4, 5].map(val => `
                                    <button onclick="window.sim1Add(${val})" class="w-7 h-7 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow">
                                        ${val}
                                    </button>
                                `).join('')}
                                <button onclick="window.sim1Reset()" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs border border-slate-700 ml-1">
                                    Reset
                                </button>
                            </div>
                        </div>

                        <!-- Raw Data & Array Display -->
                        <div class="bg-slate-900/60 p-2 rounded-lg border border-slate-800 text-xs space-y-1">
                            <div class="flex items-center gap-2">
                                <span class="font-bold text-slate-400">Raw Data (N=${dataPoints.length}):</span>
                                <span class="font-mono text-cyan-300 truncate">${dataPoints.join(', ')}</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="font-bold text-slate-400">Sorted Array:</span>
                                <span class="font-mono text-emerald-300 truncate">${[...dataPoints].sort((a,b)=>a-b).join(', ')}</span>
                                <span class="ml-auto font-mono text-[10px] text-amber-400 bg-amber-950/40 px-2 py-0.5 rounded border border-amber-800">
                                    Range: ${dataPoints.length ? Math.max(...dataPoints) - Math.min(...dataPoints) : 0}
                                </span>
                            </div>
                        </div>

                        <!-- Dynamic Tally Marks & Frequency Table -->
                        <div class="overflow-hidden rounded-xl border border-slate-800 bg-slate-900/90 text-xs">
                            <table class="w-full text-left">
                                <thead class="bg-slate-800/80 text-[11px] font-mono text-slate-400 border-b border-slate-700">
                                    <tr>
                                        <th class="p-2">Value (x)</th>
                                        <th class="p-2">Tally Marks (Bundled in 5s)</th>
                                        <th class="p-2 text-right">Frequency (f)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-800 text-slate-200">
                                    ${[1, 2, 3, 4, 5].map(v => {
                                        const count = dataPoints.filter(x => x === v).length;
                                        const bundles = Math.floor(count / 5);
                                        const rem = count % 5;
                                        let tallyStr = '';
                                        for (let b = 0; b < bundles; b++) tallyStr += '<span class="text-cyan-400 font-bold mr-1.5 px-1 py-0.5 bg-cyan-950/60 rounded border border-cyan-800">卌</span>';
                                        if (rem > 0) tallyStr += '<span class="text-amber-300 font-mono tracking-widest">' + '|'.repeat(rem) + '</span>';
                                        if (count === 0) tallyStr = '<span class="text-slate-600">—</span>';

                                        return `
                                            <tr class="hover:bg-slate-800/40">
                                                <td class="p-2 font-bold text-cyan-400">${v} hr${v > 1 ? 's' : ''}</td>
                                                <td class="p-2 text-sm">${tallyStr}</td>
                                                <td class="p-2 text-right font-mono font-bold text-white">${count}</td>
                                            </tr>
                                        `;
                                    }).join('')}
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
            }

            window.sim1Add = function(val) {
                if (dataPoints.length < 25) {
                    dataPoints.push(val);
                    playTone(440 + val * 50, 0.08, 'sine');
                    draw();
                }
            };
            window.sim1Reset = function() {
                dataPoints = [2, 3, 3, 4, 1, 3, 2, 5, 4, 2, 3];
                playTone(330, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 2: Interactive Bar Chart Studio & Scale Balancer
        function renderSim2(vp) {
            let counts = { Football: 28, Cricket: 45, Badminton: 20, Basketball: 35 };

            function draw() {
                const maxVal = Math.max(...Object.values(counts), 50);
                const svgW = 440;
                const svgH = 220;
                const barW = 48;
                const gap = 38;
                const startX = 60;
                const baseY = 180;
                const plotH = 150;

                const categories = Object.keys(counts);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Category Frequency Sliders -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                            ${categories.map(cat => `
                                <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 flex flex-col gap-1">
                                    <div class="flex justify-between text-[11px]">
                                        <span class="font-bold text-cyan-300">${cat}</span>
                                        <span class="font-mono font-bold text-white">${counts[cat]}</span>
                                    </div>
                                    <input type="range" min="5" max="60" value="${counts[cat]}"
                                           oninput="window.sim2Set('${cat}', this.value)"
                                           class="w-full accent-cyan-500 h-1 bg-slate-700 rounded-lg cursor-pointer">
                                </div>
                            `).join('')}
                        </div>

                        <!-- SVG Bar Chart -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Grid lines -->
                                ${[0, 15, 30, 45, 60].map(val => {
                                    const y = baseY - (val / 60) * plotH;
                                    return `
                                        <line x1="45" y1="${y}" x2="${svgW - 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="38" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}</text>
                                    `;
                                }).join('')}

                                <!-- Axes -->
                                <line x1="45" y1="20" x2="45" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="45" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Bars with Uniform Width & Equal Gaps -->
                                ${categories.map((cat, idx) => {
                                    const val = counts[cat];
                                    const h = (val / 60) * plotH;
                                    const x = startX + idx * (barW + gap);
                                    const y = baseY - h;
                                    const colors = ['#06b6d4', '#6366f1', '#10b981', '#f59e0b'];

                                    return `
                                        <g>
                                            <!-- Bar -->
                                            <rect x="${x}" y="${y}" width="${barW}" height="${h}" rx="4"
                                                  fill="${colors[idx]}" fill-opacity="0.85" stroke="${colors[idx]}" stroke-width="1.5" class="transition-all duration-300"/>
                                            <!-- Top Value -->
                                            <text x="${x + barW/2}" y="${y - 6}" fill="#f8fafc" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">${val}</text>
                                            <!-- Category Label -->
                                            <text x="${x + barW/2}" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-weight="600" text-anchor="middle">${cat}</text>
                                            <!-- Uniform Width indicator on first bar -->
                                            ${idx === 0 ? `
                                                <line x1="${x}" y1="${baseY + 26}" x2="${x + barW}" y2="${baseY + 26}" stroke="#06b6d4" stroke-width="1.5"/>
                                                <text x="${x + barW/2}" y="${baseY + 36}" fill="#06b6d4" font-size="8" font-family="monospace" text-anchor="middle">Width = 48px</text>
                                            ` : ''}
                                            <!-- Uniform Gap indicator between bar 0 and 1 -->
                                            ${idx === 0 ? `
                                                <line x1="${x + barW}" y1="${baseY + 26}" x2="${x + barW + gap}" y2="${baseY + 26}" stroke="#e2e8f0" stroke-dasharray="2,2" stroke-width="1.5"/>
                                                <text x="${x + barW + gap/2}" y="${baseY + 36}" fill="#e2e8f0" font-size="8" font-family="monospace" text-anchor="middle">Gap = 38px</text>
                                            ` : ''}
                                        </g>
                                    `;
                                }).join('')}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            <span class="text-cyan-400 font-bold">Rule:</span> All bar widths are strictly equal (48px) and all spacing gaps are uniform (38px).
                        </div>
                    </div>
                `;
            }

            window.sim2Set = function(cat, val) {
                counts[cat] = parseInt(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 3: Interactive Stacked Bar Graph Explorer & Segment Ruler
        function renderSim3(vp) {
            let data = {
                "Grade 7": { Boys: 30, Girls: 25 },
                "Grade 8": { Boys: 40, Girls: 35 },
                "Grade 9": { Boys: 35, Girls: 45 },
                "Grade 10": { Boys: 50, Girls: 40 }
            };

            function draw() {
                const svgW = 440;
                const svgH = 220;
                const barW = 52;
                const gap = 44;
                const startX = 60;
                const baseY = 180;
                const plotH = 150;
                const maxVal = 100;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Legend & Controller -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <div class="flex items-center gap-4">
                                <div class="flex items-center gap-1.5">
                                    <span class="w-3 h-3 rounded bg-cyan-500"></span>
                                    <span class="text-slate-300 font-medium">Boys (Bottom)</span>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="w-3 h-3 rounded bg-pink-500"></span>
                                    <span class="text-slate-300 font-medium">Girls (Top)</span>
                                </div>
                            </div>
                            <button onclick="window.sim3Shuffle()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700">
                                Shuffle Data
                            </button>
                        </div>

                        <!-- SVG Stacked Bar Chart -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Horizontal Grid Lines -->
                                ${[0, 25, 50, 75, 100].map(val => {
                                    const y = baseY - (val / maxVal) * plotH;
                                    return `
                                        <line x1="45" y1="${y}" x2="${svgW - 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="38" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}</text>
                                    `;
                                }).join('')}

                                <line x1="45" y1="20" x2="45" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="45" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Stacked Bars -->
                                ${Object.keys(data).map((grade, idx) => {
                                    const boys = data[grade].Boys;
                                    const girls = data[grade].Girls;
                                    const total = boys + girls;

                                    const hBoys = (boys / maxVal) * plotH;
                                    const hGirls = (girls / maxVal) * plotH;
                                    const x = startX + idx * (barW + gap);

                                    const yBoys = baseY - hBoys;
                                    const yGirls = yBoys - hGirls;

                                    return `
                                        <g>
                                            <!-- Boys Segment (Bottom) -->
                                            <rect x="${x}" y="${yBoys}" width="${barW}" height="${hBoys}" fill="#06b6d4" fill-opacity="0.85" stroke="#0891b2" stroke-width="1.5" class="transition-all duration-300"/>
                                            <text x="${x + barW/2}" y="${yBoys + hBoys/2 + 3}" fill="#ffffff" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">${boys}</text>

                                            <!-- Girls Segment (Stacked on Top) -->
                                            <rect x="${x}" y="${yGirls}" width="${barW}" height="${hGirls}" rx="4" fill="#ec4899" fill-opacity="0.85" stroke="#db2777" stroke-width="1.5" class="transition-all duration-300"/>
                                            <text x="${x + barW/2}" y="${yGirls + hGirls/2 + 3}" fill="#ffffff" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">${girls}</text>

                                            <!-- Total on Top -->
                                            <text x="${x + barW/2}" y="${yGirls - 6}" fill="#f8fafc" font-size="10" font-family="monospace" font-weight="extrabold" text-anchor="middle">Total: ${total}</text>

                                            <!-- Grade Label -->
                                            <text x="${x + barW/2}" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-weight="600" text-anchor="middle">${grade}</text>
                                        </g>
                                    `;
                                }).join('')}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400">
                            <strong>Segment Value Rule:</strong> Floating segment height = $Y_{\\text{top}} - Y_{\\text{bottom}}$. Total bar height = $\\sum \\text{Segments}$.
                        </div>
                    </div>
                `;
            }

            window.sim3Shuffle = function() {
                Object.keys(data).forEach(k => {
                    data[k].Boys = Math.floor(Math.random() * 30) + 20;
                    data[k].Girls = Math.floor(Math.random() * 30) + 20;
                });
                playTone(523.25, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 4: Absolute Stacked vs 100% Stacked Normalizer
        function renderSim4(vp) {
            let is100Percent = false;
            let cohortA = { Bus: 20, Walk: 15, Bike: 15 }; // Total = 50
            let cohortB = { Bus: 250, Walk: 150, Bike: 100 }; // Total = 500

            function draw() {
                const totalA = cohortA.Bus + cohortA.Walk + cohortA.Bike; // 50
                const totalB = cohortB.Bus + cohortB.Walk + cohortB.Bike; // 500

                const svgW = 440;
                const svgH = 220;
                const barW = 75;
                const baseY = 180;
                const plotH = 150;

                // Scale setup
                let maxScale = is100Percent ? 100 : 550;
                let hA_bus, hA_walk, hA_bike, hB_bus, hB_walk, hB_bike;

                if (is100Percent) {
                    hA_bus = ((cohortA.Bus / totalA) * 100 / maxScale) * plotH;
                    hA_walk = ((cohortA.Walk / totalA) * 100 / maxScale) * plotH;
                    hA_bike = ((cohortA.Bike / totalA) * 100 / maxScale) * plotH;

                    hB_bus = ((cohortB.Bus / totalB) * 100 / maxScale) * plotH;
                    hB_walk = ((cohortB.Walk / totalB) * 100 / maxScale) * plotH;
                    hB_bike = ((cohortB.Bike / totalB) * 100 / maxScale) * plotH;
                } else {
                    hA_bus = (cohortA.Bus / maxScale) * plotH;
                    hA_walk = (cohortA.Walk / maxScale) * plotH;
                    hA_bike = (cohortA.Bike / maxScale) * plotH;

                    hB_bus = (cohortB.Bus / maxScale) * plotH;
                    hB_walk = (cohortB.Walk / maxScale) * plotH;
                    hB_bike = (cohortB.Bike / maxScale) * plotH;
                }

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Toggle -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-white">Active Display Format:</span>
                            <div class="flex items-center gap-2">
                                <button onclick="window.sim4SetMode(false)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${!is100Percent ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Absolute Counts
                                </button>
                                <button onclick="window.sim4SetMode(true)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${is100Percent ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    100% Normalized
                                </button>
                            </div>
                        </div>

                        <!-- SVG Stacked Chart -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Grid Lines -->
                                ${(is100Percent ? [0, 25, 50, 75, 100] : [0, 100, 250, 400, 500]).map(val => {
                                    const y = baseY - (val / maxScale) * plotH;
                                    return `
                                        <line x1="50" y1="${y}" x2="${svgW - 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="44" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}${is100Percent ? '%' : ''}</text>
                                    `;
                                }).join('')}

                                <line x1="50" y1="20" x2="50" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="50" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Bar 1: Rural Cohort (N=50) -->
                                <g>
                                    <!-- Bus -->
                                    <rect x="110" y="${baseY - hA_bus}" width="${barW}" height="${hA_bus}" fill="#06b6d4" class="transition-all duration-500"/>
                                    <!-- Walk -->
                                    <rect x="110" y="${baseY - hA_bus - hA_walk}" width="${barW}" height="${hA_walk}" fill="#10b981" class="transition-all duration-500"/>
                                    <!-- Bike -->
                                    <rect x="110" y="${baseY - hA_bus - hA_walk - hA_bike}" width="${barW}" height="${hA_bike}" rx="4" fill="#f59e0b" class="transition-all duration-500"/>

                                    <text x="147" y="${baseY - hA_bus - hA_walk - hA_bike - 6}" fill="#f8fafc" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">
                                        ${is100Percent ? '100% (N=50)' : 'Total: 50'}
                                    </text>
                                    <text x="147" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">Rural School</text>
                                    ${is100Percent ? `<text x="147" y="${baseY - hA_bus/2 + 3}" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">40%</text>` : ''}
                                </g>

                                <!-- Bar 2: Urban Cohort (N=500) -->
                                <g>
                                    <!-- Bus -->
                                    <rect x="250" y="${baseY - hB_bus}" width="${barW}" height="${hB_bus}" fill="#06b6d4" class="transition-all duration-500"/>
                                    <!-- Walk -->
                                    <rect x="250" y="${baseY - hB_bus - hB_walk}" width="${barW}" height="${hB_walk}" fill="#10b981" class="transition-all duration-500"/>
                                    <!-- Bike -->
                                    <rect x="250" y="${baseY - hB_bus - hB_walk - hB_bike}" width="${barW}" height="${hB_bike}" rx="4" fill="#f59e0b" class="transition-all duration-500"/>

                                    <text x="287" y="${baseY - hB_bus - hB_walk - hB_bike - 6}" fill="#f8fafc" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">
                                        ${is100Percent ? '100% (N=500)' : 'Total: 500'}
                                    </text>
                                    <text x="287" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle">Urban School</text>
                                    ${is100Percent ? `<text x="287" y="${baseY - hB_bus/2 + 3}" fill="#ffffff" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">50%</text>` : ''}
                                </g>
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            ${is100Percent ?
                                '<span class="text-cyan-400 font-bold">100% Mode:</span> Eliminates total sample disparity (50 vs 500) to fairly compare transport shares.' :
                                '<span class="text-indigo-400 font-bold">Absolute Mode:</span> Rural school bar is visually crushed by the 500-student urban school.'}
                        </div>
                    </div>
                `;
            }

            window.sim4SetMode = function(flag) {
                is100Percent = flag;
                playTone(is100Percent ? 600 : 400, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 5: Continuous Interval Histogram Builder & Boundary Snapper
        function renderSim5(vp) {
            let freqs = [15, 28, 42, 30, 18];
            let intervals = ["0-10", "10-20", "20-30", "30-40", "40-50"];
            let showMidpoints = true;

            function draw() {
                const svgW = 440;
                const svgH = 220;
                const barW = 60;
                const startX = 60;
                const baseY = 180;
                const plotH = 150;
                const maxF = 50;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Controls -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Adjust Class Frequencies:</span>
                            <button onclick="window.sim5ToggleMid()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 text-[11px]">
                                ${showMidpoints ? 'Hide Class Marks' : 'Show Class Marks'}
                            </button>
                        </div>

                        <!-- Sliders -->
                        <div class="grid grid-cols-5 gap-1.5 text-center text-[10px]">
                            ${intervals.map((inv, idx) => `
                                <div class="bg-slate-900/60 p-1.5 rounded border border-slate-800">
                                    <div class="font-mono text-cyan-400 font-bold">${inv}</div>
                                    <div class="font-mono text-white text-xs font-bold">${freqs[idx]}</div>
                                    <input type="range" min="5" max="50" value="${freqs[idx]}"
                                           oninput="window.sim5SetFreq(${idx}, this.value)"
                                           class="w-full accent-cyan-500 h-1 bg-slate-700 rounded-lg cursor-pointer mt-1">
                                </div>
                            `).join('')}
                        </div>

                        <!-- SVG Histogram (Zero Gaps Between Bars) -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Grid lines -->
                                ${[0, 10, 20, 30, 40, 50].map(val => {
                                    const y = baseY - (val / maxF) * plotH;
                                    return `
                                        <line x1="50" y1="${y}" x2="${startX + 5 * barW + 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="44" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}</text>
                                    `;
                                }).join('')}

                                <line x1="50" y1="20" x2="50" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="50" y1="${baseY}" x2="${startX + 5 * barW + 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Histogram Bars (Continuous, touching) -->
                                ${freqs.map((f, idx) => {
                                    const h = (f / maxF) * plotH;
                                    const x = startX + idx * barW;
                                    const y = baseY - h;
                                    const midX = x + barW / 2;

                                    return `
                                        <g>
                                            <!-- Continuous Rectangle (No Gap) -->
                                            <rect x="${x}" y="${y}" width="${barW}" height="${h}"
                                                  fill="#06b6d4" fill-opacity="0.75" stroke="#0e7490" stroke-width="1.5" class="transition-all duration-300"/>
                                            <text x="${midX}" y="${y - 6}" fill="#f8fafc" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">${f}</text>

                                            <!-- Class Boundary Tick -->
                                            <line x1="${x}" y1="${baseY}" x2="${x}" y2="${baseY + 4}" stroke="#94a3b8" stroke-width="1.5"/>
                                            <text x="${x}" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">${idx * 10}</text>

                                            ${idx === 4 ? `
                                                <line x1="${x + barW}" y1="${baseY}" x2="${x + barW}" y2="${baseY + 4}" stroke="#94a3b8" stroke-width="1.5"/>
                                                <text x="${x + barW}" y="${baseY + 14}" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">50</text>
                                            ` : ''}

                                            <!-- Class Mark (Midpoint) Marker -->
                                            ${showMidpoints ? `
                                                <circle cx="${midX}" cy="${y}" r="3.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>
                                                <text x="${midX}" y="${y + 14}" fill="#f59e0b" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">x̄=${idx*10 + 5}</text>
                                            ` : ''}
                                        </g>
                                    `;
                                }).join('')}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            <span class="text-emerald-400 font-bold">Continuous Rule:</span> Rectangles touch seamlessly (Zero Gaps). Area = $\\text{Width} \\times \\text{Frequency} = 10 \\times f_i$.
                        </div>
                    </div>
                `;
            }

            window.sim5SetFreq = function(idx, val) {
                freqs[idx] = parseInt(val);
                draw();
            };
            window.sim5ToggleMid = function() {
                showMidpoints = !showMidpoints;
                draw();
            };
            draw();
        }

        // SIMULATOR 6: Unequal Width Frequency Density Correcter & Area Verifier
        function renderSim6(vp) {
            let isCorrected = false;

            // Unequal width intervals:
            // 0-10: width 10, freq 20 (raw height 20)
            // 10-20: width 10, freq 30 (raw height 30)
            // 20-40: width 20, freq 40 (raw height 40, adjusted height (10/20)*40 = 20)
            // 40-70: width 30, freq 30 (raw height 30, adjusted height (10/30)*30 = 10)
            const rawData = [
                { inv: "0-10", w: 10, f: 20, adjH: 20, rawH: 20 },
                { inv: "10-20", w: 10, f: 30, adjH: 30, rawH: 30 },
                { inv: "20-40", w: 20, f: 40, adjH: 20, rawH: 40 },
                { inv: "40-70", w: 30, f: 30, adjH: 10, rawH: 30 }
            ];

            function draw() {
                const svgW = 440;
                const svgH = 220;
                const scaleW = 4.5; // pixels per unit interval width
                const startX = 50;
                const baseY = 180;
                const plotH = 150;
                const maxH = 50;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Toggle Button -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <div>
                                <span class="text-xs font-bold text-white">Unequal Width Representation:</span>
                                <p class="text-[10px] text-slate-400">Min class width = 10 units</p>
                            </div>
                            <button onclick="window.sim6Toggle()" class="px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 ${isCorrected ? 'bg-emerald-600 text-white shadow glow-emerald' : 'bg-rose-600 text-white shadow'}">
                                <i data-lucide="${isCorrected ? 'check-circle' : 'alert-triangle'}" class="w-4 h-4"></i>
                                <span>${isCorrected ? 'Corrected (Frequency Density)' : 'Distorted (Raw Frequencies)'}</span>
                            </button>
                        </div>

                        <!-- SVG Histogram -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Grid lines -->
                                ${[0, 10, 20, 30, 40].map(val => {
                                    const y = baseY - (val / maxH) * plotH;
                                    return `
                                        <line x1="45" y1="${y}" x2="${svgW - 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="38" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}</text>
                                    `;
                                }).join('')}

                                <line x1="45" y1="20" x2="45" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="45" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Bars with dynamic width and height -->
                                ${(() => {
                                    let currentX = startX;
                                    return rawData.map((d, idx) => {
                                        const pxW = d.w * scaleW;
                                        const hVal = isCorrected ? d.adjH : d.rawH;
                                        const pxH = (hVal / maxH) * plotH;
                                        const x = currentX;
                                        const y = baseY - pxH;
                                        currentX += pxW;

                                        const color = isCorrected ? '#10b981' : '#f43f5e';

                                        return `
                                            <g>
                                                <rect x="${x}" y="${y}" width="${pxW}" height="${pxH}"
                                                      fill="${color}" fill-opacity="0.8" stroke="${color}" stroke-width="1.5" class="transition-all duration-500"/>
                                                <!-- Drawn Area annotation -->
                                                <text x="${x + pxW/2}" y="${y - 6}" fill="#f8fafc" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">
                                                    ${isCorrected ? `Adj H: ${d.adjH}` : `Raw H: ${d.rawH}`}
                                                </text>
                                                <text x="${x + pxW/2}" y="${y + pxH/2 + 3}" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">
                                                    f=${d.f}
                                                </text>
                                                <text x="${x + pxW/2}" y="${baseY + 14}" fill="#94a3b8" font-size="8" font-family="monospace" text-anchor="middle">${d.inv}</text>
                                            </g>
                                        `;
                                    }).join('');
                                })()}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center font-mono ${isCorrected ? 'text-emerald-400' : 'text-rose-400'}">
                            ${isCorrected ?
                                '<strong>Law Preserved:</strong> Area ∝ Frequency. Adjusted Height = (Min Width / Class Width) × f.' :
                                '<strong>Visual Distortion Alert:</strong> Width-30 bar area is inflated 3x because raw height was plotted!'}
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }

            window.sim6Toggle = function() {
                isCorrected = !isCorrected;
                playTone(isCorrected ? 523.25 : 300, 0.12, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 7: Interactive Frequency Polygon & Area Equivalence Engine
        function renderSim7(vp) {
            let showBars = true;
            let showPolygon = true;
            let showExtensions = true;

            const classes = [
                { mid: 5, f: 0, isExt: true },
                { mid: 15, f: 12, isExt: false },
                { mid: 25, f: 28, isExt: false },
                { mid: 35, f: 38, isExt: false },
                { mid: 45, f: 22, isExt: false },
                { mid: 55, f: 14, isExt: false },
                { mid: 65, f: 0, isExt: true }
            ];

            function draw() {
                const svgW = 440;
                const svgH = 220;
                const barW = 50;
                const startX = 45;
                const baseY = 180;
                const plotH = 150;
                const maxF = 45;

                // Polygon coordinates
                const polyPoints = classes.filter(c => showExtensions || !c.isExt).map((c, i) => {
                    const x = startX + (c.mid / 10) * barW;
                    const y = baseY - (c.f / maxF) * plotH;
                    return `${x},${y}`;
                }).join(' ');

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Toggles -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                            <label class="flex items-center gap-1.5 cursor-pointer text-slate-300">
                                <input type="checkbox" ${showBars ? 'checked' : ''} onchange="window.sim7Toggle('bars')" class="accent-cyan-500">
                                <span>Histogram Bars</span>
                            </label>
                            <label class="flex items-center gap-1.5 cursor-pointer text-cyan-300 font-bold">
                                <input type="checkbox" ${showPolygon ? 'checked' : ''} onchange="window.sim7Toggle('poly')" class="accent-cyan-500">
                                <span>Frequency Polygon</span>
                            </label>
                            <label class="flex items-center gap-1.5 cursor-pointer text-amber-300">
                                <input type="checkbox" ${showExtensions ? 'checked' : ''} onchange="window.sim7Toggle('ext')" class="accent-amber-500">
                                <span>Zero Baseline Extensions</span>
                            </label>
                        </div>

                        <!-- SVG Canvas -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Axes & Grid -->
                                ${[0, 15, 30, 45].map(val => {
                                    const y = baseY - (val / maxF) * plotH;
                                    return `
                                        <line x1="45" y1="${y}" x2="${svgW - 20}" y2="${y}" stroke="#334155" stroke-dasharray="3,3" stroke-width="1"/>
                                        <text x="38" y="${y + 3}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="end">${val}</text>
                                    `;
                                }).join('')}

                                <line x1="45" y1="20" x2="45" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>
                                <line x1="45" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Histogram Bars (Optional) -->
                                ${showBars ? classes.filter(c => !c.isExt).map((c) => {
                                    const h = (c.f / maxF) * plotH;
                                    const x = startX + (c.mid / 10) * barW - barW / 2;
                                    const y = baseY - h;
                                    return `
                                        <rect x="${x}" y="${y}" width="${barW}" height="${h}"
                                              fill="#06b6d4" fill-opacity="0.35" stroke="#0e7490" stroke-width="1.5"/>
                                    `;
                                }).join('') : ''}

                                <!-- Frequency Polygon -->
                                ${showPolygon ? `
                                    <polyline points="${polyPoints}" fill="none" stroke="#f59e0b" stroke-width="2.5" class="transition-all duration-300"/>
                                    ${classes.filter(c => showExtensions || !c.isExt).map(c => {
                                        const x = startX + (c.mid / 10) * barW;
                                        const y = baseY - (c.f / maxF) * plotH;
                                        return `
                                            <circle cx="${x}" cy="${y}" r="4" fill="${c.isExt ? '#ef4444' : '#f59e0b'}" stroke="#ffffff" stroke-width="1.5"/>
                                            <text x="${x}" y="${y - 8}" fill="${c.isExt ? '#ef4444' : '#f8fafc'}" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">
                                                (${c.mid}, ${c.f})
                                            </text>
                                        `;
                                    }).join('')}
                                ` : ''}

                                <!-- X Ticks -->
                                ${classes.map(c => {
                                    const x = startX + (c.mid / 10) * barW;
                                    return `
                                        <line x1="${x}" y1="${baseY}" x2="${x}" y2="${baseY + 4}" stroke="#94a3b8" stroke-width="1"/>
                                        <text x="${x}" y="${baseY + 14}" fill="#94a3b8" font-size="8" font-family="monospace" text-anchor="middle">${c.mid}</text>
                                    `;
                                }).join('')}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            <span class="text-amber-400 font-bold">Area Conservation Theorem:</span> Total enclosed polygon area equals total histogram area via congruent corner triangles.
                        </div>
                    </div>
                `;
            }

            window.sim7Toggle = function(type) {
                if (type === 'bars') showBars = !showBars;
                if (type === 'poly') showPolygon = !showPolygon;
                if (type === 'ext') showExtensions = !showExtensions;
                playTone(480, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 8: The Central Balance Fulcrum & Dynamic Center of Gravity
        function renderSim8(vp) {
            let weights = [20, 30, 30, 40, 80];

            function draw() {
                const n = weights.length;
                const mean = weights.reduce((a,b)=>a+b, 0) / n;
                const sorted = [...weights].sort((a,b)=>a-b);
                const median = (n % 2 !== 0) ? sorted[Math.floor(n/2)] : (sorted[n/2 - 1] + sorted[n/2]) / 2;

                // Mode
                const freq = {};
                weights.forEach(x => freq[x] = (freq[x] || 0) + 1);
                let maxF = 0, mode = weights[0];
                for (let k in freq) {
                    if (freq[k] > maxF) { maxF = freq[k]; mode = Number(k); }
                }

                const svgW = 440;
                const svgH = 220;
                const beamY = 130;
                const beamX1 = 40;
                const beamX2 = 400;

                // Coordinate map: 0 to 100 mapped between 40 and 400
                function valToX(v) { return beamX1 + (v / 100) * (beamX2 - beamX1); }

                const fulcrumX = valToX(mean);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Controls -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="text-slate-300 font-medium">Add/Remove Weights on Beam:</span>
                            <div class="flex gap-1.5">
                                <button onclick="window.sim8Add(90)" class="px-2 py-1 rounded bg-rose-600 hover:bg-rose-500 text-white font-bold text-[11px] shadow">
                                    + Outlier (90)
                                </button>
                                <button onclick="window.sim8Add(50)" class="px-2 py-1 rounded bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-[11px] shadow">
                                    + Center (50)
                                </button>
                                <button onclick="window.sim8Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] border border-slate-700">
                                    Reset
                                </button>
                            </div>
                        </div>

                        <!-- Seesaw Visualization -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Balance Beam -->
                                <rect x="${beamX1}" y="${beamY}" width="${beamX2 - beamX1}" height="8" rx="3" fill="#cbd5e1"/>

                                <!-- Ruler Ticks -->
                                ${[0, 20, 40, 60, 80, 100].map(v => `
                                    <line x1="${valToX(v)}" y1="${beamY + 8}" x2="${valToX(v)}" y2="${beamY + 14}" stroke="#64748b" stroke-width="1.5"/>
                                    <text x="${valToX(v)}" y="${beamY + 25}" fill="#64748b" font-size="9" font-family="monospace" text-anchor="middle">${v}</text>
                                `).join('')}

                                <!-- Dynamic Fulcrum (Triangle at Mean) -->
                                <polygon points="${fulcrumX},${beamY + 8} ${fulcrumX - 12},${beamY + 36} ${fulcrumX + 12},${beamY + 36}"
                                         fill="#10b981" stroke="#059669" stroke-width="1.5" class="transition-all duration-300"/>
                                <text x="${fulcrumX}" y="${beamY + 48}" fill="#10b981" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">
                                    Fulcrum (Mean=${mean.toFixed(1)})
                                </text>

                                <!-- Weights Stacked on Beam -->
                                ${weights.map((w, idx) => {
                                    const x = valToX(w);
                                    // Count duplicates below
                                    const stackIndex = weights.slice(0, idx).filter(item => item === w).length;
                                    const y = beamY - 14 - stackIndex * 18;
                                    return `
                                        <circle cx="${x}" cy="${y}" r="7" fill="#06b6d4" stroke="#ffffff" stroke-width="1.5" class="transition-all duration-300"/>
                                        <text x="${x}" y="${y + 2.5}" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">${w}</text>
                                    `;
                                }).join('')}

                                <!-- Measure Markers Above -->
                                <!-- Median Marker -->
                                <line x1="${valToX(median)}" y1="30" x2="${valToX(median)}" y2="${beamY}" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,2"/>
                                <rect x="${valToX(median) - 28}" y="15" width="56" height="16" rx="4" fill="#a855f7"/>
                                <text x="${valToX(median)}" y="26" fill="#ffffff" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">
                                    Median: ${median}
                                </text>

                                <!-- Mode Marker -->
                                <line x1="${valToX(mode)}" y1="55" x2="${valToX(mode)}" y2="${beamY}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,2"/>
                                <rect x="${valToX(mode) - 24}" y="42" width="48" height="16" rx="4" fill="#f59e0b"/>
                                <text x="${valToX(mode)}" y="53" fill="#ffffff" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">
                                    Mode: ${mode}
                                </text>
                            </svg>
                        </div>
                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            <span class="text-emerald-400 font-bold">Physical Principle:</span> The Mean is the exact center of gravity where torque $\\sum (x_i - \\bar{x}) = 0$.
                        </div>
                    </div>
                `;
            }

            window.sim8Add = function(val) {
                if (weights.length < 12) {
                    weights.push(val);
                    playTone(val * 8, 0.08, 'sine');
                    draw();
                }
            };
            window.sim8Reset = function() {
                weights = [20, 30, 30, 40, 80];
                playTone(350, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 9: Dynamic Mean Calculator & Zero-Deviation Balancer
        function renderSim9(vp) {
            let pts = [15, 25, 45, 65, 80];
            let shiftC = 0;

            function draw() {
                const adjustedPts = pts.map(p => p + shiftC);
                const n = adjustedPts.length;
                const mean = adjustedPts.reduce((a,b)=>a+b, 0) / n;
                const deviations = adjustedPts.map(p => p - mean);
                const sumDev = deviations.reduce((a,b)=>a+b, 0);

                const svgW = 440;
                const svgH = 200;
                const baseY = 100;
                const startX = 40;
                const plotW = 360;

                function mapX(val) { return startX + (val / 100) * plotW; }

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Transformation Controls -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                            <span class="text-slate-300 font-medium">Add Constant Shift (+c):</span>
                            <div class="flex items-center gap-2">
                                <button onclick="window.sim9Shift(-10)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">-10</button>
                                <span class="font-mono text-white font-bold">c = ${shiftC}</span>
                                <button onclick="window.sim9Shift(10)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">+10</button>
                                <button onclick="window.sim9Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700 ml-2">Reset</button>
                            </div>
                        </div>

                        <!-- Dynamic Number Line & Deviations -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Zero line (Base Axis) -->
                                <line x1="${startX}" y1="${baseY}" x2="${startX + plotW}" y2="${baseY}" stroke="#64748b" stroke-width="2"/>

                                <!-- Ticks -->
                                ${[0, 20, 40, 60, 80, 100].map(v => `
                                    <line x1="${mapX(v)}" y1="${baseY - 4}" x2="${mapX(v)}" y2="${baseY + 4}" stroke="#64748b" stroke-width="1.5"/>
                                    <text x="${mapX(v)}" y="${baseY + 16}" fill="#64748b" font-size="8" font-family="monospace" text-anchor="middle">${v}</text>
                                `).join('')}

                                <!-- Mean Vertical Line -->
                                <line x1="${mapX(mean)}" y1="20" x2="${mapX(mean)}" y2="180" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
                                <rect x="${mapX(mean) - 28}" y="10" width="56" height="16" rx="4" fill="#10b981"/>
                                <text x="${mapX(mean)}" y="21" fill="#ffffff" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">
                                    x̄ = ${mean.toFixed(1)}
                                </text>

                                <!-- Deviation Bars d_i = (x_i - x̄) -->
                                ${adjustedPts.map((p, idx) => {
                                    const x1 = mapX(mean);
                                    const x2 = mapX(p);
                                    const dev = deviations[idx];
                                    const y = baseY - 20 - idx * 12;
                                    const isPos = dev >= 0;

                                    return `
                                        <g>
                                            <line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" stroke="${isPos ? '#06b6d4' : '#ef4444'}" stroke-width="2.5"/>
                                            <circle cx="${x2}" cy="${y}" r="3.5" fill="${isPos ? '#06b6d4' : '#ef4444'}"/>
                                            <text x="${(x1 + x2)/2}" y="${y - 4}" fill="${isPos ? '#06b6d4' : '#ef4444'}" font-size="7" font-family="monospace" font-weight="bold" text-anchor="middle">
                                                ${dev >= 0 ? '+' : ''}${dev.toFixed(1)}
                                            </text>
                                        </g>
                                    `;
                                }).join('')}
                            </svg>
                        </div>
                        <div class="text-[11px] text-center font-mono text-emerald-400 bg-emerald-950/40 p-1.5 rounded-lg border border-emerald-800">
                            <strong>Zero-Deviation Invariant:</strong> $\\sum (x_i - \\bar{x}) = ${sumDev.toFixed(2)} \\equiv 0$. Positive deviations cancel negative deviations perfectly!
                        </div>
                    </div>
                `;
            }

            window.sim9Shift = function(d) {
                shiftC += d;
                playTone(400 + shiftC * 5, 0.08, 'sine');
                draw();
            };
            window.sim9Reset = function() {
                shiftC = 0;
                draw();
            };
            draw();
        }

        // SIMULATOR 10: Interactive Weighted GPA & CPI Portfolio Simulator
        function renderSim10(vp) {
            let mode = 'gpa'; // 'gpa' or 'cpi'
            let items = [
                { name: "Homework", score: 90, weight: 20 },
                { name: "Midterm Exam", score: 70, weight: 30 },
                { name: "Final Project", score: 82, weight: 50 }
            ];

            function draw() {
                const totalW = items.reduce((a,b)=>a+b.weight, 0);
                const weightedSum = items.reduce((a,b)=>a + b.score * b.weight, 0);
                const weightedAvg = weightedSum / totalW;
                const simpleAvg = items.reduce((a,b)=>a + b.score, 0) / items.length;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Tabs -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-white">Weighted Setting:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim10SetMode('gpa')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'gpa' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Student Course GPA
                                </button>
                                <button onclick="window.sim10SetMode('cpi')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'cpi' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Inflation Index (CPI)
                                </button>
                            </div>
                        </div>

                        <!-- Sliders for Items -->
                        <div class="space-y-2">
                            ${items.map((item, idx) => `
                                <div class="bg-slate-900/60 p-2 rounded-xl border border-slate-800 flex items-center justify-between gap-3 text-xs">
                                    <div class="w-28 font-medium text-slate-200 truncate">${item.name}</div>
                                    <div class="flex-1 flex items-center gap-2">
                                        <span class="text-[10px] text-slate-400">Score:</span>
                                        <input type="range" min="0" max="100" value="${item.score}"
                                               oninput="window.sim10SetScore(${idx}, this.value)"
                                               class="w-full accent-cyan-500 h-1 bg-slate-700 rounded-lg cursor-pointer">
                                        <span class="w-8 font-mono font-bold text-cyan-300 text-right">${item.score}</span>
                                    </div>
                                    <div class="flex items-center gap-1.5 w-24">
                                        <span class="text-[10px] text-slate-400">Weight:</span>
                                        <span class="font-mono font-bold text-amber-400">${item.weight}%</span>
                                    </div>
                                </div>
                            `).join('')}
                        </div>

                        <!-- Comparison Cards -->
                        <div class="grid grid-cols-2 gap-3">
                            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center">
                                <span class="text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Simple Arithmetic Mean</span>
                                <div class="text-xl font-black text-slate-300 font-mono mt-1">${simpleAvg.toFixed(1)}</div>
                                <span class="text-[10px] text-slate-500">Equal weights (33.3% each)</span>
                            </div>
                            <div class="p-3 rounded-xl bg-indigo-950/60 border border-indigo-500/40 text-center glow-indigo">
                                <span class="text-[11px] text-indigo-300 uppercase tracking-wider font-bold">Weighted Average (x̄_w)</span>
                                <div class="text-xl font-black text-cyan-300 font-mono mt-1">${weightedAvg.toFixed(1)}</div>
                                <span class="text-[10px] text-emerald-400 font-semibold">Proportional to importance</span>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim10SetScore = function(idx, val) {
                items[idx].score = parseInt(val);
                draw();
            };
            window.sim10SetMode = function(m) {
                mode = m;
                if (m === 'gpa') {
                    items = [
                        { name: "Homework", score: 90, weight: 20 },
                        { name: "Midterm Exam", score: 70, weight: 30 },
                        { name: "Final Project", score: 82, weight: 50 }
                    ];
                } else {
                    items = [
                        { name: "Food Commodities", score: 8, weight: 45 },
                        { name: "Housing Rent", score: 5, weight: 30 },
                        { name: "Fuel & Power", score: 12, weight: 25 }
                    ];
                }
                playTone(520, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 11: Interactive Sorting & Median Squeeze Engine
        function renderSim11(vp) {
            let nums = [42, 17, 89, 33, 61, 24, 75];
            let isSorted = false;

            function draw() {
                const n = nums.length;
                let medianVal = 0;
                let midIndices = [];

                if (isSorted) {
                    if (n % 2 !== 0) {
                        midIndices = [Math.floor(n / 2)];
                        medianVal = nums[midIndices[0]];
                    } else {
                        midIndices = [n / 2 - 1, n / 2];
                        medianVal = (nums[midIndices[0]] + nums[midIndices[1]]) / 2;
                    }
                }

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Toolbar -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Count: n = ${n} (${n % 2 !== 0 ? 'ODD' : 'EVEN'})</span>
                            <div class="flex items-center gap-2">
                                <button onclick="window.sim11ToggleSize()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 text-[11px]">
                                    Toggle Odd/Even
                                </button>
                                <button onclick="window.sim11Sort()" class="px-3 py-1 rounded-lg text-xs font-bold transition ${isSorted ? 'bg-emerald-600 text-white' : 'bg-cyan-600 text-white shadow'}">
                                    ${isSorted ? 'Sorted!' : 'Sort Ascending'}
                                </button>
                                <button onclick="window.sim11Shuffle()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700 text-[11px]">
                                    Shuffle
                                </button>
                            </div>
                        </div>

                        <!-- Visual Bubbles Array -->
                        <div class="min-h-[140px] flex items-center justify-center gap-2 p-4 bg-slate-950 rounded-xl border border-slate-800 flex-wrap">
                            ${nums.map((val, idx) => {
                                const isMid = isSorted && midIndices.includes(idx);
                                return `
                                    <div class="flex flex-col items-center gap-1 transition-all duration-500 transform ${isMid ? 'scale-110' : ''}">
                                        <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono font-bold text-sm shadow-lg transition-all duration-500
                                                    ${isMid ? 'bg-gradient-to-tr from-amber-500 to-emerald-400 text-slate-950 ring-4 ring-amber-400/40 glow-amber' :
                                                      isSorted ? 'bg-indigo-900/60 border border-indigo-700 text-cyan-300' : 'bg-slate-800 border border-slate-700 text-white'}">
                                            ${val}
                                        </div>
                                        <span class="text-[9px] font-mono text-slate-500">pos ${idx+1}</span>
                                    </div>
                                `;
                            }).join('')}
                        </div>

                        <!-- Results Badge -->
                        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center text-xs">
                            ${!isSorted ?
                                '<span class="text-amber-400 font-semibold">Step 1 Required:</span> Arrange raw numbers in ascending order before locating the median.' :
                                `<div class="font-mono">
                                    <span class="text-slate-400">${n % 2 !== 0 ? `Odd Formula: Position ((n+1)/2) = ${midIndices[0]+1}th term` : `Even Formula: Average of ${midIndices[0]+1}th and ${midIndices[1]+1}th terms`}</span>
                                    <div class="text-lg font-black text-amber-400 mt-1">Median = ${medianVal}</div>
                                </div>`}
                        </div>
                    </div>
                `;
            }

            window.sim11Sort = function() {
                nums.sort((a,b)=>a-b);
                isSorted = true;
                playTone(587.33, 0.15, 'triangle');
                draw();
            };
            window.sim11Shuffle = function() {
                nums.sort(()=>Math.random() - 0.5);
                isSorted = false;
                playTone(320, 0.1, 'sine');
                draw();
            };
            window.sim11ToggleSize = function() {
                if (nums.length === 7) nums = [42, 17, 89, 33, 61, 24, 75, 50];
                else nums = [42, 17, 89, 33, 61, 24, 75];
                isSorted = false;
                draw();
            };
            draw();
        }

        // SIMULATOR 12: Interactive Frequency Bar Peak & Mode Detector
        function renderSim12(vp) {
            let counts = [3, 8, 14, 8, 4, 2];
            let labels = ["Size 6", "Size 7", "Size 8", "Size 9", "Size 10", "Size 11"];

            function draw() {
                const maxF = Math.max(...counts);
                const modes = [];
                counts.forEach((c, idx) => {
                    if (c === maxF) modes.push(idx);
                });

                const isUniform = counts.every(c => c === counts[0]);

                const svgW = 440;
                const svgH = 200;
                const barW = 42;
                const gap = 20;
                const startX = 50;
                const baseY = 160;
                const plotH = 120;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Status Header -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="text-slate-300 font-medium">Retail Shoe Inventory (UK Sizes):</span>
                            <div class="font-mono font-bold text-amber-400">
                                ${isUniform ? 'No Distinct Mode (Uniform)' :
                                  modes.length === 1 ? `Unimodal: Mode = ${labels[modes[0]]} (f=${maxF})` :
                                  `Bimodal: Modes = ${modes.map(m=>labels[m]).join(' & ')} (f=${maxF})`}
                            </div>
                        </div>

                        <!-- SVG Frequency Peaks -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <line x1="40" y1="${baseY}" x2="${svgW - 20}" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                ${counts.map((c, idx) => {
                                    const h = (c / 16) * plotH;
                                    const x = startX + idx * (barW + gap);
                                    const y = baseY - h;
                                    const isMode = !isUniform && modes.includes(idx);

                                    return `
                                        <g>
                                            <rect x="${x}" y="${y}" width="${barW}" height="${h}" rx="4"
                                                  fill="${isMode ? '#f59e0b' : '#334155'}"
                                                  stroke="${isMode ? '#fbbf24' : '#475569'}" stroke-width="1.5" class="transition-all duration-300"/>
                                            <text x="${x + barW/2}" y="${y - 6}" fill="${isMode ? '#f59e0b' : '#94a3b8'}" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">${c}</text>
                                            <text x="${x + barW/2}" y="${baseY + 14}" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">${labels[idx]}</text>

                                            <!-- Crown Icon atop Mode -->
                                            ${isMode ? `
                                                <polygon points="${x + barW/2 - 8},${y - 18} ${x + barW/2 - 4},${y - 14} ${x + barW/2},${y - 20} ${x + barW/2 + 4},${y - 14} ${x + barW/2 + 8},${y - 18} ${x + barW/2 + 6},${y - 10} ${x + barW/2 - 6},${y - 10}" fill="#fbbf24"/>
                                            ` : ''}
                                        </g>
                                    `;
                                }).join('')}
                            </svg>
                        </div>

                        <!-- Sliders -->
                        <div class="grid grid-cols-6 gap-1.5 text-center text-[10px]">
                            ${counts.map((c, idx) => `
                                <div class="bg-slate-900/60 p-1 rounded border border-slate-800">
                                    <span class="text-slate-400 font-mono">${labels[idx]}</span>
                                    <input type="range" min="1" max="15" value="${c}"
                                           oninput="window.sim12Set(${idx}, this.value)"
                                           class="w-full accent-amber-500 h-1 bg-slate-700 rounded cursor-pointer mt-1">
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }

            window.sim12Set = function(idx, val) {
                counts[idx] = parseInt(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 13: The Billionaire in the Room Outlier Experiment
        function renderSim13(vp) {
            let billionaireIncome = 500000; // starts at ₹5 Lakhs, can slide to ₹1 Crore

            function draw() {
                // 9 regular workers earning ₹40,000 each
                const salaries = [40000, 40000, 40000, 40000, 40000, 40000, 40000, 40000, 40000, billionaireIncome];
                const n = 10;
                const mean = salaries.reduce((a,b)=>a+b, 0) / n;
                const sorted = [...salaries].sort((a,b)=>a-b);
                const median = (sorted[4] + sorted[5]) / 2; // (40,000 + 40,000)/2 = 40,000

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Outlier Slider -->
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 space-y-2">
                            <div class="flex items-center justify-between text-xs">
                                <span class="font-bold text-white">10th Person's Monthly Income (Outlier):</span>
                                <span class="font-mono font-black text-rose-400 text-sm">₹${billionaireIncome.toLocaleString('en-IN')}</span>
                            </div>
                            <input type="range" min="40000" max="10000000" step="50000" value="${billionaireIncome}"
                                   oninput="window.sim13Set(this.value)"
                                   class="w-full accent-rose-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer">
                            <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                                <span>₹40,000 (Equal worker)</span>
                                <span>₹50 Lakhs</span>
                                <span>₹1 Crore (Billionaire)</span>
                            </div>
                        </div>

                        <!-- Side-by-Side Comparison Meters -->
                        <div class="grid grid-cols-2 gap-3">
                            <!-- Mean Card -->
                            <div class="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/40 text-center flex flex-col justify-between">
                                <div>
                                    <span class="text-xs font-bold text-rose-300 uppercase tracking-wide">Arithmetic Mean Income</span>
                                    <div class="text-xl font-black text-rose-400 font-mono my-1 truncate">
                                        ₹${Math.round(mean).toLocaleString('en-IN')}
                                    </div>
                                </div>
                                <span class="text-[10px] text-rose-300 font-medium">
                                    Heavily skewed! Misleads public into believing typical worker earns lakhs.
                                </span>
                            </div>

                            <!-- Median Card -->
                            <div class="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-center flex flex-col justify-between glow-emerald">
                                <div>
                                    <span class="text-xs font-bold text-emerald-300 uppercase tracking-wide">Median Income (Robust)</span>
                                    <div class="text-xl font-black text-emerald-400 font-mono my-1">
                                        ₹${median.toLocaleString('en-IN')}
                                    </div>
                                </div>
                                <span class="text-[10px] text-emerald-300 font-medium">
                                    Rock Solid! Accurately reflects 90% of the population's experience.
                                </span>
                            </div>
                        </div>

                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            <span class="text-cyan-400 font-bold">Key Takeaway:</span> Outliers corrupt the Mean while the Median remains invariant and truthful.
                        </div>
                    </div>
                `;
            }

            window.sim13Set = function(val) {
                billionaireIncome = parseInt(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 14: Interactive Skewness Curve & Karl Pearson Verifier
        function renderSim14(vp) {
            let skew = 0; // -1 (left skewed), 0 (symmetric), +1 (right skewed)

            function draw() {
                // Symmetrical: Mean=50, Med=50, Mode=50
                // Right skewed (+1): Mean=65, Med=55, Mode=35 (Pearson: Mode ~ 3(55)-2(65) = 165 - 130 = 35)
                // Left skewed (-1): Mode=65, Med=45, Mean=35 (Pearson: Mode ~ 3(45)-2(35) = 135 - 70 = 65)
                let mean, median, mode;
                if (skew === 0) {
                    mean = 50; median = 50; mode = 50;
                } else if (skew > 0) {
                    mean = 64; median = 54; mode = 34;
                } else {
                    mean = 36; median = 46; mode = 66;
                }

                const svgW = 440;
                const svgH = 200;
                const baseY = 160;

                // Path curve generation
                let curvePath = "";
                if (skew === 0) {
                    curvePath = "M 40,160 Q 220,10 400,160";
                } else if (skew > 0) {
                    // Peak at left (mode 34 ~ x 160), long tail to right (400)
                    curvePath = "M 40,160 Q 140,10 200,80 T 400,160";
                } else {
                    // Long tail at left (40), peak at right (mode 66 ~ x 280)
                    curvePath = "M 40,160 Q 240,80 300,10 T 400,160";
                }

                function xPos(val) { return 40 + (val / 100) * 360; }

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Skewness Selector -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Distribution Geometry:</span>
                            <div class="flex gap-1.5">
                                <button onclick="window.sim14Set(-1)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${skew === -1 ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}">
                                    Left-Skewed
                                </button>
                                <button onclick="window.sim14Set(0)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${skew === 0 ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}">
                                    Symmetric
                                </button>
                                <button onclick="window.sim14Set(1)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${skew === 1 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}">
                                    Right-Skewed
                                </button>
                            </div>
                        </div>

                        <!-- SVG Curve -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <line x1="40" y1="${baseY}" x2="400" y2="${baseY}" stroke="#94a3b8" stroke-width="2"/>

                                <!-- Smooth Curve -->
                                <path d="${curvePath}" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="2.5"/>

                                <!-- Vertical Lines for Mode, Median, Mean -->
                                <!-- Mode (Amber) -->
                                <line x1="${xPos(mode)}" y1="20" x2="${xPos(mode)}" y2="${baseY}" stroke="#f59e0b" stroke-width="2"/>
                                <text x="${xPos(mode)}" y="16" fill="#f59e0b" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">Mode (${mode})</text>

                                <!-- Median (Purple) -->
                                <line x1="${xPos(median)}" y1="35" x2="${xPos(median)}" y2="${baseY}" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,2"/>
                                <text x="${xPos(median)}" y="31" fill="#a855f7" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">Med (${median})</text>

                                <!-- Mean (Green) -->
                                <line x1="${xPos(mean)}" y1="50" x2="${xPos(mean)}" y2="${baseY}" stroke="#10b981" stroke-width="2" stroke-dasharray="4,3"/>
                                <text x="${xPos(mean)}" y="46" fill="#10b981" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">Mean (${mean})</text>
                            </svg>
                        </div>

                        <!-- Karl Pearson Verification Box -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-center text-xs font-mono">
                            <span class="text-slate-400">Pearson's Rule: Mode ≈ 3 · Median - 2 · Mean</span>
                            <div class="text-cyan-300 font-bold mt-0.5">
                                ${mode} ≈ 3(${median}) - 2(${mean}) = ${3*median} - ${2*mean} = ${3*median - 2*mean}
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim14Set = function(s) {
                skew = s;
                playTone(480 + s * 80, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 15: Interactive Real-World Scenario Selector & Recommender
        function renderSim15(vp) {
            const scenarios = [
                {
                    title: "Housing Affordability",
                    domain: "Real Estate Economics",
                    measure: "Median",
                    reason: "House sale prices are heavily right-skewed due to multi-crore luxury villas. The median captures genuine middle-class housing affordability.",
                    color: "emerald"
                },
                {
                    title: "Shoe Factory Production",
                    domain: "Retail Inventory",
                    measure: "Mode",
                    reason: "Shoe sizes are discrete categories. A factory must mass-produce the most popular sizes (e.g. Size 8), not a non-existent average size of 8.3.",
                    color: "amber"
                },
                {
                    title: "Electric Grid Fleet Fuel",
                    domain: "Resource Logistics",
                    measure: "Arithmetic Mean",
                    reason: "Total fuel required = Number of generators × Mean fuel consumption. The total aggregate sum is strictly governed by N · x̄.",
                    color: "cyan"
                },
                {
                    title: "High School Honours Rank",
                    domain: "Academic Assessment",
                    measure: "Weighted Average",
                    reason: "Final comprehensive board exams carry greater academic rigor and credit hours than weekly classroom quizzes.",
                    color: "indigo"
                }
            ];

            let activeIdx = 0;

            function draw() {
                const sc = scenarios[activeIdx];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Scenario Selector Pills -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5">
                            ${scenarios.map((s, idx) => `
                                <button onclick="window.sim15Select(${idx})" class="p-2 rounded-xl text-left border transition text-xs ${idx === activeIdx ? 'bg-cyan-950/80 border-cyan-500 text-cyan-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                    <div class="truncate">${s.title}</div>
                                    <div class="text-[9px] text-slate-500 truncate">${s.domain}</div>
                                </button>
                            `).join('')}
                        </div>

                        <!-- Active Recommendation Card -->
                        <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
                            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                                <div>
                                    <span class="text-xs font-bold text-white">${sc.title}</span>
                                    <p class="text-[10px] text-slate-400">${sc.domain}</p>
                                </div>
                                <span class="px-3 py-1 rounded-full font-mono text-xs font-black bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">
                                    Recommended: ${sc.measure}
                                </span>
                            </div>

                            <p class="text-xs text-slate-300 leading-relaxed">${sc.reason}</p>

                            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800/80 flex items-center gap-2 text-[11px] text-slate-400 font-mono">
                                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400 shrink-0"></i>
                                <span>Optimizes genuine operational decision-making without statistical distortion.</span>
                            </div>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }

            window.sim15Select = function(idx) {
                activeIdx = idx;
                playTone(440 + idx * 40, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 16: Interactive Computational Statistics Engine & Live Visualizer
        function renderSim16(vp) {
            let inputStr = "12, 18, 15, 22, 18, 30, 25, 18, 40";

            function compute(raw) {
                const arr = raw.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
                if (!arr.length) return null;

                const n = arr.length;
                const sorted = [...arr].sort((a,b)=>a-b);
                const sum = arr.reduce((a,b)=>a+b, 0);
                const mean = sum / n;

                const median = (n % 2 !== 0) ? sorted[Math.floor(n/2)] : (sorted[n/2 - 1] + sorted[n/2]) / 2;

                const freq = {};
                arr.forEach(x => freq[x] = (freq[x] || 0) + 1);
                let maxF = 0, mode = arr[0];
                for (let k in freq) {
                    if (freq[k] > maxF) { maxF = freq[k]; mode = Number(k); }
                }

                return { n, sorted, sum, mean, median, mode, maxF, freq, min: sorted[0], max: sorted[n-1], range: sorted[n-1] - sorted[0] };
            }

            function draw() {
                const stats = compute(inputStr);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Custom Input Field -->
                        <div class="flex items-center gap-2 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs text-slate-300 font-medium shrink-0">Input Array:</span>
                            <input id="sim16Input" type="text" value="${inputStr}"
                                   onchange="window.sim16Update(this.value)"
                                   class="flex-1 bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1 text-xs text-cyan-300 font-mono">
                            <button onclick="window.sim16Update(document.getElementById('sim16Input').value)" class="px-3 py-1 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow">
                                Compute
                            </button>
                        </div>

                        ${stats ? `
                            <!-- Metrics Grid -->
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center">
                                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                    <span class="text-[10px] text-slate-400 font-mono">Count (N)</span>
                                    <div class="text-base font-bold text-white font-mono">${stats.n}</div>
                                </div>
                                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                    <span class="text-[10px] text-emerald-400 font-mono">Mean (x̄)</span>
                                    <div class="text-base font-bold text-emerald-300 font-mono">${stats.mean.toFixed(2)}</div>
                                </div>
                                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                    <span class="text-[10px] text-amber-400 font-mono">Median</span>
                                    <div class="text-base font-bold text-amber-300 font-mono">${stats.median}</div>
                                </div>
                                <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                    <span class="text-[10px] text-cyan-400 font-mono">Mode</span>
                                    <div class="text-base font-bold text-cyan-300 font-mono">${stats.mode}</div>
                                </div>
                            </div>

                            <!-- Computational Pipelines Info -->
                            <div class="p-2.5 rounded-xl bg-slate-900/60 border border-slate-800 text-[11px] font-mono space-y-1">
                                <div class="flex justify-between text-slate-300">
                                    <span>Sorted Array [O(n log n)]:</span>
                                    <span class="text-cyan-400 truncate max-w-[200px]">${stats.sorted.join(', ')}</span>
                                </div>
                                <div class="flex justify-between text-slate-300">
                                    <span>Range (Max - Min):</span>
                                    <span class="text-amber-400">${stats.max} - ${stats.min} = ${stats.range}</span>
                                </div>
                            </div>
                        ` : `
                            <div class="text-rose-400 text-xs text-center p-4">Invalid input array. Please enter comma-separated numbers.</div>
                        `}
                    </div>
                `;
            }

            window.sim16Update = function(val) {
                inputStr = val;
                playTone(550, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // Web Speech API Voiceover Narration Logic
        function initSpeechControls() {
            const toggleBtn = document.getElementById('toggleSpeechBtn');
            const pauseBtn = document.getElementById('pauseSpeechBtn');
            const stopBtn = document.getElementById('stopSpeechBtn');
            const rateSelect = document.getElementById('speechRateSelect');

            toggleBtn.onclick = toggleSpeech;
            pauseBtn.onclick = pauseSpeech;
            stopBtn.onclick = stopSpeech;
            rateSelect.onchange = (e) => {
                speechRate = parseFloat(e.target.value);
                if (isSpeaking) {
                    stopSpeech();
                    speakCurrentSlide();
                }
            };
        }

        function toggleSpeech() {
            if (isSpeaking) {
                stopSpeech();
            } else {
                speakCurrentSlide();
            }
        }

        function pauseSpeech() {
            if (speechSynth && speechSynth.speaking) {
                if (speechSynth.paused) {
                    speechSynth.resume();
                    setSpeakingState(true);
                } else {
                    speechSynth.pause();
                    setSpeakingState(false, true);
                }
            }
        }

        function stopSpeech() {
            if (speechSynth) {
                speechSynth.cancel();
            }
            setSpeakingState(false);
        }

        function speakCurrentSlide() {
            if (!('speechSynthesis' in window)) {
                alert("Speech Synthesis not supported in this browser. Please use a modern browser.");
                return;
            }

            stopSpeech();

            let narrationText = "";
            if (currentSlideIndex < 16) {
                narrationText = SLIDES[currentSlideIndex].narration;
            } else {
                narrationText = `Mastery Assessment Quiz ${currentSlideIndex - 15}. Test your understanding across data collection, bar graphs, histograms, and measures of central tendency.`;
            }

            currentUtterance = new SpeechSynthesisUtterance(narrationText);
            currentUtterance.lang = 'en-US';
            currentUtterance.rate = speechRate;

            currentUtterance.onstart = () => {
                setSpeakingState(true);
            };

            currentUtterance.onend = () => {
                setSpeakingState(false);
            };

            currentUtterance.onerror = (e) => {
                console.warn("Speech synthesis error", e);
                setSpeakingState(false);
            };

            speechSynth.speak(currentUtterance);
        }

        function setSpeakingState(speaking, paused = false) {
            isSpeaking = speaking;
            const avatar = document.getElementById('avatarContainer');
            const pulse = document.getElementById('speakingPulse');
            const dot = document.getElementById('speakingDot');
            const status = document.getElementById('speechStatus');
            const label = document.getElementById('speechBtnLabel');

            if (speaking) {
                avatar.classList.add('talking');
                pulse.classList.remove('hidden');
                dot.classList.remove('hidden');
                status.textContent = "Speaking";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800";
                label.textContent = "Stop Audio";
            } else if (paused) {
                avatar.classList.remove('talking');
                pulse.classList.add('hidden');
                dot.classList.remove('hidden');
                status.textContent = "Paused";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-amber-950 text-amber-400 border border-amber-800";
                label.textContent = "Resume";
            } else {
                avatar.classList.remove('talking');
                pulse.classList.add('hidden');
                dot.classList.add('hidden');
                status.textContent = "Idle";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400";
                label.textContent = "Explain Slide";
            }
        }
    </script>
</body>
</html>
"""

    html = html_template.replace("__SLIDES_JSON__", slides_json).replace("__QUIZZES_JSON__", quizzes_json)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {OUTPUT_PATH} ({len(html)} bytes).")

if __name__ == '__main__':
    generate_html()

