# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 1 (Biology)
THE FUNDAMENTAL UNIT OF LIFE (CELL)
Syllabus Competencies: C-3.1, C-3.2, C-3.3, C-4.2, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
Generates public/animations/class9-cell-fundamental-unit.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_cell_fundamental_unit_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-cell-fundamental-unit.html"

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
    <title>NCERT Class 9 Science • The Fundamental Unit of Life (Cell) Laboratory</title>
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
        .glow-emerald {
            box-shadow: 0 0 25px -5px rgba(16, 185, 129, 0.35);
        }
        .glow-cyan {
            box-shadow: 0 0 25px -5px rgba(6, 182, 212, 0.35);
        }
        .glow-indigo {
            box-shadow: 0 0 25px -5px rgba(99, 102, 241, 0.35);
        }
        .glow-rose {
            box-shadow: 0 0 25px -5px rgba(244, 63, 94, 0.35);
        }
        @keyframes pulse-slow {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.04); opacity: 0.85; }
        }
        .animate-cell-pulse {
            animation: pulse-slow 4s infinite ease-in-out;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-emerald-500 selection:text-white">

    <!-- Header Navigation Bar -->
    <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur-md sticky top-0 z-40 px-4 py-3 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-600 to-cyan-500 flex items-center justify-center shadow-lg shadow-emerald-500/25">
                <i data-lucide="microscope" class="w-6 h-6 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">NCERT Class 9 Science</span>
                    <span class="text-xs text-slate-400">Chapter 1 • Competencies C-3.1 to C-8.2</span>
                </div>
                <h1 class="text-base sm:text-lg font-extrabold text-white tracking-tight flex items-center gap-2">
                    The Fundamental Unit of Life (Cell) Laboratory
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
                <div class="px-3 py-1 font-mono text-emerald-400 font-bold border-x border-slate-700 text-xs">
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
            <div class="glass-panel rounded-2xl p-4 border border-emerald-500/20 relative overflow-hidden">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Avatar -->
                    <div id="avatarContainer" class="relative w-14 h-14 shrink-0 rounded-2xl bg-gradient-to-b from-emerald-950 via-slate-900 to-slate-950 border border-emerald-500/30 flex items-center justify-center shadow-inner overflow-hidden">
                        <svg class="w-12 h-12" viewBox="0 0 100 100">
                            <!-- Body / Shoulders -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#047857"/>
                            <path d="M35,85 L50,92 L65,85 L50,98 Z" fill="#10b981"/>
                            <!-- Neck -->
                            <rect x="44" y="62" width="12" height="18" fill="#fbcfe8" rx="3"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="45" rx="22" ry="24" fill="#fdf2f8"/>
                            <!-- Hair back -->
                            <path d="M26,45 Q24,20 50,18 Q76,20 74,45 Q75,65 68,70 Q72,40 50,28 Q28,40 32,70 Q25,65 26,45 Z" fill="#1e1b4b"/>
                            <!-- Hair bangs -->
                            <path d="M30,35 Q50,22 70,35 Q60,25 50,26 Q40,25 30,35 Z" fill="#312e81"/>
                            <!-- Glasses -->
                            <rect x="33" y="38" width="14" height="10" rx="3" fill="none" stroke="#047857" stroke-width="2"/>
                            <rect x="53" y="38" width="14" height="10" rx="3" fill="none" stroke="#047857" stroke-width="2"/>
                            <line x1="47" y1="43" x2="53" y2="43" stroke="#047857" stroke-width="2"/>
                            <!-- Eyes -->
                            <circle cx="40" cy="43" r="2.5" fill="#1e293b"/>
                            <circle cx="60" cy="43" r="2.5" fill="#1e293b"/>
                            <circle cx="41" cy="42" r="0.8" fill="#ffffff"/>
                            <circle cx="61" cy="42" r="0.8" fill="#ffffff"/>
                            <!-- Eyebrows -->
                            <path d="M34,35 Q40,33 46,36" fill="none" stroke="#1e1b4b" stroke-width="1.8" stroke-linecap="round"/>
                            <path d="M54,36 Q60,33 66,35" fill="none" stroke="#1e1b4b" stroke-width="1.8" stroke-linecap="round"/>
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
                        <p class="text-[11px] text-emerald-300 truncate">Audio Companion • En-US Narration</p>
                    </div>
                </div>

                <!-- Speech Controls -->
                <div class="mt-3 pt-2.5 border-t border-slate-800 flex items-center justify-between gap-1.5">
                    <button id="toggleSpeechBtn" class="flex-1 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-md shadow-emerald-600/30">
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
                        <span id="slideCategoryText" class="text-xs font-bold uppercase tracking-wider text-emerald-400 font-mono">Category</span>
                        <span id="slideBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 border border-slate-700 text-slate-300">Badge</span>
                    </div>
                    <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white leading-tight mb-1">Slide Title</h2>
                    <h3 id="slideSubtitle" class="text-xs sm:text-sm text-emerald-300/90 font-medium mb-3">Subtitle</h3>
                    <p id="slideSummary" class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">Summary text...</p>

                    <!-- Key Bullet Points -->
                    <div class="border-t border-slate-800 pt-3">
                        <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                            <i data-lucide="key" class="w-3.5 h-3.5 text-emerald-400"></i>
                            Key Biological Structures & Concepts
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
                        <div id="slideProgressBar" class="bg-gradient-to-r from-emerald-500 via-teal-500 to-cyan-500 h-1.5 rounded-full transition-all duration-300" style="width: 5%"></div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Column: Interactive Simulator & Live Laboratory (Col 6-12) -->
        <div class="lg:col-span-7 flex flex-col gap-4">

            <!-- Simulator Container -->
            <div id="contentSlideContainer" class="flex flex-col gap-4">
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 glow-emerald">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 mb-4">
                        <div class="flex items-center gap-2">
                            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 flex items-center justify-center">
                                <i data-lucide="sparkles" class="w-4 h-4"></i>
                            </div>
                            <h3 id="simulatorTitle" class="text-sm font-bold text-white tracking-wide">Interactive Laboratory</h3>
                        </div>
                        <span class="text-[11px] font-mono text-emerald-400 px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-800/40">Live Cell Simulation</span>
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
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-teal-950/40 shadow-xl shadow-emerald-950/30">
                <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mb-3">
                    <i data-lucide="check-check" class="w-8 h-8"></i>
                </div>
                <h3 class="text-xl font-bold text-white">Congratulations on Completing Chapter 1!</h3>
                <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">You have mastered the discovery of the cell, prokaryotes vs eukaryotes, plant vs animal cells, fluid mosaic membranes, turgor pressure, diffusion and osmosis, temporary slide mounts, nucleus, mitochondria, plastids, the endomembrane system, vacuoles, mitosis, meiosis, cancer dynamics, Indian cytogenetic breakthroughs, and synthetic biology.</p>
                <div class="mt-4 flex justify-center gap-3">
                    <button onclick="window.navSlide(-19)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition">
                        Review Chapter From Start
                    </button>
                    <button onclick="window.navSlide(-3)" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition">
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
                    <span>Step-by-Step Solution & Biological Explanation</span>
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
                    <span class="text-emerald-400 font-bold uppercase tracking-wider text-[10px]">Detailed Biological Explanation:</span>
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
                    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-emerald-400 shrink-0">${badge}</span>
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
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
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
                document.getElementById('slideSummary').textContent = "Test your deep mastery across all aspects of cell biology. Answer each question to receive immediate feedback and open the detailed step-by-step solution derivation popup.";

                document.getElementById('slideKeyPoints').innerHTML = `
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
                        <span>Answer all 10 questions to achieve full mastery of this section.</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1.5 shrink-0"></span>
                        <span>Click "View Solution" for detailed biological explanations and mechanisms.</span>
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
                    <span class="w-5 h-5 rounded-full bg-slate-800 text-emerald-400 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold border border-slate-700">Q${qIdx+1}</span>
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

        // SIMULATOR 1: Interactive Microscope Timeline & Cork-to-Living Cell Explorer
        function renderSim1(vp) {
            let viewMode = 'cork'; // 'cork' or 'pond'
            let mag = 40;

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Mode Tabs -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-white">Historical Specimen:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim1SetMode('cork')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${viewMode === 'cork' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Robert Hooke (1665 Dead Cork)
                                </button>
                                <button onclick="window.sim1SetMode('pond')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${viewMode === 'pond' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Leeuwenhoek (1674 Living Pond)
                                </button>
                            </div>
                        </div>

                        <!-- Microscope Eyepiece Circle View -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around">
                            <!-- Eyepiece Circle -->
                            <div class="w-44 h-44 rounded-full border-4 border-slate-700 bg-slate-900 overflow-hidden relative shadow-inner flex items-center justify-center">
                                ${viewMode === 'cork' ? `
                                    <!-- Hexagonal Honeycomb Cork Cells -->
                                    <svg width="176" height="176" viewBox="0 0 176 176" class="w-full h-full opacity-80">
                                        <pattern id="corkHex" width="24" height="20.78" patternUnits="userSpaceOnUse" patternTransform="scale(${mag/40})">
                                            <path d="M12,0 L24,6.93 L24,13.86 L12,20.78 L0,13.86 L0,6.93 Z" fill="#78350f" fill-opacity="0.3" stroke="#b45309" stroke-width="1.8"/>
                                        </pattern>
                                        <rect width="176" height="176" fill="url(#corkHex)"/>
                                    </svg>
                                    <span class="absolute bottom-2 font-mono text-[9px] bg-slate-950/80 px-2 py-0.5 rounded text-amber-400 font-bold border border-amber-800">Dead Cork Walls ('Cellulae')</span>
                                ` : `
                                    <!-- Swimming Pond Microbes -->
                                    <svg width="176" height="176" viewBox="0 0 176 176" class="w-full h-full bg-teal-950/30">
                                        <!-- Spirogyra spiral -->
                                        <path d="M20,30 Q50,70 80,30 T140,40" fill="none" stroke="#10b981" stroke-width="4" stroke-dasharray="2,2"/>
                                        <!-- Swimming Amoeba -->
                                        <path d="M50,100 Q70,80 100,90 Q120,120 90,140 Q60,130 50,100 Z" fill="#06b6d4" fill-opacity="0.5" stroke="#0891b2" stroke-width="2" class="animate-pulse"/>
                                        <!-- Mobile Paramecium -->
                                        <ellipse cx="120" cy="70" rx="14" ry="7" fill="#a855f7" fill-opacity="0.6" transform="rotate(-30 120 70)"/>
                                    </svg>
                                    <span class="absolute bottom-2 font-mono text-[9px] bg-slate-950/80 px-2 py-0.5 rounded text-emerald-400 font-bold border border-emerald-800">Living Motile Microbes</span>
                                `}
                            </div>

                            <!-- Magnification Dial & Description -->
                            <div class="space-y-2 text-xs">
                                <div>
                                    <span class="text-slate-400 text-[10px] uppercase font-mono">Magnification:</span>
                                    <div class="flex gap-1.5 mt-1">
                                        ${[10, 40, 100].map(m => `
                                            <button onclick="window.sim1SetMag(${m})" class="px-2 py-1 rounded font-mono text-[11px] font-bold transition ${mag === m ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}">
                                                ${m}x
                                            </button>
                                        `).join('')}
                                    </div>
                                </div>
                                <p class="text-[11px] text-slate-300 max-w-[180px] leading-relaxed">
                                    ${viewMode === 'cork' ?
                                        'Robert Hooke observed non-living cellulose compartments in oak bark, naming them "cells".' :
                                        'Leeuwenhoek discovered swimming bacteria, protozoa, and sperm using hand-polished lenses.'}
                                </p>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim1SetMode = function(m) {
                viewMode = m;
                playTone(m === 'cork' ? 380 : 540, 0.1, 'sine');
                draw();
            };
            window.sim1SetMag = function(m) {
                mag = m;
                playTone(440 + m * 2, 0.08, 'triangle');
                draw();
            };
            draw();
        }

        // SIMULATOR 2: Interactive Dual-Cell Architect: Prokaryote vs Eukaryote
        function renderSim2(vp) {
            let activeHighlight = 'nucleus'; // 'nucleus', 'organelles', 'ribosomes', 'size'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Feature Selector Buttons -->
                        <div class="grid grid-cols-4 gap-1.5 text-xs">
                            <button onclick="window.sim2Set('nucleus')" class="p-2 rounded-xl border transition ${activeHighlight === 'nucleus' ? 'bg-emerald-950 border-emerald-500 text-emerald-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Nuclear Region
                            </button>
                            <button onclick="window.sim2Set('organelles')" class="p-2 rounded-xl border transition ${activeHighlight === 'organelles' ? 'bg-cyan-950 border-cyan-500 text-cyan-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Organelles
                            </button>
                            <button onclick="window.sim2Set('ribosomes')" class="p-2 rounded-xl border transition ${activeHighlight === 'ribosomes' ? 'bg-amber-950 border-amber-500 text-amber-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Ribosomes
                            </button>
                            <button onclick="window.sim2Set('size')" class="p-2 rounded-xl border transition ${activeHighlight === 'size' ? 'bg-indigo-950 border-indigo-500 text-indigo-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                Scale (1-10 vs 100µm)
                            </button>
                        </div>

                        <!-- Side by Side Visual Comparison -->
                        <div class="grid grid-cols-2 gap-3 p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <!-- Prokaryote (Bacterium) -->
                            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col items-center gap-2">
                                <span class="text-xs font-bold text-amber-400 uppercase font-mono">Prokaryote (1-10 µm)</span>
                                <div class="w-28 h-40 rounded-3xl border-2 border-amber-500 bg-amber-950/20 relative flex flex-col items-center justify-center p-2">
                                    <!-- Naked Nucleoid -->
                                    <div class="w-16 h-20 rounded-full border border-dashed border-yellow-400/80 flex items-center justify-center transition-all ${activeHighlight === 'nucleus' ? 'scale-110 bg-yellow-400/20 ring-2 ring-yellow-400 glow-amber' : ''}">
                                        <svg class="w-12 h-16" viewBox="0 0 50 60">
                                            <path d="M10,20 Q30,5 40,25 T20,50 Q10,35 10,20 Z" fill="none" stroke="#facc15" stroke-width="2.5"/>
                                        </svg>
                                    </div>
                                    <span class="text-[9px] font-mono text-amber-300 mt-1">Nucleoid (No envelope)</span>
                                    <!-- 70S Ribosome dots -->
                                    <div class="flex gap-1 mt-1 ${activeHighlight === 'ribosomes' ? 'scale-125 font-bold text-amber-400' : 'text-slate-500'}">
                                        <span class="text-[8px] font-mono">70S Ribosomes</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Eukaryote (Animal/Plant Cell) -->
                            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col items-center gap-2">
                                <span class="text-xs font-bold text-emerald-400 uppercase font-mono">Eukaryote (5-100 µm)</span>
                                <div class="w-36 h-40 rounded-3xl border-2 border-emerald-500 bg-emerald-950/20 relative flex flex-col items-center justify-center p-2">
                                    <!-- True Nucleus -->
                                    <div class="w-16 h-16 rounded-full border-2 border-indigo-400 bg-indigo-900/40 flex items-center justify-center transition-all ${activeHighlight === 'nucleus' ? 'scale-110 ring-2 ring-indigo-400 glow-indigo' : ''}">
                                        <circle cx="20" cy="20" r="4" fill="#a855f7"/>
                                    </div>
                                    <span class="text-[9px] font-mono text-indigo-300 mt-1">True Double Nucleus</span>
                                    <!-- Membrane Organelles -->
                                    <div class="flex gap-1.5 mt-1 ${activeHighlight === 'organelles' ? 'scale-110 text-cyan-300 font-bold' : 'text-slate-500'}">
                                        <span class="text-[8px] font-mono">Mitochondria, ER, Golgi</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Explanatory Strip -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-center text-slate-300">
                            ${activeHighlight === 'nucleus' ?
                                '<span class="text-amber-400 font-bold">Nuclear Divergence:</span> Prokaryotes have naked circular DNA in a nucleoid; Eukaryotes house chromosomes in a double-membrane envelope.' :
                                activeHighlight === 'organelles' ?
                                '<span class="text-cyan-400 font-bold">Compartmentalization:</span> Eukaryotes contain membrane-bound organelles; prokaryotes lack internal membrane structures.' :
                                activeHighlight === 'ribosomes' ?
                                '<span class="text-amber-400 font-bold">Ribosome Density:</span> Prokaryotes utilize 70S ribosomes; eukaryotic cytoplasm utilizes 80S ribosomes.' :
                                '<span class="text-indigo-400 font-bold">Volumetric Scale:</span> Eukaryotic cells are 1,000 to 10,000 times larger by volume than typical bacteria!'}
                        </div>
                    </div>
                `;
            }

            window.sim2Set = function(h) {
                activeHighlight = h;
                playTone(480, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 3: Interactive Plant vs Animal Cell Dissection Laboratory
        function renderSim3(vp) {
            let activeOrganelle = 'wall';

            const organelles = [
                { id: 'wall', name: 'Cell Wall', plant: true, animal: false, desc: 'Rigid cellulose outer boundary giving tensile strength and turgor protection.' },
                { id: 'vacuole', name: 'Central Vacuole', plant: true, animal: false, desc: 'Huge permanent sap vacuole (50-90% volume) exerting turgor pressure.' },
                { id: 'chloroplast', name: 'Chloroplasts', plant: true, animal: false, desc: 'Solar photosynthetic factories with chlorophyll thylakoids.' },
                { id: 'centriole', name: 'Centrioles', plant: false, animal: true, desc: 'Paired cylindrical bodies organizing spindle fibers in animal mitosis.' },
                { id: 'mito', name: 'Mitochondria', plant: true, animal: true, desc: 'Universal powerhouses producing ATP in both plant and animal cells.' }
            ];

            function draw() {
                const cur = organelles.find(o => o.id === activeOrganelle);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Organelle Filter Buttons -->
                        <div class="flex items-center gap-1.5 flex-wrap text-xs">
                            ${organelles.map(o => `
                                <button onclick="window.sim3Select('${o.id}')" class="px-2.5 py-1 rounded-lg border transition ${activeOrganelle === o.id ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                    ${o.name}
                                </button>
                            `).join('')}
                        </div>

                        <!-- Side by Side Cutaways -->
                        <div class="grid grid-cols-2 gap-3 p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <!-- Plant Cell -->
                            <div class="p-2.5 rounded-xl border flex flex-col items-center gap-1.5 transition-all ${cur.plant ? 'bg-emerald-950/40 border-emerald-500 glow-emerald' : 'bg-slate-900/60 border-slate-800 opacity-40'}">
                                <span class="text-xs font-bold text-emerald-400 font-mono">Plant Cell (Rigid)</span>
                                <div class="w-32 h-36 rounded-xl border-4 border-emerald-500 bg-emerald-900/20 relative flex items-center justify-center p-2">
                                    <!-- Large Central Vacuole -->
                                    <div class="w-20 h-24 rounded-lg bg-teal-500/30 border border-teal-400/60 flex items-center justify-center">
                                        <span class="text-[8px] font-mono text-teal-200">Central Vacuole</span>
                                    </div>
                                    <!-- Chloroplast dot -->
                                    <circle cx="15" cy="15" r="4" fill="#22c55e"/>
                                </div>
                            </div>

                            <!-- Animal Cell -->
                            <div class="p-2.5 rounded-xl border flex flex-col items-center gap-1.5 transition-all ${cur.animal ? 'bg-indigo-950/40 border-indigo-500 glow-indigo' : 'bg-slate-900/60 border-slate-800 opacity-40'}">
                                <span class="text-xs font-bold text-indigo-400 font-mono">Animal Cell (Pliable)</span>
                                <div class="w-32 h-36 rounded-full border-2 border-indigo-400 bg-indigo-900/20 relative flex items-center justify-center p-2">
                                    <!-- Nucleus -->
                                    <div class="w-14 h-14 rounded-full bg-indigo-600/40 border border-indigo-300 flex items-center justify-center">
                                        <span class="text-[8px] font-mono text-indigo-200">Nucleus</span>
                                    </div>
                                    <!-- Centrioles icon -->
                                    <div class="absolute top-3 right-4 text-[9px] font-mono text-amber-400">⊥</div>
                                </div>
                            </div>
                        </div>

                        <!-- Organelle Diagnostic Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between text-xs">
                            <div>
                                <span class="text-white font-bold">${cur.name}</span>
                                <p class="text-[10px] text-slate-400">${cur.desc}</p>
                            </div>
                            <div class="text-right font-mono text-[10px]">
                                <span class="${cur.plant ? 'text-emerald-400' : 'text-slate-600'}">Plant: ${cur.plant ? 'YES' : 'NO'}</span> |
                                <span class="${cur.animal ? 'text-indigo-400' : 'text-slate-600'}">Animal: ${cur.animal ? 'YES' : 'NO'}</span>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim3Select = function(id) {
                activeOrganelle = id;
                playTone(520, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 4: Interactive Fluid Mosaic Membrane & Molecular Gatekeeper
        function renderSim4(vp) {
            let activeMol = 'o2'; // 'o2', 'water', 'glucose'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Molecule Selector -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Test Molecule Transit:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim4Set('o2')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${activeMol === 'o2' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    O₂ / CO₂ (Small Gas)
                                </button>
                                <button onclick="window.sim4Set('water')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${activeMol === 'water' ? 'bg-blue-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    H₂O (Aquaporin)
                                </button>
                                <button onclick="window.sim4Set('glucose')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${activeMol === 'glucose' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Glucose (Carrier)
                                </button>
                            </div>
                        </div>

                        <!-- Fluid Mosaic Bilayer Graphic -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="400" height="150" viewBox="0 0 400 150" class="w-full max-w-md">
                                <!-- Top Hydrophilic Heads -->
                                ${Array(16).fill(0).map((_, i) => `
                                    <circle cx="${25 + i * 23}" cy="40" r="7" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
                                    <line x1="${25 + i * 23}" y1="47" x2="${23 + i * 23}" y2="65" stroke="#f59e0b" stroke-width="1.5"/>
                                    <line x1="${25 + i * 23}" y1="47" x2="${27 + i * 23}" y2="65" stroke="#f59e0b" stroke-width="1.5"/>
                                `).join('')}

                                <!-- Bottom Hydrophilic Heads -->
                                ${Array(16).fill(0).map((_, i) => `
                                    <circle cx="${25 + i * 23}" cy="100" r="7" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
                                    <line x1="${25 + i * 23}" y1="93" x2="${23 + i * 23}" y2="75" stroke="#f59e0b" stroke-width="1.5"/>
                                    <line x1="${25 + i * 23}" y1="93" x2="${27 + i * 23}" y2="75" stroke="#f59e0b" stroke-width="1.5"/>
                                `).join('')}

                                <!-- Transmembrane Protein Channel -->
                                <rect x="180" y="30" width="36" height="80" rx="8" fill="#a855f7" stroke="#9333ea" stroke-width="2"/>
                                <text x="198" y="74" fill="#ffffff" font-size="8" font-family="monospace" font-weight="bold" text-anchor="middle">Channel</text>

                                <!-- Transit Trajectory -->
                                ${activeMol === 'o2' ? `
                                    <circle cx="80" cy="20" r="5" fill="#22c55e" class="animate-bounce"/>
                                    <path d="M80,25 L80,120" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,3"/>
                                    <text x="80" y="135" fill="#22c55e" font-size="8" font-family="monospace" text-anchor="middle">Freely Diffuses</text>
                                ` : activeMol === 'water' ? `
                                    <circle cx="198" cy="18" r="4" fill="#38bdf8" class="animate-bounce"/>
                                    <path d="M198,24 L198,122" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
                                    <text x="198" y="135" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle">Aquaporin Flow</text>
                                ` : `
                                    <circle cx="320" cy="20" r="8" fill="#f59e0b"/>
                                    <line x1="320" y1="28" x2="320" y2="35" stroke="#ef4444" stroke-width="2"/>
                                    <text x="320" y="135" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">Blocked (Needs Pump)</text>
                                `}
                            </svg>
                        </div>

                        <div class="text-[11px] text-center font-mono text-cyan-300">
                            <strong>Selective Permeability:</strong> Lipid bilayer allows small non-polar molecules through, while channel proteins transport ions and water.
                        </div>
                    </div>
                `;
            }

            window.sim4Set = function(m) {
                activeMol = m;
                playTone(m === 'o2' ? 600 : m === 'water' ? 500 : 350, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 5: Plant Cell Turgor vs Animal RBC Osmotic Rupture Simulator
        function renderSim5(vp) {
            let tonicity = 'hypo'; // 'hypo', 'iso', 'hyper'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Tonicity Controls -->
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">External Solution:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim5Set('hypo')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${tonicity === 'hypo' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Hypotonic (Pure Water)
                                </button>
                                <button onclick="window.sim5Set('iso')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${tonicity === 'iso' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Isotonic (0.9% Salt)
                                </button>
                                <button onclick="window.sim5Set('hyper')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${tonicity === 'hyper' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Hypertonic (Brine)
                                </button>
                            </div>
                        </div>

                        <!-- Side by Side Osmotic Response -->
                        <div class="grid grid-cols-2 gap-3 p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <!-- Animal RBC -->
                            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col items-center gap-2">
                                <span class="text-xs font-bold text-rose-400 font-mono">Animal RBC (No Cell Wall)</span>
                                <div class="w-28 h-32 flex items-center justify-center">
                                    ${tonicity === 'hypo' ? `
                                        <div class="text-center">
                                            <div class="w-16 h-16 rounded-full bg-rose-500/20 border-2 border-dashed border-rose-400 animate-ping"></div>
                                            <span class="text-[10px] font-mono text-rose-400 font-bold block mt-2">BURSTS! (Lysis)</span>
                                        </div>
                                    ` : tonicity === 'iso' ? `
                                        <div class="w-14 h-14 rounded-full bg-rose-600 border border-rose-400 shadow-md"></div>
                                    ` : `
                                        <div class="w-10 h-10 rounded-xl bg-rose-700 border border-rose-500 transform rotate-45"></div>
                                    `}
                                </div>
                                <span class="text-[10px] font-mono text-slate-400">${tonicity === 'hypo' ? 'Endosmosis ruptures membrane' : tonicity === 'iso' ? 'Normal biconcave disc' : 'Crenates & shrivels'}</span>
                            </div>

                            <!-- Plant Cell -->
                            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col items-center gap-2">
                                <span class="text-xs font-bold text-emerald-400 font-mono">Plant Cell (Cellulose Wall)</span>
                                <div class="w-28 h-32 flex items-center justify-center">
                                    <div class="w-24 h-28 rounded-xl border-4 border-emerald-500 bg-emerald-900/20 relative flex items-center justify-center p-2">
                                        <div class="rounded-lg transition-all duration-500 ${tonicity === 'hypo' ? 'w-20 h-24 bg-teal-500/50 border border-teal-300' : tonicity === 'iso' ? 'w-16 h-20 bg-teal-500/30' : 'w-10 h-14 bg-teal-500/20 border border-rose-500'}"></div>
                                    </div>
                                </div>
                                <span class="text-[10px] font-mono text-slate-400">${tonicity === 'hypo' ? 'Turgid! Wall pressure stops lysis' : tonicity === 'iso' ? 'Flaccid' : 'Plasmolysed!'}</span>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim5Set = function(t) {
                tonicity = t;
                playTone(t === 'hypo' ? 580 : t === 'iso' ? 440 : 300, 0.1, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 6: Interactive Diffusion vs Osmosis Chamber & Dynamic Equilibrium Studio
        function renderSim6(vp) {
            let mode = 'osmosis'; // 'diffusion' or 'osmosis'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Passive Transport Mechanism:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim6Set('diffusion')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'diffusion' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Gas/Solute Diffusion
                                </button>
                                <button onclick="window.sim6Set('osmosis')" class="px-3 py-1 rounded-lg text-xs font-bold transition ${mode === 'osmosis' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Water Osmosis
                                </button>
                            </div>
                        </div>

                        <!-- Chamber Visualization -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="360" height="150" viewBox="0 0 360 150">
                                <!-- Outer Beaker -->
                                <rect x="40" y="20" width="280" height="110" rx="6" fill="#0f172a" stroke="#475569" stroke-width="2"/>

                                <!-- Center Semipermeable Membrane -->
                                <line x1="180" y1="20" x2="180" y2="130" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4"/>
                                <text x="180" y="15" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">Semipermeable Barrier</text>

                                <!-- Left Chamber Particles -->
                                ${Array(mode === 'osmosis' ? 14 : 20).fill(0).map((_, i) => `
                                    <circle cx="${60 + (i % 5) * 22}" cy="${40 + Math.floor(i / 5) * 22}" r="3.5" fill="${mode === 'osmosis' ? '#38bdf8' : '#22c55e'}"/>
                                `).join('')}

                                <!-- Right Chamber Particles -->
                                ${Array(mode === 'osmosis' ? 6 : 4).fill(0).map((_, i) => `
                                    <circle cx="${210 + (i % 3) * 25}" cy="${50 + Math.floor(i / 3) * 25}" r="3.5" fill="${mode === 'osmosis' ? '#38bdf8' : '#22c55e'}"/>
                                `).join('')}

                                <!-- Flow Arrow -->
                                <path d="M140,80 L220,80" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                            </svg>
                        </div>

                        <div class="text-[11px] text-center font-mono text-slate-300">
                            ${mode === 'diffusion' ?
                                'Diffusion: Any solute/gas moves from high to low concentration across all space.' :
                                'Osmosis: Water specifically moves across a semipermeable membrane toward higher solute concentration.'}
                        </div>
                    </div>
                `;
            }

            window.sim6Set = function(m) {
                mode = m;
                playTone(m === 'diffusion' ? 500 : 400, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 7: Interactive Rheo Leaf Plasmolysis & Osmotic Tonicity Studio
        function renderSim7(vp) {
            let isPlasmolysed = false;

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Rheo Leaf Epidermis:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim7Toggle(false)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${!isPlasmolysed ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Pure Water (Turgid)
                                </button>
                                <button onclick="window.sim7Toggle(true)" class="px-3 py-1 rounded-lg text-xs font-bold transition ${isPlasmolysed ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Concentrated Sugar (Plasmolysis)
                                </button>
                            </div>
                        </div>

                        <!-- Microscopic Cell View -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex justify-center">
                            <div class="w-64 h-36 rounded-2xl border-4 border-emerald-600 bg-emerald-950/20 relative flex items-center justify-center p-2">
                                <!-- Cell Wall Label -->
                                <span class="absolute top-1 left-2 font-mono text-[9px] text-emerald-400 font-bold">Cellulose Cell Wall</span>

                                <!-- Living Protoplast (Purple with anthocyanin) -->
                                <div class="rounded-xl bg-purple-600/70 border border-purple-400 flex items-center justify-center transition-all duration-700 ${isPlasmolysed ? 'w-28 h-20 shadow-2xl scale-75' : 'w-56 h-28'}">
                                    <span class="font-mono text-[10px] text-white font-bold">${isPlasmolysed ? 'Shrunken Protoplast' : 'Turgid Protoplast (Full)'}</span>
                                </div>
                            </div>
                        </div>

                        <div class="text-[11px] text-center font-mono ${isPlasmolysed ? 'text-rose-400' : 'text-emerald-400'}">
                            ${isPlasmolysed ?
                                'Plasmolysis: Exosmosis pulls water out; living protoplast contracts away from the rigid wall!' :
                                'De-plasmolysed: Water re-enters via endosmosis; vacuole expands fully against cell wall.'}
                        </div>
                    </div>
                `;
            }

            window.sim7Toggle = function(flag) {
                isPlasmolysed = flag;
                playTone(flag ? 320 : 560, 0.12, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 8: Virtual Slide Preparation & Coverslip Air-Bubble Simulator
        function renderSim8(vp) {
            let angle = 45;

            function draw() {
                const hasBubbles = angle < 30;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 space-y-1">
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-white font-bold">Coverslip Lowering Angle: ${angle}°</span>
                                <span class="${hasBubbles ? 'text-rose-400' : 'text-emerald-400'} font-bold">
                                    ${hasBubbles ? 'Warning: Air Bubbles Trapped!' : 'Ideal Angle (No Bubbles)'}
                                </span>
                            </div>
                            <input type="range" min="10" max="80" value="${angle}"
                                   oninput="window.sim8Set(this.value)"
                                   class="w-full accent-emerald-500 h-1.5 bg-slate-700 rounded cursor-pointer">
                        </div>

                        <!-- Microscopic Result -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around">
                            <div class="w-36 h-36 rounded-full border-4 border-slate-700 bg-slate-900 overflow-hidden relative flex items-center justify-center">
                                <!-- Rectangular Onion Cells -->
                                <div class="grid grid-cols-3 gap-0.5 opacity-70">
                                    ${Array(9).fill(0).map(()=>`
                                        <div class="w-10 h-10 border border-rose-500/60 bg-rose-950/40 flex items-center justify-center">
                                            <div class="w-2 h-2 rounded-full bg-rose-400"></div>
                                        </div>
                                    `).join('')}
                                </div>

                                <!-- Trapped Air Bubbles (Black Rings) -->
                                ${hasBubbles ? `
                                    <div class="absolute w-8 h-8 rounded-full border-4 border-slate-950 bg-slate-800/40 top-4 left-6 animate-pulse"></div>
                                    <div class="absolute w-6 h-6 rounded-full border-4 border-slate-950 bg-slate-800/40 bottom-6 right-8 animate-pulse"></div>
                                ` : ''}
                            </div>

                            <div class="space-y-1 text-xs">
                                <span class="text-[10px] text-slate-400 uppercase font-mono">Golden Rule of Mounting:</span>
                                <p class="text-[11px] text-slate-300 max-w-[180px] leading-relaxed">
                                    Lower the coverslip gently with a mounting needle at 45° to allow liquid to spread smoothly without trapping circular air bubbles.
                                </p>
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim8Set = function(val) {
                angle = parseInt(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 9: Interactive Nucleus & Chromatin-to-Chromosome Condensation Engine
        function renderSim9(vp) {
            let stage = 0; // 0: chromatin, 1: prophase, 2: metaphase

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Chromatin Condensation:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim9Set(0)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${stage === 0 ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Interphase Chromatin
                                </button>
                                <button onclick="window.sim9Set(1)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${stage === 1 ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Prophase Coiling
                                </button>
                                <button onclick="window.sim9Set(2)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${stage === 2 ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Metaphase Chromosome
                                </button>
                            </div>
                        </div>

                        <!-- Nucleus Canvas -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex justify-center">
                            <div class="w-64 h-36 rounded-full border-4 border-indigo-500 bg-indigo-950/30 relative flex items-center justify-center overflow-hidden">
                                <span class="absolute top-1 text-[8px] font-mono text-indigo-400">Nuclear Envelope & Pores</span>

                                ${stage === 0 ? `
                                    <!-- Entangled Chromatin Thread -->
                                    <svg width="200" height="100" viewBox="0 0 200 100" class="opacity-80">
                                        <path d="M20,50 Q60,10 100,50 T180,50 Q140,90 100,50 T20,50" fill="none" stroke="#a855f7" stroke-width="2"/>
                                    </svg>
                                    <span class="absolute bottom-2 font-mono text-[9px] text-purple-300 font-bold">Diffuse DNA + Histones</span>
                                ` : stage === 1 ? `
                                    <!-- Tightening Chromatin -->
                                    <svg width="200" height="100" viewBox="0 0 200 100">
                                        <path d="M40,30 Q60,70 80,30 M120,30 Q140,70 160,30" fill="none" stroke="#06b6d4" stroke-width="4"/>
                                    </svg>
                                ` : `
                                    <!-- X-shaped Metaphase Chromosomes -->
                                    <div class="flex gap-4 items-center">
                                        <div class="w-8 h-14 relative flex items-center justify-center font-black text-amber-400 text-3xl font-mono">
                                            X
                                        </div>
                                        <div class="w-8 h-14 relative flex items-center justify-center font-black text-amber-400 text-3xl font-mono">
                                            X
                                        </div>
                                    </div>
                                    <span class="absolute bottom-2 font-mono text-[9px] text-amber-400 font-bold">Distinct Condensed Chromosomes</span>
                                `}
                            </div>
                        </div>

                        <div class="text-[11px] text-center font-mono text-slate-300">
                            DNA wraps around histone proteins to form chromatin, which condenses into rod-shaped chromosomes during division.
                        </div>
                    </div>
                `;
            }

            window.sim9Set = function(s) {
                stage = s;
                playTone(400 + s * 60, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 10: Interactive 3D Mitochondrion & Cristae ATP Generator
        function renderSim10(vp) {
            let fuelLevel = 80;

            function draw() {
                const atpRate = Math.round(fuelLevel * 0.36);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 space-y-1">
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-white font-bold">Substrate & O₂ Fuel: ${fuelLevel}%</span>
                                <span class="text-amber-400 font-bold">ATP Output: ~${atpRate} ATP / sec</span>
                            </div>
                            <input type="range" min="10" max="100" value="${fuelLevel}"
                                   oninput="window.sim10Set(this.value)"
                                   class="w-full accent-amber-500 h-1.5 bg-slate-700 rounded cursor-pointer">
                        </div>

                        <!-- 3D Cutaway Mitochondrion -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <svg width="340" height="150" viewBox="0 0 340 150">
                                <!-- Outer Membrane -->
                                <rect x="30" y="25" width="280" height="100" rx="50" fill="#78350f" fill-opacity="0.4" stroke="#d97706" stroke-width="2.5"/>

                                <!-- Inner Folded Cristae -->
                                <path d="M60,75 C70,40 90,40 100,75 C110,110 130,110 140,75 C150,40 170,40 180,75 C190,110 210,110 220,75 C230,40 250,40 260,75 C270,110 280,110 290,75" fill="none" stroke="#f59e0b" stroke-width="4"/>

                                <!-- Matrix mtDNA loop -->
                                <circle cx="80" cy="85" r="5" fill="none" stroke="#10b981" stroke-width="1.5"/>

                                <!-- Glowing ATP Coins -->
                                ${Array(Math.floor(fuelLevel / 20)).fill(0).map((_, i) => `
                                    <circle cx="${120 + i * 35}" cy="50" r="5" fill="#facc15" stroke="#ffffff" stroke-width="1" class="animate-ping"/>
                                `).join('')}
                            </svg>
                        </div>

                        <div class="text-[11px] text-center font-mono text-emerald-400">
                            <strong>Semi-Autonomous:</strong> Contains its own circular mtDNA and 70S ribosomes. Cristae maximize ATP synthesis surface area!
                        </div>
                    </div>
                `;
            }

            window.sim10Set = function(val) {
                fuelLevel = parseInt(val);
                draw();
            };
            draw();
        }

        // SIMULATOR 11: Interactive Chloroplast Anatomy & Plastid Transformation Studio
        function renderSim11(vp) {
            let plastidType = 'chloro'; // 'leuco', 'chloro', 'chromo'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Plastid Differentiation:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim11Set('leuco')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${plastidType === 'leuco' ? 'bg-slate-200 text-slate-950 font-black' : 'bg-slate-800 text-slate-400'}">
                                    Leucoplast (Starch)
                                </button>
                                <button onclick="window.sim11Set('chloro')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${plastidType === 'chloro' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Chloroplast (Solar)
                                </button>
                                <button onclick="window.sim11Set('chromo')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${plastidType === 'chromo' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Chromoplast (Pigment)
                                </button>
                            </div>
                        </div>

                        <!-- Cutaway Plastid -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex justify-center">
                            <div class="w-64 h-36 rounded-full border-4 relative flex items-center justify-center transition-all duration-500
                                        ${plastidType === 'leuco' ? 'border-slate-400 bg-slate-900/80' : plastidType === 'chloro' ? 'border-emerald-500 bg-emerald-950/40 glow-emerald' : 'border-rose-500 bg-rose-950/40 glow-rose'}">

                                ${plastidType === 'chloro' ? `
                                    <!-- Thylakoid Grana Stacks -->
                                    <div class="flex gap-4">
                                        ${[1, 2, 3].map(()=>`
                                            <div class="flex flex-col gap-1">
                                                <div class="w-6 h-2 rounded bg-emerald-400 shadow"></div>
                                                <div class="w-6 h-2 rounded bg-emerald-400 shadow"></div>
                                                <div class="w-6 h-2 rounded bg-emerald-400 shadow"></div>
                                            </div>
                                        `).join('')}
                                    </div>
                                    <span class="absolute bottom-2 font-mono text-[9px] text-emerald-300 font-bold">Grana + Stroma</span>
                                ` : plastidType === 'leuco' ? `
                                    <span class="font-mono text-xs text-slate-300 font-bold">Starch Amyloplast Grains</span>
                                ` : `
                                    <span class="font-mono text-xs text-rose-300 font-bold">Carotenoid Pigments</span>
                                `}
                            </div>
                        </div>
                    </div>
                `;
            }

            window.sim11Set = function(t) {
                plastidType = t;
                playTone(t === 'chloro' ? 560 : t === 'leuco' ? 440 : 620, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 12: Interactive Endomembrane Transport Factory & Lysosome Autophagy Engine
        function renderSim12(vp) {
            let step = 0; // 0: RER, 1: Golgi, 2: Lysosome

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Endomembrane Traffic:</span>
                            <div class="flex gap-1.5">
                                <button onclick="window.sim12Set(0)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${step === 0 ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}">1. RER</button>
                                <button onclick="window.sim12Set(1)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${step === 1 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}">2. Golgi</button>
                                <button onclick="window.sim12Set(2)" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${step === 2 ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}">3. Lysosome</button>
                            </div>
                        </div>

                        <!-- Transport Pathway Display -->
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-around">
                            <div class="p-2 rounded-xl border transition ${step === 0 ? 'border-indigo-400 bg-indigo-950/60 font-bold text-indigo-300' : 'border-slate-800 text-slate-500'}">
                                RER (Ribosomes)
                            </div>
                            <span class="text-slate-600">→</span>
                            <div class="p-2 rounded-xl border transition ${step === 1 ? 'border-amber-400 bg-amber-950/60 font-bold text-amber-300' : 'border-slate-800 text-slate-500'}">
                                Golgi Apparatus
                            </div>
                            <span class="text-slate-600">→</span>
                            <div class="p-2 rounded-xl border transition ${step === 2 ? 'border-rose-400 bg-rose-950/60 font-bold text-rose-300' : 'border-slate-800 text-slate-500'}">
                                Lysosome / Suicide Bag
                            </div>
                        </div>

                        <div class="text-[11px] text-center font-mono text-slate-300">
                            ${step === 0 ? 'RER synthesizes proteins; SER synthesizes lipids for membrane biogenesis.' :
                              step === 1 ? 'Golgi modifies, sorts, and packages ER products into transport vesicles.' :
                              'Lysosomes carry digestive hydrolytic enzymes for waste disposal and autolysis.'}
                        </div>
                    </div>
                `;
            }

            window.sim12Set = function(s) {
                step = s;
                playTone(450 + s * 70, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 13: Interactive Vacuolar Turgidity & Biomolecule Molecular Palette
        function renderSim13(vp) {
            let bioType = 'proteins';

            const biomolecules = {
                proteins: { name: 'Proteins', role: 'Enzymes, cytoskeletal filaments, transport pumps, receptors.' },
                lipids: { name: 'Lipids', role: 'Phospholipid bilayer, steroid hormones, hydrophobic barrier.' },
                carbs: { name: 'Carbohydrates', role: 'Cellulose cell wall, glucose cellular fuel, glycoproteins.' },
                nucleic: { name: 'Nucleic Acids', role: 'DNA genetic blueprints, RNA protein translation.' }
            };

            function draw() {
                const info = biomolecules[bioType];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-4 gap-1.5 text-xs">
                            ${Object.keys(biomolecules).map(k => `
                                <button onclick="window.sim13Set('${k}')" class="p-1.5 rounded-lg border transition ${bioType === k ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-900 border-slate-800 text-slate-400 hover:bg-slate-800'}">
                                    ${biomolecules[k].name}
                                </button>
                            `).join('')}
                        </div>

                        <!-- Biomolecule Card -->
                        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                            <span class="text-xs font-bold text-emerald-400 font-mono uppercase">${info.name} in Cellular Architecture</span>
                            <p class="text-xs text-slate-200 leading-relaxed">${info.role}</p>
                        </div>
                    </div>
                `;
            }

            window.sim13Set = function(k) {
                bioType = k;
                playTone(500, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 14: Mitosis vs Meiosis Chromosome Tracker & Oncogenic Tumor Simulator
        function renderSim14(vp) {
            let divType = 'mitosis'; // 'mitosis', 'meiosis', 'cancer'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Division Mode:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim14Set('mitosis')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${divType === 'mitosis' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Mitosis (2n → 2n)
                                </button>
                                <button onclick="window.sim14Set('meiosis')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${divType === 'meiosis' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Meiosis (2n → n)
                                </button>
                                <button onclick="window.sim14Set('cancer')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${divType === 'cancer' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Cancer (Unregulated)
                                </button>
                            </div>
                        </div>

                        <!-- Division Diagram -->
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-around min-h-[140px]">
                            ${divType === 'mitosis' ? `
                                <div class="text-center font-mono">
                                    <div class="w-12 h-12 mx-auto rounded-full bg-cyan-600/40 border border-cyan-400 flex items-center justify-center font-bold text-xs">2n=46</div>
                                    <span class="text-[9px] text-slate-400 mt-1 block">Parent Cell</span>
                                </div>
                                <span class="text-cyan-400">→</span>
                                <div class="flex gap-3 font-mono">
                                    <div class="w-10 h-10 rounded-full bg-cyan-600/40 border border-cyan-400 flex items-center justify-center font-bold text-[10px]">2n=46</div>
                                    <div class="w-10 h-10 rounded-full bg-cyan-600/40 border border-cyan-400 flex items-center justify-center font-bold text-[10px]">2n=46</div>
                                </div>
                            ` : divType === 'meiosis' ? `
                                <div class="text-center font-mono">
                                    <div class="w-12 h-12 mx-auto rounded-full bg-amber-600/40 border border-amber-400 flex items-center justify-center font-bold text-xs">2n=46</div>
                                </div>
                                <span class="text-amber-400">→</span>
                                <div class="grid grid-cols-2 gap-2 font-mono">
                                    ${Array(4).fill(0).map(()=>`
                                        <div class="w-8 h-8 rounded-full bg-amber-600/40 border border-amber-400 flex items-center justify-center font-bold text-[9px]">n=23</div>
                                    `).join('')}
                                </div>
                            ` : `
                                <div class="flex flex-wrap gap-1 max-w-[180px] justify-center animate-pulse">
                                    ${Array(12).fill(0).map(()=>`
                                        <div class="w-6 h-6 rounded-full bg-rose-600 border border-rose-400 shadow"></div>
                                    `).join('')}
                                </div>
                            `}
                        </div>

                        <div class="text-[11px] text-center font-mono text-slate-300">
                            ${divType === 'mitosis' ? 'Mitosis yields 2 identical diploid somatic cells for growth and tissue repair.' :
                              divType === 'meiosis' ? 'Meiosis yields 4 genetically diverse haploid gametes via crossing over.' :
                              'Cancer: Failed cell cycle checkpoints cause rapid, uncontrolled proliferation forming tumors.'}
                        </div>
                    </div>
                `;
            }

            window.sim14Set = function(t) {
                divType = t;
                playTone(t === 'mitosis' ? 520 : t === 'meiosis' ? 620 : 250, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 15: Interactive Cytogenetics Karyotyper & Mitochondrial Dysfunction Analyzer
        function renderSim15(vp) {
            let tab = 'sharma'; // 'sharma' or 'leigh'

            function draw() {
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                            <span class="font-bold text-white">Case Studies & Indian Science:</span>
                            <div class="flex gap-2">
                                <button onclick="window.sim15Set('sharma')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${tab === 'sharma' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Prof. A.K. Sharma (Orcein)
                                </button>
                                <button onclick="window.sim15Set('leigh')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${tab === 'leigh' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                                    Leigh Syndrome (ATP Loss)
                                </button>
                            </div>
                        </div>

                        <!-- Content Card -->
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                            ${tab === 'sharma' ? `
                                <div class="space-y-1.5 text-xs">
                                    <div class="font-bold text-amber-400 font-mono">Father of Indian Cytogenetics: Prof. A.K. Sharma</div>
                                    <p class="text-[11px] text-slate-300 leading-relaxed">
                                        Pioneered chromosome staining and orcein banding techniques at Calcutta University, proving that repetitive heterochromatic DNA stabilizes chromosome structure.
                                    </p>
                                </div>
                            ` : `
                                <div class="space-y-2 text-xs">
                                    <div class="font-bold text-rose-400 font-mono">Leigh Syndrome (Mitochondrial Defect)</div>
                                    <div class="grid grid-cols-2 gap-2 text-center font-mono">
                                        <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                            <span class="text-[9px] text-emerald-400">Normal Cell ATP</span>
                                            <div class="text-base font-bold text-emerald-300">100%</div>
                                        </div>
                                        <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                            <span class="text-[9px] text-rose-400">Leigh Cell ATP</span>
                                            <div class="text-base font-bold text-rose-400">15%</div>
                                        </div>
                                    </div>
                                    <p class="text-[10px] text-slate-400">Collapsing oxidative phosphorylation starves brainstem and muscle cells.</p>
                                </div>
                            `}
                        </div>
                    </div>
                `;
            }

            window.sim15Set = function(t) {
                tab = t;
                playTone(t === 'sharma' ? 520 : 340, 0.08, 'sine');
                draw();
            };
            draw();
        }

        // SIMULATOR 16: Interactive Synthetic Cell Designer & Minimal Genome Builder
        function renderSim16(vp) {
            let modules = { metabolism: true, replication: true, membrane: true, unknown: false };

            function draw() {
                const isViable = modules.metabolism && modules.replication && modules.membrane && modules.unknown;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs">
                            <span class="font-bold text-white">JCVI-syn3.0 Minimal Genome Builder:</span>
                            <span class="font-mono text-[10px] ${isViable ? 'text-emerald-400 font-bold' : 'text-amber-400'}">
                                ${isViable ? '473 Essential Genes (Cell Viable!)' : 'Incomplete Genome (Non-Viable)'}
                            </span>
                        </div>

                        <!-- Module Toggles -->
                        <div class="grid grid-cols-2 gap-2 text-xs">
                            ${[
                                { id: 'metabolism', name: 'Metabolism (112 genes)' },
                                { id: 'replication', name: 'DNA Replication (84 genes)' },
                                { id: 'membrane', name: 'Lipid Membrane (56 genes)' },
                                { id: 'unknown', name: 'Unknown Function (149 genes)' }
                            ].map(m => `
                                <button onclick="window.sim16Toggle('${m.id}')" class="p-2 rounded-xl text-left border transition flex items-center justify-between ${modules[m.id] ? 'bg-cyan-950/80 border-cyan-500 text-cyan-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-500'}">
                                    <span class="text-[11px]">${m.name}</span>
                                    <i data-lucide="${modules[m.id] ? 'check' : 'plus'}" class="w-3.5 h-3.5"></i>
                                </button>
                            `).join('')}
                        </div>

                        <!-- Synthetic Cell Visualizer -->
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center">
                            <div class="w-28 h-28 rounded-full border-4 transition-all duration-500 flex items-center justify-center
                                        ${isViable ? 'border-emerald-500 bg-emerald-950/40 glow-emerald scale-110 animate-cell-pulse' : 'border-slate-700 bg-slate-900/40 opacity-40'}">
                                <span class="font-mono text-[10px] text-center font-bold ${isViable ? 'text-emerald-300' : 'text-slate-600'}">
                                    ${isViable ? 'SYNTHETIC CELL ALIVE!' : 'DORMANT VESICLE'}
                                </span>
                            </div>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }

            window.sim16Toggle = function(id) {
                modules[id] = !modules[id];
                playTone(modules[id] ? 580 : 350, 0.08, 'sine');
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
                narrationText = `Mastery Assessment Quiz ${currentSlideIndex - 15}. Test your understanding across the discovery of the cell, organelles, membrane dynamics, mitosis, and cytogenetics.`;
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

