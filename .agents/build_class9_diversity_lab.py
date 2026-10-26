# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Science, Chapter 4 (Biology)
DIVERSITY IN LIVING ORGANISMS: CLASSIFICATION, 5 KINGDOMS, 3 DOMAINS, PLANT & ANIMAL PHYLA, BINOMIAL NOMENCLATURE, VIRUSES & CONSERVATION
Syllabus Competencies: C-4.1, C-2.8, C-7.1
Generates public/animations/class9-diversity-in-living-organisms.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_diversity_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-diversity-in-living-organisms.html"

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
    <title>NCERT Class 9 Science • Chapter 4: Diversity in Living Organisms Laboratory</title>
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
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 via-teal-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-emerald-950/40 border border-emerald-400/30">
                <i data-lucide="network" class="w-5 h-5 text-white"></i>
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold tracking-wider uppercase px-2 py-0.5 rounded bg-emerald-950/80 text-emerald-400 border border-emerald-800/60 font-mono">
                        NCERT Class 9 Science • Chapter 4
                    </span>
                    <span class="hidden sm:inline-block text-[11px] font-medium text-slate-400">• Taxonomy & Evolution Lab</span>
                </div>
                <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-1.5">
                    Diversity in Living Organisms: 5 Kingdoms, 3 Domains & Taxonomy
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
                            <rect width="100" height="100" fill="#0f1f1d"/>
                            <circle cx="50" cy="50" r="42" fill="#064e3b" opacity="0.4"/>
                            <!-- Torso / Lab Coat -->
                            <path d="M20,95 Q50,75 80,95 L80,100 L20,100 Z" fill="#334155"/>
                            <path d="M35,90 L50,100 L65,90 L60,82 L50,86 L40,82 Z" fill="#059669"/>
                            <!-- Head -->
                            <ellipse cx="50" cy="46" rx="22" ry="26" fill="#fed7aa"/>
                            <!-- Hair -->
                            <path d="M26,42 Q28,18 50,18 Q72,18 74,42 Q68,26 50,26 Q32,26 26,42 Z" fill="#374151"/>
                            <path d="M26,42 Q24,60 28,68 Q32,56 32,46 Z" fill="#374151"/>
                            <path d="M74,42 Q76,60 72,68 Q68,56 68,46 Z" fill="#374151"/>
                            <!-- Glasses -->
                            <rect x="33" y="40" width="13" height="8" rx="2" fill="none" stroke="#047857" stroke-width="2"/>
                            <rect x="54" y="40" width="13" height="8" rx="2" fill="none" stroke="#047857" stroke-width="2"/>
                            <line x1="46" y1="44" x2="54" y2="44" stroke="#047857" stroke-width="2"/>
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
                        <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-500 text-white font-mono shadow">
                            TEACHER
                        </div>
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="flex items-center justify-between gap-2">
                            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">Prof. Sophia • Voice Guide</span>
                            <span id="speechStatusIndicator" class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-400">Ready</span>
                        </div>
                        <p id="narrationText" class="text-xs text-slate-300 mt-1 line-clamp-3 leading-relaxed italic">
                            Welcome students! Today we journey across the breathtaking tapestry of life on Earth—from microscopic bacteria to colossal blue whales—discovering the evolutionary blueprint of biological classification.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Content Presentation Slide (Slides 1 to 16) -->
            <div id="contentSlideContainer" class="space-y-4">
                <!-- Slide Header Card -->
                <div class="glass-panel rounded-2xl p-5 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between">
                        <span id="slideCategoryText" class="text-[11px] font-bold text-emerald-400 uppercase tracking-widest font-mono">Section Core Theory</span>
                        <span id="slideBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 font-mono">
                            Part 1 of 20
                        </span>
                    </div>
                    <div>
                        <h2 id="slideTitle" class="text-lg sm:text-xl font-extrabold text-white tracking-tight">Introduction to Biodiversity & Classification</h2>
                        <p id="slideSubtitle" class="text-xs sm:text-sm font-medium text-emerald-400/90 mt-0.5">Taxonomic Hierarchy from Kingdom to Species</p>
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
                        <div class="w-7 h-7 rounded-lg bg-emerald-950 border border-emerald-700/60 flex items-center justify-center text-emerald-400">
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
                    You have comprehensively mastered Biodiversity, Whittaker's 5 Kingdoms, Carl Woese's 3 Domains (16S rRNA), Plant Divisions, Animal Phyla & Coelom Architecture, Binomial Nomenclature, Indian Flora/Fauna, Viruses/Viroids/Prions, and Ecological Conservation!
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

                <!-- Simulator Dynamic Viewport -->
                <div id="simulatorViewport" class="min-h-[380px] flex items-center justify-center relative">
                    <!-- Dynamic Interactive Simulator Content Rendered Here -->
                </div>
            </div>

            <!-- Global Laboratory Quick Stats -->
            <div class="glass-panel rounded-xl p-3 border border-slate-800/80 flex items-center justify-around text-center text-xs">
                <div>
                    <span class="text-slate-400 block text-[10px]">Kingdoms</span>
                    <span class="font-bold text-emerald-400 font-mono">5 Major</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Domains</span>
                    <span class="font-bold text-teal-400 font-mono">3 (Woese)</span>
                </div>
                <div class="h-6 w-px bg-slate-800"></div>
                <div>
                    <span class="text-slate-400 block text-[10px]">Animal Phyla</span>
                    <span class="font-bold text-cyan-400 font-mono">8 Major</span>
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

            <button onclick="window.nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-bold shadow-lg shadow-emerald-950/40 transition">
                <span>Next Slide</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </div>
    </footer>

    <!-- Step-by-Step Solution Pop-up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <div class="glass-panel w-full max-w-lg rounded-2xl border border-emerald-500/50 p-6 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm">
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
                <button onclick="window.closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition">
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
                btn.className = `w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between transition ${{idx === currentSlide ? 'bg-emerald-950/80 text-emerald-300 font-bold border border-emerald-700/50' : 'text-slate-300 hover:bg-slate-800/80'}}`;
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
                dot.className = `h-2 rounded-full transition-all ${{idx === currentSlide ? 'w-6 bg-emerald-500' : 'w-2 bg-slate-700 hover:bg-slate-500'}}`;
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
                indicator.className = 'text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 animate-pulse';
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
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0"></span>
                        <span>${{pt}}</span>
                    </li>
                `).join('');

                // Checkpoints List (2 per slide)
                const cpList = document.getElementById('checkpointsList');
                cpList.innerHTML = data.checkpoints.map((cp, cpIdx) => `
                    <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/80 space-y-2.5">
                        <div class="flex items-start justify-between gap-2">
                            <span class="text-xs font-semibold text-slate-200">
                                <span class="text-emerald-400 font-mono font-bold mr-1.5">Q${{cpIdx + 1}}.</span>
                                ${{cp.q}}
                            </span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                            ${{cp.options.map((opt, optIdx) => `
                                <button onclick="window.checkAnswer(${{idx}}, ${{cpIdx}}, ${{optIdx}})" 
                                        id="cp-btn-${{idx}}-${{cpIdx}}-${{optIdx}}"
                                        class="text-left px-3 py-2 rounded-lg text-xs font-medium bg-slate-950 border border-slate-800 hover:border-emerald-600/60 hover:bg-slate-800/60 transition flex items-center justify-between">
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
                                <span class="text-emerald-400 font-mono font-bold mr-1">Q${{qIdx + 1}}.</span>
                                ${{q.q}}
                            </span>
                            <button onclick="window.openSolutionModal(${{idx - 16}}, ${{qIdx}})" 
                                    class="shrink-0 text-[11px] font-mono px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-teal-300 border border-teal-800/50 flex items-center gap-1 transition">
                                <i data-lucide="help-circle" class="w-3 h-3"></i>
                                View Solution
                            </button>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            ${{q.options.map((opt, optIdx) => `
                                <button onclick="window.selectQuizAnswer(${{idx}}, ${{qIdx}}, ${{optIdx}})"
                                        id="quiz-btn-${{idx}}-${{qIdx}}-${{optIdx}}"
                                        class="text-left px-3 py-2 rounded-lg text-xs bg-slate-950 border border-slate-800 hover:border-emerald-500/60 transition flex items-center justify-between">
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
                btn.classList.remove('bg-emerald-950', 'border-emerald-500', 'text-emerald-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === cp.correct) {{
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-emerald-950/60', 'text-emerald-300', 'border-emerald-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-emerald-950/60', 'text-emerald-300', 'border', 'border-emerald-800/80');
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
                btn.classList.remove('bg-emerald-950', 'border-emerald-500', 'text-emerald-300', 'bg-rose-950', 'border-rose-500', 'text-rose-300');
                if (i === q.correct) {{
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                }} else if (i === optIdx && !isCorrect) {{
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                }}
            }});

            feedbackEl.classList.remove('hidden', 'bg-emerald-950/60', 'text-emerald-300', 'border-emerald-800', 'bg-rose-950/60', 'text-rose-300', 'border-rose-800');
            if (isCorrect) {{
                playTone(660, 0.12);
                feedbackEl.classList.add('bg-emerald-950/60', 'text-emerald-300', 'border', 'border-emerald-800/80');
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
                    <span class="text-xs font-mono font-bold text-emerald-400 block mb-1">Question ${{qIdx + 1}}:</span>
                    <p class="text-xs text-white font-semibold">${{q.q}}</p>
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/60">
                    <span class="text-xs font-mono font-bold text-emerald-300 block mb-1">Correct Answer:</span>
                    <p class="text-xs font-bold text-white">${{q.options[q.correct]}}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-mono font-bold text-teal-400 block mb-1">Detailed Explanation & Reasoning:</span>
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
                    titleEl.textContent = "Taxonomic Hierarchy Ladder";
                    renderSim1(vp); break;
                case 1:
                    titleEl.textContent = "4-Axis Classification Filter Matrix";
                    renderSim2(vp); break;
                case 2:
                    titleEl.textContent = "5-Kingdom Phylogenetic Tree & Trophic Web";
                    renderSim3(vp); break;
                case 3:
                    titleEl.textContent = "Carl Woese 3-Domain Molecular Tree (16S rRNA)";
                    renderSim4(vp); break;
                case 4:
                    titleEl.textContent = "Lichen Symbiosis & SO2 Air Pollution Sensor";
                    renderSim5(vp); break;
                case 5:
                    titleEl.textContent = "Plant Evolutionary Decision Flowchart";
                    renderSim6(vp); break;
                case 6:
                    titleEl.textContent = "Cryptogam 3-Way Diagnostic Comparator";
                    renderSim7(vp); break;
                case 7:
                    titleEl.textContent = "Phanerogam Lab: Gymnosperm vs Angiosperm";
                    renderSim8(vp); break;
                case 8:
                    titleEl.textContent = "Coelom Cross-Section Simulator";
                    renderSim9(vp); break;
                case 9:
                    titleEl.textContent = "Invertebrates I: Porifera to Nematoda";
                    renderSim10(vp); break;
                case 10:
                    titleEl.textContent = "Invertebrates II: Annelida to Echinodermata";
                    renderSim11(vp); break;
                case 11:
                    titleEl.textContent = "Vertebrate Spectrum: Hearts & Circulation";
                    renderSim12(vp); break;
                case 12:
                    titleEl.textContent = "Linnaean Nomenclature Formatter & Rule Engine";
                    renderSim13(vp); break;
                case 13:
                    titleEl.textContent = "Indian Biodiversity Flora & Fauna Explorer";
                    renderSim14(vp); break;
                case 14:
                    titleEl.textContent = "Acellular Entities: Viruses, Viroids & Prions";
                    renderSim15(vp); break;
                case 15:
                    titleEl.textContent = "Ecosystem Synergy & Conservation Framework";
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
                    <div class="w-16 h-16 rounded-2xl bg-emerald-950 border border-emerald-500/50 flex items-center justify-center text-emerald-400 shadow-xl shadow-emerald-950/50">
                        <i data-lucide="award" class="w-8 h-8"></i>
                    </div>
                    <h4 class="text-sm font-bold text-white">Quiz Challenge Module #${{quizNum}}</h4>
                    <p class="text-xs text-slate-300 leading-relaxed max-w-xs">
                        Answer all 10 in-depth questions. Use 'View Solution' for detailed step-by-step reasoning on NCERT criteria!
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 w-full text-left font-mono text-[11px] text-slate-300 space-y-1">
                        <div class="flex justify-between"><span>Curriculum Standard:</span><span class="text-emerald-400">NCERT Class 9</span></div>
                        <div class="flex justify-between"><span>Total Questions:</span><span class="text-white">10 MCQs</span></div>
                        <div class="flex justify-between"><span>Pass Standard:</span><span class="text-amber-400">80%+ Mastery</span></div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        // SIMULATOR 1: Taxonomic Hierarchy Ladder (Kingdom to Species)
        function renderSim1(vp) {{
            let tier = 0; // 0: Kingdom, 1: Phylum, 2: Class, 3: Order, 4: Family, 5: Genus, 6: Species
            const tiers = [
                {{ name: "Kingdom", human: "Animalia", tiger: "Animalia", spec: "Broadest grouping (~8.7M species)", shared: "Fewest common traits" }},
                {{ name: "Phylum / Division", human: "Chordata", tiger: "Chordata", spec: "Dorsal nerve cord, notochord", shared: "Major anatomical plan" }},
                {{ name: "Class", human: "Mammalia", tiger: "Mammalia", spec: "Mammary glands, hair, 4-chambered heart", shared: "Thermal & physiological traits" }},
                {{ name: "Order", human: "Primates", tiger: "Carnivora", spec: "Carnassial teeth (tiger) / Opposable thumb (human)", shared: "Functional ecological adaptations" }},
                {{ name: "Family", human: "Hominidae", tiger: "Felidae", spec: "Retractile claws, specialized skull", shared: "Closely related genera" }},
                {{ name: "Genus", human: "Homo", tiger: "Panthera", spec: "Roaring cats with ossified hyoid apparatus", shared: "Very high similarity" }},
                {{ name: "Species", human: "Homo sapiens", tiger: "Panthera tigris", spec: "Basic unit of classification, interbreeding", shared: "Maximum common characteristics" }}
            ];

            function draw() {{
                const cur = tiers[tier];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Select Taxonomic Rank:</span>
                            <span class="text-emerald-400 font-bold">${{cur.name}}</span>
                        </div>

                        <!-- 7 Rank Buttons -->
                        <div class="grid grid-cols-7 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            ${{tiers.map((t, idx) => `
                                <button onclick="window.sim1SetTier(${{idx}})" class="py-1 rounded text-center transition ${{tier === idx ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                    ${{t.name[0]}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Graphical Hierarchy Pyramid / Steps SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Inverted Pyramid / Tier Bands -->
                                ${{tiers.map((t, idx) => {{
                                    const y = 10 + idx * 19;
                                    const w = 240 - idx * 26;
                                    const x = 125 - w / 2;
                                    const isSel = idx === tier;
                                    return `
                                        <g onclick="window.sim1SetTier(${{idx}})" class="cursor-pointer">
                                            <rect x="${{x}}" y="${{y}}" width="${{w}}" height="16" rx="3" fill="${{isSel ? '#059669' : '#1e293b'}}" stroke="${{isSel ? '#34d399' : '#334155'}}" stroke-width="${{isSel ? 2 : 1}}"/>
                                            <text x="125" y="${{y + 11}}" fill="${{isSel ? '#ffffff' : '#94a3b8'}}" font-size="9" font-family="JetBrains Mono" font-weight="${{isSel ? 'bold' : 'normal'}}" text-anchor="middle">${{t.name}}</text>
                                        </g>
                                    `;
                                }}).join('')}}
                            </svg>
                        </div>

                        <!-- Info Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1 text-xs">
                            <div class="flex justify-between font-mono text-[11px]">
                                <span class="text-slate-400">Tiger (Panthera tigris):</span>
                                <span class="text-amber-400 font-bold">${{cur.tiger}}</span>
                            </div>
                            <div class="flex justify-between font-mono text-[11px]">
                                <span class="text-slate-400">Human (Homo sapiens):</span>
                                <span class="text-cyan-400 font-bold">${{cur.human}}</span>
                            </div>
                            <p class="text-[11px] text-slate-300 pt-1 border-t border-slate-800/80">
                                <strong>Rule:</strong> Moving downward towards Species, common characteristics <em>increase</em> while total diversity <em>decreases</em>.
                            </p>
                        </div>
                    </div>
                `;
            }}

            window.sim1SetTier = function(idx) {{
                tier = idx;
                playTone(350 + idx * 60, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 2: 4-Axis Classification Filter Matrix
        function renderSim2(vp) {{
            let cellType = 'eukaryotic'; // prokaryotic, eukaryotic
            let cellOrg = 'multicellular'; // unicellular, multicellular
            let nutrition = 'heterotrophic'; // autotrophic, heterotrophic
            let cellWall = 'chitin'; // peptidoglycan, cellulose, chitin, none

            function getKingdom() {{
                if (cellType === 'prokaryotic') return {{ name: 'Monera', desc: 'Bacteria, Cyanobacteria, Mycoplasma. Lack defined nucleus; peptidoglycan wall.', color: 'text-amber-400' }};
                if (cellOrg === 'unicellular') return {{ name: 'Protista', desc: 'Amoeba, Paramecium, Euglena. Unicellular eukaryotes with cilia/flagella.', color: 'text-cyan-400' }};
                if (nutrition === 'autotrophic' && cellWall === 'cellulose') return {{ name: 'Plantae', desc: 'Mosses, Ferns, Angiosperms. Multicellular autotrophic producers with cellulose wall.', color: 'text-emerald-400' }};
                if (nutrition === 'heterotrophic' && cellWall === 'chitin') return {{ name: 'Fungi', desc: 'Yeast, Agaricus (Mushroom), Penicillium. Saprophytic decomposers with chitin wall.', color: 'text-purple-400' }};
                if (cellWall === 'none') return {{ name: 'Animalia', desc: 'Insects, Fish, Birds, Mammals. Multicellular holozoic consumers lacking cell wall.', color: 'text-rose-400' }};
                return {{ name: 'Mixed/Special Group', desc: 'Explore differing evolutionary adaptations.', color: 'text-slate-300' }};
            }}

            function draw() {{
                const k = getKingdom();
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 text-[10px] font-mono">
                            <!-- Axis 1: Nucleus -->
                            <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
                                <span class="text-slate-400 block mb-1">1. Cellular Organization:</span>
                                <div class="grid grid-cols-2 gap-1">
                                    <button onclick="window.sim2Set('cellType', 'prokaryotic')" class="py-1 rounded text-center ${{cellType === 'prokaryotic' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Prokaryote</button>
                                    <button onclick="window.sim2Set('cellType', 'eukaryotic')" class="py-1 rounded text-center ${{cellType === 'eukaryotic' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Eukaryote</button>
                                </div>
                            </div>

                            <!-- Axis 2: Body -->
                            <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
                                <span class="text-slate-400 block mb-1">2. Body Structure:</span>
                                <div class="grid grid-cols-2 gap-1">
                                    <button onclick="window.sim2Set('cellOrg', 'unicellular')" class="py-1 rounded text-center ${{cellOrg === 'unicellular' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Unicellular</button>
                                    <button onclick="window.sim2Set('cellOrg', 'multicellular')" class="py-1 rounded text-center ${{cellOrg === 'multicellular' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Multicellular</button>
                                </div>
                            </div>

                            <!-- Axis 3: Nutrition -->
                            <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
                                <span class="text-slate-400 block mb-1">3. Mode of Nutrition:</span>
                                <div class="grid grid-cols-2 gap-1">
                                    <button onclick="window.sim2Set('nutrition', 'autotrophic')" class="py-1 rounded text-center ${{nutrition === 'autotrophic' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Autotroph</button>
                                    <button onclick="window.sim2Set('nutrition', 'heterotrophic')" class="py-1 rounded text-center ${{nutrition === 'heterotrophic' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Heterotroph</button>
                                </div>
                            </div>

                            <!-- Axis 4: Cell Wall -->
                            <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
                                <span class="text-slate-400 block mb-1">4. Cell Wall Chemistry:</span>
                                <div class="grid grid-cols-3 gap-1">
                                    <button onclick="window.sim2Set('cellWall', 'cellulose')" class="py-1 rounded text-center text-[9px] ${{cellWall === 'cellulose' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Cellulose</button>
                                    <button onclick="window.sim2Set('cellWall', 'chitin')" class="py-1 rounded text-center text-[9px] ${{cellWall === 'chitin' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Chitin</button>
                                    <button onclick="window.sim2Set('cellWall', 'none')" class="py-1 rounded text-center text-[9px] ${{cellWall === 'none' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Absent</button>
                                </div>
                            </div>
                        </div>

                        <!-- Result Display Box -->
                        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex flex-col gap-1 items-center text-center">
                            <span class="text-[10px] text-slate-400 uppercase tracking-widest font-mono">Matched Kingdom:</span>
                            <span class="text-base font-extrabold font-mono ${{k.color}}">Kingdom ${{k.name}}</span>
                            <p class="text-xs text-slate-300 mt-1">${{k.desc}}</p>
                        </div>
                    </div>
                `;
            }}

            window.sim2Set = function(axis, val) {{
                if (axis === 'cellType') cellType = val;
                if (axis === 'cellOrg') cellOrg = val;
                if (axis === 'nutrition') nutrition = val;
                if (axis === 'cellWall') cellWall = val;
                playTone(480, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 3: 5-Kingdom Phylogenetic Tree & Trophic Web
        function renderSim3(vp) {{
            let selK = 'plantae'; // monera, protista, fungi, plantae, animalia
            const kData = {{
                monera: {{ name: 'Monera', role: 'Decomposers / Primary Fixers', wall: 'Peptidoglycan (Non-cellulosic)', energy: 'Absorptive / Photosynthetic / Chemosynthetic', ex: 'Anabaena, Rhizobium, E. coli' }},
                protista: {{ name: 'Protista', role: 'Aquatic Plankton / Primary Links', wall: 'Present in some, absent in others', energy: 'Photosynthetic / Phagocytic ingestion', ex: 'Diatoms, Amoeba, Euglena' }},
                fungi: {{ name: 'Fungi', role: 'Major Terrestrial Decomposers', wall: 'Chitin (Polysaccharide polymer)', energy: 'Saprophytic extracellular digestion', ex: 'Agaricus (Mushroom), Yeast, Aspergillus' }},
                plantae: {{ name: 'Plantae', role: 'Primary Autotrophic Producers', wall: 'Cellulose & Pectin', energy: 'Oxygenic Photosynthesis (Chloroplasts)', ex: 'Mosses, Ferns, Mango, Rice' }},
                animalia: {{ name: 'Animalia', role: 'Primary & Secondary Consumers', wall: 'Completely Absent', energy: 'Holozoic ingestion & internal digestion', ex: 'Insects, Birds, Tiger, Humans' }}
            }};

            function draw() {{
                const d = kData[selK];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            ${{['monera', 'protista', 'fungi', 'plantae', 'animalia'].map(k => `
                                <button onclick="window.sim3Set('${{k}}')" class="py-1.5 rounded text-center transition ${{selK === k ? 'bg-emerald-600 text-white shadow' : 'bg-slate-800 text-slate-400'}}">
                                    ${{k[0].toUpperCase() + k.slice(1)}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Trophic Energy Flow Diagram -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                <!-- Sun Energy -->
                                <circle cx="30" cy="25" r="14" fill="#fbbf24" opacity="0.8"/>
                                <text x="30" y="28" fill="#78350f" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Sun</text>

                                <!-- Kingdom Boxes -->
                                <!-- Plantae (Producers) -->
                                <rect x="80" y="20" width="85" height="24" rx="4" fill="${{selK === 'plantae' ? '#059669' : '#064e3b'}}" stroke="#34d399" stroke-width="${{selK === 'plantae' ? 2 : 1}}"/>
                                <text x="122" y="35" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Plantae (Producers)</text>

                                <!-- Animalia (Consumers) -->
                                <rect x="155" y="70" width="85" height="24" rx="4" fill="${{selK === 'animalia' ? '#e11d48' : '#881337'}}" stroke="#fb7185" stroke-width="${{selK === 'animalia' ? 2 : 1}}"/>
                                <text x="197" y="85" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Animalia (Consumers)</text>

                                <!-- Fungi (Decomposers) -->
                                <rect x="30" y="70" width="85" height="24" rx="4" fill="${{selK === 'fungi' ? '#9333ea' : '#581c87'}}" stroke="#c084fc" stroke-width="${{selK === 'fungi' ? 2 : 1}}"/>
                                <text x="72" y="85" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Fungi (Decomposers)</text>

                                <!-- Monera / Protista Base -->
                                <rect x="10" y="115" width="105" height="22" rx="4" fill="${{selK === 'monera' ? '#d97706' : '#78350f'}}" stroke="#f59e0b" stroke-width="${{selK === 'monera' ? 2 : 1}}"/>
                                <text x="62" y="129" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Monera (Prokaryotes)</text>

                                <rect x="135" y="115" width="105" height="22" rx="4" fill="${{selK === 'protista' ? '#0891b2' : '#164e63'}}" stroke="#22d3ee" stroke-width="${{selK === 'protista' ? 2 : 1}}"/>
                                <text x="187" y="129" fill="#ffffff" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Protista (Unicell Euk)</text>

                                <!-- Arrows -->
                                <path d="M 45 25 L 80 30" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
                                <path d="M 122 45 L 175 70" stroke="#10b981" stroke-width="1.5"/>
                                <path d="M 180 95 L 95 85" stroke="#fb7185" stroke-width="1.5"/>
                                <path d="M 60 95 L 60 115" stroke="#c084fc" stroke-width="1.5"/>
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">Ecological Role:</span><span class="text-emerald-400 font-bold">${{d.role}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Cell Wall:</span><span class="text-slate-200">${{d.wall}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Examples:</span><span class="text-teal-300">${{d.ex}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim3Set = function(k) {{
                selK = k;
                playTone(420, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 4: Carl Woese 3-Domain Molecular Tree (16S rRNA) (C-7.1)
        function renderSim4(vp) {{
            let domain = 'archaea'; // archaea, bacteria, eukarya

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono font-bold">
                            <button onclick="window.sim4Set('archaea')" class="py-1.5 rounded transition ${{domain === 'archaea' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Domain Archaea</button>
                            <button onclick="window.sim4Set('bacteria')" class="py-1.5 rounded transition ${{domain === 'bacteria' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Domain Bacteria</button>
                            <button onclick="window.sim4Set('eukarya')" class="py-1.5 rounded transition ${{domain === 'eukarya' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Domain Eukarya</button>
                        </div>

                        <!-- Molecular Comparison Graphic -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="250" height="150" viewBox="0 0 250 150">
                                ${{domain === 'archaea' ? `
                                    <!-- Ether Linked Branched Lipids -->
                                    <rect x="25" y="25" width="200" height="95" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
                                    <text x="125" y="48" fill="#fef3c7" font-size="11" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Archaea (Extremophiles)</text>
                                    <text x="125" y="68" fill="#fde68a" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Ether-linked branched lipids</text>
                                    <text x="125" y="84" fill="#fde68a" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• 16S rRNA unique phylogenetic clade</text>
                                    <text x="125" y="100" fill="#fde68a" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Methanogens, Halophiles, Thermophiles</text>
                                ` : domain === 'bacteria' ? `
                                    <!-- Peptidoglycan & Ester Linked Lipids -->
                                    <rect x="25" y="25" width="200" height="95" rx="6" fill="#164e63" stroke="#22d3ee" stroke-width="2"/>
                                    <text x="125" y="48" fill="#cffafe" font-size="11" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Bacteria (Eubacteria)</text>
                                    <text x="125" y="68" fill="#a5f3fc" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Ester-linked unbranched lipids</text>
                                    <text x="125" y="84" fill="#a5f3fc" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Peptidoglycan cell wall present</text>
                                    <text x="125" y="100" fill="#a5f3fc" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Cyanobacteria, E. coli, Rhizobium</text>
                                ` : `
                                    <!-- True Nucleus & Organelles -->
                                    <rect x="25" y="25" width="200" height="95" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                                    <text x="125" y="48" fill="#d1fae5" font-size="11" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Eukarya (Eukaryotes)</text>
                                    <text x="125" y="68" fill="#a7f3d0" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• 18S rRNA molecular machinery</text>
                                    <text x="125" y="84" fill="#a7f3d0" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Membrane-enclosed nucleus & organelles</text>
                                    <text x="125" y="100" fill="#a7f3d0" font-size="9" font-family="JetBrains Mono" text-anchor="middle">• Protista, Fungi, Plantae, Animalia</text>
                                `}}
                            </svg>
                        </div>

                        <!-- C-7.1 Scientific Significance Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            <strong>Carl Woese (1977):</strong> By analyzing 16S/18S rRNA sequences, Woese discovered that Archaea are as evolutionarily distinct from Bacteria as Bacteria are from Humans!
                        </div>
                    </div>
                `;
            }}

            window.sim4Set = function(d) {{
                domain = d;
                playTone(d === 'archaea' ? 380 : d === 'bacteria' ? 460 : 540, 0.1);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 5: Lichen Symbiosis & SO2 Air Pollution Sensor (C-2.8)
        function renderSim5(vp) {{
            let so2 = 10; // 0 to 100 ppb

            function getStatus(val) {{
                if (val < 20) return {{ type: 'Fruticose (Shrubby)', color: 'text-emerald-400', bar: '#10b981', note: 'Pristine Air Quality. Luxuriant branching lichens thrive on tree bark.' }};
                if (val < 50) return {{ type: 'Foliose (Leaf-like)', color: 'text-amber-400', bar: '#f59e0b', note: 'Moderate Air Pollution. Delicate fruticose species eliminated.' }};
                if (val < 75) return {{ type: 'Crustose (Crust-like)', color: 'text-orange-400', bar: '#f97316', note: 'High SO2 Pollution. Only flat, tightly clinging crustose lichens survive.' }};
                return {{ type: 'Lichen Desert (Barren)', color: 'text-rose-400', bar: '#ef4444', note: 'Critical Industrial Smog! Lichens destroyed due to SO2 toxicity; dead rock.' }};
            }}

            function draw() {{
                const st = getStatus(so2);
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Atmospheric SO2 Level:</span>
                            <span class="font-bold font-mono text-white">${{so2}} ppb</span>
                        </div>

                        <input type="range" min="5" max="95" value="${{so2}}" oninput="window.sim5SetSO2(this.value)" class="w-full accent-emerald-500">

                        <!-- Graphic Bio-Indicator Simulation -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44 relative overflow-hidden">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                <!-- Tree Trunk or Rock Background -->
                                <rect x="20" y="10" width="70" height="130" fill="#3f2d21" rx="4"/>
                                <path d="M 35 15 L 35 135" stroke="#2a1f17" stroke-width="2"/>
                                <path d="M 65 15 L 65 135" stroke="#2a1f17" stroke-width="2"/>

                                <!-- Lichen Colony Growth on Bark -->
                                ${{so2 < 20 ? `
                                    <!-- Fruticose Bushy Lichen (Green) -->
                                    <path d="M 70 40 Q 110 30 130 50 Q 150 40 160 65 Q 120 75 80 60 Z" fill="#10b981" opacity="0.9"/>
                                    <path d="M 70 70 Q 120 60 140 85 Q 160 90 140 110 Q 100 100 75 85 Z" fill="#34d399" opacity="0.8"/>
                                    <circle cx="130" cy="50" r="4" fill="#a7f3d0"/>
                                    <text x="180" y="45" fill="#34d399" font-size="8" font-family="JetBrains Mono">Usnea (Fruticose)</text>
                                ` : so2 < 50 ? `
                                    <!-- Foliose Leafy Lichen -->
                                    <ellipse cx="95" cy="65" rx="30" ry="20" fill="#f59e0b" opacity="0.85"/>
                                    <ellipse cx="105" cy="85" rx="25" ry="18" fill="#fbbf24" opacity="0.75"/>
                                    <text x="140" y="70" fill="#f59e0b" font-size="8" font-family="JetBrains Mono">Parmelia (Foliose)</text>
                                ` : so2 < 75 ? `
                                    <!-- Crustose Flat Crust -->
                                    <rect x="70" y="55" width="20" height="40" fill="#ea580c" opacity="0.9" rx="2"/>
                                    <rect x="70" y="30" width="15" height="15" fill="#f97316" opacity="0.8" rx="2"/>
                                    <text x="105" y="65" fill="#f97316" font-size="8" font-family="JetBrains Mono">Lecanora (Crustose)</text>
                                ` : `
                                    <!-- Lichen Desert -->
                                    <text x="110" y="75" fill="#ef4444" font-size="10" font-family="JetBrains Mono" font-weight="bold">LICHEN DESERT</text>
                                    <text x="110" y="90" fill="#94a3b8" font-size="8" font-family="JetBrains Mono">Severe SO2 Toxicity</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Status Box -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between">
                                <span class="text-slate-400">Bio-Indicator Status:</span>
                                <span class="font-bold ${{st.color}}">${{st.type}}</span>
                            </div>
                            <p class="text-[10px] text-slate-300 leading-relaxed">${{st.note}}</p>
                        </div>
                    </div>
                `;
            }}

            window.sim5SetSO2 = function(val) {{
                so2 = parseInt(val);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 6: Plant Evolutionary Decision Flowchart
        function renderSim6(vp) {{
            let step = 1; // 1: Body diff?, 2: Vascular?, 3: Seeds?, 4: Naked/Enclosed?
            const branches = [
                {{
                    q: "1. Does the plant possess a differentiated body (roots, stem, leaves)?",
                    no: {{ label: "No: Undifferentiated Thallus", group: "Division Thallophyta (Algae: Spirogyra, Ulothrix, Chara)" }},
                    yes: {{ label: "Yes: Body Differentiated", next: 2 }}
                }},
                {{
                    q: "2. Does the plant possess specialized vascular tissue (xylem/phloem)?",
                    no: {{ label: "No: Non-Vascular Amphibians", group: "Division Bryophyta (Funaria, Marchantia, Riccia)" }},
                    yes: {{ label: "Yes: Vascular Tissues Present", next: 3 }}
                }},
                {{
                    q: "3. Does the plant produce seeds (Phanerogams)?",
                    no: {{ label: "No: Seedless Cryptogams", group: "Division Pteridophyta (Ferns, Marsilea, Equisetum)" }},
                    yes: {{ label: "Yes: Seed-bearing Phanerogams", next: 4 }}
                }},
                {{
                    q: "4. Are seeds naked inside cones or enclosed inside a fruit ovary?",
                    naked: {{ label: "Naked Seeds in Cones", group: "Gymnosperms (Pinus, Cycas, Deodar)" }},
                    enclosed: {{ label: "Enclosed Seeds inside Fruit", group: "Angiosperms (Monocots & Dicots: Flowering Plants)" }}
                }}
            ];

            function draw() {{
                const cur = branches[step - 1];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-3">
                        <div class="flex items-center justify-between text-xs font-mono">
                            <span class="text-slate-400">Plant Kingdom Branching:</span>
                            <span class="text-emerald-400 font-bold">Step ${{step}} of 4</span>
                        </div>

                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs font-semibold text-white">
                            ${{cur.q}}
                        </div>

                        <!-- Interactive Step Selector Buttons -->
                        <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                            ${{step < 4 ? `
                                <button onclick="window.sim6Choose('no')" class="p-2 rounded-lg bg-rose-950/80 hover:bg-rose-900/80 border border-rose-700/60 text-rose-300 text-left">
                                    <div class="font-bold">${{cur.no.label}}</div>
                                    <div class="text-[10px] text-slate-300 mt-1">${{cur.no.group}}</div>
                                </button>
                                <button onclick="window.sim6Choose('yes')" class="p-2 rounded-lg bg-emerald-950/80 hover:bg-emerald-900/80 border border-emerald-700/60 text-emerald-300 text-left">
                                    <div class="font-bold">${{cur.yes.label}}</div>
                                    <div class="text-[10px] text-slate-300 mt-1">Advance to Step ${{cur.yes.next}} →</div>
                                </button>
                            ` : `
                                <button onclick="window.sim6Choose('naked')" class="p-2 rounded-lg bg-amber-950/80 hover:bg-amber-900/80 border border-amber-700/60 text-amber-300 text-left">
                                    <div class="font-bold">${{cur.naked.label}}</div>
                                    <div class="text-[10px] text-slate-300 mt-1">${{cur.naked.group}}</div>
                                </button>
                                <button onclick="window.sim6Choose('enclosed')" class="p-2 rounded-lg bg-teal-950/80 hover:bg-teal-900/80 border border-teal-700/60 text-teal-300 text-left">
                                    <div class="font-bold">${{cur.enclosed.label}}</div>
                                    <div class="text-[10px] text-slate-300 mt-1">${{cur.enclosed.group}}</div>
                                </button>
                            `}}
                        </div>

                        <!-- Reset / Navigation Step Buttons -->
                        <div class="flex items-center justify-between pt-1">
                            <button onclick="window.sim6Reset()" class="text-[11px] font-mono px-3 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">
                                ↺ Restart Flowchart
                            </button>
                            <span class="text-[10px] font-mono text-slate-400">Class 9 Taxonomic Standard</span>
                        </div>
                    </div>
                `;
            }}

            window.sim6Choose = function(choice) {{
                playTone(450, 0.08);
                if (step < 4) {{
                    if (choice === 'yes') step = branches[step - 1].yes.next;
                }}
                draw();
            }};

            window.sim6Reset = function() {{
                step = 1;
                draw();
            }};

            draw();
        }}

        // SIMULATOR 7: Cryptogam 3-Way Diagnostic Comparator
        function renderSim7(vp) {{
            let mode = 'thallophyta'; // thallophyta, bryophyta, pteridophyta

            const d = {{
                thallophyta: {{
                    title: "Thallophyta (Algae)",
                    hab: "Predominantly aquatic (freshwater & marine)",
                    vasc: "Absent (no xylem or phloem)",
                    body: "Undifferentiated green thallus",
                    ex: "Spirogyra (ribbon chloroplast), Ulothrix, Chara"
                }},
                bryophyta: {{
                    title: "Bryophyta (Amphibians of Plant Kingdom)",
                    hab: "Terrestrial damp soil, but water required for fertilization",
                    vasc: "Absent (water conduction by simple parenchyma)",
                    body: "Thalloid or leafy shoot with unicellular/multicellular rhizoids",
                    ex: "Funaria (Moss), Marchantia (Liverwort), Riccia"
                }},
                pteridophyta: {{
                    title: "Pteridophyta (First Vascular Cryptogams)",
                    hab: "Cool, shady, damp terrestrial habitats",
                    vasc: "True Xylem & Phloem conduits present",
                    body: "Well-differentiated true roots, underground stem & fronds",
                    ex: "Marsilea, Ferns (Dryopteris), Equisetum (Horsetail)"
                }}
            }};

            function draw() {{
                const cur = d[mode];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim7Set('thallophyta')" class="py-1 rounded ${{mode === 'thallophyta' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Thallophyta</button>
                            <button onclick="window.sim7Set('bryophyta')" class="py-1 rounded ${{mode === 'bryophyta' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Bryophyta</button>
                            <button onclick="window.sim7Set('pteridophyta')" class="py-1 rounded ${{mode === 'pteridophyta' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Pteridophyta</button>
                        </div>

                        <!-- Graphical Specimen SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'thallophyta' ? `
                                    <!-- Spirogyra Filament -->
                                    <rect x="30" y="45" width="180" height="60" rx="3" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                                    <path d="M 30 75 Q 60 50 90 75 Q 120 100 150 75 Q 180 50 210 75" fill="none" stroke="#34d399" stroke-width="4"/>
                                    <circle cx="65" cy="62" r="3" fill="#a7f3d0"/>
                                    <circle cx="125" cy="88" r="3" fill="#a7f3d0"/>
                                    <circle cx="175" cy="62" r="3" fill="#a7f3d0"/>
                                    <text x="120" y="32" fill="#34d399" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Spirogyra: Spiral Ribbon Chloroplast</text>
                                ` : mode === 'bryophyta' ? `
                                    <!-- Funaria Moss Plant with Capsule -->
                                    <path d="M 120 130 L 120 70" stroke="#059669" stroke-width="3"/>
                                    <!-- Leafy Gametophyte Base -->
                                    <path d="M 105 110 L 120 95 L 135 110" fill="none" stroke="#10b981" stroke-width="2"/>
                                    <path d="M 100 125 L 120 110 L 140 125" fill="none" stroke="#10b981" stroke-width="2"/>
                                    <!-- Rhizoids -->
                                    <path d="M 120 130 L 110 145 M 120 130 L 125 145 M 120 130 L 132 143" stroke="#92400e" stroke-width="1.5"/>
                                    <!-- Seta & Capsule -->
                                    <path d="M 120 70 Q 115 45 130 35" fill="none" stroke="#d97706" stroke-width="1.5"/>
                                    <ellipse cx="132" cy="33" rx="7" ry="5" fill="#b45309"/>
                                    <text x="120" y="20" fill="#f59e0b" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Funaria: Capsule Sporophyte on Gametophyte</text>
                                ` : `
                                    <!-- Fern with Fronds & Sori -->
                                    <path d="M 80 140 Q 110 100 120 40" fill="none" stroke="#059669" stroke-width="2.5"/>
                                    <path d="M 100 80 Q 70 70 60 75" fill="none" stroke="#10b981" stroke-width="2"/>
                                    <path d="M 107 65 Q 140 55 150 60" fill="none" stroke="#10b981" stroke-width="2"/>
                                    <path d="M 115 50 Q 85 40 75 45" fill="none" stroke="#10b981" stroke-width="2"/>
                                    <!-- Sori dots -->
                                    <circle cx="70" cy="74" r="2.5" fill="#78350f"/>
                                    <circle cx="140" cy="58" r="2.5" fill="#78350f"/>
                                    <!-- Rhizome & Roots -->
                                    <path d="M 60 142 L 100 142" stroke="#78350f" stroke-width="3"/>
                                    <text x="120" y="22" fill="#34d399" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Fern Frond with Spore-bearing Sori</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex justify-between"><span class="text-slate-400">Habitat:</span><span class="text-white">${{cur.hab}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Vascular Bundles:</span><span class="text-amber-400 font-bold">${{cur.vasc}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Examples:</span><span class="text-teal-300 font-semibold">${{cur.ex}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim7Set = function(m) {{
                mode = m;
                playTone(430, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 8: Phanerogam Lab (Gymnosperms vs Angiosperms)
        function renderSim8(vp) {{
            let mode = 'gymno'; // gymno vs angio

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono font-bold">
                            <button onclick="window.sim8Set('gymno')" class="py-1.5 rounded ${{mode === 'gymno' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Gymnosperms (Naked)</button>
                            <button onclick="window.sim8Set('angio')" class="py-1.5 rounded ${{mode === 'angio' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Angiosperms (Enclosed)</button>
                        </div>

                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'gymno' ? `
                                    <!-- Pine Cone with Exposed Naked Seeds -->
                                    <ellipse cx="120" cy="80" rx="35" ry="50" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                                    <!-- Cone Scales -->
                                    <path d="M 95 60 Q 120 70 145 60" fill="none" stroke="#d97706" stroke-width="2"/>
                                    <path d="M 90 80 Q 120 90 150 80" fill="none" stroke="#d97706" stroke-width="2"/>
                                    <path d="M 95 100 Q 120 110 145 100" fill="none" stroke="#d97706" stroke-width="2"/>
                                    <!-- Naked Seed on Scale -->
                                    <ellipse cx="130" cy="74" rx="4" ry="7" fill="#fbbf24"/>
                                    <text x="120" y="22" fill="#f59e0b" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Pinus: Naked Ovules on Cone Scales</text>
                                    <text x="120" y="142" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Gymnos = Naked • Sperma = Seed</text>
                                ` : `
                                    <!-- Flower Ovary enclosing Seeds (Angiosperm) -->
                                    <path d="M 120 40 L 120 85" stroke="#059669" stroke-width="3"/>
                                    <!-- Swollen Ovary Carpel -->
                                    <ellipse cx="120" cy="100" rx="35" ry="30" fill="#065f46" stroke="#34d399" stroke-width="2"/>
                                    <!-- Enclosed Ovule Seeds Inside -->
                                    <circle cx="110" cy="98" r="6" fill="#fbbf24"/>
                                    <circle cx="130" cy="98" r="6" fill="#fbbf24"/>
                                    <!-- Petals around -->
                                    <path d="M 85 90 Q 55 50 85 45 Q 105 70 85 90 Z" fill="#f43f5e" opacity="0.8"/>
                                    <path d="M 155 90 Q 185 50 155 45 Q 135 70 155 90 Z" fill="#f43f5e" opacity="0.8"/>
                                    <text x="120" y="22" fill="#34d399" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Enclosed Ovary develops into Fruit</text>
                                    <text x="120" y="142" fill="#94a3b8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Angion = Covered • Sperma = Seed</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Diagnostic Fact -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'gymno' ? 
                                '<strong class="text-amber-400">Gymnosperms:</strong> Perennial, evergreen, woody conifers (Pinus, Cycas). Seeds develop without fruit wall.' : 
                                '<strong class="text-emerald-400">Angiosperms:</strong> Highly evolved flowering plants. Divided into <em>Monocotyledons</em> (parallel veins, fibrous roots) and <em>Dicotyledons</em> (reticulate veins, taproots).'}}
                        </div>
                    </div>
                `;
            }}

            window.sim8Set = function(m) {{
                mode = m;
                playTone(m === 'gymno' ? 440 : 520, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 9: Animal Coelom Architecture & Body Plan
        function renderSim9(vp) {{
            let cType = 'eucoelomate'; // acoelomate, pseudocoelomate, eucoelomate

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim9Set('acoelomate')" class="py-1 rounded ${{cType === 'acoelomate' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Acoelomate</button>
                            <button onclick="window.sim9Set('pseudocoelomate')" class="py-1 rounded ${{cType === 'pseudocoelomate' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}}">Pseudocoel</button>
                            <button onclick="window.sim9Set('eucoelomate')" class="py-1 rounded ${{cType === 'eucoelomate' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Eucoelomate</button>
                        </div>

                        <!-- Cross Section SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                <!-- Outer Ectoderm (Blue) -->
                                <circle cx="120" cy="75" r="62" fill="none" stroke="#3b82f6" stroke-width="4"/>
                                <text x="120" y="10" fill="#60a5fa" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Ectoderm (Outer Body Wall)</text>

                                <!-- Central Gut Endoderm (Yellow) -->
                                <circle cx="120" cy="75" r="16" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
                                <text x="120" y="78" fill="#713f12" font-size="8" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Gut</text>

                                ${{cType === 'acoelomate' ? `
                                    <!-- Solid Mesoderm (Red/Purple) - No Cavity -->
                                    <circle cx="120" cy="75" r="60" fill="#a855f7" opacity="0.35"/>
                                    <text x="120" y="142" fill="#c084fc" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Platyhelminthes: Solid Mesenchyme</text>
                                ` : cType === 'pseudocoelomate' ? `
                                    <!-- Mesoderm in scattered pouches (Nematoda) -->
                                    <circle cx="95" cy="55" r="10" fill="#f59e0b" opacity="0.8"/>
                                    <circle cx="145" cy="55" r="10" fill="#f59e0b" opacity="0.8"/>
                                    <circle cx="95" cy="95" r="10" fill="#f59e0b" opacity="0.8"/>
                                    <circle cx="145" cy="95" r="10" fill="#f59e0b" opacity="0.8"/>
                                    <text x="120" y="142" fill="#fbbf24" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Nematoda: False Cavity (Scattered Pouches)</text>
                                ` : `
                                    <!-- True Coelom lined by Mesoderm Peritoneum -->
                                    <circle cx="120" cy="75" r="50" fill="none" stroke="#10b981" stroke-width="8" opacity="0.4"/>
                                    <circle cx="120" cy="75" r="30" fill="none" stroke="#10b981" stroke-width="8" opacity="0.4"/>
                                    <text x="120" y="44" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">True Coelom Cavity</text>
                                    <text x="120" y="142" fill="#34d399" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Annelids to Mammals: True Peritoneal Cavity</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Architectural Description -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{cType === 'acoelomate' ? 'No cavity between body wall and gut (e.g. Planaria, Tapeworm).' :
                                cType === 'pseudocoelomate' ? 'Cavity present but not lined by mesoderm peritoneum (e.g. Ascaris).' :
                                'True body cavity entirely bounded by mesoderm, allowing independent visceral organ motion.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim9Set = function(t) {{
                cType = t;
                playTone(480, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 10: Invertebrates I (Porifera, Cnidaria, Platyhelminthes, Nematoda)
        function renderSim10(vp) {{
            let phy = 'porifera'; // porifera, cnidaria, platy, nematoda
            const data = {{
                porifera: {{ title: "Phylum Porifera (Sponges)", trait: "Cellular grade, porous body with Ostia and Osculum water canal system", ex: "Sycon, Spongilla, Euplectella" }},
                cnidaria: {{ title: "Phylum Coelenterata / Cnidaria", trait: "Tissue grade, blind sac gastrovascular cavity, stinging cnidocytes", ex: "Hydra, Aurelia (Jellyfish), Sea Anemone" }},
                platy: {{ title: "Phylum Platyhelminthes", trait: "Organ grade, dorsoventrally flattened, bilateral symmetry, flame cells", ex: "Planaria (regeneration), Fasciola (Liver Fluke), Taenia" }},
                nematoda: {{ title: "Phylum Nematoda", trait: "Organ system, cylindrical pseudocoelomate worms, complete gut", ex: "Ascaris (roundworm), Wuchereria (causes elephantiasis)" }}
            }};

            function draw() {{
                const cur = data[phy];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[9px] font-mono font-bold">
                            ${{['porifera', 'cnidaria', 'platy', 'nematoda'].map(p => `
                                <button onclick="window.sim10Set('${{p}}')" class="py-1.5 rounded text-center ${{phy === p ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    ${{p.slice(0, 4).toUpperCase()}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Graphical Specimen -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{phy === 'porifera' ? `
                                    <!-- Sycon Sponge Canal Model -->
                                    <path d="M 80 140 Q 60 80 90 35 L 150 35 Q 180 80 160 140 Z" fill="#047857" stroke="#10b981" stroke-width="2"/>
                                    <!-- Osculum Top Opening -->
                                    <ellipse cx="120" cy="35" rx="30" ry="8" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                                    <!-- Water Flow Arrows -->
                                    <text x="120" y="20" fill="#38bdf8" font-size="9" font-family="JetBrains Mono" text-anchor="middle">↑ Water Out (Osculum)</text>
                                    <circle cx="85" cy="70" r="2" fill="#38bdf8"/>
                                    <circle cx="155" cy="70" r="2" fill="#38bdf8"/>
                                    <text x="120" y="90" fill="#ffffff" font-size="9" font-family="JetBrains Mono" text-anchor="middle">Choanocyte Canal</text>
                                ` : phy === 'cnidaria' ? `
                                    <!-- Hydra with Tentacles -->
                                    <path d="M 110 140 L 110 80 Q 110 65 120 65 Q 130 65 130 80 L 130 140 Z" fill="#0891b2" stroke="#22d3ee" stroke-width="2"/>
                                    <!-- Tentacles -->
                                    <path d="M 115 65 Q 90 30 75 40" fill="none" stroke="#22d3ee" stroke-width="2"/>
                                    <path d="M 125 65 Q 150 30 165 40" fill="none" stroke="#22d3ee" stroke-width="2"/>
                                    <path d="M 120 65 Q 120 20 115 15" fill="none" stroke="#22d3ee" stroke-width="2"/>
                                    <text x="120" y="142" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Stinging Tentacles with Cnidocytes</text>
                                ` : phy === 'platy' ? `
                                    <!-- Planaria Flatworm -->
                                    <path d="M 60 75 Q 85 55 120 60 Q 170 65 200 75 Q 170 85 120 90 Q 85 95 60 75 Z" fill="#9333ea" stroke="#c084fc" stroke-width="2"/>
                                    <!-- Eyespots -->
                                    <circle cx="75" cy="71" r="2.5" fill="#ffffff"/>
                                    <circle cx="75" cy="79" r="2.5" fill="#ffffff"/>
                                    <circle cx="75" cy="71" r="1.2" fill="#000000"/>
                                    <circle cx="75" cy="79" r="1.2" fill="#000000"/>
                                    <text x="130" y="125" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Planaria: Bilateral & Dorsoventrally Flat</text>
                                ` : `
                                    <!-- Ascaris Cylindrical Worm -->
                                    <path d="M 40 75 Q 100 50 150 90 Q 190 110 210 75" fill="none" stroke="#ea580c" stroke-width="8" stroke-linecap="round"/>
                                    <text x="120" y="130" fill="#f97316" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Ascaris: Cylindrical Unsegmented Body</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="font-bold text-white block">${{cur.title}}</span>
                            <div class="text-emerald-400 font-semibold">${{cur.trait}}</div>
                            <div class="text-slate-400">Examples: <span class="text-teal-300 font-bold">${{cur.ex}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim10Set = function(p) {{
                phy = p;
                playTone(460, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 11: Invertebrates II (Annelida, Arthropoda, Mollusca, Echinodermata)
        function renderSim11(vp) {{
            let phy = 'arthropoda';
            const data = {{
                annelida: {{ title: "Phylum Annelida (Ringed Worms)", trait: "True coelom, metameric segmentation, nephridia for excretion", ex: "Earthworm (Pheretima), Leech (Hirudinaria)" }},
                arthropoda: {{ title: "Phylum Arthropoda (Largest Phylum)", trait: "Jointed legs, tough chitinous exoskeleton, open blood circulation", ex: "Butterfly, Prawn, Scorpion, Cockroach" }},
                mollusca: {{ title: "Phylum Mollusca (Soft-Bodied)", trait: "Muscular foot, visceral hump, mantle cavity secreting calcareous shell", ex: "Pila (Apple Snail), Unio (Mussel), Octopus" }},
                echinodermata: {{ title: "Phylum Echinodermata (Spiny-Skinned)", trait: "Radial symmetry in adults, hydraulic water vascular system with tube feet", ex: "Asterias (Starfish), Sea Urchin, Holothuria" }}
            }};

            function draw() {{
                const cur = data[phy];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[9px] font-mono font-bold">
                            ${{['annelida', 'arthropoda', 'mollusca', 'echinodermata'].map(p => `
                                <button onclick="window.sim11Set('${{p}}')" class="py-1.5 rounded text-center ${{phy === p ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    ${{p.slice(0, 4).toUpperCase()}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Graphical Specimen -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{phy === 'annelida' ? `
                                    <!-- Metameric Rings Earthworm -->
                                    <path d="M 40 75 Q 120 40 200 75" fill="none" stroke="#b45309" stroke-width="12" stroke-linecap="round"/>
                                    <!-- Metameric Ring notches -->
                                    ${{[60, 80, 100, 120, 140, 160, 180].map(x => `
                                        <line x1="${{x}}" y1="58" x2="${{x}}" y2="78" stroke="#78350f" stroke-width="2"/>
                                    `).join('')}}
                                    <!-- Clitellum -->
                                    <rect x="90" y="55" width="22" height="16" fill="#f59e0b" rx="3"/>
                                    <text x="120" y="130" fill="#f59e0b" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Metameric True Ring Segments & Clitellum</text>
                                ` : phy === 'arthropoda' ? `
                                    <!-- Jointed Legs Insect -->
                                    <!-- Head, Thorax, Abdomen -->
                                    <circle cx="75" cy="75" r="10" fill="#047857"/>
                                    <ellipse cx="105" cy="75" rx="14" ry="12" fill="#065f46"/>
                                    <ellipse cx="145" cy="75" rx="20" ry="10" fill="#064e3b"/>
                                    <!-- Jointed Legs (3 pairs) -->
                                    <path d="M 100 65 L 90 40 L 75 35" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <path d="M 105 65 L 110 35 L 125 30" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <path d="M 112 65 L 130 40 L 150 40" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <path d="M 100 85 L 90 110 L 75 115" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <path d="M 105 85 L 110 115 L 125 120" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <path d="M 112 85 L 130 110 L 150 110" fill="none" stroke="#34d399" stroke-width="2"/>
                                    <text x="120" y="140" fill="#34d399" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Arthropoda: Chitinous Exoskeleton & Jointed Appendages</text>
                                ` : phy === 'mollusca' ? `
                                    <!-- Snail Shell & Muscular Foot -->
                                    <path d="M 70 110 Q 140 115 170 110 Q 180 100 170 95 L 80 95 Z" fill="#f59e0b"/>
                                    <!-- Shell Spiral -->
                                    <ellipse cx="115" cy="75" rx="32" ry="25" fill="#78350f" stroke="#d97706" stroke-width="2"/>
                                    <circle cx="115" cy="75" r="14" fill="none" stroke="#fbbf24" stroke-width="2"/>
                                    <!-- Tentacles -->
                                    <line x1="75" y1="95" x2="65" y2="75" stroke="#f59e0b" stroke-width="2"/>
                                    <circle cx="65" cy="75" r="2" fill="#000000"/>
                                    <text x="120" y="140" fill="#fbbf24" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Mollusca: Calcareous Shell & Muscular Foot</text>
                                ` : `
                                    <!-- Starfish Pentaradial Symmetry -->
                                    <polygon points="120,35 132,65 165,65 138,85 148,115 120,95 92,115 102,85 75,65 108,65" fill="#e11d48" stroke="#f43f5e" stroke-width="2"/>
                                    <circle cx="120" cy="75" r="7" fill="#881337"/>
                                    <text x="120" y="140" fill="#fb7185" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Echinodermata: Pentamerous Tube Feet</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="font-bold text-white block">${{cur.title}}</span>
                            <div class="text-emerald-400 font-semibold">${{cur.trait}}</div>
                            <div class="text-slate-400">Examples: <span class="text-teal-300 font-bold">${{cur.ex}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim11Set = function(p) {{
                phy = p;
                playTone(490, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 12: Vertebrate Heart & Thermal Spectrum
        function renderSim12(vp) {{
            let cls = 'pisces';
            const data = {{
                pisces: {{ title: "Class Pisces (Fish)", heart: "2 Chambers (1 Atrium, 1 Ventricle)", resp: "Gills", thermal: "Poikilothermic (Cold-blooded)", circ: "Single Circulation" }},
                amphibia: {{ title: "Class Amphibia (Frogs, Salamanders)", heart: "3 Chambers (2 Atria, 1 Ventricle)", resp: "Skin & Lungs", thermal: "Poikilothermic (Cold-blooded)", circ: "Incomplete Double Circulation" }},
                reptilia: {{ title: "Class Reptilia (Lizards, Snakes)", heart: "3 Chambers (Incomplete Septum) *Crocodile has 4!", resp: "Lungs", thermal: "Poikilothermic (Cold-blooded)", circ: "Incomplete Double Circulation" }},
                aves: {{ title: "Class Aves (Birds)", heart: "4 Chambers (2 Atria, 2 Ventricles)", resp: "Lungs with pneumatic air sacs", thermal: "Homeothermic (Warm-blooded)", circ: "Complete Double Circulation" }},
                mammalia: {{ title: "Class Mammalia (Mammals)", heart: "4 Chambers (Complete Septum)", resp: "Lungs with muscular diaphragm", thermal: "Homeothermic (Warm-blooded)", circ: "Complete Double Circulation" }}
            }};

            function draw() {{
                const cur = data[cls];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[9px] font-mono font-bold">
                            ${{['pisces', 'amphibia', 'reptilia', 'aves', 'mammalia'].map(c => `
                                <button onclick="window.sim12Set('${{c}}')" class="py-1 rounded text-center ${{cls === c ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    ${{c.slice(0, 4).toUpperCase()}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Graphical Heart Comparison -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{cls === 'pisces' ? `
                                    <!-- 2 Chamber Heart (Fish) -->
                                    <rect x="80" y="40" width="80" height="35" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                                    <rect x="80" y="75" width="80" height="40" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                                    <text x="120" y="62" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Atrium</text>
                                    <text x="120" y="98" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Ventricle</text>
                                    <text x="120" y="138" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">2 Chambers • Venous Heart (Single Circuit)</text>
                                ` : (cls === 'amphibia' || cls === 'reptilia') ? `
                                    <!-- 3 Chamber Heart -->
                                    <rect x="65" y="40" width="50" height="35" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                                    <rect x="125" y="40" width="50" height="35" rx="4" fill="#e11d48" stroke="#fb7185" stroke-width="2"/>
                                    <rect x="65" y="75" width="110" height="45" rx="4" fill="#7c3aed" stroke="#c084fc" stroke-width="2"/>
                                    <text x="90" y="62" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">RA</text>
                                    <text x="150" y="62" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">LA</text>
                                    <text x="120" y="100" fill="#ffffff" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Single Ventricle</text>
                                    <text x="120" y="138" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">3 Chambers • Mixed Oxygenated Blood</text>
                                ` : `
                                    <!-- 4 Chamber Heart (Aves & Mammals) -->
                                    <rect x="65" y="40" width="50" height="35" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                                    <rect x="125" y="40" width="50" height="35" rx="4" fill="#e11d48" stroke="#fb7185" stroke-width="2"/>
                                    <rect x="65" y="75" width="50" height="45" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                                    <rect x="125" y="75" width="50" height="45" rx="4" fill="#be123c" stroke="#fb7185" stroke-width="2"/>
                                    <text x="90" y="62" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">RA</text>
                                    <text x="150" y="62" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">LA</text>
                                    <text x="90" y="100" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">RV</text>
                                    <text x="150" y="100" fill="#ffffff" font-size="8" font-family="JetBrains Mono" text-anchor="middle">LV</text>
                                    <text x="120" y="138" fill="#4ade80" font-size="8" font-family="JetBrains Mono" text-anchor="middle">4 Chambers • Zero Mixing (Complete Double Circuit)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="font-bold text-white block">${{cur.title}}</span>
                            <div class="flex justify-between"><span class="text-slate-400">Heart Chambers:</span><span class="text-amber-400 font-bold">${{cur.heart}}</span></div>
                            <div class="flex justify-between"><span class="text-slate-400">Thermal Class:</span><span class="text-cyan-400 font-bold">${{cur.thermal}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim12Set = function(c) {{
                cls = c;
                playTone(510, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 13: Linnaean Nomenclature Formatter & Rule Validator (C-4.1)
        function renderSim13(vp) {{
            let genus = "Panthera";
            let species = "tigris";

            function validate() {{
                const gOk = /^[A-Z][a-z]+$/.test(genus.trim());
                const sOk = /^[a-z]+$/.test(species.trim());
                return {{ gOk, sOk, allOk: gOk && sOk }};
            }}

            function draw() {{
                const v = validate();
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                            <div>
                                <label class="text-slate-400 block mb-1">1. Genus (Capitalized):</label>
                                <input type="text" value="${{genus}}" oninput="window.sim13Update('genus', this.value)" class="w-full px-2 py-1.5 rounded bg-slate-900 border border-slate-700 text-white font-mono text-xs">
                            </div>
                            <div>
                                <label class="text-slate-400 block mb-1">2. Species (Lowercase):</label>
                                <input type="text" value="${{species}}" oninput="window.sim13Update('species', this.value)" class="w-full px-2 py-1.5 rounded bg-slate-900 border border-slate-700 text-white font-mono text-xs">
                            </div>
                        </div>

                        <!-- Linnaean Preset Selector -->
                        <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                            <button onclick="window.sim13SetPreset('Panthera', 'tigris')" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">Tiger</button>
                            <button onclick="window.sim13SetPreset('Mangifera', 'indica')" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">Mango</button>
                            <button onclick="window.sim13SetPreset('Homo', 'sapiens')" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">Human</button>
                            <button onclick="window.sim13SetPreset('Azadirachta', 'indica')" class="py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">Neem</button>
                        </div>

                        <!-- Scientific Validation Display -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col gap-2 items-center justify-center text-center h-32">
                            <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest">Formal Scientific Binomial Rendering</span>
                            <!-- Printed Italic Format -->
                            <div class="text-lg font-mono font-bold italic text-emerald-400">
                                ${{genus}} ${{species}} <span class="text-xs not-italic font-normal text-slate-400">L.</span>
                            </div>
                            <!-- Handwritten Separately Underlined Format -->
                            <div class="text-xs font-mono text-amber-300">
                                Handwritten Form: <span class="underline mr-1.5 font-semibold">${{genus}}</span> <span class="underline font-semibold">${{species}}</span>
                            </div>
                        </div>

                        <!-- Rule Validation Status -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <div class="flex items-center gap-1.5">
                                <span class="${{v.gOk ? 'text-emerald-400' : 'text-rose-400'}}">${{v.gOk ? '✓' : '✕'}}</span>
                                <span class="text-slate-300">Rule 1: Genus name begins with a capital letter.</span>
                            </div>
                            <div class="flex items-center gap-1.5">
                                <span class="${{v.sOk ? 'text-emerald-400' : 'text-rose-400'}}">${{v.sOk ? '✓' : '✕'}}</span>
                                <span class="text-slate-300">Rule 2: Specific epithet written entirely in lowercase.</span>
                            </div>
                            <div class="flex items-center gap-1.5 text-slate-400">
                                <span>✓</span>
                                <span>Rule 3 & 4: Latinized; italicized in print; underlined separately when handwritten.</span>
                            </div>
                        </div>
                    </div>
                `;
            }}

            window.sim13Update = function(field, val) {{
                if (field === 'genus') genus = val;
                if (field === 'species') species = val;
                draw();
            }};

            window.sim13SetPreset = function(g, s) {{
                genus = g;
                species = s;
                playTone(540, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 14: Indian Biodiversity Flora & Fauna Explorer (C-4.1)
        function renderSim14(vp) {{
            let speciesIdx = 0;
            const floraFauna = [
                {{ common: "Royal Bengal Tiger", bin: "Panthera tigris", king: "Animalia", div: "Chordata", role: "Apex terrestrial predator & national animal of India" }},
                {{ common: "Neem Tree (Indian Lilac)", bin: "Azadirachta indica", king: "Plantae", div: "Angiosperm (Dicot)", role: "Natural biopesticide, antibacterial, ayurvedic keystone" }},
                {{ common: "Holy Basil (Tulsi)", bin: "Ocimum sanctum", king: "Plantae", div: "Angiosperm (Dicot)", role: "Sacred medicinal herb, immunomodulator, eugenol rich" }},
                {{ common: "Sacred Peepal Tree", bin: "Ficus religiosa", king: "Plantae", div: "Angiosperm (Dicot)", role: "High oxygen emitter, keystone fig wasp mutualism" }},
                {{ common: "Indian Elephant", bin: "Elephas maximus", king: "Animalia", div: "Chordata", role: "Ecosystem engineer, seed disperser in Western Ghats" }},
                {{ common: "Indian Banyan Tree", bin: "Ficus benghalensis", king: "Plantae", div: "Angiosperm (Dicot)", role: "National tree of India, massive prop-root canopy system" }}
            ];

            function draw() {{
                const cur = floraFauna[speciesIdx];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-6 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            ${{floraFauna.map((item, idx) => `
                                <button onclick="window.sim14Set(${{idx}})" class="py-1 rounded text-center transition ${{speciesIdx === idx ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">
                                    ${{idx + 1}}
                                </button>
                            `).join('')}}
                        </div>

                        <!-- Indian Biodiversity Card -->
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col gap-2 items-center justify-center text-center h-40">
                            <div class="w-10 h-10 rounded-full bg-emerald-950 border border-emerald-500/60 flex items-center justify-center text-emerald-400 mb-1">
                                <i data-lucide="leaf" class="w-5 h-5"></i>
                            </div>
                            <h4 class="text-sm font-bold text-white">${{cur.common}}</h4>
                            <div class="text-base font-mono font-bold italic text-emerald-400">
                                ${{cur.bin}}
                            </div>
                            <div class="flex items-center gap-2 text-[10px] font-mono text-slate-400">
                                <span>${{cur.king}}</span> • <span>${{cur.div}}</span>
                            </div>
                        </div>

                        <!-- Significance Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="text-slate-400 block">Ecological & Cultural Significance in India:</span>
                            <p class="text-slate-200">${{cur.role}}</p>
                        </div>
                    </div>
                `;
                lucide.createIcons();
            }}

            window.sim14Set = function(idx) {{
                speciesIdx = idx;
                playTone(490, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 15: Acellular Entities: Viruses, Viroids & Prions
        function renderSim15(vp) {{
            let mode = 'virus'; // virus, viroid, prion
            const data = {{
                virus: {{
                    title: "Bacteriophage / Virus",
                    struct: "Protein capsid coat enclosing DNA or RNA nucleic core",
                    cell: "Acellular (Lacks cytoplasm, ribosomes, and metabolic machinery)",
                    prop: "Inert nucleoprotein crystals outside host; obligate intracellular parasite"
                }},
                viroid: {{
                    title: "Viroid (Discovered by T.O. Diener, 1971)",
                    struct: "Free, naked single-stranded circular RNA without protein coat",
                    cell: "Lower molecular weight than viruses; lacks capsid",
                    prop: "Causes Potato Spindle Tuber disease and plant stunt infections"
                }},
                prion: {{
                    title: "Prion (Infectious Protein Particles)",
                    struct: "Abnormally folded neurodegenerative proteins lacking any nucleic acid",
                    cell: "Resistant to radiation, heat, and standard autoclaving",
                    prop: "Causes Bovine Spongiform Encephalopathy (Mad Cow Disease) and CJD"
                }}
            }};

            function draw() {{
                const cur = data[mode];
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-[10px] font-mono font-bold">
                            <button onclick="window.sim15Set('virus')" class="py-1 rounded ${{mode === 'virus' ? 'bg-cyan-600 text-white' : 'bg-slate-800 text-slate-400'}}">Viruses</button>
                            <button onclick="window.sim15Set('viroid')" class="py-1 rounded ${{mode === 'viroid' ? 'bg-purple-600 text-white' : 'bg-slate-800 text-slate-400'}}">Viroids</button>
                            <button onclick="window.sim15Set('prion')" class="py-1 rounded ${{mode === 'prion' ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Prions</button>
                        </div>

                        <!-- Graphical Architecture SVG -->
                        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'virus' ? `
                                    <!-- Bacteriophage Model -->
                                    <!-- Icosahedral Head -->
                                    <polygon points="120,20 145,35 145,60 120,75 95,60 95,35" fill="#0891b2" stroke="#22d3ee" stroke-width="2"/>
                                    <!-- DNA core inside -->
                                    <path d="M 115 35 Q 125 45 115 55 Q 125 65 120 70" fill="none" stroke="#f59e0b" stroke-width="2"/>
                                    <!-- Sheath / Tail -->
                                    <rect x="117" y="75" width="6" height="35" fill="#06b6d4"/>
                                    <!-- Baseplate & Tail Fibers -->
                                    <rect x="112" y="110" width="16" height="5" fill="#0891b2"/>
                                    <path d="M 112 115 L 85 135" stroke="#22d3ee" stroke-width="2"/>
                                    <path d="M 128 115 L 155 135" stroke="#22d3ee" stroke-width="2"/>
                                    <text x="120" y="142" fill="#38bdf8" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Bacteriophage: Protein Capsid + DNA Core</text>
                                ` : mode === 'viroid' ? `
                                    <!-- Naked ssRNA Loop (Viroid) -->
                                    <ellipse cx="120" cy="75" rx="55" ry="30" fill="none" stroke="#a855f7" stroke-width="3" stroke-dasharray="4 2"/>
                                    <text x="120" y="78" fill="#d8b4fe" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Naked Circular ssRNA</text>
                                    <text x="120" y="142" fill="#c084fc" font-size="8" font-family="JetBrains Mono" text-anchor="middle">No Capsid Protein Coat • T.O. Diener (1971)</text>
                                ` : `
                                    <!-- Misfolded Prion Sheet -->
                                    <path d="M 70 60 Q 95 40 120 60 Q 145 80 170 60" fill="none" stroke="#f43f5e" stroke-width="4"/>
                                    <path d="M 70 85 Q 95 65 120 85 Q 145 105 170 85" fill="none" stroke="#f43f5e" stroke-width="4"/>
                                    <text x="120" y="115" fill="#fb7185" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Misfolded PrPSc Beta-Sheets</text>
                                    <text x="120" y="142" fill="#fda4af" font-size="8" font-family="JetBrains Mono" text-anchor="middle">Infectious Protein • No Nucleic Acid</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Data Card -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono space-y-1">
                            <span class="font-bold text-white block">${{cur.title}}</span>
                            <div class="text-slate-300">Structure: <span class="text-teal-300 font-semibold">${{cur.struct}}</span></div>
                            <div class="text-slate-400">Pathology: <span class="text-amber-400">${{cur.prop}}</span></div>
                        </div>
                    </div>
                `;
            }}

            window.sim15Set = function(m) {{
                mode = m;
                playTone(m === 'virus' ? 520 : m === 'viroid' ? 440 : 360, 0.08);
                draw();
            }};

            draw();
        }}

        // SIMULATOR 16: Ecosystem Synergy & Conservation Framework
        function renderSim16(vp) {{
            let mode = 'insitu'; // insitu vs exsitu

            function draw() {{
                vp.innerHTML = `
                    <div class="w-full flex flex-col gap-2.5">
                        <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono font-bold">
                            <button onclick="window.sim16Set('insitu')" class="py-1.5 rounded ${{mode === 'insitu' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">In Situ (On-Site)</button>
                            <button onclick="window.sim16Set('exsitu')" class="py-1.5 rounded ${{mode === 'exsitu' ? 'bg-teal-600 text-white' : 'bg-slate-800 text-slate-400'}}">Ex Situ (Off-Site)</button>
                        </div>

                        <!-- Conservation Graphic -->
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                            <svg width="240" height="150" viewBox="0 0 240 150">
                                ${{mode === 'insitu' ? `
                                    <!-- In Situ Natural Ecosystem -->
                                    <rect x="25" y="25" width="190" height="95" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                                    <text x="120" y="48" fill="#d1fae5" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">In Situ Conservation (On-Site)</text>
                                    <text x="120" y="68" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• National Parks (Corbett, Kaziranga)</text>
                                    <text x="120" y="82" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Wildlife Sanctuaries (Periyar)</text>
                                    <text x="120" y="96" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Biosphere Reserves (Nilgiri, Sundarbans)</text>
                                    <text x="120" y="110" fill="#a7f3d0" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Sacred Groves (Tribal protected forests)</text>
                                ` : `
                                    <!-- Ex Situ Scientific Conservation -->
                                    <rect x="25" y="25" width="190" height="95" rx="6" fill="#134e4a" stroke="#2dd4bf" stroke-width="2"/>
                                    <text x="120" y="48" fill="#ccfbf1" font-size="10" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Ex Situ Conservation (Off-Site)</text>
                                    <text x="120" y="68" fill="#99f6e4" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Botanical Gardens & Herbariums</text>
                                    <text x="120" y="82" fill="#99f6e4" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Zoological Parks & Safari Reserves</text>
                                    <text x="120" y="96" fill="#99f6e4" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Seed Banks & Pollen Storage</text>
                                    <text x="120" y="110" fill="#99f6e4" font-size="8" font-family="JetBrains Mono" text-anchor="middle">• Cryopreservation in Liquid Nitrogen (-196°C)</text>
                                `}}
                            </svg>
                        </div>

                        <!-- Educational Note -->
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] font-mono text-slate-300">
                            ${{mode === 'insitu' ? 
                                '<strong class="text-emerald-400">In Situ Strategy:</strong> Conserves endangered species within their natural ecosystem, preserving ecological evolutionary pressures and food web stability.' : 
                                '<strong class="text-teal-400">Ex Situ Strategy:</strong> Preserves threatened gametes, seeds, and captive populations under controlled artificial conditions to prevent catastrophic global extinction.'}}
                        </div>
                    </div>
                `;
            }}

            window.sim16Set = function(m) {{
                mode = m;
                playTone(m === 'insitu' ? 520 : 440, 0.08);
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

