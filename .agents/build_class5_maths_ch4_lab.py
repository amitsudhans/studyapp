#!/usr/bin/env python3
"""
Compile public/animations/class5-maths-we-the-travellers-2.html
and create 7 symlinks for NCERT Class 5 Mathematics - Chapter 4: We the Travellers - II
"""
import os
import json
import re
from class5_maths_ch4_data import slides_data
from class5_maths_ch4_sims import simulators
from class5_maths_ch4_js import js_code

def build_html():
    # Final verification on data
    for s in slides_data:
        words = s["heading"].split()
        assert 1 <= len(words) <= 3, f"Heading '{s['heading']}' exceeds 3 words!"
        
        # Verify zero raw LaTeX
        corpus = s["heading"] + " " + s["tagline"] + " " + s["audio_text"]
        for tb in s.get("theory_blocks", []):
            corpus += " " + tb["title"] + " " + tb["content"]
        for cp in s.get("checkpoints", []):
            corpus += " " + cp["question"] + " " + " ".join(cp["options"]) + " " + cp["feedback"]
        for q in s.get("quizzes", []):
            corpus += " " + q["question"] + " " + " ".join(q["options"]) + " " + q["solution_html"]
            
        latex_matches = re.findall(r"\\(?:frac|times|div|pm|text|cdot|\$)|(?<!\\)\$[^$]+\$", corpus)
        if latex_matches:
            raise ValueError(f"Raw LaTeX detected on Slide {s['id']}: {latex_matches}")

    print("VERIFIED PASS: All Chapter 4 Mathematics data zero raw LaTeX verified!")

    slides_html = []
    for s in slides_data:
        slide_id = s["id"]
        is_quiz = 17 <= slide_id <= 20

        # Header of the slide
        header_html = f"""
        <div class="mb-6 pb-4 border-b border-slate-700/60 flex flex-col md:flex-row md:items-center justify-between gap-3">
            <div>
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full text-xs font-semibold bg-gradient-to-r {s['color']} text-white shadow-sm mb-2">
                    <span>{s['badge']}</span>
                </div>
                <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
                    {s['heading']}
                </h2>
                <p class="text-sm sm:text-base text-slate-300 mt-1 font-medium">{s['tagline']}</p>
            </div>
            <div class="flex items-center gap-2 self-start md:self-auto">
                <button onclick="playCurrentSlideAudio()" class="px-3.5 py-2 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-slate-950 font-bold rounded-xl text-xs sm:text-sm flex items-center gap-2 shadow-md transition transform active:scale-95">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                    <span>Listen Classroom Lecture</span>
                </button>
            </div>
        </div>
        """

        if not is_quiz:
            # Theory & Simulator layout
            theory_cards = []
            for tb in s.get("theory_blocks", []):
                theory_cards.append(f"""
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700/60 shadow-sm hover:border-amber-500/40 transition">
                    <div class="flex items-center gap-2.5 mb-2">
                        <span class="text-xl">{tb['icon']}</span>
                        <h3 class="text-sm font-bold text-white tracking-wide">{tb['title']}</h3>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed font-normal">{tb['content']}</p>
                </div>
                """)

            sim_markup = simulators.get(slide_id, '<div class="p-4 text-center text-slate-500">Simulator Loading...</div>')

            checkpoints_html = []
            for cp_idx, cp in enumerate(s.get("checkpoints", [])):
                opt_buttons = []
                for opt_idx, opt in enumerate(cp["options"]):
                    is_correct_bool = "true" if opt_idx == cp["correct"] else "false"
                    fb_escaped = cp["feedback"].replace("'", "\\'")
                    opt_buttons.append(f"""
                    <button onclick="handleCheckpoint({slide_id}, {cp_idx}, {opt_idx}, {is_correct_bool}, '{fb_escaped}')" class="w-full text-left p-2.5 rounded-lg bg-slate-800/90 hover:bg-slate-700/90 border border-slate-700 text-slate-200 text-xs font-medium transition flex items-center gap-2">
                        <span class="w-5 h-5 rounded-full bg-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-300 shrink-0">{chr(65 + opt_idx)}</span>
                        <span>{opt}</span>
                    </button>
                    """)
                checkpoints_html.append(f"""
                <div class="p-4 rounded-xl bg-slate-800/60 border border-slate-700/70">
                    <div class="flex items-center gap-2 mb-2.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">CHECKPOINT {cp_idx + 1}</span>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-3">{cp['question']}</p>
                    <div id="cp-{slide_id}-{cp_idx}-options" class="space-y-2">
                        {"".join(opt_buttons)}
                    </div>
                    <div id="cp-{slide_id}-{cp_idx}-fb" class="hidden mt-2 p-2.5 rounded-lg text-xs font-medium"></div>
                </div>
                """)

            slide_body = f"""
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Theory & Checkpoints Column -->
                <div class="lg:col-span-6 flex flex-col gap-4">
                    <div class="grid grid-cols-1 gap-3">
                        {"".join(theory_cards)}
                    </div>
                    <div class="mt-2 space-y-3">
                        <h4 class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                            <span class="inline-block w-2 h-2 rounded-full bg-amber-400"></span>
                            Formative Concept Checkpoints (Silent Practice)
                        </h4>
                        {"".join(checkpoints_html)}
                    </div>
                </div>

                <!-- Simulator Column -->
                <div class="lg:col-span-6 flex flex-col">
                    <div class="sticky top-20">
                        {sim_markup}
                    </div>
                </div>
            </div>
            """
        else:
            # 10 Questions Quiz Challenge
            quiz_cards = []
            for q_idx, q in enumerate(s.get("quizzes", [])):
                opt_buttons = []
                for opt_idx, opt in enumerate(q["options"]):
                    is_corr_bool = "true" if opt_idx == q["correct"] else "false"
                    opt_buttons.append(f"""
                    <button onclick="handleQuizOption({slide_id}, {q_idx}, {opt_idx}, {is_corr_bool})" class="w-full text-left p-2.5 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 text-slate-200 text-xs font-medium transition flex items-center gap-2">
                        <span class="w-5 h-5 rounded-full bg-slate-700 flex items-center justify-center text-[10px] font-bold text-slate-300 shrink-0">{chr(65 + opt_idx)}</span>
                        <span>{opt}</span>
                    </button>
                    """)

                quiz_cards.append(f"""
                <div class="p-4 rounded-xl bg-slate-800/70 border border-slate-700/70 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">QUESTION {q_idx + 1}</span>
                            <button id="quiz-{slide_id}-{q_idx}-solBtn" onclick="showQuizSolution({slide_id}, {q_idx})" class="hidden px-2 py-0.5 text-[11px] font-semibold text-amber-300 hover:text-amber-200 bg-amber-950/60 border border-amber-500/30 rounded transition">
                                View Solution 💡
                            </button>
                        </div>
                        <p class="text-xs sm:text-sm font-semibold text-white mb-3">{q['question']}</p>
                        <div id="quiz-{slide_id}-{q_idx}-options" class="space-y-1.5">
                            {"".join(opt_buttons)}
                        </div>
                    </div>
                </div>
                """)

            slide_body = f"""
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {"".join(quiz_cards)}
            </div>
            """

        slides_html.append(f"""
        <div id="slide-{slide_id}" class="slide-container {'hidden' if slide_id > 1 else ''} bg-slate-900/80 backdrop-blur-md rounded-2xl p-5 sm:p-8 border border-slate-800 shadow-2xl">
            {header_html}
            {slide_body}
        </div>
        """)

    # 20 Navigation Dots
    nav_dots = []
    for i in range(1, 21):
        nav_dots.append(f'<button id="dot-{i}" onclick="goToSlide({i})" title="Slide {i}" class="w-2 h-2 rounded-full bg-slate-600 hover:bg-slate-400 transition-all"></button>')

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 5 Mathematics • Chapter 4 • We the Travellers - II Master Lab</title>
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
        /* Custom scrollbar */
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=mathematics&class=class5" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition" title="Return to Class 5 Mathematics">
                    <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
                </a>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30">CLASS 5 MATHS</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 4</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight">We the Travellers - II • Master Laboratory</h1>
                </div>
            </div>

            <!-- Voice Selector & Classroom Audio Bar -->
            <div class="flex items-center gap-3 flex-wrap justify-end">
                <div class="flex items-center gap-1.5 bg-slate-800/80 px-2.5 py-1.5 rounded-xl border border-slate-700">
                    <span class="text-xs text-slate-400 font-medium">Teacher Voice:</span>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-slate-900 text-xs text-slate-200 rounded-lg px-2 py-1 border border-slate-700 focus:outline-none focus:border-amber-400 max-w-[200px] truncate">
                        <option value="">Detecting Pure Male Teacher Voice...</option>
                    </select>
                </div>

                <button id="mainAudioBtn" onclick="toggleAudio()" class="px-3.5 py-1.5 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-slate-950 font-bold rounded-xl text-xs sm:text-sm flex items-center gap-2 shadow-md transition transform active:scale-95">
                    <span id="audioPlayIcon" class="w-4 h-4 fill-current"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>
                    <span id="audioPauseIcon" class="hidden w-4 h-4 fill-current"><svg viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg></span>
                    <span id="audioBtnText">Listen Lecture</span>
                    <span id="audioPulse" class="hidden w-2 h-2 rounded-full bg-slate-950 animate-ping"></span>
                </button>
            </div>
        </div>

        <!-- Progress bar line -->
        <div class="w-full bg-slate-800 h-1">
            <div id="progressFill" class="bg-gradient-to-r from-amber-400 via-orange-500 to-rose-500 h-1 w-0 transition-all duration-300"></div>
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
                <span id="slideCounter" class="font-mono text-xs font-bold text-amber-400 bg-amber-950/60 px-3 py-1 rounded-lg border border-amber-500/30">
                    Slide 1 of 20
                </span>
                <div class="hidden md:flex items-center gap-1.5">
                    {"".join(nav_dots)}
                </div>
            </div>

            <div class="flex items-center gap-3">
                <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs sm:text-sm font-bold border border-slate-700 flex items-center gap-1.5 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    <span>Previous</span>
                </button>

                <button id="nextBtn" onclick="nextSlide()" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-slate-950 text-xs sm:text-sm font-extrabold flex items-center gap-1.5 shadow-lg transition">
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
                <h3 id="solutionModalTitle" class="text-base font-bold text-white flex items-center gap-2">
                    <span class="text-amber-400">💡</span> Step-by-Step Solution
                </h3>
                <button onclick="closeSolutionModal()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <div id="solutionModalBody" class="space-y-3"></div>
            <div class="mt-5 pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-xl transition">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- Data Injection -->
    <script>
        const slidesData = {json.dumps(slides_data)};
    </script>

    <!-- Logic Engine -->
    <script>
{js_code}
    </script>
</body>
</html>
"""

    out_path = "public/animations/class5-maths-we-the-travellers-2.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully compiled {out_path} ({len(full_html)} bytes).")

    # Symlinks
    symlinks = [
        "chapter4-maths-class5.html",
        "class5-maths-chapter4.html",
        "class5-we-the-travellers-2.html",
        "we-the-travellers-2-class5.html",
        "class5-maths-travellers-2-lab.html",
        "class5-math-travellers-2.html",
        "class5-travellers-2-lab.html"
    ]
    target_rel = "class5-maths-we-the-travellers-2.html"
    anim_dir = "public/animations"

    for sl in symlinks:
        sl_path = os.path.join(anim_dir, sl)
        if os.path.islink(sl_path) or os.path.exists(sl_path):
            os.remove(sl_path)
        os.symlink(target_rel, sl_path)
        print(f"Created symlink: {sl_path} -> {target_rel}")

    print("All build operations completed successfully.")

if __name__ == "__main__":
    build_html()

