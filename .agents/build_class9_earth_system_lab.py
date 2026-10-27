# -*- coding: utf-8 -*-
"""
Builder script for NCERT Class 9 Science Chapter 8: Earth as a System: Energy, Matter & Life
Outputs: public/animations/class9-earth-as-a-system.html
"""

import os
import json
from class9_earth_system_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-earth-as-a-system.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Science • Chapter 8 • Earth as a System: Energy, Matter & Life Master Lab</title>
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
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-600 flex items-center justify-center text-white font-extrabold shadow-lg shadow-emerald-500/20 text-lg tracking-wider">
                9S
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-emerald-400 tracking-wider uppercase font-mono">NCERT Class 9 Science • Ch 8</span>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">12 Periods</span>
                </div>
                <h1 class="text-sm md:text-base font-bold text-slate-100 tracking-tight">Earth as a System: Energy, Matter & Life</h1>
            </div>
        </div>

        <!-- Controls: Sound Toggle, Slide Counter, Navigation -->
        <div class="flex items-center gap-2 md:gap-4">
            <button id="soundToggleBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 flex items-center gap-2 transition shadow-sm">
                <span id="soundIcon">🔊</span>
                <span id="soundText" class="hidden sm:inline">Voice: ON</span>
            </button>
            <div class="text-xs font-mono font-medium text-slate-400 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
                Slide <span id="currentSlideNum" class="text-emerald-400 font-bold">1</span> / 20
            </div>
            <div class="flex items-center gap-1">
                <button id="prevBtn" onclick="changeSlide(-1)" class="w-9 h-9 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-slate-200 transition font-bold">
                    ◀
                </button>
                <button id="nextBtn" onclick="changeSlide(1)" class="w-9 h-9 rounded-lg border border-emerald-500/50 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-white transition font-bold shadow-md shadow-emerald-600/30">
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
            <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-emerald-950/40 border border-slate-800 rounded-2xl p-4 shadow-xl flex items-center gap-4 relative overflow-hidden">
                <div class="absolute -right-8 -top-8 w-32 h-32 bg-emerald-500/10 rounded-full blur-2xl pointer-events-none"></div>

                <!-- Mentor Avatar SVG -->
                <div class="relative w-16 h-16 shrink-0 rounded-2xl bg-slate-800 border-2 border-emerald-400/40 p-1 flex items-center justify-center shadow-lg">
                    <svg viewBox="0 0 100 100" class="w-full h-full">
                        <!-- Lab Coat & Collar -->
                        <path d="M 20 90 L 32 68 L 68 68 L 80 90 Z" fill="#10b981"/>
                        <path d="M 38 68 L 50 82 L 62 68 Z" fill="#047857"/>
                        <!-- Neck -->
                        <rect x="44" y="56" width="12" height="15" rx="3" fill="#fed7aa"/>
                        <!-- Head -->
                        <circle cx="50" cy="40" r="22" fill="#fed7aa"/>
                        <!-- Hair -->
                        <path d="M 26 40 C 26 20, 74 20, 74 40 C 74 24, 66 18, 50 18 C 34 18, 26 24, 26 40 Z" fill="#0f172a"/>
                        <path d="M 26 36 C 24 50, 24 64, 30 68 C 30 52, 34 44, 34 44 Z" fill="#0f172a"/>
                        <path d="M 74 36 C 76 50, 76 64, 70 68 C 70 52, 66 44, 66 44 Z" fill="#0f172a"/>
                        <!-- Glasses -->
                        <rect x="33" y="34" width="14" height="10" rx="3" fill="none" stroke="#059669" stroke-width="2.2"/>
                        <rect x="53" y="34" width="14" height="10" rx="3" fill="none" stroke="#059669" stroke-width="2.2"/>
                        <line x1="47" y1="39" x2="53" y2="39" stroke="#059669" stroke-width="2"/>
                        <!-- Eyes -->
                        <circle cx="40" cy="39" r="2" fill="#0f172a"/>
                        <circle cx="60" cy="39" r="2" fill="#0f172a"/>
                        <!-- Smile / Talking Mouth -->
                        <rect id="teacherMouth" x="44" y="50" width="12" height="4" rx="2" fill="#dc2626"/>
                    </svg>
                    <span class="absolute -bottom-1 -right-1 flex h-3.5 w-3.5">
                        <span id="speakerPulse" class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75 hidden"></span>
                        <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-emerald-500 border-2 border-slate-900"></span>
                    </span>
                </div>

                <div class="flex-1">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-emerald-300 font-mono">Prof. Sophia</span>
                            <span class="text-[10px] bg-slate-800 text-slate-400 px-2 py-0.5 rounded border border-slate-700">Earth Systems Science</span>
                        </div>
                        <button onclick="replayVoice()" class="text-xs text-slate-400 hover:text-emerald-400 flex items-center gap-1 transition">
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
                    <span id="slideBadge" class="text-[11px] font-mono font-semibold px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
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
                    <div class="text-[11px] font-bold text-emerald-300 font-mono uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
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
                        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span id="panelHeaderTitle" class="text-xs font-bold text-emerald-300 font-mono uppercase tracking-wider">
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
                    <span id="simHelpText">Interact with the controls above to explore Earth's system dynamics.</span>
                    <button onclick="resetCurrentSimulation()" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-mono text-slate-300 border border-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

        </div>

    </main>

    <!-- Last Slide Notice Container (Strict Requirement) -->
    <div id="lastSlideNotice" class="hidden max-w-7xl mx-auto px-4 py-4 w-full">
        <div class="bg-gradient-to-r from-teal-950/80 via-slate-900 to-emerald-950/80 border-2 border-emerald-500/50 rounded-2xl p-6 text-center shadow-2xl flex flex-col items-center justify-center gap-3">
            <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-3xl">
                🌍
            </div>
            <h3 class="text-lg md:text-xl font-bold text-emerald-300 tracking-wide">
                You have reached the last slide of this chapter
            </h3>
            <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
                You have completed your mastery of <strong>Earth as a System: Energy, Matter & Life</strong>—including the interconnectedness of Earth's 5 spheres, the electromagnetic spectrum, differential heating, surface albedo, local and global wind belts, biogeochemical cycles (water, carbon, nitrogen, oxygen), human greenhouse destabilization, traditional Indian water systems, and the zero differential heating frontier!
            </p>
            <div class="flex items-center gap-3 mt-2">
                <button onclick="jumpToSlide(1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 border border-slate-700 transition">
                    ↺ Restart Lab
                </button>
                <button onclick="jumpToSlide(17)" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition shadow-lg shadow-emerald-600/30">
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
                <h4 class="text-base font-bold text-emerald-300 font-mono">Step-by-Step Solution</h4>
            </div>
            <div id="solutionQuestionText" class="text-xs text-slate-400 border-l-2 border-emerald-500 pl-3 italic">
                <!-- Question -->
            </div>
            <div id="solutionBodyText" class="text-xs md:text-sm text-slate-200 leading-relaxed bg-slate-950 p-4 rounded-xl border border-slate-800">
                <!-- Detailed explanation -->
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow-md transition">
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
        let sim1State = {{ activeSphere: 'atmo' }};
        let sim2State = {{ bandIdx: 3 }}; // Visible light default
        let sim3State = {{ clouds: 23, ozone: 300 }};
        let sim4State = {{ latitude: 0, season: 'summer' }};
        let sim5State = {{ surface: 'ocean' }};
        let sim6State = {{ coriolis: true }};
        let sim7State = {{ timeOfDay: 'day' }};
        let sim8State = {{ timeOfDay: 'day' }};
        let sim9State = {{ activeStage: 'evap' }};
        let sim10State = {{ emissions: 10 }};
        let sim11State = {{ activeStep: 1 }};
        let sim12State = {{ viewMode: 'chapman' }};
        let sim13State = {{ activeStress: 'none' }};
        let sim14State = {{ co2Ppm: 420 }};
        let sim15State = {{ activeRegion: 'rajasthan' }};
        let sim16State = {{ mode: 'real' }};

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
                        el.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-mono font-bold border border-emerald-500 bg-emerald-500/20 text-emerald-300 shadow-sm shrink-0';
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
                        <span class="text-xs font-bold font-mono text-emerald-400 uppercase tracking-wider">🎯 In-Slide Checkpoints</span>
                        <span class="text-[10px] text-slate-400">(Immediate Feedback)</span>
                    </div>
                    ${{slide.checkpoints.map(cp => `
                        <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 shadow-sm flex flex-col gap-2.5">
                            <div class="text-xs font-semibold text-slate-200 flex items-start gap-2">
                                <span class="px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono text-[10px] shrink-0 font-bold">CP ${{cp.num}}</span>
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
                                <strong class="text-emerald-400">Prof. Sophia:</strong> ${{cp.exp}}
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
                simHelp.textContent = "Use the interactive controls to test and verify Earth system dynamics.";

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
                case 1: sim1State = {{ activeSphere: 'atmo' }}; break;
                case 2: sim2State = {{ bandIdx: 3 }}; break;
                case 3: sim3State = {{ clouds: 23, ozone: 300 }}; break;
                case 4: sim4State = {{ latitude: 0, season: 'summer' }}; break;
                case 5: sim5State = {{ surface: 'ocean' }}; break;
                case 6: sim6State = {{ coriolis: true }}; break;
                case 7: sim7State = {{ timeOfDay: 'day' }}; break;
                case 8: sim8State = {{ timeOfDay: 'day' }}; break;
                case 9: sim9State = {{ activeStage: 'evap' }}; break;
                case 10: sim10State = {{ emissions: 10 }}; break;
                case 11: sim11State = {{ activeStep: 1 }}; break;
                case 12: sim12State = {{ viewMode: 'chapman' }}; break;
                case 13: sim13State = {{ activeStress: 'none' }}; break;
                case 14: sim14State = {{ co2Ppm: 420 }}; break;
                case 15: sim15State = {{ activeRegion: 'rajasthan' }}; break;
                case 16: sim16State = {{ mode: 'real' }}; break;
            }}
            renderRightViewport(SLIDES[currentSlideIndex]);
        }}

        // ==========================================
        // 16 BESPOKE SIMULATOR IMPLEMENTATIONS
        // ==========================================

        // Sim 1: 5 Spheres Dynamic Coupling Explorer
        function renderSim1(vp) {{
            const spheres = [
                {{ key: "atmo", name: "Atmosphere", color: "#38bdf8", desc: "Gas envelope: filters UV, provides CO₂/O₂, transports moisture." }},
                {{ key: "hydro", name: "Hydrosphere", color: "#0284c7", desc: "Liquid water: covers 71% of surface, primary planetary heat sponge." }},
                {{ key: "geo", name: "Geosphere", color: "#a16207", desc: "Solid rock and soil: provides minerals, volcanic fluxes, continental plates." }},
                {{ key: "cryo", name: "Cryosphere", color: "#cbd5e1", desc: "Frozen realm: ice caps, sea ice, controls planetary albedo and sea levels." }},
                {{ key: "bio", name: "Biosphere", color: "#10b981", desc: "Living realm: photosynthesizers, microbes, drives biogeochemical cycles." }}
            ];

            const cur = spheres.find(s => s.key === sim1State.activeSphere) || spheres[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Dynamic Coupling Across Earth's 5 Spheres (C-2.8)
                    </div>

                    <!-- 5 Sphere Buttons -->
                    <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{spheres.map(s => `
                            <button onclick="window.sim1SetSphere('${{s.key}}')" class="py-1 rounded ${{sim1State.activeSphere === s.key ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{s.name.slice(0,4)}}</button>
                        `).join('')}}
                    </div>

                    <!-- Interactive Pentagonal Node SVG -->
                    <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 160" class="w-48 h-40">
                            <!-- Pentagonal Connecting Lines -->
                            <polygon points="100,20 176,55 147,135 53,135 24,55" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="3,3"/>
                            <!-- Center radiating lines -->
                            <line x1="100" y1="80" x2="100" y2="20" stroke="#059669" stroke-width="1.5"/>
                            <line x1="100" y1="80" x2="176" y2="55" stroke="#059669" stroke-width="1.5"/>
                            <line x1="100" y1="80" x2="147" y2="135" stroke="#059669" stroke-width="1.5"/>
                            <line x1="100" y1="80" x2="53" y2="135" stroke="#059669" stroke-width="1.5"/>
                            <line x1="100" y1="80" x2="24" y2="55" stroke="#059669" stroke-width="1.5"/>

                            <!-- Sphere Nodes -->
                            <circle cx="100" cy="20" r="16" fill="${{sim1State.activeSphere === 'atmo' ? '#38bdf8' : '#1e293b'}}" stroke="#38bdf8" stroke-width="2"/>
                            <text x="100" y="24" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">ATMO</text>

                            <circle cx="176" cy="55" r="16" fill="${{sim1State.activeSphere === 'hydro' ? '#0284c7' : '#1e293b'}}" stroke="#0284c7" stroke-width="2"/>
                            <text x="176" y="59" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">HYDRO</text>

                            <circle cx="147" cy="135" r="16" fill="${{sim1State.activeSphere === 'geo' ? '#a16207' : '#1e293b'}}" stroke="#a16207" stroke-width="2"/>
                            <text x="147" y="139" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">GEO</text>

                            <circle cx="53" cy="135" r="16" fill="${{sim1State.activeSphere === 'cryo' ? '#cbd5e1' : '#1e293b'}}" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="53" y="139" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">CRYO</text>

                            <circle cx="24" cy="55" r="16" fill="${{sim1State.activeSphere === 'bio' ? '#10b981' : '#1e293b'}}" stroke="#10b981" stroke-width="2"/>
                            <text x="24" y="59" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle">BIO</text>

                            <!-- Center Sun / Energy driver -->
                            <circle cx="100" cy="80" r="12" fill="#f59e0b"/>
                            <text x="100" y="83" font-size="7" font-weight="bold" fill="#000" text-anchor="middle">SUN</text>
                        </svg>
                    </div>

                    <!-- Selected Sphere Detail Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <div class="flex justify-between items-center text-emerald-400 font-bold mb-1">
                            <span>Domain: ${{cur.name}}</span>
                            <span class="text-[10px] text-slate-400">Open Energy System</span>
                        </div>
                        <p class="text-[11px] text-slate-300 leading-relaxed">${{cur.desc}}</p>
                    </div>
                </div>
            `;
        }}

        window.sim1SetSphere = k => {{ sim1State.activeSphere = k; renderSim1(document.getElementById('interactiveViewport')); }};

        // Sim 2: Electromagnetic Spectrum & Frequency Engine
        function renderSim2(vp) {{
            const bands = [
                {{ name: "Gamma Rays", wl: "< 10⁻¹² m", freq: "> 10²⁰ Hz", energy: "> 1 MeV", blocked: "Blocked by upper atmosphere (Thermosphere/Mesosphere)" }},
                {{ name: "X-Rays", wl: "10⁻¹² - 10⁻⁹ m", freq: "10¹⁷ - 10²⁰ Hz", energy: "100 eV - 100 keV", blocked: "Blocked by atmospheric nitrogen & oxygen" }},
                {{ name: "Ultraviolet (UV)", wl: "10 - 400 nm", freq: "7.5×10¹⁴ - 3×10¹⁶ Hz", energy: "3 - 100 eV", blocked: "UV-C & UV-B absorbed by Stratospheric Ozone (O₃)" }},
                {{ name: "Visible Light", wl: "400 - 700 nm", freq: "4×10¹⁴ - 7.5×10¹⁴ Hz", energy: "1.8 - 3.1 eV", blocked: "Transmitted cleanly to Earth's surface (Optical Window)" }},
                {{ name: "Infrared (IR)", wl: "700 nm - 1 mm", freq: "3×10¹¹ - 4×10¹⁴ Hz", energy: "0.001 - 1.8 eV", blocked: "Selectively absorbed by H₂O vapour, CO₂ (Greenhouse Effect)" }},
                {{ name: "Microwaves", wl: "1 mm - 1 m", freq: "3×10⁸ - 3×10¹¹ Hz", energy: "< 0.001 eV", blocked: "Used in radar & satellite meteorology" }},
                {{ name: "Radio Waves", wl: "> 1 m", freq: "< 3×10⁸ Hz", energy: "< 10⁻⁶ eV", blocked: "Reflected by Ionosphere; reaches Earth" }}
            ];

            const cur = bands[sim2State.bandIdx] || bands[3];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Solar Electromagnetic Spectrum & Speed of Light: c = λ·ν
                    </div>

                    <!-- Band Slider -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-1">
                        <div class="flex justify-between text-xs font-mono text-slate-300">
                            <span>Spectrum Band:</span>
                            <span class="text-emerald-400 font-bold">${{cur.name}}</span>
                        </div>
                        <input type="range" min="0" max="6" step="1" value="${{sim2State.bandIdx}}" oninput="window.sim2SetBand(this.value)" class="w-full accent-emerald-500">
                        <div class="flex justify-between text-[9px] font-mono text-slate-500">
                            <span>Gamma</span>
                            <span>X-Ray</span>
                            <span>UV</span>
                            <span>Visible</span>
                            <span>Infrared</span>
                            <span>Micro</span>
                            <span>Radio</span>
                        </div>
                    </div>

                    <!-- Metrics Grid -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Wavelength (λ):</span>
                            <span class="text-cyan-300 font-bold text-sm">${{cur.wl}}</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Frequency (ν):</span>
                            <span class="text-emerald-400 font-bold text-sm">${{cur.freq}}</span>
                        </div>
                    </div>

                    <!-- Atmospheric Behavior Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="text-[10px] text-slate-400 uppercase tracking-widest">Atmospheric Transmission Status:</div>
                        <p class="text-slate-200 text-[11px] leading-relaxed">${{cur.blocked}}</p>
                    </div>
                </div>
            `;
        }}

        window.sim2SetBand = idx => {{ sim2State.bandIdx = parseInt(idx); renderSim2(document.getElementById('interactiveViewport')); }};

        // Sim 3: Earth's Radiation Budget & Atmospheric Filter
        function renderSim3(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Global Solar Radiation Budget: 100 Units Incoming
                    </div>

                    <!-- Global Budget Visual Graphic -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <!-- Top of Atmosphere Line -->
                            <line x1="10" y1="20" x2="190" y2="20" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
                            <text x="190" y="16" font-size="6" fill="#94a3b8" font-family="monospace" text-anchor="end">TOP OF ATMOSPHERE</text>

                            <!-- Incoming Solar Beam 100 units -->
                            <line x1="30" y1="5" x2="30" y2="20" stroke="#facc15" stroke-width="6"/>
                            <polygon points="26,20 34,20 30,26" fill="#facc15"/>
                            <text x="38" y="15" font-size="7" font-weight="bold" fill="#facc15" font-family="monospace">100% Solar</text>

                            <!-- 29% Reflected (Albedo) -->
                            <path d="M 30 25 Q 50 60 70 15" fill="none" stroke="#38bdf8" stroke-width="3"/>
                            <polygon points="68,12 74,17 73,12" fill="#38bdf8"/>
                            <text x="75" y="25" font-size="7" font-weight="bold" fill="#38bdf8" font-family="monospace">29% Reflected (Albedo)</text>

                            <!-- 23% Absorbed in Atmosphere -->
                            <rect x="25" y="45" width="150" height="30" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
                            <text x="100" y="63" font-size="7" fill="#cbd5e1" font-family="monospace" text-anchor="middle">Atmosphere & Clouds: 23% Absorbed</text>

                            <!-- 48% Reaching Earth Surface -->
                            <line x1="30" y1="75" x2="30" y2="105" stroke="#f59e0b" stroke-width="4"/>
                            <polygon points="26,105 34,105 30,111" fill="#f59e0b"/>

                            <!-- Ground Surface -->
                            <rect x="10" y="110" width="180" height="15" rx="2" fill="#1e293b" stroke="#059669" stroke-width="1.5"/>
                            <text x="100" y="121" font-size="7" font-weight="bold" fill="#10b981" font-family="monospace" text-anchor="middle">Earth Land & Ocean: 48% Absorbed</text>
                        </svg>
                    </div>

                    <!-- Breakdown Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between text-slate-300">
                            <span>Solar Constant (S₀):</span>
                            <span class="text-amber-400 font-bold">~1361 W/m²</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Direct Planetary Albedo:</span>
                            <span class="text-cyan-400 font-bold">29% (~0.29)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Surface Heat Influx:</span>
                            <span class="text-emerald-400 font-bold">48% (~165 W/m²)</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        // Sim 4: Orbit, Axial Tilt & Angle of Incidence
        function renderSim4(vp) {{
            const lats = [
                {{ lat: 0, name: "Equator (0°)", angle: "90° (Perpendicular)", footprint: "1.0× (Concentrated heat)" }},
                {{ lat: 23.5, name: "Tropic of Cancer (23.5° N)", angle: "66.5°", footprint: "1.1×" }},
                {{ lat: 45, name: "Mid-Latitudes (45° N)", angle: "45°", footprint: "1.41× (Spread heat)" }},
                {{ lat: 75, name: "Arctic Circle (75° N)", angle: "15° (Grazing)", footprint: "3.86× (Dispersed/Cold)" }}
            ];

            const cur = lats.find(l => l.lat === sim4State.latitude) || lats[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Latitudinal Differential Insolation (C-2.8)
                    </div>

                    <!-- Latitude Selector -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{lats.map(l => `
                            <button onclick="window.sim4SetLat(${{l.lat}})" class="py-1 rounded ${{sim4State.latitude === l.lat ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{l.name.split(' ')[0]}}</button>
                        `).join('')}}
                    </div>

                    <!-- Beam Spread Diagram SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 120" class="w-full h-32">
                            <!-- Sunlight parallel arrows -->
                            <line x1="10" y1="40" x2="80" y2="40" stroke="#facc15" stroke-width="3"/>
                            <line x1="10" y1="60" x2="80" y2="60" stroke="#facc15" stroke-width="3"/>
                            <line x1="10" y1="80" x2="80" y2="80" stroke="#facc15" stroke-width="3"/>

                            <!-- Curved Earth Surface -->
                            <path d="M 80 10 Q 120 60 80 110" fill="none" stroke="#10b981" stroke-width="4"/>
                            <text x="130" y="64" font-size="8" fill="#10b981" font-family="monospace">Earth's Curve</text>

                            <!-- Highlighted incident beam -->
                            <circle cx="80" cy="${{sim4State.latitude === 0 ? 60 : sim4State.latitude === 23.5 ? 45 : sim4State.latitude === 45 ? 30 : 15}}" r="5" fill="#ef4444"/>
                        </svg>
                    </div>

                    <!-- Observation Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between text-slate-300">
                            <span>Selected Region:</span>
                            <span class="text-white font-bold">${{cur.name}}</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Angle of Incidence:</span>
                            <span class="text-emerald-400 font-bold">${{cur.angle}}</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Beam Footprint Area:</span>
                            <span class="text-amber-400 font-bold">${{cur.footprint}}</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim4SetLat = lat => {{ sim4State.latitude = parseFloat(lat); renderSim4(document.getElementById('interactiveViewport')); }};

        // Sim 5: Surface Albedo & Reflectivity Comparator
        function renderSim5(vp) {{
            const surfaces = [
                {{ key: "snow", name: "Fresh Snow", albedo: 0.85, reflected: "85%", absorbed: "15%", tempRise: "+1.2°C" }},
                {{ key: "sea_ice", name: "Sea Ice", albedo: 0.60, reflected: "60%", absorbed: "40%", tempRise: "+3.5°C" }},
                {{ key: "sand", name: "Desert Sand", albedo: 0.40, reflected: "40%", absorbed: "60%", tempRise: "+7.8°C" }},
                {{ key: "forest", name: "Pine Forest", albedo: 0.15, reflected: "15%", absorbed: "85%", tempRise: "+11.4°C" }},
                {{ key: "ocean", name: "Deep Ocean", albedo: 0.07, reflected: "7%", absorbed: "93%", tempRise: "+14.0°C" }}
            ];

            const cur = surfaces.find(s => s.key === sim5State.surface) || surfaces[4];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Surface Albedo (α) & Solar Heat Absorption
                    </div>

                    <!-- Surface Selector -->
                    <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{surfaces.map(s => `
                            <button onclick="window.sim5SetSurf('${{s.key}}')" class="py-1 rounded ${{sim5State.surface === s.key ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{s.name.split(' ')[0]}}</button>
                        `).join('')}}
                    </div>

                    <!-- Albedo Bar Visualization -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
                        <div class="flex justify-between">
                            <span class="text-slate-300">Surface: <strong class="text-white">${{cur.name}}</strong></span>
                            <span class="text-emerald-400 font-bold">Albedo α = ${{cur.albedo}}</span>
                        </div>
                        <div class="w-full bg-slate-900 h-4 rounded-full overflow-hidden flex border border-slate-700">
                            <div class="bg-cyan-400 h-full flex items-center justify-center text-[9px] text-slate-950 font-bold" style="width: ${{cur.albedo * 100}}%">
                                Reflected (${{cur.reflected}})
                            </div>
                            <div class="bg-amber-500 h-full flex items-center justify-center text-[9px] text-slate-950 font-bold" style="width: ${{(1 - cur.albedo) * 100}}%">
                                Absorbed (${{cur.absorbed}})
                            </div>
                        </div>
                        <div class="flex justify-between text-[11px] text-slate-400 pt-1">
                            <span>Absorption Heating Potential:</span>
                            <span class="text-rose-400 font-bold">${{cur.tempRise}}</span>
                        </div>
                    </div>

                    <!-- Ice-Albedo Runaway Feedback Note -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-[11px] font-mono text-slate-300 leading-relaxed">
                        <strong class="text-amber-400">Feedback Alert:</strong> Melting fresh snow (α = 0.85) exposes dark ocean water (α = 0.07). The water absorbs 93% of sunlight instead of 15%, multiplying heat uptake by over 600%!
                    </div>
                </div>
            `;
        }}

        window.sim5SetSurf = k => {{ sim5State.surface = k; renderSim5(document.getElementById('interactiveViewport')); }};

        // Sim 6: Atmospheric Convection Cell & Coriolis Deflection
        function renderSim6(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Hadley Convection Cells & Coriolis Deflection
                    </div>

                    <!-- Convection Diagram SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-full h-32">
                            <!-- Equator to 30 N -->
                            <rect x="10" y="110" width="180" height="15" fill="#1e293b" stroke="#334155" stroke-width="1"/>
                            <text x="30" y="122" font-size="7" fill="#facc15" font-family="monospace">Equator (0°)</text>
                            <text x="170" y="122" font-size="7" fill="#38bdf8" font-family="monospace" text-anchor="end">30° N (Subtropical)</text>

                            <!-- Equatorial Thermal Updraft -->
                            <line x1="30" y1="105" x2="30" y2="40" stroke="#ef4444" stroke-width="3"/>
                            <polygon points="26,40 34,40 30,34" fill="#ef4444"/>
                            <text x="35" y="70" font-size="7" fill="#ef4444" font-family="monospace">Warm Air Rises (Low P)</text>

                            <!-- High-altitude Poleward Flow -->
                            <line x1="35" y1="35" x2="160" y2="35" stroke="#94a3b8" stroke-width="2"/>
                            <polygon points="160,32 160,38 166,35" fill="#94a3b8"/>

                            <!-- Subtropical Sinking -->
                            <line x1="165" y1="40" x2="165" y2="105" stroke="#38bdf8" stroke-width="3"/>
                            <polygon points="161,105 169,105 165,111" fill="#38bdf8"/>
                            <text x="160" y="70" font-size="7" fill="#38bdf8" font-family="monospace" text-anchor="end">Cold Air Sinks (High P)</text>

                            <!-- Surface Return Flow (Trade Winds) -->
                            <line x1="160" y1="105" x2="35" y2="105" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,2"/>
                            <polygon points="35,102 35,108 29,105" fill="#10b981"/>
                            <text x="95" y="100" font-size="7" font-weight="bold" fill="#10b981" font-family="monospace" text-anchor="middle">Trade Winds ➔</text>
                        </svg>
                    </div>

                    <!-- Coriolis Toggle & Description -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-xs space-y-1">
                        <div class="flex justify-between items-center">
                            <span class="text-slate-300">Coriolis Deflection:</span>
                            <span class="text-emerald-400 font-bold">Rightward in North</span>
                        </div>
                        <p class="text-[11px] text-slate-400 leading-relaxed">
                            Earth's eastward spin transforms north-south convection into the prevailing Northeast Trade Winds and mid-latitude Westerlies.
                        </p>
                    </div>
                </div>
            `;
        }}

        // Sim 7: Coastal Sea Breeze vs Land Breeze Diurnal Engine
        function renderSim7(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Day/Night Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim7SetTime('day')" class="py-1 rounded-lg ${{sim7State.timeOfDay === 'day' ? 'bg-amber-600 text-white font-bold' : 'text-slate-400'}}">☀️ Daytime: Sea Breeze</button>
                        <button onclick="window.sim7SetTime('night')" class="py-1 rounded-lg ${{sim7State.timeOfDay === 'night' ? 'bg-blue-600 text-white font-bold' : 'text-slate-400'}}">🌙 Nighttime: Land Breeze</button>
                    </div>

                    <!-- Coastal Cross Section SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 120" class="w-full h-32">
                            <!-- Ocean on Left -->
                            <rect x="10" y="80" width="90" height="35" fill="#0284c7" opacity="0.6"/>
                            <text x="50" y="100" font-size="8" font-weight="bold" fill="#fff" font-family="monospace" text-anchor="middle">Ocean (Water)</text>

                            <!-- Land on Right -->
                            <rect x="100" y="75" width="90" height="40" fill="#78350f" opacity="0.7"/>
                            <text x="145" y="100" font-size="8" font-weight="bold" fill="#fff" font-family="monospace" text-anchor="middle">Land (Sand/Soil)</text>

                            ${{sim7State.timeOfDay === 'day' ? `
                                <!-- Sun -->
                                <circle cx="160" cy="25" r="10" fill="#facc15"/>
                                <!-- Land heats fast ➔ Air Rises -->
                                <line x1="145" y1="70" x2="145" y2="35" stroke="#ef4444" stroke-width="2.5"/>
                                <polygon points="142,35 148,35 145,29" fill="#ef4444"/>
                                <text x="145" y="55" font-size="6" fill="#ef4444" font-family="monospace">Low P (Warm)</text>

                                <!-- Cool Air from Sea blows inland: Sea Breeze -->
                                <line x1="55" y1="65" x2="135" y2="65" stroke="#38bdf8" stroke-width="3"/>
                                <polygon points="135,61 135,69 142,65" fill="#38bdf8"/>
                                <text x="95" y="60" font-size="8" font-weight="bold" fill="#38bdf8" font-family="monospace" text-anchor="middle">SEA BREEZE ➔</text>
                            ` : `
                                <!-- Moon -->
                                <circle cx="40" cy="25" r="8" fill="#e2e8f0"/>
                                <!-- Ocean stays warmer ➔ Air rises over ocean -->
                                <line x1="50" y1="75" x2="50" y2="40" stroke="#ef4444" stroke-width="2.5"/>
                                <polygon points="47,40 53,40 50,34" fill="#ef4444"/>
                                <text x="50" y="60" font-size="6" fill="#ef4444" font-family="monospace">Low P (Warm)</text>

                                <!-- Cool Air blows from Land to Sea: Land Breeze -->
                                <line x1="140" y1="65" x2="60" y2="65" stroke="#38bdf8" stroke-width="3"/>
                                <polygon points="60,61 60,69 53,65" fill="#38bdf8"/>
                                <text x="95" y="60" font-size="8" font-weight="bold" fill="#38bdf8" font-family="monospace" text-anchor="middle">◀ LAND BREEZE</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Thermal Fact -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-[11px] font-mono text-slate-300">
                        ${{sim7State.timeOfDay === 'day' ? `
                            <strong class="text-amber-400">Daytime Dynamics:</strong> Land heats 5× faster than ocean due to lower specific heat capacity (~800 vs 4184 J/kg·°C). Rising air pulls cool sea breeze onto shores.
                        ` : `
                            <strong class="text-blue-400">Nighttime Dynamics:</strong> Land cools rapidly via radiative heat loss, while water retains thermal inertia. Rising marine air draws the cool land breeze out to sea.
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim7SetTime = t => {{ sim7State.timeOfDay = t; renderSim7(document.getElementById('interactiveViewport')); }};

        // Sim 8: Mountain & Valley Breeze Simulator
        function renderSim8(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Day/Night Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim8SetTime('day')" class="py-1 rounded-lg ${{sim8State.timeOfDay === 'day' ? 'bg-amber-600 text-white font-bold' : 'text-slate-400'}}">Day: Valley Breeze (Anabatic)</button>
                        <button onclick="window.sim8SetTime('night')" class="py-1 rounded-lg ${{sim8State.timeOfDay === 'night' ? 'bg-indigo-600 text-white font-bold' : 'text-slate-400'}}">Night: Mountain Breeze (Katabatic)</button>
                    </div>

                    <!-- Mountain Topography SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 120" class="w-full h-32">
                            <!-- Mountain V-Shape Profiles -->
                            <polygon points="10,120 70,30 130,120" fill="#334155" stroke="#475569" stroke-width="2"/>
                            <polygon points="90,120 150,30 200,120" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                            <text x="100" y="115" font-size="8" fill="#94a3b8" font-family="monospace" text-anchor="middle">Valley Basin</text>

                            ${{sim8State.timeOfDay === 'day' ? `
                                <!-- Anabatic flow up the slope -->
                                <line x1="90" y1="100" x2="70" y2="50" stroke="#f59e0b" stroke-width="2.5"/>
                                <polygon points="68,52 74,48 73,56" fill="#f59e0b"/>
                                <text x="50" y="70" font-size="7" font-weight="bold" fill="#facc15" font-family="monospace">Upslope Anabatic Wind</text>
                            ` : `
                                <!-- Katabatic drainage down into the valley -->
                                <line x1="70" y1="50" x2="95" y2="100" stroke="#38bdf8" stroke-width="2.5"/>
                                <polygon points="93,98 97,94 98,102" fill="#38bdf8"/>
                                <text x="110" y="70" font-size="7" font-weight="bold" fill="#38bdf8" font-family="monospace">Katabatic Drainage</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Observation Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-[11px] font-mono text-slate-300">
                        ${{sim8State.timeOfDay === 'day' ? `
                            <strong class="text-amber-400">Valley Breeze:</strong> Sunny slopes heat up rapidly, creating buoyant updrafts that pull cool air up the valley axis.
                        ` : `
                            <strong class="text-indigo-400">Mountain Breeze:</strong> Chilled ridge air becomes dense and drains under gravity into valley basins, causing temperature inversions and morning fog.
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim8SetTime = t => {{ sim8State.timeOfDay = t; renderSim8(document.getElementById('interactiveViewport')); }};

        // Sim 9: Hydrological Cycle & Latent Heat Engine
        function renderSim9(vp) {{
            const stages = [
                {{ key: "evap", name: "Evaporation", heat: "Absorbs 2.26 MJ/kg", desc: "Solar heat vaporizes ocean water, carrying latent heat aloft." }},
                {{ key: "transp", name: "Transpiration", heat: "Biological flux", desc: "Plants draw soil moisture and transpire water vapour through stomata." }},
                {{ key: "cond", name: "Condensation", heat: "Releases 2.26 MJ/kg", desc: "Adiabatic cooling forms cloud droplets, liberating latent heat to air." }},
                {{ key: "precip", name: "Precipitation", heat: "Gravity return", desc: "Coalesced raindrops and snow fall back to land and oceans." }}
            ];

            const cur = stages.find(s => s.key === sim9State.activeStage) || stages[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Hydrological Cycle & Latent Heat Transport
                    </div>

                    <!-- Stage Buttons -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{stages.map(s => `
                            <button onclick="window.sim9SetStage('${{s.key}}')" class="py-1 rounded ${{sim9State.activeStage === s.key ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{s.name.slice(0,5)}}</button>
                        `).join('')}}
                    </div>

                    <!-- Selected Stage Card -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="text-white font-bold">${{cur.name}}</span>
                            <span class="text-emerald-400 font-bold text-[11px]">${{cur.heat}}</span>
                        </div>
                        <p class="text-slate-300 text-[11px] leading-relaxed">${{cur.desc}}</p>
                    </div>

                    <!-- Water Balance Data -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-[11px] text-slate-300 space-y-1">
                        <div class="flex justify-between">
                            <span>Global Annual Evaporation:</span>
                            <span class="text-cyan-400 font-bold">~505,000 km³/year</span>
                        </div>
                        <div class="flex justify-between">
                            <span>Ocean Storage Fraction:</span>
                            <span class="text-cyan-400 font-bold">96.5% of total water</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim9SetStage = k => {{ sim9State.activeStage = k; renderSim9(document.getElementById('interactiveViewport')); }};

        // Sim 10: Carbon Cycle Dynamic Balance & Reservoir Flux
        function renderSim10(vp) {{
            const emission = sim10State.emissions;
            // Base atmospheric CO2 is 420 ppm at 10 GtC/yr. Scale proportionally
            const projectedPpm = 420 + (emission - 10) * 3.5;
            const projectedPh = Math.max(7.7, (8.1 - (emission * 0.02))).toFixed(2);

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Global Carbon Flux & Ocean Acidification Simulator
                    </div>

                    <!-- Emissions Slider -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-1">
                        <div class="flex justify-between text-xs font-mono text-slate-300">
                            <span>Anthropogenic Fossil Emissions:</span>
                            <span class="text-amber-400 font-bold">${{emission}} GtC/year</span>
                        </div>
                        <input type="range" min="0" max="25" step="1" value="${{emission}}" oninput="window.sim10SetEmissions(this.value)" class="w-full accent-amber-500">
                    </div>

                    <!-- Output Indicators -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Atmospheric CO₂ Level:</span>
                            <span class="text-rose-400 font-bold text-base">${{projectedPpm.toFixed(0)}} ppm</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Ocean Surface pH:</span>
                            <span class="text-cyan-400 font-bold text-base">${{projectedPh}}</span>
                        </div>
                    </div>

                    <!-- Carbon Pools Table -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 font-mono text-[10px] text-slate-300 space-y-1">
                        <div class="text-slate-400 uppercase tracking-widest border-b border-slate-800 pb-0.5">Natural Reservoir Capacities:</div>
                        <div class="flex justify-between"><span>Lithosphere (Limestone):</span><span>60,000,000 GtC</span></div>
                        <div class="flex justify-between"><span>Oceans (Dissolved):</span><span>38,000 GtC</span></div>
                        <div class="flex justify-between"><span>Terrestrial Biosphere:</span><span>2,500 GtC</span></div>
                    </div>
                </div>
            `;
        }}

        window.sim10SetEmissions = val => {{ sim10State.emissions = parseFloat(val); renderSim10(document.getElementById('interactiveViewport')); }};

        // Sim 11: 5-Stage Nitrogen Cycle Microbial Factory
        function renderSim11(vp) {{
            const steps = [
                {{ step: 1, name: "1. Nitrogen Fixation", agent: "Rhizobium / Lightning", rx: "N₂ + 8H⁺ ➔ 2NH₃ + H₂", desc: "Converts inert N₂ into bioavailable ammonia." }},
                {{ step: 2, name: "2. Nitrification", agent: "Nitrosomonas & Nitrobacter", rx: "NH₃ ➔ NO₂⁻ ➔ NO₃⁻", desc: "Aerobic oxidation of ammonia to nitrites and nitrates." }},
                {{ step: 3, name: "3. Assimilation", agent: "Plant Root Systems", rx: "NO₃⁻ ➔ Amino acids / Proteins", desc: "Plants incorporate nitrates into organic tissues." }},
                {{ step: 4, name: "4. Ammonification", agent: "Decomposer Fungi/Bacteria", rx: "Dead Organic Matter ➔ NH₄⁺", desc: "Mineralizes wastes back into ammonium ions." }},
                {{ step: 5, name: "5. Denitrification", agent: "Pseudomonas (Anaerobic)", rx: "NO₃⁻ ➔ N₂ gas", desc: "Closes the cycle by releasing N₂ back to the atmosphere." }}
            ];

            const cur = steps.find(s => s.step === sim11State.activeStep) || steps[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        The 5-Stage Nitrogen Cycle Microbial Factory
                    </div>

                    <!-- Step Buttons -->
                    <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{steps.map(s => `
                            <button onclick="window.sim11SetStep(${{s.step}})" class="py-1 rounded ${{sim11State.activeStep === s.step ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">S${{s.step}}</button>
                        `).join('')}}
                    </div>

                    <!-- Stage Card -->
                    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                        <div class="text-emerald-400 font-bold text-sm">${{cur.name}}</div>
                        <div class="flex justify-between text-slate-400 text-[11px]">
                            <span>Key Biological Agent:</span>
                            <span class="text-cyan-300 font-bold">${{cur.agent}}</span>
                        </div>
                        <div class="bg-slate-900 p-1.5 rounded border border-slate-800 text-amber-300 text-[11px] text-center">
                            ${{cur.rx}}
                        </div>
                        <p class="text-slate-300 text-[11px] leading-relaxed pt-1">${{cur.desc}}</p>
                    </div>
                </div>
            `;
        }}

        window.sim11SetStep = s => {{ sim11State.activeStep = s; renderSim11(document.getElementById('interactiveViewport')); }};

        // Sim 12: Oxygen Cycle & Chapman Ozone Mechanism
        function renderSim12(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Mode Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim12SetView('chapman')" class="py-1 rounded-lg ${{sim12State.viewMode === 'chapman' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400'}}">Stratospheric Ozone (Chapman)</button>
                        <button onclick="window.sim12SetView('biotic')" class="py-1 rounded-lg ${{sim12State.viewMode === 'biotic' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Photosynthesis vs Respiration</button>
                    </div>

                    <!-- Panel View -->
                    ${{sim12State.viewMode === 'chapman' ? `
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                            <span class="text-[10px] text-emerald-400 uppercase tracking-widest block border-b border-slate-800 pb-1">Photochemical Chapman Cycle:</span>
                            <div class="text-slate-300">1. UV-C Photolysis: <strong class="text-cyan-300">O₂ + hν (&lt;240nm) ➔ O + O</strong></div>
                            <div class="text-slate-300">2. Ozone Synthesis: <strong class="text-cyan-300">O + O₂ + M ➔ O₃ + M</strong></div>
                            <div class="text-slate-300">3. UV-B Shielding: <strong class="text-amber-400">O₃ + hν (240-310nm) ➔ O₂ + O</strong></div>
                            <div class="text-[11px] text-slate-400 border-t border-slate-800 pt-1">
                                Dynamic equilibrium maintains the protective ozone umbrella, shielding Earth from biological radiation damage.
                            </div>
                        </div>
                    ` : `
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                            <span class="text-[10px] text-cyan-400 uppercase tracking-widest block border-b border-slate-800 pb-1">Biotic Oxygen Equilibrium:</span>
                            <div class="text-emerald-400 font-bold">Photosynthetic Source:</div>
                            <div class="bg-slate-900 p-1 rounded text-[11px]">2H₂O + Photons ➔ 4H⁺ + 4e⁻ + O₂↑</div>
                            <div class="text-rose-400 font-bold mt-1">Aerobic Sinks:</div>
                            <div class="bg-slate-900 p-1 rounded text-[11px]">C₆H₁₂O₆ + 6O₂ ➔ 6CO₂ + 6H₂O + Energy</div>
                        </div>
                    `}}
                </div>
            `;
        }}

        window.sim12SetView = v => {{ sim12State.viewMode = v; renderSim12(document.getElementById('interactiveViewport')); }};

        // Sim 13: Biogeochemical Nutrient Synergy Matrix
        function renderSim13(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Nutrient Synergy & Redfield Stoichiometry
                    </div>

                    <!-- Interactive Disruption Test -->
                    <div class="grid grid-cols-3 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        <button onclick="window.sim13SetStress('none')" class="py-1 rounded ${{sim13State.activeStress === 'none' ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Balanced</button>
                        <button onclick="window.sim13SetStress('drought')" class="py-1 rounded ${{sim13State.activeStress === 'drought' ? 'bg-amber-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">Drought</button>
                        <button onclick="window.sim13SetStress('runoff')" class="py-1 rounded ${{sim13State.activeStress === 'runoff' ? 'bg-rose-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">N Runoff</button>
                    </div>

                    <!-- Consequence Card -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                        ${{sim13State.activeStress === 'none' ? `
                            <div class="text-emerald-400 font-bold">Homeostatic Equilibrium Active</div>
                            <p class="text-[11px] text-slate-300 leading-relaxed">
                                Oceanic Redfield Ratio: 106 C : 16 N : 1 P. Primary production and decay rates are balanced across the globe.
                            </p>
                        ` : sim13State.activeStress === 'drought' ? `
                            <div class="text-amber-400 font-bold">Water-Carbon Decoupling</div>
                            <p class="text-[11px] text-slate-300 leading-relaxed">
                                Stomata close to conserve moisture. Carbon fixation drops by 80%, reducing oxygen output and slowing global biospheric carbon sequestration.
                            </p>
                        ` : `
                            <div class="text-rose-400 font-bold">Eutrophication Cascades</div>
                            <p class="text-[11px] text-slate-300 leading-relaxed">
                                Excess nitrogen triggers algal blooms. Bacterial decay consumes dissolved oxygen (hypoxia), killing fish and marine benthic communities.
                            </p>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim13SetStress = s => {{ sim13State.activeStress = s; renderSim13(document.getElementById('interactiveViewport')); }};

        // Sim 14: Atmospheric Greenhouse Effect & Global Temperature
        function renderSim14(vp) {{
            const co2 = sim14State.co2Ppm;
            // Radiative forcing delta F = 5.35 * ln(C / 280)
            const forcing = (5.35 * Math.log(co2 / 280)).toFixed(2);
            const tempAnomaly = (forcing * 0.8).toFixed(2);

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Greenhouse Forcing & Temperature Trajectory (C-8.2)
                    </div>

                    <!-- CO2 Slider -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-1">
                        <div class="flex justify-between text-xs font-mono text-slate-300">
                            <span>Atmospheric CO₂ Concentration:</span>
                            <span class="text-rose-400 font-bold">${{co2}} ppm</span>
                        </div>
                        <input type="range" min="280" max="600" step="10" value="${{co2}}" oninput="window.sim14SetCo2(this.value)" class="w-full accent-rose-500">
                        <div class="flex justify-between text-[9px] font-mono text-slate-500">
                            <span>280 (Pre-Ind)</span>
                            <span>420 (Today)</span>
                            <span>560 (2× Baseline)</span>
                        </div>
                    </div>

                    <!-- Output Dashboard -->
                    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Radiative Forcing (ΔF):</span>
                            <span class="text-amber-400 font-bold text-sm">+${{forcing}} W/m²</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                            <span class="text-[10px] text-slate-400 block">Mean Temp Anomaly (ΔT):</span>
                            <span class="text-rose-400 font-bold text-sm">+${{tempAnomaly}}°C</span>
                        </div>
                    </div>

                    <div class="text-[11px] font-mono text-slate-400 bg-slate-950 p-2 rounded-lg border border-slate-800">
                        Natural greenhouse effect warms Earth from -18°C to +15°C. Anthropogenic forcing adds extra thermal energy, altering global wind and precipitation regimes.
                    </div>
                </div>
            `;
        }}

        window.sim14SetCo2 = val => {{ sim14State.co2Ppm = parseInt(val); renderSim14(document.getElementById('interactiveViewport')); }};

        // Sim 15: Indian Traditional Eco-Architecture & Water Systems (C-6.1)
        function renderSim15(vp) {{
            const regions = [
                {{ key: "rajasthan", name: "Bawadis & Johads (Rajasthan)", desc: "Subterranean stepwells and earthen check dams that capture monsoon deluges and recharge desert aquifers." }},
                {{ key: "bihar", name: "Ahar-Pyne (South Bihar)", desc: "Canals (pynes) divert floodwaters into retaining basins (ahars) for agricultural paddy irrigation." }},
                {{ key: "himachal", name: "Kuhls (Himachal Pradesh)", desc: "Glacial meltwater diversion channels contoured along mountain cliffs to irrigate terraced valley crops." }},
                {{ key: "ladakh", name: "Zings (Ladakh)", desc: "High-altitude glacial meltwater storage tanks designed around daily freeze-thaw cycles." }}
            ];

            const cur = regions.find(r => r.key === sim15State.activeRegion) || regions[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-emerald-400 font-bold text-center">
                        Indian Traditional Ecological Systems (C-6.1)
                    </div>

                    <!-- Region Selector -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{regions.map(r => `
                            <button onclick="window.sim15SetRegion('${{r.key}}')" class="py-1 rounded ${{sim15State.activeRegion === r.key ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{r.name.split(' ')[0]}}</button>
                        `).join('')}}
                    </div>

                    <!-- Detail Card -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        <div class="text-emerald-400 font-bold text-sm">${{cur.name}}</div>
                        <p class="text-slate-300 text-[11px] leading-relaxed">${{cur.desc}}</p>
                        <div class="border-t border-slate-800 pt-1.5 text-cyan-300 text-[11px]">
                            Philosophy: <em>Vasudhaiva Kutumbakam</em> & reverence for the 5 cosmic elements (Pancha Mahabhuta).
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim15SetRegion = r => {{ sim15State.activeRegion = r; renderSim15(document.getElementById('interactiveViewport')); }};

        // Sim 16: "Zero Differential Heating" Planetary Collapse Sandbox (C-7.2)
        function renderSim16(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Mode Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim16SetMode('real')" class="py-1 rounded-lg ${{sim16State.mode === 'real' ? 'bg-emerald-600 text-white font-bold' : 'text-slate-400'}}">Real Earth (Differential Heating)</button>
                        <button onclick="window.sim16SetMode('isothermal')" class="py-1 rounded-lg ${{sim16State.mode === 'isothermal' ? 'bg-rose-600 text-white font-bold' : 'text-slate-400'}}">Hypothetical Isothermal Earth</button>
                    </div>

                    <!-- Comparison Simulation Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        ${{sim16State.mode === 'real' ? `
                            <div class="text-emerald-400 font-bold text-sm">Active Planetary Circulation Active</div>
                            <div class="flex justify-between text-slate-300"><span>Pressure Gradients (ΔP):</span><span class="text-cyan-300">Strong & Active</span></div>
                            <div class="flex justify-between text-slate-300"><span>Planetary Winds:</span><span class="text-cyan-300">Trade Winds, Westerlies Active</span></div>
                            <div class="flex justify-between text-slate-300"><span>Continental Moisture:</span><span class="text-cyan-300">Continually Transported</span></div>
                            <p class="text-[11px] text-slate-400 border-t border-slate-800 pt-1 leading-relaxed">
                                Differential heating acts as the fundamental thermodynamic heartbeat sustaining life across all continents.
                            </p>
                        ` : `
                            <div class="text-rose-400 font-bold text-sm">Total Planetary Stagnation (C-7.2)</div>
                            <div class="flex justify-between text-slate-300"><span>Pressure Gradients (ΔP):</span><span class="text-rose-400 font-bold">0 Pa (Zero Gradient)</span></div>
                            <div class="flex justify-between text-slate-300"><span>Planetary Winds:</span><span class="text-rose-400 font-bold">0 km/h (Dead Calm)</span></div>
                            <div class="flex justify-between text-slate-300"><span>Continental Rainfall:</span><span class="text-rose-400 font-bold">Collapsed (Dry Deserts)</span></div>
                            <p class="text-[11px] text-slate-400 border-t border-slate-800 pt-1 leading-relaxed">
                                Without differential heating, all wind and weather stop. Ocean circulation ceases, causing deep marine anoxia and mass biospheric extinction.
                            </p>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim16SetMode = m => {{ sim16State.mode = m; renderSim16(document.getElementById('interactiveViewport')); }};

        // ==========================================
        // DEDICATED QUIZ SLIDES (17-20) RENDERING
        // ==========================================
        function renderQuizSlide(vp, slide) {{
            const quizList = slide.quiz || [];
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3 max-h-[500px] overflow-y-auto pr-1 scrollbar-thin">
                    <div class="text-xs font-mono text-emerald-400 font-bold border-b border-slate-800 pb-1 flex justify-between">
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
                                <button onclick="openSolutionModal('${{q.q.replace(/'/g, "\\\\'") }}', '${{q.sol.replace(/'/g, "\\\\'") }}')" class="px-2.5 py-1 rounded bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 text-[10px] font-mono font-bold transition flex items-center gap-1">
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

