# -*- coding: utf-8 -*-
"""
Build Class 5 Mathematics Chapter 13: Animal Jumps Animation Lab
Compiles public/animations/class5-maths-animal-jumps.html
and creates the 7 required symlinks.
"""

import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class5_maths_ch13_data import slides
from class5_maths_ch13_sims import simulators
from class5_maths_ch13_js import js_code

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 5 Mathematics — Chapter 13: Animal Jumps Master Lab</title>
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-emerald-500/30 selection:text-emerald-200">

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
                        <span class="text-emerald-400">🐾</span>
                        <span>Animal Jumps</span>
                    </h1>
                    <div class="text-[11px] text-slate-400">Class 5 Mathematics • Joyful Mathematics (NEP 2020)</div>
                </div>
            </div>

            <!-- Voice Priority & Controls -->
            <div class="flex items-center flex-wrap gap-2.5">
                <div class="flex items-center gap-1.5 bg-slate-950/80 px-2 py-1 rounded-lg border border-slate-800">
                    <label for="voiceSelect" class="text-[11px] text-emerald-400 font-semibold whitespace-nowrap">Voice:</label>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-transparent text-[11px] text-slate-200 focus:outline-none max-w-[170px] sm:max-w-[210px] truncate cursor-pointer">
                        <option value="">Searching Voices...</option>
                    </select>
                </div>

                <button id="audioPlayBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold flex items-center gap-1.5 transition shadow-sm">
                    🔊 Speak
                </button>
            </div>
        </div>
        <!-- Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-2.5 rounded-full overflow-hidden">
            <div id="progressBar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full transition-all duration-300" style="width: 5%;"></div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 py-5 flex flex-col justify-between">
        
        <!-- Slide Header -->
        <div class="mb-4 flex flex-wrap items-baseline justify-between gap-2 border-b border-slate-800/80 pb-3">
            <div>
                <span id="slideNum" class="text-xs font-mono font-bold text-emerald-400 uppercase tracking-widest block mb-0.5">Slide 1 of 20</span>
                <h2 id="slideTitle" class="text-xl sm:text-2xl font-black text-white tracking-tight">1. Multiplier Magic Box</h2>
                <p id="slideTagline" class="text-xs sm:text-sm text-slate-400 mt-0.5">Discovery Puzzle • Uncovering the Secret Multiplier Inside the Mathematical Machine</p>
            </div>
            <div class="flex items-center gap-2">
                <button id="prevBtn" onclick="prevSlide()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-semibold text-slate-300 border border-slate-700 transition">
                    ← Previous
                </button>
                <button id="nextBtn" onclick="nextSlide()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition shadow-sm">
                    Next →
                </button>
            </div>
        </div>

        <!-- Slide Dynamic Viewport -->
        <div id="slideContent" class="flex-1 min-h-[460px]">
            <!-- Rendered by JavaScript -->
        </div>

        <!-- Last Slide Notice Container (Terminal Invariant) -->
        <div id="lastSlideNotice" class="hidden mt-6 p-4 rounded-xl bg-gradient-to-r from-emerald-950/80 via-slate-900 to-emerald-950/80 border border-emerald-500/40 text-center">
            <p class="text-sm font-bold text-emerald-300">You have reached the last slide of this chapter.</p>
            <p class="text-xs text-slate-400 mt-1">Review your mastery quiz scores or click Curriculum to explore more mathematics modules.</p>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900/60 border-t border-slate-800/80 py-2.5 px-4 text-center text-xs text-slate-500">
        NCERT Class 5 Mathematics • Chapter 13: Animal Jumps • NEP 2020 Joyful Learning Edition
    </footer>

    <!-- Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-5 shadow-2xl relative">
            <div class="flex justify-between items-center mb-3 border-b border-slate-800 pb-2">
                <h3 id="solutionTitle" class="text-sm font-bold text-emerald-300 flex items-center gap-1.5">
                    <span>💡</span> Step-by-Step Derivation
                </h3>
                <button onclick="closeSolutionModal()" class="text-slate-400 hover:text-white text-base leading-none p-1">✕</button>
            </div>
            <div id="solutionContent" class="text-xs text-slate-300 space-y-3">
                <!-- Injected via JavaScript -->
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition">
                    Close
                </button>
            </div>
        </div>
    </div>

    <!-- Application Data & Script Payload -->
    <script>
        const slidesData = __SLIDES_JSON__;
        const simulatorsHtml = __SIMS_JSON__;

        function onVoiceChange() {
            const voiceSelect = document.getElementById('voiceSelect');
            if (!voiceSelect || !synth) return;
            const voices = synth.getVoices();
            const selected = voices.find(v => v.name === voiceSelect.value);
            if (selected) {
                userPreferredVoice = selected;
                if (synth.speaking) {
                    speakCurrentSlide();
                }
            }
        }

        __JS_CODE__
    </script>
</body>
</html>
"""

def build():
    slides_json = json.dumps(slides, ensure_ascii=False)
    sims_json = json.dumps(simulators, ensure_ascii=False)

    html = HTML_TEMPLATE.replace("__SLIDES_JSON__", slides_json)
    html = html.replace("__SIMS_JSON__", sims_json)
    html = html.replace("__JS_CODE__", js_code)

    dest_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public", "animations"))
    os.makedirs(dest_dir, exist_ok=True)

    master_filename = "class5-maths-animal-jumps.html"
    master_path = os.path.join(dest_dir, master_filename)

    with open(master_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully compiled {master_path} ({len(html):,} bytes)")

    # Create 7 symlinks
    symlinks = [
        "chapter13-maths-class5.html",
        "class5-maths-chapter13.html",
        "class5-animal-jumps.html",
        "animal-jumps-class5.html",
        "class5-maths-animal-jumps-lab.html",
        "class5-math-animal-jumps.html",
        "class5-jumps-lab.html"
    ]

    for symlink in symlinks:
        link_path = os.path.join(dest_dir, symlink)
        if os.path.islink(link_path) or os.path.exists(link_path):
            os.remove(link_path)
        os.symlink(master_filename, link_path)
        print(f"Created symlink: {symlink} -> {master_filename}")

if __name__ == "__main__":
    build()
