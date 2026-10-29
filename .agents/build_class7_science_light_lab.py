# -*- coding: utf-8 -*-
"""
Compiles the complete single-file interactive animated laboratory for:
NCERT Class 7 Science Chapter 11: Light: Shadows and Reflections.
Target: public/animations/class7-science-light-shadows-reflections.html
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""
import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))

from class7_science_light_data import CHAPTER_META, SLIDES
from class7_science_light_sims import SIMULATORS
from class7_science_light_js import JAVASCRIPT_CODE

def build_html():
    print("Building class7-science-light-shadows-reflections.html...")

    slides_html = []
    
    for slide in SLIDES:
        s_id = slide["id"]
        is_hidden = "hidden" if s_id > 1 else ""
        
        # Concept Slides (1-16)
        if s_id <= 16:
            sim_content = SIMULATORS.get(s_id, "<div class='p-4 text-slate-400'>Simulator loading...</div>")
            
            # Checkpoints
            cp_html = []
            for cp in slide.get("checkpoints", []):
                cp_id = cp["id"]
                opts_html = []
                for idx, opt in enumerate(cp["options"]):
                    clean_expl = cp["explanation"].replace("'", "\\'").replace('"', '&quot;')
                    opts_html.append(f"""
                        <button onclick="checkCheckpoint('{cp_id}', {idx}, {cp['correct']}, '{clean_expl}')"
                                class="cp-option-btn w-full text-left p-2.5 rounded-lg bg-slate-800 hover:bg-slate-700/80 border border-slate-700 text-xs text-slate-200 transition flex items-start gap-2">
                            <span class="w-5 h-5 rounded-full bg-slate-700 text-slate-300 font-bold flex items-center justify-center shrink-0 text-[10px]">{chr(65+idx)}</span>
                            <span class="leading-snug">{opt}</span>
                        </button>
                    """)
                
                cp_html.append(f"""
                    <div id="cp_card_{cp_id}" class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-700/80 shadow-md">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-bold uppercase tracking-wider">Concept Check</span>
                            <span class="text-xs text-slate-400 font-medium">Test your grasp</span>
                        </div>
                        <p class="text-xs sm:text-sm font-semibold text-slate-100 mb-3 leading-snug">{cp['question']}</p>
                        <div class="space-y-1.5">
                            {''.join(opts_html)}
                        </div>
                        <div id="cp_feedback_{cp_id}" class="hidden"></div>
                    </div>
                """)
            
            takeaways_html = "".join([f"<li class='flex items-start gap-2'><span class='text-amber-400 font-bold'>•</span><span>{t}</span></li>" for t in slide.get("takeaways", [])])

            slide_body = f"""
            <div id="slide-{s_id}" class="slide-container {is_hidden} space-y-6">
                <!-- Slide Header Banner -->
                <div class="bg-gradient-to-r from-amber-950/70 via-slate-900/90 to-cyan-950/70 p-5 rounded-2xl border border-amber-500/30 shadow-lg">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-bold uppercase tracking-wide">{slide['badge']}</span>
                        <span class="text-xs text-slate-400 font-mono">Slide {s_id} of 20</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-cyan-300 mb-1">{slide['title']}</h2>
                    <h3 class="text-xs sm:text-sm font-medium text-slate-300 mb-3">{slide['subtitle']}</h3>
                    <p class="slide-summary text-xs sm:text-sm text-slate-300 leading-relaxed bg-slate-950/50 p-3 rounded-xl border border-slate-800">{slide['summary']}</p>
                </div>

                <!-- Main Two-Column Interactive Grid -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    <!-- Left Column: Theory & Takeaways (7 cols) -->
                    <div class="lg:col-span-7 space-y-5">
                        <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-800 shadow-md">
                            <h4 class="text-sm font-bold text-amber-300 uppercase tracking-wider mb-3 flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-amber-400"></span> Core Scientific Concepts
                            </h4>
                            {slide['theory']}
                        </div>

                        <!-- Key Takeaways Card -->
                        <div class="bg-gradient-to-br from-amber-950/40 to-slate-900 p-4 rounded-xl border border-amber-500/30">
                            <h4 class="text-xs font-bold text-amber-300 uppercase tracking-wider mb-2">Key Takeaways</h4>
                            <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                                {takeaways_html}
                            </ul>
                        </div>
                    </div>

                    <!-- Right Column: Bespoke Simulator & Checkpoints (5 cols) -->
                    <div class="lg:col-span-5 space-y-5">
                        <!-- Bespoke SVG Simulator -->
                        <div class="shadow-xl">
                            {sim_content}
                        </div>

                        <!-- Checkpoints Stack -->
                        <div class="space-y-3">
                            {''.join(cp_html)}
                        </div>
                    </div>
                </div>
            </div>
            """
        
        # Mastery Quiz Challenge Slides (17-20)
        else:
            q_cards = []
            for q_idx, q in enumerate(slide.get("quiz_questions", [])):
                q_num = (s_id - 17) * 10 + (q_idx + 1)
                q_id = q["id"]
                opts_html = []
                sol_val = q.get("solution") or q.get("explanation") or ""
                clean_q_text = q['question'].replace("'", "\\'").replace('"', '&quot;')
                clean_sol_text = sol_val.replace("'", "\\'").replace('"', '&quot;')
                
                for opt_idx, opt in enumerate(q["options"]):
                    opts_html.append(f"""
                        <button onclick="checkCheckpoint('{q_id}', {opt_idx}, {q['correct']}, '{clean_sol_text}')"
                                class="cp-option-btn w-full text-left p-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs text-slate-200 transition flex items-start gap-2">
                            <span class="w-5 h-5 rounded-full bg-slate-700 text-slate-300 font-bold flex items-center justify-center shrink-0 text-[10px]">{chr(65+opt_idx)}</span>
                            <span class="leading-snug">{opt}</span>
                        </button>
                    """)
                
                q_cards.append(f"""
                    <div id="cp_card_{q_id}" class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 shadow-md flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between gap-2 mb-2">
                                <span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-[10px] font-bold">Question {q_num} of 40</span>
                                <button onclick="openSolutionModal({q_num}, '{clean_q_text}', '{clean_sol_text}')"
                                        class="text-[11px] font-semibold text-amber-400 hover:text-amber-300 flex items-center gap-1 transition">
                                    <span>View Solution</span>
                                    <span>→</span>
                                </button>
                            </div>
                            <p class="text-xs sm:text-sm font-semibold text-slate-100 mb-3 leading-snug">{q['question']}</p>
                            <div class="space-y-1.5 mb-2">
                                {''.join(opts_html)}
                            </div>
                        </div>
                        <div id="cp_feedback_{q_id}" class="hidden mt-2"></div>
                    </div>
                """)

            slide_body = f"""
            <div id="slide-{s_id}" class="slide-container {is_hidden} space-y-6">
                <!-- Quiz Banner -->
                <div class="bg-gradient-to-r from-amber-950/70 via-slate-900/90 to-cyan-950/70 p-5 rounded-2xl border border-amber-500/30 shadow-lg">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-bold uppercase tracking-wide">{slide['badge']}</span>
                        <span class="text-xs text-slate-400 font-mono">Slide {s_id} of 20</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-200 to-cyan-300 mb-1">{slide['title']}</h2>
                    <h3 class="text-xs sm:text-sm font-medium text-slate-300 mb-2">{slide['subtitle']}</h3>
                    <p class="text-xs sm:text-sm text-slate-300 bg-slate-950/50 p-3 rounded-xl border border-slate-800">{slide['summary']}</p>
                </div>

                <!-- 10 Question Cards Grid (2 cols) -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {''.join(q_cards)}
                </div>
            </div>
            """

        slides_html.append(slide_body)

    # Full HTML wrapper
    full_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 7 Science • Chapter 11 • Light Master Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            850: '#111827',
                            950: '#030712',
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
        code, pre, .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #090d16;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #1e293b;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #334155;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-amber-500/30 selection:text-amber-200">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800/80 px-4 py-3">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <!-- Left Branding -->
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-400 via-yellow-500 to-amber-600 flex items-center justify-center shadow-lg shadow-amber-500/20 text-slate-950 font-black text-xl">
                    💡
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 7 Science</span>
                        <span class="text-xs text-slate-400 font-mono">Chapter 11</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-slate-100">Light</h1>
                </div>
            </div>

            <!-- Mentor Badge -->
            <div class="hidden md:flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800">
                <div class="w-7 h-7 rounded-full bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-xs">
                    🔭
                </div>
                <div class="text-left">
                    <span class="text-[10px] uppercase font-bold text-cyan-300 block leading-tight">Historical Mentors</span>
                    <span class="text-xs font-semibold text-slate-200">Ibn al-Haytham & Acharya Aryabhata</span>
                </div>
            </div>

            <!-- Controls (Voice & Progress) -->
            <div class="flex items-center gap-3">
                <!-- Narration Button -->
                <button id="narrateBtn" onclick="toggleSpeech()"
                        class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-semibold transition">
                    <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                    </svg>
                    <span class="text-slate-300 font-semibold text-xs">Voice Narration</span>
                </button>

                <!-- Slide Indicator Pill -->
                <div class="px-3 py-1.5 rounded-lg bg-amber-950/60 border border-amber-500/30 text-amber-300 text-xs font-mono font-bold">
                    <span id="slideIndicator">1 / 20</span>
                </div>
            </div>
        </div>

        <!-- Horizontal Progress Bar -->
        <div class="w-full bg-slate-900 h-1.5 mt-2.5 rounded-full overflow-hidden">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-yellow-400 to-cyan-400 h-full w-[5%] transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Slide Content Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">
        {''.join(slides_html)}
    </main>

    <!-- Bottom Sticky Navigation Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 px-4 py-3 shadow-2xl">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <!-- Left: Previous Button -->
            <button id="prevBtn" onclick="prevSlide()" disabled
                    class="flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 disabled:opacity-30 disabled:cursor-not-allowed border border-slate-700 text-xs sm:text-sm font-bold text-slate-200 transition">
                <span>←</span>
                <span>Previous Slide</span>
            </button>

            <!-- Center: Jump Picker & Terminal Message -->
            <div class="flex items-center gap-3">
                <div class="flex items-center gap-2 text-xs text-slate-400 font-medium">
                    <span class="hidden sm:inline">Jump to:</span>
                    <select onchange="goToSlide(parseInt(this.value))"
                            class="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-200 font-mono focus:outline-none focus:border-amber-500">
                        {''.join([f"<option value='{i}'>Slide {i}: {SLIDES[i-1]['title'][:32]}...</option>" for i in range(1, 21)])}
                    </select>
                </div>

                <!-- Last Slide Terminal Notice Container -->
                <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-amber-950/80 border border-amber-500/50 text-amber-200 text-xs sm:text-sm font-bold flex items-center gap-2 animate-pulse">
                    <span>🎉</span>
                    <span>You have reached the last slide of this chapter.</span>
                </div>
            </div>

            <!-- Right: Next Button -->
            <button id="nextBtn" onclick="nextSlide()"
                    class="flex items-center gap-2 px-5 py-2 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 text-xs sm:text-sm font-bold shadow-lg shadow-amber-500/30 transition">
                <span>Next Slide</span>
                <span>→</span>
            </button>
        </div>
    </footer>

    <!-- Step-by-Step Solution Modal -->
    <div id="solutionModal" style="display: none; z-index: 99999 !important;"
         class="fixed inset-0 bg-black/80 backdrop-blur-sm items-center justify-center p-4">
        <div class="bg-slate-950 max-w-xl w-full rounded-2xl border border-slate-700 shadow-2xl p-6 relative flex flex-col gap-4 animate-in fade-in zoom-in-95 duration-200">
            <!-- Modal Header -->
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
                    <h3 id="modalTitle" class="text-sm sm:text-base font-bold text-cyan-300">Question Solution</h3>
                </div>
                <button onclick="closeSolutionModal()"
                        class="w-7 h-7 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center font-bold text-sm transition">
                    ✕
                </button>
            </div>

            <!-- Modal Content -->
            <div id="modalBody" class="space-y-3">
                <!-- Injected dynamically -->
            </div>

            <!-- Modal Footer -->
            <div class="border-t border-slate-800 pt-3 flex justify-end">
                <button onclick="closeSolutionModal()"
                        class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition">
                    Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Interactive Logic Script -->
    <script>
{JAVASCRIPT_CODE}
    </script>
</body>
</html>
"""

    output_path = "public/animations/class7-science-light-shadows-reflections.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    file_size = os.path.getsize(output_path)
    print(f"Generated {output_path} ({file_size:,} bytes).")
    
    # Final Validation
    latex_pattern = re.compile(r'\\[a-zA-Z]+')
    matches = latex_pattern.findall(full_html)
    bad_latex = [m for m in matches if m not in ['\\n', '\\t', '\\r', '\\f', '\\b']]
    if bad_latex:
        print(f"CRITICAL WARNING: Found potential raw LaTeX commands: {bad_latex[:10]}")
    else:
        print("VERIFIED PASS: Strictly zero raw LaTeX in compiled HTML!")

if __name__ == "__main__":
    build_html()
