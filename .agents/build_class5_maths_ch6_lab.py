#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compile public/animations/class5-maths-the-dairy-farm.html
and create 7 symlinks for NCERT Class 5 Mathematics - Chapter 6: The Dairy Farm
NEP 2020 / Joyful Mathematics
"""

import os
import json
import re
from class5_maths_ch6_data import ALL_SLIDES
from class5_maths_ch6_sims import ALL_SIMULATORS
from class5_maths_ch6_js import js_code

def build_html():
    # Verify titles: 1-3 words
    for s in ALL_SLIDES:
        words = s["title"].strip().split()
        assert 1 <= len(words) <= 3, f"Title '{s['title']}' must be 1 to 3 words!"

    # Verify zero raw LaTeX
    corpus = ""
    for s in ALL_SLIDES:
        corpus += " " + s["title"] + " " + s["tag"] + " " + s.get("lecture", "") + " " + s.get("theory_html", "")
        for cp in s.get("checkpoints", []):
            corpus += " " + cp["question"] + " " + " ".join(cp["options"]) + " " + cp["explanation"]
        for q in s.get("questions", []):
            corpus += " " + q["question"] + " " + " ".join(q["options"]) + " " + q["solution_html"]

    latex_matches = re.findall(r"\\(?:frac|times|div|pm|text|cdot|\$)|(?<!\\)\$[^$]+\$", corpus)
    if latex_matches:
        raise ValueError(f"Raw LaTeX detected in Chapter 6: {latex_matches[:10]}")

    print("VERIFIED PASS: All Chapter 6 Mathematics data zero raw LaTeX verified!")

    slides_html = []
    for s in ALL_SLIDES:
        slide_id = s["id"]
        is_quiz = 17 <= slide_id <= 20

        # Header for slide
        header_html = f"""
        <div class="mb-5 pb-3 border-b border-slate-700/60 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
                <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mb-1.5">
                    <span>{s['tag']}</span>
                </div>
                <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
                    {s['title']}
                </h2>
            </div>
            <div class="flex items-center gap-2 self-start sm:self-auto">
                <span class="px-2.5 py-1 bg-slate-800 border border-slate-700 rounded-lg text-xs font-mono text-slate-300">
                    Slide {slide_id} of 20
                </span>
            </div>
        </div>
        """

        if not is_quiz:
            # Slides 1 to 16: Theory, Simulators, Checkpoints
            sim_markup = ALL_SIMULATORS.get(f"sim_slide_{slide_id}", '<div class="p-4 text-center text-slate-500">Simulator Loading...</div>')

            checkpoints_html = []
            for cp_idx, cp in enumerate(s.get("checkpoints", [])):
                opt_btns = []
                for opt_idx, opt in enumerate(cp["options"]):
                    exp_escaped = cp["explanation"].replace("'", "\\'").replace('"', '&quot;')
                    opt_btns.append(f"""
                    <button onclick="checkCheckpoint({cp_idx}, {opt_idx}, {cp['correct']}, '{exp_escaped}')" class="cp-opt-btn w-full text-left p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-medium transition flex items-center gap-2">
                        <span class="w-5 h-5 rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-300 shrink-0">{chr(65 + opt_idx)}</span>
                        <span>{opt}</span>
                    </button>
                    """)

                checkpoints_html.append(f"""
                <div id="cp_{slide_id}_{cp_idx}" class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">CHECKPOINT {cp_idx + 1}</span>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white">{cp['question']}</p>
                    <div class="space-y-1.5">
                        {"".join(opt_btns)}
                    </div>
                    <div id="cp_exp_{slide_id}_{cp_idx}" class="hidden p-2 rounded-lg bg-slate-900/90 border border-slate-700 text-xs"></div>
                </div>
                """)

            slide_body = f"""
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
                <!-- Theory & Checkpoints (Left Column) -->
                <div class="lg:col-span-6 space-y-4">
                    <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800">
                        {s['theory_html']}
                    </div>
                    <div class="space-y-3">
                        <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                            <span class="inline-block w-2 h-2 rounded-full bg-amber-400"></span>
                            Formative Concept Checkpoints (Silent Practice)
                        </h4>
                        {"".join(checkpoints_html)}
                    </div>
                </div>

                <!-- Simulator (Right Column) -->
                <div class="lg:col-span-6">
                    <div class="sticky top-20">
                        {sim_markup}
                    </div>
                </div>
            </div>
            """
        else:
            # Slides 17 to 20: 10 Quiz Questions
            quiz_cards = []
            for q in s.get("questions", []):
                q_id = q["id"]
                opt_btns = []
                for opt_idx, opt in enumerate(q["options"]):
                    opt_btns.append(f"""
                    <button onclick="answerQuiz({q_id}, {opt_idx}, {q['correct']})" class="quiz-opt-btn w-full text-left p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-medium transition flex items-center gap-2">
                        <span class="w-5 h-5 rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-300 shrink-0">{chr(65 + opt_idx)}</span>
                        <span>{opt}</span>
                    </button>
                    """)

                sol_escaped = q["solution_html"].replace("'", "\\'").replace('"', '&quot;')
                q_title = f"Question {q_id} Solution".replace("'", "\\'")

                quiz_cards.append(f"""
                <div id="quiz_q_{q_id}" class="p-3.5 rounded-xl bg-slate-800/70 border border-slate-700/80 flex flex-col justify-between space-y-2">
                    <div>
                        <div class="flex items-center justify-between mb-1.5">
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">QUESTION {q_id}</span>
                            <button id="quiz_sol_btn_{q_id}" onclick="showSolutionModal({q_id}, '{q_title}', '{sol_escaped}')" class="hidden px-2 py-0.5 text-[10px] font-semibold text-amber-300 hover:text-amber-200 bg-amber-950/60 border border-amber-500/30 rounded transition">
                                View Solution 💡
                            </button>
                        </div>
                        <p class="text-xs sm:text-sm font-semibold text-white mb-2">{q['question']}</p>
                        <div class="space-y-1.5">
                            {"".join(opt_btns)}
                        </div>
                    </div>
                </div>
                """)

            slide_body = f"""
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                {"".join(quiz_cards)}
            </div>
            """

        slides_html.append(f"""
        <div id="slide-{slide_id}" class="slide-card {'hidden' if slide_id > 1 else ''} bg-slate-900/90 backdrop-blur-md rounded-2xl p-5 sm:p-7 border border-slate-800 shadow-2xl">
            {header_html}
            {slide_body}
        </div>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 5 Mathematics • Chapter 6 • The Dairy Farm Master Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            850: '#0f172a',
                            950: '#020617'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-slate-950">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=mathematics&class=class5" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition" title="Return to Class 5 Mathematics">
                    <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
                </a>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">CLASS 5 MATHS</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 6</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight">The Dairy Farm • Master Laboratory</h1>
                </div>
            </div>

            <!-- Voice Selector & Classroom Audio Bar -->
            <div class="flex items-center gap-3 flex-wrap justify-end">
                <div class="flex items-center gap-1.5 bg-slate-800/80 px-2.5 py-1.5 rounded-xl border border-slate-700">
                    <span class="text-xs text-slate-400 font-medium">Teacher Voice:</span>
                    <select id="voiceSelect" onchange="onVoiceChange(this)" class="bg-slate-900 text-xs text-slate-200 rounded-lg px-2 py-1 border border-slate-700 focus:outline-none focus:border-emerald-400 max-w-[200px] truncate">
                        <option value="">Detecting Pure Male Teacher Voice...</option>
                    </select>
                </div>

                <button id="audioBtn" onclick="speakLecture()" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs sm:text-sm flex items-center gap-2 shadow-md transition transform active:scale-95">
                    <span>🔊</span>
                    <span>Listen Lecture</span>
                </button>
            </div>
        </div>

        <!-- Progress bar line -->
        <div class="w-full bg-slate-800 h-1">
            <div id="progressBar" class="bg-gradient-to-r from-emerald-400 via-teal-500 to-cyan-500 h-1 w-0 transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Slide Stage -->
    <main class="max-w-7xl mx-auto px-4 py-6 w-full flex-1">
        {"".join(slides_html)}
    </main>

    <!-- Bottom Navigation Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-slate-800 py-3 shadow-2xl">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <span class="font-mono text-xs font-bold text-emerald-400 bg-emerald-950/60 px-3 py-1 rounded-lg border border-emerald-500/30">
                    Slide <span id="curSlideNum">1</span> of 20
                </span>
            </div>

            <div class="flex items-center gap-3">
                <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs sm:text-sm font-bold border border-slate-700 flex items-center gap-1.5 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    <span>Previous</span>
                </button>

                <button id="nextBtn" onclick="nextSlide()" class="px-4 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-slate-950 text-xs sm:text-sm font-extrabold flex items-center gap-1.5 shadow-lg transition">
                    <span>Next</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>

                <!-- Terminal Slide Notice -->
                <div id="lastSlideNotice" class="hidden px-3.5 py-1.5 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 font-bold text-xs sm:text-sm flex items-center gap-2">
                    <span>You have reached the last slide of this chapter.</span>
                </div>
            </div>
        </div>
    </footer>

    <!-- Solution Popup Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-4">
                <h3 id="modalTitle" class="text-base font-bold text-white flex items-center gap-2">
                    <span class="text-amber-400">💡</span> Step-by-Step Solution
                </h3>
                <button onclick="closeSolutionModal()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <div id="modalBody" class="space-y-3 text-xs sm:text-sm text-slate-300"></div>
            <div class="mt-5 pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-xl transition">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- Data Injection -->
    <script>
        const allSlidesData = {json.dumps(ALL_SLIDES)};
    </script>

    <!-- Logic Engine -->
    <script>
{js_code}
    </script>
</body>
</html>
"""

    out_path = "public/animations/class5-maths-the-dairy-farm.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully compiled {out_path} ({len(full_html)} bytes).")

    # Symlinks
    symlinks = [
        "chapter6-maths-class5.html",
        "class5-maths-chapter6.html",
        "class5-the-dairy-farm.html",
        "the-dairy-farm-class5.html",
        "class5-maths-dairy-farm-lab.html",
        "class5-math-dairy-farm.html",
        "class5-dairy-farm-lab.html"
    ]
    target_rel = "class5-maths-the-dairy-farm.html"
    anim_dir = "public/animations"

    for sl in symlinks:
        sl_path = os.path.join(anim_dir, sl)
        if os.path.islink(sl_path) or os.path.exists(sl_path):
            os.remove(sl_path)
        os.symlink(target_rel, sl_path)
        print(f"Created symlink: {sl_path} -> {target_rel}")

    print("All Chapter 6 build operations completed successfully.")

if __name__ == "__main__":
    build_html()

