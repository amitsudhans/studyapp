# -*- coding: utf-8 -*-
"""
Master compiler script for Class 7 Science Chapter 6: Adolescence: A Stage of Growth and Change
Generates public/animations/class7-science-adolescence-growth.html
"""

import sys
import json
sys.path.insert(0, ".agents")

from class7_science_adolescence_data import SLIDES_DATA
from class7_science_adolescence_sims import SIMULATORS_HTML
from class7_science_adolescence_js import SIMULATOR_JS

html_template = r"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Science • Chapter 6: Adolescence Master Lab</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#fff1f2',
              100: '#ffe4e6',
              500: '#f43f5e',
              600: '#e11d48',
              700: '#be123c',
              900: '#881337',
              950: '#4c0519'
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-rose-500 selection:text-white">

  <!-- Fixed Top Header / Navbar -->
  <header class="sticky top-0 z-40 bg-slate-900/95 backdrop-blur border-b border-slate-800 px-4 py-2.5 shadow-md">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Left: Logo & Chapter Title -->
      <div class="flex items-center space-x-3">
        <a href="/" class="w-9 h-9 rounded-xl bg-gradient-to-br from-rose-500 to-amber-600 flex items-center justify-center text-white font-extrabold text-sm shadow-md hover:opacity-90 transition">
          S7
        </a>
        <div>
          <div class="flex items-center space-x-2">
            <span class="text-[11px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30">
              NCERT Class 7 Science
            </span>
            <span class="text-xs text-slate-400 font-medium">Chapter 6</span>
          </div>
          <h1 class="text-sm sm:text-base font-extrabold text-slate-100 truncate max-w-xs sm:max-w-md lg:max-w-lg">
            Adolescence
          </h1>
        </div>
      </div>

      <!-- Middle: Slide Indicator & Progress Bar -->
      <div class="hidden md:flex flex-col items-center w-64 lg:w-80">
        <div class="flex items-center justify-between w-full text-xs text-slate-400 font-mono mb-1">
          <span>Slide <strong id="currentSlideDisplay" class="text-rose-400">1</strong> of <span id="totalSlidesDisplay">20</span></span>
          <span id="slideTypeBadge" class="text-[10px] uppercase font-bold text-slate-400">Concept Lab</span>
        </div>
        <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden border border-slate-700/50">
          <div id="topProgressBar" class="h-full bg-gradient-to-r from-rose-500 to-amber-500 transition-all duration-300" style="width: 5%;"></div>
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
        <div class="w-8 h-8 rounded-full bg-rose-600/30 border border-rose-500/50 flex items-center justify-center text-rose-300 font-extrabold text-xs shadow">
          AJ
        </div>
        <div class="leading-tight">
          <div class="font-bold text-slate-200">Dr. Anandibai Joshi</div>
          <div class="text-[10px] text-slate-400">Pioneer Physician of Public Health & Women's Medicine</div>
        </div>
      </div>
      <div class="hidden sm:flex items-center space-x-2 text-slate-300 italic text-xs max-w-xl truncate" id="mentorVoiceText">
        "Adolescence is nature's magnificent gateway to adulthood: understand your changing body with scientific pride, nutritious care, and zero shame!"
      </div>
      <button id="mentorSpeakBtn" class="text-[11px] px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 transition flex items-center gap-1 cursor-pointer">
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
        <div id="lastSlideNotice" class="hidden text-xs sm:text-sm text-amber-400 font-bold px-3 py-1.5 bg-amber-500/10 border border-amber-500/30 rounded-xl">
          You have reached the last slide of this chapter.
        </div>
        <div id="slideDotsContainer" class="hidden sm:flex items-center space-x-1.5 overflow-x-auto max-w-md py-1 px-2">
          <!-- Slide dots rendered by JS -->
        </div>
      </div>

      <!-- Next Button -->
      <button id="nextBtn" class="px-5 py-2 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-bold text-xs sm:text-sm transition flex items-center gap-2 cursor-pointer shadow-lg shadow-rose-600/30">
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
          <span class="text-rose-400 font-bold">📑 Table of Contents</span>
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
        <h4 id="solutionModalTitle" class="text-sm sm:text-base font-bold text-amber-400 flex items-center gap-2">
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
        <button id="solutionOkBtn" class="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs cursor-pointer">
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
          osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
          osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.15); // E5
          gain.gain.setValueAtTime(0.15, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        } else if (type === 'incorrect') {
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, ctx.currentTime); // A3
          osc.frequency.exponentialRampToValueAtTime(146.83, ctx.currentTime + 0.2); // D3
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
      } catch (e) {
        // AudioContext not allowed without interaction
      }
    }
  </script>

  <!-- Injected Slide Data & Core Runtime Engine -->
  <script>
    const SLIDES_DATA = """ + json.dumps(SLIDES_DATA, ensure_ascii=False) + """;
    const SIMULATORS_HTML = """ + json.dumps(SIMULATORS_HTML, ensure_ascii=False) + """;

    let currentSlide = 1;

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
        typeBadge.className = 'text-[10px] uppercase font-bold text-rose-400 font-mono';
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
          "Growth is not a race: genetic timing, balanced nutrition, and epiphyseal cartilage ensure everyone achieves full adult stature in their own rhythm.",
          "Secondary sexual traits are nature's outward reflection of internal biological readiness—cherish your growing self without comparison.",
          "The deepening voice and Adam's apple in boys are physical triumphs of growing vocal cords; fluctuating pitch is completely normal.",
          "Acne is simply temporary glandular hyperactivity under hormonal signals—treat your skin with gentle cleanliness and patience, never harsh squeezing.",
          "Menstruation is a clean, natural, and universal hallmark of reproductive health; break superstitious taboos with scientific conviction!",
          "Food spoiling is caused by airborne microbes, not menstruating girls—empower every young woman to participate freely in sports, study, and life.",
          "Your adolescent amygdala reacts with quick passion, but pausing for three deep breaths invites the wise prefrontal cortex to guide your decisions.",
          "Fuel your growing cells with proteins, leafy greens rich in iron, and calcium-dense milk: junk food satisfies hunger but starves bone growth.",
          "Hygiene is personal dignity: changing sanitary pads every 4 to 6 hours and wrapping them safely protects health and our municipal environment.",
          "Sixty minutes of active daily games surge natural mood-uplifting endorphins while solidifying lifelong skeletal density.",
          "In the digital world, your boundaries are sacred: protect personal privacy, preserve evidence against cyberbullying, and speak up without hesitation.",
          "Saying 'NO' to harmful substances is the ultimate badge of strength, self-esteem, and unshakeable personal character.",
          "Tobacco tar, nicotine, and alcohol irreversibly destroy developing alveoli and liver tissues: keep your body pure and unpolluted.",
          "The microscopic pituitary gland commands the entire human endocrine orchestra through ductless chemical messengers traveling in the blood.",
          "Negative feedback loops maintain delicate hormonal homeostasis, proving the sheer perfection of biological self-regulation.",
          "Over two millennia ago, Sushruta Samhita revered Kishoravastha as sacred growth: honor your body with Dinacharya, pure nutrition, and dignity!"
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
      if (id <= 4) return "Section 6.1: Growing With Age: The Teenage Years";
      if (id <= 6) return "Section 6.2: Changes Indicating Reproductive Capability";
      if (id === 7) return "Section 6.3: Emotional and Behavioural Changes in Adolescents";
      if (id <= 13) return "Section 6.4: Making Adolescence a Joyful Experience";
      if (id <= 15) return "Section 6.5: The 'Why' Question for Adolescence (Hormones & Feedback)";
      if (id === 16) return "Section 6.6: Ancient Indian Heritage (Kishoravastha & Sapta Dhatus)";
      return "Section 6.7: Comprehensive Mastery Assessment Challenges";
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
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30">
                  Concept Slide ${slide.id}
                </span>
                <span class="text-xs text-slate-400 font-mono">${getSectionForSlide(slide.id)}</span>
              </div>
              <h2 class="text-lg sm:text-xl font-extrabold text-slate-100">${slide.title}</h2>
              <div class="text-xs font-semibold text-rose-400 mt-0.5">${slide.subtitle}</div>

              <!-- Content Body -->
              <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed space-y-2">
                ${slide.content}
              </div>

              <!-- Scientific Law / Biological Axiom Highlight -->
              ${slide.formula ? `
                <div class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-rose-500/30 text-rose-300 font-mono text-center text-xs sm:text-sm">
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
                    <span class="text-rose-400 font-bold">✓</span>
                    <span>${t}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- In-Slide Checkpoints (2 Checkpoints) -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 shadow-lg space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                  <span>🎯</span> Checkpoint Inquiries (Immediate Feedback)
                </h4>
                <span class="text-[11px] text-slate-400">2 Inquiries</span>
              </div>

              ${slide.checkpoints.map((cp, idx) => `
                <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2" id="checkpoint_${slide.id}_${idx}">
                  <div class="text-xs font-semibold text-slate-200">
                    <span class="text-rose-400 font-bold font-mono">Q${idx + 1}:</span> ${cp.question}
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
              <div class="text-xs font-semibold text-rose-400">${slide.subtitle}</div>
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
                  <div class="flex items-center justify-between text-xs font-bold text-rose-400 mb-1.5">
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
            <div class="mt-4 p-4 rounded-xl bg-rose-950/30 border border-rose-500/40 flex items-center justify-between">
              <div>
                <h4 class="text-sm font-bold text-rose-300">Chapter 6 Mastery Complete!</h4>
                <p class="text-xs text-slate-300">You have completed all conceptual explorations, simulations, and 40 assessment inquiries for Adolescence.</p>
              </div>
              <button onclick="openSolutionModal(null, null)" class="px-4 py-2 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-bold text-xs transition shadow-lg cursor-pointer">
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
                class="w-2.5 h-2.5 rounded-full transition-all ${s.id === currentSlide ? 'w-6 bg-rose-500' : (s.type === 'quiz_slide' ? 'bg-emerald-700/60 hover:bg-emerald-500' : 'bg-slate-700 hover:bg-slate-500')}">
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
          <div class="p-3.5 rounded-xl bg-rose-950/20 border border-rose-500/30 text-xs sm:text-sm text-slate-200 leading-relaxed">
            <h5 class="font-bold text-rose-400 mb-1">Step-by-Step Scientific Derivation:</h5>
            ${q.solution}
          </div>
        `;
      } else {
        title.innerHTML = "Master Synthesis & Assessment Key";
        body.innerHTML = `
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-xs sm:text-sm text-slate-300 leading-relaxed">
            <p class="mb-2">Congratulations on completing all 20 interactive slides for <strong>Chapter 6: Adolescence</strong>!</p>
            <p class="text-rose-400 font-semibold mb-1">Key Conceptual Pillars Explored:</p>
            <ul class="list-disc pl-5 space-y-1 text-slate-300">
              <li><strong>Physical Metamorphosis:</strong> Pubertal growth spurt driven by growth hormone and sex steroids; epiphyseal cartilage ossification; shoulders broadening in boys vs pelvic widening in girls; Adam's apple enlargement causing voice deepening; sweat and sebaceous hyperactivity causing temporary acne.</li>
              <li><strong>Reproductive Capability & Menstruation:</strong> Onset of menstrual cycle (menarche) signifying biological vitality; scientific debunking of taboos (sterile blood, zero food spoilage, hygienic exercise benefits); absolute rejection of superstitious isolation.</li>
              <li><strong>Neurodevelopment & Emotional Balance:</strong> Adolescent emotional brain (reactive amygdala) vs maturing impulse control (prefrontal cortex); mindful pause-and-reflect techniques for emotional stability.</li>
              <li><strong>Holistic Adolescent Lifestyle:</strong> Balanced diet (iron for hemoglobin/anemia prevention, calcium for bone density, proteins for tissue building); hygienic menstrual care (changing pads every 4-6 hours, paper-wrapped disposal, never flushing pads); 60-min daily exercise triggering mood-elevating endorphins; cyber safety defense against bullying.</li>
              <li><strong>Assertive Substance Refusal:</strong> Direct eye-contact refusal techniques to resist peer pressure; severe cellular pathology of tobacco tar, nicotine, and alcohol.</li>
              <li><strong>Endocrine Orchestration & Ancient Heritage:</strong> Master pituitary gland secreting LH, FSH, and GH directly into ductless capillaries; negative feedback regulation loops; and Sushruta Samhita's reverent understanding of Kishoravastha, Sapta Dhatus, and Artava Pravritti dignity.</li>
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
                class="text-left p-2.5 rounded-xl ${s.id === currentSlide ? 'bg-rose-600 text-white font-bold' : 'bg-slate-950 hover:bg-slate-800 text-slate-300'} border border-slate-800 transition flex items-center justify-between">
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

with open("public/animations/class7-science-adolescence-growth.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Master lab successfully compiled at public/animations/class7-science-adolescence-growth.html")
