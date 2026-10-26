# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 13
MENSURATION: SURFACE AREA AND VOLUME (Competencies CG-5, C-5.1, CG-9)
Generates public/animations/class9-surface-areas-volumes.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_surface_areas_volumes_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-surface-areas-volumes.html"

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
    <title>NCERT Class 9 Mathematics • Surface Area and Volume Laboratory</title>
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
                        <span class="text-xs text-slate-400 font-medium">Chapter 13</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight flex items-center gap-2">
                        <span>Surface Area & Volume</span>
                        <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-normal">Interactive 3D Lab</span>
                    </h1>
                </div>
            </div>

            <!-- Slide Progress & Navigation Controls -->
            <div class="flex items-center gap-3">
                <div class="hidden md:flex flex-col items-end mr-2">
                    <span id="slideIndicatorText" class="text-xs font-mono font-bold text-indigo-300">Slide 1 of 20</span>
                    <span id="slideCategoryText" class="text-[10px] text-slate-400">Cuboids & Cubes</span>
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
                    <h2 id="slideTitle" class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-1">Cuboids in Real Life: Anatomy & Formulas</h2>
                    <p id="slideSubtitle" class="text-xs sm:text-sm text-indigo-300 font-medium">Rectangular Prisms, 6 Faces, 12 Edges, 8 Vertices & 3D Interior Capacity</p>
                </div>
                <div class="mt-3 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
                    <span id="slideFocusLabel" class="flex items-center gap-1.5 text-slate-300">
                        <i data-lucide="box" class="w-4 h-4 text-emerald-400"></i>
                        <span>Core Focus: Surface Areas, Volume Extrusions & 3D Metric Invariance</span>
                    </span>
                    <span class="font-mono text-[11px] text-slate-400 hidden sm:inline">NCERT Ch 13 • Mensuration</span>
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
                        <h3 id="simulatorHeading" class="text-xs sm:text-sm font-bold text-slate-200 uppercase tracking-wider">Interactive 3D Simulator</h3>
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
                        <h2 id="quizTitle" class="text-2xl font-black text-white mt-2">Class 9 Surface Area & Volume Challenge</h2>
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
            <h3 class="text-xl font-bold text-white">Congratulations on Completing Chapter 13!</h3>
            <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
            <p class="text-xs sm:text-sm text-slate-400 mt-2 max-w-xl mx-auto">
                You have mastered the surface areas and volumes of cuboids, cubes, right circular cylinders, hollow pipes, right circular cones, regular pyramids, spheres, and hemispheres, alongside Archimedes' cylinder projection theorems, metal recasting conservation laws, Galileo's Square-Cube Law, and industrial can packaging optimization.
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
                playTone(587.33, 0.2);
            } else {
                btn.className = "text-left px-2.5 py-1.5 rounded-lg text-[11px] font-bold bg-rose-600 text-white border border-rose-400 flex items-center justify-between";
                buttons[correctIdx].className = "text-left px-2.5 py-1.5 rounded-lg text-[11px] font-bold bg-emerald-600/80 text-white border border-emerald-400 flex items-center justify-between";
                playTone(220, 0.25, 'sawtooth');
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

        // Sim 1: 3D Cuboid Unfolder to 2D Net & Volume Unit Cube Meter
        function renderSim1(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">l:</label>
                            <input type="range" id="sim1_l" min="5" max="10" value="8" class="w-16 accent-indigo-500">
                            <label class="text-slate-300 font-semibold ml-2">b:</label>
                            <input type="range" id="sim1_b" min="3" max="8" value="5" class="w-16 accent-emerald-500">
                            <label class="text-slate-300 font-semibold ml-2">h:</label>
                            <input type="range" id="sim1_h" min="2" max="6" value="4" class="w-16 accent-amber-500">
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Unfold Net:</label>
                            <input type="range" id="sim1_unfold" min="0" max="100" value="0" class="w-24 accent-pink-500">
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

            const lS = document.getElementById('sim1_l');
            const bS = document.getElementById('sim1_b');
            const hS = document.getElementById('sim1_h');
            const uS = document.getElementById('sim1_unfold');
            const svg = document.getElementById('sim1_svg');
            const readout = document.getElementById('sim1_readout');

            function update() {
                const l = parseFloat(lS.value);
                const b = parseFloat(bS.value);
                const h = parseFloat(hS.value);
                const unfold = parseFloat(uS.value) / 100;

                const tsa = 2 * (l * b + b * h + h * l);
                const lsa = 2 * h * (l + b);
                const vol = l * b * h;
                const diag = Math.sqrt(l * l + b * b + h * h);

                if (unfold === 0) {
                    // Isometric 3D Box view
                    const Ox = 260, Oy = 150;
                    const scale = 14;
                    const dx = l * scale * 0.866, dy = l * scale * 0.5;
                    const bdx = -b * scale * 0.866, bdy = b * scale * 0.5;
                    const hz = h * scale;

                    svg.innerHTML = `
                        <!-- Front Face -->
                        <polygon points="${Ox},${Oy} ${Ox + dx},${Oy - dy} ${Ox + dx},${Oy - dy - hz} ${Ox},${Oy - hz}" fill="rgba(99,102,241,0.4)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Side Face -->
                        <polygon points="${Ox},${Oy} ${Ox + bdx},${Oy - bdy} ${Ox + bdx},${Oy - bdy - hz} ${Ox},${Oy - hz}" fill="rgba(16,185,129,0.4)" stroke="#10b981" stroke-width="2"/>
                        <!-- Top Face -->
                        <polygon points="${Ox},${Oy - hz} ${Ox + dx},${Oy - dy - hz} ${Ox + dx + bdx},${Oy - dy - bdy - hz} ${Ox + bdx},${Oy - bdy - hz}" fill="rgba(245,158,11,0.4)" stroke="#f59e0b" stroke-width="2"/>

                        <!-- Dimension Labels -->
                        <text x="${Ox + dx/2 + 10}" y="${Oy - dy/2 + 15}" fill="#a5b4fc" font-size="11" font-weight="bold">l = ${l}</text>
                        <text x="${Ox + bdx/2 - 25}" y="${Oy - bdy/2 + 15}" fill="#6ee7b7" font-size="11" font-weight="bold">b = ${b}</text>
                        <text x="${Ox - 20}" y="${Oy - hz/2}" fill="#fcd34d" font-size="11" font-weight="bold">h = ${h}</text>
                    `;
                } else {
                    // 2D Net
                    const scale = 9;
                    const cx = 300, cy = 125;
                    const lw = l * scale, bw = b * scale, hw = h * scale;

                    svg.innerHTML = `
                        <!-- Bottom Face -->
                        <rect x="${cx - lw/2}" y="${cy - bw/2}" width="${lw}" height="${bw}" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2"/>
                        <text x="${cx}" y="${cy + 4}" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">Base (lb)</text>

                        <!-- Top Face -->
                        <rect x="${cx - lw/2}" y="${cy - bw/2 - bw - hw}" width="${lw}" height="${bw}" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2"/>
                        <text x="${cx}" y="${cy - bw/2 - hw - bw/2 + 4}" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">Top (lb)</text>

                        <!-- Front/Back Faces -->
                        <rect x="${cx - lw/2}" y="${cy + bw/2}" width="${lw}" height="${hw}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <rect x="${cx - lw/2}" y="${cy - bw/2 - hw}" width="${lw}" height="${hw}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>

                        <!-- Left/Right Faces -->
                        <rect x="${cx - lw/2 - hw}" y="${cy - bw/2}" width="${hw}" height="${bw}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <rect x="${cx + lw/2}" y="${cy - bw/2}" width="${hw}" height="${bw}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                    `;
                }

                readout.innerHTML = `
                    TSA = 2(lb+bh+hl) = <b>${tsa} cm²</b> | 4 Walls LSA = <b>${lsa} cm²</b> | 
                    <b>Volume = ${vol} cm³</b> | Space Diagonal = <b>${diag.toFixed(2)} cm</b>
                `;
            }

            lS.oninput = update;
            bS.oninput = update;
            hS.oninput = update;
            uS.oninput = update;
            update();
        }

        // Sim 2: Cuboid-to-Cube Constraint Lock Morph & Isometric Dissector
        function renderSim2(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Side a:</label>
                            <input type="range" id="sim2_a" min="4" max="10" value="6" class="w-28 accent-indigo-500">
                            <span id="sim2_a_val" class="text-indigo-400 font-bold font-mono">6 cm</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span id="sim2_badge" class="px-2.5 py-0.5 rounded font-bold font-mono text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Special Case: l = b = h = a</span>
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

            const aSlider = document.getElementById('sim2_a');
            const aVal = document.getElementById('sim2_a_val');
            const svg = document.getElementById('sim2_svg');
            const readout = document.getElementById('sim2_readout');

            function update() {
                const a = parseFloat(aSlider.value);
                aVal.textContent = `${a} cm`;

                const tsa = 6 * a * a;
                const lsa = 4 * a * a;
                const vol = a * a * a;
                const diag = a * Math.sqrt(3);

                const Ox = 300, Oy = 160;
                const scale = 14;
                const d = a * scale * 0.866;
                const h = a * scale;

                svg.innerHTML = `
                    <!-- Isometric Cube -->
                    <polygon points="${Ox},${Oy} ${Ox + d},${Oy - d/2} ${Ox + d},${Oy - d/2 - h} ${Ox},${Oy - h}" fill="rgba(99,102,241,0.35)" stroke="#6366f1" stroke-width="3"/>
                    <polygon points="${Ox},${Oy} ${Ox - d},${Oy - d/2} ${Ox - d},${Oy - d/2 - h} ${Ox},${Oy - h}" fill="rgba(16,185,129,0.35)" stroke="#10b981" stroke-width="3"/>
                    <polygon points="${Ox},${Oy - h} ${Ox + d},${Oy - d/2 - h} ${Ox},${Oy - d - h} ${Ox - d},${Oy - d/2 - h}" fill="rgba(245,158,11,0.35)" stroke="#f59e0b" stroke-width="3"/>

                    <text x="${Ox + d/2 + 10}" y="${Oy - d/4 + 15}" fill="#a5b4fc" font-size="11" font-weight="bold">a = ${a}</text>
                    <text x="${Ox - d/2 - 25}" y="${Oy - d/4 + 15}" fill="#6ee7b7" font-size="11" font-weight="bold">a = ${a}</text>
                    <text x="${Ox - 25}" y="${Oy - h/2}" fill="#fcd34d" font-size="11" font-weight="bold">a = ${a}</text>
                `;

                readout.innerHTML = `
                    TSA = 6a² = <b>${tsa} cm²</b> | LSA = 4a² = <b>${lsa} cm²</b> | 
                    <b>Volume = a³ = ${vol} cm³</b> | Space Diagonal = a√3 = <b>${diag.toFixed(2)} cm</b>
                `;
            }

            aSlider.oninput = update;
            update();
        }

        // Sim 3: Cylinder Revolution Generator & Curved Surface Net Unroller
        function renderSim3(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Radius r:</label>
                            <input type="range" id="sim3_r" min="20" max="60" value="40" class="w-16 accent-indigo-500">
                            <label class="text-slate-300 font-semibold ml-2">Height h:</label>
                            <input type="range" id="sim3_h" min="50" max="110" value="80" class="w-16 accent-emerald-500">
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Unroll Net:</label>
                            <input type="range" id="sim3_unroll" min="0" max="100" value="0" class="w-24 accent-pink-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim3_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim3_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const rS = document.getElementById('sim3_r');
            const hS = document.getElementById('sim3_h');
            const uS = document.getElementById('sim3_unroll');
            const svg = document.getElementById('sim3_svg');
            const readout = document.getElementById('sim3_readout');

            function update() {
                const r = parseFloat(rS.value);
                const h = parseFloat(hS.value);
                const unfold = parseFloat(uS.value) / 100;

                const csa = 2 * Math.PI * r * h;
                const tsa = 2 * Math.PI * r * (h + r);
                const vol = Math.PI * r * r * h;

                if (unfold === 0) {
                    // 3D Cylinder view
                    const Ox = 300, topY = 70, botY = topY + h;
                    const ry = r * 0.35;

                    svg.innerHTML = `
                        <!-- Body -->
                        <rect x="${Ox - r}" y="${topY}" width="${2 * r}" height="${h}" fill="rgba(99,102,241,0.25)"/>
                        <line x1="${Ox - r}" y1="${topY}" x2="${Ox - r}" y2="${botY}" stroke="#6366f1" stroke-width="2.5"/>
                        <line x1="${Ox + r}" y1="${topY}" x2="${Ox + r}" y2="${botY}" stroke="#6366f1" stroke-width="2.5"/>

                        <!-- Bottom Ellipse -->
                        <ellipse cx="${Ox}" cy="${botY}" rx="${r}" ry="${ry}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <!-- Top Ellipse -->
                        <ellipse cx="${Ox}" cy="${topY}" rx="${r}" ry="${ry}" fill="rgba(16,185,129,0.5)" stroke="#10b981" stroke-width="2.5"/>

                        <!-- Dimension Markers -->
                        <line x1="${Ox}" y1="${topY}" x2="${Ox + r}" y2="${topY}" stroke="#ffffff" stroke-width="1.5"/>
                        <text x="${Ox + r/2}" y="${topY - 6}" fill="#ffffff" font-size="10" font-weight="bold">r = ${r}</text>
                        <line x1="${Ox + r + 15}" y1="${topY}" x2="${Ox + r + 15}" y2="${botY}" stroke="#fcd34d" stroke-width="2"/>
                        <text x="${Ox + r + 25}" y="${topY + h/2}" fill="#fcd34d" font-size="11" font-weight="bold">h = ${h}</text>
                    `;
                } else {
                    // Unrolled Net: Rectangle of 2πr × h and 2 circular lids
                    const netW = 2 * Math.PI * r * 0.6;
                    const netH = h;
                    const cx = 300, cy = 125;

                    svg.innerHTML = `
                        <!-- Unrolled Rectangular Sheet -->
                        <rect x="${cx - netW/2}" y="${cy - netH/2}" width="${netW}" height="${netH}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Circular Lids -->
                        <circle cx="${cx}" cy="${cy - netH/2 - r*0.6}" r="${r*0.6}" fill="rgba(16,185,129,0.4)" stroke="#10b981" stroke-width="2"/>
                        <circle cx="${cx}" cy="${cy + netH/2 + r*0.6}" r="${r*0.6}" fill="rgba(16,185,129,0.4)" stroke="#10b981" stroke-width="2"/>

                        <text x="${cx}" y="${cy - netH/2 - 8}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Length = 2πr</text>
                        <text x="${cx + netW/2 + 10}" y="${cy}" fill="#fcd34d" font-size="11" font-weight="bold">h</text>
                    `;
                }

                readout.innerHTML = `
                    CSA = 2πrh = <b>${csa.toFixed(1)} cm²</b> | 
                    TSA = 2πr(h+r) = <b>${tsa.toFixed(1)} cm²</b> | 
                    Volume = πr²h = <b>${vol.toFixed(1)} cm³</b>
                `;
            }

            rS.oninput = update;
            hS.oninput = update;
            uS.oninput = update;
            update();
        }

        // Sim 4: Cylindrical Liquid Reservoir Filler & Hollow Pipe Material Meter
        function renderSim4(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Liquid Level (%):</label>
                            <input type="range" id="sim4_fill" min="0" max="100" value="65" class="w-32 accent-sky-500">
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim4_btn_solid" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Water Tank</button>
                            <button id="sim4_btn_hollow" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Hollow Metal Pipe</button>
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

            let mode = 'solid';
            const fSlider = document.getElementById('sim4_fill');
            const sBtn = document.getElementById('sim4_btn_solid');
            const hBtn = document.getElementById('sim4_btn_hollow');
            const svg = document.getElementById('sim4_svg');
            const readout = document.getElementById('sim4_readout');

            function update() {
                const fill = parseFloat(fSlider.value) / 100;
                const r = 50, h = 120;
                const Ox = 300, topY = 60, botY = topY + h;
                const ry = r * 0.35;

                if (mode === 'solid') {
                    sBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    hBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";

                    const liquidH = h * fill;
                    const liquidTopY = botY - liquidH;
                    const maxLitres = (Math.PI * r * r * h / 1000).toFixed(1);
                    const currLitres = (maxLitres * fill).toFixed(1);

                    svg.innerHTML = `
                        <!-- Tank Boundary -->
                        <rect x="${Ox - r}" y="${topY}" width="${2 * r}" height="${h}" fill="rgba(30,41,59,0.4)"/>
                        <line x1="${Ox - r}" y1="${topY}" x2="${Ox - r}" y2="${botY}" stroke="#64748b" stroke-width="2"/>
                        <line x1="${Ox + r}" y1="${topY}" x2="${Ox + r}" y2="${botY}" stroke="#64748b" stroke-width="2"/>
                        <ellipse cx="${Ox}" cy="${topY}" rx="${r}" ry="${ry}" fill="none" stroke="#64748b" stroke-width="2"/>
                        <ellipse cx="${Ox}" cy="${botY}" rx="${r}" ry="${ry}" fill="none" stroke="#64748b" stroke-width="2"/>

                        <!-- Filled Liquid -->
                        ${liquidH > 0 ? `
                            <rect x="${Ox - r}" y="${liquidTopY}" width="${2 * r}" height="${liquidH}" fill="rgba(56,189,248,0.5)"/>
                            <ellipse cx="${Ox}" cy="${liquidTopY}" rx="${r}" ry="${ry}" fill="rgba(56,189,248,0.8)" stroke="#38bdf8" stroke-width="2"/>
                            <ellipse cx="${Ox}" cy="${botY}" rx="${r}" ry="${ry}" fill="rgba(56,189,248,0.6)"/>
                        ` : ''}
                    `;

                    readout.innerHTML = `
                        Water Storage Tank: Total Capacity = <b>${maxLitres} L</b> | 
                        Current Filled Volume: <b>${currLitres} L (${(fill * 100).toFixed(0)}%)</b>
                    `;
                } else {
                    sBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    hBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                    const R = 60, innerR = 40;
                    const Ry = R * 0.35, innerRy = innerR * 0.35;

                    svg.innerHTML = `
                        <!-- Outer Cylinder -->
                        <line x1="${Ox - R}" y1="${topY}" x2="${Ox - R}" y2="${botY}" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="${Ox + R}" y1="${topY}" x2="${Ox + R}" y2="${botY}" stroke="#f59e0b" stroke-width="3"/>
                        <ellipse cx="${Ox}" cy="${botY}" rx="${R}" ry="${Ry}" fill="none" stroke="#f59e0b" stroke-width="2"/>

                        <!-- Top Ring Face -->
                        <ellipse cx="${Ox}" cy="${topY}" rx="${R}" ry="${Ry}" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2"/>
                        <ellipse cx="${Ox}" cy="${topY}" rx="${innerR}" ry="${innerRy}" fill="#020617" stroke="#38bdf8" stroke-width="2"/>

                        <!-- Inner Bore lines -->
                        <line x1="${Ox - innerR}" y1="${topY}" x2="${Ox - innerR}" y2="${botY}" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="${Ox + innerR}" y1="${topY}" x2="${Ox + innerR}" y2="${botY}" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
                    `;

                    readout.innerHTML = `
                        Hollow Pipe: Metal Volume = <b>π(R² - r²)h</b> | 
                        Total Surface Area = <b>2π(R + r)h + 2π(R² - r²)</b>
                    `;
                }
            }

            sBtn.onclick = () => { mode = 'solid'; update(); };
            hBtn.onclick = () => { mode = 'hollow'; update(); };
            fSlider.oninput = update;
            update();
        }

        // Sim 5: Right Triangle Revolution Simulator & Slant Height Pythagorean Lock
        function renderSim5(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Radius r:</label>
                            <input type="range" id="sim5_r" min="30" max="80" value="50" class="w-20 accent-indigo-500">
                            <label class="text-slate-300 font-semibold ml-2">Height h:</label>
                            <input type="range" id="sim5_h" min="60" max="130" value="100" class="w-20 accent-emerald-500">
                        </div>
                        <span class="text-amber-400 font-mono text-[11px] font-bold">l² = r² + h²</span>
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

            const rS = document.getElementById('sim5_r');
            const hS = document.getElementById('sim5_h');
            const svg = document.getElementById('sim5_svg');
            const readout = document.getElementById('sim5_readout');

            function update() {
                const r = parseFloat(rS.value);
                const h = parseFloat(hS.value);
                const l = Math.sqrt(r * r + h * h);

                const Ox = 300, topY = 50, botY = topY + h;
                const ry = r * 0.35;

                svg.innerHTML = `
                    <!-- Base Ellipse -->
                    <ellipse cx="${Ox}" cy="${botY}" rx="${r}" ry="${ry}" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="3,3"/>

                    <!-- Cone Slant Outlines -->
                    <line x1="${Ox}" y1="${topY}" x2="${Ox - r}" y2="${botY}" stroke="#6366f1" stroke-width="2.5"/>
                    <line x1="${Ox}" y1="${topY}" x2="${Ox + r}" y2="${botY}" stroke="#6366f1" stroke-width="2.5"/>

                    <!-- Generator Right Triangle (ΔOAP) -->
                    <polygon points="${Ox},${topY} ${Ox},${botY} ${Ox + r},${botY}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2.5"/>

                    <!-- Right Angle Marker at Center -->
                    <rect x="${Ox}" y="${botY - 12}" width="12" height="12" fill="none" stroke="#ffffff" stroke-width="1.5"/>

                    <!-- Dimension Labels -->
                    <text x="${Ox - 18}" y="${topY + h/2}" fill="#ffffff" font-size="11" font-weight="bold">h = ${h}</text>
                    <text x="${Ox + r/2}" y="${botY + 16}" fill="#6ee7b7" font-size="11" font-weight="bold">r = ${r}</text>
                    <text x="${Ox + r/2 + 15}" y="${topY + h/2}" fill="#f59e0b" font-size="12" font-weight="bold">l = ${l.toFixed(1)}</text>
                `;

                readout.innerHTML = `
                    Right Triangle Generator: r = ${r} cm, h = ${h} cm ⇒ 
                    <b>Slant Height l = √(r² + h²) = √(${r*r} + ${h*h}) = ${l.toFixed(2)} cm</b>
                `;
            }

            rS.oninput = update;
            hS.oninput = update;
            update();
        }

        // Sim 6: Conical Net Unroller to Circular Sector & Fabric Calculator
        function renderSim6(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Unroll Conical Tent Canvas:</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Unfold Net:</label>
                            <input type="range" id="sim6_unfold" min="0" max="100" value="0" class="w-32 accent-indigo-500">
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

            const uSlider = document.getElementById('sim6_unfold');
            const svg = document.getElementById('sim6_svg');
            const readout = document.getElementById('sim6_readout');

            function update() {
                const unfold = parseFloat(uSlider.value) / 100;
                const r = 50, h = 90;
                const l = Math.sqrt(r * r + h * h); // ~103
                const csa = Math.PI * r * l;

                if (unfold === 0) {
                    const Ox = 300, topY = 60, botY = topY + h;
                    svg.innerHTML = `
                        <!-- 3D Cone -->
                        <ellipse cx="${Ox}" cy="${botY}" rx="${r}" ry="${r*0.35}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <polygon points="${Ox},${topY} ${Ox - r},${botY} ${Ox + r},${botY}" fill="rgba(99,102,241,0.35)" stroke="#6366f1" stroke-width="2"/>
                        <text x="${Ox}" y="${topY - 8}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Apex</text>
                    `;
                } else {
                    // Unrolled Sector of radius l and arc 2πr
                    const Ox = 300, Oy = 80;
                    const sectorAngle = (r / l) * 2 * Math.PI; // In radians
                    const startA = Math.PI / 2 - sectorAngle / 2;
                    const endA = Math.PI / 2 + sectorAngle / 2;

                    const Ax = Ox + l * Math.cos(startA);
                    const Ay = Oy + l * Math.sin(startA);
                    const Bx = Ox + l * Math.cos(endA);
                    const By = Oy + l * Math.sin(endA);

                    svg.innerHTML = `
                        <!-- Unrolled Sector of Canvas -->
                        <path d="M${Ox},${Oy} L${Ax},${Ay} A${l},${l} 0 0,1 ${Bx},${By} Z" fill="rgba(99,102,241,0.35)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Radius l marker -->
                        <line x1="${Ox}" y1="${Oy}" x2="${Ax}" y2="${Ay}" stroke="#f59e0b" stroke-width="2"/>
                        <text x="${Ox + l/2}" y="${Oy + 30}" fill="#f59e0b" font-size="11" font-weight="bold">Radius = l</text>
                        <!-- Arc label -->
                        <text x="${Ox}" y="${Oy + l + 18}" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Curved Arc = 2πr</text>
                    `;
                }

                readout.innerHTML = `
                    Sector Area = (1/2) × (2πr) × l = <b>πrl = ${csa.toFixed(1)} cm²</b> (Curved Surface Area!)
                `;
            }

            uSlider.oninput = update;
            update();
        }

        // Sim 7: Interactive 3-Cone Pouring Experiment to Matching Cylinder
        function renderSim7(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Volume Experiment (Cone vs Cylinder):</span>
                        <div class="flex gap-2">
                            <button id="sim7_pour" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition shadow">Pour Cone</button>
                            <button id="sim7_reset" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Reset</button>
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim7_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim7_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            let pouredCount = 0;
            const pBtn = document.getElementById('sim7_pour');
            const rBtn = document.getElementById('sim7_reset');
            const svg = document.getElementById('sim7_svg');
            const readout = document.getElementById('sim7_readout');

            function update() {
                const r = 45, h = 110;
                const coneX = 200, cylX = 400;
                const topY = 60, botY = topY + h;

                const cylFillH = (pouredCount / 3) * h;
                const cylFillTopY = botY - cylFillH;

                svg.innerHTML = `
                    <!-- Cone Container -->
                    <polygon points="${coneX},${botY} ${coneX - r},${topY} ${coneX + r},${topY}" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="2"/>
                    <ellipse cx="${coneX}" cy="${topY}" rx="${r}" ry="${r*0.35}" fill="rgba(99,102,241,0.4)" stroke="#6366f1" stroke-width="1.5"/>
                    <text x="${coneX}" y="${botY + 20}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Cone (1/3 V)</text>

                    <!-- Matching Cylinder -->
                    <rect x="${cylX - r}" y="${topY}" width="${2 * r}" height="${h}" fill="rgba(30,41,59,0.3)"/>
                    <line x1="${cylX - r}" y1="${topY}" x2="${cylX - r}" y2="${botY}" stroke="#64748b" stroke-width="2"/>
                    <line x1="${cylX + r}" y1="${topY}" x2="${cylX + r}" y2="${botY}" stroke="#64748b" stroke-width="2"/>
                    <ellipse cx="${cylX}" cy="${botY}" rx="${r}" ry="${r*0.35}" fill="none" stroke="#64748b" stroke-width="2"/>
                    <ellipse cx="${cylX}" cy="${topY}" rx="${r}" ry="${r*0.35}" fill="none" stroke="#64748b" stroke-width="2"/>

                    <!-- Cylinder Water Levels -->
                    ${cylFillH > 0 ? `
                        <rect x="${cylX - r}" y="${cylFillTopY}" width="${2 * r}" height="${cylFillH}" fill="rgba(56,189,248,0.5)"/>
                        <ellipse cx="${cylX}" cy="${cylFillTopY}" rx="${r}" ry="${r*0.35}" fill="rgba(56,189,248,0.8)" stroke="#38bdf8" stroke-width="2"/>
                    ` : ''}

                    <!-- 1/3 and 2/3 Guide Lines -->
                    <line x1="${cylX - r - 5}" y1="${botY - h/3}" x2="${cylX + r + 5}" y2="${botY - h/3}" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3,3"/>
                    <line x1="${cylX - r - 5}" y1="${botY - 2*h/3}" x2="${cylX + r + 5}" y2="${botY - 2*h/3}" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3,3"/>

                    <text x="${cylX}" y="${botY + 20}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Cylinder Level: ${pouredCount}/3</text>
                `;

                if (pouredCount === 3) {
                    readout.innerHTML = `
                        <b>3 Full Cones Completely Fill 1 Matching Cylinder!</b> ⇒ 
                        <b>V_cone = (1/3) × V_cylinder = (1/3)πr²h</b>
                    `;
                } else {
                    readout.innerHTML = `
                        Poured: <b>${pouredCount} of 3 cones</b> into the cylinder. Click "Pour Cone" to continue!
                    `;
                }
            }

            pBtn.onclick = () => {
                if (pouredCount < 3) {
                    pouredCount++;
                    playTone(400 + pouredCount * 100, 0.2);
                    update();
                }
            };
            rBtn.onclick = () => {
                pouredCount = 0;
                update();
            };
            update();
        }

        // Sim 8: 3D Square Pyramid Net Unfolder & Slant Height Geometry
        function renderSim8(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Square Pyramid Net:</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Unfold Faces:</label>
                            <input type="range" id="sim8_unfold" min="0" max="100" value="0" class="w-32 accent-indigo-500">
                        </div>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim8_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim8_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const uSlider = document.getElementById('sim8_unfold');
            const svg = document.getElementById('sim8_svg');
            const readout = document.getElementById('sim8_readout');

            function update() {
                const unfold = parseFloat(uSlider.value) / 100;
                const a = 12, h = 8;
                const l = Math.sqrt(h * h + (a / 2) * (a / 2)); // 10

                if (unfold === 0) {
                    // 3D wireframe pyramid
                    const Ox = 300, Oy = 50;
                    svg.innerHTML = `
                        <!-- Base -->
                        <polygon points="230,170 370,170 330,130 190,130" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2"/>
                        <!-- Lateral Faces -->
                        <line x1="${Ox}" y1="${Oy}" x2="230" y2="170" stroke="#6366f1" stroke-width="2.5"/>
                        <line x1="${Ox}" y1="${Oy}" x2="370" y2="170" stroke="#6366f1" stroke-width="2.5"/>
                        <line x1="${Ox}" y1="${Oy}" x2="330" y2="130" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="${Ox}" y1="${Oy}" x2="190" y2="130" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3,3"/>

                        <!-- Apex Point -->
                        <circle cx="${Ox}" cy="${Oy}" r="5" fill="#ec4899"/>
                        <text x="${Ox}" y="${Oy - 10}" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">Apex</text>
                    `;
                } else {
                    // 2D Flower Net
                    const cx = 300, cy = 125, s = 60, lh = 60;
                    svg.innerHTML = `
                        <!-- Square Base -->
                        <rect x="${cx - s/2}" y="${cy - s/2}" width="${s}" height="${s}" fill="rgba(245,158,11,0.4)" stroke="#f59e0b" stroke-width="2"/>
                        <!-- Top Triangle -->
                        <polygon points="${cx - s/2},${cy - s/2} ${cx + s/2},${cy - s/2} ${cx},${cy - s/2 - lh}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Bottom Triangle -->
                        <polygon points="${cx - s/2},${cy + s/2} ${cx + s/2},${cy + s/2} ${cx},${cy + s/2 + lh}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Left Triangle -->
                        <polygon points="${cx - s/2},${cy - s/2} ${cx - s/2},${cy + s/2} ${cx - s/2 - lh},${cy}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                        <!-- Right Triangle -->
                        <polygon points="${cx + s/2},${cy - s/2} ${cx + s/2},${cy + s/2} ${cx + s/2 + lh},${cy}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                    `;
                }

                readout.innerHTML = `
                    Slant Height l = √[h² + (a/2)²] = √[8² + 6²] = <b>10 m</b> | 
                    LSA = 4 × (1/2 al) = <b>2al = 240 m²</b> | TSA = a² + 2al = <b>384 m²</b>
                `;
            }

            uSlider.oninput = update;
            update();
        }

        // Sim 9: 6-Pyramid Cube Dissection Explosion & Volume Equivalence
        function renderSim9(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Cube Dissection Proof:</span>
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Dissect 6 Pyramids:</label>
                            <input type="range" id="sim9_burst" min="0" max="100" value="0" class="w-32 accent-indigo-500">
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

            const bSlider = document.getElementById('sim9_burst');
            const svg = document.getElementById('sim9_svg');
            const readout = document.getElementById('sim9_readout');

            function update() {
                const burst = parseFloat(bSlider.value) / 100;
                const Ox = 300, Oy = 125, s = 80;

                svg.innerHTML = `
                    <!-- Center Point of Cube -->
                    <circle cx="${Ox}" cy="${Oy}" r="4" fill="#ffffff"/>

                    <!-- Radiating Pyramids -->
                    <polygon points="${Ox},${Oy} ${Ox - s - burst*40},${Oy - s/2} ${Ox},${Oy - s - burst*40}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                    <polygon points="${Ox},${Oy} ${Ox + s + burst*40},${Oy - s/2} ${Ox},${Oy - s - burst*40}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                    <polygon points="${Ox},${Oy} ${Ox - s - burst*40},${Oy + s/2} ${Ox},${Oy + s + burst*40}" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2"/>
                    <polygon points="${Ox},${Oy} ${Ox + s + burst*40},${Oy + s/2} ${Ox},${Oy + s + burst*40}" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="2"/>
                `;

                readout.innerHTML = `
                    1 Cube divides into <b>6 Congruent Pyramids</b> ⇒ 
                    V_pyramid = (1/6) a³ = (1/6) a²(2h) = <b>(1/3) Base Area × Height!</b>
                `;
            }

            bSlider.oninput = update;
            update();
        }

        // Sim 10: 3D Wireframe Sphere Rotator & Great Circle Slicer
        function renderSim10(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Sphere Radius r:</label>
                            <input type="range" id="sim10_r" min="50" max="90" value="75" class="w-24 accent-indigo-500">
                        </div>
                        <div class="flex gap-1.5">
                            <button id="sim10_btn_great" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Slice Great Circle</button>
                        </div>
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

            let showSlice = false;
            const rSlider = document.getElementById('sim10_r');
            const gBtn = document.getElementById('sim10_btn_great');
            const svg = document.getElementById('sim10_svg');
            const readout = document.getElementById('sim10_readout');

            function update() {
                const r = parseFloat(rSlider.value);
                const Ox = 300, Oy = 125;

                svg.innerHTML = `
                    <!-- Sphere Outer Silhouette -->
                    <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="3"/>

                    <!-- Latitude / Longitude Wireframe Ellipses -->
                    <ellipse cx="${Ox}" cy="${Oy}" rx="${r}" ry="${r * 0.35}" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <ellipse cx="${Ox}" cy="${Oy}" rx="${r * 0.35}" ry="${r}" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

                    <!-- Great Circle Slicing Disc -->
                    ${showSlice ? `
                        <ellipse cx="${Ox}" cy="${Oy}" rx="${r}" ry="${r * 0.35}" fill="rgba(16,185,129,0.5)" stroke="#10b981" stroke-width="3"/>
                        <text x="${Ox}" y="${Oy - 8}" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Great Circle Area = πr²</text>
                    ` : ''}

                    <circle cx="${Ox}" cy="${Oy}" r="4" fill="#ffffff"/>
                `;

                readout.innerHTML = `
                    Great Circle passes through Center O (Radius = r) ⇒ 
                    <b>Area = πr² = ${(Math.PI * r * r).toFixed(0)} px²</b> (Exactly 1/4th of sphere surface area!)
                `;
            }

            gBtn.onclick = () => { showSlice = !showSlice; gBtn.textContent = showSlice ? "Remove Slice" : "Slice Great Circle"; update(); };
            rSlider.oninput = update;
            update();
        }

        // Sim 11: Archimedes' Hat-Box Projection & 4-Disc Skin Peeling Simulator
        function renderSim11(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Archimedes' Proof (Sphere Surface Area):</span>
                        <div class="flex gap-1.5">
                            <button id="sim11_btn_cyl" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Hat-Box Cylinder</button>
                            <button id="sim11_btn_4disc" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">4 Great Discs</button>
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

            let mode = 'cyl';
            const cBtn = document.getElementById('sim11_btn_cyl');
            const dBtn = document.getElementById('sim11_btn_4disc');
            const svg = document.getElementById('sim11_svg');
            const readout = document.getElementById('sim11_readout');

            function update() {
                const r = 70;
                const Ox = 300, Oy = 125;

                if (mode === 'cyl') {
                    cBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    dBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";

                    svg.innerHTML = `
                        <!-- Circumscribing Cylinder of Height 2r -->
                        <rect x="${Ox - r}" y="${Oy - r}" width="${2 * r}" height="${2 * r}" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4"/>

                        <!-- Sphere Inside -->
                        <circle cx="${Ox}" cy="${Oy}" r="${r}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="3"/>

                        <text x="${Ox + r + 20}" y="${Oy}" fill="#f59e0b" font-size="11" font-weight="bold">Height = 2r</text>
                    `;

                    readout.innerHTML = `
                        Archimedes' Hat-Box Theorem: <b>Surface Area of Sphere = Cylinder Curved Area = 2πr(2r) = 4πr²!</b>
                    `;
                } else {
                    cBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    dBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                    svg.innerHTML = `
                        <!-- 4 Great Discs -->
                        <circle cx="150" cy="80" r="45" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <circle cx="260" cy="80" r="45" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <circle cx="370" cy="80" r="45" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                        <circle cx="480" cy="80" r="45" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>

                        <text x="300" y="165" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">Sphere Outer Skin = 4 Flat Circular Discs of Radius r</text>
                    `;

                    readout.innerHTML = `
                        Peeling the Sphere Skin: πr² + πr² + πr² + πr² = <b>4πr²</b>!
                    `;
                }
            }

            cBtn.onclick = () => { mode = 'cyl'; update(); };
            dBtn.onclick = () => { mode = 'disc'; update(); };
            update();
        }

        // Sim 12: Archimedean Tombstone 1:2:3 Volume Balance Scale
        function renderSim12(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Archimedes' Gravestone Inscription (Ratio 1 : 2 : 3):</span>
                        <span class="text-amber-400 font-mono text-[11px] font-bold">V_cone + V_sphere = V_cylinder</span>
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

            const svg = document.getElementById('sim12_svg');
            const readout = document.getElementById('sim12_readout');

            const r = 40, h = 2 * r;
            svg.innerHTML = `
                <!-- 1. Cone (h = 2r) -->
                <polygon points="120,60 80,140 160,140" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                <text x="120" y="170" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Cone: (2/3)πr³</text>
                <text x="120" y="190" fill="#94a3b8" font-size="10" text-anchor="middle">(Ratio 1)</text>

                <!-- Plus Sign -->
                <text x="210" y="110" fill="#ffffff" font-size="20" font-weight="bold">+</text>

                <!-- 2. Sphere -->
                <circle cx="300" cy="100" r="${r}" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2.5"/>
                <text x="300" y="170" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Sphere: (4/3)πr³</text>
                <text x="300" y="190" fill="#94a3b8" font-size="10" text-anchor="middle">(Ratio 2)</text>

                <!-- Equals Sign -->
                <text x="390" y="110" fill="#ffffff" font-size="20" font-weight="bold">=</text>

                <!-- 3. Cylinder (h = 2r) -->
                <rect x="440" y="60" width="${2 * r}" height="${h}" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="480" y="170" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Cylinder: 2πr³</text>
                <text x="480" y="190" fill="#94a3b8" font-size="10" text-anchor="middle">(Ratio 3)</text>
            `;

            readout.innerHTML = `
                Archimedes' Volume Ratio: <b>Cone : Sphere : Cylinder = 1 : 2 : 3</b> | 
                Sphere is exactly <b>2/3 of Cylinder = (2/3)(2πr³) = (4/3)πr³</b>!
            `;
        }

        // Sim 13: Solid vs. Hollow Hemisphere 3D Dissector & Rim Meter
        function renderSim13(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Hemisphere Geometry:</span>
                        <div class="flex gap-1.5">
                            <button id="sim13_btn_solid" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition">Solid Hemisphere</button>
                            <button id="sim13_btn_hollow" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition">Hollow Bowl</button>
                        </div>
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

            let mode = 'solid';
            const sBtn = document.getElementById('sim13_btn_solid');
            const hBtn = document.getElementById('sim13_btn_hollow');
            const svg = document.getElementById('sim13_svg');
            const readout = document.getElementById('sim13_readout');

            function update() {
                const Ox = 300, Oy = 110, r = 70;

                if (mode === 'solid') {
                    sBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";
                    hBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";

                    svg.innerHTML = `
                        <!-- Curved Dome -->
                        <path d="M${Ox - r},${Oy} A${r},${r} 0 0,0 ${Ox + r},${Oy} Z" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="3"/>
                        <!-- Flat Top Base Disc -->
                        <ellipse cx="${Ox}" cy="${Oy}" rx="${r}" ry="${r*0.35}" fill="rgba(16,185,129,0.5)" stroke="#10b981" stroke-width="2.5"/>

                        <text x="${Ox}" y="${Oy - 15}" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Flat Circular Base = πr²</text>
                        <text x="${Ox}" y="${Oy + 45}" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Curved Dome = 2πr²</text>
                    `;

                    readout.innerHTML = `
                        Solid Hemisphere: Curved CSA (2πr²) + Flat Base (πr²) ⇒ 
                        <b>Total Surface Area (TSA) = 3πr²!</b> | Volume = <b>(2/3)πr³</b>
                    `;
                } else {
                    sBtn.className = "px-2.5 py-1 rounded bg-slate-800 text-slate-300 font-bold transition";
                    hBtn.className = "px-2.5 py-1 rounded bg-indigo-600 text-white font-bold transition";

                    const R = 75, inR = 55;

                    svg.innerHTML = `
                        <!-- Outer Bowl -->
                        <path d="M${Ox - R},${Oy} A${R},${R} 0 0,0 ${Ox + R},${Oy} Z" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="2"/>
                        <!-- Circular Rim -->
                        <ellipse cx="${Ox}" cy="${Oy}" rx="${R}" ry="${R*0.35}" fill="rgba(245,158,11,0.4)" stroke="#f59e0b" stroke-width="2"/>
                        <ellipse cx="${Ox}" cy="${Oy}" rx="${inR}" ry="${inR*0.35}" fill="#020617" stroke="#38bdf8" stroke-width="2"/>
                    `;

                    readout.innerHTML = `
                        Hollow Bowl: External CSA (2πR²) + Internal CSA (2πr²) + Rim Area π(R² - r²) | 
                        Material Volume = <b>(2/3)π(R³ - r³)</b>
                    `;
                }
            }

            sBtn.onclick = () => { mode = 'solid'; update(); };
            hBtn.onclick = () => { mode = 'hollow'; update(); };
            update();
        }

        // Sim 14: Molten Metal Crucible Recasting & Invariant Volume Engine
        function renderSim14(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-300 font-semibold">Melt Solid Sphere into Ball Bearings:</span>
                        <button id="sim14_melt" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition shadow">Melt & Recast</button>
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

            let isMelted = false;
            const mBtn = document.getElementById('sim14_melt');
            const svg = document.getElementById('sim14_svg');
            const readout = document.getElementById('sim14_readout');

            function update() {
                if (!isMelted) {
                    svg.innerHTML = `
                        <!-- Big Sphere (R = 8 cm) -->
                        <circle cx="300" cy="120" r="70" fill="rgba(245,158,11,0.4)" stroke="#f59e0b" stroke-width="3"/>
                        <text x="300" y="125" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Large Sphere R = 8 cm</text>
                    `;
                    readout.innerHTML = `Original Solid Sphere: Volume = (4/3)π(8)³ = <b>682.67π cm³</b>. Click 'Melt & Recast'!`;
                } else {
                    // Grid of 512 tiny spheres
                    let dots = "";
                    for (let row = 0; row < 6; row++) {
                        for (let col = 0; col < 12; col++) {
                            dots += `<circle cx="${130 + col * 30}" cy="${50 + row * 25}" r="5" fill="#38bdf8"/>`;
                        }
                    }
                    svg.innerHTML = `
                        ${dots}
                        <text x="300" y="215" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">512 Small Ball Bearings of Radius r = 1 cm!</text>
                    `;
                    readout.innerHTML = `
                        Volume Conserved: n = R³ / r³ = 8³ / 1³ = <b>512 Spheres!</b> | 
                        Total Surface Area <b>increased by 8 times!</b>
                    `;
                }
            }

            mBtn.onclick = () => { isMelted = !isMelted; mBtn.textContent = isMelted ? "Reset Sphere" : "Melt & Recast"; update(); };
            update();
        }

        // Sim 15: Square-Cube Law Scaling Lab & Biological Heat Loss Curve
        function renderSim15(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Scale Factor (k):</label>
                            <input type="range" id="sim15_k" min="1" max="5" value="1" step="1" class="w-28 accent-indigo-500">
                            <span id="sim15_k_val" class="font-bold text-indigo-400 font-mono">1x</span>
                        </div>
                        <span class="text-amber-400 font-mono text-[11px] font-bold">Square-Cube Law (Galileo)</span>
                    </div>

                    <div class="flex-1 min-h-[250px] bg-slate-950/60 rounded-xl border border-slate-800/80 p-2 flex items-center justify-center">
                        <svg id="sim15_svg" viewBox="0 0 600 250" class="w-full h-full max-h-[250px]">
                            <!-- Injected by JS -->
                        </svg>
                    </div>

                    <div id="sim15_readout" class="p-2.5 rounded-xl text-center text-xs font-mono font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300">
                        <!-- Populated by JS -->
                    </div>
                </div>
            `;

            const kSlider = document.getElementById('sim15_k');
            const kVal = document.getElementById('sim15_k_val');
            const svg = document.getElementById('sim15_svg');
            const readout = document.getElementById('sim15_readout');

            function update() {
                const k = parseInt(kSlider.value);
                kVal.textContent = `${k}x`;

                const sa = 6 * k * k;
                const vol = k * k * k;
                const sa_v = (sa / vol).toFixed(2);

                const size = k * 18;
                const Ox = 300, Oy = 125;

                svg.innerHTML = `
                    <rect x="${Ox - size/2}" y="${Oy - size/2}" width="${size}" height="${size}" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2"/>
                    <text x="${Ox}" y="${Oy + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">${k}a</text>
                `;

                readout.innerHTML = `
                    Length = <b>${k}a</b> | Surface Area ∝ k² = <b>${sa}</b> | Volume ∝ k³ = <b>${vol}</b> | 
                    <b>SA / V Ratio = 6/a = ${sa_v}</b> (Plummets as size increases!)
                `;
            }

            kSlider.oninput = update;
            update();
        }

        // Sim 16: Industrial Beverage Can Metal Optimizer & Cost Minimum Graph
        function renderSim16(container) {
            container.innerHTML = `
                <div class="flex flex-col gap-3 h-full">
                    <div class="flex items-center justify-between bg-slate-900/80 p-2.5 rounded-xl border border-slate-800 text-xs">
                        <div class="flex items-center gap-2">
                            <label class="text-slate-300 font-semibold">Can Radius r:</label>
                            <input type="range" id="sim16_r" min="20" max="60" value="38" class="w-32 accent-indigo-500">
                            <span id="sim16_r_val" class="font-bold text-indigo-400 font-mono">3.8 cm</span>
                        </div>
                        <span class="text-emerald-400 font-mono text-[11px] font-bold">Fixed Volume = 355 ml</span>
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

            const rSlider = document.getElementById('sim16_r');
            const rVal = document.getElementById('sim16_r_val');
            const svg = document.getElementById('sim16_svg');
            const readout = document.getElementById('sim16_readout');

            function update() {
                const r = parseFloat(rSlider.value) / 10;
                rVal.textContent = `${r.toFixed(1)} cm`;

                const V = 355; // cm3
                const h = V / (Math.PI * r * r);
                const tsa = 2 * Math.PI * r * r + 2 * Math.PI * r * h;
                const isOptimal = Math.abs(h - 2 * r) < 0.5;

                const Ox = 300, Oy = 70;
                const rPx = r * 10;
                const hPx = Math.min(130, h * 10);

                svg.innerHTML = `
                    <!-- 3D Can -->
                    <rect x="${Ox - rPx}" y="${Oy}" width="${2 * rPx}" height="${hPx}" fill="${isOptimal ? 'rgba(16,185,129,0.3)' : 'rgba(99,102,241,0.3)'}" stroke="${isOptimal ? '#10b981' : '#6366f1'}" stroke-width="2.5"/>
                    <ellipse cx="${Ox}" cy="${Oy}" rx="${rPx}" ry="${rPx * 0.35}" fill="${isOptimal ? '#10b981' : '#6366f1'}"/>
                    <ellipse cx="${Ox}" cy="${Oy + hPx}" rx="${rPx}" ry="${rPx * 0.35}" fill="${isOptimal ? '#10b981' : '#6366f1'}"/>

                    <text x="${Ox}" y="${Oy + hPx/2}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">h = ${h.toFixed(1)} cm</text>
                `;

                if (isOptimal) {
                    readout.innerHTML = `
                        <span class="text-emerald-400 font-bold">✓ OPTIMAL MINIMUM METAL COST: h ≈ 2r (${h.toFixed(1)} cm ≈ 2 × ${r.toFixed(1)} cm)!</span>
                        Total Surface Area = <b>${tsa.toFixed(1)} cm²</b> (Lowest possible packaging metal!)
                    `;
                } else {
                    readout.innerHTML = `
                        r = ${r.toFixed(1)} cm, h = ${h.toFixed(1)} cm ⇒ TSA = <b>${tsa.toFixed(1)} cm²</b>. Adjust slider until h = 2r for minimum cost!
                    `;
                }
            }

            rSlider.oninput = update;
            update();
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

