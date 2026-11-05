"""
Builder for NCERT Class 6 Science Chapter 10: Living Creatures: Exploring their Characteristics
Compiles the 20-slide interactive animated lab HTML file with zero raw LaTeX, Web Speech API Indian Male voice, and 16 bespoke simulators.
"""

import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from class6_science_ch10_data import CHAPTER_META, SLIDES, QUIZ_QUESTIONS
from class6_science_ch10_sims import SIMULATORS
from class6_science_ch10_js import JS_CODE

output_file = "public/animations/class6-science-living-creatures.html"

# Verify all components have zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def verify_no_latex(text, context):
    if not isinstance(text, str):
        return
    matches = raw_latex_pattern.findall(text)
    if matches:
        raise ValueError(f"Found raw LaTeX in {context}: {set(matches)}")

verify_no_latex(CHAPTER_META['title'], "CHAPTER_META title")
for s in SLIDES:
    verify_no_latex(s['title'], f"Slide {s['id']} title")
    verify_no_latex(s['concept_html'], f"Slide {s['id']} concept_html")
    verify_no_latex(s['lecture_script'], f"Slide {s['id']} lecture_script")
    verify_no_latex(s['spoken_text'], f"Slide {s['id']} spoken_text")
    for cp in s.get('checkpoints', []):
        verify_no_latex(cp['question'], f"Slide {s['id']} cp question")
        verify_no_latex(cp['explanation'], f"Slide {s['id']} cp explanation")
        verify_no_latex(cp['study_insight'], f"Slide {s['id']} cp study_insight")

for q in QUIZ_QUESTIONS:
    verify_no_latex(q['question'], f"Quiz Q{q['id']} question")
    verify_no_latex(q['explanation'], f"Quiz Q{q['id']} explanation")
    verify_no_latex(q['solution_html'], f"Quiz Q{q['id']} solution_html")

for sim_id, sim_code in SIMULATORS.items():
    verify_no_latex(sim_code, f"Simulator {sim_id}")

verify_no_latex(JS_CODE, "JS_CODE")

print("VERIFIED PASS: All data zero raw LaTeX verified!")

# Build HTML Slides
slides_html = []

# 1. Concept Slides (1 to 16)
for s in SLIDES:
    slide_no = s['id']
    short_title = s['title']
    subtitle = s['subtitle']
    concept_html = s['concept_html']
    spoken_text = s['spoken_text']
    sim_html = SIMULATORS.get(slide_no, f"<div class='p-4 text-center text-slate-500'>Simulator {slide_no}</div>")

    # Render Checkpoints
    checkpoints_html = []
    for idx, cp in enumerate(s.get('checkpoints', [])):
        cp_id = f"{slide_no}-{idx+1}"
        opts_html = []
        for opt_idx, opt_text in enumerate(cp['options']):
            escaped_expl = cp['explanation'].replace("'", "&#39;").replace('"', '&quot;')
            opts_html.append(f"""
                <button onclick="checkCheckpoint('{cp_id}', {opt_idx}, {cp['correct']}, '{escaped_expl}')"
                        class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs text-slate-200 border border-slate-700/60 transition flex items-start space-x-2">
                    <span class="font-bold text-indigo-400 shrink-0">{'ABCD'[opt_idx]}.</span>
                    <span>{opt_text}</span>
                </button>
            """)

        checkpoints_html.append(f"""
            <div class="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 space-y-2.5">
                <div class="flex items-center justify-between">
                    <span class="text-[11px] font-bold text-indigo-400 uppercase tracking-wider">Checkpoint {slide_no}.{idx+1}</span>
                    <span class="text-[10px] text-slate-400 italic">Formative Inquiry</span>
                </div>
                <p class="text-xs font-medium text-white leading-relaxed">{cp['question']}</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                    {''.join(opts_html)}
                </div>
                <div id="cp-feedback-{cp_id}" class="hidden"></div>
                <div class="p-2 rounded-lg bg-indigo-950/30 border border-indigo-500/20 text-[11px] text-indigo-300">
                    💡 <strong>Study Insight:</strong> {cp['study_insight']}
                </div>
            </div>
        """)

    all_cp_html = "".join(checkpoints_html)

    slide_block = f"""
    <div id="slide-{slide_no}" class="slide-container" style="display: {'block' if slide_no == 1 else 'none'};">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
            <!-- Left Column: Content & Checkpoints (7 cols) -->
            <div class="lg:col-span-7 space-y-4">
                <!-- Theory Card -->
                <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-xl backdrop-blur-sm">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Slide {slide_no} of 20</span>
                        <span class="text-xs font-medium text-slate-400">Class 6 • Chapter 10</span>
                    </div>
                    <h2 class="text-xl font-bold text-white mb-1 tracking-tight">{short_title}</h2>
                    <p class="text-xs text-indigo-300/80 font-medium mb-3">{subtitle}</p>
                    <div class="text-sm text-slate-300 leading-relaxed space-y-2">
                        {concept_html}
                    </div>
                </div>

                <!-- Classroom Audio Lecture Card (Full spoken explanation, zero lecturer names) -->
                <div class="p-4 rounded-2xl bg-gradient-to-br from-indigo-950/70 via-slate-900/90 to-slate-950/80 border border-indigo-500/40 shadow-lg space-y-3">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <span class="text-base sm:text-lg">🎙️</span>
                            <span class="text-xs font-bold text-indigo-300 uppercase tracking-wider">Classroom Audio Lecture</span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span id="slide-audio-badge-{slide_no}" class="px-2 py-0.5 rounded text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Audio Lecture Ready</span>
                            <button id="slide-audio-btn-{slide_no}" onclick="startLectureSpeech(document.getElementById('slide-spoken-text-{slide_no}').textContent, {slide_no})"
                                    class="px-3 py-1.5 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 text-xs font-bold flex items-center space-x-1.5 border border-indigo-500/30 transition shadow-sm"
                                    title="Listen to Full Slide Lecture">
                                <span>▶</span>
                                <span>Listen to Full Lecture</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm text-indigo-100/90 leading-relaxed italic border-l-2 border-indigo-500/50 pl-3">
                        "{spoken_text}"
                    </p>
                    <!-- Hidden container holding full plain-text lecture to speak (excluding exercises) -->
                    <div id="slide-spoken-text-{slide_no}" style="display: none;">
                        {spoken_text}
                    </div>
                </div>

                <!-- Checkpoints Section -->
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Interactive Formative Checkpoints</span>
                        <span class="text-xs text-indigo-400 font-semibold">2 Inquiries</span>
                    </div>
                    {all_cp_html}
                </div>
            </div>

            <!-- Right Column: Bespoke SVG/HTML Interactive Simulator (5 cols) -->
            <div class="lg:col-span-5 space-y-4">
                <div class="sticky top-20">
                    <div class="p-1 rounded-2xl bg-gradient-to-br from-indigo-500/30 via-slate-800 to-indigo-500/10 shadow-xl">
                        <div class="p-4 rounded-[14px] bg-slate-900 border border-slate-800/80">
                            <div class="flex items-center justify-between mb-3 pb-2 border-b border-slate-800">
                                <div class="flex items-center space-x-2">
                                    <span class="text-base">🧪</span>
                                    <span class="text-xs font-bold text-white uppercase tracking-wider">Interactive Laboratory</span>
                                </div>
                                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Active Sim {slide_no}</span>
                            </div>
                            {sim_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    slides_html.append(slide_block)

# 2. Mastery Challenge Slides (17 to 20)
for challenge_idx in range(4):
    slide_no = 17 + challenge_idx
    short_title = f"Challenge {challenge_idx + 1}"
    q_start = challenge_idx * 10
    q_end = q_start + 10
    quiz_subset = QUIZ_QUESTIONS[q_start:q_end]
    quiz_desc = f"Test your understanding with Questions {q_start+1} through {q_end}. Select an answer for instant feedback and review step-by-step solutions."
    study_insight_quote = "Carefully analyze biological criteria, cellular respiration, response to stimuli, seed germination parameters, and life cycles before selecting your answer."

    q_cards_html = []
    for q in quiz_subset:
        q_id = q['id']
        q_opts = []
        clean_title = f"Question {q_id}: Living Creatures Mastery Challenge"
        clean_q = q['question'].replace("'", "&#39;").replace('"', '&quot;')
        clean_sol = q['solution_html'].replace("'", "&#39;").replace('"', '&quot;')

        for opt_idx, opt_text in enumerate(q['options']):
            escaped_expl = q['explanation'].replace("'", "&#39;").replace('"', '&quot;')
            q_opts.append(f"""
                <button onclick="selectQuizOption({q_id}, {opt_idx}, {q['answer']}, '{clean_title}', '{clean_q}', '{escaped_expl}')"
                        class="quiz-opt-btn w-full text-left p-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-medium text-slate-200 border border-slate-800 hover:border-slate-700 transition flex items-start space-x-2.5">
                    <span class="w-5 h-5 rounded-md bg-slate-800 text-indigo-400 font-bold flex items-center justify-center shrink-0 text-[11px]">{'ABCD'[opt_idx]}</span>
                    <span>{opt_text}</span>
                </button>
            """)

        q_cards_html.append(f"""
            <div id="q-card-{q_id}" class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/80 shadow-md space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Question {q_id} of 40</span>
                    <button id="q-sol-btn-{q_id}" onclick="openSolutionModal('{clean_title}', '{clean_q}', '{clean_sol}')"
                            class="hidden px-2.5 py-1 rounded-lg text-xs font-bold bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/30 transition items-center space-x-1">
                        <span>💡</span>
                        <span>View Solution</span>
                    </button>
                </div>
                <p class="text-sm font-semibold text-white leading-relaxed">{q['question']}</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                    {''.join(q_opts)}
                </div>
                <div id="q-fb-{q_id}" class="hidden"></div>
            </div>
        """)

    all_q_cards = "".join(q_cards_html)

    quiz_slide_block = f"""
    <div id="slide-{slide_no}" class="slide-container" style="display: none;">
        <div class="max-w-4xl mx-auto space-y-5">
            <!-- Challenge Header -->
            <div class="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/80 via-slate-900 to-slate-900 border border-indigo-500/30 shadow-xl">
                <div class="flex items-center justify-between mb-2">
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Slide {slide_no} of 20</span>
                    <span class="text-xs font-medium text-slate-400">Class 6 • Chapter 10</span>
                </div>
                <h2 class="text-2xl font-extrabold text-white mb-2">{short_title}</h2>
                <p class="text-sm text-slate-300 leading-relaxed mb-3">{quiz_desc}</p>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 text-xs text-indigo-200">
                    💡 <strong>Mastery Tip:</strong> {study_insight_quote}
                </div>
            </div>

            <!-- Quiz Questions Grid -->
            <div class="space-y-4">
                {all_q_cards}
            </div>

            {'<div id="lastSlideNotice" class="hidden p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-center my-6"><span class="text-amber-300 font-bold text-sm">You have reached the last slide of this chapter.</span></div>' if slide_no == 20 else ''}
        </div>
    </div>
    """
    slides_html.append(quiz_slide_block)

all_slides_html = "\n".join(slides_html)

# Quick Jump Dropdown Options
jump_options = "".join([f'<option value="{s["id"]}">Slide {s["id"]}: {s["title"]}</option>' for s in SLIDES])
jump_options += "".join([f'<option value="{17+i}">Slide {17+i}: Challenge {i+1}</option>' for i in range(4)])

# Assemble Complete HTML File
full_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 6 Science — Chapter 10: Living Creatures: Exploring their Characteristics</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{ 850: '#152033', 950: '#070d19' }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #030712;
            color: #f3f4f6;
        }}
        code, pre {{
            font-family: 'Fira Code', monospace;
        }}
        .slide-container {{
            animation: fadeIn 0.3s ease-in-out;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 selection:bg-indigo-500 selection:text-white">

    <!-- Global App Header -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold text-sm">
                    10
                </span>
                <div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight flex items-center space-x-2">
                        <span>NCERT Class 6 Science</span>
                        <span class="text-slate-500">•</span>
                        <span class="text-indigo-400">Chapter 10</span>
                    </h1>
                    <p class="text-xs text-slate-400 hidden sm:block">Living Creatures: Exploring their Characteristics</p>
                </div>
            </div>

            <!-- Global Audio Lecture Player & Slide Progress -->
            <div class="flex items-center space-x-3">
                <button id="globalAudioBtn" onclick="toggleCurrentSlideLecture()"
                        class="px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/30 flex items-center space-x-1.5 transition">
                    <span>🔊</span>
                    <span>Listen to Lecture</span>
                </button>
                <span id="slideCounter" class="text-xs sm:text-sm font-semibold text-slate-300 bg-slate-800/80 px-3 py-1.5 rounded-xl border border-slate-700/60">
                    1 / 20
                </span>
            </div>
        </div>
    </header>

    <!-- Main Slide Body -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {all_slides_html}
    </main>

    <!-- Navigation Footer Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-slate-800 py-3">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
            <button id="prevBtn" onclick="prevSlide()" disabled
                    class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-slate-800 hover:bg-slate-700 text-white border border-slate-700/80 transition flex items-center space-x-1.5">
                <span>←</span>
                <span>Previous</span>
            </button>

            <!-- Quick Jump Dropdown -->
            <div class="flex items-center space-x-2 text-xs text-slate-400">
                <span>Jump to:</span>
                <select id="slideSelect" onchange="goToSlide(parseInt(this.value, 10))" class="bg-slate-900 border border-slate-800 text-slate-200 text-xs rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-indigo-500">
                    {jump_options}
                </select>
            </div>

            <button id="nextBtn" onclick="nextSlide()"
                    class="px-5 py-2 rounded-xl text-xs sm:text-sm font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30 transition flex items-center space-x-1.5">
                <span>Next</span>
                <span>→</span>
            </button>
        </div>
    </footer>

    <!-- Solution Modal Popup -->
    <div id="solutionModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
        <div class="max-w-lg w-full bg-slate-900 rounded-2xl border border-slate-800 shadow-2xl p-6 space-y-4 relative">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold">
                ✕
            </button>
            <div class="flex items-center space-x-2">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">Life Sciences Verification</span>
                <h3 id="modalTitle" class="text-base font-bold text-white">Solution</h3>
            </div>
            <div id="modalQuestion" class="text-xs sm:text-sm text-slate-300 bg-slate-950/60 p-3 rounded-xl border border-slate-800"></div>
            <div id="modalSolution" class="text-xs sm:text-sm text-slate-200 leading-relaxed bg-indigo-950/30 p-3.5 rounded-xl border border-indigo-500/30"></div>
            <div class="text-right pt-2">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-white transition">
                    Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Interactive JavaScript Engine -->
    <script>
{JS_CODE}
    </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully compiled {output_file} ({len(full_html)} bytes).")

# Create symlinks
symlinks = [
    "public/animations/chapter10-science-class6.html",
    "public/animations/class6-science-chapter10.html",
    "public/animations/class6-living-creatures.html",
    "public/animations/living-creatures-class6.html",
    "public/animations/class6-living-creatures-characteristics.html",
    "public/animations/class6-science-living-creatures-characteristics.html",
    "public/animations/class6-science-living-creatures-lab.html"
]

target = "class6-science-living-creatures.html"
for sym in symlinks:
    if os.path.exists(sym) or os.path.islink(sym):
        os.remove(sym)
    os.symlink(target, sym)
    print(f"Created symlink: {sym} -> {target}")

print("All build operations completed successfully.")

