# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 15
INTRODUCTION TO PROBABILITY (Competencies CG-6, C-6.2, CG-9)
Generates public/animations/class9-probability.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_probability_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-probability.html"

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
    <title>NCERT Class 9 Mathematics • Introduction to Probability Laboratory</title>
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
        .glow-amber {
            box-shadow: 0 0 25px -5px rgba(245, 158, 11, 0.35);
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
        @keyframes coinFlip {
            0% { transform: rotateY(0deg) scale(1); }
            50% { transform: rotateY(720deg) scale(1.2); }
            100% { transform: rotateY(1440deg) scale(1); }
        }
        .animate-coin {
            animation: coinFlip 0.6s ease-out;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-amber-500 selection:text-white">

    <!-- Header Navigation Bar -->
    <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur-md sticky top-0 z-40 px-4 py-3 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 via-indigo-600 to-cyan-500 flex items-center justify-center shadow-lg shadow-amber-500/25">
                <i data-lucide="dice-5" class="w-6 h-6 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 border border-amber-500/30">NCERT Class 9</span>
                    <span class="text-xs text-slate-400">Chapter 15 • Competencies CG-6, C-6.2, CG-9</span>
                </div>
                <h1 class="text-base sm:text-lg font-extrabold text-white tracking-tight flex items-center gap-2">
                    Introduction to Probability Laboratory
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
                <div class="px-3 py-1 font-mono text-amber-400 font-bold border-x border-slate-700 text-xs">
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
            <div class="glass-panel rounded-2xl p-4 border border-amber-500/20 relative overflow-hidden">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Avatar -->
                    <div id="avatarContainer" class="relative w-14 h-14 shrink-0 rounded-2xl bg-gradient-to-b from-amber-950 via-slate-900 to-slate-950 border border-amber-500/30 flex items-center justify-center shadow-inner overflow-hidden">
                        <svg class="w-12 h-12" viewBox="0 0 100 100">
                            <!-- Body / Shoulders -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#d97706"/>
                            <path d="M35,85 L50,92 L65,85 L50,98 Z" fill="#f59e0b"/>
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
                        <p class="text-[11px] text-amber-300 truncate">Audio Companion • En-US Narration</p>
                    </div>
                </div>

                <!-- Speech Controls -->
                <div class="mt-3 pt-2.5 border-t border-slate-800 flex items-center justify-between gap-1.5">
                    <button id="toggleSpeechBtn" class="flex-1 px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-md shadow-amber-600/30">
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
                        <span id="slideCategoryText" class="text-xs font-bold uppercase tracking-wider text-amber-400 font-mono">Category</span>
                        <span id="slideBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 border border-slate-700 text-slate-300">Badge</span>
                    </div>
                    <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white leading-tight mb-1">Slide Title</h2>
                    <h3 id="slideSubtitle" class="text-xs sm:text-sm text-amber-300/90 font-medium mb-3">Subtitle</h3>
                    <p id="slideSummary" class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">Summary text...</p>

                    <!-- Key Bullet Points -->
                    <div class="border-t border-slate-800 pt-3">
                        <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                            <i data-lucide="key" class="w-3.5 h-3.5 text-amber-400"></i>
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
                        <div id="slideProgressBar" class="bg-gradient-to-r from-amber-500 via-indigo-500 to-cyan-500 h-1.5 rounded-full transition-all duration-300" style="width: 5%"></div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Column: Interactive Simulator & Live Laboratory (Col 6-12) -->
        <div class="lg:col-span-7 flex flex-col gap-4">

            <!-- Simulator Container -->
            <div id="contentSlideContainer" class="flex flex-col gap-4">
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 glow-amber">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 mb-4">
                        <div class="flex items-center gap-2">
                            <div class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 border border-amber-500/30 flex items-center justify-center">
                                <i data-lucide="sparkles" class="w-4 h-4"></i>
                            </div>
                            <h3 id="simulatorTitle" class="text-sm font-bold text-white tracking-wide">Interactive Laboratory</h3>
                        </div>
                        <span class="text-[11px] font-mono text-amber-400 px-2 py-0.5 rounded bg-amber-950/60 border border-amber-800/40">Real-time Simulation</span>
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
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-amber-950/40 shadow-xl shadow-emerald-950/30">
                <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mb-3">
                    <i data-lucide="check-check" class="w-8 h-8"></i>
                </div>
                <h3 class="text-xl font-bold text-white">Congratulations on Completing Chapter 15!</h3>
                <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">You have mastered the foundations of randomness, the universal probability scale, empirical relative frequencies, the Law of Large Numbers, sample spaces, Laplace's theoretical ratio formula, complementary events, two-way contingency tables, dice sums, multi-coin binomial trees, sequential tree diagrams, sampling with/without replacement, 52-card combinatorics, geometric continuous probability, and Monte Carlo computational algorithms.</p>
                <div class="mt-4 flex justify-center gap-3">
                    <button onclick="window.navSlide(-19)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition">
                        Review Chapter From Start
                    </button>
                    <button onclick="window.navSlide(-3)" class="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold shadow-lg shadow-amber-600/30 transition">
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
                    <span class="text-amber-400 font-bold uppercase tracking-wider text-[10px]">Detailed Derivation:</span>
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
                    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-amber-400 shrink-0">${badge}</span>
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
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0"></span>
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
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0"></span>
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
                    <span class="w-5 h-5 rounded-full bg-slate-800 text-amber-400 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold border border-slate-700">Q${qIdx+1}</span>
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

        // SIMULATOR 1: Interactive Randomness vs Determinism Lab & Streak Tester
        function renderSim1(vp) {
            let flips = ['H', 'T', 'H', 'H', 'T'];
            let mode = 'random'; // 'random' or 'deterministic'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Tabs -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-white">Experimental Model:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim1SetMode('deterministic')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'deterministic' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Deterministic Physics
                                </button>
                                <button onclick="window.sim1SetMode('random')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'random' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Random Coin Flip
                                </button>
                            </div>
                        </div>

                        <!-- Visual Canvas -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 min-h-[170px] flex flex-col justify-center items-center">
                            ${mode === 'deterministic' ? `
                                <div class="text-center space-y-2">
                                    <div class="w-16 h-16 mx-auto rounded-full bg-indigo-950 border-2 border-indigo-500 flex items-center justify-center text-indigo-400 text-xl font-bold shadow-lg">
                                        100°C
                                    </div>
                                    <div class="text-xs text-white font-bold">Heating Water at Sea Level (1 atm)</div>
                                    <p class="text-[11px] text-slate-400 max-w-sm">Strictly deterministic! Outcome is 100% predictable: water boils into steam every single time. No chance involved.</p>
                                </div>
                            ` : `
                                <div class="w-full flex flex-col items-center gap-3">
                                    <div class="flex items-center gap-2">
                                        <button onclick="window.sim1Flip()" class="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs shadow-lg shadow-amber-600/30 transition flex items-center gap-1.5">
                                            <i data-lucide="rotate-cw" class="w-4 h-4"></i>
                                            <span>Flip Coin (Random Trial)</span>
                                        </button>
                                        <button onclick="window.sim1Reset()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs border border-slate-700">
                                            Clear
                                        </button>
                                    </div>

                                    <!-- Streak Tape -->
                                    <div class="flex items-center gap-1.5 p-2 bg-slate-900 rounded-xl border border-slate-800 overflow-x-auto max-w-full">
                                        ${flips.slice(-12).map((res, i) => `
                                            <div class="w-8 h-8 rounded-lg flex items-center justify-center font-mono font-black text-xs shrink-0 shadow
                                                        ${res === 'H' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/40' : 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/40'}">
                                                ${res}
                                            </div>
                                        `).join('')}
                                    </div>

                                    <div class="text-[11px] text-slate-400 font-mono">
                                        Trials: <span class="text-white font-bold">${flips.length}</span> |
                                        Heads: <span class="text-amber-400 font-bold">${flips.filter(f=>f==='H').length}</span> |
                                        Tails: <span class="text-cyan-400 font-bold">${flips.filter(f=>f==='T').length}</span>
                                    </div>
                                </div>
                            `}
                        </div>

                        <div class="text-[11px] text-center text-slate-400 font-mono">
                            ${mode === 'deterministic' ?
                                '<span class="text-indigo-400 font-bold">Deterministic:</span> Exact laws guarantee identical results.' :
                                '<span class="text-amber-400 font-bold">Random:</span> Individual trial outcome cannot be known in advance!'}
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }

            window.sim1SetMode = function(m) {
                mode = m;
                playTone(m === 'random' ? 440 : 330, 0.1, 'sine');
                draw();
            };
            window.sim1Flip = function() {
                const outcome = Math.random() < 0.5 ? 'H' : 'T';
                flips.push(outcome);
                playTone(outcome === 'H' ? 587.33 : 440, 0.08, 'triangle');
                draw();
            };
            window.sim1Reset = function() {
                flips = [];
                draw();
            };
            draw();
        }

        // SIMULATOR 2: The Interactive Probability Spectrum Slider & Verbal Mapper
        function renderSim2(vp) {
            let pVal = 0.5;

            const benchmarks = [
                { p: 0.0, label: "Impossible", color: "rose", desc: "Rolling an 8 on standard 6-sided die" },
                { p: 0.1, label: "Highly Unlikely", color: "orange", desc: "Snowing in Chennai today" },
                { p: 0.25, label: "Unlikely", color: "amber", desc: "Drawing a Heart suit from 52 cards" },
                { p: 0.5, label: "Even Chance (50/50)", color: "cyan", desc: "Tossing Heads on an unbiased coin" },
                { p: 0.75, label: "Likely", color: "indigo", desc: "Drawing a non-Spade card" },
                { p: 0.9, label: "Highly Likely", color: "teal", desc: "Newborn baby will breathe air" },
                { p: 1.0, label: "Certain / Sure", color: "emerald", desc: "Rolling a number ≤ 6 on standard die" }
            ];

            function getActiveLabel(p) {
                if (p === 0) return { label: "Impossible", color: "text-rose-400" };
                if (p < 0.2) return { label: "Highly Unlikely", color: "text-orange-400" };
                if (p < 0.4) return { label: "Unlikely", color: "text-amber-400" };
                if (p >= 0.4 && p <= 0.6) return { label: "Even Chance", color: "text-cyan-400" };
                if (p < 0.85) return { label: "Likely", color: "text-indigo-400" };
                if (p < 1.0) return { label: "Highly Likely", color: "text-teal-400" };
                return { label: "Certain (Sure Event)", color: "text-emerald-400" };
            }

            function draw() {
                const info = getActiveLabel(pVal);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Numeric Display Cards -->
                        <div class="grid grid-cols-3 gap-2 text-center">
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-slate-400 font-mono">Decimal P(E)</span>
                                <div class="text-base font-black text-amber-400 font-mono">${pVal.toFixed(2)}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-cyan-400 font-mono">Percentage</span>
                                <div class="text-base font-black text-cyan-300 font-mono">${(pVal * 100).toFixed(0)}%</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-slate-400 font-mono">Likelihood</span>
                                <div class="text-xs font-bold font-mono mt-0.5 truncate ${info.color}">${info.label}</div>
                            </div>
                        </div>

                        <!-- Probability Slider -->
                        <div class="bg-slate-900/80 p-3 rounded-xl border border-slate-800 space-y-2">
                            <input type="range" min="0" max="1" step="0.01" value="${pVal}"
                                   oninput="window.sim2Set(this.value)"
                                   class="w-full accent-amber-500 h-2 bg-gradient-to-r from-rose-500 via-amber-500 to-emerald-500 rounded-lg cursor-pointer">
                            <div class="flex justify-between text-[10px] font-mono text-slate-500">
                                <span class="text-rose-400 font-bold">0.0 (Impossible)</span>
                                <span class="text-cyan-400 font-bold">0.5 (Even Chance)</span>
                                <span class="text-emerald-400 font-bold">1.0 (Certain)</span>
                            </div>
                        </div>

                        <!-- Real-World Benchmarks Grid -->
                        <div class="grid grid-cols-2 gap-1.5 text-[10px]">
                            ${benchmarks.map(b => `
                                <button onclick="window.sim2Set(${b.p})" class="p-1.5 rounded-lg text-left bg-slate-900/60 hover:bg-slate-800 border border-slate-800/80 flex items-center justify-between">
                                    <div class="truncate pr-1">
                                        <span class="font-bold text-white">${b.label}</span>
                                        <p class="text-slate-400 truncate text-[9px]">${b.desc}</p>
                                    </div>
                                    <span class="font-mono text-amber-400 font-bold shrink-0">${b.p.toFixed(2)}</span>
                                </button>
                            `).join('')}
                        </div>
                    </div>
                `;
            }

            window.sim2Set = function(val) {
                pVal = parseFloat(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 3: Live Kerrich & Buffon Coin Tossing Experiment & Relative Frequency Tracker
        function renderSim3(vp) {
            let total = 0;
            let heads = 0;

            function draw() {
                const tails = total - heads;
                const relFreq = total > 0 ? (heads / total) : 0.5000;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Buttons Toolbar -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 flex-wrap gap-2">
                            <div class="flex gap-1.5">
                                <button onclick="window.sim3Toss(1)" class="px-2.5 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs shadow">
                                    +1 Toss
                                </button>
                                <button onclick="window.sim3Toss(10)" class="px-2.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow">
                                    +10
                                </button>
                                <button onclick="window.sim3Toss(100)" class="px-2.5 py-1 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow">
                                    +100
                                </button>
                            </div>
                            <div class="flex gap-1.5">
                                <button onclick="window.sim3SetHistoric(4040, 2048)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 text-[10px] border border-slate-700">
                                    Buffon (4,040)
                                </button>
                                <button onclick="window.sim3SetHistoric(10000, 5067)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-[10px] border border-slate-700">
                                    Kerrich (10,000)
                                </button>
                                <button onclick="window.sim3Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 text-[10px] border border-slate-700">
                                    Reset
                                </button>
                            </div>
                        </div>

                        <!-- Live Stats Bar -->
                        <div class="grid grid-cols-4 gap-2 text-center">
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-slate-400 font-mono">Total Trials (n)</span>
                                <div class="text-base font-bold text-white font-mono">${total}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-amber-400 font-mono">Heads (H)</span>
                                <div class="text-base font-bold text-amber-400 font-mono">${heads}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-cyan-400 font-mono">Tails (T)</span>
                                <div class="text-base font-bold text-cyan-400 font-mono">${tails}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-indigo-950/60 border border-indigo-500/40 glow-indigo">
                                <span class="text-[10px] text-emerald-400 font-mono">Relative Freq</span>
                                <div class="text-base font-black text-emerald-300 font-mono">${relFreq.toFixed(4)}</div>
                            </div>
                        </div>

                        <!-- Visual Coin & Deviation Meter -->
                        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-amber-500 to-yellow-300 border-2 border-yellow-200 text-slate-950 flex items-center justify-center font-serif font-black text-xl shadow-lg">
                                    H
                                </div>
                                <div class="text-xs">
                                    <div class="font-bold text-white">Theoretical Target: 0.5000</div>
                                    <p class="text-slate-400 text-[10px]">Deviation: |${(relFreq - 0.5).toFixed(4)}|</p>
                                </div>
                            </div>
                            <div class="text-right">
                                <span class="text-[11px] font-mono text-cyan-300 font-bold">${(relFreq * 100).toFixed(2)}% Heads</span>
                                <div class="w-32 bg-slate-800 rounded-full h-2 mt-1 overflow-hidden">
                                    <div class="bg-amber-400 h-2 rounded-full transition-all duration-300" style="width: ${relFreq * 100}%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim3Toss = function(count) {
                for (let i = 0; i < count; i++) {
                    total++;
                    if (Math.random() < 0.5) heads++;
                }
                playTone(count > 1 ? 600 : 480, 0.08, 'sine');
                draw();
            };
            window.sim3SetHistoric = function(t, h) {
                total = t;
                heads = h;
                playTone(520, 0.1, 'triangle');
                draw();
            };
            window.sim3Reset = function() {
                total = 0;
                heads = 0;
                draw();
            };
            draw();
        }

        // SIMULATOR 4: Interactive Law of Large Numbers Oscillation & Convergence Graph
        function renderSim4(vp) {
            let history = [0.5];

            function generateRun(maxN = 100) {
                let h = 0;
                history = [];
                for (let i = 1; i <= maxN; i++) {
                    if (Math.random() < 0.5) h++;
                    history.push(h / i);
                }
            }
            generateRun(100);

            function draw() {
                const svgW = 440;
                const svgH = 200;
                const baseY = 100; // 0.5 is at y = 100
                const maxN = history.length;

                const points = history.map((val, idx) => {
                    const x = 40 + (idx / maxN) * 370;
                    // val ranges from 0.0 to 1.0; 1.0 at y=20, 0.0 at y=180
                    const y = 180 - (val * 160);
                    return `${x},${y}`;
                }).join(' ');

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Law of Large Numbers: n = ${maxN} trials</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim4Run(50)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 text-[11px]">n = 50</button>
                                <button onclick="window.sim4Run(200)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 text-[11px]">n = 200</button>
                                <button onclick="window.sim4Run(500)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700 text-[11px]">n = 500</button>
                            </div>
                        </div>

                        <!-- SVG Convergence Graph -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="${svgW}" height="${svgH}" viewBox="0 0 ${svgW} ${svgH}" class="w-full max-w-lg">
                                <!-- Horizontal Theoretical 0.5 line -->
                                <line x1="40" y1="${baseY}" x2="410" y2="${baseY}" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,3"/>
                                <text x="415" y="${baseY + 3}" fill="#10b981" font-size="8" font-family="monospace">P=0.5</text>

                                <!-- Y Axis Ticks -->
                                <line x1="40" y1="20" x2="40" y2="180" stroke="#64748b" stroke-width="1.5"/>
                                <text x="35" y="24" fill="#64748b" font-size="8" font-family="monospace" text-anchor="end">1.0</text>
                                <text x="35" y="104" fill="#64748b" font-size="8" font-family="monospace" text-anchor="end">0.5</text>
                                <text x="35" y="184" fill="#64748b" font-size="8" font-family="monospace" text-anchor="end">0.0</text>

                                <!-- X Axis -->
                                <line x1="40" y1="180" x2="410" y2="180" stroke="#64748b" stroke-width="1.5"/>
                                <text x="40" y="194" fill="#64748b" font-size="8" font-family="monospace">1</text>
                                <text x="410" y="194" fill="#64748b" font-size="8" font-family="monospace" text-anchor="end">${maxN}</text>

                                <!-- Dynamic Trajectory Polyline -->
                                <polyline points="${points}" fill="none" stroke="#f59e0b" stroke-width="2" class="transition-all duration-300"/>
                            </svg>
                        </div>
                        <div class="text-[11px] text-center font-mono text-emerald-400">
                            <strong>Bernoulli Invariant:</strong> Wild oscillations at small $n$ settle into a stable narrow ribbon around $0.5$ as $n \\to \\infty$.
                        </div>
                    </div>
                `;
            }

            window.sim4Run = function(n) {
                generateRun(n);
                playTone(500, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 5: Interactive Sample Space Visualizer & Symmetry / Fairness Tester
        function renderSim5(vp) {
            let dieType = 'fair'; // 'fair' or 'loaded'
            let rollCounts = [0, 0, 0, 0, 0, 0];

            function draw() {
                const totalRolls = rollCounts.reduce((a,b)=>a+b, 0);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Die Selector -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Physical Symmetry:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim5SetType('fair')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${dieType === 'fair' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Fair Symmetrical Die
                                </button>
                                <button onclick="window.sim5SetType('loaded')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${dieType === 'loaded' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Loaded Die (Weighted 6)
                                </button>
                            </div>
                        </div>

                        <!-- Action Toolbar -->
                        <div class="flex items-center justify-between bg-slate-900/60 p-2 rounded-xl border border-slate-800 text-xs">
                            <button onclick="window.sim5Roll(60)" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold transition shadow">
                                Roll 60 Times
                            </button>
                            <span class="font-mono text-slate-300">Total Rolls: ${totalRolls}</span>
                            <button onclick="window.sim5Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs border border-slate-700">
                                Reset
                            </button>
                        </div>

                        <!-- 6 Frequency Bars -->
                        <div class="grid grid-cols-6 gap-2">
                            ${[1, 2, 3, 4, 5, 6].map((face, idx) => {
                                const c = rollCounts[idx];
                                const pct = totalRolls > 0 ? (c / totalRolls) * 100 : 16.6;
                                return `
                                    <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 flex flex-col items-center gap-1.5">
                                        <div class="w-8 h-8 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center font-mono font-bold text-sm text-white">
                                            ${face}
                                        </div>
                                        <span class="font-mono text-xs font-bold text-amber-400">${c}</span>
                                        <div class="w-full bg-slate-800 rounded-full h-12 flex items-end overflow-hidden p-0.5">
                                            <div class="w-full rounded-b bg-cyan-500 transition-all duration-300" style="height: ${Math.min(pct * 2, 100)}%"></div>
                                        </div>
                                        <span class="text-[9px] font-mono text-slate-400">${pct.toFixed(0)}%</span>
                                    </div>
                                `;
                            }).join('')}
                        </div>

                        <div class="text-[11px] text-center font-mono ${dieType === 'fair' ? 'text-emerald-400' : 'text-rose-400'}">
                            ${dieType === 'fair' ?
                                'Equally Likely: Each face has identical 1/6 (16.7%) chance.' :
                                'Non-Equally Likely: Face 6 is weighted with 45% probability; classical ratio does NOT apply!'}
                        </div>
                    </div>
                `;
            }

            window.sim5SetType = function(t) {
                dieType = t;
                rollCounts = [0, 0, 0, 0, 0, 0];
                draw();
            };
            window.sim5Roll = function(n) {
                for (let i = 0; i < n; i++) {
                    let face;
                    if (dieType === 'fair') {
                        face = Math.floor(Math.random() * 6);
                    } else {
                        // Weighted die: 6 has 45% chance, others ~11%
                        const r = Math.random();
                        if (r < 0.45) face = 5;
                        else face = Math.floor((r - 0.45) / 0.11);
                    }
                    if (face >= 0 && face < 6) rollCounts[face]++;
                }
                playTone(550, 0.08, 'sine');
                draw();
            };
            window.sim5Reset = function() {
                rollCounts = [0, 0, 0, 0, 0, 0];
                draw();
            };
            draw();
        }

        // SIMULATOR 6: Classical Probability Calculator & Venn Diagram Circle Engine
        function renderSim6(vp) {
            let activeFilter = 'prime'; // 'even', 'prime', 'gt4', 'all'

            const sampleSpace = [1, 2, 3, 4, 5, 6];

            function isFavorable(val) {
                if (activeFilter === 'even') return val % 2 === 0;
                if (activeFilter === 'prime') return [2, 3, 5].includes(val);
                if (activeFilter === 'gt4') return val > 4;
                return true;
            }

            function draw() {
                const favorable = sampleSpace.filter(isFavorable);
                const nE = favorable.length;
                const nS = 6;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Filter Chips -->
                        <div class="grid grid-cols-4 gap-1.5 text-xs">
                            <button onclick="window.sim6Set('prime')" class="p-2 rounded-xl border transition ${activeFilter === 'prime' ? 'bg-amber-950/80 border-amber-500 text-amber-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Prime Numbers
                            </button>
                            <button onclick="window.sim6Set('even')" class="p-2 rounded-xl border transition ${activeFilter === 'even' ? 'bg-cyan-950/80 border-cyan-500 text-cyan-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Even Numbers
                            </button>
                            <button onclick="window.sim6Set('gt4')" class="p-2 rounded-xl border transition ${activeFilter === 'gt4' ? 'bg-indigo-950/80 border-indigo-500 text-indigo-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Greater than 4
                            </button>
                            <button onclick="window.sim6Set('all')" class="p-2 rounded-xl border transition ${activeFilter === 'all' ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Number ≤ 6
                            </button>
                        </div>

                        <!-- Venn Diagram Visualization -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-around">
                            <!-- Sample Space Circle -->
                            <div class="w-48 h-48 rounded-full border-2 border-slate-700 bg-slate-900/60 p-3 relative flex items-center justify-center">
                                <span class="absolute top-2 left-4 text-[10px] font-mono font-bold text-slate-500">S = {1..6}</span>

                                <!-- Favorable Inner Event Loop -->
                                <div class="w-36 h-36 rounded-full border-2 border-dashed border-amber-500/60 bg-amber-950/20 flex flex-wrap items-center justify-center p-2 gap-2">
                                    ${sampleSpace.map(val => {
                                        const fav = isFavorable(val);
                                        return `
                                            <div class="w-8 h-8 rounded-lg flex items-center justify-center font-mono font-bold text-xs shadow transition-all duration-300
                                                        ${fav ? 'bg-amber-500 text-slate-950 scale-110 ring-2 ring-amber-300 glow-amber' : 'bg-slate-800/60 text-slate-500'}">
                                                ${val}
                                            </div>
                                        `;
                                    }).join('')}
                                </div>
                            </div>

                            <!-- Calculation Panel -->
                            <div class="space-y-2 text-xs">
                                <div>
                                    <span class="text-slate-400 text-[10px] uppercase font-mono">Favorable Count n(E):</span>
                                    <div class="text-sm font-bold text-amber-400 font-mono">${nE} (${favorable.join(', ')})</div>
                                </div>
                                <div>
                                    <span class="text-slate-400 text-[10px] uppercase font-mono">Sample Space n(S):</span>
                                    <div class="text-sm font-bold text-white font-mono">${nS}</div>
                                </div>
                                <div class="pt-2 border-t border-slate-800">
                                    <span class="text-emerald-400 text-[10px] font-bold uppercase font-mono">Laplace's Formula:</span>
                                    <div class="text-lg font-black text-emerald-300 font-mono">
                                        P(E) = ${nE}/${nS} = ${(nE/nS).toFixed(3)}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim6Set = function(f) {
                activeFilter = f;
                playTone(480, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 7: Interactive Pie Slice & Complementary Balance Engine
        function renderSim7(vp) {
            let pE = 0.70;

            function draw() {
                const pNotE = 1.0 - pE;

                const svgW = 440;
                const svgH = 200;
                const cx = 130;
                const cy = 100;
                const r = 70;

                // Arc calculation for Event E
                const angleE = pE * 360;
                const radE = (angleE - 90) * (Math.PI / 180);
                const xE = cx + r * Math.cos(radE);
                const yE = cy + r * Math.sin(radE);
                const largeArc = angleE > 180 ? 1 : 0;

                const pathE = angleE >= 360 ?
                    `M ${cx},${cy - r} A ${r},${r} 0 1,1 ${cx - 0.01},${cy - r} Z` :
                    `M ${cx},${cy} L ${cx},${cy - r} A ${r},${r} 0 ${largeArc},1 ${xE},${yE} Z`;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Probability Slider -->
                        <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-cyan-400 font-bold">P(Event E): ${(pE * 100).toFixed(0)}%</span>
                                <span class="text-rose-400 font-bold">P(Not E): ${(pNotE * 100).toFixed(0)}%</span>
                            </div>
                            <input type="range" min="0" max="1" step="0.05" value="${pE}"
                                   oninput="window.sim7Set(this.value)"
                                   class="w-full accent-cyan-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer">
                        </div>

                        <!-- Pie Chart & Formula Invariant -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-around">
                            <svg width="260" height="${svgH}" viewBox="0 0 260 ${svgH}">
                                <!-- Base Circle for Not E (Rose) -->
                                <circle cx="${cx}" cy="${cy}" r="${r}" fill="#f43f5e" fill-opacity="0.8"/>
                                <!-- Arc for Event E (Cyan) -->
                                <path d="${pathE}" fill="#06b6d4" fill-opacity="0.85"/>
                                <!-- Center core -->
                                <circle cx="${cx}" cy="${cy}" r="22" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
                                <text x="${cx}" y="${cy + 3}" fill="#ffffff" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">1.0</text>
                            </svg>

                            <div class="space-y-3 text-xs">
                                <div class="p-2.5 rounded-xl bg-cyan-950/40 border border-cyan-500/40">
                                    <span class="text-cyan-400 font-bold font-mono">P(E) = ${pE.toFixed(2)}</span>
                                </div>
                                <div class="p-2.5 rounded-xl bg-rose-950/40 border border-rose-500/40">
                                    <span class="text-rose-400 font-bold font-mono">P(Ē) = 1 - P(E) = ${pNotE.toFixed(2)}</span>
                                </div>
                                <div class="text-[11px] font-mono text-emerald-400 font-bold">
                                    Sum: ${pE.toFixed(2)} + ${pNotE.toFixed(2)} ≡ 1.00
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim7Set = function(val) {
                pE = parseFloat(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 8: Interactive Two-Way Contingency Table Studio & Joint Probability Calculator
        function renderSim8(vp) {
            let tableData = [
                [25, 20, 15], // Grade 9: Sports, Music, Coding
                [15, 10, 15]  // Grade 10: Sports, Music, Coding
            ];

            let selectedCell = { r: 0, c: 2 }; // default Grade 9 Coding

            function draw() {
                const rowTotals = [
                    tableData[0].reduce((a,b)=>a+b, 0),
                    tableData[1].reduce((a,b)=>a+b, 0)
                ];
                const colTotals = [
                    tableData[0][0] + tableData[1][0],
                    tableData[0][1] + tableData[1][1],
                    tableData[0][2] + tableData[1][2]
                ];
                const grandTotal = rowTotals[0] + rowTotals[1];

                const selVal = tableData[selectedCell.r][selectedCell.c];
                const jointP = selVal / grandTotal;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs">
                            <span class="font-bold text-white">Student Cross-Tabulation (N = ${grandTotal}):</span>
                            <span class="text-[10px] text-slate-400">Click any cell to inspect joint probability</span>
                        </div>

                        <!-- Two-Way Table -->
                        <div class="overflow-hidden rounded-xl border border-slate-800 bg-slate-900/90 text-xs">
                            <table class="w-full text-center">
                                <thead class="bg-slate-800 text-[10px] font-mono text-slate-300">
                                    <tr>
                                        <th class="p-2 text-left">Cohort</th>
                                        <th class="p-2">Sports</th>
                                        <th class="p-2">Music</th>
                                        <th class="p-2">Coding</th>
                                        <th class="p-2 bg-slate-850 font-bold text-amber-400">Row Total</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-800 font-mono text-xs">
                                    ${['Grade 9', 'Grade 10'].map((g, r) => `
                                        <tr>
                                            <td class="p-2 text-left font-bold text-white">${g}</td>
                                            ${[0, 1, 2].map(c => `
                                                <td onclick="window.sim8Select(${r}, ${c})" class="p-2 cursor-pointer transition ${selectedCell.r === r && selectedCell.c === c ? 'bg-amber-500 text-slate-950 font-black' : 'hover:bg-slate-800 text-cyan-300'}">
                                                    ${tableData[r][c]}
                                                </td>
                                            `).join('')}
                                            <td class="p-2 bg-slate-900 text-amber-400 font-bold">${rowTotals[r]}</td>
                                        </tr>
                                    `).join('')}
                                    <tr class="bg-slate-850 font-bold text-amber-400 border-t-2 border-slate-700">
                                        <td class="p-2 text-left">Col Total</td>
                                        <td class="p-2">${colTotals[0]}</td>
                                        <td class="p-2">${colTotals[1]}</td>
                                        <td class="p-2">${colTotals[2]}</td>
                                        <td class="p-2 text-emerald-400 font-black">${grandTotal}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Selected Joint Probability Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between text-xs">
                            <div>
                                <span class="text-slate-400 text-[10px]">Selected Joint Event:</span>
                                <div class="font-bold text-white">
                                    P(${selectedCell.r === 0 ? 'Grade 9' : 'Grade 10'} AND ${selectedCell.c === 0 ? 'Sports' : selectedCell.c === 1 ? 'Music' : 'Coding'})
                                </div>
                            </div>
                            <div class="text-right font-mono">
                                <span class="text-amber-400 font-bold">${selVal} / ${grandTotal}</span>
                                <div class="text-sm font-black text-emerald-400">= ${jointP.toFixed(3)} (${(jointP * 100).toFixed(1)}%)</div>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim8Select = function(r, c) {
                selectedCell = { r, c };
                playTone(500, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 9: Interactive 6×6 Dual Dice Matrix & Symmetrical Sum Pyramid
        function renderSim9(vp) {
            let activeSum = 7;

            function draw() {
                let favorableCount = 0;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Sum Selector Buttons -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs flex-wrap gap-1">
                            <span class="font-bold text-white">Target Sum:</span>
                            <div class="flex gap-1 flex-wrap">
                                ${[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(s => `
                                    <button onclick="window.sim9SetSum(${s})" class="w-6 h-6 rounded font-mono text-[11px] font-bold transition ${activeSum === s ? 'bg-amber-500 text-slate-950 font-black glow-amber' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
                                        ${s}
                                    </button>
                                `).join('')}
                            </div>
                        </div>

                        <!-- 6x6 Matrix View -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <div class="grid grid-cols-6 gap-1 p-1">
                                ${[1, 2, 3, 4, 5, 6].map(d1 => `
                                    ${[1, 2, 3, 4, 5, 6].map(d2 => {
                                        const sum = d1 + d2;
                                        const isMatch = (sum === activeSum);
                                        if (isMatch) favorableCount++;
                                        return `
                                            <div class="w-8 h-8 rounded flex items-center justify-center font-mono text-[10px] font-bold transition-all duration-300
                                                        ${isMatch ? 'bg-amber-500 text-slate-950 scale-110 shadow glow-amber font-black' : 'bg-slate-900 text-slate-400 border border-slate-800'}">
                                                ${d1},${d2}
                                            </div>
                                        `;
                                    }).join('')}
                                `).join('')}
                            </div>
                        </div>

                        <!-- Sum Odds Badge -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-300 font-bold">Sum ${activeSum} Favorable: ${favorableCount} pairs</span>
                            <span class="text-emerald-400 font-black">P(Sum ${activeSum}) = ${favorableCount} / 36 = ${(favorableCount/36).toFixed(4)}</span>
                        </div>
                    </div>
                `;
            }

            window.sim9SetSum = function(s) {
                activeSum = s;
                playTone(400 + s * 30, 0.08, 'triangle');
                draw();
            };
            draw();
        }

        // SIMULATOR 10: Multi-Coin Permutation Explorer & Pascal Pyramid Visualizer
        function renderSim10(vp) {
            let coinsCount = 3;

            function draw() {
                const total = Math.pow(2, coinsCount);

                // Generate binary strings
                const outcomes = [];
                for (let i = 0; i < total; i++) {
                    let bin = i.toString(2).padStart(coinsCount, '0');
                    outcomes.push(bin.replace(/0/g, 'H').replace(/1/g, 'T'));
                }

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Coin Count Selector -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Number of Coins:</span>
                            <div class="flex gap-2">
                                ${[1, 2, 3, 4].map(c => `
                                    <button onclick="window.sim10Set(${c})" class="px-3 py-1 rounded-lg text-xs font-bold transition ${coinsCount === c ? 'bg-amber-500 text-slate-950 font-black shadow' : 'bg-slate-800 text-slate-400'}">
                                        ${c} Coin${c > 1 ? 's' : ''} (2^${c}=${Math.pow(2, c)})
                                    </button>
                                `).join('')}
                            </div>
                        </div>

                        <!-- Permutations Grid -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 max-h-[170px] overflow-y-auto flex flex-wrap gap-1.5 justify-center">
                            ${outcomes.map(out => `
                                <div class="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono font-bold tracking-widest text-cyan-300">
                                    ${out}
                                </div>
                            `).join('')}
                        </div>

                        <!-- D'Alembert Alert Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300 font-mono text-center">
                            ${coinsCount === 2 ?
                                '<span class="text-amber-400 font-bold">D&apos;Alembert Alert:</span> HT and TH are 2 distinct outcomes! P(1 Head, 1 Tail) = 2/4 = 1/2 (NOT 1/3).' :
                                `Pascal Row ${coinsCount}: Total sample space size is strictly $2^{${coinsCount}} = ${total}$ equally likely outcomes.`}
                        </div>
                    </div>
                `;
            }

            window.sim10Set = function(c) {
                coinsCount = c;
                playTone(450 + c * 50, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 11: Interactive Multi-Stage Tree Diagram Builder & Path Multiplier
        function renderSim11(vp) {
            let pRain = 0.6; // P(Rain)
            let pWinRain = 0.8; // P(Win | Rain)
            let pWinDry = 0.4;  // P(Win | Dry)

            function draw() {
                const pDry = 1.0 - pRain;
                const pLossRain = 1.0 - pWinRain;
                const pLossDry = 1.0 - pWinDry;

                const path1 = pRain * pWinRain;
                const path2 = pRain * pLossRain;
                const path3 = pDry * pWinDry;
                const path4 = pDry * pLossDry;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Branch Sliders -->
                        <div class="grid grid-cols-2 gap-2 text-[10px]">
                            <div class="bg-slate-900/80 p-2 rounded border border-slate-800">
                                <div class="flex justify-between font-mono">
                                    <span class="text-slate-400">P(Rain):</span>
                                    <span class="text-cyan-400 font-bold">${pRain.toFixed(2)}</span>
                                </div>
                                <input type="range" min="0.1" max="0.9" step="0.1" value="${pRain}"
                                       oninput="window.sim11Set('rain', this.value)"
                                       class="w-full accent-cyan-500 h-1 bg-slate-700 rounded cursor-pointer mt-1">
                            </div>
                            <div class="bg-slate-900/80 p-2 rounded border border-slate-800">
                                <div class="flex justify-between font-mono">
                                    <span class="text-slate-400">P(Win | Rain):</span>
                                    <span class="text-amber-400 font-bold">${pWinRain.toFixed(2)}</span>
                                </div>
                                <input type="range" min="0.1" max="0.9" step="0.1" value="${pWinRain}"
                                       oninput="window.sim11Set('winRain', this.value)"
                                       class="w-full accent-amber-500 h-1 bg-slate-700 rounded cursor-pointer mt-1">
                            </div>
                        </div>

                        <!-- 4 Terminal Leaf Outcomes -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center text-xs">
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[9px] text-slate-400 font-mono">Rain → Win</span>
                                <div class="font-mono text-cyan-300 font-bold mt-0.5">${path1.toFixed(3)}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[9px] text-slate-400 font-mono">Rain → Loss</span>
                                <div class="font-mono text-slate-400 font-bold mt-0.5">${path2.toFixed(3)}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[9px] text-slate-400 font-mono">Dry → Win</span>
                                <div class="font-mono text-amber-300 font-bold mt-0.5">${path3.toFixed(3)}</div>
                            </div>
                            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[9px] text-slate-400 font-mono">Dry → Loss</span>
                                <div class="font-mono text-slate-400 font-bold mt-0.5">${path4.toFixed(3)}</div>
                            </div>
                        </div>

                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-center text-emerald-400">
                            <strong>Sum of Leaves:</strong> ${(path1+path2+path3+path4).toFixed(3)} ≡ 1.000. Overall P(Win) = ${(path1 + path3).toFixed(3)}.
                        </div>
                    </div>
                `;
            }

            window.sim11Set = function(key, val) {
                if (key === 'rain') pRain = parseFloat(val);
                if (key === 'winRain') pWinRain = parseFloat(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 12: Interactive Marbles Urn: Replacement Switcher & Dependency Engine
        function renderSim12(vp) {
            let withReplacement = false;
            let urn = { red: 5, blue: 3 };

            function draw() {
                const total = urn.red + urn.blue;
                const pRedRed = withReplacement ?
                    ((5/8) * (5/8)) :
                    ((5/8) * (4/7));

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Toggle -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Sampling Protocol:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim12Toggle(true)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${withReplacement ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    With Replacement
                                </button>
                                <button onclick="window.sim12Toggle(false)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${!withReplacement ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Without Replacement
                                </button>
                            </div>
                        </div>

                        <!-- Urn Display -->
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-around">
                            <div class="text-center">
                                <div class="text-[10px] text-slate-400 font-mono mb-1">Urn Contents (N = 8)</div>
                                <div class="flex gap-1 justify-center flex-wrap max-w-[140px]">
                                    ${Array(5).fill(0).map(()=>`<span class="w-5 h-5 rounded-full bg-rose-500 shadow"></span>`).join('')}
                                    ${Array(3).fill(0).map(()=>`<span class="w-5 h-5 rounded-full bg-cyan-500 shadow"></span>`).join('')}
                                </div>
                            </div>

                            <div class="space-y-1.5 text-xs font-mono">
                                <div>1st Red Draw: <span class="text-rose-400 font-bold">5 / 8</span></div>
                                <div>2nd Red Draw: <span class="${withReplacement ? 'text-rose-400' : 'text-amber-400'} font-bold">${withReplacement ? '5 / 8' : '4 / 7'}</span></div>
                                <div class="pt-1 border-t border-slate-800 text-emerald-400 font-black">
                                    P(Two Reds) = ${withReplacement ? '25/64 ≈ 0.391' : '20/56 = 5/14 ≈ 0.357'}
                                </div>
                            </div>
                        </div>

                        <div class="text-[11px] text-center font-mono text-slate-400">
                            ${withReplacement ?
                                'Independent Trials: Urn resets to 8 marbles every draw.' :
                                'Dependent Trials: Total drops from 8 to 7, and red drops from 5 to 4!'}
                        </div>
                    </div>
                `;
            }

            window.sim12Toggle = function(flag) {
                withReplacement = flag;
                playTone(flag ? 500 : 400, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 13: Interactive 52-Card Deck Grid & Probability Filter Engine
        function renderSim13(vp) {
            let filter = 'face';

            function isMatch(suit, rank) {
                if (filter === 'all') return true;
                if (filter === 'face') return ['J', 'Q', 'K'].includes(rank);
                if (filter === 'redFace') return ['♥', '♦'].includes(suit) && ['J', 'Q', 'K'].includes(rank);
                if (filter === 'aces') return rank === 'A';
                if (filter === 'spades') return suit === '♠';
                return true;
            }

            const suits = ['♠', '♣', '♥', '♦'];
            const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

            function draw() {
                let count = 0;
                suits.forEach(s => ranks.forEach(r => { if (isMatch(s, r)) count++; }));

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <!-- Filters -->
                        <div class="flex items-center gap-1.5 flex-wrap text-[11px]">
                            ${[
                                { id: 'face', label: 'Face Cards (12)' },
                                { id: 'redFace', label: 'Red Face (6)' },
                                { id: 'aces', label: 'Aces (4)' },
                                { id: 'spades', label: 'Spades (13)' },
                                { id: 'all', label: 'All 52 Cards' }
                            ].map(btn => `
                                <button onclick="window.sim13Set('${btn.id}')" class="px-2.5 py-1 rounded-lg border transition ${filter === btn.id ? 'bg-amber-500 text-slate-950 font-bold' : 'bg-slate-900 border-slate-800 text-slate-300 hover:bg-slate-800'}">
                                    ${btn.label}
                                </button>
                            `).join('')}
                        </div>

                        <!-- Mini Deck Grid -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 overflow-x-auto">
                            <div class="grid grid-rows-4 gap-1 min-w-[380px]">
                                ${suits.map(s => `
                                    <div class="flex gap-1">
                                        ${ranks.map(r => {
                                            const match = isMatch(s, r);
                                            const isRed = ['♥', '♦'].includes(s);
                                            return `
                                                <div class="w-6 h-8 rounded border flex flex-col items-center justify-center text-[9px] font-mono font-bold transition-all
                                                            ${match ? (isRed ? 'bg-rose-950 border-rose-500 text-rose-300 scale-105' : 'bg-cyan-950 border-cyan-500 text-cyan-300 scale-105') : 'bg-slate-900/40 border-slate-800 text-slate-600 opacity-30'}">
                                                    <span>${r}</span>
                                                    <span class="text-[8px]">${s}</span>
                                                </div>
                                            `;
                                        }).join('')}
                                    </div>
                                `).join('')}
                            </div>
                        </div>

                        <!-- Result -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono text-center">
                            <span class="text-amber-400 font-bold">P(${filter}) = ${count} / 52</span>
                            <span class="text-emerald-400 font-black ml-2">= ${(count/52).toFixed(4)} (${(count/52*100).toFixed(1)}%)</span>
                        </div>
                    </div>
                `;
            }

            window.sim13Set = function(f) {
                filter = f;
                playTone(520, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 14: Interactive Archery Dartboard & Geometric Area Calculator
        function renderSim14(vp) {
            let bullseyeR = 30; // outer board radius is 80

            function draw() {
                const boardR = 80;
                const pBullseye = (bullseyeR * bullseyeR) / (boardR * boardR);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 space-y-1">
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-slate-300">Bullseye Radius: ${bullseyeR}px (Board = 80px)</span>
                                <span class="text-amber-400 font-bold">P = ${(pBullseye * 100).toFixed(1)}%</span>
                            </div>
                            <input type="range" min="10" max="70" value="${bullseyeR}"
                                   oninput="window.sim14Set(this.value)"
                                   class="w-full accent-amber-500 h-1.5 bg-slate-700 rounded cursor-pointer">
                        </div>

                        <!-- SVG Dartboard -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="220" height="170" viewBox="0 0 220 170">
                                <!-- Outer Board -->
                                <circle cx="110" cy="85" r="${boardR}" fill="#1e293b" stroke="#475569" stroke-width="2"/>
                                <!-- Inner Bullseye -->
                                <circle cx="110" cy="85" r="${bullseyeR}" fill="#f59e0b" fill-opacity="0.85" stroke="#fbbf24" stroke-width="2" class="transition-all duration-300"/>
                                <text x="110" y="88" fill="#0f172a" font-size="9" font-family="monospace" font-weight="black" text-anchor="middle">Target</text>
                            </svg>
                        </div>

                        <div class="text-[11px] text-center font-mono text-emerald-400">
                            <strong>Geometric Ratio:</strong> $P = \\frac{\\pi r^2}{\\pi R^2} = (\\frac{${bullseyeR}}{80})^2 = ${pBullseye.toFixed(3)}$. $\\pi$ cancels out!
                        </div>
                    </div>
                `;
            }

            window.sim14Set = function(r) {
                bullseyeR = parseInt(r);
                draw();
            };
            draw();
        }

        // SIMULATOR 15: Interactive Monte Carlo Pi Estimator & Dartboard Simulation
        function renderSim15(vp) {
            let totalPts = 0;
            let insidePts = 0;
            let samplePoints = [];

            function draw() {
                const piEst = totalPts > 0 ? (4 * (insidePts / totalPts)) : 3.1416;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Buttons -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Monte Carlo Pi</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim15Throw(100)" class="px-2.5 py-1 rounded bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs shadow">+100</button>
                                <button onclick="window.sim15Throw(1000)" class="px-2.5 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow">+1,000</button>
                                <button onclick="window.sim15Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs border border-slate-700">Reset</button>
                            </div>
                        </div>

                        <!-- Canvas & Stats -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-around">
                            <!-- SVG Quarter Circle Square -->
                            <svg width="150" height="150" viewBox="0 0 150 150" class="border border-slate-700 bg-slate-900 rounded">
                                <!-- Quarter Arc -->
                                <path d="M 0,150 A 150,150 0 0,0 150,0 L 0,0 Z" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="2"/>

                                <!-- Random Dots -->
                                ${samplePoints.slice(-150).map(pt => `
                                    <circle cx="${pt.x * 150}" cy="${(1 - pt.y) * 150}" r="1.5" fill="${pt.inside ? '#10b981' : '#f43f5e'}"/>
                                `).join('')}
                            </svg>

                            <div class="space-y-1.5 text-xs font-mono">
                                <div>Total Points: <span class="text-white font-bold">${totalPts}</span></div>
                                <div>Inside Arc: <span class="text-emerald-400 font-bold">${insidePts}</span></div>
                                <div class="pt-1 border-t border-slate-800">
                                    <span class="text-[10px] text-slate-400">Formula: 4 × (N_in / N)</span>
                                    <div class="text-base font-black text-amber-400">π ≈ ${piEst.toFixed(4)}</div>
                                    <span class="text-[9px] text-slate-500">True π = 3.14159...</span>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim15Throw = function(n) {
                for (let i = 0; i < n; i++) {
                    const x = Math.random();
                    const y = Math.random();
                    const inside = (x * x + y * y <= 1.0);
                    totalPts++;
                    if (inside) insidePts++;
                    if (samplePoints.length < 200) samplePoints.push({ x, y, inside });
                }
                playTone(587.33, 0.08, 'triangle');
                draw();
            };
            window.sim15Reset = function() {
                totalPts = 0;
                insidePts = 0;
                samplePoints = [];
                draw();
            };
            draw();
        }

        // SIMULATOR 16: Interactive Real-World Decision Tree & Risk Payoff Analyzer
        function renderSim16(vp) {
            let pIncident = 0.05; // 5% chance of crash/damage
            let damageCost = 100000;
            let insuranceCost = 6000;

            function draw() {
                const evUninsured = pIncident * damageCost;
                const isInsuredBetter = insuranceCost < evUninsured;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Risk Slider -->
                        <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 space-y-1">
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-slate-300">Accident Probability:</span>
                                <span class="text-rose-400 font-bold">${(pIncident * 100).toFixed(1)}%</span>
                            </div>
                            <input type="range" min="0.01" max="0.20" step="0.01" value="${pIncident}"
                                   oninput="window.sim16Set(this.value)"
                                   class="w-full accent-rose-500 h-1.5 bg-slate-700 rounded cursor-pointer">
                        </div>

                        <!-- Expected Value Comparison -->
                        <div class="grid grid-cols-2 gap-3 text-center text-xs">
                            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-slate-400 font-mono">Fixed Insurance Premium</span>
                                <div class="text-lg font-black text-cyan-300 font-mono mt-1">₹${insuranceCost}</div>
                                <span class="text-[9px] text-slate-500">Certain, known cost</span>
                            </div>
                            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                                <span class="text-[10px] text-slate-400 font-mono">Expected Loss (Uninsured)</span>
                                <div class="text-lg font-black text-rose-400 font-mono mt-1">₹${Math.round(evUninsured)}</div>
                                <span class="text-[9px] text-slate-500">P(Crash) × ₹1,00,000</span>
                            </div>
                        </div>

                        <!-- Rational Decision Badge -->
                        <div class="p-2.5 rounded-xl border text-center text-xs font-mono ${isInsuredBetter ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300' : 'bg-amber-950/40 border-amber-500/40 text-amber-300'}">
                            <strong>Actuarial Recommendation:</strong> ${isInsuredBetter ?
                                'Buy Insurance! Expected risk loss (₹' + Math.round(evUninsured) + ') exceeds premium (₹6,000).' :
                                'Self-Insure / Drive Cautiously: Premium is higher than mathematical expected risk loss.'}
                        </div>
                    </div>
                `;
            }

            window.sim16Set = function(val) {
                pIncident = parseFloat(val);
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
                narrationText = `Mastery Assessment Quiz ${currentSlideIndex - 15}. Test your understanding across probability scale, empirical trials, theoretical sample spaces, tree diagrams, and Monte Carlo algorithms.`;
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
