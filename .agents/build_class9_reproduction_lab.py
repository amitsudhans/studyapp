# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 3 (Biology)
REPRODUCTION: MODES, FLORAL BIOLOGY, HUMAN REPRODUCTIVE SYSTEMS & REPRODUCTIVE HEALTH
Syllabus Competencies: C-2.8, C-3.2, C-3.3, C-4.3, C-5.1, C-5.2, C-6.1, C-7.1, C-7.2
Generates public/animations/class9-reproduction.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_reproduction_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-reproduction.html"

# Split teaching slides (0-15) and quiz slides (16-19)
SLIDES = SLIDES_DATA[:16]
QUIZZES = SLIDES_DATA[16:]

def generate_html():
    slides_json = json.dumps(SLIDES)
    quizzes_json = json.dumps(QUIZZES)

    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Science • Chapter 3: Reproduction Laboratory</title>
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
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 3px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
        .glass-panel {{
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(51, 65, 85, 0.6);
        }}
        @keyframes mouthMove {{
            0%, 100% {{ transform: scaleY(0.2); }}
            50% {{ transform: scaleY(1); }}
        }}
        .talking {{
            animation: mouthMove 0.22s infinite alternate ease-in-out;
            transform-origin: center;
        }}
        @keyframes pulseGlow {{
            0%, 100% {{ box-shadow: 0 0 15px rgba(236, 72, 153, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(236, 72, 153, 0.45); }}
        }}
        .pulse-border {{
            animation: pulseGlow 2.5s infinite;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-rose-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="glass-panel sticky top-0 z-40 border-b border-slate-800/80 px-4 py-2.5 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-rose-600 to-pink-400 flex items-center justify-center shadow-lg shadow-rose-950/40 border border-rose-400/30">
                <i data-lucide="dna" class="w-5 h-5 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold tracking-wider uppercase px-2 py-0.5 rounded bg-rose-950/80 text-rose-400 border border-rose-800/60 font-mono">
                        NCERT Class 9 Science • Chapter 3
                    </span>
                    <span class="hidden sm:inline-block text-[11px] font-medium text-slate-400">• Biology Master Lab</span>
                </div>
                <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-1.5">
                    Reproduction: Modes, Floral Biology & Human Systems
                </h1>
            </div>
        </div>

        <!-- Slide Selector & Nav Controls -->
        <div class="flex items-center gap-2 sm:gap-3">
            <div class="relative">
                <button onclick="window.toggleSlideMenu()" id="slideMenuBtn" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700/70 hover:bg-slate-800 text-xs font-semibold text-slate-200 transition">
                    <i data-lucide="compass" class="w-3.5 h-3.5 text-rose-400"></i>
                    <span>Slide <span id="currentSlideNum">1</span> / 20</span>
                    <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-slate-400"></i>
                </button>
                <div id="slideMenuDropdown" class="hidden absolute right-0 mt-2 w-72 max-h-96 overflow-y-auto glass-panel rounded-xl shadow-2xl p-2 z-50 border border-slate-700 space-y-1">
                    <div class="text-[11px] font-bold px-2.5 py-1 text-slate-400 uppercase tracking-wider font-mono">Curriculum Syllabus Index</div>
                    <div id="slideListItems" class="space-y-0.5"></div>
                </div>
            </div>

            <!-- Voice Controls -->
            <div class="flex items-center gap-1 bg-slate-900/90 rounded-lg p-1 border border-slate-800">
                <button onclick="window.toggleSpeech()" id="speechBtn" title="Play Voiceover Narration" class="w-8 h-8 rounded-md bg-rose-600 hover:bg-rose-500 text-white flex items-center justify-center transition">
                    <i data-lucide="volume-2" id="speechIcon" class="w-4 h-4"></i>
                </button>
                <button onclick="window.stopSpeech()" title="Stop Voiceover" class="w-8 h-8 rounded-md hover:bg-slate-800 text-slate-400 hover:text-slate-200 flex items-center justify-center transition">
                    <i data-lucide="square" class="w-3.5 h-3.5"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Workspace Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-6 items-start">

        <!-- Left Column: Talking Avatar, Theory Points, Checkpoints & Quizzes (7 cols) -->
        <div class="lg:col-span-7 flex flex-col gap-4">

            <!-- Teacher Avatar & Audio Card -->
            <div class="glass-panel rounded-2xl p-4 border border-slate-800/80 shadow-xl relative overflow-hidden bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-rose-950/20">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Talking Avatar (Prof. Sophia) -->
                    <div class="relative w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-b from-rose-600 to-pink-800 p-0.5 shadow-md shrink-0">
                        <svg viewBox="0 0 100 100" class="w-full h-full rounded-[14px] bg-slate-900 overflow-hidden">
                            <rect width="100" height="100" fill="#1e1022"/>
                            <circle cx="50" cy="50" r="42" fill="#831843" opacity="0.3"/>
                            <!-- Torso / Lab Coat -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#334155"/>
                            <path d="M35,90 L50,100 L65,90 L60,82 L50,86 L40,82 Z" fill="#e11d48"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="46" rx="22" ry="26" fill="#fed7aa"/>
                            <!-- Hair -->
                            <path d="M26,42 Q28,18 50,18 Q72,18 74,42 Q68,26 50,26 Q32,26 26,42 Z" fill="#374151"/>
                            <path d="M26,42 Q24,60 28,68 Q32,56 32,46 Z" fill="#374151"/>
                            <path d="M74,42 Q76,60 72,68 Q68,56 68,46 Z" fill="#374151"/>
                            <!-- Glasses -->
                            <rect x="33" y="40" width="13" height="8" rx="2" fill="none" stroke="#be123c" stroke-width="2"/>
                            <rect x="54" y="40" width="13" height="8" rx="2" fill="none" stroke="#be123c" stroke-width="2"/>
                            <line x1="46" y1="44" x2="54" y2="44" stroke="#be123c" stroke-width="2"/>
                            <!-- Eyes -->
                            <circle cx="39.5" cy="44" r="2.2" fill="#1f2937"/>
                            <circle cx="60.5" cy="44" r="2.2" fill="#1f2937"/>
                            <!-- Nose -->
                            <path d="M50,47 L48,53 L52,53" fill="none" stroke="#fba06f" stroke-width="1.6" stroke-linecap="round"/>
                            <!-- Talking Mouth -->
                            <g id="teacherMouthGroup" transform="translate(50, 61)">
                                <ellipse id="teacherMouth" cx="0" cy="0" rx="6" ry="1.8" fill="#991b1b"/>
                            </g>
                        </svg>
                        <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded text-[9px] font-bold bg-rose-500 text-white font-mono shadow">
                            TEACHER
                        </div>
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between gap-2">
                            <span class="text-xs font-bold text-rose-400 uppercase tracking-wider font-mono">Prof. Sophia • Voice Guide</span>
                            <span id="speechStatusIndicator" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Ready</span>
                        </div>
                        <p id="narrationText" class="text-xs text-slate-300 mt-1 line-clamp-3 leading-relaxed italic">
                            Welcome students! Today we explore Reproduction—the biological continuum linking single-celled life, flowering plants, and human beings across generations.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Content Presentation Slide (Slides 1 to 16) -->
            <div id="contentSlideContainer" class="space-y-4">
                <!-- Slide Header Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between">
                        <span id="slideCategoryText" class="text-[11px] font-bold text-rose-400 uppercase tracking-widest font-mono">Section Core Theory</span>
                        <span id="slideBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-rose-950/80 text-rose-300 border border-rose-800/60 font-mono">
                            Part 1 of 20
                        </span>
                    </div>
                    <div>
                        <h2 id="slideTitle" class="text-lg sm:text-xl font-extrabold text-white tracking-tight">Introduction to Reproduction & Evolutionary Significance</h2>
                        <p id="slideSubtitle" class="text-xs sm:text-sm font-medium text-rose-400/90 mt-0.5">Continuity of Life, DNA Replication Fidelity, and the Emergence of Variations</p>
                    </div>
                    <ul id="slideKeyPoints" class="text-xs sm:text-sm text-slate-300 space-y-2 pt-1 border-t border-slate-800/80 leading-relaxed">
                        <!-- Injected via JavaScript -->
                    </ul>
                </div>

                <!-- Checkpoints Container -->
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle" class="w-4 h-4 text-rose-400"></i>
                            <h3 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Concept Checkpoints</h3>
                        </div>
                        <span class="text-[11px] font-mono text-slate-400">2 In-Slide Questions</span>
                    </div>
                    <div id="checkpointsList" class="space-y-4">
                        <!-- Injected via JavaScript -->
                    </div>
                </div>
            </div>

            <!-- Dedicated Quiz Slide (Slides 17 to 20) -->
            <div id="quizSlideContainer" class="hidden glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-3">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-rose-950 border border-rose-700/60 flex items-center justify-center text-rose-400">
                            <i data-lucide="award" class="w-4 h-4"></i>
                        </div>
                        <div>
                            <h3 id="quizTitleDisplay" class="text-sm font-extrabold text-white">Mastery Assessment</h3>
                            <p class="text-[11px] text-slate-400">10 Comprehensive Questions with Step-by-Step Solutions</p>
                        </div>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-mono font-bold text-rose-400">Score: <span id="quizScoreVal">0</span> / 10</span>
                    </div>
                </div>

                <div id="quizQuestionsList" class="space-y-4">
                    <!-- Injected via JavaScript -->
                </div>
            </div>

            <!-- Slide 20 Last Slide Notice -->
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-rose-500/40 bg-gradient-to-r from-rose-950/40 via-slate-900 to-pink-950/40 shadow-xl shadow-rose-950/30">
                <div class="w-12 h-12 rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/40 flex items-center justify-center mx-auto mb-2">
                    <i data-lucide="check-check" class="w-6 h-6"></i>
                </div>
                <h4 class="text-lg font-bold text-white">Curriculum Chapter Mastered!</h4>
                <p class="text-base sm:text-lg text-rose-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">
                    You have comprehensively mastered Asexual & Sexual Modes, Floral Pollination, Double Fertilisation, Human Reproductive Systems, Menstrual Cycles, Contraception, ART Technologies, and Indian Biological Pioneers.
                </p>
            </div>

        </div>

        <!-- Right Column: Interactive Bespoke SVG Simulators (5 cols) -->
        <div class="lg:col-span-5 flex flex-col gap-4 sticky top-20">
            <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 shadow-2xl flex flex-col gap-3">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4 text-rose-400"></i>
                        <h3 id="simulatorTitle" class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">
                            Interactive Visual Laboratory
                        </h3>
                    </div>
                    <span id="simulatorBadge" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-pink-400 border border-slate-700">
                        Interactive SVG
                    </span>
                </div>

                <!-- Viewport Container for Dynamic Bespoke Simulators -->
                <div id="simulatorViewport" class="w-full min-h-[420px] bg-slate-950/90 rounded-xl border border-slate-800/90 p-3 sm:p-4 flex flex-col items-center justify-center overflow-hidden relative">
                    <!-- Dynamic Bespoke SVG Simulators Injected Here -->
                </div>
            </div>

            <!-- Slide Navigation Footer -->
            <div class="glass-panel rounded-2xl p-3 border border-slate-800 flex items-center justify-between gap-2">
                <button onclick="window.navSlide(-1)" id="prevBtn" class="flex-1 px-3 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700/80 text-xs font-bold transition flex items-center justify-center gap-1.5 disabled:opacity-40 disabled:cursor-not-allowed">
                    <i data-lucide="chevron-left" class="w-4 h-4"></i>
                    <span>Previous</span>
                </button>
                <div class="px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 text-center shrink-0">
                    <span id="slideProgressRatio" class="text-xs font-mono font-bold text-rose-400">1 / 20</span>
                </div>
                <button onclick="window.navSlide(1)" id="nextBtn" class="flex-1 px-3 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-lg shadow-rose-950/50">
                    <span>Next</span>
                    <i data-lucide="chevron-right" class="w-4 h-4"></i>
                </button>
            </div>
            <!-- Progress Bar -->
            <div class="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden border border-slate-800">
                <div id="slideProgressBar" class="h-full bg-gradient-to-r from-rose-500 to-pink-400 transition-all duration-300" style="width: 5%;"></div>
            </div>
        </div>
    </main>

    <!-- Step-by-Step Solution Pop-Up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="glass-panel rounded-2xl border border-slate-700 max-w-lg w-full p-5 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-rose-950 text-rose-400 border border-rose-800 flex items-center justify-center">
                        <i data-lucide="book-open" class="w-4 h-4"></i>
                    </div>
                    <h4 class="text-sm font-bold text-white">Step-by-Step Question Solution</h4>
                </div>
                <button onclick="window.closeSolutionModal()" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            </div>
            <div class="space-y-3 text-xs leading-relaxed">
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                    <div class="text-[11px] font-mono text-rose-400 uppercase font-bold mb-1">Question Prompt</div>
                    <div id="modalQuestionText" class="text-slate-200 font-medium"></div>
                </div>
                <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-800/40">
                    <div class="text-[11px] font-mono text-rose-400 uppercase font-bold mb-1">Correct Answer & Principle</div>
                    <div id="modalAnswerText" class="text-rose-300 font-bold"></div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                    <div class="text-[11px] font-mono text-slate-400 uppercase font-bold mb-1">Biological Derivation & Explanation</div>
                    <div id="modalExplanationText" class="text-slate-300"></div>
                </div>
            </div>
            <div class="pt-2 text-right">
                <button onclick="window.closeSolutionModal()" class="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold transition shadow-lg">
                    Got It, Continue
                </button>
            </div>
        </div>
    </div>

    <!-- Data Injection & Application Scripts -->
    <script>
        const SLIDES = {slides_json};
        const QUIZZES = {quizzes_json};

        let currentSlideIndex = 0;
        let isSpeaking = false;
        let synth = window.speechSynthesis || null;
        let currentUtterance = null;

        // Fallback Web Audio Synthesizer
        let audioCtx = null;
        function playTone(freq, duration, type='sine') {{
            try {{
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
            }} catch(e) {{
                console.warn("Audio Context fallback unavailable", e);
            }}
        }}

        // Initialize App on DOM Ready
        document.addEventListener('DOMContentLoaded', () => {{
            initSlideDropdown();
            renderSlide(0);
            initSpeechControls();
            lucide.createIcons();
        }});

        // Populate Slide Jump Menu
        function initSlideDropdown() {{
            const list = document.getElementById('slideListItems');
            list.innerHTML = '';

            for (let i = 0; i < 20; i++) {{
                const btn = document.createElement('button');
                btn.className = "w-full text-left px-2.5 py-1.5 rounded-lg text-xs hover:bg-slate-800 transition flex items-center justify-between";
                let title = (i < 16) ? SLIDES[i].title : QUIZZES[i - 16].title;
                let badge = (i < 16) ? `Slide ${{i+1}}` : `Quiz ${{i-15}}`;

                btn.innerHTML = `
                    <span class="truncate pr-2">${{i+1}}. ${{title}}</span>
                    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-rose-400 shrink-0">${{badge}}</span>
                `;
                btn.onclick = () => {{
                    window.renderSlide(i);
                    window.toggleSlideMenu();
                }};
                list.appendChild(btn);
            }}
        }}

        window.toggleSlideMenu = function() {{
            const dd = document.getElementById('slideMenuDropdown');
            dd.classList.toggle('hidden');
        }};

        // Navigation Controller
        window.navSlide = function(delta) {{
            const nextIndex = currentSlideIndex + delta;
            if (nextIndex >= 0 && nextIndex < 20) {{
                stopSpeech();
                renderSlide(nextIndex);
            }}
        }};

        // Render Active Slide
        window.renderSlide = function(index) {{
            currentSlideIndex = index;
            document.getElementById('currentSlideNum').textContent = currentSlideIndex + 1;
            document.getElementById('slideProgressRatio').textContent = `${{currentSlideIndex + 1}} / 20`;
            document.getElementById('slideProgressBar').style.width = `${{((currentSlideIndex + 1) / 20) * 100}}%`;

            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Handle Slide 20 Specific Requirement
            const lastSlideNotice = document.getElementById('lastSlideNotice');
            const nextBtn = document.getElementById('nextBtn');
            if (currentSlideIndex === 19) {{
                lastSlideNotice.classList.remove('hidden');
                nextBtn.style.display = 'none';
            }} else {{
                lastSlideNotice.classList.add('hidden');
                nextBtn.style.display = 'flex';
                nextBtn.disabled = false;
            }}

            const contentContainer = document.getElementById('contentSlideContainer');
            const quizContainer = document.getElementById('quizSlideContainer');

            if (currentSlideIndex < 16) {{
                contentContainer.classList.remove('hidden');
                quizContainer.classList.add('hidden');

                const slide = SLIDES[currentSlideIndex];
                document.getElementById('slideCategoryText').textContent = "Section " + (currentSlideIndex + 1) + " • Core Theory";
                document.getElementById('slideBadge').textContent = `Slide ${{currentSlideIndex + 1}} of 20`;
                document.getElementById('slideTitle').textContent = slide.title;
                document.getElementById('slideSubtitle').textContent = slide.subtitle;
                document.getElementById('narrationText').textContent = slide.narration;

                // Render Key Points
                const kpList = document.getElementById('slideKeyPoints');
                kpList.innerHTML = slide.points.map(pt => `
                    <li class="flex items-start gap-2">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-400 mt-1.5 shrink-0"></span>
                        <span>${{pt}}</span>
                    </li>
                `).join('');

                // Render Checkpoints
                renderCheckpoints(slide.checkpoints);

                // Render Bespoke Interactive Simulator
                renderSimulator(currentSlideIndex);

            }} else {{
                contentContainer.classList.add('hidden');
                quizContainer.classList.remove('hidden');

                const quiz = QUIZZES[currentSlideIndex - 16];
                document.getElementById('quizTitleDisplay').textContent = quiz.quiz_title || quiz.title;
                document.getElementById('narrationText').textContent = quiz.narration;

                renderQuizSlide(quiz.questions);
                renderQuizSimulator(currentSlideIndex - 16);
            }}

            if (window.renderMathInElement) {{
                renderMathInElement(document.body);
            }}
            lucide.createIcons();
        }};

        // Render In-Slide Checkpoints
        function renderCheckpoints(checkpoints) {{
            const container = document.getElementById('checkpointsList');
            container.innerHTML = '';

            checkpoints.forEach((cp, idx) => {{
                const box = document.createElement('div');
                box.className = "p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5";

                const qTitle = document.createElement('div');
                qTitle.className = "text-xs font-semibold text-white flex items-start gap-2";
                qTitle.innerHTML = `
                    <span class="w-5 h-5 rounded bg-rose-950 text-rose-400 border border-rose-800 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold">Q${{idx+1}}</span>
                    <span>${{cp.question}}</span>
                `;
                box.appendChild(qTitle);

                const optsGrid = document.createElement('div');
                optsGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1";

                const expPanel = document.createElement('div');
                expPanel.className = "hidden p-2.5 rounded-lg bg-rose-950/40 border border-rose-800/60 text-xs text-rose-300 space-y-1";

                cp.options.forEach((opt, oIdx) => {{
                    const btn = document.createElement('button');
                    btn.className = "text-left px-3 py-2 rounded-lg bg-slate-800/90 hover:bg-slate-700/90 text-xs text-slate-300 border border-slate-700/60 transition flex items-center gap-2";
                    btn.innerHTML = `
                        <span class="w-4 h-4 rounded text-[9px] font-mono font-bold bg-slate-900 text-slate-400 flex items-center justify-center shrink-0 border border-slate-700">${{String.fromCharCode(65 + oIdx)}}</span>
                        <span>${{opt}}</span>
                    `;

                    btn.onclick = () => {{
                        optsGrid.querySelectorAll('button').forEach(b => b.disabled = true);
                        expPanel.classList.remove('hidden');

                        if (oIdx === cp.correct) {{
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            expPanel.innerHTML = `
                                <div class="font-bold flex items-center gap-1.5 text-rose-400">
                                    <i data-lucide="check-circle-2" class="w-4 h-4"></i> Correct Concept!
                                </div>
                                <div class="text-[11px] text-slate-300">${{cp.explanation}}</div>
                            `;
                            playTone(523.25, 0.15, 'sine');
                        }} else {{
                            btn.classList.add('bg-slate-800', 'text-slate-400', 'border-rose-500/50', 'font-bold');
                            expPanel.innerHTML = `
                                <div class="font-bold flex items-center gap-1.5 text-amber-400">
                                    <i data-lucide="alert-circle" class="w-4 h-4"></i> Incorrect (Correct Answer: ${{String.fromCharCode(65 + cp.correct)}})
                                </div>
                                <div class="text-[11px] text-slate-300">${{cp.explanation}}</div>
                            `;
                            playTone(220, 0.2, 'sawtooth');
                        }}
                        lucide.createIcons();
                    }};
                    optsGrid.appendChild(btn);
                }});

                box.appendChild(optsGrid);
                box.appendChild(expPanel);
                container.appendChild(box);
            }});
        }}

        // Render Quiz Slides (Slides 17 to 20)
        function renderQuizSlide(questions) {{
            const list = document.getElementById('quizQuestionsList');
            list.innerHTML = '';
            let score = 0;
            document.getElementById('quizScoreVal').textContent = score;

            questions.forEach((qObj, qIdx) => {{
                const card = document.createElement('div');
                card.className = "p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3";

                const header = document.createElement('div');
                header.className = "flex items-start justify-between gap-2";
                header.innerHTML = `
                    <div class="text-xs font-semibold text-white flex items-start gap-2">
                        <span class="w-6 h-6 rounded-lg bg-rose-950 text-rose-400 border border-rose-800/50 flex items-center justify-center text-xs font-mono font-bold shrink-0">${{qIdx+1}}</span>
                        <span class="mt-0.5">${{qObj.q}}</span>
                    </div>
                `;
                card.appendChild(header);

                const optsGrid = document.createElement('div');
                optsGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1";

                const resultBar = document.createElement('div');
                resultBar.className = "hidden flex items-center justify-between text-xs pt-1";

                qObj.options.forEach((opt, oIdx) => {{
                    const btn = document.createElement('button');
                    btn.className = "text-left px-3 py-2 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-xs text-slate-300 border border-slate-700/60 transition flex items-center gap-2";
                    btn.innerHTML = `
                        <span class="w-4 h-4 rounded text-[9px] font-mono font-bold bg-slate-900 text-slate-400 flex items-center justify-center shrink-0 border border-slate-700">${{String.fromCharCode(65 + oIdx)}}</span>
                        <span>${{opt}}</span>
                    `;

                    btn.onclick = () => {{
                        optsGrid.querySelectorAll('button').forEach(b => b.disabled = true);
                        resultBar.classList.remove('hidden');

                        if (oIdx === qObj.correct) {{
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            score++;
                            document.getElementById('quizScoreVal').textContent = score;
                            resultBar.innerHTML = `
                                <span class="text-rose-400 font-bold flex items-center gap-1">
                                    <i data-lucide="check" class="w-4 h-4"></i> Correct Answer
                                </span>
                                <button onclick="window.openSolutionModal(${{currentSlideIndex - 16}}, ${{qIdx}})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 text-[11px] font-semibold transition">
                                    View Solution
                                </button>
                            `;
                            playTone(587.33, 0.12, 'triangle');
                        }} else {{
                            btn.classList.add('bg-slate-800', 'text-slate-400', 'border-rose-500/50', 'font-bold');
                            resultBar.innerHTML = `
                                <span class="text-amber-400 font-bold flex items-center gap-1">
                                    <i data-lucide="x" class="w-4 h-4"></i> Incorrect (Correct: ${{String.fromCharCode(65 + qObj.correct)}})
                                </span>
                                <button onclick="window.openSolutionModal(${{currentSlideIndex - 16}}, ${{qIdx}})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 text-[11px] font-semibold transition">
                                    View Solution
                                </button>
                            `;
                            playTone(220, 0.2, 'sawtooth');
                        }}
                        lucide.createIcons();
                    }};
                    optsGrid.appendChild(btn);
                }});

                card.appendChild(optsGrid);
                card.appendChild(resultBar);
                list.appendChild(card);
            }});
        }}

        // Solution Pop-Up Modal Logic
        window.openSolutionModal = function(quizIdx, qIdx) {{
            const qObj = QUIZZES[quizIdx].questions[qIdx];
            document.getElementById('modalQuestionText').textContent = qObj.q;
            document.getElementById('modalAnswerText').textContent = `${{String.fromCharCode(65 + qObj.correct)}}. ${{qObj.options[qObj.correct]}}`;
            document.getElementById('modalExplanationText').textContent = qObj.solution;
            document.getElementById('solutionModal').classList.remove('hidden');
            lucide.createIcons();
        }};

        window.closeSolutionModal = function() {{
            document.getElementById('solutionModal').classList.add('hidden');
        }};

        // Voiceover Controller (Web Speech API)
        function initSpeechControls() {{
            if (!('speechSynthesis' in window)) {{
                document.getElementById('speechStatusIndicator').textContent = "Speech API Unavailable";
                return;
            }}
        }}

        window.toggleSpeech = function() {{
            if (isSpeaking) {{
                stopSpeech();
            }} else {{
                playSpeech();
            }}
        }};

        function playSpeech() {{
            if (!synth) return;
            synth.cancel();

            let text = "";
            if (currentSlideIndex < 16) {{
                const s = SLIDES[currentSlideIndex];
                text = `${{s.title}}. ${{s.subtitle}}. ${{s.narration}}`;
            }} else {{
                const q = QUIZZES[currentSlideIndex - 16];
                text = `${{q.quiz_title}}. ${{q.narration}}`;
            }}

            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.rate = 0.98;
            currentUtterance.pitch = 1.05;
            currentUtterance.lang = 'en-US';

            const voices = synth.getVoices();
            const preferredVoice = voices.find(v => (v.name.includes('Samantha') || v.name.includes('Zira') || v.name.includes('Female') || v.name.includes('Google UK English Female')) && v.lang.startsWith('en'));
            if (preferredVoice) currentUtterance.voice = preferredVoice;

            currentUtterance.onstart = () => {{
                isSpeaking = true;
                document.getElementById('speechIcon').setAttribute('data-lucide', 'pause');
                document.getElementById('speechStatusIndicator').textContent = "Speaking...";
                document.getElementById('speechStatusIndicator').className = "text-[10px] font-mono px-2 py-0.5 rounded bg-rose-950 text-rose-400 border border-rose-800";
                document.getElementById('teacherMouth').classList.add('talking');
                lucide.createIcons();
            }};

            currentUtterance.onend = () => {{
                stopSpeechUI();
            }};

            currentUtterance.onerror = () => {{
                stopSpeechUI();
            }};

            synth.speak(currentUtterance);
        }}

        window.stopSpeech = function() {{
            if (synth) synth.cancel();
            stopSpeechUI();
        }};

        function stopSpeechUI() {{
            isSpeaking = false;
            document.getElementById('speechIcon').setAttribute('data-lucide', 'volume-2');
            document.getElementById('speechStatusIndicator').textContent = "Ready";
            document.getElementById('speechStatusIndicator').className = "text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400";
            document.getElementById('teacherMouth').classList.remove('talking');
            lucide.createIcons();
        }}

        // Dispatcher for 16 Bespoke Interactive SVG Simulators
        function renderSimulator(slideIdx) {{
            const vp = document.getElementById('simulatorViewport');
            const titleEl = document.getElementById('simulatorTitle');

            switch(slideIdx) {{
                case 0:
                    titleEl.textContent = "Clonal Replication vs Genetic Diversity";
                    renderSim1(vp); break;
                case 1:
                    titleEl.textContent = "Asexual Fission, Budding & Sporogenesis";
                    renderSim2(vp); break;
                case 2:
                    titleEl.textContent = "Fragmentation, Regeneration & Vegetative Buds";
                    renderSim3(vp); break;
                case 3:
                    titleEl.textContent = "Floral Anatomy 3D Dissection Model";
                    renderSim4(vp); break;
                case 4:
                    titleEl.textContent = "Pollination Simulator: Wind vs Biotic Vectors";
                    renderSim5(vp); break;
                case 5:
                    titleEl.textContent = "Chemotropism & Double Fertilisation in Angiosperms";
                    renderSim6(vp); break;
                case 6:
                    titleEl.textContent = "Ovule to Seed & Ovary to Fruit Morphing Lab";
                    renderSim7(vp); break;
                case 7:
                    titleEl.textContent = "Male Reproductive System & Sperm Ultrastructure";
                    renderSim8(vp); break;
                case 8:
                    titleEl.textContent = "Female Reproductive System & Ovulation Journey";
                    renderSim9(vp); break;
                case 9:
                    titleEl.textContent = "28-Day Menstrual Cycle Hormone Dial";
                    renderSim10(vp); break;
                case 10:
                    titleEl.textContent = "Fertilisation, Blastocyst & Placental Exchange";
                    renderSim11(vp); break;
                case 11:
                    titleEl.textContent = "Evolutionary Fuel: Variations in Changing Niches";
                    renderSim12(vp); break;
                case 12:
                    titleEl.textContent = "Reproductive Health, STIs & Heat/Toxin Toxicity";
                    renderSim13(vp); break;
                case 13:
                    titleEl.textContent = "Contraceptive Methods Interactive Decision Matrix";
                    renderSim14(vp); break;
                case 14:
                    titleEl.textContent = "Assisted Reproductive Technologies (IVF/ICSI)";
                    renderSim15(vp); break;
                case 15:
                    titleEl.textContent = "Acharya Sushruta & Prof. Panchanan Maheshwari";
                    renderSim16(vp); break;
                default:
                    vp.innerHTML = `<div class="text-slate-400 text-xs">Simulator initialized.</div>`;
            }}
        }}

        // Quiz Simulator Rendering for Slides 17 to 20
        function renderQuizSimulator(quizIdx) {{
            const vp = document.getElementById('simulatorViewport');
            const titleEl = document.getElementById('simulatorTitle');
            titleEl.textContent = "Mastery Challenge Interactive Board";

            const topics = [
                "Asexual Modalities & Flowering Plant Reproduction",
                "Human Reproductive Systems, Spermatogenesis & Menstrual Cycle",
                "Embryology, Contraceptive Strategies & Reproductive Health",
                "Genetic Variations, Assisted Technologies (ART) & Indian Science"
            ];

            vp.innerHTML = `
                <div class="w-full flex flex-col items-center justify-center p-4 text-center space-y-4">
                    <div class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-rose-600 via-pink-600 to-amber-400 p-1 shadow-xl flex items-center justify-center">
                        <div class="w-full h-full bg-slate-950 rounded-xl flex items-center justify-center">
                            <i data-lucide="award" class="w-10 h-10 text-rose-400"></i>
                        </div>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono text-rose-400 font-bold uppercase tracking-wider">Evaluation Domain</div>
                        <h4 class="text-sm font-bold text-white mt-1">${{topics[quizIdx]}}</h4>
                        <p class="text-xs text-slate-400 max-w-xs mx-auto mt-1">
                            Answer each question on the left to reveal instant feedback and comprehensive step-by-step scientific solutions.
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 w-full max-w-xs text-left text-xs space-y-1.5 font-mono">
                        <div class="flex justify-between text-slate-300">
                            <span>Stage:</span>
                            <span class="text-rose-400 font-bold">Quiz ${{quizIdx + 1}} of 4</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Questions:</span>
                            <span class="text-white">10 MCQs</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Passing Standard:</span>
                            <span class="text-pink-300">80% Mastery</span>
                        </div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        // SIMULATOR 1: Clonal Replication vs Genetic Diversity
        function renderSim1(vp) {{
            let mode = 'asexual'; // 'asexual' or 'sexual'
            let stress = 30; // 0 to 100

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim1SetMode('asexual')" class="py-1.5 rounded-lg transition ${{mode === 'asexual' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Asexual Clones (1 Parent)
                            </button>
                            <button onclick="window.sim1SetMode('sexual')" class="py-1.5 rounded-lg transition ${{mode === 'sexual' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Sexual Diversity (2 Parents)
                            </button>
                        </div>

                        <!-- Graphical Petri Dish Population -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative overflow-hidden">
                            <svg width="220" height="150" viewBox="0 0 220 150">
                                <!-- Petri Dish Glass Circle -->
                                <circle cx="110" cy="75" r="68" fill="#0f172a" stroke="#475569" stroke-width="2.5"/>
                                
                                ${{mode === 'asexual' ? `
                                    <!-- Identical Green Clones -->
                                    ${{[
                                        [80,50],[110,45],[140,55],[75,85],[105,80],[135,90],[95,110],[125,115]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="${{stress > 60 ? 2 : 7}}" fill="${{stress > 60 ? '#ef4444' : '#10b981'}}" stroke="${{stress > 60 ? '#b91c1c' : '#059669'}}" stroke-width="1.5" opacity="${{stress > 60 ? 0.2 : 0.9}}"/>
                                    `).join('')}}
                                    ${{stress > 60 ? `
                                        <text x="50" y="80" fill="#ef4444" font-size="11" font-family="JetBrains Mono" font-weight="bold">Colony Extinction!</text>
                                    ` : ''}}
                                ` : `
                                    <!-- Diverse Varied Sexual Population with Different Alleles -->
                                    ${{[
                                        [80,50,'#f43f5e'],[110,45,'#38bdf8'],[140,55,'#f59e0b'],
                                        [75,85,'#a855f7'],[105,80,'#10b981'],[135,90,'#ec4899'],
                                        [95,110,'#e11d48'],[125,115,'#06b6d4']
                                    ].map(([cx,cy,col]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="7" fill="${{col}}" stroke="#ffffff" stroke-width="1" opacity="0.9"/>
                                    `).join('')}}
                                    ${{stress > 60 ? `
                                        <text x="50" y="80" fill="#10b981" font-size="11" font-family="JetBrains Mono" font-weight="bold">Resilient Variants Survive</text>
                                    ` : ''}}
                                `}}
                            </svg>
                        </div>

                        <!-- Environmental Stress Slider -->
                        <div class="space-y-1">
                            <div class="flex justify-between text-xs text-slate-300 font-mono">
                                <span>Environmental Heat / Disease Stress:</span>
                                <span class="text-rose-400 font-bold">${{stress}}%</span>
                            </div>
                            <input type="range" min="0" max="100" value="${{stress}}" oninput="window.sim1SetStress(this.value)" class="w-full accent-rose-500 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        </div>

                        <!-- Description Pill -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'asexual' ? 
                                '<span class="text-cyan-400 font-bold">Asexual Cloning:</span> Identical genetic copies mean an entire population shares the same vulnerability to environmental catastrophe.' : 
                                '<span class="text-rose-400 font-bold">Sexual Recombination:</span> Meiotic variation generates diverse traits, ensuring resilient individuals survive niche shifts.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim1SetMode = function(m) {{
                mode = m;
                playTone(m === 'asexual' ? 380 : 520, 0.1);
                draw();
            }};

            window.sim1SetStress = function(val) {{
                stress = parseInt(val);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 2: Asexual Fission, Budding & Sporogenesis
        function renderSim2(vp) {{
            let mode = 'amoeba'; // 'amoeba', 'leishmania', 'plasmodium', 'hydra', 'rhizopus'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[9px] font-bold">
                            <button onclick="window.sim2Set('amoeba')" class="py-1 rounded transition ${{mode === 'amoeba' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Amoeba</button>
                            <button onclick="window.sim2Set('leishmania')" class="py-1 rounded transition ${{mode === 'leishmania' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Leishmania</button>
                            <button onclick="window.sim2Set('plasmodium')" class="py-1 rounded transition ${{mode === 'plasmodium' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Plasmodium</button>
                            <button onclick="window.sim2Set('hydra')" class="py-1 rounded transition ${{mode === 'hydra' ? 'bg-pink-600 text-white' : 'bg-slate-800 text-slate-400'}}">Hydra</button>
                            <button onclick="window.sim2Set('rhizopus')" class="py-1 rounded transition ${{mode === 'rhizopus' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">Rhizopus</button>
                        </div>

                        <!-- Graphical Canvas -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'amoeba' ? `
                                    <!-- Amoeba simple binary fission -->
                                    <path d="M40,75 Q25,50 50,40 Q75,30 90,55 Q105,75 80,100 Q55,110 40,75 Z" fill="#047857" stroke="#10b981" stroke-width="2"/>
                                    <ellipse cx="65" cy="70" rx="9" ry="6" fill="#022c22"/>
                                    <!-- Daughter forming -->
                                    <path d="M140,75 Q125,50 150,40 Q175,30 190,55 Q205,75 180,100 Q155,110 140,75 Z" fill="#047857" stroke="#10b981" stroke-width="2"/>
                                    <ellipse cx="165" cy="70" rx="9" ry="6" fill="#022c22"/>
                                    <text x="65" y="130" fill="#34d399" font-size="9" font-family="JetBrains Mono">Binary Fission (Any Plane)</text>
                                ` : mode === 'leishmania' ? `
                                    <!-- Leishmania longitudinal cleavage -->
                                    <ellipse cx="110" cy="80" rx="18" ry="40" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                                    <line x1="110" y1="40" x2="110" y2="120" stroke="#0f172a" stroke-width="3" stroke-dasharray="4,2"/>
                                    <!-- Whip flagellum -->
                                    <path d="M110,40 Q130,20 120,5" fill="none" stroke="#e0f2fe" stroke-width="2.5"/>
                                    <circle cx="110" cy="70" r="5" fill="#082f49"/>
                                    <text x="50" y="140" fill="#38bdf8" font-size="9" font-family="JetBrains Mono">Longitudinal Plane Fission</text>
                                ` : mode === 'plasmodium' ? `
                                    <!-- Multiple fission in cyst -->
                                    <circle cx="110" cy="70" r="45" fill="#451a03" stroke="#f59e0b" stroke-width="3"/>
                                    ${{[
                                        [95,55],[120,55],[105,70],[85,75],[125,75],[100,90],[115,90]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="6" fill="#fde68a" stroke="#d97706"/>
                                    `).join('')}}
                                    <text x="55" y="135" fill="#fbbf24" font-size="9" font-family="JetBrains Mono">Multiple Fission in Cyst</text>
                                ` : mode === 'hydra' ? `
                                    <!-- Hydra with growing lateral bud -->
                                    <path d="M80,120 Q85,70 85,30 M85,30 Q65,10 60,5 M85,30 Q80,5 85,2 M85,30 Q105,10 110,5" stroke="#ec4899" stroke-width="4" fill="none"/>
                                    <!-- Lateral bud -->
                                    <path d="M85,80 Q120,75 135,70 M135,70 Q145,60 148,55 M135,70 Q145,75 150,75" stroke="#f472b6" stroke-width="2.5" fill="none"/>
                                    <text x="75" y="140" fill="#f472b6" font-size="9" font-family="JetBrains Mono">Budding in Hydra</text>
                                ` : `
                                    <!-- Rhizopus sporangium with releasing spores -->
                                    <line x1="110" y1="130" x2="110" y2="55" stroke="#6366f1" stroke-width="3"/>
                                    <circle cx="110" cy="55" r="22" fill="#312e81" stroke="#818cf8" stroke-width="2"/>
                                    <!-- Releasing spores -->
                                    <circle cx="140" cy="40" r="3.5" fill="#c7d2fe"/>
                                    <circle cx="155" cy="55" r="3" fill="#c7d2fe"/>
                                    <circle cx="145" cy="70" r="3" fill="#c7d2fe"/>
                                    <text x="60" y="140" fill="#a5b4fc" font-size="9" font-family="JetBrains Mono">Sporangium Spore Burst</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Mechanism Fact -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'amoeba' ? 'Amoeba splits into two equal daughter cells in any arbitrary plane.' : 
                              mode === 'leishmania' ? 'Leishmania divides strictly longitudinally in relation to its whip-like flagellum.' : 
                              mode === 'plasmodium' ? 'Plasmodium divides inside a protective cyst into multiple daughter cells (multiple fission).' : 
                              mode === 'hydra' ? 'Hydra uses regenerative cells to form a bud that matures and detaches as a clone.' : 
                              'Rhizopus houses hundreds of resistant spores in globular sporangia that disperse by wind.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim2Set = function(m) {{
                mode = m;
                playTone(400, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 3: Fragmentation, Regeneration & Vegetative Buds
        function renderSim3(vp) {{
            let mode = 'bryophyllum'; // 'spirogyra', 'planaria', 'bryophyllum'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim3Set('spirogyra')" class="py-1.5 rounded transition ${{mode === 'spirogyra' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Spirogyra</button>
                            <button onclick="window.sim3Set('planaria')" class="py-1.5 rounded transition ${{mode === 'planaria' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Planaria</button>
                            <button onclick="window.sim3Set('bryophyllum')" class="py-1.5 rounded transition ${{mode === 'bryophyllum' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">Bryophyllum</button>
                        </div>

                        <!-- Canvas SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'spirogyra' ? `
                                    <!-- Spirogyra breaking into fragments -->
                                    <rect x="25" y="60" width="85" height="25" fill="#047857" stroke="#10b981" stroke-width="2" rx="3"/>
                                    <rect x="130" y="60" width="85" height="25" fill="#047857" stroke="#10b981" stroke-width="2" rx="3"/>
                                    <!-- Spiral chloroplast ribbon -->
                                    <path d="M25,72 Q45,62 65,72 T105,72" stroke="#34d399" stroke-width="3" fill="none"/>
                                    <path d="M130,72 Q150,62 170,72 T210,72" stroke="#34d399" stroke-width="3" fill="none"/>
                                    <text x="65" y="115" fill="#34d399" font-size="9" font-family="JetBrains Mono">Fragmentation Cleavage</text>
                                ` : mode === 'planaria' ? `
                                    <!-- Planaria cut into 3 regenerating pieces -->
                                    <g transform="translate(40, 25)">
                                        <polygon points="20,0 35,25 5,25" fill="#d97706"/>
                                        <circle cx="16" cy="12" r="1.5" fill="#ffffff"/>
                                        <circle cx="24" cy="12" r="1.5" fill="#ffffff"/>
                                        <rect x="5" y="32" width="30" height="25" fill="#d97706"/>
                                        <polygon points="5,64 35,64 20,90" fill="#d97706"/>
                                    </g>
                                    <!-- Regeneration Arrows -->
                                    <text x="100" y="70" fill="#fbbf24" font-size="16">➔</text>
                                    <g transform="translate(140, 30)">
                                        <!-- Complete regenerated planaria -->
                                        <path d="M20,10 Q35,30 35,60 Q35,80 20,95 Q5,80 5,60 Q5,30 20,10 Z" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
                                        <circle cx="16" cy="25" r="2" fill="#ffffff"/>
                                        <circle cx="24" cy="25" r="2" fill="#ffffff"/>
                                    </g>
                                    <text x="50" y="140" fill="#fbbf24" font-size="9" font-family="JetBrains Mono">Regeneration via Neoblasts</text>
                                ` : `
                                    <!-- Bryophyllum Leaf with foliar buds in notches -->
                                    <path d="M110,135 Q50,110 40,75 Q35,40 110,15 Q185,40 180,75 Q170,110 110,135 Z" fill="#065f46" stroke="#10b981" stroke-width="2.5"/>
                                    <!-- Notch miniature plantlets with rootlets -->
                                    <circle cx="40" cy="75" r="5" fill="#34d399"/>
                                    <path d="M40,80 L32,88 M40,80 L35,92" stroke="#78350f" stroke-width="1.5"/>
                                    <circle cx="180" cy="75" r="5" fill="#34d399"/>
                                    <path d="M180,80 L188,88 M180,80 L185,92" stroke="#78350f" stroke-width="1.5"/>
                                    <circle cx="65" cy="45" r="4.5" fill="#34d399"/>
                                    <circle cx="155" cy="45" r="4.5" fill="#34d399"/>
                                    <text x="45" y="145" fill="#34d399" font-size="9" font-family="JetBrains Mono">Bryophyllum Leaf Marginal Buds</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Info Pill -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'spirogyra' ? 'Spirogyra simply fragments upon maturity into independent growing filaments.' : 
                              mode === 'planaria' ? 'Planaria pieces regenerate into complete organisms via specialized proliferating cells.' : 
                              'Bryophyllum leaves bear adventitious vegetative buds in marginal notches that root into new plants.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim3Set = function(m) {{
                mode = m;
                playTone(450, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 4: Floral Anatomy 3D Dissection Model
        function renderSim4(vp) {{
            let highlighted = 'stamen'; // 'calyx', 'corolla', 'stamen', 'carpel'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim4Set('calyx')" class="py-1.5 rounded transition ${{highlighted === 'calyx' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Calyx</button>
                            <button onclick="window.sim4Set('corolla')" class="py-1.5 rounded transition ${{highlighted === 'corolla' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Corolla</button>
                            <button onclick="window.sim4Set('stamen')" class="py-1.5 rounded transition ${{highlighted === 'stamen' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Stamen</button>
                            <button onclick="window.sim4Set('carpel')" class="py-1.5 rounded transition ${{highlighted === 'carpel' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">Carpel</button>
                        </div>

                        <!-- Flower Cutaway Diagram SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-48 relative">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Pedicel & Receptacle -->
                                <line x1="120" y1="165" x2="120" y2="135" stroke="#15803d" stroke-width="6"/>
                                <ellipse cx="120" cy="135" rx="22" ry="8" fill="#166534"/>

                                <!-- Calyx / Sepals -->
                                <path d="M100,135 Q75,130 65,120 M140,135 Q165,130 175,120" stroke="${{highlighted === 'calyx' ? '#22c55e' : '#15803d'}}" stroke-width="${{highlighted === 'calyx' ? 6 : 3}}" fill="none"/>

                                <!-- Corolla / Petals -->
                                <path d="M98,135 Q40,90 55,40 Q90,70 105,100" fill="${{highlighted === 'corolla' ? '#f43f5e' : '#be123c'}}" opacity="0.85"/>
                                <path d="M142,135 Q200,90 185,40 Q150,70 135,100" fill="${{highlighted === 'corolla' ? '#f43f5e' : '#be123c'}}" opacity="0.85"/>

                                <!-- Stamens (Filament + Anther) -->
                                <g stroke="${{highlighted === 'stamen' ? '#f59e0b' : '#b45309'}}" stroke-width="2.5">
                                    <path d="M110,130 Q90,90 85,55" fill="none"/>
                                    <ellipse cx="85" cy="52" rx="6" ry="4" fill="#fbbf24"/>
                                    <path d="M130,130 Q150,90 155,55" fill="none"/>
                                    <ellipse cx="155" cy="52" rx="6" ry="4" fill="#fbbf24"/>
                                </g>

                                <!-- Central Carpel (Stigma + Style + Ovary + Ovule) -->
                                <g fill="${{highlighted === 'carpel' ? '#2dd4bf' : '#0f766e'}}">
                                    <!-- Ovary -->
                                    <ellipse cx="120" cy="115" rx="16" ry="20" stroke="#14b8a6" stroke-width="2"/>
                                    <!-- Ovule inside -->
                                    <circle cx="120" cy="115" r="5" fill="#fef08a"/>
                                    <!-- Style -->
                                    <line x1="120" y1="95" x2="120" y2="40" stroke="#14b8a6" stroke-width="4"/>
                                    <!-- Sticky Stigma -->
                                    <ellipse cx="120" cy="38" rx="8" ry="4" fill="#5eead4"/>
                                </g>
                            </svg>
                        </div>

                        <!-- Organ Description -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{highlighted === 'calyx' ? '<span class="text-emerald-400 font-bold">Calyx (Sepals):</span> Green outer whorl that shields the delicate bud prior to blooming.' : 
                              highlighted === 'corolla' ? '<span class="text-rose-400 font-bold">Corolla (Petals):</span> Pigmented, scented petals that attract insect and bird pollinators.' : 
                              highlighted === 'stamen' ? '<span class="text-amber-400 font-bold">Stamen (Androecium):</span> Male unit made of filament and anther producing haploid pollen.' : 
                              '<span class="text-teal-400 font-bold">Carpel (Gynoecium):</span> Female unit with sticky stigma, style conduit, and ovary with ovules.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim4Set = function(h) {{
                highlighted = h;
                playTone(480, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 5: Pollination Simulator: Wind vs Biotic Vectors (C-2.8, C-4.3)
        function renderSim5(vp) {{
            let mode = 'biotic'; // 'wind' or 'biotic'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim5Set('wind')" class="py-1.5 rounded-lg transition ${{mode === 'wind' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Abiotic Wind (Anemophily)
                            </button>
                            <button onclick="window.sim5Set('biotic')" class="py-1.5 rounded-lg transition ${{mode === 'biotic' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Biotic Honeybee (Entomophily)
                            </button>
                        </div>

                        <!-- Pollination Animation Canvas -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative overflow-hidden">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'wind' ? `
                                    <!-- Wind blowing corn / grass pollen -->
                                    <path d="M30,120 L30,40 M30,40 L15,25 M30,40 L45,25" stroke="#16a34a" stroke-width="3"/>
                                    <!-- Feathery Stigma -->
                                    <path d="M190,120 L190,45 M190,45 L175,30 M190,45 L205,30 M190,40 L175,20 M190,40 L205,20" stroke="#facc15" stroke-width="2"/>
                                    <!-- Drifting Pollen grains -->
                                    ${{[0,1,2,3,4,5,6].map(i => `
                                        <circle cx="${{60 + i*18}}" cy="${{35 + (i%3)*10}}" r="2.5" fill="#fef08a" class="animate-pulse"/>
                                    `).join('')}}
                                    <text x="65" y="90" fill="#38bdf8" font-size="9" font-family="JetBrains Mono">Wind Current Carrier</text>
                                ` : `
                                    <!-- Biotic Honeybee carrying pollen -->
                                    <!-- Flower 1 (Donor) -->
                                    <ellipse cx="40" cy="110" rx="20" ry="15" fill="#e11d48"/>
                                    <circle cx="40" cy="100" r="4" fill="#fbbf24"/>
                                    <!-- Flower 2 (Recipient) -->
                                    <ellipse cx="200" cy="110" rx="20" ry="15" fill="#e11d48"/>
                                    <circle cx="200" cy="100" r="4" fill="#fbbf24"/>
                                    <!-- Honeybee hovering -->
                                    <g transform="translate(115, 60)" class="animate-bounce">
                                        <ellipse cx="0" cy="0" rx="14" ry="9" fill="#eab308"/>
                                        <line x1="-6" y1="-8" x2="-6" y2="8" stroke="#1e293b" stroke-width="2.5"/>
                                        <line x1="2" y1="-8" x2="2" y2="8" stroke="#1e293b" stroke-width="2.5"/>
                                        <!-- Translucent wings -->
                                        <ellipse cx="-4" cy="-12" rx="9" ry="5" fill="#e0f2fe" opacity="0.7"/>
                                        <!-- Dusting of golden pollen -->
                                        <circle cx="6" cy="4" r="2" fill="#fbbf24"/>
                                        <circle cx="10" cy="1" r="2" fill="#fbbf24"/>
                                    </g>
                                    <text x="55" y="140" fill="#f59e0b" font-size="9" font-family="JetBrains Mono">Plant-Pollinator Co-Evolution</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-2.8 Mutualism Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'wind' ? 
                                '<span class="text-cyan-400 font-bold">Wind (Anemophily):</span> Light, non-sticky pollen produced in vast quantities to guarantee contact with feathery stigmas.' : 
                                '<span class="text-amber-400 font-bold">Biotic Mutualism (C-2.8):</span> Plants provide nectar rewards & aroma; insect pollinators transfer pollen for 35% of human food crops.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim5Set = function(m) {{
                mode = m;
                playTone(m === 'wind' ? 350 : 500, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 6: Chemotropism & Double Fertilisation in Angiosperms
        function renderSim6(vp) {{
            let progress = 75; // 0 to 100

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex justify-between items-center text-xs font-mono text-slate-300">
                            <span>Pollen Tube Chemotropic Elongation:</span>
                            <span class="text-rose-400 font-bold">${{progress}}%</span>
                        </div>
                        <input type="range" min="10" max="100" value="${{progress}}" oninput="window.sim6SetProg(this.value)" class="w-full accent-rose-500 bg-slate-800 rounded-lg h-2 cursor-pointer">

                        <!-- Longitudinal Section of Pistil with Pollen Tube SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-48">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Stigma -->
                                <ellipse cx="120" cy="20" rx="20" ry="7" fill="#0d9488" stroke="#14b8a6"/>
                                <!-- Germinating pollen grain on stigma -->
                                <circle cx="118" cy="16" r="4" fill="#fbbf24"/>

                                <!-- Style neck -->
                                <line x1="110" y1="25" x2="110" y2="90" stroke="#0f766e" stroke-width="2"/>
                                <line x1="130" y1="25" x2="130" y2="90" stroke="#0f766e" stroke-width="2"/>

                                <!-- Swollen Basal Ovary -->
                                <ellipse cx="120" cy="120" rx="30" ry="28" fill="#134e4a" stroke="#14b8a6" stroke-width="2"/>

                                <!-- Ovule & Embryo Sac -->
                                <ellipse cx="120" cy="120" rx="16" ry="18" fill="#042f2e" stroke="#2dd4bf" stroke-width="1.8"/>
                                <!-- Central Polar Nuclei -->
                                <circle cx="118" cy="118" r="2.5" fill="#fde047"/>
                                <circle cx="123" cy="118" r="2.5" fill="#fde047"/>
                                <!-- Egg cell near micropyle -->
                                <circle cx="120" cy="130" r="3.5" fill="#f43f5e"/>

                                <!-- Growing Pollen Tube (Chemotropic response) -->
                                <path d="M118,20 L118,${{20 + progress*0.8}} Q118,${{20 + progress*1.1}} ${{progress > 85 ? 120 : 118}},${{20 + progress*1.1}}" fill="none" stroke="#facc15" stroke-width="2.5"/>

                                ${{progress >= 95 ? `
                                    <!-- Double Fertilisation Event Highlight -->
                                    <circle cx="120" cy="130" r="6" fill="#f43f5e" opacity="0.8" class="animate-ping"/>
                                    <text x="145" y="132" fill="#f43f5e" font-size="8" font-family="JetBrains Mono">Syngamy (2n)</text>
                                    <text x="145" y="118" fill="#fde047" font-size="8" font-family="JetBrains Mono">Triple Fusion (3n)</text>
                                ` : ''}}
                            </svg>
                        </div>

                        <!-- Double Fertilisation Breakdown -->
                        <div class="grid grid-cols-2 gap-2 text-[10px] font-mono">
                            <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                <span class="text-rose-400 font-bold">1. Syngamy:</span>
                                <p class="text-slate-300">Male Gamete ($n$) + Egg ($n$) $\\to$ Zygote ($2n$)</p>
                            </div>
                            <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                <span class="text-amber-400 font-bold">2. Triple Fusion:</span>
                                <p class="text-slate-300">Male Gamete ($n$) + 2 Polar Nuclei ($2n$) $\\to$ Endosperm ($3n$)</p>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim6SetProg = function(v) {{
                progress = parseInt(v);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 7: Ovule to Seed & Ovary to Fruit Morphing Lab
        function renderSim7(vp) {{
            let stage = 'flower'; // 'flower', 'fruit', 'dispersal'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim7Set('flower')" class="py-1.5 rounded transition ${{stage === 'flower' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Ovary & Ovule</button>
                            <button onclick="window.sim7Set('fruit')" class="py-1.5 rounded transition ${{stage === 'fruit' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Ripened Fruit & Seed</button>
                            <button onclick="window.sim7Set('dispersal')" class="py-1.5 rounded transition ${{stage === 'dispersal' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Dispersal Vectors</button>
                        </div>

                        <!-- Transformation Canvas -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{stage === 'flower' ? `
                                    <!-- Swollen ovary with internal ovule -->
                                    <ellipse cx="120" cy="75" rx="45" ry="40" fill="#065f46" stroke="#10b981" stroke-width="2.5"/>
                                    <ellipse cx="120" cy="75" rx="18" ry="20" fill="#fde047" stroke="#eab308" stroke-width="2"/>
                                    <text x="85" y="30" fill="#34d399" font-size="10" font-family="JetBrains Mono" font-weight="bold">Ovary Wall</text>
                                    <text x="105" y="78" fill="#78350f" font-size="9" font-family="JetBrains Mono" font-weight="bold">Ovule</text>
                                ` : stage === 'fruit' ? `
                                    <!-- Ripened succulent fruit (e.g. mango/tomato) with tough seed inside -->
                                    <ellipse cx="120" cy="75" rx="55" ry="48" fill="#ea580c" stroke="#f97316" stroke-width="2.5"/>
                                    <!-- Hardened Seed (Testa + Cotyledons) -->
                                    <ellipse cx="120" cy="75" rx="20" ry="22" fill="#78350f" stroke="#b45309" stroke-width="3"/>
                                    <text x="75" y="22" fill="#fb923c" font-size="10" font-family="JetBrains Mono" font-weight="bold">Fruit (from Ovary)</text>
                                    <text x="102" y="78" fill="#fef08a" font-size="9" font-family="JetBrains Mono" font-weight="bold">Seed</text>
                                ` : `
                                    <!-- 4 Dispersal Vectors Graphic -->
                                    <!-- Wind Dandelion -->
                                    <circle cx="50" cy="50" r="12" fill="#e0f2fe"/>
                                    <text x="35" y="75" fill="#38bdf8" font-size="8" font-family="JetBrains Mono">Wind</text>
                                    <!-- Water Coconut -->
                                    <ellipse cx="120" cy="50" rx="14" ry="10" fill="#78350f"/>
                                    <text x="105" y="75" fill="#34d399" font-size="8" font-family="JetBrains Mono">Water</text>
                                    <!-- Animal Xanthium Bur -->
                                    <circle cx="190" cy="50" r="10" fill="#ca8a04"/>
                                    <text x="172" y="75" fill="#eab308" font-size="8" font-family="JetBrains Mono">Animal Bur</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Golden Curricular Rule -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono text-center">
                            <span class="text-rose-400 font-bold">Cardinal Botanical Rule: </span>
                            <span class="text-white">Ovule $\\to$ Seed; Ovary $\\to$ Ripened Fruit</span>
                        </div>
                    </div>
                `;
            }}

            window.sim7Set = function(s) {{
                stage = s;
                playTone(420, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 8: Male Reproductive System & Sperm Ultrastructure
        function renderSim8(vp) {{
            let view = 'anatomy'; // 'anatomy' vs 'sperm'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim8Set('anatomy')" class="py-1.5 rounded-lg transition ${{view === 'anatomy' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Pelvic Anatomy Cutaway
                            </button>
                            <button onclick="window.sim8Set('sperm')" class="py-1.5 rounded-lg transition ${{view === 'sperm' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Sperm Ultrastructure Zoom
                            </button>
                        </div>

                        <!-- Graphic Window -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-48">
                            ${{view === 'anatomy' ? `
                                <svg width="240" height="170" viewBox="0 0 240 170">
                                    <!-- Urinary Bladder -->
                                    <ellipse cx="140" cy="50" rx="25" ry="20" fill="#0f172a" stroke="#475569"/>
                                    <!-- Testis in Scrotal Pouch -->
                                    <rect x="75" y="110" width="45" height="50" rx="15" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
                                    <ellipse cx="98" cy="135" rx="14" ry="18" fill="#0369a1"/>
                                    <text x="65" y="105" fill="#38bdf8" font-size="8" font-family="JetBrains Mono">Scrotum (34.5°C)</text>

                                    <!-- Vas Deferens loop -->
                                    <path d="M102,125 Q105,70 135,70 Q155,70 150,90" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

                                    <!-- Prostate & Seminal Vesicle -->
                                    <circle cx="148" cy="80" r="8" fill="#d97706"/>
                                    <rect x="156" y="65" width="12" height="15" rx="3" fill="#f59e0b"/>

                                    <!-- Urethra through Penis -->
                                    <path d="M148,88 L148,125 L125,125 L125,145" fill="none" stroke="#64748b" stroke-width="7" stroke-linecap="round"/>
                                    <path d="M148,88 L148,125 L125,125 L125,145" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
                                </svg>
                            ` : `
                                <!-- Sperm high-power anatomy -->
                                <svg width="240" height="170" viewBox="0 0 240 170">
                                    <!-- Head with Acrosome cap & Nucleus -->
                                    <ellipse cx="45" cy="85" rx="18" ry="12" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                                    <!-- Acrosome enzymatic hood -->
                                    <path d="M45,73 Q30,85 45,97 Z" fill="#fb7185"/>
                                    <text x="25" y="60" fill="#fb7185" font-size="8" font-family="JetBrains Mono">Acrosome</text>

                                    <!-- Middle piece (Spiral Mitochondria) -->
                                    <rect x="63" y="80" width="30" height="10" rx="2" fill="#047857" stroke="#10b981"/>
                                    <text x="62" y="68" fill="#34d399" font-size="8" font-family="JetBrains Mono">Mitochondria</text>

                                    <!-- Flagellum Tail -->
                                    <path d="M93,85 Q130,65 160,95 T220,85" fill="none" stroke="#cbd5e1" stroke-width="3" stroke-linecap="round" class="animate-pulse"/>
                                    <text x="175" y="68" fill="#cbd5e1" font-size="8" font-family="JetBrains Mono">Tail</text>
                                </svg>
                            `}}
                        </div>

                        <!-- Scrotal Temperature Note -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-center">
                            <span class="text-cyan-400 font-bold">Thermoregulation: </span>
                            <span class="text-slate-300">Scrotum maintains 2 to 2.5 °C lower temperature essential for viable spermatogenesis.</span>
                        </div>
                    </div>
                `;
            }}

            window.sim8Set = function(v) {{
                view = v;
                playTone(440, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 9: Female Reproductive System & Ovulation Journey
        function renderSim9(vp) {{
            let ovulated = false;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <button onclick="window.sim9Trigger()" class="w-full py-2 rounded-xl bg-gradient-to-r from-rose-600 to-pink-500 hover:from-rose-500 hover:to-pink-400 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-1.5">
                            <i data-lucide="play" class="w-4 h-4"></i>
                            <span>Trigger Ovulation & Ovum Transit</span>
                        </button>

                        <!-- Female Anatomy Diagram SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-48 relative">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Muscular Uterus -->
                                <path d="M90,70 Q120,45 150,70 L140,120 L100,120 Z" fill="#881337" stroke="#e11d48" stroke-width="2"/>
                                <!-- Endometrium cavity -->
                                <ellipse cx="120" cy="85" rx="14" ry="20" fill="#4c0519"/>

                                <!-- Cervix & Vagina -->
                                <rect x="110" y="120" width="20" height="35" fill="#9f1239" stroke="#e11d48"/>

                                <!-- Fallopian Tubes (Oviducts) -->
                                <path d="M90,70 Q60,40 35,55" stroke="#f43f5e" stroke-width="4" fill="none"/>
                                <path d="M150,70 Q180,40 205,55" stroke="#f43f5e" stroke-width="4" fill="none"/>

                                <!-- Fimbriae Funnels -->
                                <path d="M35,55 Q25,60 20,70" stroke="#fb7185" stroke-width="3" fill="none"/>
                                <path d="M205,55 Q215,60 220,70" stroke="#fb7185" stroke-width="3" fill="none"/>

                                <!-- Left & Right Ovaries -->
                                <ellipse cx="30" cy="80" rx="12" ry="16" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
                                <ellipse cx="210" cy="80" rx="12" ry="16" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>

                                <!-- Ovum Transit -->
                                ${{ovulated ? `
                                    <circle cx="60" cy="50" r="5" fill="#ffffff" stroke="#f43f5e" stroke-width="2" class="animate-ping"/>
                                    <text x="25" y="32" fill="#fbbf24" font-size="8" font-family="JetBrains Mono" font-weight="bold">Fertilisation Site in Oviduct</text>
                                ` : `
                                    <circle cx="30" cy="78" r="4" fill="#ffffff"/>
                                `}}
                            </svg>
                        </div>

                        <!-- Golden Fact -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-center">
                            <span class="text-rose-400 font-bold">Fertilisation Site: </span>
                            <span class="text-slate-300">Strictly occurs in the Fallopian Tube (Oviduct), not in the uterus!</span>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }}

            window.sim9Trigger = function() {{
                ovulated = !ovulated;
                playTone(ovulated ? 587.33 : 330, 0.15);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 10: 28-Day Menstrual Cycle Hormone Dial
        function renderSim10(vp) {{
            let day = 14; // Day 1 to 28

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex justify-between items-center text-xs font-mono text-slate-300">
                            <span>Cycle Day:</span>
                            <span class="text-rose-400 font-bold">Day ${{day}} / 28 (${{day <= 5 ? 'Menstrual' : day <= 13 ? 'Follicular' : day === 14 ? 'Ovulatory LH Surge' : 'Luteal Phase'}})</span>
                        </div>
                        <input type="range" min="1" max="28" value="${{day}}" oninput="window.sim10SetDay(this.value)" class="w-full accent-rose-500 bg-slate-800 rounded-lg h-2 cursor-pointer">

                        <!-- Hormone & Endometrium Curve SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                <!-- Endometrial Thickness Base -->
                                <path d="M10,130 Q${{day*7}},${{day <= 5 ? 130 : day <= 14 ? 110 : 85}} 230,${{day <= 5 ? 130 : 85}}" stroke="#e11d48" stroke-width="4" fill="none"/>
                                <rect x="10" y="${{day <= 5 ? 130 : day <= 14 ? 110 : 85}}" width="220" height="30" fill="#881337" opacity="0.3"/>

                                <!-- LH Surge Spike at Day 14 -->
                                <path d="M10,80 L100,75 L120,25 L140,75 L230,80" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="105" y="18" fill="#f59e0b" font-size="8" font-family="JetBrains Mono">LH Surge</text>

                                <!-- Progesterone peak during Luteal Phase (Day 15-28) -->
                                <path d="M10,95 L120,95 Q170,45 230,95" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
                                <text x="160" y="42" fill="#38bdf8" font-size="8" font-family="JetBrains Mono">Progesterone</text>

                                <!-- Vertical Indicator Line for Selected Day -->
                                <line x1="${{10 + day*7.8}}" y1="10" x2="${{10 + day*7.8}}" y2="140" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="3,3"/>
                            </svg>
                        </div>

                        <!-- Phase Summary Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{day <= 5 ? '<span class="text-rose-400 font-bold">Days 1–5 (Menstrual):</span> Progesterone drops; vascular endometrium sloughs off.' : 
                              day <= 13 ? '<span class="text-teal-400 font-bold">Days 6–13 (Follicular):</span> Estrogen rises, reconstructing endometrial lining.' : 
                              day === 14 ? '<span class="text-amber-400 font-bold">Day 14 (Ovulation):</span> Massive LH surge induces mature follicle to rupture.' : 
                              '<span class="text-cyan-400 font-bold">Days 15–28 (Luteal):</span> Corpus Luteum secretes progesterone to maintain pregnancy readiness.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim10SetDay = function(d) {{
                day = parseInt(d);
                playTone(250 + day * 15, 0.05);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 11: Fertilisation, Blastocyst & Placental Exchange
        function renderSim11(vp) {{
            let stage = 'placenta'; // 'syngamy', 'blastocyst', 'placenta'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim11Set('syngamy')" class="py-1.5 rounded transition ${{stage === 'syngamy' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Syngamy</button>
                            <button onclick="window.sim11Set('blastocyst')" class="py-1.5 rounded transition ${{stage === 'blastocyst' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Blastocyst</button>
                            <button onclick="window.sim11Set('placenta')" class="py-1.5 rounded transition ${{stage === 'placenta' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">Placental Villi</button>
                        </div>

                        <!-- Canvas SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{stage === 'syngamy' ? `
                                    <!-- Sperm penetrating ovum -->
                                    <circle cx="120" cy="75" r="40" fill="#be123c" stroke="#f43f5e" stroke-width="2.5"/>
                                    <circle cx="120" cy="75" r="14" fill="#881337"/>
                                    <!-- Sperm penetrating -->
                                    <polygon points="75,75 60,70 60,80" fill="#facc15"/>
                                    <path d="M60,75 L30,75" stroke="#facc15" stroke-width="2"/>
                                    <text x="65" y="135" fill="#f43f5e" font-size="9" font-family="JetBrains Mono">Monospermic Syngamy (2n)</text>
                                ` : stage === 'blastocyst' ? `
                                    <!-- Hollow blastocyst with inner cell mass -->
                                    <circle cx="120" cy="75" r="42" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                                    <!-- Trophoblast outer ring -->
                                    <circle cx="120" cy="75" r="38" fill="none" stroke="#d97706" stroke-width="3" stroke-dasharray="4,4"/>
                                    <!-- Inner Cell Mass (future embryo) -->
                                    <circle cx="105" cy="65" r="14" fill="#fbbf24"/>
                                    <text x="65" y="135" fill="#fbbf24" font-size="9" font-family="JetBrains Mono">Blastocyst (Day 7 Implantation)</text>
                                ` : `
                                    <!-- Hemochorial Placental Villi bathed in maternal blood -->
                                    <rect x="20" y="20" width="40" height="110" fill="#881337" rx="3"/>
                                    <text x="25" y="75" fill="#fca5a5" font-size="7" font-family="JetBrains Mono" transform="rotate(-90 25,75)">Uterine Wall</text>
                                    <!-- Intervillous Space with maternal blood -->
                                    <rect x="60" y="20" width="60" height="110" fill="#991b1b" opacity="0.4"/>
                                    <!-- Chorionic Villi branching -->
                                    <path d="M120,40 Q85,45 80,55 M120,75 Q85,75 75,75 M120,110 Q85,105 80,95" stroke="#38bdf8" stroke-width="4" fill="none"/>
                                    <!-- Umbilical Cord vessels -->
                                    <line x1="120" y1="75" x2="200" y2="75" stroke="#38bdf8" stroke-width="6"/>
                                    <line x1="120" y1="75" x2="200" y2="75" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
                                    <text x="135" y="65" fill="#38bdf8" font-size="8" font-family="JetBrains Mono">Umbilical Cord</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Placental Exchange Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <span class="text-teal-400 font-bold">Placental Diffusion: </span>
                            Mother supplies $O_2$ and glucose; fetus returns $CO_2$ and urea without direct blood mixing.
                        </div>
                    </div>
                `;
            }}

            window.sim11Set = function(s) {{
                stage = s;
                playTone(460, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 12: Evolutionary Fuel: Variations in Changing Niches (C-3.3)
        function renderSim12(vp) {{
            let stressType = 'antibiotic'; // 'antibiotic' or 'heat'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim12Set('antibiotic')" class="py-1.5 rounded-lg transition ${{stressType === 'antibiotic' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Virulent Antibiotic Attack
                            </button>
                            <button onclick="window.sim12Set('heat')" class="py-1.5 rounded-lg transition ${{stressType === 'heat' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Extreme Thermal Wave
                            </button>
                        </div>

                        <!-- Comparative Survival Canvas -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around h-44">
                            <!-- Dish 1: Clonal Asexual Population (100% Death) -->
                            <div class="flex flex-col items-center">
                                <span class="text-[10px] font-mono text-slate-400 mb-1">Clonal Asexual</span>
                                <div class="w-24 h-24 rounded-full border-2 border-slate-700 bg-slate-900 flex items-center justify-center relative">
                                    <span class="text-rose-500 font-bold font-mono text-[10px] text-center">TOTAL DIE-OFF<br>(0% Survival)</span>
                                </div>
                            </div>

                            <!-- Dish 2: Recombining Sexual Population (Variants Survive) -->
                            <div class="flex flex-col items-center">
                                <span class="text-[10px] font-mono text-emerald-400 font-bold mb-1">Sexual Recombination</span>
                                <div class="w-24 h-24 rounded-full border-2 border-emerald-700 bg-slate-900 flex items-center justify-center relative">
                                    <circle cx="35" cy="40" r="5" fill="#10b981"/>
                                    <circle cx="65" cy="55" r="5" fill="#10b981"/>
                                    <circle cx="45" cy="70" r="5" fill="#10b981"/>
                                    <span class="absolute bottom-2 text-[8px] font-mono text-emerald-300 font-bold">Variants Survive!</span>
                                </div>
                            </div>
                        </div>

                        <!-- Evolutionary Law -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <span class="text-rose-400 font-bold">C-3.3 Evolutionary Invariant: </span>
                            Variation is the raw substrate for natural selection, protecting species from catastrophic extinction.
                        </div>
                    </div>
                `;
            }}

            window.sim12Set = function(s) {{
                stressType = s;
                playTone(400, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 13: Reproductive Health, STIs & Heat/Toxin Toxicity (C-7.2)
        function renderSim13(vp) {{
            let mode = 'toxin'; // 'toxin' or 'heat'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim13Set('toxin')" class="py-1.5 rounded-lg transition ${{mode === 'toxin' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Heavy Metals (Lead/Cadmium)
                            </button>
                            <button onclick="window.sim13Set('heat')" class="py-1.5 rounded-lg transition ${{mode === 'heat' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Extreme Scrotal Heat
                            </button>
                        </div>

                        <!-- Graphical Diagnostic Scanner -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'toxin' ? `
                                    <!-- Heavy Metal Induced DNA Fragmentation -->
                                    <rect x="30" y="30" width="180" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                                    <!-- Fragmented DNA Ladder -->
                                    <line x1="50" y1="50" x2="80" y2="50" stroke="#ef4444" stroke-width="3"/>
                                    <line x1="50" y1="70" x2="70" y2="70" stroke="#ef4444" stroke-width="3"/>
                                    <line x1="50" y1="90" x2="85" y2="90" stroke="#ef4444" stroke-width="3"/>
                                    <text x="100" y="60" fill="#f59e0b" font-size="9" font-family="JetBrains Mono" font-weight="bold">Pb / Cd Toxicity</text>
                                    <text x="100" y="80" fill="#f87171" font-size="8" font-family="JetBrains Mono">Oxidative Stress (ROS)</text>
                                    <text x="100" y="98" fill="#f87171" font-size="8" font-family="JetBrains Mono">Sperm DNA Fragmentation</text>
                                ` : `
                                    <!-- Thermometer Showing Scrotal Heat Elevation -->
                                    <rect x="50" y="30" width="20" height="90" rx="10" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                                    <rect x="54" y="60" width="12" height="60" rx="6" fill="#ef4444"/>
                                    <circle cx="60" cy="115" r="14" fill="#ef4444"/>
                                    <text x="85" y="55" fill="#f87171" font-size="10" font-family="JetBrains Mono" font-weight="bold">> 37.0°C (Core Heat)</text>
                                    <text x="85" y="75" fill="#fbbf24" font-size="8" font-family="JetBrains Mono">Normal Scrotal: 34.5°C</text>
                                    <text x="85" y="95" fill="#f87171" font-size="8" font-family="JetBrains Mono">Germ Cell Apoptosis</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-7.2 Critical Inquiry Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <span class="text-rose-400 font-bold">C-7.2 Critical Inquiry: </span>
                            ${{mode === 'toxin' ? 
                                'Heavy metals (lead, cadmium) cross gonadal barriers, elevating reactive oxygen species that fragment sperm DNA.' : 
                                'Elevated scrotal heat suppresses spermatogenesis; testes require 2–2.5°C cooler temperatures to prevent germ cell death.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim13Set = function(m) {{
                mode = m;
                playTone(450, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 14: Contraceptive Methods Interactive Decision Matrix (C-5.2)
        function renderSim14(vp) {{
            let method = 'barrier'; // 'barrier', 'hormonal', 'iud', 'surgical'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim14Set('barrier')" class="py-1.5 rounded transition ${{method === 'barrier' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Barrier</button>
                            <button onclick="window.sim14Set('hormonal')" class="py-1.5 rounded transition ${{method === 'hormonal' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Hormonal</button>
                            <button onclick="window.sim14Set('iud')" class="py-1.5 rounded transition ${{method === 'iud' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">IUD (Cu-T)</button>
                            <button onclick="window.sim14Set('surgical')" class="py-1.5 rounded transition ${{method === 'surgical' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">Surgical</button>
                        </div>

                        <!-- Graphical Mode Viewer -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="140" viewBox="0 0 240 140">
                                ${{method === 'barrier' ? `
                                    <!-- Condom physical shield blocking sperm -->
                                    <path d="M40,70 L140,70 L140,55 Q160,55 160,70 Q160,85 140,85 L140,70" stroke="#f43f5e" stroke-width="4" fill="none"/>
                                    <!-- Blocked sperms -->
                                    <circle cx="110" cy="65" r="3" fill="#ffffff"/>
                                    <circle cx="120" cy="75" r="3" fill="#ffffff"/>
                                    <text x="50" y="125" fill="#f43f5e" font-size="9" font-family="JetBrains Mono" font-weight="bold">Dual Protection: Pregnancy & STIs</text>
                                ` : method === 'hormonal' ? `
                                    <!-- Oral Contraceptive Pill blister pack -->
                                    <rect x="40" y="30" width="160" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                                    ${{[0,1,2,3,4,5,6].map(i => `
                                        <circle cx="${{60 + i*18}}" cy="50" r="5" fill="#fbbf24"/>
                                        <circle cx="${{60 + i*18}}" cy="75" r="5" fill="#fbbf24"/>
                                    `).join('')}}
                                    <text x="55" y="125" fill="#fbbf24" font-size="9" font-family="JetBrains Mono" font-weight="bold">Inhibits Pituitary Ovulation</text>
                                ` : method === 'iud' ? `
                                    <!-- Copper-T intrauterine device -->
                                    <path d="M120,40 L120,100 M90,40 L150,40" stroke="#2dd4bf" stroke-width="6" stroke-linecap="round"/>
                                    <!-- Copper wire coiled -->
                                    <line x1="115" y1="50" x2="125" y2="50" stroke="#f97316" stroke-width="2"/>
                                    <line x1="115" y1="65" x2="125" y2="65" stroke="#f97316" stroke-width="2"/>
                                    <line x1="115" y1="80" x2="125" y2="80" stroke="#f97316" stroke-width="2"/>
                                    <text x="45" y="125" fill="#2dd4bf" font-size="9" font-family="JetBrains Mono" font-weight="bold">Copper-T: Spermicidal & Anti-Implantation</text>
                                ` : `
                                    <!-- Vasectomy / Tubectomy cut & tied conduit -->
                                    <line x1="40" y1="70" x2="95" y2="70" stroke="#818cf8" stroke-width="6"/>
                                    <circle cx="100" cy="70" r="4" fill="#ef4444"/>
                                    <line x1="110" y1="60" x2="110" y2="80" stroke="#ffffff" stroke-width="2"/>
                                    <circle cx="120" cy="70" r="4" fill="#ef4444"/>
                                    <line x1="125" y1="70" x2="180" y2="70" stroke="#818cf8" stroke-width="6"/>
                                    <text x="50" y="125" fill="#818cf8" font-size="9" font-family="JetBrains Mono" font-weight="bold">Permanent Surgical Sterilization</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Contraceptive Summary -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{method === 'barrier' ? '<span class="text-rose-400 font-bold">Barrier Method:</span> Condoms prevent sperm entry and are the ONLY method protecting against STIs.' : 
                              method === 'hormonal' ? '<span class="text-amber-400 font-bold">Hormonal Pills:</span> Synthetic estrogen/progesterone blocks pituitary LH surge and prevents ovulation.' : 
                              method === 'iud' ? '<span class="text-teal-400 font-bold">Copper-T:</span> Medically inserted into uterus; releases copper ions suppressing sperm motility.' : 
                              '<span class="text-indigo-400 font-bold">Surgical:</span> Vasectomy (vas deferens cut) & Tubectomy (fallopian tubes ligated); permanent and irreversible.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim14Set = function(m) {{
                method = m;
                playTone(430, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 15: Assisted Reproductive Technologies (IVF/ICSI) (C-7.1)
        function renderSim15(vp) {{
            let step = 2; // 1 to 4

            function draw() {{
                const steps = [
                    {{ title: "1. Oocyte Harvesting", desc: "Mature ova aspirated from ovarian follicles under ultrasound guidance." }},
                    {{ title: "2. ICSI Micro-Injection", desc: "Single viable sperm micro-injected directly into oocyte cytoplasm under inverted microscope." }},
                    {{ title: "3. Incubator Culture", desc: "Zygote cultured in nutrient media to 8-cell or blastocyst stage." }},
                    {{ title: "4. Embryo Transfer", desc: "Selected viable embryo transferred into receptive uterine endometrium for gestation." }}
                ];
                const cur = steps[step - 1];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">IVF / ICSI Workflow:</span>
                            <span class="text-rose-400 font-bold">Step ${{step}} of 4</span>
                        </div>

                        <!-- 4 Step Buttons -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800">
                            ${{[1,2,3,4].map(s => `
                                <button onclick="window.sim15Set(${{s}})" class="py-1 rounded text-xs font-mono font-bold transition ${{step === s ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                    S${{s}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Graphic Window -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="140" viewBox="0 0 240 140">
                                ${{step === 1 ? `
                                    <ellipse cx="120" cy="70" rx="35" ry="30" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                                    <!-- Aspiration needle -->
                                    <line x1="20" y1="20" x2="90" y2="65" stroke="#38bdf8" stroke-width="3"/>
                                    <text x="50" y="125" fill="#38bdf8" font-size="9" font-family="JetBrains Mono">Follicle Oocyte Retrieval</text>
                                ` : step === 2 ? `
                                    <!-- Holding pipette on left -->
                                    <rect x="20" y="60" width="60" height="20" fill="#334155" stroke="#64748b"/>
                                    <!-- Oocyte held -->
                                    <circle cx="120" cy="70" r="35" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                                    <!-- ICSI Injection micropipette with single sperm -->
                                    <line x1="210" y1="70" x2="110" y2="70" stroke="#38bdf8" stroke-width="2.5"/>
                                    <circle cx="118" cy="70" r="3" fill="#facc15"/>
                                    <text x="45" y="125" fill="#facc15" font-size="9" font-family="JetBrains Mono">ICSI Micropipette Injection</text>
                                ` : step === 3 ? `
                                    <!-- Petri dish incubator cleavage -->
                                    <ellipse cx="120" cy="70" rx="65" ry="35" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                                    <!-- 4-cell cleavage embryo -->
                                    <circle cx="110" cy="62" r="10" fill="#fbbf24"/>
                                    <circle cx="130" cy="62" r="10" fill="#fbbf24"/>
                                    <circle cx="110" cy="78" r="10" fill="#fbbf24"/>
                                    <circle cx="130" cy="78" r="10" fill="#fbbf24"/>
                                    <text x="65" y="125" fill="#fbbf24" font-size="9" font-family="JetBrains Mono">Incubator Cleavage Culture</text>
                                ` : `
                                    <!-- Catheter entering uterus -->
                                    <path d="M80,50 Q120,30 160,50 L150,90 L90,90 Z" fill="#881337" stroke="#e11d48"/>
                                    <line x1="120" y1="120" x2="120" y2="60" stroke="#38bdf8" stroke-width="3"/>
                                    <circle cx="120" cy="55" r="4" fill="#fde047"/>
                                    <text x="60" y="125" fill="#38bdf8" font-size="9" font-family="JetBrains Mono">Uterine Embryo Transfer (IUT)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Step Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono leading-relaxed space-y-1">
                            <div class="text-rose-400 font-bold">${{cur.title}}</div>
                            <p class="text-slate-300 text-[10px]">${{cur.desc}}</p>
                        </div>
                    </div>
                `;
            }}

            window.sim15Set = function(s) {{
                step = s;
                playTone(320 + s * 60, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 16: Acharya Sushruta & Prof. Panchanan Maheshwari (C-6.1)
        function renderSim16(vp) {{
            let mode = 'sushruta'; // 'sushruta' vs 'maheshwari'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim16Set('sushruta')" class="py-1.5 rounded-lg transition ${{mode === 'sushruta' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Acharya Sushruta (~6th c. BCE)
                            </button>
                            <button onclick="window.sim16Set('maheshwari')" class="py-1.5 rounded-lg transition ${{mode === 'maheshwari' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Prof. P. Maheshwari (1904–1966)
                            </button>
                        </div>

                        <!-- Historical Chronicle SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'sushruta' ? `
                                    <!-- Sushruta Samhita Palm Leaf Manuscript & Anatomical Dissection -->
                                    <rect x="30" y="25" width="180" height="95" rx="6" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                                    <rect x="40" y="35" width="160" height="75" fill="#fef3c7" rx="3"/>
                                    <text x="50" y="55" fill="#78350f" font-size="10" font-family="JetBrains Mono" font-weight="bold">Sushruta Samhita</text>
                                    <text x="50" y="72" fill="#92400e" font-size="8" font-family="JetBrains Mono">• Sharira Sthana (Anatomy)</text>
                                    <text x="50" y="86" fill="#92400e" font-size="8" font-family="JetBrains Mono">• Garbha-Sharira (Embryology)</text>
                                    <text x="50" y="100" fill="#92400e" font-size="8" font-family="JetBrains Mono">• Water Immersion Dissection</text>
                                ` : `
                                    <!-- Prof. Panchanan Maheshwari In Vitro Test-Tube Ovule Culture -->
                                    <rect x="30" y="25" width="180" height="95" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <rect x="40" y="35" width="160" height="75" fill="#ecfdf5" rx="3"/>
                                    <text x="50" y="55" fill="#065f46" font-size="10" font-family="JetBrains Mono" font-weight="bold">Prof. P. Maheshwari (FRS)</text>
                                    <text x="50" y="72" fill="#047857" font-size="8" font-family="JetBrains Mono">• Embryology of Angiosperms (1950)</text>
                                    <text x="50" y="86" fill="#047857" font-size="8" font-family="JetBrains Mono">• Test-Tube Ovule Fertilisation</text>
                                    <text x="50" y="100" fill="#047857" font-size="8" font-family="JetBrains Mono">• Founder of Indian Plant Tissue Culture</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-6.1 Contribution Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'sushruta' ? 
                                '<span class="text-amber-400 font-bold">Acharya Sushruta:</span> Father of Surgery in ancient India, pioneer of cadaveric immersion dissection and Garbha-Sharira human embryology.' : 
                                '<span class="text-emerald-400 font-bold">Prof. Panchanan Maheshwari:</span> Global pioneer of in vitro angiosperm ovule fertilisation, establishing modern plant tissue culture in India.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim16Set = function(m) {{
                mode = m;
                playTone(m === 'sushruta' ? 440 : 520, 0.1);
                draw();
            }};

            draw();
        }}
    </script>
</body>
</html>
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_code)

    print(f"Successfully generated {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH)} bytes).")

if __name__ == "__main__":
    generate_html()
