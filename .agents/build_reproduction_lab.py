#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 7: How do Organisms Reproduce?
Master Interactive Multimedia Lab
File: public/animations/how-do-organisms-reproduce.html
"""

import json
import os
import sys

# Add .agents to sys.path
sys.path.append(os.path.abspath('.agents'))
from reproduction_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def generate_html():
    print("Generating public/animations/how-do-organisms-reproduce.html...")

    slides_html_list = []

    for s_idx, slide in enumerate(ALL_SLIDES):
        is_quiz = (s_idx >= 17)
        slide_num = s_idx + 1
        total_slides = len(ALL_SLIDES)

        if not is_quiz:
            theory_blocks_html = ""
            for tb in slide["theory_blocks"]:
                theory_blocks_html += f"""
                <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-4 hover:border-slate-700 transition">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-rose-400 mb-1.5 flex items-center gap-1.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                        {tb['heading']}
                    </h4>
                    <div class="text-xs sm:text-sm text-slate-300 leading-relaxed space-y-1.5">
                        {tb['content']}
                    </div>
                </div>
            """

            checkpoints_html = ""
            for q_idx, cp in enumerate(slide["checkpoints"]):
                options_html = ""
                for o_idx, opt in enumerate(cp["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="chk-{s_idx}-{q_idx}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_idx}, {o_idx}, {cp['ans']}, 'chk-sol-{s_idx}-{q_idx}')" class="mt-0.5 text-rose-600 focus:ring-rose-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                cp_q_esc = cp['q'].replace("'", "\\'").replace('"', '&quot;')
                cp_sol_esc = cp['solution'].replace("'", "\\'").replace('"', '&quot;')

                checkpoints_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 mb-3">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Checkpoint {q_idx + 1} of 2</span>
                        <div class="flex items-center gap-2">
                            <div id="feedback-{s_idx}-{q_idx}"></div>
                            <button onclick="openQuizSolution('Slide {s_idx + 1} Checkpoint {q_idx + 1}', '{cp_q_esc}', '{cp_sol_esc}')" class="px-2.5 py-1 rounded-md bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Solution</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-2.5">{cp['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        {options_html}
                    </div>
                    <div id="chk-sol-{s_idx}-{q_idx}" class="hidden mt-2.5 p-3 rounded-lg bg-rose-950/30 border border-rose-500/30 text-xs text-slate-200">
                        <span class="font-bold text-rose-400">Step-by-Step Teacher Explanation:</span><br>
                        {cp['solution']}
                    </div>
                </div>
            """

            teacher_card_html = f"""
            <!-- Person Talking: Dr. Sophia Biology Teacher Avatar -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-rose-950/40 via-slate-900 to-rose-950/20 border border-rose-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#e11d48" stroke="#f43f5e" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <circle cx="60" cy="50" r="26" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
                        <path d="M34 50 C34 25, 86 25, 86 50 C86 35, 75 22, 60 22 C45 22, 34 35, 34 50 Z" fill="#4c1d95"/>
                        <circle cx="50" cy="48" r="7" fill="none" stroke="#be123c" stroke-width="2"/>
                        <circle cx="70" cy="48" r="7" fill="none" stroke="#be123c" stroke-width="2"/>
                        <line x1="57" y1="48" x2="63" y2="48" stroke="#be123c" stroke-width="2"/>
                        <circle cx="50" cy="48" r="2.5" fill="#1e293b"/>
                        <circle cx="70" cy="48" r="2.5" fill="#1e293b"/>
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-rose-500/20 text-rose-300 border border-rose-500/30 mt-1">
                        Dr. Sophia • Biology Teacher
                    </span>
                </div>

                <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                    <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-bold text-rose-400 flex items-center gap-1.5">
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

            simulator_html = get_simulator_markup(s_idx, slide["interactive_type"])

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl relative overflow-hidden">
                    <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-rose-500/10 to-transparent pointer-events-none"></div>
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/40">
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

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mb-6">
                    <div class="lg:col-span-7 space-y-4">
                        <div class="space-y-3">
                            {theory_blocks_html}
                        </div>
                        <div class="pt-2">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-3 flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                                Slide Checkpoint Questions & Step-by-Step Solutions
                            </h3>
                            {checkpoints_html}
                        </div>
                    </div>

                    <div class="lg:col-span-5">
                        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 sticky top-20 shadow-xl">
                            {simulator_html}
                        </div>
                    </div>
                </div>
            </div>
            """
        else:
            questions_html = ""
            for q in slide["questions"]:
                q_id = q["id"]
                options_html = ""
                for o_idx, opt in enumerate(q["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="quiz-{s_idx}-{q_id}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_id}, {o_idx}, {q['ans']}, 'quiz-feedback-{q_id}')" class="mt-0.5 text-rose-600 focus:ring-rose-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                q_title_esc = q['q'].replace("'", "\\'").replace('"', '&quot;')
                q_sol_esc = q['solution'].replace("'", "\\'").replace('"', '&quot;')

                questions_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Question {q_id}</span>
                        <div class="flex items-center gap-2">
                            <div id="quiz-feedback-{q_id}"></div>
                            <button onclick="openQuizSolution({q_id}, '{q_title_esc}', '{q_sol_esc}')" class="px-2.5 py-1 rounded-md bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
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

            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-rose-950/40 border border-rose-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-rose-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 7: How do Organisms Reproduce?)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 17 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl">
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/40">
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
        <button id="pill-{s_idx}" onclick="goToSlide({s_idx})" class="px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all {'bg-rose-600 text-white font-bold' if s_idx == 0 else 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
            {short}
        </button>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 7: How do Organisms Reproduce? Master Lab</title>
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
            from {{ filter: drop-shadow(0 0 2px rgba(244, 63, 94, 0.4)); }}
            to {{ filter: drop-shadow(0 0 10px rgba(244, 63, 94, 0.8)); }}
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-rose-500 selection:text-white">

    <!-- Top Navigation Bar -->
    <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md px-4 py-2.5 sm:px-6">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-gradient-to-tr from-rose-600 to-pink-500 flex items-center justify-center font-extrabold text-white text-sm shadow-lg shadow-rose-500/20">
                    7
                </span>
                <div>
                    <h1 class="text-xs sm:text-sm font-bold text-white tracking-wide">
                        How do Organisms Reproduce?
                    </h1>
                    <p class="text-[10px] text-rose-400 font-mono">
                        NCERT Class 10 Science • Chapter 7 • Master Multimedia Lab
                    </p>
                </div>
            </div>

            <div class="flex items-center gap-2 sm:gap-4">
                <button id="voiceToggleBtn" onclick="toggleVoiceNarration()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-rose-600/20 text-rose-300 hover:bg-rose-600/30 border border-rose-500/40 text-xs font-semibold transition cursor-pointer" title="Toggle Teacher Voice">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"/></svg>
                    <span id="voiceStatusText">Teacher Voice: Active</span>
                </button>
                <button onclick="replayVoice()" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700 border border-slate-700 transition cursor-pointer" title="Replay Voice">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                </button>
                <div class="text-xs font-mono text-slate-400 border-l border-slate-700 pl-3">
                    <span id="currentSlideIndicator" class="text-rose-400 font-bold text-sm">1</span> / 21
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 md:p-8 flex flex-col justify-start">
        {''.join(slides_html_list)}
    </main>

    <!-- Bottom Navigation Footer & Topic Pills -->
    <footer class="bg-slate-900 border-t border-slate-800 sticky bottom-0 z-30 px-4 py-3 sm:px-6 shadow-2xl">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 disabled:opacity-40 disabled:cursor-not-allowed border border-slate-700 cursor-pointer">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    <span>Previous</span>
                </button>
                <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-rose-600 to-pink-500 hover:from-rose-500 hover:to-pink-400 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-lg shadow-rose-600/30 cursor-pointer">
                    <span>Next Slide</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

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
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40" id="modalQuestionId">
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
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold transition cursor-pointer">
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
                document.getElementById('voiceToggleBtn').className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-rose-600/20 text-rose-300 hover:bg-rose-600/30 border border-rose-500/40 text-xs font-semibold transition";
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
                currentPill.classList.remove('bg-rose-600', 'text-white', 'font-bold');
                currentPill.classList.add('bg-slate-800', 'text-slate-300');
            }}

            currentSlideIndex = index;
            const newEl = document.getElementById(`slide-${{currentSlideIndex}}`);
            if (newEl) newEl.classList.add('active');

            const newPill = document.getElementById(`pill-${{currentSlideIndex}}`);
            if (newPill) {{
                newPill.classList.remove('bg-slate-800', 'text-slate-300');
                newPill.classList.add('bg-rose-600', 'text-white', 'font-bold');
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

        // 1. DNA Replication & Cellular Apparatus (Slide 0)
        let isDnaDuplicated = false;
        function triggerDnaReplication() {{
            isDnaDuplicated = !isDnaDuplicated;
            const dnaLeft = document.getElementById('dnaStrandA');
            const dnaRight = document.getElementById('dnaStrandB');
            const status = document.getElementById('dnaSimStatus');
            if (isDnaDuplicated) {{
                dnaRight.classList.remove('hidden');
                dnaLeft.setAttribute('transform', 'translate(-30, 0)');
                dnaRight.setAttribute('transform', 'translate(30, 0)');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>DNA Copied & Apparatus Created:</span> Enzymes synthesize second DNA helix + organelles assemble → cell prepares to divide!";
                playTone(660, 'sine', 0.25);
            }} else {{
                dnaRight.classList.add('hidden');
                dnaLeft.setAttribute('transform', 'translate(0, 0)');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Parent Cell:</span> Single nucleus housing original DNA chromosome blueprint.";
                playTone(440, 'sine', 0.15);
            }}
        }}

        // 2. Variation & Niche Resilience (Slide 1)
        function setNicheTemp(val) {{
            const tempDisplay = document.getElementById('nicheTempDisplay');
            const status = document.getElementById('nicheStatus');
            const normals = document.querySelectorAll('.normal-bacteria');
            const variants = document.querySelectorAll('.variant-bacteria');
            tempDisplay.textContent = `${{val}}°C`;

            if (val > 45) {{
                normals.forEach(b => b.setAttribute('opacity', '0.15'));
                variants.forEach(b => b.setAttribute('opacity', '1'));
                status.innerHTML = "<span class='text-rose-400 font-bold'>Heat Wave!</span> Standard bacteria perish, but heat-resistant mutant variants survive and multiply, preventing extinction!";
                playTone(850, 'sine', 0.2);
            }} else {{
                normals.forEach(b => b.setAttribute('opacity', '0.9'));
                variants.forEach(b => b.setAttribute('opacity', '0.9'));
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Optimal Niche:</span> Both standard and variant bacteria coexist harmoniously.";
                playTone(550, 'sine', 0.12);
            }}
        }}

        // 3. Fission Modes Lab (Slide 2)
        function selectFissionMode(mode) {{
            const status = document.getElementById('fissionStatus');
            const amoeba = document.getElementById('fissionAmoeba');
            const leish = document.getElementById('fissionLeishmania');
            const plas = document.getElementById('fissionPlasmodium');
            amoeba.classList.add('hidden');
            leish.classList.add('hidden');
            plas.classList.add('hidden');

            if (mode === 'amoeba') {{
                amoeba.classList.remove('hidden');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Amoeba (Binary Fission):</span> Irregular cell splits across any plane into two equal daughter cells.";
            }} else if (mode === 'leishmania') {{
                leish.classList.remove('hidden');
                status.innerHTML = "<span class='text-amber-300 font-bold'>Leishmania (Binary Fission):</span> Possesses whip-like flagellum; division occurs strictly in a definite longitudinal orientation!";
            }} else if (mode === 'plasmodium') {{
                plas.classList.remove('hidden');
                status.innerHTML = "<span class='text-rose-400 font-bold'>Plasmodium (Multiple Fission):</span> Under unfavorable conditions, divides repeatedly inside a cyst to release dozens of cells simultaneously!";
            }}
            playTone(700, 'sine', 0.2);
        }}

        // 4. Spirogyra Fragmentation (Slide 3)
        let isFragmented = false;
        function toggleFragmentation() {{
            isFragmented = !isFragmented;
            const fragA = document.getElementById('spiroFragA');
            const fragB = document.getElementById('spiroFragB');
            const status = document.getElementById('fragStatus');
            if (isFragmented) {{
                fragA.setAttribute('transform', 'translate(-25, 0)');
                fragB.setAttribute('transform', 'translate(25, 0)');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Filament Fragmented:</span> Simple body organization allows each severed fragment to grow by mitosis into a full alga!";
                playTone(600, 'sine', 0.25);
            }} else {{
                fragA.setAttribute('transform', 'translate(0, 0)');
                fragB.setAttribute('transform', 'translate(0, 0)');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Mature Spirogyra Filament:</span> Ready to fragment upon reaching full cell length.";
                playTone(400, 'sine', 0.15);
            }}
        }}

        // 5. Planaria Regeneration (Slide 4)
        let isPlanariaCut = false;
        function slicePlanaria() {{
            isPlanariaCut = !isPlanariaCut;
            const pHead = document.getElementById('planariaHead');
            const pMid = document.getElementById('planariaMid');
            const pTail = document.getElementById('planariaTail');
            const status = document.getElementById('regenStatus');
            if (isPlanariaCut) {{
                pHead.setAttribute('transform', 'translate(-40, -20)');
                pMid.setAttribute('transform', 'translate(0, 0)');
                pTail.setAttribute('transform', 'translate(40, 20)');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>3 Fragments → 3 Planaria:</span> Proliferating regenerative cells form blastema masses and differentiate into 3 whole worms!";
                playTone(800, 'sine', 0.3);
            }} else {{
                pHead.setAttribute('transform', 'translate(0, 0)');
                pMid.setAttribute('transform', 'translate(0, 0)');
                pTail.setAttribute('transform', 'translate(0, 0)');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Intact Planaria:</span> Simple flatworm with bilateral eyespots and abundant regenerative cells.";
                playTone(480, 'sine', 0.15);
            }}
        }}

        // 6. Hydra & Yeast Budding (Slide 5)
        let isBudGrown = false;
        function toggleHydraBud() {{
            isBudGrown = !isBudGrown;
            const bud = document.getElementById('hydraBudGroup');
            const status = document.getElementById('buddingStatus');
            if (isBudGrown) {{
                bud.classList.remove('hidden');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Mature Bud Formed:</span> Repeated mitotic divisions at one specific site produce tiny Hydra with tentacles, ready to detach!";
                playTone(720, 'sine', 0.25);
            }} else {{
                bud.classList.add('hidden');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Hydra Parent:</span> Regenerative cells at specific body site await budding trigger.";
                playTone(420, 'sine', 0.15);
            }}
        }}

        // 7. Vegetative Propagation (Slide 6)
        function selectVegetative(type) {{
            const status = document.getElementById('vegetativeStatus');
            if (type === 'bryo') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Bryophyllum Leaf Notches:</span> Adventitious buds develop in scalloped leaf margins; when dropped on moist soil, each grows roots!";
            }} else if (type === 'potato') {{
                status.innerHTML = "<span class='text-amber-300 font-bold'>Potato Tuber 'Eyes':</span> Notches on potato slices contain dormant buds that sprout vigorous green shoots on moist cotton!";
            }} else if (type === 'money') {{
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Money Plant Stem Node:</span> Cuttings containing at least one leaf and node readily grow adventitious water roots!";
            }}
            playTone(640, 'sine', 0.2);
        }}

        // 8. Tissue Culture & Spores (Slide 7)
        function triggerTissueCulture() {{
            const status = document.getElementById('cultureStatus');
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Micropropagation:</span> Shoot tip cells → Callus mass formed in agar → Hormones induce roots and shoots → 10,000 disease-free clones!";
            playTone(880, 'triangle', 0.3);
        }}

        function burstSporangium() {{
            const spores = document.getElementById('airborneSpores');
            const status = document.getElementById('cultureStatus');
            spores.classList.remove('hidden');
            status.innerHTML = "<span class='text-rose-400 font-bold'>Spores Discharged:</span> Sporangium wall bursts, releasing thousands of thick-walled armored spores into air currents!";
            playTone(950, 'sine', 0.25);
        }}

        // 9. Meiosis & Gametic Dimorphism (Slide 8)
        function triggerMeiosis() {{
            const status = document.getElementById('meiosisStatus');
            status.innerHTML = "<span class='text-purple-400 font-bold'>Meiosis Complete:</span> Diploid ($2n = 46$) cell divides into haploid ($n = 23$) gametes! Motile tiny sperm + large nutrient ovum ensure $2n$ restoration upon fertilisation.";
            playTone(760, 'sine', 0.25);
        }}

        // 10. Flower Anatomy (Slide 9)
        function highlightFlowerPart(part) {{
            const status = document.getElementById('flowerStatus');
            if (part === 'stamen') {{
                status.innerHTML = "<span class='text-amber-300 font-bold'>Stamen (Male):</span> Anther + Filament. Anthers produce powdery yellow pollen grains containing male germ-cells.";
            }} else if (part === 'pistil') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Pistil (Female):</span> Sticky Stigma (pollen trap) + elongated Style + swollen Ovary containing ovules with egg cells.";
            }} else if (part === 'petals') {{
                status.innerHTML = "<span class='text-rose-400 font-bold'>Petals (Corolla):</span> Brightly colored and scented to attract pollinating insects and birds!";
            }}
            playTone(680, 'sine', 0.15);
        }}

        // 11. Pollination & Seed (Slide 10)
        let isPollinated = false;
        function triggerPollenGermination() {{
            isPollinated = !isPollinated;
            const tube = document.getElementById('pollenTubeGrowth');
            const status = document.getElementById('pollinationStatus');
            if (isPollinated) {{
                tube.classList.remove('hidden');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Pollen Tube Grown:</span> Tube penetrates down style into ovule! Zygote divides into embryo, ovule becomes seed, ovary ripens into fruit!";
                playTone(840, 'sine', 0.3);
            }} else {{
                tube.classList.add('hidden');
                status.innerHTML = "<span class='text-slate-300 font-bold'>Pollen on Stigma:</span> Awaiting moisture to germinate tube.";
                playTone(450, 'sine', 0.15);
            }}
        }}

        // 12. Puberty Timeline (Slide 11)
        function setPubertyAge(age) {{
            const label = document.getElementById('pubertyAgeLabel');
            const status = document.getElementById('pubertyStatus');
            label.textContent = `${{age}} Years`;
            if (age >= 12) {{
                status.innerHTML = "<span class='text-rose-400 font-bold'>Puberty Active:</span> Testosterone & oestrogen surge! Armpit/pubic hair, voice deepening in boys, breast development & menstruation in girls.";
            }} else {{
                status.innerHTML = "<span class='text-slate-300 font-bold'>Childhood Growth:</span> Bodily resources prioritized for somatic growth (height, teeth, bones).";
            }}
            playTone(400 + age * 25, 'sine', 0.1);
        }}

        // 13. Male Reproductive System (Slide 12)
        function traceSpermPath() {{
            const path = document.getElementById('spermTransitPath');
            const status = document.getElementById('maleSystemStatus');
            path.classList.remove('hidden');
            status.innerHTML = "<span class='text-cyan-400 font-bold'>Sperm Transit:</span> Testes (2-2.5°C cooler in scrotum) → Vas deferens → Seminal vesicles & prostate add fluid/fructose → Urethra!";
            playTone(720, 'sine', 0.25);
        }}

        // 14. Female Reproductive System (Slide 13)
        function triggerOvulation() {{
            const egg = document.getElementById('ovulatedEggDot');
            const status = document.getElementById('femaleSystemStatus');
            egg.classList.remove('hidden');
            status.innerHTML = "<span class='text-rose-400 font-bold'>Ovulation (Day 14):</span> Mature ovum released into fallopian tube! Ciliated oviduct awaits sperms for fertilisation.";
            playTone(780, 'sine', 0.25);
        }}

        // 15. Placental Exchange (Slide 14)
        function pulsePlacentaExchange() {{
            const status = document.getElementById('placentaStatus');
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Placental Lifeline:</span> Embryonic villi in maternal blood spaces diffuse glucose & $O_2$ to foetus, and flush $CO_2$ & urea to mother!";
            playTone(660, 'sine', 0.25);
        }}

        // 16. Menstrual Cycle (Slide 15)
        function setCycleDay(day) {{
            const dayLabel = document.getElementById('cycleDayLabel');
            const status = document.getElementById('menstrualStatus');
            dayLabel.textContent = `Day ${{day}} of 28`;
            if (day <= 5) {{
                status.innerHTML = "<span class='text-rose-400 font-bold'>Menstruation (Days 1–5):</span> Unfertilised egg degenerated; spongy uterine lining sheds through vagina as blood and mucus.";
            }} else if (day <= 13) {{
                status.innerHTML = "<span class='text-amber-300 font-bold'>Follicular Phase:</span> Uterine endometrium thickens and becomes rich with blood capillaries.";
            }} else if (day === 14) {{
                status.innerHTML = "<span class='text-purple-400 font-bold'>Ovulation:</span> Mature egg released from ovary into oviduct!";
            }} else {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Luteal Phase:</span> Lining spongy and prepared for embryo; if fertilisation fails, resets to Day 1.";
            }}
            playTone(450 + day * 15, 'sine', 0.1);
        }}

        // 17. Contraception & STDs (Slide 16)
        function testContraceptive(type) {{
            const status = document.getElementById('contraceptionStatus');
            if (type === 'barrier') {{
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Condom (Barrier):</span> Mechanically blocks sperms AND protects against bacterial (gonorrhoea/syphilis) and viral (HIV) STDs!";
            }} else if (type === 'pill') {{
                status.innerHTML = "<span class='text-amber-300 font-bold'>Oral Pills (Hormonal):</span> Changes body hormonal balance to prevent egg release. Does NOT protect against STDs!";
            }} else if (type === 'iucd') {{
                status.innerHTML = "<span class='text-cyan-400 font-bold'>Copper-T (IUCD):</span> Placed in uterus to block embryo implantation. Does NOT protect against STDs!";
            }} else if (type === 'surgery') {{
                status.innerHTML = "<span class='text-purple-400 font-bold'>Surgical Ligation:</span> Vasectomy in males (vas deferens blocked) or Tubectomy in females (fallopian tubes blocked). Permanent contraception!";
            }}
            playTone(700, 'sine', 0.2);
        }}

        // Audio unlock on user gesture
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
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">DNA Duplication Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Blueprint Copying</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 160" class="w-full h-full">
                        <ellipse cx="110" cy="80" rx="90" ry="60" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                        <circle cx="110" cy="80" r="35" fill="#0f172a" stroke="#f43f5e" stroke-dasharray="3"/>
                        <!-- DNA Strand A -->
                        <g id="dnaStrandA" class="transition-all duration-500">
                            <path d="M100,60 Q115,70 100,80 T100,100" fill="none" stroke="#38bdf8" stroke-width="4"/>
                            <circle cx="100" cy="70" r="4" fill="#38bdf8"/>
                            <circle cx="100" cy="90" r="4" fill="#38bdf8"/>
                        </g>
                        <!-- DNA Strand B -->
                        <g id="dnaStrandB" class="hidden transition-all duration-500">
                            <path d="M120,60 Q105,70 120,80 T120,100" fill="none" stroke="#f43f5e" stroke-width="4"/>
                            <circle cx="120" cy="70" r="4" fill="#f43f5e"/>
                            <circle cx="120" cy="90" r="4" fill="#f43f5e"/>
                        </g>
                    </svg>
                </div>
                <button onclick="triggerDnaReplication()" class="w-full py-2 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition cursor-pointer">
                    🧬 Replicate DNA & Assemble Apparatus
                </button>
                <div id="dnaSimStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    DNA copying duplicates genetic blueprints; cellular apparatus must assemble before cell division!
                </div>
            </div>
        """,
        1: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Niche Resilience Lab</span>
                    <span id="nicheTempDisplay" class="text-xs font-mono font-bold text-amber-300">25°C</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <rect x="10" y="10" width="180" height="130" rx="10" fill="#0c4a6e" opacity="0.4"/>
                        <!-- Normal bacteria (green) -->
                        <circle class="normal-bacteria" cx="40" cy="40" r="7" fill="#10b981"/>
                        <circle class="normal-bacteria" cx="80" cy="50" r="7" fill="#10b981"/>
                        <circle class="normal-bacteria" cx="130" cy="35" r="7" fill="#10b981"/>
                        <circle class="normal-bacteria" cx="60" cy="110" r="7" fill="#10b981"/>
                        <circle class="normal-bacteria" cx="150" cy="100" r="7" fill="#10b981"/>
                        <!-- Variant heat resistant (red) -->
                        <circle class="variant-bacteria" cx="100" cy="90" r="7" fill="#ef4444"/>
                        <circle class="variant-bacteria" cx="160" cy="60" r="7" fill="#ef4444"/>
                        <text x="20" y="130" fill="#38bdf8" font-size="8">Pond Microcosm</text>
                    </svg>
                </div>
                <div>
                    <label class="text-[10px] text-slate-400 block mb-1">Water Temperature Slider (Simulate Global Warming):</label>
                    <input type="range" min="20" max="65" value="25" oninput="setNicheTemp(this.value)" class="w-full accent-rose-500 cursor-pointer">
                </div>
                <div id="nicheStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Slide temperature up: heat-sensitive bacteria die, but pre-existing heat-resistant variants survive!
                </div>
            </div>
        """,
        2: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Fission Modes Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 7.1 & 7.2</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Amoeba mode -->
                        <g id="fissionAmoeba">
                            <path d="M40,75 Q60,40 100,50 T160,75 Q150,110 100,105 T40,75" fill="#38bdf8" opacity="0.6"/>
                            <circle cx="80" cy="75" r="8" fill="#0284c7"/>
                            <circle cx="120" cy="75" r="8" fill="#0284c7"/>
                            <line x1="100" y1="45" x2="100" y2="110" stroke="#f43f5e" stroke-dasharray="3"/>
                        </g>
                        <!-- Leishmania mode -->
                        <g id="fissionLeishmania" class="hidden">
                            <ellipse cx="80" cy="75" rx="14" ry="40" fill="#f59e0b" opacity="0.7"/>
                            <ellipse cx="120" cy="75" rx="14" ry="40" fill="#f59e0b" opacity="0.7"/>
                            <path d="M80,35 Q70,15 85,10 M120,35 Q130,15 115,10" stroke="#fbbf24" stroke-width="2" fill="none"/>
                            <text x="60" y="130" fill="#f59e0b" font-size="8">Longitudinal Fission</text>
                        </g>
                        <!-- Plasmodium mode -->
                        <g id="fissionPlasmodium" class="hidden">
                            <circle cx="100" cy="75" r="45" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
                            <circle cx="85" cy="65" r="4" fill="#ef4444"/>
                            <circle cx="115" cy="65" r="4" fill="#ef4444"/>
                            <circle cx="95" cy="85" r="4" fill="#ef4444"/>
                            <circle cx="110" cy="95" r="4" fill="#ef4444"/>
                            <circle cx="75" cy="85" r="4" fill="#ef4444"/>
                            <text x="60" y="135" fill="#ef4444" font-size="8">Multiple Daughter Cells</text>
                        </g>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="selectFissionMode('amoeba')" class="px-2 py-1.5 rounded-lg bg-sky-600/30 hover:bg-sky-600/50 text-sky-300 text-xs font-semibold border border-sky-500/40">Amoeba</button>
                    <button onclick="selectFissionMode('leishmania')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40">Leishmania</button>
                    <button onclick="selectFissionMode('plasmodium')" class="px-2 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 text-xs font-semibold border border-rose-500/40">Plasmodium</button>
                </div>
                <div id="fissionStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Compare binary fission in Amoeba & Leishmania vs multiple fission in Plasmodium!
                </div>
            </div>
        """,
        3: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Spirogyra Fragmentation</span>
                    <span class="text-[10px] font-mono text-slate-400">Activity 7.4</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 150" class="w-full h-full">
                        <g id="spiroFragA" class="transition-all duration-500">
                            <rect x="30" y="65" width="70" height="25" rx="3" fill="#059669" stroke="#10b981" stroke-width="2"/>
                            <path d="M40,65 Q65,80 90,65" stroke="#34d399" stroke-width="2" fill="none"/>
                        </g>
                        <g id="spiroFragB" class="transition-all duration-500">
                            <rect x="120" y="65" width="70" height="25" rx="3" fill="#059669" stroke="#10b981" stroke-width="2"/>
                            <path d="M130,65 Q155,80 180,65" stroke="#34d399" stroke-width="2" fill="none"/>
                        </g>
                        <line x1="110" y1="50" x2="110" y2="105" stroke="#ef4444" stroke-dasharray="3"/>
                    </svg>
                </div>
                <button onclick="toggleFragmentation()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    ✂️ Mature & Break into Fragments
                </button>
                <div id="fragStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Simple filaments fragment upon maturation, each piece growing into a complete new Spirogyra!
                </div>
            </div>
        """,
        4: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Planaria Regeneration Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 7.3</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 150" class="w-full h-full">
                        <!-- Head -->
                        <g id="planariaHead" class="transition-all duration-500">
                            <path d="M90,45 Q110,35 130,45 L130,60 L90,60 Z" fill="#d97706" stroke="#b45309"/>
                            <circle cx="102" cy="45" r="2" fill="#000"/>
                            <circle cx="118" cy="45" r="2" fill="#000"/>
                        </g>
                        <!-- Mid -->
                        <g id="planariaMid" class="transition-all duration-500">
                            <rect x="90" y="65" width="40" height="25" fill="#d97706" stroke="#b45309"/>
                        </g>
                        <!-- Tail -->
                        <g id="planariaTail" class="transition-all duration-500">
                            <path d="M90,95 L130,95 L110,125 Z" fill="#d97706" stroke="#b45309"/>
                        </g>
                    </svg>
                </div>
                <button onclick="slicePlanaria()" class="w-full py-2 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-300 text-xs font-bold transition cursor-pointer">
                    🔪 Slice Planaria into 3 Segments!
                </button>
                <div id="regenStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Cut pieces use specialized proliferating cells to regenerate 3 complete individual flatworms!
                </div>
            </div>
        """,
        5: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Hydra & Yeast Budding</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 7.4</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Hydra Parent Stalk -->
                        <path d="M80,140 C80,90 75,60 75,40" stroke="#15803d" stroke-width="14" fill="none" stroke-linecap="round"/>
                        <!-- Tentacles -->
                        <path d="M75,40 Q55,20 40,25 M75,40 Q75,15 70,5 M75,40 Q95,20 105,15" stroke="#22c55e" stroke-width="3" fill="none"/>
                        <!-- Outgrowth Bud -->
                        <g id="hydraBudGroup" class="hidden">
                            <path d="M85,90 C110,85 125,75 130,65" stroke="#22c55e" stroke-width="8" fill="none" stroke-linecap="round"/>
                            <path d="M130,65 Q140,55 145,50 M130,65 Q135,50 130,45" stroke="#4ade80" stroke-width="2" fill="none"/>
                        </g>
                    </svg>
                </div>
                <button onclick="toggleHydraBud()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    🌱 Sprout & Detach Mature Bud
                </button>
                <div id="buddingStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Repeated cell division creates an outgrowth bud that develops tentacles and detaches as a new Hydra!
                </div>
            </div>
        """,
        6: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Vegetative Propagation Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 7.5</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Bryophyllum leaf with buds in notches -->
                        <path d="M40,75 C40,40 80,30 160,75 C80,120 40,110 40,75 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <!-- Notches plantlets -->
                        <circle cx="80" cy="38" r="4" fill="#a3e635"/>
                        <circle cx="120" cy="45" r="4" fill="#a3e635"/>
                        <circle cx="80" cy="112" r="4" fill="#a3e635"/>
                        <circle cx="120" cy="105" r="4" fill="#a3e635"/>
                        <text x="50" y="140" fill="#a3e635" font-size="8">Bryophyllum Leaf Notches</text>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="selectVegetative('bryo')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40">Bryophyllum</button>
                    <button onclick="selectVegetative('potato')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40">Potato Eye</button>
                    <button onclick="selectVegetative('money')" class="px-2 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-300 text-xs font-semibold border border-cyan-500/40">Money Plant</button>
                </div>
                <div id="vegetativeStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Inspect natural vegetative propagation from leaves, potato tuber eyes, and stem nodes!
                </div>
            </div>
        """,
        7: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Culture & Spores Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Fig 7.6</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Bread mould Rhizopus -->
                        <line x1="20" y1="120" x2="180" y2="120" stroke="#78350f" stroke-width="4"/>
                        <!-- Hyphae -->
                        <path d="M40,120 Q50,90 60,70 M100,120 Q95,80 100,60 M150,120 Q160,90 150,70" stroke="#94a3b8" stroke-width="2" fill="none"/>
                        <!-- Sporangia blobs -->
                        <circle cx="60" cy="70" r="12" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
                        <circle cx="100" cy="60" r="14" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
                        <circle cx="150" cy="70" r="12" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
                        <!-- Spores bursting -->
                        <g id="airborneSpores" class="hidden">
                            <circle cx="95" cy="40" r="2" fill="#38bdf8"/>
                            <circle cx="105" cy="42" r="2" fill="#38bdf8"/>
                            <circle cx="100" cy="35" r="2" fill="#38bdf8"/>
                        </g>
                    </svg>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="triggerTissueCulture()" class="px-2.5 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-semibold transition cursor-pointer">
                        🧫 Tissue Culture Callus
                    </button>
                    <button onclick="burstSporangium()" class="px-2.5 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-semibold transition cursor-pointer">
                        🍄 Burst Sporangium Spores
                    </button>
                </div>
                <div id="cultureStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Test micropropagation in sterile callus media or burst thick-walled spores in Rhizopus!
                </div>
            </div>
        """,
        8: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Meiosis & Gametic Dimorphism</span>
                    <span class="text-[10px] font-mono text-slate-400">2n → n</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 150" class="w-full h-full">
                        <!-- Large female ovum -->
                        <circle cx="150" cy="75" r="30" fill="#f43f5e" opacity="0.5" stroke="#be123c" stroke-width="2"/>
                        <circle cx="150" cy="75" r="8" fill="#fda4af"/>
                        <text x="135" y="125" fill="#fda4af" font-size="8">Ovum (n=23)</text>
                        <!-- Tiny motile male sperm -->
                        <ellipse cx="60" cy="75" rx="7" ry="4" fill="#38bdf8"/>
                        <path d="M53,75 Q40,70 30,80 T15,75" stroke="#38bdf8" stroke-width="2" fill="none"/>
                        <text x="25" y="100" fill="#38bdf8" font-size="8">Sperm (n=23)</text>
                    </svg>
                </div>
                <button onclick="triggerMeiosis()" class="w-full py-2 rounded-lg bg-purple-600/30 hover:bg-purple-600/50 border border-purple-500/40 text-purple-300 text-xs font-bold transition cursor-pointer">
                    🧬 Perform Meiosis (Halve Chromosomes: 2n → n)
                </button>
                <div id="meiosisStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Meiosis ensures gametes carry half the chromosomes ($n$), restoring diploid balance ($2n$) upon fertilisation!
                </div>
            </div>
        """,
        9: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Flower Anatomy (Fig 7.7)</span>
                    <span class="text-[10px] font-mono text-slate-400">Angiosperm Whorls</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Petals -->
                        <path d="M40,50 Q100,10 160,50 Q100,70 40,50" fill="#f43f5e" opacity="0.4"/>
                        <!-- Pistil (Female) -->
                        <path d="M95,115 L95,65 Q100,55 105,65 L105,115 Q125,120 100,135 Q75,120 95,115" fill="#10b981"/>
                        <circle cx="100" cy="55" r="5" fill="#059669"/>
                        <!-- Stamens (Male) -->
                        <line x1="75" y1="120" x2="65" y2="70" stroke="#e2e8f0" stroke-width="2"/>
                        <ellipse cx="65" cy="70" rx="4" ry="7" fill="#fbbf24"/>
                        <line x1="125" y1="120" x2="135" y2="70" stroke="#e2e8f0" stroke-width="2"/>
                        <ellipse cx="135" cy="70" rx="4" ry="7" fill="#fbbf24"/>
                    </svg>
                </div>
                <div class="grid grid-cols-3 gap-1.5">
                    <button onclick="highlightFlowerPart('stamen')" class="px-2 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 text-xs font-semibold border border-amber-500/40">Stamen (♂)</button>
                    <button onclick="highlightFlowerPart('pistil')" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 text-xs font-semibold border border-emerald-500/40">Pistil (♀)</button>
                    <button onclick="highlightFlowerPart('petals')" class="px-2 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 text-xs font-semibold border border-rose-500/40">Petals</button>
                </div>
                <div id="flowerStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Inspect male stamens (anther + pollen) vs female pistil (stigma, style, ovary with ovules)!
                </div>
            </div>
        """,
        10: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Pollination & Pollen Tube (Fig 7.8)</span>
                    <span class="text-[10px] font-mono text-slate-400">Zygote Formation</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Carpel structure -->
                        <path d="M85,50 Q100,45 115,50 L108,95 C125,100 130,130 100,135 C70,130 75,100 92,95 Z" fill="#065f46" stroke="#10b981" stroke-width="2"/>
                        <!-- Pollen grain on stigma -->
                        <circle cx="100" cy="45" r="4" fill="#fbbf24"/>
                        <!-- Pollen tube -->
                        <path id="pollenTubeGrowth" d="M100,49 L100,115" stroke="#fbbf24" stroke-width="3" stroke-dasharray="2" fill="none" class="hidden"/>
                        <!-- Ovule -->
                        <ellipse cx="100" cy="115" rx="8" ry="12" fill="#fef08a"/>
                    </svg>
                </div>
                <button onclick="triggerPollenGermination()" class="w-full py-2 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-300 text-xs font-bold transition cursor-pointer">
                    🐝 Pollinate & Grow Pollen Tube Down Style
                </button>
                <div id="pollinationStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Pollen tube tunnels through the style into ovary to fertilise ovule, forming zygote and seed!
                </div>
            </div>
        """,
        11: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Puberty Hormone Surge</span>
                    <span id="pubertyAgeLabel" class="text-xs font-mono font-bold text-rose-400">14 Years</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                    <div class="flex justify-between text-xs text-slate-300">
                        <span>Adolescence Age:</span>
                        <span>10 — 18 Years</span>
                    </div>
                    <input type="range" min="10" max="18" value="14" oninput="setPubertyAge(this.value)" class="w-full accent-rose-500 cursor-pointer">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800 text-[10px] text-slate-400 flex justify-between">
                        <span>Testosterone: High</span>
                        <span>Oestrogen: High</span>
                    </div>
                </div>
                <div id="pubertyStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Slide age to explore when general somatic growth slows down and sexual maturation accelerates!
                </div>
            </div>
        """,
        12: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Male System (Fig 7.10)</span>
                    <span class="text-[10px] font-mono text-slate-400">Testis Scrotum -2.5°C</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Scrotum & Testis -->
                        <ellipse cx="65" cy="115" rx="18" ry="22" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
                        <circle cx="65" cy="115" r="10" fill="#38bdf8"/>
                        <!-- Vas deferens -->
                        <path id="spermTransitPath" d="M65,105 Q65,40 120,40 Q150,40 140,95 L140,120" stroke="#f43f5e" stroke-width="3" stroke-dasharray="3" fill="none" class="hidden"/>
                        <!-- Glands -->
                        <circle cx="130" cy="55" r="6" fill="#fbbf24"/>
                        <circle cx="135" cy="70" r="8" fill="#f59e0b"/>
                        <text x="145" y="65" fill="#fbbf24" font-size="8">Prostate & Seminal</text>
                    </svg>
                </div>
                <button onclick="traceSpermPath()" class="w-full py-2 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-300 text-xs font-bold transition cursor-pointer">
                    🧪 Trace Sperm Transit & Semen Addition
                </button>
                <div id="maleSystemStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Testes in scrotum maintain cool temperature; vas deferens receives prostate & seminal vesicle fluids!
                </div>
            </div>
        """,
        13: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Female System (Fig 7.11)</span>
                    <span class="text-[10px] font-mono text-slate-400">Oviduct & Uterus</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 200 150" class="w-full h-full">
                        <!-- Uterus pear shape -->
                        <path d="M85,120 L85,85 C70,70 60,65 100,55 C140,65 130,70 115,85 L115,120 Z" fill="#be123c" opacity="0.6"/>
                        <!-- Fallopian tubes -->
                        <path d="M75,65 Q45,55 35,70" stroke="#fda4af" stroke-width="4" fill="none"/>
                        <path d="M125,65 Q155,55 165,70" stroke="#fda4af" stroke-width="4" fill="none"/>
                        <!-- Ovaries -->
                        <circle cx="35" cy="80" r="9" fill="#f43f5e"/>
                        <circle cx="165" cy="80" r="9" fill="#f43f5e"/>
                        <circle id="ovulatedEggDot" cx="55" cy="62" r="4" fill="#fbbf24" class="hidden pulse-glow"/>
                    </svg>
                </div>
                <button onclick="triggerOvulation()" class="w-full py-2 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition cursor-pointer">
                    🥚 Release Monthly Egg (Ovulation into Oviduct)
                </button>
                <div id="femaleSystemStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Ovary releases 1 egg per month into oviduct (fertilisation site); uterus lining prepares for embryo!
                </div>
            </div>
        """,
        14: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Placental Diffusion Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Villi & Blood Spaces</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center h-48">
                    <svg viewBox="0 0 220 150" class="w-full h-full">
                        <!-- Uterine wall -->
                        <rect x="20" y="20" width="35" height="110" fill="#881337"/>
                        <!-- Placenta disc -->
                        <rect x="55" y="25" width="20" height="100" rx="3" fill="#e11d48"/>
                        <!-- Villi projections -->
                        <path d="M75,40 Q95,40 75,55 M75,65 Q100,65 75,80 M75,90 Q95,90 75,105" stroke="#fecdd3" stroke-width="3" fill="none"/>
                        <!-- Umbilical cord -->
                        <path d="M75,70 Q130,70 170,90" stroke="#0284c7" stroke-width="5" fill="none"/>
                        <circle cx="170" cy="90" r="14" fill="#38bdf8" opacity="0.6"/>
                        <text x="160" y="93" fill="#ffffff" font-size="8">Foetus</text>
                    </svg>
                </div>
                <button onclick="pulsePlacentaExchange()" class="w-full py-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition cursor-pointer">
                    🔄 Diffuse Oxygen & Glucose via Villi
                </button>
                <div id="placentaStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Villi provide huge surface area for nutrient and gas exchange without mixing maternal and foetal blood!
                </div>
            </div>
        """,
        15: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Menstrual Cycle (28 Days)</span>
                    <span id="cycleDayLabel" class="text-xs font-mono font-bold text-rose-400">Day 1 of 28</span>
                </div>
                <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                    <div class="flex justify-between text-xs text-slate-300">
                        <span>Menstrual Timeline:</span>
                        <span>Days 1 to 28</span>
                    </div>
                    <input type="range" min="1" max="28" value="1" oninput="setCycleDay(this.value)" class="w-full accent-rose-500 cursor-pointer">
                    <div class="grid grid-cols-3 gap-1 text-[10px] text-slate-400 text-center">
                        <span class="p-1 rounded bg-rose-950/40 text-rose-300">Days 1-5 Flow</span>
                        <span class="p-1 rounded bg-purple-950/40 text-purple-300">Day 14 Ovulation</span>
                        <span class="p-1 rounded bg-amber-950/40 text-amber-300">Days 15-28 Luteal</span>
                    </div>
                </div>
                <div id="menstrualStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Unfertilised egg lives 1 day; thick uterine lining sheds through vagina as blood and mucus (2–8 days)!
                </div>
            </div>
        """,
        16: """
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Contraceptive Strategies Lab</span>
                    <span class="text-[10px] font-mono text-slate-400">Family Planning & STDs</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="testContraceptive('barrier')" class="p-2 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold text-left">
                        🛡️ Barrier (Condoms)
                        <span class="block text-[9px] font-normal text-slate-400">Blocks sperm & STDs</span>
                    </button>
                    <button onclick="testContraceptive('pill')" class="p-2 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-300 text-xs font-bold text-left">
                        💊 Oral Pills (Hormonal)
                        <span class="block text-[9px] font-normal text-slate-400">Suppresses ovulation</span>
                    </button>
                    <button onclick="testContraceptive('iucd')" class="p-2 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-300 text-xs font-bold text-left">
                        🧲 Copper-T (IUCD)
                        <span class="block text-[9px] font-normal text-slate-400">Blocks implantation</span>
                    </button>
                    <button onclick="testContraceptive('surgery')" class="p-2 rounded-lg bg-purple-600/30 hover:bg-purple-600/50 border border-purple-500/40 text-purple-300 text-xs font-bold text-left">
                        ✂️ Surgical Block
                        <span class="block text-[9px] font-normal text-slate-400">Vasectomy / Tubectomy</span>
                    </button>
                </div>
                <div id="contraceptionStatus" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
                    Click methods to discover how barrier, hormonal, IUCD, and surgical techniques prevent pregnancy & STDs!
                </div>
            </div>
        """
    }
    return sims.get(idx, "<div class='text-slate-400 text-xs'>Interactive Simulator</div>")

if __name__ == '__main__':
    html_out = generate_html()
    out_path = 'public/animations/how-do-organisms-reproduce.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_out)
    print(f"Successfully generated {out_path} ({len(html_out)} bytes)")
