# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 5
UNIT: LINEAR EQUATIONS IN TWO VARIABLES (Competencies CG-3, C-3.2, C-8.1, CG-9)
Generates public/animations/class9-linear-equations.html
"""

import json
import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from class9_linear_equations_data import SLIDES_DATA, QUIZ_SLIDES

OUTPUT_PATH = "public/animations/class9-linear-equations.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA)
    quizzes_json = json.dumps(QUIZ_SLIDES)

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Mathematics • Linear Equations in Two Variables Lab</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX CSS & JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body);"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }
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
        .mouth-talking {
            animation: mouthTalk 0.25s infinite alternate ease-in-out;
            transform-origin: 50% 65%;
        }
        @keyframes mouthTalk {
            0% { transform: scaleY(0.2); }
            100% { transform: scaleY(1.4); }
        }
        .slide-fade-in {
            animation: fadeIn 0.3s ease-out forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-indigo-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
                    <i data-lucide="git-commit" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">Class 9 Maths • Chapter 5</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 font-semibold">Concept 1</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Linear Equations in Two Variables Lab</h1>
                </div>
            </div>

            <!-- Central Slide Indicator -->
            <div class="flex items-center gap-2 bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800">
                <span class="text-xs text-slate-400">Slide</span>
                <span id="slideCounter" class="text-sm font-bold text-indigo-400 font-mono">1 / 20</span>
                <div class="w-20 sm:w-28 bg-slate-800 h-2 rounded-full overflow-hidden ml-1">
                    <div id="progressBar" class="bg-gradient-to-r from-indigo-500 to-violet-500 h-full w-[5%] transition-all duration-300"></div>
                </div>
            </div>

            <!-- Voice Controls & Speed -->
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-800/80 rounded-lg p-0.5 border border-slate-700">
                    <button onclick="changeSpeed(0.8)" id="spd08" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">0.8x</button>
                    <button onclick="changeSpeed(1.0)" id="spd10" class="px-2 py-1 text-[11px] rounded font-bold bg-indigo-600 text-white transition">1.0x</button>
                    <button onclick="changeSpeed(1.2)" id="spd12" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">1.2x</button>
                </div>
                <button onclick="toggleAudio()" id="voiceToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white transition shadow-md shadow-indigo-600/30">
                    <i data-lucide="volume-2" class="w-4 h-4"></i>
                    <span id="voiceBtnText">Voice On</span>
                </button>
                <button onclick="replayAudio()" title="Replay Audio" class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">
                    <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Canvas -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 flex flex-col gap-6">

        <!-- Teacher Avatar & Live Dialogue Box -->
        <div class="bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 p-4 rounded-2xl border border-indigo-500/30 shadow-xl flex flex-col sm:flex-row items-center gap-4">
            <div class="relative shrink-0">
                <div class="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-gradient-to-tr from-indigo-700 via-indigo-600 to-violet-500 p-0.5 shadow-lg shadow-indigo-500/20">
                    <svg viewBox="0 0 100 100" class="w-full h-full rounded-2xl overflow-hidden bg-slate-900">
                        <circle cx="50" cy="50" r="45" fill="#1e1b4b"/>
                        <path d="M 20 95 C 20 75, 80 75, 80 95 Z" fill="#4338ca"/>
                        <path d="M 38 78 L 50 90 L 62 78 Z" fill="#e0e7ff"/>
                        <path d="M 48 84 L 52 84 L 50 92 Z" fill="#fbbf24"/>
                        <rect x="44" y="60" width="12" height="15" fill="#fcd34d" rx="4"/>
                        <ellipse cx="50" cy="46" rx="24" ry="26" fill="#fde68a"/>
                        <path d="M 24 45 C 24 20, 76 20, 76 45 C 76 30, 70 24, 50 24 C 30 24, 24 30, 24 45 Z" fill="#312e81"/>
                        <path d="M 24 45 C 20 60, 22 70, 26 75 C 24 65, 27 50, 30 45 Z" fill="#312e81"/>
                        <path d="M 76 45 C 80 60, 78 70, 74 75 C 76 65, 73 50, 70 45 Z" fill="#312e81"/>
                        <circle cx="41" cy="44" r="5" fill="#1e293b"/>
                        <circle cx="59" cy="44" r="5" fill="#1e293b"/>
                        <circle cx="42" cy="43" r="1.5" fill="#ffffff"/>
                        <circle cx="60" cy="43" r="1.5" fill="#ffffff"/>
                        <rect x="33" y="38" width="16" height="12" rx="3" fill="none" stroke="#6366f1" stroke-width="2"/>
                        <rect x="51" y="38" width="16" height="12" rx="3" fill="none" stroke="#6366f1" stroke-width="2"/>
                        <line x1="49" y1="44" x2="51" y2="44" stroke="#6366f1" stroke-width="2"/>
                        <path d="M 50 48 L 48 53 L 52 53" fill="none" stroke="#d97706" stroke-width="1.5" stroke-linecap="round"/>
                        <ellipse id="teacherMouth" cx="50" cy="62" rx="6" ry="2" fill="#be123c"/>
                    </svg>
                </div>
                <div class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded bg-emerald-500/90 text-[10px] font-black text-slate-950 uppercase tracking-wider">
                    Prof. Sophia
                </div>
            </div>

            <div class="flex-1 w-full text-center sm:text-left">
                <div class="flex items-center justify-center sm:justify-between gap-2 mb-1">
                    <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                        <span id="speechIndicator" class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        Teacher's Voiceover Explanation
                    </span>
                    <span class="text-[11px] text-slate-400 hidden sm:inline">Web Speech & Web Audio Synthesizer</span>
                </div>
                <p id="teacherSpeechText" class="text-sm text-slate-200 leading-relaxed font-normal italic">
                    Welcome to Linear Equations in Two Variables! Let us master graphing, solutions, and algebraic systems.
                </p>
            </div>
        </div>

        <!-- Slide Presentation Container -->
        <div id="slideContentContainer" class="bg-slate-900/60 rounded-2xl border border-slate-800 p-5 sm:p-6 shadow-2xl relative min-h-[460px] flex flex-col justify-between">
            <!-- Dynamic Slide HTML inserted by JS -->
        </div>

        <!-- Bottom Navigation Bar -->
        <div class="flex flex-wrap items-center justify-between gap-4 pt-2">
            <button onclick="prevSlide()" id="prevBtn" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-slate-800 hover:bg-slate-700 text-slate-200 transition border border-slate-700 disabled:opacity-40 disabled:cursor-not-allowed">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                Previous Slide
            </button>

            <!-- Slide Selection Dots / Quick Jump -->
            <div id="slideThumbnails" class="hidden md:flex items-center gap-1.5 overflow-x-auto max-w-[60%] py-1 px-2 bg-slate-900/80 rounded-xl border border-slate-800">
                <!-- 20 mini buttons generated by JS -->
            </div>

            <button onclick="nextSlide()" id="nextBtn" class="flex items-center gap-2 px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white transition shadow-lg shadow-indigo-600/30">
                Next Slide
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </div>

    </main>

    <!-- Step-by-Step Pop-up Solution Modal -->
    <div id="solutionModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-slate-900 border border-indigo-500/40 rounded-2xl max-w-xl w-full p-6 shadow-2xl relative animate-in fade-in zoom-in-95 duration-200">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm">
                        ✓
                    </div>
                    <h3 id="solutionModalTitle" class="text-base font-bold text-white">Solution & Derivation</h3>
                </div>
                <button onclick="closeSolutionModal()" id="solutionModalClose" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <div id="solutionModalBody" class="py-4 text-sm text-slate-300 space-y-3 leading-relaxed">
                <!-- Dynamic solution inserted here -->
            </div>
            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-xl transition">
                    Got It, Continue!
                </button>
            </div>
        </div>
    </div>

    <!-- Data Injection -->
    <script>
        const CONTENT_SLIDES = __SLIDES_JSON__;
        const QUIZ_SLIDES = __QUIZZES_JSON__;
        const ALL_SLIDES = [...CONTENT_SLIDES, ...QUIZ_SLIDES];
    </script>

    <!-- Laboratory Script & Audio Engine -->
    <script>
        let currentSlideIndex = 0;
        let isVoiceEnabled = true;
        let speechRate = 1.0;
        let currentUtterance = null;
        let audioCtx = null;

        function initAudioContext() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) audioCtx = new AudioContext();
            }
            if (audioCtx && audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        function playTone(freq, type, duration) {
            try {
                initAudioContext();
                if (!audioCtx) return;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type || 'sine';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch(e) {
                console.warn("Audio chime error:", e);
            }
        }

        function playSuccessSound() {
            playTone(523.25, 'triangle', 0.15);
            setTimeout(() => playTone(659.25, 'triangle', 0.2), 100);
            setTimeout(() => playTone(783.99, 'triangle', 0.3), 200);
        }

        function playErrorSound() {
            playTone(330, 'sawtooth', 0.15);
            setTimeout(() => playTone(280, 'sawtooth', 0.25), 120);
        }

        function speakCurrentSlide() {
            if (!isVoiceEnabled || !('speechSynthesis' in window)) return;

            window.speechSynthesis.cancel();
            const slide = ALL_SLIDES[currentSlideIndex];
            const textToSpeak = slide.audio_text || (slide.title + ". Practice challenge questions. Select your answer and view the step-by-step solution.");

            const utterance = new SpeechSynthesisUtterance(textToSpeak);
            utterance.rate = speechRate;
            utterance.lang = 'en-US';

            const mouth = document.getElementById('teacherMouth');
            const ind = document.getElementById('speechIndicator');

            utterance.onstart = () => {
                if (mouth) mouth.classList.add('mouth-talking');
                if (ind) ind.classList.add('animate-pulse', 'bg-emerald-400');
            };

            utterance.onend = utterance.onerror = () => {
                if (mouth) mouth.classList.remove('mouth-talking');
                if (ind) ind.classList.remove('animate-pulse');
            };

            currentUtterance = utterance;
            window.speechSynthesis.speak(utterance);
        }

        function toggleAudio() {
            isVoiceEnabled = !isVoiceEnabled;
            const btn = document.getElementById('voiceToggleBtn');
            const text = document.getElementById('voiceBtnText');
            if (isVoiceEnabled) {
                btn.classList.remove('bg-slate-700');
                btn.classList.add('bg-indigo-600');
                text.textContent = 'Voice On';
                speakCurrentSlide();
            } else {
                window.speechSynthesis.cancel();
                btn.classList.remove('bg-indigo-600');
                btn.classList.add('bg-slate-700');
                text.textContent = 'Voice Muted';
                const mouth = document.getElementById('teacherMouth');
                if (mouth) mouth.classList.remove('mouth-talking');
            }
        }

        function replayAudio() {
            if (isVoiceEnabled) speakCurrentSlide();
        }

        function changeSpeed(rate) {
            speechRate = rate;
            ['spd08', 'spd10', 'spd12'].forEach(id => {
                const el = document.getElementById(id);
                el.classList.remove('bg-indigo-600', 'text-white', 'font-bold');
                el.classList.add('text-slate-300');
            });
            const activeId = rate === 0.8 ? 'spd08' : (rate === 1.0 ? 'spd10' : 'spd12');
            const el = document.getElementById(activeId);
            el.classList.add('bg-indigo-600', 'text-white', 'font-bold');
            el.classList.remove('text-slate-300');
            if (isVoiceEnabled) speakCurrentSlide();
        }

        function renderCurrentSlide() {
            const slide = ALL_SLIDES[currentSlideIndex];
            const container = document.getElementById('slideContentContainer');
            const counter = document.getElementById('slideCounter');
            const progress = document.getElementById('progressBar');
            const badge = document.getElementById('currentBadge');
            const speechText = document.getElementById('teacherSpeechText');
            const nextBtn = document.getElementById('nextBtn');
            const prevBtn = document.getElementById('prevBtn');

            const total = ALL_SLIDES.length;
            const currNum = currentSlideIndex + 1;
            counter.textContent = `${currNum} / ${total}`;
            progress.style.width = `${(currNum / total) * 100}%`;
            badge.textContent = slide.badge || `Slide ${currNum}`;
            speechText.textContent = slide.audio_text || slide.title;

            prevBtn.disabled = (currentSlideIndex === 0);

            if (currentSlideIndex === total - 1) {
                nextBtn.style.display = 'none';
            } else {
                nextBtn.style.display = 'flex';
            }

            if (currentSlideIndex < 16) {
                container.innerHTML = `
                    <div class="slide-fade-in space-y-5">
                        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                            <h2 class="text-lg sm:text-xl font-bold text-white flex items-center gap-2">
                                <span class="text-indigo-400 font-mono">#${currNum}</span>
                                ${slide.title}
                            </h2>
                            <span class="text-xs text-indigo-400 font-medium">${slide.badge}</span>
                        </div>
                        ${slide.content_html}

                        <div class="mt-6 pt-4 border-t border-slate-800">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-amber-400 mb-3 flex items-center gap-1.5">
                                <i data-lucide="help-circle" class="w-4 h-4"></i>
                                Slide Checkpoints (${slide.checkpoints.length} Questions)
                            </h4>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                ${slide.checkpoints.map((cp, cIdx) => `
                                    <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 flex flex-col justify-between">
                                        <div class="text-xs font-semibold text-slate-200 mb-2">Q${cIdx + 1}: ${cp.q}</div>
                                        <div class="space-y-1.5 mb-2">
                                            ${cp.options.map((opt, oIdx) => `
                                                <button onclick="checkCheckpoint(${cIdx}, ${oIdx}, ${cp.ans})" id="cp_${cIdx}_${oIdx}" class="w-full text-left text-xs px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-850 text-slate-300 transition flex items-center justify-between">
                                                    <span>${opt}</span>
                                                    <span id="cp_ind_${cIdx}_${oIdx}" class="hidden font-bold text-xs"></span>
                                                </button>
                                            `).join('')}
                                        </div>
                                        <div id="cp_exp_${cIdx}" class="hidden text-[11px] p-2 rounded bg-indigo-950/40 border border-indigo-500/20 text-indigo-200">
                                            ${cp.explanation}
                                        </div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                `;
            } else {
                const isLast = (currentSlideIndex === total - 1);
                container.innerHTML = `
                    <div class="slide-fade-in space-y-5">
                        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                            <h2 class="text-lg sm:text-xl font-bold text-white flex items-center gap-2">
                                <span class="text-amber-400 font-mono">Quiz #${currNum - 16}</span>
                                ${slide.title}
                            </h2>
                            <span class="text-xs px-2.5 py-0.5 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-300 font-bold">10 Challenge Questions</span>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            ${slide.questions.map((q, qIdx) => `
                                <div class="p-3.5 bg-slate-950/80 rounded-xl border border-slate-800 flex flex-col justify-between">
                                    <div>
                                        <div class="flex items-start justify-between gap-2 mb-2">
                                            <span class="text-xs font-bold text-indigo-400 font-mono">Q${q.id}</span>
                                            <button onclick="showSolution(${currentSlideIndex}, ${qIdx})" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30 hover:bg-amber-500/20 transition flex items-center gap-1">
                                                <i data-lucide="eye" class="w-3 h-3"></i>
                                                View Solution
                                            </button>
                                        </div>
                                        <p class="text-xs text-slate-200 font-medium mb-3">${q.q}</p>
                                        <div class="space-y-1.5 mb-2">
                                            ${q.options.map((opt, oIdx) => `
                                                <button onclick="answerQuiz(${q.id}, ${oIdx}, ${q.ans})" id="quiz_${q.id}_${oIdx}" class="w-full text-left text-xs px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-indigo-500 text-slate-300 transition flex items-center justify-between">
                                                    <span>${opt}</span>
                                                    <span id="quiz_ind_${q.id}_${oIdx}" class="hidden font-bold"></span>
                                                </button>
                                            `).join('')}
                                        </div>
                                    </div>
                                    <div id="quiz_feedback_${q.id}" class="hidden text-[11px] p-2 rounded bg-slate-900 border text-slate-300"></div>
                                </div>
                            `).join('')}
                        </div>

                        ${isLast ? `
                            <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-emerald-950/60 border border-emerald-500/40 text-center">
                                <div class="text-emerald-400 font-bold text-base mb-1">🎉 Congratulations! You have completed Linear Equations in Two Variables!</div>
                                <div class="text-slate-300 text-xs">You have reached the last slide of this chapter. You have mastered standard form, infinite solution coordinates, Cartesian lines, slope-intercept form, pairs of linear equations, consistency ratios, substitution, elimination, river current models, and matrix determinants!</div>
                            </div>
                        ` : ''}
                    </div>
                `;
            }

            if (window.lucide) lucide.createIcons();
            if (window.renderMathInElement) {
                renderMathInElement(container, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false
                });
            }

            initSlideSimulator(currentSlideIndex + 1);
            renderThumbnails();
            speakCurrentSlide();
        }

        function renderThumbnails() {
            const thumbContainer = document.getElementById('slideThumbnails');
            if (!thumbContainer) return;
            thumbContainer.innerHTML = ALL_SLIDES.map((s, idx) => `
                <button onclick="goToSlide(${idx})" title="${s.title}" class="w-6 h-6 rounded-md text-[10px] font-bold font-mono transition flex items-center justify-center ${idx === currentSlideIndex ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-800 text-slate-400 hover:bg-slate-700'}">
                    ${idx + 1}
                </button>
            `).join('');
        }

        function nextSlide() {
            if (currentSlideIndex < ALL_SLIDES.length - 1) {
                currentSlideIndex++;
                renderCurrentSlide();
            }
        }

        function prevSlide() {
            if (currentSlideIndex > 0) {
                currentSlideIndex--;
                renderCurrentSlide();
            }
        }

        function goToSlide(idx) {
            if (idx >= 0 && idx < ALL_SLIDES.length) {
                currentSlideIndex = idx;
                renderCurrentSlide();
            }
        }

        function checkCheckpoint(cIdx, oIdx, ans) {
            const isCorrect = (oIdx === ans);
            if (isCorrect) playSuccessSound(); else playErrorSound();

            const curSlide = ALL_SLIDES[currentSlideIndex];
            const opts = curSlide.checkpoints[cIdx].options;

            for (let i = 0; i < opts.length; i++) {
                const btn = document.getElementById(`cp_${cIdx}_${i}`);
                const ind = document.getElementById(`cp_ind_${cIdx}_${i}`);
                if (btn && ind) {
                    btn.disabled = true;
                    if (i === ans) {
                        btn.classList.add('bg-emerald-950/70', 'border-emerald-500/50', 'text-emerald-300');
                        ind.textContent = '✓ Correct';
                        ind.classList.remove('hidden');
                        ind.classList.add('text-emerald-400');
                    } else if (i === oIdx && !isCorrect) {
                        btn.classList.add('bg-rose-950/70', 'border-rose-500/50', 'text-rose-300');
                        ind.textContent = '✗';
                        ind.classList.remove('hidden');
                        ind.classList.add('text-rose-400');
                    }
                }
            }
            const exp = document.getElementById(`cp_exp_${cIdx}`);
            if (exp) exp.classList.remove('hidden');
        }

        function answerQuiz(qId, oIdx, ans) {
            const isCorrect = (oIdx === ans);
            if (isCorrect) playSuccessSound(); else playErrorSound();

            for (let i = 0; i < 4; i++) {
                const btn = document.getElementById(`quiz_${qId}_${i}`);
                const ind = document.getElementById(`quiz_ind_${qId}_${i}`);
                if (btn && ind) {
                    btn.disabled = true;
                    if (i === ans) {
                        btn.classList.add('bg-emerald-950/70', 'border-emerald-500/50', 'text-emerald-300');
                        ind.textContent = '✓';
                        ind.classList.remove('hidden');
                        ind.classList.add('text-emerald-400');
                    } else if (i === oIdx && !isCorrect) {
                        btn.classList.add('bg-rose-950/70', 'border-rose-500/50', 'text-rose-300');
                        ind.textContent = '✗';
                        ind.classList.remove('hidden');
                        ind.classList.add('text-rose-400');
                    }
                }
            }
            const fb = document.getElementById(`quiz_feedback_${qId}`);
            if (fb) {
                fb.classList.remove('hidden');
                fb.innerHTML = isCorrect ?
                    '<span class="text-emerald-400 font-bold">✓ Correct Answer!</span> Excellent analytical work.' :
                    '<span class="text-rose-400 font-bold">✗ Incorrect.</span> Click "View Solution" for detailed steps.';
            }
        }

        function showSolution(slideIdx, qIdx) {
            const slide = ALL_SLIDES[slideIdx];
            const q = slide.questions[qIdx];
            const modal = document.getElementById('solutionModal');
            const title = document.getElementById('solutionModalTitle');
            const body = document.getElementById('solutionModalBody');

            title.textContent = `Question ${q.id} Solution: ${q.q.substring(0, 40)}...`;
            body.innerHTML = `
                <div class="p-3 bg-slate-950 rounded-lg border border-slate-800 text-xs text-slate-300">
                    <strong>Question:</strong> ${q.q}
                </div>
                <div class="p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/30 text-xs text-indigo-200">
                    <strong class="text-emerald-400">Step-by-Step Derivation:</strong><br>
                    ${q.solution}
                </div>
                <div class="text-xs text-amber-300 font-semibold">
                    Correct Option: ${q.options[q.ans]}
                </div>
            `;
            modal.classList.remove('hidden');
            if (window.renderMathInElement) renderMathInElement(body);
        }

        function closeSolutionModal() {
            document.getElementById('solutionModal').classList.add('hidden');
        }

        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
            if (e.key === 'Escape') closeSolutionModal();
        });

        // --- SIMULATORS 1 TO 16 LOGIC ---

        function initSlideSimulator(sNum) {
            if (sNum === 1) updateSim1();
            else if (sNum === 2) updateSim2();
            else if (sNum === 3) drawSim3();
            else if (sNum === 4) drawSim4();
            else if (sNum === 5) setSim5Mode('continuous');
            else if (sNum === 6) drawSim6();
            else if (sNum === 7) drawSim7();
            else if (sNum === 8) drawSim8();
            else if (sNum === 9) setSim9Case('intersect');
            else if (sNum === 10) testSim10([1, -2, 0], [3, 4, -20]);
            else if (sNum === 11) resetSim11();
            else if (sNum === 12) resetSim12();
            else if (sNum === 13) runSim13();
            else if (sNum === 14) runSim14();
            else if (sNum === 15) runSim15();
            else if (sNum === 16) runSim16();
        }

        // Sim 1: Problem Translator
        function updateSim1() {
            const sc = document.getElementById('sim1_scenario').value;
            const disp = document.getElementById('sim1_display');
            const std = document.getElementById('sim1_standard');
            if (!disp) return;

            if (sc === 'cricket') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Two batsmen scored 176 runs together.</div>
                    <div class="text-slate-300">Let Rohit's runs = x, Virat's runs = y</div>
                    <div class="text-cyan-300 font-mono">x + y = 176</div>
                `;
                std.textContent = "Standard: 1x + 1y - 176 = 0 (a=1, b=1, c=-176)";
            } else if (sc === 'stationery') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Cost of 5 notebooks and 7 pens is ₹250.</div>
                    <div class="text-slate-300">Let notebook = x, pen = y</div>
                    <div class="text-cyan-300 font-mono">5x + 7y = 250</div>
                `;
                std.textContent = "Standard: 5x + 7y - 250 = 0 (a=5, b=7, c=-250)";
            } else if (sc === 'fare') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Taxi fare: ₹15 for 1st km, ₹8/km thereafter. Total distance x, fare y.</div>
                    <div class="text-slate-300">y = 15 + (x - 1)8 = 8x + 7</div>
                    <div class="text-cyan-300 font-mono">8x - y + 7 = 0</div>
                `;
                std.textContent = "Standard: 8x - 1y + 7 = 0 (a=8, b=-1, c=7)";
            }
        }

        // Sim 2: Table Generator
        function updateSim2() {
            const x = parseInt(document.getElementById('sim2_x').value);
            document.getElementById('sim2_x_val').textContent = x;
            document.getElementById('sim2_sub_x').textContent = x;
            document.getElementById('sim2_pair_x').textContent = x;

            const y = (12 - 2 * x) / 3;
            document.getElementById('sim2_y_val').textContent = y.toFixed(2);
            document.getElementById('sim2_pair_y').textContent = y.toFixed(2);

            const tbl = document.getElementById('sim2_table');
            if (!tbl) return;
            const pts = [-3, 0, 3, 6];
            tbl.innerHTML = pts.map(px => {
                const py = (12 - 2 * px) / 3;
                return `<div class="p-1 bg-slate-900 rounded border border-slate-800"><span class="text-slate-500">x=${px}:</span> <span class="text-emerald-400 font-bold">(${px}, ${py.toFixed(1)})</span></div>`;
            }).join('');
        }

        // Sim 3: Cartesian Line Plotter
        function drawSim3() {
            const svg = document.getElementById('sim3_svg');
            if (!svg) return;

            svg.innerHTML = `
                <line x1="20" y1="100" x2="240" y2="100" stroke="#334155" stroke-width="1.5"/>
                <line x1="130" y1="10" x2="130" y2="190" stroke="#334155" stroke-width="1.5"/>
                <text x="235" y="115" fill="#94a3b8" font-size="10">x</text>
                <text x="135" y="20" fill="#94a3b8" font-size="10">y</text>

                <!-- Line x + 2y = 6: (0, 3) ⟹ cx=130, cy=100 - 3*18 = 46. (6, 0) ⟹ cx=130 + 6*18 = 238, cy=100 -->
                <line x1="40" y1="19" x2="240" y2="109" stroke="#6366f1" stroke-width="2.5"/>
                <circle cx="130" cy="46" r="4.5" fill="#38bdf8"/>
                <text x="145" y="44" fill="#38bdf8" font-size="9" font-family="monospace">(0, 3)</text>
                <circle cx="238" cy="100" r="4.5" fill="#facc15"/>
                <text x="220" y="90" fill="#facc15" font-size="9" font-family="monospace">(6, 0)</text>
                <circle cx="166" cy="64" r="4.5" fill="#10b981"/>
                <text x="180" y="62" fill="#10b981" font-size="9" font-family="monospace">(2, 2)</text>
            `;
        }

        // Sim 4: Slope-Intercept Sandbox
        function drawSim4() {
            const m = parseFloat(document.getElementById('sim4_m').value);
            const c = parseFloat(document.getElementById('sim4_c').value);
            document.getElementById('sim4_m_val').textContent = m;
            document.getElementById('sim4_c_val').textContent = c;
            const svg = document.getElementById('sim4_svg');
            const eq = document.getElementById('sim4_eq');
            if (!svg) return;

            eq.textContent = `y = ${m}x + (${c})`;

            const scale = 14;
            const cx0 = 130;
            const cy0 = 90;

            const x1 = -6;
            const y1 = m * x1 + c;
            const x2 = 6;
            const y2 = m * x2 + c;

            const px1 = cx0 + x1 * scale;
            const py1 = cy0 - y1 * scale;
            const px2 = cx0 + x2 * scale;
            const py2 = cy0 - y2 * scale;

            svg.innerHTML = `
                <line x1="20" y1="${cy0}" x2="240" y2="${cy0}" stroke="#334155" stroke-width="1.5"/>
                <line x1="${cx0}" y1="10" x2="${cx0}" y2="170" stroke="#334155" stroke-width="1.5"/>
                <line x1="${px1}" y1="${py1}" x2="${px2}" y2="${py2}" stroke="#10b981" stroke-width="2.5"/>
                <circle cx="${cx0}" cy="${cy0 - c * scale}" r="4" fill="#f59e0b"/>
                <text x="${cx0 + 10}" y="${cy0 - c * scale + 4}" fill="#f59e0b" font-size="9" font-family="monospace">(0, ${c})</text>
            `;
        }

        // Sim 5: Domain Switcher
        function setSim5Mode(mode) {
            const svg = document.getElementById('sim5_svg');
            const info = document.getElementById('sim5_info');
            const bCont = document.getElementById('sim5_btn_cont');
            const bDisc = document.getElementById('sim5_btn_disc');
            if (!svg) return;

            if (mode === 'continuous') {
                bCont.className = "px-2 py-0.5 rounded bg-indigo-600 text-white text-[11px]";
                bDisc.className = "px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]";
                info.textContent = "Continuous line: infinitely many real solutions spanning quadrants.";
                svg.innerHTML = `
                    <line x1="20" y1="150" x2="220" y2="150" stroke="#334155" stroke-width="1.5"/>
                    <line x1="40" y1="10" x2="40" y2="170" stroke="#334155" stroke-width="1.5"/>
                    <line x1="20" y1="20" x2="180" y2="160" stroke="#38bdf8" stroke-width="2"/>
                `;
            } else {
                bDisc.className = "px-2 py-0.5 rounded bg-indigo-600 text-white text-[11px]";
                bCont.className = "px-2 py-0.5 rounded bg-slate-700 text-white text-[11px]";
                info.textContent = "Discrete points in Quadrant I: (0,10), (1,8), (2,6), (3,4), (4,2), (5,0).";
                let dots = [];
                for (let x = 0; x <= 5; x++) {
                    let y = 10 - 2 * x;
                    let px = 40 + x * 28;
                    let py = 150 - y * 11;
                    dots.push(`<circle cx="${px}" cy="${py}" r="5" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>`);
                    dots.push(`<text x="${px}" y="${py - 8}" fill="#fde68a" font-size="8" text-anchor="middle">(${x},${y})</text>`);
                }
                svg.innerHTML = `
                    <line x1="30" y1="150" x2="220" y2="150" stroke="#334155" stroke-width="1.5"/>
                    <line x1="40" y1="20" x2="40" y2="160" stroke="#334155" stroke-width="1.5"/>
                    <line x1="40" y1="40" x2="180" y2="150" stroke="#475569" stroke-dasharray="3,3"/>
                    ${dots.join('')}
                `;
            }
        }

        // Sim 6: Parallel Axes
        function drawSim6() {
            const x = parseInt(document.getElementById('sim6_x').value);
            const y = parseInt(document.getElementById('sim6_y').value);
            document.getElementById('sim6_x_val').textContent = x;
            document.getElementById('sim6_y_val').textContent = y;
            document.getElementById('sim6_pt').textContent = `${x}, ${y}`;
            const svg = document.getElementById('sim6_svg');
            if (!svg) return;

            const scale = 16;
            const cx0 = 120;
            const cy0 = 90;

            const vertX = cx0 + x * scale;
            const horizY = cy0 - y * scale;

            svg.innerHTML = `
                <line x1="20" y1="${cy0}" x2="220" y2="${cy0}" stroke="#475569" stroke-width="1.5"/>
                <line x1="${cx0}" y1="15" x2="${cx0}" y2="165" stroke="#475569" stroke-width="1.5"/>
                <line x1="${vertX}" y1="15" x2="${vertX}" y2="165" stroke="#38bdf8" stroke-width="2.5"/>
                <line x1="20" y1="${horizY}" x2="220" y2="${horizY}" stroke="#fbbf24" stroke-width="2.5"/>
                <circle cx="${vertX}" cy="${horizY}" r="5" fill="#ef4444"/>
            `;
        }

        // Sim 7: Dual Line Visualizer
        function drawSim7() {
            const svg = document.getElementById('sim7_svg');
            if (!svg) return;

            svg.innerHTML = `
                <line x1="20" y1="120" x2="220" y2="120" stroke="#334155" stroke-width="1.5"/>
                <line x1="60" y1="20" x2="60" y2="160" stroke="#334155" stroke-width="1.5"/>
                <!-- Line 1: x + y = 5 -->
                <line x1="30" y1="60" x2="190" y2="140" stroke="#6366f1" stroke-width="2"/>
                <!-- Line 2: 2x - y = 4 -->
                <line x1="70" y1="150" x2="160" y2="30" stroke="#f59e0b" stroke-width="2"/>
                <!-- Intersection at (3, 2) -->
                <circle cx="120" cy="90" r="5" fill="#10b981"/>
                <text x="135" y="85" fill="#10b981" font-size="10" font-weight="bold" font-family="monospace">(3, 2)</text>
            `;
        }

        // Sim 8: Graphical Intersection Finder
        function revealSim8() {
            drawSim8(true);
        }
        function drawSim8(reveal = false) {
            const svg = document.getElementById('sim8_svg');
            const res = document.getElementById('sim8_result');
            if (!svg) return;

            svg.innerHTML = `
                <line x1="20" y1="130" x2="220" y2="130" stroke="#334155" stroke-width="1.5"/>
                <line x1="50" y1="20" x2="50" y2="160" stroke="#334155" stroke-width="1.5"/>
                <!-- x - y = 1 ⟹ y = x - 1 -->
                <line x1="40" y1="140" x2="180" y2="40" stroke="#38bdf8" stroke-width="2"/>
                <!-- 2x + y = 8 ⟹ y = 8 - 2x -->
                <line x1="50" y1="30" x2="140" y2="150" stroke="#f43f5e" stroke-width="2"/>
                ${reveal ? '<circle cx="110" cy="70" r="6" fill="#10b981" stroke="#fff" stroke-width="1.5"/><text x="125" y="65" fill="#10b981" font-size="11" font-weight="bold" font-family="monospace">(3, 2)</text>' : ''}
            `;
            if (reveal) {
                res.innerHTML = `<span class="text-emerald-400 font-bold">Intersection Verified at x = 3, y = 2! Satisfies both equations.</span>`;
            }
        }

        // Sim 9: 3-Case Geometric Morphing
        function setSim9Case(cType) {
            const svg = document.getElementById('sim9_svg');
            const desc = document.getElementById('sim9_desc');
            const b1 = document.getElementById('sim9_btn_1');
            const b2 = document.getElementById('sim9_btn_2');
            const b3 = document.getElementById('sim9_btn_3');
            if (!svg) return;

            [b1, b2, b3].forEach(b => b.className = "px-2.5 py-1 rounded bg-slate-700 text-white text-xs font-semibold");

            if (cType === 'intersect') {
                b1.className = "px-2.5 py-1 rounded bg-indigo-600 text-white text-xs font-semibold";
                desc.textContent = "1. Intersecting Lines: Unique single solution (Consistent & Independent).";
                svg.innerHTML = `
                    <line x1="30" y1="50" x2="210" y2="130" stroke="#38bdf8" stroke-width="2.5"/>
                    <line x1="50" y1="140" x2="190" y2="40" stroke="#fbbf24" stroke-width="2.5"/>
                    <circle cx="120" cy="90" r="5" fill="#10b981"/>
                `;
            } else if (cType === 'parallel') {
                b2.className = "px-2.5 py-1 rounded bg-indigo-600 text-white text-xs font-semibold";
                desc.textContent = "2. Parallel Lines: No intersection, Zero solutions (Inconsistent system).";
                svg.innerHTML = `
                    <line x1="30" y1="60" x2="210" y2="60" stroke="#ef4444" stroke-width="2.5"/>
                    <line x1="30" y1="120" x2="210" y2="120" stroke="#fbbf24" stroke-width="2.5"/>
                `;
            } else if (cType === 'coincident') {
                b3.className = "px-2.5 py-1 rounded bg-indigo-600 text-white text-xs font-semibold";
                desc.textContent = "3. Coincident Lines: Overlapping lines with infinitely many solutions (Dependent).";
                svg.innerHTML = `
                    <line x1="30" y1="90" x2="210" y2="90" stroke="#6366f1" stroke-width="6"/>
                    <line x1="30" y1="90" x2="210" y2="90" stroke="#10b981" stroke-dasharray="8,6" stroke-width="3"/>
                `;
            }
        }

        // Sim 10: Ratio Test Scanner
        function testSim10(e1, e2) {
            const disp = document.getElementById('sim10_display');
            if (!disp) return;

            const r1 = (e1[0] / e2[0]).toFixed(2);
            const r2 = (e1[1] / e2[1]).toFixed(2);
            const r3 = (e1[2] / e2[2]).toFixed(2);

            let res = `<div class="font-bold text-amber-300">Eq 1: ${e1[0]}x + (${e1[1]})y + (${e1[2]}) = 0</div>`;
            res += `<div class="font-bold text-amber-300">Eq 2: ${e2[0]}x + (${e2[1]})y + (${e2[2]}) = 0</div>`;
            res += `<div class="text-cyan-300">a₁/a₂ = ${r1} | b₁/b₂ = ${r2} | c₁/c₂ = ${r3}</div>`;

            if (r1 !== r2) {
                res += `<div class="text-emerald-400 font-bold mt-1">✓ a₁/a₂ ≠ b₁/b₂ ⟹ Intersecting Lines (Unique Solution, Consistent)</div>`;
            } else if (r1 === r2 && r2 === r3) {
                res += `<div class="text-amber-400 font-bold mt-1">✓ a₁/a₂ = b₁/b₂ = c₁/c₂ ⟹ Coincident Lines (Infinite Solutions, Dependent)</div>`;
            } else {
                res += `<div class="text-rose-400 font-bold mt-1">✓ a₁/a₂ = b₁/b₂ ≠ c₁/c₂ ⟹ Parallel Lines (No Solution, Inconsistent)</div>`;
            }
            disp.innerHTML = res;
        }

        // Sim 11: Substitution Stepper
        let sim11Step = 0;
        function resetSim11() {
            sim11Step = 0;
            stepSim11();
        }
        function stepSim11() {
            const box = document.getElementById('sim11_box');
            if (!box) return;
            sim11Step = (sim11Step % 4) + 1;

            if (sim11Step === 1) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 1: Isolate variable y from Equation 1</div>
                    <div>2x + y = 7 ⟹ <span class="text-amber-300 font-bold">y = 7 - 2x</span></div>
                `;
            } else if (sim11Step === 2) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 2: Substitute into Equation 2</div>
                    <div>4x - 3(<span class="text-amber-300">7 - 2x</span>) = -1</div>
                    <div>4x - 21 + 6x = -1 ⟹ 10x - 21 = -1</div>
                `;
            } else if (sim11Step === 3) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 3: Solve for x</div>
                    <div>10x = 20 ⟹ <span class="text-emerald-400 font-bold">x = 2</span></div>
                `;
            } else if (sim11Step === 4) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 4: Back-substitute to find y</div>
                    <div>y = 7 - 2(2) = 7 - 4 = <span class="text-emerald-400 font-bold">3</span></div>
                    <div class="text-emerald-300 font-bold mt-1">✓ Unique Solution: (2, 3)</div>
                `;
            }
        }

        // Sim 12: Elimination Balancer
        let sim12Step = 0;
        function resetSim12() {
            sim12Step = 0;
            stepSim12();
        }
        function stepSim12() {
            const box = document.getElementById('sim12_box');
            if (!box) return;
            sim12Step = (sim12Step % 4) + 1;

            if (sim12Step === 1) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 1: Target variable y for elimination</div>
                    <div>Multiply Eq 2 by 2: 2(2x - 2y) = 2(2) ⟹ <span class="text-amber-300">4x - 4y = 4</span></div>
                `;
            } else if (sim12Step === 2) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 2: Add equations to eliminate y</div>
                    <div>(3x + 4y) + (4x - 4y) = 10 + 4</div>
                    <div>7x + 0 = 14 ⟹ <span class="text-emerald-400 font-bold">7x = 14</span></div>
                `;
            } else if (sim12Step === 3) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 3: Solve for x</div>
                    <div><span class="text-emerald-400 font-bold">x = 2</span></div>
                `;
            } else if (sim12Step === 4) {
                box.innerHTML = `
                    <div class="text-indigo-400 font-bold">Step 4: Substitute x = 2 into Eq 1</div>
                    <div>3(2) + 4y = 10 ⟹ 6 + 4y = 10 ⟹ 4y = 4 ⟹ <span class="text-emerald-400 font-bold">y = 1</span></div>
                    <div class="text-emerald-300 font-bold mt-1">✓ Unique Solution: (2, 1)</div>
                `;
            }
        }

        // Sim 13: River Current Simulator
        function runSim13() {
            const x = parseInt(document.getElementById('sim13_x').value);
            const y = parseInt(document.getElementById('sim13_y').value);
            document.getElementById('sim13_x_val').textContent = x;
            document.getElementById('sim13_y_val').textContent = y;
            const svg = document.getElementById('sim13_svg');
            const res = document.getElementById('sim13_result');
            if (!svg) return;

            const down = x + y;
            const up = Math.max(0, x - y);

            svg.innerHTML = `
                <!-- River banks -->
                <rect x="10" y="20" width="220" height="100" fill="#0369a1" rx="8"/>
                <line x1="20" y1="50" x2="200" y2="50" stroke="#38bdf8" stroke-dasharray="6,4" stroke-width="2"/>
                <line x1="20" y1="90" x2="200" y2="90" stroke="#38bdf8" stroke-dasharray="6,4" stroke-width="2"/>
                <!-- Boat Downstream -->
                <polygon points="120,40 150,45 120,50 110,45" fill="#f59e0b"/>
                <text x="160" y="48" fill="#fff" font-size="9" font-family="monospace">Down ⟹</text>
                <!-- Boat Upstream -->
                <polygon points="120,80 90,85 120,90 130,85" fill="#ef4444"/>
                <text x="50" y="88" fill="#fff" font-size="9" font-family="monospace">⟸ Up</text>
            `;

            res.textContent = `Downstream Speed: ${down} km/h | Upstream Speed: ${up} km/h`;
        }

        // Sim 14: Digit Reversal
        function runSim14() {
            const x = parseInt(document.getElementById('sim14_x').value);
            const y = parseInt(document.getElementById('sim14_y').value);
            document.getElementById('sim14_x_val').textContent = x;
            document.getElementById('sim14_y_val').textContent = y;
            const disp = document.getElementById('sim14_display');
            if (!disp) return;

            const orig = 10 * x + y;
            const rev = 10 * y + x;
            const sum = orig + rev;
            const diff = orig - rev;

            disp.innerHTML = `
                <div class="text-amber-300 font-bold">Original: 10(${x}) + ${y} = ${orig}</div>
                <div class="text-cyan-300 font-bold">Reversed: 10(${y}) + ${x} = ${rev}</div>
                <div>Sum: ${orig} + ${rev} = ${sum} = 11 × (${x + y})</div>
                <div>Difference: ${orig} - ${rev} = ${diff} = 9 × (${x - y})</div>
            `;
        }

        // Sim 15: Cost Simulator
        function runSim15() {
            const km = parseInt(document.getElementById('sim15_km').value);
            document.getElementById('sim15_km_label').textContent = `Distance: ${km} km`;
            const svg = document.getElementById('sim15_svg');
            const tot = document.getElementById('sim15_total');
            if (!svg) return;

            const fare = 5 + km * 10;
            tot.textContent = `Total Fare for ${km} km = ₹5 + ${km}(₹10) = ₹${fare}`;

            const barW = Math.min(200, km * 8);

            svg.innerHTML = `
                <text x="20" y="30" fill="#94a3b8" font-size="10">Base Charge</text>
                <rect x="20" y="35" width="20" height="20" rx="3" fill="#6366f1"/>
                <text x="25" y="50" fill="#fff" font-size="9">₹5</text>
                <text x="20" y="80" fill="#94a3b8" font-size="10">Distance Charge (${km} km × ₹10)</text>
                <rect x="20" y="85" width="${barW}" height="20" rx="3" fill="#10b981"/>
                <text x="${barW + 30}" y="100" fill="#10b981" font-size="11" font-weight="bold">₹${km * 10}</text>
            `;
        }

        // Sim 16: Matrix Cramer Solver
        function runSim16() {
            const a1 = parseFloat(document.getElementById('sim16_a1').value) || 0;
            const b1 = parseFloat(document.getElementById('sim16_b1').value) || 0;
            const c1 = parseFloat(document.getElementById('sim16_c1').value) || 0;
            const a2 = parseFloat(document.getElementById('sim16_a2').value) || 0;
            const b2 = parseFloat(document.getElementById('sim16_b2').value) || 0;
            const c2 = parseFloat(document.getElementById('sim16_c2').value) || 0;
            const res = document.getElementById('sim16_result');
            if (!res) return;

            const D = a1 * b2 - a2 * b1;
            const Dx = b1 * c2 - b2 * c1;
            const Dy = c1 * a2 - c2 * a1;

            if (Math.abs(D) > 0.0001) {
                const x = Dx / D;
                const y = Dy / D;
                res.innerHTML = `
                    <div>Determinant D = (${a1})(${b2}) - (${a2})(${b1}) = <span class="text-cyan-300 font-bold">${D}</span> ≠ 0</div>
                    <div>Dx = ${Dx.toFixed(1)}, Dy = ${Dy.toFixed(1)}</div>
                    <div class="text-emerald-400 font-bold text-sm">Solution: x = ${x.toFixed(2)}, y = ${y.toFixed(2)}</div>
                `;
            } else {
                res.innerHTML = `<span class="text-rose-400 font-bold">Determinant D = 0! System has either no solution or infinite solutions.</span>`;
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderCurrentSlide();
        });
    </script>
</body>
</html>
"""

    html_content = html_template.replace("__SLIDES_JSON__", slides_json).replace("__QUIZZES_JSON__", quizzes_json)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated {OUTPUT_PATH} ({len(html_content)} bytes)")

if __name__ == "__main__":
    generate_html()
