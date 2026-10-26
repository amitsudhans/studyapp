# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 5 (Chemistry)
EXPLORING MIXTURES AND THEIR SEPARATION
Homogeneous & Heterogeneous Mixtures, Solutions, Suspensions, Colloids, Concentration Formulas,
Separation Techniques, Traditional Kannauj Distillation, Paperfuge, Dr. Dilip Mahalanabis ORS & Artificial Blood
Syllabus Competencies: C-1.2, C-5.1, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
Generates public/animations/class9-exploring-mixtures-and-separation.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_mixtures_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-exploring-mixtures-and-separation.html"

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
    <title>NCERT Class 9 Science • Chapter 5: Exploring Mixtures & Separation Laboratory</title>
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
        body {{
            font-family: 'Inter', sans-serif;
        }}
        code, pre, .font-mono {{
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
            0%, 100% {{ box-shadow: 0 0 15px rgba(99, 102, 241, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(99, 102, 241, 0.45); }}
        }}
        .pulse-border {{
            animation: pulseGlow 2.5s infinite;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-indigo-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="glass-panel sticky top-0 z-40 border-b border-slate-800/80 px-4 py-2.5 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 via-violet-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-indigo-950/40 border border-indigo-400/30">
                <i data-lucide="flask-conical" class="w-5 h-5 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold tracking-wider uppercase px-2 py-0.5 rounded bg-indigo-950/80 text-indigo-400 border border-indigo-800/60 font-mono">
                        NCERT Class 9 Science • Chapter 5
                    </span>
                    <span class="hidden sm:inline-block text-[11px] font-medium text-slate-400">• Chemistry & Separation Science</span>
                </div>
                <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-1.5">
                    Exploring Mixtures and their Separation
                </h1>
            </div>
        </div>

        <!-- Slide Selector & Nav Controls -->
        <div class="flex items-center gap-2 sm:gap-3">
            <div class="relative">
                <button onclick="window.toggleSlideMenu()" id="slideMenuBtn" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700/70 hover:bg-slate-800 text-xs font-semibold text-slate-200 transition">
                    <i data-lucide="compass" class="w-3.5 h-3.5 text-indigo-400"></i>
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
                <button onclick="window.toggleSpeech()" id="speechBtn" title="Play Voiceover Narration" class="w-8 h-8 rounded-md bg-indigo-600 hover:bg-indigo-500 text-white flex items-center justify-center transition">
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
            <div class="glass-panel rounded-2xl p-4 border border-slate-800/80 shadow-xl relative overflow-hidden bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-indigo-950/20">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Talking Avatar (Prof. Sophia) -->
                    <div class="relative w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-b from-indigo-600 to-violet-800 p-0.5 shadow-md shrink-0">
                        <svg viewBox="0 0 100 100" class="w-full h-full rounded-[14px] bg-slate-900 overflow-hidden">
                            <rect width="100" height="100" fill="#13102b"/>
                            <circle cx="50" cy="50" r="42" fill="#312e81" opacity="0.4"/>
                            <!-- Torso / Lab Coat -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#334155"/>
                            <path d="M35,90 L50,100 L65,90 L60,82 L50,86 L40,82 Z" fill="#4f46e5"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="46" rx="22" ry="26" fill="#fed7aa"/>
                            <!-- Hair -->
                            <path d="M26,42 Q28,18 50,18 Q72,18 74,42 Q68,26 50,26 Q32,26 26,42 Z" fill="#374151"/>
                            <path d="M26,42 Q24,60 28,68 Q32,56 32,46 Z" fill="#374151"/>
                            <path d="M74,42 Q76,60 72,68 Q68,56 68,46 Z" fill="#374151"/>
                            <!-- Glasses -->
                            <rect x="33" y="40" width="13" height="8" rx="2" fill="none" stroke="#4338ca" stroke-width="2"/>
                            <rect x="54" y="40" width="13" height="8" rx="2" fill="none" stroke="#4338ca" stroke-width="2"/>
                            <line x1="46" y1="44" x2="54" y2="44" stroke="#4338ca" stroke-width="2"/>
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
                        <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded text-[9px] font-bold bg-indigo-500 text-white font-mono shadow">
                            TEACHER
                        </div>
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between gap-2">
                            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider font-mono">Prof. Sophia • Voice Guide</span>
                            <span id="speechStatusIndicator" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Ready</span>
                        </div>
                        <p id="narrationText" class="text-xs text-slate-300 mt-1 line-clamp-3 leading-relaxed italic">
                            Welcome students! Today we unlock the science of mixtures, solutions, colloids, and separation techniques—bridging fundamental chemistry, classical Indian distillation, and life-saving medical discoveries.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Content Presentation Slide (Slides 1 to 16) -->
            <div id="contentSlideContainer" class="space-y-4">
                <!-- Slide Header Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between">
                        <span id="slideCategoryText" class="text-[11px] font-bold text-indigo-400 uppercase tracking-widest font-mono">Section Core Theory</span>
                        <span id="slideBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-indigo-950/80 text-indigo-300 border border-indigo-800/60 font-mono">
                            Part 1 of 20
                        </span>
                    </div>
                    <div>
                        <h2 id="slideTitle" class="text-lg sm:text-xl font-extrabold text-white tracking-tight">Matter & Purity: Pure Substances vs Mixtures</h2>
                        <p id="slideSubtitle" class="text-xs sm:text-sm font-medium text-indigo-400/90 mt-0.5">Homogeneous vs Heterogeneous Systems: Physical Combinations without Fixed Ratios</p>
                    </div>
                    <ul id="slideKeyPoints" class="text-xs sm:text-sm text-slate-300 space-y-2 pt-1 border-t border-slate-800/80 leading-relaxed">
                        <!-- Injected via JavaScript -->
                    </ul>
                </div>

                <!-- Checkpoints Container -->
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle" class="w-4 h-4 text-indigo-400"></i>
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
                        <span class="text-xs font-mono font-bold text-indigo-400">Score: <span id="quizScoreVal">0</span> / 10</span>
                    </div>
                </div>

                <div id="quizQuestionsList" class="space-y-4">
                    <!-- Injected via JavaScript -->
                </div>
            </div>

            <!-- Slide 20 Last Slide Notice -->
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-indigo-500/40 bg-gradient-to-r from-indigo-950/40 via-slate-900 to-violet-950/40 shadow-xl shadow-indigo-950/30">
                <div class="w-12 h-12 rounded-full bg-indigo-500/20 text-indigo-400 border border-indigo-500/40 flex items-center justify-center mx-auto mb-2">
                    <i data-lucide="check-check" class="w-6 h-6"></i>
                </div>
                <h4 class="text-lg font-bold text-white">Curriculum Chapter Mastered!</h4>
                <p class="text-base sm:text-lg text-indigo-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">
                    You have comprehensively mastered Solutions, Suspensions, Colloids, Concentration Formulas, Separation Techniques (Sublimation, Centrifugation, Chromatography, Fractional Distillation, Crystallisation, Alum Coagulation), Kannauj Deg-Bhapka, the Paperfuge, Dr. Dilip Mahalanabis's ORS, and Artificial Blood science!
                </p>
            </div>

        </div>

        <!-- Right Column: Interactive Bespoke SVG Simulators (5 cols) -->
        <div class="lg:col-span-5 flex flex-col gap-4 sticky top-20">
            <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 shadow-2xl flex flex-col gap-3">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4 text-indigo-400"></i>
                        <h3 id="simulatorTitle" class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">
                            Interactive Visual Laboratory
                        </h3>
                    </div>
                    <span id="simulatorBadge" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-violet-400 border border-slate-700">
                        Interactive SVG
                    </span>
                </div>

                <!-- Simulator Dynamic Viewport -->
                <div id="simulatorViewport" class="min-h-[380px] flex items-center justify-center relative">
                    <!-- Dynamic Interactive Simulator Content Rendered Here -->
                </div>
            </div>

            <!-- Global Laboratory Quick Stats -->
            <div class="glass-panel rounded-xl p-3 border border-slate-800/80 flex items-center justify-around text-center text-xs">
                <div>
                    <span class="text-slate-400 block text-[10px]">Mixture Types</span>
                    <span class="font-bold text-indigo-400 font-mono">3 Classes</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Separations</span>
                    <span class="font-bold text-violet-400 font-mono">6 Methods</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Pioneers</span>
                    <span class="font-bold text-cyan-400 font-mono">ORS & Paperfuge</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Checkpoints</span>
                    <span class="font-bold text-amber-400 font-mono">32 Total</span>
                </div>
            </div>
        </div>

    </main>

    <!-- Bottom Action Navigation Bar -->
    <footer class="glass-panel sticky bottom-0 z-40 border-t border-slate-800/90 px-4 py-3 mt-auto">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <button onclick="window.prevSlide()" id="prevBtn" class="flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-300 transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                <span>Previous Slide</span>
            </button>

            <!-- Slide Dots -->
            <div id="slideDots" class="hidden md:flex items-center gap-1.5 overflow-x-auto max-w-md py-1 px-2">
                <!-- 20 Indicator Dots -->
            </div>

            <button onclick="window.nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white text-xs font-bold shadow-lg shadow-indigo-950/40 transition">
                <span>Next Slide</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </div>
    </footer>

    <!-- Step-by-Step Solution Pop-up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <div class="glass-panel w-full max-w-lg rounded-2xl border border-indigo-500/50 p-6 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm">
                    <i data-lucide="lightbulb" class="w-4 h-4"></i>
                    <span>Step-by-Step Pedagogical Solution</span>
                </div>
                <button onclick="window.closeSolutionModal()" class="w-7 h-7 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            </div>
            <div id="solutionModalBody" class="text-xs sm:text-sm text-slate-300 space-y-3 leading-relaxed">
                <!-- Dynamic Solution Content -->
            </div>
            <div class="text-right pt-2 border-t border-slate-800">
                <button onclick="window.closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                    Understood & Continue
                </button>
            </div>
        </div>
    </div>

    <!-- Application Script -->
    <script>
        const SLIDES = {slides_json};
        const QUIZZES = {quizzes_json};
        let currentSlide = 0; // 0 to 19
        let isSpeaking = false;
        let synth = window.speechSynthesis;
        let currentUtterance = null;
        let quizAnswers = {{}}; // slideIndex: {{ qIdx: selectedOpt }}

        // Audio synthesizer fallback
        let audioCtx = null;
        function playTone(freq = 440, duration = 0.15) {{
            try {{
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.frequency.value = freq;
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }} catch(e) {{}}
        }}

        // Slide dropdown menu builder
        function buildSlideMenu() {{
            const list = document.getElementById('slideListItems');
            const dots = document.getElementById('slideDots');
            list.innerHTML = '';
            dots.innerHTML = '';

            const allSlides = [...SLIDES, ...QUIZZES];
            allSlides.forEach((s, idx) => {{
                // Menu item
                const btn = document.createElement('button');
                btn.className = `w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between transition ${{idx === currentSlide ? 'bg-indigo-950/80 text-indigo-300 font-bold border border-indigo-700/50' : 'text-slate-300 hover:bg-slate-800/80'}}`;
                btn.innerHTML = `
                    <span class="truncate pr-2">${{idx + 1}}. ${{s.title}}</span>
                    <span class="text-[10px] font-mono ${{idx >= 16 ? 'text-amber-400' : 'text-slate-400'}}">${{idx >= 16 ? 'Quiz' : 'Theory'}}</span>
                `;
                btn.onclick = () => {{
                    goToSlide(idx);
                    toggleSlideMenu(false);
                }};
                list.appendChild(btn);

                // Indicator dot
                const dot = document.createElement('button');
                dot.className = `h-2 rounded-full transition-all ${{idx === currentSlide ? 'w-6 bg-indigo-500' : 'w-2 bg-slate-700 hover:bg-slate-500'}}`;
                dot.title = `Slide ${{idx + 1}}: ${{s.title}}`;
                dot.onclick = () => goToSlide(idx);
                dots.appendChild(dot);
            }});
        }}

        function toggleSlideMenu(force) {{
            const el = document.getElementById('slideMenuDropdown');
            if (typeof force === 'boolean') {{
                if (force) el.classList.remove('hidden'); else el.classList.add('hidden');
            }} else {{
                el.classList.toggle('hidden');
            }}
        }}

        // Narration Voiceover Controller
        function toggleSpeech() {{
            if (isSpeaking) {{
                stopSpeech();
            }} else {{
                playNarration();
            }}
        }}

        function stopSpeech() {{
            if (synth) {{
                synth.cancel();
            }}
            isSpeaking = false;
            updateSpeechUI(false);
        }}

        function playNarration() {{
            stopSpeech();
            const slideData = currentSlide < 16 ? SLIDES[currentSlide] : QUIZZES[currentSlide - 16];
            const textToSpeak = slideData.narration || slideData.title;

            if ('speechSynthesis' in window) {{
                currentUtterance = new SpeechSynthesisUtterance(textToSpeak);
                currentUtterance.rate = 0.96;
                currentUtterance.pitch = 1.05;
                currentUtterance.lang = 'en-US';

                currentUtterance.onstart = () => {{
                    isSpeaking = true;
                    updateSpeechUI(true);
                }};
                currentUtterance.onend = () => {{
                    isSpeaking = false;
                    updateSpeechUI(false);
                }};
                currentUtterance.onerror = () => {{
                    isSpeaking = false;
                    updateSpeechUI(false);
                }};
                synth.speak(currentUtterance);
            }} else {{
                playTone(550, 0.3);
            }}
        }}

        function updateSpeechUI(speaking) {{
            const mouth = document.getElementById('teacherMouth');
            const icon = document.getElementById('speechIcon');
            const indicator = document.getElementById('speechStatusIndicator');
            if (speaking) {{
                mouth.classList.add('talking');
                icon.setAttribute('data-lucide', 'volume-x');
                indicator.textContent = 'Speaking...';
                indicator.className = 'text-[10px] font-mono px-2 py-0.5 rounded bg-indigo-950 text-indigo-400 border border-indigo-800 animate-pulse';
            }} else {{
                mouth.classList.remove('talking');
                icon.setAttribute('data-lucide', 'volume-2');
                indicator.textContent = 'Ready';
                indicator.className = 'text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400';
            }}
            lucide.createIcons();
        }}

        function renderSlide(idx) {{
            stopSpeech();
            currentSlide = idx;
            document.getElementById('currentSlideNum').textContent = idx + 1;

            buildSlideMenu();

            const isQuiz = idx >= 16;
            const contentContainer = document.getElementById('contentSlideContainer');
            const quizContainer = document.getElementById('quizSlideContainer');
            const lastNotice = document.getElementById('lastSlideNotice');
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');

            // Previous / Next Button Visibility
            prevBtn.disabled = (idx === 0);
            prevBtn.classList.toggle('opacity-40', idx === 0);

            if (idx === 19) {{
                // Slide 20 (index 19) is the last slide
                nextBtn.style.display = 'none';
                lastNotice.classList.remove('hidden');
            }} else {{
                nextBtn.style.display = 'flex';
                lastNotice.classList.add('hidden');
            }}

            if (!isQuiz) {{
                // Slide 1 to 16: Theory & Checkpoints
                contentContainer.classList.remove('hidden');
                quizContainer.classList.add('hidden');

                const data = SLIDES[idx];
                document.getElementById('slideTitle').textContent = data.title;
                document.getElementById('slideSubtitle').textContent = data.subtitle;
                document.getElementById('slideBadge').textContent = `Part ${{idx + 1}} of 20`;
                document.getElementById('narrationText').textContent = data.narration;

                // Points List
                const pointsList = document.getElementById('slideKeyPoints');
                pointsList.innerHTML = data.points.map(pt => `
                    <li class="flex items-start gap-2.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 mt-2 shrink-0"></span>
                        <span>${{pt}}</span>
                    </li>
                `).join('');

                // Checkpoints List (2 per slide)
                const cpList = document.getElementById('checkpointsList');
                cpList.innerHTML = data.checkpoints.map((cp, cpIdx) => `
                    <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/80 space-y-2.5">
                        <div class="flex items-start justify-between gap-2">
                            <span class="text-xs font-semibold text-slate-200">
                                <span class="text-indigo-400 font-mono font-bold mr-1.5">Q${{cpIdx + 1}}.</span>
                                ${{cp.q}}
                            </span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                            ${{cp.options.map((opt, optIdx) => `
                                <button onclick="window.checkAnswer(${{idx}}, ${{cpIdx}}, ${{optIdx}})" 
                                        id="cp-btn-${{idx}}-${{cpIdx}}-${{optIdx}}"
                                        class="text-left px-3 py-2 rounded-lg text-xs font-medium bg-slate-950 border border-slate-800 hover:border-indigo-600/60 hover:bg-slate-800/60 transition flex items-center justify-between">
                                    <span>${{opt}}</span>
                                    <span class="w-3.5 h-3.5 rounded-full border border-slate-700 shrink-0 ml-2"></span>
                                </button>
                            `).join('')}}
                        </div>
                        <div id="cp-feedback-${{idx}}-${{cpIdx}}" class="hidden text-xs p-2 rounded-lg mt-1 font-mono"></div>
                    </div>
                `).join('');

                // Render Interactive Simulator
                renderSimulator(idx);

            }} else {{
                // Slides 17 to 20: Dedicated Quiz
                contentContainer.classList.add('hidden');
                quizContainer.classList.remove('hidden');

                const qData = QUIZZES[idx - 16];
                document.getElementById('quizTitleDisplay').textContent = qData.title;
                document.getElementById('narrationText').textContent = qData.narration;

                updateQuizScoreDisplay(idx);

                const qList = document.getElementById('quizQuestionsList');
                qList.innerHTML = qData.questions.map((q, qIdx) => `
                    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
                        <div class="flex items-start justify-between gap-3">
                            <span class="text-xs sm:text-sm font-semibold text-slate-100">
                                <span class="text-indigo-400 font-mono font-bold mr-1">Q${{qIdx + 1}}.</span>
                                ${{q.q}}
                            </span>
                            <button onclick="window.openSolutionModal(${{idx - 16}}, ${{qIdx}})" 
                                    class="shrink-0 text-[11px] font-mono px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-800/50 flex items-center gap-1 transition">
                                <i data-lucide="help-circle" class="w-3 h-3"></i>
                                View Solution
                            </button>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            ${{q.options.map((opt, optIdx) => `
                                <button onclick="window.selectQuizAnswer(${{idx}}, ${{qIdx}}, ${{optIdx}})"
                                        id="quiz-btn-${{idx}}-${{qIdx}}-${{optIdx}}"
                                        class="text-left px-3 py-2 rounded-lg text-xs bg-slate-950 border border-slate-800 hover:border-indigo-500/60 transition flex items-center justify-between">
                                    <span>${{opt}}</span>
                                    <span class="w-3 h-3 rounded-full border border-slate-700 shrink-0 ml-2"></span>
                                </button>
                            `).join('')}}
                        </div>
                        <div id="quiz-feedback-${{idx}}-${{qIdx}}" class="hidden text-xs p-2 rounded-lg font-mono"></div>
                    </div>
                `).join('');

                // Render Summary View in Simulator Window
                renderQuizSimulator(idx);
            }}

            lucide.createIcons();
            if (window.renderMathInElement) {{
                renderMathInElement(document.body);
            }}
        }}

        function checkAnswer(slideIdx, cpIdx, optIdx) {{
            const cp = SLIDES[slideIdx].checkpoints[cpIdx];
            const feedbackEl = document.getElementById(`cp-feedback-${{slideIdx}}-${{cpIdx}}`);
            const isCorrect = (optIdx === cp.correct);

            // Highlight all option buttons
            cp.options.forEach((_, i) => {{
                const btn = document.getElementById(`cp-btn-${{slideIdx}}-${{cpIdx}}-${{i}}`);
                btn.classList.remove('bg-indigo-950', 'border-indigo-500', 'text-indigo-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === cp.correct) {{
                    btn.classList.add('bg-indigo-950/80', 'border-indigo-500', 'text-indigo-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-indigo-950/60', 'text-indigo-300', 'border-indigo-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-indigo-950/60', 'text-indigo-300', 'border', 'border-indigo-800/80');
                feedbackEl.innerHTML = `✓ <strong>Spot On!</strong> ${{cp.explanation}}`;
            }} else {{
                playTone(280, 0.2);
                feedbackEl.classList.add('bg-rose-950/60', 'text-rose-300', 'border', 'border-rose-800/80');
                feedbackEl.innerHTML = `✕ <strong>Review:</strong> ${{cp.explanation}}`;
            }}
        }}

        function selectQuizAnswer(slideIdx, qIdx, optIdx) {{
            if (!quizAnswers[slideIdx]) quizAnswers[slideIdx] = {{}};
            quizAnswers[slideIdx][qIdx] = optIdx;

            const q = QUIZZES[slideIdx - 16].questions[qIdx];
            const feedbackEl = document.getElementById(`quiz-feedback-${{slideIdx}}-${{qIdx}}`);
            const isCorrect = (optIdx === q.correct);

            q.options.forEach((_, i) => {{
                const btn = document.getElementById(`quiz-btn-${{slideIdx}}-${{qIdx}}-${{i}}`);
                btn.classList.remove('bg-indigo-950', 'border-indigo-500', 'text-indigo-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === q.correct) {{
                    btn.classList.add('bg-indigo-950/80', 'border-indigo-500', 'text-indigo-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-indigo-950/60', 'text-indigo-300', 'border-indigo-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-indigo-950/60', 'text-indigo-300', 'border', 'border-indigo-800/80');
                feedbackEl.innerHTML = `✓ Correct! Keep mastering the concepts.`;
            }} else {{
                playTone(280, 0.2);
                feedbackEl.classList.add('bg-rose-950/60', 'text-rose-300', 'border', 'border-rose-800/80');
                feedbackEl.innerHTML = `✕ Needs Review. Click 'View Solution' for detailed derivation.`;
            }}

            updateQuizScoreDisplay(slideIdx);
        }}

        function updateQuizScoreDisplay(slideIdx) {{
            const answers = quizAnswers[slideIdx] || {{}};
            let score = 0;
            const questions = QUIZZES[slideIdx - 16].questions;
            for (let qIdx in answers) {{
                if (answers[qIdx] === questions[qIdx].correct) {{
                    score++;
                }}
            }}
            document.getElementById('quizScoreVal').textContent = score;
        }}

        function openSolutionModal(quizOffset, qIdx) {{
            const q = QUIZZES[quizOffset].questions[qIdx];
            const modal = document.getElementById('solutionModal');
            const body = document.getElementById('solutionModalBody');

            body.innerHTML = `
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-mono font-bold text-indigo-400 block mb-1">Question ${{qIdx + 1}}:</span>
                    <p class="text-xs text-white font-semibold">${{q.q}}</p>
                </div>
                <div class="p-3 rounded-xl bg-indigo-950/40 border border-indigo-800/60">
                    <span class="text-xs font-mono font-bold text-indigo-300 block mb-1">Correct Answer:</span>
                    <p class="text-xs font-bold text-white">${{q.options[q.correct]}}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-mono font-bold text-cyan-400 block mb-1">Detailed Explanation & Reasoning:</span>
                    <p class="text-xs text-slate-300 leading-relaxed">${{q.solution}}</p>
                </div>
            `;
            modal.classList.remove('hidden');
            playTone(480, 0.1);
        }}

        function closeSolutionModal() {{
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        function prevSlide() {{
            if (currentSlide > 0) goToSlide(currentSlide - 1);
        }}

        function nextSlide() {{
            if (currentSlide < 19) goToSlide(currentSlide + 1);
        }}

        function goToSlide(idx) {{
            if (idx >= 0 && idx < 20) {{
                renderSlide(idx);
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }}
        }}

        // ==========================================
        // BESPOKE INTERACTIVE SIMULATORS (SLIDES 1-16)
        // ==========================================

        function renderSimulator(slideIdx) {{
            const vp = document.getElementById('simulatorViewport');
            const titleEl = document.getElementById('simulatorTitle');

            switch(slideIdx) {{
                case 0:
                    titleEl.textContent = "Homogeneous vs Heterogeneous Phase Matrix";
                    renderSim1(vp); break;
                case 1:
                    titleEl.textContent = "True Solution Nanoscale Sizer & Alloy Metallurgy";
                    renderSim2(vp); break;
                case 2:
                    titleEl.textContent = "Suspension Gravitational Sedimentation Lab";
                    renderSim3(vp); break;
                case 3:
                    titleEl.textContent = "Tyndall Effect & Brownian Motion Chamber";
                    renderSim4(vp); break;
                case 4:
                    titleEl.textContent = "Interactive Solution Concentration Calculator";
                    renderSim5(vp); break;
                case 5:
                    titleEl.textContent = "Solubility-Temperature Equilibrium Curves";
                    renderSim6(vp); break;
                case 6:
                    titleEl.textContent = "Sublimation Inverted Funnel Apparatus";
                    renderSim7(vp); break;
                case 7:
                    titleEl.textContent = "Centrifugation & Kathak Spin Biomechanics";
                    renderSim8(vp); break;
                case 8:
                    titleEl.textContent = "Paper Chromatography Chamber & Rf Metric";
                    renderSim9(vp); break;
                case 9:
                    titleEl.textContent = "Simple Distillation vs Kannauj Deg-Bhapka Still";
                    renderSim10(vp); break;
                case 10:
                    titleEl.textContent = "Fractional Distillation & Air Liquefaction";
                    renderSim11(vp); break;
                case 11:
                    titleEl.textContent = "Copper Sulfate Microscale Crystallisation (C-7.1)";
                    renderSim12(vp); break;
                case 12:
                    titleEl.textContent = "Municipal Water Purification Works (Alum Loading)";
                    renderSim13(vp); break;
                case 13:
                    titleEl.textContent = "Dr. Manu Prakash 125,000 RPM Paperfuge (C-8.1)";
                    renderSim14(vp); break;
                case 14:
                    titleEl.textContent = "Dr. Dilip Mahalanabis ORS & SGLT1 Transport (C-6.1)";
                    renderSim15(vp); break;
                case 15:
                    titleEl.textContent = "Artificial Blood Engineering: PFCs & HBOCs (C-7.2)";
                    renderSim16(vp); break;
                default:
                    vp.innerHTML = `<div class="text-slate-400 text-xs">Visual module active.</div>`;
            }}
        }}

        function renderQuizSimulator(slideIdx) {{
            const vp = document.getElementById('simulatorViewport');
            const titleEl = document.getElementById('simulatorTitle');
            titleEl.textContent = "Curriculum Assessment Hub";

            const quizNum = slideIdx - 15;
            vp.innerHTML = `
                <div class="w-full flex flex-col items-center justify-center p-4 text-center space-y-3">
                    <div class="w-16 h-16 rounded-2xl bg-indigo-950 border border-indigo-500/50 flex items-center justify-center text-indigo-400 shadow-xl shadow-indigo-950/50">
                        <i data-lucide="award" class="w-8 h-8"></i>
                    </div>
                    <h4 class="text-sm font-bold text-white">Quiz Challenge Module #${{quizNum}}</h4>
                    <p class="text-xs text-slate-300 leading-relaxed max-w-xs">
                        Answer all 10 in-depth chemistry questions. Use 'View Solution' for detailed step-by-step reasoning on NCERT criteria!
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 w-full text-left font-mono text-[11px] text-slate-300 space-y-1">
                        <div class="flex justify-between"><span>Curriculum Standard:</span><span class="text-indigo-400">NCERT Class 9</span></div>
                        <div class="flex justify-between"><span>Total Questions:</span><span class="text-white">10 MCQs</span></div>
                        <div class="flex justify-between"><span>Pass Standard:</span><span class="text-amber-400">80%+ Mastery</span></div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        // SIMULATOR 1: Homogeneous vs Heterogeneous Phase Comparator
        function renderSim1(vp) {{
            let mode = 'homo'; // 'homo' vs 'hetero'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim1Set('homo')" class="py-1.5 rounded-lg transition ${{mode === 'homo' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Homogeneous (Single Phase)
                            </button>
                            <button onclick="window.sim1Set('hetero')" class="py-1.5 rounded-lg transition ${{mode === 'hetero' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Heterogeneous (Distinct Phases)
                            </button>
                        </div>

                        <!-- Graphical Petri Dish / Beaker SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Beaker Outline -->
                                <rect x="55" y="20" width="140" height="110" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                                <!-- Graduation Marks -->
                                <line x1="55" y1="50" x2="68" y2="50" stroke="#64748b" stroke-width="1.5"/>
                                <line x1="55" y1="80" x2="68" y2="80" stroke="#64748b" stroke-width="1.5"/>
                                <line x1="55" y1="110" x2="68" y2="110" stroke="#64748b" stroke-width="1.5"/>

                                ${{mode === 'homo' ? `
                                    <!-- Liquid Fill (Uniform Cyan/Blue) -->
                                    <rect x="57" y="45" width="136" height="83" fill="#0369a1" opacity="0.4"/>
                                    <!-- Uniform Dissolved Na+ and Cl- Ions -->
                                    ${{[
                                        [75,60],[100,55],[130,62],[160,58],[85,80],[115,75],[145,82],[175,78],[75,100],[105,105],[135,102],[165,108]
                                    ].map(([cx,cy], i) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="4" fill="${{i % 2 === 0 ? '#38bdf8' : '#34d399'}}"/>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Uniform Salt Solution (No Boundary)</text>
                                ` : `
                                    <!-- Two Distinct Phases: Water on Top, Sand at Bottom -->
                                    <rect x="57" y="45" width="136" height="55" fill="#0369a1" opacity="0.3"/>
                                    <rect x="57" y="100" width="136" height="28" fill="#78350f" opacity="0.8"/>
                                    <!-- Separation Boundary Line -->
                                    <line x1="57" y1="100" x2="193" y2="100" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
                                    <!-- Coarse Sand Grains at Bottom -->
                                    ${{[
                                        [70,110],[90,118],[110,108],[130,115],[150,112],[170,120],[80,122],[100,125],[120,120],[140,122],[160,118],[180,110]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="3.5" fill="#d97706"/>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#f59e0b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Physical Boundary: Water (Top) & Sand (Bottom)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">Phase Count:</span><span class="${{mode === 'homo' ? 'text-indigo-400' : 'text-amber-400'}} font-bold">${{mode === 'homo' ? 'Single (1 Phase)' : 'Two or More Distinct Phases'}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Composition:</span><span class="text-slate-200">${{mode === 'homo' ? 'Uniform throughout' : 'Non-uniform distribution'}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Examples:</span><span class="text-teal-300 font-semibold">${{mode === 'homo' ? 'Sugar in water, Air, Brass' : 'Oil in water, Sand & Iron, Chalk in water'}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim1Set = function(m) {{
                mode = m;
                playTone(m === 'homo' ? 440 : 360, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 2: True Solution Particle Sizer & Alloy Metallurgy Lab
        function renderSim2(vp) {{
            let type = 'brass'; // 'liquid', 'brass', 'air'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim2Set('liquid')" class="py-1 rounded ${{type === 'liquid' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">Liquid (Iodine)</button>
                            <button onclick="window.sim2Set('brass')" class="py-1 rounded ${{type === 'brass' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Solid (Brass)</button>
                            <button onclick="window.sim2Set('air')" class="py-1 rounded ${{type === 'air' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Gas (Air)</button>
                        </div>

                        <!-- Nanoscale Molecular Window -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{type === 'brass' ? `
                                    <!-- Brass Solid Solution: 70% Cu (Orange) + 30% Zn (Blue) -->
                                    <text x="125" y="20" fill="#f59e0b" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Brass Alloy: Cu (70%) + Zn (30%)</text>
                                    ${{[
                                        [50,45,1],[80,45,0],[110,45,0],[140,45,1],[170,45,0],[200,45,0],
                                        [50,75,0],[80,75,0],[110,75,1],[140,75,0],[170,75,0],[200,75,1],
                                        [50,105,0],[80,105,1],[110,105,0],[140,105,0],[170,105,1],[200,105,0]
                                    ].map(([cx,cy,isZn]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="11" fill="${{isZn ? '#38bdf8' : '#ea580c'}}" stroke="#1e293b" stroke-width="2"/>
                                        <text x="${{cx}}" y="${{cy + 3}}" fill="#ffffff" font-size="7" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">${{isZn ? 'Zn' : 'Cu'}}</text>
                                    `).join('')}}
                                    <text x="125" y="138" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Substitutional Atomic Solid Solution</text>
                                ` : type === 'liquid' ? `
                                    <!-- Tincture of Iodine: I2 dissolved in Ethanol -->
                                    <text x="125" y="20" fill="#818cf8" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Tincture: I₂ Solute (< 1 nm) in C₂H₅OH</text>
                                    <rect x="40" y="30" width="170" height="95" rx="4" fill="#1e1b4b" stroke="#4338ca" stroke-width="1.5"/>
                                    ${{[
                                        [65,55],[120,50],[170,60],[90,80],[145,85],[80,110],[135,115],[185,105]
                                    ].map(([cx,cy]) => `
                                        <!-- I2 Diatomic Solute Molecule -->
                                        <ellipse cx="${{cx}}" cy="${{cy}}" rx="4" ry="2.5" fill="#a855f7"/>
                                        <ellipse cx="${{cx + 5}}" cy="${{cy}}" rx="4" ry="2.5" fill="#a855f7"/>
                                    `).join('')}}
                                    <text x="125" y="140" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Diatomic Solute Particles (< 1 nm)</text>
                                ` : `
                                    <!-- Atmospheric Air Gaseous Solution -->
                                    <text x="125" y="20" fill="#38bdf8" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Air: 78% N₂, 21% O₂, 0.9% Ar</text>
                                    <rect x="40" y="30" width="170" height="95" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.5"/>
                                    ${{[
                                        [60,55,'#38bdf8','N2'],[105,50,'#38bdf8','N2'],[150,60,'#f43f5e','O2'],[190,50,'#38bdf8','N2'],
                                        [80,80,'#38bdf8','N2'],[125,75,'#f43f5e','O2'],[170,85,'#38bdf8','N2'],
                                        [65,110,'#f43f5e','O2'],[110,112,'#38bdf8','N2'],[155,108,'#fbbf24','Ar'],[190,115,'#38bdf8','N2']
                                    ].map(([cx,cy,col,label]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="7" fill="${{col}}"/>
                                        <text x="${{cx}}" y="${{cy + 2.5}}" fill="#ffffff" font-size="6" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">${{label}}</text>
                                    `).join('')}}
                                    <text x="125" y="140" fill="#7dd3fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Homogeneous Gaseous Dispersion</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="text-slate-300 font-bold">Key Invariant:</span>
                            <p class="text-slate-400">In true solutions, solute particles are single molecules or ions (&lt; 1 nm), making light scattering impossible.</p>
                        </div>
                    </div>
                `;
            }}

            window.sim2Set = function(t) {{
                type = t;
                playTone(460, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 3: Suspension Gravitational Sedimentation Lab
        function renderSim3(vp) {{
            let timeMins = 0; // 0, 15, 30, 60

            function draw() {{
                const settledPercent = timeMins === 0 ? 0 : timeMins === 15 ? 40 : timeMins === 30 ? 75 : 100;
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Suspension Standing Time:</span>
                            <span class="text-amber-400 font-bold">${{timeMins}} Minutes</span>
                        </div>

                        <!-- 4 Time Buttons -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim3SetTime(0)" class="py-1 rounded ${{timeMins === 0 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">0m (Stirred)</button>
                            <button onclick="window.sim3SetTime(15)" class="py-1 rounded ${{timeMins === 15 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">15 mins</button>
                            <button onclick="window.sim3SetTime(30)" class="py-1 rounded ${{timeMins === 30 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">30 mins</button>
                            <button onclick="window.sim3SetTime(60)" class="py-1 rounded ${{timeMins === 60 ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">60 mins</button>
                        </div>

                        <!-- Beaker Sedimentation Graphic -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Beaker -->
                                <rect x="75" y="20" width="100" height="110" rx="3" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                                <!-- Liquid Base -->
                                <rect x="77" y="45" width="96" height="83" fill="#0284c7" opacity="${{timeMins === 0 ? 0.7 : timeMins === 15 ? 0.5 : timeMins === 30 ? 0.3 : 0.15}}"/>
                                
                                <!-- Floating Chalk Particles (>100 nm) -->
                                ${{timeMins === 0 ? `
                                    ${{[
                                        [90,55],[120,52],[150,60],[100,75],[135,70],[160,80],[95,95],[125,90],[155,98],[110,115],[140,118]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="3.5" fill="#f8fafc"/>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#f8fafc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Turbid: Chalk suspended throughout</text>
                                ` : timeMins === 60 ? `
                                    <!-- Clear Supernatant on Top -->
                                    <text x="125" y="65" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Clear Supernatant Water</text>
                                    <!-- Compact Sediment at Bottom -->
                                    <rect x="77" y="105" width="96" height="23" fill="#e2e8f0" opacity="0.9"/>
                                    <text x="125" y="120" fill="#0f172a" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Chalk Sediment</text>
                                ` : `
                                    <!-- Partial Settling -->
                                    <rect x="77" y="${{128 - (settledPercent / 100) * 23}}" width="96" height="${{(settledPercent / 100) * 23}}" fill="#e2e8f0" opacity="0.8"/>
                                    <circle cx="100" cy="80" r="3" fill="#f8fafc"/>
                                    <circle cx="140" cy="75" r="3" fill="#f8fafc"/>
                                    <circle cx="120" cy="95" r="3" fill="#f8fafc"/>
                                    <text x="125" y="142" fill="#cbd5e1" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Sedimentation in Progress...</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Scientific Summary -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Thermodynamic Instability:</strong> Unlike solutions, suspensions contain macroscopic particles (&gt; 100 nm) too heavy for thermal collisions to support; they inevitably settle out under gravity.
                        </div>
                    </div>
                `;
            }}

            window.sim3SetTime = function(t) {{
                timeMins = t;
                playTone(400 + t * 3, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 4: Tyndall Effect & Brownian Motion Chamber
        function renderSim4(vp) {{
            let laserOn = true;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Optics Experiment:</span>
                            <button onclick="window.sim4ToggleLaser()" class="px-3 py-1 rounded-lg font-bold transition ${{laserOn ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Laser Beam: ${{laserOn ? 'ACTIVE' : 'OFF'}}
                            </button>
                        </div>

                        <!-- 3 Cuvettes Optical Bench -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative overflow-hidden">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Laser Source on Left -->
                                <rect x="5" y="65" width="22" height="20" rx="3" fill="#334155" stroke="#64748b"/>
                                <circle cx="27" cy="75" r="3" fill="${{laserOn ? '#ef4444' : '#64748b'}}"/>

                                <!-- Cuvette 1: True Solution (CuSO4) -->
                                <rect x="45" y="35" width="55" height="80" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
                                <rect x="47" y="45" width="51" height="68" fill="#0284c7" opacity="0.3"/>
                                <text x="72" y="128" fill="#38bdf8" font-size="7" font-family="JetBrains Mono" text-anchor="middle">True Solution</text>

                                <!-- Cuvette 2: Colloid (Milk/Starch) -->
                                <rect x="115" y="35" width="55" height="80" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
                                <rect x="117" y="45" width="51" height="68" fill="#475569" opacity="0.4"/>
                                <text x="142" y="128" fill="#c084fc" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Colloid Sol</text>

                                <!-- Cuvette 3: Suspension (Chalk) -->
                                <rect x="185" y="35" width="55" height="80" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
                                <rect x="187" y="45" width="51" height="68" fill="#64748b" opacity="0.7"/>
                                <text x="212" y="128" fill="#f59e0b" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Suspension</text>

                                ${{laserOn ? `
                                    <!-- Laser Ray through True Solution (Invisible inside) -->
                                    <line x1="27" y1="75" x2="47" y2="75" stroke="#ef4444" stroke-width="2"/>
                                    <line x1="98" y1="75" x2="117" y2="75" stroke="#ef4444" stroke-width="2"/>
                                    <!-- Luminous Tyndall Cone inside Colloid (SCATTERED) -->
                                    <polygon points="117,73 168,67 168,83 117,77" fill="#f43f5e" opacity="0.65"/>
                                    <line x1="117" y1="75" x2="168" y2="75" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="2 1"/>
                                    <!-- Blocked / Diffuse in Suspension -->
                                    <line x1="168" y1="75" x2="187" y2="75" stroke="#ef4444" stroke-width="2"/>
                                    <circle cx="200" cy="75" r="12" fill="#ef4444" opacity="0.4"/>
                                    <text x="142" y="58" fill="#fecdd3" font-size="7" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Tyndall Cone</text>
                                ` : ''}}
                            </svg>
                        </div>

                        <!-- Diagnostic Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>John Tyndall (1869):</strong> Colloidal particles (1 to 100 nm) are precisely the size required to scatter visible electromagnetic light, illuminating the beam's trajectory!
                        </div>
                    </div>
                `;
            }}

            window.sim4ToggleLaser = function() {{
                laserOn = !laserOn;
                playTone(laserOn ? 620 : 310, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 5: Interactive Solution Concentration Calculator
        function renderSim5(vp) {{
            let soluteMass = 40; // grams
            let solventMass = 320; // grams

            function draw() {{
                const solutionMass = soluteMass + solventMass;
                const massPercent = ((soluteMass / solutionMass) * 100).toFixed(2);

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                            <div>
                                <label class="text-slate-400 block mb-1">Solute Salt (g): <strong class="text-white">${{soluteMass}}g</strong></label>
                                <input type="range" min="5" max="100" step="5" value="${{soluteMass}}" oninput="window.sim5SetSolute(this.value)" class="w-full accent-indigo-500">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">Solvent Water (g): <strong class="text-white">${{solventMass}}g</strong></label>
                                <input type="range" min="100" max="500" step="10" value="${{solventMass}}" oninput="window.sim5SetSolvent(this.value)" class="w-full accent-indigo-500">
                            </div>
                        </div>

                        <!-- Live Calculation Step-by-Step Box -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                            <div class="flex justify-between text-slate-400">
                                <span>1. Total Solution Mass:</span>
                                <span class="text-white font-bold">${{soluteMass}}g + ${{solventMass}}g = ${{solutionMass}}g</span>
                            </div>
                            <div class="flex justify-between text-slate-400">
                                <span>2. Mass % Formula:</span>
                                <span class="text-indigo-300">(\\text{{Mass Solute}} / \\text{{Mass Solution}}) \\times 100</span>
                            </div>
                            <div class="flex justify-between text-slate-400 pt-1 border-t border-slate-800">
                                <span>3. Calculated Concentration:</span>
                                <span class="text-base text-indigo-400 font-extrabold">${{massPercent}}\\% (w/w)</span>
                            </div>
                        </div>

                        <!-- NCERT Presets -->
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                            <button onclick="window.sim5Preset(40, 320)" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">NCERT Ex (40g/320g)</button>
                            <button onclick="window.sim5Preset(50, 200)" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">20% Standard</button>
                            <button onclick="window.sim5Preset(10, 90)" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">10% Dilute</button>
                        </div>
                    </div>
                `;
            }}

            window.sim5SetSolute = function(v) {{
                soluteMass = parseInt(v);
                draw();
            }};

            window.sim5SetSolvent = function(v) {{
                solventMass = parseInt(v);
                draw();
            }};

            window.sim5Preset = function(sol, solv) {{
                soluteMass = sol;
                solventMass = solv;
                playTone(490, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 6: Solubility-Temperature Equilibrium Curves
        function renderSim6(vp) {{
            let temp = 20; // 0 to 100°C

            function getSolubility(t) {{
                // KNO3: 13g at 0°C, 32g at 20°C, 106g at 60°C, 167g at 80°C
                const kno3 = Math.round(13 + (t * t) / 40 + t * 0.5);
                // NaCl: 35.7 at 0°C, 36.0 at 20°C, 38.0 at 80°C
                const nacl = Math.round(35.7 + t * 0.035);
                return {{ kno3, nacl }};
            }}

            function draw() {{
                const s = getSolubility(temp);
                const sCool = getSolubility(20);
                const excessCrystals = temp > 20 ? (s.kno3 - sCool.kno3) : 0;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Solution Temperature:</span>
                            <span class="text-indigo-400 font-bold text-sm">${{temp}}°C</span>
                        </div>

                        <input type="range" min="0" max="80" step="5" value="${{temp}}" oninput="window.sim6SetTemp(this.value)" class="w-full accent-indigo-500">

                        <!-- Beaker & Crystals Visualization -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Beaker -->
                                <rect x="75" y="25" width="100" height="100" rx="3" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                                <!-- Hot or Warm Liquid Glow -->
                                <rect x="77" y="45" width="96" height="78" fill="${{temp > 50 ? '#f43f5e' : temp > 25 ? '#818cf8' : '#0284c7'}}" opacity="${{0.2 + temp / 160}}"/>
                                
                                <text x="125" y="65" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">T = ${{temp}}°C</text>
                                <text x="125" y="80" fill="#a5b4fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">KNO₃ Dissolved: ${{s.kno3}}g</text>

                                ${{excessCrystals > 0 ? `
                                    <!-- Crystal precipitate if cooled from this temp down to 20°C -->
                                    <text x="125" y="105" fill="#f59e0b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Cooling to 20°C yields:</text>
                                    <text x="125" y="118" fill="#34d399" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">+${{excessCrystals}}g Crystals</text>
                                ` : `
                                    <text x="125" y="105" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Equilibrium at 20°C (32g)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Metrics Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">KNO₃ Solubility (per 100g water):</span><span class="text-emerald-400 font-bold">${{s.kno3}} g</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">NaCl Solubility (almost flat):</span><span class="text-cyan-400 font-bold">${{s.nacl}} g</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim6SetTemp = function(v) {{
                temp = parseInt(v);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 7: Sublimation Inverted Funnel Apparatus
        function renderSim7(vp) {{
            let burnerOn = false;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Bunsen Burner State:</span>
                            <button onclick="window.sim7ToggleBurner()" class="px-3 py-1 rounded-lg font-bold transition ${{burnerOn ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                Burner: ${{burnerOn ? 'HEATING ACTIVE' : 'COLD (CLICK TO HEAT)'}}
                            </button>
                        </div>

                        <!-- Sublimation Funnel SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Cotton Plug in Top Stem -->
                                <ellipse cx="125" cy="22" rx="7" ry="5" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5"/>
                                <text x="160" y="24" fill="#94a3b8" font-size="7" font-family="JetBrains Mono">Cotton Plug</text>

                                <!-- Inverted Glass Funnel -->
                                <path d="M 122 22 L 122 55 L 75 110 L 175 110 L 128 55 L 128 22 Z" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5"/>

                                <!-- China Dish -->
                                <path d="M 65 110 Q 125 125 185 110 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>

                                <!-- Mixture inside Dish (NaCl + NH4Cl) -->
                                <ellipse cx="125" cy="112" rx="45" ry="5" fill="#94a3b8"/>

                                ${{burnerOn ? `
                                    <!-- Bunsen Flame -->
                                    <polygon points="125,120 120,140 130,140" fill="#f59e0b"/>
                                    <polygon points="125,123 122,138 128,138" fill="#38bdf8"/>
                                    <!-- Rising NH4Cl Vapours -->
                                    <path d="M 115 100 Q 120 80 115 65" stroke="#ffffff" stroke-width="2" stroke-dasharray="3 2" opacity="0.8"/>
                                    <path d="M 135 100 Q 130 80 135 65" stroke="#ffffff" stroke-width="2" stroke-dasharray="3 2" opacity="0.8"/>
                                    <!-- Pure NH4Cl Sublimate on Cool Inner Walls -->
                                    <polygon points="85,100 95,85 100,90 90,105" fill="#ffffff"/>
                                    <polygon points="165,100 155,85 150,90 160,105" fill="#ffffff"/>
                                    <text x="125" y="75" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">NH₄Cl Sublimate Deposits</text>
                                ` : `
                                    <text x="125" y="138" fill="#64748b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Burner Off • Turn on to sublimate</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Phase Shift:</strong> Solid NH4Cl vaporizes without melting, condensing on cool glass as pure sublimate; non-volatile common salt remains in dish.
                        </div>
                    </div>
                `;
            }}

            window.sim7ToggleBurner = function() {{
                burnerOn = !burnerOn;
                playTone(burnerOn ? 520 : 330, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 8: Centrifugation & Kathak Spin Biomechanics (C-5.3)
        function renderSim8(vp) {{
            let mode = 'blood'; // 'blood' vs 'dance'
            let rpm = 3500;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim8SetMode('blood')" class="py-1.5 rounded-lg transition ${{mode === 'blood' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Blood Separation Centrifuge
                            </button>
                            <button onclick="window.sim8SetMode('dance')" class="py-1.5 rounded-lg transition ${{mode === 'dance' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Kathak Spin Biomechanics (C-5.3)
                            </button>
                        </div>

                        <!-- Visualization SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'blood' ? `
                                    <!-- Centrifuge Tube -->
                                    <rect x="105" y="20" width="40" height="100" rx="3" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                                    <!-- Conical tip -->
                                    <polygon points="105,120 145,120 125,138" fill="#0f172a" stroke="#475569" stroke-width="2"/>

                                    <!-- Plasma (55% Straw Yellow at Top) -->
                                    <rect x="107" y="30" width="36" height="45" fill="#facc15" opacity="0.8"/>
                                    <!-- Buffy Coat (1% White WBCs in Middle) -->
                                    <rect x="107" y="75" width="36" height="5" fill="#f8fafc"/>
                                    <!-- Dense Erythrocytes (45% Red RBCs at Bottom) -->
                                    <rect x="107" y="80" width="36" height="40" fill="#be123c"/>
                                    <polygon points="107,120 143,120 125,135" fill="#be123c"/>

                                    <text x="60" y="50" fill="#facc15" font-size="8" font-family="JetBrains Mono">Plasma (55%)</text>
                                    <text x="50" y="78" fill="#f8fafc" font-size="7" font-family="JetBrains Mono">Buffy Coat (1%)</text>
                                    <text x="60" y="105" fill="#fb7185" font-size="8" font-family="JetBrains Mono">RBC Pellet (45%)</text>
                                ` : `
                                    <!-- Kathak Dancer Pirouette Outward Inertia -->
                                    <circle cx="125" cy="35" r="10" fill="#fed7aa"/>
                                    <!-- Torso -->
                                    <rect x="120" y="45" width="10" height="30" fill="#f43f5e"/>
                                    <!-- Extended Arms -->
                                    <line x1="85" y1="52" x2="165" y2="52" stroke="#fed7aa" stroke-width="4" stroke-linecap="round"/>
                                    <!-- Flared Ghaghra Skirt expanding horizontally due to centrifugal force -->
                                    <polygon points="125,75 55,120 195,120" fill="#e11d48" opacity="0.85"/>
                                    <!-- Outward Force Vectors -->
                                    <path d="M 70 120 L 40 120" stroke="#facc15" stroke-width="2" marker-end="url(#arrow)"/>
                                    <path d="M 180 120 L 210 120" stroke="#facc15" stroke-width="2"/>
                                    <text x="125" y="140" fill="#facc15" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Outward Centrifugal Flaring (Chakkars)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-5.3 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'blood' ? 
                                '<strong>Density Gradient:</strong> Centrifugal acceleration separates dense erythrocytes (1.09 g/mL) from lighter plasma (1.025 g/mL).' : 
                                '<strong>C-5.3 Biomechanics:</strong> High-speed spinning in Kathak/Sufi turns generates outward inertial momentum identical to centrifugal separation in tubes!'}}
                        </div>
                    </div>
                `;
            }}

            window.sim8SetMode = function(m) {{
                mode = m;
                playTone(m === 'blood' ? 440 : 520, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 9: Paper Chromatography Chamber & Rf Metric
        function renderSim9(vp) {{
            let runProgress = 100; // 0 to 100%

            function draw() {{
                const solventY = 120 - (runProgress / 100) * 80; // 120 down to 40
                const yellowY = 120 - (runProgress / 100) * 65; // Rf = 0.81
                const redY = 120 - (runProgress / 100) * 45; // Rf = 0.56
                const blueY = 120 - (runProgress / 100) * 25; // Rf = 0.31

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Chromatogram Development:</span>
                            <button onclick="window.sim9Reset()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-[11px]">
                                ↺ Reset Run
                            </button>
                        </div>

                        <!-- Chromatography Chamber SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Glass Jar Container -->
                                <rect x="70" y="15" width="110" height="120" rx="4" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
                                <!-- Solvent Reservoir Pool at Bottom -->
                                <rect x="72" y="125" width="106" height="9" fill="#0284c7" opacity="0.6"/>

                                <!-- Filter Paper Strip -->
                                <rect x="105" y="25" width="40" height="105" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                                <!-- Baseline Pencil Line (Origin) -->
                                <line x1="105" y1="120" x2="145" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2 1"/>

                                <!-- Ascending Solvent Front -->
                                <line x1="105" y1="${{solventY}}" x2="145" y2="${{solventY}}" stroke="#0284c7" stroke-width="1.5"/>
                                <text x="155" y="${{solventY + 3}}" fill="#38bdf8" font-size="7" font-family="JetBrains Mono">Solvent Front</text>

                                <!-- Separated Dye Bands -->
                                <!-- Yellow Spot (Fastest) -->
                                <ellipse cx="125" cy="${{yellowY}}" rx="6" ry="3.5" fill="#facc15"/>
                                <!-- Red Spot (Medium) -->
                                <ellipse cx="125" cy="${{redY}}" rx="6" ry="3.5" fill="#f43f5e"/>
                                <!-- Blue Spot (Slowest) -->
                                <ellipse cx="125" cy="${{blueY}}" rx="6" ry="3.5" fill="#3b82f6"/>

                                <text x="90" y="${{yellowY + 3}}" fill="#facc15" font-size="7" font-family="JetBrains Mono" text-anchor="end">Rf 0.81</text>
                                <text x="90" y="${{redY + 3}}" fill="#f43f5e" font-size="7" font-family="JetBrains Mono" text-anchor="end">Rf 0.56</text>
                                <text x="90" y="${{blueY + 3}}" fill="#3b82f6" font-size="7" font-family="JetBrains Mono" text-anchor="end">Rf 0.31</text>
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="text-slate-300 font-bold block">Retention Factor Formula:</span>
                            <div class="text-indigo-400">R_f = (\\text{{Distance by Dye}}) / (\\text{{Distance by Solvent Front}})</div>
                        </div>
                    </div>
                `;
            }}

            window.sim9Reset = function() {{
                runProgress = 0;
                draw();
                let timer = setInterval(() => {{
                    runProgress += 10;
                    if (runProgress >= 100) {{
                        runProgress = 100;
                        clearInterval(timer);
                    }}
                    draw();
                }}, 100);
            }};

            draw();
        }}

        // SIMULATOR 10: Simple Distillation vs Kannauj Deg-Bhapka Still (C-6.1)
        function renderSim10(vp) {{
            let mode = 'kannauj'; // 'modern' vs 'kannauj'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim10Set('modern')" class="py-1.5 rounded-lg transition ${{mode === 'modern' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Modern Laboratory Distillation
                            </button>
                            <button onclick="window.sim10Set('kannauj')" class="py-1.5 rounded-lg transition ${{mode === 'kannauj' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Kannauj Deg-Bhapka Still (C-6.1)
                            </button>
                        </div>

                        <!-- Graphical Still SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'modern' ? `
                                    <!-- Modern Glass Distillation Flask & Liebig Condenser -->
                                    <circle cx="65" cy="95" r="25" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                                    <line x1="65" y1="70" x2="65" y2="35" stroke="#38bdf8" stroke-width="3"/>
                                    <!-- Thermometer -->
                                    <line x1="65" y1="35" x2="65" y2="75" stroke="#ef4444" stroke-width="1.5"/>
                                    <text x="65" y="25" fill="#ef4444" font-size="8" font-family="JetBrains Mono" text-anchor="middle">56°C</text>
                                    <!-- Liebig Condenser Angle -->
                                    <line x1="65" y1="45" x2="180" y2="105" stroke="#38bdf8" stroke-width="4"/>
                                    <rect x="90" y="55" width="70" height="20" rx="3" fill="#0284c7" opacity="0.3" transform="rotate(27 125 65)"/>
                                    <!-- Conical Receiver Flask -->
                                    <polygon points="180,105 165,135 205,135 190,105" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                                    <text x="185" y="145" fill="#38bdf8" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Pure Acetone</text>
                                ` : `
                                    <!-- Traditional Copper Deg-Bhapka of Kannauj -->
                                    <!-- Copper Deg Still over Hearth -->
                                    <path d="M 35 125 Q 25 75 60 70 L 60 55 L 75 55 L 75 70 Q 110 75 100 125 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
                                    <!-- Clay Multani Mitti Seal -->
                                    <rect x="58" y="52" width="19" height="6" fill="#78350f" rx="2"/>
                                    <text x="67" y="45" fill="#f59e0b" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Deg (Copper Still)</text>

                                    <!-- Bamboo Chonga Pipe -->
                                    <path d="M 67 52 Q 130 20 180 85" fill="none" stroke="#84cc16" stroke-width="3"/>

                                    <!-- Cold Water Tank (Gaddi) -->
                                    <rect x="150" y="70" width="80" height="65" rx="3" fill="#0369a1" opacity="0.4" stroke="#38bdf8"/>
                                    <!-- Copper Bhapka Receiver inside Tank -->
                                    <ellipse cx="190" cy="110" rx="18" ry="20" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
                                    <text x="190" y="145" fill="#38bdf8" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Bhapka in Water Tank</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-6.1 Culture Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'modern' ? 
                                '<strong>Simple Distillation:</strong> Efficient when miscible liquids differ in boiling point by &gt; 25°C (e.g. Acetone 56°C & Water 100°C).' : 
                                '<strong>C-6.1 Kannauj Heritage:</strong> Over 1,000 years of artisan hydro-distillation without electricity, using copper *Deg*, clay seal, bamboo *Chonga*, and water-submerged *Bhapka*!'}}
                        </div>
                    </div>
                `;
            }}

            window.sim10Set = function(m) {{
                mode = m;
                playTone(m === 'modern' ? 480 : 540, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 11: Fractional Distillation & Air Liquefaction
        function renderSim11(vp) {{
            let mode = 'air'; // 'air' vs 'column'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim11Set('air')" class="py-1.5 rounded-lg transition ${{mode === 'air' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Atmospheric Air Separation
                            </button>
                            <button onclick="window.sim11Set('column')" class="py-1.5 rounded-lg transition ${{mode === 'column' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Packed Column Glass Beads
                            </button>
                        </div>

                        <!-- Graphic Window -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'air' ? `
                                    <!-- Air Liquefaction Tall Fractionator -->
                                    <rect x="75" y="15" width="100" height="120" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                                    <!-- Temperature Gradient Lines -->
                                    <!-- Top: Nitrogen -196°C -->
                                    <rect x="77" y="17" width="96" height="30" fill="#0284c7" opacity="0.3"/>
                                    <text x="125" y="32" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">↑ N₂ Gas (-196°C / 77K)</text>

                                    <!-- Middle: Argon -186°C -->
                                    <rect x="77" y="47" width="96" height="35" fill="#f59e0b" opacity="0.2"/>
                                    <text x="125" y="67" fill="#fbbf24" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">→ Argon Gas (-186°C / 87K)</text>

                                    <!-- Bottom: Liquid Oxygen -183°C -->
                                    <rect x="77" y="82" width="96" height="51" fill="#e11d48" opacity="0.3"/>
                                    <text x="125" y="112" fill="#fb7185" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">↓ Liquid O₂ (-183°C / 90K)</text>
                                ` : `
                                    <!-- Fractionating Column with Glass Beads -->
                                    <rect x="100" y="20" width="50" height="110" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
                                    <!-- Packed Glass Beads -->
                                    ${{[
                                        [112,35],[138,35],[125,50],[112,65],[138,65],[125,80],[112,95],[138,95],[125,110]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="7" fill="#6366f1" opacity="0.5" stroke="#c7d2fe"/>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#c7d2fe" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Glass Beads: Enormous Surface Area</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Criterion:</strong> Used when boiling point difference is &lt; 25°C. Glass beads cause continuous condensation-vaporization cycles.
                        </div>
                    </div>
                `;
            }}

            window.sim11Set = function(m) {{
                mode = m;
                playTone(m === 'air' ? 520 : 460, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 12: Copper Sulfate Microscale Crystallisation (C-7.1)
        function renderSim12(vp) {{
            let mode = 'micro'; // 'micro' vs 'bulk'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim12Set('micro')" class="py-1.5 rounded-lg transition ${{mode === 'micro' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Microscale Green Lab (C-7.1)
                            </button>
                            <button onclick="window.sim12Set('bulk')" class="py-1.5 rounded-lg transition ${{mode === 'bulk' ? 'bg-rose-900 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Bulk Evaporation (Charred/Impure)
                            </button>
                        </div>

                        <!-- Graphic Window -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'micro' ? `
                                    <!-- Microscale Well Slide with Pure Blue Crystals -->
                                    <rect x="40" y="35" width="170" height="80" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                                    <circle cx="125" cy="75" r="28" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                                    <!-- Perfect Triclinic Blue Vitriol Crystals -->
                                    <polygon points="115,60 135,55 140,75 120,80" fill="#2563eb" stroke="#60a5fa" stroke-width="1.5"/>
                                    <polygon points="105,75 125,70 130,90 110,95" fill="#1d4ed8" stroke="#93c5fd" stroke-width="1.5"/>
                                    <polygon points="125,78 145,72 150,92 130,98" fill="#3b82f6" stroke="#bfdbfe" stroke-width="1.5"/>
                                    <text x="125" y="130" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Pure CuSO₄·5H₂O Crystals (Zero Waste)</text>
                                ` : `
                                    <!-- Bulk Charred Dirty Crust -->
                                    <path d="M 55 105 Q 125 125 195 105 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                                    <ellipse cx="125" cy="108" rx="55" ry="8" fill="#451a03"/>
                                    <circle cx="110" cy="108" r="3" fill="#000000"/>
                                    <circle cx="140" cy="106" r="3" fill="#000000"/>
                                    <text x="125" y="70" fill="#ef4444" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Evaporated to Dryness:</text>
                                    <text x="125" y="85" fill="#fca5a5" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Charred & Trapped Soluble Impurities</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-7.1 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>C-7.1 Green Chemistry:</strong> Microscale crystallization uses milligrams instead of hundreds of grams, producing pure blue vitriol without toxic chemical effluents!
                        </div>
                    </div>
                `;
            }}

            window.sim12Set = function(m) {{
                mode = m;
                playTone(m === 'micro' ? 560 : 320, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 13: Municipal Water Purification Works (Alum Loading) (C-5.2)
        function renderSim13(vp) {{
            let stage = 2; // 1: Sedimentation, 2: Alum Loading, 3: Filtration, 4: Chlorination
            const stages = [
                {{ title: "Stage 1: Sedimentation Tank", desc: "Coarse sand and heavy particles settle gravitationally over time." }},
                {{ title: "Stage 2: Alum Loading Tank", desc: "Trivalent Al³⁺ from potash alum neutralizes colloidal clay charges; flocs settle rapidly!" }},
                {{ title: "Stage 3: Multi-tier Sand Filter", desc: "Successive layers of fine sand, coarse sand, and gravel filter remaining particulates." }},
                {{ title: "Stage 4: Chlorination Tank", desc: "Chlorine gas eliminates harmful bacterial and viral pathogens before public supply." }}
            ];

            function draw() {{
                const cur = stages[stage - 1];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Municipal Water Works:</span>
                            <span class="text-indigo-400 font-bold">Stage ${{stage}} of 4</span>
                        </div>

                        <!-- 4 Stage Selector Buttons -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            ${{[1,2,3,4].map(s => `
                                <button onclick="window.sim13SetStage(${{s}})" class="py-1 rounded ${{stage === s ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    Stage ${{s}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Animated Process SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{stage === 1 ? `
                                    <!-- Sedimentation Tank -->
                                    <rect x="50" y="30" width="150" height="90" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                                    <rect x="52" y="45" width="146" height="60" fill="#0284c7" opacity="0.3"/>
                                    <rect x="52" y="105" width="146" height="13" fill="#78350f"/>
                                    <text x="125" y="75" fill="#f8fafc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Heavy Silt Settling Under Gravity</text>
                                ` : stage === 2 ? `
                                    <!-- Alum Loading Tank -->
                                    <rect x="50" y="30" width="150" height="90" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="2"/>
                                    <!-- Suspended Clay Flocs Agglomerating with Al3+ -->
                                    <circle cx="85" cy="65" r="5" fill="#f59e0b"/>
                                    <circle cx="115" cy="75" r="7" fill="#f59e0b"/>
                                    <circle cx="155" cy="70" r="6" fill="#f59e0b"/>
                                    <!-- Settled Flocs at bottom -->
                                    <rect x="52" y="108" width="146" height="10" fill="#d97706" opacity="0.8"/>
                                    <text x="125" y="45" fill="#a5b4fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Al³⁺ Neutralizes Clay Charges</text>
                                    <text x="125" y="98" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Agglomerated Flocs Settle Fast</text>
                                ` : stage === 3 ? `
                                    <!-- Filtration Tank Layers -->
                                    <rect x="50" y="30" width="150" height="90" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                                    <rect x="52" y="45" width="146" height="20" fill="#fef08a" opacity="0.6"/>
                                    <text x="125" y="58" fill="#713f12" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Fine Sand Layer</text>
                                    <rect x="52" y="65" width="146" height="25" fill="#d97706" opacity="0.7"/>
                                    <text x="125" y="80" fill="#ffffff" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Coarse Sand Layer</text>
                                    <rect x="52" y="90" width="146" height="28" fill="#64748b" opacity="0.8"/>
                                    <text x="125" y="107" fill="#f8fafc" font-size="7" font-family="JetBrains Mono" text-anchor="middle">Gravel Support Layer</text>
                                ` : `
                                    <!-- Chlorination -->
                                    <rect x="50" y="30" width="150" height="90" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                                    <rect x="52" y="45" width="146" height="73" fill="#10b981" opacity="0.25"/>
                                    <text x="125" y="65" fill="#34d399" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Chlorine (Cl₂) Injection</text>
                                    <text x="125" y="85" fill="#d1fae5" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Destroys 99.9% of Pathogens</text>
                                    <text x="125" y="105" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Potable Safe Drinking Water</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="text-indigo-400 font-bold">${{cur.title}}</span>
                            <p class="text-slate-300">${{cur.desc}}</p>
                        </div>
                    </div>
                `;
            }}

            window.sim13SetStage = function(s) {{
                stage = s;
                playTone(450 + s * 30, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 14: Dr. Manu Prakash 125,000 RPM Paperfuge (C-8.1)
        function renderSim14(vp) {{
            let spinning = false;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Manu Prakash Whirligig (C-8.1):</span>
                            <button onclick="window.sim14ToggleSpin()" class="px-3 py-1 rounded-lg font-bold transition ${{spinning ? 'bg-indigo-600 text-white animate-pulse' : 'bg-slate-800 text-slate-400'}}">
                                ${{spinning ? 'PULLING STRINGS (125,000 RPM)' : 'PULL STRINGS TO SPIN'}}
                            </button>
                        </div>

                        <!-- Paperfuge Disc Graphic -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Braided Twisted Strings -->
                                <line x1="20" y1="75" x2="95" y2="75" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="${{spinning ? '1 1' : 'none'}}"/>
                                <line x1="155" y1="75" x2="230" y2="75" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="${{spinning ? '1 1' : 'none'}}"/>

                                <!-- Central Paper Disc -->
                                <circle cx="125" cy="75" r="32" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
                                <!-- Central Two Holes -->
                                <circle cx="120" cy="75" r="2.5" fill="#0f172a"/>
                                <circle cx="130" cy="75" r="2.5" fill="#0f172a"/>

                                <!-- Radial Capillary Tube mounted on Disc -->
                                <rect x="100" y="73" width="50" height="4" rx="2" fill="#38bdf8" opacity="0.8"/>
                                ${{spinning ? `
                                    <!-- Blood Separation occurring under 30,000 g -->
                                    <rect x="100" y="73" width="22" height="4" fill="#facc15"/>
                                    <rect x="122" y="73" width="28" height="4" fill="#be123c"/>
                                    <text x="125" y="32" fill="#38bdf8" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">125,000 RPM • 30,000 g</text>
                                    <text x="125" y="128" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Plasma separated in 90 seconds!</text>
                                ` : `
                                    <text x="125" y="32" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Cost: ~20 Cents • Zero Electricity</text>
                                    <text x="125" y="128" fill="#64748b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Click button to spin whirligig</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-8.1 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Frugal Science:</strong> Stanford bioengineer Dr. Manu Prakash designed a 20-cent paper centrifuge that achieves $30,000\\ g$ acceleration, diagnosing malaria in off-grid clinics!
                        </div>
                    </div>
                `;
            }}

            window.sim14ToggleSpin = function() {{
                spinning = !spinning;
                playTone(spinning ? 700 : 350, 0.15);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 15: Dr. Dilip Mahalanabis ORS & SGLT1 Transport (C-6.1)
        function renderSim15(vp) {{
            let orsActive = true;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Dr. Dilip Mahalanabis ORS (C-6.1):</span>
                            <button onclick="window.sim15Toggle()" class="px-3 py-1 rounded-lg font-bold transition ${{orsActive ? 'bg-emerald-600 text-white' : 'bg-rose-900 text-white'}}">
                                Oral Rehydration: ${{orsActive ? 'ACTIVE (SGLT1 ON)' : 'NO ORS (CHOLERA LEAK)'}}
                            </button>
                        </div>

                        <!-- Intestinal Epithelial SGLT1 Co-Transport SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Intestinal Lumen (Left) and Blood Capillary (Right) -->
                                <rect x="20" y="20" width="85" height="110" fill="#0f172a" stroke="#334155"/>
                                <text x="62" y="35" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Intestinal Lumen</text>

                                <!-- Cell Membrane Epithelium (Middle) -->
                                <rect x="105" y="20" width="40" height="110" fill="#312e81" stroke="#6366f1"/>
                                <!-- SGLT1 Protein Channel -->
                                <rect x="110" y="60" width="30" height="30" rx="4" fill="#10b981" stroke="#34d399"/>
                                <text x="125" y="78" fill="#ffffff" font-size="7" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">SGLT1</text>

                                <!-- Blood Vessel (Right) -->
                                <rect x="145" y="20" width="85" height="110" fill="#881337" opacity="0.3" stroke="#f43f5e"/>
                                <text x="187" y="35" fill="#fb7185" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Blood Stream</text>

                                ${{orsActive ? `
                                    <!-- Co-Transport of Na+ and Glucose into Blood -->
                                    <circle cx="55" cy="65" r="4" fill="#38bdf8"/>
                                    <text x="55" y="68" fill="#ffffff" font-size="6" font-family="JetBrains Mono" text-anchor="middle">Na+</text>
                                    <rect x="70" y="62" width="8" height="8" rx="2" fill="#fbbf24"/>
                                    <text x="74" y="68" fill="#000000" font-size="5" font-family="JetBrains Mono" text-anchor="middle">G</text>
                                    <!-- Flow through SGLT1 pulling Water -->
                                    <path d="M 85 75 L 170 75" stroke="#34d399" stroke-width="2" stroke-dasharray="3 2"/>
                                    <text x="187" y="78" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">+H₂O Osmosis!</text>
                                    <text x="125" y="142" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Cholera Mortality Slashed: 30% → 3.6%</text>
                                ` : `
                                    <!-- Dehydration Fluid Loss -->
                                    <path d="M 170 75 L 85 75" stroke="#ef4444" stroke-width="2"/>
                                    <text x="125" y="142" fill="#ef4444" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Severe Fluid Loss & Shock</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-6.1 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Dr. Dilip Mahalanabis (1934–2022):</strong> Formulated homogeneous solution chemistry (3.5g NaCl + 2.5g NaHCO3 + 1.5g KCl + 20g Glucose in 1L water), saving over 50 million lives!
                        </div>
                    </div>
                `;
            }}

            window.sim15Toggle = function() {{
                orsActive = !orsActive;
                playTone(orsActive ? 600 : 290, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 16: Artificial Blood Engineering: PFCs & HBOCs (C-7.2)
        function renderSim16(vp) {{
            let cand = 'pfc'; // 'pfc', 'hboc', 'natural'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim16Set('natural')" class="py-1 rounded ${{cand === 'natural' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Natural Blood</button>
                            <button onclick="window.sim16Set('pfc')" class="py-1 rounded ${{cand === 'pfc' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">PFC Emulsion</button>
                            <button onclick="window.sim16Set('hboc')" class="py-1 rounded ${{cand === 'hboc' ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}}">HBOC Carriers</button>
                        </div>

                        <!-- Microcapillary Fluid Viewport -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Capillary Walls -->
                                <line x1="20" y1="40" x2="230" y2="40" stroke="#f43f5e" stroke-width="3"/>
                                <line x1="20" y1="110" x2="230" y2="110" stroke="#f43f5e" stroke-width="3"/>

                                ${{cand === 'natural' ? `
                                    <!-- Flexible Biconcave RBCs in Plasma -->
                                    <ellipse cx="60" cy="75" rx="14" ry="9" fill="#be123c"/>
                                    <ellipse cx="125" cy="75" rx="14" ry="9" fill="#be123c"/>
                                    <ellipse cx="190" cy="75" rx="14" ry="9" fill="#be123c"/>
                                    <!-- Platelets -->
                                    <circle cx="95" cy="60" r="3" fill="#fbbf24"/>
                                    <text x="125" y="130" fill="#fb7185" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Natural Blood: O₂ + Clotting + Immunity</text>
                                ` : cand === 'pfc' ? `
                                    <!-- Perfluorocarbon Micro-Emulsion -->
                                    ${{[
                                        [50,65],[80,85],[110,60],[140,85],[170,65],[200,80]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="6" fill="#06b6d4" stroke="#67e8f9" stroke-width="1.5"/>
                                        <circle cx="${{cx + 2}}" cy="${{cy - 2}}" r="2" fill="#ffffff"/>
                                    `).join('')}}
                                    <text x="125" y="130" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">PFCs: 50x O₂ solubility; zero clotting</text>
                                ` : `
                                    <!-- Polymerized Hemoglobin Chains -->
                                    <circle cx="70" cy="75" r="5" fill="#881337"/>
                                    <circle cx="80" cy="75" r="5" fill="#881337"/>
                                    <circle cx="120" cy="75" r="5" fill="#881337"/>
                                    <circle cx="130" cy="75" r="5" fill="#881337"/>
                                    <circle cx="170" cy="75" r="5" fill="#881337"/>
                                    <circle cx="180" cy="75" r="5" fill="#881337"/>
                                    <text x="125" y="130" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">HBOC: O₂ Carrier, but scavenges arterial NO</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-7.2 Open Scientific Question -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>C-7.2 Scientific Frontier:</strong> Can artificial blood work universally? While PFCs transport $O_2$, they lack clotting platelets, immune leukocytes, and nitric oxide buffering!
                        </div>
                    </div>
                `;
            }}

            window.sim16Set = function(c) {{
                cand = c;
                playTone(c === 'natural' ? 440 : c === 'pfc' ? 520 : 480, 0.08);
                draw();
            }};

            draw();
        }}

        // Initialize on Load
        document.addEventListener('DOMContentLoaded', () => {{
            renderSlide(0);
        }});
    </script>
</body>
</html>
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_code)

    print(f"Successfully generated {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH)} bytes).")

if __name__ == "__main__":
    generate_html()
