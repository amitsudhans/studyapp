# -*- coding: utf-8 -*-
"""
Builder script for NCERT Class 9 Science Chapter 7: Atoms and Molecules
Outputs: public/animations/class9-atoms-and-molecules.html
"""

import os
import json
import re
from class9_atoms_and_molecules_data import SLIDES_DATA

OUTPUT_PATH = "public/animations/class9-atoms-and-molecules.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Science • Chapter 7 • Atoms and Molecules Master Lab</title>
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
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white font-extrabold shadow-lg shadow-cyan-500/20 text-lg tracking-wider">
                9S
            </div>
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-cyan-400 tracking-wider uppercase font-mono">NCERT Class 9 Science • Ch 7</span>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">14 Periods</span>
                </div>
                <h1 class="text-sm md:text-base font-bold text-slate-100 tracking-tight">Atoms and Molecules Master Lab</h1>
            </div>
        </div>

        <!-- Controls: Sound Toggle, Slide Counter, Navigation -->
        <div class="flex items-center gap-2 md:gap-4">
            <button id="soundToggleBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 flex items-center gap-2 transition shadow-sm">
                <span id="soundIcon">🔊</span>
                <span id="soundText" class="hidden sm:inline">Voice: ON</span>
            </button>
            <div class="text-xs font-mono font-medium text-slate-400 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
                Slide <span id="currentSlideNum" class="text-cyan-400 font-bold">1</span> / 20
            </div>
            <div class="flex items-center gap-1">
                <button id="prevBtn" onclick="changeSlide(-1)" class="w-9 h-9 rounded-lg border border-slate-700 bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-slate-200 transition font-bold">
                    ◀
                </button>
                <button id="nextBtn" onclick="changeSlide(1)" class="w-9 h-9 rounded-lg border border-cyan-500/50 bg-cyan-600 hover:bg-cyan-500 disabled:opacity-30 disabled:cursor-not-allowed flex items-center justify-center text-white transition font-bold shadow-md shadow-cyan-600/30">
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
            <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-cyan-950/40 border border-slate-800 rounded-2xl p-4 shadow-xl flex items-center gap-4 relative overflow-hidden">
                <div class="absolute -right-8 -top-8 w-32 h-32 bg-cyan-500/10 rounded-full blur-2xl pointer-events-none"></div>

                <!-- Mentor Avatar SVG -->
                <div class="relative w-16 h-16 shrink-0 rounded-2xl bg-slate-800 border-2 border-cyan-400/40 p-1 flex items-center justify-center shadow-lg">
                    <svg viewBox="0 0 100 100" class="w-full h-full">
                        <!-- Lab Coat & Collar -->
                        <path d="M 20 90 L 32 68 L 68 68 L 80 90 Z" fill="#38bdf8"/>
                        <path d="M 38 68 L 50 82 L 62 68 Z" fill="#0284c7"/>
                        <!-- Neck -->
                        <rect x="44" y="56" width="12" height="15" rx="3" fill="#fed7aa"/>
                        <!-- Head -->
                        <circle cx="50" cy="40" r="22" fill="#fed7aa"/>
                        <!-- Hair -->
                        <path d="M 26 40 C 26 20, 74 20, 74 40 C 74 24, 66 18, 50 18 C 34 18, 26 24, 26 40 Z" fill="#0f172a"/>
                        <path d="M 26 36 C 24 50, 24 64, 30 68 C 30 52, 34 44, 34 44 Z" fill="#0f172a"/>
                        <path d="M 74 36 C 76 50, 76 64, 70 68 C 70 52, 66 44, 66 44 Z" fill="#0f172a"/>
                        <!-- Glasses -->
                        <rect x="33" y="34" width="14" height="10" rx="3" fill="none" stroke="#0284c7" stroke-width="2.2"/>
                        <rect x="53" y="34" width="14" height="10" rx="3" fill="none" stroke="#0284c7" stroke-width="2.2"/>
                        <line x1="47" y1="39" x2="53" y2="39" stroke="#0284c7" stroke-width="2"/>
                        <!-- Eyes -->
                        <circle cx="40" cy="39" r="2" fill="#0f172a"/>
                        <circle cx="60" cy="39" r="2" fill="#0f172a"/>
                        <!-- Smile / Talking Mouth -->
                        <rect id="teacherMouth" x="44" y="50" width="12" height="4" rx="2" fill="#dc2626"/>
                    </svg>
                    <span class="absolute -bottom-1 -right-1 flex h-3.5 w-3.5">
                        <span id="speakerPulse" class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75 hidden"></span>
                        <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-cyan-500 border-2 border-slate-900"></span>
                    </span>
                </div>

                <div class="flex-1">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-bold text-cyan-300 font-mono">Prof. Sophia</span>
                            <span class="text-[10px] bg-slate-800 text-slate-400 px-2 py-0.5 rounded border border-slate-700">Atomic Science Faculty</span>
                        </div>
                        <button onclick="replayVoice()" class="text-xs text-slate-400 hover:text-cyan-400 flex items-center gap-1 transition">
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
                    <span id="slideBadge" class="text-[11px] font-mono font-semibold px-2.5 py-1 rounded-md bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
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
                    <div class="text-[11px] font-bold text-cyan-300 font-mono uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
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
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
                        <span id="panelHeaderTitle" class="text-xs font-bold text-cyan-300 font-mono uppercase tracking-wider">
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
                    <span id="simHelpText">Interact with the controls above to explore the atomic principles.</span>
                    <button onclick="resetCurrentSimulation()" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] font-mono text-slate-300 border border-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

        </div>

    </main>

    <!-- Last Slide Notice Container (Strict Requirement) -->
    <div id="lastSlideNotice" class="hidden max-w-7xl mx-auto px-4 py-4 w-full">
        <div class="bg-gradient-to-r from-emerald-950/80 via-slate-900 to-cyan-950/80 border-2 border-emerald-500/50 rounded-2xl p-6 text-center shadow-2xl flex flex-col items-center justify-center gap-3">
            <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-3xl">
                🏆
            </div>
            <h3 class="text-lg md:text-xl font-bold text-emerald-300 tracking-wide">
                You have reached the last slide of this chapter
            </h3>
            <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
                You have thoroughly mastered <strong>Atoms and Molecules</strong>—including the Law of Conservation of Mass, the Law of Constant Proportions, Dalton's Atomic Theory, IUPAC chemical symbols, valency, the criss-cross formula method, molecular and formula unit mass, ancient Indian Rasashastra cinnabar metallurgy, and modern mass-energy conservation boundaries!
            </p>
            <div class="flex items-center gap-3 mt-2">
                <button onclick="jumpToSlide(1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 border border-slate-700 transition">
                    ↺ Restart Lab
                </button>
                <button onclick="jumpToSlide(17)" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white transition shadow-lg shadow-cyan-600/30">
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
                <h4 class="text-base font-bold text-cyan-300 font-mono">Step-by-Step Solution</h4>
            </div>
            <div id="solutionQuestionText" class="text-xs text-slate-400 border-l-2 border-cyan-500 pl-3 italic">
                <!-- Question -->
            </div>
            <div id="solutionBodyText" class="text-xs md:text-sm text-slate-200 leading-relaxed bg-slate-950 p-4 rounded-xl border border-slate-800">
                <!-- Detailed explanation -->
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow-md transition">
                    Got It!
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
        let sim1State = {{ mixed: false, scale: 142.50 }};
        let sim2State = {{ hMass: 2.0, oMass: 16.0 }};
        let sim3State = {{ activePostulate: 1, activeSymbol: 'H' }};
        let sim4State = {{ scaleVal: 0.1, activeElement: 'Na' }};
        let sim5State = {{ targetElem: 'C', currentSlices: 0, balanced: false }};
        let sim6State = {{ type: 'di' }};
        let sim7State = {{ molecule: 'h2', bonded: false }};
        let sim8State = {{ mode: 'cation', activeRadical: 'NH4' }};
        let sim9State = {{ state: 'solid' }};
        let sim10State = {{ cation: 'Al3', anion: 'SO4' }};
        let sim11State = {{ targetIdx: 0, score: 0, streak: 0, selectedCation: null, selectedAnion: null }};
        let sim12State = {{ selectedFormula: 'H2O' }};
        let sim13State = {{ mode: 'molecular' }};
        let sim14State = {{ molecule: 'h2o', angle: 0 }};
        let sim15State = {{ view: 'ancient', heated: false }};
        let sim16State = {{ reactionType: 'chemical' }};

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
                        el.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-mono font-bold border border-cyan-500 bg-cyan-500/20 text-cyan-300 shadow-sm shrink-0';
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
                        <span class="text-xs font-bold font-mono text-cyan-400 uppercase tracking-wider">🎯 In-Slide Checkpoints</span>
                        <span class="text-[10px] text-slate-400">(Immediate Feedback)</span>
                    </div>
                    ${{slide.checkpoints.map(cp => `
                        <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 shadow-sm flex flex-col gap-2.5">
                            <div class="text-xs font-semibold text-slate-200 flex items-start gap-2">
                                <span class="px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[10px] shrink-0 font-bold">CP ${{cp.num}}</span>
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
                                <strong class="text-cyan-400">Prof. Sophia:</strong> ${{cp.exp}}
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
            const cleanText = text.replace(/\$/g, '');
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
                simHelp.textContent = "Use the interactive controls to test and verify atomic principles.";

                // Call simulator specific renderer
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
                case 1: sim1State = {{ mixed: false, scale: 142.50 }}; break;
                case 2: sim2State = {{ hMass: 2.0, oMass: 16.0 }}; break;
                case 3: sim3State = {{ activePostulate: 1, activeSymbol: 'H' }}; break;
                case 4: sim4State = {{ scaleVal: 0.1, activeElement: 'Na' }}; break;
                case 5: sim5State = {{ targetElem: 'C', currentSlices: 0, balanced: false }}; break;
                case 6: sim6State = {{ type: 'di' }}; break;
                case 7: sim7State = {{ molecule: 'h2', bonded: false }}; break;
                case 8: sim8State = {{ mode: 'cation', activeRadical: 'NH4' }}; break;
                case 9: sim9State = {{ state: 'solid' }}; break;
                case 10: sim10State = {{ cation: 'Al3', anion: 'SO4' }}; break;
                case 11: sim11State = {{ targetIdx: 0, score: 0, streak: 0, selectedCation: null, selectedAnion: null }}; break;
                case 12: sim12State = {{ selectedFormula: 'H2O' }}; break;
                case 13: sim13State = {{ mode: 'molecular' }}; break;
                case 14: sim14State = {{ molecule: 'h2o', angle: 0 }}; break;
                case 15: sim15State = {{ view: 'ancient', heated: false }}; break;
                case 16: sim16State = {{ reactionType: 'chemical' }}; break;
            }}
            renderRightViewport(SLIDES[currentSlideIndex]);
        }}

        // ==========================================
        // 16 BESPOKE SIMULATOR IMPLEMENTATIONS
        // ==========================================

        // Sim 1: Conservation of Mass Flask & Balance
        function renderSim1(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col items-center gap-3">
                    <!-- Digital Balance Scale Display -->
                    <div class="bg-slate-900 border-2 border-cyan-500/40 rounded-xl px-4 py-2 flex items-center justify-between w-full max-w-xs shadow-lg">
                        <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest">Analytical Scale</span>
                        <div class="text-2xl font-mono font-extrabold text-cyan-400">
                            ${{sim1State.scale.toFixed(2)}} <span class="text-xs text-slate-400 font-sans">g</span>
                        </div>
                    </div>

                    <!-- SVG Sealed Conical Flask -->
                    <svg viewBox="0 0 240 220" class="w-56 h-52">
                        <!-- Rubber Cork -->
                        <polygon points="105,25 135,25 140,40 100,40" fill="#78350f" stroke="#451a03" stroke-width="1.5"/>
                        <text x="120" y="34" font-size="7" fill="#fef3c7" font-family="monospace" text-anchor="middle">SEALED CORK</text>

                        <!-- Conical Flask Body -->
                        <path d="M 100 40 L 140 40 L 140 70 L 205 185 C 210 195, 205 205, 190 205 L 50 205 C 35 205, 30 195, 35 185 L 100 70 Z"
                              fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" opacity="0.9"/>

                        ${{!sim1State.mixed ? `
                            <!-- Clear Na2SO4 solution at bottom -->
                            <path d="M 45 190 L 195 190 C 200 197, 195 203, 190 203 L 50 203 C 45 203, 40 197, 45 190 Z" fill="#38bdf8" opacity="0.4"/>
                            <text x="120" y="198" font-size="8" fill="#bae6fd" font-family="monospace" text-anchor="middle">Na₂SO₄ (aq)</text>

                            <!-- Suspended Ignition Tube with BaCl2 -->
                            <line x1="120" y1="40" x2="120" y2="90" stroke="#f1f5f9" stroke-width="1" stroke-dasharray="2,2"/>
                            <rect x="112" y="90" width="16" height="55" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5" transform="rotate(15 120 115)"/>
                            <rect x="114" y="115" width="12" height="28" rx="6" fill="#0284c7" opacity="0.6" transform="rotate(15 120 115)"/>
                            <text x="150" y="115" font-size="8" fill="#e2e8f0" font-family="monospace">BaCl₂ (aq)</text>
                        ` : `
                            <!-- Mixed Cloudy White Precipitate BaSO4 -->
                            <path d="M 45 175 L 195 175 C 200 197, 195 203, 190 203 L 50 203 C 45 203, 40 197, 45 190 Z" fill="#e2e8f0" opacity="0.85"/>
                            <circle cx="80" cy="185" r="3" fill="#cbd5e1"/>
                            <circle cx="110" cy="192" r="3.5" fill="#f8fafc"/>
                            <circle cx="140" cy="182" r="2.5" fill="#94a3b8"/>
                            <circle cx="160" cy="190" r="3" fill="#cbd5e1"/>
                            <text x="120" y="193" font-size="9" font-weight="bold" fill="#090d16" font-family="monospace" text-anchor="middle">BaSO₄ ↓ (White Ppt)</text>

                            <!-- Dropped Empty Tube -->
                            <rect x="90" y="170" width="14" height="40" rx="7" fill="#334155" stroke="#94a3b8" stroke-width="1.2" transform="rotate(75 100 185)"/>
                        `}}
                    </svg>

                    <!-- Reaction Equation & Action Button -->
                    <div class="w-full text-center">
                        <div class="text-[11px] font-mono text-cyan-300 bg-slate-900 py-1 px-2 rounded-lg border border-slate-800">
                            BaCl₂(aq) + Na₂SO₄(aq) ➔ BaSO₄(s)↓ + 2NaCl(aq)
                        </div>
                        <button onclick="window.sim1Tilt()" class="mt-2.5 px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-md shadow-cyan-600/30 transition">
                            ${{!sim1State.mixed ? "Tilt Flask & Mix Solutions" : "Reset Apparatus"}}
                        </button>
                    </div>
                </div>
            `;
        }}

        window.sim1Tilt = () => {{
            sim1State.mixed = !sim1State.mixed;
            renderSim1(document.getElementById('interactiveViewport'));
        }};

        // Sim 2: Constant Proportions Synthesizer
        function renderSim2(vp) {{
            const h = sim2State.hMass;
            const o = sim2State.oMass;

            // 1 g H reacts with 8 g O
            const requiredO = h * 8;
            let waterFormed = 0;
            let excessH = 0;
            let excessO = 0;

            if (o >= requiredO) {{
                waterFormed = h + requiredO;
                excessO = o - requiredO;
            }} else {{
                const reactedH = o / 8;
                waterFormed = reactedH + o;
                excessH = h - reactedH;
            }}

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <div class="text-xs font-mono text-cyan-300 font-bold text-center">
                        Stoichiometric Definite Ratio: 1 g H : 8 g O ➔ 9 g H₂O
                    </div>

                    <!-- Sliders -->
                    <div class="space-y-2 bg-slate-900 p-3 rounded-xl border border-slate-800">
                        <div>
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-cyan-300">Hydrogen Mass (H):</span>
                                <span class="text-white font-bold">${{h.toFixed(1)}} g</span>
                            </div>
                            <input type="range" min="1" max="10" step="0.5" value="${{h}}" oninput="window.sim2SetH(this.value)" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <div class="flex justify-between text-xs font-mono">
                                <span class="text-rose-400">Oxygen Mass (O):</span>
                                <span class="text-white font-bold">${{o.toFixed(1)}} g</span>
                            </div>
                            <input type="range" min="8" max="80" step="2" value="${{o}}" oninput="window.sim2SetO(this.value)" class="w-full accent-rose-500">
                        </div>
                    </div>

                    <!-- Reaction Output Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col gap-1.5 font-mono text-xs">
                        <div class="flex justify-between text-emerald-400 font-bold">
                            <span>Water Formed (H₂O):</span>
                            <span>${{waterFormed.toFixed(2)}} g</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Excess Unreacted Reagent:</span>
                            <span class="text-amber-400 font-bold">
                                ${{excessH > 0.05 ? excessH.toFixed(2) + ' g H' : excessO > 0.05 ? excessO.toFixed(2) + ' g O' : 'None (Perfect 1:8)'}}
                            </span>
                        </div>
                        <div class="text-[10px] text-slate-400 border-t border-slate-800 pt-1 mt-1">
                            ${{excessH > 0.05 ? `Oxygen is limiting reactant! ${{excessH.toFixed(2)}} g of Hydrogen cannot find oxygen.` : excessO > 0.05 ? `Hydrogen is limiting reactant! ${{excessO.toFixed(2)}} g of Oxygen remains untouched.` : `Complete stoichiometric reaction! Zero reactants wasted.`}}
                        </div>
                    </div>

                    <!-- Beaker visualization -->
                    <div class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 flex items-center justify-center">
                        <svg viewBox="0 0 160 80" class="w-40 h-20">
                            <rect x="30" y="10" width="100" height="65" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                            <rect x="32" y="${{75 - Math.min(60, waterFormed * 0.7)}}" width="96" height="${{Math.min(60, waterFormed * 0.7)}}" fill="#0284c7" opacity="0.65"/>
                            <text x="80" y="50" font-size="9" fill="#f8fafc" font-weight="bold" font-family="monospace" text-anchor="middle">H₂O: ${{waterFormed.toFixed(1)}}g</text>
                        </svg>
                    </div>
                </div>
            `;
        }}

        window.sim2SetH = val => {{ sim2State.hMass = parseFloat(val); renderSim2(document.getElementById('interactiveViewport')); }};
        window.sim2SetO = val => {{ sim2State.oMass = parseFloat(val); renderSim2(document.getElementById('interactiveViewport')); }};

        // Sim 3: Dalton's Postulate Explorer & Historic Symbols
        function renderSim3(vp) {{
            const symbols = [
                {{ sym: "H", name: "Hydrogen", glyph: "⊙", desc: "Circle with central dot" }},
                {{ sym: "C", name: "Carbon", glyph: "●", desc: "Solid filled circle" }},
                {{ sym: "O", name: "Oxygen", glyph: "○", desc: "Empty open circle" }},
                {{ sym: "N", name: "Nitrogen", glyph: "⦶", desc: "Circle with vertical bisector" }},
                {{ sym: "S", name: "Sulphur", glyph: "⊕", desc: "Circle with cross (+)" }},
                {{ sym: "P", name: "Phosphorus", glyph: "🜊", desc: "Circle with 3 radial spokes" }}
            ];

            const activeSym = symbols.find(s => s.sym === sim3State.activeSymbol) || symbols[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Postulate Tabs -->
                    <div class="grid grid-cols-6 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{[1,2,3,4,5,6].map(num => `
                            <button onclick="window.sim3SetPostulate(${{num}})" class="py-1 rounded ${{sim3State.activePostulate === num ? 'bg-cyan-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">P${{num}}</button>
                        `).join('')}}
                    </div>

                    <!-- Postulate Details -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs">
                        <div class="text-cyan-400 font-bold font-mono text-[11px] mb-1">
                            ${{
                                sim3State.activePostulate === 1 ? "Postulate 1: Fundamental Particles" :
                                sim3State.activePostulate === 2 ? "Postulate 2: Indivisible Atoms (Conservation of Mass)" :
                                sim3State.activePostulate === 3 ? "Postulate 3: Elements Have Identical Atoms" :
                                sim3State.activePostulate === 4 ? "Postulate 4: Different Elements Have Different Atoms" :
                                sim3State.activePostulate === 5 ? "Postulate 5: Small Whole Number Ratios (Definite Proportions)" :
                                "Postulate 6: Constant Kinds & Numbers in Compounds"
                            }}
                        </div>
                        <p class="text-slate-300 text-[11px] leading-relaxed">
                            ${{
                                sim3State.activePostulate === 1 ? "All matter is composed of very tiny indivisible building blocks called atoms." :
                                sim3State.activePostulate === 2 ? "Atoms cannot be created, divided, or destroyed in any chemical reaction." :
                                sim3State.activePostulate === 3 ? "All atoms of a specific chemical element share identical mass and chemical behavior." :
                                sim3State.activePostulate === 4 ? "Atoms of different chemical elements possess distinct masses and chemical reactivities." :
                                sim3State.activePostulate === 5 ? "Compounds form when atoms combine in fixed, simple whole-number ratios (e.g. 2:1 for H₂O)." :
                                "In any given chemical compound, the relative numbers and types of atoms are constant."
                            }}
                        </p>
                    </div>

                    <!-- Historic Dalton Glyph Matrix -->
                    <div class="border-t border-slate-800 pt-2">
                        <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest block mb-1">Dalton's 1808 Elemental Glyphs:</span>
                        <div class="grid grid-cols-6 gap-1.5">
                            ${{symbols.map(s => `
                                <button onclick="window.sim3SetSymbol('${{s.sym}}')" class="p-1 rounded-lg border ${{sim3State.activeSymbol === s.sym ? 'border-cyan-500 bg-cyan-500/20' : 'border-slate-800 bg-slate-900'}} flex flex-col items-center">
                                    <span class="text-lg">${{s.glyph}}</span>
                                    <span class="text-[9px] font-mono text-slate-300">${{s.sym}}</span>
                                </button>
                            `).join('')}}
                        </div>
                        <div class="mt-2 text-center text-xs font-mono text-cyan-300 bg-slate-900 py-1.5 px-2 rounded-lg border border-slate-800">
                            ${{activeSym.name}} • Glyph: "${{activeSym.glyph}}" (${{activeSym.desc}}) ➔ IUPAC: <strong class="text-white">${{activeSym.sym}}</strong>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim3SetPostulate = p => {{ sim3State.activePostulate = p; renderSim3(document.getElementById('interactiveViewport')); }};
        window.sim3SetSymbol = sym => {{ sim3State.activeSymbol = sym; renderSim3(document.getElementById('interactiveViewport')); }};

        // Sim 4: Nanoscale Zoom Lens & Latin Origin Matrix
        function renderSim4(vp) {{
            const latinElements = [
                {{ sym: "Na", name: "Sodium", latin: "Natrium" }},
                {{ sym: "K", name: "Potassium", latin: "Kalium" }},
                {{ sym: "Fe", name: "Iron", latin: "Ferrum" }},
                {{ sym: "Cu", name: "Copper", latin: "Cuprum" }},
                {{ sym: "Ag", name: "Silver", latin: "Argentum" }},
                {{ sym: "Au", name: "Gold", latin: "Aurum" }},
                {{ sym: "Pb", name: "Lead", latin: "Plumbum" }},
                {{ sym: "Hg", name: "Mercury", latin: "Hydrargyrum" }}
            ];

            const activeEl = latinElements.find(e => e.sym === sim4State.activeElement) || latinElements[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Scale Zoom Graphic -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center text-center">
                        <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest">Atomic Scale Comparison</span>
                        <div class="text-lg font-mono font-bold text-cyan-400 mt-1">
                            Radius: 10⁻¹⁰ m = 0.1 nm = 1 Å
                        </div>
                        <div class="w-full bg-slate-900 h-2 rounded-full mt-2 relative overflow-hidden">
                            <div class="bg-gradient-to-r from-cyan-500 to-blue-600 h-full w-[20%]"></div>
                        </div>
                        <div class="flex justify-between w-full text-[9px] font-mono text-slate-500 mt-1">
                            <span>0.1 nm (Atom)</span>
                            <span>1 nm (H₂O)</span>
                            <span>10 nm (Protein)</span>
                            <span>10⁵ nm (Sand)</span>
                        </div>
                    </div>

                    <!-- Latin Origin Matrix -->
                    <div>
                        <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest block mb-1.5">Classical Latin Origin Matrix (C-1.3):</span>
                        <div class="grid grid-cols-4 gap-1.5">
                            ${{latinElements.map(e => `
                                <button onclick="window.sim4SetElement('${{e.sym}}')" class="p-2 rounded-xl border ${{sim4State.activeElement === e.sym ? 'border-cyan-500 bg-cyan-500/20 text-cyan-200' : 'border-slate-800 bg-slate-900 text-slate-300'}} flex flex-col items-center transition">
                                    <span class="text-base font-bold font-mono">${{e.sym}}</span>
                                    <span class="text-[9px] text-slate-400 truncate w-full text-center">${{e.name}}</span>
                                </button>
                            `).join('')}}
                        </div>
                    </div>

                    <!-- Highlight Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between font-mono text-xs">
                        <div>
                            <span class="text-slate-400">Element:</span> <strong class="text-white">${{activeEl.name}}</strong>
                        </div>
                        <div>
                            <span class="text-slate-400">Latin:</span> <span class="text-cyan-400 font-bold italic">${{activeEl.latin}}</span>
                        </div>
                        <div class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold">
                            ${{activeEl.sym}}
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim4SetElement = sym => {{ sim4State.activeElement = sym; renderSim4(document.getElementById('interactiveViewport')); }};

        // Sim 5: Atomic Mass Beam Balance with C-12 Slices
        function renderSim5(vp) {{
            const elements = [
                {{ sym: "H", name: "Hydrogen", mass: 1 }},
                {{ sym: "He", name: "Helium", mass: 4 }},
                {{ sym: "C", name: "Carbon", mass: 12 }},
                {{ sym: "N", name: "Nitrogen", mass: 14 }},
                {{ sym: "O", name: "Oxygen", mass: 16 }},
                {{ sym: "Na", name: "Sodium", mass: 23 }},
                {{ sym: "Mg", name: "Magnesium", mass: 24 }}
            ];

            const currentEl = elements.find(e => e.sym === sim5State.targetElem) || elements[2];
            const targetMass = currentEl.mass;
            const diff = targetMass - sim5State.currentSlices;
            const tilt = Math.max(-20, Math.min(20, diff * 1.5));

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Element Selector -->
                    <div class="flex items-center justify-between bg-slate-900 p-2 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-400 font-mono">Select Element:</span>
                        <select onchange="window.sim5SetElem(this.value)" class="bg-slate-950 border border-slate-700 text-cyan-300 rounded px-2 py-1 font-mono">
                            ${{elements.map(e => `
                                <option value="${{e.sym}}" ${{sim5State.targetElem === e.sym ? 'selected' : ''}}>${{e.name}} (${{e.sym}} = ${{e.mass}} u)</option>
                            `).join('')}}
                        </select>
                    </div>

                    <!-- Beam Balance SVG -->
                    <svg viewBox="0 0 240 140" class="w-full h-36">
                        <!-- Stand -->
                        <polygon points="120,40 115,120 125,120" fill="#475569"/>
                        <rect x="90" y="120" width="60" height="8" rx="2" fill="#334155"/>

                        <!-- Fulcrum -->
                        <polygon points="120,35 110,48 130,48" fill="#0284c7"/>

                        <!-- Tilting Beam -->
                        <g transform="rotate(${{tilt}} 120 40)">
                            <rect x="30" y="38" width="180" height="4" rx="2" fill="#38bdf8"/>

                            <!-- Left Pan (Element Atom) -->
                            <line x1="45" y1="40" x2="45" y2="75" stroke="#94a3b8" stroke-width="1.2"/>
                            <path d="M 25 75 Q 45 85 65 75 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                            <circle cx="45" cy="65" r="10" fill="#0284c7"/>
                            <text x="45" y="68" font-size="8" font-weight="bold" fill="#fff" font-family="monospace" text-anchor="middle">${{currentEl.sym}}</text>

                            <!-- Right Pan (C-12 1u Slices) -->
                            <line x1="195" y1="40" x2="195" y2="75" stroke="#94a3b8" stroke-width="1.2"/>
                            <path d="M 175 75 Q 195 85 215 75 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                            <text x="195" y="68" font-size="8" font-weight="bold" fill="#38bdf8" font-family="monospace" text-anchor="middle">${{sim5State.currentSlices}} × 1u</text>
                        </g>
                    </svg>

                    <!-- Control Buttons -->
                    <div class="flex items-center justify-between gap-2">
                        <button onclick="window.sim5AddSlice(1)" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700">
                            +1 Slice (1u)
                        </button>
                        <button onclick="window.sim5AddSlice(5)" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700">
                            +5 Slices
                        </button>
                        <button onclick="window.sim5AutoBalance()" class="flex-1 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow-md">
                            Auto-Balance
                        </button>
                    </div>

                    <!-- Status Display -->
                    <div class="text-center text-xs font-mono p-2 rounded-lg border ${{diff === 0 ? 'bg-emerald-950/60 border-emerald-500 text-emerald-300' : 'bg-slate-950 border-slate-800 text-slate-400'}}">
                        ${{diff === 0 ? `⚖️ Perfectly Balanced! 1 atom of ${{currentEl.name}} = ${{targetMass}} unified atomic mass units (u)` : `Current: ${{sim5State.currentSlices}} u • Target: ${{targetMass}} u (Difference: ${{diff}} u)`}}
                    </div>
                </div>
            `;
        }}

        window.sim5SetElem = sym => {{ sim5State.targetElem = sym; sim5State.currentSlices = 0; renderSim5(document.getElementById('interactiveViewport')); }};
        window.sim5AddSlice = n => {{ sim5State.currentSlices += n; renderSim5(document.getElementById('interactiveViewport')); }};
        window.sim5AutoBalance = () => {{
            const elements = [{{ sym: "H", mass: 1 }}, {{ sym: "He", mass: 4 }}, {{ sym: "C", mass: 12 }}, {{ sym: "N", mass: 14 }}, {{ sym: "O", mass: 16 }}, {{ sym: "Na", mass: 23 }}, {{ sym: "Mg", mass: 24 }}];
            const el = elements.find(e => e.sym === sim5State.targetElem);
            if (el) sim5State.currentSlices = el.mass;
            renderSim5(document.getElementById('interactiveViewport'));
        }};

        // Sim 6: 3D Atomicity Molecule Assembler
        function renderSim6(vp) {{
            const types = [
                {{ key: "mono", name: "Monoatomic (Ar)", n: 1, formula: "Ar" }},
                {{ key: "di", name: "Diatomic (O₂)", n: 2, formula: "O₂" }},
                {{ key: "tri", name: "Triatomic (O₃)", n: 3, formula: "O₃" }},
                {{ key: "tetra", name: "Tetra-atomic (P₄)", n: 4, formula: "P₄" }},
                {{ key: "poly", name: "Poly-atomic (S₈)", n: 8, formula: "S₈" }}
            ];

            const cur = types.find(t => t.key === sim6State.type) || types[1];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Atomicity Type Ribbon -->
                    <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{types.map(t => `
                            <button onclick="window.sim6SetType('${{t.key}}')" class="py-1 rounded ${{sim6State.type === t.key ? 'bg-cyan-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{t.formula}}</button>
                        `).join('')}}
                    </div>

                    <!-- Visual Molecule Canvas -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                        <svg viewBox="0 0 200 160" class="w-48 h-40">
                            ${{
                                cur.key === 'mono' ? `
                                    <circle cx="100" cy="80" r="24" fill="#a855f7" stroke="#e9d5ff" stroke-width="2"/>
                                    <text x="100" y="85" font-size="12" font-weight="bold" fill="#fff" font-family="monospace" text-anchor="middle">Ar</text>
                                ` : cur.key === 'di' ? `
                                    <line x1="75" y1="80" x2="125" y2="80" stroke="#ef4444" stroke-width="6"/>
                                    <circle cx="75" cy="80" r="18" fill="#ef4444"/>
                                    <circle cx="125" cy="80" r="18" fill="#ef4444"/>
                                    <text x="75" y="84" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">O</text>
                                    <text x="125" y="84" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">O</text>
                                ` : cur.key === 'tri' ? `
                                    <polygon points="100,50 65,110 135,110" fill="none" stroke="#ef4444" stroke-width="3"/>
                                    <circle cx="100" cy="50" r="16" fill="#ef4444"/>
                                    <circle cx="65" cy="110" r="16" fill="#ef4444"/>
                                    <circle cx="135" cy="110" r="16" fill="#ef4444"/>
                                    <text x="100" y="54" font-size="9" font-weight="bold" fill="#fff" text-anchor="middle">O</text>
                                    <text x="65" y="114" font-size="9" font-weight="bold" fill="#fff" text-anchor="middle">O</text>
                                    <text x="135" y="114" font-size="9" font-weight="bold" fill="#fff" text-anchor="middle">O</text>
                                ` : cur.key === 'tetra' ? `
                                    <!-- P4 Tetrahedron -->
                                    <polygon points="100,35 60,115 140,115" fill="none" stroke="#f59e0b" stroke-width="2"/>
                                    <line x1="100" y1="35" x2="100" y2="90" stroke="#f59e0b" stroke-width="2"/>
                                    <line x1="60" y1="115" x2="100" y2="90" stroke="#f59e0b" stroke-width="2"/>
                                    <line x1="140" y1="115" x2="100" y2="90" stroke="#f59e0b" stroke-width="2"/>
                                    <circle cx="100" cy="35" r="12" fill="#f59e0b"/><text x="100" y="38" font-size="8" fill="#fff" text-anchor="middle">P</text>
                                    <circle cx="60" cy="115" r="12" fill="#f59e0b"/><text x="60" y="118" font-size="8" fill="#fff" text-anchor="middle">P</text>
                                    <circle cx="140" cy="115" r="12" fill="#f59e0b"/><text x="140" y="118" font-size="8" fill="#fff" text-anchor="middle">P</text>
                                    <circle cx="100" cy="90" r="12" fill="#d97706"/><text x="100" y="93" font-size="8" fill="#fff" text-anchor="middle">P</text>
                                ` : `
                                    <!-- S8 Puckered Crown Ring -->
                                    <polygon points="60,60 100,45 140,60 160,100 140,120 100,105 60,120 40,100" fill="none" stroke="#eab308" stroke-width="2.5"/>
                                    <circle cx="60" cy="60" r="9" fill="#eab308"/><circle cx="100" cy="45" r="9" fill="#eab308"/>
                                    <circle cx="140" cy="60" r="9" fill="#eab308"/><circle cx="160" cy="100" r="9" fill="#eab308"/>
                                    <circle cx="140" cy="120" r="9" fill="#eab308"/><circle cx="100" cy="105" r="9" fill="#eab308"/>
                                    <circle cx="60" cy="120" r="9" fill="#eab308"/><circle cx="40" cy="100" r="9" fill="#eab308"/>
                                    <text x="100" y="80" font-size="10" font-weight="bold" fill="#fef08a" text-anchor="middle">S₈ Crown</text>
                                `
                            }}
                        </svg>
                    </div>

                    <!-- Atomicity Data Card -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex items-center justify-between text-xs font-mono">
                        <div>
                            <span class="text-slate-400">Molecule:</span> <strong class="text-white">${{cur.name}}</strong>
                        </div>
                        <div class="px-2.5 py-1 rounded bg-cyan-600/30 border border-cyan-500/40 text-cyan-300 font-bold">
                            Atomicity = ${{cur.n}}
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim6SetType = k => {{ sim6State.type = k; renderSim6(document.getElementById('interactiveViewport')); }};

        // Sim 7: Lewis Electron Dot & Covalent Sharing Studio
        function renderSim7(vp) {{
            const mols = [
                {{ key: "h2", name: "H₂ (Single Bond)", formula: "H-H", shared: 1 }},
                {{ key: "o2", name: "O₂ (Double Bond)", formula: "O=O", shared: 2 }},
                {{ key: "n2", name: "N₂ (Triple Bond)", formula: "N≡N", shared: 3 }},
                {{ key: "h2o", name: "H₂O (Water)", formula: "H-O-H", shared: 2 }},
                {{ key: "ch4", name: "CH₄ (Methane)", formula: "C(H)₄", shared: 4 }}
            ];

            const cur = mols.find(m => m.key === sim7State.molecule) || mols[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Molecule Selector -->
                    <div class="grid grid-cols-5 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{mols.map(m => `
                            <button onclick="window.sim7SetMol('${{m.key}}')" class="py-1 rounded ${{sim7State.molecule === m.key ? 'bg-cyan-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{m.key.toUpperCase()}}</button>
                        `).join('')}}
                    </div>

                    <!-- Lewis Visualizer -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center h-44">
                        <svg viewBox="0 0 220 120" class="w-full h-36">
                            ${{!sim7State.bonded ? `
                                <!-- Separate Atoms -->
                                <circle cx="70" cy="60" r="32" fill="#0f172a" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
                                <circle cx="150" cy="60" r="32" fill="#0f172a" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
                                <text x="70" y="64" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Atom 1</text>
                                <text x="150" y="64" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Atom 2</text>
                                <!-- Unshared electron dots -->
                                <circle cx="85" cy="60" r="3" fill="#38bdf8"/>
                                <circle cx="135" cy="60" r="3" fill="#38bdf8"/>
                            ` : `
                                <!-- Overlapping Covalent Shells -->
                                <circle cx="90" cy="60" r="38" fill="#0284c7" opacity="0.3"/>
                                <circle cx="130" cy="60" r="38" fill="#0284c7" opacity="0.3"/>
                                <circle cx="90" cy="60" r="38" fill="none" stroke="#38bdf8" stroke-width="2"/>
                                <circle cx="130" cy="60" r="38" fill="none" stroke="#38bdf8" stroke-width="2"/>
                                <!-- Shared Pairs in Intersecting Region -->
                                ${{cur.shared === 1 ? `
                                    <circle cx="110" cy="54" r="3" fill="#38bdf8"/>
                                    <circle cx="110" cy="66" r="3" fill="#38bdf8"/>
                                ` : cur.shared === 2 ? `
                                    <circle cx="106" cy="50" r="3" fill="#38bdf8"/><circle cx="114" cy="50" r="3" fill="#38bdf8"/>
                                    <circle cx="106" cy="70" r="3" fill="#38bdf8"/><circle cx="114" cy="70" r="3" fill="#38bdf8"/>
                                ` : `
                                    <circle cx="106" cy="45" r="2.8" fill="#38bdf8"/><circle cx="114" cy="45" r="2.8" fill="#38bdf8"/>
                                    <circle cx="106" cy="60" r="2.8" fill="#38bdf8"/><circle cx="114" cy="60" r="2.8" fill="#38bdf8"/>
                                    <circle cx="106" cy="75" r="2.8" fill="#38bdf8"/><circle cx="114" cy="75" r="2.8" fill="#38bdf8"/>
                                `}}
                                <text x="70" y="64" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Octet</text>
                                <text x="150" y="64" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Octet</text>
                            `}}
                        </svg>
                    </div>

                    <!-- Action and Details -->
                    <div class="flex items-center justify-between">
                        <button onclick="window.sim7ToggleBond()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-md">
                            ${{!sim7State.bonded ? "Overlap Valence Shells (Form Bond)" : "Reset Valence Shells"}}
                        </button>
                        <span class="text-xs font-mono text-cyan-300">
                            Structure: <strong class="text-white">${{cur.formula}}</strong>
                        </span>
                    </div>
                </div>
            `;
        }}

        window.sim7SetMol = k => {{ sim7State.molecule = k; sim7State.bonded = false; renderSim7(document.getElementById('interactiveViewport')); }};
        window.sim7ToggleBond = () => {{ sim7State.bonded = !sim7State.bonded; renderSim7(document.getElementById('interactiveViewport')); }};

        // Sim 8: Ion Formation & Radical Inspector
        function renderSim8(vp) {{
            const radicals = [
                {{ sym: "NH4", name: "Ammonium", f: "NH₄⁺", charge: "+1", val: 1 }},
                {{ sym: "OH", name: "Hydroxide", f: "OH⁻", charge: "-1", val: 1 }},
                {{ sym: "NO3", name: "Nitrate", f: "NO₃⁻", charge: "-1", val: 1 }},
                {{ sym: "HCO3", name: "Bicarbonate", f: "HCO₃⁻", charge: "-1", val: 1 }},
                {{ sym: "CO3", name: "Carbonate", f: "CO₃²⁻", charge: "-2", val: 2 }},
                {{ sym: "SO4", name: "Sulphate", f: "SO₄²⁻", charge: "-2", val: 2 }},
                {{ sym: "PO4", name: "Phosphate", f: "PO₄³⁻", charge: "-3", val: 3 }}
            ];

            const curRad = radicals.find(r => r.sym === sim8State.activeRadical) || radicals[0];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Ion Formation Demo Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim8SetMode('cation')" class="py-1 rounded-lg ${{sim8State.mode === 'cation' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Cation: Na ➔ Na⁺ + e⁻</button>
                        <button onclick="window.sim8SetMode('anion')" class="py-1 rounded-lg ${{sim8State.mode === 'anion' ? 'bg-rose-600 text-white font-bold' : 'text-slate-400'}}">Anion: Cl + e⁻ ➔ Cl⁻</button>
                    </div>

                    <!-- Animated Ion Box -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center font-mono text-xs">
                        ${{sim8State.mode === 'cation' ? `
                            <div class="text-cyan-400 font-bold text-sm">Na Atom (2, 8, 1) Loses 1 Valence Electron</div>
                            <div class="text-slate-400 text-[11px] mt-1">Result: Sodium Cation (Na⁺) with stable Neon octet (2, 8). Charge = +1.</div>
                        ` : `
                            <div class="text-rose-400 font-bold text-sm">Cl Atom (2, 8, 7) Gains 1 Electron</div>
                            <div class="text-slate-400 text-[11px] mt-1">Result: Chloride Anion (Cl⁻) with stable Argon octet (2, 8, 8). Charge = -1.</div>
                        `}}
                    </div>

                    <!-- Polyatomic Radicals Grid -->
                    <div>
                        <span class="text-[10px] font-mono text-slate-400 uppercase tracking-widest block mb-1.5">Common Polyatomic Radicals (C-1.1):</span>
                        <div class="grid grid-cols-4 gap-1.5">
                            ${{radicals.map(r => `
                                <button onclick="window.sim8SetRadical('${{r.sym}}')" class="p-1.5 rounded-lg border ${{sim8State.activeRadical === r.sym ? 'border-cyan-500 bg-cyan-500/20 text-cyan-200' : 'border-slate-800 bg-slate-900 text-slate-300'}} flex flex-col items-center">
                                    <span class="text-xs font-bold font-mono">${{r.f}}</span>
                                    <span class="text-[9px] text-slate-400">${{r.charge}}</span>
                                </button>
                            `).join('')}}
                        </div>
                    </div>

                    <!-- Selected Radical Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between font-mono text-xs">
                        <div>
                            <span class="text-slate-400">Radical:</span> <strong class="text-white">${{curRad.name}}</strong>
                        </div>
                        <div class="text-cyan-300 font-bold">
                            Formula: ${{curRad.f}}
                        </div>
                        <div class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold">
                            Valency = ${{curRad.val}}
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim8SetMode = m => {{ sim8State.mode = m; renderSim8(document.getElementById('interactiveViewport')); }};
        window.sim8SetRadical = sym => {{ sim8State.activeRadical = sym; renderSim8(document.getElementById('interactiveViewport')); }};

        // Sim 9: Ionic Crystal Lattice & Electrolytic Circuit Tester
        function renderSim9(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Circuit State Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim9SetState('solid')" class="py-1 rounded-lg ${{sim9State.state === 'solid' ? 'bg-slate-700 text-white font-bold' : 'text-slate-400'}}">Solid NaCl Crystal</button>
                        <button onclick="window.sim9SetState('aqueous')" class="py-1 rounded-lg ${{sim9State.state === 'aqueous' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Aqueous / Molten NaCl</button>
                    </div>

                    <!-- Circuit SVG -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-center">
                        <svg viewBox="0 0 200 130" class="w-48 h-32">
                            <!-- Beaker -->
                            <rect x="50" y="55" width="100" height="65" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                            <!-- Liquid / Solid Content -->
                            ${{sim9State.state === 'aqueous' ? `
                                <rect x="52" y="70" width="96" height="48" fill="#0284c7" opacity="0.4"/>
                                <!-- Mobile ions -->
                                <circle cx="70" cy="85" r="5" fill="#a855f7"/><text x="70" y="88" font-size="6" fill="#fff" text-anchor="middle">Na⁺</text>
                                <circle cx="120" cy="95" r="6" fill="#22c55e"/><text x="120" y="98" font-size="6" fill="#fff" text-anchor="middle">Cl⁻</text>
                                <circle cx="95" cy="100" r="5" fill="#a855f7"/><text x="95" y="103" font-size="6" fill="#fff" text-anchor="middle">Na⁺</text>
                            ` : `
                                <!-- Rigid Crystal Lattice Grid -->
                                <rect x="65" y="75" width="70" height="40" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
                                <text x="100" y="98" font-size="8" fill="#94a3b8" font-family="monospace" text-anchor="middle">Locked Lattice</text>
                            `}}

                            <!-- Electrodes -->
                            <rect x="70" y="45" width="8" height="60" fill="#64748b"/>
                            <rect x="122" y="45" width="8" height="60" fill="#64748b"/>

                            <!-- Circuit Wires -->
                            <polyline points="74,45 74,20 90,20" fill="none" stroke="#f1f5f9" stroke-width="1.5"/>
                            <polyline points="126,45 126,20 110,20" fill="none" stroke="#f1f5f9" stroke-width="1.5"/>

                            <!-- Light Bulb -->
                            <circle cx="100" cy="20" r="10" fill="${{sim9State.state === 'aqueous' ? '#facc15' : '#334155'}}" stroke="#e2e8f0" stroke-width="1.5"/>
                            ${{sim9State.state === 'aqueous' ? `
                                <!-- Glowing Rays -->
                                <line x1="100" y1="5" x2="100" y2="0" stroke="#facc15" stroke-width="2"/>
                                <line x1="85" y1="12" x2="80" y2="8" stroke="#facc15" stroke-width="2"/>
                                <line x1="115" y1="12" x2="120" y2="8" stroke="#facc15" stroke-width="2"/>
                            ` : ''}}
                        </svg>
                    </div>

                    <!-- Observation Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-xs font-mono">
                        ${{sim9State.state === 'aqueous' ? `
                            <div class="text-emerald-400 font-bold">💡 Light Bulb GLOWS Brightly!</div>
                            <div class="text-slate-300 text-[11px] mt-0.5">Water overcomes ionic lattice forces. Free mobile Na⁺ and Cl⁻ ions migrate to electrodes, conducting electric current.</div>
                        ` : `
                            <div class="text-rose-400 font-bold">❌ Light Bulb is OFF (Insulator)</div>
                            <div class="text-slate-300 text-[11px] mt-0.5">In solid state, strong electrostatic forces hold ions in fixed positions. Zero mobile charge carriers ➔ No current.</div>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim9SetState = st => {{ sim9State.state = st; renderSim9(document.getElementById('interactiveViewport')); }};

        // Sim 10: Step-by-Step Criss-Cross Formula Builder
        function renderSim10(vp) {{
            const cations = [
                {{ sym: "Na", charge: "+1", v: 1, label: "Na⁺" }},
                {{ sym: "Mg", charge: "+2", v: 2, label: "Mg²⁺" }},
                {{ sym: "Al", charge: "+3", v: 3, label: "Al³⁺" }},
                {{ sym: "Ca", charge: "+2", v: 2, label: "Ca²⁺" }},
                {{ sym: "NH4", charge: "+1", v: 1, label: "NH₄⁺", poly: true }}
            ];

            const anions = [
                {{ sym: "Cl", charge: "-1", v: 1, label: "Cl⁻" }},
                {{ sym: "O", charge: "-2", v: 2, label: "O²⁻" }},
                {{ sym: "OH", charge: "-1", v: 1, label: "OH⁻", poly: true }},
                {{ sym: "SO4", charge: "-2", v: 2, label: "SO₄²⁻", poly: true }},
                {{ sym: "CO3", charge: "-2", v: 2, label: "CO₃²⁻", poly: true }}
            ];

            const cat = cations.find(c => c.sym === sim10State.cation) || cations[0];
            const an = anions.find(a => a.sym === sim10State.anion) || anions[0];

            // Formula calculation & simplification
            let cSub = an.v;
            let aSub = cat.v;

            function gcd(a, b) {{ return b === 0 ? a : gcd(b, a % b); }}
            const g = gcd(cSub, aSub);
            cSub /= g;
            aSub /= g;

            let cStr = cat.sym;
            if (cSub > 1) {{
                cStr = cat.poly ? `(${{cat.sym}})${{cSub}}` : `${{cat.sym}}${{cSub}}`;
            }}

            let aStr = an.sym;
            if (aSub > 1) {{
                aStr = an.poly ? `(${{an.sym}})${{aSub}}` : `${{an.sym}}${{aSub}}`;
            }}

            const finalFormula = `${{cStr}}${{aStr}}`;

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Dropdown Selectors -->
                    <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                        <div>
                            <span class="text-cyan-300 block mb-1">Cation (Metal/Radical):</span>
                            <select onchange="window.sim10SetCat(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-white">
                                ${{cations.map(c => `<option value="${{c.sym}}" ${{cat.sym === c.sym ? 'selected' : ''}}>${{c.label}}</option>`).join('')}}
                            </select>
                        </div>
                        <div>
                            <span class="text-rose-400 block mb-1">Anion (Non-metal/Radical):</span>
                            <select onchange="window.sim10SetAn(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-white">
                                ${{anions.map(a => `<option value="${{a.sym}}" ${{an.sym === a.sym ? 'selected' : ''}}>${{a.label}}</option>`).join('')}}
                            </select>
                        </div>
                    </div>

                    <!-- Criss-Cross Step Box -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center gap-2">
                        <!-- Step 1 & 2: Symbols and Valencies -->
                        <div class="flex justify-around w-full max-w-xs text-center font-mono">
                            <div>
                                <span class="text-lg font-bold text-cyan-300">${{cat.sym}}</span>
                                <div class="text-xs text-slate-400 mt-1">Valency: <strong class="text-cyan-400">${{cat.v}}</strong></div>
                            </div>
                            <div class="text-xl text-slate-500 font-bold self-center">⤩</div>
                            <div>
                                <span class="text-lg font-bold text-rose-400">${{an.sym}}</span>
                                <div class="text-xs text-slate-400 mt-1">Valency: <strong class="text-rose-400">${{an.v}}</strong></div>
                            </div>
                        </div>

                        <!-- Result Box -->
                        <div class="border-t border-slate-800 w-full pt-2 mt-1 text-center font-mono">
                            <span class="text-[10px] text-slate-400 uppercase tracking-widest block">Standard IUPAC Formula:</span>
                            <div class="text-2xl font-extrabold text-emerald-400 tracking-wider mt-1">
                                ${{finalFormula}}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim10SetCat = c => {{ sim10State.cation = c; renderSim10(document.getElementById('interactiveViewport')); }};
        window.sim10SetAn = a => {{ sim10State.anion = a; renderSim10(document.getElementById('interactiveViewport')); }};

        // Sim 11: Valency Criss-Cross Educational Game (C-5.3)
        function renderSim11(vp) {{
            const targets = [
                {{ name: "Aluminium Oxide", cat: "Al", cV: 3, an: "O", aV: 2, f: "Al₂O₃" }},
                {{ name: "Magnesium Hydroxide", cat: "Mg", cV: 2, an: "OH", aV: 1, f: "Mg(OH)₂" }},
                {{ name: "Sodium Carbonate", cat: "Na", cV: 1, an: "CO3", aV: 2, f: "Na₂CO₃" }},
                {{ name: "Calcium Phosphate", cat: "Ca", cV: 2, an: "PO4", aV: 3, f: "Ca₃(PO₄)₂" }}
            ];

            const curTarget = targets[sim11State.targetIdx % targets.length];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Game Header -->
                    <div class="flex items-center justify-between bg-slate-900 p-2 rounded-xl border border-slate-800 text-xs font-mono">
                        <span class="text-cyan-300 font-bold">🎯 Formula Challenge Game</span>
                        <div class="flex gap-2">
                            <span>Score: <strong class="text-emerald-400">${{sim11State.score}}</strong></span>
                            <span>Streak: <strong class="text-amber-400">${{sim11State.streak}}🔥</strong></span>
                        </div>
                    </div>

                    <!-- Target Card -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center font-mono">
                        <span class="text-[10px] text-slate-400 uppercase tracking-widest">Target Compound:</span>
                        <div class="text-base font-extrabold text-cyan-300 mt-0.5">${{curTarget.name}}</div>
                    </div>

                    <!-- Interactive Tile Selector -->
                    <div class="space-y-2 text-xs font-mono">
                        <div>
                            <span class="text-[10px] text-slate-400 block mb-1">Pick Cation:</span>
                            <div class="grid grid-cols-4 gap-1">
                                ${{[{{ sym: "Na", v: 1 }}, {{ sym: "Mg", v: 2 }}, {{ sym: "Al", v: 3 }}, {{ sym: "Ca", v: 2 }}].map(c => `
                                    <button onclick="window.sim11SelectCat('${{c.sym}}')" class="py-1 rounded border ${{sim11State.selectedCation === c.sym ? 'border-cyan-500 bg-cyan-500/20 text-cyan-200' : 'border-slate-800 bg-slate-900 text-slate-300'}}">${{c.sym}}</button>
                                `).join('')}}
                            </div>
                        </div>
                        <div>
                            <span class="text-[10px] text-slate-400 block mb-1">Pick Anion:</span>
                            <div class="grid grid-cols-4 gap-1">
                                ${{[{{ sym: "Cl", v: 1 }}, {{ sym: "O", v: 2 }}, {{ sym: "OH", v: 1 }}, {{ sym: "CO3", v: 2 }}, {{ sym: "PO4", v: 3 }}].map(a => `
                                    <button onclick="window.sim11SelectAn('${{a.sym}}')" class="py-1 rounded border ${{sim11State.selectedAnion === a.sym ? 'border-rose-500 bg-rose-500/20 text-rose-200' : 'border-slate-800 bg-slate-900 text-slate-300'}}">${{a.sym}}</button>
                                `).join('')}}
                            </div>
                        </div>
                    </div>

                    <!-- Action and Feedback -->
                    <button onclick="window.sim11Check()" class="w-full py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs shadow-md transition">
                        Verify Formula Formula
                    </button>
                    <div id="sim11Feedback" class="text-center text-xs font-mono min-h-[20px]"></div>
                </div>
            `;
        }}

        window.sim11SelectCat = c => {{ sim11State.selectedCation = c; renderSim11(document.getElementById('interactiveViewport')); }};
        window.sim11SelectAn = a => {{ sim11State.selectedAnion = a; renderSim11(document.getElementById('interactiveViewport')); }};
        window.sim11Check = () => {{
            const targets = [
                {{ cat: "Al", an: "O", f: "Al₂O₃" }},
                {{ cat: "Mg", an: "OH", f: "Mg(OH)₂" }},
                {{ cat: "Na", an: "CO3", f: "Na₂CO₃" }},
                {{ cat: "Ca", an: "PO4", f: "Ca₃(PO₄)₂" }}
            ];
            const cur = targets[sim11State.targetIdx % targets.length];
            const fb = document.getElementById('sim11Feedback');

            if (sim11State.selectedCation === cur.cat && sim11State.selectedAnion === cur.an) {{
                sim11State.score += 10;
                sim11State.streak += 1;
                sim11State.targetIdx += 1;
                sim11State.selectedCation = null;
                sim11State.selectedAnion = null;
                fb.innerHTML = `<span class="text-emerald-400 font-bold">✨ Correct! Formula: ${{cur.f}} (+10 Pts)</span>`;
                setTimeout(() => renderSim11(document.getElementById('interactiveViewport')), 900);
            }} else {{
                sim11State.streak = 0;
                fb.innerHTML = `<span class="text-rose-400 font-bold">Incorrect ions selected! Try again.</span>`;
            }}
        }};

        // Sim 12: Molecular Mass Breakdown & Summation Engine
        function renderSim12(vp) {{
            const data = {{
                "H2O": {{ name: "Water", formula: "H₂O", items: [{{ elem: "H", n: 2, m: 1 }}, {{ elem: "O", n: 1, m: 16 }}], total: 18 }},
                "CO2": {{ name: "Carbon Dioxide", formula: "CO₂", items: [{{ elem: "C", n: 1, m: 12 }}, {{ elem: "O", n: 2, m: 16 }}], total: 44 }},
                "CH4": {{ name: "Methane", formula: "CH₄", items: [{{ elem: "C", n: 1, m: 12 }}, {{ elem: "H", n: 4, m: 1 }}], total: 16 }},
                "HNO3": {{ name: "Nitric Acid", formula: "HNO₃", items: [{{ elem: "H", n: 1, m: 1 }}, {{ elem: "N", n: 1, m: 14 }}, {{ elem: "O", n: 3, m: 16 }}], total: 63 }},
                "C6H12O6": {{ name: "Glucose", formula: "C₆H₁₂O₆", items: [{{ elem: "C", n: 6, m: 12 }}, {{ elem: "H", n: 12, m: 1 }}, {{ elem: "O", n: 6, m: 16 }}], total: 180 }}
            }};

            const cur = data[sim12State.selectedFormula] || data["H2O"];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Dropdown Picker -->
                    <div class="flex items-center justify-between bg-slate-900 p-2 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-400 font-mono">Select Substance:</span>
                        <select onchange="window.sim12SetFormula(this.value)" class="bg-slate-950 border border-slate-700 text-cyan-300 rounded px-2 py-1 font-mono">
                            ${{Object.keys(data).map(k => `<option value="${{k}}" ${{sim12State.selectedFormula === k ? 'selected' : ''}}>${{data[k].name}} (${{data[k].formula}})</option>`).join('')}}
                        </select>
                    </div>

                    <!-- Breakdown Table -->
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs space-y-1.5">
                        <div class="text-[10px] text-slate-400 uppercase tracking-widest border-b border-slate-800 pb-1">
                            Atomic Summation Breakdown:
                        </div>
                        ${{cur.items.map(it => `
                            <div class="flex justify-between text-slate-300">
                                <span>${{it.n}} × Mass of ${{it.elem}} (${{it.m}} u):</span>
                                <span class="text-cyan-400 font-bold">${{it.n * it.m}} u</span>
                            </div>
                        `).join('')}}
                        <div class="border-t border-slate-800 pt-1.5 flex justify-between text-emerald-400 font-bold text-sm">
                            <span>Total Molecular Mass:</span>
                            <span>${{cur.total}} u</span>
                        </div>
                    </div>

                    <!-- Percentage Bars -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 font-mono text-[11px] space-y-1.5">
                        <span class="text-[10px] text-slate-400 uppercase tracking-widest block">Mass Composition %:</span>
                        ${{cur.items.map(it => {{
                            const pct = ((it.n * it.m) / cur.total * 100).toFixed(1);
                            return `
                                <div>
                                    <div class="flex justify-between text-[10px]">
                                        <span class="text-slate-300">${{it.elem}}:</span>
                                        <span class="text-cyan-300">${{pct}}%</span>
                                    </div>
                                    <div class="w-full bg-slate-950 h-1.5 rounded-full overflow-hidden mt-0.5">
                                        <div class="bg-cyan-500 h-full" style="width: ${{pct}}%"></div>
                                    </div>
                                </div>
                            `;
                        }}).join('')}}
                    </div>
                </div>
            `;
        }}

        window.sim12SetFormula = f => {{ sim12State.selectedFormula = f; renderSim12(document.getElementById('interactiveViewport')); }};

        // Sim 13: Formula Unit Mass vs Molecular Mass Comparator
        function renderSim13(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Toggle Mode -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim13SetMode('molecular')" class="py-1 rounded-lg ${{sim13State.mode === 'molecular' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Molecular Mass (H₂O)</button>
                        <button onclick="window.sim13SetMode('formula')" class="py-1 rounded-lg ${{sim13State.mode === 'formula' ? 'bg-purple-600 text-white font-bold' : 'text-slate-400'}}">Formula Unit Mass (NaCl)</button>
                    </div>

                    <!-- Visual Comparison Graphic -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center text-center">
                        ${{sim13State.mode === 'molecular' ? `
                            <div class="text-cyan-300 font-bold font-mono text-sm">Discrete Independent Molecules (H₂O)</div>
                            <div class="text-[11px] text-slate-400 mt-1 max-w-xs">
                                Water exists as separate, distinct individual H₂O units. Mass = 2(1) + 16 = <strong class="text-emerald-400">18 u</strong>.
                            </div>
                        ` : `
                            <div class="text-purple-300 font-bold font-mono text-sm">Infinite 3D Ionic Crystal Lattice (NaCl)</div>
                            <div class="text-[11px] text-slate-400 mt-1 max-w-xs">
                                No single 'NaCl' molecule exists! Each Na⁺ is surrounded by 6 Cl⁻ ions. We sum the formula unit: 23 + 35.5 = <strong class="text-emerald-400">58.5 u</strong>.
                            </div>
                        `}}
                    </div>

                    <!-- Comparison Matrix -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 text-xs font-mono space-y-1.5">
                        <div class="text-[10px] text-slate-400 uppercase tracking-widest border-b border-slate-800 pb-1">Distinction Summary:</div>
                        <div class="flex justify-between text-slate-300">
                            <span>CaCl₂ (Calcium Chloride):</span>
                            <span class="text-cyan-400 font-bold">111 u (Formula Unit)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>CO₂ (Carbon Dioxide):</span>
                            <span class="text-cyan-400 font-bold">44 u (Molecular Mass)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>CuSO₄·5H₂O (Blue Vitriol):</span>
                            <span class="text-cyan-400 font-bold">249.5 u (Formula Unit)</span>
                        </div>
                    </div>
                </div>
            `;
        }}

        window.sim13SetMode = m => {{ sim13State.mode = m; renderSim13(document.getElementById('interactiveViewport')); }};

        // Sim 14: 3D Molecular Architect & Geometries (C-8.1)
        function renderSim14(vp) {{
            const geoms = [
                {{ key: "co2", name: "CO₂ (Linear)", angle: "180°", desc: "Straight line with dual double bonds" }},
                {{ key: "h2o", name: "H₂O (Bent)", angle: "104.5°", desc: "Bent V-shape squeezed by 2 oxygen lone pairs" }},
                {{ key: "nh3", name: "NH₃ (Pyramidal)", angle: "107.8°", desc: "Trigonal pyramid with apex lone pair" }},
                {{ key: "ch4", name: "CH₄ (Tetrahedral)", angle: "109.5°", desc: "Regular 3D tetrahedron" }}
            ];

            const cur = geoms.find(g => g.key === sim14State.molecule) || geoms[1];

            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Geometry Selector -->
                    <div class="grid grid-cols-4 gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-[10px] font-mono">
                        ${{geoms.map(g => `
                            <button onclick="window.sim14SetMol('${{g.key}}')" class="py-1 rounded ${{sim14State.molecule === g.key ? 'bg-cyan-600 text-white font-bold' : 'bg-slate-800 text-slate-400'}}">${{g.key.toUpperCase()}}</button>
                        `).join('')}}
                    </div>

                    <!-- 3D SVG Geometry Canvas -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center h-44">
                        <svg viewBox="0 0 200 140" class="w-48 h-36">
                            ${{
                                cur.key === 'co2' ? `
                                    <line x1="40" y1="70" x2="160" y2="70" stroke="#94a3b8" stroke-width="4"/>
                                    <circle cx="100" cy="70" r="16" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                                    <circle cx="40" cy="70" r="14" fill="#ef4444"/>
                                    <circle cx="160" cy="70" r="14" fill="#ef4444"/>
                                    <text x="100" y="74" font-size="9" fill="#fff" text-anchor="middle">C</text>
                                    <text x="40" y="74" font-size="9" fill="#fff" text-anchor="middle">O</text>
                                    <text x="160" y="74" font-size="9" fill="#fff" text-anchor="middle">O</text>
                                    <text x="100" y="105" font-size="10" font-mono font-bold fill="#38bdf8" text-anchor="middle">180° Linear</text>
                                ` : cur.key === 'h2o' ? `
                                    <line x1="100" y1="50" x2="60" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="50" x2="140" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <circle cx="100" cy="50" r="18" fill="#ef4444"/>
                                    <circle cx="60" cy="105" r="12" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                                    <circle cx="140" cy="105" r="12" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                                    <text x="100" y="54" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">O</text>
                                    <text x="60" y="108" font-size="8" fill="#0f172a" font-weight="bold" text-anchor="middle">H</text>
                                    <text x="140" y="108" font-size="8" fill="#0f172a" font-weight="bold" text-anchor="middle">H</text>
                                    <text x="100" y="130" font-size="10" font-mono font-bold fill="#38bdf8" text-anchor="middle">104.5° Bent</text>
                                ` : cur.key === 'nh3' ? `
                                    <line x1="100" y1="45" x2="60" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="45" x2="100" y2="115" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="45" x2="140" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <circle cx="100" cy="45" r="18" fill="#3b82f6"/>
                                    <circle cx="60" cy="105" r="11" fill="#f8fafc"/>
                                    <circle cx="100" cy="115" r="11" fill="#f8fafc"/>
                                    <circle cx="140" cy="105" r="11" fill="#f8fafc"/>
                                    <text x="100" y="49" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">N</text>
                                    <text x="100" y="132" font-size="10" font-mono font-bold fill="#38bdf8" text-anchor="middle">107.8° Pyramidal</text>
                                ` : `
                                    <line x1="100" y1="70" x2="100" y2="25" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="70" x2="55" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="70" x2="100" y2="115" stroke="#94a3b8" stroke-width="3"/>
                                    <line x1="100" y1="70" x2="145" y2="105" stroke="#94a3b8" stroke-width="3"/>
                                    <circle cx="100" cy="70" r="16" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                                    <circle cx="100" cy="25" r="10" fill="#f8fafc"/>
                                    <circle cx="55" cy="105" r="10" fill="#f8fafc"/>
                                    <circle cx="100" cy="115" r="10" fill="#f8fafc"/>
                                    <circle cx="145" cy="105" r="10" fill="#f8fafc"/>
                                    <text x="100" y="74" font-size="9" fill="#fff" text-anchor="middle">C</text>
                                    <text x="100" y="135" font-size="10" font-mono font-bold fill="#38bdf8" text-anchor="middle">109.5° Tetrahedral</text>
                                `
                            }}
                        </svg>
                    </div>

                    <!-- Details Card -->
                    <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between text-xs font-mono">
                        <span class="text-slate-400">${{cur.desc}}</span>
                        <span class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold">${{cur.angle}}</span>
                    </div>
                </div>
            `;
        }}

        window.sim14SetMol = k => {{ sim14State.molecule = k; renderSim14(document.getElementById('interactiveViewport')); }};

        // Sim 15: Indian Rasashastra & Modern Peaceful Science
        function renderSim15(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Mode Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim15SetView('ancient')" class="py-1 rounded-lg ${{sim15State.view === 'ancient' ? 'bg-amber-600 text-white font-bold' : 'text-slate-400'}}">Ancient: Cinnabar Metallurgy</button>
                        <button onclick="window.sim15SetView('modern')" class="py-1 rounded-lg ${{sim15State.view === 'modern' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Modern: BARC Peaceful Science</button>
                    </div>

                    <!-- Content Panel -->
                    ${{sim15State.view === 'ancient' ? `
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center gap-2 text-center">
                            <span class="text-[10px] font-mono text-amber-400 uppercase tracking-widest">Rasashastra Urdhva-patana Yantra (Sublimation)</span>
                            <div class="text-xs font-mono text-slate-300 mt-1">
                                Heating red cinnabar mineral (HgS, Hingula):
                            </div>
                            <div class="text-xs font-mono text-amber-300 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
                                HgS(s) + O₂(g) ➔ Hg(g)↑ (Mercury Vapor) + SO₂(g)
                            </div>
                            <div class="text-[11px] text-slate-400 leading-relaxed mt-1">
                                Liquid mercury condensed on the upper inverted clay pot, illustrating early Indian chemical distillation.
                            </div>
                        </div>
                    ` : `
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col gap-2 font-mono text-xs">
                            <span class="text-[10px] text-cyan-400 uppercase tracking-widest border-b border-slate-800 pb-1">BARC Peaceful Atomic Innovations (C-5.2):</span>
                            <div class="flex items-center gap-2 text-slate-300">
                                <span class="text-cyan-400">🏥</span>
                                <span>Cobalt-60 & I-131: Targeted cancer and thyroid therapies</span>
                            </div>
                            <div class="flex items-center gap-2 text-slate-300">
                                <span class="text-emerald-400">🌱</span>
                                <span>Trombay Mutant Crops: High-yield pulses & groundnuts</span>
                            </div>
                            <div class="flex items-center gap-2 text-slate-300">
                                <span class="text-purple-400">🤝</span>
                                <span>Social Bonding Metaphor: Covalent sharing & Ionic complement</span>
                            </div>
                        </div>
                    `}}
                </div>
            `;
        }}

        window.sim15SetView = v => {{ sim15State.view = v; renderSim15(document.getElementById('interactiveViewport')); }};

        // Sim 16: Mass Defect & Relativity Conservation Boundary (C-7.2)
        function renderSim16(vp) {{
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3">
                    <!-- Reaction Type Toggle -->
                    <div class="grid grid-cols-2 gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-mono">
                        <button onclick="window.sim16Set('chemical')" class="py-1 rounded-lg ${{sim16State.reactionType === 'chemical' ? 'bg-cyan-600 text-white font-bold' : 'text-slate-400'}}">Chemical Combustion (CH₄)</button>
                        <button onclick="window.sim16Set('nuclear')" class="py-1 rounded-lg ${{sim16State.reactionType === 'nuclear' ? 'bg-rose-600 text-white font-bold' : 'text-slate-400'}}">Nuclear Fission (²³⁵U)</button>
                    </div>

                    <!-- Defect Calculator Card -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
                        ${{sim16State.reactionType === 'chemical' ? `
                            <div class="text-cyan-300 font-bold text-sm">Chemical Reaction: 1 mol CH₄ Burning</div>
                            <div class="flex justify-between text-slate-300">
                                <span>Energy Released (ΔE):</span>
                                <span class="text-amber-400 font-bold">890 kJ</span>
                            </div>
                            <div class="flex justify-between text-slate-300">
                                <span>Relativistic Mass Defect (Δm = ΔE/c²):</span>
                                <span class="text-emerald-400 font-bold">9.9 × 10⁻¹² kg (~10⁻⁸ mg)</span>
                            </div>
                            <div class="text-[11px] text-slate-400 border-t border-slate-800 pt-1 leading-relaxed">
                                Because 10⁻⁸ mg is completely unmeasurable on any analytical balance, <strong>Lavoisier's Law of Conservation of Mass holds with absolute perfection</strong> in all chemistry!
                            </div>
                        ` : `
                            <div class="text-rose-400 font-bold text-sm">Nuclear Fission: 1 kg ²³⁵U Fission</div>
                            <div class="flex justify-between text-slate-300">
                                <span>Energy Released (ΔE):</span>
                                <span class="text-amber-400 font-bold">8.2 × 10¹³ J</span>
                            </div>
                            <div class="flex justify-between text-slate-300">
                                <span>Mass Converted to Energy (Δm):</span>
                                <span class="text-rose-400 font-bold">~0.91 grams (0.09%)</span>
                            </div>
                            <div class="text-[11px] text-slate-400 border-t border-slate-800 pt-1 leading-relaxed">
                                In nuclear physics, mass defect is large and measurable. Separate mass and energy conservation laws merge into the <strong>Unified Law of Conservation of Mass-Energy</strong>.
                            </div>
                        `}}
                    </div>
                </div>
            `;
        }}

        window.sim16Set = t => {{ sim16State.reactionType = t; renderSim16(document.getElementById('interactiveViewport')); }};

        // ==========================================
        // DEDICATED QUIZ SLIDES (17-20) RENDERING
        // ==========================================
        function renderQuizSlide(vp, slide) {{
            const quizList = slide.quiz || [];
            vp.innerHTML = `
                <div class="w-full flex flex-col gap-3 max-h-[500px] overflow-y-auto pr-1 scrollbar-thin">
                    <div class="text-xs font-mono text-cyan-300 font-bold border-b border-slate-800 pb-1 flex justify-between">
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
                                <button onclick="openSolutionModal('${{q.q.replace(/'/g, "\\\\'") }}', '${{q.sol.replace(/'/g, "\\\\'") }}')" class="px-2.5 py-1 rounded bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-300 border border-cyan-500/30 text-[10px] font-mono font-bold transition flex items-center gap-1">
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
