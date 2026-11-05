import sys
import os
import re

# Import data modules
sys.path.append(os.path.abspath(".agents"))
from class6_science_ch7_data import CHAPTER_META, SLIDES, QUIZ_QUESTIONS
from class6_science_ch7_sims import SIMULATORS
from class6_science_ch7_js import JS_CODE

output_file = "public/animations/class6-science-temperature-measurement.html"

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
    subtitle = s.get('subtitle', '')
    concept = s['concept_html']
    lecture_text = s['lecture_script']
    spoken_text = s['spoken_text']
    sim_html = SIMULATORS[slide_no]
    
    # Build checkpoints HTML
    cps_html = []
    for idx, cp in enumerate(s.get('checkpoints', [])):
        cp_id = f"{slide_no}-{idx+1}"
        opts_html = []
        for opt_idx, opt in enumerate(cp['options']):
            clean_exp = cp['explanation'].replace('"', '&quot;').replace("'", "&#39;")
            clean_ins = cp['study_insight'].replace('"', '&quot;').replace("'", "&#39;")
            full_exp = f"{clean_exp} <span class='text-slate-400 block mt-1'>💡 Study Insight: {clean_ins}</span>"
            opts_html.append(f'''
                <button onclick="checkCheckpoint('{cp_id}', {opt_idx}, {cp['correct']}, '{full_exp}')"
                        class="w-full text-left p-2.5 rounded-lg border border-slate-700/80 bg-slate-800/60 hover:bg-slate-700/80 text-xs text-slate-300 transition">
                    <span class="font-bold text-indigo-400 mr-1.5">{chr(65+opt_idx)}.</span> {opt}
                </button>
            ''')
        
        cps_html.append(f'''
            <div class="p-3.5 rounded-xl bg-slate-900/70 border border-slate-800/80 mb-3 shadow-inner">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Checkpoint {idx+1}</span>
                    <span id="cp-badge-{cp_id}" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700">Unsolved</span>
                </div>
                <p class="text-xs text-slate-200 mb-2.5 font-medium leading-relaxed">{cp['question']}</p>
                <div class="space-y-1.5">
                    {''.join(opts_html)}
                </div>
                <div id="cp-feedback-{cp_id}" style="display: none;"></div>
            </div>
        ''')
    
    slide_card = f'''
    <div id="slide-{slide_no}" class="slide-container" style="display: {'block' if slide_no == 1 else 'none'};">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <!-- Left Column: Theory & Classroom Audio Lecture & Checkpoints -->
            <div class="lg:col-span-5 space-y-4">
                <!-- Concept Card -->
                <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-xl backdrop-blur-sm">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Slide {slide_no} of 20</span>
                        <span class="text-xs font-medium text-slate-400">Class 6 • Chapter 7</span>
                    </div>
                    <h2 class="text-xl font-bold text-white mb-1 tracking-tight">{short_title}</h2>
                    <p class="text-xs text-indigo-300/80 font-medium mb-3">{subtitle}</p>
                    <div class="text-sm text-slate-300 leading-relaxed space-y-2">
                        {concept}
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
                        "{lecture_text}"
                    </p>
                    <!-- Hidden container holding full plain-text lecture to speak (excluding exercises) -->
                    <div id="slide-spoken-text-{slide_no}" style="display: none;">
                        {spoken_text}
                    </div>
                </div>

                <!-- Checkpoints (Exercises: NOT spoken in lecture) -->
                <div class="space-y-3">
                    <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                        <span>🎯</span>
                        <span>Interactive Mastery Checkpoints</span>
                    </h3>
                    {''.join(cps_html)}
                </div>
            </div>

            <!-- Right Column: Interactive Bespoke Simulator -->
            <div class="lg:col-span-7">
                {sim_html}
            </div>
        </div>
    </div>
    '''
    slides_html.append(slide_card)

# 2. Quiz Slides (17 to 20 - Mastery Challenges)
quiz_titles = {
    17: "Challenge 1",
    18: "Challenge 2",
    19: "Challenge 3",
    20: "Challenge 4"
}

for slide_no in range(17, 21):
    short_title = quiz_titles[slide_no]
    q_start = (slide_no - 17) * 10
    q_end = q_start + 10
    quiz_subset = QUIZ_QUESTIONS[q_start:q_end]
    quiz_desc = f"Test your understanding with Questions {q_start+1} through {q_end}. Select an answer for instant feedback and review step-by-step solutions."
    study_insight_quote = "Carefully analyze temperature definitions, clinical steps, least count formulas, zero parallax alignment, immersion rules, and phase plateaus before selecting your answer."

    q_cards_html = []
    for q in quiz_subset:
        q_id = q['id']
        q_opts = []
        clean_title = f"Question {q_id}: Temperature Measurement Mastery Challenge"
        clean_q = q['question'].replace("'", "&#39;").replace('"', '&quot;')
        clean_sol = q['solution_html'].replace("'", "&#39;").replace('"', '&quot;')

        for opt_idx, opt_text in enumerate(q['options']):
            q_opts.append(f'''
                <button onclick="selectQuizOption({q_id}, '{chr(65+opt_idx)}', '{chr(65+q['correct'])}', '{clean_title}', '{clean_q}', '{clean_sol}')"
                        class="w-full text-left p-3 rounded-xl border border-slate-700/80 bg-slate-800/60 hover:bg-slate-700 text-xs sm:text-sm text-slate-200 font-medium transition">
                    <span class="font-bold text-indigo-400 mr-2">{chr(65+opt_idx)}.</span> {opt_text}
                </button>
            ''')

        clean_correct_ans = q['options'][q['correct']].replace("'", "&#39;")

        q_cards_html.append(f'''
            <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-xl space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Question {q_id} of 40</span>
                    <span class="text-xs text-slate-400 font-medium">Concept Assessment</span>
                </div>
                <p class="text-sm font-medium text-slate-100 leading-relaxed">{q['question']}</p>
                <div id="q-options-{q_id}" class="space-y-2">
                    {''.join(q_opts)}
                </div>
                <div id="q-feedback-{q_id}" style="display: none;"></div>
                <div class="pt-1">
                    <button id="q-sol-btn-{q_id}" 
                            onclick="openSolutionModal('{clean_title}', '{clean_q}', '{clean_correct_ans}', '{clean_sol}')"
                            style="display: none;"
                            class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/30 transition flex items-center space-x-1.5">
                        <span>🔍</span>
                        <span>View Step-by-Step Solution</span>
                    </button>
                </div>
            </div>
        ''')

    slide_card = f'''
    <div id="slide-{slide_no}" class="slide-container" style="display: none;">
        <div class="max-w-4xl mx-auto space-y-6">
            <!-- Quiz Header Card -->
            <div class="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/60 via-slate-900/90 to-purple-950/60 border border-indigo-500/30 shadow-2xl backdrop-blur-md">
                <div class="flex items-center justify-between mb-3">
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Mastery Assessment • Slide {slide_no} of 20</span>
                    <span class="text-xs font-semibold text-slate-400">Questions {q_start+1} – {q_end} of 40</span>
                </div>
                <h2 class="text-2xl font-extrabold text-white mb-2">{short_title}</h2>
                <p class="text-sm text-slate-300 leading-relaxed">
                    {quiz_desc}
                </p>
                <div class="mt-4 p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 flex items-center justify-between">
                    <div class="flex items-center space-x-2 text-xs text-amber-300">
                        <span>💡 Study Insight:</span>
                        <span class="italic text-slate-300">"{study_insight_quote}"</span>
                    </div>
                </div>
            </div>

            <!-- 10 Questions Grid -->
            <div class="space-y-4">
                {''.join(q_cards_html)}
            </div>
        </div>
    </div>
    '''
    slides_html.append(slide_card)

# Build Dropdown Options for All 20 Slides
dropdown_options = []
for s in SLIDES:
    dropdown_options.append(f'<option value="{s["id"]}">Slide {s["id"]}: {s["title"]}</option>')
for slide_no in range(17, 21):
    dropdown_options.append(f'<option value="{slide_no}">Slide {slide_no}: {quiz_titles[slide_no]}</option>')

# Full Page Template
html_content = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CHAPTER_META['title']} - Class 6 Science Curiosity</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            850: '#151e2e',
                            950: '#0b0f19',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        pre, code {{
            font-family: 'JetBrains Mono', monospace;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-indigo-500/20 selection:text-indigo-300">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-slate-900/80 backdrop-blur-md border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold text-sm">
                    07
                </span>
                <div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight flex items-center space-x-2">
                        <span>{CHAPTER_META['title']}</span>
                        <span class="text-xs px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 hidden sm:inline-block">NCERT Class 6 Curiosity</span>
                    </h1>
                    <p class="text-xs text-slate-400 hidden sm:block">Classroom Audio Lectures & Interactive Laboratory • 20 High-Yield Modules</p>
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

        <!-- Global Linear Progress Bar -->
        <div class="w-full bg-slate-800 h-1">
            <div id="progressBar" class="bg-gradient-to-r from-indigo-500 via-sky-500 to-emerald-500 h-1 transition-all duration-300" style="width: 5%;"></div>
        </div>
    </header>

    <!-- Main Interactive Slides Workspace -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {''.join(slides_html)}
    </main>

    <!-- Fixed Bottom Sticky Control Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-900/90 backdrop-blur-md border-t border-slate-800 py-3 px-4 sm:px-6">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/80 transition flex items-center space-x-2">
                    <span>←</span>
                    <span>Previous</span>
                </button>
                <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl text-xs sm:text-sm font-bold bg-gradient-to-r from-indigo-500 to-sky-600 hover:from-indigo-400 hover:to-sky-500 text-white shadow-lg shadow-indigo-500/20 transition flex items-center space-x-2">
                    <span>Next</span>
                    <span>→</span>
                </button>
            </div>

            <!-- Terminal Slide Notice -->
            <div id="lastSlideNotice" style="display: none;" class="px-4 py-2 rounded-xl bg-emerald-950/70 border border-emerald-500/50 text-emerald-300 text-xs sm:text-sm font-bold tracking-wide animate-pulse text-center">
                You have reached the last slide of this chapter.
            </div>

            <!-- Slide Quick Switcher Dropdown -->
            <div class="flex items-center space-x-2 text-xs text-slate-400">
                <span>Jump to:</span>
                <select id="slideSelect" onchange="goToSlide(parseInt(this.value, 10))" class="bg-slate-900 border border-slate-800 text-slate-200 text-xs rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-indigo-500">
                    {''.join(dropdown_options)}
                </select>
            </div>
        </div>
    </footer>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" style="display: none; z-index: 99999 !important;" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
        <div class="max-w-xl w-full bg-slate-900 border border-indigo-500/40 rounded-2xl p-6 shadow-2xl relative space-y-4 max-h-[90vh] overflow-y-auto">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold p-1">
                ✕
            </button>
            <div class="flex items-center space-x-2">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">Thermometry Verification</span>
                <h3 id="modalTitle" class="text-base font-bold text-white">Solution</h3>
            </div>
            <div id="modalQuestion" class="text-xs sm:text-sm text-slate-300 bg-slate-950/60 p-3 rounded-xl border border-slate-800"></div>
            <div id="modalAnswer" class="text-xs sm:text-sm font-semibold text-emerald-400 bg-emerald-950/30 p-2.5 rounded-xl border border-emerald-500/30"></div>
            <div id="modalExplanation" class="text-xs sm:text-sm text-slate-300 leading-relaxed bg-slate-950/40 p-3.5 rounded-xl border border-slate-800 space-y-2"></div>
            <div class="pt-2 text-right">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-white transition">
                    Close Window
                </button>
            </div>
        </div>
    </div>

    <!-- Interactive JavaScript -->
    <script>
{JS_CODE}
    </script>
</body>
</html>
'''

# Verify zero raw LaTeX in compiled HTML
matches = raw_latex_pattern.findall(html_content)
if matches:
    print("FATAL ERROR: Found raw LaTeX in generated HTML:", set(matches))
    sys.exit(1)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully compiled {output_file} ({len(html_content)} bytes).")

