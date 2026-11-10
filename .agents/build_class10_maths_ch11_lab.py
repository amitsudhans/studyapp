#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Class 10 Mathematics Chapter 11: Areas Related to Circles Interactive Animation Lab
Replaces public/animations/areas-related-to-circles.html cleanly with full 20-slide lab

Equipped with Pure Indian Male Teacher Sound Engine (Speaking All Text).
"""

import os
import json
import sys
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class10_maths_ch11_data import slides as slides_data
from class10_maths_ch11_sims import simulators

FORBIDDEN_CHARACTERS = [
    'Sonia', 'Niharika', 'Preet', 'Champa', 'Chameli', 'Rashmi', 'Subba Rao', 'Subba', 'Ramkali', 'John', 'Jivanti', 'Ravi', 'Akhila', 'Appooppan', 'Ammu', 'Khushi', 'Moyna', 'Dadu', 'Harpreet', 'Shirin', 'Raghav', 'Shambhu', 'Gopu', 'Simmi', 'Raj',
    'Rishi', 'Chiya', 'Nonikaa', 'Unni', 'Mama', 'Mami',
    'Nita', 'Radha', 'Sneha', 'Rohit', 'Mohan', 'Chacha', 'Dadiji', 'Dadaji',
    'Bela', 'Banku', 'Bishu', 'Munni', 'Kusum', 'Ronnie',
    'Kishan', 'Peter', 'Ritu', 'Monu', 'Chintu', 'Leena',
    'Adi', 'Shelly', 'Akbar', 'Birbal', 'Shabnam', 'Mukta', 'Gopal', 'Dhara',
    'Atya', 'Jagannath', 'Mithu', 'Dhruv', 'Roro', 'Toto', 'Ajji', 'Teji',
    'Jojo', 'Farooq', 'Arvind', 'Amma', 'Chirag', 'Nandini', 'Deba',
    'Meera', 'Pihu', 'Soni', 'Avi'
]
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VERIFYING CLASS 10 MATHS CH 11 SLIDES DATA ===")
assert len(slides_data) == 20, f"Expected 20 slides, found {len(slides_data)}"

formatted_slides = []

for idx, slide in enumerate(slides_data):
    sid = slide['id']
    title = slide['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    slide_str = json.dumps(slide)
    for name in FORBIDDEN_CHARACTERS:
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_str), f"Slide {sid} contains persona '{persona}'"

    formatted_slide = {
        'id': sid,
        'title': title,
        'subtitle': slide.get('subtitle', ''),
        'speech': slide.get('speech', ''),
    }

    if sid <= 16:
        wc = len(slide['speech'].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words (must be 195-215)"
        assert len(slide['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"

        formatted_cps = []
        for cidx, cp in enumerate(slide['checkpoints']):
            assert len(cp['options']) == 4, f"Slide {sid} checkpoint must have 4 options"
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
        assert len(slide['questions']) == 10, f"Slide {sid} must have 10 challenge questions"
        formatted_qs = []
        for qidx, q in enumerate(slide['questions']):
            qid = f"c{sid}_q{qidx+1}"
            assert 'hint' in q, f"Slide {sid} question {qid} missing hint"
            assert len(q['options']) == 4, f"Slide {sid} question {qid} must have 4 options"
            ans_str = q['options'][q['answer']]
            assert len(q['solution_steps']) == 3, f"Slide {sid} question {qid} must have 3 solution steps"
            formatted_qs.append({
                'id': qid,
                'q': q['question'],
                'options': q['options'],
                'ans': ans_str,
                'hint': q['hint'],
                'explanation': q['explanation'],
                'solution_steps': q['solution_steps']
            })
        formatted_slide['questions'] = formatted_qs

    formatted_slides.append(formatted_slide)

print("All 20 slides for Class 10 Maths Chapter 11 passed strict validation!")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 10 Mathematics - Chapter 11: Areas Related to Circles</title>
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
        .sim-container {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 18px;
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-slate-950">

    <!-- Top Fixed Header -->
    <header class="bg-slate-900/90 backdrop-blur sticky top-0 z-30 border-b border-slate-800 px-4 py-3 sm:px-6">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <!-- Brand / Context -->
            <div class="flex items-center gap-3 w-full sm:w-auto">
                <span class="text-2xl sm:text-3xl">🍕</span>
                <div>
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">NCERT Class 10</span>
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Mathematics</span>
                        <span class="text-xs text-slate-400 font-medium">Chapter 11</span>
                    </div>
                    <h1 class="text-base sm:text-lg font-bold text-white tracking-tight">Areas Related to Circles Interactive Animated Laboratory</h1>
                </div>
            </div>

            <!-- Header Controls -->
            <div class="flex items-center flex-wrap gap-2 w-full sm:w-auto justify-between sm:justify-end">
                <div class="flex items-center gap-1.5 bg-slate-800/90 border border-slate-700 rounded-xl px-2.5 py-1 text-xs">
                    <span class="text-slate-400 text-[11px] font-medium hidden md:inline">Voice:</span>
                    <select id="voiceSelect" onchange="onVoiceChange()" class="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-lg px-2 py-1 focus:ring-1 focus:ring-cyan-500 outline-none max-w-[150px] sm:max-w-[210px] truncate" title="Select Pure Indian Male Voice">
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
                    <span class="text-xs font-bold text-cyan-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700">Slide <span id="slideCounter">1 / 20</span></span>
                </div>
            </div>
        </div>

        <!-- Chapter Progress Bar -->
        <div class="w-full bg-slate-800 h-1 mt-3">
            <div id="progressBar" class="bg-gradient-to-r from-cyan-500 via-amber-500 to-emerald-500 h-1 w-[5%] transition-all duration-300"></div>
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
            <div id="lastSlideNotice" class="hidden px-4 py-2 rounded-xl bg-cyan-500/20 border border-cyan-500/40 text-cyan-300 font-bold text-xs sm:text-sm text-center">
                You have reached the last slide of this chapter.
            </div>

            <button id="nextBtn" onclick="nextSlide()" class="px-5 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs sm:text-sm flex items-center gap-2 transition shadow-md">
                Next <span>→</span>
            </button>
        </div>
    </footer>

    <!-- 3-Step Mathematical/Scientific Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <h3 class="text-sm sm:text-base font-bold text-white tracking-tight">Scientific Solution Walkthrough</h3>
                <button onclick="closeSolutionModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center text-sm font-bold">✕</button>
            </div>
            <div id="solutionModalBody" class="py-4 space-y-4 max-h-[70vh] overflow-y-auto custom-scrollbar">
                <!-- Dynamically Populated -->
            </div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-1.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs transition">Got It!</button>
            </div>
        </div>
    </div>

    <!-- Data & Client Logic -->
    <script>
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
                                <span class="w-5 h-5 rounded-md bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-[10px]">Q{cidx + 1}</span>
                                <span class="text-xs font-semibold text-white">{cp['q']}</span>
                            </div>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-cyan-400 hover:text-cyan-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
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
                            <span class="w-6 h-6 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                            <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                        </div>
                        <p class="text-xs text-slate-400">{subtitle}</p>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-cyan-300 border border-slate-700 font-semibold self-start sm:self-auto">Slide {sid} of 20</span>
                </div>

                <!-- Classroom Teacher Spoken Lecture Card (Displaying All Teaching Text) -->
                <div class="teacher-lecture-card bg-slate-900/90 border border-cyan-500/30 rounded-2xl p-4 sm:p-5 shadow-lg relative overflow-hidden">
                    <div class="flex items-center justify-between gap-3 mb-2 pb-2 border-b border-slate-800">
                        <div class="flex items-center gap-2">
                            <span class="text-xl">👨‍🏫</span>
                            <div>
                                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Classroom Teacher Spoken Lecture</span>
                                <span class="text-[10px] text-slate-400 block sm:inline sm:ml-2">Pure Indian Male Teacher Sound</span>
                            </div>
                        </div>
                        <button onclick="speakLecture()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white flex items-center gap-1.5 text-xs font-bold transition shadow shrink-0" title="Listen with Pure Indian Male Teacher Voice">
                            <span>🔊</span> Listen to Lecture
                        </button>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-normal">
                        {s['speech']}
                    </p>
                </div>

                <!-- Bespoke Simulator -->
                <div class="simulator-wrapper">
                    {sim_markup}
                </div>

                <!-- 2 Checkpoints (Exercises with Individual Audio) -->
                <div class="space-y-3 pt-2">
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                        <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Concept Checkpoints (Exercises)</h4>
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
                            <span class="w-6 h-6 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs shrink-0">{qidx + 1}</span>
                            <p class="text-xs sm:text-sm font-semibold text-white flex-1">{q['q']}</p>
                            <button onclick="window.speakText('{safe_q_speak}')" title="Listen with Pure Indian Male Teacher Voice" class="text-cyan-400 hover:text-cyan-300 transition text-xs p-1 rounded-lg hover:bg-slate-800 shrink-0">🔊</button>
                        </div>
                        <div class="space-y-1.5 mt-3">
                            {opts_joined}
                        </div>
                    </div>
                    <div class="q-feedback-box hidden"></div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-800/80 text-[11px]">
                        <span class="text-slate-500 italic">💡 Hint: {q['hint']}</span>
                        <button onclick="showSolutionModal('{q['id']}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 font-semibold transition">
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
                        <span class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-center font-bold text-xs">{sid}</span>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">{title}</h2>
                    </div>
                    <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-medium">10 Questions Multi-Choice Quiz</span>
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
// Global Slide State & Curriculum Data
window.slideCurriculumData = __SLIDES_JSON__;
const slidesData = window.slideCurriculumData;
let currentSlide = 1;
const totalSlides = 20;

window.challengeQuestionsMap = {};
slidesData.forEach(s => {
    if (s.questions) {
        s.questions.forEach(q => {
            window.challengeQuestionsMap[q.id] = q;
        });
    }
});

let isAudioPlaying = false;
let currentUtterance = null;
let synth = window.speechSynthesis;
let selectedVoice = null;
let allVoices = [];
let speechKeepAliveTimer = null;

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
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.08);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.16);
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.32);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.32);
    } catch(e) { console.warn("Audio chime unsupported:", e); }
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
    } catch(e) { console.warn("Audio chime unsupported:", e); }
}

const femaleBlockList = [
    'female', 'woman', 'girl', 'lady', 'zira', 'kavya', 'kalpana', 'veena',
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

    const fullLecture = `${currentSlideData.title}. ${currentSlideData.subtitle}. ${currentSlideData.speech}`;
    currentUtterance = new SpeechSynthesisUtterance(fullLecture);

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

function showSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    const wasPlaying = isAudioPlaying;
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

    const progBar = document.getElementById('progressBar');
    if (progBar) progBar.style.width = `${(currentSlide / totalSlides) * 100}%`;

    const audioControls = document.getElementById('audioControls');
    if (audioControls) {
        audioControls.style.display = (currentSlide <= 16) ? 'block' : 'none';
    }

    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        prevBtn.style.visibility = (currentSlide === 1) ? 'hidden' : 'visible';
    }

    const nextBtn = document.getElementById('nextBtn');
    const noticeEl = document.getElementById('lastSlideNotice');

    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (noticeEl) noticeEl.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (noticeEl) noticeEl.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (wasPlaying && currentSlide <= 16) {
        speakLecture();
    }
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

function checkCheckpoint(sid, cidx, btnEl, selectedOpt, correctAns, explanation) {
    const parentContainer = btnEl.closest('.checkpoint-container');
    if (!parentContainer) return;

    const allButtons = parentContainer.querySelectorAll('.checkpoint-opt');
    const feedbackBox = parentContainer.querySelector('.checkpoint-feedback');

    allButtons.forEach(b => {
        b.disabled = true;
        const optVal = b.getAttribute('data-option');
        if (optVal === correctAns) {
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
            feedbackBox.className = 'checkpoint-feedback p-3 rounded-xl bg-emerald-950/70 border border-emerald-800 text-xs text-emerald-300';
            feedbackBox.innerHTML = `<strong>Correct!</strong> ${explanation}`;
        } else {
            playErrorChime();
            feedbackBox.className = 'checkpoint-feedback p-3 rounded-xl bg-rose-950/70 border border-rose-800 text-xs text-rose-300';
            feedbackBox.innerHTML = `<strong>Incorrect.</strong> ${explanation}`;
        }
    }
}

function handleChallengeOption(qid, btnEl, selectedOpt, correctAns, explanation) {
    const card = document.getElementById(`qcard-${qid}`);
    if (!card) return;

    const allButtons = card.querySelectorAll('.q-opt-btn');
    const feedbackBox = card.querySelector('.q-feedback-box');

    allButtons.forEach(b => {
        b.disabled = true;
        const optVal = b.getAttribute('data-option');
        if (optVal === correctAns) {
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

function showSolutionModal(qid) {
    const qData = window.challengeQuestionsMap[qid];
    if (!qData) return;

    const modal = document.getElementById('solutionModal');
    const body = document.getElementById('solutionModalBody');
    if (!modal || !body) return;

    let stepsHtml = '';
    if (qData.solution_steps && qData.solution_steps.length >= 3) {
        stepsHtml = `
            <div class="space-y-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Step 1: Material &amp; Optical Observation</span>
                    <p class="text-xs text-slate-300">${qData.solution_steps[0]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Step 2: Physical &amp; State Analysis</span>
                    <p class="text-xs text-slate-300">${qData.solution_steps[1]}</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Step 3: Verification &amp; NCERT Conclusion</span>
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
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-2">3-Step Scientific Breakdown</span>
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

window.addEventListener('DOMContentLoaded', () => {
    initSpeechEngine();
    showSlide(1);
});
'''

# Compile Master File
slides_markup = generate_slides_html()
slides_json_str = json.dumps(formatted_slides, ensure_ascii=False)

js_compiled = complete_js.replace("__SLIDES_JSON__", slides_json_str)

final_html = HTML_TEMPLATE.replace("__SLIDES_HTML__", slides_markup)
final_html = final_html.replace("__JS_CODE__", js_compiled)
final_html = final_html.replace("__SLIDES_JSON__", slides_json_str)

assert "__SLIDES_JSON__" not in final_html, "Unreplaced __SLIDES_JSON__ token in final_html!"
assert "__SLIDES_HTML__" not in final_html, "Unreplaced __SLIDES_HTML__ token in final_html!"
assert "__JS_CODE__" not in final_html, "Unreplaced __JS_CODE__ token in final_html!"

out_file = os.path.join(os.path.dirname(__file__), "..", "public", "animations", "areas-related-to-circles.html")
out_file = os.path.abspath(out_file)

with open(out_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Master animation lab written to: {out_file} ({len(final_html):,} bytes)")

symlinks = []

animations_dir = os.path.dirname(out_file)
master_basename = os.path.basename(out_file)

for link_name in symlinks:
    link_path = os.path.join(animations_dir, link_name)
    if os.path.exists(link_path) or os.path.islink(link_path):
        os.remove(link_path)
    os.symlink(master_basename, link_path)
    print(f"Created symlink: {link_name} -> {master_basename}")

print("=== CLASS 10 MATHS CHAPTER 11 LAB GENERATION COMPLETE ===")
