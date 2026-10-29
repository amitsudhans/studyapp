# -*- coding: utf-8 -*-
"""
Master compiler script for Class 7 Science Chapter 2: Acids, Bases, and Salts (Exploring Substances)
Generates public/animations/class7-science-exploring-substances.html
"""

import sys
import json
sys.path.insert(0, ".agents")

from class7_science_substances_data import SLIDES_DATA
from class7_science_substances_sims import SIMULATORS_HTML
from class7_science_substances_js import SIMULATORS_JS

html_template = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Science • Chapter 2: Acids, Bases, and Salts Master Lab</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#fdf4ff',
              100: '#fae8ff',
              500: '#d946ef',
              600: '#c026d3',
              700: '#a21caf',
              900: '#701a75',
              950: '#4a044e'
            }
          }
        }
      }
    }
  </script>

  <!-- KaTeX for High-Fidelity Math & Chemical Formula Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="if (window.renderAllMath) window.renderAllMath();"></script>

  <style>
    /* Custom Scrollbars */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0f172a; }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #475569; }

    .slide-transition {
      transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .modal-backdrop {
      background-color: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans antialiased select-none">

  <!-- TOP APP BAR -->
  <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-40 px-4 py-2.5 flex items-center justify-between">
    <div class="flex items-center space-x-3">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-purple-500 to-amber-500 flex items-center justify-center shadow-lg shadow-purple-500/20 text-white font-bold text-lg">
        ⚗️
      </div>
      <div>
        <div class="text-xs font-bold text-amber-400 uppercase tracking-wider">NCERT Class 7 Science • Chapter 2</div>
        <h1 class="text-sm sm:text-base font-extrabold text-slate-100 flex items-center gap-2">
          <span>Acids, Bases, and Salts</span>
          <span class="text-[11px] px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30 font-semibold">Master Lab</span>
        </h1>
      </div>
    </div>

    <!-- Slide Index Navigation Controls -->
    <div class="flex items-center space-x-2">
      <button id="prevBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 transition active:scale-95 flex items-center gap-1 cursor-pointer">
        <span>◀</span> <span class="hidden sm:inline">Prev</span>
      </button>
      
      <div class="px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-800 text-xs font-mono font-bold text-amber-400">
        <span id="currentSlideDisplay">1</span> / <span id="totalSlidesDisplay">20</span>
      </div>

      <button id="nextBtn" class="px-3 py-1.5 rounded-lg bg-gradient-to-r from-purple-600 to-amber-600 hover:from-purple-500 hover:to-amber-500 text-xs font-bold text-white shadow-md shadow-purple-600/30 transition active:scale-95 flex items-center gap-1 cursor-pointer">
        <span class="hidden sm:inline">Next</span> <span>▶</span>
      </button>

      <!-- TOC Quick Drawer Toggle -->
      <button id="tocBtn" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition" title="Table of Contents">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/></svg>
      </button>
    </div>
  </header>

  <!-- TABLE OF CONTENTS OVERLAY -->
  <div id="tocModal" class="fixed inset-0 z-50 modal-backdrop hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="px-5 py-3.5 border-b border-slate-800 flex items-center justify-between">
        <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
          <span>📑</span> Table of Contents • Chapter 2: Acids, Bases, and Salts
        </h3>
        <button id="closeTocBtn" class="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">✕</button>
      </div>
      <div id="tocList" class="p-4 overflow-y-auto grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
        <!-- Injected via JS -->
      </div>
    </div>
  </div>

  <!-- MAIN VIEWPORT CONTAINER -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-5 flex flex-col">
    
    <!-- SLIDE WORKSPACE (DYNAMIC CONTAINER) -->
    <div id="slideContainer" class="flex-1 flex flex-col">
      <!-- Active slide rendered dynamically -->
    </div>

    <!-- TERMINAL SLIDE NOTICE (SLIDE 20 TERMINAL ENFORCEMENT) -->
    <div id="lastSlideNotice" class="hidden mt-4 p-4 rounded-2xl bg-gradient-to-r from-emerald-950/80 to-slate-900 border border-emerald-500/40 text-center shadow-xl">
      <div class="text-emerald-400 font-extrabold text-base mb-1 flex items-center justify-center gap-2">
        <span>🎉</span> You have reached the last slide of this chapter.
      </div>
      <p class="text-xs text-slate-300 max-w-xl mx-auto">
        Outstanding work! You have completed the study of acids, bases, natural indicators (litmus, red rose, turmeric, olfactory indicators), exothermic neutralisation reactions, titration dynamics, real-world neutralisation applications (ant bites, soil treatment, industrial wastewater, antacids, and oral hygiene), and the inspiring scientific legacy of Acharya Prafulla Chandra Ray!
      </p>
      <div class="mt-3 flex items-center justify-center gap-2">
        <button onclick="goToSlide(1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition">
          ↺ Review from Slide 1
        </button>
        <button onclick="openSolutionModal(0, 0)" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-600/30">
          View Master Solutions
        </button>
      </div>
    </div>
  </main>

  <!-- MENTOR AVATAR FLOATING DOCK -->
  <aside class="sticky bottom-0 z-30 bg-slate-900/90 border-t border-slate-800 px-4 py-2 flex items-center justify-between text-xs">
    <div class="flex items-center space-x-3">
      <div class="relative">
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-600 to-amber-600 flex items-center justify-center text-white font-bold text-sm shadow-md shadow-purple-600/30 ring-2 ring-purple-400/40">
          ⚗️
        </div>
        <span class="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 rounded-full bg-emerald-500 ring-2 ring-slate-950"></span>
      </div>
      <div>
        <div class="font-extrabold text-amber-300 flex items-center gap-1.5">
          <span>Acharya Prafulla Chandra Ray</span>
          <span class="text-[10px] text-slate-400 font-normal hidden sm:inline">• Father of Indian Chemistry & Founder of Bengal Chemicals</span>
        </div>
        <div id="mentorVoiceText" class="text-[11px] text-slate-300 line-clamp-1 italic">
          "Welcome to nature's chemical laboratory! Substances all around us speak in the language of acids, bases, and indicators. Let us explore with curiosity and safety."
        </div>
      </div>
    </div>
    
    <div class="flex items-center space-x-2">
      <button id="mentorSpeakBtn" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold flex items-center gap-1 transition" title="Speak mentor insight">
        <span>🔊</span> <span class="hidden sm:inline">Narrate</span>
      </button>
      <button id="soundToggleBtn" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition" title="Toggle Sound FX">
        🔔
      </button>
    </div>
  </aside>

  <!-- STEP-BY-STEP POP-UP SOLUTION MODAL -->
  <div id="solutionModal" style="display: none; z-index: 99999 !important;" class="fixed inset-0 modal-backdrop flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-purple-500/50 rounded-2xl w-full max-w-xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
      <div class="px-5 py-3.5 border-b border-slate-800 bg-slate-950/70 flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-amber-400 text-lg">💡</span>
          <h3 id="solutionModalTitle" class="font-extrabold text-amber-400 text-sm sm:text-base">
            Detailed Step-by-Step Derivation
          </h3>
        </div>
        <button id="closeSolutionModalBtn" class="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">✕</button>
      </div>
      <div class="p-5 overflow-y-auto text-xs sm:text-sm text-slate-200 space-y-3" id="solutionModalBody">
        <!-- Injected via openSolutionModal -->
      </div>
      <div class="px-5 py-3 border-t border-slate-800 bg-slate-950/70 flex justify-end">
        <button id="solutionOkBtn" class="px-4 py-1.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition shadow-md shadow-purple-600/30">
          Got It, Continue!
        </button>
      </div>
    </div>
  </div>

  <!-- SCRIPT ENGINE -->
  <script>
    // Injected slides data
    const SLIDES_DATA = """ + json.dumps(SLIDES_DATA) + r""";

    // Injected simulator templates
    const SIMULATORS_HTML = """ + json.dumps(SIMULATORS_HTML) + r""";

    // App state
    let currentSlide = 1;
    let soundEnabled = true;

    // Web Audio Synthesizer
    const audioCtx = (window.AudioContext || window.webkitAudioContext) ? new (window.AudioContext || window.webkitAudioContext)() : null;
    function playSfx(type) {
      if (!soundEnabled || !audioCtx) return;
      try {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        const t = audioCtx.currentTime;

        if (type === 'click') {
          osc.frequency.setValueAtTime(480, t);
          osc.frequency.exponentialRampToValueAtTime(800, t + 0.05);
          gain.gain.setValueAtTime(0.08, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.05);
          osc.start(t);
          osc.stop(t + 0.05);
        } else if (type === 'correct') {
          osc.frequency.setValueAtTime(523.25, t); // C5
          osc.frequency.setValueAtTime(659.25, t + 0.08); // E5
          osc.frequency.setValueAtTime(783.99, t + 0.16); // G5
          gain.gain.setValueAtTime(0.12, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
          osc.start(t);
          osc.stop(t + 0.35);
        } else if (type === 'incorrect') {
          osc.frequency.setValueAtTime(280, t);
          osc.frequency.linearRampToValueAtTime(180, t + 0.18);
          gain.gain.setValueAtTime(0.12, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.2);
          osc.start(t);
          osc.stop(t + 0.2);
        }
      } catch (err) { }
    }

    // Robust KaTeX Math Renderer with retry loop & MutationObserver
    function renderAllMath(targetEl) {
      const el = targetEl || document.body;
      if (window.renderMathInElement) {
        window.renderMathInElement(el, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false},
            {left: '\\[', right: '\\]', display: true},
            {left: '\\(', right: '\\)', display: false}
          ],
          throwOnError: false
        });
      } else {
        setTimeout(() => renderAllMath(targetEl), 100);
      }
    }

    // Render active slide
    function renderSlide(slideNum) {
      const slide = SLIDES_DATA.find(s => s.id === slideNum);
      if (!slide) return;
      currentSlide = slideNum;

      // Update Top Bar indicators
      document.getElementById('currentSlideDisplay').textContent = currentSlide;
      document.getElementById('totalSlidesDisplay').textContent = SLIDES_DATA.length;

      // Terminal Rule on Slide 20
      const nextBtn = document.getElementById('nextBtn');
      const prevBtn = document.getElementById('prevBtn');
      const lastSlideNotice = document.getElementById('lastSlideNotice');

      if (currentSlide === 20) {
        nextBtn.style.display = 'none';
        lastSlideNotice.classList.remove('hidden');
      } else {
        nextBtn.style.display = 'flex';
        lastSlideNotice.classList.add('hidden');
      }

      if (currentSlide === 1) {
        prevBtn.disabled = true;
        prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
      } else {
        prevBtn.disabled = false;
        prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
      }

      const container = document.getElementById('slideContainer');
      container.innerHTML = '';

      if (slide.type === 'quiz_slide') {
        renderQuizSlide(slide, container);
      } else {
        renderTheorySlide(slide, container);
      }

      // Update mentor voice
      const mentorText = document.getElementById('mentorVoiceText');
      if (mentorText) {
        const insights = [
          "Nature is our greatest chemistry laboratory: from lemon juice to soap, acids and bases are everywhere around us!",
          "Never taste or touch unknown chemicals in the laboratory! Always let indicators reveal the truth safely.",
          "Litmus is nature's own paper from lichens: acids turn blue litmus red, while bases turn red litmus blue.",
          "In neutral water or saline, blue stays blue and red stays red—indicators distinguish neutrality with absolute precision.",
          "Red rose extract contains anthocyanin pigments—turning fiery red in acids and deep emerald green in bases.",
          "Turmeric paper is a brilliant natural indicator: turning deep reddish-brown in bases like soap, but staying golden in acids.",
          "Olfactory indicators like onion and vanilla lose their characteristic scent in basic solutions, giving a sensory detection method.",
          "Acharya Prafulla Chandra Ray synthesized mercurous nitrite in 1896 and established India's first modern pharmaceutical industry.",
          "Neutralisation is a molecular dance: acid and base react to form salt and water, releasing warmth in an exothermic reaction.",
          "Titration with phenolphthalein shows the exact stoichiometric equivalence point: just one drop flips clear acid to vibrant pink!",
          "An ant's stinging bite injects formic acid: soothing baking soda or calamine lotion neutralises the acid instantly.",
          "A wasp sting is alkaline: soothe it with mild acid like vinegar, the exact opposite of an acidic ant bite!",
          "Farmers balance soil chemistry: slaked lime cures acidic soil, while organic compost and manure heal basic soil.",
          "Industrial wastewater carries lethal acids: treatment plants neutralise effluents with lime slurry to protect aquatic life.",
          "Excess gastric hydrochloric acid causes heartburn: antacids like Milk of Magnesia provide gentle, life-saving neutralisation.",
          "Your daily toothpaste is mildly alkaline: it neutralises bacterial acids in dental plaque to shield your tooth enamel!"
        ];
        mentorText.textContent = `"${insights[(slideNum - 1) % insights.length]}"`;
      }

      // Re-trigger math render
      renderAllMath(container);

      // Scroll to top of viewport
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Determine section string
    function getSectionForSlide(id) {
      if (id <= 2) return "Section 2.1: Nature - Our Science Laboratory & Sensory Classification";
      if (id <= 8) return "Section 2.1.1 - 2.1.3: Natural Indicators (Litmus, Rose, Turmeric & Olfactory)";
      if (id <= 10) return "Section 2.2: Neutralisation Reactions & Titration Dynamics";
      if (id <= 16) return "Section 2.3: Neutralisation in Daily Life & Indian Chemistry Heritage";
      return "Section 2.4: Mastery Assessment Challenge";
    }

    // Theory slide template renderer
    function renderTheorySlide(slide, container) {
      const simHtml = SIMULATORS_HTML[slide.simulator_type] || '<div class="p-4 text-slate-400">Simulator Loading...</div>';

      const html = `
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 flex-1">
          <!-- Left Column: Content & Theory (7 Cols) -->
          <div class="lg:col-span-7 flex flex-col space-y-4">
            
            <!-- Title & Subtitle Card -->
            <div class="p-4 sm:p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl">
              <div class="flex items-center space-x-2 mb-1">
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wider bg-purple-500/20 text-purple-300 border border-purple-500/30">
                  Concept Slide ${slide.id}
                </span>
                <span class="text-xs text-slate-400 font-mono">${getSectionForSlide(slide.id)}</span>
              </div>
              <h2 class="text-lg sm:text-xl font-extrabold text-slate-100">${slide.title}</h2>
              <div class="text-xs font-semibold text-amber-400 mt-0.5">${slide.subtitle}</div>

              <!-- Content Body -->
              <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
                ${slide.content}
              </div>

              <!-- Mathematical / Scientific Law Highlight -->
              ${slide.formula ? `
                <div class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-purple-500/30 text-amber-300 font-mono text-center text-xs sm:text-sm">
                  ${slide.formula}
                </div>
              ` : ''}
            </div>

            <!-- Key Takeaways Card -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 shadow-lg">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                <span>⭐</span> Core Principles & Key Takeaways
              </h4>
              <ul class="space-y-1.5 text-xs text-slate-300">
                ${slide.key_takeaways.map(t => `
                  <li class="flex items-start space-x-2">
                    <span class="text-amber-400 font-bold">✓</span>
                    <span>${t}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- In-Slide Checkpoints (2 Checkpoints) -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 shadow-lg space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
                  <span>🎯</span> Checkpoint Inquiries (Immediate Feedback)
                </h4>
                <span class="text-[11px] text-slate-400">2 Inquiries</span>
              </div>

              ${slide.checkpoints.map((cp, idx) => `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2" id="checkpoint_${slide.id}_${idx}">
                  <div class="text-xs font-semibold text-slate-200">
                    <span class="text-purple-400 font-bold font-mono">Q${idx + 1}:</span> ${cp.question}
                  </div>
                  <div class="grid grid-cols-1 gap-1.5 pt-1">
                    ${cp.options.map((opt, optIdx) => `
                      <button onclick="handleCheckpointAnswer(${slide.id}, ${idx}, ${optIdx}, ${cp.correct})"
                              class="cp-opt-${slide.id}-${idx} w-full text-left px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                        <span>${opt}</span>
                        <span class="cp-indicator text-xs font-bold"></span>
                      </button>
                    `).join('')}
                  </div>
                  <div id="cp_feedback_${slide.id}_${idx}" class="hidden p-2 rounded-lg text-xs leading-tight"></div>
                </div>
              `).join('')}
            </div>

          </div>

          <!-- Right Column: Interactive Bespoke Simulator (5 Cols) -->
          <div class="lg:col-span-5 flex flex-col">
            <div class="sticky top-16" id="simWrapper">
              ${simHtml}
            </div>
          </div>
        </div>
      `;

      container.innerHTML = html;

      // Initialize simulator JS engine
      const simWrapper = container.querySelector('#simWrapper');
      initSimulatorForSlide(slide.id, simWrapper);
    }

    // Checkpoint Answer Handler
    function handleCheckpointAnswer(slideId, cpIdx, selectedIdx, correctIdx) {
      const slide = SLIDES_DATA.find(s => s.id === slideId);
      if (!slide || !slide.checkpoints[cpIdx]) return;
      const cp = slide.checkpoints[cpIdx];

      const parent = document.getElementById(`checkpoint_${slideId}_${cpIdx}`);
      const buttons = parent.querySelectorAll(`.cp-opt-${slideId}-${cpIdx}`);
      const feedback = document.getElementById(`cp_feedback_${slideId}_${cpIdx}`);

      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800');
        if (idx === correctIdx) {
          btn.classList.add('bg-emerald-950', 'border-emerald-500', 'text-emerald-200');
          btn.querySelector('.cp-indicator').textContent = '✓ Correct';
          btn.querySelector('.cp-indicator').classList.add('text-emerald-400');
        } else if (idx === selectedIdx) {
          btn.classList.add('bg-rose-950', 'border-rose-500', 'text-rose-200');
          btn.querySelector('.cp-indicator').textContent = '✕ Incorrect';
          btn.querySelector('.cp-indicator').classList.add('text-rose-400');
        }
      });

      feedback.classList.remove('hidden');
      if (selectedIdx === correctIdx) {
        playSfx('correct');
        feedback.className = "p-2 rounded-lg text-xs bg-emerald-950/60 border border-emerald-500/40 text-emerald-300";
        feedback.innerHTML = `<strong>Spot On!</strong> ${cp.explanation}`;
      } else {
        playSfx('incorrect');
        feedback.className = "p-2 rounded-lg text-xs bg-rose-950/60 border border-rose-500/40 text-rose-300";
        feedback.innerHTML = `<strong>Insight:</strong> ${cp.explanation}`;
      }

      renderAllMath(feedback);
    }

    // Quiz Slide Renderer (Slides 17 to 20)
    function renderQuizSlide(slide, container) {
      const html = `
        <div class="p-5 sm:p-6 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-2xl flex-1 flex flex-col space-y-4">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <div class="flex items-center space-x-2">
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  Mastery Assessment
                </span>
                <span class="text-xs text-slate-400 font-mono">10 Challenge Inquiries</span>
              </div>
              <h2 class="text-lg sm:text-xl font-extrabold text-slate-100 mt-1">${slide.title}</h2>
              <div class="text-xs font-semibold text-purple-400">${slide.subtitle}</div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Quiz Slide</div>
              <div class="text-base font-extrabold text-amber-400 font-mono">${slide.id - 16} of 4</div>
            </div>
          </div>

          <!-- Questions Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 flex-1">
            ${slide.questions.map((q, idx) => `
              <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col justify-between space-y-3" id="quiz_card_${slide.id}_${idx}">
                <div>
                  <div class="flex items-center justify-between text-xs font-bold text-amber-400 mb-1.5">
                    <span>Question ${idx + 1}</span>
                    <button onclick="openSolutionModal(${slide.id}, ${idx})" class="text-[11px] text-purple-400 hover:text-purple-300 underline cursor-pointer">
                      View Solution 🔍
                    </button>
                  </div>
                  <div class="text-xs sm:text-sm font-semibold text-slate-200 leading-snug">
                    ${q.question}
                  </div>
                </div>

                <div class="space-y-1.5">
                  ${q.options.map((opt, optIdx) => `
                    <button onclick="handleQuizAnswer(${slide.id}, ${idx}, ${optIdx}, ${q.correct})"
                            class="quiz-btn-${slide.id}-${idx} w-full text-left px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                      <span>${opt}</span>
                      <span class="quiz-ans-icon font-bold text-xs"></span>
                    </button>
                  `).join('')}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      `;

      container.innerHTML = html;
    }

    // Quiz Answer Handler
    function handleQuizAnswer(slideId, qIdx, selectedIdx, correctIdx) {
      const slide = SLIDES_DATA.find(s => s.id === slideId);
      if (!slide || !slide.questions[qIdx]) return;
      const q = slide.questions[qIdx];

      const parent = document.getElementById(`quiz_card_${slideId}_${qIdx}`);
      const buttons = parent.querySelectorAll(`.quiz-btn-${slideId}-${qIdx}`);

      buttons.forEach((btn, idx) => {
        btn.disabled = true;
        btn.classList.remove('hover:bg-slate-800');
        if (idx === correctIdx) {
          btn.classList.add('bg-emerald-950', 'border-emerald-500', 'text-emerald-200');
          btn.querySelector('.quiz-ans-icon').textContent = '✓';
          btn.querySelector('.quiz-ans-icon').classList.add('text-emerald-400');
        } else if (idx === selectedIdx) {
          btn.classList.add('bg-rose-950', 'border-rose-500', 'text-rose-200');
          btn.querySelector('.quiz-ans-icon').textContent = '✕';
          btn.querySelector('.quiz-ans-icon').classList.add('text-rose-400');
        }
      });

      if (selectedIdx === correctIdx) {
        playSfx('correct');
      } else {
        playSfx('incorrect');
      }
    }

    // Modal popup solution viewer
    function openSolutionModal(slideId, qIdx) {
      const modal = document.getElementById('solutionModal');
      const title = document.getElementById('solutionModalTitle');
      const body = document.getElementById('solutionModalBody');

      let q;
      if (slideId >= 17 && slideId <= 20) {
        const slide = SLIDES_DATA.find(s => s.id === slideId);
        if (slide && slide.questions) q = slide.questions[qIdx];
      }

      if (q) {
        title.innerHTML = `Solution • Question: ${q.question}`;
        body.innerHTML = `
          <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300">
            <strong>Correct Answer:</strong> <span class="text-emerald-400 font-bold">${q.options[q.correct]}</span>
          </div>
          <div class="p-3.5 rounded-xl bg-purple-950/20 border border-purple-500/30 text-xs sm:text-sm text-slate-200 leading-relaxed">
            <h5 class="font-bold text-amber-400 mb-1">Step-by-Step Scientific Derivation:</h5>
            ${q.solution}
          </div>
        `;
      } else {
        title.innerHTML = `Chapter 2: Acids, Bases, and Salts Master Solutions`;
        body.innerHTML = `
          <p class="text-xs text-slate-300">All 40 challenge questions are derived from scientific principles of acid-base chemistry, natural indicators (litmus, red rose, turmeric, olfactory indicators), stoichiometric neutralisation (Acid + Base -> Salt + Water + Heat), and everyday neutralisation phenomena (ant stings, agricultural soil management, industrial effluent treatment, antacids, and dental hygiene).</p>
        `;
      }

      modal.style.display = 'flex';
      renderAllMath(body);
    }

    function closeSolutionModal() {
      document.getElementById('solutionModal').style.display = 'none';
    }

    document.getElementById('closeSolutionModalBtn').addEventListener('click', closeSolutionModal);
    document.getElementById('solutionOkBtn').addEventListener('click', closeSolutionModal);

    // Slide navigation functions
    function goToSlide(num) {
      if (num < 1 || num > SLIDES_DATA.length) return;
      playSfx('click');
      renderSlide(num);
    }

    document.getElementById('prevBtn').addEventListener('click', () => {
      if (currentSlide > 1) goToSlide(currentSlide - 1);
    });

    document.getElementById('nextBtn').addEventListener('click', () => {
      if (currentSlide < SLIDES_DATA.length) goToSlide(currentSlide + 1);
    });

    // Keyboard Arrow Keys Navigation
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        if (currentSlide < SLIDES_DATA.length) goToSlide(currentSlide + 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        if (currentSlide > 1) goToSlide(currentSlide - 1);
      } else if (e.key === 'Escape') {
        closeSolutionModal();
        document.getElementById('tocModal').classList.add('hidden');
      }
    });

    // Table of Contents Drawer
    const tocModal = document.getElementById('tocModal');
    document.getElementById('tocBtn').addEventListener('click', () => {
      const list = document.getElementById('tocList');
      list.innerHTML = SLIDES_DATA.map(s => `
        <button onclick="goToSlide(${s.id}); document.getElementById('tocModal').classList.add('hidden');"
                class="text-left p-2.5 rounded-xl ${s.id === currentSlide ? 'bg-purple-600 text-white font-bold' : 'bg-slate-950 hover:bg-slate-800 text-slate-300'} border border-slate-800 transition flex items-center justify-between">
          <span class="line-clamp-1">${s.id}. ${s.title}</span>
          <span class="text-[10px] opacity-75 font-mono ml-2">${s.type === 'quiz_slide' ? 'Quiz' : 'Lab'}</span>
        </button>
      `).join('');
      tocModal.classList.remove('hidden');
    });

    document.getElementById('closeTocBtn').addEventListener('click', () => {
      tocModal.classList.add('hidden');
    });

    // Speech synthesis narration
    document.getElementById('mentorSpeakBtn').addEventListener('click', () => {
      if (!window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const slide = SLIDES_DATA.find(s => s.id === currentSlide);
      if (!slide) return;
      const textToSpeak = `Slide ${slide.id}: ${slide.title}. ${slide.subtitle}. ` + (slide.key_takeaways ? slide.key_takeaways.join('. ') : 'Practice these questions.');
      const utter = new SpeechSynthesisUtterance(textToSpeak);
      utter.rate = 0.95;
      utter.pitch = 1.0;
      window.speechSynthesis.speak(utter);
    });

    // Sound toggle
    document.getElementById('soundToggleBtn').addEventListener('click', (e) => {
      soundEnabled = !soundEnabled;
      e.target.textContent = soundEnabled ? '🔔' : '🔕';
    });

    // Injected Simulator Engine JS
    """ + SIMULATORS_JS + r"""

    // Bootstrap
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(1);
    });
  </script>
</body>
</html>
"""

with open("public/animations/class7-science-exploring-substances.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Master lab successfully compiled at public/animations/class7-science-exploring-substances.html")

