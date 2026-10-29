# -*- coding: utf-8 -*-
"""
Master compiler script for Class 7 Science Chapter 9: Life Processes in Animals
Generates public/animations/class7-science-life-processes-animals.html
"""

import sys
import json
sys.path.insert(0, ".agents")

from class7_science_life_processes_data import SLIDES_DATA
from class7_science_life_processes_sims import SIMULATORS_HTML
from class7_science_life_processes_js import SIMULATOR_JS

html_template = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Science • Chapter 9: Life Processes in Animals Master Lab</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#fff7ed',
              100: '#ffedd5',
              500: '#10b981',
              600: '#059669',
              700: '#047857',
              900: '#064e3b',
              950: '#022c22'
            }
          }
        }
      }
    }
  </script>

  <!-- KaTeX for Scientific Formula Rendering -->
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
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-emerald-500 selection:text-white">

  <!-- Fixed Top Header / Navbar -->
  <header class="sticky top-0 z-40 bg-slate-900/95 backdrop-blur border-b border-slate-800 px-4 py-2.5 shadow-md">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Left: Logo & Chapter Title -->
      <div class="flex items-center space-x-3">
        <a href="/" class="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-cyan-600 flex items-center justify-center text-white font-extrabold text-sm shadow-md hover:opacity-90 transition">
          S9
        </a>
        <div>
          <div class="flex items-center space-x-2">
            <span class="text-[11px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
              NCERT Class 7 Science
            </span>
            <span class="text-xs text-slate-400 font-medium">Chapter 9</span>
          </div>
          <h1 class="text-sm sm:text-base font-extrabold text-slate-100 truncate max-w-xs sm:max-w-md lg:max-w-lg">
            Life Processes in Animals
          </h1>
        </div>
      </div>

      <!-- Middle: Slide Indicator & Progress Bar -->
      <div class="hidden md:flex flex-col items-center w-64 lg:w-80">
        <div class="flex items-center justify-between w-full text-xs text-slate-400 font-mono mb-1">
          <span>Slide <strong id="currentSlideDisplay" class="text-emerald-400">1</strong> of <span id="totalSlidesDisplay">20</span></span>
          <span id="slideTypeBadge" class="text-[10px] uppercase font-bold text-slate-400">Concept Lab</span>
        </div>
        <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden border border-slate-700/50">
          <div id="topProgressBar" class="h-full bg-gradient-to-r from-emerald-500 to-cyan-500 transition-all duration-300" style="width: 5%;"></div>
        </div>
      </div>

      <!-- Right: Action Controls -->
      <div class="flex items-center space-x-2">
        <button id="tocBtn" title="Table of Contents" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-semibold border border-slate-700 transition flex items-center gap-1.5 cursor-pointer">
          <span>📑</span>
          <span class="hidden sm:inline">Contents</span>
        </button>
        <button id="soundToggleBtn" title="Toggle Sound Feedback" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm border border-slate-700 transition cursor-pointer">
          🔔
        </button>
      </div>

    </div>
  </header>

  <!-- Mentor Insight Strip -->
  <div class="bg-slate-900 border-b border-slate-800/80 px-4 py-2">
    <div class="max-w-7xl mx-auto flex items-center justify-between text-xs">
      <div class="flex items-center space-x-3">
        <div class="w-8 h-8 rounded-full bg-emerald-600/30 border border-emerald-500/50 flex items-center justify-center text-emerald-300 font-extrabold text-xs shadow">
          WH
        </div>
        <div class="leading-tight">
          <div class="font-bold text-slate-200">William Harvey & Sushruta</div>
          <div class="text-[10px] text-slate-400">Pioneers of Circulation, Surgery & Digestive Agni</div>
        </div>
      </div>
      <div class="hidden sm:flex items-center space-x-2 text-slate-300 italic text-xs max-w-xl truncate" id="mentorVoiceText">
        "Food is the fuel of life, disassembled by the digestive tract; oxygen is the breath of fire, delivered to every cell to sustain vitality!"
      </div>
      <button id="mentorSpeakBtn" class="text-[11px] px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700 transition flex items-center gap-1 cursor-pointer">
        <span>🔊</span>
        <span class="hidden md:inline">Listen</span>
      </button>
    </div>
  </div>

  <!-- Main Slide Workspace -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-5 flex flex-col">
    <div id="slideContainer" class="flex-1 flex flex-col slide-transition">
      <!-- Injected dynamically via renderSlide() -->
    </div>
  </main>

  <!-- Fixed Bottom Navigation Bar -->
  <footer class="sticky bottom-0 z-40 bg-slate-900/95 backdrop-blur border-t border-slate-800 px-4 py-3 shadow-2xl">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Prev Button -->
      <button id="prevBtn" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white font-semibold text-xs sm:text-sm border border-slate-700 transition flex items-center gap-2 cursor-pointer shadow">
        <span>←</span>
        <span>Previous</span>
      </button>

      <!-- Center Slide Dots / Terminal Slide Notice -->
      <div class="flex items-center space-x-2">
        <div id="lastSlideNotice" class="hidden text-xs sm:text-sm text-emerald-400 font-bold px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/30 rounded-xl">
          You have reached the last slide of this chapter.
        </div>
        <div id="slideDotsContainer" class="hidden sm:flex items-center space-x-1.5 overflow-x-auto max-w-md py-1 px-2">
          <!-- Slide dots rendered by JS -->
        </div>
      </div>

      <!-- Next Button -->
      <button id="nextBtn" class="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-xs sm:text-sm transition flex items-center gap-2 cursor-pointer shadow-lg shadow-emerald-600/30">
        <span>Next</span>
        <span>→</span>
      </button>

    </div>
  </footer>

  <!-- Table of Contents Modal Drawer -->
  <div id="tocModal" class="hidden fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <span class="text-emerald-400 font-bold">📑 Table of Contents</span>
          <span class="text-xs text-slate-400 font-mono">(20 Slides)</span>
        </div>
        <button id="closeTocBtn" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center cursor-pointer">
          ✕
        </button>
      </div>
      <div id="tocList" class="p-4 overflow-y-auto space-y-2 flex-1 text-sm">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <!-- Step-by-Step Solution & Synthesis Modal -->
  <div id="solutionModal" style="display: none; z-index: 99999 !important;" class="fixed inset-0 bg-black/80 backdrop-blur-sm items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/80">
        <h4 id="solutionModalTitle" class="text-sm sm:text-base font-bold text-emerald-400 flex items-center gap-2">
          <span>🔍</span> Step-by-Step Solution & Scientific Derivation
        </h4>
        <button id="closeSolutionModalBtn" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center justify-center cursor-pointer">
          ✕
        </button>
      </div>
      <div id="solutionModalBody" class="p-4 sm:p-6 overflow-y-auto space-y-4 flex-1 text-sm text-slate-200">
        <!-- Injected dynamically -->
      </div>
      <div class="p-3 border-t border-slate-800 bg-slate-950 flex justify-end">
        <button id="solutionOkBtn" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs cursor-pointer">
          Understood & Close
        </button>
      </div>
    </div>
  </div>

  <!-- Audio Synthesis / Sound Generator Engine -->
  <script>
    let soundEnabled = true;
    function playSfx(type) {
      if (!soundEnabled) return;
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        if (type === 'correct') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(523.25, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.15);
          gain.gain.setValueAtTime(0.15, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        } else if (type === 'incorrect') {
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(146.83, ctx.currentTime + 0.2);
          gain.gain.setValueAtTime(0.15, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.35);
        } else if (type === 'click') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(800, ctx.currentTime);
          gain.gain.setValueAtTime(0.05, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.05);
        }
      } catch (e) {}
    }

    // Injected Slide and Simulator Data
    const SLIDES_DATA = """ + json.dumps(SLIDES_DATA, ensure_ascii=False) + """;
    const SIMULATORS_HTML = """ + json.dumps(SIMULATORS_HTML, ensure_ascii=False) + """;

    let currentSlide = 1;

    // Robust KaTeX Math Renderer
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

      // Update Progress Bar
      const pct = (currentSlide / SLIDES_DATA.length) * 100;
      document.getElementById('topProgressBar').style.width = `${pct}%`;

      // Update Slide Type Badge
      const typeBadge = document.getElementById('slideTypeBadge');
      if (slide.type === 'quiz_slide') {
        typeBadge.textContent = 'Mastery Quiz';
        typeBadge.className = 'text-[10px] uppercase font-bold text-emerald-400 font-mono';
      } else {
        typeBadge.textContent = 'Interactive Lab';
        typeBadge.className = 'text-[10px] uppercase font-bold text-cyan-400 font-mono';
      }

      // Render Dots
      renderSlideDots();

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
          "Animals are living biochemical engines: heterotrophic creatures taking complex organic fuel and dismantling it into simple assimilable molecules!",
          "The 9-metre alimentary canal is a one-way highway of chemical transformation, assisted by the liver and pancreas glands!",
          "Digestion starts in the mouth: teeth perform mechanical comminution while salivary amylase begins the enzymatic conversion of starch into sugar!",
          "Peristalsis is muscular poetry: rhythmic waves of contraction and relaxation propel the food bolus safely down the oesophagus, defying gravity!",
          "The stomach is a chemical crucible: hydrochloric acid sterilizes food and activates pepsin, while an alkaline mucus shield protects the wall!",
          "In the duodenum, liver bile emulsifies insoluble fats into micro-droplets, allowing pancreatic enzymes to complete digestion!",
          "Millions of microscopic villi expand the small intestine surface area to over 250 m², absorbing glucose, amino acids, and fatty acids into circulation!",
          "The large intestine reclaims 90% of vital water and salts, compacting residue into solid faeces for orderly egestion through the anus!",
          "Ruminants perform biological marvels: four stomach chambers and billions of symbiotic microbes ferment tough plant cellulose into energy!",
          "Birds lack teeth to stay light for flight: the crop softens seeds, while swallowed stones inside the muscular gizzard grind them to meal!",
          "Breathing is physical ventilation, but cellular respiration is the true life flame: mitochondria burn glucose with oxygen to forge ATP energy!",
          "The respiratory tract is an air-conditioning marvel: nasal hairs and mucus filter and warm the air, while cartilage rings keep the windpipe open!",
          "Lungs have no muscles of their own: the contracting diaphragm flattens down, expanding thoracic volume and dropping pressure so air rushes in!",
          "Across 300 million balloon-like alveoli, oxygen diffuses into capillary blood to bind with red hemoglobin, while carbon dioxide is exhaled!",
          "Nature adapts respiration to every niche: fish extract water oxygen with feathery gills, earthworms breathe through moist skin, and insects use air tubes!",
          "Frogs are triple breathers: gills in tadpoles, moist skin underwater, and lungs on land! Ancient Ayurveda honored this as the harmony of Jatharagni and Prana!"
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
      if (id <= 2) return "Section 9.1: Nutrition in Animals & The Alimentary Canal";
      if (id <= 5) return "Section 9.1.1: Upper Digestive Tract: Mouth, Oesophagus & Stomach";
      if (id <= 8) return "Section 9.1.1: Intestinal Digestion, Villi Absorption & Egestion";
      if (id <= 10) return "Section 9.1.2: Comparative Digestion: Ruminants & Avian Gizzards";
      if (id <= 12) return "Section 9.2: Cellular Respiration & Human Airway Anatomy";
      if (id <= 14) return "Section 9.2.1: Breathing Mechanics & Alveolar Gas Exchange";
      if (id <= 16) return "Section 9.2.2: Animal Breathing Diversity & Ancient Heritage";
      return "Section 9.3: Comprehensive Mastery Assessment Challenges";
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
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  Concept Slide ${slide.id}
                </span>
                <span class="text-xs text-slate-400 font-mono">${getSectionForSlide(slide.id)}</span>
              </div>
              <h2 class="text-lg sm:text-xl font-extrabold text-slate-100">${slide.title}</h2>
              <div class="text-xs font-semibold text-emerald-400 mt-0.5">${slide.subtitle}</div>

              <!-- Content Body -->
              <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
                ${slide.content}
              </div>

              <!-- Scientific Law Highlight -->
              ${slide.formula ? `
                <div class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-emerald-300 font-mono text-center text-xs sm:text-sm">
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
                    <span class="text-emerald-400 font-bold">✓</span>
                    <span>${t}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- In-Slide Checkpoints (2 Checkpoints) -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 shadow-lg space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                  <span>🎯</span> Checkpoint Inquiries (Immediate Feedback)
                </h4>
                <span class="text-[11px] text-slate-400">2 Inquiries</span>
              </div>

              ${slide.checkpoints.map((cp, idx) => `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2" id="checkpoint_${slide.id}_${idx}">
                  <div class="text-xs font-semibold text-slate-200">
                    <span class="text-emerald-400 font-bold font-mono">Q${idx + 1}:</span> ${cp.question}
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
      if (typeof window.initSimulatorForSlide === 'function') {
        window.initSimulatorForSlide(slide.id, simWrapper);
      }
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
              <div class="text-xs font-semibold text-emerald-400">${slide.subtitle}</div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Quiz Slide</div>
              <div class="text-base font-extrabold text-cyan-400 font-mono">${slide.id - 16} of 4</div>
            </div>
          </div>

          <!-- Questions Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 flex-1">
            ${slide.questions.map((q, idx) => `
              <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col justify-between space-y-3" id="quiz_card_${slide.id}_${idx}">
                <div>
                  <div class="flex items-center justify-between text-xs font-bold text-amber-400 mb-1.5">
                    <span>Question ${idx + 1}</span>
                    <button onclick="openSolutionModal(${slide.id}, ${idx})" class="text-[11px] text-cyan-400 hover:text-cyan-300 underline cursor-pointer">
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

                <div id="quiz_feedback_${slide.id}_${idx}" class="hidden p-2 rounded-lg text-xs leading-tight"></div>
              </div>
            `).join('')}
          </div>

          <!-- Slide 20 Summary Callout -->
          ${slide.id === 20 ? `
            <div class="mt-4 p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/40 flex items-center justify-between">
              <div>
                <h4 class="text-sm font-bold text-emerald-300">Chapter 9 Mastery Complete!</h4>
                <p class="text-xs text-slate-300">You have completed all conceptual explorations, simulations, and 40 assessment inquiries for Life Processes in Animals.</p>
              </div>
              <button onclick="openSolutionModal(null, null)" class="px-4 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-xs transition shadow-lg cursor-pointer">
                Full Conceptual Synthesis
              </button>
            </div>
          ` : ''}

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
      const feedback = document.getElementById(`quiz_feedback_${slideId}_${qIdx}`);

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

      feedback.classList.remove('hidden');
      if (selectedIdx === correctIdx) {
        playSfx('correct');
        feedback.className = "p-2 rounded-lg text-xs bg-emerald-950/60 border border-emerald-500/40 text-emerald-300";
        feedback.innerHTML = `<strong>Accurate!</strong> Correct answer selected.`;
      } else {
        playSfx('incorrect');
        feedback.className = "p-2 rounded-lg text-xs bg-rose-950/60 border border-rose-500/40 text-rose-300";
        feedback.innerHTML = `<strong>Review Required:</strong> Correct answer is <em>${q.options[correctIdx]}</em>.`;
      }
    }

    // Render Bottom Slide Indicator Dots
    function renderSlideDots() {
      const dots = document.getElementById('slideDotsContainer');
      dots.innerHTML = SLIDES_DATA.map(s => `
        <button onclick="goToSlide(${s.id})"
                title="Slide ${s.id}: ${s.title}"
                class="w-2.5 h-2.5 rounded-full transition-all ${s.id === currentSlide ? 'w-6 bg-emerald-500' : (s.type === 'quiz_slide' ? 'bg-cyan-700/60 hover:bg-cyan-500' : 'bg-slate-700 hover:bg-slate-500')}">
        </button>
      `).join('');
    }

    // Solution Modal Handlers
    function openSolutionModal(slideId, qIdx) {
      const modal = document.getElementById('solutionModal');
      const title = document.getElementById('solutionModalTitle');
      const body = document.getElementById('solutionModalBody');

      let q = null;
      if (slideId && qIdx !== null) {
        const slide = SLIDES_DATA.find(s => s.id === slideId);
        if (slide && slide.questions) {
          q = slide.questions[qIdx];
        }
      }

      if (q) {
        title.innerHTML = `Solution • Question: ${q.question}`;
        body.innerHTML = `
          <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300">
            <strong>Correct Answer:</strong> <span class="text-emerald-400 font-bold">${q.options[q.correct]}</span>
          </div>
          <div class="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/30 text-xs sm:text-sm text-slate-200 leading-relaxed">
            <h5 class="font-bold text-emerald-400 mb-1">Step-by-Step Scientific Derivation:</h5>
            ${q.solution}
          </div>
        `;
      } else {
        title.innerHTML = "Master Synthesis & Assessment Key";
        body.innerHTML = `
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed">
            <p class="mb-2">Congratulations on completing all 20 interactive slides for <strong>Chapter 9: Life Processes in Animals</strong>!</p>
            <p class="text-emerald-400 font-semibold mb-1">Key Conceptual Pillars Explored:</p>
            <ul class="list-disc pl-5 space-y-1 text-slate-300">
              <li><strong>Nutrition in Animals:</strong> Breaking down insoluble macromolecules into simple absorbable units: carbohydrates to glucose, proteins to amino acids, and fats to fatty acids and glycerol.</li>
              <li><strong>Human Alimentary Canal:</strong> Buccal cavity (teeth comminution + salivary amylase starch cleavage), oesophagus (peristalsis defying gravity), stomach (gastric churning + HCl sterilization + pepsin proteolysis + mucus shield), small intestine (~6m, liver bile fat emulsification + pancreatic enzymes), and large intestine (water/salt recovery + rectal egestion).</li>
              <li><strong>Absorption & Villi:</strong> Millions of finger-like villi expanding surface area past 250 m²; blood capillaries absorb sugars/amino acids while the central lacteal absorbs fats.</li>
              <li><strong>Animal Digestive Adaptations:</strong> Ruminants (cows, buffaloes) with four stomach chambers (Rumen, Reticulum, Omasum, Abomasum) and symbiotic cellulose-fermenting microbes; birds with toothless crops and muscular gizzards grinding seeds with swallowed pebbles.</li>
              <li><strong>Cellular Respiration:</strong> Mitochondria oxidation: Glucose + Oxygen → Carbon Dioxide + Water + ATP Energy. Physical breathing (ventilation) vs chemical cellular respiration.</li>
              <li><strong>Human Breathing Mechanics:</strong> Nasal filtering/warming, epiglottis airway protection, C-shaped tracheal cartilage rings, and pressure-volume diaphragm dynamics (inhalation: diaphragm contracts down, volume expands, pressure drops, air rushes in).</li>
              <li><strong>Alveolar Gas Exchange:</strong> 300+ million alveoli (80 m² area); oxygen binds with red blood cell hemoglobin to form oxyhemoglobin, while carbon dioxide diffuses into alveoli for exhalation.</li>
              <li><strong>Diverse Animal Breathing:</strong> Aquatic fish gills with feathery capillary lamellae; earthworm cutaneous breathing through moist, mucus-coated skin; insect spiracles delivering air directly through tracheal pipes; and frogs with triple respiratory modes (tadpole gills, underwater skin, land lungs).</li>
              <li><strong>Ancient Indian Heritage:</strong> Maharishi Sushruta and Charaka's foundational insights into Jatharagni (digestive metabolic fire) and Prana Vayu (vital respiratory life breath).</li>
            </ul>
          </div>
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
                class="text-left p-2.5 rounded-xl ${s.id === currentSlide ? 'bg-emerald-600 text-white font-bold' : 'bg-slate-950 hover:bg-slate-800 text-slate-300'} border border-slate-800 transition flex items-center justify-between cursor-pointer">
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
    """ + SIMULATOR_JS + r"""

    // Bootstrap
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(1);
    });
  </script>
</body>
</html>
"""

with open("public/animations/class7-science-life-processes-animals.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Master lab successfully compiled at public/animations/class7-science-life-processes-animals.html")
