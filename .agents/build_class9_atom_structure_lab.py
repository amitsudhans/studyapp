# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 6
STRUCTURE OF AN ATOM
Subatomic Particles, Thomson, Rutherford, Bohr Models, Bohr-Bury Rules,
First 18 Elements, Valency, Atomic & Mass Numbers, Isotopes, Isobars, Dr. Homi Bhabha & Quantum Clouds
Syllabus Competencies: C-1.1, C-1.3, C-5.1, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
Generates public/animations/class9-structure-of-atom.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_atom_structure_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-structure-of-atom.html"

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
    <title>NCERT Class 9 Science • Chapter 6: Structure of an Atom Laboratory</title>
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
            0%, 100% {{ box-shadow: 0 0 15px rgba(168, 85, 247, 0.2); }}
            50% {{ box-shadow: 0 0 25px rgba(168, 85, 247, 0.45); }}
        }}
        .pulse-border {{
            animation: pulseGlow 2.5s infinite;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-purple-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="glass-panel sticky top-0 z-40 border-b border-slate-800/80 px-4 py-2.5 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-purple-600 via-indigo-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-purple-950/40 border border-purple-400/30">
                <i data-lucide="atom" class="w-5 h-5 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold tracking-wider uppercase px-2 py-0.5 rounded bg-purple-950/80 text-purple-400 border border-purple-800/60 font-mono">
                        NCERT Class 9 Science • Chapter 6
                    </span>
                    <span class="hidden sm:inline-block text-[11px] font-medium text-slate-400">• Atomic Physics & Chemistry</span>
                </div>
                <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-1.5">
                    Structure of an Atom: Models, Configurations & Nuclear Isotopes
                </h1>
            </div>
        </div>

        <!-- Slide Selector & Nav Controls -->
        <div class="flex items-center gap-2 sm:gap-3">
            <div class="relative">
                <button onclick="window.toggleSlideMenu()" id="slideMenuBtn" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700/70 hover:bg-slate-800 text-xs font-semibold text-slate-200 transition">
                    <i data-lucide="compass" class="w-3.5 h-3.5 text-purple-400"></i>
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
                <button onclick="window.toggleSpeech()" id="speechBtn" title="Play Voiceover Narration" class="w-8 h-8 rounded-md bg-purple-600 hover:bg-purple-500 text-white flex items-center justify-center transition">
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
            <div class="glass-panel rounded-2xl p-4 border border-slate-800/80 shadow-xl relative overflow-hidden bg-gradient-to-r from-slate-900/95 via-slate-900/80 to-purple-950/20">
                <div class="flex items-center gap-3.5">
                    <!-- SVG Talking Avatar (Prof. Sophia) -->
                    <div class="relative w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-b from-purple-600 to-indigo-800 p-0.5 shadow-md shrink-0">
                        <svg viewBox="0 0 100 100" class="w-full h-full rounded-[14px] bg-slate-900 overflow-hidden">
                            <rect width="100" height="100" fill="#1e102a"/>
                            <circle cx="50" cy="50" r="42" fill="#581c87" opacity="0.4"/>
                            <!-- Torso / Lab Coat -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#334155"/>
                            <path d="M35,90 L50,100 L65,90 L60,82 L50,86 L40,82 Z" fill="#9333ea"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="46" rx="22" ry="26" fill="#fed7aa"/>
                            <!-- Hair -->
                            <path d="M26,42 Q28,18 50,18 Q72,18 74,42 Q68,26 50,26 Q32,26 26,42 Z" fill="#374151"/>
                            <path d="M26,42 Q24,60 28,68 Q32,56 32,46 Z" fill="#374151"/>
                            <path d="M74,42 Q76,60 72,68 Q68,56 68,46 Z" fill="#374151"/>
                            <!-- Glasses -->
                            <rect x="33" y="40" width="13" height="8" rx="2" fill="none" stroke="#7e22ce" stroke-width="2"/>
                            <rect x="54" y="40" width="13" height="8" rx="2" fill="none" stroke="#7e22ce" stroke-width="2"/>
                            <line x1="46" y1="44" x2="54" y2="44" stroke="#7e22ce" stroke-width="2"/>
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
                        <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded text-[9px] font-bold bg-purple-500 text-white font-mono shadow">
                            TEACHER
                        </div>
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between gap-2">
                            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider font-mono">Prof. Sophia • Voice Guide</span>
                            <span id="speechStatusIndicator" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Ready</span>
                        </div>
                        <p id="narrationText" class="text-xs text-slate-300 mt-1 line-clamp-3 leading-relaxed italic">
                            Welcome students! Today we enter the quantum heart of matter—journeying from Acharya Kanad’s ancient Parmanu to subatomic particles, atomic models, and modern nuclear energy.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Content Presentation Slide (Slides 1 to 16) -->
            <div id="contentSlideContainer" class="space-y-4">
                <!-- Slide Header Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between">
                        <span id="slideCategoryText" class="text-[11px] font-bold text-purple-400 uppercase tracking-widest font-mono">Section Core Theory</span>
                        <span id="slideBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-purple-950/80 text-purple-300 border border-purple-800/60 font-mono">
                            Part 1 of 20
                        </span>
                    </div>
                    <div>
                        <h2 id="slideTitle" class="text-lg sm:text-xl font-extrabold text-white tracking-tight">Historical Foundations: Acharya Kanad’s Parmanu to Subatomic Discoveries</h2>
                        <p id="slideSubtitle" class="text-xs sm:text-sm font-medium text-purple-400/90 mt-0.5">From Ancient Indivisibility Philosophies to the Cleavage of the Atom</p>
                    </div>
                    <ul id="slideKeyPoints" class="text-xs sm:text-sm text-slate-300 space-y-2 pt-1 border-t border-slate-800/80 leading-relaxed">
                        <!-- Injected via JavaScript -->
                    </ul>
                </div>

                <!-- Checkpoints Container -->
                <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check-circle" class="w-4 h-4 text-purple-400"></i>
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
                        <div class="w-7 h-7 rounded-lg bg-purple-950 border border-purple-700/60 flex items-center justify-center text-purple-400">
                            <i data-lucide="award" class="w-4 h-4"></i>
                        </div>
                        <div>
                            <h3 id="quizTitleDisplay" class="text-sm font-extrabold text-white">Mastery Assessment</h3>
                            <p class="text-[11px] text-slate-400">10 Comprehensive Questions with Step-by-Step Solutions</p>
                        </div>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-mono font-bold text-purple-400">Score: <span id="quizScoreVal">0</span> / 10</span>
                    </div>
                </div>

                <div id="quizQuestionsList" class="space-y-4">
                    <!-- Injected via JavaScript -->
                </div>
            </div>

            <!-- Slide 20 Last Slide Notice -->
            <div id="lastSlideNotice" class="hidden glass-panel rounded-2xl p-6 text-center border-2 border-purple-500/40 bg-gradient-to-r from-purple-950/40 via-slate-900 to-indigo-950/40 shadow-xl shadow-purple-950/30">
                <div class="w-12 h-12 rounded-full bg-purple-500/20 text-purple-400 border border-purple-500/40 flex items-center justify-center mx-auto mb-2">
                    <i data-lucide="check-check" class="w-6 h-6"></i>
                </div>
                <h4 class="text-lg font-bold text-white">Curriculum Chapter Mastered!</h4>
                <p class="text-base sm:text-lg text-purple-300 font-semibold mt-1">You have reached the last slide of this chapter</p>
                <p class="text-xs text-slate-400 mt-2 max-w-md mx-auto">
                    You have comprehensively mastered Subatomic Particles, Thomson, Rutherford & Bohr Models, Bohr-Bury Shell Distributions, First 18 Elements, Valency, Atomic/Mass Numbers, Isotopes, Isobars, Dr. Homi Bhabha’s Thorium Vision, and Quantum Cloud Frontiers!
                </p>
            </div>

        </div>

        <!-- Right Column: Interactive Bespoke SVG Simulators (5 cols) -->
        <div class="lg:col-span-5 flex flex-col gap-4 sticky top-20">
            <div class="glass-panel rounded-2xl p-4 sm:p-5 border border-slate-800 shadow-2xl flex flex-col gap-3">
                <div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
                    <div class="flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4 text-purple-400"></i>
                        <h3 id="simulatorTitle" class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">
                            Interactive Visual Laboratory
                        </h3>
                    </div>
                    <span id="simulatorBadge" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-indigo-400 border border-slate-700">
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
                    <span class="text-slate-400 block text-[10px]">Particles</span>
                    <span class="font-bold text-purple-400 font-mono">e⁻, p⁺, n⁰</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Models</span>
                    <span class="font-bold text-indigo-400 font-mono">3 Classical</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Elements</span>
                    <span class="font-bold text-cyan-400 font-mono">1 to 18</span>
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

            <button onclick="window.nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-purple-950/40 transition">
                <span>Next Slide</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </div>
    </footer>

    <!-- Step-by-Step Solution Pop-up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <div class="glass-panel w-full max-w-lg rounded-2xl border border-purple-500/50 p-6 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2 text-purple-400 font-bold text-sm">
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
                <button onclick="window.closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition">
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
                btn.className = `w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between transition ${{idx === currentSlide ? 'bg-purple-950/80 text-purple-300 font-bold border border-purple-700/50' : 'text-slate-300 hover:bg-slate-800/80'}}`;
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
                dot.className = `h-2 rounded-full transition-all ${{idx === currentSlide ? 'w-6 bg-purple-500' : 'w-2 bg-slate-700 hover:bg-slate-500'}}`;
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
                indicator.className = 'text-[10px] font-mono px-2 py-0.5 rounded bg-purple-950 text-purple-400 border border-purple-800 animate-pulse';
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
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-400 mt-2 shrink-0"></span>
                        <span>${{pt}}</span>
                    </li>
                `).join('');

                // Checkpoints List (2 per slide)
                const cpList = document.getElementById('checkpointsList');
                cpList.innerHTML = data.checkpoints.map((cp, cpIdx) => `
                    <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/80 space-y-2.5">
                        <div class="flex items-start justify-between gap-2">
                            <span class="text-xs font-semibold text-slate-200">
                                <span class="text-purple-400 font-mono font-bold mr-1.5">Q${{cpIdx + 1}}.</span>
                                ${{cp.q}}
                            </span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                            ${{cp.options.map((opt, optIdx) => `
                                <button onclick="window.checkAnswer(${{idx}}, ${{cpIdx}}, ${{optIdx}})" 
                                        id="cp-btn-${{idx}}-${{cpIdx}}-${{optIdx}}"
                                        class="text-left px-3 py-2 rounded-lg text-xs font-medium bg-slate-950 border border-slate-800 hover:border-purple-600/60 hover:bg-slate-800/60 transition flex items-center justify-between">
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
                                <span class="text-purple-400 font-mono font-bold mr-1">Q${{qIdx + 1}}.</span>
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
                                        class="text-left px-3 py-2 rounded-lg text-xs bg-slate-950 border border-slate-800 hover:border-purple-500/60 transition flex items-center justify-between">
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
                btn.classList.remove('bg-purple-950', 'border-purple-500', 'text-purple-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === cp.correct) {{
                    btn.classList.add('bg-purple-950/80', 'border-purple-500', 'text-purple-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-purple-950/60', 'text-purple-300', 'border-purple-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-purple-950/60', 'text-purple-300', 'border', 'border-purple-800/80');
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
                btn.classList.remove('bg-purple-950', 'border-purple-500', 'text-purple-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === q.correct) {{
                    btn.classList.add('bg-purple-950/80', 'border-purple-500', 'text-purple-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-purple-950/60', 'text-purple-300', 'border-purple-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-purple-950/60', 'text-purple-300', 'border', 'border-purple-800/80');
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
                    <span class="text-xs font-mono font-bold text-purple-400 block mb-1">Question ${{qIdx + 1}}:</span>
                    <p class="text-xs text-white font-semibold">${{q.q}}</p>
                </div>
                <div class="p-3 rounded-xl bg-purple-950/40 border border-purple-800/60">
                    <span class="text-xs font-mono font-bold text-purple-300 block mb-1">Correct Answer:</span>
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
                    titleEl.textContent = "Acharya Kanad's Parmanu Division Timeline";
                    renderSim1(vp); break;
                case 1:
                    titleEl.textContent = "Subatomic Particle Triad Comparator";
                    renderSim2(vp); break;
                case 2:
                    titleEl.textContent = "J.J. Thomson Watermelon / Plum Pudding Model";
                    renderSim3(vp); break;
                case 3:
                    titleEl.textContent = "Rutherford Alpha Scattering Gold Foil Chamber";
                    renderSim4(vp); break;
                case 4:
                    titleEl.textContent = "Nuclear Atom vs Maxwell Spiral Collapse Paradox";
                    renderSim5(vp); break;
                case 5:
                    titleEl.textContent = "Bohr Stationary Orbits & Quantum Jump Emission";
                    renderSim6(vp); break;
                case 6:
                    titleEl.textContent = "Bohr-Bury 2n² Shell Capacity & Octet Ceiling";
                    renderSim7(vp); break;
                case 7:
                    titleEl.textContent = "First 18 Elements Interactive Shell Configurator";
                    renderSim8(vp); break;
                case 8:
                    titleEl.textContent = "Valency & Combining Capacity Engine";
                    renderSim9(vp); break;
                case 9:
                    titleEl.textContent = "Atomic Notation & Subatomic Particle Counter";
                    renderSim10(vp); break;
                case 10:
                    titleEl.textContent = "Hydrogen Isotopes Triad: Protium, Deuterium, Tritium";
                    renderSim11(vp); break;
                case 11:
                    titleEl.textContent = "Chlorine Fractional Atomic Mass (35.5 u) Lab";
                    renderSim12(vp); break;
                case 12:
                    titleEl.textContent = "Societal Radioisotopes: Medicine & Energy (C-5.3)";
                    renderSim13(vp); break;
                case 13:
                    titleEl.textContent = "Isobars vs Isotopes Diagnostic Bench";
                    renderSim14(vp); break;
                case 14:
                    titleEl.textContent = "Dr. Homi J. Bhabha & India's 3-Stage Nuclear Plan (C-5.2)";
                    renderSim15(vp); break;
                case 15:
                    titleEl.textContent = "Quantum Orbital Clouds & Quark Substructure (C-7.2)";
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
                    <div class="w-16 h-16 rounded-2xl bg-purple-950 border border-purple-500/50 flex items-center justify-center text-purple-400 shadow-xl shadow-purple-950/50">
                        <i data-lucide="award" class="w-8 h-8"></i>
                    </div>
                    <h4 class="text-sm font-bold text-white">Quiz Challenge Module #${{quizNum}}</h4>
                    <p class="text-xs text-slate-300 leading-relaxed max-w-xs">
                        Answer all 10 in-depth atomic physics questions. Use 'View Solution' for detailed step-by-step reasoning on NCERT criteria!
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 w-full text-left font-mono text-[11px] text-slate-300 space-y-1">
                        <div class="flex justify-between"><span>Curriculum Standard:</span><span class="text-purple-400">NCERT Class 9</span></div>
                        <div class="flex justify-between"><span>Total Questions:</span><span class="text-white">10 MCQs</span></div>
                        <div class="flex justify-between"><span>Pass Standard:</span><span class="text-amber-400">80%+ Mastery</span></div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        // SIMULATOR 1: Acharya Kanad's Parmanu Division Timeline (C-6.1)
        function renderSim1(vp) {{
            let step = 1; // 1: Grain, 2: Micro-Speck, 3: Parmanu (Kanad), 4: Subatomic (Thomson/Rutherford)

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Subdivision Stage:</span>
                            <span class="text-purple-400 font-bold">Stage ${{step}} of 4</span>
                        </div>

                        <!-- 4 Step Buttons -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim1Set(1)" class="py-1 rounded ${{step === 1 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">1. Grain</button>
                            <button onclick="window.sim1Set(2)" class="py-1 rounded ${{step === 2 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">2. Micro-dust</button>
                            <button onclick="window.sim1Set(3)" class="py-1 rounded ${{step === 3 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">3. Parmanu</button>
                            <button onclick="window.sim1Set(4)" class="py-1 rounded ${{step === 4 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">4. Subatomic</button>
                        </div>

                        <!-- Graphical Canvas -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{step === 1 ? `
                                    <!-- Visible Grain of Rice / Mustard -->
                                    <ellipse cx="125" cy="75" rx="55" ry="32" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>
                                    <text x="125" y="78" fill="#713f12" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Macroscopic Matter</text>
                                    <text x="125" y="135" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Divisible with human eye</text>
                                ` : step === 2 ? `
                                    <!-- Microscopic dust specks -->
                                    ${{[
                                        [80,50],[120,40],[160,55],[95,85],[140,80],[175,95],[110,115],[150,110]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="6" fill="#fbbf24" stroke="#d97706"/>
                                    `).join('')}}
                                    <text x="125" y="135" fill="#f59e0b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Fine Colloidal Subdivision</text>
                                ` : step === 3 ? `
                                    <!-- Glowing Indivisible Parmanu Sphere (Kanad ~600 BCE) -->
                                    <circle cx="125" cy="75" r="35" fill="#9333ea" opacity="0.3"/>
                                    <circle cx="125" cy="75" r="22" fill="#a855f7" stroke="#c084fc" stroke-width="2.5"/>
                                    <text x="125" y="78" fill="#ffffff" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">PARMANU</text>
                                    <text x="125" y="135" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Acharya Kanad: Indivisible Limit</text>
                                ` : `
                                    <!-- Cleaved Subatomic Atom (1897-1932) -->
                                    <circle cx="125" cy="75" r="50" fill="none" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3 2"/>
                                    <circle cx="125" cy="75" r="10" fill="#ef4444"/>
                                    <text x="125" y="78" fill="#ffffff" font-size="7" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">p⁺, n⁰</text>
                                    <!-- Orbiting electron -->
                                    <circle cx="125" cy="25" r="4" fill="#38bdf8"/>
                                    <circle cx="175" cy="75" r="4" fill="#38bdf8"/>
                                    <text x="125" y="135" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Subatomic Particles (e⁻, p⁺, n⁰)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-6.1 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Acharya Kanad (~600 BCE):</strong> Ancient Indian philosophy anticipated modern atomic theory by positing the Parmanu as the indestructible building block of all elements.
                        </div>
                    </div>
                `;
            }}

            window.sim1Set = function(s) {{
                step = s;
                playTone(380 + s * 50, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 2: Subatomic Particle Triad Comparator
        function renderSim2(vp) {{
            let selP = 'electron'; // electron, proton, neutron
            const pData = {{
                electron: {{ symbol: "e⁻", disc: "J.J. Thomson (1897)", charge: "-1.602 × 10⁻¹⁹ C (-1)", mass: "9.109 × 10⁻³¹ kg (~1/1840 u)", loc: "Orbits in extranuclear shells", col: "text-cyan-400", bg: "#0284c7" }},
                proton: {{ symbol: "p⁺", disc: "E. Goldstein (1886) / Rutherford", charge: "+1.602 × 10⁻¹⁹ C (+1)", mass: "1.673 × 10⁻²⁷ kg (~1 u)", loc: "Inside dense atomic nucleus", col: "text-rose-400", bg: "#be123c" }},
                neutron: {{ symbol: "n⁰", disc: "James Chadwick (1932)", charge: "0 C (Electrically Neutral)", mass: "1.675 × 10⁻²⁷ kg (~1 u)", loc: "Inside dense atomic nucleus", col: "text-amber-400", bg: "#d97706" }}
            }};

            function draw() {{
                const cur = pData[selP];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono font-bold">
                            <button onclick="window.sim2Set('electron')" class="py-1 rounded ${{selP === 'electron' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Electron (e⁻)</button>
                            <button onclick="window.sim2Set('proton')" class="py-1 rounded ${{selP === 'proton' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Proton (p⁺)</button>
                            <button onclick="window.sim2Set('neutron')" class="py-1 rounded ${{selP === 'neutron' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Neutron (n⁰)</button>
                        </div>

                        <!-- Graphical Particle Visualizer -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <circle cx="125" cy="75" r="45" fill="${{cur.bg}}" opacity="0.2"/>
                                <circle cx="125" cy="75" r="30" fill="${{cur.bg}}" stroke="#ffffff" stroke-width="2"/>
                                <text x="125" y="82" fill="#ffffff" font-size="16" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">${{cur.symbol}}</text>
                                <text x="125" y="135" fill="#cbd5e1" font-size="8" font-family="JetBrains Mono" text-anchor="middle">${{cur.disc}}</text>
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">Electrical Charge:</span><span class="${{cur.col}} font-bold">${{cur.charge}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Relative Rest Mass:</span><span class="text-slate-200">${{cur.mass}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Atomic Position:</span><span class="text-teal-300 font-semibold">${{cur.loc}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim2Set = function(p) {{
                selP = p;
                playTone(p === 'electron' ? 580 : p === 'proton' ? 440 : 360, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 3: Thomson's Watermelon / Plum Pudding Model
        function renderSim3(vp) {{
            let mode = 'watermelon'; // 'watermelon' vs 'pudding'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim3Set('watermelon')" class="py-1.5 rounded-lg transition ${{mode === 'watermelon' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Watermelon Analogy
                            </button>
                            <button onclick="window.sim3Set('pudding')" class="py-1.5 rounded-lg transition ${{mode === 'pudding' ? 'bg-amber-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Plum Pudding Model
                            </button>
                        </div>

                        <!-- Graphical Sphere -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'watermelon' ? `
                                    <!-- Watermelon Slice: Red Flesh is Positive Charge, Seeds are Electrons -->
                                    <circle cx="125" cy="75" r="55" fill="#e11d48" stroke="#16a34a" stroke-width="4"/>
                                    <!-- Embedded Black Seeds (Electrons) -->
                                    ${{[
                                        [105,55],[145,55],[95,75],[125,75],[155,75],[110,95],[140,95]
                                    ].map(([cx,cy]) => `
                                        <ellipse cx="${{cx}}" cy="${{cy}}" rx="4" ry="2.5" fill="#000000" transform="rotate(30 ${{cx}} ${{cy}})"/>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#f43f5e" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Red Flesh: Positive Charge • Seeds: Electrons</text>
                                ` : `
                                    <!-- Plum Pudding Model -->
                                    <circle cx="125" cy="75" r="55" fill="#d97706" opacity="0.8" stroke="#f59e0b" stroke-width="3"/>
                                    <!-- Embedded Raisins (Electrons) -->
                                    ${{[
                                        [100,55],[145,50],[85,75],[120,70],[155,80],[105,95],[135,100]
                                    ].map(([cx,cy]) => `
                                        <circle cx="${{cx}}" cy="${{cy}}" r="5" fill="#1e1b4b" stroke="#38bdf8" stroke-width="1.5"/>
                                        <text x="${{cx}}" y="${{cy + 2.5}}" fill="#ffffff" font-size="6" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">-</text>
                                    `).join('')}}
                                    <text x="125" y="142" fill="#fbbf24" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Positive Pudding Sphere • Embedded Negative Plums</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Neutrality Equation:</strong> Total Positive Charge ($+e$) = Total Negative Electron Charge ($-e$). Net charge = $0$. Failed to explain alpha particle scattering!
                        </div>
                    </div>
                `;
            }}

            window.sim3Set = function(m) {{
                mode = m;
                playTone(m === 'watermelon' ? 440 : 500, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 4: Rutherford Alpha Scattering Gold Foil Chamber (C-5.1)
        function renderSim4(vp) {{
            let fired = false;

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Alpha Scattering Setup:</span>
                            <button onclick="window.sim4Fire()" class="px-3 py-1 rounded-lg font-bold transition ${{fired ? 'bg-purple-600 text-white animate-pulse' : 'bg-slate-800 text-slate-400'}}">
                                ${{fired ? 'BEAM FIRING...' : 'FIRE ALPHA BEAM (He²⁺)'}}
                            </button>
                        </div>

                        <!-- Chamber SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Circular Zinc Sulfide (ZnS) Screen -->
                                <path d="M 50 30 A 85 85 0 1 1 50 120" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="4 2"/>
                                <text x="195" y="30" fill="#4ade80" font-size="7" font-family="JetBrains Mono">ZnS Screen</text>

                                <!-- Central Ultra-Thin Gold Foil -->
                                <line x1="125" y1="40" x2="125" y2="110" stroke="#f59e0b" stroke-width="4"/>
                                <text x="125" y="32" fill="#fbbf24" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Gold Foil</text>

                                <!-- Alpha Source on Left -->
                                <rect x="15" y="65" width="20" height="20" rx="3" fill="#334155" stroke="#64748b"/>
                                <circle cx="25" cy="75" r="3" fill="#ef4444"/>

                                ${{fired ? `
                                    <!-- Most pass straight (>99%) -->
                                    <line x1="35" y1="70" x2="205" y2="70" stroke="#a855f7" stroke-width="1.5"/>
                                    <line x1="35" y1="75" x2="210" y2="75" stroke="#a855f7" stroke-width="2"/>
                                    <line x1="35" y1="80" x2="205" y2="80" stroke="#a855f7" stroke-width="1.5"/>
                                    <circle cx="210" cy="75" r="3" fill="#4ade80"/>

                                    <!-- Small Angle Deflection -->
                                    <path d="M 35 65 L 125 65 L 180 40" stroke="#a855f7" stroke-width="1.5"/>
                                    <circle cx="180" cy="40" r="3" fill="#4ade80"/>

                                    <!-- Rare Rebound Backwards (1 in 12,000) -->
                                    <path d="M 35 78 L 125 78 L 45 105" stroke="#f43f5e" stroke-width="2"/>
                                    <circle cx="45" cy="105" r="3" fill="#ef4444"/>
                                    <text x="125" y="138" fill="#f43f5e" font-size="8" font-family="JetBrains Mono" text-anchor="middle">1 in 12,000 Rebounds (Dense Nucleus!)</text>
                                ` : `
                                    <text x="125" y="138" fill="#64748b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Click button to fire He²⁺ beam</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Rutherford's Deduction:</strong> Massive positive mass is confined to a microscopic nucleus; 99.9% of the atom is completely empty space.
                        </div>
                    </div>
                `;
            }}

            window.sim4Fire = function() {{
                fired = !fired;
                playTone(fired ? 650 : 320, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 5: Nuclear Atom vs Maxwell Spiral Collapse Paradox
        function renderSim5(vp) {{
            let mode = 'maxwell'; // 'rutherford' vs 'maxwell'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim5Set('rutherford')" class="py-1.5 rounded-lg transition ${{mode === 'rutherford' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Planetary Circular Orbit
                            </button>
                            <button onclick="window.sim5Set('maxwell')" class="py-1.5 rounded-lg transition ${{mode === 'maxwell' ? 'bg-rose-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Maxwell Spiral Collapse
                            </button>
                        </div>

                        <!-- Graphic Canvas -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Central Nucleus -->
                                <circle cx="125" cy="75" r="8" fill="#ef4444"/>
                                <text x="125" y="78" fill="#ffffff" font-size="7" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">+</text>

                                ${{mode === 'rutherford' ? `
                                    <!-- Stable Circular Orbit -->
                                    <circle cx="125" cy="75" r="45" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2"/>
                                    <circle cx="125" cy="30" r="4" fill="#38bdf8"/>
                                    <text x="125" y="138" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Rutherford Model: Fixed Circular Track</text>
                                ` : `
                                    <!-- Inward Radiation Spiral Decay -->
                                    <path d="M 125 25 A 50 50 0 0 1 170 75 A 40 40 0 0 1 125 110 A 30 30 0 0 1 95 75 A 20 20 0 0 1 125 58 A 12 12 0 0 1 125 75" fill="none" stroke="#f43f5e" stroke-width="2"/>
                                    <circle cx="125" cy="75" r="5" fill="#f43f5e"/>
                                    <!-- Radiated EM Wave Packets -->
                                    <path d="M 175 60 Q 185 55 195 60" stroke="#f59e0b" stroke-width="1.5" fill="none"/>
                                    <path d="M 160 100 Q 170 95 180 100" stroke="#f59e0b" stroke-width="1.5" fill="none"/>
                                    <text x="125" y="140" fill="#f43f5e" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Collapse into Nucleus in ~10⁻⁸ Seconds!</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Classical Paradox:</strong> Accelerating charges radiate energy. Under classical mechanics, electrons must spiral into the nucleus within a split microsecond!
                        </div>
                    </div>
                `;
            }}

            window.sim5Set = function(m) {{
                mode = m;
                playTone(m === 'rutherford' ? 520 : 310, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 6: Bohr Stationary Orbits & Quantum Jump Emission
        function renderSim6(vp) {{
            let shell = 2; // 1: K, 2: L, 3: M, 4: N

            function draw() {{
                const r = shell === 1 ? 22 : shell === 2 ? 38 : shell === 3 ? 52 : 65;
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Target Quantum Shell:</span>
                            <span class="text-purple-400 font-bold">${{shell === 1 ? 'K-shell (n=1)' : shell === 2 ? 'L-shell (n=2)' : shell === 3 ? 'M-shell (n=3)' : 'N-shell (n=4)'}}</span>
                        </div>

                        <!-- 4 Shell Buttons -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim6Set(1)" class="py-1 rounded ${{shell === 1 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">K (n=1)</button>
                            <button onclick="window.sim6Set(2)" class="py-1 rounded ${{shell === 2 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">L (n=2)</button>
                            <button onclick="window.sim6Set(3)" class="py-1 rounded ${{shell === 3 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">M (n=3)</button>
                            <button onclick="window.sim6Set(4)" class="py-1 rounded ${{shell === 4 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">N (n=4)</button>
                        </div>

                        <!-- Bohr Atom Graphic -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Nucleus -->
                                <circle cx="125" cy="75" r="8" fill="#ef4444"/>
                                <text x="125" y="78" fill="#ffffff" font-size="6" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">+</text>

                                <!-- Discrete Concentric Shells K, L, M, N -->
                                <circle cx="125" cy="75" r="22" fill="none" stroke="#6366f1" stroke-width="${{shell === 1 ? 2 : 1}}" stroke-dasharray="2 1" opacity="${{shell === 1 ? 1 : 0.4}}"/>
                                <circle cx="125" cy="75" r="38" fill="none" stroke="#6366f1" stroke-width="${{shell === 2 ? 2 : 1}}" stroke-dasharray="2 1" opacity="${{shell === 2 ? 1 : 0.4}}"/>
                                <circle cx="125" cy="75" r="52" fill="none" stroke="#6366f1" stroke-width="${{shell === 3 ? 2 : 1}}" stroke-dasharray="2 1" opacity="${{shell === 3 ? 1 : 0.4}}"/>
                                <circle cx="125" cy="75" r="65" fill="none" stroke="#6366f1" stroke-width="${{shell === 4 ? 2 : 1}}" stroke-dasharray="2 1" opacity="${{shell === 4 ? 1 : 0.4}}"/>

                                <!-- Active Electron in Selected Shell -->
                                <circle cx="125" cy="${{75 - r}}" r="4" fill="#38bdf8"/>
                                <!-- Emitted Photon Wave when jumping down -->
                                <path d="M 130 50 Q 140 45 150 50 Q 160 55 170 50" stroke="#facc15" stroke-width="2" fill="none"/>
                                <text x="180" y="52" fill="#facc15" font-size="8" font-family="JetBrains Mono">hν</text>

                                <text x="125" y="142" fill="#a855f7" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Non-radiating Discrete Level (ΔE = E₂ - E₁ = hν)</text>
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Niels Bohr (1913):</strong> Electrons revolve strictly in quantized stationary energy levels; radiation occurs only when transitioning between levels.
                        </div>
                    </div>
                `;
            }}

            window.sim6Set = function(s) {{
                shell = s;
                playTone(400 + s * 60, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 7: Bohr-Bury 2n² Shell Capacity & Octet Ceiling
        function renderSim7(vp) {{
            let n = 2; // 1, 2, 3, 4

            function draw() {{
                const cap = 2 * n * n;
                const name = n === 1 ? 'K-shell' : n === 2 ? 'L-shell' : n === 3 ? 'M-shell' : 'N-shell';
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim7Set(1)" class="py-1 rounded ${{n === 1 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">n=1 (K)</button>
                            <button onclick="window.sim7Set(2)" class="py-1 rounded ${{n === 2 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">n=2 (L)</button>
                            <button onclick="window.sim7Set(3)" class="py-1 rounded ${{n === 3 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">n=3 (M)</button>
                            <button onclick="window.sim7Set(4)" class="py-1 rounded ${{n === 4 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">n=4 (N)</button>
                        </div>

                        <!-- Capacity Display Card -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col gap-2 items-center justify-center text-center h-40">
                            <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest">${{name}} Capacity (n = ${{n}})</span>
                            <div class="text-3xl font-mono font-extrabold text-purple-400">
                                ${{cap}} Electrons
                            </div>
                            <div class="text-xs font-mono text-slate-300">
                                Formula: 2n² = 2 × (${{n}})² = 2 × ${{n*n}} = ${{cap}}
                            </div>
                            <div class="text-[11px] font-mono text-amber-300 pt-1 border-t border-slate-800 w-full">
                                ${{n >= 3 ? 'Outermost Shell Ceiling: Strictly 8 Electrons (Octet Rule)!' : 'Completely Filled Shell Capacity'}}
                            </div>
                        </div>

                        <!-- Bohr-Bury Rule Summary -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Rule 2 Invariant:</strong> The outermost shell of an atom can never accommodate more than 8 electrons, regardless of the $2n^2$ capacity limit!
                        </div>
                    </div>
                `;
            }}

            window.sim7Set = function(val) {{
                n = val;
                playTone(450 + val * 50, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 8: First 18 Elements Interactive Shell Configurator (C-1.3)
        function renderSim8(vp) {{
            let z = 11; // Sodium default
            const elemNames = [
                "H","He","Li","Be","B","C","N","O","F","Ne",
                "Na","Mg","Al","Si","P","S","Cl","Ar"
            ];
            const fullNames = [
                "Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon",
                "Sodium","Magnesium","Aluminium","Silicon","Phosphorus","Sulfur","Chlorine","Argon"
            ];

            function getConfig(atomicNum) {{
                let k = Math.min(atomicNum, 2);
                let l = Math.max(0, Math.min(atomicNum - 2, 8));
                let m = Math.max(0, atomicNum - 10);
                return {{ k, l, m }};
            }}

            function draw() {{
                const cfg = getConfig(z);
                const sym = elemNames[z - 1];
                const name = fullNames[z - 1];

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Element: <strong class="text-white">${{z}}. ${{name}} (${{sym}})</strong></span>
                            <span class="text-purple-400 font-bold">${{cfg.k}}, ${{cfg.l}}${{cfg.m > 0 ? ', ' + cfg.m : ''}}</span>
                        </div>

                        <input type="range" min="1" max="18" value="${{z}}" oninput="window.sim8SetZ(this.value)" class="w-full accent-purple-500">

                        <!-- Concentric Atom SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Central Nucleus -->
                                <circle cx="125" cy="75" r="14" fill="#881337" stroke="#f43f5e" stroke-width="1.5"/>
                                <text x="125" y="78" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">${{sym}}</text>

                                <!-- K Shell -->
                                <circle cx="125" cy="75" r="28" fill="none" stroke="#6366f1" stroke-width="1" stroke-dasharray="2 1"/>
                                ${{Array.from({{length: cfg.k}}).map((_, i) => {{
                                    const ang = i * Math.PI;
                                    const cx = 125 + 28 * Math.cos(ang);
                                    const cy = 75 + 28 * Math.sin(ang);
                                    return `<circle cx="${{cx}}" cy="${{cy}}" r="3" fill="#38bdf8"/>`;
                                }}).join('')}}

                                <!-- L Shell -->
                                ${{cfg.l > 0 ? `
                                    <circle cx="125" cy="75" r="46" fill="none" stroke="#6366f1" stroke-width="1" stroke-dasharray="2 1"/>
                                    ${{Array.from({{length: cfg.l}}).map((_, i) => {{
                                        const ang = i * (2 * Math.PI / cfg.l);
                                        const cx = 125 + 46 * Math.cos(ang);
                                        const cy = 75 + 46 * Math.sin(ang);
                                        return `<circle cx="${{cx}}" cy="${{cy}}" r="3" fill="#a855f7"/>`;
                                    }}).join('')}}
                                ` : ''}}

                                <!-- M Shell -->
                                ${{cfg.m > 0 ? `
                                    <circle cx="125" cy="75" r="62" fill="none" stroke="#6366f1" stroke-width="1" stroke-dasharray="2 1"/>
                                    ${{Array.from({{length: cfg.m}}).map((_, i) => {{
                                        const ang = i * (2 * Math.PI / cfg.m);
                                        const cx = 125 + 62 * Math.cos(ang);
                                        const cy = 75 + 62 * Math.sin(ang);
                                        return `<circle cx="${{cx}}" cy="${{cy}}" r="3" fill="#facc15"/>`;
                                    }}).join('')}}
                                ` : ''}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono flex justify-around text-center">
                            <div><span class="text-slate-400 block text-[10px]">K-Shell</span><span class="text-cyan-400 font-bold">${{cfg.k}}</span></div>
                            <div><span class="text-slate-400 block text-[10px]">L-Shell</span><span class="text-purple-400 font-bold">${{cfg.l}}</span></div>
                            <div><span class="text-slate-400 block text-[10px]">M-Shell</span><span class="text-amber-400 font-bold">${{cfg.m}}</span></div>
                            <div><span class="text-slate-400 block text-[10px]">Valence e⁻</span><span class="text-emerald-400 font-bold">${{cfg.m > 0 ? cfg.m : cfg.l > 0 ? cfg.l : cfg.k}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim8SetZ = function(val) {{
                z = parseInt(val);
                playTone(300 + z * 20, 0.05);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 9: Valency & Combining Capacity Calculator
        function renderSim9(vp) {{
            let elemIdx = 10; // Sodium (Z=11, index 10)
            const elements = [
                {{ sym: "H", z: 1, cfg: "1", v: 1, val: 1 }},
                {{ sym: "He", z: 2, cfg: "2", v: 2, val: 0 }},
                {{ sym: "Li", z: 3, cfg: "2, 1", v: 1, val: 1 }},
                {{ sym: "Be", z: 4, cfg: "2, 2", v: 2, val: 2 }},
                {{ sym: "B", z: 5, cfg: "2, 3", v: 3, val: 3 }},
                {{ sym: "C", z: 6, cfg: "2, 4", v: 4, val: 4 }},
                {{ sym: "N", z: 7, cfg: "2, 5", v: 5, val: 3 }},
                {{ sym: "O", z: 8, cfg: "2, 6", v: 6, val: 2 }},
                {{ sym: "F", z: 9, cfg: "2, 7", v: 7, val: 1 }},
                {{ sym: "Ne", z: 10, cfg: "2, 8", v: 8, val: 0 }},
                {{ sym: "Na", z: 11, cfg: "2, 8, 1", v: 1, val: 1 }},
                {{ sym: "Mg", z: 12, cfg: "2, 8, 2", v: 2, val: 2 }},
                {{ sym: "Al", z: 13, cfg: "2, 8, 3", v: 3, val: 3 }},
                {{ sym: "Si", z: 14, cfg: "2, 8, 4", v: 4, val: 4 }},
                {{ sym: "P", z: 15, cfg: "2, 8, 5", v: 5, val: 3 }},
                {{ sym: "S", z: 16, cfg: "2, 8, 6", v: 6, val: 2 }},
                {{ sym: "Cl", z: 17, cfg: "2, 8, 7", v: 7, val: 1 }},
                {{ sym: "Ar", z: 18, cfg: "2, 8, 8", v: 8, val: 0 }}
            ];

            function draw() {{
                const el = elements[elemIdx];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <!-- Quick Pick Buttons -->
                        <div class="grid grid-cols-6 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                            ${{elements.slice(0, 12).map((e, idx) => `
                                <button onclick="window.sim9Set(${{idx}})" class="py-1 rounded ${{elemIdx === idx ? 'bg-purple-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{e.sym}}</button>
                            `).join('')}}
                        </div>
                        <div class="grid grid-cols-6 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                            ${{elements.slice(12).map((e, idx) => `
                                <button onclick="window.sim9Set(${{idx + 12}})" class="py-1 rounded ${{elemIdx === idx + 12 ? 'bg-purple-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{e.sym}}</button>
                            `).join('')}}
                        </div>

                        <!-- Valency Result Box -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col gap-1 items-center justify-center text-center h-32">
                            <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest">Element: ${{el.sym}} (Z = ${{el.z}}) • Config: ${{el.cfg}}</span>
                            <div class="text-3xl font-mono font-extrabold text-emerald-400">
                                Valency = ${{el.val}}
                            </div>
                            <span class="text-xs font-mono text-slate-300">
                                ${{el.v <= 4 ? 'Valence electrons ≤ 4: Valency = ' + el.v : el.sym === 'He' || el.sym === 'Ne' || el.sym === 'Ar' ? 'Complete octet/duplet: Valency = 0' : 'Valence electrons > 4: Valency = 8 - ' + el.v + ' = ' + el.val}}
                            </span>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Combining Capacity:</strong> The number of electrons gained, lost, or shared to achieve an octet (8 electrons) in the outermost shell.
                        </div>
                    </div>
                `;
            }}

            window.sim9Set = function(idx) {{
                elemIdx = idx;
                playTone(420 + idx * 15, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 10: Atomic Notation & Subatomic Particle Counter
        function renderSim10(vp) {{
            let selIdx = 2; // Na-23 default
            const presets = [
                {{ sym: "H", name: "Hydrogen", a: 1, z: 1 }},
                {{ sym: "C", name: "Carbon-12", a: 12, z: 6 }},
                {{ sym: "Na", name: "Sodium-23", a: 23, z: 11 }},
                {{ sym: "Cl", name: "Chlorine-35", a: 35, z: 17 }},
                {{ sym: "Ca", name: "Calcium-40", a: 40, z: 20 }}
            ];

            function draw() {{
                const cur = presets[selIdx];
                const protons = cur.z;
                const electrons = cur.z;
                const neutrons = cur.a - cur.z;

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            ${{presets.map((p, idx) => `
                                <button onclick="window.sim10Set(${{idx}})" class="py-1 rounded ${{selIdx === idx ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    ${{p.sym}} (${{p.a}})
                                </button>
                            `).join('')}}
                        </div>

                        <!-- IUPAC Notation Box -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center gap-6 h-36">
                            <!-- Superscript A and Subscript Z Notation -->
                            <div class="flex items-center font-mono">
                                <div class="flex flex-col text-right font-bold pr-1.5 text-sm">
                                    <span class="text-amber-400">${{cur.a}}</span>
                                    <span class="text-cyan-400">${{cur.z}}</span>
                                </div>
                                <span class="text-4xl font-extrabold text-white">${{cur.sym}}</span>
                            </div>

                            <!-- Subatomic Particle Counts -->
                            <div class="font-mono text-xs space-y-1 border-l border-slate-800 pl-4">
                                <div><span class="text-slate-400">Protons (p⁺ = Z):</span> <span class="text-rose-400 font-bold">${{protons}}</span></div>
                                <div><span class="text-slate-400">Electrons (e⁻ = Z):</span> <span class="text-cyan-400 font-bold">${{electrons}}</span></div>
                                <div><span class="text-slate-400">Neutrons (A - Z):</span> <span class="text-amber-400 font-bold">${{neutrons}}</span></div>
                            </div>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>IUPAC Notation:</strong> Upper prefix is Mass Number ($A = p^+ + n^0$), lower prefix is Atomic Number ($Z = p^+$).
                        </div>
                    </div>
                `;
            }}

            window.sim10Set = function(idx) {{
                selIdx = idx;
                playTone(460, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 11: Hydrogen Isotopes Triad (Protium, Deuterium, Tritium)
        function renderSim11(vp) {{
            let iso = 'protium'; // protium, deuterium, tritium

            function draw() {{
                const p = 1, e = 1;
                const n = iso === 'protium' ? 0 : iso === 'deuterium' ? 1 : 2;
                const a = iso === 'protium' ? 1 : iso === 'deuterium' ? 2 : 3;
                const name = iso === 'protium' ? "Protium (¹₁H)" : iso === 'deuterium' ? "Deuterium (²₁H / D)" : "Tritium (³₁H / T)";

                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim11Set('protium')" class="py-1 rounded ${{iso === 'protium' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Protium (¹H)</button>
                            <button onclick="window.sim11Set('deuterium')" class="py-1 rounded ${{iso === 'deuterium' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Deuterium (²H)</button>
                            <button onclick="window.sim11Set('tritium')" class="py-1 rounded ${{iso === 'tritium' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Tritium (³H)</button>
                        </div>

                        <!-- Nucleus & Shell Cross Section -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- K-Shell Orbit -->
                                <circle cx="125" cy="75" r="45" fill="none" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3 2"/>
                                <!-- Single Electron -->
                                <circle cx="125" cy="30" r="4" fill="#38bdf8"/>
                                <text x="133" y="32" fill="#38bdf8" font-size="7" font-family="JetBrains Mono">1 e⁻</text>

                                <!-- Nucleus Cluster -->
                                <circle cx="125" cy="75" r="16" fill="#1e1b4b" stroke="#818cf8"/>
                                <!-- 1 Proton (Always 1) -->
                                <circle cx="${{n === 0 ? 125 : 120}}" cy="${{n === 0 ? 75 : 72}}" r="6" fill="#ef4444"/>
                                <text x="${{n === 0 ? 125 : 120}}" y="${{n === 0 ? 77 : 74}}" fill="#ffffff" font-size="5" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">p⁺</text>

                                ${{n >= 1 ? `
                                    <!-- 1st Neutron -->
                                    <circle cx="128" cy="78" r="6" fill="#f59e0b"/>
                                    <text x="128" y="80" fill="#ffffff" font-size="5" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">n⁰</text>
                                ` : ''}}
                                ${{n === 2 ? `
                                    <!-- 2nd Neutron (Tritium) -->
                                    <circle cx="120" cy="80" r="5" fill="#f59e0b"/>
                                    <text x="120" y="82" fill="#ffffff" font-size="5" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">n⁰</text>
                                ` : ''}}

                                <text x="125" y="140" fill="#a855f7" font-size="8" font-family="JetBrains Mono" text-anchor="middle">${{name}}</text>
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">Protons / Electrons:</span><span class="text-white font-bold">1 p⁺ / 1 e⁻ (Same Chemistry)</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Neutrons:</span><span class="text-amber-400 font-bold">${{n}} neutrons (Mass A = ${{a}})</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim11Set = function(m) {{
                iso = m;
                playTone(m === 'protium' ? 440 : m === 'deuterium' ? 480 : 520, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 12: Chlorine Fractional Atomic Mass (35.5 u) Lab
        function renderSim12(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-2.5">
                    <!-- Weighted Average Calculation Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        <div class="text-center font-bold text-sm text-purple-400 mb-1">
                            Natural Chlorine Isotopic Composition
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>• Chlorine-35 (³⁵₁₇Cl):</span>
                            <span class="text-emerald-400 font-bold">75% (3/4 ratio)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>• Chlorine-37 (³⁷₁₇Cl):</span>
                            <span class="text-cyan-400 font-bold">25% (1/4 ratio)</span>
                        </div>

                        <div class="p-2 rounded bg-slate-900 border border-slate-800 text-[11px] text-slate-300 leading-relaxed pt-2">
                            $$\\text{{Average Mass}} = \\left(35 \\times \\frac{{75}}{{100}}\\right) + \\left(37 \\times \\frac{{25}}{{100}}\\right)$$
                            $$= \\frac{{105}}{{4}} + \\frac{{37}}{{4}} = \\frac{{142}}{{4}} = \\mathbf{{35.5\\text{{ u}}}}$$
                        </div>

                        <div class="text-center text-xs text-amber-300 font-bold pt-1">
                            Individual atoms: strictly 35 u or 37 u!<br>
                            35.5 u is the statistical weighted average.
                        </div>
                    </div>

                    <!-- Visual Ratio Bar -->
                    <div class="w-full h-4 rounded-full overflow-hidden flex border border-slate-700">
                        <div class="bg-emerald-500 h-full flex items-center justify-center text-[9px] font-mono font-bold text-slate-950" style="width: 75%">³⁵Cl (75%)</div>
                        <div class="bg-cyan-500 h-full flex items-center justify-center text-[9px] font-mono font-bold text-slate-950" style="width: 25%">³⁷Cl (25%)</div>
                    </div>
                </div>
            `;
            if (window.renderMathInElement) renderMathInElement(vp);
        }}

        // SIMULATOR 13: Societal Radioisotopes: Medicine & Energy (C-5.3)
        function renderSim13(vp) {{
            let app = 'co60'; // co60, i131, u235, c14
            const data = {{
                co60: {{ title: "Cobalt-60 (⁶⁰Co)", use: "High-Energy Gamma Radiotherapy", desc: "Emits collimated γ-rays used in hospital teletherapy to destroy cancer tumors.", col: "text-rose-400" }},
                i131: {{ title: "Iodine-131 (¹³¹I)", use: "Thyroid Goitre & Oncology", desc: "Thyroid tissue selectively absorbs iodine; targeted beta radiation treats goitres.", col: "text-purple-400" }},
                u235: {{ title: "Uranium-235 (²³⁵U)", use: "Nuclear Power Reactor Fuel", desc: "Undergoes controlled fission releasing ~200 MeV energy to generate baseload electricity.", col: "text-amber-400" }},
                c14: {{ title: "Carbon-14 (¹⁴C)", use: "Archaeological Radiocarbon Dating", desc: "Half-life of 5,730 years allows dating of fossilized organic remains and ancient artifacts.", col: "text-emerald-400" }}
            }};

            function draw() {{
                const cur = data[app];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[9px] font-mono font-bold">
                            <button onclick="window.sim13Set('co60')" class="py-1 rounded ${{app === 'co60' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">⁶⁰Co (Cancer)</button>
                            <button onclick="window.sim13Set('i131')" class="py-1 rounded ${{app === 'i131' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">¹³¹I (Thyroid)</button>
                            <button onclick="window.sim13Set('u235')" class="py-1 rounded ${{app === 'u235' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">²³⁵U (Reactor)</button>
                            <button onclick="window.sim13Set('c14')" class="py-1 rounded ${{app === 'c14' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">¹⁴C (Dating)</button>
                        </div>

                        <!-- Graphical Display -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col gap-2 items-center justify-center text-center h-40">
                            <div class="w-10 h-10 rounded-full bg-purple-950 border border-purple-500/60 flex items-center justify-center text-purple-400">
                                <i data-lucide="radioactive" class="w-5 h-5"></i>
                            </div>
                            <h4 class="text-sm font-bold text-white">${{cur.title}}</h4>
                            <span class="text-xs font-mono font-bold ${{cur.col}}">${{cur.use}}</span>
                            <p class="text-[11px] text-slate-300 max-w-xs leading-relaxed">${{cur.desc}}</p>
                        </div>

                        <!-- C-5.3 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Societal Impact:</strong> Nuclear isotopes save lives in oncology and provide carbon-free energy when harnessed for peaceful human advancement.
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }}

            window.sim13Set = function(m) {{
                app = m;
                playTone(500, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 14: Isobars vs Isotopes Diagnostic Bench
        function renderSim14(vp) {{
            let mode = 'isobar'; // 'isobar' vs 'isotope'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim14Set('isobar')" class="py-1.5 rounded-lg transition ${{mode === 'isobar' ? 'bg-purple-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Isobars (⁴⁰Ar vs ⁴⁰Ca)
                            </button>
                            <button onclick="window.sim14Set('isotope')" class="py-1.5 rounded-lg transition ${{mode === 'isotope' ? 'bg-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Isotopes (¹²C vs ¹⁴C)
                            </button>
                        </div>

                        <!-- Comparison Window -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-around h-40">
                            ${{mode === 'isobar' ? `
                                <!-- Argon-40 vs Calcium-40 -->
                                <div class="text-center font-mono space-y-1">
                                    <div class="text-lg font-bold text-amber-400">⁴⁰₁₈Ar</div>
                                    <div class="text-[10px] text-slate-300">18 p⁺ • 22 n⁰</div>
                                    <div class="text-[10px] text-cyan-400">Inert Noble Gas</div>
                                </div>
                                <div class="text-center text-xs font-mono font-bold text-purple-400">
                                    Mass Number A = 40<br>
                                    <span class="text-[10px] text-slate-400 font-normal">Different Elements!</span>
                                </div>
                                <div class="text-center font-mono space-y-1">
                                    <div class="text-lg font-bold text-amber-400">⁴⁰₂₀Ca</div>
                                    <div class="text-[10px] text-slate-300">20 p⁺ • 20 n⁰</div>
                                    <div class="text-[10px] text-rose-400">Reactive Metal</div>
                                </div>
                            ` : `
                                <!-- Carbon-12 vs Carbon-14 -->
                                <div class="text-center font-mono space-y-1">
                                    <div class="text-lg font-bold text-cyan-400">¹²₆C</div>
                                    <div class="text-[10px] text-slate-300">6 p⁺ • 6 n⁰</div>
                                    <div class="text-[10px] text-emerald-400">Stable Carbon</div>
                                </div>
                                <div class="text-center text-xs font-mono font-bold text-purple-400">
                                    Atomic Number Z = 6<br>
                                    <span class="text-[10px] text-slate-400 font-normal">Same Chemistry!</span>
                                </div>
                                <div class="text-center font-mono space-y-1">
                                    <div class="text-lg font-bold text-cyan-400">¹⁴₆C</div>
                                    <div class="text-[10px] text-slate-300">6 p⁺ • 8 n⁰</div>
                                    <div class="text-[10px] text-rose-400">Radioactive Tracer</div>
                                </div>
                            `}}
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'isobar' ? 
                                '<strong>Isobars:</strong> Same mass number ($A$), different atomic number ($Z$). Different electron counts $\\to$ completely different chemistry!' : 
                                '<strong>Isotopes:</strong> Same atomic number ($Z$), different mass number ($A$). Identical valence electrons $\\to$ identical chemical reactions.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim14Set = function(m) {{
                mode = m;
                playTone(m === 'isobar' ? 480 : 540, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 15: Dr. Homi J. Bhabha & India's 3-Stage Nuclear Plan (C-5.2)
        function renderSim15(vp) {{
            let stage = 1; // 1, 2, 3

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Dr. Homi Bhabha 3-Stage Plan:</span>
                            <span class="text-purple-400 font-bold">Stage ${{stage}} of 3</span>
                        </div>

                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono font-bold">
                            <button onclick="window.sim15Set(1)" class="py-1 rounded ${{stage === 1 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Stage 1: PHWR</button>
                            <button onclick="window.sim15Set(2)" class="py-1 rounded ${{stage === 2 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Stage 2: FBR</button>
                            <button onclick="window.sim15Set(3)" class="py-1 rounded ${{stage === 3 ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Stage 3: Thorium</button>
                        </div>

                        <!-- Graphical Display -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{stage === 1 ? `
                                    <rect x="30" y="25" width="190" height="95" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
                                    <text x="125" y="48" fill="#c7d2fe" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Stage 1: PHWRs (Uranium)</text>
                                    <text x="125" y="70" fill="#a5b4fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Natural Uranium fuel + Heavy Water</text>
                                    <text x="125" y="86" fill="#a5b4fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Generates Electricity + Breeds Plutonium-239</text>
                                    <text x="125" y="102" fill="#a5b4fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Foundation of Indian Nuclear Fleet</text>
                                ` : stage === 2 ? `
                                    <rect x="30" y="25" width="190" height="95" rx="6" fill="#4c0519" stroke="#f43f5e" stroke-width="2"/>
                                    <text x="125" y="48" fill="#fecdd3" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Stage 2: Fast Breeder (FBRs)</text>
                                    <text x="125" y="70" fill="#fda4af" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Plutonium-239 core + Thorium blanket</text>
                                    <text x="125" y="86" fill="#fda4af" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Breeds more fuel than it consumes!</text>
                                    <text x="125" y="102" fill="#fda4af" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Converts ²³²Th into fissile ²³³U</text>
                                ` : `
                                    <rect x="30" y="25" width="190" height="95" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                                    <text x="125" y="48" fill="#d1fae5" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Stage 3: Thorium-233 Cycle</text>
                                    <text x="125" y="70" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Utilizes coastal Kerala monazite sands</text>
                                    <text x="125" y="86" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• India holds ~25% of world Thorium reserves</text>
                                    <text x="125" y="102" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Centuries of self-reliant clean energy!</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-5.2 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Dr. Homi J. Bhabha (1909–1966):</strong> Father of the Indian Nuclear Programme, architect of TIFR and BARC, and champion of peaceful atomic energy.
                        </div>
                    </div>
                `;
            }}

            window.sim15Set = function(s) {{
                stage = s;
                playTone(450 + s * 40, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 16: Quantum Orbital Clouds & Quark Substructure (C-7.2)
        function renderSim16(vp) {{
            let mode = 'cloud'; // 'cloud' vs 'quark'

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-bold">
                            <button onclick="window.sim16Set('cloud')" class="py-1.5 rounded-lg transition ${{mode === 'cloud' ? 'bg-purple-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Quantum Orbital Cloud (ψ²)
                            </button>
                            <button onclick="window.sim16Set('quark')" class="py-1.5 rounded-lg transition ${{mode === 'quark' ? 'bg-cyan-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                Inside a Proton (Quarks)
                            </button>
                        </div>

                        <!-- Graphical Display -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{mode === 'cloud' ? `
                                    <!-- 3D Probability Density Cloud -->
                                    <circle cx="125" cy="75" r="55" fill="#a855f7" opacity="0.1"/>
                                    <circle cx="125" cy="75" r="40" fill="#a855f7" opacity="0.25"/>
                                    <circle cx="125" cy="75" r="25" fill="#a855f7" opacity="0.45"/>
                                    <circle cx="125" cy="75" r="8" fill="#ef4444"/>
                                    <text x="125" y="78" fill="#ffffff" font-size="6" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">+</text>
                                    <text x="125" y="140" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Heisenberg Cloud: 90% Probability Wavepacket</text>
                                ` : `
                                    <!-- Proton Quark Triad (u, u, d) -->
                                    <circle cx="125" cy="75" r="45" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2"/>
                                    <!-- 2 Up Quarks (+2/3) -->
                                    <circle cx="105" cy="65" r="10" fill="#ef4444"/>
                                    <text x="105" y="68" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">u</text>
                                    <circle cx="145" cy="65" r="10" fill="#ef4444"/>
                                    <text x="145" y="68" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">u</text>
                                    <!-- 1 Down Quark (-1/3) -->
                                    <circle cx="125" cy="95" r="10" fill="#3b82f6"/>
                                    <text x="125" y="98" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">d</text>
                                    <!-- Gluon strings connecting quarks -->
                                    <line x1="105" y1="65" x2="145" y2="65" stroke="#facc15" stroke-width="1.5" stroke-dasharray="2 1"/>
                                    <line x1="105" y1="65" x2="125" y2="95" stroke="#facc15" stroke-width="1.5" stroke-dasharray="2 1"/>
                                    <line x1="145" y1="65" x2="125" y2="95" stroke="#facc15" stroke-width="1.5" stroke-dasharray="2 1"/>
                                    <text x="125" y="140" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Proton = u (+2/3) + u (+2/3) + d (-1/3) = +1</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-7.2 Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>C-7.2 Quantum Frontier:</strong> The atom is not a mechanical solar system—electrons exist as quantum probability clouds, and nucleons are made of vibrating quarks!
                        </div>
                    </div>
                `;
            }}

            window.sim16Set = function(m) {{
                mode = m;
                playTone(m === 'cloud' ? 520 : 460, 0.08);
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
