#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 6: Control and Coordination
Master Interactive Multimedia Lab
File: public/animations/control-and-coordination.html
"""

import json
import os
import sys

# Add .agents to sys.path
sys.path.append(os.path.abspath('.agents'))
from control_coordination_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def generate_html():
    print("Generating public/animations/control-and-coordination.html...")

    # Build slides HTML
    slides_html_list = []

    for s_idx, slide in enumerate(ALL_SLIDES):
        is_quiz = (s_idx >= 17)
        slide_num = s_idx + 1
        total_slides = len(ALL_SLIDES)

        if not is_quiz:
            # Content Slide
            theory_blocks_html = ""
            for tb in slide["theory_blocks"]:
                theory_blocks_html += f"""
                <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-4 hover:border-slate-700 transition">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400 mb-1.5 flex items-center gap-1.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                        {tb['heading']}
                    </h4>
                    <div class="text-xs sm:text-sm text-slate-300 leading-relaxed space-y-1.5">
                        {tb['content']}
                    </div>
                </div>
            """

            # 2 Checkpoints
            checkpoints_html = ""
            for q_idx, cp in enumerate(slide["checkpoints"]):
                options_html = ""
                for o_idx, opt in enumerate(cp["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="chk-{s_idx}-{q_idx}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_idx}, {o_idx}, {cp['ans']}, 'chk-sol-{s_idx}-{q_idx}')" class="mt-0.5 text-emerald-600 focus:ring-emerald-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                checkpoints_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 mb-3">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Checkpoint {q_idx + 1} of 2</span>
                        <div id="feedback-{s_idx}-{q_idx}"></div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-2.5">{cp['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        {options_html}
                    </div>
                    <div id="chk-sol-{s_idx}-{q_idx}" class="hidden mt-2.5 p-3 rounded-lg bg-emerald-950/30 border border-emerald-500/30 text-xs text-slate-200">
                        <span class="font-bold text-emerald-400">Step-by-Step Teacher Explanation:</span><br>
                        {cp['solution']}
                    </div>
                </div>
            """

            # Teacher Avatar Card with synchronized mouth
            teacher_card_html = f"""
            <!-- Person Talking: Dr. Sophia Biology Teacher Avatar -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-emerald-950/20 border border-emerald-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <!-- Lab coat shoulders -->
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#059669" stroke="#10b981" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <!-- Head / Face -->
                        <circle cx="60" cy="50" r="26" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
                        <!-- Hair -->
                        <path d="M34 50 C34 25, 86 25, 86 50 C86 35, 75 22, 60 22 C45 22, 34 35, 34 50 Z" fill="#78350f"/>
                        <!-- Eyes & Glasses -->
                        <circle cx="50" cy="48" r="7" fill="none" stroke="#047857" stroke-width="2"/>
                        <circle cx="70" cy="48" r="7" fill="none" stroke="#047857" stroke-width="2"/>
                        <line x1="57" y1="48" x2="63" y2="48" stroke="#047857" stroke-width="2"/>
                        <circle cx="50" cy="48" r="2.5" fill="#1e293b"/>
                        <circle cx="70" cy="48" r="2.5" fill="#1e293b"/>
                        <!-- Eyebrows -->
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <!-- Talking Mouth -->
                        <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mt-1">
                        Dr. Sophia • Biology Teacher
                    </span>
                </div>

                <!-- Speech Bubble Dialogue -->
                <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                    <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                            Teacher's Live Audio Commentary
                        </span>
                        <span class="text-[10px] text-slate-500 font-mono">Web Speech Narration</span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300 italic leading-relaxed">
                        "{slide['narration']}"
                    </p>
                </div>
            </div>
            """

            # Simulator Container
            simulator_html = get_simulator_markup(s_idx, slide["interactive_type"])

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl relative overflow-hidden">
                    <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-emerald-500/10 to-transparent pointer-events-none"></div>
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            {slide['badge']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {slide_num} of {total_slides}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-2">
                        {slide['title']}
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
                        {slide['lead']}
                    </p>
                </div>

                {teacher_card_html}

                <!-- Main Content Grid: Theory & Interactive Simulator -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mb-6">
                    <!-- Left: In-Depth NCERT Theory & Checkpoints (7 Cols) -->
                    <div class="lg:col-span-7 space-y-4">
                        <div class="space-y-3">
                            {theory_blocks_html}
                        </div>
                        <div class="pt-2">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-3 flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                                Slide Checkpoint Questions & Step-by-Step Solutions
                            </h3>
                            {checkpoints_html}
                        </div>
                    </div>

                    <!-- Right: Interactive Lab Simulator (5 Cols) -->
                    <div class="lg:col-span-5">
                        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 sticky top-20 shadow-xl">
                            {simulator_html}
                        </div>
                    </div>
                </div>
            </div>
            """
        else:
            # Quiz Challenge Slide
            questions_html = ""
            for q in slide["questions"]:
                q_id = q["id"]
                options_html = ""
                for o_idx, opt in enumerate(q["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="quiz-{s_idx}-{q_id}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_id}, {o_idx}, {q['ans']}, 'quiz-feedback-{q_id}')" class="mt-0.5 text-emerald-600 focus:ring-emerald-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                # Clean quotes for JS call
                q_title_esc = q['q'].replace("'", "\\'").replace('"', '&quot;')
                q_sol_esc = q['solution'].replace("'", "\\'").replace('"', '&quot;')

                questions_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Question {q_id}</span>
                        <div class="flex items-center gap-2">
                            <div id="quiz-feedback-{q_id}"></div>
                            <button onclick="openQuizSolution({q_id}, '{q_title_esc}', '{q_sol_esc}')" class="px-2.5 py-1 rounded-md bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Solution</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-3">{q['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        {options_html}
                    </div>
                </div>
                """

            # If last slide, add completion banner
            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-emerald-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of Chapter 6: Control and Coordination!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 17 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl">
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            {slide['badge']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {slide_num} of {total_slides}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-2">
                        {slide['title']}
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
                        {slide['description']}
                    </p>
                </div>

                <div class="space-y-4">
                    {questions_html}
                </div>

                {completion_banner}
            </div>
            """

        slides_html_list.append(slide_markup)

    # Bottom Topic Pills
    pills_html = ""
    for s_idx, slide in enumerate(ALL_SLIDES):
        short = slide["short_title"]
        pills_html += f"""
        <button id="pill-{s_idx}" onclick="goToSlide({s_idx})" class="px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all {'bg-emerald-600 text-white font-bold' if s_idx == 0 else 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
            {short}
        </button>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 6: Control and Coordination Master Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            850: '#111827',
                            950: '#030712'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <!-- KaTeX for crisp scientific notation -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

    <style>
        .slide-container {{
            display: none;
        }}
        .slide-container.active {{
            display: block;
            animation: fadeIn 0.3s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .talking-mouth {{
            animation: mouthTalk 0.25s infinite alternate ease-in-out;
        }}
        @keyframes mouthTalk {{
            0% {{ transform: scaleY(0.2); }}
            100% {{ transform: scaleY(1.4); }}
        }}
        .teacher-bob {{
            animation: teacherBob 3s infinite ease-in-out;
        }}
        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-4px); }}
        }}
        .pulse-glow {{
            animation: pulseGlow 2s infinite alternate;
        }}
        @keyframes pulseGlow {{
            from {{ filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.4)); }}
            to {{ filter: drop-shadow(0 0 10px rgba(16, 185, 129, 0.8)); }}
        }}
        .impulse-wave {{
            animation: impulseMove 1.2s infinite linear;
        }}
        @keyframes impulseMove {{
            0% {{ stroke-dashoffset: 60; }}
            100% {{ stroke-dashoffset: 0; }}
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 3px;
        }}
        .modal-backdrop {{
            background-color: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(4px);
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-emerald-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md px-4 py-2.5 sm:px-6">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <!-- Title & Badge -->
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center font-extrabold text-white text-sm shadow-lg shadow-emerald-500/20">
                    6
                </span>
                <div>
                    <h1 class="text-xs sm:text-sm font-bold text-white tracking-wide">
                        Control and Coordination
                    </h1>
                    <p class="text-[10px] text-emerald-400 font-mono">
                        NCERT Class 10 Science • Chapter 6 • Master Multimedia Lab
                    </p>
                </div>
            </div>

            <!-- Voice Controls & Slide Counter -->
            <div class="flex items-center gap-2 sm:gap-4">
                <button id="voiceToggleBtn" onclick="toggleVoiceNarration()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border border-emerald-500/40 text-xs font-semibold transition cursor-pointer" title="Toggle Teacher Voice">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"/></svg>
                    <span id="voiceStatusText">Teacher Voice: Active</span>
                </button>
                <button onclick="replayVoice()" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border border-slate-700 transition cursor-pointer" title="Replay Voice">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                </button>
                <div class="text-xs font-mono text-slate-400 border-l border-slate-700 pl-3">
                    <span id="currentSlideIndicator" class="text-emerald-400 font-bold text-sm">1</span> / 21
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 md:p-8 flex flex-col justify-start">
        <!-- Slides Container -->
        {''.join(slides_html_list)}
    </main>

    <!-- Bottom Navigation Footer & Topic Pills -->
    <footer class="bg-slate-900 border-t border-slate-800 sticky bottom-0 z-30 px-4 py-3 sm:px-6 shadow-2xl">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <!-- Prev / Next Controls -->
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 disabled:opacity-40 disabled:cursor-not-allowed border border-slate-700 cursor-pointer">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    <span>Previous</span>
                </button>
                <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-lg shadow-emerald-600/30 cursor-pointer">
                    <span>Next Slide</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

            <!-- Scrollable Topic Pills -->
            <div class="flex items-center gap-1.5 overflow-x-auto max-w-full sm:max-w-2xl py-1 custom-scrollbar">
                {pills_html}
            </div>
        </div>
    </footer>

    <!-- Universal Solution Popup Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative animate-fadeIn">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 cursor-pointer">
                ✕
            </button>
            <div class="flex items-center gap-2 mb-3">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40" id="modalQuestionId">
                    Question Solution
                </span>
                <span class="text-xs text-slate-400 font-mono">Detailed Teacher Analysis</span>
            </div>
            <h3 class="text-sm sm:text-base font-bold text-white mb-3" id="modalQuestionTitle">
                Question Title
            </h3>
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed max-h-72 overflow-y-auto custom-scrollbar" id="modalSolutionContent">
                Detailed step-by-step teacher explanation will appear here.
            </div>
            <div class="mt-4 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition cursor-pointer">
                    Got it, Continue
                </button>
            </div>
        </div>
    </div>

    <!-- JavaScript Data & Logic -->
    <script>
        const slidesData = {json.dumps(ALL_SLIDES)};

        let currentSlideIndex = 0;
        let voiceActive = true;
        let synth = window.speechSynthesis;
        let currentUtterance = null;
        let audioCtx = null;

        function getAudioContext() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            return audioCtx;
        }}

        function playTone(freq, type = 'sine', duration = 0.15) {{
            try {{
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.08, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            }} catch (e) {{
                console.warn("Web Audio tone warning:", e);
            }}
        }}

        function playCorrectSound() {{
            playTone(523.25, 'triangle', 0.1);
            setTimeout(() => playTone(659.25, 'triangle', 0.1), 100);
            setTimeout(() => playTone(783.99, 'triangle', 0.2), 200);
        }}

        function playIncorrectSound() {{
            playTone(280, 'sawtooth', 0.15);
            setTimeout(() => playTone(220, 'sawtooth', 0.25), 120);
        }}

        function playSlideClickSound() {{
            playTone(440, 'sine', 0.08);
        }}

        function setTeacherTalking(isTalking) {{
            const mouth = document.getElementById(`teacherMouth-${{currentSlideIndex}}`);
            if (mouth) {{
                if (isTalking) {{
                    mouth.classList.add('talking-mouth');
                }} else {{
                    mouth.classList.remove('talking-mouth');
                }}
            }}
        }}

        function speakText(text) {{
            if (!voiceActive || !synth) return;
            synth.cancel();
            const cleanText = text.replace(/<[^>]*>/g, '').replace(/\\$/g, '');
            currentUtterance = new SpeechSynthesisUtterance(cleanText);
            currentUtterance.rate = 1.0;
            currentUtterance.pitch = 1.05;
            
            const voices = synth.getVoices();
            const preferred = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Teacher')));
            if (preferred) currentUtterance.voice = preferred;

            currentUtterance.onstart = () => {{
                setTeacherTalking(true);
            }};
            currentUtterance.onend = () => {{
                setTeacherTalking(false);
            }};
            currentUtterance.onerror = () => {{
                setTeacherTalking(false);
            }};

            synth.speak(currentUtterance);
        }}

        function toggleVoiceNarration() {{
            voiceActive = !voiceActive;
            const statusText = document.getElementById('voiceStatusText');
            if (voiceActive) {{
                statusText.textContent = "Teacher Voice: Active";
                document.getElementById('voiceToggleBtn').className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border border-emerald-500/40 text-xs font-semibold transition";
                playTone(660, 'sine', 0.1);
                replayVoice();
            }} else {{
                statusText.textContent = "Teacher Voice: Muted";
                document.getElementById('voiceToggleBtn').className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:bg-slate-700 border border-slate-700 text-xs font-semibold transition";
                if (synth) synth.cancel();
                setTeacherTalking(false);
                playTone(330, 'sine', 0.1);
            }}
        }}

        function replayVoice() {{
            const slide = slidesData[currentSlideIndex];
            if (slide && slide.narration) {{
                speakText(slide.narration);
            }}
        }}

        function navigateSlide(direction) {{
            const newIndex = currentSlideIndex + direction;
            if (newIndex >= 0 && newIndex < slidesData.length) {{
                goToSlide(newIndex);
            }}
        }}

        function goToSlide(index) {{
            playSlideClickSound();
            if (synth) synth.cancel();
            setTeacherTalking(false);

            const currentEl = document.getElementById(`slide-${{currentSlideIndex}}`);
            if (currentEl) currentEl.classList.remove('active');

            const currentPill = document.getElementById(`pill-${{currentSlideIndex}}`);
            if (currentPill) {{
                currentPill.classList.remove('bg-emerald-600', 'text-white', 'font-bold');
                currentPill.classList.add('bg-slate-800', 'text-slate-300');
            }}

            currentSlideIndex = index;
            const newEl = document.getElementById(`slide-${{currentSlideIndex}}`);
            if (newEl) newEl.classList.add('active');

            const newPill = document.getElementById(`pill-${{currentSlideIndex}}`);
            if (newPill) {{
                newPill.classList.remove('bg-slate-800', 'text-slate-300');
                newPill.classList.add('bg-emerald-600', 'text-white', 'font-bold');
                newPill.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
            }}

            document.getElementById('currentSlideIndicator').textContent = currentSlideIndex + 1;
            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Hide next button on last slide
            const nextBtn = document.getElementById('nextBtn');
            if (currentSlideIndex === slidesData.length - 1) {{
                nextBtn.style.display = 'none';
            }} else {{
                nextBtn.style.display = 'flex';
            }}

            replayVoice();

            if (window.renderMathInElement) {{
                renderMathInElement(newEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {{
            const solEl = document.getElementById(solutionId);
            let feedbackEl = document.getElementById(`feedback-${{slideIdx}}-${{qIdx}}`);
            if (!feedbackEl && solEl && solEl.id && solEl.id.startsWith('quiz-feedback')) {{
                feedbackEl = solEl;
            }}
            
            if (selectedOption === correctOption) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct! Excellent</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Incorrect. Click Solution</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            }}
        }}

        function openQuizSolution(qId, title, solutionHtml) {{
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `Question ${{qId}} Solution`;
            document.getElementById('modalQuestionTitle').textContent = title;
            const solEl = document.getElementById('modalSolutionContent');
            solEl.innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');

            if (window.renderMathInElement) {{
                renderMathInElement(solEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function closeSolutionModal() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < slidesData.length - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        }});

        // ==========================================
        // 17 INTERACTIVE LAB SIMULATORS JAVASCRIPT
        // ==========================================

        // 1. Movement Types Simulator (Slide 0)
        let isSeedGrown = false;
        function toggleSeedGrowth() {{
            isSeedGrown = !isSeedGrown;
            const sprout = document.getElementById('seedlingShoot');
            const roots = document.getElementById('seedlingRoot');
            const status = document.getElementById('movementSimStatus');
            if (isSeedGrown) {{
                sprout.setAttribute('y2', '35');
                sprout.setAttribute('stroke-width', '4');
                roots.setAttribute('y2', '115');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Growth-Dependent Movement:</span> Seedling pushes soil aside by cell division & elongation!";
                playTone(600, 'sine', 0.2);
            }} else {{
                sprout.setAttribute('y2', '65');
                sprout.setAttribute('stroke-width', '2');
                roots.setAttribute('y2', '85');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Dormant Seed:</span> No growth means zero movement occurs.";
                playTone(350, 'sine', 0.15);
            }}
        }}

        function simulateCatSprint() {{
            const cat = document.getElementById('catRunner');
            const status = document.getElementById('movementSimStatus');
            cat.classList.add('impulse-wave');
            status.innerHTML = "<span class='text-amber-300 font-bold'>Growth-Independent Movement:</span> Cat sprints via rapid skeletal muscle contractions to catch prey!";
            playTone(720, 'sine', 0.25);
            setTimeout(() => cat.classList.remove('impulse-wave'), 1200);
        }}

        // 2. Neuron Action Potential & Synapse (Slide 1)
        function fireActionPotential() {{
            const impulse = document.getElementById('impulseDot');
            const status = document.getElementById('neuronStatus');
            const vesicles = document.getElementById('synapticVesicles');
            impulse.classList.remove('hidden');
            impulse.classList.add('impulse-wave');
            status.innerHTML = "<span class='text-cyan-400 font-bold'>Action Potential Firing:</span> Electrical wave shoots along axon → triggers chemical exocytosis across synaptic cleft!";
            playTone(800, 'sine', 0.25);
            setTimeout(() => {{
                vesicles.classList.remove('hidden');
                playTone(1000, 'triangle', 0.15);
            }}, 600);
        }}

        // 3. Olfactory & Gustatory Receptors (Slide 2)
        let isNoseBlocked = false;
        function toggleNoseBlock() {{
            isNoseBlocked = !isNoseBlocked;
            const noseTag = document.getElementById('noseStateTag');
            const status = document.getElementById('receptorStatus');
            if (isNoseBlocked) {{
                noseTag.textContent = "Nose: Blocked (Cold)";
                noseTag.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40";
                status.innerHTML = "<span class='text-rose-400 font-bold'>Olfactory Blocked:</span> Only basic tongue tastes detected; rich food aromas are completely lost!";
                playTone(300, 'sawtooth', 0.15);
            }} else {{
                noseTag.textContent = "Nose: Open (Normal)";
                noseTag.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Sensory Integration:</span> Tongue taste + nasal olfaction combine to create full culinary flavour!";
                playTone(550, 'sine', 0.15);
            }}
        }}

        function testFoodTaste(type) {{
            const status = document.getElementById('receptorStatus');
            if (type === 'sugar') {{
                status.innerHTML = isNoseBlocked ? "<span class='text-amber-300 font-bold'>Sugar Eaten:</span> Still tastes sweet! Gustatory receptors on tongue detect dissolved sucrose directly." : "<span class='text-emerald-400 font-bold'>Sugar Eaten:</span> Sweet taste detected via tongue gustatory receptors.";
            }} else {{
                status.innerHTML = isNoseBlocked ? "<span class='text-rose-400 font-bold'>Curry Eaten (Nose Blocked):</span> Tastes bland and salty! Volatile spices cannot stimulate blocked olfactory receptors." : "<span class='text-emerald-400 font-bold'>Curry Eaten (Normal):</span> Delicious! Olfactory receptors detect airborne aromatics while tongue detects salt and spices!";
            }}
            playTone(650, 'sine', 0.15);
        }}

        // 4. Reflex Arc Simulator (Slide 3)
        function triggerReflexArc() {{
            const flameSpark = document.getElementById('flameSpark');
            const arm = document.getElementById('armMuscle');
            const status = document.getElementById('reflexStatus');
            flameSpark.classList.remove('hidden');
            arm.setAttribute('stroke', '#ef4444');
            arm.setAttribute('transform', 'rotate(-18 100 80)');
            status.innerHTML = "<span class='text-rose-400 font-bold'>Reflex Triggered:</span> Pain receptor → Sensory neuron → Spinal cord interneuron → Motor neuron → Bicep contracts! Hand pulled away in 0.2s before brain thinks!";
            playTone(880, 'sine', 0.3);
            setTimeout(() => {{
                arm.setAttribute('transform', 'rotate(0 100 80)');
                arm.setAttribute('stroke', '#10b981');
                flameSpark.classList.add('hidden');
            }}, 1500);
        }}

        // 5. Brain Anatomy Explorer (Slide 4)
        function highlightBrainPart(part) {{
            const fore = document.getElementById('foreBrainSvg');
            const mid = document.getElementById('midBrainSvg');
            const hind = document.getElementById('hindBrainSvg');
            const status = document.getElementById('brainAnatomyStatus');
            fore.setAttribute('opacity', '0.35');
            mid.setAttribute('opacity', '0.35');
            hind.setAttribute('opacity', '0.35');

            if (part === 'fore') {{
                fore.setAttribute('opacity', '1');
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Fore-Brain (Cerebrum):</span> Thinking, memory, sensory interpretation, voluntary motor commands, and hunger center.";
                playTone(600, 'sine', 0.15);
            }} else if (part === 'mid') {{
                mid.setAttribute('opacity', '1');
                status.innerHTML = "<span class='text-amber-300 font-bold'>Mid-Brain:</span> Coordinates visual and auditory reflexes, head-neck movements, and pupil diameter.";
                playTone(700, 'sine', 0.15);
            }} else if (part === 'hind') {{
                hind.setAttribute('opacity', '1');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Hind-Brain (Cerebellum, Medulla, Pons):</span> Posture, balance, and vital involuntary controls (BP, salivation, vomiting).";
                playTone(800, 'sine', 0.15);
            }}
        }}

        // 6. Fore-Brain Sensory Lobes & Satiety Meter (Slide 5)
        function activateSensoryLobe(lobe) {{
            const status = document.getElementById('forebrainStatus');
            if (lobe === 'visual') {{
                status.innerHTML = "<span class='text-blue-400 font-bold'>Visual Cortex Active:</span> Decodes photons and shapes from retinal photoreceptors.";
            }} else if (lobe === 'auditory') {{
                status.innerHTML = "<span class='text-purple-400 font-bold'>Auditory Cortex Active:</span> Interprets sound frequencies and language patterns.";
            }} else if (lobe === 'association') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Association Area Active:</span> Synthesizes incoming sensory signals with stored memories to make decisions!";
            }}
            playTone(640, 'triangle', 0.15);
        }}

        function adjustSatiety(val) {{
            const bar = document.getElementById('satietyBar');
            const status = document.getElementById('forebrainStatus');
            bar.style.width = val + '%';
            if (val > 80) {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Satiety Center Firing:</span> Sensation of fullness detected in fore-brain! Eating stopped.";
                playTone(750, 'sine', 0.12);
            }} else {{
                status.innerHTML = `<span class='text-amber-300 font-bold'>Hunger Level:</span> ${{100 - val}}% hungry. Fore-brain prompts food seeking.`;
            }}
        }}

        // 7. Hind-Brain Medulla & Cerebellum (Slide 6)
        function triggerInvoluntary(action) {{
            const status = document.getElementById('hindbrainStatus');
            if (action === 'salivation') {{
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Medulla Oblongata:</span> Scent of favorite food automatically sparks salivary secretion!";
                playTone(660, 'sine', 0.2);
            }} else if (action === 'bp') {{
                status.innerHTML = "<span class='text-rose-400 font-bold'>Medulla Oblongata:</span> Arteriolar diameter adjusted to maintain 120/80 mm Hg systemic blood pressure!";
                playTone(520, 'sine', 0.2);
            }} else if (action === 'balance') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Cerebellum:</span> Posture and equilibrium maintained! Walker strides steadily across the narrow line.";
                playTone(840, 'sine', 0.2);
            }}
        }}

        // 8. Protection & Muscle Contraction (Slide 7)
        function applyCraniumShock() {{
            const skull = document.getElementById('craniumBox');
            const csf = document.getElementById('csfFluid');
            const status = document.getElementById('protectionStatus');
            skull.classList.add('pulse-glow');
            csf.setAttribute('fill', '#0284c7');
            status.innerHTML = "<span class='text-sky-300 font-bold'>Mechanical Impact Absorbed:</span> Rigid cranium shields bone shock while cerebrospinal fluid balloon dampens hydraulic waves!";
            playTone(300, 'sine', 0.25);
            setTimeout(() => skull.classList.remove('pulse-glow'), 1000);
        }}

        let isMuscleContracted = false;
        function toggleMuscleSarcomere() {{
            isMuscleContracted = !isMuscleContracted;
            const filamentA = document.getElementById('actinFilamentA');
            const filamentB = document.getElementById('actinFilamentB');
            const status = document.getElementById('protectionStatus');
            if (isMuscleContracted) {{
                filamentA.setAttribute('x2', '140');
                filamentB.setAttribute('x1', '160');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Muscle Contraction:</span> Actin and myosin proteins change shape and slide past each other, shortening the muscle cell!";
                playTone(700, 'sine', 0.2);
            }} else {{
                filamentA.setAttribute('x2', '110');
                filamentB.setAttribute('x1', '190');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Muscle Relaxed:</span> Filament proteins return to extended resting length.";
                playTone(450, 'sine', 0.15);
            }}
        }}

        // 9. Mimosa Pudica Turgor Droop (Slide 8)
        let isMimosaDrooped = false;
        function touchMimosaLeaf() {{
            isMimosaDrooped = !isMimosaDrooped;
            const leafA = document.getElementById('mimosaLeafA');
            const leafB = document.getElementById('mimosaLeafB');
            const petiole = document.getElementById('mimosaPetiole');
            const status = document.getElementById('mimosaStatus');
            if (isMimosaDrooped) {{
                leafA.setAttribute('transform', 'rotate(40 60 70)');
                leafB.setAttribute('transform', 'rotate(-40 140 70)');
                petiole.setAttribute('d', 'M20,100 Q100,140 180,120');
                status.innerHTML = "<span class='text-rose-400 font-bold'>Touch Response (0.5s):</span> Electrochemical signal causes rapid water efflux from pulvini; cells shrink and leaves collapse!";
                playTone(420, 'sine', 0.25);
            }} else {{
                leafA.setAttribute('transform', 'rotate(0 60 70)');
                leafB.setAttribute('transform', 'rotate(0 140 70)');
                petiole.setAttribute('d', 'M20,100 Q100,60 180,60');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Turgor Restored:</span> Cells re-absorb water; leaflets unfold and stand upright!";
                playTone(680, 'sine', 0.2);
            }}
        }}

        // 10. Tendril Thigmotropism (Slide 9)
        let isTendrilCoiled = false;
        function toggleTendrilSupport() {{
            isTendrilCoiled = !isTendrilCoiled;
            const coil = document.getElementById('tendrilHelix');
            const status = document.getElementById('tendrilStatus');
            if (isTendrilCoiled) {{
                coil.setAttribute('d', 'M30,100 Q60,70 90,100 T120,100 T150,100 T180,80');
                coil.setAttribute('stroke', '#10b981');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Thigmotropic Coiling:</span> Contact side slows growth; outer side elongates rapidly under auxin, wrapping tendril tightly around fence!";
                playTone(740, 'triangle', 0.2);
            }} else {{
                coil.setAttribute('d', 'M30,100 Q90,95 180,95');
                coil.setAttribute('stroke', '#64748b');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Searching Tendril:</span> Growing straight forward in search of physical contact.";
                playTone(480, 'sine', 0.15);
            }}
        }}

        // 11. Phototropism Window Box (Slide 10)
        let isFlaskRotated = false;
        function toggleFlaskRotation() {{
            isFlaskRotated = !isFlaskRotated;
            const shoot = document.getElementById('phototropismShoot');
            const root = document.getElementById('phototropismRoot');
            const status = document.getElementById('photoBoxStatus');
            if (isFlaskRotated) {{
                shoot.setAttribute('d', 'M100,100 C100,70 140,50 170,40');
                root.setAttribute('d', 'M100,100 C100,130 60,150 40,160');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Flask Rotated 180°:</span> Newly growing shoot tip bends back toward window light! Roots curve away into dark.";
                playTone(800, 'sine', 0.25);
            }} else {{
                shoot.setAttribute('d', 'M100,100 C100,70 120,60 140,50');
                root.setAttribute('d', 'M100,100 C100,130 80,140 60,150');
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Initial Position:</span> Shoots show positive phototropism (bend toward light); roots show negative phototropism.";
                playTone(550, 'sine', 0.15);
            }}
        }}

        // 12. Multi-Tropism Lab (Slide 11)
        function triggerTropism(type) {{
            const status = document.getElementById('multiTropismStatus');
            const stem = document.getElementById('tropismStem');
            const root = document.getElementById('tropismRoot');

            if (type === 'geotropism') {{
                stem.setAttribute('d', 'M100,100 C120,100 130,60 140,40');
                root.setAttribute('d', 'M100,100 C80,100 70,140 60,160');
                status.innerHTML = "<span class='text-amber-300 font-bold'>Geotropism:</span> In horizontal pot, roots grow down (+ geotropic) while shoot curves up (- geotropic)!";
            }} else if (type === 'hydrotropism') {{
                stem.setAttribute('d', 'M100,100 C100,70 100,50 100,40');
                root.setAttribute('d', 'M100,100 C110,130 140,140 170,145');
                status.innerHTML = "<span class='text-sky-300 font-bold'>Hydrotropism:</span> Root curves laterally toward moisture-rich soil zone!";
            }} else if (type === 'chemotropism') {{
                stem.setAttribute('d', 'M100,100 C100,70 100,50 100,40');
                root.setAttribute('d', 'M100,100 C100,130 100,150 100,160');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Chemotropism:</span> Pollen tube grows down the style towards ovule attracted by chemical signals!";
            }}
            playTone(660, 'sine', 0.2);
        }}

        // 13. Auxin Diffusion Simulator (Slide 12)
        function setLightDirection(dir) {{
            const status = document.getElementById('auxinStatus');
            const stem = document.getElementById('auxinStem');
            const darkCells = document.getElementById('shadedCells');
            if (dir === 'unilateral') {{
                stem.setAttribute('d', 'M90,140 C90,80 120,60 150,45');
                darkCells.setAttribute('fill', '#10b981');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Unilateral Light:</span> Auxin migrates to shaded side → stimulates cell elongation on dark flank → stem bends to light!";
                playTone(780, 'sine', 0.25);
            }} else {{
                stem.setAttribute('d', 'M90,140 C90,80 90,60 90,40');
                darkCells.setAttribute('fill', '#334155');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Uniform Light:</span> Auxin distributed symmetrically down all sides → stem grows straight upward.";
                playTone(500, 'sine', 0.15);
            }}
        }}

        // 14. Plant Hormones Quartet (Slide 13)
        function applyPhytohormone(type) {{
            const plant = document.getElementById('hormonePlantShoot');
            const status = document.getElementById('phytoStatus');
            if (type === 'auxin') {{
                plant.setAttribute('d', 'M100,140 C100,90 120,70 140,50');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Auxin Applied:</span> Shoot tip cells elongate; induces phototropic curvature!";
            }} else if (type === 'gibberellin') {{
                plant.setAttribute('d', 'M100,140 L100,30');
                status.innerHTML = "<span class='text-amber-300 font-bold'>Gibberellin Applied:</span> Rapid internodal elongation! Dwarf stem stretches 3x taller.";
            }} else if (type === 'cytokinin') {{
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Cytokinin Applied:</span> Rapid cell division (cytokinesis) stimulated in developing seeds and fruits!";
            }} else if (type === 'aba') {{
                plant.setAttribute('d', 'M100,140 Q100,110 90,100');
                status.innerHTML = "<span class='text-rose-400 font-bold'>Abscisic Acid (ABA) Applied:</span> Growth inhibited! Stomata snap shut, leaves wilt and droop.";
            }}
            playTone(720, 'sine', 0.2);
        }}

        // 15. Adrenaline Fight or Flight (Slide 14)
        let isAdrenalineActive = false;
        function toggleAdrenaline() {{
            isAdrenalineActive = !isAdrenalineActive;
            const heartRate = document.getElementById('heartRateDisplay');
            const status = document.getElementById('adrenalineStatus');
            if (isAdrenalineActive) {{
                heartRate.textContent = "165 BPM (Tachycardia)";
                heartRate.className = "text-sm font-mono font-bold text-rose-400";
                status.innerHTML = "<span class='text-rose-400 font-bold'>Adrenaline Surge!</span> Heart pumps faster, breathing surges, blood diverted from gut to leg skeletal muscles for fight/flight!";
                playTone(880, 'sine', 0.25);
            }} else {{
                heartRate.textContent = "72 BPM (Resting)";
                heartRate.className = "text-sm font-mono font-bold text-emerald-400";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Rest & Digest:</span> Baseline homeostasis restored. Normal blood distribution to visceral organs.";
                playTone(440, 'sine', 0.15);
            }}
        }}

        // 16. Endocrine Glands Explorer (Slide 15)
        function selectGland(gland) {{
            const status = document.getElementById('endocrineStatus');
            if (gland === 'pituitary') {{
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Pituitary Gland (Master):</span> Secretes Growth Hormone. Deficiency causes Dwarfism; excess causes Gigantism.";
            }} else if (gland === 'thyroid') {{
                status.innerHTML = "<span class='text-amber-300 font-bold'>Thyroid Gland:</span> Secretes Thyroxin for carbohydrate/fat metabolism. Dietary iodine deficiency causes Goitre (swollen neck).";
            }} else if (gland === 'pancreas') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Pancreas (Islets):</span> Secretes Insulin to lower blood glucose. Deficiency causes Diabetes Mellitus.";
            }} else if (gland === 'adrenal') {{
                status.innerHTML = "<span class='text-rose-400 font-bold'>Adrenal Glands:</span> Secrete Adrenaline for emergency fight-or-flight energy surges.";
            }} else if (gland === 'gonads') {{
                status.innerHTML = "<span class='text-purple-400 font-bold'>Gonads (Testes/Ovaries):</span> Secrete Testosterone (males) and Oestrogen (females) governing puberty and reproduction.";
            }}
            playTone(680, 'sine', 0.15);
        }}

        // 17. Pancreatic Feedback Loop (Slide 16)
        let bloodSugar = 90;
        function ingestCarbMeal() {{
            bloodSugar = 165;
            updateFeedbackDisplay();
            playTone(450, 'sine', 0.2);
            setTimeout(() => {{
                bloodSugar = 92;
                updateFeedbackDisplay();
                playTone(650, 'sine', 0.2);
            }}, 2000);
        }}

        function updateFeedbackDisplay() {{
            const val = document.getElementById('glucoseValue');
            const status = document.getElementById('feedbackStatus');
            val.textContent = `${{bloodSugar}} mg/dL`;
            if (bloodSugar > 120) {{
                val.className = "text-sm font-mono font-bold text-rose-400";
                status.innerHTML = "<span class='text-rose-400 font-bold'>High Blood Glucose:</span> Pancreatic beta cells sense spike → secrete INSULIN to store glucose as glycogen in liver!";
            }} else {{
                val.className = "text-sm font-mono font-bold text-emerald-400";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Negative Feedback Activated:</span> Glucose normalized to ~90 mg/dL → stimulus removed → insulin secretion shut down!";
            }}
        }}

        // Gesture unlock for audio
        let audioUnlocked = false;
        function unlockAudio() {{
            if (audioUnlocked) return;
            audioUnlocked = true;
            try {{
                const ctx = getAudioContext();
                if (ctx && ctx.state === 'suspended') {{
                    ctx.resume();
                }}
            }} catch (e) {{}}
            if (voiceActive && synth && !synth.speaking) {{
                replayVoice();
            }}
        }}
        document.addEventListener('click', unlockAudio, {{ once: true }});
        document.addEventListener('touchstart', unlockAudio, {{ once: true }});
        document.addEventListener('keydown', unlockAudio, {{ once: true }});

        window.addEventListener('DOMContentLoaded', () => {{
            goToSlide(0);
        }});
    </script>
</body>
</html>
"""
    return full_html

def get_simulator_markup(idx, sim_type):
    sims = {
        0: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Movement Comparison Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Growth vs Non-Growth</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 160" class="w-full h-full">
                        <line x1="10" y1="90" x2="190" y2="90" stroke="#78350f" stroke-width="3" stroke-dasharray="4"/>
                        <rect x="10" y="90" width="180" height="60" fill="#451a03" opacity="0.3"/>
                        <text x="15" y="110" fill="#a16207" font-size="9" font-family="monospace">SOIL</text>
                        <circle cx="60" cy="90" r="7" fill="#78350f"/>
                        <line id="seedlingShoot" x1="60" y1="90" x2="60" y2="65" stroke="#10b981" stroke-width="2" stroke-linecap="round"/>
                        <line id="seedlingRoot" x1="60" y1="90" x2="60" y2="105" stroke="#ca8a04" stroke-width="2" stroke-linecap="round"/>
                        <g id="catRunner" transform="translate(130, 70)">
                            <ellipse cx="15" cy="10" rx="14" ry="7" fill="#f59e0b"/>
                            <circle cx="28" cy="6" r="5" fill="#f59e0b"/>
                            <line x1="5" y1="12" x2="0" y2="18" stroke="#f59e0b" stroke-width="2"/>
                            <line x1="22" y1="12" x2="26" y2="18" stroke="#f59e0b" stroke-width="2"/>
                        </g>
                    </svg>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="toggleSeedGrowth()" class="px-2.5 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-semibold transition cursor-pointer">
                        🌱 Sprout Seedling
                    </button>
                    <button onclick="simulateCatSprint()" class="px-2.5 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-300 text-xs font-semibold transition cursor-pointer">
                        🐈 Cat Sprint
                    </button>
                </div>
                <div id="movementSimStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Click buttons above to compare growth-dependent seedling movement with growth-independent muscular sprint!
                </div>
            </div>
        """,
        1: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Neuron Action Potential Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 6.1 (a & b)</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 240 160" class="w-full h-full">
                        <circle cx="45" cy="80" r="16" fill="#3b82f6" opacity="0.6"/>
                        <circle cx="45" cy="80" r="6" fill="#1d4ed8"/>
                        <path d="M45,64 L30,45 M45,64 L55,40 M30,80 L15,80 M45,96 L30,115" stroke="#60a5fa" stroke-width="2"/>
                        <line x1="61" y1="80" x2="160" y2="80" stroke="#93c5fd" stroke-width="4"/>
                        <rect x="75" y="73" width="20" height="14" rx="3" fill="#fbbf24"/>
                        <rect x="105" y="73" width="20" height="14" rx="3" fill="#fbbf24"/>
                        <rect x="135" y="73" width="20" height="14" rx="3" fill="#fbbf24"/>
                        <circle id="impulseDot" cx="160" cy="80" r="5" fill="#f43f5e" class="hidden"/>
                        <path d="M165,80 L180,70 M165,80 L180,90" stroke="#93c5fd" stroke-width="2"/>
                        <rect x="195" y="55" width="30" height="50" rx="4" fill="#be123c" opacity="0.5"/>
                        <g id="synapticVesicles" class="hidden">
                            <circle cx="185" cy="75" r="2" fill="#38bdf8"/>
                            <circle cx="188" cy="80" r="2" fill="#38bdf8"/>
                            <circle cx="185" cy="85" r="2" fill="#38bdf8"/>
                        </g>
                    </svg>
                </div>
                <button onclick="fireActionPotential()" class="w-full py-2 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-300 text-xs font-bold transition cursor-pointer">
                    ⚡ Fire Nerve Impulse Across Synapse
                </button>
                <div id="neuronStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Dendrites acquire signal → Cyton generates electrical impulse → Axon propagates wave → Synapse releases chemicals!
                </div>
            </div>
        """,
        2: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Taste & Smell Lab (Activity 6.1)</span>
                    <span id="noseStateTag" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Nose: Open</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 160" class="w-full h-full">
                        <path d="M70,20 C120,20 140,50 140,75 C140,85 130,95 145,105 C140,110 130,110 125,125 C120,140 100,150 70,150" fill="none" stroke="#64748b" stroke-width="2"/>
                        <path d="M100,115 Q120,115 130,112" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
                        <text x="75" y="125" fill="#f43f5e" font-size="8">Taste Buds</text>
                        <path d="M110,85 Q125,85 135,92" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <circle cx="105" cy="80" r="5" fill="#38bdf8"/>
                        <text x="65" y="80" fill="#38bdf8" font-size="8">Olfactory</text>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="toggleNoseBlock()" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition cursor-pointer">
                        👃 Pinch Nose
                    </button>
                    <button onclick="testFoodTaste('sugar')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40 transition cursor-pointer">
                        🍬 Sugar
                    </button>
                    <button onclick="testFoodTaste('curry')" class="px-2 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 text-xs font-semibold border border-rose-500/40 transition cursor-pointer">
                        🍲 Curry
                    </button>
                </div>
                <div id="receptorStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test how sugar vs seasoned curry tastes with nose open vs blocked!
                </div>
            </div>
        """,
        3: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Reflex Arc Circuit (Fig 6.2)</span>
                    <span class="text-[10px] font-mono text-slate-400">Spinal Shortcut</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 160" class="w-full h-full">
                        <rect x="20" y="115" width="14" height="30" fill="#f8fafc"/>
                        <path d="M27,115 Q22,100 27,90 Q32,100 27,115" fill="#f59e0b"/>
                        <circle id="flameSpark" cx="27" cy="90" r="6" fill="#ef4444" class="hidden pulse-glow"/>
                        <line id="armMuscle" x1="45" y1="95" x2="110" y2="80" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                        <rect x="150" y="40" width="50" height="80" rx="10" fill="#1e293b" stroke="#475569"/>
                        <path d="M165,65 Q175,80 165,95 M185,65 Q175,80 185,95" stroke="#f43f5e" stroke-width="2"/>
                        <path d="M50,95 Q100,50 165,65" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
                        <path d="M165,95 Q100,110 80,85" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3"/>
                    </svg>
                </div>
                <button onclick="triggerReflexArc()" class="w-full py-2 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition cursor-pointer">
                    🔥 Touch Flame! (Test 0.2s Spinal Reflex)
                </button>
                <div id="reflexStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Click flame to trigger instant spinal reflex withdrawal before brain processing!
                </div>
            </div>
        """,
        4: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Human Brain Anatomy (Fig 6.3)</span>
                    <span class="text-[10px] font-mono text-slate-400">3 Master Regions</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 160" class="w-full h-full">
                        <path d="M40,110 C30,50 80,25 140,25 C190,25 200,60 195,110" fill="none" stroke="#64748b" stroke-width="4"/>
                        <path id="foreBrainSvg" d="M50,105 C40,55 90,35 140,35 C185,35 185,70 170,100 C150,90 120,110 50,105 Z" fill="#38bdf8" opacity="0.8"/>
                        <circle id="midBrainSvg" cx="130" cy="95" r="9" fill="#fbbf24" opacity="0.8"/>
                        <g id="hindBrainSvg" opacity="0.8">
                            <ellipse cx="75" cy="115" rx="18" ry="12" fill="#10b981"/>
                            <rect x="120" y="105" width="16" height="35" rx="4" fill="#059669"/>
                        </g>
                        <line x1="128" y1="140" x2="128" y2="160" stroke="#f43f5e" stroke-width="4"/>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="highlightBrainPart('fore')" class="px-2 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-300 text-xs font-semibold border border-cyan-500/40 transition cursor-pointer">
                        Fore-Brain
                    </button>
                    <button onclick="highlightBrainPart('mid')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40 transition cursor-pointer">
                        Mid-Brain
                    </button>
                    <button onclick="highlightBrainPart('hind')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40 transition cursor-pointer">
                        Hind-Brain
                    </button>
                </div>
                <div id="brainAnatomyStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Click regions above to inspect the functional specializations of the Fore-, Mid-, and Hind-brain!
                </div>
            </div>
        """,
        5: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Fore-Brain Senses & Satiety</span>
                    <span class="text-[10px] font-mono text-slate-400">Cerebral Cortex</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                    <div class="flex justify-between text-xs text-slate-300">
                        <span>Meal Satiety Meter:</span>
                        <span id="satietyPercent">Eat to Fill</span>
                    </div>
                    <div class="w-full bg-slate-800 rounded-full h-3 overflow-hidden">
                        <div id="satietyBar" class="bg-gradient-to-r from-amber-500 to-emerald-500 h-full w-1/4 transition-all duration-300"></div>
                    </div>
                    <input type="range" min="0" max="100" value="25" oninput="adjustSatiety(this.value)" class="w-full accent-emerald-500 cursor-pointer">
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="activateSensoryLobe('visual')" class="px-2 py-1.5 rounded-lg bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 text-xs font-semibold border border-blue-500/40 transition cursor-pointer">
                        👁️ Vision
                    </button>
                    <button onclick="activateSensoryLobe('auditory')" class="px-2 py-1.5 rounded-lg bg-purple-600/30 hover:bg-purple-600/50 text-purple-300 text-xs font-semibold border border-purple-500/40 transition cursor-pointer">
                        👂 Hearing
                    </button>
                    <button onclick="activateSensoryLobe('association')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40 transition cursor-pointer">
                        🧠 Think
                    </button>
                </div>
                <div id="forebrainStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Drag the satiety meter to observe when your fore-brain signals that you have eaten enough!
                </div>
            </div>
        """,
        6: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Hind-Brain Vital Centers</span>
                    <span class="text-[10px] font-mono text-slate-400">Medulla & Cerebellum</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 140" class="w-full h-full">
                        <line x1="20" y1="110" x2="180" y2="110" stroke="#475569" stroke-width="3"/>
                        <circle cx="100" cy="55" r="8" fill="#10b981"/>
                        <line x1="100" y1="63" x2="100" y2="95" stroke="#10b981" stroke-width="4"/>
                        <line x1="60" y1="75" x2="140" y2="75" stroke="#fbbf24" stroke-width="3"/>
                        <line x1="100" y1="95" x2="95" y2="110" stroke="#10b981" stroke-width="3"/>
                        <line x1="100" y1="95" x2="105" y2="110" stroke="#10b981" stroke-width="3"/>
                        <text x="50" y="130" fill="#94a3b8" font-size="9">Cerebellum Balance Path</text>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="triggerInvoluntary('salivation')" class="px-2 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-300 text-xs font-semibold border border-cyan-500/40 transition cursor-pointer">
                        🤤 Salivate
                    </button>
                    <button onclick="triggerInvoluntary('bp')" class="px-2 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 text-xs font-semibold border border-rose-500/40 transition cursor-pointer">
                        ❤️ Pulse / BP
                    </button>
                    <button onclick="triggerInvoluntary('balance')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40 transition cursor-pointer">
                        ⚖️ Balance
                    </button>
                </div>
                <div id="hindbrainStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test how the medulla governs automatic visceral reflexes while the cerebellum balances voluntary movement!
                </div>
            </div>
        """,
        7: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Protection & Muscle Action</span>
                    <span class="text-[10px] font-mono text-slate-400">CSF & Actin-Myosin</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 140" class="w-full h-full">
                        <path id="craniumBox" d="M30,70 C30,20 190,20 190,70" fill="none" stroke="#e2e8f0" stroke-width="5"/>
                        <path id="csfFluid" d="M35,68 C35,28 185,28 185,68" fill="#38bdf8" opacity="0.3"/>
                        <line x1="20" y1="105" x2="20" y2="135" stroke="#f43f5e" stroke-width="4"/>
                        <line x1="200" y1="105" x2="200" y2="135" stroke="#f43f5e" stroke-width="4"/>
                        <line id="actinFilamentA" x1="20" y1="115" x2="110" y2="115" stroke="#38bdf8" stroke-width="3"/>
                        <line id="actinFilamentB" x1="200" y1="125" x2="110" y2="125" stroke="#38bdf8" stroke-width="3"/>
                    </svg>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="applyCraniumShock()" class="px-2.5 py-1.5 rounded-lg bg-sky-600/30 hover:bg-sky-600/50 border border-sky-500/40 text-sky-300 text-xs font-semibold transition cursor-pointer">
                        🛡️ Test CSF Shock Absorption
                    </button>
                    <button onclick="toggleMuscleSarcomere()" class="px-2.5 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-semibold transition cursor-pointer">
                        💪 Slide Muscle Filaments
                    </button>
                </div>
                <div id="protectionStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test how CSF cushions impacts and how actin-myosin proteins shorten muscle cells!
                </div>
            </div>
        """,
        8: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Mimosa Pudica Touch Lab (Fig 6.4)</span>
                    <span class="text-[10px] font-mono text-slate-400">Chhui-mui Turgor</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <line x1="20" y1="140" x2="20" y2="60" stroke="#15803d" stroke-width="4"/>
                        <circle cx="20" cy="100" r="7" fill="#84cc16"/>
                        <path id="mimosaPetiole" d="M20,100 Q100,60 180,60" fill="none" stroke="#16a34a" stroke-width="3"/>
                        <g id="mimosaLeafA">
                            <ellipse cx="90" cy="50" rx="14" ry="6" fill="#22c55e" stroke="#15803d"/>
                            <ellipse cx="120" cy="50" rx="14" ry="6" fill="#22c55e" stroke="#15803d"/>
                        </g>
                        <g id="mimosaLeafB">
                            <ellipse cx="150" cy="50" rx="14" ry="6" fill="#22c55e" stroke="#15803d"/>
                            <ellipse cx="180" cy="50" rx="14" ry="6" fill="#22c55e" stroke="#15803d"/>
                        </g>
                    </svg>
                </div>
                <button onclick="touchMimosaLeaf()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    👆 Touch Leaf Tip! (Simulate Turgor Collapse)
                </button>
                <div id="mimosaStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Touch the sensitive plant to watch water evacuate pulvinar cells, causing instantaneous drooping!
                </div>
            </div>
        """,
        9: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Tendril Thigmotropism</span>
                    <span class="text-[10px] font-mono text-slate-400">Tactile Coiling</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 150" class="w-full h-full">
                        <rect x="140" y="20" width="12" height="120" rx="2" fill="#d97706" stroke="#b45309"/>
                        <text x="135" y="15" fill="#f59e0b" font-size="8">Fence Stake</text>
                        <path d="M20,130 Q30,100 30,70" fill="none" stroke="#15803d" stroke-width="4"/>
                        <path id="tendrilHelix" d="M30,100 Q90,95 180,95" fill="none" stroke="#64748b" stroke-width="3" stroke-linecap="round"/>
                    </svg>
                </div>
                <button onclick="toggleTendrilSupport()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    🪵 Contact Support (Watch Differential Coiling)
                </button>
                <div id="tendrilStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Contact inhibits inner cell growth while outer flank accelerates under auxin, forcing a tight spiral anchor!
                </div>
            </div>
        """,
        10: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Phototropism Light Box (Activity 6.2)</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 6.5</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 160" class="w-full h-full">
                        <rect x="20" y="20" width="150" height="130" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                        <line x1="170" y1="30" x2="170" y2="130" stroke="#f59e0b" stroke-width="4"/>
                        <text x="175" y="80" fill="#f59e0b" font-size="9">Light</text>
                        <path d="M85,130 L115,130 L105,95 L95,95 Z" fill="#38bdf8" opacity="0.4" stroke="#0284c7"/>
                        <path id="phototropismShoot" d="M100,100 C100,70 120,60 140,50" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round"/>
                        <path id="phototropismRoot" d="M100,100 C100,130 80,140 60,150" fill="none" stroke="#d97706" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                <button onclick="toggleFlaskRotation()" class="w-full py-2 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-300 text-xs font-bold transition cursor-pointer">
                    🔄 Rotate Flask 180° Away From Window Light
                </button>
                <div id="photoBoxStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Rotate the flask to verify how newly growing shoot tips adjust direction and bend right back to the light!
                </div>
            </div>
        """,
        11: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Environmental Tropisms</span>
                    <span class="text-[10px] font-mono text-slate-400">Geo / Hydro / Chemo</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 160" class="w-full h-full">
                        <line x1="20" y1="100" x2="180" y2="100" stroke="#334155" stroke-dasharray="2"/>
                        <path id="tropismStem" d="M100,100 C100,70 100,50 100,40" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                        <path id="tropismRoot" d="M100,100 C100,130 100,150 100,160" fill="none" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
                        <circle cx="100" cy="100" r="5" fill="#475569"/>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="triggerTropism('geotropism')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40 transition cursor-pointer">
                        🌍 Gravity
                    </button>
                    <button onclick="triggerTropism('hydrotropism')" class="px-2 py-1.5 rounded-lg bg-sky-600/30 hover:bg-sky-600/50 text-sky-300 text-xs font-semibold border border-sky-500/40 transition cursor-pointer">
                        💧 Water
                    </button>
                    <button onclick="triggerTropism('chemotropism')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40 transition cursor-pointer">
                        🧪 Chemical
                    </button>
                </div>
                <div id="multiTropismStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test geotropism in tilted pots, hydrotropism toward moisture, and chemotropism of pollen tubes!
                </div>
            </div>
        """,
        12: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Auxin Diffusion Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Cell Elongation</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 160" class="w-full h-full">
                        <path id="auxinStem" d="M90,140 C90,80 90,60 90,40" fill="none" stroke="#22c55e" stroke-width="12" stroke-linecap="round"/>
                        <rect id="shadedCells" x="75" y="60" width="10" height="40" rx="2" fill="#334155"/>
                        <circle cx="170" cy="40" r="12" fill="#fbbf24"/>
                        <line x1="150" y1="40" x2="110" y2="40" stroke="#f59e0b" stroke-dasharray="2"/>
                    </svg>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="setLightDirection('overhead')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition cursor-pointer">
                        ☀️ Overhead Uniform Light
                    </button>
                    <button onclick="setLightDirection('unilateral')" class="px-2.5 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-semibold transition cursor-pointer">
                        🌅 Unilateral Angle Light
                    </button>
                </div>
                <div id="auxinStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Unilateral light forces auxin to diffuse to the shaded side, stimulating elongation that curves the stem!
                </div>
            </div>
        """,
        13: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Phytohormones Matrix</span>
                    <span class="text-[10px] font-mono text-slate-400">Growth vs Inhibition</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 160" class="w-full h-full">
                        <line x1="20" y1="140" x2="180" y2="140" stroke="#334155"/>
                        <path id="hormonePlantShoot" d="M100,140 L100,80" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                        <circle cx="100" cy="80" r="6" fill="#10b981"/>
                    </svg>
                </div>
                <div class="grid grid-cols-2 gap-1.5">
                    <button onclick="applyPhytohormone('auxin')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40 transition cursor-pointer">
                        Auxin (Elongate)
                    </button>
                    <button onclick="applyPhytohormone('gibberellin')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40 transition cursor-pointer">
                        Gibberellin (Stem)
                    </button>
                    <button onclick="applyPhytohormone('cytokinin')" class="px-2 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-300 text-xs font-semibold border border-cyan-500/40 transition cursor-pointer">
                        Cytokinin (Divide)
                    </button>
                    <button onclick="applyPhytohormone('aba')" class="px-2 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 text-xs font-semibold border border-rose-500/40 transition cursor-pointer">
                        ABA (Inhibit/Wilt)
                    </button>
                </div>
                <div id="phytoStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test the 4 plant hormones to observe stem stretching, cell division, or leaf wilting!
                </div>
            </div>
        """,
        14: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Adrenaline Fight or Flight</span>
                    <span id="heartRateDisplay" class="text-xs font-mono font-bold text-emerald-400">72 BPM (Resting)</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <ellipse cx="65" cy="80" rx="14" ry="22" fill="#831843"/>
                        <ellipse cx="135" cy="80" rx="14" ry="22" fill="#831843"/>
                        <polygon points="55,60 65,48 75,60" fill="#f43f5e" class="pulse-glow"/>
                        <polygon points="125,60 135,48 145,60" fill="#f43f5e" class="pulse-glow"/>
                        <text x="50" y="40" fill="#f43f5e" font-size="8">Adrenal Gland</text>
                        <path d="M100,30 L100,130" stroke="#ef4444" stroke-width="4"/>
                    </svg>
                </div>
                <button onclick="toggleAdrenaline()" class="w-full py-2 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition cursor-pointer">
                    ⚠️ Trigger Predator Threat (Adrenaline Surge)
                </button>
                <div id="adrenalineStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Watch adrenaline accelerate heart rate, dilate airways, and shunt blood directly to skeletal muscles!
                </div>
            </div>
        """,
        15: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Endocrine Glands Body Map</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 6.7</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 160 160" class="w-full h-full">
                        <path d="M80,20 C85,20 90,25 90,32 C90,40 85,45 80,45 C75,45 70,40 70,32 C70,25 75,20 80,20 Z" fill="#475569"/>
                        <path d="M60,50 L100,50 L110,95 L95,145 L85,145 L85,100 L75,100 L75,145 L65,145 L50,95 Z" fill="#334155"/>
                        <circle cx="80" cy="30" r="4" fill="#38bdf8"/>
                        <circle cx="80" cy="50" r="5" fill="#f59e0b"/>
                        <circle cx="80" cy="80" r="5" fill="#10b981"/>
                        <circle cx="75" cy="90" r="4" fill="#f43f5e"/>
                        <circle cx="85" cy="90" r="4" fill="#f43f5e"/>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1">
                    <button onclick="selectGland('pituitary')" class="px-1.5 py-1 rounded bg-cyan-600/30 text-cyan-300 text-[11px] font-semibold border border-cyan-500/40">Pituitary</button>
                    <button onclick="selectGland('thyroid')" class="px-1.5 py-1 rounded bg-amber-600/30 text-amber-300 text-[11px] font-semibold border border-amber-500/40">Thyroid</button>
                    <button onclick="selectGland('pancreas')" class="px-1.5 py-1 rounded bg-emerald-600/30 text-emerald-300 text-[11px] font-semibold border border-emerald-500/40">Pancreas</button>
                    <button onclick="selectGland('adrenal')" class="px-1.5 py-1 rounded bg-rose-600/30 text-rose-300 text-[11px] font-semibold border border-rose-500/40">Adrenal</button>
                    <button onclick="selectGland('gonads')" class="px-1.5 py-1 rounded bg-purple-600/30 text-purple-300 text-[11px] font-semibold border border-purple-500/40">Gonads</button>
                </div>
                <div id="endocrineStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Click glands to examine target organs, functions, and clinical deficiency disorders (Goitre, Dwarfism, Diabetes).
                </div>
            </div>
        """,
        16: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Blood Sugar Feedback Loop</span>
                    <span id="glucoseValue" class="text-xs font-mono font-bold text-emerald-400">90 mg/dL (Normal)</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <path d="M100,25 C150,25 170,75 170,100 C170,135 100,135 50,135 C30,100 50,25 100,25" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="4"/>
                        <rect x="80" y="15" width="40" height="20" rx="5" fill="#f59e0b"/>
                        <text x="85" y="28" fill="#1e293b" font-size="8" font-weight="bold">Pancreas</text>
                        <rect x="75" y="125" width="50" height="20" rx="5" fill="#3b82f6"/>
                        <text x="85" y="138" fill="#ffffff" font-size="8" font-weight="bold">Liver/Cells</text>
                    </svg>
                </div>
                <button onclick="ingestCarbMeal()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    🍰 Eat Sweet Meal (Watch Insulin Negative Feedback)
                </button>
                <div id="feedbackStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Eat a meal to watch blood sugar rise → Pancreas secrete insulin → Glycogen stored → Feedback loop shuts off insulin!
                </div>
            </div>
        """
    }
    return sims.get(idx, "<div class='text-slate-400 text-xs'>Interactive Simulator</div>")

if __name__ == '__main__':
    html_out = generate_html()
    out_path = 'public/animations/control-and-coordination.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f"Successfully generated {out_path} ({len(html_out)} bytes)")

