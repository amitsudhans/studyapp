#!/usr/bin/env python3
"""
Master Builder for NCERT Class 7 Mathematics - Chapter 5:
Connecting the Dots... (Data Handling & Statistics) Interactive Master Lab.
Generates: public/animations/class7-math-connecting-the-dots.html
"""

import sys
import json
sys.path.append('.agents')

from class7_math_connecting_the_dots_data import SLIDES_DATA, QUIZ_QUESTIONS
from class7_math_connecting_the_dots_sims import SIMULATORS
from class7_math_connecting_the_dots_js import SIMULATORS_JS

# Prepare full slides structure
full_slides = []
for s in SLIDES_DATA:
    if "quiz_range" in s:
        start_q, end_q = s["quiz_range"]
        s["questions"] = QUIZ_QUESTIONS[start_q - 1:end_q]
        s["is_quiz"] = True
    else:
        s["is_quiz"] = False
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)
QUIZ_QUESTIONS_JSON = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)
SIMULATORS_JSON = json.dumps(SIMULATORS, ensure_ascii=False)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Mathematics • Chapter 5: Connecting the Dots... Master Lab</title>
  
  <!-- KaTeX CSS & JS (Synchronous loading for reliable initial math render) -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script>
    function triggerMathRender(el) {
      const target = el || document.body;
      if (typeof renderMathInElement === 'function') {
        try {
          renderMathInElement(target, {
            delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\[', right: '\\]', display: true},
              {left: '\\(', right: '\\)', display: false}
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
          });
        } catch (e) {
          console.warn('KaTeX render error:', e);
        }
      } else {
        setTimeout(() => triggerMathRender(target), 50);
      }
    }
    window.triggerMathRender = triggerMathRender;

    // Fallback Pure-JavaScript Math Beautifier (if KaTeX CDN is blocked or delayed)
    function formatSimpleMath(tex) {
      let s = tex.trim();
      s = s.replace(/\\textbf\{([^}]+)\}/g, '<b>$1</b>');
      s = s.replace(/\\mathbf\{([^}]+)\}/g, '<b>$1</b>');
      s = s.replace(/\\text\{([^}]+)\}/g, '$1');
      s = s.replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '<span style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.1;margin:0 2px;"><span style="display:block;border-bottom:1px solid currentColor;padding:0 2px;">$1</span><span style="display:block;padding:0 2px;">$2</span></span>');
      s = s.replace(/\\times/g, '×');
      s = s.replace(/\\div/g, '÷');
      s = s.replace(/\\cdot/g, '·');
      s = s.replace(/\\dots/g, '…');
      s = s.replace(/\\cdots/g, '…');
      s = s.replace(/\\implies/g, '⇒');
      s = s.replace(/\\rightarrow/g, '→');
      s = s.replace(/\\leftarrow/g, '←');
      s = s.replace(/\\approx/g, '≈');
      s = s.replace(/\\le/g, '≤');
      s = s.replace(/\\ge/g, '≥');
      s = s.replace(/\\lt/g, '&lt;');
      s = s.replace(/\\gt/g, '&gt;');
      s = s.replace(/\\pi/g, 'π');
      s = s.replace(/\\overline\{([^}]+)\}/g, '<span style="text-decoration:overline;">$1</span>');
      s = s.replace(/\\quad/g, '&nbsp;&nbsp;');
      s = s.replace(/\\qquad/g, '&nbsp;&nbsp;&nbsp;&nbsp;');
      return `<span class="math-fallback" style="font-family:'Cambria Math', 'Times New Roman', serif;font-style:italic;">${s}</span>`;
    }

    function fallbackMathBeautify(root) {
      if (typeof renderMathInElement === 'function') return;
      const target = root || document.body;
      const walker = document.createTreeWalker(target, NodeFilter.SHOW_TEXT, null, false);
      const textNodes = [];
      let node;
      while (node = walker.nextNode()) {
        if (node.parentElement && ['SCRIPT', 'STYLE', 'TEXTAREA', 'CODE'].includes(node.parentElement.tagName)) continue;
        if (node.nodeValue && node.nodeValue.includes('$')) {
          textNodes.push(node);
        }
      }
      textNodes.forEach(tn => {
        let text = tn.nodeValue;
        text = text.replace(/\$\$([\s\S]*?)\$\$/g, (m, eq) => formatSimpleMath(eq));
        text = text.replace(/\$([\s\S]*?)\$/g, (m, eq) => formatSimpleMath(eq));
        if (text !== tn.nodeValue) {
          const span = document.createElement('span');
          span.innerHTML = text;
          tn.parentNode.replaceChild(span, tn);
        }
      });
    }

    // MutationObserver to auto-render KaTeX on dynamic simulator updates
    let mathObserverTimeout = null;
    const mathObserver = new MutationObserver((mutations) => {
      let hasMath = false;
      for (const m of mutations) {
        const el = (m.target && m.target.nodeType === 1) ? m.target : (m.target ? m.target.parentElement : null);
        if (el) {
          if (el.closest && el.closest('.katex')) continue;
          const txt = el.textContent || '';
          if (txt.includes('$') && !el.querySelector('.katex')) {
            hasMath = true;
            break;
          }
        }
      }
      if (hasMath) {
        clearTimeout(mathObserverTimeout);
        mathObserverTimeout = setTimeout(() => {
          triggerMathRender(document.body);
        }, 30);
      }
    });

    window.addEventListener('DOMContentLoaded', () => {
      mathObserver.observe(document.body, { childList: true, subtree: true, characterData: true });
      setTimeout(() => fallbackMathBeautify(document.body), 2000);
    });
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            slate: {
              850: '#0f172a',
              900: '#0b1120',
              950: '#060a12'
            }
          }
        }
      }
    }
  </script>

  <style>
    :root {
      --bg-dark: #070d19;
      --card-bg: rgba(15, 23, 42, 0.85);
      --accent-cyan: #06b6d4;
      --accent-amber: #f59e0b;
      --accent-teal: #14b8a6;
      --border-glow: rgba(6, 182, 212, 0.25);
    }

    * {
      box-sizing: border-box;
      user-select: none;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 0% 0%, rgba(20, 184, 166, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.6) 0px, transparent 100%);
      background-attachment: fixed;
      color: #f8fafc;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    .header-bar {
      backdrop-filter: blur(12px);
      background: rgba(7, 13, 25, 0.85);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: sticky;
      top: 0;
      z-index: 40;
    }

    .main-workspace {
      flex: 1;
      max-width: 1440px;
      margin: 0 auto;
      width: 100%;
      padding: 1rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .content-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 1.25rem;
      min-height: 600px;
    }

    @media (max-width: 1024px) {
      .content-grid {
        grid-template-columns: 1fr;
      }
    }

    .theory-card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 1.25rem;
      padding: 1.5rem;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .lab-card {
      background: rgba(11, 17, 32, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 1.25rem;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    .mentor-avatar {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: linear-gradient(135deg, #0d9488, #0284c7);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(13, 148, 136, 0.3);
      position: relative;
    }

    .speech-bubble {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(20, 184, 166, 0.3);
      border-radius: 16px;
      padding: 0.85rem 1.15rem;
      position: relative;
      font-size: 0.85rem;
      line-height: 1.45;
      color: #e2e8f0;
      flex: 1;
    }

    .speech-bubble::before {
      content: '';
      position: absolute;
      left: -8px;
      top: 18px;
      border-width: 6px 8px 6px 0;
      border-style: solid;
      border-color: transparent rgba(20, 184, 166, 0.3) transparent transparent;
    }

    .checkpoint-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 0.85rem;
      padding: 0.85rem;
      margin-top: 0.65rem;
    }

    .checkpoint-btn {
      width: 100%;
      text-align: left;
      padding: 0.5rem 0.75rem;
      border-radius: 0.5rem;
      font-size: 0.75rem;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .checkpoint-btn:hover:not(:disabled) {
      background: rgba(51, 65, 85, 0.8);
      border-color: var(--accent-cyan);
      color: #fff;
    }

    .checkpoint-btn.is-correct {
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 600;
    }

    .checkpoint-btn.is-wrong {
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: #f43f5e !important;
      color: #fda4af !important;
    }

    .checkpoint-feedback {
      font-size: 0.72rem;
      margin-top: 0.4rem;
      padding: 0.4rem 0.6rem;
      border-radius: 0.4rem;
      display: none;
    }

    .checkpoint-feedback.is-correct {
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #a7f3d0;
    }

    .checkpoint-feedback.is-wrong {
      display: block;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fecdd3;
    }

    .nav-bar {
      backdrop-filter: blur(12px);
      background: rgba(7, 13, 25, 0.9);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      position: sticky;
      bottom: 0;
      z-index: 40;
      padding: 0.75rem 1.5rem;
    }

    .nav-btn {
      padding: 0.55rem 1.25rem;
      border-radius: 0.75rem;
      font-size: 0.82rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .nav-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
      pointer-events: none;
    }

    .btn-primary {
      background: linear-gradient(135deg, #0d9488, #0284c7);
      color: white;
      box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
    }

    .btn-primary:hover:not(:disabled) {
      box-shadow: 0 6px 20px rgba(13, 148, 136, 0.45);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
    }

    .btn-secondary:hover:not(:disabled) {
      background: rgba(51, 65, 85, 0.9);
      color: white;
    }

    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 1rem;
      width: 100%;
    }

    .quiz-item-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 1rem;
      padding: 1rem 1.25rem;
      margin-bottom: 0.75rem;
    }

    .quiz-opt-btn {
      width: 100%;
      text-align: left;
      padding: 0.65rem 0.9rem;
      border-radius: 0.6rem;
      font-size: 0.8rem;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(51, 65, 85, 0.8);
      border-color: var(--accent-cyan);
      color: #fff;
    }

    .quiz-opt-btn.is-correct {
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 600;
    }

    .quiz-opt-btn.is-wrong {
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: #f43f5e !important;
      color: #fda4af !important;
    }

    .btn-show-solution {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.75rem;
      border-radius: 0.5rem;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fcd34d;
      margin-top: 0.6rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-show-solution:hover {
      background: rgba(245, 158, 11, 0.28);
      transform: translateY(-1px);
    }

    /* Step-by-Step Solution Pop-Up Modal (#solutionModal) */
    #solutionModal {
      position: fixed;
      inset: 0;
      z-index: 99999 !important;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }

    #solutionModal.is-active {
      display: flex !important;
    }

    .modal-content-card {
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 20px;
      max-width: 650px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 40px rgba(13, 148, 136, 0.2);
      padding: 1.5rem;
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
      margin-bottom: 1rem;
    }

    .modal-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .modal-close-btn {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .modal-close-btn:hover {
      background: rgba(244, 63, 94, 0.2);
      color: #fb7185;
      border-color: rgba(244, 63, 94, 0.4);
    }
  </style>
</head>
<body>

  <!-- Top Sticky Header -->
  <header class="header-bar">
    <div class="max-w-[1440px] mx-auto px-6 py-3 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-teal-600 to-cyan-500 flex items-center justify-center font-black text-white text-base shadow-lg shadow-teal-500/20">
          7
        </div>
        <div>
          <div class="text-xs font-bold text-amber-400 uppercase tracking-wider">NCERT Class 7 Mathematics • Chapter 5</div>
          <h1 class="text-sm font-black text-slate-100 tracking-tight sm:text-base">Connecting the Dots... (Data Handling) Master Lab</h1>
        </div>
      </div>
      
      <div class="flex items-center gap-3">
        <div id="slideCounter" class="px-3 py-1 rounded-full bg-slate-800/80 border border-slate-700 text-xs font-bold text-slate-300">
          Slide 1 / 20
        </div>
        <select id="slideJumpSelect" class="bg-slate-900 border border-slate-700 text-xs text-slate-300 rounded-lg px-2.5 py-1.5 font-medium outline-none focus:border-cyan-500 cursor-pointer">
          <!-- Populated by JS -->
        </select>
        <button id="btnToggleAudio" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white transition-colors" title="Toggle Narration Voice">
          <svg id="iconAudioOn" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
          </svg>
          <svg id="iconAudioOff" class="w-4 h-4 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2" />
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Animated Workspace -->
  <main class="main-workspace">
    <!-- Mentor Speech Bar -->
    <div class="flex items-center gap-3 bg-slate-900/60 p-3 rounded-2xl border border-slate-800/80">
      <div class="mentor-avatar flex-shrink-0" title="Prof. P. C. Mahalanobis • Father of Indian Statistics">
        <span class="text-xl">📊</span>
      </div>
      <div class="speech-bubble">
        <span class="text-[10px] font-bold text-teal-400 uppercase tracking-wider block mb-0.5">Prof. P. C. Mahalanobis • Data Mentor</span>
        <span id="speechBubbleText">Welcome, young researchers! I am Professor P. C. Mahalanobis. Let us discover the power of statistical thinking and connecting the dots!</span>
      </div>
    </div>

    <!-- Slide Content Grid (Theory & Interactive Simulator) -->
    <div id="slideContentGrid" class="content-grid">
      <!-- Left Column: Theory & 2 Checkpoints -->
      <section id="theoryCol" class="theory-card">
        <div class="flex items-center justify-between mb-2">
          <span id="slideBadge" class="text-xs font-bold text-teal-400 uppercase tracking-wider">Section 5.1</span>
          <span id="slideSectionTitle" class="text-xs text-slate-400 font-semibold">Of Questions and Statements</span>
        </div>

        <h2 id="slideTitle" class="text-xl font-black text-slate-100 mb-3 tracking-tight">The Art of Statistical Thinking</h2>

        <div id="theoryBody" class="text-sm text-slate-300 leading-relaxed overflow-y-auto max-h-[380px] pr-1 mb-4">
          <!-- Injected Theory HTML -->
        </div>

        <!-- 2 In-Slide Checkpoint Inquiries -->
        <div id="checkpointsWrapper" class="space-y-3 mt-auto pt-2 border-t border-slate-800/80">
          <!-- Checkpoints injected by JS -->
        </div>
      </section>

      <!-- Right Column: Interactive Simulator Lab -->
      <section id="labCol" class="lab-card">
        <div class="flex items-center justify-between mb-2 pb-2 border-b border-slate-800">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-teal-400 animate-ping"></span>
            <span id="simHeaderTitle" class="text-xs font-bold text-slate-200">Interactive Laboratory</span>
          </div>
          <span class="text-[10px] font-mono text-slate-400">Live Engine</span>
        </div>

        <div id="simContainer" class="flex-1 flex flex-col justify-center">
          <!-- Simulator injected here -->
        </div>
      </section>
    </div>

    <!-- Mastery Quiz Challenge View (Slides 17-20) -->
    <div id="quizContainer" class="quiz-container">
      <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl flex items-center justify-between">
        <div>
          <span id="quizBadge" class="text-xs font-bold text-amber-400 uppercase tracking-wider">Mastery Challenge</span>
          <h2 id="quizTitle" class="text-lg font-black text-white">Quiz Challenge</h2>
        </div>
        <div id="quizScorePill" class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold font-mono text-sm">
          Score: 0 / 10
        </div>
      </div>

      <div id="quizItemsList" class="space-y-3">
        <!-- 10 Quiz Cards injected here -->
      </div>
    </div>
  </main>

  <!-- Step-by-Step Pop-up Solution Modal (#solutionModal) -->
  <div id="solutionModal" style="display: none;">
    <div class="modal-content-card">
      <div class="modal-header">
        <div class="modal-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 16v-4"/>
            <path d="M12 8h.01"/>
          </svg>
          <span id="modalTitleText">Step-by-Step Solution</span>
        </div>
        <button id="btnCloseModal" class="modal-close-btn" title="Close Modal">&times;</button>
      </div>

      <div id="modalQuestionText" class="text-xs text-slate-300 font-semibold mb-3 p-2.5 bg-slate-950/60 rounded-xl border border-slate-800">
        <!-- Question injected here -->
      </div>

      <div id="modalSolutionSteps" class="text-sm text-slate-200 space-y-3 font-sans">
        <!-- KaTeX Math steps injected here -->
      </div>
    </div>
  </div>

  <!-- Bottom Navigation Bar -->
  <footer class="nav-bar">
    <div class="max-w-[1440px] mx-auto flex items-center justify-between">
      <button id="prevBtn" class="nav-btn btn-secondary">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <span>Previous</span>
      </button>

      <!-- Slide 20 Terminal Completion Notice -->
      <div id="lastSlideNotice" class="hidden items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-bold">
        <span>🎉 You have reached the last slide of this chapter!</span>
      </div>

      <button id="nextBtn" class="nav-btn btn-primary">
        <span>Next</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </button>
    </div>
  </footer>

  <!-- Script Payloads -->
  <script>
    const SLIDES_DATA = __SLIDES_JSON__;
    const QUIZ_QUESTIONS = __QUIZ_QUESTIONS_JSON__;
    const SIMULATORS = __SIMULATORS_JSON__;

    // Web Audio Synthesizer SFX
    const sfx = {
      ctx: null,
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      },
      playTone(freq, type, duration, gainVal = 0.08) {
        try {
          this.init();
          if (!this.ctx) return;
          if (this.ctx.state === 'suspended') this.ctx.resume();
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch (e) {
          // Audio blocked or unsupported
        }
      },
      playClick() { this.playTone(600, 'sine', 0.04, 0.04); },
      playCorrect() {
        this.playTone(523.25, 'triangle', 0.08, 0.08);
        setTimeout(() => this.playTone(659.25, 'triangle', 0.12, 0.08), 80);
      },
      playWrong() {
        this.playTone(220, 'sawtooth', 0.12, 0.06);
        setTimeout(() => this.playTone(180, 'sawtooth', 0.16, 0.06), 90);
      }
    };
    window.sfx = sfx;

    // Text to Speech
    let isAudioMuted = false;
    const btnToggleAudio = document.getElementById('btnToggleAudio');
    const iconAudioOn = document.getElementById('iconAudioOn');
    const iconAudioOff = document.getElementById('iconAudioOff');

    function speakNarration(text) {
      if (isAudioMuted || !('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.0;
      utterance.pitch = 1.0;
      window.speechSynthesis.speak(utterance);
    }

    if (btnToggleAudio) {
      btnToggleAudio.addEventListener('click', () => {
        isAudioMuted = !isAudioMuted;
        if (iconAudioOn && iconAudioOff) {
          iconAudioOn.classList.toggle('hidden', isAudioMuted);
          iconAudioOff.classList.toggle('hidden', !isAudioMuted);
        }
        if (isAudioMuted && ('speechSynthesis' in window)) {
          window.speechSynthesis.cancel();
        } else if (!isAudioMuted) {
          const currentSlide = SLIDES_DATA[currentSlideIdx];
          if (currentSlide && currentSlide.narration) speakNarration(currentSlide.narration);
        }
      });
    }

    // Slide Engine State
    let currentSlideIdx = 0;
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideCounter = document.getElementById('slideCounter');
    const slideJumpSelect = document.getElementById('slideJumpSelect');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const slideBadge = document.getElementById('slideBadge');
    const slideSectionTitle = document.getElementById('slideSectionTitle');
    const slideTitle = document.getElementById('slideTitle');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsWrapper = document.getElementById('checkpointsWrapper');
    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simContainer = document.getElementById('simContainer');
    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const labCol = document.getElementById('labCol');
    const quizContainer = document.getElementById('quizContainer');
    const quizBadge = document.getElementById('quizBadge');
    const quizTitle = document.getElementById('quizTitle');
    const quizScorePill = document.getElementById('quizScorePill');
    const quizItemsList = document.getElementById('quizItemsList');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    // Modal elements
    const solutionModal = document.getElementById('solutionModal');
    const btnCloseModal = document.getElementById('btnCloseModal');
    const modalTitleText = document.getElementById('modalTitleText');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');

    // Populate Jump Select
    SLIDES_DATA.forEach((s, i) => {
      const opt = document.createElement('option');
      opt.value = i;
      opt.textContent = `Slide ${s.slide_num}: ${s.title.substring(0, 32)}...`;
      slideJumpSelect.appendChild(opt);
    });

    // Checkpoint Renderer
    function renderCheckpoints(checkpoints) {
      checkpointsWrapper.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) {
        checkpointsWrapper.style.display = 'none';
        return;
      }
      checkpointsWrapper.style.display = 'block';

      checkpoints.forEach((cp, cpIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const title = document.createElement('div');
        title.className = 'text-[11px] font-bold text-teal-400 mb-1 flex items-center gap-1.5';
        title.innerHTML = `<span>Checkpoint ${cpIdx + 1}</span>`;

        const q = document.createElement('div');
        q.className = 'text-xs text-slate-200 mb-2 font-medium';
        q.innerHTML = cp.question;

        const optsGrid = document.createElement('div');
        optsGrid.className = 'space-y-1.5';

        const fb = document.createElement('div');
        fb.className = 'checkpoint-feedback';

        cp.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'checkpoint-btn';
          btn.innerHTML = `${String.fromCharCode(65 + optIdx)}. ${optText}`;

          btn.addEventListener('click', () => {
            const btns = optsGrid.querySelectorAll('.checkpoint-btn');
            btns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('is-correct');
              sfx.playCorrect();
              fb.className = 'checkpoint-feedback is-correct';
              fb.innerHTML = `<b>✓ Correct!</b> ${cp.explanation}`;
            } else {
              btn.classList.add('is-wrong');
              btns[cp.correct].classList.add('is-correct');
              sfx.playWrong();
              fb.className = 'checkpoint-feedback is-wrong';
              fb.innerHTML = `<b>✗ Not quite.</b> ${cp.explanation}`;
            }
            if (window.triggerMathRender) triggerMathRender(fb);
          });

          optsGrid.appendChild(btn);
        });

        card.appendChild(title);
        card.appendChild(q);
        card.appendChild(optsGrid);
        card.appendChild(fb);
        checkpointsWrapper.appendChild(card);
      });
    }

    // Solution Modal Controller
    function openSolutionModal(qId) {
      sfx.playClick();
      const q = QUIZ_QUESTIONS.find(item => item.id === qId);
      if (!q) return;

      if (modalTitleText) modalTitleText.textContent = `Question ${q.id} • Step-by-Step Solution`;
      if (modalQuestionText) modalQuestionText.textContent = q.question;
      
      const correctOptText = q.options[q.correct];
      const solutionContent = q.solution ? q.solution.trim() : q.explanation;

      if (modalSolutionSteps) {
        modalSolutionSteps.innerHTML = `
          <div style="font-weight:800; color:#34d399; margin-bottom:0.6rem; font-size:0.95rem;">
            ✓ Correct Answer: Option ${String.fromCharCode(65 + q.correct)} (${correctOptText})
          </div>
          <div style="color:#e2e8f0; line-height:1.6; white-space:pre-wrap;">${solutionContent}</div>
        `;
      }

      if (solutionModal) {
        solutionModal.style.setProperty('display', 'flex', 'important');
        solutionModal.classList.add('is-active');
      }
      if (window.triggerMathRender) {
        triggerMathRender(solutionModal);
        setTimeout(() => triggerMathRender(solutionModal), 60);
      }
    }
    window.openSolutionModal = openSolutionModal;

    function closeSolutionModal() {
      sfx.playClick();
      if (solutionModal) {
        solutionModal.style.setProperty('display', 'none', 'important');
        solutionModal.classList.remove('is-active');
      }
    }
    window.closeSolutionModal = closeSolutionModal;

    if (btnCloseModal) btnCloseModal.addEventListener('click', closeSolutionModal);
    if (solutionModal) {
      solutionModal.addEventListener('click', (e) => {
        if (e.target === solutionModal) closeSolutionModal();
      });
    }

    // Quiz Slide Renderer
    function renderQuizSlide(slide) {
      slideContentGrid.style.display = 'none';
      theoryCol.style.display = 'none';
      labCol.style.display = 'none';
      quizContainer.style.display = 'flex';

      quizBadge.textContent = slide.badge;
      quizTitle.textContent = slide.title;
      quizItemsList.innerHTML = '';

      let scoreCount = 0;
      let answeredCount = 0;

      slide.questions.forEach((q, qIndex) => {
        const itemCard = document.createElement('div');
        itemCard.className = 'quiz-item-card';

        const qTitle = document.createElement('div');
        qTitle.className = 'text-xs font-bold text-slate-200 mb-2 leading-relaxed';
        qTitle.innerHTML = `<span class="text-amber-400 font-mono">Q${q.id}.</span> ${q.question}`;

        const optGrid = document.createElement('div');
        optGrid.className = 'grid grid-cols-1 md:grid-cols-2 gap-2 mb-2';

        q.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.textContent = `${String.fromCharCode(65 + oIdx)}. ${optText}`;

          btn.addEventListener('click', () => {
            const btns = optGrid.querySelectorAll('.quiz-opt-btn');
            btns.forEach(b => b.disabled = true);

            answeredCount++;
            if (oIdx === q.correct) {
              btn.classList.add('is-correct');
              sfx.playCorrect();
              scoreCount++;
            } else {
              btn.classList.add('is-wrong');
              btns[q.correct].classList.add('is-correct');
              sfx.playWrong();
            }

            quizScorePill.textContent = `Score: ${scoreCount} / ${slide.questions.length}`;
          });

          optGrid.appendChild(btn);
        });

        const solBtn = document.createElement('button');
        solBtn.className = 'btn-show-solution';
        solBtn.innerHTML = `
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
            <circle cx="12" cy="12" r="3"/>
          </svg>
          <span>View Step-by-Step Solution</span>
        `;
        solBtn.onclick = () => openSolutionModal(q.id);

        itemCard.appendChild(qTitle);
        itemCard.appendChild(optGrid);
        itemCard.appendChild(solBtn);
        quizItemsList.appendChild(itemCard);
      });

      quizScorePill.textContent = `Score: 0 / ${slide.questions.length}`;
      if (window.triggerMathRender) {
        triggerMathRender(quizContainer);
        setTimeout(() => triggerMathRender(quizContainer), 60);
        setTimeout(() => triggerMathRender(quizContainer), 250);
      }
    }

    // Master Slide Renderer
    function renderSlide(idx) {
      if (idx < 0 || idx >= SLIDES_DATA.length) return;
      currentSlideIdx = idx;
      const slide = SLIDES_DATA[idx];

      slideCounter.textContent = `Slide ${slide.slide_num} / ${SLIDES_DATA.length}`;
      slideJumpSelect.value = idx;

      // Update Navigation Buttons & Slide 20 Terminal Rule
      prevBtn.disabled = (idx === 0);
      
      if (currentSlideIdx === SLIDES_DATA.length - 1) {
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'inline-flex';
      } else {
        nextBtn.style.display = 'inline-flex';
        lastSlideNotice.style.display = 'none';
      }

      speechBubbleText.textContent = slide.narration || '';
      speakNarration(slide.narration || '');

      if (slide.is_quiz) {
        renderQuizSlide(slide);
      } else {
        slideContentGrid.style.display = 'grid';
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideBadge.textContent = slide.badge;
        slideSectionTitle.textContent = slide.section;
        slideTitle.textContent = slide.title;
        theoryBody.innerHTML = slide.theory;

        renderCheckpoints(slide.checkpoints);

        // Simulator injection
        if (slide.sim_id && SIMULATORS[slide.sim_id]) {
          simHeaderTitle.textContent = slide.title;
          simContainer.innerHTML = SIMULATORS[slide.sim_id];
          
          // Re-init simulator JS engines
          if (window.initSimulators) {
            window.initSimulators();
          }
          if (window.triggerMathRender) {
            triggerMathRender(simContainer);
            setTimeout(() => triggerMathRender(simContainer), 50);
            setTimeout(() => triggerMathRender(simContainer), 200);
          }
        } else {
          simContainer.innerHTML = '<div class="text-xs text-slate-400 p-4 text-center">Interactive simulator ready.</div>';
        }

        if (window.triggerMathRender) {
          triggerMathRender(slideContentGrid);
          setTimeout(() => triggerMathRender(slideContentGrid), 60);
          setTimeout(() => triggerMathRender(slideContentGrid), 250);
        }
      }
    }

    // Navigation Click Listeners
    prevBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx > 0) renderSlide(currentSlideIdx - 1);
    });

    nextBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx < SLIDES_DATA.length - 1) renderSlide(currentSlideIdx + 1);
    });

    slideJumpSelect.addEventListener('change', (e) => {
      sfx.playClick();
      renderSlide(parseInt(e.target.value));
    });

    // Keyboard Arrow Navigation & Modal Esc Key
    window.addEventListener('keydown', (e) => {
      if (solutionModal && (solutionModal.classList.contains('is-active') || solutionModal.style.display !== 'none')) {
        if (e.key === 'Escape') {
          closeSolutionModal();
        }
        return;
      }
      if (e.key === 'ArrowRight' && currentSlideIdx < SLIDES_DATA.length - 1) {
        sfx.playClick();
        renderSlide(currentSlideIdx + 1);
      } else if (e.key === 'ArrowLeft' && currentSlideIdx > 0) {
        sfx.playClick();
        renderSlide(currentSlideIdx - 1);
      }
    });

    // Embedded Simulator Engines
    __SIMULATORS_JS__

    // Startup Initialization
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(0);
      if (window.triggerMathRender) {
        triggerMathRender(document.body);
        setTimeout(() => triggerMathRender(document.body), 100);
        setTimeout(() => triggerMathRender(document.body), 400);
      }
    });
    window.addEventListener('load', () => {
      if (window.triggerMathRender) triggerMathRender(document.body);
    });
  </script>
</body>
</html>
"""

# Replace placeholders safely
final_html = HTML_CONTENT.replace('__SLIDES_JSON__', SLIDES_JSON)
final_html = final_html.replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)
final_html = final_html.replace('__SIMULATORS_JSON__', SIMULATORS_JSON)
final_html = final_html.replace('__SIMULATORS_JS__', SIMULATORS_JS)

output_path = 'public/animations/class7-math-connecting-the-dots.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

import os
file_size = os.path.getsize(output_path)
print(f"Generated {output_path} successfully!")
print(f"File size: {file_size} bytes")

