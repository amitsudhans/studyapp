# -*- coding: utf-8 -*-
"""
Build Class 3 Mathematics Chapter 4: Vacation with My Nani Maa Interactive Animation Lab
Compiles public/animations/class3-maths-vacation-with-my-nani-maa.html
and creates the 7 required canonical symlinks.
Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class3_maths_ch4_data import SLIDES
from class3_maths_ch4_sims import simulators

# Strict Validation Lists
FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani']
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VERIFYING CHAPTER 4 MATHS SLIDES DATA ===")
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
    <title>Class 3 Mathematics - Chapter 4: Vacation with My Nani Maa</title>
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
                <span class="text-2xl sm:text-3xl">🏡</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">NCERT Class 3</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Joyful Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 4</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">Vacation Mathematics Interactive Animated Laboratory</h1>
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
// NCERT Class 3 Mathematics - Chapter 4: Vacation with My Nani Maa
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

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') nextSlide();
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
});

// =========================================================================
// 16 BESPOKE INTERACTIVE SIMULATORS FOR CHAPTER 4
// =========================================================================

// Simulator 1: Hidden Marble Trick
let marbleTotal = 15;
let marbleVisible = 9;
let isClothPeeking = false;

function setMarblePreset(tot, vis) {
    marbleTotal = tot;
    marbleVisible = vis;
    isClothPeeking = false;
    playTone(450, 'sine', 0.08);
    renderMarbles();
}

function toggleCloth() {
    isClothPeeking = !isClothPeeking;
    playTone(520, 'triangle', 0.1);
    renderMarbles();
}

function renderMarbles() {
    const visCont = document.getElementById('visibleMarblesContainer');
    const hidCont = document.getElementById('hiddenMarblesContainer');
    const clothCover = document.getElementById('clothCover');
    const clothBtn = document.getElementById('clothToggleBtn');
    const totDisp = document.getElementById('marbleTotalDisp');
    const badge = document.getElementById('marbleVisibleCountBadge');
    const visTxt = document.getElementById('visibleMarblesCountTxt');
    const hidTxt = document.getElementById('hiddenMarblesCountTxt');
    const eqSum = document.getElementById('marbleEquationSummary');

    if (!visCont || !clothCover) return;

    const hiddenCount = marbleTotal - marbleVisible;
    if (totDisp) totDisp.textContent = marbleTotal;
    if (badge) badge.textContent = `Visible: ${marbleVisible} | Hidden: ${hiddenCount}`;
    if (visTxt) visTxt.textContent = `${marbleVisible} Visible`;
    if (hidTxt) hidTxt.textContent = `${hiddenCount} Hidden (${marbleTotal} - ${marbleVisible} = ${hiddenCount})`;

    if (eqSum) {
        eqSum.innerHTML = `Total ${marbleTotal} - Visible ${marbleVisible} = <strong>${hiddenCount} Hidden Marbles</strong> (Verified by ${marbleVisible} + ${hiddenCount} = ${marbleTotal})`;
    }

    let visHtml = '';
    for (let i = 0; i < marbleVisible; i++) {
        visHtml += `<div class="w-6 h-6 rounded-full bg-gradient-to-tr from-cyan-600 to-sky-300 shadow border border-cyan-200 flex items-center justify-center text-[9px] font-black text-slate-900">●</div>`;
    }
    visCont.innerHTML = visHtml;

    if (clothBtn) clothBtn.textContent = isClothPeeking ? 'Peeking: ON' : 'Peeking: Off';

    if (isClothPeeking) {
        clothCover.classList.add('opacity-40');
        hidCont.classList.remove('hidden');
        let hidHtml = '';
        for (let i = 0; i < hiddenCount; i++) {
            hidHtml += `<div class="w-6 h-6 rounded-full bg-gradient-to-tr from-amber-600 to-yellow-300 shadow border border-amber-200 flex items-center justify-center text-[9px] font-black text-slate-900">●</div>`;
        }
        hidCont.innerHTML = hidHtml;
    } else {
        clothCover.classList.remove('opacity-40');
        hidCont.classList.add('hidden');
        hidCont.innerHTML = '';
    }
}

// Simulator 2: Balushahi Sweet Counts
let currentSweets = 12;

function addSweet() {
    if (currentSweets < 20) {
        currentSweets++;
        playTone(550, 'sine', 0.08);
        renderSweets(`Added 1 sweet! Total is now ${currentSweets}.`);
    }
}

function eatSweet() {
    if (currentSweets > 0) {
        currentSweets--;
        playTone(350, 'sine', 0.08);
        renderSweets(`1 sweet eaten! Remaining: ${currentSweets}.`);
    }
}

function eatMultipleSweets(n) {
    currentSweets = Math.max(0, currentSweets - n);
    playTone(320, 'sawtooth', 0.12);
    renderSweets(`Afternoon teatime: ${n} sweets eaten! Remaining: ${currentSweets}.`);
}

function resetSweets() {
    currentSweets = 12;
    playSuccessChime();
    renderSweets('Reset to fresh platter: 7 + 5 = 12 Sweets.');
}

function renderSweets(msg = '') {
    const platter = document.getElementById('balushahiPlatter');
    const badge = document.getElementById('balushahiCountBadge');
    const eq = document.getElementById('balushahiEquation');
    const status = document.getElementById('balushahiStatusTxt');

    if (!platter) return;
    if (badge) badge.textContent = `${currentSweets} Sweets on Platter`;
    if (eq) eq.textContent = `Current Count: ${currentSweets} Balushahis`;
    if (status && msg) status.textContent = msg;

    let html = '';
    for (let i = 0; i < currentSweets; i++) {
        html += `<div class="w-8 h-8 rounded-full bg-gradient-to-br from-amber-500 to-orange-600 border-2 border-amber-300 shadow flex items-center justify-center text-xs">🍩</div>`;
    }
    if (currentSweets === 0) {
        html = '<span class="text-xs text-slate-400 italic">All sweets have been eaten! Click Add or Reset to refill.</span>';
    }
    platter.innerHTML = html;
}

// Simulator 3: Story Books Total (Ten-Frame)
let booksStory = 9;
let booksPuzzle = 7;
let isMadeTen = false;

function executeMakeTen() {
    isMadeTen = true;
    playSuccessChime();
    renderTenFrames();
}

function resetTenFrames() {
    isMadeTen = false;
    booksStory = 9;
    booksPuzzle = 7;
    playTone(400, 'sine', 0.08);
    renderTenFrames();
}

function setBookCustom(s, p) {
    booksStory = s;
    booksPuzzle = p;
    isMadeTen = false;
    playTone(480, 'sine', 0.08);
    renderTenFrames();
}

function renderTenFrames() {
    const f1 = document.getElementById('tenFrame1');
    const f2 = document.getElementById('tenFrame2');
    const b1 = document.getElementById('frame1CountBadge');
    const b2 = document.getElementById('frame2CountBadge');
    const eq = document.getElementById('bookTenFrameEquation');
    const txt = document.getElementById('bookTenFrameStepTxt');
    const btn = document.getElementById('btnMakeTen');

    if (!f1 || !f2) return;

    let count1 = booksStory;
    let count2 = booksPuzzle;

    if (isMadeTen) {
        const needed = 10 - booksStory;
        if (needed > 0 && booksPuzzle >= needed) {
            count1 = 10;
            count2 = booksPuzzle - needed;
        }
        if (eq) eq.textContent = `10 + ${count2} = ${10 + count2} Books!`;
        if (txt) txt.textContent = `Success! Borrowed 1 from 7 to make a full 10: 10 + 6 = 16.`;
        if (btn) btn.disabled = true;
    } else {
        if (eq) eq.textContent = `${booksStory} + ${booksPuzzle} = ${booksStory + booksPuzzle} Books`;
        if (txt) txt.textContent = `Initial state: ${booksStory} books need ${10 - booksStory} more to complete a decade.`;
        if (btn) btn.disabled = false;
    }

    if (b1) b1.textContent = `${count1} Books`;
    if (b2) b2.textContent = `${count2} Books`;

    let html1 = '';
    for (let i = 1; i <= 10; i++) {
        if (i <= count1) {
            html1 += `<div class="aspect-square rounded bg-indigo-600 border border-indigo-400 flex items-center justify-center text-xs">📖</div>`;
        } else {
            html1 += `<div class="aspect-square rounded bg-slate-900 border border-slate-800"></div>`;
        }
    }
    f1.innerHTML = html1;

    let html2 = '';
    for (let i = 1; i <= 10; i++) {
        if (i <= count2) {
            html2 += `<div class="aspect-square rounded bg-emerald-600 border border-emerald-400 flex items-center justify-center text-xs">🧩</div>`;
        } else {
            html2 += `<div class="aspect-square rounded bg-slate-900 border border-slate-800"></div>`;
        }
    }
    f2.innerHTML = html2;
}

// Simulator 4: Card Equation Triplets
let cardA = 7, cardB = 8, cardTotal = 15;

function setTripletPreset(a, b, tot) {
    cardA = a; cardB = b; cardTotal = tot;
    playTone(460, 'sine', 0.1);
    updateTripletUI();
}

function updateTripletUI() {
    const elA = document.getElementById('tripletCardA');
    const elB = document.getElementById('tripletCardB');
    const elTot = document.getElementById('tripletCardTotal');
    const b1 = document.getElementById('eqBox1');
    const b2 = document.getElementById('eqBox2');
    const b3 = document.getElementById('eqBox3');
    const b4 = document.getElementById('eqBox4');

    if (!elA) return;
    elA.textContent = cardA;
    elB.textContent = cardB;
    elTot.textContent = cardTotal;

    if (b1) b1.textContent = `${cardA} + ${cardB} = ${cardTotal}`;
    if (b2) b2.textContent = `${cardB} + ${cardA} = ${cardTotal}`;
    if (b3) b3.textContent = `${cardTotal} - ${cardA} = ${cardB}`;
    if (b4) b4.textContent = `${cardTotal} - ${cardB} = ${cardA}`;
}

// Simulator 5: Bead String Strategies
let beadStrategy = 'bridge';

function setBeadStrategy(mode) {
    beadStrategy = mode;
    ['tabStratBridge', 'tabStratComp', 'tabStratOnes'].forEach(id => {
        const tab = document.getElementById(id);
        if (tab) {
            tab.classList.remove('bg-teal-600', 'text-white');
            tab.classList.add('bg-slate-800', 'text-slate-300');
        }
    });

    const activeMap = { bridge: 'tabStratBridge', comp: 'tabStratComp', ones: 'tabStratOnes' };
    const active = document.getElementById(activeMap[mode]);
    if (active) {
        active.classList.remove('bg-slate-800', 'text-slate-300');
        active.classList.add('bg-teal-600', 'text-white');
    }

    playTone(500, 'sine', 0.1);
    renderBeadStrategy();
}

function renderBeadStrategy() {
    const track = document.getElementById('ginladiStrategyTrack');
    const exp = document.getElementById('beadStrategyExplanation');
    if (!track) return;

    let html = '';
    for (let i = 1; i <= 30; i++) {
        const isRedGroup = Math.floor((i - 1) / 10) % 2 === 0;
        let colorCls = isRedGroup ? 'bg-rose-500' : 'bg-slate-200';
        let ringCls = '';

        if (i <= 15) {
            ringCls = 'ring-1 ring-teal-400 opacity-90';
        } else if (i <= 22) {
            ringCls = 'ring-2 ring-amber-400 scale-110 font-bold';
        } else {
            colorCls = 'opacity-30 ' + colorCls;
        }

        html += `<div class="w-3 h-3 rounded-full ${colorCls} ${ringCls} transition"></div>`;
    }
    track.innerHTML = html;

    if (exp) {
        if (beadStrategy === 'bridge') {
            exp.innerHTML = `<div class="text-base font-bold font-mono text-teal-300">15 + 5 = 20, then 20 + 2 = 22</div>
            <div class="text-xs text-slate-300 mt-1">Split 7 into 5 and 2: reach benchmark decade 20 first, then add 2!</div>`;
        } else if (beadStrategy === 'comp') {
            exp.innerHTML = `<div class="text-base font-bold font-mono text-teal-300">15 + 10 = 25, then 25 - 3 = 22</div>
            <div class="text-xs text-slate-300 mt-1">Leap a full ten (+10) to 25, then compensate by stepping back 3!</div>`;
        } else {
            exp.innerHTML = `<div class="text-base font-bold font-mono text-teal-300">15 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 22</div>
            <div class="text-xs text-slate-300 mt-1">Count forward seven individual beads one by one from 15 to 22.</div>`;
        }
    }
}

// Simulator 6: Stamp Album Decade Bundles
let stampBase = 22, stampAdd = 30;

function setStampAddition(base, add) {
    stampBase = base; stampAdd = add;
    playTone(480, 'sine', 0.1);
    renderStampBundles();
}

function renderStampBundles() {
    const disp = document.getElementById('stampBundlesDisplay');
    const txt = document.getElementById('stampBundlesTotalTxt');
    const eq = document.getElementById('stampAddingEquation');

    if (!disp) return;

    const total = stampBase + stampAdd;
    const baseTens = Math.floor(stampBase / 10);
    const addTens = Math.floor(stampAdd / 10);
    const totalTens = Math.floor(total / 10);
    const ones = total % 10;

    let html = '';
    for (let i = 0; i < totalTens; i++) {
        html += `<div class="w-8 h-12 bg-cyan-900 border border-cyan-400 rounded flex flex-col items-center justify-center text-[10px] text-cyan-200 font-bold shadow">
            <span>10</span>
            <span class="text-[8px] text-cyan-400">STAMPS</span>
        </div>`;
    }
    disp.innerHTML = html;

    if (txt) txt.textContent = `${totalTens} Tens Bundles (${totalTens * 10}) + ${ones} Loose = ${total} Stamps`;
    if (eq) eq.textContent = `${stampBase} + ${stampAdd} = ${total} Stamps`;
}

// Simulator 7: Backward Line Jumps
function setBackJumpDemo(start, sub) {
    playTone(420, 'sine', 0.1);
    const resTxt = document.getElementById('backJumpResultTxt');
    if (resTxt) {
        resTxt.innerHTML = `${start} - ${sub} = <strong>${start - sub} Monument Stamps</strong>!`;
    }
}

// Simulator 8: Target Jump Projections
function setTargetDemo(curr, goal) {
    playTone(440, 'sine', 0.1);
    const gap = goal - curr;
    const gapEl = document.getElementById('targetGapDisplay');
    if (gapEl) gapEl.textContent = gap;
}

// Simulator 9: Leaping Garden Creatures
let creaturePos = 34;

function creatureHop(delta) {
    creaturePos = Math.max(0, Math.min(100, creaturePos + delta));
    playTone(delta > 0 ? 550 : 350, 'triangle', 0.1);
    renderCreatureTrail();
}

function setCreatureStart(start) {
    creaturePos = start;
    playTone(400, 'sine', 0.08);
    renderCreatureTrail();
}

function renderCreatureTrail() {
    const posBadge = document.getElementById('creaturePosBadge');
    const onesFix = document.getElementById('creatureOnesFix');
    const trail = document.getElementById('creatureJumpTrail');
    const status = document.getElementById('creatureActionStatus');

    if (!posBadge) return;
    posBadge.textContent = creaturePos;
    if (onesFix) onesFix.textContent = creaturePos % 10;

    if (trail) {
        trail.innerHTML = `
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-400">${Math.max(0, creaturePos - 20)}</span>
            <span>➜</span>
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-300">${Math.max(0, creaturePos - 10)}</span>
            <span>➜</span>
            <span class="px-3 py-1 rounded bg-green-600 text-white font-bold text-base shadow">${creaturePos}</span>
            <span>➜</span>
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-300">${Math.min(100, creaturePos + 10)}</span>
        `;
    }
    if (status) {
        status.textContent = `Current spot is ${creaturePos}. Tens place = ${Math.floor(creaturePos / 10)}, Ones place = ${creaturePos % 10}.`;
    }
}

// Simulator 10: Hidden Leaf Puzzles
let totalAnts = 50, visAnts = 35, isLeafLifted = false;

function setAntPreset(tot, vis) {
    totalAnts = tot; visAnts = vis; isLeafLifted = false;
    playTone(460, 'sine', 0.08);
    renderAnts();
}

function toggleLeaf() {
    isLeafLifted = !isLeafLifted;
    playTone(490, 'sine', 0.08);
    renderAnts();
}

function renderAnts() {
    const visBadge = document.getElementById('antVisibleBadge');
    const leafBtn = document.getElementById('leafToggleBtn');
    const leafGraphic = document.getElementById('leafCoverGraphic');
    const revBox = document.getElementById('hiddenAntsRevealed');
    const countTxt = document.getElementById('leafCountTxt');

    if (!visBadge) return;
    const hidden = totalAnts - visAnts;

    visBadge.textContent = `${visAnts} Ants`;
    if (countTxt) countTxt.textContent = `Hidden: ${hidden} Ants (${totalAnts} - ${visAnts} = ${hidden})`;
    if (leafBtn) leafBtn.textContent = isLeafLifted ? 'Lower Leaf' : 'Lift Leaf';

    if (isLeafLifted) {
        if (leafGraphic) leafGraphic.classList.add('opacity-40');
        if (revBox) {
            revBox.classList.remove('hidden');
            revBox.textContent = `🐜 ${hidden} Ants Revealed Resting Here!`;
        }
    } else {
        if (leafGraphic) leafGraphic.classList.remove('opacity-40');
        if (revBox) revBox.classList.add('hidden');
    }
}

// Simulator 11: Hundred Grid Navigation
let navPos = 45;

function initNavGrid() {
    const grid = document.getElementById('navMiniGrid');
    if (!grid) return;
    let html = '';
    for (let i = 1; i <= 100; i++) {
        html += `<div id="navCell${i}" class="text-[9px] font-mono flex items-center justify-center rounded ${i === navPos ? 'bg-sky-500 text-slate-950 font-black' : 'bg-slate-800 text-slate-400'}">${i}</div>`;
    }
    grid.innerHTML = html;
}

function navGridStep(dir) {
    let next = navPos;
    if (dir === 'up' && navPos > 10) next -= 10;
    else if (dir === 'down' && navPos <= 90) next += 10;
    else if (dir === 'left' && (navPos - 1) % 10 !== 0) next -= 1;
    else if (dir === 'right' && navPos % 10 !== 0) next += 1;

    navPos = next;
    playTone(300 + navPos * 4, 'sine', 0.08);
    updateNavGrid();
}

function navGridReset() {
    navPos = 45;
    playTone(400, 'sine', 0.08);
    updateNavGrid();
}

function updateNavGrid() {
    const posBadge = document.getElementById('navGridPos');
    if (posBadge) posBadge.textContent = navPos;

    for (let i = 1; i <= 100; i++) {
        const c = document.getElementById(`navCell${i}`);
        if (c) {
            if (i === navPos) {
                c.className = 'text-[9px] font-mono flex items-center justify-center rounded bg-sky-500 text-slate-950 font-black ring-2 ring-sky-300';
            } else {
                c.className = 'text-[9px] font-mono flex items-center justify-center rounded bg-slate-800 text-slate-400';
            }
        }
    }
}

// Simulator 12: Grid Race Game
let racePos = 42, die1 = 3, die2 = 5;

function rollRaceDice() {
    die1 = Math.floor(Math.random() * 6) + 1;
    die2 = Math.floor(Math.random() * 6) + 1;
    playTone(600, 'triangle', 0.1);
    updateRaceUI();
}

function applyRaceMove(action, useHigh) {
    const dSmall = Math.min(die1, die2);
    const dBig = Math.max(die1, die2);
    const val = useHigh ? (dBig * 10 + dSmall) : (dSmall * 10 + dBig);

    let next = racePos;
    if (action === 'add') {
        if (racePos + val <= 100) next += val;
        else alert("Move exceeds 100! Choose subtraction or alternate digits.");
    } else {
        next = Math.max(1, racePos - val);
    }

    racePos = next;
    playSuccessChime();
    updateRaceUI();
}

function resetRaceGame() {
    racePos = 1;
    playTone(350, 'sine', 0.08);
    updateRaceUI();
}

function updateRaceUI() {
    const posEl = document.getElementById('racePlayerPos');
    const badge = document.getElementById('raceStatusBadge');
    const dA = document.getElementById('diceA');
    const dB = document.getElementById('diceB');
    const choices = document.getElementById('raceMoveChoicesTxt');
    const bAddLow = document.getElementById('btnRaceAddLow');
    const bAddHigh = document.getElementById('btnRaceAddHigh');
    const bSubLow = document.getElementById('btnRaceSubLow');

    if (!posEl) return;
    posEl.textContent = racePos;

    if (dA) dA.textContent = die1;
    if (dB) dB.textContent = die2;

    const dSmall = Math.min(die1, die2);
    const dBig = Math.max(die1, die2);
    const lowNum = dSmall * 10 + dBig;
    const highNum = dBig * 10 + dSmall;

    if (choices) choices.textContent = `${lowNum} or ${highNum}`;
    if (bAddLow) bAddLow.textContent = `Add ${lowNum} (+${lowNum})`;
    if (bAddHigh) bAddHigh.textContent = `Add ${highNum} (+${highNum})`;
    if (bSubLow) bSubLow.textContent = `Sub ${lowNum} (-${lowNum})`;

    if (badge) {
        if (racePos >= 91) {
            badge.textContent = "🏆 WINNER! IN 91-100 ZONE!";
            badge.className = "text-amber-300 font-bold font-mono animate-pulse";
        } else {
            badge.textContent = "Racing Forward!";
            badge.className = "text-emerald-400 font-bold font-mono";
        }
    }
}

// Simulator 13: Magic Square Matrix
function checkMagicLine(type) {
    playTone(520, 'sine', 0.1);
    const eq = document.getElementById('magicSumEquation');
    if (!eq) return;

    if (type === 'r1') eq.textContent = "Row 1: 8 + 1 + 6 = 15";
    else if (type === 'r2') eq.textContent = "Row 2: 3 + 5 + 7 = 15";
    else if (type === 'r3') eq.textContent = "Row 3: 4 + 9 + 2 = 15";
    else if (type === 'c1') eq.textContent = "Column 1: 8 + 3 + 4 = 15";
    else if (type === 'diag') eq.textContent = "Main Diagonal: 8 + 5 + 2 = 15 (Centered at 5)";
}

// Simulator 15: Vegetable Crate Complements
function setCrateTomatoes(n) {
    playTone(450, 'sine', 0.08);
    const tVal = document.getElementById('crateTomatoesVal');
    const cVal = document.getElementById('crateCarrotsVal');
    const tBar = document.getElementById('crateTomatoesBar');
    const cBar = document.getElementById('crateCarrotsBar');
    const eq = document.getElementById('crateComplementEquation');

    if (!tVal) return;
    const carrots = 100 - n;

    tVal.textContent = n;
    cVal.textContent = carrots;
    if (tBar) {
        tBar.style.width = `${n}%`;
        tBar.textContent = `${n} Tomatoes`;
    }
    if (cBar) {
        cBar.style.width = `${carrots}%`;
        cBar.textContent = `${carrots} Carrots`;
    }
    if (eq) {
        eq.innerHTML = `Complement: 100 - ${n} = <strong>${carrots} Carrots</strong> (${n} + ${carrots} = 100)`;
    }
}

// Simulator 16: Apple Harvest Comparison
function setAppleMode(mode) {
    playTone(500, 'sine', 0.1);
    const disp = document.getElementById('appleComparisonDisplay');
    if (!disp) return;

    if (mode === 'total') {
        disp.innerHTML = `<div class="text-emerald-400 font-bold text-base">Combined Total: 85 + 67 = 152 Apples</div>
        <div class="text-slate-300 text-xs">80 + 60 = 140, and 5 + 7 = 12. 140 + 12 = 152.</div>`;
    } else {
        disp.innerHTML = `<div class="text-amber-300 font-bold text-base">Difference Margin: 85 - 67 = 18 Apples!</div>
        <div class="text-slate-300 text-xs">Basket A exceeds Basket B by exactly 18 sweet apples.</div>`;
    }
}

// Simulator Initializer on Slide Entry
function initSlideSimulator(slideId) {
    if (slideId === 1) renderMarbles();
    else if (slideId === 2) renderSweets();
    else if (slideId === 3) renderTenFrames();
    else if (slideId === 4) updateTripletUI();
    else if (slideId === 5) renderBeadStrategy();
    else if (slideId === 6) renderStampBundles();
    else if (slideId === 9) renderCreatureTrail();
    else if (slideId === 10) renderAnts();
    else if (slideId === 11) initNavGrid();
    else if (slideId === 12) updateRaceUI();
}

document.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
'''

# Generate full HTML
print("Generating full animation lab HTML with Pure Indian Male Teacher Sound...")
slides_markup = generate_slides_html()
slides_json = json.dumps(SLIDES, ensure_ascii=False)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__SLIDES_JSON__", slides_json)
final_html = final_html.replace("__JS_CODE__", complete_js)

output_dir = "public/animations"
os.makedirs(output_dir, exist_ok=True)
master_filename = "class3-maths-vacation-with-my-nani-maa.html"
master_path = os.path.join(output_dir, master_filename)

with open(master_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation lab written to {master_path} ({len(final_html):,} bytes)")

# Create the 7 canonical symlinks
symlinks = [
    "chapter4-maths-class3.html",
    "class3-maths-chapter4.html",
    "class3-vacation-with-my-nani-maa.html",
    "vacation-with-my-nani-maa-class3.html",
    "class3-maths-vacation-with-my-nani-maa-lab.html",
    "class3-math-vacation-with-my-nani-maa.html",
    "class3-vacation-with-my-nani-maa-lab.html"
]

print("Creating symlinks...")
for link_name in symlinks:
    link_path = os.path.join(output_dir, link_name)
    if os.path.lexists(link_path):
        os.remove(link_path)
    os.symlink(master_filename, link_path)
    print(f"  Created symlink: {link_name} -> {master_filename}")

print("=== Class 3 Mathematics Chapter 4 Lab Build Complete! ===")

