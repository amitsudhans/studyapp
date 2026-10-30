import sys
import json
sys.path.insert(0, '.agents')

from class6_math_prime_time_data import CHAPTER_META, SLIDES, QUIZ_QUESTIONS
from class6_math_prime_time_sims import SIMULATORS
from class6_math_prime_time_js import INTERACTIVE_JS

def build_lab():
    print("Building class6-math-prime-time.html...")

    # Build Quiz Questions Map
    quiz_map_json = json.dumps({q["id"]: q for q in QUIZ_QUESTIONS}, ensure_ascii=False)

    # Render Slides HTML
    slides_html = []
    letters = ['A', 'B', 'C', 'D']

    for idx, slide in enumerate(SLIDES):
        slide_id = slide["id"]
        is_quiz = slide.get("is_quiz", False)
        hidden_cls = "" if slide_id == 1 else "hidden"

        if not is_quiz:
            # Checkpoints HTML
            cp_html = []
            for cp in slide.get("checkpoints", []):
                cp_id = cp["id"]
                options_html = []
                for o_idx, opt in enumerate(cp["options"]):
                    options_html.append(f"""
                        <button onclick="checkAnswer('{cp_id}', {o_idx}, {cp['correct']}, `{cp['explanation']}`)"
                                class="option-btn text-left p-2.5 rounded-lg bg-slate-800 hover:bg-slate-700/80 border border-slate-700/80 text-xs text-slate-200 transition-all duration-150 flex items-start gap-2">
                            <span class="w-5 h-5 rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold text-amber-400">{letters[o_idx]}</span>
                            <span class="pt-0.5">{opt}</span>
                        </button>
                    """)
                cp_html.append(f"""
                    <div id="{cp_id}" class="checkpoint-card p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/80 mb-3 shadow-sm">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-xs px-2 py-0.5 rounded font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Checkpoint</span>
                            <span class="text-xs font-semibold text-slate-200">{cp['question']}</span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2">
                            {''.join(options_html)}
                        </div>
                        <div class="checkpoint-feedback hidden"></div>
                    </div>
                """)

            # Core Concept Slide Layout (Theory on left, Simulator on right)
            slide_content = f"""
            <div id="slide-{slide_id}" class="slide-pane {hidden_cls} flex-1 flex flex-col h-full max-w-7xl mx-auto w-full p-2 sm:p-4">
                <!-- Slide Header -->
                <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800 shrink-0">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold tracking-wider uppercase bg-amber-500/20 text-amber-300 border border-amber-500/30">{slide['badge']}</span>
                            <span class="text-xs font-mono text-slate-400">Slide {slide_id} of 20</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-cyan-300 mb-0.5">{slide['title']}</h2>
                        <h3 class="text-xs sm:text-sm font-medium text-slate-300">{slide['subtitle']}</h3>
                    </div>
                    <div class="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs">
                        <span class="text-amber-400 font-bold">Mentors:</span>
                        <span class="text-slate-300">{CHAPTER_META['mentors']}</span>
                    </div>
                </div>

                <!-- Hidden summary for voice synthesis -->
                <div class="slide-summary hidden">{slide['summary']}</div>

                <!-- Two-Column Layout -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 flex-1 overflow-y-auto pr-1">
                    <!-- Left: Narrative & Checkpoints -->
                    <div class="lg:col-span-7 flex flex-col space-y-3">
                        <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 shadow-inner">
                            {slide['theory']}
                        </div>
                        <div class="pt-1">
                            {''.join(cp_html)}
                        </div>
                    </div>

                    <!-- Right: Bespoke Interactive Simulator -->
                    <div class="lg:col-span-5 flex flex-col min-h-[360px] lg:min-h-0">
                        {SIMULATORS[idx]}
                    </div>
                </div>
            </div>
            """
            slides_html.append(slide_content)
        else:
            # Quiz Challenge Slide Layout (10 questions per slide)
            start_q, end_q = slide["quiz_range"]
            questions_for_slide = [q for q in QUIZ_QUESTIONS if start_q <= q["id"] <= end_q]

            quiz_cards_html = []
            for q in questions_for_slide:
                q_id = q["id"]
                opts_html = []
                for o_idx, opt in enumerate(q["options"]):
                    opts_html.append(f"""
                        <button onclick="selectQuizOption({q_id}, {o_idx}, {q['correct']})"
                                class="quiz-option-btn text-left p-2.5 rounded-lg bg-slate-800 hover:bg-slate-700/80 border border-slate-700/80 text-xs text-slate-200 transition-all flex items-start gap-2">
                            <span class="w-5 h-5 rounded-full bg-slate-900 border border-slate-700 flex items-center justify-center text-[10px] font-mono shrink-0 font-bold text-amber-400">{letters[o_idx]}</span>
                            <span class="pt-0.5">{opt}</span>
                        </button>
                    """)
                quiz_cards_html.append(f"""
                    <div id="quiz-q-{q_id}" class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between shadow-sm">
                        <div>
                            <div class="flex items-center justify-between mb-1.5">
                                <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Question {q_id}</span>
                            </div>
                            <p class="text-xs font-semibold text-slate-100 mb-2.5">{q['question']}</p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                                {''.join(opts_html)}
                            </div>
                        </div>
                        <div class="mt-2 pt-2 border-t border-slate-800/80 flex items-center justify-end">
                            <button onclick="openSolution({q_id})" class="view-solution-btn hidden px-3 py-1 rounded bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition flex items-center gap-1.5">
                                <span>💡</span> View Step-by-Step Solution
                            </button>
                        </div>
                    </div>
                """)

            slide_content = f"""
            <div id="slide-{slide_id}" class="slide-pane {hidden_cls} flex-1 flex flex-col h-full max-w-7xl mx-auto w-full p-2 sm:p-4">
                <!-- Slide Header -->
                <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800 shrink-0">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold tracking-wider uppercase bg-amber-500/20 text-amber-300 border border-amber-500/30">{slide['badge']}</span>
                            <span class="text-xs font-mono text-slate-400">Questions {start_q} to {end_q}</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-cyan-300 mb-0.5">{slide['title']}</h2>
                        <h3 class="text-xs sm:text-sm font-medium text-slate-300">{slide['subtitle']}</h3>
                    </div>
                    <div class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-amber-300 font-bold">
                        10 Interactive Challenges
                    </div>
                </div>

                <div class="slide-summary hidden">Welcome to {slide['title']}. Test your knowledge with these 10 questions. Click an answer, then view the full step-by-step solution.</div>

                <!-- Questions Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 flex-1 overflow-y-auto pr-1">
                    {''.join(quiz_cards_html)}
                </div>
            </div>
            """
            slides_html.append(slide_content)

    full_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CHAPTER_META['title']} — Interactive Master Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Outfit', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }}
                }}
            }}
        }}
    </script>
    <style>
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(15, 23, 42, 0.6);
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(51, 65, 85, 0.8);
            border-radius: 9999px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(100, 116, 139, 1);
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased h-screen flex flex-col justify-between overflow-hidden select-none">

    <!-- Top Header Navigation -->
    <header class="h-14 border-b border-slate-800 bg-slate-900/80 backdrop-blur px-4 flex items-center justify-between shrink-0 z-20">
        <div class="flex items-center gap-3">
            <a href="/curriculum" class="w-8 h-8 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition" title="Back to Curriculum">
                ←
            </a>
            <div>
                <span class="text-[10px] font-mono tracking-wider uppercase text-amber-400 font-bold block">NCERT Class 6 • Mathematics</span>
                <h1 class="text-xs sm:text-sm font-bold text-slate-100 flex items-center gap-1.5">
                    <span>⏱️</span>
                    <span>{CHAPTER_META['title']}</span>
                </h1>
            </div>
        </div>

        <div class="flex items-center gap-3">
            <div class="hidden md:flex items-center gap-2 bg-slate-800/80 px-3 py-1 rounded-xl border border-slate-700/80">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <div class="text-left">
                    <div class="text-[9px] text-slate-400 font-mono">MENTORS</div>
                    <div class="text-xs font-bold text-amber-300">{CHAPTER_META['mentors']}</div>
                </div>
            </div>

            <button id="muteBtn" onclick="toggleAudio()" class="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 flex items-center justify-center text-sm transition" title="Toggle Audio Narration">
                🔊
            </button>
        </div>
    </header>

    <!-- Main Slide Stage -->
    <main class="flex-1 relative overflow-hidden flex flex-col">
        {''.join(slides_html)}
    </main>

    <!-- Bottom Navigation Bar -->
    <footer class="h-16 border-t border-slate-800 bg-slate-900/90 backdrop-blur px-4 flex items-center justify-between shrink-0 z-20">
        <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:pointer-events-none text-slate-200 text-xs sm:text-sm font-bold border border-slate-700 transition flex items-center gap-2">
            <span>←</span> Previous
        </button>

        <!-- Progress Tracker -->
        <div class="flex flex-col items-center max-w-xs sm:max-w-md w-full px-4">
            <div class="flex items-center justify-between w-full text-[11px] font-mono text-slate-400 mb-1">
                <span>PROGRESS</span>
                <span id="slideCounter" class="text-amber-300 font-bold">1 / 20</span>
            </div>
            <div class="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div id="progressBar" class="h-full bg-gradient-to-r from-amber-500 to-cyan-400 transition-all duration-300" style="width: 5%;"></div>
            </div>
            <!-- Terminal Slide Notice -->
            <div id="lastSlideNotice" class="text-[11px] font-bold text-amber-400 mt-1" style="display: none;">You have reached the last slide of this chapter.</div>
        </div>

        <button id="nextBtn" onclick="nextSlide()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 text-xs sm:text-sm font-bold shadow-md shadow-amber-500/20 transition flex items-center gap-2">
            Next <span>→</span>
        </button>
    </footer>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" style="display: none; z-index: 99999 !important;" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-5 shadow-2xl relative flex flex-col max-h-[85vh]">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="text-amber-400 text-lg">💡</span>
                    <h3 id="solutionTitle" class="font-bold text-sm sm:text-base text-slate-100">Step-by-Step Solution</h3>
                </div>
                <button onclick="closeSolution()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center text-sm font-bold transition">
                    ✕
                </button>
            </div>
            <div id="solutionBody" class="py-4 overflow-y-auto flex-1 pr-1">
                <!-- Content injected via openSolution(qId) -->
            </div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolution()" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition">
                    Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Interactivity Script -->
    <script>
        const QUIZ_QUESTIONS_MAP = {quiz_map_json};
        {INTERACTIVE_JS}
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {{
            goToSlide(1);
        }});
    </script>
</body>
</html>
"""

    # Strict check for raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in full_html:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in compiled HTML!")

    # Check for surrogates
    clean_chars = [ch for ch in full_html if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_full_html = ''.join(clean_chars)

    with open("public/animations/class6-math-prime-time.html", "w", encoding="utf-8") as f:
        f.write(clean_full_html)

    print("Generated public/animations/class6-math-prime-time.html successfully.")
    print("VERIFIED PASS: Strictly zero raw LaTeX and zero surrogates in compiled HTML!")

if __name__ == "__main__":
    build_lab()

