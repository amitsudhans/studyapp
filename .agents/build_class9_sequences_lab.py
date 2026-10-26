# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 3
UNIT: SEQUENCES AND PROGRESSIONS (Competencies CG-11, C-8.1, CG-9)
Generates public/animations/class9-sequences-progressions.html
"""

import json
import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from class9_sequences_data import SLIDES_DATA, QUIZ_SLIDES

OUTPUT_PATH = "public/animations/class9-sequences-progressions.html"

def generate_html():
    slides_json = json.dumps(SLIDES_DATA)
    quizzes_json = json.dumps(QUIZ_SLIDES)

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Mathematics • Chapter 3 • Sequences and Progressions Lab</title>
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
                    <i data-lucide="sparkles" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">Class 9 Maths • Chapter 3</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 font-semibold">Concept 1</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Sequences & Progressions Lab</h1>
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
                        <!-- Background Glow -->
                        <circle cx="50" cy="50" r="45" fill="#1e1b4b"/>
                        <!-- Teacher Body / Shoulders -->
                        <path d="M 20 95 C 20 75, 80 75, 80 95 Z" fill="#4338ca"/>
                        <path d="M 38 78 L 50 90 L 62 78 Z" fill="#e0e7ff"/>
                        <path d="M 48 84 L 52 84 L 50 92 Z" fill="#fbbf24"/>
                        <!-- Head / Neck -->
                        <rect x="44" y="60" width="12" height="15" fill="#fcd34d" rx="4"/>
                        <ellipse cx="50" cy="46" rx="24" ry="26" fill="#fde68a"/>
                        <!-- Hair -->
                        <path d="M 24 45 C 24 20, 76 20, 76 45 C 76 30, 70 24, 50 24 C 30 24, 24 30, 24 45 Z" fill="#312e81"/>
                        <path d="M 24 45 C 20 60, 22 70, 26 75 C 24 65, 27 50, 30 45 Z" fill="#312e81"/>
                        <path d="M 76 45 C 80 60, 78 70, 74 75 C 76 65, 73 50, 70 45 Z" fill="#312e81"/>
                        <!-- Eyes & Glasses -->
                        <circle cx="41" cy="44" r="5" fill="#1e293b"/>
                        <circle cx="59" cy="44" r="5" fill="#1e293b"/>
                        <circle cx="42" cy="43" r="1.5" fill="#ffffff"/>
                        <circle cx="60" cy="43" r="1.5" fill="#ffffff"/>
                        <!-- Modern Glasses Frame -->
                        <rect x="33" y="38" width="16" height="12" rx="3" fill="none" stroke="#6366f1" stroke-width="2"/>
                        <rect x="51" y="38" width="16" height="12" rx="3" fill="none" stroke="#6366f1" stroke-width="2"/>
                        <line x1="49" y1="44" x2="51" y2="44" stroke="#6366f1" stroke-width="2"/>
                        <!-- Nose -->
                        <path d="M 50 48 L 48 53 L 52 53" fill="none" stroke="#d97706" stroke-width="1.5" stroke-linecap="round"/>
                        <!-- Mouth (Animated when speaking) -->
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
                        Teacher's Direct Voiceover Explanation
                    </span>
                    <span class="text-[11px] text-slate-400 hidden sm:inline">Web Speech & Web Audio Synthesizer</span>
                </div>
                <p id="teacherSpeechText" class="text-sm text-slate-200 leading-relaxed font-normal italic">
                    Welcome to Sequences and Progressions! Let us explore patterns, formulas, AP, GP, and computational puzzles.
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
                // Standard Curriculum Slide
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
                // Dedicated Quiz Slide (17-20)
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
                                <div class="text-emerald-400 font-bold text-base mb-1">🎉 Congratulations! You have completed Chapter 3!</div>
                                <div class="text-slate-300 text-xs">You have reached the last slide of this chapter. You have mastered sequences, explicit & recursive rules, Arithmetic Progressions, Geometric Progressions, fractals, and computational algorithms!</div>
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
                    '<span class="text-emerald-400 font-bold">✓ Correct Answer!</span> Excellent reasoning.' :
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

        // Key listeners (ArrowLeft, ArrowRight)
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
            if (e.key === 'Escape') closeSolutionModal();
        });

        // --- SIMULATORS 1 TO 16 LOGIC ---

        function initSlideSimulator(sNum) {
            if (sNum === 1) setSim1Pattern('odds');
            else if (sNum === 2) updateSim2();
            else if (sNum === 3) setSim3Rule('ap');
            else if (sNum === 4) runSim4Race(10);
            else if (sNum === 5) scanSim5([3, 7, 11, 15, 19]);
            else if (sNum === 6) updateSim6();
            else if (sNum === 7) drawSim7();
            else if (sNum === 8) drawSim8();
            else if (sNum === 9) drawSim9();
            else if (sNum === 10) scanSim10([2, 6, 18, 54, 162]);
            else if (sNum === 11) updateSim11();
            else if (sNum === 12) resetSim12();
            else if (sNum === 13) runSim13();
            else if (sNum === 14) setSim14Type('koch');
            else if (sNum === 15) initSim15();
            else if (sNum === 16) runSim16Classifier();
        }

        // Sim 1: Sequence Generator
        let sim1Pattern = 'odds';
        function setSim1Pattern(type) {
            sim1Pattern = type;
            const display = document.getElementById('sim1_display');
            const rule = document.getElementById('sim1_rule');
            const next = document.getElementById('sim1_next');
            if (!display) return;

            let terms = [];
            let rText = "";
            let nextVal = 0;

            if (type === 'odds') {
                rText = "$a_n = 2n - 1$";
                for (let n = 1; n <= 8; n++) terms.push(2*n - 1);
                nextVal = 2*9 - 1;
            } else if (type === 'evens') {
                rText = "$a_n = 2n$";
                for (let n = 1; n <= 8; n++) terms.push(2*n);
                nextVal = 2*9;
            } else if (type === 'squares') {
                rText = "$a_n = n^2$";
                for (let n = 1; n <= 8; n++) terms.push(n*n);
                nextVal = 9*9;
            } else if (type === 'triangular') {
                rText = "$a_n = \\frac{n(n+1)}{2}$";
                for (let n = 1; n <= 8; n++) terms.push((n*(n+1))/2);
                nextVal = (9*10)/2;
            }

            display.innerHTML = terms.map((t, idx) => `
                <div class="flex flex-col items-center">
                    <span class="text-[9px] text-slate-500 font-mono">a_${idx+1}</span>
                    <div class="w-8 h-8 rounded-lg bg-indigo-900/60 border border-indigo-500/40 flex items-center justify-center font-mono font-bold text-xs text-indigo-200">
                        ${t}
                    </div>
                </div>
            `).join('<span class="text-slate-600 font-bold">,</span>');

            rule.innerHTML = rText;
            next.textContent = nextVal;
            if (window.renderMathInElement) renderMathInElement(rule);
        }

        // Sim 2: Explicit Evaluator
        function updateSim2() {
            const fEl = document.getElementById('sim2_formula');
            const nEl = document.getElementById('sim2_n');
            const nVal = document.getElementById('sim2_n_val');
            const step = document.getElementById('sim2_step');
            const res = document.getElementById('sim2_result');
            const table = document.getElementById('sim2_terms_table');
            if (!fEl || !nEl) return;

            const n = parseInt(nEl.value);
            nVal.textContent = n;
            const formula = fEl.value;
            let result = 0;
            let stepText = "";

            if (formula === '3n-1') {
                result = 3*n - 1;
                stepText = `a_${n} = 3(${n}) - 1 = ${3*n} - 1`;
            } else if (formula === 'n2+1') {
                result = n*n + 1;
                stepText = `a_${n} = ${n}² + 1 = ${n*n} + 1`;
            } else if (formula === '2^n') {
                result = Math.pow(2, n);
                stepText = `a_${n} = 2^${n}`;
            } else if (formula === 'frac') {
                result = (n / (n + 1)).toFixed(3);
                stepText = `a_${n} = ${n} / (${n} + 1) = ${n}/${n+1}`;
            }

            step.textContent = stepText;
            res.textContent = result;

            if (table) {
                let preview = [];
                for (let k = 1; k <= 5; k++) {
                    let val = formula === '3n-1' ? 3*k - 1 : (formula === 'n2+1' ? k*k+1 : (formula === '2^n' ? Math.pow(2, k) : (k/(k+1)).toFixed(2)));
                    preview.push(`<div class="p-1 rounded bg-slate-900 border border-slate-800"><span class="text-slate-500">a_${k}:</span> <span class="font-bold text-amber-300">${val}</span></div>`);
                }
                table.innerHTML = preview.join('');
            }
        }

        // Sim 3: Recursive Stepper
        let sim3Type = 'ap';
        let sim3Terms = [2];
        function setSim3Rule(type) {
            sim3Type = type;
            if (type === 'ap') sim3Terms = [4];
            else if (type === 'gp') sim3Terms = [3];
            else if (type === 'fib') sim3Terms = [1, 1];
            updateSim3Display();
        }

        function stepSim3() {
            const n = sim3Terms.length;
            if (n >= 8) return;
            if (sim3Type === 'ap') {
                const nextVal = sim3Terms[n - 1] + 3;
                sim3Terms.push(nextVal);
            } else if (sim3Type === 'gp') {
                const nextVal = sim3Terms[n - 1] * 2;
                sim3Terms.push(nextVal);
            } else if (sim3Type === 'fib') {
                const nextVal = sim3Terms[n - 1] + sim3Terms[n - 2];
                sim3Terms.push(nextVal);
            }
            playTone(440 + n * 40, 'sine', 0.1);
            updateSim3Display();
        }

        function resetSim3() {
            setSim3Rule(sim3Type);
        }

        function updateSim3Display() {
            const box = document.getElementById('sim3_callstack');
            if (!box) return;
            box.innerHTML = sim3Terms.map((t, idx) => `
                <div class="flex items-center justify-between text-xs py-0.5 border-b border-slate-900">
                    <span class="text-indigo-400 font-bold">a_${idx + 1}</span>
                    <span class="text-slate-400">${idx === 0 ? 'Base seed value' : (sim3Type === 'ap' ? `a_${idx} + 3` : (sim3Type === 'gp' ? `2 × a_${idx}` : `a_${idx} + a_${idx-1}`))}</span>
                    <span class="text-emerald-400 font-bold font-mono">${t}</span>
                </div>
            `).join('');
        }

        // Sim 4: Complexity Race
        function runSim4Race(n) {
            const target = document.getElementById('sim4_target');
            const expSteps = document.getElementById('sim4_exp_steps');
            const expBar = document.getElementById('sim4_exp_bar');
            const recSteps = document.getElementById('sim4_rec_steps');
            const recBar = document.getElementById('sim4_rec_bar');
            const summary = document.getElementById('sim4_summary');
            if (!target) return;

            target.textContent = `a_${n}`;
            expSteps.textContent = `1 direct formula evaluation`;
            expBar.style.width = `10%`;
            recSteps.textContent = `${n} sequential recursive steps`;
            recBar.style.width = `${Math.min(100, n)}%`;

            const ans = 4*n + 1;
            summary.innerHTML = `Computed <span class="text-amber-300 font-mono">a_${n} = ${ans}</span>. Explicit took 1 instant calculation; recursion had to evaluate all ${n} ancestors!`;
        }

        // Sim 5: AP Common Difference Scanner
        function scanSim5(arr) {
            const disp = document.getElementById('sim5_display');
            const verd = document.getElementById('sim5_verdict');
            if (!disp) return;

            let diffs = [];
            for (let i = 0; i < arr.length - 1; i++) {
                diffs.push(arr[i + 1] - arr[i]);
            }
            const isAP = diffs.every(d => d === diffs[0]);

            disp.innerHTML = `
                <div class="flex items-center gap-2 mb-2 font-mono text-sm text-amber-300">
                    ${arr.join(' , ')}
                </div>
                <div class="flex items-center gap-4 text-xs font-mono text-cyan-300">
                    ${diffs.map((d, i) => `<span>Δ_${i+1} = ${d}</span>`).join('')}
                </div>
            `;

            if (isAP) {
                verd.innerHTML = `<span class="text-emerald-400">✓ Verified Arithmetic Progression (AP) with common difference d = ${diffs[0]}</span>`;
            } else {
                verd.innerHTML = `<span class="text-rose-400">✗ Not an AP! Consecutive differences are varying (${diffs.join(', ')}).</span>`;
            }
        }

        // Sim 6: AP n-th Term Sandbox
        function updateSim6() {
            const a = parseFloat(document.getElementById('sim6_a').value) || 0;
            const d = parseFloat(document.getElementById('sim6_d').value) || 0;
            const n = parseInt(document.getElementById('sim6_n').value) || 1;
            const bd = document.getElementById('sim6_breakdown');
            const ans = document.getElementById('sim6_ans');
            const line = document.getElementById('sim6_visual_line');
            if (!bd) return;

            const res = a + (n - 1) * d;
            bd.textContent = `a_${n} = ${a} + (${n} - 1) × ${d} = ${a} + ${n - 1} × ${d}`;
            ans.textContent = res;

            let blocks = [];
            for (let i = 1; i <= Math.min(6, n); i++) {
                let val = a + (i - 1) * d;
                blocks.push(`
                    <div class="flex flex-col items-center">
                        <span class="text-[9px] text-slate-500 font-mono">n=${i}</span>
                        <div class="px-2 py-1 bg-indigo-900/50 border border-indigo-500/40 rounded text-xs font-mono font-bold text-indigo-300">${val}</div>
                    </div>
                `);
            }
            if (n > 6) {
                blocks.push(`<span class="text-slate-500">...</span>`);
                blocks.push(`
                    <div class="flex flex-col items-center">
                        <span class="text-[9px] text-emerald-500 font-mono">n=${n}</span>
                        <div class="px-2 py-1 bg-emerald-900/50 border border-emerald-500/40 rounded text-xs font-mono font-bold text-emerald-300">${res}</div>
                    </div>
                `);
            }
            line.innerHTML = blocks.join('');
        }

        // Sim 7: AP Cartesian Plotter
        function drawSim7() {
            const d = parseFloat(document.getElementById('sim7_d').value);
            document.getElementById('sim7_d_val').textContent = d;
            const svg = document.getElementById('sim7_svg');
            if (!svg) return;

            const a = 2; // base
            let pts = [];
            let circles = [];
            for (let n = 1; n <= 6; n++) {
                const val = a + (n - 1) * d;
                const cx = 40 + (n - 1) * 45;
                const cy = 150 - (val * 10);
                pts.push(`${cx},${cy}`);
                circles.push(`<circle cx="${cx}" cy="${cy}" r="4.5" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>`);
                circles.push(`<text x="${cx}" y="${cy - 8}" fill="#facc15" font-size="9" text-anchor="middle" font-family="monospace">(${n},${val})</text>`);
            }

            svg.innerHTML = `
                <!-- Grid Lines -->
                <line x1="30" y1="160" x2="300" y2="160" stroke="#334155" stroke-width="1.5"/>
                <line x1="30" y1="20" x2="30" y2="160" stroke="#334155" stroke-width="1.5"/>
                <text x="295" y="175" fill="#94a3b8" font-size="10">n</text>
                <text x="15" y="25" fill="#94a3b8" font-size="10">a_n</text>
                <!-- Guideline line -->
                <polyline points="${pts.join(' ')}" fill="none" stroke="#6366f1" stroke-dasharray="4,4" stroke-width="1.5"/>
                ${circles.join('')}
            `;
        }

        // Sim 8: Stadium Seating
        function drawSim8() {
            const a = parseInt(document.getElementById('sim8_a').value) || 20;
            const d = parseInt(document.getElementById('sim8_d').value) || 4;
            const svg = document.getElementById('sim8_svg');
            const info = document.getElementById('sim8_info');
            if (!svg) return;

            let arcs = [];
            for (let r = 1; r <= 5; r++) {
                const seats = a + (r - 1) * d;
                const radius = 30 + r * 18;
                arcs.push(`
                    <path d="M ${150 - radius} 140 A ${radius} ${radius} 0 0 1 ${150 + radius} 140" fill="none" stroke="#4f46e5" stroke-width="5" stroke-linecap="round"/>
                    <text x="${150 + radius + 10}" y="143" fill="#cbd5e1" font-size="9" font-family="monospace">R${r}: ${seats}</text>
                `);
            }

            svg.innerHTML = `
                <circle cx="150" cy="140" r="14" fill="#10b981"/>
                <text x="150" y="143" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">Stage</text>
                ${arcs.join('')}
            `;

            info.textContent = `Row 1: ${a} seats | Row 5: ${a + 4*d} seats | Total (5 rows): ${5*a + 10*d} seats`;
        }

        // Sim 9: Gauss Staircase Doubler
        let sim9Doubled = false;
        function toggleSim9Double() {
            sim9Doubled = !sim9Doubled;
            drawSim9();
        }

        function drawSim9() {
            const n = parseInt(document.getElementById('sim9_n').value);
            document.getElementById('sim9_n_val').textContent = n;
            const svg = document.getElementById('sim9_svg');
            const calc = document.getElementById('sim9_calc');
            if (!svg) return;

            const sum = (n * (n + 1)) / 2;
            calc.textContent = `S_${n} = ${n}(${n+1})/2 = ${sum} dots`;

            const rSize = 12;
            const gap = 3;
            let dots = [];

            // Primary Staircase
            for (let row = 0; row < n; row++) {
                for (let col = 0; col <= row; col++) {
                    const x = 30 + col * (rSize + gap);
                    const y = 30 + row * (rSize + gap);
                    dots.push(`<circle cx="${x}" cy="${y}" r="${rSize/2}" fill="#6366f1"/>`);
                }
            }

            // Second Inverted Staircase if toggled
            if (sim9Doubled) {
                for (let row = 0; row < n; row++) {
                    for (let col = row + 1; col < n + 1; col++) {
                        const x = 30 + col * (rSize + gap);
                        const y = 30 + row * (rSize + gap);
                        dots.push(`<circle cx="${x}" cy="${y}" r="${rSize/2}" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>`);
                    }
                }
            }

            svg.innerHTML = `
                ${dots.join('')}
                <text x="160" y="20" fill="#94a3b8" font-size="10" font-family="monospace">
                    ${sim9Doubled ? `Rectangle: ${n} rows × ${n+1} cols = ${n*(n+1)} dots` : 'Single Triangle Staircase'}
                </text>
            `;
        }

        // Sim 10: GP Common Ratio Scanner
        function scanSim10(arr) {
            const disp = document.getElementById('sim10_display');
            const verd = document.getElementById('sim10_verdict');
            if (!disp) return;

            let ratios = [];
            for (let i = 0; i < arr.length - 1; i++) {
                ratios.push((arr[i + 1] / arr[i]).toFixed(2));
            }
            const isGP = ratios.every(r => r === ratios[0]);

            disp.innerHTML = `
                <div class="flex items-center gap-2 mb-2 font-mono text-sm text-amber-300">
                    ${arr.join(' , ')}
                </div>
                <div class="flex items-center gap-3 text-xs font-mono text-cyan-300">
                    ${ratios.map((r, i) => `<span>r_${i+1} = ${r}</span>`).join('')}
                </div>
            `;

            if (isGP) {
                verd.innerHTML = `<span class="text-emerald-400">✓ Verified Geometric Progression (GP) with common ratio r = ${ratios[0]}</span>`;
            } else {
                verd.innerHTML = `<span class="text-rose-400">✗ Not a GP! Consecutive ratios are varying (${ratios.join(', ')}).</span>`;
            }
        }

        // Sim 11: GP n-th Term Sandbox
        function updateSim11() {
            const a = parseFloat(document.getElementById('sim11_a').value) || 1;
            const r = parseFloat(document.getElementById('sim11_r').value) || 1;
            const n = parseInt(document.getElementById('sim11_n').value) || 1;
            const bd = document.getElementById('sim11_breakdown');
            const ans = document.getElementById('sim11_ans');
            const bars = document.getElementById('sim11_visual_bars');
            if (!bd) return;

            const res = a * Math.pow(r, n - 1);
            bd.textContent = `a_${n} = ${a} × (${r})^(${n} - 1) = ${a} × ${Math.pow(r, n-1).toFixed(2)}`;
            ans.textContent = res.toLocaleString();

            let barElements = [];
            for (let i = 1; i <= Math.min(6, n); i++) {
                let val = a * Math.pow(r, i - 1);
                let height = Math.min(90, Math.max(10, Math.log2(Math.abs(val) + 1) * 12));
                barElements.push(`
                    <div class="flex flex-col items-center">
                        <span class="text-[9px] text-slate-400 font-mono">${val > 999 ? val.toExponential(1) : val.toFixed(0)}</span>
                        <div class="w-6 bg-gradient-to-t from-violet-700 to-indigo-500 rounded-t" style="height: ${height}px;"></div>
                        <span class="text-[9px] text-slate-500 font-mono">n=${i}</span>
                    </div>
                `);
            }
            bars.innerHTML = barElements.join('');
        }

        // Sim 12: Growth Battle
        let sim12Step = 1;
        function stepSim12() {
            if (sim12Step < 9) sim12Step++;
            renderSim12();
        }
        function resetSim12() {
            sim12Step = 1;
            renderSim12();
        }
        function renderSim12() {
            const svg = document.getElementById('sim12_svg');
            const nVal = document.getElementById('sim12_n_val');
            const status = document.getElementById('sim12_status');
            if (!svg) return;

            nVal.textContent = sim12Step;
            const apVal = 20 + (sim12Step - 1) * 10;
            const gpVal = 2 * Math.pow(2, sim12Step - 1);

            const apW = Math.min(220, apVal * 1.5);
            const gpW = Math.min(220, gpVal * 0.8);

            svg.innerHTML = `
                <!-- AP Bar -->
                <text x="15" y="45" fill="#38bdf8" font-size="11" font-family="monospace">AP (Linear)</text>
                <rect x="15" y="55" width="${apW}" height="22" rx="4" fill="#0284c7"/>
                <text x="${Math.max(30, apW + 25)}" y="70" fill="#38bdf8" font-size="11" font-weight="bold" font-family="monospace">${apVal}</text>

                <!-- GP Bar -->
                <text x="15" y="105" fill="#fbbf24" font-size="11" font-family="monospace">GP (Exponential)</text>
                <rect x="15" y="115" width="${gpW}" height="22" rx="4" fill="#d97706"/>
                <text x="${Math.max(30, gpW + 25)}" y="130" fill="#fbbf24" font-size="11" font-weight="bold" font-family="monospace">${gpVal}</text>
            `;

            if (gpVal > apVal) {
                status.innerHTML = `<span class="text-amber-400 font-bold">★ GP has overtaken AP! (${gpVal} vs ${apVal})</span>`;
            } else {
                status.innerHTML = `<span class="text-cyan-400 font-bold">AP currently leads (${apVal} vs ${gpVal})</span>`;
            }
        }

        // Sim 13: Bouncing Ball
        function runSim13() {
            const r = parseFloat(document.getElementById('sim13_r').value);
            document.getElementById('sim13_r_val').textContent = r;
            const svg = document.getElementById('sim13_svg');
            const tbl = document.getElementById('sim13_table');
            if (!svg) return;

            let paths = [];
            let heights = [100];
            let x = 30;

            for (let b = 1; b <= 4; b++) {
                const h = heights[b - 1] * r;
                heights.push(h);
                const nextX = x + 60;
                const peakY = 130 - h * 1.1;
                paths.push(`<path d="M ${x} 130 Q ${(x + nextX)/2} ${peakY}, ${nextX} 130" fill="none" stroke="#f59e0b" stroke-width="2.5"/>`);
                paths.push(`<circle cx="${(x + nextX)/2}" cy="${peakY}" r="4" fill="#ef4444"/>`);
                paths.push(`<text x="${(x + nextX)/2}" y="${peakY - 6}" fill="#fde68a" font-size="8" text-anchor="middle" font-family="monospace">${h.toFixed(1)}cm</text>`);
                x = nextX;
            }

            svg.innerHTML = `
                <line x1="20" y1="130" x2="280" y2="130" stroke="#475569" stroke-width="2"/>
                ${paths.join('')}
            `;

            tbl.innerHTML = `Bounce Heights: 100cm → ${heights.slice(1).map(h => h.toFixed(1) + 'cm').join(' → ')}`;
        }

        // Sim 14: Fractal Explorer
        let sim14Type = 'koch';
        let sim14Iter = 0;
        function setSim14Type(type) {
            sim14Type = type;
            sim14Iter = 0;
            renderSim14();
        }
        function stepSim14() {
            sim14Iter = (sim14Iter + 1) % 4;
            renderSim14();
        }
        function renderSim14() {
            const svg = document.getElementById('sim14_svg');
            const iterVal = document.getElementById('sim14_iter_val');
            const stats = document.getElementById('sim14_stats');
            if (!svg) return;

            iterVal.textContent = sim14Iter;

            if (sim14Type === 'koch') {
                const segs = 3 * Math.pow(4, sim14Iter);
                stats.textContent = `Segments: ${segs} | Perimeter: 3s × (4/3)^${sim14Iter} = ${(3 * Math.pow(4/3, sim14Iter)).toFixed(2)}s`;
                // Render stylized snowflake triangle with spikes
                let r = 70;
                let paths = [];
                for (let i = 0; i < 3; i++) {
                    let angle = (i * 120 - 90) * Math.PI / 180;
                    let nextAngle = ((i + 1) * 120 - 90) * Math.PI / 180;
                    let x1 = 130 + r * Math.cos(angle);
                    let y1 = 105 + r * Math.sin(angle);
                    let x2 = 130 + r * Math.cos(nextAngle);
                    let y2 = 105 + r * Math.sin(nextAngle);

                    if (sim14Iter === 0) {
                        paths.push(`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#38bdf8" stroke-width="2"/>`);
                    } else {
                        // Simulated sub-spikes
                        let mx = (x1 + x2) / 2 + 10 * sim14Iter * Math.cos(angle + Math.PI/3);
                        let my = (y1 + y2) / 2 + 10 * sim14Iter * Math.sin(angle + Math.PI/3);
                        paths.push(`<polyline points="${x1},${y1} ${mx},${my} ${x2},${y2}" stroke="#38bdf8" stroke-width="1.5" fill="none"/>`);
                    }
                }
                svg.innerHTML = paths.join('');
            } else {
                const areaRatio = Math.pow(3/4, sim14Iter);
                stats.textContent = `Triangles: ${Math.pow(3, sim14Iter)} | Remaining Area: (3/4)^${sim14Iter} = ${(areaRatio * 100).toFixed(1)}%`;
                svg.innerHTML = `
                    <polygon points="130,25 50,175 210,175" fill="#4338ca"/>
                    ${sim14Iter >= 1 ? '<polygon points="130,175 90,100 170,100" fill="#020617"/>' : ''}
                    ${sim14Iter >= 2 ? '<polygon points="90,175 70,138 110,138" fill="#020617"/><polygon points="170,175 150,138 190,138" fill="#020617"/><polygon points="130,100 110,63 150,63" fill="#020617"/>' : ''}
                `;
            }
        }

        // Sim 15: Tower of Hanoi
        let hanoiDisks = 3;
        let hanoiMoves = 0;
        let hanoiState = [[], [], []];
        function initSim15() {
            hanoiDisks = parseInt(document.getElementById('sim15_disks').value) || 3;
            hanoiMoves = 0;
            hanoiState = [[], [], []];
            for (let i = hanoiDisks; i >= 1; i--) hanoiState[0].push(i);
            document.getElementById('sim15_moves').textContent = 0;
            document.getElementById('sim15_min').textContent = Math.pow(2, hanoiDisks) - 1;
            document.getElementById('sim15_status').textContent = "Ready";
            renderSim15();
        }

        function autoSolveSim15() {
            hanoiMoves++;
            document.getElementById('sim15_moves').textContent = hanoiMoves;
            document.getElementById('sim15_status').textContent = `Solving recursively (Step ${hanoiMoves})`;
            playTone(500 + hanoiMoves * 30, 'sine', 0.1);
            // Simulated state shift
            if (hanoiMoves >= Math.pow(2, hanoiDisks) - 1) {
                hanoiState = [[], [], []];
                for (let i = hanoiDisks; i >= 1; i--) hanoiState[2].push(i);
                document.getElementById('sim15_status').textContent = "Solved in minimal moves!";
            }
            renderSim15();
        }

        function renderSim15() {
            const svg = document.getElementById('sim15_svg');
            if (!svg) return;

            const pegX = [60, 150, 240];
            let elements = [
                '<line x1="20" y1="120" x2="280" y2="120" stroke="#475569" stroke-width="4"/>'
            ];

            // 3 Pegs
            pegX.forEach((px, idx) => {
                elements.push(`<line x1="${px}" y1="30" x2="${px}" y2="120" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>`);
                elements.push(`<text x="${px}" y="128" fill="#94a3b8" font-size="9" text-anchor="middle">Peg ${String.fromCharCode(65 + idx)}</text>`);
            });

            // Disks
            hanoiState.forEach((peg, pIdx) => {
                peg.forEach((diskSize, dIdx) => {
                    const w = 20 + diskSize * 16;
                    const h = 10;
                    const x = pegX[pIdx] - w / 2;
                    const y = 116 - dIdx * 12;
                    const color = diskSize === 1 ? '#38bdf8' : (diskSize === 2 ? '#818cf8' : (diskSize === 3 ? '#a855f7' : '#f59e0b'));
                    elements.push(`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="3" fill="${color}"/>`);
                });
            });

            svg.innerHTML = elements.join('');
        }

        // Sim 16: Computational Thinking Pipeline
        function runSim16Classifier() {
            const input = document.getElementById('sim16_input').value;
            const output = document.getElementById('sim16_output');
            if (!output) return;

            const nums = input.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
            if (nums.length < 3) {
                output.innerHTML = `<span class="text-rose-400">Please enter at least 3 numbers.</span>`;
                return;
            }

            let diffs = [];
            let ratios = [];
            for (let i = 0; i < nums.length - 1; i++) {
                diffs.push(nums[i + 1] - nums[i]);
                ratios.push((nums[i + 1] / nums[i]).toFixed(2));
            }

            const isAP = diffs.every(d => Math.abs(d - diffs[0]) < 0.001);
            const isGP = ratios.every(r => Math.abs(r - ratios[0]) < 0.001);

            let res = `<div class="text-indigo-300 font-bold">Pipeline Analysis:</div>`;
            res += `<div>• Input Series: [${nums.join(', ')}]</div>`;
            res += `<div>• Differences Δ: [${diffs.join(', ')}]</div>`;
            res += `<div>• Quotients r: [${ratios.join(', ')}]</div>`;

            if (isAP) {
                res += `<div class="text-emerald-400 font-bold mt-1">✓ Classified as: Arithmetic Progression (AP)</div>`;
                res += `<div class="text-amber-300">Rule: a_n = ${nums[0]} + (n - 1) × ${diffs[0]}</div>`;
            } else if (isGP) {
                res += `<div class="text-emerald-400 font-bold mt-1">✓ Classified as: Geometric Progression (GP)</div>`;
                res += `<div class="text-amber-300">Rule: a_n = ${nums[0]} × (${ratios[0]})^(n - 1)</div>`;
            } else {
                res += `<div class="text-cyan-400 font-bold mt-1">✓ Classified as: Non-Linear / General Sequence</div>`;
            }
            output.innerHTML = res;
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
