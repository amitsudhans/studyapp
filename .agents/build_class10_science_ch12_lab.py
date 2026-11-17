# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 12: Magnetic Effects of Electric Current
Build complete HTML laboratory: public/animations/class10-magnetic-effects.html
"""

import json
import re
import os
import sys

sys.path.insert(0, os.path.abspath(".agents"))

# Import slide data, simulators, and JS handlers
from class10_science_ch12_data import slides
from class10_science_ch12_sims import simulators
from c10s_ch12_sim_handlers import SIMULATOR_JS

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
        assert sid in simulators or str(sid) in simulators, f"Missing simulator for slide {sid}"

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
            qid = f"c12_q{qidx+1 + (sid-17)*10}"
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

print("All 20 slides for Class 10 Science Chapter 12 passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science — Chapter 12: Magnetic Effects of Electric Current Interactive Lab</title>
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
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 antialiased selection:bg-indigo-500 selection:text-slate-950">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-40 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=science&class=class10" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 flex items-center justify-center text-slate-300 hover:text-white transition-colors text-sm font-semibold">
                    ←
                </a>
                <div>
                    <span class="text-[10px] uppercase font-bold tracking-widest text-indigo-400 block">NCERT Class 10 Science • Chapter 12</span>
                    <h1 class="text-sm sm:text-base font-extrabold text-white flex items-center gap-2">
                        <span>Magnetic Effects of Electric Current</span>
                        <span class="text-[10px] px-1.5 py-0.5 rounded bg-indigo-600/30 text-indigo-300 border border-indigo-500/40">Lab 1</span>
                    </h1>
                </div>
            </div>

            <!-- Voice Controls (Slides 1-16 only) -->
            <div id="audioControls" class="flex items-center gap-2">
                <div class="hidden md:flex items-center gap-1.5 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700/80 text-xs">
                    <span class="text-slate-400">🎙️ Voice:</span>
                    <select id="voiceSelect" class="bg-transparent text-indigo-400 font-medium focus:outline-none max-w-[150px] truncate cursor-pointer text-xs">
                        <option value="">Teacher Sound Engine...</option>
                    </select>
                </div>
                <button id="audioLectureBtn" onclick="toggleSpokenLecture()" class="px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 transition-all">
                    <span id="audioPlayIcon">🔊</span>
                    <span id="audioButtonText" class="hidden sm:inline">Teacher Sound Lecture</span>
                </button>
            </div>

            <div class="flex items-center gap-2">
                <span id="slideIndicator" class="text-xs font-mono px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 border border-slate-700">Slide 1/20</span>
                <span id="scoreBadge" class="hidden sm:inline-block text-xs font-semibold px-2.5 py-1 rounded-lg bg-indigo-950/60 text-indigo-300 border border-indigo-500/30">Score: 0</span>
            </div>
        </div>

        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-800/60 h-1.5 mt-2.5 rounded-full overflow-hidden">
            <div id="slideProgressBar" class="h-full bg-gradient-to-r from-indigo-500 via-sky-400 to-cyan-400 transition-all duration-300" style="width: 5%;"></div>
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
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-bold text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 transition-all">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- 3-Step Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-xl w-full p-5 space-y-4 shadow-2xl">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <h3 class="text-sm sm:text-base font-bold text-white tracking-tight">Step-by-Step Magnetic Calculation</h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm font-bold">✕</button>
            </div>
            <div id="solutionModalBody" class="py-4 space-y-4 max-h-[70vh] overflow-y-auto custom-scrollbar"></div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs">Close Solution</button>
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
            sim_obj = simulators.get(sid) or simulators.get(str(sid), {})
            sim_markup = f"""
            <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 sm:p-5 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <div class="flex items-center gap-2">
                        <span class="text-sm">🧲</span>
                        <h3 class="text-xs font-bold text-slate-100 uppercase tracking-wider">{sim_obj.get('title', '')}</h3>
                    </div>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                        Interactive Studio
                    </span>
                </div>
                <p class="text-xs text-slate-400 leading-relaxed">{sim_obj.get('description', '')}</p>
                <div class="pt-1">
                    {sim_obj.get('html', '')}
                </div>
            </div>
            """

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
                <div class="checkpoint-container bg-slate-900/50 border border-slate-800/80 rounded-xl p-4 space-y-3">
                    <div class="flex items-start justify-between gap-3">
                        <div class="flex items-start gap-2">
                            <span class="w-5 h-5 rounded-md bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">{cidx+1}</span>
                            <p class="text-xs font-semibold text-slate-200">{cp['q']}</p>
                        </div>
                        <button onclick="speakText('{safe_q_speak}')" class="p-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white text-xs transition-colors shrink-0" title="Listen">🔊</button>
                    </div>

                    <div class="space-y-1.5">
                        {opts_str}
                    </div>

                    <div class="checkpoint-feedback hidden"></div>
                </div>
                """
                cp_html.append(cp_card)

            checkpoints_markup = f"""
            <div class="space-y-3">
                <div class="flex items-center justify-between pb-1">
                    <h4 class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                        <span>🎯</span> Concept Checkpoints
                    </h4>
                    <span class="text-[10px] text-slate-400 font-mono">+10 points each</span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {"".join(cp_html)}
                </div>
            </div>
            """

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-5 {hidden_cls}">
                <!-- Header of slide -->
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 text-xs font-bold flex items-center justify-center">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-mono">Lecture & Lab</span>
                </div>
                <p class="text-xs text-slate-400">{subtitle}</p>

                <!-- Simulator Section -->
                {sim_markup}

                <!-- Checkpoints Section -->
                {checkpoints_markup}
            </div>
            """
            slides_html.append(slide_content)

        else:
            # Exercise slides 17-20 (Silent review, 10 challenge questions each)
            questions_html = []
            for q in s['questions']:
                safe_qid = q['id']
                safe_ans = q['ans'].replace("'", "\\'").replace('"', '&quot;')
                safe_expl = q['explanation'].replace("'", "\\'").replace('"', '&quot;')

                opts_markup = []
                for opt in q['options']:
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    opts_markup.append(f"""
                        <button onclick="handleChallengeOption('{safe_qid}', this, '{safe_opt}', '{safe_ans}', '{safe_expl}')" data-option="{safe_opt}" class="q-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 text-xs text-slate-300 hover:text-white transition-all flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_str = "\n".join(opts_markup)

                q_card = f"""
                <div id="qcard-{safe_qid}" class="bg-slate-900/50 border border-slate-800/80 rounded-2xl p-4 flex flex-col justify-between space-y-3">
                    <div class="space-y-3">
                        <div class="flex items-start justify-between gap-2">
                            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                                {safe_qid.upper()}
                            </span>
                            <span class="text-[10px] text-slate-500 italic">Hint: {q['hint']}</span>
                        </div>
                        <p class="text-xs font-medium text-slate-200 leading-relaxed">{q['q']}</p>
                        <div class="space-y-1.5">
                            {opts_str}
                        </div>
                    </div>
                    <div>
                        <div class="q-feedback-box hidden mt-3"></div>
                        <button onclick="showSolutionModal('{safe_qid}')" class="mt-3 w-full py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-[11px] font-semibold text-indigo-400 hover:text-indigo-300 flex items-center justify-center gap-1.5 transition-colors">
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
                        <span class="w-7 h-7 rounded-lg bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 text-xs font-bold flex items-center justify-center">{sid}</span>
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
                    const s = slidesData[currentSlide - 1];
                    if (s && s.speech) startSpeaking(s.speech);
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
    updateAudioBtnUI();
}

function updateAudioBtnUI() {
    const btn = document.getElementById('audioLectureBtn');
    const icon = document.getElementById('audioPlayIcon');
    const txt = document.getElementById('audioButtonText');
    if (!btn || !icon || !txt) return;

    if (isAudioPlaying) {
        icon.textContent = '⏹️';
        txt.textContent = 'Pause Lecture';
        btn.className = 'px-3 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs flex items-center gap-1.5 transition-all';
    } else {
        icon.textContent = '🔊';
        txt.textContent = 'Teacher Sound Lecture';
        btn.className = 'px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 transition-all';
    }
}

function startSpeaking(text) {
    if (!synth || !text) return;
    stopSpeaking();

    const clean = text.replace(/<[^>]*>/g, '').trim();
    if (!clean) return;

    currentUtterance = new SpeechSynthesisUtterance(clean);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    currentUtterance.rate = 0.90;
    currentUtterance.pitch = 0.88;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioBtnUI();
        speechKeepAliveTimer = setInterval(() => {
            if (synth.speaking) {
                synth.pause();
                synth.resume();
            }
        }, 12000);
    };

    currentUtterance.onend = () => {
        stopSpeaking();
    };

    currentUtterance.onerror = (e) => {
        console.warn('Speech error:', e);
        stopSpeaking();
    };

    synth.speak(currentUtterance);
}

function toggleSpokenLecture() {
    if (currentSlide > 16) return;
    if (isAudioPlaying) {
        stopSpeaking();
    } else {
        const s = slidesData[currentSlide - 1];
        if (s && s.speech) {
            startSpeaking(s.speech);
        }
    }
}

window.speakText = function(text) {
    if (!synth || !text) return;
    stopSpeaking();
    const utt = new SpeechSynthesisUtterance(text);
    if (chosenVoice) utt.voice = chosenVoice;
    utt.rate = 0.90;
    utt.pitch = 0.88;
    synth.speak(utt);
};

function speakLecture() {
    toggleSpokenLecture();
}

let score = 0;
const answeredMap = {};

function checkCheckpoint(slideId, cpIdx, btn, chosenOpt, correctAns, explanation) {
    const key = `cp_${slideId}_${cpIdx}`;
    if (answeredMap[key]) return;
    answeredMap[key] = true;

    const parent = btn.closest('.checkpoint-container');
    const allBtns = parent.querySelectorAll('.checkpoint-opt');
    const feedbackBox = parent.querySelector('.checkpoint-feedback');

    const isCorrect = (chosenOpt === correctAns);

    allBtns.forEach(b => {
        b.disabled = true;
        const optVal = b.getAttribute('data-option');
        if (optVal === correctAns) {
            b.className = 'checkpoint-opt w-full text-left p-2.5 rounded-xl bg-emerald-950/80 border border-emerald-500 text-xs text-emerald-200 flex items-center justify-between font-bold';
            b.querySelector('span:last-child').textContent = '✓';
            b.querySelector('span:last-child').className = 'text-emerald-400 font-bold';
        } else if (b === btn && !isCorrect) {
            b.className = 'checkpoint-opt w-full text-left p-2.5 rounded-xl bg-rose-950/80 border border-rose-500 text-xs text-rose-200 flex items-center justify-between font-bold';
            b.querySelector('span:last-child').textContent = '✕';
            b.querySelector('span:last-child').className = 'text-rose-400 font-bold';
        } else {
            b.className = 'checkpoint-opt w-full text-left p-2.5 rounded-xl bg-slate-900/40 border border-slate-800 text-xs text-slate-500 opacity-50 flex items-center justify-between';
        }
    });

    if (isCorrect) {
        score += 10;
        playSuccessChime();
        feedbackBox.className = 'checkpoint-feedback mt-3 p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs space-y-1 block';
        feedbackBox.innerHTML = `
            <div class="font-bold flex items-center gap-1.5"><span>✅</span> Correct Answer! (+10 pts)</div>
            <p class="text-slate-300 leading-relaxed font-normal">${explanation}</p>
        `;
    } else {
        playErrorBuzz();
        feedbackBox.className = 'checkpoint-feedback mt-3 p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-300 text-xs space-y-1 block';
        feedbackBox.innerHTML = `
            <div class="font-bold flex items-center gap-1.5"><span>❌</span> Incorrect</div>
            <p class="text-slate-300 leading-relaxed font-normal">${explanation}</p>
        `;
    }

    const scoreEl = document.getElementById('scoreBadge');
    if (scoreEl) scoreEl.textContent = `Score: ${score}`;
}

function handleChallengeOption(qid, btn, chosenOpt, correctAns, explanation) {
    if (answeredMap[qid]) return;
    answeredMap[qid] = true;

    const card = document.getElementById(`qcard-${qid}`);
    if (!card) return;

    const allBtns = card.querySelectorAll('.q-opt-btn');
    const feedbackBox = card.querySelector('.q-feedback-box');
    const isCorrect = (chosenOpt === correctAns);

    allBtns.forEach(b => {
        b.disabled = true;
        const optVal = b.getAttribute('data-option');
        if (optVal === correctAns) {
            b.className = 'q-opt-btn w-full text-left p-2.5 rounded-xl bg-emerald-950/80 border border-emerald-500 text-xs text-emerald-200 flex items-center justify-between font-bold';
            b.querySelector('span:last-child').textContent = '✓';
            b.querySelector('span:last-child').className = 'text-emerald-400 font-bold';
        } else if (b === btn && !isCorrect) {
            b.className = 'q-opt-btn w-full text-left p-2.5 rounded-xl bg-rose-950/80 border border-rose-500 text-xs text-rose-200 flex items-center justify-between font-bold';
            b.querySelector('span:last-child').textContent = '✕';
            b.querySelector('span:last-child').className = 'text-rose-400 font-bold';
        } else {
            b.className = 'q-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900/40 border border-slate-800 text-xs text-slate-500 opacity-50 flex items-center justify-between';
        }
    });

    if (isCorrect) {
        score += 10;
        playSuccessChime();
        feedbackBox.className = 'q-feedback-box mt-3 p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 text-xs space-y-1 block';
        feedbackBox.innerHTML = `
            <div class="font-bold flex items-center gap-1.5"><span>✅</span> Correct Solution! (+10 pts)</div>
            <p class="text-slate-300 leading-relaxed font-normal">${explanation}</p>
        `;
    } else {
        playErrorBuzz();
        feedbackBox.className = 'q-feedback-box mt-3 p-3 rounded-xl bg-rose-950/60 border border-rose-500/40 text-rose-300 text-xs space-y-1 block';
        feedbackBox.innerHTML = `
            <div class="font-bold flex items-center gap-1.5"><span>❌</span> Solution Derivation Below</div>
            <p class="text-slate-300 leading-relaxed font-normal">${explanation}</p>
        `;
    }

    const scoreEl = document.getElementById('scoreBadge');
    if (scoreEl) scoreEl.textContent = `Score: ${score}`;
}

function showSolutionModal(qid) {
    let targetQuestion = null;
    for (let s of slidesData) {
        if (s.questions) {
            for (let q of s.questions) {
                if (q.id === qid) {
                    targetQuestion = q;
                    break;
                }
            }
        }
        if (targetQuestion) break;
    }
    if (!targetQuestion) return;

    const modal = document.getElementById('solutionModal');
    const modalBody = document.getElementById('solutionModalBody');
    if (!modal || !modalBody) return;

    const stepsHtml = (targetQuestion.solution_steps || []).map((step, idx) => `
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
            <span class="text-[10px] uppercase font-bold text-indigo-400 tracking-wider">Step ${idx+1}</span>
            <p class="text-xs text-slate-200 leading-relaxed font-normal">${step}</p>
        </div>
    `).join('');

    modalBody.innerHTML = `
        <div class="p-3.5 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-xs text-indigo-300 font-semibold">
            ${targetQuestion.q}
        </div>
        <div class="space-y-2">
            ${stepsHtml}
        </div>
        <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-300">
            <strong>Key takeaway:</strong> ${targetQuestion.explanation}
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

    for (let i = 1; i <= totalSlides; i++) {
        const el = document.getElementById(`slide-${i}`);
        if (el) {
            if (i === currentSlide) {
                el.classList.remove('hidden');
            } else {
                el.classList.add('hidden');
            }
        }
    }

    const slideIndicator = document.getElementById('slideIndicator');
    if (slideIndicator) slideIndicator.textContent = `Slide ${currentSlide}/${totalSlides}`;

    const progressBar = document.getElementById('slideProgressBar');
    if (progressBar) progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;

    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.style.visibility = (currentSlide === 1) ? 'hidden' : 'visible';
    }

    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    // Terminal Slide Invariant for Slide 20
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    // Voice controls visible only for slides 1-16
    const audioControls = document.getElementById('audioControls');
    if (audioControls) {
        audioControls.style.display = (currentSlide <= 16) ? 'flex' : 'none';
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Initialize Simulator for current slide
    if (currentSlide <= 16 && typeof initSimulator === 'function') {
        setTimeout(() => {
            initSimulator(currentSlide);
        }, 50);
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
js_code_str = complete_js.replace("__SLIDES_JSON__", json.dumps(formatted_slides, ensure_ascii=False))

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_html_str).replace("__SIMULATOR_JS__", SIMULATOR_JS).replace("__JS_CODE__", js_code_str)

output_path = "public/animations/class10-magnetic-effects.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {output_path} successfully ({len(final_html)} bytes).")

# Establish symlinks:
# Lab 1: class10-magnetic-effects.html
# Lab 2: magnetic-effects-of-electric-current.html (the existing classic lab)
symlinks = [
    ("public/animations/chapter12-science-class10.html", "class10-magnetic-effects.html"),
    ("public/animations/class10-magnetic-effects-lab1.html", "class10-magnetic-effects.html"),
    ("public/animations/class10-magnetic-effects-lab2.html", "magnetic-effects-of-electric-current.html")
]

for link_name, target in symlinks:
    if os.path.exists(link_name) or os.path.islink(link_name):
        os.remove(link_name)
    os.symlink(target, link_name)
    print(f"Symlinked {link_name} -> {target}")
