# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 4
UNIT: EXPLORING ALGEBRAIC IDENTITIES (Competencies CG-7, C-7.2, CG-9)
Generates public/animations/class9-algebraic-identities.html
"""

import json
import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from class9_algebraic_identities_data import SLIDES_DATA, QUIZ_SLIDES

OUTPUT_PATH = "public/animations/class9-algebraic-identities.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA)
    quizzes_json = json.dumps(QUIZ_SLIDES)

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Mathematics • Chapter 4 • Exploring Algebraic Identities Lab</title>
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
                    <i data-lucide="layers" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">Class 9 Maths • Chapter 4</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 font-semibold">Concept 1</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Exploring Algebraic Identities Lab</h1>
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
            <!-- Animated SVG Avatar: Prof. Sophia -->
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

            <!-- Speech Text Display -->
            <div class="flex-1 w-full text-center sm:text-left">
                <div class="flex items-center justify-center sm:justify-between gap-2 mb-1">
                    <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                        <span id="speechIndicator" class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        Teacher's Voiceover Explanation
                    </span>
                    <span class="text-[11px] text-slate-400 hidden sm:inline">Web Speech & Web Audio Synthesizer</span>
                </div>
                <p id="teacherSpeechText" class="text-sm text-slate-200 leading-relaxed font-normal italic">
                    Welcome to Exploring Algebraic Identities! Let us visualize formulas with geometric models and master factorisation.
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

        // Sound Synthesizer
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
            playTone(523.25, 'triangle', 0.15); // C5
            setTimeout(() => playTone(659.25, 'triangle', 0.2), 100); // E5
            setTimeout(() => playTone(783.99, 'triangle', 0.3), 200); // G5
        }

        function playErrorSound() {
            playTone(330, 'sawtooth', 0.15);
            setTimeout(() => playTone(280, 'sawtooth', 0.25), 120);
        }

        // Teacher Voiceover
        function speakCurrentSlide() {
            if (!isVoiceEnabled || !('speechSynthesis' in window)) return;

            window.speechSynthesis.cancel();
            const slide = ALL_SLIDES[currentSlideIndex];
            const textToSpeak = slide.audio_text || (slide.title + ". Challenge questions. Select the correct option and view the step-by-step solution.");

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

        // Slide Rendering Engine
        function renderCurrentSlide() {
            const slide = ALL_SLIDES[currentSlideIndex];
            const container = document.getElementById('slideContentContainer');
            const counter = document.getElementById('slideCounter');
            const progress = document.getElementById('progressBar');
            const badge = document.getElementById('currentBadge');
            const speechText = document.getElementById('teacherSpeechText');
            const nextBtn = document.getElementById('nextBtn');
            const prevBtn = document.getElementById('prevBtn');

            // Update Progress
            const total = ALL_SLIDES.length;
            const currNum = currentSlideIndex + 1;
            counter.textContent = `${currNum} / ${total}`;
            progress.style.width = `${(currNum / total) * 100}%`;
            badge.textContent = slide.badge || `Slide ${currNum}`;
            speechText.textContent = slide.audio_text || slide.title;

            // Nav buttons state
            prevBtn.disabled = (currentSlideIndex === 0);

            // Strict last slide check
            if (currentSlideIndex === total - 1) {
                nextBtn.style.display = 'none';
            } else {
                nextBtn.style.display = 'flex';
            }

            // Render Content
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

                        <!-- In-Slide Checkpoints -->
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
                                <div class="text-emerald-400 font-bold text-base mb-1">🎉 Congratulations! You have completed Chapter 4!</div>
                                <div class="text-slate-300 text-xs">You have reached the last slide of this chapter. You have mastered algebraic identities, geometric models, quadratic factorisation with algebra tiles, cubic identities, rational expressions, and computational decomposition!</div>
                            </div>
                        ` : ''}
                    </div>
                `;
            }

            // Refresh icons and math
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

            // Initialize simulator for current slide
            initSlideSimulator(currentSlideIndex + 1);

            // Update mini-thumbnails
            renderThumbnails();

            // Speak slide
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

        // Checkpoint handler
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

        // Quiz Question Answer
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
                    '<span class="text-emerald-400 font-bold">✓ Correct Answer!</span> Great work.' :
                    '<span class="text-rose-400 font-bold">✗ Incorrect.</span> Click "View Solution" for detailed steps.';
            }
        }

        // Pop-up Solution Modal
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
            else if (sNum === 2) drawSim2();
            else if (sNum === 3) drawSim3();
            else if (sNum === 4) setSim4Step(1);
            else if (sNum === 5) drawSim5();
            else if (sNum === 6) factorSim6('49x2-36');
            else if (sNum === 7) drawSim7();
            else if (sNum === 8) runSim8();
            else if (sNum === 9) drawSim9();
            else if (sNum === 10) drawSim10();
            else if (sNum === 11) soapSim11('27x3+8y3');
            else if (sNum === 12) calcSim12();
            else if (sNum === 13) runSim13();
            else if (sNum === 14) scanSim14('x2-4');
            else if (sNum === 15) reduceSim15('diff_sq');
            else if (sNum === 16) drawSim16();
        }

        // Sim 1: Identity vs Equation
        function updateSim1() {
            const mode = document.getElementById('sim1_mode').value;
            const x = parseFloat(document.getElementById('sim1_x').value);
            document.getElementById('sim1_x_val').textContent = x;
            const lhsEl = document.getElementById('sim1_lhs');
            const rhsEl = document.getElementById('sim1_rhs');
            const status = document.getElementById('sim1_status');

            if (mode === 'identity') {
                const lhs = Math.pow(x + 3, 2);
                const rhs = x * x + 6 * x + 9;
                lhsEl.textContent = lhs.toFixed(1);
                rhsEl.textContent = rhs.toFixed(1);
                status.innerHTML = `<span class="text-emerald-400">✓ LHS = RHS identically (${lhs} = ${rhs})! Holds for ALL x.</span>`;
            } else {
                const lhs = 2 * x + 5;
                const rhs = 15;
                lhsEl.textContent = lhs.toFixed(1);
                rhsEl.textContent = rhs;
                if (Math.abs(lhs - rhs) < 0.001) {
                    status.innerHTML = `<span class="text-emerald-400">✓ Solution found! At x = ${x}, 2x + 5 = 15.</span>`;
                } else {
                    status.innerHTML = `<span class="text-rose-400">✗ LHS ≠ RHS (${lhs} ≠ 15). Conditional equation only true at x = 5!</span>`;
                }
            }
        }

        // Sim 2: (a + b)² Area Dissector
        function drawSim2() {
            const a = parseInt(document.getElementById('sim2_a').value);
            const b = parseInt(document.getElementById('sim2_b').value);
            document.getElementById('sim2_a_val').textContent = a;
            document.getElementById('sim2_b_val').textContent = b;
            const svg = document.getElementById('sim2_svg');
            const calc = document.getElementById('sim2_calc');
            if (!svg) return;

            const scale = 22;
            const wA = a * scale;
            const wB = b * scale;
            const offX = 20;
            const offY = 20;

            svg.innerHTML = `
                <!-- Square a² -->
                <rect x="${offX}" y="${offY}" width="${wA}" height="${wA}" fill="#4f46e5" stroke="#312e81" stroke-width="2"/>
                <text x="${offX + wA/2}" y="${offY + wA/2 + 5}" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">a² = ${a*a}</text>

                <!-- Rectangle ab (top right) -->
                <rect x="${offX + wA}" y="${offY}" width="${wB}" height="${wA}" fill="#0ea5e9" stroke="#0369a1" stroke-width="2"/>
                <text x="${offX + wA + wB/2}" y="${offY + wA/2 + 5}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">ab = ${a*b}</text>

                <!-- Rectangle ab (bottom left) -->
                <rect x="${offX}" y="${offY + wA}" width="${wA}" height="${wB}" fill="#0ea5e9" stroke="#0369a1" stroke-width="2"/>
                <text x="${offX + wA/2}" y="${offY + wA + wB/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">ab = ${a*b}</text>

                <!-- Square b² (bottom right) -->
                <rect x="${offX + wA}" y="${offY + wA}" width="${wB}" height="${wB}" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
                <text x="${offX + wA + wB/2}" y="${offY + wA + wB/2 + 4}" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">b² = ${b*b}</text>
            `;

            const tot = (a + b) * (a + b);
            calc.textContent = `(${a} + ${b})² = ${a*a} + ${a*b} + ${a*b} + ${b*b} = ${tot}`;
        }

        // Sim 3: a² - b² Rearranger
        let sim3Rearranged = false;
        function toggleSim3Rearrange() {
            sim3Rearranged = !sim3Rearranged;
            drawSim3();
        }

        function drawSim3() {
            const svg = document.getElementById('sim3_svg');
            const btn = document.getElementById('sim3_btn');
            const status = document.getElementById('sim3_status');
            if (!svg) return;

            if (!sim3Rearranged) {
                btn.textContent = "Slice & Rearrange to (a+b)(a-b)";
                status.textContent = "L-shape Area: a² - b²";
                svg.innerHTML = `
                    <!-- Big Square with corner cut -->
                    <rect x="30" y="20" width="140" height="80" fill="#6366f1" stroke="#4338ca" stroke-width="2"/>
                    <rect x="30" y="100" width="80" height="60" fill="#0ea5e9" stroke="#0284c7" stroke-width="2"/>
                    <!-- Cutout region -->
                    <rect x="110" y="100" width="60" height="60" fill="#1e293b" stroke="#ef4444" stroke-dasharray="4,4" stroke-width="2"/>
                    <text x="140" y="135" fill="#f87171" font-size="11" text-anchor="middle">Removed b²</text>
                    <text x="100" y="65" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Part A: (a-b)×a</text>
                    <text x="70" y="135" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Part B: (a-b)×b</text>
                `;
            } else {
                btn.textContent = "Revert to L-Shape";
                status.textContent = "Combined Rectangle: (a + b) × (a - b)";
                svg.innerHTML = `
                    <!-- Rearranged continuous rectangle -->
                    <rect x="20" y="50" width="140" height="80" fill="#6366f1" stroke="#4338ca" stroke-width="2"/>
                    <rect x="160" y="50" width="100" height="80" fill="#0ea5e9" stroke="#0284c7" stroke-width="2"/>
                    <text x="90" y="95" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Part A (length a)</text>
                    <text x="210" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Part B (length b)</text>
                    <text x="140" y="35" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Total Length: a + b</text>
                    <text x="10" y="95" fill="#facc15" font-size="11" font-weight="bold" text-anchor="end">Width: a - b</text>
                `;
            }
        }

        // Sim 4: (a - b)² Inclusion-Exclusion
        function setSim4Step(step) {
            const svg = document.getElementById('sim4_svg');
            const exp = document.getElementById('sim4_exp');
            if (!svg) return;

            if (step === 1) {
                exp.textContent = "Step 1: Start with total outer square of area a² = 25";
                svg.innerHTML = `
                    <rect x="20" y="20" width="180" height="180" fill="#4f46e5" stroke="#312e81" stroke-width="2"/>
                    <text x="110" y="115" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">Total Area a²</text>
                `;
            } else if (step === 2) {
                exp.textContent = "Step 2: Subtract two strips of area ab (-2ab). Corner b² is subtracted twice!";
                svg.innerHTML = `
                    <rect x="20" y="20" width="180" height="180" fill="#4f46e5"/>
                    <!-- Horizontal Strip -->
                    <rect x="20" y="140" width="180" height="60" fill="#ef4444" opacity="0.6"/>
                    <!-- Vertical Strip -->
                    <rect x="140" y="20" width="60" height="180" fill="#ef4444" opacity="0.6"/>
                    <text x="110" y="80" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">(a - b)²</text>
                    <text x="170" y="175" fill="#ffffff" font-size="10" text-anchor="middle">-2× b²!</text>
                `;
            } else if (step === 3) {
                exp.textContent = "Step 3: Add back the doubly-subtracted corner (+b²). Net area = a² - 2ab + b²";
                svg.innerHTML = `
                    <rect x="20" y="20" width="120" height="120" fill="#10b981" stroke="#047857" stroke-width="2"/>
                    <rect x="140" y="20" width="60" height="120" fill="#334155" opacity="0.5"/>
                    <rect x="20" y="140" width="120" height="60" fill="#334155" opacity="0.5"/>
                    <rect x="140" y="140" width="60" height="60" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
                    <text x="80" y="85" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">(a - b)² = 9</text>
                    <text x="170" y="175" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">+b² = 4</text>
                `;
            }
        }

        // Sim 5: (x + a)(x + b) Grid
        function drawSim5() {
            const x = parseInt(document.getElementById('sim5_x').value);
            const a = parseInt(document.getElementById('sim5_a').value);
            const b = parseInt(document.getElementById('sim5_b').value);
            document.getElementById('sim5_x_val').textContent = x;
            document.getElementById('sim5_a_val').textContent = a;
            document.getElementById('sim5_b_val').textContent = b;
            const svg = document.getElementById('sim5_svg');
            const calc = document.getElementById('sim5_calc');
            if (!svg) return;

            const scale = 18;
            const wX = x * scale;
            const wB = b * scale;
            const hA = a * scale;

            svg.innerHTML = `
                <!-- x² -->
                <rect x="25" y="20" width="${wX}" height="${wX}" fill="#4f46e5" stroke="#312e81" stroke-width="2"/>
                <text x="${25 + wX/2}" y="${20 + wX/2 + 5}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">x²</text>

                <!-- bx -->
                <rect x="${25 + wX}" y="20" width="${wB}" height="${wX}" fill="#0ea5e9" stroke="#0369a1" stroke-width="2"/>
                <text x="${25 + wX + wB/2}" y="${20 + wX/2 + 5}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">${b}x</text>

                <!-- ax -->
                <rect x="25" y="${20 + wX}" width="${wX}" height="${hA}" fill="#10b981" stroke="#047857" stroke-width="2"/>
                <text x="${25 + wX/2}" y="${20 + wX + hA/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">${a}x</text>

                <!-- ab -->
                <rect x="${25 + wX}" y="${20 + wX}" width="${wB}" height="${hA}" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
                <text x="${25 + wX + wB/2}" y="${20 + wX + hA/2 + 4}" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${a*b}</text>
            `;

            calc.textContent = `(x + ${a})(x + ${b}) = x² + (${a} + ${b})x + (${a} × ${b}) = x² + ${a+b}x + ${a*b}`;
        }

        // Sim 6: Identity Factorizer
        function factorSim6(type) {
            const disp = document.getElementById('sim6_display');
            if (!disp) return;

            if (type === '49x2-36') {
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-300">49x² - 36</div>
                    <div class="text-xs text-slate-300">Form: a² - b² where a = 7x, b = 6</div>
                    <div class="text-xs text-indigo-300 font-mono">= (7x)² - 6²</div>
                    <div class="text-sm font-bold text-emerald-400 font-mono">= (7x - 6)(7x + 6)</div>
                `;
            } else if (type === '9x2+24x+16') {
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-300">9x² + 24x + 16</div>
                    <div class="text-xs text-slate-300">Form: a² + 2ab + b² where a = 3x, b = 4</div>
                    <div class="text-xs text-indigo-300 font-mono">= (3x)² + 2(3x)(4) + 4²</div>
                    <div class="text-sm font-bold text-emerald-400 font-mono">= (3x + 4)²</div>
                `;
            } else if (type === '25x2-30xy+9y2') {
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-300">25x² - 30xy + 9y²</div>
                    <div class="text-xs text-slate-300">Form: a² - 2ab + b² where a = 5x, b = 3y</div>
                    <div class="text-xs text-indigo-300 font-mono">= (5x)² - 2(5x)(3y) + (3y)²</div>
                    <div class="text-sm font-bold text-emerald-400 font-mono">= (5x - 3y)²</div>
                `;
            }
        }

        // Sim 7: Algebra Tiles
        function drawSim7() {
            const poly = document.getElementById('sim7_poly').value;
            const svg = document.getElementById('sim7_svg');
            const facts = document.getElementById('sim7_factors');
            if (!svg) return;

            if (poly === 'x2+5x+6') {
                facts.textContent = "Dimensions: (x + 3) × (x + 2)";
                svg.innerHTML = `
                    <rect x="30" y="30" width="80" height="80" fill="#4f46e5" stroke="#312e81" stroke-width="2"/>
                    <text x="70" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">x²</text>
                    <!-- 3 horizontal strips -->
                    <rect x="115" y="30" width="25" height="80" fill="#10b981"/>
                    <rect x="145" y="30" width="25" height="80" fill="#10b981"/>
                    <rect x="175" y="30" width="25" height="80" fill="#10b981"/>
                    <!-- 2 vertical strips -->
                    <rect x="30" y="115" width="80" height="25" fill="#10b981"/>
                    <rect x="30" y="145" width="80" height="25" fill="#10b981"/>
                    <!-- 6 units -->
                    <g fill="#f59e0b">
                        <rect x="115" y="115" width="25" height="25" rx="2"/>
                        <rect x="145" y="115" width="25" height="25" rx="2"/>
                        <rect x="175" y="115" width="25" height="25" rx="2"/>
                        <rect x="115" y="145" width="25" height="25" rx="2"/>
                        <rect x="145" y="145" width="25" height="25" rx="2"/>
                        <rect x="175" y="145" width="25" height="25" rx="2"/>
                    </g>
                `;
            } else if (poly === 'x2+4x+3') {
                facts.textContent = "Dimensions: (x + 3) × (x + 1)";
                svg.innerHTML = `
                    <rect x="30" y="30" width="80" height="80" fill="#4f46e5" stroke="#312e81" stroke-width="2"/>
                    <text x="70" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">x²</text>
                    <rect x="115" y="30" width="25" height="80" fill="#10b981"/>
                    <rect x="145" y="30" width="25" height="80" fill="#10b981"/>
                    <rect x="175" y="30" width="25" height="80" fill="#10b981"/>
                    <rect x="30" y="115" width="80" height="25" fill="#10b981"/>
                    <g fill="#f59e0b">
                        <rect x="115" y="115" width="25" height="25" rx="2"/>
                        <rect x="145" y="115" width="25" height="25" rx="2"/>
                        <rect x="175" y="115" width="25" height="25" rx="2"/>
                    </g>
                `;
            } else if (poly === 'x2+6x+8') {
                facts.textContent = "Dimensions: (x + 4) × (x + 2)";
                svg.innerHTML = `
                    <rect x="25" y="30" width="70" height="70" fill="#4f46e5"/>
                    <rect x="100" y="30" width="20" height="70" fill="#10b981"/>
                    <rect x="125" y="30" width="20" height="70" fill="#10b981"/>
                    <rect x="150" y="30" width="20" height="70" fill="#10b981"/>
                    <rect x="175" y="30" width="20" height="70" fill="#10b981"/>
                    <rect x="25" y="105" width="70" height="20" fill="#10b981"/>
                    <rect x="25" y="130" width="70" height="20" fill="#10b981"/>
                    <rect x="100" y="105" width="95" height="45" fill="#f59e0b"/>
                `;
            }
        }

        // Sim 8: Middle-Term Splitter
        function runSim8() {
            const a = parseInt(document.getElementById('sim8_a').value) || 1;
            const b = parseInt(document.getElementById('sim8_b').value) || 0;
            const c = parseInt(document.getElementById('sim8_c').value) || 0;
            const steps = document.getElementById('sim8_steps');
            if (!steps) return;

            const ac = a * c;
            let pair = null;
            for (let i = -100; i <= 100; i++) {
                if (i !== 0 && ac % i === 0) {
                    let j = ac / i;
                    if (i + j === b) {
                        pair = [i, j];
                        break;
                    }
                }
            }

            if (pair) {
                const [p, q] = pair;
                steps.innerHTML = `
                    <div class="text-indigo-300 font-bold">1. Product AC = ${ac}, Sum B = ${b}</div>
                    <div class="text-cyan-300">2. Factors found: p = ${p}, q = ${q} (${p} × ${q} = ${ac}, ${p} + ${q} = ${b})</div>
                    <div class="text-slate-300">3. Split middle term: ${a}x² + ${p}x + ${q}x + ${c}</div>
                    <div class="text-emerald-400 font-bold">4. Factored: Grouping yields factors!</div>
                `;
            } else {
                steps.innerHTML = `<span class="text-rose-400">No integer factor pair exists for AC = ${ac} and B = ${b}. Use quadratic formula.</span>`;
            }
        }

        // Sim 9: (a + b + c)² Grid
        function drawSim9() {
            const svg = document.getElementById('sim9_svg');
            if (!svg) return;

            const dims = [70, 45, 30]; // a, b, c
            let elements = [];
            let currY = 20;

            for (let r = 0; r < 3; r++) {
                let currX = 20;
                for (let c = 0; c < 3; c++) {
                    const w = dims[c];
                    const h = dims[r];
                    const isSquare = (r === c);
                    const color = isSquare ? '#4f46e5' : '#0ea5e9';
                    const label = (r === 0 && c === 0) ? 'a²' :
                                  ((r === 1 && c === 1) ? 'b²' :
                                  ((r === 2 && c === 2) ? 'c²' :
                                  (((r === 0 && c === 1) || (r === 1 && c === 0)) ? 'ab' :
                                  (((r === 1 && c === 2) || (r === 2 && c === 1)) ? 'bc' : 'ca'))));

                    elements.push(`
                        <rect x="${currX}" y="${currY}" width="${w}" height="${h}" fill="${color}" stroke="#0f172a" stroke-width="1.5"/>
                        <text x="${currX + w/2}" y="${currY + h/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">${label}</text>
                    `);
                    currX += w;
                }
                currY += dims[r];
            }
            svg.innerHTML = elements.join('');
        }

        // Sim 10: 3D Binomial Cube
        let sim10Exploded = false;
        function toggleSim10Explode() {
            sim10Exploded = !sim10Exploded;
            drawSim10();
        }

        function drawSim10() {
            const svg = document.getElementById('sim10_svg');
            const btn = document.getElementById('sim10_btn');
            const status = document.getElementById('sim10_status');
            if (!svg) return;

            if (!sim10Exploded) {
                btn.textContent = "Explode into 8 Solids";
                status.textContent = "Volume = (a + b)³";
                svg.innerHTML = `
                    <polygon points="70,50 140,25 210,50 140,75" fill="#6366f1" stroke="#312e81"/>
                    <polygon points="70,50 140,75 140,155 70,130" fill="#4f46e5" stroke="#312e81"/>
                    <polygon points="140,75 210,50 210,130 140,155" fill="#4338ca" stroke="#312e81"/>
                    <text x="140" y="105" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">(a + b)³</text>
                `;
            } else {
                btn.textContent = "Assemble Solid Cube";
                status.textContent = "8 Solids: a³ + 3a²b + 3ab² + b³";
                svg.innerHTML = `
                    <rect x="30" y="30" width="50" height="50" fill="#6366f1"/><text x="55" y="60" fill="#fff" font-size="10">a³</text>
                    <rect x="90" y="30" width="50" height="25" fill="#0ea5e9"/><text x="115" y="47" fill="#fff" font-size="9">a²b</text>
                    <rect x="150" y="30" width="50" height="25" fill="#0ea5e9"/><text x="175" y="47" fill="#fff" font-size="9">a²b</text>
                    <rect x="90" y="65" width="50" height="25" fill="#0ea5e9"/><text x="115" y="82" fill="#fff" font-size="9">a²b</text>
                    <rect x="30" y="95" width="25" height="50" fill="#10b981"/><text x="42" y="125" fill="#fff" font-size="9">ab²</text>
                    <rect x="65" y="95" width="25" height="50" fill="#10b981"/><text x="77" y="125" fill="#fff" font-size="9">ab²</text>
                    <rect x="100" y="95" width="25" height="50" fill="#10b981"/><text x="112" y="125" fill="#fff" font-size="9">ab²</text>
                    <rect x="140" y="110" width="30" height="30" fill="#f59e0b"/><text x="155" y="130" fill="#000" font-size="9">b³</text>
                `;
            }
        }

        // Sim 11: Cubic Factoriser (SOAP)
        function soapSim11(type) {
            const disp = document.getElementById('sim11_display');
            if (!disp) return;

            if (type === '27x3+8y3') {
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-300">27x³ + 8y³ = (3x)³ + (2y)³</div>
                    <div class="text-xs text-slate-300">Applying: a³ + b³ = (a + b)(a² - ab + b²)</div>
                    <div class="text-sm font-bold text-emerald-400 font-mono">= (3x + 2y)(9x² - 6xy + 4y²)</div>
                    <div class="text-[11px] text-cyan-300">SOAP: Same sign (+), Opposite sign (-), Always Positive (+)</div>
                `;
            } else if (type === 'x3-64') {
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-300">x³ - 64 = x³ - 4³</div>
                    <div class="text-xs text-slate-300">Applying: a³ - b³ = (a - b)(a² + ab + b²)</div>
                    <div class="text-sm font-bold text-emerald-400 font-mono">= (x - 4)(x² + 4x + 16)</div>
                    <div class="text-[11px] text-cyan-300">SOAP: Same sign (-), Opposite sign (+), Always Positive (+)</div>
                `;
            }
        }

        // Sim 12: Conditional Cubic Identity Supercomputer
        function calcSim12() {
            const a = parseFloat(document.getElementById('sim12_a').value) || 0;
            const b = parseFloat(document.getElementById('sim12_b').value) || 0;
            const c = -(a + b);
            document.getElementById('sim12_c').value = c;
            const res = document.getElementById('sim12_result');
            if (!res) return;

            const sumCubes = Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3);
            const threeAbc = 3 * a * b * c;

            res.innerHTML = `
                <div>Sum: (${a}) + (${b}) + (${c}) = 0</div>
                <div class="text-emerald-400 font-bold">a³ + b³ + c³ = 3abc = 3 × (${a}) × (${b}) × (${c}) = ${threeAbc}</div>
                <div class="text-cyan-300">Direct Sum of Cubes: (${a})³ + (${b})³ + (${c})³ = ${sumCubes}</div>
                <div class="text-amber-300 font-bold">✓ Match confirmed! Calculated without evaluating individual cubes.</div>
            `;
        }

        // Sim 13: Sophie Germain
        function runSim13() {
            const a = parseInt(document.getElementById('sim13_a').value) || 1;
            const b = parseInt(document.getElementById('sim13_b').value) || 1;
            const out = document.getElementById('sim13_output');
            if (!out) return;

            const exprVal = Math.pow(a, 4) + 4 * Math.pow(b, 4);
            const f1 = a*a + 2*b*b - 2*a*b;
            const f2 = a*a + 2*b*b + 2*a*b;

            out.innerHTML = `
                <div class="text-indigo-300 font-bold">${a}⁴ + 4(${b})⁴ = ${exprVal}</div>
                <div>Factor 1: (a² - 2ab + 2b²) = ${a*a} - ${2*a*b} + ${2*b*b} = ${f1}</div>
                <div>Factor 2: (a² + 2ab + 2b²) = ${a*a} + ${2*a*b} + ${2*b*b} = ${f2}</div>
                <div class="text-emerald-400 font-bold">${f1} × ${f2} = ${f1 * f2} (Exact Match!)</div>
            `;
        }

        // Sim 14: Excluded Value Scanner
        function scanSim14(type) {
            const disp = document.getElementById('sim14_display');
            if (!disp) return;

            if (type === 'x2-4') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Expression: 1 / (x² - 4)</div>
                    <div>Denominator: x² - 4 = 0 ⟹ (x - 2)(x + 2) = 0</div>
                    <div class="text-rose-400 font-bold">Excluded Values: x = 2, x = -2</div>
                    <div class="text-emerald-400">Domain: All Real Numbers ℝ except {-2, 2}</div>
                `;
            } else if (type === 'x2-5x+6') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Expression: (x + 1) / (x² - 5x + 6)</div>
                    <div>Denominator: x² - 5x + 6 = 0 ⟹ (x - 2)(x - 3) = 0</div>
                    <div class="text-rose-400 font-bold">Excluded Values: x = 2, x = 3</div>
                    <div class="text-emerald-400">Domain: ℝ \\ {2, 3}</div>
                `;
            } else if (type === '2x+1') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">Expression: 5 / (2x - 8)</div>
                    <div>Denominator: 2x - 8 = 0 ⟹ 2x = 8 ⟹ x = 4</div>
                    <div class="text-rose-400 font-bold">Excluded Value: x = 4</div>
                    <div class="text-emerald-400">Domain: ℝ \\ {4}</div>
                `;
            }
        }

        // Sim 15: Rational Simplifier
        function reduceSim15(type) {
            const disp = document.getElementById('sim15_display');
            if (!disp) return;

            if (type === 'diff_sq') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">(x² - 16) / (x² + x - 12)</div>
                    <div>= [(x - 4)(x + 4)] / [(x + 4)(x - 3)]</div>
                    <div class="text-rose-400 line-through">Cancel common factor (x + 4)</div>
                    <div class="text-emerald-400 font-bold text-sm">= (x - 4) / (x - 3)</div>
                    <div class="text-[10px] text-slate-400">Valid for x ≠ 3, -4</div>
                `;
            } else if (type === 'cubic') {
                disp.innerHTML = `
                    <div class="text-amber-300 font-bold">(x³ - 8) / (x² - 4)</div>
                    <div>= [(x - 2)(x² + 2x + 4)] / [(x - 2)(x + 2)]</div>
                    <div class="text-rose-400 line-through">Cancel common factor (x - 2)</div>
                    <div class="text-emerald-400 font-bold text-sm">= (x² + 2x + 4) / (x + 2)</div>
                    <div class="text-[10px] text-slate-400">Valid for x ≠ ±2</div>
                `;
            }
        }

        // Sim 16: Computational AST
        let sim16Step = 1;
        function stepSim16() {
            sim16Step = (sim16Step % 3) + 1;
            drawSim16();
        }

        function drawSim16() {
            const svg = document.getElementById('sim16_svg');
            const status = document.getElementById('sim16_status');
            if (!svg) return;

            if (sim16Step === 1) {
                status.textContent = "Stage 1: Parsed into Abstract Syntax Tree (AST)";
                svg.innerHTML = `
                    <circle cx="130" cy="25" r="14" fill="#6366f1"/>
                    <text x="130" y="29" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">÷</text>
                    <line x1="130" y1="39" x2="70" y2="70" stroke="#475569" stroke-width="2"/>
                    <line x1="130" y1="39" x2="190" y2="70" stroke="#475569" stroke-width="2"/>
                    <circle cx="70" cy="80" r="14" fill="#0ea5e9"/><text x="70" y="84" fill="#fff" font-size="9" text-anchor="middle">x²-9</text>
                    <circle cx="190" cy="80" r="14" fill="#0ea5e9"/><text x="190" y="84" fill="#fff" font-size="9" text-anchor="middle">x+3</text>
                `;
            } else if (sim16Step === 2) {
                status.textContent = "Stage 2: Pattern Matcher factors numerator into (x-3)(x+3)";
                svg.innerHTML = `
                    <circle cx="130" cy="25" r="14" fill="#6366f1"/><text x="130" y="29" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">÷</text>
                    <line x1="130" y1="39" x2="70" y2="70" stroke="#475569" stroke-width="2"/>
                    <line x1="130" y1="39" x2="190" y2="70" stroke="#475569" stroke-width="2"/>
                    <circle cx="70" cy="80" r="14" fill="#10b981"/><text x="70" y="84" fill="#fff" font-size="8" text-anchor="middle">(x-3)(x+3)</text>
                    <circle cx="190" cy="80" r="14" fill="#10b981"/><text x="190" y="84" fill="#fff" font-size="9" text-anchor="middle">x+3</text>
                `;
            } else if (sim16Step === 3) {
                status.textContent = "Stage 3: Euclidean GCD Algorithm cancels common (x+3) ⟹ Result: x - 3";
                svg.innerHTML = `
                    <rect x="70" y="45" width="120" height="50" rx="10" fill="#10b981"/>
                    <text x="130" y="75" fill="#0f172a" font-size="16" font-weight="bold" text-anchor="middle">x - 3</text>
                `;
            }
        }

        // Initialize on Load
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
