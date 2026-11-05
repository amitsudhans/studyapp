# -*- coding: utf-8 -*-
"""
Build Class 4 Mathematics Chapter 5: Sharing and Measuring Animation Lab
Compiles public/animations/class4-maths-sharing-and-measuring.html
and creates the 7 required symlinks.
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class4_maths_ch5_data import slides
from class4_maths_ch5_sims import simulators
from class4_maths_ch5_js import js_code

# Strict Validation
HUMAN_NAMES = [
    'Ikra', 'Samina', 'Sumedha', 'Vinayak', 'Kumar', 'Paridhi', 'Idha', 'Karan',
    'Jaspreet', 'Gulnaz', 'Zoltán', 'Dienes', 'Mithali', 'Suzie', 'Bates',
    'Gundappa', 'Muniamma', 'Shirley', 'Shiv',
    'Mini', 'Jagat', 'Bholu', 'Rani', 'Preet',
    'Diksha', 'Raghav', 'Raman', 'Sheela', 'Sunita', 'Mary', 'Akira', 'Preetha', 'Adrit',
    'Rohan', 'Aarav', 'Ananya', 'Diya', 'Priya', 'Rahul', 'Amit', 'Neha', 'Sanjay', 'Vikram'
]

print("=== VERIFYING CHAPTER 5 SLIDES DATA ===")
assert len(slides) == 20, f"Expected 20 slides, found {len(slides)}"

for idx, slide in enumerate(slides):
    sid = slide['id']
    title = slide['title']
    print(f"Slide {sid}: {title}")

    # Check headings word length (1 to 3 words)
    words_in_title = len(title.split())
    assert 1 <= words_in_title <= 3, f"Slide {sid} title '{title}' has {words_in_title} words (must be 1-3)!"

    # Verify lecture word count for Slides 1-16 (195-215 words)
    if sid <= 16:
        lecture = slide.get('speech') or slide.get('lecture')
        wc = len(lecture.split())
        print(f"  Lecture words: {wc}")
        assert 195 <= wc <= 215, f"Slide {sid} lecture word count {wc} is outside 195-215!"
        assert len(slide['checkpoints']) == 2, f"Slide {sid} must have exactly 2 checkpoints!"
    else:
        quiz_items = slide.get('quiz') or slide.get('questions')
        assert len(quiz_items) == 10, f"Slide {sid} must have exactly 10 questions!"

    # Check zero human names in entire slide
    slide_str = json.dumps(slide)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + name + r'\b', slide_str, re.IGNORECASE), f"Forbidden human name '{name}' detected in slide {sid}!"

print("All slides passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 4 Mathematics — Chapter 5: Sharing and Measuring Master Lab</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        h1, h2, h3, h4, .font-heading {
            font-family: 'Outfit', sans-serif;
        }
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur sticky top-0 z-40 border-b border-slate-800 px-4 py-3">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <span class="text-2xl sm:text-3xl">🍰</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 4</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Joyful Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 5</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">Sharing and Measuring Master Lab</h1>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center gap-2.5 w-full sm:w-auto justify-between sm:justify-end">
                <button id="audioLectureBtn" onclick="playAudioLecture()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 flex items-center gap-2 text-xs font-semibold transition shadow-sm">
                    <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    <span class="text-xs font-bold text-emerald-300">Listen Teacher Lecture</span>
                </button>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-amber-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700">Slide <span id="currentSlideNum">1</span> of 20</span>
                </div>
            </div>
        </div>
        <!-- Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-2.5 rounded-full overflow-hidden">
            <div id="chapterProgressBar" class="bg-gradient-to-r from-amber-500 via-indigo-500 to-emerald-500 h-full w-[5%] transition-all duration-300 ease-out"></div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-5">
        __SLIDES_HTML__
    </main>

    <!-- Bottom Navigation Footer -->
    <footer class="bg-slate-900/90 backdrop-blur sticky bottom-0 z-40 border-t border-slate-800 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
            <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-semibold text-xs sm:text-sm flex items-center gap-2 transition shadow">
                <span>←</span> Previous
            </button>

            <!-- Slide 20 Terminal Invariant Container -->
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-amber-500/20 border border-amber-500/40 text-amber-300 font-bold text-xs sm:text-sm text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs sm:text-sm flex items-center gap-2 transition shadow-md">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- Step-by-Step Solution Pop-up Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-3 bg-slate-950/80 backdrop-blur-sm">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-2xl w-full max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between p-4 border-b border-slate-800">
                <h3 id="solutionModalTitle" class="font-bold text-amber-400 text-base flex items-center gap-2">
                    <span>💡</span> Step-by-Step Solution
                </h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center text-sm font-bold transition">✕</button>
            </div>
            <div id="solutionModalContent" class="p-4 sm:p-5 overflow-y-auto space-y-3">
                <!-- Injected via openSolutionModal() -->
            </div>
            <div class="p-3 border-t border-slate-800 bg-slate-950/60 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs transition">Close</button>
            </div>
        </div>
    </div>

    <!-- Embedded Client Data & JS Engine -->
    <script>
        const SLIDES = __SLIDES_JSON__;
    </script>
    <script>
        __JS_CODE__
    </script>
</body>
</html>
"""

def generate_slides_html():
    slides_html = []

    for idx, slide in enumerate(slides):
        sid = slide['id']
        title = slide['title']
        section = slide.get('section', '')
        hidden_class = "" if sid == 1 else "hidden"

        if sid <= 16:
            # Theory + Simulator Slide
            lecture = slide.get('speech') or slide.get('lecture')
            sim_markup = simulators.get(sid, f"<div class='p-4 text-center text-slate-400'>Simulator {sid}</div>")

            cp_html = []
            for cpidx, cp in enumerate(slide['checkpoints']):
                q_text = cp.get('q') or cp.get('question')
                ans_idx = cp.get('ans') if cp.get('ans') is not None else cp.get('answer')
                exp_text = cp.get('exp') or cp.get('explanation')

                opts_html = "".join([
                    f"<button onclick='checkCheckpoint({sid}, {cpidx}, {oidx})' class='cp-btn-{sid}-{cpidx} text-left p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-medium text-xs transition'>{opt}</button>"
                    for oidx, opt in enumerate(cp['options'])
                ])
                cp_html.append(f"""
                <div id="cp-{sid}-{cpidx}" class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 space-y-2">
                    <div class="flex items-center gap-2 text-xs font-bold text-amber-400">
                        <span>🔍</span> Checkpoint {cpidx + 1}
                    </div>
                    <p class="text-xs text-slate-200 font-medium">{q_text}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                        {opts_html}
                    </div>
                    <div id="cp-fb-{sid}-{cpidx}" class="hidden"></div>
                </div>
                """)

            checkpoints_rendered = "\n".join(cp_html)

            slide_content = f"""
            <div id="slide-{sid}" class="slide-pane {hidden_class} space-y-4">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-medium">{section}</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
                    <!-- Left Column: Spoken Lecture & Checkpoints -->
                    <div class="lg:col-span-6 space-y-3">
                        <!-- Lecture Card -->
                        <div class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 space-y-3 shadow-md">
                            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                                    <span>📖</span> Spoken Classroom Lecture
                                </h3>
                                <span class="text-[11px] text-slate-400 font-medium">Authentic Indian Male Narration</span>
                            </div>
                            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed text-justify">
                                {lecture}
                            </p>
                        </div>

                        <!-- Checkpoints Container -->
                        <div class="space-y-2.5">
                            {checkpoints_rendered}
                        </div>
                    </div>

                    <!-- Right Column: Interactive Bespoke Simulator -->
                    <div class="lg:col-span-6">
                        {sim_markup}
                    </div>
                </div>
            </div>
            """
            slides_html.append(slide_content)

        else:
            # Mastery Challenge Slides (17 to 20, 10 Questions Each)
            challenge_num = sid - 16
            questions_rendered = []
            quiz_list = slide.get('quiz') or slide.get('questions')

            for qidx, q in enumerate(quiz_list):
                q_id = q['id']
                q_text = q['q']
                opts_html = "".join([
                    f"<button onclick='selectQuizOption({q_id}, {oidx})' class='quiz-opt-btn-{q_id} text-left p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-medium text-xs transition'>{chr(65 + oidx)}. {opt}</button>"
                    for oidx, opt in enumerate(q['options'])
                ])

                questions_rendered.append(f"""
                <div id="quiz-card-{q_id}" class="bg-slate-900 border border-slate-800 rounded-2xl p-4 space-y-3 shadow-sm">
                    <div class="flex items-start justify-between gap-2 border-b border-slate-800 pb-2">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-amber-500/20 text-amber-300 text-xs font-bold flex items-center justify-center shrink-0">{q_id}</span>
                            <span class="font-bold text-slate-100 text-xs sm:text-sm">{q_text}</span>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                        {opts_html}
                    </div>

                    <div id="quiz-fb-{q_id}" class="hidden"></div>
                </div>
                """)

            all_q_html = "\n".join(questions_rendered)

            slide_content = f"""
            <div id="slide-{sid}" class="slide-pane {hidden_class} space-y-4">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Questions {(challenge_num-1)*10 + 1} to {challenge_num*10}</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {all_q_html}
                </div>
            </div>
            """
            slides_html.append(slide_content)

    return "\n".join(slides_html)

# Build HTML
slides_markup = generate_slides_html()
slides_json_str = json.dumps(slides)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__SLIDES_JSON__", slides_json_str)
final_html = final_html.replace("__JS_CODE__", js_code)

output_path = "public/animations/class4-maths-sharing-and-measuring.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation file successfully compiled: {output_path} ({len(final_html)} bytes)")

# Create the 7 Symlinks
SYMLINKS = [
    "chapter5-maths-class4.html",
    "class4-maths-chapter5.html",
    "class4-sharing-and-measuring.html",
    "sharing-and-measuring-class4.html",
    "class4-maths-sharing-and-measuring-lab.html",
    "class4-math-sharing-and-measuring.html",
    "class4-sharing-measuring-lab.html"
]

target_file = "class4-maths-sharing-and-measuring.html"
for sl in SYMLINKS:
    sl_path = os.path.join("public/animations", sl)
    if os.path.islink(sl_path) or os.path.exists(sl_path):
        os.remove(sl_path)
    os.symlink(target_file, sl_path)
    print(f"Created symlink: {sl} -> {target_file}")

print("All 7 symlinks successfully generated!")

