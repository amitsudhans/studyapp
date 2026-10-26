# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 12
MENSURATION: AREA AND PERIMETER (Competencies CG-5, C-5.1, CG-9)
Generates public/animations/class9-mensuration.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_mensuration_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-mensuration.html"

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
    <title>NCERT Class 9 Mathematics • Mensuration Laboratory</title>
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
                        <span class="text-xs text-slate-400 font-medium">Chapter 12</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Mensuration: Area & Perimeter</span>
                        <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-normal">Interactive Lab</span>
                    </h1>
                </div>
            </div>

            <!-- Slide Progress & Navigation Controls -->
            <div class="flex items-center gap-3">
                <div class="hidden md:flex flex-col items-end mr-2">
                    <span id="slideIndicatorText" class="text-xs font-mono font-bold text-indigo-300">Slide 1 of 20</span>
                    <span id="slideCategoryText" class="text-[10px] text-slate-400">Boundary Metrics</span>
                </div>
                <button id="prevBtn" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 disabled:opacity-30 disabled:pointer-events-none transition border border-slate-700">
                    <i data-lucide="chevron-left" class="w-5 h-5"></i>
                </button>
                <div class="relative">
                    <button id="slidePickerBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 border border-slate-700 flex items-center gap-1.5">
                        <i data-lucide="layout-grid" class="w-4 h-4 text-indigo-400"></i>
                        <span id="currentSlideBtnNum">1</span>/20
                    </button>
                    <!-- Slide Dropdown / Grid -->
                    <div id="slidePickerMenu" class="hidden absolute right-0 mt-2 w-72 sm:w-80 p-3 rounded-2xl glass-panel border border-slate-700 shadow-2xl z-50">
                        <div class="text-xs font-bold text-slate-300 mb-2 px-1 flex items-center justify-between">
                            <span>JUMP TO SLIDE</span>
                            <span class="text-[10px] text-indigo-400">20 Total Slides</span>
                        </div>
                        <div id="slideGrid" class="grid grid-cols-5 gap-1.5 max-h-60 overflow-y-auto p-1">
                            <!-- Populated dynamically by JS -->
                        </div>
                    </div>
                </div>
                <button id="nextBtn" class="p-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white disabled:opacity-30 disabled:pointer-events-none transition shadow-lg shadow-indigo-600/30">
                    <i data-lucide="chevron-right" class="w-5 h-5"></i>
                </button>
            </div>
        </div>
        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-800/80 h-1 mt-3 rounded-full overflow-hidden">
            <div id="progressBar" class="bg-gradient-to-r from-indigo-500 via-sky-400 to-emerald-400 h-full w-[5%] transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Dynamic Workspace Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 flex flex-col gap-6">

        <!-- Top Row: Slide Header Banner & Teacher Avatar Control -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-stretch">
            <!-- Slide Meta Banner (8 cols) -->
            <div class="lg:col-span-8 glass-panel rounded-2xl p-5 flex flex-col justify-between border border-slate-800 relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 w-48 h-48 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none"></div>
                <div>
                    <div class="flex flex-wrap items-center gap-2 mb-2">
                        <span id="slideBadge" class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Competency CG-5</span>
                        <span id="slideSubBadge" class="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-slate-800 text-slate-300 border border-slate-700">Class 9 Mathematics</span>
                    </div>
                    <h2 id="slideTitle" class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-1">Perimeter of Shapes & Boundary Metrics</h2>
                    <p id="slideSubtitle" class="text-xs sm:text-sm text-indigo-300 font-medium">Defining the 1D Closed Contour Enclosing a 2D Planar Region</p>
                </div>
                <div class="mt-3 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
                    <span id="slideFocusLabel" class="flex items-center gap-1.5 text-slate-300">
                        <i data-lucide="compass" class="w-4 h-4 text-emerald-400"></i>
                        <span>Core Focus: Polygons, Boundary Unrolling & Rectilinear Enclosures</span>
                    </span>
                    <span class="font-mono text-[11px] text-slate-400 hidden sm:inline">NCERT Ch 12 • Mensuration</span>
                </div>
            </div>

            <!-- Prof. Sophia Voiceover & Avatar Card (4 cols) -->
            <div class="lg:col-span-4 glass-panel rounded-2xl p-4 flex flex-col justify-between border border-slate-800 relative">
                <div class="flex items-center gap-3">
                    <!-- SVG Avatar with animated mouth -->
                    <div id="avatarContainer" class="relative w-14 h-14 rounded-2xl bg-gradient-to-tr from-indigo-900 via-slate-800 to-indigo-700 border-2 border-indigo-400/30 p-1 flex items-center justify-center shrink-0 shadow-lg shadow-indigo-950/50">
                        <svg id="teacherSvg" viewBox="0 0 100 100" class="w-full h-full">
                            <!-- Background / Shoulders -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#4338ca"/>
                            <!-- Collar / Necklace -->
                            <path d="M42,78 L50,85 L58,78" fill="none" stroke="#fbbf24" stroke-width="2"/>
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
                        <p class="text-[11px] text-indigo-300 truncate">Audio Companion • En-US Narration</p>
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
                    <button id="stopSpeechBtn" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-rose-300 hover:text-rose-200 transition border border-slate-700">
                        <i data-lucide="square" class="w-4 h-4"></i>
                    </button>
                    <button id="speechSpeedBtn" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 text-[11px] font-mono font-bold transition border border-slate-700">
                        1.0x
                    </button>
                </div>
            </div>
        </div>

        <!-- Middle Row: Interactive Animation / Simulation Canvas + Dynamic Content Area -->
        <div id="contentSlideContainer" class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <!-- Left / Main Canvas: Interactive SVG Simulator (7 cols) -->
            <div class="lg:col-span-7 glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 flex flex-col gap-3 min-h-[460px]">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <div class="p-1.5 rounded-md bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
                            <i data-lucide="play-circle" class="w-4 h-4"></i>
                        </div>
                        <h3 id="simulatorHeading" class="text-xs sm:text-sm font-bold text-slate-200 uppercase tracking-wider">Interactive Simulator</h3>
                    </div>
                    <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded">Live Physics Canvas</span>
                </div>

                <!-- Simulation Display Viewport -->
                <div id="simulatorViewport" class="flex-1 w-full min-h-[360px] bg-slate-950/70 rounded-xl border border-slate-800/80 p-2 sm:p-4 relative flex flex-col justify-between overflow-hidden">
                    <!-- Dynamic Interactive SVG & HTML injected here -->
                </div>
            </div>

            <!-- Right Column: Structured Educational Theory + 2 In-Slide Checkpoints (5 cols) -->
            <div class="lg:col-span-5 flex flex-col gap-4">
                <!-- Theory & Key Formulas Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 flex flex-col gap-3">
                    <div class="flex items-center gap-2 border-b border-slate-800/80 pb-2.5">
                        <i data-lucide="book-open" class="w-4 h-4 text-indigo-400"></i>
                        <h3 class="text-xs sm:text-sm font-bold text-slate-200 uppercase tracking-wider">Concept Summary & Insights</h3>
                    </div>
                    <p id="slideSummaryText" class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                        <!-- Populated by JS -->
                    </p>

                    <div class="mt-2">
                        <h4 class="text-[11px] font-bold text-indigo-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-400"></i>
                            <span>Key Takeaways & Formulas</span>
                        </h4>
                        <ul id="slideKeyPointsList" class="space-y-1.5 text-xs text-slate-300">
                            <!-- Populated by JS -->
                        </ul>
                    </div>
                </div>

                <!-- In-Slide Checkpoints (2 Quick Concept Checks) -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 flex flex-col gap-3">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-2">
                        <div class="flex items-center gap-2">
                            <i data-lucide="help-circle" class="w-4 h-4 text-amber-400"></i>
                            <h3 class="text-xs sm:text-sm font-bold text-slate-200 uppercase tracking-wider">In-Slide Checkpoints</h3>
                        </div>
                        <span class="text-[10px] font-mono text-amber-400 bg-amber-500/10 border border-amber-500/20 px-2 py-0.5 rounded">2 Questions</span>
                    </div>

                    <div id="checkpointsContainer" class="flex flex-col gap-4">
                        <!-- Populated dynamically by JS -->
                    </div>
                </div>
            </div>
        </div>

        <!-- Dedicated Mastery Quiz Container (Slides 17, 18, 19, 20) -->
        <div id="quizSlideContainer" class="hidden flex-col gap-6">
            <!-- Quiz Header Banner -->
            <div class="glass-panel rounded-2xl p-6 border border-indigo-500/30 bg-gradient-to-r from-indigo-950/40 via-slate-900 to-slate-900">
                <div class="flex flex-wrap items-center justify-between gap-4">
                    <div>
                        <span id="quizBadge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Mastery Quiz Challenge</span>
                        <h2 id="quizTitle" class="text-2xl font-black text-white mt-2">Class 9 Mensuration Challenge</h2>
                        <p id="quizDesc" class="text-sm text-slate-300 mt-1">10 dedicated questions with instant scoring, feedback, and full step-by-step mathematical solutions.</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="p-3 rounded-xl bg-slate-800 border border-slate-700 text-center">
                            <span class="text-[10px] text-slate-400 block uppercase font-bold">Quiz Score</span>
                            <span id="quizScoreText" class="text-xl font-black text-emerald-400 font-mono">0 / 10</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quiz Questions Grid (10 Questions) -->
            <div id="quizQuestionsList" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Populated dynamically by JS -->
            </div>
        </div>

        <!-- Strict Last Slide Notice on Slide 20 -->
        <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-indigo-950/40 shadow-xl shadow-emerald-950/30">
            <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mb-3">
                <i data-lucide="check-check" class="w-8 h-8"></i>
            </div>
            <h3 class="text-xl font-bold text-white">Congratulations on Completing Chapter 12!</h3>
            <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
            <p class="text-xs sm:text-sm text-slate-400 mt-2 max-w-xl mx-auto">
                You have mastered boundary metrics, the constant ratio π and historical approximations, arc length, polygon areas, the triangle median theorem, Heron's formula, Baudhayana's squaring of rectangles, circle area derivations, sectors and segments, Brahmagupta's formula for cyclic quadrilaterals, generalisation hierarchies, and computational mensuration.
            </p>
            <div class="mt-4 flex flex-wrap justify-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=mathematics&class=class9" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition flex items-center gap-2">
                    <i data-lucide="layout-grid" class="w-4 h-4"></i>
                    <span>Return to Mathematics Curriculum</span>
                </a>
                <button onclick="window.location.reload()" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs transition border border-slate-700 flex items-center gap-2">
                    <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                    <span>Restart Laboratory</span>
                </button>
            </div>
        </div>

    </main>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="glass-panel w-full max-w-xl rounded-2xl border border-slate-700 shadow-2xl p-6 flex flex-col gap-4 animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2 text-indigo-400">
                    <i data-lucide="file-check-2" class="w-5 h-5"></i>
                    <h3 class="text-base font-bold text-white">Step-by-Step Mathematical Solution</h3>
                </div>
                <button onclick="window.closeSolutionModal()" class="p-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <div id="modalQuestionText" class="text-xs sm:text-sm font-semibold text-slate-200 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
                <!-- Question text -->
            </div>
            <div id="modalSolutionText" class="text-xs sm:text-sm text-slate-300 font-mono whitespace-pre-wrap leading-relaxed bg-slate-950/80 p-4 rounded-xl border border-slate-800/80 max-h-80 overflow-y-auto">
                <!-- Solution text -->
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
            } catch (e) {
                console.warn("Audio Context fallback unavailable:", e);
            }
        }

        // Initialize Slide Picker Dropdown
        function initSlidePicker() {
            const grid = document.getElementById('slideGrid');
            grid.innerHTML = '';
            for (let i = 0; i < 20; i++) {
                const btn = document.createElement('button');
                btn.className = `p-2 rounded-lg text-xs font-bold transition flex flex-col items-center justify-center ${
                    i === currentSlideIndex
                    ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/40 ring-2 ring-indigo-400'
                    : 'bg-slate-800/90 text-slate-300 hover:bg-slate-700'
                }`;
                btn.innerHTML = `<span>${i + 1}</span><span class="text-[9px] font-normal opacity-70">${i < 16 ? 'Lab' : 'Quiz'}</span>`;
                btn.onclick = () => {
                    goToSlide(i);
                    document.getElementById('slidePickerMenu').classList.add('hidden');
                };
                grid.appendChild(btn);
            }
        }

        document.getElementById('slidePickerBtn').addEventListener('click', () => {
            const menu = document.getElementById('slidePickerMenu');
            menu.classList.toggle('hidden');
        });

        // Speech Synthesis Controls
        function speakCurrentSlideNarration() {
            if (speechSynth.speaking) {
                speechSynth.cancel();
            }

            let text = "";
            if (currentSlideIndex < 16) {
                text = SLIDES[currentSlideIndex].narration;
            } else {
                const quiz = QUIZZES[currentSlideIndex - 16];
                text = `Welcome to ${quiz.title}. ${quiz.desc} Answer all ten questions and click View Solution for full steps.`;
            }

            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.rate = speechRate;
            currentUtterance.lang = 'en-US';

            const speakingPulse = document.getElementById('speakingPulse');
            const speakingDot = document.getElementById('speakingDot');
            const avatar = document.getElementById('avatarContainer');
            const status = document.getElementById('speechStatus');
            const btnLabel = document.getElementById('speechBtnLabel');

            currentUtterance.onstart = () => {
                isSpeaking = true;
                speakingPulse.classList.remove('hidden');
                speakingDot.classList.remove('hidden');
                avatar.classList.add('talking');
                status.textContent = "Speaking";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
                btnLabel.textContent = "Stop Explaining";
            };

            currentUtterance.onend = () => {
                isSpeaking = false;
                speakingPulse.classList.add('hidden');
                speakingDot.classList.add('hidden');
                avatar.classList.remove('talking');
                status.textContent = "Idle";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400";
                btnLabel.textContent = "Explain Slide";
            };

            currentUtterance.onerror = () => {
                isSpeaking = false;
                speakingPulse.classList.add('hidden');
                speakingDot.classList.add('hidden');
                avatar.classList.remove('talking');
                status.textContent = "Audio Fallback";
                status.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300";
                btnLabel.textContent = "Explain Slide";
                playTone(440, 0.3);
            };

            speechSynth.speak(currentUtterance);
        }

        document.getElementById('toggleSpeechBtn').addEventListener('click', () => {
            if (isSpeaking) {
                speechSynth.cancel();
                isSpeaking = false;
                document.getElementById('speakingPulse').classList.add('hidden');
                document.getElementById('speakingDot').classList.add('hidden');
                document.getElementById('avatarContainer').classList.remove('talking');
                document.getElementById('speechStatus').textContent = "Stopped";
                document.getElementById('speechBtnLabel').textContent = "Explain Slide";
            } else {
                speakCurrentSlideNarration();
            }
        });

        document.getElementById('pauseSpeechBtn').addEventListener('click', () => {
            if (speechSynth.speaking) {
                if (speechSynth.paused) {
                    speechSynth.resume();
                    document.getElementById('speechStatus').textContent = "Speaking";
                } else {
                    speechSynth.pause();
                    document.getElementById('speechStatus').textContent = "Paused";
                }
            }
        });

        document.getElementById('stopSpeechBtn').addEventListener('click', () => {
            if (speechSynth.speaking) {
                speechSynth.cancel();
                isSpeaking = false;
                document.getElementById('speakingPulse').classList.add('hidden');
                document.getElementById('speakingDot').classList.add('hidden');
                document.getElementById('avatarContainer').classList.remove('talking');
                document.getElementById('speechStatus').textContent = "Stopped";
                document.getElementById('speechBtnLabel').textContent = "Explain Slide";
            }
        });

        document.getElementById('speechSpeedBtn').addEventListener('click', () => {
            if (speechRate === 1.0) speechRate = 1.2;
            else if (speechRate === 1.2) speechRate = 0.8;
            else speechRate = 1.0;
            document.getElementById('speechSpeedBtn').textContent = speechRate.toFixed(1) + 'x';
            if (isSpeaking) {
                speechSynth.cancel();
                speakCurrentSlideNarration();
            }
        });

        // Navigation Controllers
        function goToSlide(index) {
            if (index < 0 || index >= 20) return;
            if (speechSynth.speaking) speechSynth.cancel();

            currentSlideIndex = index;
            renderCurrentSlide();
            initSlidePicker();
        }

        document.getElementById('prevBtn').addEventListener('click', () => {
            if (currentSlideIndex > 0) goToSlide(currentSlideIndex - 1);
        });

        const nextBtn = document.getElementById('nextBtn');
        nextBtn.addEventListener('click', () => {
            if (currentSlideIndex < 19) goToSlide(currentSlideIndex + 1);
        });

        // Core Render Function
        function renderCurrentSlide() {
            // Update Progress Bar & Counters
            const percent = ((currentSlideIndex + 1) / 20) * 100;
            document.getElementById('progressBar').style.width = `${percent}%`;
            document.getElementById('slideIndicatorText').textContent = `Slide ${currentSlideIndex + 1} of 20`;
            document.getElementById('currentSlideBtnNum').textContent = currentSlideIndex + 1;

            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Handle Slide 20 Specific Requirement
            const lastSlideNotice = document.getElementById('lastSlideNotice');
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
                // Content Slide Mode
                contentContainer.classList.remove('hidden');
                quizContainer.classList.add('hidden');

                const slide = SLIDES[currentSlideIndex];
                document.getElementById('slideCategoryText').textContent = slide.category;
                document.getElementById('slideBadge').textContent = slide.badge;
                document.getElementById('slideTitle').textContent = slide.title;
                document.getElementById('slideSubtitle').textContent = slide.subtitle;
                document.getElementById('simulatorHeading').textContent = slide.sim_title;
                document.getElementById('slideSummaryText').textContent = slide.summary;

                // Render Key Points
                const keyPointsList = document.getElementById('slideKeyPointsList');
                keyPointsList.innerHTML = slide.key_points.map(pt => `
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 mt-1.5 shrink-0"></span>
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
                document.getElementById('slideSubtitle').textContent = `10 Dedicated Questions • Questions ${ (currentSlideIndex - 16) * 10 + 1 } to ${ (currentSlideIndex - 16 + 1) * 10 }`;

                document.getElementById('quizBadge').textContent = quiz.badge;
                document.getElementById('quizTitle').textContent = quiz.title;
                document.getElementById('quizDesc').textContent = quiz.desc;

                renderQuizQuestions(quiz.questions);
            }

            // Re-render KaTeX math formulas across updated elements
            if (window.renderMathInElement) {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
            if (window.lucide) {
                lucide.createIcons();
            }
        }

        // Render In-Slide Checkpoints
        function renderCheckpoints(checkpoints) {
            const container = document.getElementById('checkpointsContainer');
            container.innerHTML = checkpoints.map((cp, idx) => `
                <div class="glass-card p-3 rounded-xl border border-slate-700/60 flex flex-col gap-2">
                    <p class="text-xs font-semibold text-slate-200">
                        <span class="text-indigo-400 font-bold">Q${idx + 1}:</span> ${cp.q}
                    </p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                        ${cp.options.map((opt, oIdx) => `
                            <button onclick="window.checkAnswer(this, ${currentSlideIndex}, ${idx}, ${oIdx}, ${cp.ans})"
                                    class="text-left px-2.5 py-1.5 rounded-lg text-[11px] font-medium bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700/80 transition flex items-center justify-between">
                                <span>${String.fromCharCode(65 + oIdx)}. ${opt}</span>
                                <span class="feedback-icon hidden"></span>
                            </button>
                        `).join('')}
                    </div>
                    <div id="cp-exp-${idx}" class="hidden p-2 rounded-lg text-[11px] bg-slate-900/90 border border-slate-700 text-slate-300">
                        <span class="font-bold text-emerald-400">Explanation:</span> ${cp.explanation}
                    </div>
                </div>
            `).join('');
        }

        window.checkAnswer = function(btn, slideIdx, cpIdx, selectedIdx, correctIdx) {
            const parent = btn.parentElement;
            const buttons = parent.querySelectorAll('button');
            buttons.forEach(b => b.disabled = true);

            const expBox = document.getElementById(`cp-exp-${cpIdx}`);
            if (expBox) expBox.classList.remove('hidden');

            if (selectedIdx === correctIdx) {
                btn.className = "text-left px-2.5 py-1.5 rounded-lg text-[11px] font-bold bg-emerald-600 text-white border border-emerald-400 shadow-md shadow-emerald-600/30 flex items-center justify-between";
                playTone(587.33, 0.2); // D5 success tone
            } else {
                btn.className = "text-left px-2.5 py-1.5 rounded-lg text-[11px] font-bold bg-rose-600 text-white border border-rose-400 flex items-center justify-between";
                buttons[correctIdx].className = "text-left px-2.5 py-1.5 rounded-lg text-[11px] font-bold bg-emerald-600/80 text-white border border-emerald-400 flex items-center justify-between";
                playTone(220, 0.25, 'sawtooth'); // Low alert tone
            }
        };

        // Render Quiz Questions (Slides 17–20)
        let quizAnswersState = {};

        function renderQuizQuestions(questions) {
            const list = document.getElementById('quizQuestionsList');
            const quizKey = `quiz_${currentSlideIndex}`;
            if (!quizAnswersState[quizKey]) quizAnswersState[quizKey] = Array(10).fill(null);

            list.innerHTML = questions.map((qObj, idx) => `
                <div class="glass-panel p-4 rounded-2xl border border-slate-800 flex flex-col justify-between gap-3">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-bold">Question ${idx + 1}</span>
                            <button onclick="window.openSolutionModal(${idx})" class="text-[11px] font-bold text-amber-400 hover:text-amber-300 flex items-center gap-1 transition">
                                <i data-lucide="eye" class="w-3.5 h-3.5"></i>
                                <span>View Solution</span>
                            </button>
                        </div>
                        <p class="text-xs sm:text-sm font-semibold text-slate-100">${qObj.q}</p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-1">
                        ${qObj.options.map((opt, oIdx) => `
                            <button onclick="window.selectQuizOption(this, ${idx}, ${oIdx}, ${qObj.ans})"
                                    class="text-left p-2.5 rounded-xl text-xs font-medium bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700 transition">
                                <span class="font-bold text-indigo-400 mr-1">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
                            </button>
                        `).join('')}
                    </div>
                </div>
            `).join('');

            updateQuizScoreDisplay();
        }

        window.selectQuizOption = function(btn, qIdx, selectedIdx, correctIdx) {
            const parent = btn.parentElement;
            const buttons = parent.querySelectorAll('button');
            buttons.forEach(b => b.disabled = true);

            const quizKey = `quiz_${currentSlideIndex}`;
            quizAnswersState[quizKey][qIdx] = (selectedIdx === correctIdx);

            if (selectedIdx === correctIdx) {
                btn.className = "text-left p-2.5 rounded-xl text-xs font-bold bg-emerald-600 text-white border border-emerald-400 shadow-lg shadow-emerald-600/30";
                playTone(523.25, 0.2);
            } else {
                btn.className = "text-left p-2.5 rounded-xl text-xs font-bold bg-rose-600 text-white border border-rose-400";
                buttons[correctIdx].className = "text-left p-2.5 rounded-xl text-xs font-bold bg-emerald-600/80 text-white border border-emerald-400";
                playTone(220, 0.3, 'sawtooth');
            }

            updateQuizScoreDisplay();
        };

        function updateQuizScoreDisplay() {
            const quizKey = `quiz_${currentSlideIndex}`;
            const state = quizAnswersState[quizKey] || [];
            const correctCount = state.filter(s => s === true).length;
            const answeredCount = state.filter(s => s !== null).length;
            const scoreDisplay = document.getElementById('quizScoreText');
            if (scoreDisplay) {
                scoreDisplay.textContent = `${correctCount} / 10`;
            }
        }

        window.openSolutionModal = function(qIdx) {
            const quiz = QUIZZES[currentSlideIndex - 16];
            const qObj = quiz.questions[qIdx];
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
                default: vp.innerHTML = `<div class="p-6 text-center text-slate-400">Simulator ready for Slide ${slideIndex + 1}</div>`;
            }

            if (window.lucide) lucide.createIcons();
        }

        // Sim 1: Polygon Boundary Unroller & Linear Meter
        function renderSim1(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <span class="text-slate-300 font-semibold">Select 2D Shape:</span>
                            <button id="sim1_tri" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Triangle</button>
                            <button id="sim1_rect" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Rectangle</button>
                            <button id="sim1_hex" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Hexagon</button>
                            <button id="sim1_L" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">L-Shape</button>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Unroll Boundary:</label>
                            <input type="range" id="sim1_unroll" min="0" max="100" value="0" class="w-28 accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim1_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim1_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let currentShape = 'tri';
            const triBtn = document.getElementById('sim1_tri');
            const rectBtn = document.getElementById('sim1_rect');
            const hexBtn = document.getElementById('sim1_hex');
            const lBtn = document.getElementById('sim1_L');
            const slider = document.getElementById('sim1_unroll');
            const svg = document.getElementById('sim1_svg');
            const readout = document.getElementById('sim1_readout');

            function update() {
                const unroll = parseFloat(slider.value) / 100;
                [triBtn, rectBtn, hexBtn, lBtn].forEach(b => b.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition");
                if (currentShape === 'tri') triBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                if (currentShape === 'rect') rectBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                if (currentShape === 'hex') hexBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                if (currentShape === 'L') lBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                let sides = [];
                let shapeName = "";
                if (currentShape === 'tri') {
                    sides = [12, 16, 20];
                    shapeName = "Right Triangle (Sides: 12, 16, 20 cm)";
                } else if (currentShape === 'rect') {
                    sides = [18, 10, 18, 10];
                    shapeName = "Rectangle (Length: 18 cm, Breadth: 10 cm)";
                } else if (currentShape === 'hex') {
                    sides = [8, 8, 8, 8, 8, 8];
                    shapeName = "Regular Hexagon (6 sides of 8 cm each)";
                } else {
                    sides = [8, 6, 3, 2, 5, 4];
                    shapeName = "Irregular L-Shaped Room (6 Boundary Segments)";
                }

                const totalPerimeter = sides.reduce((a, b) => a + b, 0);

                let svgContent = `
                    <!-- Ground Tape Ruler -->
                    <line x1="40" y1="210" x2="560" y2="210" stroke="#334155" stroke-width="3"/>
                    <text x="40" y="230" fill="#64748b" font-size="10" font-family="monospace">0 cm</text>
                    <text x="560" y="230" fill="#64748b" font-size="10" font-family="monospace" text-anchor="end">${totalPerimeter} cm</text>
                `;

                // Render shape on the left or morphed ribbon
                if (unroll === 0) {
                    if (currentShape === 'tri') {
                        svgContent += `
                            <polygon points="180,60 180,180 340,180" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="3"/>
                            <text x="160" y="125" fill="#a5b4fc" font-size="11" font-weight="bold">12 cm</text>
                            <text x="260" y="198" fill="#a5b4fc" font-size="11" font-weight="bold">16 cm</text>
                            <text x="275" y="115" fill="#38bdf8" font-size="11" font-weight="bold">20 cm</text>
                        `;
                    } else if (currentShape === 'rect') {
                        svgContent += `
                            <rect x="180" y="80" width="220" height="100" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="3"/>
                            <text x="290" y="70" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">18 cm</text>
                            <text x="410" y="135" fill="#6ee7b7" font-size="11" font-weight="bold">10 cm</text>
                        `;
                    } else if (currentShape === 'hex') {
                        svgContent += `
                            <polygon points="270,70 330,70 360,120 330,170 270,170 240,120" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="3"/>
                            <text x="300" y="125" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">6 × 8 cm</text>
                        `;
                    } else {
                        svgContent += `
                            <polygon points="200,70 320,70 320,130 260,130 260,180 200,180" fill="rgba(236,72,153,0.2)" stroke="#ec4899" stroke-width="3"/>
                            <text x="260" y="60" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">Composite L-Shape</text>
                        `;
                    }
                } else {
                    // Unrolled straight line tape
                    const startX = 40;
                    const maxLen = 500;
                    let currentX = startX;
                    const colors = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#38bdf8', '#8b5cf6'];

                    sides.forEach((s, idx) => {
                        const segW = (s / totalPerimeter) * maxLen * unroll;
                        const c = colors[idx % colors.length];
                        svgContent += `
                            <rect x="${currentX}" y="195" width="${segW}" height="15" fill="${c}" rx="2"/>
                            ${segW > 25 ? `<text x="${currentX + segW/2}" y="190" fill="${c}" font-size="10" font-weight="bold" text-anchor="middle">${s} cm</text>` : ''}
                        `;
                        currentX += segW;
                    });
                }

                svg.innerHTML = svgContent;
                readout.innerHTML = `
                    ${shapeName} • Perimeter <b>P = ${sides.join(' + ')} = ${totalPerimeter} cm</b> (Unrolled: ${(unroll * 100).toFixed(0)}%)
                `;
            }

            triBtn.onclick = () => { currentShape = 'tri'; update(); };
            rectBtn.onclick = () => { currentShape = 'rect'; update(); };
            hexBtn.onclick = () => { currentShape = 'hex'; update(); };
            lBtn.onclick = () => { currentShape = 'L'; update(); };
            slider.oninput = update;
            update();
        }

        // Sim 2: Rolling Circle Kinematic Unroller & Invariant C/d Meter
        function renderSim2(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Circle Radius (r):</label>
                            <input type="range" id="sim2_r" min="25" max="50" value="35" class="w-28 accent-indigo-500">
                            <span id="sim2_r_val" class="font-bold text-indigo-400 font-mono">35 px</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Roll Wheel:</label>
                            <input type="range" id="sim2_roll" min="0" max="360" value="0" class="w-32 accent-emerald-500">
                            <span id="sim2_roll_val" class="font-bold text-emerald-400 font-mono">0°</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim2_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim2_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const rSlider = document.getElementById('sim2_r');
            const rollSlider = document.getElementById('sim2_roll');
            const rVal = document.getElementById('sim2_r_val');
            const rollVal = document.getElementById('sim2_roll_val');
            const svg = document.getElementById('sim2_svg');
            const readout = document.getElementById('sim2_readout');

            function update() {
                const r = parseFloat(rSlider.value);
                const rollDeg = parseFloat(rollSlider.value);
                rVal.textContent = `${r} px`;
                rollVal.textContent = `${rollDeg}°`;

                const startX = 70;
                const groundY = 190;
                const d = 2 * r;
                const totalC = 2 * Math.PI * r;
                const distTraveled = (rollDeg / 360) * totalC;
                const currentCenterX = startX + distTraveled;
                const currentCenterY = groundY - r;

                // Angle in radians for rotation
                const angleRad = (rollDeg * Math.PI) / 180;
                // Marker point on rim
                const markerX = currentCenterX - r * Math.sin(angleRad);
                const markerY = currentCenterY + r * Math.cos(angleRad);

                svg.innerHTML = `
                    <!-- Ground Horizontal Line -->
                    <line x1="20" y1="${groundY}" x2="580" y2="${groundY}" stroke="#475569" stroke-width="3"/>
                    <!-- Traced rolled path -->
                    <line x1="${startX}" y1="${groundY}" x2="${currentCenterX}" y2="${groundY}" stroke="#10b981" stroke-width="4"/>

                    <!-- Complete Revolution Target Marker -->
                    <line x1="${startX + totalC}" y1="${groundY - 15}" x2="${startX + totalC}" y2="${groundY + 15}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                    <text x="${startX + totalC}" y="${groundY + 28}" fill="#f59e0b" font-size="10" font-family="monospace" text-anchor="middle">2πr = πd</text>

                    <!-- Rolling Circle -->
                    <circle cx="${currentCenterX}" cy="${currentCenterY}" r="${r}" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="3"/>
                    <circle cx="${currentCenterX}" cy="${currentCenterY}" r="3" fill="#6366f1"/>

                    <!-- Radius Spoke -->
                    <line x1="${currentCenterX}" y1="${currentCenterY}" x2="${markerX}" y2="${markerY}" stroke="#ec4899" stroke-width="2.5"/>
                    <circle cx="${markerX}" cy="${markerY}" r="5" fill="#ec4899"/>

                    <!-- Dimension Labels -->
                    <text x="${currentCenterX}" y="${currentCenterY - r - 8}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">d = ${d} px</text>
                    <text x="${(startX + currentCenterX) / 2}" y="${groundY - 8}" fill="#34d399" font-size="10" font-family="monospace" text-anchor="middle">${distTraveled.toFixed(1)} px</text>
                `;

                readout.innerHTML = `
                    Circumference <b>C = 2πr = ${(2 * Math.PI * r).toFixed(2)} px</b> | Diameter <b>d = ${d} px</b> | 
                    Invariant Ratio: <b>C / d = ${Math.PI.toFixed(6)}... = π</b>
                `;
            }

            rSlider.oninput = update;
            rollSlider.oninput = update;
            update();
        }

        // Sim 3: Archimedean Polygon Exhaustion & Multi-Civilisation Error Comparator
        function renderSim3(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Archimedes' Polygon Sides (n):</label>
                            <input type="range" id="sim3_n" min="1" max="5" value="1" step="1" class="w-28 accent-indigo-500">
                            <span id="sim3_n_val" class="font-bold text-indigo-400 font-mono">6 sides</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <span class="text-slate-400">Historical Comparison:</span>
                            <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold font-mono text-[10px]">Aryabhata: 3.1416</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim3_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim3_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim3_n');
            const nVal = document.getElementById('sim3_n_val');
            const svg = document.getElementById('sim3_svg');
            const readout = document.getElementById('sim3_readout');

            const sidesList = [6, 12, 24, 48, 96];

            function update() {
                const idx = parseInt(slider.value) - 1;
                const n = sidesList[idx];
                nVal.textContent = `${n} sides`;

                const Ox = 300, Oy = 125, R = 90;
                // Calculate inscribed and circumscribed polygon perimeter ratios
                const lowerPi = n * Math.sin(Math.PI / n);
                const upperPi = n * Math.tan(Math.PI / n);

                // Generate points
                let inPoints = [];
                let outPoints = [];
                for (let k = 0; k < n; k++) {
                    const angle = (2 * Math.PI * k) / n - Math.PI / 2;
                    const inX = Ox + R * Math.cos(angle);
                    const inY = Oy + R * Math.sin(angle);
                    inPoints.push(`${inX},${inY}`);

                    const outR = R / Math.cos(Math.PI / n);
                    const outX = Ox + outR * Math.cos(angle);
                    const outY = Oy + outR * Math.sin(angle);
                    outPoints.push(`${outX},${outY}`);
                }

                svg.innerHTML = `
                    <!-- Circumscribed Polygon (Outer Bound) -->
                    <polygon points="${outPoints.join(' ')}" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="2"/>
                    <!-- Target Perfect Circle -->
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                    <!-- Inscribed Polygon (Inner Bound) -->
                    <polygon points="${inPoints.join(' ')}" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="2"/>

                    <!-- Centre Point -->
                    <circle cx="${Ox}" cy="${Oy}" r="3" fill="#ffffff"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Ox + R}" y2="${Oy}" stroke="#a5b4fc" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="${Ox + R/2}" y="${Oy - 6}" fill="#a5b4fc" font-size="10" font-family="monospace">r</text>
                `;

                readout.innerHTML = `
                    Archimedes' Squeeze with <b>${n}-gon</b>: 
                    <span class="text-emerald-400">${lowerPi.toFixed(5)}</span> < <b>π</b> < <span class="text-amber-400">${upperPi.toFixed(5)}</span>
                    ${n === 96 ? ' • (Proved 223/71 < π < 22/7!)' : ''}
                `;
            }

            slider.oninput = update;
            update();
        }

        // Sim 4: Dynamic Arc Length & Sector Perimeter Simulator
        function renderSim4(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Central Angle (θ):</label>
                            <input type="range" id="sim4_theta" min="15" max="340" value="90" class="w-28 accent-indigo-500">
                            <span id="sim4_theta_val" class="font-bold text-indigo-400 font-mono">90°</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Radius (r):</label>
                            <input type="range" id="sim4_r" min="50" max="100" value="80" class="w-24 accent-emerald-500">
                            <span id="sim4_r_val" class="font-bold text-emerald-400 font-mono">80 cm</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim4_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim4_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const thetaSlider = document.getElementById('sim4_theta');
            const rSlider = document.getElementById('sim4_r');
            const thetaVal = document.getElementById('sim4_theta_val');
            const rVal = document.getElementById('sim4_r_val');
            const svg = document.getElementById('sim4_svg');
            const readout = document.getElementById('sim4_readout');

            function update() {
                const theta = parseFloat(thetaSlider.value);
                const r = parseFloat(rSlider.value);
                thetaVal.textContent = `${theta}°`;
                rVal.textContent = `${r} cm`;

                const Ox = 300, Oy = 125;
                const startAngle = 0;
                const endAngle = (theta * Math.PI) / 180;

                const Ax = Ox + r * Math.cos(startAngle);
                const Ay = Oy + r * Math.sin(startAngle);
                const Bx = Ox + r * Math.cos(endAngle);
                const By = Oy + r * Math.sin(endAngle);
                const largeArc = theta > 180 ? 1 : 0;

                const arcLen = (theta / 360) * 2 * Math.PI * r;
                const sectorPerimeter = arcLen + 2 * r;

                svg.innerHTML = `
                    <!-- Complete Circle Faint Outline -->
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>

                    <!-- Shaded Sector -->
                    <path d="M${Ox},${Oy} L${Ax},${Ay} A${r},${r} 0 ${largeArc},1 ${Bx},${By} Z" fill="rgba(99,102,241,0.2)"/>

                    <!-- Bounding Radii (Amber) -->
                    <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${Ay}" stroke="#f59e0b" stroke-width="3"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="3"/>

                    <!-- Highlighted Arc (Cyan/Emerald) -->
                    <path d="M${Ax},${Ay} A${r},${r} 0 ${largeArc},1 ${Bx},${By}" fill="none" stroke="#10b981" stroke-width="4"/>

                    <!-- Center & Vertices -->
                    <circle cx="${Ox}" cy="${Oy}" r="4" fill="#ffffff"/>
                    <circle cx="${Ax}" cy="${Ay}" r="4" fill="#10b981"/>
                    <circle cx="${Bx}" cy="${By}" r="4" fill="#10b981"/>

                    <!-- Labels -->
                    <text x="${Ox - 15}" y="${Oy - 5}" fill="#ffffff" font-size="11" font-weight="bold">O</text>
                    <text x="${Ox + r/2}" y="${Oy - 8}" fill="#f59e0b" font-size="10" font-weight="bold">r = ${r}</text>
                    <text x="${Bx + 8}" y="${By}" fill="#10b981" font-size="11" font-weight="bold">Arc l</text>
                `;

                readout.innerHTML = `
                    Arc Length <b>l = (θ/360°) × 2πr = ${arcLen.toFixed(1)} cm</b> | 
                    Total Sector Perimeter <b>P = l + 2r = ${sectorPerimeter.toFixed(1)} cm</b>
                `;
            }

            thetaSlider.oninput = update;
            rSlider.oninput = update;
            update();
        }

        // Sim 5: Shearing Transformation: Parallelogram to Rectangle & Triangle Doubling
        function renderSim5(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Shear Angle / Morph:</label>
                            <input type="range" id="sim5_shear" min="0" max="60" value="0" class="w-28 accent-indigo-500">
                            <span id="sim5_shear_val" class="font-bold text-indigo-400 font-mono">0°</span>
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim5_mode_para" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Parallelogram Shearing</button>
                            <button id="sim5_mode_tri" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Triangle Doubling</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim5_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim5_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = 'para';
            const shearSlider = document.getElementById('sim5_shear');
            const shearVal = document.getElementById('sim5_shear_val');
            const paraBtn = document.getElementById('sim5_mode_para');
            const triBtn = document.getElementById('sim5_mode_tri');
            const svg = document.getElementById('sim5_svg');
            const readout = document.getElementById('sim5_readout');

            function update() {
                const shear = parseFloat(shearSlider.value);
                shearVal.textContent = `${shear}°`;

                const b = 200;
                const h = 100;
                const baseY = 180;
                const topY = baseY - h;
                const shiftX = Math.tan((shear * Math.PI) / 180) * h;
                const leftX = 200;

                if (mode === 'para') {
                    svg.innerHTML = `
                        <!-- Sheared Parallelogram -->
                        <polygon points="${leftX},${baseY} ${leftX + b},${baseY} ${leftX + b + shiftX},${topY} ${leftX + shiftX},${topY}" 
                                 fill="rgba(99,102,241,0.25)" stroke="#6366f1" stroke-width="3"/>

                        <!-- Equivalent Base Rectangle Ghost -->
                        <rect x="${leftX}" y="${topY}" width="${b}" height="${h}" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>

                        <!-- Height Guide Line -->
                        <line x1="${leftX}" y1="${topY}" x2="${leftX}" y2="${baseY}" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,3"/>
                        <text x="${leftX - 15}" y="${topY + h/2}" fill="#f472b6" font-size="11" font-weight="bold">h = 10</text>
                        <text x="${leftX + b/2}" y="${baseY + 18}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">base = 20</text>
                    `;
                    readout.innerHTML = `
                        Cavalieri Shearing Principle: Base = 20 cm, Height = 10 cm ⇒ <b>Area = b × h = 200 cm²</b> (Identical to rectangle!)
                    `;
                } else {
                    svg.innerHTML = `
                        <!-- Triangle 1 -->
                        <polygon points="${leftX},${baseY} ${leftX + b},${baseY} ${leftX + shiftX},${topY}" 
                                 fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="3"/>
                        <!-- Inverted Congruent Triangle 2 Completing Parallelogram -->
                        <polygon points="${leftX + b},${baseY} ${leftX + b + shiftX},${topY} ${leftX + shiftX},${topY}" 
                                 fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>

                        <line x1="${leftX + shiftX}" y1="${topY}" x2="${leftX + shiftX}" y2="${baseY}" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,3"/>
                        <text x="${leftX + b/2}" y="${baseY + 18}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">base = 20</text>
                        <text x="${leftX + shiftX - 15}" y="${topY + h/2}" fill="#f472b6" font-size="11" font-weight="bold">h = 10</text>
                    `;
                    readout.innerHTML = `
                        Triangle Doubling: Parallelogram Area = 200 cm² ⇒ <b>Triangle Area = (1/2) × b × h = 100 cm²</b>
                    `;
                }
            }

            paraBtn.onclick = () => { mode = 'para'; paraBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition"; triBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition"; update(); };
            triBtn.onclick = () => { mode = 'tri'; triBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition"; paraBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition"; update(); };
            shearSlider.oninput = update;
            update();
        }

        // Sim 6: Interactive Triangle Median & Centroid Area Equalizer
        function renderSim6(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Skew Vertex A (X):</label>
                            <input type="range" id="sim6_skew" min="150" max="450" value="260" class="w-32 accent-indigo-500">
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim6_view_median" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">1 Median (2 Halves)</button>
                            <button id="sim6_view_centroid" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Centroid (3 Equal Areas)</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim6_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim6_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = 'median';
            const slider = document.getElementById('sim6_skew');
            const medBtn = document.getElementById('sim6_view_median');
            const cenBtn = document.getElementById('sim6_view_centroid');
            const svg = document.getElementById('sim6_svg');
            const readout = document.getElementById('sim6_readout');

            function update() {
                const Ax = parseFloat(slider.value);
                const Ay = 60;
                const Bx = 160, By = 190;
                const Cx = 440, Cy = 190;
                const Dx = (Bx + Cx) / 2, Dy = By; // Midpoint of BC = 300, 190

                const base = Cx - Bx; // 280
                const height = By - Ay; // 130
                const totalArea = (0.5 * base * height);

                if (mode === 'median') {
                    medBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    cenBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";

                    svg.innerHTML = `
                        <!-- Left Sub-Triangle ABD -->
                        <polygon points="${Ax},${Ay} ${Bx},${By} ${Dx},${Dy}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Right Sub-Triangle ACD -->
                        <polygon points="${Ax},${Ay} ${Dx},${Dy} ${Cx},${Cy}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>

                        <!-- Median AD -->
                        <line x1="${Ax}" y1="${Ay}" x2="${Dx}" y2="${Dy}" stroke="#f59e0b" stroke-width="3"/>

                        <!-- Shared Altitude -->
                        <line x1="${Ax}" y1="${Ay}" x2="${Ax}" y2="${By}" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,3"/>

                        <!-- Points -->
                        <circle cx="${Ax}" cy="${Ay}" r="5" fill="#f8fafc"/>
                        <circle cx="${Bx}" cy="${By}" r="5" fill="#f8fafc"/>
                        <circle cx="${Cx}" cy="${Cy}" r="5" fill="#f8fafc"/>
                        <circle cx="${Dx}" cy="${Dy}" r="5" fill="#f59e0b"/>

                        <text x="${Ax}" y="${Ay - 8}" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">A</text>
                        <text x="${Bx - 15}" y="${By + 5}" fill="#ffffff" font-size="12" font-weight="bold">B</text>
                        <text x="${Cx + 10}" y="${Cy + 5}" fill="#ffffff" font-size="12" font-weight="bold">C</text>
                        <text x="${Dx}" y="${Dy + 16}" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">D (Midpoint)</text>
                    `;
                    readout.innerHTML = `
                        Shared Altitude h = ${height} px | Equal Bases BD = DC = 140 px ⇒ 
                        <b>Area(ΔABD) = Area(ΔACD) = ${(totalArea / 2).toFixed(0)} px²</b> (Exactly 50% each!)
                    `;
                } else {
                    medBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    cenBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                    // Centroid G = (Ax + Bx + Cx)/3, (Ay + By + Cy)/3
                    const Gx = (Ax + Bx + Cx) / 3;
                    const Gy = (Ay + By + Cy) / 3;

                    svg.innerHTML = `
                        <!-- ΔGAB -->
                        <polygon points="${Ax},${Ay} ${Bx},${By} ${Gx},${Gy}" fill="rgba(99,102,241,0.25)" stroke="#6366f1" stroke-width="2"/>
                        <!-- ΔGBC -->
                        <polygon points="${Bx},${By} ${Cx},${Cy} ${Gx},${Gy}" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="2"/>
                        <!-- ΔGCA -->
                        <polygon points="${Cx},${Cy} ${Ax},${Ay} ${Gx},${Gy}" fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="2"/>

                        <!-- Centroid G -->
                        <circle cx="${Gx}" cy="${Gy}" r="6" fill="#ec4899"/>
                        <text x="${Gx + 10}" y="${Gy - 5}" fill="#f472b6" font-size="12" font-weight="bold">Centroid G</text>
                    `;
                    readout.innerHTML = `
                        Centroid Tripartition: <b>Area(ΔGAB) = Area(ΔGBC) = Area(ΔGCA) = ${(totalArea / 3).toFixed(0)} px²</b> (Exactly 1/3 each!)
                    `;
                }
            }

            medBtn.onclick = () => { mode = 'median'; update(); };
            cenBtn.onclick = () => { mode = 'centroid'; update(); };
            slider.oninput = update;
            update();
        }

        // Sim 7: Heron’s Formula Geometric Computer & Incircle Radius
        function renderSim7(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Side a:</label>
                            <input type="range" id="sim7_a" min="10" max="25" value="13" class="w-16 accent-indigo-500">
                            <span id="sim7_a_val" class="text-indigo-400 font-bold font-mono">13</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Side b:</label>
                            <input type="range" id="sim7_b" min="10" max="25" value="14" class="w-16 accent-emerald-500">
                            <span id="sim7_b_val" class="text-emerald-400 font-bold font-mono">14</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Side c:</label>
                            <input type="range" id="sim7_c" min="10" max="25" value="15" class="w-16 accent-amber-500">
                            <span id="sim7_c_val" class="text-amber-400 font-bold font-mono">15</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim7_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim7_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const aS = document.getElementById('sim7_a');
            const bS = document.getElementById('sim7_b');
            const cS = document.getElementById('sim7_c');
            const aV = document.getElementById('sim7_a_val');
            const bV = document.getElementById('sim7_b_val');
            const cV = document.getElementById('sim7_c_val');
            const svg = document.getElementById('sim7_svg');
            const readout = document.getElementById('sim7_readout');

            function update() {
                const a = parseFloat(aS.value);
                const b = parseFloat(bS.value);
                const c = parseFloat(cS.value);
                aV.textContent = a;
                bV.textContent = b;
                cV.textContent = c;

                // Triangle inequality check
                const isValid = (a + b > c) && (b + c > a) && (c + a > b);
                if (!isValid) {
                    svg.innerHTML = `<text x="300" y="125" fill="#f43f5e" font-size="14" font-weight="bold" text-anchor="middle">Triangle Inequality Violated! (a + b must be > c)</text>`;
                    readout.innerHTML = `<span class="text-rose-400">Cannot form a real triangle with these lengths.</span>`;
                    return;
                }

                const s = (a + b + c) / 2;
                const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
                const inradius = area / s;

                // Geometry coordinates for visualization
                const scale = 12;
                const Bx = 180, By = 190;
                const Cx = Bx + c * scale, Cy = By;
                const cosB = (a * a + c * c - b * b) / (2 * a * c);
                const sinB = Math.sqrt(Math.max(0, 1 - cosB * cosB));
                const Ax = Bx + a * scale * cosB;
                const Ay = By - a * scale * sinB;

                // Incenter coordinates
                const Ix = (a * Cx + b * Bx + c * Ax) / (a + b + c);
                const Iy = (a * Cy + b * By + c * Ay) / (a + b + c);

                svg.innerHTML = `
                    <!-- Triangle -->
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="3"/>

                    <!-- Incircle -->
                    <circle cx="${Ix}" cy="${Iy}" r="${inradius * scale}" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="2"/>
                    <circle cx="${Ix}" cy="${Iy}" r="3" fill="#10b981"/>

                    <!-- Vertices -->
                    <circle cx="${Ax}" cy="${Ay}" r="4" fill="#ffffff"/>
                    <circle cx="${Bx}" cy="${By}" r="4" fill="#ffffff"/>
                    <circle cx="${Cx}" cy="${Cy}" r="4" fill="#ffffff"/>

                    <!-- Labels -->
                    <text x="${Ax}" y="${Ay - 8}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">A</text>
                    <text x="${Bx - 12}" y="${By + 5}" fill="#ffffff" font-size="11" font-weight="bold">B</text>
                    <text x="${Cx + 12}" y="${Cy + 5}" fill="#ffffff" font-size="11" font-weight="bold">C</text>
                    <text x="${(Bx+Cx)/2}" y="${By + 18}" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">c = ${c}</text>
                `;

                readout.innerHTML = `
                    s = (${a}+${b}+${c})/2 = <b>${s.toFixed(1)}</b> | Radicand: ${s}(${s-a})(${s-b})(${s-c}) | 
                    <b>Area = ${area.toFixed(2)} cm²</b> | Inradius r_in = ${inradius.toFixed(2)} cm
                `;
            }

            aS.oninput = update;
            bS.oninput = update;
            cS.oninput = update;
            update();
        }

        // Sim 8: Baudhayana Sulbasutra 5-Step Rectangular Squaring Animation
        function renderSim8(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Baudhayana Sulbasutra Construction:</span>
                        <div class="flex items-center gap-1.5" id="sim8_steps">
                            <button data-step="1" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold transition">1. Rectangle</button>
                            <button data-step="2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">2. Cut Square</button>
                            <button data-step="3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">3. Bisect Strip</button>
                            <button data-step="4" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">4. Gnomon</button>
                            <button data-step="5" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">5. Square Side</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim8_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim8_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let step = 1;
            const buttons = document.querySelectorAll('#sim8_steps button');
            const svg = document.getElementById('sim8_svg');
            const readout = document.getElementById('sim8_readout');

            function update() {
                buttons.forEach(b => {
                    if (parseInt(b.dataset.step) === step) {
                        b.className = "px-2 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    } else {
                        b.className = "px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    }
                });

                const a = 180, b = 80;
                const Ox = 200, Oy = 70;

                if (step === 1) {
                    svg.innerHTML = `
                        <rect x="${Ox}" y="${Oy}" width="${a}" height="${b}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="3"/>
                        <text x="${Ox + a/2}" y="${Oy - 10}" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Length a = 18</text>
                        <text x="${Ox - 15}" y="${Oy + b/2}" fill="#a5b4fc" font-size="12" font-weight="bold">b = 8</text>
                    `;
                    readout.innerHTML = `Step 1: Start with target rectangle of dimensions a = 18 and b = 8 (Area = 144).`;
                } else if (step === 2) {
                    svg.innerHTML = `
                        <rect x="${Ox}" y="${Oy}" width="${b}" height="${b}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="3"/>
                        <rect x="${Ox + b}" y="${Oy}" width="${a - b}" height="${b}" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                        <text x="${Ox + b/2}" y="${Oy + b/2}" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Square b × b</text>
                        <text x="${Ox + b + (a-b)/2}" y="${Oy + b/2}" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Strip (a - b)</text>
                    `;
                    readout.innerHTML = `Step 2: Cut a square of side b = 8 from the rectangle; excess strip has width (a - b) = 10.`;
                } else if (step === 3) {
                    svg.innerHTML = `
                        <rect x="${Ox}" y="${Oy}" width="${b}" height="${b}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="3"/>
                        <rect x="${Ox + b}" y="${Oy}" width="${(a - b)/2}" height="${b}" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                        <rect x="${Ox + b + (a - b)/2}" y="${Oy}" width="${(a - b)/2}" height="${b}" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                        <text x="${Ox + b + (a-b)/4}" y="${Oy + b/2}" fill="#f472b6" font-size="9" font-weight="bold" text-anchor="middle">Half 1</text>
                        <text x="${Ox + b + 3*(a-b)/4}" y="${Oy + b/2}" fill="#f472b6" font-size="9" font-weight="bold" text-anchor="middle">Half 2</text>
                    `;
                    readout.innerHTML = `Step 3: Bisect the remaining strip into two equal halves of width (a - b)/2 = 5.`;
                } else if (step === 4) {
                    svg.innerHTML = `
                        <rect x="${Ox}" y="${Oy + 50}" width="${b}" height="${b}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <!-- Side strip -->
                        <rect x="${Ox + b}" y="${Oy + 50}" width="50" height="${b}" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                        <!-- Top strip -->
                        <rect x="${Ox}" y="${Oy}" width="${b}" height="50" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                        <!-- Small corner square completing (a+b)/2 -->
                        <rect x="${Ox + b}" y="${Oy}" width="50" height="50" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
                        <text x="${Ox + b + 25}" y="${Oy + 30}" fill="#fcd34d" font-size="9" font-weight="bold" text-anchor="middle">[(a-b)/2]²</text>
                    `;
                    readout.innerHTML = `Step 4: Form L-gnomon of side (a + b)/2 = 13. Area = [(a+b)/2]² - [(a-b)/2]² = 13² - 5² = 144!`;
                } else {
                    svg.innerHTML = `
                        <!-- Final Equivalent Square -->
                        <rect x="240" y="60" width="120" height="120" fill="rgba(16,185,129,0.4)" stroke="#10b981" stroke-width="3"/>
                        <text x="300" y="125" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">Square Side x = √144 = 12</text>
                    `;
                    readout.innerHTML = `Step 5: By Baudhayana's Rope Theorem, x² = 13² - 5² = 12² ⇒ <b>Side x = √(ab) = 12 cm!</b>`;
                }
            }

            buttons.forEach(b => {
                b.onclick = () => { step = parseInt(b.dataset.step); update(); };
            });
            update();
        }

        // Sim 9: Interactive Sector Slicing to Rectangle & Archimedes Concentric Ring Unroller
        function renderSim9(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Sector Slices (N):</label>
                            <input type="range" id="sim9_n" min="4" max="64" value="8" step="4" class="w-28 accent-indigo-500">
                            <span id="sim9_n_val" class="font-bold text-indigo-400 font-mono">8 wedges</span>
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim9_btn_circle" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Pie Slicing</button>
                            <button id="sim9_btn_rings" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Archimedes' Rings</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim9_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim9_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let mode = 'pie';
            const slider = document.getElementById('sim9_n');
            const nVal = document.getElementById('sim9_n_val');
            const pieBtn = document.getElementById('sim9_btn_circle');
            const ringsBtn = document.getElementById('sim9_btn_rings');
            const svg = document.getElementById('sim9_svg');
            const readout = document.getElementById('sim9_readout');

            function update() {
                const n = parseInt(slider.value);
                nVal.textContent = `${n} wedges`;

                if (mode === 'pie') {
                    pieBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    ringsBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";

                    // Render pseudo-rectangle with n wedges
                    const wedgeW = 320 / n;
                    const h = 80;
                    let wedgesSvg = "";
                    for (let i = 0; i < n; i++) {
                        const x = 140 + i * wedgeW;
                        const isUp = (i % 2 === 0);
                        const c = isUp ? 'rgba(99,102,241,0.4)' : 'rgba(16,185,129,0.4)';
                        const stroke = isUp ? '#6366f1' : '#10b981';
                        wedgesSvg += `<polygon points="${x},${isUp ? 80 : 80+h} ${x + wedgeW},${isUp ? 80 : 80+h} ${x + wedgeW/2},${isUp ? 80+h : 80}" fill="${c}" stroke="${stroke}" stroke-width="1.5"/>`;
                    }

                    svg.innerHTML = `
                        <!-- Rearranged Wedges -->
                        ${wedgesSvg}
                        <!-- Dimension Annotations -->
                        <line x1="140" y1="65" x2="460" y2="65" stroke="#a5b4fc" stroke-width="2"/>
                        <text x="300" y="55" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Base = C / 2 = πr</text>
                        <line x1="120" y1="80" x2="120" y2="160" stroke="#f472b6" stroke-width="2"/>
                        <text x="105" y="125" fill="#f472b6" font-size="11" font-weight="bold">Height = r</text>
                    `;
                    readout.innerHTML = `
                        As N → ∞ (${n} slices): Base approaches <b>πr</b> and Height equals <b>r</b> ⇒ <b>Area = (πr) × r = πr²</b>!
                    `;
                } else {
                    pieBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    ringsBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                    svg.innerHTML = `
                        <!-- Concentric Circles unrolled into Right Triangle -->
                        <polygon points="150,180 450,180 150,80" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="3"/>
                        <text x="300" y="200" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Base = 2πr (Circumference)</text>
                        <text x="110" y="135" fill="#a5b4fc" font-size="11" font-weight="bold">Height = r</text>
                    `;
                    readout.innerHTML = `
                        Archimedes' Concentric Ring Method: Triangle of Base 2πr and Height r ⇒ <b>Area = (1/2) × 2πr × r = πr²</b>!
                    `;
                }
            }

            pieBtn.onclick = () => { mode = 'pie'; update(); };
            ringsBtn.onclick = () => { mode = 'rings'; update(); };
            slider.oninput = update;
            update();
        }

        // Sim 10: Multi-Civilisation Circle Area Comparator & Historical Error Dials
        function renderSim10(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Circle Diameter (d):</label>
                            <input type="range" id="sim10_d" min="10" max="30" value="18" class="w-28 accent-indigo-500">
                            <span id="sim10_d_val" class="font-bold text-indigo-400 font-mono">18 cm</span>
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px]">Egyptian Rhind Papyrus vs True πr²</span>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim10_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim10_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const dSlider = document.getElementById('sim10_d');
            const dVal = document.getElementById('sim10_d_val');
            const svg = document.getElementById('sim10_svg');
            const readout = document.getElementById('sim10_readout');

            function update() {
                const d = parseFloat(dSlider.value);
                const r = d / 2;
                dVal.textContent = `${d} cm`;

                const trueArea = Math.PI * r * r;
                // Egyptian rule: Area ≈ [(8/9) d]²
                const egyptianSide = (8 / 9) * d;
                const egyptianArea = egyptianSide * egyptianSide;
                const errorPercent = Math.abs(egyptianArea - trueArea) / trueArea * 100;

                const scale = 5;
                const Ox = 300, Oy = 125;
                const rPx = r * scale;
                const sqPx = egyptianSide * scale;

                svg.innerHTML = `
                    <!-- True Circle (Indigo) -->
                    <circle cx="${Ox}" cy="${Oy}" r="${rPx}" fill="rgba(99,102,241,0.25)" stroke="#6366f1" stroke-width="3"/>
                    <!-- Egyptian Equivalent Square (Amber) -->
                    <rect x="${Ox - sqPx/2}" y="${Oy - sqPx/2}" width="${sqPx}" height="${sqPx}" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4"/>

                    <text x="${Ox}" y="${Oy}" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">d = ${d} cm</text>
                `;

                readout.innerHTML = `
                    True Area: <b>${trueArea.toFixed(2)} cm²</b> | 
                    Egyptian Rhind Square [(8/9)d]²: <b>${egyptianArea.toFixed(2)} cm²</b> | 
                    Accuracy: <b>99.4% (Error: only ${errorPercent.toFixed(2)}%)</b>
                `;
            }

            dSlider.oninput = update;
            update();
        }

        // Sim 11: Rotary Sprinkler & Wiper Sweep Sector Laboratory
        function renderSim11(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Sweep Angle (θ):</label>
                            <input type="range" id="sim11_theta" min="30" max="240" value="120" class="w-28 accent-indigo-500">
                            <span id="sim11_theta_val" class="font-bold text-indigo-400 font-mono">120°</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Radius (r):</label>
                            <input type="range" id="sim11_r" min="5" max="15" value="7" class="w-24 accent-emerald-500">
                            <span id="sim11_r_val" class="font-bold text-emerald-400 font-mono">7 m</span>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim11_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim11_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const tSlider = document.getElementById('sim11_theta');
            const rSlider = document.getElementById('sim11_r');
            const tVal = document.getElementById('sim11_theta_val');
            const rVal = document.getElementById('sim11_r_val');
            const svg = document.getElementById('sim11_svg');
            const readout = document.getElementById('sim11_readout');

            function update() {
                const theta = parseFloat(tSlider.value);
                const r = parseFloat(rSlider.value);
                tVal.textContent = `${theta}°`;
                rVal.textContent = `${r} m`;

                const Ox = 300, Oy = 160;
                const rPx = r * 10;
                const startAngle = -Math.PI / 2 - (theta * Math.PI) / 360;
                const endAngle = -Math.PI / 2 + (theta * Math.PI) / 360;

                const Ax = Ox + rPx * Math.cos(startAngle);
                const Ay = Oy + rPx * Math.sin(startAngle);
                const Bx = Ox + rPx * Math.cos(endAngle);
                const By = Oy + rPx * Math.sin(endAngle);

                const area = (theta / 360) * Math.PI * r * r;
                const arcL = (theta / 360) * 2 * Math.PI * r;

                svg.innerHTML = `
                    <!-- Ground/Lawn Field -->
                    <line x1="50" y1="${Oy}" x2="550" y2="${Oy}" stroke="#334155" stroke-width="2"/>
                    <!-- Watered Sector -->
                    <path d="M${Ox},${Oy} L${Ax},${Ay} A${rPx},${rPx} 0 0,1 ${Bx},${By} Z" fill="rgba(56,189,248,0.3)" stroke="#38bdf8" stroke-width="2"/>

                    <!-- Sprinkler Nozzle -->
                    <circle cx="${Ox}" cy="${Oy}" r="6" fill="#38bdf8"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${Ay}" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="${Ox}" y1="${Oy}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="2"/>
                `;

                readout.innerHTML = `
                    Sprinkler Coverage: <b>Area = (θ/360) × πr² = ${area.toFixed(2)} m²</b> | 
                    Triangular Equivalent: <b>(1/2) × l × r = (1/2) × ${arcL.toFixed(2)} × ${r} = ${area.toFixed(2)} m²</b>
                `;
            }

            tSlider.oninput = update;
            rSlider.oninput = update;
            update();
        }

        // Sim 12: Circular Segment Decomposer & Triangle Subtraction Simulator
        function renderSim12(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Central Angle (θ):</label>
                            <input type="range" id="sim12_theta" min="40" max="140" value="90" class="w-28 accent-indigo-500">
                            <span id="sim12_theta_val" class="font-bold text-indigo-400 font-mono">90°</span>
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim12_btn_decomp" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Decompose Region</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim12_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim12_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let isDecomposed = false;
            const tSlider = document.getElementById('sim12_theta');
            const tVal = document.getElementById('sim12_theta_val');
            const decBtn = document.getElementById('sim12_btn_decomp');
            const svg = document.getElementById('sim12_svg');
            const readout = document.getElementById('sim12_readout');

            function update() {
                const theta = parseFloat(tSlider.value);
                tVal.textContent = `${theta}°`;

                const Ox = 300, Oy = 125, r = 85;
                const halfRad = (theta * Math.PI) / 360;
                const Ax = Ox - r * Math.sin(halfRad);
                const Ay = Oy - r * Math.cos(halfRad);
                const Bx = Ox + r * Math.sin(halfRad);
                const By = Oy - r * Math.cos(halfRad);

                const sectorArea = (theta / 360) * Math.PI * r * r;
                const triArea = 0.5 * r * r * Math.sin((theta * Math.PI) / 180);
                const segArea = sectorArea - triArea;

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="none" stroke="#334155" stroke-width="2"/>

                    <!-- Minor Segment (Emerald) -->
                    <path d="M${Ax},${Ay} A${r},${r} 0 0,1 ${Bx},${By} Z" fill="rgba(16,185,129,0.5)" stroke="#10b981" stroke-width="2"/>

                    <!-- Triangle OAB (Fades out when decomposed) -->
                    <polygon points="${Ox},${Oy} ${Ax},${Ay} ${Bx},${By}" 
                             fill="${isDecomposed ? 'rgba(99,102,241,0.05)' : 'rgba(99,102,241,0.35)'}" 
                             stroke="#6366f1" stroke-width="2" stroke-dasharray="${isDecomposed ? '3,3' : 'none'}"/>

                    <!-- Chord AB -->
                    <line x1="${Ax}" y1="${Ay}" x2="${Bx}" y2="${By}" stroke="#f59e0b" stroke-width="3"/>
                `;

                readout.innerHTML = `
                    Sector Area = ${sectorArea.toFixed(0)} - Triangle Area = ${triArea.toFixed(0)} ⇒ 
                    <b>Minor Segment Area = ${segArea.toFixed(0)} px²</b>
                `;
            }

            decBtn.onclick = () => { isDecomposed = !isDecomposed; decBtn.textContent = isDecomposed ? "Reassemble Sector" : "Decompose Region"; update(); };
            tSlider.oninput = update;
            update();
        }

        // Sim 13: Brahmagupta Cyclic Quadrilateral Lab & Area Maximizer
        function renderSim13(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Brahmagupta (628 CE) Cyclic 4-Gon:</span>
                        <span class="text-emerald-400 font-mono text-[11px]">Opposite Angles Sum to 180°</span>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim13_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim13_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const svg = document.getElementById('sim13_svg');
            const readout = document.getElementById('sim13_readout');

            const Ox = 300, Oy = 125, R = 90;
            // Sides approx 2, 3, 4, 5
            const Ax = 236, Ay = 61;
            const Bx = 210, By = 125;
            const Cx = 300, Cy = 215;
            const Dx = 385, Dy = 95;

            svg.innerHTML = `
                <!-- Circumcircle -->
                <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#6366f1" stroke-width="3"/>
                <!-- Inscribed Cyclic Quadrilateral -->
                <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="3"/>

                <circle cx="${Ax}" cy="${Ay}" r="5" fill="#ffffff"/>
                <circle cx="${Bx}" cy="${By}" r="5" fill="#ffffff"/>
                <circle cx="${Cx}" cy="${Cy}" r="5" fill="#ffffff"/>
                <circle cx="${Dx}" cy="${Dy}" r="5" fill="#ffffff"/>

                <text x="${Ax - 10}" y="${Ay - 5}" fill="#ffffff" font-size="11" font-weight="bold">A</text>
                <text x="${Bx - 15}" y="${By}" fill="#ffffff" font-size="11" font-weight="bold">B</text>
                <text x="${Cx}" y="${Cy + 16}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">C</text>
                <text x="${Dx + 10}" y="${Dy}" fill="#ffffff" font-size="11" font-weight="bold">D</text>
            `;

            readout.innerHTML = `
                Brahmagupta's Formula: <b>Area = √[(s-a)(s-b)(s-c)(s-d)]</b> | 
                Optimal Isoperimetric Maximization (Encloses Max Possible Area for Fixed Sides!)
            `;
        }

        // Sim 14: Vertex Collapse Morphing: Brahmagupta to Heron Continuity Simulator
        function renderSim14(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Collapse Side d to 0:</label>
                            <input type="range" id="sim14_d" min="0" max="80" value="60" class="w-32 accent-indigo-500">
                            <span id="sim14_d_val" class="font-bold text-indigo-400 font-mono">60 px</span>
                        </div>
                        <span id="sim14_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">4-gon (Brahmagupta)</span>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim14_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim14_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const slider = document.getElementById('sim14_d');
            const dVal = document.getElementById('sim14_d_val');
            const badge = document.getElementById('sim14_badge');
            const svg = document.getElementById('sim14_svg');
            const readout = document.getElementById('sim14_readout');

            function update() {
                const d = parseFloat(slider.value);
                dVal.textContent = `${d} px`;

                const Ox = 300, Oy = 125, R = 90;
                const Ax = 230, Ay = 65;
                const Bx = 210, By = 185;
                const Cx = 390, Cy = 160;
                // Move vertex D towards A as d -> 0
                const Dx = Ax + (d / 80) * 150;
                const Dy = Ay + (d / 80) * 20;

                const isCollapsed = (d === 0);
                if (isCollapsed) {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
                    badge.textContent = "3-gon / Triangle (Heron's Formula!)";
                } else {
                    badge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30";
                    badge.textContent = "4-gon (Brahmagupta's Formula)";
                }

                svg.innerHTML = `
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="3,3"/>
                    <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy} ${Dx},${Dy}" fill="rgba(99,102,241,0.25)" stroke="#6366f1" stroke-width="3"/>

                    <circle cx="${Ax}" cy="${Ay}" r="5" fill="#ffffff"/>
                    <circle cx="${Bx}" cy="${By}" r="5" fill="#ffffff"/>
                    <circle cx="${Cx}" cy="${Cy}" r="5" fill="#ffffff"/>
                    <circle cx="${Dx}" cy="${Dy}" r="5" fill="${isCollapsed ? '#10b981' : '#f59e0b'}"/>

                    <text x="${Ax - 15}" y="${Ay}" fill="#ffffff" font-size="11" font-weight="bold">A</text>
                    <text x="${Bx - 15}" y="${By}" fill="#ffffff" font-size="11" font-weight="bold">B</text>
                    <text x="${Cx + 10}" y="${Cy}" fill="#ffffff" font-size="11" font-weight="bold">C</text>
                    <text x="${Dx + 5}" y="${Dy - 8}" fill="${isCollapsed ? '#34d399' : '#fcd34d'}" font-size="11" font-weight="bold">${isCollapsed ? 'D = A' : 'D'}</text>
                `;

                if (isCollapsed) {
                    readout.innerHTML = `
                        <b>d = 0: Factor (s - d) = (s - 0) = s!</b> ⇒ 
                        Brahmagupta √[(s-a)(s-b)(s-c)(s-d)] becomes <b>√[s(s-a)(s-b)(s-c)] (Heron's Formula!)</b>
                    `;
                } else {
                    readout.innerHTML = `
                        Side d = ${d} px. Drag slider to 0 to watch Brahmagupta collapse into Heron's Formula!
                    `;
                }
            }

            slider.oninput = update;
            update();
        }

        // Sim 15: Interactive Mensuration Formula Hierarchy Tree & Constraint Engine
        function renderSim15(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Click a Hierarchy Node:</span>
                        <div class="flex flex-wrap gap-1" id="sim15_nodes">
                            <button data-node="bret" class="px-2 py-1 rounded bg-indigo-600 text-white font-bold transition">1. Bretschneider</button>
                            <button data-node="brahma" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">2. Brahmagupta</button>
                            <button data-node="heron" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">3. Heron</button>
                            <button data-node="equi" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">4. Equilateral</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim15_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim15_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-indigo-950/40 border border-indigo-500/40 text-indigo-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let activeNode = 'bret';
            const buttons = document.querySelectorAll('#sim15_nodes button');
            const svg = document.getElementById('sim15_svg');
            const readout = document.getElementById('sim15_readout');

            function update() {
                buttons.forEach(b => {
                    b.className = (b.dataset.node === activeNode) 
                        ? "px-2 py-1 rounded bg-indigo-600 text-white font-bold transition"
                        : "px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                });

                if (activeNode === 'bret') {
                    svg.innerHTML = `
                        <rect x="100" y="40" width="400" height="60" rx="10" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <text x="300" y="75" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Bretschneider's Formula (Any Convex 4-gon)</text>
                        <text x="300" y="150" fill="#a5b4fc" font-size="12" font-mono text-anchor="middle">√[(s-a)(s-b)(s-c)(s-d) - abcd cos²((A+C)/2)]</text>
                    `;
                    readout.innerHTML = `Universal Parent Formula: Accounts for non-cyclic distortion using the cosine correction term.`;
                } else if (activeNode === 'brahma') {
                    svg.innerHTML = `
                        <rect x="120" y="40" width="360" height="60" rx="10" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <text x="300" y="75" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Brahmagupta's Formula (Cyclic 4-gon)</text>
                        <text x="300" y="150" fill="#6ee7b7" font-size="12" font-mono text-anchor="middle">Constraint A+C=180° ⇒ cos(90°)=0 ⇒ √[(s-a)(s-b)(s-c)(s-d)]</text>
                    `;
                    readout.innerHTML = `Specialization 1: When vertices lie on a circle, opposite angles are supplementary and the cosine term vanishes!`;
                } else if (activeNode === 'heron') {
                    svg.innerHTML = `
                        <rect x="140" y="40" width="320" height="60" rx="10" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2"/>
                        <text x="300" y="75" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Heron's Formula (Triangle)</text>
                        <text x="300" y="150" fill="#fcd34d" font-size="12" font-mono text-anchor="middle">Constraint d=0 ⇒ (s-d)=s ⇒ √[s(s-a)(s-b)(s-c)]</text>
                    `;
                    readout.innerHTML = `Specialization 2: When one side collapses to zero, the cyclic 4-gon becomes a 3-gon (Heron's Formula!).`;
                } else {
                    svg.innerHTML = `
                        <rect x="160" y="40" width="280" height="60" rx="10" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                        <text x="300" y="75" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Equilateral Triangle</text>
                        <text x="300" y="150" fill="#f472b6" font-size="13" font-mono text-anchor="middle">Constraint a=b=c ⇒ Area = (√3 / 4) a²</text>
                    `;
                    readout.innerHTML = `Specialization 3: When all 3 sides are equal, Heron reduces to the classic equilateral area formula.`;
                }
            }

            buttons.forEach(b => {
                b.onclick = () => { activeNode = b.dataset.node; update(); };
            });
            update();
        }

        // Sim 16: Monte Carlo Pi Dartboard Simulator & Gauss Shoelace Polygon Engine
        function renderSim16(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-indigo-400 font-bold">Monte Carlo Dartboard Simulation:</span>
                        <div class="flex gap-2">
                            <button id="sim16_throw" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition shadow">Throw 500 Darts</button>
                            <button id="sim16_reset" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Reset</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim16_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim16_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let totalDarts = 0;
            let insideDarts = 0;
            const throwBtn = document.getElementById('sim16_throw');
            const resetBtn = document.getElementById('sim16_reset');
            const svg = document.getElementById('sim16_svg');
            const readout = document.getElementById('sim16_readout');

            const Ox = 300, Oy = 125, R = 80;
            let dotsSvg = "";

            function render() {
                const estPi = totalDarts > 0 ? (4 * insideDarts / totalDarts).toFixed(4) : "0.0000";
                svg.innerHTML = `
                    <!-- Bounding Square -->
                    <rect x="${Ox - R}" y="${Oy - R}" width="${2 * R}" height="${2 * R}" fill="rgba(30,41,59,0.5)" stroke="#64748b" stroke-width="2"/>
                    <!-- Inscribed Circle -->
                    <circle cx="${Ox}" cy="${Oy}" r="${R}" fill="none" stroke="#10b981" stroke-width="3"/>

                    <!-- Dart Points -->
                    ${dotsSvg}
                `;

                readout.innerHTML = `
                    Darts Thrown: <b>${totalDarts}</b> | Inside Circle: <b>${insideDarts}</b> | 
                    Estimated <b>π ≈ 4 × (${insideDarts} / ${totalDarts || 1}) = ${estPi}</b>
                `;
            }

            throwBtn.onclick = () => {
                for (let i = 0; i < 500; i++) {
                    const rx = (Math.random() - 0.5) * 2 * R;
                    const ry = (Math.random() - 0.5) * 2 * R;
                    const isInside = (rx * rx + ry * ry <= R * R);
                    totalDarts++;
                    if (isInside) insideDarts++;
                    if (totalDarts <= 1500) {
                        dotsSvg += `<circle cx="${Ox + rx}" cy="${Oy + ry}" r="1.5" fill="${isInside ? '#10b981' : '#f43f5e'}"/>`;
                    }
                }
                render();
            };

            resetBtn.onclick = () => {
                totalDarts = 0;
                insideDarts = 0;
                dotsSvg = "";
                render();
            };

            render();
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

