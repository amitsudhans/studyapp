# -*- coding: utf-8 -*-
"""
Build Class 3 Mathematics Chapter 1: What's in a Name? Interactive Animation Lab
Compiles public/animations/class3-maths-whats-in-a-name.html
and creates the 7 required symlinks.
Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class3_maths_ch1_data import slides
from class3_maths_ch1_sims import simulators

# Strict Validation Lists
FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv']
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VERIFYING CHAPTER 1 MATHS SLIDES DATA ===")
assert len(slides) == 20, f"Expected 20 slides, found {len(slides)}"

for idx, slide in enumerate(slides):
    sid = slide['id']
    title = slide['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    slide_str = json.dumps(slide)
    for name in FORBIDDEN_CHARACTERS:
        # Note: "deep" as an adjective ("deep river", "deepen") is permitted; check "Deep's" or uppercase story character
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str), f"Slide {sid} contains character name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    if sid <= 16:
        wc = len(slide['speech'].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words (must be 195-215)"
        assert len(slide['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in slide['checkpoints']:
            assert len(cp['options']) == 4, f"Slide {sid} checkpoint must have 4 options"
    else:
        assert len(slide['questions']) == 10, f"Slide {sid} must have 10 challenge questions"
        for q in slide['questions']:
            assert len(q['options']) == 4, f"Slide {sid} question {q.get('id')} must have 4 options"
            assert len(q['solution_steps']) == 3, f"Slide {sid} question {q.get('id')} must have 3 solution steps"

print("All 20 slides passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 3 Mathematics - Chapter 1: What's in a Name?</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #0f172a;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 9999px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-white">

    <!-- Top Fixed Header -->
    <header class="bg-slate-900/90 backdrop-blur sticky top-0 z-30 border-b border-slate-800 px-4 py-3 sm:px-6">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <!-- Brand / Context -->
            <div class="flex items-center gap-3 w-full sm:w-auto">
                <span class="text-2xl sm:text-3xl">🪪</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 3</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Joyful Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 1</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">What's in a Name? Interactive Animated Laboratory</h1>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center flex-wrap gap-2 w-full sm:w-auto justify-between sm:justify-end">
                <div class="flex items-center gap-1.5 bg-slate-800/90 border border-slate-700 rounded-xl px-2.5 py-1 text-xs">
                    <span class="text-slate-400 text-[11px] font-medium hidden md:inline">Voice:</span>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-2 py-1 focus:ring-1 focus:ring-cyan-500 outline-none max-w-[150px] sm:max-w-[210px] truncate" title="Select Indian Male Voice">
                        <option value="">Detecting Voice...</option>
                    </select>
                </div>
                <div id="audioControls" class="transition-opacity">
                    <button id="audioLectureBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white flex items-center gap-1.5 text-xs font-semibold transition shadow-sm" title="Listen to Pure Indian Male Teacher Lecture">
                        <span id="audioPlayIcon">🔊</span>
                        <span id="audioButtonText" class="text-xs font-bold">Teacher Sound Lecture</span>
                    </button>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-cyan-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700">Slide <span id="slideCounter">1 / 20</span></span>
                </div>
            </div>
        </div>

        <!-- Chapter Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-3">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-cyan-500 to-emerald-500 h-1 w-[5%] transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto w-full p-4 sm:p-6 flex-1">
__SLIDES_HTML__
    </main>

    <!-- Bottom Navigation Footer -->
    <footer class="bg-slate-900/90 backdrop-blur sticky bottom-0 border-t border-slate-800 px-4 py-3 z-30">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-semibold text-xs sm:text-sm flex items-center gap-2 transition shadow">
                <span>←</span> Previous
            </button>

            <!-- Slide 20 Terminal Invariant Container -->
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-cyan-500/20 border border-cyan-500/40 text-cyan-300 font-bold text-xs sm:text-sm text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs sm:text-sm flex items-center gap-2 transition shadow-md">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- 3-Step Scientific Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <h3 id="modalTitle" class="text-sm sm:text-base font-bold text-white tracking-tight">Mathematical Solution</h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center text-sm font-bold">✕</button>
            </div>
            <div id="modalContent" class="py-4"></div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold">Close</button>
            </div>
        </div>
    </div>

    <!-- Data Injection & Engine Script -->
    <script>
        window.slideCurriculumData = __SLIDES_JSON__;
        __JS_CODE__
    </script>
</body>
</html>
"""

def generate_slides_html():
    slides_html = []

    for s in slides:
        sid = s['id']
        title = s['title']
        badge = s.get('badge', '')
        desc = s.get('description', '')
        hidden_cls = "" if sid == 1 else "hidden"

        if sid <= 16:
            sim_markup = simulators.get(s['sim_id'], "<div class='p-4 text-center text-slate-500'>Simulator loading...</div>")

            # Format Checkpoints
            cp_html = []
            for cidx, cp in enumerate(s['checkpoints']):
                options_markup = []
                for opt_idx, opt in enumerate(cp['options']):
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    safe_ans = cp['ans'].replace("'", "\\'").replace('"', '&quot;')
                    options_markup.append(f"""
                        <button onclick="window.checkAnswer({sid}, {cidx}, {opt_idx}, '{safe_ans}')" data-opt-val="{safe_opt}" class="checkpoint-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-cyan-500/50 text-xs text-slate-300 transition flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_str = "\n".join(options_markup)

                safe_expl = cp['explanation'].replace('"', '&quot;')
                safe_q_speak = cp['q'].replace("'", "\\'").replace('"', '&quot;')
                cp_card = f"""
                <div id="cp-{sid}-{cidx}" class="checkpoint-card bg-slate-950/70 border border-slate-800 rounded-2xl p-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between gap-2 mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-5 h-5 rounded-md bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-[10px]">Q{cidx + 1}</span>
                                <span class="text-xs font-semibold text-white">{cp['q']}</span>
                            </div>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-cyan-400 hover:text-cyan-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
                        </div>
                        <div class="space-y-1.5 mt-3">
                            {opts_str}
                        </div>
                    </div>
                    <div id="fb-{sid}-{cidx}" class="hidden mt-3" data-explanation="{safe_expl}"></div>
                </div>
                """
                cp_html.append(cp_card)

            checkpoints_str = "\n".join(cp_html)

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-6 {hidden_cls}">
                <!-- Title Header -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-800">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="w-6 h-6 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                            <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                        </div>
                        <p class="text-xs text-slate-400">{desc}</p>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-cyan-300 border border-slate-700 font-semibold self-start sm:self-auto">{badge}</span>
                </div>

                <!-- Bespoke Simulator -->
                <div class="simulator-wrapper">
                    {sim_markup}
                </div>

                <!-- 2 Checkpoints -->
                <div class="space-y-3 pt-2">
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                        <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Concept Checkpoints</h4>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {checkpoints_str}
                    </div>
                </div>
            </div>
            """
            slides_html.append(slide_content)
        else:
            # Challenge Slides (17-20)
            questions_html = []
            for qidx, q in enumerate(s['questions']):
                opts_html = []
                for opt in q['options']:
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    safe_ans = q['ans'].replace("'", "\\'").replace('"', '&quot;')
                    safe_qid = q['id'].replace("'", "\\'")
                    opts_html.append(f"""
                        <button onclick="window.checkQuizAnswer('{safe_qid}', '{safe_opt}', '{safe_ans}')" data-opt-val="{safe_opt}" class="quiz-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-cyan-500/50 text-xs text-slate-300 transition flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_joined = "\n".join(opts_html)

                safe_expl = q['explanation'].replace('"', '&quot;')
                safe_q_speak = q['q'].replace("'", "\\'").replace('"', '&quot;')
                card = f"""
                <div id="quiz-q-{q['id']}" class="quiz-question-card bg-slate-950/80 border border-slate-800 rounded-2xl p-4 flex flex-col justify-between space-y-3">
                    <div>
                        <div class="flex items-start justify-between gap-2">
                            <span class="w-6 h-6 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs shrink-0">{qidx + 1}</span>
                            <p class="text-xs sm:text-sm font-semibold text-white flex-1">{q['q']}</p>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-cyan-400 hover:text-cyan-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
                        </div>
                        <div class="space-y-1.5 mt-3">
                            {opts_joined}
                        </div>
                    </div>
                    <div id="quiz-fb-{q['id']}" class="hidden" data-explanation="{safe_expl}"></div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-800/80 text-[11px]">
                        <span class="text-slate-500 italic">💡 Hint: {q['hint']}</span>
                        <button onclick="window.showSolutionModal('{q['id']}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 font-semibold transition">
                            Solution Walkthrough →
                        </button>
                    </div>
                </div>
                """
                questions_html.append(card)

            all_questions_html = "\n".join(questions_html)

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-6 {hidden_cls}">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-medium">10 Questions Multi-Choice Quiz</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {all_questions_html}
                </div>
            </div>
            """
            slides_html.append(slide_content)

    return "\n".join(slides_html)

# Read JS code from .agents/class3_maths_ch1_js.js
with open(os.path.join('.agents', 'class3_maths_ch1_js.js'), 'r', encoding='utf-8') as f:
    complete_js = f.read()

# Generate final HTML
print("Generating full animation lab HTML with Pure Indian Male Teacher Sound...")
slides_markup = generate_slides_html()
slides_json = json.dumps(slides, ensure_ascii=False)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__SLIDES_JSON__", slides_json)
final_html = final_html.replace("__JS_CODE__", complete_js)

output_dir = "public/animations"
os.makedirs(output_dir, exist_ok=True)
master_filename = "class3-maths-whats-in-a-name.html"
master_path = os.path.join(output_dir, master_filename)

with open(master_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation lab written to {master_path} ({len(final_html):,} bytes)")

# Create the 7 symlinks
symlinks = [
    "chapter1-maths-class3.html",
    "class3-maths-chapter1.html",
    "class3-whats-in-a-name.html",
    "whats-in-a-name-class3.html",
    "class3-maths-whats-in-a-name-lab.html",
    "class3-math-whats-in-a-name.html",
    "class3-whats-in-a-name-lab.html"
]

print("Creating symlinks...")
for link_name in symlinks:
    link_path = os.path.join(output_dir, link_name)
    if os.path.lexists(link_path):
        os.remove(link_path)
    os.symlink(master_filename, link_path)
    print(f"  Created symlink: {link_name} -> {master_filename}")

print("=== Class 3 Mathematics Chapter 1 Lab Build Complete! ===")

