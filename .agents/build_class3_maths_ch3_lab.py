# -*- coding: utf-8 -*-
"""
Build Class 3 Mathematics Chapter 3: Double Century Interactive Animation Lab
Compiles public/animations/class3-maths-double-century.html
and creates the 7 required symlinks.
Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class3_maths_ch3_data import SLIDES
from class3_maths_ch3_sims import simulators

# Strict Validation Lists
FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu']
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VERIFYING CHAPTER 3 MATHS SLIDES DATA ===")
assert len(SLIDES) == 20, f"Expected 20 slides, found {len(SLIDES)}"

for idx, slide in enumerate(SLIDES):
    sid = slide['id']
    title = slide['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    slide_str = json.dumps(slide)
    for name in FORBIDDEN_CHARACTERS:
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str), f"Slide {sid} contains character name '{name}'"
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
    <title>Class 3 Mathematics - Chapter 3: Double Century</title>
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
                <span class="text-2xl sm:text-3xl">🏏</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 3</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Joyful Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 3</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">Double Century Interactive Animated Laboratory</h1>
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
// NCERT Class 3 Mathematics - Chapter 3: Double Century
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

// Live High/Low Feedback Chimes
function playSuccessChime() {
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc1 = ctx.createOscillator();
        const osc2 = ctx.createOscillator();
        const gain = ctx.createGain();

        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(523.25, now); // C5
        osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.12); // E5
        osc1.frequency.exponentialRampToValueAtTime(783.99, now + 0.24); // G5

        osc2.type = 'triangle';
        osc2.frequency.setValueAtTime(659.25, now);
        osc2.frequency.exponentialRampToValueAtTime(783.99, now + 0.12);
        osc2.frequency.exponentialRampToValueAtTime(1046.50, now + 0.24); // C6

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
        osc.frequency.setValueAtTime(261.63, now); // C4
        osc.frequency.exponentialRampToValueAtTime(196.00, now + 0.20); // G3

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

// Female blocker list to guarantee Pure Indian Male Voice
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
    if (synth) {
        synth.cancel();
    }
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

    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide > 16) {
            audioBtn.style.opacity = '0.5';
            audioBtn.title = "Challenge questions are interactive quiz slides. Use 🔊 on questions to read aloud.";
        } else {
            audioBtn.style.opacity = '1';
            audioBtn.title = "Listen to Pure Indian Male Teacher Lecture";
        }
    }

    // Initialize slide simulator
    initSlideSimulator(currentSlide);

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
    }
}

// Checkpoint Answer Checking
function checkCheckpoint(slideId, cpIdx, selectedBtn, selectedOption, correctAns, explanation) {
    const parentContainer = selectedBtn.closest('.checkpoint-container');
    const buttons = parentContainer.querySelectorAll('.checkpoint-opt');
    const feedbackBox = parentContainer.querySelector('.checkpoint-feedback');

    buttons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800', 'border-slate-700');
        if (btn.dataset.option === correctAns) {
            btn.classList.add('bg-emerald-700', 'text-white', 'border-emerald-500');
        } else if (btn === selectedBtn) {
            btn.classList.add('bg-rose-700', 'text-white', 'border-rose-500');
        } else {
            btn.classList.add('opacity-50');
        }
    });

    if (feedbackBox) {
        feedbackBox.classList.remove('hidden');
        if (selectedOption === correctAns) {
            playSuccessChime();
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-xs">
                    <span class="font-bold">✅ Excellent!</span> ${explanation}
                </div>
            `;
        } else {
            playErrorChime();
            feedbackBox.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/60 border border-rose-500/50 text-rose-200 text-xs">
                    <span class="font-bold">❌ Not quite!</span> Correct answer: <strong>${correctAns}</strong>.<br>${explanation}
                </div>
            `;
        }
    }
}

// Challenge Question Handler
function handleChallengeOption(qId, selectedBtn, selectedOption, correctAns, explanation) {
    const card = document.getElementById(`qcard-${qId}`);
    if (!card) return;

    const buttons = card.querySelectorAll('.q-opt-btn');
    const feedback = card.querySelector('.q-feedback-box');

    buttons.forEach(btn => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800');
        if (btn.dataset.option === correctAns) {
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-500');
        } else if (btn === selectedBtn) {
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-500');
        } else {
            btn.classList.add('opacity-40');
        }
    });

    if (feedback) {
        feedback.classList.remove('hidden');
        if (selectedOption === correctAns) {
            playSuccessChime();
            feedback.innerHTML = `
                <div class="p-3 rounded-xl bg-emerald-950/70 border border-emerald-500/60 text-emerald-200 text-xs">
                    <span class="font-bold">🎉 Correct!</span> ${explanation}
                </div>
            `;
        } else {
            playErrorChime();
            feedback.innerHTML = `
                <div class="p-3 rounded-xl bg-rose-950/70 border border-rose-500/60 text-rose-200 text-xs">
                    <span class="font-bold">❌ Incorrect!</span> Correct answer: <strong>${correctAns}</strong>.<br>${explanation}
                </div>
            `;
        }
    }
}

function toggleHint(qId) {
    const el = document.getElementById(`hint-${qId}`);
    if (el) el.classList.toggle('hidden');
}

function showSolutionModal(qId) {
    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body || !window.challengeQuestionsMap) return;

    const q = window.challengeQuestionsMap[qId];
    if (!q) return;

    body.innerHTML = `
        <div class="space-y-3 text-slate-200 text-xs sm:text-sm">
            <div class="font-bold text-amber-300 text-sm sm:text-base">${q.q}</div>
            <div class="p-2.5 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-emerald-300 font-semibold">
                Correct Answer: ${q.ans}
            </div>
            <div class="space-y-2 pt-2">
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold">Step 1:</span> ${q.solution_steps.step1}
                </div>
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-sky-400 font-bold">Step 2:</span> ${q.solution_steps.step2}
                </div>
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-emerald-400 font-bold">Step 3:</span> ${q.solution_steps.step3}
                </div>
            </div>
            <div class="pt-2 text-slate-400 text-xs border-t border-slate-800">
                <strong>Explanation:</strong> ${q.explanation}
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        prevSlide();
    }
});

// =========================================================================
// 16 BESPOKE INTERACTIVE SIMULATORS FOR CHAPTER 3
// =========================================================================

// Simulator 1: Cave Wall Tally
let tallyCount = 17;
let tallyGroupSize = 5;

function addTally(delta) {
    tallyCount = Math.max(0, Math.min(60, tallyCount + delta));
    playTone(440, 'triangle', 0.08);
    renderTally();
}

function setTallyGroup(size) {
    tallyGroupSize = size;
    ['btnGroup5', 'btnGroup10', 'btnGroup20'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-amber-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });
    const active = document.getElementById(`btnGroup${size}`);
    if (active) {
        active.classList.add('bg-amber-600', 'text-white');
    }
    playTone(520, 'sine', 0.1);
    renderTally();
}

function resetTally() {
    tallyCount = 0;
    renderTally();
}

function renderTally() {
    const area = document.getElementById('tallyDisplayArea');
    const badge = document.getElementById('tallyCountBadge');
    const summary = document.getElementById('tallyGroupingSummary');
    if (!area || !badge) return;

    badge.textContent = `Total Marks: ${tallyCount}`;

    const bundles = Math.floor(tallyCount / tallyGroupSize);
    const singles = tallyCount % tallyGroupSize;

    if (summary) {
        summary.textContent = `Grouping: ${bundles} bundle${bundles !== 1 ? 's' : ''} of ${tallyGroupSize} + ${singles} single scratch${singles !== 1 ? 'es' : ''} = ${tallyCount} marks`;
    }

    let html = '';
    for (let b = 0; b < bundles; b++) {
        html += `<div class="bg-stone-900 border border-amber-600/60 p-2 rounded-lg flex items-center gap-1.5 shadow">
            <span class="text-[10px] text-amber-400 font-mono font-bold mr-1">[${tallyGroupSize}]</span>
            <div class="flex gap-1">`;
        for (let i = 0; i < Math.min(tallyGroupSize, 10); i++) {
            html += `<div class="w-1.5 h-7 bg-amber-400 rounded-full"></div>`;
        }
        if (tallyGroupSize > 10) {
            html += `<span class="text-xs text-amber-300 font-mono">+${tallyGroupSize - 10}</span>`;
        }
        html += `</div></div>`;
    }

    if (singles > 0) {
        html += `<div class="bg-stone-900/50 border border-stone-700 p-2 rounded-lg flex items-center gap-1.5">
            <span class="text-[10px] text-stone-400 font-mono mr-1">[Loose]</span>
            <div class="flex gap-1.5">`;
        for (let s = 0; s < singles; s++) {
            html += `<div class="w-1.5 h-6 bg-stone-300 rounded-full"></div>`;
        }
        html += `</div></div>`;
    }

    if (tallyCount === 0) {
        html = `<div class="text-xs text-stone-500 italic p-2">Cave surface is clear. Click +1 or +5 to carve tally scratches!</div>`;
    }

    area.innerHTML = html;
}

// Simulator 2: Base Ten System
let digitH = 1, digitT = 4, digitO = 6;

function changeDigit(col, delta) {
    if (col === 'h') digitH = Math.max(0, Math.min(9, digitH + delta));
    else if (col === 't') digitT = Math.max(0, Math.min(9, digitT + delta));
    else if (col === 'o') digitO = Math.max(0, Math.min(9, digitO + delta));
    playTone(350 + (col === 'h' ? 200 : col === 't' ? 100 : 0), 'sine', 0.08);
    updateBaseTenView();
}

function setBaseTenPreset(h, t, o) {
    digitH = h; digitT = t; digitO = o;
    playSuccessChime();
    updateBaseTenView();
}

function updateBaseTenView() {
    const elH = document.getElementById('digitH');
    const elT = document.getElementById('digitT');
    const elO = document.getElementById('digitO');
    const vH = document.getElementById('valH');
    const vT = document.getElementById('valT');
    const vO = document.getElementById('valO');
    const eq = document.getElementById('baseTenEquation');
    const nameEl = document.getElementById('baseTenWordName');

    if (!elH || !elT || !elO) return;

    elH.textContent = digitH; elT.textContent = digitT; elO.textContent = digitO;
    if (vH) vH.textContent = `${digitH * 100}`;
    if (vT) vT.textContent = `${digitT * 10}`;
    if (vO) vO.textContent = `${digitO}`;

    const total = (digitH * 100) + (digitT * 10) + digitO;
    if (eq) eq.textContent = `${digitH * 100} + ${digitT * 10} + ${digitO} = ${total}`;
    if (nameEl) nameEl.textContent = `"${numberToWords(total)}"`;
}

function numberToWords(n) {
    if (n === 0) return 'Zero';
    const ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
    const tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];

    let words = '';
    if (Math.floor(n / 100) > 0) {
        words += ones[Math.floor(n / 100)] + ' Hundred ';
        n %= 100;
        if (n > 0) words += 'and ';
    }
    if (n > 0) {
        if (n < 20) {
            words += ones[n];
        } else {
            words += tens[Math.floor(n / 10)];
            if (n % 10 > 0) words += '-' + ones[n % 10];
        }
    }
    return words.trim();
}

// Simulator 3: Zero Placeholder
function setZeroDemo(val) {
    playTone(480, 'sine', 0.1);
    const boxWith = document.getElementById('withZeroBox');
    const boxWithout = document.getElementById('withoutZeroBox');
    if (!boxWith || !boxWithout) return;

    if (val === 105) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">With Zero Placeholder (105)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40">
                    <span class="text-[10px] text-indigo-300 block">HUNDREDS</span>
                    <span class="text-2xl font-black font-mono text-indigo-300">1</span>
                    <span class="text-[10px] text-slate-400 block">1 bundle (100)</span>
                </div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40">
                    <span class="text-[10px] text-cyan-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-cyan-300">0</span>
                    <span class="text-[10px] text-cyan-400 block font-bold">Empty space</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">5</span>
                    <span class="text-[10px] text-slate-400 block">5 singles</span>
                </div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 100 + 0 + 5 = <strong class="text-cyan-300 text-sm">105</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Zero (Collapsed: 15)</span>
            <div class="grid grid-cols-2 gap-2 w-3/4 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40">
                    <span class="text-[10px] text-rose-300 block">TENS</span>
                    <span class="text-2xl font-black font-mono text-rose-300">1</span>
                    <span class="text-[10px] text-slate-400 block">1 ten (10)</span>
                </div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40">
                    <span class="text-[10px] text-amber-300 block">ONES</span>
                    <span class="text-2xl font-black font-mono text-amber-300">5</span>
                    <span class="text-[10px] text-slate-400 block">5 singles</span>
                </div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 10 + 5 = <strong class="text-rose-400 text-sm">15 (Disaster! Lost 90!)</strong></div>
        `;
    } else if (val === 150) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">With Zero in Ones (150)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40"><span class="text-[10px] text-indigo-300 block">HUNDREDS</span><span class="text-2xl font-black font-mono text-indigo-300">1</span><span class="text-[10px] text-slate-400 block">100</span></div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40"><span class="text-[10px] text-cyan-300 block">TENS</span><span class="text-2xl font-black font-mono text-cyan-300">5</span><span class="text-[10px] text-slate-400 block">50</span></div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40"><span class="text-[10px] text-amber-300 block">ONES</span><span class="text-2xl font-black font-mono text-amber-300">0</span><span class="text-[10px] text-cyan-400 block font-bold">0 ones</span></div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 100 + 50 + 0 = <strong class="text-cyan-300 text-sm">150</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Ones Zero (15)</span>
            <div class="grid grid-cols-2 gap-2 w-3/4 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40"><span class="text-[10px] text-rose-300 block">TENS</span><span class="text-2xl font-black font-mono text-rose-300">1</span></div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40"><span class="text-[10px] text-amber-300 block">ONES</span><span class="text-2xl font-black font-mono text-amber-300">5</span></div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 15 (Lost 135 units!)</div>
        `;
    } else if (val === 200) {
        boxWith.innerHTML = `
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Double Century (200)</span>
            <div class="grid grid-cols-3 gap-2 w-full my-3 text-center">
                <div class="bg-indigo-950/50 p-2 rounded border border-indigo-700/40"><span class="text-[10px] text-indigo-300 block">HUNDREDS</span><span class="text-2xl font-black font-mono text-indigo-300">2</span><span class="text-[10px] text-slate-400 block">200</span></div>
                <div class="bg-cyan-950/50 p-2 rounded border border-cyan-700/40"><span class="text-[10px] text-cyan-300 block">TENS</span><span class="text-2xl font-black font-mono text-cyan-300">0</span><span class="text-[10px] text-cyan-400 block font-bold">0 tens</span></div>
                <div class="bg-amber-950/50 p-2 rounded border border-amber-700/40"><span class="text-[10px] text-amber-300 block">ONES</span><span class="text-2xl font-black font-mono text-amber-300">0</span><span class="text-[10px] text-cyan-400 block font-bold">0 ones</span></div>
            </div>
            <div class="text-xs text-center text-slate-300 font-mono">Value: 200 + 0 + 0 = <strong class="text-cyan-300 text-sm">200</strong></div>
        `;
        boxWithout.innerHTML = `
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wide">Without Two Zeros (Collapsed: 2)</span>
            <div class="grid grid-cols-1 gap-2 w-1/3 my-3 text-center">
                <div class="bg-rose-950/50 p-2 rounded border border-rose-700/40"><span class="text-[10px] text-rose-300 block">ONES</span><span class="text-2xl font-black font-mono text-rose-300">2</span></div>
            </div>
            <div class="text-xs text-center text-rose-300 font-mono">Value: 2 (Lost 198 items!)</div>
        `;
    }
}

// Simulator 4: Marketplace Counting
let currentStall = 'laddoos', stallBoxes = 4, stallSingles = 7;

function selectMarketStall(type) {
    currentStall = type;
    ['stallBtnLaddoos', 'stallBtnBangles', 'stallBtnBananas'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) {
            btn.classList.remove('bg-orange-600', 'text-white');
            btn.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = { laddoos: 'stallBtnLaddoos', bangles: 'stallBtnBangles', bananas: 'stallBtnBananas' };
    const active = document.getElementById(activeMap[type]);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-orange-600', 'text-white');
    }

    if (type === 'laddoos') { stallBoxes = 4; stallSingles = 7; }
    else if (type === 'bangles') { stallBoxes = 5; stallSingles = 3; }
    else if (type === 'bananas') { stallBoxes = 6; stallSingles = 8; }

    playTone(460, 'sine', 0.1);
    renderMarketStall();
}

function adjustMarketItem(kind, delta) {
    if (kind === 'box') stallBoxes = Math.max(0, Math.min(9, stallBoxes + delta));
    else stallSingles = Math.max(0, Math.min(9, stallSingles + delta));
    playTone(380 + (kind === 'box' ? 120 : 0), 'sine', 0.08);
    renderMarketStall();
}

function renderMarketStall() {
    const title = document.getElementById('stallItemTitle');
    const badge = document.getElementById('stallTotalBadge');
    const container = document.getElementById('stallVisualContainer');
    const tensEl = document.getElementById('stallTensCount');
    const onesEl = document.getElementById('stallOnesCount');

    if (!container || !badge) return;

    const names = {
        laddoos: { name: 'Laddoo Sweet Stall', icon: '🟡', boxIcon: '📦' },
        bangles: { name: 'Glass Bangle Stall', icon: '⭕', boxIcon: '🎁' },
        bananas: { name: 'Fresh Banana Stall', icon: '🍌', boxIcon: '🧺' }
    };

    const cfg = names[currentStall];
    if (title) title.textContent = `${cfg.name}: Packed Tens & Loose Items`;

    const total = (stallBoxes * 10) + stallSingles;
    badge.textContent = `Total: ${total}`;

    if (tensEl) tensEl.textContent = `${stallBoxes} packed (${stallBoxes * 10})`;
    if (onesEl) onesEl.textContent = `${stallSingles} loose singles (${stallSingles})`;

    let html = '';
    for (let b = 0; b < stallBoxes; b++) {
        html += `<div class="bg-orange-950/60 border border-orange-600/60 p-2 rounded-xl flex items-center gap-2 shadow">
            <span class="text-2xl">${cfg.boxIcon}</span>
            <div class="text-left">
                <span class="text-xs font-bold text-orange-300 block font-mono">Ten (10)</span>
                <span class="text-[10px] text-slate-400 block">${currentStall}</span>
            </div>
        </div>`;
    }

    if (stallSingles > 0) {
        html += `<div class="bg-amber-950/40 border border-amber-600/40 p-2 rounded-xl flex flex-wrap items-center gap-1.5 max-w-xs">`;
        for (let s = 0; s < stallSingles; s++) html += `<span class="text-xl">${cfg.icon}</span>`;
        html += `</div>`;
    }

    if (stallBoxes === 0 && stallSingles === 0) {
        html = `<div class="text-xs text-slate-500 italic p-2">Stall is empty. Add boxes or loose items to begin!</div>`;
    }

    container.innerHTML = html;
}

// Simulator 5: Snakes & Ladders 100-Grid
let gridPos = 24;

function initSnakesGrid() {
    const grid = document.getElementById('snakesMiniGrid');
    if (!grid) return;

    let html = '';
    for (let r = 9; r >= 0; r--) {
        const isEvenRow = (r % 2 === 1);
        for (let c = 0; c < 10; c++) {
            const num = isEvenRow ? (r * 10 + (10 - c)) : (r * 10 + (c + 1));
            html += `<div id="gridCell${num}" onclick="setGridPos(${num})" class="text-[10px] font-mono flex items-center justify-center rounded cursor-pointer transition ${getCellColor(num)}">
                ${num}
            </div>`;
        }
    }
    grid.innerHTML = html;
    updateGridDisplay();
}

function getCellColor(n) {
    if (n === 34 || n === 85) return 'bg-emerald-900/60 text-emerald-200 border border-emerald-500';
    if (n === 12 || n === 55) return 'bg-emerald-950/40 text-emerald-300';
    if (n === 21 || n === 52) return 'bg-rose-950/40 text-rose-300';
    if (n === 43 || n === 88) return 'bg-rose-900/60 text-rose-200 border border-rose-500';
    return 'bg-slate-800/80 text-slate-300 hover:bg-slate-700';
}

function setGridPos(n) {
    gridPos = Math.max(1, Math.min(100, n));
    playTone(400 + (n * 3), 'sine', 0.08);
    updateGridDisplay();
}

function stepGridPos(delta) {
    const next = gridPos + delta;
    if (next >= 1 && next <= 100) setGridPos(next);
}

function rollSnakesDice() {
    const roll = Math.floor(Math.random() * 6) + 1;
    playTone(600, 'triangle', 0.1);
    let next = Math.min(100, gridPos + roll);

    let statusText = `Rolled a ${roll}! Moved to ${next}.`;
    if (next === 12) { next = 34; statusText = `Rolled a ${roll}! Climbed ladder to 34!`; playSuccessChime(); }
    else if (next === 55) { next = 85; statusText = `Rolled a ${roll}! Big ladder! Climbed to 85!`; playSuccessChime(); }
    else if (next === 43) { next = 21; statusText = `Bitten by snake at 43! Slid down to 21.`; playErrorChime(); }
    else if (next === 88) { next = 52; statusText = `Snake slide! Landed at 88, fell to 52.`; playErrorChime(); }

    gridPos = next;
    updateGridDisplay();
    const st = document.getElementById('gridActionStatus');
    if (st) st.textContent = statusText;
}

function resetGridPos() {
    setGridPos(1);
    const st = document.getElementById('gridActionStatus');
    if (st) st.textContent = 'Reset to start position: 1';
}

function updateGridDisplay() {
    for (let i = 1; i <= 100; i++) {
        const c = document.getElementById(`gridCell${i}`);
        if (c) {
            c.classList.remove('ring-2', 'ring-amber-400', 'bg-amber-500', 'text-slate-950', 'font-black');
            if (i === gridPos) {
                c.classList.add('ring-2', 'ring-amber-400', 'bg-amber-500', 'text-slate-950', 'font-black');
            }
        }
    }

    const posEl = document.getElementById('gridPlayerPos');
    const bundleEl = document.getElementById('gridBundleNotation');
    if (posEl) posEl.textContent = gridPos;

    if (bundleEl) {
        const tens = Math.floor(gridPos / 10);
        const ones = gridPos % 10;
        bundleEl.textContent = `${tens} tens bundle${tens !== 1 ? 's' : ''} + ${ones} loose stick${ones !== 1 ? 's' : ''}`;
    }
}

// Simulator 6: The Talking Pot
function activateTalkingPot() {
    const input = document.getElementById('potInputNumber');
    if (!input) return;
    const n = parseInt(input.value, 10);
    if (isNaN(n)) return;

    const next = n + 1;
    playSuccessChime();

    const potSvg = document.getElementById('potSvg');
    const potBubble = document.getElementById('potBubble');
    const speechEl = document.getElementById('potSpeechOutput');

    if (potSvg) {
        potSvg.classList.add('scale-110');
        setTimeout(() => potSvg.classList.remove('scale-110'), 300);
    }

    if (potBubble) {
        potBubble.textContent = `${next}!`;
        potBubble.classList.remove('scale-0');
        potBubble.classList.add('scale-100');
    }

    if (speechEl) {
        speechEl.textContent = `"You gave me ${n}... so the next number is ${next} (${numberToWords(next)})!"`;
    }

    window.speakText(`The number after ${n} is ${next}!`);
}

function quickFeedPot(n) {
    const input = document.getElementById('potInputNumber');
    if (input) input.value = n;
    activateTalkingPot();
}

// Simulator 7: Defining 100
function setHundredView(view) {
    ['hViewTabCricket', 'hViewTabBundles', 'hViewTabSuccessor', 'hViewTabBindis'].forEach(id => {
        const tab = document.getElementById(id);
        if (tab) {
            tab.classList.remove('bg-yellow-600', 'text-white');
            tab.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = {
        cricket: 'hViewTabCricket',
        bundles: 'hViewTabBundles',
        successor: 'hViewTabSuccessor',
        bindis: 'hViewTabBindis'
    };
    const active = document.getElementById(activeMap[view]);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-yellow-600', 'text-white');
    }

    playTone(550, 'sine', 0.1);
    const panel = document.getElementById('hundredViewPanel');
    if (!panel) return;

    if (view === 'cricket') {
        panel.innerHTML = `
            <div class="text-center space-y-2">
                <span class="text-4xl">🏏 💯 🎆</span>
                <div class="text-lg font-black text-yellow-300 font-mono">BATSMAN SCORES A CENTURY!</div>
                <p class="text-xs text-slate-300 max-w-sm">
                    In cricket, when a batsman scores exactly 100 runs, it is celebrated as a "Century". The crowd erupts and teammates applaud!
                </p>
                <div class="inline-block bg-yellow-950/60 border border-yellow-500/40 px-3 py-1 rounded text-xs font-mono text-yellow-200">
                    Runs: 100 = 100 Runs Milestone
                </div>
            </div>
        `;
    } else if (view === 'bundles') {
        let bHtml = '<div class="flex flex-wrap gap-2 justify-center my-2 max-w-md">';
        for (let i = 0; i < 10; i++) {
            bHtml += `<div class="bg-indigo-900/70 border border-indigo-400 p-1.5 rounded flex flex-col items-center">
                <span class="text-[10px] text-indigo-300 font-bold">10</span>
                <span class="text-xs">🪵</span>
            </div>`;
        }
        bHtml += '</div>';

        panel.innerHTML = `
            <div class="text-center space-y-1">
                <div class="text-sm font-bold text-indigo-300">10 Bundles of 10 Matchsticks</div>
                ${bHtml}
                <div class="text-xs font-mono text-yellow-300 font-bold">10 × 10 = 100 Matchsticks</div>
            </div>
        `;
    } else if (view === 'successor') {
        panel.innerHTML = `
            <div class="text-center space-y-2">
                <div class="text-3xl font-black font-mono text-white">99 + 1 = 100</div>
                <div class="text-xs text-slate-300 max-w-sm">
                    99 is the biggest 2-digit number (9 tens and 9 ones). When you add just 1 single more, the ones place bursts, triggering a double regrouping into the first 3-digit number: 100!
                </div>
                <div class="text-xs font-mono text-emerald-400 font-bold">99 Ones + 1 One = 10 Tens = 1 Hundred</div>
            </div>
        `;
    } else if (view === 'bindis') {
        let cardsHtml = '<div class="grid grid-cols-5 gap-1.5 justify-center my-2 max-w-xs">';
        for (let i = 0; i < 10; i++) {
            cardsHtml += `<div class="bg-rose-950/50 border border-rose-500/50 p-1 rounded text-center">
                <span class="text-[9px] text-rose-300 font-bold block">Card ${i+1}</span>
                <span class="text-[11px]">🔴🔴🔴</span>
            </div>`;
        }
        cardsHtml += '</div>';

        panel.innerHTML = `
            <div class="text-center space-y-1">
                <div class="text-sm font-bold text-rose-300">10 Packets of 10 Decorative Bindis</div>
                ${cardsHtml}
                <div class="text-xs font-mono text-yellow-300 font-bold">10 Packets × 10 Bindis = 100 Bindis</div>
            </div>
        `;
    }
}

// Simulator 8: Ginladi 100-Bead String
let ginladiVal = 60;

function updateGinladi(val) {
    ginladiVal = parseInt(val, 10);
    const splitEl = document.getElementById('beadSplitValue');
    const sliderDisp = document.getElementById('sliderValDisplay');
    const eq = document.getElementById('hundredPairEquation');
    const exp = document.getElementById('hundredPairExplanation');
    const slider = document.getElementById('ginladiSlider');

    if (splitEl) splitEl.textContent = ginladiVal;
    if (sliderDisp) sliderDisp.textContent = ginladiVal;
    if (slider && slider.value !== String(ginladiVal)) slider.value = ginladiVal;

    const complement = 100 - ginladiVal;
    if (eq) eq.textContent = `${ginladiVal} + ${complement} = 100`;
    if (exp) exp.textContent = `Part A: ${ginladiVal} beads + Part B: ${complement} beads = 100 beads in total`;

    renderGinladiBeads();
}

function setGinladiVal(val) {
    playTone(490, 'sine', 0.08);
    updateGinladi(val);
}

function renderGinladiBeads() {
    const track = document.getElementById('ginladiBeadTrack');
    if (!track) return;

    let html = '';
    for (let i = 1; i <= 100; i++) {
        const groupTen = Math.floor((i - 1) / 10);
        const isRedGroup = (groupTen % 2 === 0);
        const isPartA = (i <= ginladiVal);
        const opacityClass = isPartA ? 'opacity-100 ring-1 ring-teal-400' : 'opacity-40';
        const colorClass = isRedGroup ? 'bg-rose-500' : 'bg-slate-200';

        html += `<div title="Bead ${i}" class="w-2.5 h-2.5 sm:w-3 sm:h-3 rounded-full ${colorClass} ${opacityClass} transition"></div>`;
    }
    track.innerHTML = html;
}

// Simulator 9: Flower Petals
const petalSets = [
    [25, 75, 40, 60, 15, 85, 30, 70],
    [10, 90, 35, 65, 45, 55, 20, 80],
    [5, 95, 50, 50, 18, 82, 32, 68]
];
let currentPetalSetIdx = 0;
let selectedPetalIdx = null;

function renderFlowerPetals() {
    const container = document.getElementById('flowerPetalsContainer');
    if (!container) return;

    const petals = petalSets[currentPetalSetIdx];
    let html = '';
    const radius = 95; const cx = 140; const cy = 140;

    petals.forEach((val, idx) => {
        const angle = (idx * (360 / petals.length)) * (Math.PI / 180);
        const x = cx + radius * Math.cos(angle) - 24;
        const y = cy + radius * Math.sin(angle) - 24;

        html += `<button onclick="selectPetal(${idx})" id="petalBtn${idx}" style="left: ${x}px; top: ${y}px;" class="absolute w-12 h-12 rounded-full bg-pink-700/80 hover:bg-pink-600 border-2 border-pink-400 flex items-center justify-center font-mono font-bold text-white text-sm shadow transition transform hover:scale-110 active:scale-95">
            ${val}
        </button>`;
    });

    container.innerHTML = html;
}

function selectPetal(idx) {
    const petals = petalSets[currentPetalSetIdx];
    const status = document.getElementById('petalPairStatus');

    if (selectedPetalIdx === null) {
        selectedPetalIdx = idx;
        const btn = document.getElementById(`petalBtn${idx}`);
        if (btn) btn.classList.add('ring-4', 'ring-amber-300', 'bg-pink-500');
        playTone(420, 'sine', 0.1);
        if (status) status.innerHTML = `Selected <strong class="text-pink-300">${petals[idx]}</strong>. Now click the matching petal that adds to 100!`;
    } else {
        if (selectedPetalIdx === idx) {
            const btn = document.getElementById(`petalBtn${idx}`);
            if (btn) btn.classList.remove('ring-4', 'ring-amber-300', 'bg-pink-500');
            selectedPetalIdx = null;
            if (status) status.textContent = 'Petal deselected. Click any first petal to start!';
            return;
        }

        const v1 = petals[selectedPetalIdx];
        const v2 = petals[idx];
        const sum = v1 + v2;

        if (sum === 100) {
            playSuccessChime();
            const btn1 = document.getElementById(`petalBtn${selectedPetalIdx}`);
            const btn2 = document.getElementById(`petalBtn${idx}`);
            if (btn1) btn1.classList.add('bg-emerald-600', 'border-emerald-300');
            if (btn2) btn2.classList.add('bg-emerald-600', 'border-emerald-300');
            if (status) status.innerHTML = `🎉 <strong>Match Made!</strong> ${v1} + ${v2} = 100! Excellent calculation!`;
            selectedPetalIdx = null;
        } else {
            playErrorChime();
            if (status) status.innerHTML = `⚠️ <strong>Not 100:</strong> ${v1} + ${v2} = ${sum}. Try another partner!`;
            const btn = document.getElementById(`petalBtn${selectedPetalIdx}`);
            if (btn) btn.classList.remove('ring-4', 'ring-amber-300', 'bg-pink-500');
            selectedPetalIdx = null;
        }
    }
}

function resetFlowerPuzzle() {
    currentPetalSetIdx = (currentPetalSetIdx + 1) % petalSets.length;
    selectedPetalIdx = null;
    const status = document.getElementById('petalPairStatus');
    if (status) status.textContent = 'Click any first petal to start pairing!';
    renderFlowerPetals();
}

// Simulator 10: Stepping Past 100
let seqNum = 108;

function stepSeq(delta) {
    const next = seqNum + delta;
    if (next >= 100 && next <= 130) setSeqNum(next);
}

function setSeqNum(n) {
    seqNum = n;
    playTone(380 + ((n - 100) * 10), 'sine', 0.08);
    updateSeqView();
}

function updateSeqView() {
    const numEl = document.getElementById('seqNumberDisplay');
    const wordEl = document.getElementById('seqWordDisplay');
    const tensVal = document.getElementById('seqTensVal');
    const tensTxt = document.getElementById('seqTensTxt');
    const onesVal = document.getElementById('seqOnesVal');
    const onesTxt = document.getElementById('seqOnesTxt');
    const eq = document.getElementById('seqEquation');

    if (!numEl) return;

    numEl.textContent = seqNum;
    if (wordEl) wordEl.textContent = `"${numberToWords(seqNum)}"`;

    const remainder = seqNum - 100;
    const tens = Math.floor(remainder / 10);
    const ones = remainder % 10;

    if (tensVal) tensVal.textContent = tens;
    if (tensTxt) tensTxt.textContent = `${tens} tens (${tens * 10})`;
    if (onesVal) onesVal.textContent = ones;
    if (onesTxt) onesTxt.textContent = `${ones} loose singles (${ones})`;

    if (eq) eq.textContent = `100 + ${tens * 10} + ${ones} = ${seqNum}`;
}

// Simulator 11: Matchsticks 150
let matchH = 1, matchT = 3, matchO = 6;

function adjustMatchUnit(col, delta) {
    if (col === 'h') matchH = Math.max(0, Math.min(2, matchH + delta));
    else if (col === 't') matchT = Math.max(0, Math.min(9, matchT + delta));
    else if (col === 'o') matchO = Math.max(0, Math.min(9, matchO + delta));
    playTone(300 + (col === 'h' ? 250 : col === 't' ? 120 : 0), 'sine', 0.08);
    renderMatchsticks();
}

function setMatchPreset(h, t, o) {
    matchH = h; matchT = t; matchO = o;
    playSuccessChime();
    renderMatchsticks();
}

function renderMatchsticks() {
    const badge = document.getElementById('matchstickTotalBadge');
    const tensDisp = document.getElementById('matchTensDisplay');
    const onesDisp = document.getElementById('matchOnesDisplay');
    const hCount = document.getElementById('matchCountH');
    const tCount = document.getElementById('matchCountT');
    const oCount = document.getElementById('matchCountO');
    const eq = document.getElementById('matchSummaryEquation');

    if (!badge) return;

    const total = (matchH * 100) + (matchT * 10) + matchO;
    badge.textContent = `${total} Matchsticks`;

    if (hCount) hCount.textContent = `${matchH} bundle${matchH !== 1 ? 's' : ''} = ${matchH * 100}`;
    if (tCount) tCount.textContent = `${matchT} bundle${matchT !== 1 ? 's' : ''} = ${matchT * 10}`;
    if (oCount) oCount.textContent = `${matchO} single${matchO !== 1 ? 's' : ''} = ${matchO}`;

    if (tensDisp) {
        let tHtml = '';
        for (let i = 0; i < matchT; i++) {
            tHtml += `<div class="w-6 h-10 bg-emerald-900 border border-emerald-400 rounded flex items-center justify-center text-[10px] text-emerald-200 font-bold" title="Bundle of 10">10</div>`;
        }
        if (matchT === 0) tHtml = '<span class="text-[11px] text-slate-500 italic">0 bundles</span>';
        tensDisp.innerHTML = tHtml;
    }

    if (onesDisp) {
        let oHtml = '';
        for (let i = 0; i < matchO; i++) {
            oHtml += `<div class="w-1.5 h-8 bg-amber-400 rounded-full" title="Single stick"></div>`;
        }
        if (matchO === 0) oHtml = '<span class="text-[11px] text-slate-500 italic">0 loose</span>';
        onesDisp.innerHTML = oHtml;
    }

    if (eq) eq.textContent = `Total: ${matchH * 100} + ${matchT * 10} + ${matchO} = ${total} Matchsticks`;
}

// Simulator 12: Range 100 to 150
function updateRange150(val) {
    const num = parseInt(val, 10);
    const numEl = document.getElementById('range150Number');
    const wordEl = document.getElementById('range150Word');
    const dist100 = document.getElementById('rangeDist100');
    const dist150 = document.getElementById('rangeDist150');
    const nearestTen = document.getElementById('rangeNearestTen');

    if (!numEl) return;

    numEl.textContent = num;
    if (wordEl) wordEl.textContent = `"${numberToWords(num)}"`;
    if (dist100) dist100.textContent = `+${num - 100}`;
    if (dist150) dist150.textContent = `${150 - num} to go`;
    if (nearestTen) nearestTen.textContent = `${Math.round(num / 10) * 10}`;
}

function setRange150Val(val) {
    const slider = document.getElementById('sliderRange150');
    if (slider) slider.value = val;
    playTone(400 + (val - 100) * 3, 'sine', 0.08);
    updateRange150(val);
}

// Simulator 13: Clap Snap Pat
let rhythmSequence = [];

function triggerRhythm(action) {
    if (action === 'clap') {
        playTone(180, 'triangle', 0.25, 0.4);
        rhythmSequence.push({ type: 'clap', val: 100, icon: '👏', label: '100' });
    } else if (action === 'snap') {
        playTone(850, 'square', 0.08, 0.25);
        rhythmSequence.push({ type: 'snap', val: 10, icon: '🫰', label: '10' });
    } else if (action === 'pat') {
        playTone(320, 'sine', 0.15, 0.3);
        rhythmSequence.push({ type: 'pat', val: 1, icon: '🦵', label: '1' });
    }
    renderRhythmLog();
}

function clearRhythm() {
    rhythmSequence = [];
    renderRhythmLog();
}

function playRhythmTarget(target) {
    clearRhythm();
    const h = Math.floor(target / 100);
    const rem = target % 100;
    const t = Math.floor(rem / 10);
    const o = rem % 10;

    for (let i = 0; i < h; i++) rhythmSequence.push({ type: 'clap', val: 100, icon: '👏', label: '100' });
    for (let i = 0; i < t; i++) rhythmSequence.push({ type: 'snap', val: 10, icon: '🫰', label: '10' });
    for (let i = 0; i < o; i++) rhythmSequence.push({ type: 'pat', val: 1, icon: '🦵', label: '1' });

    playSuccessChime();
    renderRhythmLog();
}

function renderRhythmLog() {
    const log = document.getElementById('rhythmSoundLog');
    const totalEl = document.getElementById('rhythmTotalNumber');
    const breakEl = document.getElementById('rhythmBreakdownTxt');

    if (!log || !totalEl) return;

    let sum = 0, claps = 0, snaps = 0, pats = 0;
    let html = '';

    rhythmSequence.forEach(item => {
        sum += item.val;
        if (item.type === 'clap') claps++;
        else if (item.type === 'snap') snaps++;
        else if (item.type === 'pat') pats++;

        html += `<span class="px-2 py-1 bg-slate-800 rounded border border-slate-700 font-mono text-sm shadow">
            ${item.icon} <strong class="text-xs text-slate-300">${item.label}</strong>
        </span>`;
    });

    if (rhythmSequence.length === 0) {
        html = '<span class="text-xs text-slate-500 italic">Tap Clap (100), Snap (10), or Pat (1) to start rhythm!</span>';
    }

    log.innerHTML = html;
    totalEl.textContent = sum;

    if (breakEl) {
        breakEl.textContent = `${claps} Clap${claps !== 1 ? 's' : ''} (${claps * 100}) + ${snaps} Snap${snaps !== 1 ? 's' : ''} (${snaps * 10}) + ${pats} Pat${pats !== 1 ? 's' : ''} (${pats}) = ${sum}`;
    }
}

// Simulator 14: Place Value Breakdowns (150-159)
function setChart150(n) {
    playTone(450 + ((n - 150) * 15), 'sine', 0.08);

    const targetEl = document.getElementById('chartTargetNum');
    const onesDigit = document.getElementById('chartOnesDigit');
    const onesVal = document.getElementById('chartOnesValue');
    const eq = document.getElementById('chartExpandedForm');
    const word = document.getElementById('chartWordName');

    if (!targetEl) return;

    targetEl.textContent = n;
    const ones = n % 10;

    if (onesDigit) onesDigit.textContent = ones;
    if (onesVal) onesVal.textContent = `= ${ones}`;

    if (eq) eq.textContent = `100 + 50 + ${ones} = ${n}`;
    if (word) word.textContent = `"${numberToWords(n)}"`;
}

// Simulator 15: Number Line Jumps
let jumperPos = 140;

function leapStep(delta) {
    let next = Math.min(200, jumperPos + delta);
    jumperPos = next;
    playTone(350 + (delta * 12), 'triangle', 0.12);
    if (jumperPos === 200) playSuccessChime();
    updateJumperView();
}

function resetJumper() {
    jumperPos = 100;
    playTone(350, 'sine', 0.08);
    updateJumperView();
}

function updateJumperView() {
    const posEl = document.getElementById('jumpCurrentPos');
    const token = document.getElementById('jumperToken');
    const log = document.getElementById('jumpActionLog');

    if (!posEl || !token) return;

    posEl.textContent = jumperPos;

    const pct = (jumperPos - 100) / 100;
    const cx = 30 + (pct * 540);
    token.setAttribute('cx', cx);

    if (log) {
        const past = jumperPos - 100;
        const left = 200 - jumperPos;
        log.textContent = `Current Spot: ${jumperPos} is ${past} steps past 100, and ${left} steps away from 200!`;
    }
}

// Simulator 16: Double Century Summit
function triggerDoubleCenturyCheer() {
    playSuccessChime();
    const banner = document.getElementById('doubleCenturyCelebration');
    if (banner) {
        banner.classList.remove('bg-amber-500/10');
        banner.classList.add('bg-amber-500/30', 'ring-2', 'ring-amber-400');
        setTimeout(() => {
            banner.classList.remove('bg-amber-500/30', 'ring-2', 'ring-amber-400');
            banner.classList.add('bg-amber-500/10');
        }, 1200);
    }
    window.speakText("Sensational achievement! You have reached two hundred, the grand Double Century! Two hundred ones, twenty tens, and two whole hundreds!");
}

// Simulator Initializer on Slide Entry
function initSlideSimulator(slideId) {
    if (slideId === 1) renderTally();
    else if (slideId === 2) updateBaseTenView();
    else if (slideId === 3) setZeroDemo(105);
    else if (slideId === 4) renderMarketStall();
    else if (slideId === 5) initSnakesGrid();
    else if (slideId === 7) setHundredView('cricket');
    else if (slideId === 8) renderGinladiBeads();
    else if (slideId === 9) renderFlowerPetals();
    else if (slideId === 10) updateSeqView();
    else if (slideId === 11) renderMatchsticks();
    else if (slideId === 12) updateRange150(125);
    else if (slideId === 13) renderRhythmLog();
    else if (slideId === 14) setChart150(154);
    else if (slideId === 15) updateJumperView();
}

// DOM Ready
document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
'''

# Generate final HTML
print("Generating full animation lab HTML with Pure Indian Male Teacher Sound...")
slides_markup = generate_slides_html()
slides_json = json.dumps(SLIDES, ensure_ascii=False)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__SLIDES_JSON__", slides_json)
final_html = final_html.replace("__JS_CODE__", complete_js)

output_dir = "public/animations"
os.makedirs(output_dir, exist_ok=True)
master_filename = "class3-maths-double-century.html"
master_path = os.path.join(output_dir, master_filename)

with open(master_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation lab written to {master_path} ({len(final_html):,} bytes)")

# Create the 7 canonical symlinks
symlinks = [
    "chapter3-maths-class3.html",
    "class3-maths-chapter3.html",
    "class3-double-century.html",
    "double-century-class3.html",
    "class3-maths-double-century-lab.html",
    "class3-math-double-century.html",
    "class3-double-century-lab.html"
]

print("Creating symlinks...")
for link_name in symlinks:
    link_path = os.path.join(output_dir, link_name)
    if os.path.lexists(link_path):
        os.remove(link_path)
    os.symlink(master_filename, link_path)
    print(f"  Created symlink: {link_name} -> {master_filename}")

print("=== Class 3 Mathematics Chapter 3 Lab Build Complete! ===")

