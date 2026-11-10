# -*- coding: utf-8 -*-
"""
Build Class 3 Mathematics Chapter 5: Fun with Shapes Interactive Animation Lab
Compiles public/animations/class3-maths-fun-with-shapes.html
and creates the 7 required canonical symlinks.
Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class3_maths_ch5_data import SLIDES
from class3_maths_ch5_sims import simulators

# Strict Validation Lists
FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Amma']
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VERIFYING CHAPTER 5 MATHS SLIDES DATA ===")
assert len(SLIDES) == 20, f"Expected 20 slides, found {len(SLIDES)}"

for idx, slide in enumerate(SLIDES):
    sid = slide['id']
    title = slide['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    slide_str = json.dumps(slide)
    for name in FORBIDDEN_CHARACTERS:
        if name.lower() == 'deep':
            assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
        else:
            assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    if sid <= 16:
        wc = len(slide['speech'].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words (must be 195-215)"
        assert len(slide['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in slide['checkpoints']:
            assert len(cp['options']) == 4, f"Slide {sid} checkpoint must have 4 options"
            assert cp['ans'] in cp['options']
    else:
        assert len(slide['questions']) == 10, f"Slide {sid} must have 10 challenge questions"
        for q in slide['questions']:
            assert len(q['options']) == 4, f"Slide {sid} question {q.get('id')} must have 4 options"
            assert q['ans'] in q['options']
            assert len(q['solution_steps']) == 3, f"Slide {sid} question {q.get('id')} must have 3 solution steps"

print("All 20 slides passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 3 Mathematics - Chapter 5: Fun with Shapes</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Fixed Header -->
    <header class="bg-slate-900/90 backdrop-blur sticky top-0 z-30 border-b border-slate-800 px-4 py-3 sm:px-6">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <!-- Brand / Context -->
            <div class="flex items-center gap-3 w-full sm:w-auto">
                <span class="text-2xl sm:text-3xl">📐</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 3</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Joyful Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 5</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">Fun with Shapes Interactive Animated Laboratory</h1>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center flex-wrap gap-2 w-full sm:w-auto justify-between sm:justify-end">
                <div class="flex items-center gap-1.5 bg-slate-800/90 border border-slate-700 rounded-xl px-2.5 py-1 text-xs">
                    <span class="text-slate-400 text-[11px] font-medium hidden md:inline">Voice:</span>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-2 py-1 focus:ring-1 focus:ring-amber-500 outline-none max-w-[150px] sm:max-w-[210px] truncate" title="Select Indian Male Voice">
                        <option value="">Detecting Voice...</option>
                    </select>
                </div>
                <div id="audioControls" class="transition-opacity">
                    <button id="audioLectureBtn" onclick="toggleAudio()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white flex items-center gap-1.5 text-xs font-semibold transition shadow-sm" title="Listen to Pure Indian Male Teacher Lecture">
                        <span id="audioPlayIcon">🔊</span>
                        <span id="audioButtonText" class="text-xs font-bold">Teacher Sound Lecture</span>
                    </button>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-amber-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700">Slide <span id="slideCounter">1 / 20</span></span>
                </div>
            </div>
        </div>

        <!-- Chapter Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-3">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-sky-500 to-emerald-500 h-1 w-[5%] transition-all duration-300"></div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto w-full p-4 sm:p-6 flex-1">
__SLIDES_HTML__
    </main>

    <!-- Bottom Navigation Footer -->
    <footer class="bg-slate-900/90 backdrop-blur sticky bottom-0 border-t border-slate-800 px-4 py-3 z-30">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <button id="prevBtn" onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-semibold text-xs sm:text-sm flex items-center gap-2 transition shadow">
                <span>←</span> Previous
            </button>

            <!-- Slide 20 Terminal Invariant Container -->
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-amber-500/20 border border-amber-500/40 text-amber-300 font-bold text-xs sm:text-sm text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs sm:text-sm flex items-center gap-2 transition shadow-md">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- 3-Step Mathematical Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <h3 class="text-sm sm:text-base font-bold text-white tracking-tight">Mathematical Solution Walkthrough</h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center text-sm font-bold">✕</button>
            </div>
            <div id="solutionModalBody" class="py-4"></div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold">Close</button>
            </div>
        </div>
    </div>

    <!-- Data Injection & Engine Script -->
    <script>
        window.slideCurriculumData = __SLIDES_JSON__;
        window.challengeQuestionsMap = {};
        window.slideCurriculumData.forEach(s => {
            if (s.questions) {
                s.questions.forEach(q => {
                    window.challengeQuestionsMap[q.id] = q;
                });
            }
        });
        __JS_CODE__
    </script>
</body>
</html>
"""

def generate_slides_html():
    slides_html = []

    for s in SLIDES:
        sid = s['id']
        title = s['title']
        badge = s.get('badge', '')
        desc = s.get('description', '')
        hidden_cls = "" if sid == 1 else "hidden"

        if sid <= 16:
            sim_markup = simulators.get(s['sim_id'], "<div class='p-4 text-center text-slate-500'>Simulator loading...</div>")

            # Format Checkpoints
            cp_html = []
            for cidx, cp in enumerate(s['checkpoints']):
                options_markup = []
                safe_ans = cp['ans'].replace("'", "\\'").replace('"', '&quot;')
                safe_expl = cp['explanation'].replace("'", "\\'").replace('"', '&quot;')

                for opt_idx, opt in enumerate(cp['options']):
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    options_markup.append(f"""
                        <button onclick="checkCheckpoint({sid}, {cidx}, this, '{safe_opt}', '{safe_ans}', '{safe_expl}')" data-option="{safe_opt}" class="checkpoint-opt w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between">
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
                                <span class="w-5 h-5 rounded-md bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center justify-center font-bold text-[10px]">Q{cidx + 1}</span>
                                <span class="text-xs font-semibold text-white">{cp['q']}</span>
                            </div>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-amber-400 hover:text-amber-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
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
                <!-- Title Header -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-800">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="w-6 h-6 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                            <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                        </div>
                        <p class="text-xs text-slate-400">{desc}</p>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-amber-300 border border-slate-700 font-semibold self-start sm:self-auto">{badge}</span>
                </div>

                <!-- Bespoke Simulator -->
                <div class="simulator-wrapper">
                    {sim_markup}
                </div>

                <!-- 2 Checkpoints -->
                <div class="space-y-3 pt-2">
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
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
            # Challenge Slides (17-20)
            questions_html = []
            for qidx, q in enumerate(s['questions']):
                opts_html = []
                safe_ans = q['ans'].replace("'", "\\'").replace('"', '&quot;')
                safe_expl = q['explanation'].replace("'", "\\'").replace('"', '&quot;')
                safe_qid = q['id'].replace("'", "\\'")

                for opt in q['options']:
                    safe_opt = opt.replace("'", "\\'").replace('"', '&quot;')
                    opts_html.append(f"""
                        <button onclick="handleChallengeOption('{safe_qid}', this, '{safe_opt}', '{safe_ans}', '{safe_expl}')" data-option="{safe_opt}" class="q-opt-btn w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between">
                            <span>{opt}</span>
                            <span class="text-slate-600 text-[10px]">●</span>
                        </button>
                    """)
                opts_joined = "\n".join(opts_html)

                safe_q_speak = q['q'].replace("'", "\\'").replace('"', '&quot;')
                card = f"""
                <div id="qcard-{q['id']}" class="quiz-question-card bg-slate-950/80 border border-slate-800 rounded-2xl p-4 flex flex-col justify-between space-y-3">
                    <div>
                        <div class="flex items-start justify-between gap-2">
                            <span class="w-6 h-6 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center justify-center font-bold text-xs shrink-0">{qidx + 1}</span>
                            <p class="text-xs sm:text-sm font-semibold text-white flex-1">{q['q']}</p>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-amber-400 hover:text-amber-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
                        </div>
                        <div class="space-y-1.5 mt-3">
                            {opts_joined}
                        </div>
                    </div>
                    <div class="q-feedback-box hidden"></div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-800/80 text-[11px]">
                        <span class="text-slate-500 italic">💡 Hint: {q['hint']}</span>
                        <button onclick="showSolutionModal('{q['id']}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 font-semibold transition">
                            Solution Walkthrough →
                        </button>
                    </div>
                </div>
                """
                questions_html.append(card)

            all_questions_html = "\n".join(questions_html)

            slide_content = f"""
            <div id="slide-{sid}" class="space-y-6 {hidden_cls}">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-medium">10 Questions Multi-Choice Quiz</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {all_questions_html}
                </div>
            </div>
            """
            slides_html.append(slide_content)

    return "\n".join(slides_html)

# Generate JS engine code
complete_js = r'''
// =========================================================================
// PURE INDIAN MALE TEACHER SOUND ENGINE & SLIDE ORCHESTRATION
// NCERT Class 3 Mathematics - Chapter 5: Fun with Shapes
// =========================================================================

let currentSlide = 1;
const totalSlides = 20;
let isAudioPlaying = false;
let currentUtterance = null;
let synth = window.speechSynthesis;
let selectedVoice = null;
let allVoices = [];
let speechKeepAliveTimer = null;

// Audio Context for Chimes & Acoustics
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSuccessChime() {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(523.25, now);
        osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.12);
        osc1.frequency.exponentialRampToValueAtTime(783.99, now + 0.24);

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(659.25, now);
        osc2.frequency.exponentialRampToValueAtTime(783.99, now + 0.12);
        osc2.frequency.exponentialRampToValueAtTime(1046.50, now + 0.24);

        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.38);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 0.38);
        osc2.stop(now + 0.38);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
    }
}

function playErrorChime() {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(261.63, now);
        osc.frequency.exponentialRampToValueAtTime(196.00, now + 0.20);

        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.28);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.28);
    } catch(e) {
        console.warn("Audio chime unsupported:", e);
    }
}

function playTone(freq, type = 'sine', duration = 0.15, gainVol = 0.2) {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = type;
        osc.frequency.setValueAtTime(freq, now);

        gain.gain.setValueAtTime(gainVol, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + duration);
    } catch(e) {}
}

const femaleBlockList = [
    'female', 'woman', 'girl', 'zira', 'kavya', 'kalpana', 'veena',
    'siri', 'samantha', 'victoria', 'karen', 'moira', 'tessa', 'fiona',
    'helena', 'catherine', 'monica', 'paulina', 'lucia', 'sara', 'anna',
    'jenny', 'aria', 'google हिन्दी', 'google english (india)', 'neerja',
    'heera', 'priya', 'swara', 'ananya', 'aditi', 'pallavi', 'shreya',
    'vani', 'maya', 'pooja', 'sunita', 'geeta', 'seema', 'rekha'
];

function isIndianMaleVoice(v) {
    if (!v) return false;
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

    if (lang.includes('en-in') || lang.includes('hi-in') || lang.includes('ta-in') || lang.includes('mr-in')) {
        return !name.includes('female');
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
        let indianMaleVoices = [];
        let otherMaleVoices = [];

        allVoices.forEach((v, index) => {
            const nameLower = (v.name || '').toLowerCase();
            let isFemale = femaleBlockList.some(f => nameLower.includes(f));
            if (isFemale) return;

            if (isIndianMaleVoice(v)) {
                indianMaleVoices.push({ voice: v, index: index });
            } else if (nameLower.includes('male') || nameLower.includes('david') || nameLower.includes('george') || nameLower.includes('guy')) {
                otherMaleVoices.push({ voice: v, index: index });
            }
        });

        const sortedCandidates = [...indianMaleVoices, ...otherMaleVoices];

        if (sortedCandidates.length === 0) {
            allVoices.forEach((v, index) => {
                if (!femaleBlockList.some(f => (v.name || '').toLowerCase().includes(f))) {
                    sortedCandidates.push({ voice: v, index: index });
                }
            });
        }

        sortedCandidates.forEach(item => {
            const opt = document.createElement('option');
            opt.value = item.index;
            opt.textContent = `${item.voice.name} (${item.voice.lang})${isIndianMaleVoice(item.voice) ? ' 🇮🇳 Pure Indian Male' : ' 👨 Male'}`;
            voiceSelect.appendChild(opt);
        });

        if (sortedCandidates.length > 0) {
            selectedVoice = sortedCandidates[0].voice;
            voiceSelect.value = sortedCandidates[0].index;
        }
    }

    populateVoices();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoices;
    }
}

function onVoiceChange() {
    const voiceSelect = document.getElementById('voiceSelect');
    if (!voiceSelect || !allVoices) return;
    const idx = parseInt(voiceSelect.value);
    if (!isNaN(idx) && allVoices[idx]) {
        selectedVoice = allVoices[idx];
        if (isAudioPlaying) {
            speakLecture();
        }
    }
}

function toggleAudio() {
    if (isAudioPlaying) {
        stopSpeaking();
    } else {
        speakLecture();
    }
}

function stopSpeaking() {
    if (synth) synth.cancel();
    stopKeepAlive();
    isAudioPlaying = false;
    updateAudioButtonUI(false);
}

function startKeepAlive() {
    stopKeepAlive();
    speechKeepAliveTimer = setInterval(() => {
        if (synth && synth.speaking) {
            synth.pause();
            synth.resume();
        } else {
            stopKeepAlive();
        }
    }, 8000);
}

function stopKeepAlive() {
    if (speechKeepAliveTimer) {
        clearInterval(speechKeepAliveTimer);
        speechKeepAliveTimer = null;
    }
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    const icon = document.getElementById('audioPlayIcon');
    const label = document.getElementById('audioButtonText');
    if (!btn || !icon || !label) return;

    if (playing) {
        btn.classList.remove('bg-cyan-600', 'hover:bg-cyan-500');
        btn.classList.add('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        icon.textContent = '⏹️';
        label.textContent = 'Pause Lecture';
    } else {
        btn.classList.remove('bg-amber-600', 'hover:bg-amber-500', 'animate-pulse');
        btn.classList.add('bg-cyan-600', 'hover:bg-cyan-500');
        icon.textContent = '🔊';
        label.textContent = 'Teacher Sound Lecture';
    }
}

function speakLecture() {
    if (!synth) return;
    stopSpeaking();

    if (currentSlide > 16) {
        alert("Challenge questions are interactive quiz slides. Use the 🔊 speaker button on any question to hear it spoken aloud!");
        return;
    }

    const currentSlideData = window.slideCurriculumData ? window.slideCurriculumData.find(s => s.id === currentSlide) : null;
    if (!currentSlideData || !currentSlideData.speech) return;

    const speechText = currentSlideData.speech;
    currentUtterance = new SpeechSynthesisUtterance(speechText);

    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }
    currentUtterance.rate = 0.90;
    currentUtterance.pitch = 0.88;

    currentUtterance.onstart = () => {
        isAudioPlaying = true;
        updateAudioButtonUI(true);
        startKeepAlive();
    };

    currentUtterance.onend = () => {
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        stopKeepAlive();
    };

    currentUtterance.onerror = (e) => {
        console.warn("Speech synthesis error:", e);
        isAudioPlaying = false;
        updateAudioButtonUI(false);
        stopKeepAlive();
    };

    synth.speak(currentUtterance);
}

window.speakText = function(text) {
    if (!synth || !text) return;
    synth.cancel();
    stopKeepAlive();

    const u = new SpeechSynthesisUtterance(text);
    if (selectedVoice) {
        u.voice = selectedVoice;
    }
    u.rate = 0.90;
    u.pitch = 0.88;
    synth.speak(u);
};

// Slide Navigation & Invariant Enforcement
function showSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    stopSpeaking();
    currentSlide = slideNum;

    for (let i = 1; i <= totalSlides; i++) {
        const slideEl = document.getElementById(`slide-${i}`);
        if (slideEl) {
            if (i === currentSlide) {
                slideEl.classList.remove('hidden');
            } else {
                slideEl.classList.add('hidden');
            }
        }
    }

    const counterEl = document.getElementById('slideCounter');
    if (counterEl) counterEl.textContent = `${currentSlide} / ${totalSlides}`;

    const progressEl = document.getElementById('progressBar');
    if (progressEl) {
        const pct = (currentSlide / totalSlides) * 100;
        progressEl.style.width = `${pct}%`;
    }

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');

    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }

    // STRICT INVARIANT FOR SLIDE 20: Next button hidden, Last slide notice shown
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.disabled = false;
        }
        if (lastNotice) lastNotice.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

// Checkpoint Handling
function checkCheckpoint(slideId, cpIdx, btnEl, selectedOpt, correctAns, explanation) {
    const container = btnEl.closest('.checkpoint-container');
    if (!container) return;

    const allButtons = container.querySelectorAll('.checkpoint-opt');
    const feedbackEl = container.querySelector('.checkpoint-feedback');

    allButtons.forEach(b => {
        b.disabled = true;
        b.classList.remove('hover:bg-slate-800', 'bg-slate-900');
        const bOpt = b.getAttribute('data-option');
        if (bOpt === correctAns) {
            b.classList.add('bg-emerald-950/80', 'border-emerald-600', 'text-emerald-300');
            b.querySelector('span:last-child').textContent = '✓';
            b.querySelector('span:last-child').className = 'text-emerald-400 font-bold';
        } else if (b === btnEl) {
            b.classList.add('bg-rose-950/80', 'border-rose-600', 'text-rose-300');
            b.querySelector('span:last-child').textContent = '✕';
            b.querySelector('span:last-child').className = 'text-rose-400 font-bold';
        } else {
            b.classList.add('opacity-40');
        }
    });

    if (feedbackEl) {
        feedbackEl.classList.remove('hidden');
        if (selectedOpt === correctAns) {
            playSuccessChime();
            feedbackEl.className = 'checkpoint-feedback mt-3 p-3 rounded-xl bg-emerald-950/60 border border-emerald-800/80 text-xs text-emerald-300';
            feedbackEl.innerHTML = `<strong>Correct!</strong> ${explanation}`;
        } else {
            playErrorChime();
            feedbackEl.className = 'checkpoint-feedback mt-3 p-3 rounded-xl bg-rose-950/60 border border-rose-800/80 text-xs text-rose-300';
            feedbackEl.innerHTML = `<strong>Not quite.</strong> ${explanation}`;
        }
    }
}

// Challenge Option Handling
function handleChallengeOption(qId, btnEl, selectedOpt, correctAns, explanation) {
    const card = document.getElementById(`qcard-${qId}`);
    if (!card) return;

    const allBtns = card.querySelectorAll('.q-opt-btn');
    const feedbackBox = card.querySelector('.q-feedback-box');

    allBtns.forEach(b => {
        b.disabled = true;
        b.classList.remove('hover:bg-slate-800', 'bg-slate-900');
        const bOpt = b.getAttribute('data-option');
        if (bOpt === correctAns) {
            b.classList.add('bg-emerald-950/80', 'border-emerald-600', 'text-emerald-300');
            b.querySelector('span:last-child').textContent = '✓';
            b.querySelector('span:last-child').className = 'text-emerald-400 font-bold';
        } else if (b === btnEl) {
            b.classList.add('bg-rose-950/80', 'border-rose-600', 'text-rose-300');
            b.querySelector('span:last-child').textContent = '✕';
            b.querySelector('span:last-child').className = 'text-rose-400 font-bold';
        } else {
            b.classList.add('opacity-40');
        }
    });

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOpt === correctAns) {
            playSuccessChime();
            feedbackBox.className = 'q-feedback-box p-3 rounded-xl bg-emerald-950/70 border border-emerald-800 text-xs text-emerald-300';
            feedbackBox.innerHTML = `<strong>Correct!</strong> ${explanation}`;
        } else {
            playErrorChime();
            feedbackBox.className = 'q-feedback-box p-3 rounded-xl bg-rose-950/70 border border-rose-800 text-xs text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect.</strong> ${explanation}`;
        }
    }
}

// 3-Step Solution Modal Display
function showSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    const qData = window.challengeQuestionsMap[qId];
    if (!modal || !body || !qData) return;

    let stepsHtml = '';
    if (qData.solution_steps && qData.solution_steps.length >= 3) {
        stepsHtml = `
            <div class="space-y-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Step 1: Geometric Premise</span>
                    <p class="text-xs text-slate-300">${qData.solution_steps[0]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Step 2: Mathematical Deduction</span>
                    <p class="text-xs text-slate-300">${qData.solution_steps[1]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Step 3: Verification & Conclusion</span>
                    <p class="text-xs text-slate-300">${qData.solution_steps[2]}</p>
                </div>
            </div>
        `;
    } else {
        stepsHtml = `<p class="text-xs text-slate-300">${qData.explanation}</p>`;
    }

    body.innerHTML = `
        <div class="space-y-4">
            <div class="border-b border-slate-800 pb-3">
                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Problem Statement</span>
                <p class="text-sm font-semibold text-white mt-1">${qData.q}</p>
                <div class="mt-2 text-xs text-emerald-400 font-bold">Answer: ${qData.ans}</div>
            </div>
            <div>
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-2">3-Step Solution Breakdown</span>
                ${stepsHtml}
            </div>
        </div>
    `;

    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
'''

# Compile Master File
slides_markup = generate_slides_html()
slides_json_str = json.dumps(SLIDES, ensure_ascii=False)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__SLIDES_JSON__", slides_json_str)
final_html = final_html.replace("__JS_CODE__", complete_js)

out_file = os.path.join(os.path.dirname(__file__), "..", "public", "animations", "class3-maths-fun-with-shapes.html")
out_file = os.path.abspath(out_file)

with open(out_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation lab written to: {out_file} ({len(final_html):,} bytes)")

# Create 7 Canonical Symlinks
symlinks = [
    "chapter5-maths-class3.html",
    "class3-maths-chapter5.html",
    "class3-fun-with-shapes.html",
    "fun-with-shapes-class3.html",
    "class3-maths-fun-with-shapes-lab.html",
    "class3-math-fun-with-shapes.html",
    "class3-fun-with-shapes-lab.html"
]

animations_dir = os.path.dirname(out_file)
master_basename = os.path.basename(out_file)

for link_name in symlinks:
    link_path = os.path.join(animations_dir, link_name)
    if os.path.exists(link_path) or os.path.islink(link_path):
        os.remove(link_path)
    os.symlink(master_basename, link_path)
    print(f"Created symlink: {link_name} -> {master_basename}")

print("=== CHAPTER 5 MATHS LAB GENERATION COMPLETE ===")
