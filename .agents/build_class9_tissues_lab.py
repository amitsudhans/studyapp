# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 2 (Biology)
TISSUES
Syllabus Competencies: C-4.2, C-5.3, C-6.1, C-7.1, C-8.2
Generates public/animations/class9-tissues.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_tissues_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-tissues.html"

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
    <title>NCERT Class 9 Science • Chapter 2: Tissues Laboratory</title>
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
            0%, 100% {{ box-shadow: 0 0 15px rgba(16, 185, 129, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(16, 185, 129, 0.45); }}
        }}
        .pulse-border {{
            animation: pulseGlow 2.5s infinite;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-emerald-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="glass-panel sticky top-0 z-40 border-b border-slate-800/80 px-4 py-2.5 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-950/40 border border-emerald-400/30">
                <i data-lucide="layers" class="w-5 h-5 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold tracking-wider uppercase px-2 py-0.5 rounded bg-emerald-950/80 text-emerald-400 border border-emerald-800/60 font-mono">
                        NCERT Class 9 Science • Chapter 2
                    </span>
                    <span class="hidden sm:inline-block text-[11px] font-medium text-slate-400">• Biology Master Lab</span>
                </div>
                <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-1.5">
                    Tissues: Structure, Function & Biomechanics
                </h1>
            </div>
        </div>

        <!-- Slide Selector & Nav Controls -->
        <div class="flex items-center gap-2 sm:gap-3">
            <div class="relative">
                <button onclick="window.toggleSlideMenu()" id="slideMenuBtn" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700/70 hover:bg-slate-800 text-xs font-semibold text-slate-200 transition">
                    <i data-lucide="compass" class="w-3.5 h-3.5 text-emerald-400"></i>
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
                <button onclick="window.toggleSpeech()" id="speechBtn" title="Play Voiceover Narration" class="w-8 h-8 rounded-md bg-emerald-600 hover:bg-emerald-500 text-white flex items-center justify-center transition">
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
            <div class="glass-panel rounded-2xl p-4 border border-slate-800/80 shadow-xl relative overflow-hidden bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-emerald-950/20">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Talking Avatar (Prof. Sophia) -->
                    <div class="relative w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-b from-emerald-600 to-teal-800 p-0.5 shadow-md shrink-0">
                        <svg viewBox="0 0 100 100" class="w-full h-full rounded-[14px] bg-slate-900 overflow-hidden">
                            <!-- Background gradient -->
                            <rect width="100" height="100" fill="#091e1d"/>
                            <circle cx="50" cy="50" r="42" fill="#134e4a" opacity="0.3"/>
                            <!-- Torso / Lab Coat -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#334155"/>
                            <path d="M35,90 L50,100 L65,90 L60,82 L50,86 L40,82 Z" fill="#0d9488"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="46" rx="22" ry="26" fill="#fed7aa"/>
                            <!-- Hair -->
                            <path d="M26,42 Q28,18 50,18 Q72,18 74,42 Q68,26 50,26 Q32,26 26,42 Z" fill="#374151"/>
                            <path d="M26,42 Q24,60 28,68 Q32,56 32,46 Z" fill="#374151"/>
                            <path d="M74,42 Q76,60 72,68 Q68,56 68,46 Z" fill="#374151"/>
                            <!-- Glasses -->
                            <rect x="33" y="40" width="13" height="8" rx="2" fill="none" stroke="#065f46" stroke-width="2"/>
                            <rect x="54" y="40" width="13" height="8" rx="2" fill="none" stroke="#065f46" stroke-width="2"/>
                            <line x1="46" y1="44" x2="54" y2="44" stroke="#065f46" stroke-width="2"/>
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
                        <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-500 text-slate-950 font-mono shadow">
                            TEACHER
                        </div>
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between gap-2">
                            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">Prof. Sophia • Voice Guide</span>
                            <span id="speechStatusIndicator" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Ready</span>
                        </div>
                        <p id="narrationText" class="text-xs text-slate-300 mt-1 line-clamp-3 leading-relaxed italic">
                            Welcome students! Today we investigate Tissues—the cellular building blocks that bridge single cells into living organisms.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Content Presentation Slide (Slides 1 to 16) -->
            <div id="contentSlideContainer" class="space-y-4">
                <!-- Slide Header Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between">
                        <span id="slideCategoryText" class="text-[11px] font-bold text-teal-400 uppercase tracking-widest font-mono">Section Core Theory</span>
                        <span id="slideBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 font-mono">
                            Part 1 of 20
                        </span>
                    </div>
                    <div>
                        <h2 id="slideTitle" class="text-lg sm:text-xl font-extrabold text-white tracking-tight">Introduction to Tissues & Levels of Organisation</h2>
                        <p id="slideSubtitle" class="text-xs sm:text-sm font-medium text-emerald-400/90 mt-0.5">Division of Labour: From Specialized Cells to Complex Multicellular Organisms</p>
                    </div>
                    <ul id="slideKeyPoints" class="text-xs sm:text-sm text-slate-300 space-y-2 pt-1 border-t border-slate-800/80 leading-relaxed">
                        <!-- Injected via JavaScript -->
                    </ul>
                </div>

                <!-- Checkpoints Container -->
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
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
                        <div class="w-7 h-7 rounded-lg bg-indigo-950 border border-indigo-700/60 flex items-center justify-center text-indigo-400">
                            <i data-lucide="award" class="w-4 h-4"></i>
                        </div>
                        <div>
                            <h3 id="quizTitleDisplay" class="text-sm font-extrabold text-white">Mastery Assessment</h3>
                            <p class="text-[11px] text-slate-400">10 Comprehensive Questions with Step-by-Step Solutions</p>
                        </div>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-mono font-bold text-emerald-400">Score: <span id="quizScoreVal">0</span> / 10</span>
                    </div>
                </div>

                <div id="quizQuestionsList" class="space-y-4">
                    <!-- Injected via JavaScript -->
                </div>
            </div>

            <!-- Slide 20 Last Slide Notice -->
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-emerald-500/40 bg-gradient-to-r from-emerald-950/40 via-slate-900 to-teal-950/40 shadow-xl shadow-emerald-950/30">
                <div class="w-12 h-12 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 flex items-center justify-center mx-auto mb-2">
                    <i data-lucide="check-check" class="w-6 h-6"></i>
                </div>
                <h4 class="text-lg font-bold text-white">Curriculum Chapter Mastered!</h4>
                <p class="text-base sm:text-lg text-emerald-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">
                    You have comprehensively covered Plant & Animal Tissues, Meristems, Onion Root Growth Experiment, Musculoskeletal Anatomy, R.I.C.E. Rehabilitation, and Indian Science Milestones.
                </p>
            </div>

        </div>

        <!-- Right Column: Interactive Bespoke SVG Simulators (5 cols) -->
        <div class="lg:col-span-5 flex flex-col gap-4 sticky top-20">
            <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 shadow-2xl flex flex-col gap-3">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4 text-emerald-400"></i>
                        <h3 id="simulatorTitle" class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">
                            Interactive Visual Laboratory
                        </h3>
                    </div>
                    <span id="simulatorBadge" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-teal-400 border border-slate-700">
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
                    <span id="slideProgressRatio" class="text-xs font-mono font-bold text-emerald-400">1 / 20</span>
                </div>
                <button onclick="window.navSlide(1)" id="nextBtn" class="flex-1 px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-lg shadow-emerald-950/50">
                    <span>Next</span>
                    <i data-lucide="chevron-right" class="w-4 h-4"></i>
                </button>
            </div>
            <!-- Progress Bar -->
            <div class="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden border border-slate-800">
                <div id="slideProgressBar" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-300" style="width: 5%;"></div>
            </div>
        </div>
    </main>

    <!-- Step-by-Step Solution Pop-Up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="glass-panel rounded-2xl border border-slate-700 max-w-lg w-full p-5 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center justify-center">
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
                    <div class="text-[11px] font-mono text-emerald-400 uppercase font-bold mb-1">Question Prompt</div>
                    <div id="modalQuestionText" class="text-slate-200 font-medium"></div>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/30 border border-emerald-800/40">
                    <div class="text-[11px] font-mono text-emerald-400 uppercase font-bold mb-1">Correct Answer & Principle</div>
                    <div id="modalAnswerText" class="text-emerald-300 font-bold"></div>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800">
                    <div class="text-[11px] font-mono text-slate-400 uppercase font-bold mb-1">Biological Derivation & Explanation</div>
                    <div id="modalExplanationText" class="text-slate-300"></div>
                </div>
            </div>
            <div class="pt-2 text-right">
                <button onclick="window.closeSolutionModal()" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg">
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
                    <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-800 text-emerald-400 shrink-0">${{badge}}</span>
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
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
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
                    <span class="w-5 h-5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold">Q${{idx+1}}</span>
                    <span>${{cp.question}}</span>
                `;
                box.appendChild(qTitle);

                const optsGrid = document.createElement('div');
                optsGrid.className = "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1";

                const expPanel = document.createElement('div');
                expPanel.className = "hidden p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/60 text-xs text-emerald-300 space-y-1";

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
                            btn.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/50', 'font-bold');
                            expPanel.innerHTML = `
                                <div class="font-bold flex items-center gap-1.5 text-emerald-400">
                                    <i data-lucide="check-circle-2" class="w-4 h-4"></i> Correct Concept!
                                </div>
                                <div class="text-[11px] text-slate-300">${{cp.explanation}}</div>
                            `;
                            playTone(523.25, 0.15, 'sine');
                        }} else {{
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            expPanel.innerHTML = `
                                <div class="font-bold flex items-center gap-1.5 text-rose-400">
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
                        <span class="w-6 h-6 rounded-lg bg-indigo-950 text-indigo-400 border border-indigo-800/50 flex items-center justify-center text-xs font-mono font-bold shrink-0">${{qIdx+1}}</span>
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
                            btn.classList.add('bg-emerald-950/80', 'text-emerald-300', 'border-emerald-500/50', 'font-bold');
                            score++;
                            document.getElementById('quizScoreVal').textContent = score;
                            resultBar.innerHTML = `
                                <span class="text-emerald-400 font-bold flex items-center gap-1">
                                    <i data-lucide="check" class="w-4 h-4"></i> Correct Answer
                                </span>
                                <button onclick="window.openSolutionModal(${{currentSlideIndex - 16}}, ${{qIdx}})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 text-[11px] font-semibold transition">
                                    View Solution
                                </button>
                            `;
                            playTone(587.33, 0.12, 'triangle');
                        }} else {{
                            btn.classList.add('bg-rose-950/80', 'text-rose-300', 'border-rose-500/50', 'font-bold');
                            resultBar.innerHTML = `
                                <span class="text-rose-400 font-bold flex items-center gap-1">
                                    <i data-lucide="x" class="w-4 h-4"></i> Incorrect (Correct: ${{String.fromCharCode(65 + qObj.correct)}})
                                </span>
                                <button onclick="window.openSolutionModal(${{currentSlideIndex - 16}}, ${{qIdx}})" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 text-[11px] font-semibold transition">
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
                document.getElementById('speechStatusIndicator').className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800";
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
                    titleEl.textContent = "Hierarchical Levels of Organisation";
                    renderSim1(vp); break;
                case 1:
                    titleEl.textContent = "Plant vs Animal Architectural Contrast";
                    renderSim2(vp); break;
                case 2:
                    titleEl.textContent = "Meristematic Zones (Apical, Intercalary, Lateral)";
                    renderSim3(vp); break;
                case 3:
                    titleEl.textContent = "C-8.2 Onion Root Tip Excision Lab";
                    renderSim4(vp); break;
                case 4:
                    titleEl.textContent = "Differentiation & Permanent Tissue Genesis";
                    renderSim5(vp); break;
                case 5:
                    titleEl.textContent = "Parenchyma, Chlorenchyma & Aerenchyma Explorer";
                    renderSim6(vp); break;
                case 6:
                    titleEl.textContent = "Collenchyma vs Sclerenchyma Stress Bench";
                    renderSim7(vp); break;
                case 7:
                    titleEl.textContent = "Epidermis, Stomatal Gates & Suberised Cork";
                    renderSim8(vp); break;
                case 8:
                    titleEl.textContent = "Xylem Vascular Plumbing & Sap Ascent";
                    renderSim9(vp); break;
                case 9:
                    titleEl.textContent = "Phloem Translocation & Sieve Tube Anatomy";
                    renderSim10(vp); break;
                case 10:
                    titleEl.textContent = "Animal Epithelial Histology Microscope";
                    renderSim11(vp); break;
                case 11:
                    titleEl.textContent = "Connective Tissue & Joint Synovial Matrix";
                    renderSim12(vp); break;
                case 12:
                    titleEl.textContent = "3-Way Muscular Triad: Striated, Smooth & Cardiac";
                    renderSim13(vp); break;
                case 13:
                    titleEl.textContent = "Neuron Electrochemical Impulse Simulator";
                    renderSim14(vp); break;
                case 14:
                    titleEl.textContent = "Musculoskeletal Biomechanics, R.I.C.E. & Yoga";
                    renderSim15(vp); break;
                case 15:
                    titleEl.textContent = "1964 Delhi Univ Anther Culture & Totipotency";
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
                "Plant Tissues: Meristems, Ground Tissue, Xylem & Phloem",
                "Animal Tissues: Epithelial, Connective, Muscular & Nervous",
                "Musculoskeletal System, Joint Varieties, R.I.C.E. & Yogic Posture",
                "Comprehensive Competency Synthesis & Indian Scientific Discovery"
            ];

            vp.innerHTML = `
                <div class="w-full flex flex-col items-center justify-center p-4 text-center space-y-4">
                    <div class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-indigo-600 via-emerald-600 to-teal-400 p-1 shadow-xl flex items-center justify-center">
                        <div class="w-full h-full bg-slate-950 rounded-xl flex items-center justify-center">
                            <i data-lucide="award" class="w-10 h-10 text-emerald-400"></i>
                        </div>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono text-emerald-400 font-bold uppercase tracking-wider">Evaluation Domain</div>
                        <h4 class="text-sm font-bold text-white mt-1">${{topics[quizIdx]}}</h4>
                        <p class="text-xs text-slate-400 max-w-xs mx-auto mt-1">
                            Answer each question on the left to reveal instant feedback and comprehensive step-by-step scientific solutions.
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 w-full max-w-xs text-left text-xs space-y-1.5 font-mono">
                        <div class="flex justify-between text-slate-300">
                            <span>Stage:</span>
                            <span class="text-emerald-400 font-bold">Quiz ${{quizIdx + 1}} of 4</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Questions:</span>
                            <span class="text-white">10 MCQs</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Passing Standard:</span>
                            <span class="text-teal-300">80% Mastery</span>
                        </div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        // SIMULATOR 1: Levels of Organisation Interactive Pyramid
        function renderSim1(vp) {{
            let activeLevel = 2; // 1: Cell, 2: Tissue, 3: Organ, 4: System, 5: Organism
            const levels = [
                {{ name: "Specialized Cell", sub: "Muscle cell / Meristem cell", desc: "Single functional unit with specialized shape and protein machinery.", icon: "box", color: "#10b981" }},
                {{ name: "Tissue Ensemble", sub: "Striated muscle / Xylem bundle", desc: "Cooperative ensemble of similar cells performing a synchronized task.", icon: "layers", color: "#06b6d4" }},
                {{ name: "Functional Organ", sub: "Biceps muscle / Leaf / Heart", desc: "Distinct anatomic structure built of multiple coordinated tissues.", icon: "activity", color: "#6366f1" }},
                {{ name: "Organ System", sub: "Musculoskeletal system / Shoot vascular network", desc: "Integrated physiological network executing systemic survival workflows.", icon: "network", color: "#ec4899" }},
                {{ name: "Complex Organism", sub: "Human athlete / Giant Banyan tree", desc: "Unified multicellular lifeform exhibiting total division of labour.", icon: "user", color: "#f59e0b" }}
            ];

            function draw() {{
                const cur = levels[activeLevel - 1];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs font-mono text-slate-400">
                            <span>Interactive Hierarchy Slider:</span>
                            <span class="text-emerald-400 font-bold">Level ${{activeLevel}} of 5</span>
                        </div>

                        <!-- 5 Level Stepper Buttons -->
                        <div class="grid grid-cols-5 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800">
                            ${{levels.map((lvl, idx) => `
                                <button onclick="window.sim1SetLevel(${{idx + 1}})" class="py-1.5 rounded-lg text-[10px] font-bold font-mono transition ${{activeLevel === idx + 1 ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800/80 text-slate-400 hover:text-white'}}">
                                    L${{idx + 1}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Visual Hierarchy SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center">
                            <svg width="280" height="150" viewBox="0 0 280 150" class="w-full max-w-[280px]">
                                <!-- Pyramid Steps -->
                                <polygon points="140,10 165,36 115,36" fill="${{activeLevel >= 5 ? '#f59e0b' : '#334155'}}" opacity="${{activeLevel === 5 ? '1' : '0.4'}}"/>
                                <polygon points="115,38 165,38 190,64 90,64" fill="${{activeLevel >= 4 ? '#ec4899' : '#334155'}}" opacity="${{activeLevel === 4 ? '1' : '0.4'}}"/>
                                <polygon points="90,66 190,66 215,92 65,92" fill="${{activeLevel >= 3 ? '#6366f1' : '#334155'}}" opacity="${{activeLevel === 3 ? '1' : '0.4'}}"/>
                                <polygon points="65,94 215,94 240,120 40,120" fill="${{activeLevel >= 2 ? '#06b6d4' : '#334155'}}" opacity="${{activeLevel === 2 ? '1' : '0.4'}}"/>
                                <polygon points="40,122 240,122 265,148 15,148" fill="${{activeLevel >= 1 ? '#10b981' : '#334155'}}" opacity="${{activeLevel === 1 ? '1' : '0.4'}}"/>
                                <!-- Active Level Marker -->
                                <circle cx="140" cy="${{activeLevel === 5 ? 23 : activeLevel === 4 ? 51 : activeLevel === 3 ? 79 : activeLevel === 2 ? 107 : 135}}" r="5" fill="#ffffff" class="animate-ping"/>
                            </svg>
                        </div>

                        <!-- Information Detail Card -->
                        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1">
                            <div class="flex items-center justify-between">
                                <span class="font-bold text-white text-sm" style="color: ${{cur.color}};">${{cur.name}}</span>
                                <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-300">${{cur.sub}}</span>
                            </div>
                            <p class="text-slate-300 text-[11px] leading-relaxed">${{cur.desc}}</p>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }}

            window.sim1SetLevel = function(lvl) {{
                activeLevel = lvl;
                playTone(200 + lvl * 70, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 2: Plant vs Animal Architectural Contrast
        function renderSim2(vp) {{
            let mode = 'plant'; // 'plant' or 'animal'
            let stress = 50;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800">
                            <button onclick="window.sim2SetMode('plant')" class="py-2 rounded-lg text-xs font-bold transition ${{mode === 'plant' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800/80 text-slate-400'}}">
                                Stationary Plant Habit
                            </button>
                            <button onclick="window.sim2SetMode('animal')" class="py-2 rounded-lg text-xs font-bold transition ${{mode === 'animal' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800/80 text-slate-400'}}">
                                Motile Animal Habit
                            </button>
                        </div>

                        <!-- Graphical Simulation View -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-around h-44 relative overflow-hidden">
                            ${{mode === 'plant' ? `
                                <svg width="220" height="150" viewBox="0 0 220 150">
                                    <!-- Soil Base -->
                                    <line x1="10" y1="130" x2="210" y2="130" stroke="#78350f" stroke-width="4"/>
                                    <!-- Trunk swaying with stress -->
                                    <path d="M110,130 Q${{110 - stress*0.4}},75 ${{110 - stress*0.7}},20" fill="none" stroke="#92400e" stroke-width="14" stroke-linecap="round"/>
                                    <!-- Canopy foliage -->
                                    <circle cx="${{110 - stress*0.7}}" cy="25" r="32" fill="#047857" opacity="0.85"/>
                                    <circle cx="${{90 - stress*0.7}}" cy="20" r="22" fill="#10b981" opacity="0.75"/>
                                    <!-- Root anchors -->
                                    <path d="M110,130 Q90,145 60,148 M110,130 Q130,145 160,146" fill="none" stroke="#78350f" stroke-width="4"/>
                                </svg>
                                <div class="absolute bottom-2 right-2 text-[10px] font-mono text-emerald-400 bg-slate-900/90 px-2 py-0.5 rounded border border-emerald-800">
                                    Structural Rigidity (Dead Sclerenchyma)
                                </div>
                            ` : `
                                <svg width="220" height="150" viewBox="0 0 220 150">
                                    <!-- Running Cheetah / Athlete Stick figure with dynamic motion -->
                                    <circle cx="${{40 + stress*1.2}}" cy="35" r="14" fill="#38bdf8"/>
                                    <!-- Spine -->
                                    <line x1="${{40 + stress*1.2}}" y1="49" x2="${{30 + stress*1.2}}" y2="85" stroke="#38bdf8" stroke-width="4"/>
                                    <!-- Legs -->
                                    <line x1="${{30 + stress*1.2}}" y1="85" x2="${{10 + stress*1.2}}" y2="125" stroke="#38bdf8" stroke-width="3.5"/>
                                    <line x1="${{30 + stress*1.2}}" y1="85" x2="${{55 + stress*1.2}}" y2="115" stroke="#38bdf8" stroke-width="3.5"/>
                                    <!-- Arms -->
                                    <line x1="${{35 + stress*1.2}}" y1="58" x2="${{15 + stress*1.2}}" y2="78" stroke="#38bdf8" stroke-width="3.5"/>
                                    <line x1="${{35 + stress*1.2}}" y1="58" x2="${{60 + stress*1.2}}" y2="72" stroke="#38bdf8" stroke-width="3.5"/>
                                </svg>
                                <div class="absolute bottom-2 right-2 text-[10px] font-mono text-cyan-400 bg-slate-900/90 px-2 py-0.5 rounded border border-cyan-800">
                                    High Motility & Active Living Tissues
                                </div>
                            `}}
                        </div>

                        <!-- Interactive Stress/Speed Slider -->
                        <div class="space-y-1">
                            <div class="flex justify-between text-xs text-slate-300 font-mono">
                                <span>${{mode === 'plant' ? 'Wind / Environmental Stress:' : 'Locomotion Speed / Exertion:'}}</span>
                                <span class="text-emerald-400 font-bold">${{stress}}%</span>
                            </div>
                            <input type="range" min="0" max="100" value="${{stress}}" oninput="window.sim2SetStress(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        </div>

                        <!-- Comparison Matrix Table -->
                        <div class="grid grid-cols-2 gap-2 text-[11px] font-mono">
                            <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                                <span class="text-slate-400">Growth Zone:</span>
                                <div class="text-white font-bold">${{mode === 'plant' ? 'Localized (Meristems)' : 'Uniform Across Organs'}}</div>
                            </div>
                            <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                                <span class="text-slate-400">Energy Rate:</span>
                                <div class="text-emerald-400 font-bold">${{mode === 'plant' ? 'Low (~15-25 W)' : 'High (~100-300 W)'}}</div>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim2SetMode = function(m) {{
                mode = m;
                playTone(320, 0.1);
                draw();
            }};

            window.sim2SetStress = function(val) {{
                stress = parseInt(val);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 3: Meristematic Zones (Apical, Intercalary, Lateral)
        function renderSim3(vp) {{
            let zone = 'apical'; // 'apical', 'intercalary', 'lateral'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Zone Selector -->
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                            <button onclick="window.sim3SetZone('apical')" class="py-1.5 rounded-lg transition ${{zone === 'apical' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Apical (Tip)
                            </button>
                            <button onclick="window.sim3SetZone('intercalary')" class="py-1.5 rounded-lg transition ${{zone === 'intercalary' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Intercalary (Nodes)
                            </button>
                            <button onclick="window.sim3SetZone('lateral')" class="py-1.5 rounded-lg transition ${{zone === 'lateral' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Lateral (Cambium)
                            </button>
                        </div>

                        <!-- Shoot Diagram SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Main Stem -->
                                <rect x="100" y="30" width="40" height="130" fill="#065f46" stroke="#047857" stroke-width="2" rx="4"/>
                                <!-- Nodes / Internodes -->
                                <line x1="100" y1="80" x2="140" y2="80" stroke="#022c22" stroke-width="3"/>
                                <line x1="100" y1="120" x2="140" y2="120" stroke="#022c22" stroke-width="3"/>
                                <!-- Leaves at node -->
                                <path d="M100,80 Q70,70 50,75 Q75,90 100,80" fill="#10b981"/>
                                <path d="M140,80 Q170,70 190,75 Q165,90 140,80" fill="#10b981"/>

                                <!-- Highlights based on active zone -->
                                ${{zone === 'apical' ? `
                                    <!-- Shoot apex highlight -->
                                    <path d="M100,30 Q120,5 140,30 Z" fill="#34d399" stroke="#10b981" stroke-width="2" class="animate-pulse"/>
                                    <!-- Upward arrow -->
                                    <line x1="120" y1="20" x2="120" y2="0" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow)"/>
                                    <text x="135" y="15" fill="#fbbf24" font-size="10" font-family="JetBrains Mono" font-weight="bold">+ Height (Linear)</text>
                                ` : zone === 'intercalary' ? `
                                    <!-- Node base highlights -->
                                    <rect x="96" y="75" width="48" height="10" fill="#f59e0b" opacity="0.85" rx="3" class="animate-pulse"/>
                                    <rect x="96" y="115" width="48" height="10" fill="#f59e0b" opacity="0.85" rx="3" class="animate-pulse"/>
                                    <text x="150" y="83" fill="#f59e0b" font-size="10" font-family="JetBrains Mono" font-weight="bold">+ Internode Regrowth</text>
                                ` : `
                                    <!-- Lateral Cambium cylinders on sides -->
                                    <line x1="104" y1="35" x2="104" y2="155" stroke="#818cf8" stroke-width="4" stroke-dasharray="3,3" class="animate-pulse"/>
                                    <line x1="136" y1="35" x2="136" y2="155" stroke="#818cf8" stroke-width="4" stroke-dasharray="3,3" class="animate-pulse"/>
                                    <!-- Radial expansion arrows -->
                                    <line x1="95" y1="100" x2="75" y2="100" stroke="#818cf8" stroke-width="2.5"/>
                                    <line x1="145" y1="100" x2="165" y2="100" stroke="#818cf8" stroke-width="2.5"/>
                                    <text x="145" y="135" fill="#818cf8" font-size="10" font-family="JetBrains Mono" font-weight="bold">+ Girth / Thickness</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Cytology Characteristics Box -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300 space-y-1">
                            <div class="text-emerald-400 font-bold uppercase">Cytological Blueprint:</div>
                            <div class="flex items-center justify-between">
                                <span>Wall: Thin primary cellulose</span>
                                <span>Cytoplasm: Dense & granular</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span>Nucleus: Prominent & active</span>
                                <span class="text-rose-400 font-bold">Vacuoles: NONE (No storage)</span>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim3SetZone = function(z) {{
                zone = z;
                playTone(z === 'apical' ? 440 : z === 'intercalary' ? 493.88 : 554.37, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 4: C-8.2 Onion Root Tip Excision Lab
        function renderSim4(vp) {{
            let currentDay = 3; // 1 to 5
            let jar2Clipped = false;

            function draw() {{
                // Growth data
                const jar1Lengths = [1.2, 2.0, 2.9, 3.8, 4.7];
                const jar2Lengths = jar2Clipped ? [1.2, 2.0, 2.9, 2.9, 2.9] : [1.2, 2.0, 2.9, 3.7, 4.6];

                const l1 = jar1Lengths[currentDay - 1];
                const l2 = jar2Lengths[currentDay - 1];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Top Controls: Day Slider + Clip Action -->
                        <div class="flex items-center justify-between bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                            <div class="flex items-center gap-2">
                                <span class="text-xs font-mono font-bold text-slate-300">Observation Day:</span>
                                <span class="text-xs font-mono font-bold text-emerald-400">Day ${{currentDay}}</span>
                            </div>
                            <button onclick="window.sim4ClipJar2()" class="px-2.5 py-1 rounded-lg text-xs font-bold transition ${{jar2Clipped ? 'bg-rose-950 text-rose-300 border border-rose-800' : 'bg-amber-600 hover:bg-amber-500 text-white shadow'}}">
                                ${{jar2Clipped ? '✓ Tip Excised (Jar 2)' : '✂ Clip 1cm Tip (Jar 2)'}}
                            </button>
                        </div>

                        <!-- Days Stepper -->
                        <div class="grid grid-cols-5 gap-1">
                            ${{[1,2,3,4,5].map(d => `
                                <button onclick="window.sim4SetDay(${{d}})" class="py-1 rounded text-xs font-mono font-bold transition ${{currentDay === d ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800/80 text-slate-400'}}">
                                    D${{d}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Two Jars SVG Comparison -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around">
                            <!-- Jar 1 (Control) -->
                            <div class="flex flex-col items-center">
                                <div class="text-[11px] font-mono text-emerald-400 font-bold mb-1">Jar 1 (Intact Control)</div>
                                <svg width="90" height="130" viewBox="0 0 90 130">
                                    <!-- Glass Jar -->
                                    <rect x="15" y="30" width="60" height="95" fill="#0f172a" stroke="#475569" stroke-width="2" rx="4"/>
                                    <!-- Water line -->
                                    <rect x="16" y="45" width="58" height="79" fill="#0284c7" opacity="0.25"/>
                                    <!-- Onion Bulb on Mouth -->
                                    <ellipse cx="45" cy="28" rx="20" ry="14" fill="#a855f7"/>
                                    <!-- Growing Roots -->
                                    <path d="M40,38 Q38,${{38 + l1*15}} 40,${{38 + l1*18}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <path d="M45,38 Q46,${{38 + l1*16}} 45,${{38 + l1*19}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <path d="M50,38 Q52,${{38 + l1*15}} 50,${{38 + l1*18}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <!-- Root tip green dot -->
                                    <circle cx="45" cy="${{38 + l1*19}}" r="2.5" fill="#10b981"/>
                                </svg>
                                <span class="text-xs font-mono text-emerald-400 font-bold mt-1">${{l1.toFixed(1)}} cm</span>
                            </div>

                            <!-- Jar 2 (Intervention) -->
                            <div class="flex flex-col items-center">
                                <div class="text-[11px] font-mono text-amber-400 font-bold mb-1">Jar 2 (${{jar2Clipped ? 'Clipped' : 'Intact'}})</div>
                                <svg width="90" height="130" viewBox="0 0 90 130">
                                    <!-- Glass Jar -->
                                    <rect x="15" y="30" width="60" height="95" fill="#0f172a" stroke="#475569" stroke-width="2" rx="4"/>
                                    <!-- Water line -->
                                    <rect x="16" y="45" width="58" height="79" fill="#0284c7" opacity="0.25"/>
                                    <!-- Onion Bulb on Mouth -->
                                    <ellipse cx="45" cy="28" rx="20" ry="14" fill="#c084fc"/>
                                    <!-- Roots -->
                                    <path d="M40,38 Q38,${{38 + l2*15}} 40,${{38 + l2*18}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <path d="M45,38 Q46,${{38 + l2*16}} 45,${{38 + l2*19}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <path d="M50,38 Q52,${{38 + l2*15}} 50,${{38 + l2*18}}" stroke="#f8fafc" stroke-width="2.5" fill="none"/>
                                    <!-- Root tip indicator -->
                                    ${{jar2Clipped ? `
                                        <line x1="36" y1="${{38 + l2*19}}" x2="54" y2="${{38 + l2*19}}" stroke="#ef4444" stroke-width="2"/>
                                    ` : `
                                        <circle cx="45" cy="${{38 + l2*19}}" r="2.5" fill="#10b981"/>
                                    `}}
                                </svg>
                                <span class="text-xs font-mono font-bold mt-1 ${{jar2Clipped && currentDay >= 4 ? 'text-rose-400' : 'text-amber-400'}}">${{l2.toFixed(1)}} cm</span>
                            </div>
                        </div>

                        <!-- Scientific Conclusion Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] leading-relaxed">
                            <span class="text-emerald-400 font-bold font-mono">C-8.2 Empirical Inference: </span>
                            <span class="text-slate-300">
                                ${{jar2Clipped && currentDay >= 4 ? 
                                    'When the terminal 1 cm tip of Jar 2 is excised, linear root elongation halts completely. This proves the dividing cell population driving primary elongation resides strictly within the terminal apical meristem.' : 
                                    'Both onion root sets elongate at approx 0.8–0.9 cm/day when apical meristems are intact.'}}
                            </span>
                        </div>
                    </div>
                `;
            }}

            window.sim4SetDay = function(d) {{
                currentDay = d;
                playTone(300 + d * 50, 0.08);
                draw();
            }};

            window.sim4ClipJar2 = function() {{
                jar2Clipped = !jar2Clipped;
                playTone(jar2Clipped ? 600 : 250, 0.15);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 5: Differentiation & Permanent Tissue Genesis
        function renderSim5(vp) {{
            let selectedType = 'parenchyma'; // 'parenchyma', 'collenchyma', 'sclerenchyma', 'xylem'
            const types = {{
                parenchyma: {{ title: "Storage Parenchyma", status: "Living", wall: "Thin cellulose", function: "Food storage & metabolic packing" }},
                collenchyma: {{ title: "Flexible Collenchyma", status: "Living", wall: "Pectin-cellulose corner thickenings", function: "Tensile flexibility in petioles and tendrils" }},
                sclerenchyma: {{ title: "Armoured Sclerenchyma", status: "Dead at maturity", wall: "Heavily lignified secondary walls", function: "Compressive hardness in coconut husk & shells" }},
                xylem: {{ title: "Conducting Xylem Vessel", status: "Dead tubular pipeline", wall: "Dissolved end plates & lignified walls", function: "Unidirectional upward water & mineral ascent" }}
            }};

            function draw() {{
                const info = types[selectedType];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                            <button onclick="window.sim5SetType('parenchyma')" class="py-1.5 rounded-lg transition ${{selectedType === 'parenchyma' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Parenchyma
                            </button>
                            <button onclick="window.sim5SetType('collenchyma')" class="py-1.5 rounded-lg transition ${{selectedType === 'collenchyma' ? 'bg-teal-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Collenchyma
                            </button>
                            <button onclick="window.sim5SetType('sclerenchyma')" class="py-1.5 rounded-lg transition ${{selectedType === 'sclerenchyma' ? 'bg-amber-700 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Sclerenchyma
                            </button>
                            <button onclick="window.sim5SetType('xylem')" class="py-1.5 rounded-lg transition ${{selectedType === 'xylem' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Xylem Vessel
                            </button>
                        </div>

                        <!-- Differentiation Flow SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around h-44">
                            <!-- Undifferentiated Meristem -->
                            <div class="flex flex-col items-center">
                                <span class="text-[10px] font-mono text-slate-400 mb-1">Meristematic Cell</span>
                                <svg width="55" height="55" viewBox="0 0 55 55">
                                    <rect x="5" y="5" width="45" height="45" rx="6" fill="#047857" stroke="#10b981" stroke-width="1.5"/>
                                    <!-- Dense nucleus -->
                                    <circle cx="27.5" cy="27.5" r="9" fill="#022c22" stroke="#34d399" stroke-width="1.5"/>
                                </svg>
                                <span class="text-[9px] font-mono text-emerald-400 mt-1">Actively Dividing</span>
                            </div>

                            <!-- Differentiation Arrow -->
                            <div class="flex flex-col items-center">
                                <svg width="40" height="24" viewBox="0 0 40 24">
                                    <line x1="0" y1="12" x2="32" y2="12" stroke="#94a3b8" stroke-width="2.5"/>
                                    <polygon points="32,6 40,12 32,18" fill="#94a3b8"/>
                                </svg>
                                <span class="text-[9px] font-mono text-slate-400">Differentiation</span>
                            </div>

                            <!-- Resulting Specialized Cell -->
                            <div class="flex flex-col items-center">
                                <span class="text-[10px] font-mono text-white font-bold mb-1">${{info.title}}</span>
                                <svg width="65" height="65" viewBox="0 0 65 65">
                                    ${{selectedType === 'parenchyma' ? `
                                        <circle cx="32.5" cy="32.5" r="28" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                                        <ellipse cx="32.5" cy="32.5" rx="14" ry="12" fill="#047857" opacity="0.6"/>
                                        <circle cx="42" cy="25" r="4" fill="#022c22"/>
                                    ` : selectedType === 'collenchyma' ? `
                                        <rect x="8" y="8" width="49" height="49" rx="8" fill="#0d9488" stroke="#14b8a6" stroke-width="2"/>
                                        <!-- Corner thickenings -->
                                        <circle cx="8" cy="8" r="8" fill="#2dd4bf"/>
                                        <circle cx="57" cy="8" r="8" fill="#2dd4bf"/>
                                        <circle cx="8" cy="57" r="8" fill="#2dd4bf"/>
                                        <circle cx="57" cy="57" r="8" fill="#2dd4bf"/>
                                    ` : selectedType === 'sclerenchyma' ? `
                                        <polygon points="32.5,5 58,20 58,45 32.5,60 7,45 7,20" fill="#78350f" stroke="#b45309" stroke-width="5"/>
                                        <polygon points="32.5,20 44,27 44,38 32.5,45 21,38 21,27" fill="#0f172a"/>
                                    ` : `
                                        <rect x="12" y="5" width="41" height="55" rx="3" fill="#312e81" stroke="#6366f1" stroke-width="4"/>
                                        <line x1="12" y1="5" x2="53" y2="5" stroke="#a5b4fc" stroke-width="3" stroke-dasharray="2,2"/>
                                        <line x1="12" y1="60" x2="53" y2="60" stroke="#a5b4fc" stroke-width="3" stroke-dasharray="2,2"/>
                                    `}}
                                </svg>
                                <span class="text-[9px] font-mono font-bold mt-1 ${{info.status.includes('Dead') ? 'text-rose-400' : 'text-emerald-400'}}">${{info.status}}</span>
                            </div>
                        </div>

                        <!-- Info Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono space-y-1">
                            <div class="flex justify-between text-slate-300">
                                <span>Cell Wall:</span>
                                <span class="text-white font-bold">${{info.wall}}</span>
                            </div>
                            <div class="flex justify-between text-slate-300">
                                <span>Function:</span>
                                <span class="text-emerald-400 font-bold">${{info.function}}</span>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim5SetType = function(t) {{
                selectedType = t;
                playTone(400, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 6: Parenchyma, Chlorenchyma & Aerenchyma Explorer
        function renderSim6(vp) {{
            let mode = 'chlorenchyma'; // 'storage', 'chlorenchyma', 'aerenchyma'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                            <button onclick="window.sim6SetMode('storage')" class="py-1.5 rounded-lg transition ${{mode === 'storage' ? 'bg-purple-700 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Storage Ground
                            </button>
                            <button onclick="window.sim6SetMode('chlorenchyma')" class="py-1.5 rounded-lg transition ${{mode === 'chlorenchyma' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Chlorenchyma
                            </button>
                            <button onclick="window.sim6SetMode('aerenchyma')" class="py-1.5 rounded-lg transition ${{mode === 'aerenchyma' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Aerenchyma
                            </button>
                        </div>

                        <!-- Microscopic Canvas View -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'storage' ? `
                                    <!-- Loose parenchyma cells with starch granules -->
                                    <ellipse cx="60" cy="50" rx="35" ry="30" fill="#4c1d95" opacity="0.6" stroke="#8b5cf6" stroke-width="1.8"/>
                                    <ellipse cx="120" cy="55" rx="32" ry="28" fill="#4c1d95" opacity="0.6" stroke="#8b5cf6" stroke-width="1.8"/>
                                    <ellipse cx="180" cy="50" rx="35" ry="30" fill="#4c1d95" opacity="0.6" stroke="#8b5cf6" stroke-width="1.8"/>
                                    <ellipse cx="90" cy="105" rx="36" ry="30" fill="#4c1d95" opacity="0.6" stroke="#8b5cf6" stroke-width="1.8"/>
                                    <ellipse cx="155" cy="105" rx="34" ry="29" fill="#4c1d95" opacity="0.6" stroke="#8b5cf6" stroke-width="1.8"/>
                                    <!-- Starch amylum grains -->
                                    <circle cx="60" cy="48" r="4" fill="#c084fc"/>
                                    <circle cx="122" cy="52" r="5" fill="#c084fc"/>
                                    <circle cx="92" cy="102" r="4.5" fill="#c084fc"/>
                                    <circle cx="152" cy="102" r="5" fill="#c084fc"/>
                                ` : mode === 'chlorenchyma' ? `
                                    <!-- Leaf mesophyll cells with chloroplasts -->
                                    <rect x="30" y="25" width="40" height="100" rx="10" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <rect x="80" y="25" width="40" height="100" rx="10" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <rect x="130" y="25" width="40" height="100" rx="10" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <rect x="180" y="25" width="40" height="100" rx="10" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <!-- Chloroplast disks -->
                                    ${{[0,1,2,3,4,5].map(i => `<circle cx="${{50}}" cy="${{35 + i*16}}" r="3.5" fill="#34d399"/>`).join('')}}
                                    ${{[0,1,2,3,4,5].map(i => `<circle cx="${{100}}" cy="${{35 + i*16}}" r="3.5" fill="#34d399"/>`).join('')}}
                                    ${{[0,1,2,3,4,5].map(i => `<circle cx="${{150}}" cy="${{35 + i*16}}" r="3.5" fill="#34d399"/>`).join('')}}
                                    ${{[0,1,2,3,4,5].map(i => `<circle cx="${{200}}" cy="${{35 + i*16}}" r="3.5" fill="#34d399"/>`).join('')}}
                                ` : `
                                    <!-- Aquatic aerenchyma with massive air lacunae -->
                                    <circle cx="70" cy="55" r="32" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
                                    <circle cx="170" cy="55" r="32" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
                                    <circle cx="120" cy="110" r="30" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
                                    <!-- Trapped air bubble text -->
                                    <text x="50" y="58" fill="#7dd3fc" font-size="10" font-family="JetBrains Mono" font-weight="bold">Air Lacuna</text>
                                    <text x="150" y="58" fill="#7dd3fc" font-size="10" font-family="JetBrains Mono" font-weight="bold">Air Lacuna</text>
                                    <text x="100" y="113" fill="#7dd3fc" font-size="10" font-family="JetBrains Mono" font-weight="bold">Buoyancy</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Adaptation Description -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono leading-relaxed text-slate-300">
                            ${{mode === 'storage' ? 
                                '<span class="text-purple-400 font-bold">Storage Parenchyma:</span> Thin cellulose walls with large vacuoles storing starch, proteins, and water in potato tubers and fruit flesh.' : 
                              mode === 'chlorenchyma' ? 
                                '<span class="text-emerald-400 font-bold">Chlorenchyma:</span> Specialized mesophyll parenchyma packed with chloroplasts to execute photosynthetic solar conversion.' : 
                                '<span class="text-cyan-400 font-bold">Aerenchyma:</span> Massive internal air chambers in aquatic plants (e.g. Eichhornia) imparting positive hydrophyte buoyancy.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim6SetMode = function(m) {{
                mode = m;
                playTone(m === 'storage' ? 350 : m === 'chlorenchyma' ? 450 : 550, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 7: Collenchyma vs Sclerenchyma Stress Bench
        function renderSim7(vp) {{
            let material = 'collenchyma'; // 'collenchyma' vs 'sclerenchyma'
            let load = 30; // 0 to 100

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim7SetMat('collenchyma')" class="py-1.5 rounded-lg transition ${{material === 'collenchyma' ? 'bg-teal-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Collenchyma (Tensile Elasticity)
                            </button>
                            <button onclick="window.sim7SetMat('sclerenchyma')" class="py-1.5 rounded-lg transition ${{material === 'sclerenchyma' ? 'bg-amber-700 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Sclerenchyma (Rigid Armour)
                            </button>
                        </div>

                        <!-- Mechanical Testing Rig -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                <!-- Base Mount -->
                                <rect x="20" y="20" width="25" height="110" fill="#334155" stroke="#475569" stroke-width="2"/>
                                
                                ${{material === 'collenchyma' ? `
                                    <!-- Flexible Petiole Bending under Load -->
                                    <path d="M45,75 Q${{120}},${{75 + load*0.5}} ${{200}},${{75 + load*0.9}}" fill="none" stroke="#2dd4bf" stroke-width="12" stroke-linecap="round"/>
                                    <!-- Load Weight Icon -->
                                    <rect x="185" y="${{65 + load*0.9}}" width="30" height="25" rx="3" fill="#e11d48"/>
                                    <text x="190" y="${{82 + load*0.9}}" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold">${{load}}N</text>
                                    <text x="60" y="40" fill="#2dd4bf" font-size="10" font-family="JetBrains Mono">Bends without snapping!</text>
                                ` : `
                                    <!-- Rigid Lignified Rod with Crushing Anvil -->
                                    <rect x="45" y="70" width="150" height="16" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                                    <rect x="180" y="30" width="30" height="${{load > 80 ? 40 : 35}}" fill="#e11d48"/>
                                    <text x="185" y="52" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold">${{load}}N</text>
                                    ${{load > 80 ? `
                                        <!-- Micro-fracture lines -->
                                        <line x1="120" y1="70" x2="125" y2="86" stroke="#f87171" stroke-width="2"/>
                                        <text x="60" y="40" fill="#ef4444" font-size="10" font-family="JetBrains Mono" font-weight="bold">Fracture at high load!</text>
                                    ` : `
                                        <text x="60" y="40" fill="#f59e0b" font-size="10" font-family="JetBrains Mono">Extreme Compressive Hardness</text>
                                    `}}
                                `}}
                            </svg>
                        </div>

                        <!-- Load Slider -->
                        <div class="space-y-1">
                            <div class="flex justify-between text-xs text-slate-300 font-mono">
                                <span>Applied Mechanical Force:</span>
                                <span class="text-emerald-400 font-bold">${{load}} Newtons</span>
                            </div>
                            <input type="range" min="0" max="100" value="${{load}}" oninput="window.sim7SetLoad(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg h-2 cursor-pointer">
                        </div>
                    </div>
                `;
            }}

            window.sim7SetMat = function(m) {{
                material = m;
                playTone(380, 0.1);
                draw();
            }};

            window.sim7SetLoad = function(val) {{
                load = parseInt(val);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 8: Epidermis, Stomatal Gates & Suberised Cork
        function renderSim8(vp) {{
            let mode = 'stomata'; // 'stomata' or 'cork'
            let stomataOpen = true;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim8SetMode('stomata')" class="py-1.5 rounded-lg transition ${{mode === 'stomata' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Stomatal Guard Cells
                            </button>
                            <button onclick="window.sim8SetMode('cork')" class="py-1.5 rounded-lg transition ${{mode === 'cork' ? 'bg-amber-800 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Suberised Cork Bark
                            </button>
                        </div>

                        <!-- Graphic Window -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative">
                            ${{mode === 'stomata' ? `
                                <svg width="220" height="140" viewBox="0 0 220 140">
                                    <!-- Surrounding Epidermal Cells -->
                                    <path d="M20,20 Q60,10 100,20 Q110,60 100,70 Q60,80 20,70 Z" fill="#064e3b" stroke="#047857"/>
                                    <path d="M120,20 Q160,10 200,20 Q210,60 200,70 Q160,80 120,70 Z" fill="#064e3b" stroke="#047857"/>
                                    
                                    <!-- Paired Kidney Guard Cells -->
                                    ${{stomataOpen ? `
                                        <!-- Open Pore -->
                                        <path d="M90,40 Q75,70 90,100 Q105,70 90,40 Z" fill="#10b981" stroke="#059669" stroke-width="2"/>
                                        <path d="M130,40 Q145,70 130,100 Q115,70 130,40 Z" fill="#10b981" stroke="#059669" stroke-width="2"/>
                                        <!-- Open aperture pore -->
                                        <ellipse cx="110" cy="70" rx="10" ry="22" fill="#022c22"/>
                                        <text x="75" y="125" fill="#34d399" font-size="10" font-family="JetBrains Mono" font-weight="bold">Turgid Guard Cells: OPEN</text>
                                    ` : `
                                        <!-- Closed Pore -->
                                        <path d="M102,40 Q94,70 102,100 Q110,70 102,40 Z" fill="#047857" stroke="#065f46" stroke-width="2"/>
                                        <path d="M118,40 Q126,70 118,100 Q110,70 118,40 Z" fill="#047857" stroke="#065f46" stroke-width="2"/>
                                        <line x1="110" y1="45" x2="110" y2="95" stroke="#022c22" stroke-width="3"/>
                                        <text x="72" y="125" fill="#fbbf24" font-size="10" font-family="JetBrains Mono" font-weight="bold">Flaccid Guard Cells: CLOSED</text>
                                    `}}
                                </svg>
                            ` : `
                                <svg width="220" height="140" viewBox="0 0 220 140">
                                    <!-- Multi-layered brick-like cork cells with suberin walls -->
                                    <pattern id="corkBricks" width="36" height="18" patternUnits="userSpaceOnUse">
                                        <rect width="36" height="18" fill="#451a03" stroke="#b45309" stroke-width="2.5"/>
                                    </pattern>
                                    <rect x="20" y="25" width="180" height="90" rx="4" fill="url(#corkBricks)"/>
                                    <!-- Water drop repelled -->
                                    <path d="M40,15 Q45,22 45,28 A5,5 0 0,1 35,28 Q35,22 40,15 Z" fill="#38bdf8"/>
                                    <text x="60" y="20" fill="#38bdf8" font-size="10" font-family="JetBrains Mono" font-weight="bold">Impervious to Water & Gas (Suberin)</text>
                                </svg>
                            `}}
                        </div>

                        ${{mode === 'stomata' ? `
                            <button onclick="window.sim8ToggleStomata()" class="w-full py-2 rounded-xl text-xs font-bold font-mono transition ${{stomataOpen ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-300'}}">
                                ${{stomataOpen ? 'Trigger Night / Drought (Close Stomata)' : 'Trigger Daylight / Water (Open Stomata)'}}
                            </button>
                        ` : `
                            <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                                <span class="text-amber-400 font-bold">Suberin Architecture:</span> Dead, compactly arranged cells without intercellular spaces provide impermeable, fire-resistant armor for mature tree bark.
                            </div>
                        `}}
                    </div>
                `;
            }}

            window.sim8SetMode = function(m) {{
                mode = m;
                playTone(400, 0.1);
                draw();
            }};

            window.sim8ToggleStomata = function() {{
                stomataOpen = !stomataOpen;
                playTone(stomataOpen ? 520 : 320, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 9: Xylem Vascular Plumbing & Sap Ascent
        function renderSim9(vp) {{
            let rate = 50;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <!-- Transpiration Control -->
                        <div class="flex justify-between items-center text-xs font-mono text-slate-300">
                            <span>Transpirational Pull Rate:</span>
                            <span class="text-emerald-400 font-bold">${{rate}}%</span>
                        </div>
                        <input type="range" min="10" max="100" value="${{rate}}" oninput="window.sim9SetRate(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg h-2 cursor-pointer">

                        <!-- Xylem 4-Element Cutaway SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around h-48 relative overflow-hidden">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Element 1: Tracheid (tapered ends with pits) -->
                                <g transform="translate(15, 10)">
                                    <polygon points="15,0 30,25 30,125 15,150 0,125 0,25" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
                                    <!-- Bordered pits -->
                                    <circle cx="15" cy="45" r="3" fill="#4338ca"/>
                                    <circle cx="15" cy="75" r="3" fill="#4338ca"/>
                                    <circle cx="15" cy="105" r="3" fill="#4338ca"/>
                                    <text x="-5" y="165" fill="#a5b4fc" font-size="9" font-family="JetBrains Mono">Tracheid</text>
                                </g>

                                <!-- Element 2: Continuous Open Vessel Tube -->
                                <g transform="translate(65, 10)">
                                    <rect x="0" y="10" width="45" height="130" fill="#0c4a6e" stroke="#0284c7" stroke-width="2.5" rx="3"/>
                                    <!-- Dissolved end plates -->
                                    <line x1="0" y1="10" x2="45" y2="10" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
                                    <line x1="0" y1="140" x2="45" y2="140" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
                                    <!-- Rising water molecules -->
                                    <circle cx="22" cy="${{130 - (rate*1.1)%110}}" r="4.5" fill="#38bdf8" class="animate-bounce"/>
                                    <circle cx="22" cy="${{80 - (rate*0.8)%60}}" r="4" fill="#7dd3fc"/>
                                    <text x="5" y="165" fill="#38bdf8" font-size="9" font-family="JetBrains Mono" font-weight="bold">Vessel</text>
                                </g>

                                <!-- Element 3: Xylem Parenchyma (Living!) -->
                                <g transform="translate(130, 20)">
                                    <ellipse cx="20" cy="30" rx="18" ry="22" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <circle cx="20" cy="30" r="5" fill="#022c22"/>
                                    <ellipse cx="20" cy="85" rx="18" ry="22" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                                    <circle cx="20" cy="85" r="5" fill="#022c22"/>
                                    <text x="-5" y="155" fill="#34d399" font-size="9" font-family="JetBrains Mono" font-weight="bold">Parenchyma (Living)</text>
                                </g>

                                <!-- Element 4: Sclerenchymatous Fibre -->
                                <g transform="translate(200, 10)">
                                    <polygon points="10,0 20,20 20,130 10,150 0,130 0,20" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                                    <text x="0" y="165" fill="#f59e0b" font-size="9" font-family="JetBrains Mono">Fibre</text>
                                </g>
                            </svg>
                        </div>

                        <!-- Direction Tag -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono flex items-center justify-between">
                            <span class="text-slate-400">Conduction Vector:</span>
                            <span class="text-emerald-400 font-bold">Unidirectional Upward (Roots $\\to$ Leaves)</span>
                        </div>
                    </div>
                `;
            }}

            window.sim9SetRate = function(r) {{
                rate = parseInt(r);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 10: Phloem Sugar Translocation & Sieve Tube Anatomy
        function renderSim10(vp) {{
            let dir = 'downward'; // 'downward' to roots or 'upward' to buds

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim10SetDir('downward')" class="py-1.5 rounded-lg transition ${{dir === 'downward' ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Translocate Down (To Root Storage)
                            </button>
                            <button onclick="window.sim10SetDir('upward')" class="py-1.5 rounded-lg transition ${{dir === 'upward' ? 'bg-teal-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Translocate Up (To Growing Bud)
                            </button>
                        </div>

                        <!-- Phloem Unit SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-48 relative">
                            <svg width="240" height="170" viewBox="0 0 240 170">
                                <!-- Sieve Tube -->
                                <rect x="40" y="10" width="60" height="150" fill="#064e3b" stroke="#10b981" stroke-width="2.5" rx="4"/>
                                <!-- Perforated Sieve Plates -->
                                <line x1="40" y1="55" x2="100" y2="55" stroke="#34d399" stroke-width="3" stroke-dasharray="4,4"/>
                                <line x1="40" y1="115" x2="100" y2="115" stroke="#34d399" stroke-width="3" stroke-dasharray="4,4"/>

                                <!-- Moving Sucrose Solute Packets -->
                                <circle cx="70" cy="${{dir === 'downward' ? 30 : 135}}" r="5" fill="#facc15" class="animate-pulse"/>
                                <circle cx="70" cy="${{dir === 'downward' ? 85 : 85}}" r="5" fill="#facc15" class="animate-pulse"/>

                                <!-- Companion Cell (Metabolic Lifeline) -->
                                <rect x="110" y="25" width="45" height="120" fill="#134e4a" stroke="#2dd4bf" stroke-width="2" rx="6"/>
                                <!-- Large active nucleus -->
                                <ellipse cx="132" cy="85" rx="14" ry="16" fill="#042f2e" stroke="#5eead4" stroke-width="1.8"/>
                                <text x="122" y="88" fill="#5eead4" font-size="8" font-family="JetBrains Mono" font-weight="bold">Nucleus</text>

                                <!-- Plasmodesmata connections -->
                                <line x1="100" y1="70" x2="110" y2="70" stroke="#f59e0b" stroke-width="2"/>
                                <line x1="100" y1="100" x2="110" y2="100" stroke="#f59e0b" stroke-width="2"/>

                                <text x="45" y="165" fill="#34d399" font-size="9" font-family="JetBrains Mono" font-weight="bold">Sieve Tube</text>
                                <text x="110" y="165" fill="#2dd4bf" font-size="9" font-family="JetBrains Mono" font-weight="bold">Companion Cell</text>
                            </svg>
                        </div>

                        <!-- Metabolic Fact -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <span class="text-amber-400 font-bold">Nucleus Sharing:</span> Mature sieve tubes lack a nucleus to facilitate flow; the adjacent companion cell actively regulates ATP sucrose loading.
                        </div>
                    </div>
                `;
            }}

            window.sim10SetDir = function(d) {{
                dir = d;
                playTone(d === 'downward' ? 380 : 480, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 11: Animal Epithelial Histology Microscope
        function renderSim11(vp) {{
            let epType = 'squamous'; // 'squamous', 'stratified', 'cuboidal', 'columnar', 'ciliated'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 sm:grid-cols-5 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim11Set('squamous')" class="py-1 rounded transition ${{epType === 'squamous' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Squamous</button>
                            <button onclick="window.sim11Set('stratified')" class="py-1 rounded transition ${{epType === 'stratified' ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}}">Stratified</button>
                            <button onclick="window.sim11Set('cuboidal')" class="py-1 rounded transition ${{epType === 'cuboidal' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">Cuboidal</button>
                            <button onclick="window.sim11Set('columnar')" class="py-1 rounded transition ${{epType === 'columnar' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">Columnar</button>
                            <button onclick="window.sim11Set('ciliated')" class="py-1 rounded transition ${{epType === 'ciliated' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Ciliated</button>
                        </div>

                        <!-- Circular Eyepiece Field -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                            <div class="w-40 h-40 rounded-full border-4 border-slate-700 bg-slate-900 overflow-hidden relative flex items-center justify-center shadow-inner">
                                <svg width="160" height="160" viewBox="0 0 160 160">
                                    <!-- Acellular Basement Membrane -->
                                    <line x1="10" y1="120" x2="150" y2="120" stroke="#f43f5e" stroke-width="3" stroke-dasharray="3,2"/>
                                    
                                    ${{epType === 'squamous' ? `
                                        <!-- Flat pavement tile cells -->
                                        <path d="M15,120 Q50,110 85,120 Q120,110 145,120 L145,112 Q120,102 85,112 Q50,102 15,112 Z" fill="#0891b2" stroke="#06b6d4"/>
                                        <ellipse cx="50" cy="115" rx="6" ry="2" fill="#083344"/>
                                        <ellipse cx="115" cy="115" rx="6" ry="2" fill="#083344"/>
                                    ` : epType === 'stratified' ? `
                                        <!-- Multiple stratified layers -->
                                        <rect x="20" y="60" width="120" height="60" fill="#1e40af" stroke="#3b82f6"/>
                                        ${{[0,1,2].map(r => `<line x1="20" y1="${{75 + r*15}}" x2="140" y2="${{75 + r*15}}" stroke="#60a5fa" stroke-width="1.5"/>`).join('')}}
                                    ` : epType === 'cuboidal' ? `
                                        <!-- Cube shaped cells -->
                                        ${{[0,1,2,3].map(i => `
                                            <rect x="${{25 + i*28}}" y="85" width="26" height="35" rx="2" fill="#0f766e" stroke="#14b8a6" stroke-width="1.5"/>
                                            <circle cx="${{38 + i*28}}" cy="102" r="4.5" fill="#042f2e"/>
                                        `).join('')}}
                                    ` : epType === 'columnar' ? `
                                        <!-- Tall pillar like cells -->
                                        ${{[0,1,2,3].map(i => `
                                            <rect x="${{25 + i*28}}" y="45" width="26" height="75" rx="2" fill="#3730a3" stroke="#6366f1" stroke-width="1.5"/>
                                            <ellipse cx="${{38 + i*28}}" cy="95" rx="4.5" ry="7" fill="#1e1b4b"/>
                                        `).join('')}}
                                    ` : `
                                        <!-- Tall cells with waving cilia -->
                                        ${{[0,1,2,3].map(i => `
                                            <rect x="${{25 + i*28}}" y="55" width="26" height="65" rx="2" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
                                            <ellipse cx="${{38 + i*28}}" cy="95" rx="4" ry="6" fill="#022c22"/>
                                            <!-- Cilia hair tips -->
                                            <line x1="${{30 + i*28}}" y1="55" x2="${{28 + i*28}}" y2="42" stroke="#34d399" stroke-width="1.5"/>
                                            <line x1="${{38 + i*28}}" y1="55" x2="${{36 + i*28}}" y2="40" stroke="#34d399" stroke-width="1.5"/>
                                            <line x1="${{46 + i*28}}" y1="55" x2="${{44 + i*28}}" y2="42" stroke="#34d399" stroke-width="1.5"/>
                                        `).join('')}}
                                    `}}
                                </svg>
                            </div>
                        </div>

                        <!-- Anatomical Location Box -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <span class="text-cyan-400 font-bold">Body Location: </span>
                            ${{epType === 'squamous' ? 'Lung alveoli, blood capillaries (rapid gas diffusion).' : 
                              epType === 'stratified' ? 'Skin epidermis (resists mechanical abrasion and wear).' : 
                              epType === 'cuboidal' ? 'Kidney tubules, salivary gland ducts (secretion and absorption).' : 
                              epType === 'columnar' ? 'Stomach and intestinal lining (active nutrient absorption).' : 
                              'Trachea and respiratory tract (cilia propel mucus and dust outward).'}}
                        </div>
                    </div>
                `;
            }}

            window.sim11Set = function(t) {{
                epType = t;
                playTone(420, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 12: Connective Tissue & Joint Synovial Matrix
        function renderSim12(vp) {{
            let highlighted = 'ligament'; // 'ligament', 'tendon', 'cartilage', 'bone'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-bold">
                            <button onclick="window.sim12Set('ligament')" class="py-1.5 rounded transition ${{highlighted === 'ligament' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Ligament</button>
                            <button onclick="window.sim12Set('tendon')" class="py-1.5 rounded transition ${{highlighted === 'tendon' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Tendon</button>
                            <button onclick="window.sim12Set('cartilage')" class="py-1.5 rounded transition ${{highlighted === 'cartilage' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Cartilage</button>
                            <button onclick="window.sim12Set('bone')" class="py-1.5 rounded transition ${{highlighted === 'bone' ? 'bg-slate-600 text-white' : 'bg-slate-800 text-slate-400'}}">Bone</button>
                        </div>

                        <!-- Articulating Synovial Joint SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                <!-- Upper Femur Bone -->
                                <path d="M100,10 L140,10 L140,50 Q145,65 130,68 Q110,65 100,50 Z" fill="${{highlighted === 'bone' ? '#f8fafc' : '#94a3b8'}}" stroke="#cbd5e1" stroke-width="2"/>
                                <!-- Lower Tibia Bone -->
                                <path d="M100,140 L140,140 L140,100 Q145,85 130,82 Q110,85 100,100 Z" fill="${{highlighted === 'bone' ? '#f8fafc' : '#94a3b8'}}" stroke="#cbd5e1" stroke-width="2"/>

                                <!-- Articular Cartilage caps -->
                                <path d="M100,50 Q110,65 130,68" stroke="${{highlighted === 'cartilage' ? '#06b6d4' : '#0891b2'}}" stroke-width="${{highlighted === 'cartilage' ? 6 : 4}}" fill="none"/>
                                <path d="M100,100 Q110,85 130,82" stroke="${{highlighted === 'cartilage' ? '#06b6d4' : '#0891b2'}}" stroke-width="${{highlighted === 'cartilage' ? 6 : 4}}" fill="none"/>

                                <!-- Collateral Ligament (Bone to Bone) -->
                                <line x1="90" y1="40" x2="90" y2="110" stroke="${{highlighted === 'ligament' ? '#f59e0b' : '#78350f'}}" stroke-width="${{highlighted === 'ligament' ? 6 : 4}}" stroke-linecap="round" class="${{highlighted === 'ligament' ? 'animate-pulse' : ''}}"/>

                                <!-- Tendon (Muscle to Bone) -->
                                <line x1="150" y1="20" x2="150" y2="70" stroke="${{highlighted === 'tendon' ? '#f43f5e' : '#881337'}}" stroke-width="${{highlighted === 'tendon' ? 6 : 4}}" stroke-linecap="round" class="${{highlighted === 'tendon' ? 'animate-pulse' : ''}}"/>
                                <rect x="155" y="10" width="25" height="35" rx="3" fill="#be123c"/>
                                <text x="185" y="25" fill="#f43f5e" font-size="9" font-family="JetBrains Mono">Muscle</text>
                            </svg>
                        </div>

                        <!-- Info Pill -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{highlighted === 'ligament' ? '<span class="text-amber-400 font-bold">Ligament:</span> Connects Bone to Bone; exceptionally elastic with high tensile strength.' : 
                              highlighted === 'tendon' ? '<span class="text-rose-400 font-bold">Tendon:</span> Connects Muscle to Bone; fibrous with great toughness and limited elasticity.' : 
                              highlighted === 'cartilage' ? '<span class="text-cyan-400 font-bold">Cartilage:</span> Flexible proteoglycan matrix smoothing bone joint articular surfaces.' : 
                              '<span class="text-slate-200 font-bold">Bone:</span> Hard, rigid calcium phosphate matrix with osteocytes in Haversian canals.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim12Set = function(h) {{
                highlighted = h;
                playTone(450, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 13: 3-Way Muscular Triad: Striated, Smooth & Cardiac
        function renderSim13(vp) {{
            let musc = 'striated'; // 'striated', 'smooth', 'cardiac'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                            <button onclick="window.sim13Set('striated')" class="py-1.5 rounded-lg transition ${{musc === 'striated' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Striated (Skeletal)</button>
                            <button onclick="window.sim13Set('smooth')" class="py-1.5 rounded-lg transition ${{musc === 'smooth' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Smooth (Visceral)</button>
                            <button onclick="window.sim13Set('cardiac')" class="py-1.5 rounded-lg transition ${{musc === 'cardiac' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Cardiac (Heart)</button>
                        </div>

                        <!-- Microscopic Fiber View SVG -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="140" viewBox="0 0 240 140">
                                ${{musc === 'striated' ? `
                                    <!-- Long cylindrical unbranched syncytial fiber -->
                                    <rect x="20" y="35" width="200" height="30" rx="4" fill="#9f1239" stroke="#f43f5e" stroke-width="2"/>
                                    <rect x="20" y="75" width="200" height="30" rx="4" fill="#9f1239" stroke="#f43f5e" stroke-width="2"/>
                                    <!-- Cross striations -->
                                    ${{[0,1,2,3,4,5,6,7,8,9].map(i => `
                                        <line x1="${{35 + i*18}}" y1="35" x2="${{35 + i*18}}" y2="65" stroke="#fda4af" stroke-width="2"/>
                                        <line x1="${{35 + i*18}}" y1="75" x2="${{35 + i*18}}" y2="105" stroke="#fda4af" stroke-width="2"/>
                                    `).join('')}}
                                    <!-- Multiple peripheral nuclei -->
                                    <circle cx="60" cy="40" r="3" fill="#ffe4e6"/>
                                    <circle cx="140" cy="40" r="3" fill="#ffe4e6"/>
                                    <circle cx="90" cy="80" r="3" fill="#ffe4e6"/>
                                ` : musc === 'smooth' ? `
                                    <!-- Spindle shaped unbranched fibers -->
                                    <path d="M20,60 Q120,35 220,60 Q120,85 20,60 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
                                    <!-- Single central nucleus -->
                                    <ellipse cx="120" cy="60" rx="7" ry="4" fill="#fef3c7"/>
                                ` : `
                                    <!-- Cylindrical branched fibers with intercalated discs -->
                                    <rect x="20" y="30" width="110" height="26" fill="#047857" stroke="#10b981" stroke-width="1.8"/>
                                    <path d="M130,43 Q160,43 180,25 L220,25 L220,45 L180,45 Q160,57 130,57 Z" fill="#047857" stroke="#10b981" stroke-width="1.8"/>
                                    <rect x="20" y="75" width="200" height="26" fill="#047857" stroke="#10b981" stroke-width="1.8"/>
                                    <!-- Intercalated Discs -->
                                    <line x1="85" y1="30" x2="85" y2="56" stroke="#a7f3d0" stroke-width="4"/>
                                    <line x1="145" y1="75" x2="145" y2="101" stroke="#a7f3d0" stroke-width="4"/>
                                    <!-- Nuclei -->
                                    <circle cx="55" cy="43" r="4" fill="#ecfdf5"/>
                                    <circle cx="95" cy="88" r="4" fill="#ecfdf5"/>
                                `}}
                            </svg>
                        </div>

                        <!-- Diagnostic Properties -->
                        <div class="grid grid-cols-3 gap-1.5 text-[10px] font-mono text-center">
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                                <span class="text-slate-400">Control:</span>
                                <div class="text-white font-bold">${{musc === 'striated' ? 'Voluntary' : 'Involuntary'}}</div>
                            </div>
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                                <span class="text-slate-400">Nuclei:</span>
                                <div class="text-white font-bold">${{musc === 'striated' ? 'Multinucleate' : 'Uninucleate'}}</div>
                            </div>
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                                <span class="text-slate-400">Fatigue:</span>
                                <div class="font-bold ${{musc === 'striated' ? 'text-rose-400' : 'text-emerald-400'}}">${{musc === 'striated' ? 'Fatigues' : 'Fatigue-Free'}}</div>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim13Set = function(m) {{
                musc = m;
                playTone(m === 'striated' ? 440 : m === 'smooth' ? 330 : 520, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 14: Neuron Electrochemical Impulse Simulator
        function renderSim14(vp) {{
            let fired = false;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <button onclick="window.sim14Fire()" class="w-full py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white font-bold text-xs shadow-lg transition flex items-center justify-center gap-1.5">
                            <i data-lucide="zap" class="w-4 h-4"></i>
                            <span>Trigger Sensory Action Potential</span>
                        </button>

                        <!-- Neuron Diagram SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative overflow-hidden">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Cyton / Cell Body -->
                                <path d="M40,75 L20,40 M40,75 L15,70 M40,75 L20,110 M40,75 L25,130" stroke="#10b981" stroke-width="2.5"/>
                                <circle cx="45" cy="75" r="16" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                                <circle cx="45" cy="75" r="6" fill="#022c22"/>

                                <!-- Axon Fiber -->
                                <line x1="61" y1="75" x2="200" y2="75" stroke="#047857" stroke-width="4"/>

                                <!-- Myelin Sheath Schwann Cells -->
                                <rect x="75" y="66" width="22" height="18" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
                                <rect x="110" y="66" width="22" height="18" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
                                <rect x="145" y="66" width="22" height="18" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
                                <rect x="180" y="66" width="22" height="18" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>

                                <!-- Axon Terminals & Synapse Knobs -->
                                <path d="M202,75 L225,55 M202,75 L230,75 M202,75 L225,95" stroke="#10b981" stroke-width="2"/>
                                <circle cx="225" cy="55" r="3" fill="#34d399"/>
                                <circle cx="230" cy="75" r="3" fill="#34d399"/>
                                <circle cx="225" cy="95" r="3" fill="#34d399"/>

                                <!-- Firing Action Potential Wave -->
                                ${{fired ? `
                                    <circle cx="45" cy="75" r="8" fill="#facc15" opacity="0.9" class="animate-ping"/>
                                    <line x1="60" y1="75" x2="225" y2="75" stroke="#fbbf24" stroke-width="4" stroke-dasharray="8,8" class="animate-pulse"/>
                                ` : ''}}
                            </svg>
                        </div>

                        <!-- Conduction Pathway -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-center">
                            <span class="text-emerald-400 font-bold">Impulse Pathway: </span>
                            <span class="text-slate-300">Dendrite $\\to$ Cyton (Cell Body) $\\to$ Axon $\\to$ Synapse</span>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }}

            window.sim14Fire = function() {{
                fired = true;
                playTone(660, 0.15, 'sawtooth');
                draw();
                setTimeout(() => {{ fired = false; draw(); }}, 1000);
            }};

            draw();
        }}

        // SIMULATOR 15: Musculoskeletal Biomechanics, R.I.C.E. & Yoga
        function renderSim15(vp) {{
            let mode = 'biceps'; // 'biceps', 'rice', 'yoga'
            let flex = 45; // elbow angle

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1.5 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[11px] font-bold">
                            <button onclick="window.sim15Set('biceps')" class="py-1.5 rounded transition ${{mode === 'biceps' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">Antagonist Pair</button>
                            <button onclick="window.sim15Set('rice')" class="py-1.5 rounded transition ${{mode === 'rice' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">R.I.C.E. Protocol</button>
                            <button onclick="window.sim15Set('yoga')" class="py-1.5 rounded transition ${{mode === 'yoga' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Yoga Asanas</button>
                        </div>

                        <!-- Interactive Visualization Frame -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            ${{mode === 'biceps' ? `
                                <svg width="220" height="150" viewBox="0 0 220 150">
                                    <!-- Upper arm bone (Humerus) -->
                                    <line x1="40" y1="40" x2="110" y2="75" stroke="#94a3b8" stroke-width="12" stroke-linecap="round"/>
                                    <!-- Forearm (Radius/Ulna) moving with flex -->
                                    <line x1="110" y1="75" x2="${{110 + 60*Math.cos((flex-30)*Math.PI/180)}}" y2="${{75 - 60*Math.sin((flex-30)*Math.PI/180)}}" stroke="#94a3b8" stroke-width="10" stroke-linecap="round"/>
                                    <!-- Hinge joint circle -->
                                    <circle cx="110" cy="75" r="7" fill="#38bdf8"/>
                                    <!-- Biceps Muscle (Contracted when high flex) -->
                                    <path d="M50,45 Q75,${{50 - flex*0.3}} 105,70" stroke="#e11d48" stroke-width="${{6 + flex*0.1}}" fill="none" stroke-linecap="round"/>
                                    <!-- Triceps Muscle (Relaxed) -->
                                    <path d="M45,55 Q75,70 105,80" stroke="#fda4af" stroke-width="5" fill="none" stroke-linecap="round"/>
                                </svg>
                            ` : mode === 'rice' ? `
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-left w-full">
                                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                        <span class="text-rose-400 font-bold">R - Rest:</span>
                                        <p class="text-slate-300 text-[10px]">Immobilize to prevent micro-tear expansion.</p>
                                    </div>
                                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                        <span class="text-cyan-400 font-bold">I - Ice:</span>
                                        <p class="text-slate-300 text-[10px]">Vasoconstrict vessels to limit swelling.</p>
                                    </div>
                                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                        <span class="text-amber-400 font-bold">C - Compression:</span>
                                        <p class="text-slate-300 text-[10px]">Elastic wrap to curb interstitial fluid edema.</p>
                                    </div>
                                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                                        <span class="text-emerald-400 font-bold">E - Elevation:</span>
                                        <p class="text-slate-300 text-[10px]">Gravity lymphatic & venous fluid return.</p>
                                    </div>
                                </div>
                            ` : `
                                <div class="text-center space-y-2">
                                    <div class="text-xs font-mono text-emerald-400 font-bold">Tadasana & Bhujangasana Postural Ergonomics</div>
                                    <p class="text-[11px] text-slate-300 max-w-xs leading-relaxed">
                                        Yoga asanas engage the deep transverse abdominis and erector spinae muscles, lubricate synovial joint cartilage, and prevent kyphotic/lordotic spinal deformities.
                                    </p>
                                </div>
                            `}}
                        </div>

                        ${{mode === 'biceps' ? `
                            <div class="space-y-1">
                                <div class="flex justify-between text-xs text-slate-300 font-mono">
                                    <span>Elbow Joint Flexion Angle:</span>
                                    <span class="text-emerald-400 font-bold">${{flex}}°</span>
                                </div>
                                <input type="range" min="10" max="90" value="${{flex}}" oninput="window.sim15SetFlex(this.value)" class="w-full accent-emerald-500 bg-slate-800 rounded-lg h-2 cursor-pointer">
                            </div>
                        ` : ''}}
                    </div>
                `;
            }}

            window.sim15Set = function(m) {{
                mode = m;
                playTone(480, 0.08);
                draw();
            }};

            window.sim15SetFlex = function(f) {{
                flex = parseInt(f);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 16: 1964 Delhi Univ Anther Culture & Totipotency
        function renderSim16(vp) {{
            let step = 1; // 1 to 5

            function draw() {{
                const steps = [
                    {{ title: "1. Datura innoxia Bud", desc: "Immature floral buds dissected to harvest fresh intact anthers containing uninucleate pollen microspores." }},
                    {{ title: "2. Plating on Nutrient Agar", desc: "Anthers cultured under sterile conditions on Nitsch's synthetic mineral medium with vitamins." }},
                    {{ title: "3. Androgenic Division", desc: "Haploid microspores triggered to bypass normal gamete fate and undergo sporophytic mitotic divisions." }},
                    {{ title: "4. Embryoid Formation", desc: "Cellular totipotency proven as haploid cells form globular and heart-shaped plant embryoids." }},
                    {{ title: "5. Haploid Plantlet Emergence", desc: "Complete viable haploid plants regenerate! Chromosome doubling yields instant homozygous pure lines." }}
                ];

                const cur = steps[step - 1];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">1964 Experiment Timeline:</span>
                            <span class="text-emerald-400 font-bold">Step ${{step}} of 5</span>
                        </div>

                        <!-- 5 Steps Button Strip -->
                        <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800">
                            ${{[1,2,3,4,5].map(s => `
                                <button onclick="window.sim16Set(${{s}})" class="py-1 rounded text-xs font-mono font-bold transition ${{step === s ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                    S${{s}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Step Graphic SVG -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="220" height="140" viewBox="0 0 220 140">
                                ${{step === 1 ? `
                                    <!-- Datura flower bud -->
                                    <path d="M110,120 Q80,70 110,20 Q140,70 110,120" fill="#047857" stroke="#10b981" stroke-width="2"/>
                                    <circle cx="110" cy="70" r="12" fill="#facc15" stroke="#eab308"/>
                                    <text x="60" y="135" fill="#facc15" font-size="9" font-family="JetBrains Mono">Anther Dissection</text>
                                ` : step === 2 ? `
                                    <!-- Petri dish with agar -->
                                    <ellipse cx="110" cy="90" rx="80" ry="35" fill="#0f172a" stroke="#64748b" stroke-width="3"/>
                                    <ellipse cx="110" cy="90" rx="72" ry="30" fill="#065f46" opacity="0.4"/>
                                    <!-- Cultured anthers -->
                                    <ellipse cx="80" cy="88" rx="8" ry="4" fill="#eab308"/>
                                    <ellipse cx="110" cy="95" rx="8" ry="4" fill="#eab308"/>
                                    <ellipse cx="140" cy="85" rx="8" ry="4" fill="#eab308"/>
                                ` : step === 3 ? `
                                    <!-- Microspore pollen dividing -->
                                    <circle cx="110" cy="70" r="35" fill="#134e4a" stroke="#2dd4bf" stroke-width="2.5"/>
                                    <line x1="75" y1="70" x2="145" y2="70" stroke="#2dd4bf" stroke-width="2" stroke-dasharray="3,3"/>
                                    <circle cx="95" cy="55" r="7" fill="#a7f3d0"/>
                                    <circle cx="125" cy="85" r="7" fill="#a7f3d0"/>
                                    <text x="45" y="125" fill="#2dd4bf" font-size="9" font-family="JetBrains Mono">Totipotent Mitotic Division</text>
                                ` : step === 4 ? `
                                    <!-- Heart shaped embryoid -->
                                    <path d="M110,95 Q70,55 90,30 A15,15 0 0,1 110,45 A15,15 0 0,1 130,30 Q150,55 110,95 Z" fill="#10b981" stroke="#34d399" stroke-width="2.5"/>
                                    <text x="60" y="125" fill="#34d399" font-size="9" font-family="JetBrains Mono">Heart-Stage Embryoid</text>
                                ` : `
                                    <!-- Regenerated Haploid Plantlet -->
                                    <line x1="110" y1="120" x2="110" y2="40" stroke="#10b981" stroke-width="4"/>
                                    <!-- Leaves -->
                                    <path d="M110,70 Q80,55 60,65 Q85,80 110,70" fill="#34d399"/>
                                    <path d="M110,50 Q140,35 160,45 Q135,60 110,50" fill="#34d399"/>
                                    <!-- Rootlets -->
                                    <path d="M110,120 Q95,135 80,138 M110,120 Q125,135 140,138" stroke="#78350f" stroke-width="2.5" fill="none"/>
                                    <text x="50" y="25" fill="#facc15" font-size="10" font-family="JetBrains Mono" font-weight="bold">Haploid Plantlet (n) Regenerated!</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Step Description -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono leading-relaxed space-y-1">
                            <div class="text-emerald-400 font-bold">${{cur.title}}</div>
                            <p class="text-slate-300 text-[10px]">${{cur.desc}}</p>
                        </div>
                    </div>
                `;
            }}

            window.sim16Set = function(s) {{
                step = s;
                playTone(300 + s * 70, 0.1);
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

