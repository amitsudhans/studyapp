# -*- coding: utf-8 -*-
"""
Build Class 5 Mathematics Chapter 8: Weight and Capacity Animation Lab
Compiles public/animations/class5-maths-weight-and-capacity.html
and creates the 7 required symlinks.
"""

import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class5_maths_ch8_data import slides
from class5_maths_ch8_sims import simulators
from class5_maths_ch8_js import js_code

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 5 Mathematics — Chapter 8: Weight and Capacity Master Lab</title>
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-cyan-500/30 selection:text-cyan-200">

    <!-- Top Sticky Header Bar -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0">Class 5 • NCERT Mathematics</span>
                <span class="text-xs text-slate-400 font-medium hidden md:inline">Chapter 8 • Weight and Capacity</span>
            </div>

            <div class="flex items-center gap-2 flex-wrap">
                <!-- Voice Selector -->
                <div class="flex items-center gap-1.5 bg-slate-800/80 px-2 py-1 rounded-lg border border-slate-700">
                    <span class="text-[11px] text-slate-400">🎙️</span>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-transparent text-slate-200 text-xs focus:outline-none max-w-[170px] sm:max-w-[220px] truncate">
                        <option value="">Detecting Male Voices...</option>
                    </select>
                </div>

                <!-- Audio Toggle Button -->
                <button id="audioBtn" onclick="toggleAudio()" class="px-2.5 py-1 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-500/40 text-xs font-semibold flex items-center gap-1 transition-all">
                    <span>🔊</span> Listen to Lecture
                </button>

                <!-- Slide Navigation Controls -->
                <div class="flex items-center gap-1 bg-slate-800/80 p-0.5 rounded-lg border border-slate-700">
                    <button id="prevBtn" onclick="prevSlide()" class="px-2 py-1 rounded hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:hover:bg-transparent text-xs font-semibold transition-all">
                        ◀ Prev
                    </button>
                    <span id="slideCounter" class="px-2 text-xs font-mono font-bold text-amber-300 min-w-[85px] text-center">
                        Slide 1 of 20
                    </span>
                    <button id="nextBtn" onclick="nextSlide()" class="px-2 py-1 rounded hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:hover:bg-transparent text-xs font-semibold transition-all">
                        Next ▶
                    </button>
                </div>
            </div>
        </div>

        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-2 rounded-full overflow-hidden">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-cyan-500 to-emerald-500 h-full transition-all duration-300" style="width: 5%;"></div>
        </div>
    </header>

    <!-- Main Learning Stage -->
    <main class="max-w-7xl mx-auto w-full p-4 md:p-6 flex-1 flex flex-col justify-between">
        <!-- Title and Subtitle -->
        <div class="mb-4">
            <h1 id="slideTitle" class="text-2xl sm:text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-cyan-300 to-emerald-300 tracking-tight">
                Weight Estimation
            </h1>
            <p id="slideTagline" class="text-xs sm:text-sm text-slate-400 font-medium mt-1">
                Check! Check! • Estimating Real-World Masses & Reading Scales
            </p>
        </div>

        <!-- 2-Column Split: Theory & Simulator -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 mb-5 items-start">
            <!-- Theory Block -->
            <div id="theoryContainer" class="lg:col-span-7 space-y-4">
                <!-- Populated dynamically -->
            </div>

            <!-- Simulator Block (Slides 1 to 16) -->
            <div id="simulatorContainer" class="lg:col-span-5 bg-slate-900/40 p-4 rounded-2xl border border-slate-800 shadow-xl">
                <!-- Populated dynamically -->
            </div>
        </div>

        <!-- Checkpoints or Quiz Challenge Deck -->
        <div id="checkpointContainer" class="w-full mb-6">
            <!-- Populated dynamically -->
        </div>

        <!-- Last Slide Notice (Terminal Invariant) -->
        <div id="lastSlideNotice" style="display: none;" class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 font-bold text-center text-sm mb-4">
            You have reached the last slide of this chapter.
        </div>
    </main>

    <!-- Step-by-Step Solution Modal -->
    <div id="solutionModal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm hidden items-center justify-center p-4">
        <div class="bg-slate-900 border border-slate-700 max-w-lg w-full rounded-2xl p-5 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/80 pb-2">
                <h3 class="font-bold text-amber-300 text-sm flex items-center gap-2">
                    <span>💡</span> Step-by-Step Mathematical Walkthrough
                </h3>
                <button onclick="closeSolutionModal()" class="text-slate-400 hover:text-slate-200 text-lg leading-none font-bold">
                    ✕
                </button>
            </div>
            <div id="solutionModalBody" class="max-h-[70vh] overflow-y-auto pr-1">
                <!-- Populated dynamically -->
            </div>
            <div class="pt-2 text-right">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">
                    Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-900/60 border-t border-slate-800/80 py-3 px-4 text-center text-[11px] text-slate-500">
        NCERT Class 5 Mathematics (Joyful Mathematics, NEP 2020) • Chapter 8: Weight and Capacity • Interactive Laboratory
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
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'animations', 'class5-maths-weight-and-capacity.html'))
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
        'chapter8-maths-class5.html',
        'class5-maths-chapter8.html',
        'class5-weight-and-capacity.html',
        'weight-and-capacity-class5.html',
        'class5-maths-weight-capacity-lab.html',
        'class5-math-weight-and-capacity.html',
        'class5-weight-capacity-lab.html'
    ]

    anim_dir = os.path.dirname(output_path)
    target_rel = 'class5-maths-weight-and-capacity.html'

    for link in symlinks:
        link_path = os.path.join(anim_dir, link)
        if os.path.lexists(link_path):
            os.remove(link_path)
        os.symlink(target_rel, link_path)
        print(f"Created symlink: {link} -> {target_rel}")

if __name__ == '__main__':
    build_lab()

