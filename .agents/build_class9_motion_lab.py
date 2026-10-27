# -*- coding: utf-8 -*-
"""
Builder script for NCERT Class 9 Science Chapter 9: Motion
Outputs: public/animations/class9-motion.html
"""

import os
import json
from class9_motion_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-motion.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Science • Chapter 9 • Motion Master Lab</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX for LaTeX Math -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\\\(', right: '\\\\)', display: false}}]}});">
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: #020617;
            color: #f1f5f9;
        }}
        .font-mono {{
            font-family: 'Fira Code', monospace;
        }}
        /* Custom Scrollbars */
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
        /* Teacher Mouth Animation */
        @keyframes talkPulse {{
            0%, 100% {{ transform: scaleY(0.15); }}
            50% {{ transform: scaleY(1.0); }}
        }}
        .mouth-talking {{
            animation: talkPulse 0.22s ease-in-out infinite;
            transform-origin: center;
        }}
        /* Smooth transitions */
        .tab-btn {{
            transition: all 0.2s ease-in-out;
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 overflow-x-hidden select-none">

    <!-- Top Navigation Bar -->
    <header class="h-16 border-b border-slate-800 bg-slate-900/80 backdrop-blur-md sticky top-0 z-40 px-4 md:px-8 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-500 to-indigo-600 flex items-center justify-center text-white font-extrabold shadow-lg shadow-blue-500/20 text-lg tracking-wider">
                9S
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-blue-400 tracking-wider uppercase font-mono">NCERT Class 9 Science • Ch 9</span>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-blue-500/10 text-blue-300 border border-blue-500/20">13 Periods</span>
                </div>
                <h1 class="text-sm md:text-base font-bold text-slate-100 tracking-tight">Motion Master Lab</h1>
            </div>
        </div>

        <!-- Controls: Sound Toggle, Slide Counter, Navigation -->
        <div class="flex items-center gap-2 md:gap-4">
            <button id="soundToggleBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 flex items-center gap-2 transition shadow-sm">
                <span id="soundIcon">🔊</span>
                <span id="soundText" class="hidden sm:inline">Voice: ON</span>
            </button>
            <div class="text-xs font-mono font-medium text-slate-400 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
                Slide <span id="currentSlideNum" class="text-blue-400 font-bold">1</span> / 20
            </div>
            <div class="flex items-center gap-1">
                <button id="prevBtn" onclick="changeSlide(-1)" class="w-9 h-9 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-slate-200 transition font-bold">
                    ◀
                </button>
                <button id="nextBtn" onclick="changeSlide(1)" class="w-9 h-9 rounded-lg border border-blue-500/50 bg-blue-600 hover:bg-blue-500 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-white transition font-bold shadow-md shadow-blue-600/30">
                    ▶
                </button>
            </div>
        </div>
    </header>

    <!-- Slide Quick Ribbon -->
    <div class="border-b border-slate-800/80 bg-slate-900/50 py-1.5 px-4 overflow-x-auto whitespace-nowrap scrollbar-thin">
        <div id="slideThumbRibbon" class="flex gap-1.5 max-w-7xl mx-auto items-center">
            <!-- Rendered via JS -->
        </div>
    </div>

    <!-- Main Dynamic Content Workspace -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-3 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">

        <!-- Left Column: Pedagogical Guide & Theory (7 Cols) -->
        <div class="lg:col-span-7 flex flex-col gap-4">

            <!-- Teacher Avatar Voice Card -->
            <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-blue-950/40 border border-slate-800 rounded-2xl p-4 shadow-xl flex items-center gap-4 relative overflow-hidden">
                <div class="absolute -right-8 -top-8 w-32 h-32 bg-blue-500/10 rounded-full blur-2xl pointer-events-none"></div>

                <!-- Mentor Avatar SVG -->
                <div class="relative w-16 h-16 shrink-0 rounded-2xl bg-slate-800 border-2 border-blue-400/40 p-1 flex items-center justify-center shadow-lg">
                    <svg viewBox="0 0 100 100" class="w-full h-full">
                        <!-- Lab Coat & Collar -->
                        <path d="M 20 90 L 32 68 L 68 68 L 80 90 Z" fill="#3b82f6"/>
                        <path d="M 38 68 L 50 82 L 62 68 Z" fill="#1d4ed8"/>
                        <!-- Neck -->
                        <rect x="44" y="56" width="12" height="15" rx="3" fill="#fed7aa"/>
                        <!-- Head -->
                        <circle cx="50" cy="40" r="22" fill="#fed7aa"/>
                        <!-- Hair -->
                        <path d="M 26 40 C 26 20, 74 20, 74 40 C 74 24, 66 18, 50 18 C 34 18, 26 24, 26 40 Z" fill="#0f172a"/>
                        <path d="M 26 36 C 24 50, 24 64, 30 68 C 30 52, 34 44, 34 44 Z" fill="#0f172a"/>
                        <path d="M 74 36 C 76 50, 76 64, 70 68 C 70 52, 66 44, 66 44 Z" fill="#0f172a"/>
                        <!-- Glasses -->
                        <rect x="33" y="34" width="14" height="10" rx="3" fill="none" stroke="#2563eb" stroke-width="2.2"/>
                        <rect x="53" y="34" width="14" height="10" rx="3" fill="none" stroke="#2563eb" stroke-width="2.2"/>
                        <line x1="47" y1="39" x2="53" y2="39" stroke="#2563eb" stroke-width="2"/>
                        <!-- Eyes -->
                        <circle cx="40" cy="39" r="2" fill="#0f172a"/>
                        <circle cx="60" cy="39" r="2" fill="#0f172a"/>
                        <!-- Smile / Talking Mouth -->
                        <rect id="teacherMouth" x="44" y="50" width="12" height="4" rx="2" fill="#dc2626"/>
                    </svg>
                    <span class="absolute -bottom-1 -right-1 flex h-3.5 w-3.5">
                        <span id="speakerPulse" class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75 hidden"></span>
                        <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-blue-500 border-2 border-slate-900"></span>
                    </span>
                </div>

                <div class="flex-1">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-blue-300 font-mono">Prof. Sophia</span>
                            <span class="text-[10px] bg-slate-800 text-slate-400 px-2 py-0.5 rounded border border-slate-700">Physics Kinematics</span>
                        </div>
                        <button onclick="replayVoice()" class="text-xs text-slate-400 hover:text-blue-400 flex items-center gap-1 transition">
                            <span>↻</span> Replay
                        </button>
                    </div>
                    <p id="teacherSpeechText" class="text-xs md:text-sm text-slate-200 mt-1 leading-relaxed italic">
                        <!-- Populated by JS -->
                    </p>
                </div>
            </div>

            <!-- Theory Content Card -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl flex flex-col gap-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span id="slideBadge" class="text-[11px] font-mono font-semibold px-2.5 py-1 rounded-md bg-blue-500/10 text-blue-400 border border-blue-500/20">
                        Slide 01
                    </span>
                    <span id="slideSubtitle" class="text-xs text-slate-400 font-medium truncate max-w-xs md:max-w-md">
                        Subtitle
                    </span>
                </div>

                <h2 id="slideTitle" class="text-lg md:text-xl font-extrabold text-slate-50 tracking-tight">
                    <!-- Title -->
                </h2>

                <div id="slideTheoryBody" class="text-xs md:text-sm text-slate-300 leading-relaxed space-y-2.5">
                    <!-- Theory Paragraphs -->
                </div>

                <!-- Key Concepts Bullet Ribbon -->
                <div id="slideKeyPointsContainer" class="mt-2 p-3 bg-slate-950/80 rounded-xl border border-slate-800/80">
                    <div class="text-[11px] font-bold text-blue-300 font-mono uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
                        <span>⚡</span> Key Principles
                    </div>
                    <ul id="slideKeyPointsList" class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <!-- Bullets -->
                    </ul>
                </div>
            </div>

            <!-- In-Slide Checkpoints Container (2 Checkpoints on Content Slides) -->
            <div id="checkpointsWrapper" class="space-y-3">
                <!-- Checkpoints injected by JS -->
            </div>

        </div>

        <!-- Right Column: Interactive Simulators / Quiz Arena (5 Cols) -->
        <div class="lg:col-span-5 flex flex-col gap-4">

            <!-- Simulator or Quiz Viewport Card -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 md:p-5 shadow-xl flex flex-col gap-3 sticky top-20">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
                        <span id="panelHeaderTitle" class="text-xs font-bold text-blue-300 font-mono uppercase tracking-wider">
                            Interactive Simulator
                        </span>
                    </div>
                    <span id="panelSubHeader" class="text-[11px] text-slate-400 font-mono">
                        Active Mode
                    </span>
                </div>

                <!-- Dynamic Viewport Area -->
                <div id="interactiveViewport" class="min-h-[420px] flex flex-col items-center justify-center relative bg-slate-950 rounded-xl border border-slate-800/80 p-3 overflow-hidden">
                    <!-- Interactive SVG Simulators (1-16) or Quiz Engine (17-20) rendered here -->
                </div>

                <!-- Simulation Info/Instructions footer -->
                <div id="simulatorFooterInstructions" class="text-[11px] text-slate-400 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 flex items-center justify-between">
                    <span id="simHelpText">Interact with the controls above to explore motion mechanics.</span>
                    <button onclick="resetCurrentSimulation()" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-mono text-slate-300 border border-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

        </div>

    </main>

    <!-- Last Slide Notice Container (Strict Requirement) -->
    <div id="lastSlideNotice" class="hidden max-w-7xl mx-auto px-4 py-4 w-full">
        <div class="bg-gradient-to-r from-blue-950/80 via-slate-900 to-indigo-950/80 border-2 border-blue-500/50 rounded-2xl p-6 text-center shadow-2xl flex flex-col items-center justify-center gap-3">
            <div class="w-14 h-14 rounded-2xl bg-blue-500/20 border border-blue-500/40 flex items-center justify-center text-3xl">
                🚀
            </div>
            <h3 class="text-lg md:text-xl font-bold text-blue-300 tracking-wide">
                You have reached the last slide of this chapter
            </h3>
            <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
                You have completed your mastery of <strong>Motion</strong>—including distance vs displacement, speed and velocity, uniform and non-uniform acceleration, graphical analysis (s-t and v-t slopes and areas), the graphical derivations of the 3 kinematic equations (v = u + at, s = ut + ½at², v² = u² + 2as), uniform circular motion, road safety braking distance physics, and Einstein's cosmic speed limit!
            </p>
            <div class="flex items-center gap-3 mt-2">
                <button onclick="jumpToSlide(1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 border border-slate-700 transition">
                    ↺ Restart Lab
                </button>
                <button onclick="jumpToSlide(17)" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white transition shadow-lg shadow-blue-600/30">
                    📝 Retake Mastery Quiz
                </button>
            </div>
        </div>
    </div>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-lg w-full p-5 shadow-2xl flex flex-col gap-4 relative animate-in fade-in zoom-in-95 duration-200">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 flex items-center justify-center font-bold text-sm">
                ✕
            </button>
            <div class="flex items-center gap-2">
                <span class="text-lg">💡</span>
                <h4 class="text-base font-bold text-blue-300 font-mono">Step-by-Step Solution</h4>
            </div>
            <div id="solutionQuestionText" class="text-xs text-slate-400 border-l-2 border-blue-500 pl-3 italic">
                <!-- Question -->
            </div>
            <div id="solutionBodyText" class="text-xs md:text-sm text-slate-200 leading-relaxed bg-slate-950 p-4 rounded-xl border border-slate-800">
                <!-- Detailed explanation -->
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow-md transition">
                    Understood!
                </button>
            </div>
        </div>
    </div>

    <!-- Application Script Data & Runtime Engine -->
    <script>
        const SLIDES = {slides_json};
        let currentSlideIndex = 0;
        let isAudioEnabled = true;
        let speechSynth = window.speechSynthesis;
        let currentUtterance = null;

        // Simulator State Objects
        let sim1State = {{ frame: 'road' }};
        let sim2State = {{ pathStep: 2 }}; // A->B->C
        let sim3State = {{ running: false }};
        let sim4State = {{ u: 10, a: 2 }};
        let sim5State = {{ mode: 'uniform' }};
        let sim6State = {{ mode: 'uniform_acc' }};
        let sim7State = {{ highlight: 'all' }};
        let sim8State = {{ step: 1 }};
        let sim9State = {{ step: 1 }};
        let sim10State = {{ step: 1 }};
        let sim11State = {{ u: 0, a: 2, t: 10 }};
        let sim12State = {{ u: 20, g: 9.8 }};
        let sim13State = {{ speed: 10, cut: false }};
        let sim14State = {{ r: 100, v: 20 }};
        let sim15State = {{ speedKm: 60, distracted: false }};
        let sim16State = {{ vFraction: 0.5 }};

        // Initialize Application
        window.addEventListener('DOMContentLoaded', () => {{
            renderRibbon();
            loadSlide(0);
        }});

        function renderRibbon() {{
            const ribbon = document.getElementById('slideThumbRibbon');
            ribbon.innerHTML = SLIDES.map((s, idx) => `
                <button onclick="jumpToSlide(${{idx + 1}})" id="thumb-${{idx}}" class="tab-btn px-2.5 py-1 rounded-lg text-xs font-mono font-medium border border-slate-800 bg-slate-900/60 hover:bg-slate-800 text-slate-400 hover:text-slate-200 shrink-0">
                    ${{s.id <= 16 ? s.id : 'Q' + (s.id - 16)}}
                </button>
            `).join('');
        }}

        function loadSlide(idx) {{
            if (idx < 0 || idx >= SLIDES.length) return;
            currentSlideIndex = idx;
            const slide = SLIDES[idx];

            // Update Header & Ribbon
            document.getElementById('currentSlideNum').textContent = slide.id;
            document.getElementById('prevBtn').disabled = idx === 0;

            // Strict Last Slide Rule: Hide nextBtn on slide 20
            const nextBtn = document.getElementById('nextBtn');
            const lastSlideNotice = document.getElementById('lastSlideNotice');
            if (slide.id === 20) {{
                nextBtn.style.display = 'none';
                lastSlideNotice.classList.remove('hidden');
            }} else {{
                nextBtn.style.display = 'flex';
                nextBtn.disabled = false;
                lastSlideNotice.classList.add('hidden');
            }}

            // Highlight ribbon tab
            SLIDES.forEach((_, i) => {{
                const el = document.getElementById(`thumb-${{i}}`);
                if (el) {{
                    if (i === idx) {{
                        el.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-mono font-bold border border-blue-500 bg-blue-500/20 text-blue-300 shadow-sm shrink-0';
                    }} else {{
                        el.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-mono font-medium border border-slate-800 bg-slate-900/60 hover:bg-slate-800 text-slate-400 hover:text-slate-200 shrink-0';
                    }}
                }}
            }});

            // Update Slide Texts
            document.getElementById('slideBadge').textContent = slide.badge;
            document.getElementById('slideSubtitle').textContent = slide.subtitle;
            document.getElementById('slideTitle').textContent = slide.title;
            document.getElementById('teacherSpeechText').textContent = `"${{slide.teacher}}"`;

            // Render Theory
            const theoryEl = document.getElementById('slideTheoryBody');
            if (slide.theory) {{
                theoryEl.innerHTML = slide.theory.map(p => `<p>${{p}}</p>`).join('');
            }} else {{
                theoryEl.innerHTML = `<p class="italic text-slate-400">Mastery Quiz Challenge session. Select the correct options on the right and open the popup modal for detailed solutions.</p>`;
            }}

            // Render Key Points
            const keyPointsContainer = document.getElementById('slideKeyPointsContainer');
            const keyPointsList = document.getElementById('slideKeyPointsList');
            if (slide.key_points && slide.key_points.length > 0) {{
                keyPointsContainer.classList.remove('hidden');
                keyPointsList.innerHTML = slide.key_points.map(kp => `<li>${{kp}}</li>`).join('');
            }} else {{
                keyPointsContainer.classList.add('hidden');
            }}

            // Render Checkpoints (if content slide)
            const checkpointsWrapper = document.getElementById('checkpointsWrapper');
            if (slide.checkpoints && slide.checkpoints.length > 0) {{
                checkpointsWrapper.classList.remove('hidden');
                checkpointsWrapper.innerHTML = `
                    <div class="flex items-center gap-2 pt-2">
                        <span class="text-xs font-bold font-mono text-blue-400 uppercase tracking-wider">🎯 In-Slide Checkpoints</span>
                        <span class="text-[10px] text-slate-400">(Immediate Feedback)</span>
                    </div>
                    ${{slide.checkpoints.map(cp => `
                        <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 shadow-sm flex flex-col gap-2.5">
                            <div class="text-xs font-semibold text-slate-200 flex items-start gap-2">
                                <span class="px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-300 font-mono text-[10px] shrink-0 font-bold">CP ${{cp.num}}</span>
                                <span>${{cp.q}}</span>
                            </div>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs">
                                ${{cp.options.map((opt, oIdx) => `
                                    <button onclick="handleCheckpointAnswer(${{cp.num}}, ${{oIdx}}, ${{cp.ans}})" id="cp-btn-${{cp.num}}-${{oIdx}}" class="text-left px-2.5 py-1.5 rounded-lg border border-slate-800 bg-slate-950 hover:bg-slate-800 text-slate-300 hover:text-white transition">
                                        ${{opt}}
                                    </button>
                                `).join('')}}
                            </div>
                            <div id="cp-exp-${{cp.num}}" class="hidden text-[11px] p-2 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">
                                <strong class="text-blue-400">Prof. Sophia:</strong> ${{cp.exp}}
                            </div>
                        </div>
                    `).join('')}}
                `;
            }} else {{
                checkpointsWrapper.classList.add('hidden');
                checkpointsWrapper.innerHTML = '';
            }}

            // Render Right Viewport: Simulators 1-16 or Quiz Slides 17-20
            renderRightViewport(slide);

            // Re-render LaTeX math
            if (window.renderMathInElement) {{
                renderMathInElement(document.getElementById('slideTheoryBody'), {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\(', right: '\\)', display: false}}]}});
                renderMathInElement(document.getElementById('checkpointsWrapper'), {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\(', right: '\\)', display: false}}]}});
            }}

            // Voice narration
            speakText(slide.teacher);
        }}

        function changeSlide(delta) {{
            const nextIdx = currentSlideIndex + delta;
            if (nextIdx >= 0 && nextIdx < SLIDES.length) {{
                loadSlide(nextIdx);
            }}
        }}

        function jumpToSlide(num) {{
            loadSlide(num - 1);
        }}

        // Checkpoint Handler
        function handleCheckpointAnswer(cpNum, selectedIdx, correctIdx) {{
            const expEl = document.getElementById(`cp-exp-${{cpNum}}`);
            if (expEl) expEl.classList.remove('hidden');

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`cp-btn-${{cpNum}}-${{i}}`);
                if (!btn) continue;
                if (i === correctIdx) {{
                    btn.className = 'text-left px-2.5 py-1.5 rounded-lg border border-emerald-500 bg-emerald-500/20 text-emerald-200 font-semibold';
                }} else if (i === selectedIdx) {{
                    btn.className = 'text-left px-2.5 py-1.5 rounded-lg border border-rose-500 bg-rose-500/20 text-rose-300';
                }} else {{
                    btn.className = 'text-left px-2.5 py-1.5 rounded-lg border border-slate-800 bg-slate-950 text-slate-500 opacity-50';
                }}
            }}
        }}

        // Voice Engine
        function speakText(text) {{
            if (!isAudioEnabled) return;
            if (!window.speechSynthesis) return;

            window.speechSynthesis.cancel();
            const cleanText = text.replace(/\\$/g, '');
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.lang = 'en-US';
            utterance.rate = 1.0;
            utterance.pitch = 1.05;

            const mouth = document.getElementById('teacherMouth');
            const pulse = document.getElementById('speakerPulse');

            utterance.onstart = () => {{
                if (mouth) mouth.classList.add('mouth-talking');
                if (pulse) pulse.classList.remove('hidden');
            }};

            utterance.onend = () => {{
                if (mouth) mouth.classList.remove('mouth-talking');
                if (pulse) pulse.classList.add('hidden');
            }};

            utterance.onerror = () => {{
                if (mouth) mouth.classList.remove('mouth-talking');
                if (pulse) pulse.classList.add('hidden');
            }};

            window.speechSynthesis.speak(utterance);
        }}

        function toggleAudio() {{
            isAudioEnabled = !isAudioEnabled;
            const text = document.getElementById('soundText');
            const icon = document.getElementById('soundIcon');
            if (isAudioEnabled) {{
                text.textContent = 'Voice: ON';
                icon.textContent = '🔊';
                speakText(SLIDES[currentSlideIndex].teacher);
            }} else {{
                text.textContent = 'Voice: OFF';
                icon.textContent = '🔇';
                window.speechSynthesis.cancel();
                const mouth = document.getElementById('teacherMouth');
                const pulse = document.getElementById('speakerPulse');
                if (mouth) mouth.classList.remove('mouth-talking');
                if (pulse) pulse.classList.add('hidden');
            }}
        }}

        function replayVoice() {{
            if (isAudioEnabled) {{
                speakText(SLIDES[currentSlideIndex].teacher);
            }}
        }}

        // Solution Modal Handlers
        function openSolutionModal(qText, solText) {{
            document.getElementById('solutionQuestionText').textContent = qText;
            document.getElementById('solutionBodyText').innerHTML = solText;
            document.getElementById('solutionModal').classList.remove('hidden');
            if (window.renderMathInElement) {{
                renderMathInElement(document.getElementById('solutionBodyText'), {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\(', right: '\\)', display: false}}]}});
            }}
        }}

        function closeSolutionModal() {{
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        // Viewport Renderer Routing
        function renderRightViewport(slide) {{
            const vp = document.getElementById('interactiveViewport');
            const pTitle = document.getElementById('panelHeaderTitle');
            const pSub = document.getElementById('panelSubHeader');
            const simHelp = document.getElementById('simHelpText');

            if (slide.id <= 16) {{
                pTitle.textContent = `Interactive Simulator ${{slide.id}}`;
                pSub.textContent = "Simulation Mode";
                simHelp.textContent = "Use the interactive controls to test and verify motion mechanics.";

                switch(slide.id) {{
                    case 1: renderSim1(vp); break;
                    case 2: renderSim2(vp); break;
                    case 3: renderSim3(vp); break;
                    case 4: renderSim4(vp); break;
                    case 5: renderSim5(vp); break;
                    case 6: renderSim6(vp); break;
                    case 7: renderSim7(vp); break;
                    case 8: renderSim8(vp); break;
                    case 9: renderSim9(vp); break;
                    case 10: renderSim10(vp); break;
                    case 11: renderSim11(vp); break;
                    case 12: renderSim12(vp); break;
                    case 13: renderSim13(vp); break;
                    case 14: renderSim14(vp); break;
                    case 15: renderSim15(vp); break;
                    case 16: renderSim16(vp); break;
                }}
            }} else {{
                pTitle.textContent = `Mastery Quiz Arena • Slide ${{slide.id}}`;
                pSub.textContent = "Challenge Mode";
                simHelp.textContent = "Answer questions and click 'View Solution' for detailed step-by-step guidance.";
                renderQuizSlide(vp, slide);
            }}
        }}

        function resetCurrentSimulation() {{
            const sId = SLIDES[currentSlideIndex].id;
            switch(sId) {{
                case 1: sim1State = {{ frame: 'road' }}; break;
                case 2: sim2State = {{ pathStep: 2 }}; break;
                case 3: sim3State = {{ running: false }}; break;
                case 4: sim4State = {{ u: 10, a: 2 }}; break;
                case 5: sim5State = {{ mode: 'uniform' }}; break;
                case 6: sim6State = {{ mode: 'uniform_acc' }}; break;
                case 7: sim7State = {{ highlight: 'all' }}; break;
                case 8: sim8State = {{ step: 1 }}; break;
                case 9: sim9State = {{ step: 1 }}; break;
                case 10: sim10State = {{ step: 1 }}; break;
                case 11: sim11State = {{ u: 0, a: 2, t: 10 }}; break;
                case 12: sim12State = {{ u: 20, g: 9.8 }}; break;
                case 13: sim13State = {{ speed: 10, cut: false }}; break;
                case 14: sim14State = {{ r: 100, v: 20 }}; break;
                case 15: sim15State = {{ speedKm: 60, distracted: false }}; break;
                case 16: sim16State = {{ vFraction: 0.5 }}; break;
            }}
            renderRightViewport(SLIDES[currentSlideIndex]);
        }}

        // ==========================================
        // 16 BESPOKE SIMULATOR IMPLEMENTATIONS
        // ==========================================

        // Sim 1: Relative Motion & Reference Frame Track
        function renderSim1(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Frame of Reference: Observer on Road vs Inside Bus
                    </div>

                    <!-- Observer Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim1SetFrame('road')" class="py-1 rounded-lg ${{sim1State.frame === 'road' ? 'bg-blue-600 text-white font-bold' : 'text-slate-400'}}">Observer on Road</button>
                        <button onclick="window.sim1SetFrame('bus')" class="py-1 rounded-lg ${{sim1State.frame === 'bus' ? 'bg-indigo-600 text-white font-bold' : 'text-slate-400'}}">Observer inside Bus</button>
                    </div>

                    <!-- Visual Track SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 110" class="w-full h-28">
                            <!-- Roadway -->
                            <rect x="0" y="80" width="200" height="25" fill="#1e293b"/>
                            <line x1="0" y1="92" x2="200" y2="92" stroke="#facc15" stroke-dasharray="8,6" stroke-width="2"/>

                            <!-- Bus -->
                            <rect x="60" y="45" width="80" height="35" rx="4" fill="#3b82f6" stroke="#93c5fd" stroke-width="1.5"/>
                            <rect x="70" y="52" width="16" height="12" rx="2" fill="#bae6fd"/>
                            <rect x="95" y="52" width="16" height="12" rx="2" fill="#bae6fd"/>
                            <rect x="120" y="52" width="14" height="12" rx="2" fill="#bae6fd"/>
                            <!-- Passengers -->
                            <circle cx="78" cy="58" r="3" fill="#0f172a"/>
                            <circle cx="103" cy="58" r="3" fill="#0f172a"/>
                            <!-- Wheels -->
                            <circle cx="78" cy="80" r="7" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                            <circle cx="125" cy="80" r="7" fill="#0f172a" stroke="#64748b" stroke-width="2"/>

                            ${{sim1State.frame === 'road' ? `
                                <!-- Observer on road standing still -->
                                <circle cx="25" cy="70" r="4" fill="#10b981"/>
                                <line x1="25" y1="74" x2="25" y2="82" stroke="#10b981" stroke-width="2"/>
                                <text x="25" y="62" font-size="6" fill="#10b981" font-family="monospace" text-anchor="middle">Observer (Rest)</text>
                                <!-- Bus velocity vector -->
                                <line x1="145" y1="62" x2="175" y2="62" stroke="#38bdf8" stroke-width="2"/>
                                <polygon points="175,59 175,65 180,62" fill="#38bdf8"/>
                                <text x="160" y="56" font-size="7" fill="#38bdf8" font-family="monospace">v = 15 m/s</text>
                            ` : `
                                <!-- Inside frame: Road moves backwards -->
                                <line x1="150" y1="92" x2="120" y2="92" stroke="#ef4444" stroke-width="2"/>
                                <polygon points="120,89 120,95 115,92" fill="#ef4444"/>
                                <text x="135" y="102" font-size="7" fill="#ef4444" font-family="monospace">Road: -15 m/s</text>
                                <text x="100" y="38" font-size="7" fill="#38bdf8" font-family="monospace" text-anchor="middle">Passenger at Rest (v = 0)</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Observation Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs font-mono">
                        ${{sim1State.frame === 'road' ? `
                            <div class="text-blue-400 font-bold">Observer on Road:</div>
                            <div class="text-slate-300 text-[11px] mt-0.5">Bus and passengers move forward at 15 m/s. Roadside trees are stationary.</div>
                        ` : `
                            <div class="text-indigo-400 font-bold">Observer inside Bus:</div>
                            <div class="text-slate-300 text-[11px] mt-0.5">Fellow passenger is at rest (v = 0). Road, trees, and ground appear to fly backwards at -15 m/s!</div>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim1SetFrame = f => {{ sim1State.frame = f; renderSim1(document.getElementById('interactiveViewport')); }};

        // Sim 2: Interactive Path Tracer: Distance vs Displacement
        function renderSim2(vp) {{
            const steps = [
                {{ step: 1, label: "Leg 1: A ➔ B (40 m East)", dist: 40, disp: 40, angle: "0° (East)" }},
                {{ step: 2, label: "Leg 2: B ➔ C (30 m North)", dist: 70, disp: 50, angle: "36.9° North of East" }},
                {{ step: 3, label: "Leg 3: Return C ➔ A (Round Trip)", dist: 120, disp: 0, angle: "Zero Displacement" }}
            ];

            const cur = steps[sim2State.pathStep - 1] || steps[1];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Path Distance (Scalar) vs Net Displacement (Vector)
                    </div>

                    <!-- Step Selector -->
                    <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{steps.map(s => `
                            <button onclick="window.sim2SetStep(${{s.step}})" class="py-1 rounded ${{sim2State.pathStep === s.step ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Stage ${{s.step}}</button>
                        `).join('')}}
                    </div>

                    <!-- 2D Vector Path SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <!-- Grid dots -->
                            <circle cx="40" cy="100" r="4" fill="#3b82f6"/><text x="35" y="112" font-size="8" fill="#3b82f6" font-family="monospace">A</text>
                            <circle cx="140" cy="100" r="4" fill="#3b82f6"/><text x="145" y="112" font-size="8" fill="#3b82f6" font-family="monospace">B</text>
                            <circle cx="140" cy="30" r="4" fill="#3b82f6"/><text x="145" y="25" font-size="8" fill="#3b82f6" font-family="monospace">C</text>

                            <!-- Leg 1: A to B (40 m) -->
                            <line x1="40" y1="100" x2="140" y2="100" stroke="#f59e0b" stroke-width="3"/>
                            <text x="90" y="95" font-size="7" fill="#f59e0b" font-family="monospace">40 m East</text>

                            ${{sim2State.pathStep >= 2 ? `
                                <!-- Leg 2: B to C (30 m) -->
                                <line x1="140" y1="100" x2="140" y2="30" stroke="#f59e0b" stroke-width="3"/>
                                <text x="145" y="65" font-size="7" fill="#f59e0b" font-family="monospace">30 m North</text>
                            ` : ''}}

                            ${{sim2State.pathStep === 2 ? `
                                <!-- Displacement vector A to C (50 m) -->
                                <line x1="40" y1="100" x2="140" y2="30" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,3"/>
                                <polygon points="135,32 142,30 138,37" fill="#38bdf8"/>
                                <text x="80" y="60" font-size="8" font-weight="bold" fill="#38bdf8" font-family="monospace">s = 50 m</text>
                            ` : sim2State.pathStep === 3 ? `
                                <!-- Return path C to A -->
                                <line x1="140" y1="30" x2="40" y2="100" stroke="#f59e0b" stroke-width="2.5"/>
                                <text x="80" y="60" font-size="8" font-weight="bold" fill="#ef4444" font-family="monospace">Displacement = 0 m</text>
                            ` : ''}}
                        </svg>
                    </div>

                    <!-- Metrics Card -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Total Distance:</span>
                            <span class="text-amber-400 font-bold text-sm">${{cur.dist}} m</span>
                        </div>
                        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Displacement Magnitude:</span>
                            <span class="text-cyan-300 font-bold text-sm">${{cur.disp}} m</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim2SetStep = st => {{ sim2State.pathStep = st; renderSim2(document.getElementById('interactiveViewport')); }};

        // Sim 3: Speedometer vs Velocimeter Digital Dashboard
        function renderSim3(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Speedometer vs Velocimeter: 100 m Round Trip
                    </div>

                    <!-- Dual Gauge Display -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center">
                            <span class="text-[10px] text-slate-400 uppercase tracking-widest">Average Speed</span>
                            <div class="text-2xl font-bold text-amber-400 mt-1">20.0 <span class="text-xs">m/s</span></div>
                            <span class="text-[9px] text-slate-500 mt-1">Total Distance / Time (200m / 10s)</span>
                        </div>
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center">
                            <span class="text-[10px] text-slate-400 uppercase tracking-widest">Average Velocity</span>
                            <div class="text-2xl font-bold text-cyan-400 mt-1">0.0 <span class="text-xs">m/s</span></div>
                            <span class="text-[9px] text-slate-500 mt-1">Net Displacement / Time (0m / 10s)</span>
                        </div>
                    </div>

                    <!-- Explanatory Card -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="text-emerald-400 font-bold text-xs">The Round Trip Paradox:</div>
                        <p class="text-[11px] text-slate-300 leading-relaxed">
                            A car drives 100 m East at 20 m/s and immediately returns 100 m West at 20 m/s. Its speedometer registers a high average speed of 20 m/s (72 km/h). But because initial and final positions are identical, net displacement is 0, so average velocity is precisely 0 m/s!
                        </p>
                    </div>
                </div>
            `;
        }}

        // Sim 4: Acceleration & Braking Dynamic Track
        function renderSim4(vp) {{
            const u = sim4State.u;
            const a = sim4State.a;
            const v10 = Math.max(0, u + a * 5); // velocity after 5 seconds

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Acceleration Formula: a = (v - u) / t
                    </div>

                    <!-- Controls -->
                    <div class="space-y-2 bg-slate-900 p-3 rounded-xl border border-slate-800">
                        <div>
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-slate-300">Initial Velocity (u):</span>
                                <span class="text-cyan-300 font-bold">${{u}} m/s</span>
                            </div>
                            <input type="range" min="0" max="30" step="2" value="${{u}}" oninput="window.sim4SetU(this.value)" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-slate-300">Acceleration (a):</span>
                                <span class="${{a >= 0 ? 'text-emerald-400' : 'text-rose-400'}} font-bold">${{a > 0 ? '+' + a : a}} m/s²</span>
                            </div>
                            <input type="range" min="-5" max="5" step="1" value="${{a}}" oninput="window.sim4SetA(this.value)" class="w-full accent-emerald-500">
                        </div>
                    </div>

                    <!-- Live Calculation Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between">
                            <span class="text-slate-400">Velocity after 5 seconds (v = u + at):</span>
                            <span class="text-white font-bold text-sm">${{v10.toFixed(1)}} m/s</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-400">Motion Status:</span>
                            <span class="${{a > 0 ? 'text-emerald-400' : a < 0 ? 'text-rose-400' : 'text-cyan-300'}} font-bold">
                                ${{a > 0 ? 'Accelerating (Speeding Up)' : a < 0 ? 'Retarding / Braking' : 'Uniform Velocity (a = 0)'}}
                            </span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim4SetU = val => {{ sim4State.u = parseFloat(val); renderSim4(document.getElementById('interactiveViewport')); }};
        window.sim4SetA = val => {{ sim4State.a = parseFloat(val); renderSim4(document.getElementById('interactiveViewport')); }};

        // Sim 5: Distance-Time Graph Plotter & Slope Calculator
        function renderSim5(vp) {{
            const modes = [
                {{ key: "rest", name: "Rest (v = 0)", slope: "0 m/s", desc: "Horizontal line parallel to time axis." }},
                {{ key: "uniform", name: "Uniform Speed", slope: "10 m/s", desc: "Straight line with constant positive slope." }},
                {{ key: "fast", name: "High Speed", slope: "25 m/s", desc: "Steeper slope indicates higher speed." }},
                {{ key: "accel", name: "Accelerating", slope: "Variable", desc: "Curved line bending upwards." }}
            ];

            const cur = modes.find(m => m.key === sim5State.mode) || modes[1];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Distance-Time Graph: Slope = Speed = Δs / Δt
                    </div>

                    <!-- Mode Selector -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{modes.map(m => `
                            <button onclick="window.sim5SetMode('${{m.key}}')" class="py-1 rounded ${{sim5State.mode === m.key ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{m.name.split(' ')[0]}}</button>
                        `).join('')}}
                    </div>

                    <!-- s-t Graph SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <!-- Axes -->
                            <line x1="30" y1="105" x2="185" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
                            <line x1="30" y1="105" x2="30" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                            <text x="185" y="117" font-size="7" fill="#94a3b8" font-family="monospace">Time (t)</text>
                            <text x="15" y="20" font-size="7" fill="#94a3b8" font-family="monospace">s (m)</text>

                            ${{sim5State.mode === 'rest' ? `
                                <!-- Horizontal line -->
                                <line x1="30" y1="60" x2="175" y2="60" stroke="#38bdf8" stroke-width="3"/>
                                <text x="100" y="52" font-size="8" fill="#38bdf8" font-family="monospace">Slope = 0 (At Rest)</text>
                            ` : sim5State.mode === 'uniform' ? `
                                <!-- Moderate straight line -->
                                <line x1="30" y1="105" x2="160" y2="35" stroke="#10b981" stroke-width="3"/>
                                <!-- Slope Triangle -->
                                <polygon points="100,67 150,67 150,40" fill="#10b981" opacity="0.2"/>
                                <line x1="100" y1="67" x2="150" y2="67" stroke="#cbd5e1" stroke-dasharray="2,2"/>
                                <line x1="150" y1="67" x2="150" y2="40" stroke="#cbd5e1" stroke-dasharray="2,2"/>
                                <text x="125" y="75" font-size="6" fill="#cbd5e1" font-family="monospace">Δt</text>
                                <text x="155" y="55" font-size="6" fill="#cbd5e1" font-family="monospace">Δs</text>
                            ` : sim5State.mode === 'fast' ? `
                                <!-- Steep line -->
                                <line x1="30" y1="105" x2="100" y2="25" stroke="#f59e0b" stroke-width="3"/>
                                <text x="110" y="35" font-size="8" fill="#f59e0b" font-family="monospace">Steep Slope (Fast)</text>
                            ` : `
                                <!-- Curved upward parabola -->
                                <path d="M 30 105 Q 110 95 170 25" fill="none" stroke="#ef4444" stroke-width="3"/>
                                <text x="100" y="45" font-size="8" fill="#ef4444" font-family="monospace">Accelerating (Curved)</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Detail Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs flex justify-between items-center">
                        <div>
                            <span class="text-slate-400">Profile:</span> <strong class="text-white">${{cur.name}}</strong>
                        </div>
                        <div class="px-2.5 py-1 rounded bg-blue-600/30 text-blue-300 font-bold border border-blue-500/40">
                            Slope = ${{cur.slope}}
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim5SetMode = m => {{ sim5State.mode = m; renderSim5(document.getElementById('interactiveViewport')); }};

        // Sim 6: Velocity-Time Slope & Acceleration Studio
        function renderSim6(vp) {{
            const modes = [
                {{ key: "uniform_v", name: "Uniform Velocity", a: "0 m/s²", desc: "Horizontal line parallel to time axis." }},
                {{ key: "uniform_acc", name: "Uniform Accel", a: "+2.5 m/s²", desc: "Straight line with positive slope." }},
                {{ key: "retard", name: "Uniform Retardation", a: "-3.0 m/s²", desc: "Straight line with negative slope." }}
            ];

            const cur = modes.find(m => m.key === sim6State.mode) || modes[1];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Velocity-Time Graph: Slope = Acceleration = Δv / Δt
                    </div>

                    <!-- Mode Buttons -->
                    <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{modes.map(m => `
                            <button onclick="window.sim6SetMode('${{m.key}}')" class="py-1 rounded ${{sim6State.mode === m.key ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{m.name.split(' ')[0]}}</button>
                        `).join('')}}
                    </div>

                    <!-- v-t Graph SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <line x1="30" y1="105" x2="185" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
                            <line x1="30" y1="105" x2="30" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
                            <text x="185" y="117" font-size="7" fill="#94a3b8" font-family="monospace">t (s)</text>
                            <text x="15" y="20" font-size="7" fill="#94a3b8" font-family="monospace">v (m/s)</text>

                            ${{sim6State.mode === 'uniform_v' ? `
                                <line x1="30" y1="60" x2="175" y2="60" stroke="#38bdf8" stroke-width="3"/>
                                <text x="100" y="52" font-size="8" fill="#38bdf8" font-family="monospace">Slope = 0 (a = 0)</text>
                            ` : sim6State.mode === 'uniform_acc' ? `
                                <line x1="30" y1="85" x2="165" y2="30" stroke="#10b981" stroke-width="3"/>
                                <polygon points="90,60 145,60 145,38" fill="#10b981" opacity="0.2"/>
                                <line x1="90" y1="60" x2="145" y2="60" stroke="#cbd5e1" stroke-dasharray="2,2"/>
                                <line x1="145" y1="60" x2="145" y2="38" stroke="#cbd5e1" stroke-dasharray="2,2"/>
                                <text x="115" y="70" font-size="6" fill="#cbd5e1" font-family="monospace">Δt</text>
                                <text x="150" y="50" font-size="6" fill="#cbd5e1" font-family="monospace">Δv</text>
                            ` : `
                                <line x1="30" y1="30" x2="165" y2="95" stroke="#ef4444" stroke-width="3"/>
                                <text x="100" y="50" font-size="8" fill="#ef4444" font-family="monospace">Negative Slope (Retardation)</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Metric -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs flex justify-between items-center">
                        <span class="text-slate-400">Calculated Acceleration:</span>
                        <span class="text-emerald-400 font-bold text-sm">${{cur.a}}</span>
                    </div>
                </div>
            `;
        }}

        window.sim6SetMode = m => {{ sim6State.mode = m; renderSim6(document.getElementById('interactiveViewport')); }};

        // Sim 7: Velocity-Time Area Integrator
        function renderSim7(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Displacement = Area Under v-t Graph (Rectangle + Triangle)
                    </div>

                    <!-- Highlight Mode -->
                    <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        <button onclick="window.sim7SetHighlight('rect')" class="py-1 rounded ${{sim7State.highlight === 'rect' ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Rectangle (ut)</button>
                        <button onclick="window.sim7SetHighlight('tri')" class="py-1 rounded ${{sim7State.highlight === 'tri' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Triangle (½at²)</button>
                        <button onclick="window.sim7SetHighlight('all')" class="py-1 rounded ${{sim7State.highlight === 'all' ? 'bg-purple-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Total Trapezium</button>
                    </div>

                    <!-- Area Diagram SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <line x1="30" y1="105" x2="185" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
                            <line x1="30" y1="105" x2="30" y2="15" stroke="#94a3b8" stroke-width="1.5"/>

                            <!-- Lower Rectangle (ut) -->
                            <rect x="30" y="65" width="130" height="40" fill="#3b82f6" opacity="${{sim7State.highlight === 'tri' ? 0.1 : 0.4}}" stroke="#38bdf8" stroke-width="1"/>
                            <text x="95" y="88" font-size="8" fill="#bae6fd" font-family="monospace" text-anchor="middle">Rectangle: ut = 100 m</text>

                            <!-- Upper Triangle (½at²) -->
                            <polygon points="30,65 160,65 160,25" fill="#10b981" opacity="${{sim7State.highlight === 'rect' ? 0.1 : 0.4}}" stroke="#34d399" stroke-width="1"/>
                            <text x="115" y="52" font-size="8" fill="#a7f3d0" font-family="monospace" text-anchor="middle">Triangle: ½at² = 100 m</text>

                            <!-- Inclined Line AB -->
                            <line x1="30" y1="65" x2="160" y2="25" stroke="#facc15" stroke-width="2.5"/>
                            <circle cx="30" cy="65" r="3" fill="#facc15"/>
                            <circle cx="160" cy="25" r="3" fill="#facc15"/>
                        </svg>
                    </div>

                    <!-- Area Summary -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between text-slate-300">
                            <span>Initial Velocity Contribution (ut):</span>
                            <span class="text-blue-400 font-bold">100 m</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Acceleration Contribution (½at²):</span>
                            <span class="text-emerald-400 font-bold">100 m</span>
                        </div>
                        <div class="border-t border-slate-800 pt-1 flex justify-between text-white font-bold">
                            <span>Total Displacement (s):</span>
                            <span class="text-purple-400">200 m</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim7SetHighlight = h => {{ sim7State.highlight = h; renderSim7(document.getElementById('interactiveViewport')); }};

        // Sim 8: 1st Kinematic Equation Derivation Engine (v = u + at)
        function renderSim8(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Graphical Derivation: v = u + at (Velocity-Time Relation)
                    </div>

                    <!-- Derivation Step Buttons -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        <button onclick="window.sim8SetStep(1)" class="py-1 rounded ${{sim8State.step === 1 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 1</button>
                        <button onclick="window.sim8SetStep(2)" class="py-1 rounded ${{sim8State.step === 2 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 2</button>
                        <button onclick="window.sim8SetStep(3)" class="py-1 rounded ${{sim8State.step === 3 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 3</button>
                        <button onclick="window.sim8SetStep(4)" class="py-1 rounded ${{sim8State.step === 4 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Result</button>
                    </div>

                    <!-- Step Explanation Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        ${{sim8State.step === 1 ? `
                            <div class="text-blue-400 font-bold">Step 1: Identify Coordinates</div>
                            <p class="text-slate-300 text-[11px] leading-relaxed">
                                Initial velocity OA = u. Final velocity BC = v. Time interval OC = AD = t.
                            </p>
                        ` : sim8State.step === 2 ? `
                            <div class="text-blue-400 font-bold">Step 2: Change in Velocity</div>
                            <p class="text-slate-300 text-[11px] leading-relaxed">
                                The vertical change BD = BC - CD = v - u.
                            </p>
                        ` : sim8State.step === 3 ? `
                            <div class="text-blue-400 font-bold">Step 3: Acceleration as Slope</div>
                            <div class="bg-slate-900 p-2 rounded text-emerald-300 text-center">
                                a = Slope = BD / AD = (v - u) / t
                            </div>
                        ` : `
                            <div class="text-emerald-400 font-bold text-center text-base">
                                ➔ v = u + at
                            </div>
                            <p class="text-slate-300 text-[11px] text-center leading-relaxed">
                                Multiplying by t yields at = v - u, so v = u + at.
                            </p>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim8SetStep = s => {{ sim8State.step = s; renderSim8(document.getElementById('interactiveViewport')); }};

        // Sim 9: 2nd Kinematic Equation Derivation Engine (s = ut + ½at²)
        function renderSim9(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Graphical Derivation: s = ut + ½at² (Position-Time Relation)
                    </div>

                    <!-- Step Buttons -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        <button onclick="window.sim9SetStep(1)" class="py-1 rounded ${{sim9State.step === 1 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 1</button>
                        <button onclick="window.sim9SetStep(2)" class="py-1 rounded ${{sim9State.step === 2 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 2</button>
                        <button onclick="window.sim9SetStep(3)" class="py-1 rounded ${{sim9State.step === 3 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 3</button>
                        <button onclick="window.sim9SetStep(4)" class="py-1 rounded ${{sim9State.step === 4 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Result</button>
                    </div>

                    <!-- Step Explanation Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        ${{sim9State.step === 1 ? `
                            <div class="text-blue-400 font-bold">Step 1: Total Area under v-t Graph</div>
                            <p class="text-slate-300 text-[11px] leading-relaxed">
                                Distance s = Area of Trapezium OABC = Area(Rectangle OADC) + Area(Triangle ABD).
                            </p>
                        ` : sim9State.step === 2 ? `
                            <div class="text-blue-400 font-bold">Step 2: Area of Rectangle OADC</div>
                            <div class="bg-slate-900 p-2 rounded text-cyan-300 text-center">
                                Area(OADC) = OA × OC = u × t = ut
                            </div>
                        ` : sim9State.step === 3 ? `
                            <div class="text-blue-400 font-bold">Step 3: Area of Triangle ABD</div>
                            <div class="bg-slate-900 p-2 rounded text-emerald-300 text-center">
                                Area(ABD) = ½ × AD × BD = ½ × t × (at) = ½at²
                            </div>
                        ` : `
                            <div class="text-emerald-400 font-bold text-center text-base">
                                ➔ s = ut + ½at²
                            </div>
                            <p class="text-slate-300 text-[11px] text-center leading-relaxed">
                                Summing the rectangle (ut) and triangle (½at²) gives the second equation of motion.
                            </p>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim9SetStep = s => {{ sim9State.step = s; renderSim9(document.getElementById('interactiveViewport')); }};

        // Sim 10: 3rd Kinematic Equation Derivation Engine (v² = u² + 2as)
        function renderSim10(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Graphical Derivation: v² = u² + 2as (Position-Velocity Relation)
                    </div>

                    <!-- Step Buttons -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        <button onclick="window.sim10SetStep(1)" class="py-1 rounded ${{sim10State.step === 1 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 1</button>
                        <button onclick="window.sim10SetStep(2)" class="py-1 rounded ${{sim10State.step === 2 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 2</button>
                        <button onclick="window.sim10SetStep(3)" class="py-1 rounded ${{sim10State.step === 3 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Step 3</button>
                        <button onclick="window.sim10SetStep(4)" class="py-1 rounded ${{sim10State.step === 4 ? 'bg-blue-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Result</button>
                    </div>

                    <!-- Step Explanation Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        ${{sim10State.step === 1 ? `
                            <div class="text-blue-400 font-bold">Step 1: Area of Trapezium Formula</div>
                            <div class="bg-slate-900 p-2 rounded text-cyan-300 text-center">
                                s = [(OA + BC) × OC] / 2 = [(u + v) × t] / 2
                            </div>
                        ` : sim10State.step === 2 ? `
                            <div class="text-blue-400 font-bold">Step 2: Eliminate Time (t)</div>
                            <p class="text-slate-300 text-[11px] leading-relaxed">
                                From 1st equation: v = u + at ➔ t = (v - u) / a.
                            </p>
                        ` : sim10State.step === 3 ? `
                            <div class="text-blue-400 font-bold">Step 3: Substitute t into Area</div>
                            <div class="bg-slate-900 p-2 rounded text-emerald-300 text-center">
                                s = [(v + u)(v - u)] / 2a = (v² - u²) / 2a
                            </div>
                        ` : `
                            <div class="text-emerald-400 font-bold text-center text-base">
                                ➔ 2as = v² - u²  (v² = u² + 2as)
                            </div>
                            <p class="text-slate-300 text-[11px] text-center leading-relaxed">
                                Cross-multiplying 2a yields the time-independent 3rd equation of motion.
                            </p>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim10SetStep = s => {{ sim10State.step = s; renderSim10(document.getElementById('interactiveViewport')); }};

        // Sim 11: Interactive Kinematic Equation Solver & Motion Replay
        function renderSim11(vp) {{
            const u = sim11State.u;
            const a = sim11State.a;
            const t = sim11State.t;
            const v = u + a * t;
            const s = u * t + 0.5 * a * t * t;

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Kinematic Equation Calculator & Motion Replay
                    </div>

                    <!-- Input Controls -->
                    <div class="grid grid-cols-3 gap-2 bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <div>
                            <span class="text-slate-400 block text-[10px]">Initial u (m/s):</span>
                            <input type="number" value="${{u}}" onchange="window.sim11SetU(this.value)" class="w-full bg-slate-950 border border-slate-700 rounded px-1.5 py-0.5 text-white">
                        </div>
                        <div>
                            <span class="text-slate-400 block text-[10px]">Accel a (m/s²):</span>
                            <input type="number" value="${{a}}" onchange="window.sim11SetA(this.value)" class="w-full bg-slate-950 border border-slate-700 rounded px-1.5 py-0.5 text-white">
                        </div>
                        <div>
                            <span class="text-slate-400 block text-[10px]">Time t (s):</span>
                            <input type="number" value="${{t}}" onchange="window.sim11SetT(this.value)" class="w-full bg-slate-950 border border-slate-700 rounded px-1.5 py-0.5 text-white">
                        </div>
                    </div>

                    <!-- Output Results -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Final Velocity (v):</span>
                            <span class="text-emerald-400 font-bold text-base">${{v.toFixed(1)}} m/s</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Distance Travelled (s):</span>
                            <span class="text-cyan-300 font-bold text-base">${{s.toFixed(1)}} m</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim11SetU = val => {{ sim11State.u = parseFloat(val); renderSim11(document.getElementById('interactiveViewport')); }};
        window.sim11SetA = val => {{ sim11State.a = parseFloat(val); renderSim11(document.getElementById('interactiveViewport')); }};
        window.sim11SetT = val => {{ sim11State.t = parseFloat(val); renderSim11(document.getElementById('interactiveViewport')); }};

        // Sim 12: Vertical Motion & Free Fall Under Gravity
        function renderSim12(vp) {{
            const u = sim12State.u;
            const g = sim12State.g;
            const hMax = (u * u) / (2 * g);
            const tUp = u / g;

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Vertical Motion Under Gravity: a = -g
                    </div>

                    <!-- Controls -->
                    <div class="space-y-2 bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <div class="flex justify-between">
                            <span class="text-slate-300">Launch Velocity (u):</span>
                            <span class="text-cyan-300 font-bold">${{u}} m/s</span>
                        </div>
                        <input type="range" min="10" max="40" step="5" value="${{u}}" oninput="window.sim12SetU(this.value)" class="w-full accent-cyan-500">
                        <div class="flex justify-between items-center pt-1 border-t border-slate-800">
                            <span class="text-slate-400">Environment:</span>
                            <div class="flex gap-1 text-[10px]">
                                <button onclick="window.sim12SetG(9.8)" class="px-2 py-0.5 rounded ${{sim12State.g === 9.8 ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}}">Earth (9.8)</button>
                                <button onclick="window.sim12SetG(1.6)" class="px-2 py-0.5 rounded ${{sim12State.g === 1.6 ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}}">Moon (1.6)</button>
                            </div>
                        </div>
                    </div>

                    <!-- Results -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Maximum Height (h_max):</span>
                            <span class="text-emerald-400 font-bold text-base">${{hMax.toFixed(1)}} m</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Time to Peak (t = u/g):</span>
                            <span class="text-cyan-300 font-bold text-base">${{tUp.toFixed(2)}} s</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim12SetU = val => {{ sim12State.u = parseFloat(val); renderSim12(document.getElementById('interactiveViewport')); }};
        window.sim12SetG = val => {{ sim12State.g = parseFloat(val); renderSim12(document.getElementById('interactiveViewport')); }};

        // Sim 13: Uniform Circular Motion & Tangential Speed
        function renderSim13(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Uniform Circular Motion: v = 2πr / T (Tangential Velocity)
                    </div>

                    <!-- SVG Circle -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 160 140" class="w-40 h-36">
                            <!-- Circular path -->
                            <circle cx="80" cy="70" r="45" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="${{sim13State.cut ? '4,4' : 'none'}}"/>
                            <circle cx="80" cy="70" r="3" fill="#64748b"/>

                            ${{!sim13State.cut ? `
                                <!-- Whirling particle on circle -->
                                <circle cx="80" cy="25" r="7" fill="#f59e0b"/>
                                <!-- String radius -->
                                <line x1="80" y1="70" x2="80" y2="25" stroke="#94a3b8" stroke-width="1.5"/>
                                <text x="85" y="52" font-size="7" fill="#94a3b8" font-family="monospace">r</text>

                                <!-- Tangential velocity arrow -->
                                <line x1="80" y1="25" x2="125" y2="25" stroke="#38bdf8" stroke-width="2.5"/>
                                <polygon points="125,22 125,28 130,25" fill="#38bdf8"/>
                                <text x="105" y="18" font-size="7" font-weight="bold" fill="#38bdf8" font-family="monospace">Velocity v</text>
                            ` : `
                                <!-- Cut string: Flies tangentially -->
                                <line x1="80" y1="70" x2="80" y2="40" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
                                <circle cx="130" cy="25" r="7" fill="#ef4444"/>
                                <line x1="80" y1="25" x2="145" y2="25" stroke="#ef4444" stroke-width="2"/>
                                <polygon points="145,22 145,28 150,25" fill="#ef4444"/>
                                <text x="80" y="50" font-size="7" fill="#ef4444" font-family="monospace" text-anchor="middle">Tangential Flight!</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Cut String Button -->
                    <button onclick="window.sim13ToggleCut()" class="w-full py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-md">
                        ${{!sim13State.cut ? "Cut Whirling String (Release Centripetal Force)" : "Reset Circular Orbit"}}
                    </button>
                </div>
            `;
        }}

        window.sim13ToggleCut = () => {{ sim13State.cut = !sim13State.cut; renderSim13(document.getElementById('interactiveViewport')); }};

        // Sim 14: Centripetal Acceleration & Orbit Dynamics
        function renderSim14(vp) {{
            const r = sim14State.r;
            const v = sim14State.v;
            const ac = (v * v) / r;

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Centripetal Acceleration: a_c = v² / r
                    </div>

                    <!-- Sliders -->
                    <div class="space-y-2 bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs">
                        <div>
                            <div class="flex justify-between">
                                <span class="text-slate-300">Speed (v):</span>
                                <span class="text-cyan-300 font-bold">${{v}} m/s</span>
                            </div>
                            <input type="range" min="10" max="40" step="2" value="${{v}}" oninput="window.sim14SetV(this.value)" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <div class="flex justify-between">
                                <span class="text-slate-300">Radius (r):</span>
                                <span class="text-amber-400 font-bold">${{r}} m</span>
                            </div>
                            <input type="range" min="50" max="200" step="10" value="${{r}}" oninput="window.sim14SetR(this.value)" class="w-full accent-amber-500">
                        </div>
                    </div>

                    <!-- Metric Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs flex justify-between items-center">
                        <span class="text-slate-400">Centripetal Acceleration (a_c):</span>
                        <span class="text-emerald-400 font-bold text-base">${{ac.toFixed(2)}} m/s²</span>
                    </div>
                </div>
            `;
        }}

        window.sim14SetV = val => {{ sim14State.v = parseFloat(val); renderSim14(document.getElementById('interactiveViewport')); }};
        window.sim14SetR = val => {{ sim14State.r = parseFloat(val); renderSim14(document.getElementById('interactiveViewport')); }};

        // Sim 15: Road Safety Physics: Reaction Time & Braking Distance
        function renderSim15(vp) {{
            const spd = sim15State.speedKm;
            const vMs = spd * (5 / 18);
            const tr = sim15State.distracted ? 1.5 : 0.7; // reaction time
            const a = 6.0; // braking deceleration

            const dThink = vMs * tr;
            const dBrake = (vMs * vMs) / (2 * a);
            const dTotal = dThink + dBrake;

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Total Stopping Distance = Thinking + Braking (s ∝ v²)
                    </div>

                    <!-- Speed & Attention Controls -->
                    <div class="space-y-2 bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs">
                        <div class="flex justify-between">
                            <span class="text-slate-300">Driving Speed:</span>
                            <span class="text-amber-400 font-bold">${{spd}} km/h (${{vMs.toFixed(1)}} m/s)</span>
                        </div>
                        <input type="range" min="30" max="120" step="10" value="${{spd}}" oninput="window.sim15SetSpeed(this.value)" class="w-full accent-amber-500">
                        <div class="flex justify-between items-center pt-1 border-t border-slate-800">
                            <span class="text-slate-400">Driver State:</span>
                            <div class="flex gap-1 text-[10px]">
                                <button onclick="window.sim15SetDistracted(false)" class="px-2 py-0.5 rounded ${{!sim15State.distracted ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}}">Alert (0.7s)</button>
                                <button onclick="window.sim15SetDistracted(true)" class="px-2 py-0.5 rounded ${{sim15State.distracted ? 'bg-rose-600 text-white' : 'bg-slate-800 text-slate-400'}}">Phone/Distracted (1.5s)</button>
                            </div>
                        </div>
                    </div>

                    <!-- Breakdown Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between text-cyan-300">
                            <span>Thinking Distance:</span>
                            <span class="font-bold">${{dThink.toFixed(1)}} m</span>
                        </div>
                        <div class="flex justify-between text-amber-400">
                            <span>Braking Distance (v²/2a):</span>
                            <span class="font-bold">${{dBrake.toFixed(1)}} m</span>
                        </div>
                        <div class="border-t border-slate-800 pt-1 flex justify-between text-rose-400 font-bold text-sm">
                            <span>Total Stopping Distance:</span>
                            <span>${{dTotal.toFixed(1)}} m</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim15SetSpeed = val => {{ sim15State.speedKm = parseInt(val); renderSim15(document.getElementById('interactiveViewport')); }};
        window.sim15SetDistracted = d => {{ sim15State.distracted = d; renderSim15(document.getElementById('interactiveViewport')); }};

        // Sim 16: Cosmic Speed Limit & Special Relativity Sandbox
        function renderSim16(vp) {{
            const vFrac = sim16State.vFraction;
            // Time dilation gamma = 1 / sqrt(1 - v^2)
            const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - vFrac * vFrac));

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-blue-400 font-bold text-center">
                        Cosmic Speed Limit (c = 3.0×10⁸ m/s) & Relativity
                    </div>

                    <!-- Velocity Fraction Slider -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-1 font-mono text-xs">
                        <div class="flex justify-between text-slate-300">
                            <span>Speed Fraction (v / c):</span>
                            <span class="text-cyan-300 font-bold">${{vFrac.toFixed(2)}} c</span>
                        </div>
                        <input type="range" min="0.05" max="0.95" step="0.05" value="${{vFrac}}" oninput="window.sim16SetV(this.value)" class="w-full accent-cyan-500">
                        <div class="flex justify-between text-[9px] text-slate-500">
                            <span>0.1c (Everyday v ≪ c)</span>
                            <span>0.5c</span>
                            <span>0.95c (Near Light Speed)</span>
                        </div>
                    </div>

                    <!-- Relativistic Dilation Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between">
                            <span class="text-slate-400">Lorentz Factor (γ):</span>
                            <span class="text-emerald-400 font-bold">${{gamma.toFixed(2)}}×</span>
                        </div>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            At everyday speeds (cars, planes), v/c ≈ 0 and γ = 1.0000000. Classical kinematics (v = u + at) is an exact low-speed reality.
                        </p>
                    </div>
                </div>
            `;
        }}

        window.sim16SetV = val => {{ sim16State.vFraction = parseFloat(val); renderSim16(document.getElementById('interactiveViewport')); }};

        // ==========================================
        // DEDICATED QUIZ SLIDES (17-20) RENDERING
        // ==========================================
        function renderQuizSlide(vp, slide) {{
            const quizList = slide.quiz || [];
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3 max-h-[500px] overflow-y-auto pr-1 scrollbar-thin">
                    <div class="text-xs font-mono text-blue-400 font-bold border-b border-slate-800 pb-1 flex justify-between">
                        <span>${{slide.title}}</span>
                        <span class="text-slate-400 font-normal">10 Questions</span>
                    </div>
                    ${{quizList.map(q => `
                        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col gap-2">
                            <div class="text-xs font-semibold text-slate-200">
                                ${{q.q}}
                            </div>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs">
                                ${{q.options.map((opt, oIdx) => `
                                    <button onclick="handleQuizAnswer('${{q.id}}', ${{oIdx}}, ${{q.ans}})" id="quiz-btn-${{q.id}}-${{oIdx}}" class="text-left px-2 py-1 rounded border border-slate-800 bg-slate-900 hover:bg-slate-800 text-slate-300 transition">
                                        ${{opt}}
                                    </button>
                                `).join('')}}
                            </div>
                            <div class="flex justify-end pt-1">
                                <button onclick="openSolutionModal('${{q.q.replace(/'/g, "\\\\'") }}', '${{q.sol.replace(/'/g, "\\\\'") }}')" class="px-2.5 py-1 rounded bg-blue-600/20 hover:bg-blue-600/30 text-blue-300 border border-blue-500/30 text-[10px] font-mono font-bold transition flex items-center gap-1">
                                    <span>🔍</span> View Solution
                                </button>
                            </div>
                        </div>
                    `).join('')}}
                </div>
            `;
        }}

        window.handleQuizAnswer = (qId, selectedIdx, correctIdx) => {{
            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`quiz-btn-${{qId}}-${{i}}`);
                if (!btn) continue;
                if (i === correctIdx) {{
                    btn.className = 'text-left px-2 py-1 rounded border border-emerald-500 bg-emerald-500/20 text-emerald-200 font-bold';
                }} else if (i === selectedIdx) {{
                    btn.className = 'text-left px-2 py-1 rounded border border-rose-500 bg-rose-500/20 text-rose-300';
                }} else {{
                    btn.className = 'text-left px-2 py-1 rounded border border-slate-800 bg-slate-950 text-slate-600 opacity-40';
                }}
            }}
        }};
    </script>
</body>
</html>
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated {OUTPUT_PATH} ({len(html_content.encode('utf-8'))} bytes).")

if __name__ == "__main__":
    generate_html()

