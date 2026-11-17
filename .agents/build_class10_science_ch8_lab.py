# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 8: Heredity
Build complete HTML laboratory: public/animations/class10-heredity.html
"""

import json
import re
import os
import shutil
import sys

# Import slide data, simulators, and JS handlers
from class10_science_ch8_data import slides
from class10_science_ch8_sims import simulators
from c10s_ch8_sim_handlers import SIMULATOR_JS

print(f"Loaded {len(slides)} slides and {len(simulators)} simulators.")

# Validate and format slides
formatted_slides = []

for s in slides:
    sid = s['id']
    title = s['title']
    subtitle = s.get('subtitle', '')
    speech = s.get('speech', '')

    formatted_slide = {
        'id': sid,
        'title': title,
        'subtitle': subtitle,
        'speech': speech
    }

    if sid <= 16:
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words"
        assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
        assert sid in simulators, f"Missing simulator for slide {sid}"

        formatted_cps = []
        for cidx, cp in enumerate(s['checkpoints']):
            assert len(cp['options']) == 4, f"Slide {sid} checkpoint {cidx+1} must have 4 options"
            ans_str = cp['options'][cp['answer']]
            formatted_cps.append({
                'q': cp['question'],
                'options': cp['options'],
                'ans': ans_str,
                'hint': cp['hint'],
                'explanation': cp['explanation']
            })
        formatted_slide['checkpoints'] = formatted_cps
    else:
        assert len(s['questions']) == 10, f"Slide {sid} must have 10 challenge questions"
        formatted_qs = []
        for qidx, q in enumerate(s['questions']):
            qid = f"c{sid}_q{qidx+1}"
            assert 'hint' in q, f"Slide {sid} question {qid} missing hint"
            assert len(q['options']) == 4, f"Slide {sid} question {qid} must have 4 options"
            ans_str = q['options'][q['answer']]
            sol_steps = q.get('solution') or q.get('solution_steps') or q.get('steps')
            assert len(sol_steps) == 3, f"Slide {sid} question {qid} must have 3 solution steps"
            formatted_qs.append({
                'id': qid,
                'q': q['question'],
                'options': q['options'],
                'ans': ans_str,
                'hint': q['hint'],
                'explanation': q['explanation'],
                'solution_steps': sol_steps
            })
        formatted_slide['questions'] = formatted_qs

    formatted_slides.append(formatted_slide)

print("All 20 slides for Class 10 Science Chapter 8 passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science — Chapter 8: Heredity Interactive Lab</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Outfit', sans-serif;
            background-color: #030712;
            color: #f3f4f6;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
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
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 antialiased selection:bg-emerald-500 selection:text-slate-950">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-40 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=science&class=class10" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition-colors text-sm font-semibold">
                    ←
                </a>
                <div>
                    <span class="text-[10px] uppercase font-bold tracking-widest text-emerald-400 block">NCERT Class 10 Science • Chapter 8</span>
                    <h1 class="text-sm sm:text-base font-extrabold text-white flex items-center gap-2">
                        <span>Heredity</span>
                        <span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-600/30 text-emerald-300 border border-emerald-500/40">Lab 1</span>
                    </h1>
                </div>
            </div>

            <!-- Voice Controls (Slides 1-16 only) -->
            <div id="audioControls" class="flex items-center gap-2">
                <div class="hidden md:flex items-center gap-1.5 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700/80 text-xs">
                    <span class="text-slate-400">🎙️ Voice:</span>
                    <select id="voiceSelect" class="bg-transparent text-emerald-400 font-medium focus:outline-none max-w-[150px] truncate cursor-pointer text-xs">
                        <option value="">Teacher Sound Engine...</option>
                    </select>
                </div>
                <button id="audioLectureBtn" onclick="toggleSpokenLecture()" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span id="audioPlayIcon">🔊</span>
                    <span id="audioButtonText" class="hidden sm:inline">Teacher Sound Lecture</span>
                </button>
            </div>

            <div class="flex items-center gap-2">
                <span id="slideIndicator" class="text-xs font-mono px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 border border-slate-700">Slide 1/20</span>
                <span id="scoreBadge" class="hidden sm:inline-block text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-950/60 text-emerald-300 border border-emerald-500/30">Score: 0</span>
            </div>
        </div>

        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-800/60 h-1.5 mt-2.5 rounded-full overflow-hidden">
            <div id="slideProgressBar" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-300" style="width: 5%;"></div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto w-full p-4 sm:p-6 flex-1">
__SLIDES_HTML__
    </main>

    <!-- Sticky Footer Controls -->
    <footer class="bg-slate-900/90 backdrop-blur sticky bottom-0 border-t border-slate-800 py-3 px-4 z-40">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs flex items-center gap-1.5 transition-colors">
                <span>←</span> Previous
            </button>

            <!-- Terminal Slide Invariant Notice -->
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-bold text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- 3-Step Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-xl w-full p-5 space-y-4 shadow-2xl">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <h3 class="text-sm sm:text-base font-bold text-white tracking-tight">Biological Walkthrough & Detailed Solution</h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm font-bold">✕</button>
            </div>
            <div id="solutionModalBody" class="py-4 space-y-4 max-h-[70vh] overflow-y-auto custom-scrollbar"></div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs">Close Walkthrough</button>
            </div>
        </div>
    </div>

    <script>
__SIMULATOR_JS__

__JS_CODE__
    </script>
</body>
</html>
"""

def generate_slides_html():
    slides_html = []

    for s in formatted_slides:
        sid = s['id']
        title = s['title']
        subtitle = s.get('subtitle', '')
        hidden_cls = "" if sid == 1 else "hidden"

        if sid <= 16:
            sim_markup = simulators.get(sid, "<div class='p-4 text-center text-slate-500'>Simulator loading...</div>")

            cp_html = []
            for cidx, cp in enumerate(s['checkpoints']):
                options_markup = []
                safe_ans = cp['ans'].replace("'", "\\'").replace('"', '&quot;')
                safe_expl = cp['explanation'].replace("'", "\\'").replace('"', '&quot;')

                for opt in cp['options']:
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    options_markup.append(f"""
                        <button onclick="checkCheckpoint({sid}, {cidx}, this, '{safe_opt}', '{safe_ans}', '{safe_expl}')" data-option="{safe_opt}" class="checkpoint-opt w-full text-left p-2.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs text-slate-300 hover:text-white transition-all flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_str = "\n".join(options_markup)

                safe_q_speak = cp['q'].replace("'", "\\'").replace('"', '&quot;')
                cp_card = f"""
                <div class="checkpoint-container bg-slate-950/70 border border-slate-800 rounded-2xl p-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between gap-2 mb-2">
                            <div class="flex items-center gap-2">
                                <span class="w-5 h-5 rounded-md bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold flex items-center justify-center">Q{cidx+1}</span>
                                <span class="text-xs font-semibold text-white">{cp['q']}</span>
                            </div>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Teacher Voice" class="text-xs text-slate-400 hover:text-emerald-400 p-1">🗣️</button>
                        </div>
                        <div class="space-y-1.5 mt-3">
                            {opts_str}
                        </div>
                    </div>
                    <div class="checkpoint-feedback hidden mt-3"></div>
                </div>
                """
                cp_html.append(cp_card)

            checkpoints_str = "\n".join(cp_html)

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-6 {hidden_cls}">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-800">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs font-bold flex items-center justify-center">{sid}</span>
                            <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                        </div>
                        <p class="text-xs text-slate-400">{subtitle}</p>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-emerald-300 border border-slate-700 font-semibold self-start sm:self-auto">NCERT Theory & Laboratory</span>
                </div>

                <div class="teacher-lecture-card bg-slate-900/90 border border-emerald-500/30 rounded-2xl p-4 sm:p-5 shadow-lg relative overflow-hidden">
                    <div class="flex items-center justify-between gap-3 mb-2 pb-2 border-b border-slate-800/80">
                        <div class="flex items-center gap-2">
                            <span class="text-xl">👨‍🏫</span>
                            <div>
                                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Classroom Lecture Audio</span>
                                <span class="text-[10px] text-slate-400 block sm:inline sm:ml-2">Teacher Voice Lecture • 0.90x Rate</span>
                            </div>
                        </div>
                        <button onclick="speakLecture()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 transition-all">
                            <span>🔊</span> Listen to Lecture
                        </button>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-normal">
                        {s['speech']}
                    </p>
                </div>

                <div class="simulator-wrapper">
                    {sim_markup}
                </div>

                <div class="space-y-3 pt-2">
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
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
            questions_html = []
            for qidx, q in enumerate(s['questions']):
                opts_html = []
                safe_ans = q['ans'].replace("'", "\\'").replace('"', '&quot;')
                safe_expl = q['explanation'].replace("'", "\\'").replace('"', '&quot;')
                safe_qid = q['id'].replace("'", "\\'")

                for opt in q['options']:
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    opts_html.append(f"""
                        <button onclick="handleChallengeOption('{safe_qid}', this, '{safe_opt}', '{safe_ans}', '{safe_expl}')" data-option="{safe_opt}" class="q-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs text-slate-300 hover:text-white transition-all flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_str = "\n".join(opts_html)

                safe_hint = q['hint'].replace("'", "\\'").replace('"', '&quot;')

                q_card = f"""
                <div id="qcard-{q['id']}" class="bg-slate-950/70 border border-slate-800 rounded-2xl p-4 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between gap-2 mb-2">
                            <span class="w-5 h-5 rounded-md bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold flex items-center justify-center">Q{qidx+1}</span>
                            <button onclick="alert('💡 Hint: {safe_hint}')" class="text-[10px] text-amber-400 hover:text-amber-300 font-semibold flex items-center gap-1">
                                <span>💡</span> Hint
                            </button>
                        </div>
                        <p class="text-xs font-semibold text-white leading-relaxed mb-3">{q['q']}</p>
                        <div class="space-y-1.5">
                            {opts_str}
                        </div>
                    </div>
                    <div>
                        <div class="q-feedback-box hidden mt-3"></div>
                        <button onclick="showSolutionModal('{safe_qid}')" class="mt-3 w-full py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-[11px] font-semibold text-emerald-400 hover:text-emerald-300 flex items-center justify-center gap-1.5 transition-colors">
                            <span>📋</span> Step-by-Step Solution
                        </button>
                    </div>
                </div>
                """
                questions_html.append(q_card)

            all_questions_html = "\n".join(questions_html)

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-6 {hidden_cls}">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs font-bold flex items-center justify-center">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-mono">Silent Comprehensive Review</span>
                </div>
                <p class="text-xs text-slate-400">{subtitle}</p>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {all_questions_html}
                </div>
            </div>
            """
            slides_html.append(slide_content)

    return "\n".join(slides_html)

complete_js = '''
const slidesData = __SLIDES_JSON__;
let currentSlide = 1;
const totalSlides = 20;

const synth = window.speechSynthesis;
let allVoices = [];
let chosenVoice = null;
let currentUtterance = null;
let isAudioPlaying = false;
let speechKeepAliveTimer = null;

let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSuccessChime() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc2.type = 'triangle';
        osc1.frequency.setValueAtTime(523.25, now);
        osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.12);
        osc2.frequency.setValueAtTime(659.25, now);
        osc2.frequency.exponentialRampToValueAtTime(1046.50, now + 0.22);

        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now + 0.05);
        osc1.stop(now + 0.35);
        osc2.stop(now + 0.35);
    } catch (e) {
        console.warn('Audio chime skipped', e);
    }
}

function playErrorBuzz() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(160, now);
        osc.frequency.setValueAtTime(120, now + 0.12);

        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.3);
    } catch (e) {
        console.warn('Audio chime skipped', e);
    }
}

const femaleBlockList = [
    'zira', 'hazel', 'heera', 'priya', 'kalpana', 'veena', 'neerja',
    'aditi', 'kavya', 'ananya', 'pooja', 'sunita', 'shreya', 'sita',
    'geeta', 'meera', 'rekha', 'leela', 'jaya', 'female', 'woman',
    'girl', 'eva', 'sarah', 'samantha', 'victoria', 'karen', 'fiona', 'sophia'
];

function isHindiVoice(v) {
    if (!v) return false;
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    if (lang.includes('hi-in') || lang.includes('hi_in')) return true;
    if (name.includes('hindi') || name.includes('हिन्दी')) return true;
    return false;
}

function isIndianMaleVoice(v) {
    if (!v) return false;
    if (isHindiVoice(v)) return false; // Strictly block Google Hindi
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    for (let f of femaleBlockList) {
        if (name.includes(f)) return false;
    }
    const indianMaleKeywords = [
        'prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'mohan',
        'deepak', 'kumar', 'sanjay', 'ajay', 'vijay', 'amit',
        'rahul', 'rajesh', 'vikram', 'arun', 'manish', 'suresh',
        'ramesh', 'anil', 'sunil', 'ahp', 'cxx'
    ];
    for (let k of indianMaleKeywords) {
        if (name.includes(k)) return true;
    }
    if (lang.includes('en-in') || lang.includes('ta-in') || lang.includes('mr-in')) {
        return !name.includes('female');
    }
    return false;
}

function isUKMaleVoice(v) {
    if (!v) return false;
    if (isHindiVoice(v)) return false;
    const name = (v.name || '').toLowerCase();
    const lang = (v.lang || '').toLowerCase();
    for (let f of femaleBlockList) {
        if (name.includes(f)) return false;
    }
    if (lang.includes('en-gb') || lang.includes('en_gb')) {
        if (name.includes('male') || name.includes('george') || name.includes('oliver') || name.includes('harry')) {
            return true;
        }
        return !femaleBlockList.some(f => name.includes(f));
    }
    if (name.includes('uk english male') || name.includes('google uk english male')) {
        return true;
    }
    return false;
}

function initSpeechEngine() {
    if (!synth) return;

    function populateVoices() {
        allVoices = synth.getVoices() || [];
        const voiceSelect = document.getElementById('voiceSelect');
        if (!voiceSelect) return;

        voiceSelect.innerHTML = '';
        let ukMaleVoices = [];
        let indianMaleVoices = [];
        let otherMaleVoices = [];

        allVoices.forEach((v, index) => {
            if (isHindiVoice(v)) return; // Exclude Google Hindi
            const nameLower = (v.name || '').toLowerCase();
            let isFemale = femaleBlockList.some(f => nameLower.includes(f));
            if (isFemale) return;

            if (isUKMaleVoice(v)) {
                ukMaleVoices.push({ voice: v, index: index, badge: ' 🇬🇧 UK Male' });
            } else if (isIndianMaleVoice(v)) {
                indianMaleVoices.push({ voice: v, index: index, badge: ' 🇮🇳 Indian Male' });
            } else if (nameLower.includes('male') || nameLower.includes('david') || nameLower.includes('george') || nameLower.includes('guy')) {
                otherMaleVoices.push({ voice: v, index: index, badge: ' 👨 Male' });
            }
        });

        // Priority order: UK Male & Indian Male first
        const sortedCandidates = [...ukMaleVoices, ...indianMaleVoices, ...otherMaleVoices];

        if (sortedCandidates.length === 0) {
            allVoices.forEach((v, index) => {
                if (isHindiVoice(v)) return;
                if (!femaleBlockList.some(f => (v.name || '').toLowerCase().includes(f))) {
                    sortedCandidates.push({ voice: v, index: index, badge: '' });
                }
            });
        }

        sortedCandidates.forEach(item => {
            const opt = document.createElement('option');
            opt.value = item.index;
            opt.textContent = `${item.voice.name} (${item.voice.lang})${item.badge || ''}`;
            voiceSelect.appendChild(opt);
        });

        if (sortedCandidates.length > 0) {
            chosenVoice = sortedCandidates[0].voice;
            voiceSelect.value = sortedCandidates[0].index;
        } else if (allVoices.length > 0) {
            chosenVoice = allVoices[0];
            voiceSelect.value = 0;
        }

        voiceSelect.addEventListener('change', (e) => {
            const idx = parseInt(e.target.value);
            if (!isNaN(idx) && allVoices[idx]) {
                chosenVoice = allVoices[idx];
                if (isAudioPlaying) {
                    stopSpeaking();
                    speakLecture();
                }
            }
        });
    }

    populateVoices();
    if (synth.onvoiceschanged !== undefined) {
        synth.onvoiceschanged = populateVoices;
    }
}

function stopSpeaking() {
    if (speechKeepAliveTimer) {
        clearInterval(speechKeepAliveTimer);
        speechKeepAliveTimer = null;
    }
    if (synth) {
        synth.cancel();
    }
    isAudioPlaying = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(playing) {
    const icon = document.getElementById('audioPlayIcon');
    const text = document.getElementById('audioButtonText');
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;

    if (playing) {
        if (icon) icon.textContent = '⏹️';
        if (text) text.textContent = 'Stop Teacher Audio';
        btn.classList.remove('bg-emerald-600', 'hover:bg-emerald-500');
        btn.classList.add('bg-rose-600', 'hover:bg-rose-500', 'text-white');
    } else {
        if (icon) icon.textContent = '🔊';
        if (text) text.textContent = 'Teacher Sound Lecture';
        btn.classList.remove('bg-rose-600', 'hover:bg-rose-500', 'text-white');
        btn.classList.add('bg-emerald-600', 'hover:bg-emerald-500', 'text-slate-950');
    }
}

function speakText(text) {
    if (!synth) return;
    stopSpeaking();

    const cleanText = text.replace(/<[^>]*>/g, '').trim();
    if (!cleanText) return;

    currentUtterance = new SpeechSynthesisUtterance(cleanText);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    currentUtterance.rate = 0.90;
    currentUtterance.pitch = 0.88;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioButtonUI(true);
    };

    currentUtterance.onend = () => {
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        if (speechKeepAliveTimer) {
            clearInterval(speechKeepAliveTimer);
            speechKeepAliveTimer = null;
        }
    };

    currentUtterance.onerror = () => {
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        if (speechKeepAliveTimer) {
            clearInterval(speechKeepAliveTimer);
            speechKeepAliveTimer = null;
        }
    };

    synth.speak(currentUtterance);

    // Keep-alive workaround for Chrome speech synthesis pauses
    speechKeepAliveTimer = setInterval(() => {
        if (synth && synth.speaking) {
            synth.pause();
            synth.resume();
        }
    }, 10000);
}

function speakLecture() {
    if (currentSlide > 16) return; // Silent on exercises
    const currentSlideData = slidesData.find(s => s.id === currentSlide);
    if (!currentSlideData || !currentSlideData.speech) return;
    speakText(currentSlideData.speech);
}

function toggleSpokenLecture() {
    if (isAudioPlaying) {
        stopSpeaking();
    } else {
        speakLecture();
    }
}

window.speakText = speakText;

let userScore = 0;
function addScore(pts = 10) {
    userScore += pts;
    const badge = document.getElementById('scoreBadge');
    if (badge) badge.textContent = `Score: ${userScore}`;
}

function checkCheckpoint(slideId, cpIdx, btn, selectedOpt, correctAns, explanation) {
    const parentContainer = btn.closest('.checkpoint-container');
    if (!parentContainer) return;

    const allButtons = parentContainer.querySelectorAll('.checkpoint-opt');
    allButtons.forEach(b => {
        b.disabled = true;
        b.classList.remove('hover:border-slate-700', 'hover:text-white');
    });

    const isCorrect = (selectedOpt.trim() === correctAns.trim());
    const feedbackBox = parentContainer.querySelector('.checkpoint-feedback');

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-emerald-950/80', 'border-emerald-500/80', 'text-emerald-300');
        playSuccessChime();
        addScore(10);
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-950/80', 'border-rose-500/80', 'text-rose-300');
        playErrorBuzz();

        // Highlight correct option
        allButtons.forEach(b => {
            if (b.getAttribute('data-option') && b.getAttribute('data-option').trim() === correctAns.trim()) {
                b.classList.remove('bg-slate-900', 'border-slate-800');
                b.classList.add('bg-emerald-950/60', 'border-emerald-500/60', 'text-emerald-300');
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        feedbackBox.className = `checkpoint-feedback p-3 rounded-xl border text-xs leading-relaxed ${isCorrect ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300' : 'bg-rose-950/40 border-rose-500/40 text-rose-300'}`;
        feedbackBox.innerHTML = `
            <div class="font-bold mb-1 flex items-center gap-1.5">
                <span>${isCorrect ? '✓ Excellent!' : '✕ Needs Review'}</span>
            </div>
            <p class="text-slate-200">${explanation}</p>
        `;
    }
}

function handleChallengeOption(qid, btn, selectedOpt, correctAns, explanation) {
    const card = document.getElementById(`qcard-${qid}`);
    if (!card) return;

    const allButtons = card.querySelectorAll('.q-opt-btn');
    allButtons.forEach(b => {
        b.disabled = true;
        b.classList.remove('hover:border-slate-700', 'hover:text-white');
    });

    const isCorrect = (selectedOpt.trim() === correctAns.trim());
    const feedbackBox = card.querySelector('.q-feedback-box');

    if (isCorrect) {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-emerald-950/80', 'border-emerald-500/80', 'text-emerald-300');
        playSuccessChime();
        addScore(10);
    } else {
        btn.classList.remove('bg-slate-900', 'border-slate-800');
        btn.classList.add('bg-rose-950/80', 'border-rose-500/80', 'text-rose-300');
        playErrorBuzz();

        allButtons.forEach(b => {
            if (b.getAttribute('data-option') && b.getAttribute('data-option').trim() === correctAns.trim()) {
                b.classList.remove('bg-slate-900', 'border-slate-800');
                b.classList.add('bg-emerald-950/60', 'border-emerald-500/60', 'text-emerald-300');
            }
        });
    }

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        feedbackBox.className = `q-feedback-box p-3 rounded-xl border text-xs leading-relaxed ${isCorrect ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300' : 'bg-rose-950/40 border-rose-500/40 text-rose-300'}`;
        feedbackBox.innerHTML = `
            <div class="font-bold mb-1 flex items-center gap-1.5">
                <span>${isCorrect ? '✓ Correct Answer' : '✕ Incorrect'}</span>
            </div>
            <p class="text-slate-200">${explanation}</p>
        `;
    }
}

function showSolutionModal(qid) {
    let questionObj = null;
    for (let s of slidesData) {
        if (s.questions) {
            const found = s.questions.find(q => q.id === qid);
            if (found) {
                questionObj = found;
                break;
            }
        }
    }
    if (!questionObj) return;

    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body) return;

    const steps = questionObj.solution_steps || [
        "Step 1: Identify key biological parameters and principles from NCERT Class 10.",
        "Step 2: Compare all 4 options against textbook definitions.",
        "Step 3: Confirm final verified answer."
    ];

    body.innerHTML = `
        <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-[10px] uppercase font-bold text-emerald-400 block mb-1">Question</span>
            <p class="text-xs font-semibold text-white">${questionObj.q}</p>
        </div>

        <div class="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40">
            <span class="text-[10px] uppercase font-bold text-emerald-300 block mb-1">Correct Answer</span>
            <p class="text-xs font-bold text-white">${questionObj.ans}</p>
        </div>

        <div class="space-y-2">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-300 block">Step-by-Step Breakdown</span>
            <div class="space-y-2">
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                    <p class="text-xs text-slate-200 leading-relaxed">${steps[0]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                    <p class="text-xs text-slate-200 leading-relaxed">${steps[1]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 flex items-start gap-2.5">
                    <span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                    <p class="text-xs text-slate-200 leading-relaxed">${steps[2]}</p>
                </div>
            </div>
        </div>

        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
            <span class="text-[10px] uppercase font-bold text-slate-400 block mb-1">Key Takeaway</span>
            <p class="text-xs text-slate-300 leading-relaxed">${questionObj.explanation}</p>
        </div>
    `;

    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

function updateSlideView() {
    stopSpeaking();

    // Hide all slides
    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) el.classList.add('hidden');
    }

    // Show current slide
    const curEl = document.getElementById(`slide-${currentSlide}`);
    if (curEl) curEl.classList.remove('hidden');

    // Update Progress bar & indicator
    const prog = document.getElementById('slideProgressBar');
    if (prog) prog.style.width = `${(currentSlide / totalSlides) * 100}%`;

    const ind = document.getElementById('slideIndicator');
    if (ind) ind.textContent = `Slide ${currentSlide}/${totalSlides}`;

    // Audio controls visibility: Slides 1-16 only, silent on 17-20
    const audioControls = document.getElementById('audioControls');
    if (audioControls) {
        audioControls.style.display = (currentSlide <= 16) ? 'flex' : 'none';
    }

    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.style.visibility = (currentSlide === 1) ? 'hidden' : 'visible';
    }

    const nextBtn = document.getElementById('nextBtn');
    const noticeEl = document.getElementById('lastSlideNotice');

    // Terminal slide 20 invariant: Next hidden, lastSlideNotice shown
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (noticeEl) noticeEl.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (noticeEl) noticeEl.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Initialize slide-specific simulator hook if present
    const hookName = `initSlide${currentSlide}`;
    if (typeof window[hookName] === 'function') {
        try {
            window[hookName]();
        } catch (e) {
            console.error(`Error initializing simulator for slide ${currentSlide}:`, e);
        }
    }
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        currentSlide++;
        updateSlideView();
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        currentSlide--;
        updateSlideView();
    }
}

window.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    updateSlideView();
});
'''

slides_html_str = generate_slides_html()
js_code_str = complete_js.replace("__SLIDES_JSON__", json.dumps(formatted_slides))

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_html_str).replace("__SIMULATOR_JS__", SIMULATOR_JS).replace("__JS_CODE__", js_code_str)

output_path = "public/animations/class10-heredity.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {output_path} successfully ({len(final_html)} bytes).")

# Also copy or symlink heredity.html for Lab 2
shutil.copyfile("public/animations/class10-heredity.html", "public/animations/heredity.html")
print("Copied to public/animations/heredity.html for Lab 2.")

# Establish symlinks for all access aliases
symlinks = [
    ("public/animations/chapter8-science-class10.html", "class10-heredity.html"),
    ("public/animations/class10-heredity-lab1.html", "class10-heredity.html"),
    ("public/animations/class10-heredity-lab2.html", "heredity.html")
]

for link_name, target in symlinks:
    if os.path.exists(link_name) or os.path.islink(link_name):
        os.remove(link_name)
    os.symlink(target, link_name)
    print(f"Symlinked {link_name} -> {target}")
