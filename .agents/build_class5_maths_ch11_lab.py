# -*- coding: utf-8 -*-
"""
Build Class 5 Mathematics Chapter 11: Grandmother's Quilt Animation Lab
Compiles public/animations/class5-maths-grandmothers-quilt.html
and creates the 7 required symlinks.
"""

import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class5_maths_ch11_data import slides
from class5_maths_ch11_sims import simulators
from class5_maths_ch11_js import js_code

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 5 Mathematics — Chapter 11: Grandmother's Quilt Master Lab</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Outfit', sans-serif;
        }
        code, pre, .font-mono {
            font-family: 'JetBrains Mono', monospace;
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-amber-500/30 selection:text-amber-200">

    <!-- Top Navigation / Header -->
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <a href="/multimedia" class="text-xs px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 flex items-center gap-1.5 transition-colors">
                    <span>←</span> Curriculum
                </a>
                <div class="h-4 w-px bg-slate-700"></div>
                <div>
                    <h1 class="text-sm font-bold text-white tracking-wide flex items-center gap-1.5">
                        <span class="text-amber-400">🧵</span>
                        <span>Grandmother's Quilt</span>
                    </h1>
                    <div class="text-[11px] text-slate-400">Class 5 Mathematics • Joyful Mathematics (NEP 2020)</div>
                </div>
            </div>

            <!-- Voice Priority & Controls -->
            <div class="flex items-center flex-wrap gap-2.5">
                <div class="flex items-center gap-1.5 bg-slate-950/80 px-2 py-1 rounded-lg border border-slate-800">
                    <label for="voiceSelect" class="text-[11px] text-amber-400 font-semibold whitespace-nowrap">Voice:</label>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-transparent text-[11px] text-slate-200 focus:outline-none max-w-[170px] sm:max-w-[210px] truncate cursor-pointer">
                        <option value="">Searching Voices...</option>
                    </select>
                </div>

                <button id="audioBtn" onclick="toggleAudio()" class="px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 shadow transition-all active:scale-95">
                    <span>🔊</span> Listen to Lecture
                </button>

                <div class="hidden sm:flex items-center gap-1.5 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700 font-mono text-xs text-amber-300">
                    <span id="slideCounter">Slide 1 of 20</span>
                </div>
            </div>
        </div>

        <!-- Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-2 rounded-full overflow-hidden">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-orange-500 to-amber-400 h-full w-[5%] transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Learning Canvas -->
    <main class="max-w-7xl mx-auto w-full p-4 flex-1 flex flex-col justify-between gap-4">
        <!-- Slide Title & Tagline -->
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-2 shadow-lg">
            <div>
                <span class="text-[10px] font-bold uppercase tracking-widest text-amber-400 block mb-0.5 font-mono">Module Interactive Exploration</span>
                <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white tracking-tight">Quilt Perimeter</h2>
                <p id="slideTagline" class="text-xs text-slate-300 mt-0.5">Decorative Lace Borders • Measuring Outer Boundary Lengths</p>
            </div>
            <div class="flex items-center gap-2 self-end sm:self-center">
                <button id="prevBtn" onclick="prevSlide()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-xs font-semibold text-slate-200 border border-slate-700 transition-all flex items-center gap-1">
                    <span>‹</span> Prev
                </button>
                <button id="nextBtn" onclick="nextSlide()" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-xs font-bold text-white shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-1">
                    Next <span>›</span>
                </button>
            </div>
        </div>

        <!-- Dynamic Slide Stage -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 flex-1 items-stretch">
            <!-- Left Side: Conceptual Theory & Formative Checkpoints -->
            <div id="theoryContainer" class="lg:col-span-7 space-y-4">
                <!-- Injected via showSlide -->
            </div>

            <!-- Right Side: Interactive Bespoke Simulator -->
            <div id="simulatorContainer" class="lg:col-span-5 bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
                <!-- Injected via showSlide -->
            </div>
        </div>

        <!-- Formative Checkpoints or Challenge Deck Row -->
        <div id="checkpointContainer" class="w-full">
            <!-- Injected via renderCheckpoints or renderQuizChallenge -->
        </div>

        <!-- Last Slide Notice (Terminal Slide Invariant for Slide 20) -->
        <div id="lastSlideNotice" class="hidden p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-emerald-200 text-center font-bold text-sm shadow-lg">
            You have reached the last slide of this chapter.
        </div>
    </main>

    <!-- Step-by-Step Solution Modal -->
    <div id="solutionModal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm hidden items-center justify-center p-4">
        <div class="bg-slate-900 border border-slate-700 max-w-lg w-full rounded-2xl p-5 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700 pb-2.5">
                <h3 class="text-sm font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
                    <span>💡</span> Step-by-Step Solution & Verification
                </h3>
                <button onclick="closeSolutionModal()" class="text-slate-400 hover:text-slate-200 text-lg font-bold p-1">
                    ✕
                </button>
            </div>
            <div id="solutionModalBody" class="max-h-[60vh] overflow-y-auto space-y-3 pr-1 text-slate-200">
                <!-- Populated dynamically -->
            </div>
            <div class="flex justify-end pt-2 border-t border-slate-800">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-900/60 border-t border-slate-800/80 py-3 px-4 text-center text-[11px] text-slate-500">
        NCERT Class 5 Mathematics (Joyful Mathematics, NEP 2020) • Chapter 11: Grandmother's Quilt • Interactive Laboratory
    </footer>

    <!-- Data Injection & Engine Script -->
    <script>
        const slidesData = __SLIDES_JSON__;
        const simulatorsHtml = __SIMS_JSON__;

        __JS_CODE__
    </script>
</body>
</html>
"""

def build_lab():
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'animations', 'class5-maths-grandmothers-quilt.html'))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    slides_json = json.dumps(slides, ensure_ascii=False)
    sims_json = json.dumps(simulators, ensure_ascii=False)

    html_content = HTML_TEMPLATE.replace('__SLIDES_JSON__', slides_json)
    html_content = html_content.replace('__SIMS_JSON__', sims_json)
    html_content = html_content.replace('__JS_CODE__', js_code)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully compiled {output_path} ({len(html_content):,} bytes)")

    # Symlinks creation
    symlinks = [
        'chapter11-maths-class5.html',
        'class5-maths-chapter11.html',
        'class5-grandmothers-quilt.html',
        'grandmothers-quilt-class5.html',
        'class5-maths-grandmothers-quilt-lab.html',
        'class5-math-grandmothers-quilt.html',
        'class5-quilt-lab.html'
    ]

    anim_dir = os.path.dirname(output_path)
    target_rel = 'class5-maths-grandmothers-quilt.html'

    for link in symlinks:
        link_path = os.path.join(anim_dir, link)
        if os.path.lexists(link_path):
            os.remove(link_path)
        os.symlink(target_rel, link_path)
        print(f"Created symlink: {link} -> {target_rel}")

if __name__ == '__main__':
    build_lab()
