import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_data_handling_dots_lines_data import SLIDES_DATA

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 12: Data Handling (Tales by Dots and Lines) Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script>
    function triggerMathRender(el) {
      if (window.renderMathInElement) {
        window.renderMathInElement(el || document.body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }
    }
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="if (window.triggerMathRender) triggerMathRender(document.body);"></script>

  <style>
    :root {
      --bg-primary: #070b14;
      --bg-secondary: #0f172a;
      --card-bg: rgba(15, 23, 42, 0.85);
      --card-border: rgba(99, 102, 241, 0.25);
      --accent-indigo: #6366f1;
      --accent-cyan: #06b6d4;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
      --accent-teal: #14b8a6;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: radial-gradient(circle at top right, #1e1b4b 0%, #070b14 65%);
      color: var(--text-main);
      font-family: var(--font-stack);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Top Sticky Header */
    header {
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid var(--card-border);
      backdrop-filter: blur(12px);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .header-badge {
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 20px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }

    .header-title {
      font-size: 16px;
      font-weight: 700;
      color: #e2e8f0;
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .slide-indicator {
      font-size: 13px;
      font-weight: 600;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.1);
      padding: 4px 12px;
      border-radius: 8px;
      border: 1px solid rgba(6, 182, 212, 0.25);
    }

    .speech-btn {
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid var(--accent-indigo);
      color: #c7d2fe;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .speech-btn:hover {
      background: rgba(99, 102, 241, 0.3);
      color: #fff;
    }

    /* Main Container */
    main {
      flex: 1;
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Lesson Grid Layout (Slides 1-16) */
    .lesson-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      align-items: stretch;
    }

    @media (max-width: 1024px) {
      .lesson-grid {
        grid-template-columns: 1fr;
      }
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .card-header {
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 12px;
    }

    .slide-title {
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .slide-subtitle {
      font-size: 13px;
      font-weight: 600;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 4px;
    }

    .avatar-box {
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(99, 102, 241, 0.1);
      border: 1px solid rgba(99, 102, 241, 0.2);
      padding: 10px 14px;
      border-radius: 12px;
    }

    .avatar-icon {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: linear-gradient(135deg, #6366f1, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 4px 10px rgba(99, 102, 241, 0.4);
    }

    .avatar-text {
      font-size: 13px;
      color: #cbd5e1;
    }
    .avatar-name {
      font-weight: 700;
      color: #a5b4fc;
    }

    .theory-box {
      font-size: 14.5px;
      color: #cbd5e1;
      line-height: 1.7;
    }
    .theory-box p {
      margin-bottom: 10px;
    }
    .theory-box ul {
      margin-left: 20px;
      margin-bottom: 10px;
    }
    .theory-box li {
      margin-bottom: 6px;
    }

    .key-points-box {
      background: rgba(16, 185, 129, 0.08);
      border-left: 4px solid var(--accent-emerald);
      padding: 12px 16px;
      border-radius: 0 10px 10px 0;
    }
    .key-points-title {
      font-size: 12px;
      font-weight: 700;
      color: #6ee7b7;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }
    .key-points-list {
      list-style-type: none;
      font-size: 13.5px;
      color: #d1fae5;
    }
    .key-points-list li {
      margin-bottom: 4px;
      position: relative;
      padding-left: 18px;
    }
    .key-points-list li::before {
      content: "✦";
      position: absolute;
      left: 0;
      color: #34d399;
      font-size: 11px;
    }

    .formula-banner {
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 12px 18px;
      border-radius: 12px;
      text-align: center;
      font-size: 15px;
      color: #fde68a;
    }

    /* Checkpoints Section */
    .checkpoint-section {
      margin-top: 8px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .checkpoint-card {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .checkpoint-q {
      font-size: 13.5px;
      font-weight: 600;
      color: #f1f5f9;
    }

    .options-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
    }

    .option-btn {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(99, 102, 241, 0.2);
      color: #e2e8f0;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 13px;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s ease;
    }
    .option-btn:hover:not(:disabled) {
      background: rgba(99, 102, 241, 0.25);
      border-color: var(--accent-indigo);
      color: #fff;
    }
    .option-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #6ee7b7 !important;
      font-weight: 700;
    }
    .option-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fca5a5 !important;
    }

    .feedback-box {
      font-size: 12.5px;
      line-height: 1.5;
      padding: 10px 14px;
      border-radius: 8px;
      display: none;
    }
    .feedback-box.show {
      display: block;
    }
    .feedback-box.correct-box {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--accent-emerald);
      color: #a7f3d0;
    }
    .feedback-box.incorrect-box {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid var(--accent-rose);
      color: #fecdd3;
    }

    /* Simulator Canvas Container */
    .sim-card {
      background: #090e1a;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
    }

    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
    }

    .sim-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sim-canvas-area {
      background: #030712;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      height: 380px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }

    .sim-controls {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      background: rgba(15, 23, 42, 0.6);
      padding: 12px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .control-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .control-label {
      font-size: 12px;
      color: #94a3b8;
      font-weight: 600;
    }
    .control-slider {
      accent-color: var(--accent-indigo);
      cursor: pointer;
    }
    .control-val {
      font-size: 12px;
      color: var(--accent-cyan);
      font-weight: 700;
      min-width: 32px;
    }

    .sim-btn {
      background: rgba(99, 102, 241, 0.2);
      border: 1px solid var(--accent-indigo);
      color: #c7d2fe;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .sim-btn:hover {
      background: rgba(99, 102, 241, 0.4);
      color: #fff;
    }
    .sim-btn.active {
      background: var(--accent-indigo);
      color: #fff;
    }

    .sim-stats-bar {
      display: flex;
      gap: 16px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 8px 14px;
      font-size: 12.5px;
      color: #cbd5e1;
    }
    .stat-pill {
      display: flex;
      gap: 6px;
    }
    .stat-pill strong {
      color: var(--accent-cyan);
    }

    /* Quiz Slide Styles (Slides 17 to 20) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 20px;
    }

    .quiz-header-card {
      background: linear-gradient(135deg, rgba(30, 27, 75, 0.8), rgba(15, 23, 42, 0.9));
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .quiz-title-area h2 {
      font-size: 24px;
      font-weight: 800;
      color: #fff;
    }
    .quiz-title-area p {
      font-size: 13.5px;
      color: var(--accent-cyan);
      margin-top: 4px;
    }

    .quiz-score-pill {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--accent-emerald);
      color: #6ee7b7;
      padding: 8px 20px;
      border-radius: 30px;
      font-size: 15px;
      font-weight: 800;
    }

    .quiz-questions-list {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .quiz-item-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .q-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .q-num-badge {
      background: rgba(99, 102, 241, 0.25);
      color: #a5b4fc;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
    }

    .sol-btn {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--accent-amber);
      color: #fcd34d;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
    }
    .sol-btn:hover {
      background: rgba(245, 158, 11, 0.3);
      color: #fff;
    }

    /* Navigation Footer */
    footer {
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid var(--card-border);
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      bottom: 0;
      z-index: 100;
    }

    .nav-btn {
      background: linear-gradient(135deg, #4f46e5, #6366f1);
      color: #fff;
      border: none;
      padding: 10px 22px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .nav-btn:hover:not(:disabled) {
      background: linear-gradient(135deg, #4338ca, #4f46e5);
      transform: translateY(-1px);
    }
    .nav-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    .last-slide-notice {
      color: #34d399;
      font-size: 13.5px;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      padding: 8px 18px;
      border-radius: 20px;
      display: none;
    }

    /* Modal Backdrop */
    .modal-backdrop {
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
    }
  </style>
</head>
<body>

  <!-- Sticky Header Navigation -->
  <header>
    <div class="header-left">
      <span class="header-badge">CLASS 8 • MATHEMATICS • CHAPTER 12</span>
      <span class="header-title">Data Handling: Tales by Dots and Lines Master Lab</span>
    </div>
    <div class="header-right">
      <div class="slide-indicator" id="slideNumDisplay">Slide 1 of 20</div>
      <button class="speech-btn" id="voiceToggleBtn" onclick="toggleVoice()">
        <span id="speakerIcon">🔊</span>
        <span id="voiceStatusText">Listen</span>
      </button>
    </div>
  </header>

  <!-- Main Slide Workspace -->
  <main>
    <!-- Lesson Slide (Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      <!-- Left Column: Pedagogical Theory & Checkpoints -->
      <div class="card">
        <div class="card-header">
          <div class="slide-title">
            <span id="slideIcon">📊</span>
            <span id="slideHeading">Title Here</span>
          </div>
          <div class="slide-subtitle" id="slideSubheading">Subtitle Here</div>
        </div>

        <div class="avatar-box">
          <div class="avatar-icon">🧑‍🏫</div>
          <div class="avatar-text">
            <span class="avatar-name">Mathematics Mentor:</span>
            <span id="mentorBrief">Welcome to Chapter 12. Let us explore the tales told by data, balancing means, robust medians, and visual graphs!</span>
          </div>
        </div>

        <div class="theory-box" id="theoryContent">
          <!-- Slide HTML content populated here -->
        </div>

        <div class="formula-banner" id="formulaBanner">
          <!-- Formula content here -->
        </div>

        <div class="key-points-box">
          <div class="key-points-title">Core Principles to Remember</div>
          <ul class="key-points-list" id="keyTakeawaysList">
            <!-- Key takeaways here -->
          </ul>
        </div>

        <!-- In-Slide Conceptual Checkpoints -->
        <div class="checkpoint-section" id="checkpointContainer">
          <div style="font-size: 13px; font-weight: 700; color: #a5b4fc; text-transform: uppercase; letter-spacing: 0.5px;">
            In-Slide Conceptual Checkpoints
          </div>
          <div id="checkpointsList"></div>
        </div>
      </div>

      <!-- Right Column: Interactive Bespoke Simulator -->
      <div class="sim-card">
        <div class="sim-header">
          <div class="sim-title">
            <span>🔬</span>
            <span id="simTitle">Interactive Statistical Simulator</span>
          </div>
          <div class="sim-stats-bar" id="simStatsBar">
            <!-- Stats pills populated here -->
          </div>
        </div>

        <div class="sim-canvas-area" id="simCanvasArea">
          <!-- Dynamic Canvas/SVG injected here -->
        </div>

        <div class="sim-controls" id="simControls">
          <!-- Controls injected here -->
        </div>
      </div>
    </div>

    <!-- Quiz Slide (Slides 17 to 20) -->
    <div class="quiz-container" id="quizContainer">
      <div class="quiz-header-card">
        <div class="quiz-title-area">
          <h2 id="quizTitle">Mastery Quiz Challenge</h2>
          <p id="quizSubtitle">Answer all 10 questions to master these statistical concepts.</p>
        </div>
        <div class="quiz-score-pill" id="quizScorePill">Score: 0 / 10</div>
      </div>

      <div class="quiz-questions-list" id="quizQuestionsList">
        <!-- 10 Questions injected here -->
      </div>
    </div>
  </main>

  <!-- Navigation Footer -->
  <footer>
    <button class="nav-btn" id="prevBtn" onclick="prevSlide()" disabled>
      <span>←</span> Previous
    </button>

    <div id="lastSlideNotice" class="last-slide-notice">
      You have reached the last slide of this chapter
    </div>

    <button class="nav-btn" id="nextBtn" onclick="nextSlide()">
      Next <span>→</span>
    </button>
  </footer>

  <!-- Mathematical Solution Pop-up Modal -->
  <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop" style="position:fixed; top:0; left:0; width:100vw; height:100vh; display:none; align-items:center; justify-content:center; z-index:1000;">
    <div class="bg-slate-900 border border-amber-500/40 rounded-2xl max-w-xl w-full p-6 shadow-2xl relative" style="background:#0f172a; border:1px solid rgba(245, 158, 11, 0.4); border-radius:16px; max-width:600px; width:90%; padding:24px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.8); position:relative;">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:12px; margin-bottom:16px;">
        <div style="font-size:16px; font-weight:800; color:#fbbf24; display:flex; align-items:center; gap:8px;">
          <span>💡</span> Step-by-Step Mathematical Solution
        </div>
        <button onclick="closeSolutionModal()" style="background:none; border:none; color:#94a3b8; font-size:20px; font-weight:700; cursor:pointer;">✕</button>
      </div>

      <div id="modalQuestionText" style="font-size:13.5px; color:#94a3b8; margin-bottom:14px; font-weight:600;"></div>
      <div id="modalSolutionBody" style="font-size:14px; color:#e2e8f0; line-height:1.7; background:rgba(15,23,42,0.6); padding:16px; border-radius:10px; border:1px solid rgba(255,255,255,0.05);"></div>

      <div style="margin-top:18px; text-align:right;">
        <button onclick="closeSolutionModal()" style="background:rgba(245, 158, 11, 0.2); border:1px solid #f59e0b; color:#fbbf24; padding:8px 20px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">
          Understood
        </button>
      </div>
    </div>
  </div>

  <script>
    // Injected slides data from python
    const SLIDES = %%SLIDES_JSON%%;

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let quizUserScores = {};

    function triggerMathRender(el) {
      if (window.renderMathInElement) {
        renderMathInElement(el || document.body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }
    }

    function loadSlide(index) {
      if (index < 0 || index >= SLIDES.length) return;
      currentSlideIndex = index;
      stopSpeech();

      const slide = SLIDES[index];
      const indicator = document.getElementById('slideNumDisplay');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const lastNotice = document.getElementById('lastSlideNotice');
      const lessonGrid = document.getElementById('lessonGrid');
      const quizContainer = document.getElementById('quizContainer');

      indicator.textContent = `Slide ${index + 1} of ${SLIDES.length}`;
      prevBtn.disabled = (index === 0);

      if (index === SLIDES.length - 1) {
        nextBtn.style.display = 'none';
        lastNotice.style.display = 'block';
      } else {
        nextBtn.style.display = 'inline-block';
        lastNotice.style.display = 'none';
      }

      if (index < 16) {
        // Lesson Slide
        lessonGrid.style.display = 'grid';
        quizContainer.style.display = 'none';

        document.getElementById('slideHeading').textContent = slide.title;
        document.getElementById('slideSubheading').textContent = slide.subtitle;
        document.getElementById('theoryContent').innerHTML = slide.content;
        document.getElementById('formulaBanner').innerHTML = slide.formula;
        
        const takeaways = document.getElementById('keyTakeawaysList');
        takeaways.innerHTML = '';
        slide.key_takeaways.forEach(pt => {
          const li = document.createElement('li');
          li.textContent = pt;
          takeaways.appendChild(li);
        });

        renderCheckpoints(slide.checkpoints);
        renderSimulator(slide.simulator_type);
      } else {
        // Dedicated Quiz Slide (Slides 17 to 20)
        lessonGrid.style.display = 'none';
        quizContainer.style.display = 'flex';

        document.getElementById('quizTitle').textContent = slide.title;
        document.getElementById('quizSubtitle').textContent = slide.subtitle;
        renderQuizSlide(slide.questions);
      }

      setTimeout(() => {
        triggerMathRender(document.body);
      }, 50);
    }

    function prevSlide() {
      if (currentSlideIndex > 0) {
        loadSlide(currentSlideIndex - 1);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function nextSlide() {
      if (currentSlideIndex < SLIDES.length - 1) {
        loadSlide(currentSlideIndex + 1);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // ==========================================
    // In-Slide Conceptual Checkpoints
    // ==========================================
    function renderCheckpoints(checkpoints) {
      const list = document.getElementById('checkpointsList');
      list.innerHTML = '';

      if (!checkpoints || checkpoints.length === 0) {
        document.getElementById('checkpointContainer').style.display = 'none';
        return;
      }
      document.getElementById('checkpointContainer').style.display = 'flex';

      checkpoints.forEach((cp, cpIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';
        card.innerHTML = `
          <div class="checkpoint-q"><strong>Checkpoint ${cpIdx + 1}:</strong> ${cp.question}</div>
          <div class="options-grid" id="cpOptions${cpIdx}"></div>
          <div class="feedback-box" id="cpFeedback${cpIdx}"></div>
        `;

        const optGrid = card.querySelector(`#cpOptions${cpIdx}`);
        const feedback = card.querySelector(`#cpFeedback${cpIdx}`);

        cp.options.forEach((opt, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'option-btn';
          btn.innerHTML = `<span style="font-weight:700; color:#38bdf8;">${String.fromCharCode(65 + optIdx)}.</span> <span>${opt}</span>`;
          btn.onclick = () => {
            const allBtns = optGrid.querySelectorAll('.option-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('correct');
              feedback.className = 'feedback-box show correct-box';
              feedback.innerHTML = `<strong>✓ Excellent!</strong> ${cp.explanation}`;
            } else {
              btn.classList.add('incorrect');
              allBtns[cp.correct].classList.add('correct');
              feedback.className = 'feedback-box show incorrect-box';
              feedback.innerHTML = `<strong>✗ Not quite.</strong> ${cp.explanation}`;
            }
            triggerMathRender(feedback);
          };
          optGrid.appendChild(btn);
        });

        list.appendChild(card);
      });
    }

    // ==========================================
    // Mastery Quiz Slides (10 questions per slide)
    // ==========================================
    function renderQuizSlide(questions) {
      const container = document.getElementById('quizQuestionsList');
      container.innerHTML = '';
      quizUserScores[currentSlideIndex] = quizUserScores[currentSlideIndex] || { correct: 0, answered: 0 };

      updateQuizScoreDisplay();

      questions.forEach((q, qIdx) => {
        const qCard = document.createElement('div');
        qCard.className = 'quiz-item-card';
        qCard.innerHTML = `
          <div class="q-top-row">
            <span class="q-num-badge">Question ${qIdx + 1} of 10</span>
            <button class="sol-btn" onclick="openSolutionModal(${currentSlideIndex}, ${qIdx})">
              <span>💡</span> View Solution
            </button>
          </div>
          <div style="font-size: 14.5px; font-weight: 600; color: #f8fafc; line-height: 1.5;">${q.question}</div>
          <div class="options-grid" id="quizOpts${qIdx}"></div>
          <div class="feedback-box" id="quizFeed${qIdx}"></div>
        `;

        const optGrid = qCard.querySelector(`#quizOpts${qIdx}`);
        const feed = qCard.querySelector(`#quizFeed${qIdx}`);

        q.options.forEach((opt, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'option-btn';
          btn.innerHTML = `<span style="font-weight:700; color:#38bdf8;">${String.fromCharCode(65 + optIdx)}.</span> <span>${opt}</span>`;

          btn.onclick = () => {
            const allBtns = optGrid.querySelectorAll('.option-btn');
            allBtns.forEach(b => b.disabled = true);

            quizUserScores[currentSlideIndex].answered++;

            if (optIdx === q.correct) {
              btn.classList.add('correct');
              feed.className = 'feedback-box show correct-box';
              feed.innerHTML = `<strong>✓ Correct!</strong> Well reasoned.`;
              quizUserScores[currentSlideIndex].correct++;
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
              feed.className = 'feedback-box show incorrect-box';
              feed.innerHTML = `<strong>✗ Incorrect.</strong> Review the step-by-step solution.`;
            }
            updateQuizScoreDisplay();
          };
          optGrid.appendChild(btn);
        });

        container.appendChild(qCard);
      });
    }

    function updateQuizScoreDisplay() {
      const scorePill = document.getElementById('quizScorePill');
      const score = quizUserScores[currentSlideIndex] || { correct: 0, answered: 0 };
      scorePill.textContent = `Score: ${score.correct} / 10`;
    }

    // Modal logic
    function openSolutionModal(slideIdx, qIdx) {
      const q = SLIDES[slideIdx].questions[qIdx];
      document.getElementById('modalQuestionText').innerHTML = `<strong>Question:</strong> ${q.question}`;
      document.getElementById('modalSolutionBody').innerHTML = q.solution;

      const modal = document.getElementById('solutionModal');
      modal.style.display = 'flex';
      triggerMathRender(modal);
    }

    function closeSolutionModal() {
      document.getElementById('solutionModal').style.display = 'none';
    }

    // Audio narration Web Speech API
    function toggleVoice() {
      if (isSpeaking) {
        stopSpeech();
      } else {
        startSpeech();
      }
    }

    function startSpeech() {
      if (!synth) return;
      stopSpeech();

      const slide = SLIDES[currentSlideIndex];
      let textToRead = "";

      if (currentSlideIndex < 16) {
        textToRead = `${slide.title}. ${slide.subtitle}. `;
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = slide.content;
        textToRead += tempDiv.textContent || tempDiv.innerText || "";
      } else {
        textToRead = `${slide.title}. ${slide.subtitle}. Please answer the ten mastery challenge questions.`;
      }

      const utter = new SpeechSynthesisUtterance(textToRead);
      utter.rate = 0.95;
      utter.pitch = 1.0;

      utter.onend = () => {
        isSpeaking = false;
        updateVoiceButton();
      };
      utter.onerror = () => {
        isSpeaking = false;
        updateVoiceButton();
      };

      synth.speak(utter);
      isSpeaking = true;
      updateVoiceButton();
    }

    function stopSpeech() {
      if (synth && synth.speaking) {
        synth.cancel();
      }
      isSpeaking = false;
      updateVoiceButton();
    }

    function updateVoiceButton() {
      const btn = document.getElementById('voiceToggleBtn');
      const icon = document.getElementById('speakerIcon');
      const txt = document.getElementById('voiceStatusText');

      if (isSpeaking) {
        btn.style.background = 'rgba(239, 68, 68, 0.2)';
        btn.style.borderColor = '#ef4444';
        icon.textContent = '⏹️';
        txt.textContent = 'Stop';
      } else {
        btn.style.background = 'rgba(99, 102, 241, 0.15)';
        btn.style.borderColor = 'var(--accent-indigo)';
        icon.textContent = '🔊';
        txt.textContent = 'Listen';
      }
    }

    // ==========================================
    // 16 Bespoke Interactive SVG Simulators
    // ==========================================
    function renderSimulator(simType) {
      const title = document.getElementById('simTitle');
      const stats = document.getElementById('simStatsBar');
      const canvas = document.getElementById('simCanvasArea');
      const controls = document.getElementById('simControls');

      canvas.innerHTML = '';
      controls.innerHTML = '';
      stats.innerHTML = '';

      switch (simType) {
        case 'tales_dots_lines_intro':
          renderTalesDotsLinesIntro(title, stats, canvas, controls);
          break;
        case 'balancing_act_mean_fulcrum':
          renderBalancingActMeanFulcrum(title, stats, canvas, controls);
          break;
        case 'unchanging_mean_properties':
          renderUnchangingMeanProperties(title, stats, canvas, controls);
          break;
        case 'outlier_robustness_comparator':
          renderOutlierRobustnessComparator(title, stats, canvas, controls);
          break;
        case 'median_ordered_ranker':
          renderMedianOrderedRanker(title, stats, canvas, controls);
          break;
        case 'finding_unknown_equation_solver':
          renderFindingUnknownEquationSolver(title, stats, canvas, controls);
          break;
        case 'frequency_table_mean_median':
          renderFrequencyTableMeanMedian(title, stats, canvas, controls);
          break;
        case 'spreadsheet_formula_studio':
          renderSpreadsheetFormulaStudio(title, stats, canvas, controls);
          break;
        case 'data_visualization_scale_lab':
          renderDataVisualizationScaleLab(title, stats, canvas, controls);
          break;
        case 'line_graph_slope_navigator':
          renderLineGraphSlopeNavigator(title, stats, canvas, controls);
          break;
        case 'space_jam_orbital_traffic':
          renderSpaceJamOrbitalTraffic(title, stats, canvas, controls);
          break;
        case 'rain_pattern_time_series':
          renderRainPatternTimeSeries(title, stats, canvas, controls);
          break;
        case 'infographics_visual_storyteller':
          renderInfographicsVisualStoryteller(title, stats, canvas, controls);
          break;
        case 'strip_chart_percentage_segmenter':
          renderStripChartPercentageSegmenter(title, stats, canvas, controls);
          break;
        case 'sleepy_deepy_data_story':
          renderSleepyDeepyDataStory(title, stats, canvas, controls);
          break;
        case 'game_of_hex_puzzle_lab':
          renderGameOfHexPuzzleLab(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Statistical Visualiser';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Tales by Dots and Lines
    function renderTalesDotsLinesIntro(title, stats, canvas, controls) {
      title.textContent = "Dot Plot & Frequency Line Generator";
      let points = [2, 3, 3, 5, 5, 5, 6, 8, 8, 9];
      let showLine = false;

      function updateStats() {
        const n = points.length;
        const freqMap = {};
        for (let i = 1; i <= 10; i++) freqMap[i] = 0;
        points.forEach(p => { if (freqMap[p] !== undefined) freqMap[p]++; });

        let maxF = 0;
        let modes = [];
        for (let k = 1; k <= 10; k++) {
          if (freqMap[k] > maxF) {
            maxF = freqMap[k];
            modes = [k];
          } else if (freqMap[k] === maxF && maxF > 0) {
            modes.push(k);
          }
        }

        const sum = points.reduce((acc, v) => acc + v, 0);
        const mean = n > 0 ? (sum / n).toFixed(2) : "0.00";

        let median = "0.00";
        if (n > 0) {
          const sorted = [...points].sort((a, b) => a - b);
          const mid = Math.floor(n / 2);
          if (n % 2 !== 0) {
            median = sorted[mid].toString();
          } else {
            median = ((sorted[mid - 1] + sorted[mid]) / 2).toFixed(1);
          }
        }

        const modeStr = maxF > 0 ? `${modes.join(', ')} (Freq: ${maxF})` : 'None';

        stats.innerHTML = `
          <div class="stat-pill">Data Count (N): <strong id="dotN">${n}</strong></div>
          <div class="stat-pill">Mean (x̄): <strong id="dotMean" style="color:#a855f7;">${mean}</strong></div>
          <div class="stat-pill">Median (M): <strong id="dotMedian" style="color:#10b981;">${median}</strong></div>
          <div class="stat-pill">Peak Mode: <strong id="dotMode" style="color:#38bdf8;">${modeStr}</strong></div>
        `;
      }

      function updateControls() {
        controls.innerHTML = `
          <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap; width:100%; margin-bottom:8px;">
            <span style="font-size:12px; color:#94a3b8; font-weight:700;">Drop Dot at:</span>
            ${[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(v => `
              <button class="sim-btn" style="padding:4px 9px; min-width:28px; font-weight:700; font-size:12px;" onclick="addPoint(${v})">${v}</button>
            `).join('')}
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap; width:100%;">
            <button class="sim-btn" onclick="addPoint(Math.floor(Math.random() * 10) + 1)">🎲 Random Dot</button>
            <button class="sim-btn" onclick="removeLastPoint()">↩ Remove Last</button>
            <button class="sim-btn" onclick="resetPoints()">🔄 Reset</button>
            <button class="sim-btn ${showLine ? 'active' : ''}" id="btnToggleLine" onclick="toggleLine()">📈 ${showLine ? 'Hide' : 'Show'} Line Graph</button>
          </div>
        `;
      }

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Subtle guide text at top
        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "26");
        tip.setAttribute("fill", "#94a3b8");
        tip.setAttribute("font-size", "11");
        tip.setAttribute("font-weight", "500");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "👆 Click column or tap buttons to drop dots • Toggle line graph for trend";
        svg.appendChild(tip);

        // Axis line
        const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axis.setAttribute("x1", "30");
        axis.setAttribute("y1", "300");
        axis.setAttribute("x2", "430");
        axis.setAttribute("y2", "300");
        axis.setAttribute("stroke", "#64748b");
        axis.setAttribute("stroke-width", "2.5");
        svg.appendChild(axis);

        // Frequency mapping
        const freqMap = {};
        for (let i = 1; i <= 10; i++) freqMap[i] = 0;
        points.forEach(p => { if (freqMap[p] !== undefined) freqMap[p]++; });

        const maxCount = Math.max(...Object.values(freqMap), 1);
        const dy = maxCount > 8 ? Math.max(12, Math.floor(220 / maxCount)) : 22;
        const dotR = Math.min(8.5, Math.max(4.5, Math.floor(dy * 0.4)));

        // Gridlines
        for (let yLevel = 1; yLevel <= Math.min(maxCount, 8); yLevel++) {
          const gridY = 300 - yLevel * dy;
          const gLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          gLine.setAttribute("x1", "35");
          gLine.setAttribute("y1", gridY);
          gLine.setAttribute("x2", "425");
          gLine.setAttribute("y2", gridY);
          gLine.setAttribute("stroke", "rgba(255,255,255,0.05)");
          gLine.setAttribute("stroke-dasharray", "3,3");
          svg.appendChild(gLine);
        }

        // Column interactive click areas and ticks
        for (let i = 1; i <= 10; i++) {
          const x = 35 + i * 36;

          // Clickable column zone
          const colHitbox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          colHitbox.setAttribute("x", x - 17);
          colHitbox.setAttribute("y", "35");
          colHitbox.setAttribute("width", "34");
          colHitbox.setAttribute("height", "265");
          colHitbox.setAttribute("fill", "transparent");
          colHitbox.setAttribute("rx", "4");
          colHitbox.style.cursor = "pointer";
          colHitbox.addEventListener("mouseenter", () => {
            colHitbox.setAttribute("fill", "rgba(99, 102, 241, 0.12)");
          });
          colHitbox.addEventListener("mouseleave", () => {
            colHitbox.setAttribute("fill", "transparent");
          });
          colHitbox.addEventListener("click", () => {
            window.addPoint(i);
          });
          svg.appendChild(colHitbox);

          // Tick marks
          const tick = document.createElementNS("http://www.w3.org/2000/svg", "line");
          tick.setAttribute("x1", x);
          tick.setAttribute("y1", "300");
          tick.setAttribute("x2", x);
          tick.setAttribute("y2", "308");
          tick.setAttribute("stroke", "#94a3b8");
          tick.setAttribute("stroke-width", "2");
          svg.appendChild(tick);

          // Number label
          const lbl = document.createElementNS("http://www.w3.org/2000/svg", "text");
          lbl.setAttribute("x", x);
          lbl.setAttribute("y", "328");
          lbl.setAttribute("fill", "#cbd5e1");
          lbl.setAttribute("font-size", "12");
          lbl.setAttribute("font-weight", "bold");
          lbl.setAttribute("text-anchor", "middle");
          lbl.textContent = i;
          svg.appendChild(lbl);
        }

        // Collect line vertices
        const linePts = [];
        for (let val = 1; val <= 10; val++) {
          const count = freqMap[val];
          const x = 35 + val * 36;
          const y = 300 - count * dy;
          linePts.push({ x, y, count });

          // Stacked dots
          for (let c = 1; c <= count; c++) {
            const dotY = 300 - c * dy;
            const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            dot.setAttribute("cx", x);
            dot.setAttribute("cy", dotY);
            dot.setAttribute("r", dotR);
            dot.setAttribute("fill", "#6366f1");
            dot.setAttribute("stroke", "#c7d2fe");
            dot.setAttribute("stroke-width", "1.5");
            dot.style.cursor = "pointer";
            dot.addEventListener("click", (e) => {
              e.stopPropagation();
              window.removePoint(val);
            });
            svg.appendChild(dot);
          }

          // Count badge on top if non-zero
          if (count > 0) {
            const cntTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
            cntTxt.setAttribute("x", x);
            cntTxt.setAttribute("y", 300 - count * dy - (dotR + 4));
            cntTxt.setAttribute("fill", "#38bdf8");
            cntTxt.setAttribute("font-size", "10");
            cntTxt.setAttribute("font-weight", "bold");
            cntTxt.setAttribute("text-anchor", "middle");
            cntTxt.textContent = count;
            svg.appendChild(cntTxt);
          }
        }

        // Draw Line Graph if enabled
        if (showLine) {
          // Area fill under polygon
          const areaPoints = [
            `${linePts[0].x},300`,
            ...linePts.map(p => `${p.x},${p.y}`),
            `${linePts[linePts.length - 1].x},300`
          ].join(' ');

          const areaPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          areaPoly.setAttribute("points", areaPoints);
          areaPoly.setAttribute("fill", "rgba(56, 189, 248, 0.15)");
          svg.appendChild(areaPoly);

          // Path line
          const pathD = linePts.map((p, idx) => `${idx === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');
          const line = document.createElementNS("http://www.w3.org/2000/svg", "path");
          line.setAttribute("d", pathD);
          line.setAttribute("fill", "none");
          line.setAttribute("stroke", "#38bdf8");
          line.setAttribute("stroke-width", "2.5");
          svg.appendChild(line);

          // Vertex markers
          linePts.forEach(p => {
            const vDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            vDot.setAttribute("cx", p.x);
            vDot.setAttribute("cy", p.y);
            vDot.setAttribute("r", "4");
            vDot.setAttribute("fill", "#38bdf8");
            vDot.setAttribute("stroke", "#070b14");
            vDot.setAttribute("stroke-width", "1.5");
            svg.appendChild(vDot);
          });
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        updateStats();
        updateControls();
      }

      window.addPoint = (val) => {
        if (points.length < 50) {
          points.push(val);
          draw();
        }
      };

      window.removePoint = (val) => {
        const idx = points.lastIndexOf(val);
        if (idx !== -1) {
          points.splice(idx, 1);
          draw();
        }
      };

      window.removeLastPoint = () => {
        if (points.length > 0) {
          points.pop();
          draw();
        }
      };

      window.resetPoints = () => {
        points = [2, 3, 3, 5, 5, 5, 6, 8, 8, 9];
        draw();
      };

      window.toggleLine = () => {
        showLine = !showLine;
        draw();
      };

      draw();
    }

    // 2. The Balancing Act (Mean as Fulcrum)
    function renderBalancingActMeanFulcrum(title, stats, canvas, controls) {
      title.textContent = "The Balancing Act: Arithmetic Mean as the Seesaw Fulcrum";
      let weights = [2, 4, 9];
      let fulcrum = 5.0; // Mean is (2+4+9)/3 = 5.0

      stats.innerHTML = `
        <div class="stat-pill">True Mean: <strong id="meanVal">5.0</strong></div>
        <div class="stat-pill">Fulcrum: <strong id="fulcrumVal">5.0</strong></div>
        <div class="stat-pill">Net Torque: <strong id="torqueVal" style="color:#34d399;">0.00 (Equilibrium)</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Move Fulcrum:</span>
          <input type="range" class="control-slider" min="1" max="9" step="0.1" value="5.0" id="fulcrumSlider">
          <span class="control-val" id="fulcrumText">5.0</span>
        </div>
        <button class="sim-btn" onclick="setBalanced()">Auto-Balance</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const actualMean = weights.reduce((a, b) => a + b, 0) / weights.length;
        const torque = weights.reduce((acc, w) => acc + (w - fulcrum), 0);
        const tiltAngle = Math.max(-15, Math.min(15, torque * 4)); // degrees

        const rad = (tiltAngle * Math.PI) / 180;
        const cx = 40 + fulcrum * 38;
        const cy = 230;

        // Fulcrum stand
        const triangle = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        triangle.setAttribute("points", `${cx},${cy} ${cx - 20},${cy + 45} ${cx + 20},${cy + 45}`);
        triangle.setAttribute("fill", Math.abs(torque) < 0.1 ? "#10b981" : "#f59e0b");
        triangle.setAttribute("stroke", "#f8fafc");
        triangle.setAttribute("stroke-width", "2");
        svg.appendChild(triangle);

        // Ground base
        const ground = document.createElementNS("http://www.w3.org/2000/svg", "line");
        ground.setAttribute("x1", "40");
        ground.setAttribute("y1", cy + 45);
        ground.setAttribute("x2", "420");
        ground.setAttribute("y2", cy + 45);
        ground.setAttribute("stroke", "#64748b");
        ground.setAttribute("stroke-width", "3");
        svg.appendChild(ground);

        // Seesaw Beam rotated around (cx, cy)
        const gBeam = document.createElementNS("http://www.w3.org/2000/svg", "g");
        gBeam.setAttribute("transform", `rotate(${tiltAngle}, ${cx}, ${cy})`);

        const beam = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        beam.setAttribute("x", "40");
        beam.setAttribute("y", cy - 8);
        beam.setAttribute("width", "380");
        beam.setAttribute("height", "16");
        beam.setAttribute("rx", "6");
        beam.setAttribute("fill", "#6366f1");
        beam.setAttribute("stroke", "#818cf8");
        beam.setAttribute("stroke-width", "2");
        gBeam.appendChild(beam);

        // Scale ticks along beam
        for (let i = 1; i <= 9; i++) {
          const bx = 40 + i * 38;
          const tick = document.createElementNS("http://www.w3.org/2000/svg", "line");
          tick.setAttribute("x1", bx);
          tick.setAttribute("y1", cy - 8);
          tick.setAttribute("x2", bx);
          tick.setAttribute("y2", cy + 8);
          tick.setAttribute("stroke", "#e2e8f0");
          tick.setAttribute("stroke-width", "1.5");
          gBeam.appendChild(tick);

          const lbl = document.createElementNS("http://www.w3.org/2000/svg", "text");
          lbl.setAttribute("x", bx);
          lbl.setAttribute("y", cy + 24);
          lbl.setAttribute("fill", "#cbd5e1");
          lbl.setAttribute("font-size", "11");
          lbl.setAttribute("text-anchor", "middle");
          lbl.textContent = i;
          gBeam.appendChild(lbl);
        }

        // Draw weights on beam
        weights.forEach(w => {
          const wx = 40 + w * 38;
          const weightBox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          weightBox.setAttribute("x", wx - 14);
          weightBox.setAttribute("y", cy - 36);
          weightBox.setAttribute("width", "28");
          weightBox.setAttribute("height", "28");
          weightBox.setAttribute("rx", "5");
          weightBox.setAttribute("fill", "#f43f5e");
          weightBox.setAttribute("stroke", "#fda4af");
          weightBox.setAttribute("stroke-width", "2");
          gBeam.appendChild(weightBox);

          const wText = document.createElementNS("http://www.w3.org/2000/svg", "text");
          wText.setAttribute("x", wx);
          wText.setAttribute("y", cy - 18);
          wText.setAttribute("fill", "#fff");
          wText.setAttribute("font-size", "12");
          wText.setAttribute("font-weight", "bold");
          wText.setAttribute("text-anchor", "middle");
          wText.textContent = "1kg";
          gBeam.appendChild(wText);
        });

        svg.appendChild(gBeam);
        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('meanVal').textContent = actualMean.toFixed(1);
        document.getElementById('fulcrumVal').textContent = fulcrum.toFixed(1);
        document.getElementById('torqueVal').textContent = Math.abs(torque) < 0.05 ? "0.00 (Balanced!)" : `${torque > 0 ? '+' : ''}${torque.toFixed(2)}`;
        document.getElementById('torqueVal').style.color = Math.abs(torque) < 0.05 ? "#34d399" : "#f43f5e";
        document.getElementById('fulcrumText').textContent = fulcrum.toFixed(1);
      }

      window.setBalanced = () => {
        fulcrum = 5.0;
        document.getElementById('fulcrumSlider').value = 5.0;
        draw();
      };

      document.getElementById('fulcrumSlider').oninput = (e) => {
        fulcrum = parseFloat(e.target.value);
        draw();
      };

      draw();
    }

    // 3. Unchanging Mean & Shifts
    function renderUnchangingMeanProperties(title, stats, canvas, controls) {
      title.textContent = "Unchanging Mean: Shift (+c) & Scale (×k) Invariance";
      let shift = 0;
      let scale = 1.0;
      const baseData = [4, 6, 8, 10, 12]; // base mean = 8

      stats.innerHTML = `
        <div class="stat-pill">Base Mean: <strong>8.0</strong></div>
        <div class="stat-pill">Transformed Mean: <strong id="transMean" style="color:#fbbf24;">8.0</strong></div>
        <div class="stat-pill">Formula: <strong id="transFormula">1.0 × 8 + 0 = 8.0</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Shift (+c):</span>
          <input type="range" class="control-slider" min="-5" max="10" value="0" id="shiftSlider">
          <span class="control-val" id="shiftText">+0</span>
        </div>
        <div class="control-group">
          <span class="control-label">Scale (×k):</span>
          <input type="range" class="control-slider" min="0.5" max="2.5" step="0.5" value="1.0" id="scaleSlider">
          <span class="control-val" id="scaleText">×1.0</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Transformed data
        const currentData = baseData.map(x => x * scale + shift);
        const currentMean = 8.0 * scale + shift;

        // Number line
        const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axis.setAttribute("x1", "30");
        axis.setAttribute("y1", "200");
        axis.setAttribute("x2", "430");
        axis.setAttribute("y2", "200");
        axis.setAttribute("stroke", "#64748b");
        axis.setAttribute("stroke-width", "2");
        svg.appendChild(axis);

        // Draw points
        currentData.forEach(val => {
          const px = 30 + (val / 40) * 400;
          if (px >= 20 && px <= 440) {
            const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            dot.setAttribute("cx", px);
            dot.setAttribute("cy", "200");
            dot.setAttribute("r", "8");
            dot.setAttribute("fill", "#38bdf8");
            dot.setAttribute("stroke", "#0284c7");
            dot.setAttribute("stroke-width", "2");
            svg.appendChild(dot);
          }
        });

        // Mean indicator arrow
        const mx = 30 + (currentMean / 40) * 400;
        if (mx >= 20 && mx <= 440) {
          const arrow = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          arrow.setAttribute("points", `${mx},182 ${mx - 8},160 ${mx + 8},160`);
          arrow.setAttribute("fill", "#f59e0b");
          svg.appendChild(arrow);

          const meanTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          meanTxt.setAttribute("x", mx);
          meanTxt.setAttribute("y", "148");
          meanTxt.setAttribute("fill", "#fbbf24");
          meanTxt.setAttribute("font-size", "13");
          meanTxt.setAttribute("font-weight", "bold");
          meanTxt.setAttribute("text-anchor", "middle");
          meanTxt.textContent = `Mean = ${currentMean.toFixed(1)}`;
          svg.appendChild(meanTxt);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('transMean').textContent = currentMean.toFixed(1);
        document.getElementById('transFormula').textContent = `${scale.toFixed(1)} × 8 + (${shift}) = ${currentMean.toFixed(1)}`;
        document.getElementById('shiftText').textContent = shift >= 0 ? `+${shift}` : `${shift}`;
        document.getElementById('scaleText').textContent = `×${scale.toFixed(1)}`;
      }

      document.getElementById('shiftSlider').oninput = (e) => {
        shift = parseInt(e.target.value);
        draw();
      };
      document.getElementById('scaleSlider').oninput = (e) => {
        scale = parseFloat(e.target.value);
        draw();
      };

      draw();
    }

    // 4. Outlier Robustness: Mean vs Median
    function renderOutlierRobustnessComparator(title, stats, canvas, controls) {
      title.textContent = "Relatively Unchanged: Mean Sensitivity vs Median Robustness";
      let outlier = 30; // initial dataset: 10, 15, 20, 25, 30

      stats.innerHTML = `
        <div class="stat-pill">Outlier Value: <strong id="outVal">30</strong></div>
        <div class="stat-pill">Arithmetic Mean: <strong id="outMean" style="color:#f43f5e;">20.0</strong></div>
        <div class="stat-pill">Median: <strong id="outMed" style="color:#10b981;">20.0</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Drag 5th Value (Outlier):</span>
          <input type="range" class="control-slider" min="30" max="180" step="5" value="30" id="outlierSlider">
          <span class="control-val" id="outlierValText">30</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const data = [10, 15, 20, 25, outlier];
        const mean = (10 + 15 + 20 + 25 + outlier) / 5;
        const median = 20; // sorted 3rd element is always 20 for outlier >= 25

        // Number line (0 to 200)
        const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axis.setAttribute("x1", "40");
        axis.setAttribute("y1", "220");
        axis.setAttribute("x2", "420");
        axis.setAttribute("y2", "220");
        axis.setAttribute("stroke", "#64748b");
        axis.setAttribute("stroke-width", "2");
        svg.appendChild(axis);

        // Data points
        data.forEach((val, idx) => {
          const px = 40 + (val / 200) * 380;
          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", px);
          dot.setAttribute("cy", "220");
          dot.setAttribute("r", idx === 4 ? "10" : "7");
          dot.setAttribute("fill", idx === 4 ? "#f43f5e" : "#6366f1");
          dot.setAttribute("stroke", "#fff");
          dot.setAttribute("stroke-width", "2");
          svg.appendChild(dot);
        });

        // Median Marker (Green vertical line)
        const medX = 40 + (median / 200) * 380;
        const medLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
        medLine.setAttribute("x1", medX);
        medLine.setAttribute("y1", "120");
        medLine.setAttribute("x2", medX);
        medLine.setAttribute("y2", "240");
        medLine.setAttribute("stroke", "#10b981");
        medLine.setAttribute("stroke-width", "3.5");
        medLine.setAttribute("stroke-dasharray", "6,4");
        svg.appendChild(medLine);

        const medText = document.createElementNS("http://www.w3.org/2000/svg", "text");
        medText.setAttribute("x", medX);
        medText.setAttribute("y", "105");
        medText.setAttribute("fill", "#6ee7b7");
        medText.setAttribute("font-size", "12");
        medText.setAttribute("font-weight", "bold");
        medText.setAttribute("text-anchor", "middle");
        medText.textContent = "MEDIAN = 20 (Unchanged!)";
        svg.appendChild(medText);

        // Mean Marker (Red vertical arrow)
        const meanX = 40 + (mean / 200) * 380;
        const meanArrow = document.createElementNS("http://www.w3.org/2000/svg", "line");
        meanArrow.setAttribute("x1", meanX);
        meanArrow.setAttribute("y1", "160");
        meanArrow.setAttribute("x2", meanX);
        meanArrow.setAttribute("y2", "220");
        meanArrow.setAttribute("stroke", "#f43f5e");
        meanArrow.setAttribute("stroke-width", "3.5");
        svg.appendChild(meanArrow);

        const meanText = document.createElementNS("http://www.w3.org/2000/svg", "text");
        meanText.setAttribute("x", meanX);
        meanText.setAttribute("y", "150");
        meanText.setAttribute("fill", "#fca5a5");
        meanText.setAttribute("font-size", "12");
        meanText.setAttribute("font-weight", "bold");
        meanText.setAttribute("text-anchor", "middle");
        meanText.textContent = `MEAN = ${mean.toFixed(1)}`;
        svg.appendChild(meanText);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('outVal').textContent = outlier;
        document.getElementById('outMean').textContent = mean.toFixed(1);
        document.getElementById('outMed').textContent = "20.0 (Robust!)";
        document.getElementById('outlierValText').textContent = outlier;
      }

      document.getElementById('outlierSlider').oninput = (e) => {
        outlier = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 5. Tinkering with Median (Odd vs Even)
    function renderMedianOrderedRanker(title, stats, canvas, controls) {
      title.textContent = "Tinkering with Median: Odd vs Even Rank Splitting";
      let isEven = false;

      stats.innerHTML = `
        <div class="stat-pill">Count (N): <strong id="medCount">7 (Odd)</strong></div>
        <div class="stat-pill">Rank: <strong id="medRank">(7+1)/2 = 4th Item</strong></div>
        <div class="stat-pill">Median: <strong id="medVal" style="color:#10b981;">18</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnOdd" onclick="setCount(false)">Odd Count (N = 7)</button>
        <button class="sim-btn" id="btnEven" onclick="setCount(true)">Even Count (N = 8)</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const data = isEven ? [6, 9, 14, 18, 22, 28, 32, 40] : [6, 9, 14, 18, 22, 28, 35];
        const n = data.length;
        const boxW = 44;
        const startX = (460 - n * (boxW + 10)) / 2;

        data.forEach((val, i) => {
          const x = startX + i * (boxW + 10);
          const y = 140;
          const isMid = isEven ? (i === 3 || i === 4) : (i === 3);

          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", x);
          rect.setAttribute("y", y);
          rect.setAttribute("width", boxW);
          rect.setAttribute("height", "55");
          rect.setAttribute("rx", "8");
          rect.setAttribute("fill", isMid ? "rgba(16, 185, 129, 0.4)" : "rgba(99, 102, 241, 0.2)");
          rect.setAttribute("stroke", isMid ? "#10b981" : "#6366f1");
          rect.setAttribute("stroke-width", isMid ? "3" : "1.5");
          svg.appendChild(rect);

          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", x + boxW / 2);
          txt.setAttribute("y", y + 34);
          txt.setAttribute("fill", isMid ? "#6ee7b7" : "#e2e8f0");
          txt.setAttribute("font-size", "16");
          txt.setAttribute("font-weight", "bold");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = val;
          svg.appendChild(txt);

          // Rank label
          const rTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          rTxt.setAttribute("x", x + boxW / 2);
          rTxt.setAttribute("y", y + 78);
          rTxt.setAttribute("fill", "#94a3b8");
          rTxt.setAttribute("font-size", "11");
          rTxt.setAttribute("text-anchor", "middle");
          rTxt.textContent = `Rank ${i + 1}`;
          svg.appendChild(rTxt);
        });

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        if (isEven) {
          document.getElementById('medCount').textContent = '8 (Even)';
          document.getElementById('medRank').textContent = 'Avg of 4th (18) & 5th (22)';
          document.getElementById('medVal').textContent = '20.0';
        } else {
          document.getElementById('medCount').textContent = '7 (Odd)';
          document.getElementById('medRank').textContent = '(7+1)/2 = 4th Item';
          document.getElementById('medVal').textContent = '18.0';
        }
      }

      window.setCount = (even) => {
        isEven = even;
        document.getElementById('btnOdd').className = `sim-btn ${!even ? 'active' : ''}`;
        document.getElementById('btnEven').className = `sim-btn ${even ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 6. Finding the Unknown
    function renderFindingUnknownEquationSolver(title, stats, canvas, controls) {
      title.textContent = "Finding the Unknown: Inverse Mean Equation Solver";
      let missingX = 75; // Target mean = 80 for 5 tests, sum = 400. Known 4: 70, 75, 80, 85 (sum=310) => X = 90

      stats.innerHTML = `
        <div class="stat-pill">Target Mean: <strong>80.0</strong></div>
        <div class="stat-pill">Current Test 5 Score: <strong id="unkX">${missingX}</strong></div>
        <div class="stat-pill">Current Mean: <strong id="currMean" style="color:#f59e0b;">77.0</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Tune Score X:</span>
          <input type="range" class="control-slider" min="50" max="100" value="75" id="unkSlider">
          <span class="control-val" id="unkSliderText">75</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const sum = 70 + 75 + 80 + 85 + missingX;
        const mean = sum / 5;
        const isMatched = Math.abs(mean - 80) < 0.1;

        // Balance scales graphic
        svg.innerHTML = `
          <!-- Target Mean Box -->
          <rect x="50" y="80" width="160" height="90" rx="12" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="2"/>
          <text x="130" y="115" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">TARGET MEAN</text>
          <text x="130" y="145" fill="#fff" font-size="24" font-weight="800" text-anchor="middle">80.0</text>
          <text x="130" y="160" fill="#94a3b8" font-size="11" text-anchor="middle">Sum Required: 400</text>

          <!-- Actual Total Sum Box -->
          <rect x="250" y="80" width="160" height="90" rx="12" fill="${isMatched ? 'rgba(16, 185, 129, 0.3)' : 'rgba(244, 63, 94, 0.2)'}" stroke="${isMatched ? '#10b981' : '#f43f5e'}" stroke-width="2"/>
          <text x="330" y="115" fill="${isMatched ? '#6ee7b7' : '#fca5a5'}" font-size="12" font-weight="bold" text-anchor="middle">CURRENT MEAN</text>
          <text x="330" y="145" fill="#fff" font-size="24" font-weight="800" text-anchor="middle">${mean.toFixed(1)}</text>
          <text x="330" y="160" fill="#94a3b8" font-size="11" text-anchor="middle">Total Sum: ${sum} / 400</text>

          <!-- Equation Display -->
          <text x="230" y="240" fill="#e2e8f0" font-size="15" font-weight="bold" text-anchor="middle">
            (70 + 75 + 80 + 85 + X) ÷ 5 = 80
          </text>
          <text x="230" y="275" fill="${isMatched ? '#34d399' : '#fbbf24'}" font-size="16" font-weight="800" text-anchor="middle">
            ${isMatched ? '✓ PERFECT! Required Score X = 90' : `310 + X = 400 ⟹ Needed X = 90 (Current X = ${missingX})`}
          </text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('unkX').textContent = missingX;
        document.getElementById('currMean').textContent = mean.toFixed(1);
        document.getElementById('currMean').style.color = isMatched ? '#34d399' : '#f59e0b';
        document.getElementById('unkSliderText').textContent = missingX;
      }

      document.getElementById('unkSlider').oninput = (e) => {
        missingX = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 7. Mean & Median with Frequencies
    function renderFrequencyTableMeanMedian(title, stats, canvas, controls) {
      title.textContent = "Frequency Distribution: Weighted Mean & Cumulative Median";
      let weights = [10, 20, 30, 40];
      let freqs = [3, 8, 12, 7]; // Total N = 30

      stats.innerHTML = `
        <div class="stat-pill">Total Items (N): <strong id="ftN">30</strong></div>
        <div class="stat-pill">Weighted Mean: <strong id="ftMean" style="color:#38bdf8;">27.67</strong></div>
        <div class="stat-pill">Median Class: <strong id="ftMed" style="color:#10b981;">30</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn" onclick="bumpFreq(1)">+ Count at 20</button>
        <button class="sim-btn" onclick="bumpFreq(2)">+ Count at 30</button>
        <button class="sim-btn" onclick="resetFreqs()">Reset</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        let totalN = 0, sumFX = 0;
        let cf = 0;
        const rows = weights.map((w, i) => {
          const f = freqs[i];
          totalN += f;
          sumFX += w * f;
          cf += f;
          return { w, f, fx: w * f, cf };
        });

        const mean = sumFX / totalN;
        const medianPos = (totalN + 1) / 2;
        let medianVal = 10;
        for (let r of rows) {
          if (r.cf >= medianPos) { medianVal = r.w; break; }
        }

        // Table Header
        svg.innerHTML = `
          <rect x="30" y="30" width="400" height="35" fill="rgba(99, 102, 241, 0.4)" rx="6"/>
          <text x="70" y="52" fill="#c7d2fe" font-size="12" font-weight="bold">Value (x)</text>
          <text x="160" y="52" fill="#c7d2fe" font-size="12" font-weight="bold">Frequency (f)</text>
          <text x="260" y="52" fill="#c7d2fe" font-size="12" font-weight="bold">f · x</text>
          <text x="360" y="52" fill="#c7d2fe" font-size="12" font-weight="bold">Cum. Freq (cf)</text>
        `;

        rows.forEach((r, idx) => {
          const y = 80 + idx * 42;
          const isMed = r.w === medianVal;
          const rowBg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rowBg.setAttribute("x", "30");
          rowBg.setAttribute("y", y);
          rowBg.setAttribute("width", "400");
          rowBg.setAttribute("height", "36");
          rowBg.setAttribute("fill", isMed ? "rgba(16, 185, 129, 0.25)" : (idx % 2 === 0 ? "rgba(255, 255, 255, 0.03)" : "rgba(255, 255, 255, 0.07)"));
          rowBg.setAttribute("stroke", isMed ? "#10b981" : "none");
          rowBg.setAttribute("rx", "4");
          svg.appendChild(rowBg);

          svg.innerHTML += `
            <text x="70" y="${y + 22}" fill="#fff" font-size="13" font-weight="bold">${r.w}</text>
            <text x="160" y="${y + 22}" fill="#38bdf8" font-size="13" font-weight="bold">${r.f}</text>
            <text x="260" y="${y + 22}" fill="#fbbf24" font-size="13">${r.fx}</text>
            <text x="360" y="${y + 22}" fill="#a7f3d0" font-size="13" font-weight="bold">${r.cf}</text>
          `;
        });

        // Summary Bar
        svg.innerHTML += `
          <rect x="30" y="260" width="400" height="50" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#6366f1" stroke-width="1.5"/>
          <text x="50" y="290" fill="#cbd5e1" font-size="13">
            Mean = ${sumFX} ÷ ${totalN} = <tspan fill="#38bdf8" font-weight="bold">${mean.toFixed(2)}</tspan> | Median (Item ${medianPos.toFixed(1)}) = <tspan fill="#34d399" font-weight="bold">${medianVal}</tspan>
          </text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('ftN').textContent = totalN;
        document.getElementById('ftMean').textContent = mean.toFixed(2);
        document.getElementById('ftMed').textContent = medianVal;
      }

      window.bumpFreq = (idx) => {
        freqs[idx]++;
        draw();
      };
      window.resetFreqs = () => {
        freqs = [3, 8, 12, 7];
        draw();
      };

      draw();
    }

    // 8. Spreadsheets
    function renderSpreadsheetFormulaStudio(title, stats, canvas, controls) {
      title.textContent = "Spreadsheets: Interactive Cells, Ranges & Formulas";
      let cellValues = [14, 22, 18, 30, 26];

      stats.innerHTML = `
        <div class="stat-pill">Range: <strong>A1:A5</strong></div>
        <div class="stat-pill">=AVERAGE: <strong id="spAvg" style="color:#38bdf8;">22.0</strong></div>
        <div class="stat-pill">=MEDIAN: <strong id="spMed" style="color:#10b981;">22.0</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn" onclick="modifyCell(0, 5)">A1 +5</button>
        <button class="sim-btn" onclick="modifyCell(3, 10)">A4 +10</button>
        <button class="sim-btn" onclick="resetCells()">Reset Data</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const sum = cellValues.reduce((a, b) => a + b, 0);
        const avg = sum / cellValues.length;
        const sorted = [...cellValues].sort((a, b) => a - b);
        const med = sorted[2];

        // Spreadsheet grid layout
        svg.innerHTML = `
          <!-- Header Row -->
          <rect x="50" y="30" width="40" height="30" fill="#1e293b" stroke="#475569"/>
          <rect x="90" y="30" width="130" height="30" fill="#334155" stroke="#475569"/>
          <text x="155" y="50" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Column A</text>

          <!-- Formula Bar -->
          <rect x="240" y="30" width="190" height="30" fill="#0f172a" stroke="#6366f1" rx="4"/>
          <text x="250" y="50" fill="#a5b4fc" font-size="11" font-family="monospace">fx: =AVERAGE(A1:A5)</text>
        `;

        cellValues.forEach((val, i) => {
          const y = 60 + i * 32;
          svg.innerHTML += `
            <rect x="50" y="${y}" width="40" height="32" fill="#1e293b" stroke="#475569"/>
            <text x="70" y="${y + 20}" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">${i + 1}</text>

            <rect x="90" y="${y}" width="130" height="32" fill="rgba(255, 255, 255, 0.04)" stroke="#475569"/>
            <text x="155" y="${y + 21}" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">${val}</text>
          `;
        });

        // Function Output Cards (Right Side)
        svg.innerHTML += `
          <g transform="translate(240, 75)">
            <rect width="190" height="45" rx="6" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1"/>
            <text x="12" y="20" fill="#a5b4fc" font-size="10" font-weight="bold">=SUM(A1:A5)</text>
            <text x="12" y="37" fill="#fff" font-size="16" font-weight="800">${sum}</text>
          </g>

          <g transform="translate(240, 130)">
            <rect width="190" height="45" rx="6" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4"/>
            <text x="12" y="20" fill="#67e8f9" font-size="10" font-weight="bold">=AVERAGE(A1:A5)</text>
            <text x="12" y="37" fill="#fff" font-size="16" font-weight="800">${avg.toFixed(1)}</text>
          </g>

          <g transform="translate(240, 185)">
            <rect width="190" height="45" rx="6" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981"/>
            <text x="12" y="20" fill="#6ee7b7" font-size="10" font-weight="bold">=MEDIAN(A1:A5)</text>
            <text x="12" y="37" fill="#fff" font-size="16" font-weight="800">${med}</text>
          </g>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('spAvg').textContent = avg.toFixed(1);
        document.getElementById('spMed').textContent = med;
      }

      window.modifyCell = (idx, delta) => {
        cellValues[idx] += delta;
        draw();
      };
      window.resetCells = () => {
        cellValues = [14, 22, 18, 30, 26];
        draw();
      };

      draw();
    }

    // 9. Visualising & Interpreting Data (Scale Integrity)
    function renderDataVisualizationScaleLab(title, stats, canvas, controls) {
      title.textContent = "Data Visualisation: Misleading Truncated Axes vs True Scale";
      let truncated = true;

      stats.innerHTML = `
        <div class="stat-pill">Axis Mode: <strong id="scMode">Truncated Baseline (Starts at 90)</strong></div>
        <div class="stat-pill">Visual Distortion: <strong id="scDistort" style="color:#f43f5e;">Exaggerated ~400%</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnTrunc" onclick="setScaleMode(true)">Truncated Axis (Starts at 90)</button>
        <button class="sim-btn" id="btnZero" onclick="setScaleMode(false)">Honest Axis (Starts at 0)</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const vA = 94; // Product A score
        const vB = 98; // Product B score

        const yBase = 280;
        let hA, hB, yAxisText;

        if (truncated) {
          // Range 90 to 100
          hA = ((vA - 90) / 10) * 180;
          hB = ((vB - 90) / 10) * 180;
          yAxisText = ["90", "95", "100"];
        } else {
          // Range 0 to 100
          hA = (vA / 100) * 180;
          hB = (vB / 100) * 180;
          yAxisText = ["0", "50", "100"];
        }

        // Axis
        svg.innerHTML = `
          <line x1="80" y1="80" x2="80" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
          <line x1="80" y1="${yBase}" x2="380" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
        `;

        if (truncated) {
          // Kink zigzag symbol near origin
          svg.innerHTML += `
            <path d="M 76 265 L 84 260 L 76 255 L 84 250 L 80 245" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
          `;
        }

        // Ticks
        yAxisText.forEach((lbl, idx) => {
          const y = yBase - idx * 90;
          svg.innerHTML += `
            <line x1="72" y1="${y}" x2="80" y2="${y}" stroke="#94a3b8" stroke-width="2"/>
            <text x="62" y="${y + 4}" fill="#cbd5e1" font-size="11" text-anchor="end">${lbl}%</text>
          `;
        });

        // Bar A
        svg.innerHTML += `
          <rect x="130" y="${yBase - hA}" width="70" height="${hA}" fill="rgba(99, 102, 241, 0.7)" stroke="#818cf8" stroke-width="2" rx="4"/>
          <text x="165" y="${yBase - hA - 10}" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">94%</text>
          <text x="165" y="${yBase + 24}" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Brand A</text>
        `;

        // Bar B
        svg.innerHTML += `
          <rect x="250" y="${yBase - hB}" width="70" height="${hB}" fill="rgba(16, 185, 129, 0.7)" stroke="#34d399" stroke-width="2" rx="4"/>
          <text x="285" y="${yBase - hB - 10}" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">98%</text>
          <text x="285" y="${yBase + 24}" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Brand B</text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('scMode').textContent = truncated ? 'Truncated Baseline (Starts at 90)' : 'Honest Baseline (Starts at 0)';
        document.getElementById('scDistort').textContent = truncated ? 'Exaggerated ~400% visual gap!' : 'True 4% difference';
        document.getElementById('scDistort').style.color = truncated ? '#f43f5e' : '#34d399';
      }

      window.setScaleMode = (t) => {
        truncated = t;
        document.getElementById('btnTrunc').className = `sim-btn ${t ? 'active' : ''}`;
        document.getElementById('btnZero').className = `sim-btn ${!t ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 10. Line Graphs & Slopes
    function renderLineGraphSlopeNavigator(title, stats, canvas, controls) {
      title.textContent = "Line Graphs: Tracking Continuous Trajectories & Slopes";
      let activeSeg = 1; // 0: 6AM-10AM, 1: 10AM-2PM, 2: 2PM-6PM

      const pts = [
        { t: "6 AM", val: 18 },
        { t: "10 AM", val: 26 },
        { t: "2 PM", val: 34 },
        { t: "6 PM", val: 34 },
        { t: "10 PM", val: 22 }
      ];

      stats.innerHTML = `
        <div class="stat-pill">Interval: <strong id="lgInterval">10 AM to 2 PM</strong></div>
        <div class="stat-pill">Rate of Change: <strong id="lgSlope" style="color:#34d399;">+2.0°C / hour</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn" onclick="setSeg(0)">6 AM – 10 AM (Morning Rise)</button>
        <button class="sim-btn active" id="btnS1" onclick="setSeg(1)">10 AM – 2 PM (Peak Rise)</button>
        <button class="sim-btn" id="btnS2" onclick="setSeg(2)">2 PM – 6 PM (Plateau Flat)</button>
        <button class="sim-btn" id="btnS3" onclick="setSeg(3)">6 PM – 10 PM (Night Drop)</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const xBase = 60, yBase = 280;

        // Axes
        svg.innerHTML = `
          <line x1="${xBase}" y1="60" x2="${xBase}" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
          <line x1="${xBase}" y1="${yBase}" x2="420" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
        `;

        const coords = pts.map((p, i) => {
          const x = xBase + i * 85;
          const y = yBase - (p.val / 40) * 200;
          return { x, y, ...p };
        });

        // Draw line segments
        for (let i = 0; i < coords.length - 1; i++) {
          const isSelected = i === activeSeg;
          const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", coords[i].x);
          line.setAttribute("y1", coords[i].y);
          line.setAttribute("x2", coords[i+1].x);
          line.setAttribute("y2", coords[i+1].y);
          line.setAttribute("stroke", isSelected ? "#f59e0b" : "#6366f1");
          line.setAttribute("stroke-width", isSelected ? "4.5" : "2.5");
          svg.appendChild(line);
        }

        // Points
        coords.forEach((p, i) => {
          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", p.x);
          dot.setAttribute("cy", p.y);
          dot.setAttribute("r", "6");
          dot.setAttribute("fill", "#fff");
          dot.setAttribute("stroke", "#38bdf8");
          dot.setAttribute("stroke-width", "2");
          svg.appendChild(dot);

          svg.innerHTML += `
            <text x="${p.x}" y="${p.y - 12}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">${p.val}°C</text>
            <text x="${p.x}" y="${yBase + 22}" fill="#cbd5e1" font-size="11" text-anchor="middle">${p.t}</text>
          `;
        });

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const p1 = pts[activeSeg];
        const p2 = pts[activeSeg + 1];
        const dt = 4; // 4 hours
        const dy = p2.val - p1.val;
        const slope = dy / dt;

        document.getElementById('lgInterval').textContent = `${p1.t} to ${p2.t}`;
        document.getElementById('lgSlope').textContent = slope === 0 ? "0.0°C / hr (Constant Temperature)" : `${slope > 0 ? '+' : ''}${slope.toFixed(2)}°C / hr`;
        document.getElementById('lgSlope').style.color = slope > 0 ? "#34d399" : (slope < 0 ? "#f43f5e" : "#fbbf24");
      }

      window.setSeg = (idx) => {
        activeSeg = idx;
        draw();
      };

      draw();
    }

    // 11. Space Jam: Orbital Traffic
    function renderSpaceJamOrbitalTraffic(title, stats, canvas, controls) {
      title.textContent = "Space Jam: Exponential Satellite Traffic in Low Earth Orbit";
      let year = 2024;

      const satData = {
        1960: { sats: 50, debris: 200 },
        1980: { sats: 400, debris: 4500 },
        2000: { sats: 900, debris: 9000 },
        2020: { sats: 3500, debris: 25000 },
        2024: { sats: 10000, debris: 36000 },
        2030: { sats: 25000, debris: 60000 }
      };

      stats.innerHTML = `
        <div class="stat-pill">Year: <strong id="orbYear">2024</strong></div>
        <div class="stat-pill">Active Satellites: <strong id="orbSats" style="color:#38bdf8;">10,000</strong></div>
        <div class="stat-pill">Debris Pieces (>10cm): <strong id="orbDebris" style="color:#f43f5e;">36,000</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Year:</span>
          <input type="range" class="control-slider" min="1960" max="2030" step="10" value="2024" id="yearSlider">
          <span class="control-val" id="yearValText">2024</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -180 400 360");

        // Earth
        const earth = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        earth.setAttribute("cx", "0");
        earth.setAttribute("cy", "0");
        earth.setAttribute("r", "55");
        earth.setAttribute("fill", "#1d4ed8");
        earth.setAttribute("stroke", "#38bdf8");
        earth.setAttribute("stroke-width", "2");
        svg.appendChild(earth);

        // Orbital shells
        const shell1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        shell1.setAttribute("cx", "0");
        shell1.setAttribute("cy", "0");
        shell1.setAttribute("r", "95");
        shell1.setAttribute("fill", "none");
        shell1.setAttribute("stroke", "rgba(99, 102, 241, 0.3)");
        shell1.setAttribute("stroke-dasharray", "4,4");
        svg.appendChild(shell1);

        const shell2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        shell2.setAttribute("cx", "0");
        shell2.setAttribute("cy", "0");
        shell2.setAttribute("r", "140");
        shell2.setAttribute("fill", "none");
        shell2.setAttribute("stroke", "rgba(244, 63, 94, 0.25)");
        shell2.setAttribute("stroke-dasharray", "4,4");
        svg.appendChild(shell2);

        // Density cloud particles based on year
        const closestYear = [1960, 1980, 2000, 2020, 2024, 2030].reduce((prev, curr) => Math.abs(curr - year) < Math.abs(prev - year) ? curr : prev);
        const data = satData[closestYear];
        const particleCount = Math.min(180, Math.floor(data.sats / 120) + 15);

        for (let i = 0; i < particleCount; i++) {
          const angle = Math.random() * 2 * Math.PI;
          const dist = 65 + Math.random() * 85;
          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", dist * Math.cos(angle));
          dot.setAttribute("cy", dist * Math.sin(angle));
          dot.setAttribute("r", Math.random() > 0.8 ? "2.5" : "1.5");
          dot.setAttribute("fill", Math.random() > 0.4 ? "#38bdf8" : "#f43f5e");
          svg.appendChild(dot);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('orbYear').textContent = closestYear;
        document.getElementById('orbSats').textContent = data.sats.toLocaleString();
        document.getElementById('orbDebris').textContent = data.debris.toLocaleString();
        document.getElementById('yearValText').textContent = closestYear;
      }

      document.getElementById('yearSlider').oninput = (e) => {
        year = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 12. Catch the Pattern in Rain (Monsoon Seasonal Curves)
    function renderRainPatternTimeSeries(title, stats, canvas, controls) {
      title.textContent = "Catch the Pattern in Rain: Seasonal Monsoons & Moving Averages";
      let showMA = true;

      const rain = [
        { m: "Jan", v: 15 }, { m: "Feb", v: 20 }, { m: "Mar", v: 25 }, { m: "Apr", v: 45 },
        { m: "May", v: 90 }, { m: "Jun", v: 210 }, { m: "Jul", v: 340 }, { m: "Aug", v: 310 },
        { m: "Sep", v: 180 }, { m: "Oct", v: 80 }, { m: "Nov", v: 30 }, { m: "Dec", v: 15 }
      ];

      stats.innerHTML = `
        <div class="stat-pill">Monsoon Peak: <strong style="color:#38bdf8;">July (340 mm)</strong></div>
        <div class="stat-pill">Smoothing: <strong id="maStatus">3-Month Moving Average Active</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnToggleMA" onclick="toggleMA()">Toggle 3-Month Moving Average</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const xBase = 45, yBase = 290;

        // Bars
        rain.forEach((d, i) => {
          const x = xBase + i * 33;
          const h = (d.v / 360) * 210;
          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", x);
          rect.setAttribute("y", yBase - h);
          rect.setAttribute("width", "22");
          rect.setAttribute("height", h);
          rect.setAttribute("fill", "rgba(6, 182, 212, 0.4)");
          rect.setAttribute("stroke", "#0891b2");
          rect.setAttribute("stroke-width", "1");
          rect.setAttribute("rx", "3");
          svg.appendChild(rect);

          svg.innerHTML += `
            <text x="${x + 11}" y="${yBase + 18}" fill="#94a3b8" font-size="10" text-anchor="middle">${d.m}</text>
          `;
        });

        // 3-Month Moving Average Line
        if (showMA) {
          const maPts = [];
          for (let i = 1; i < rain.length - 1; i++) {
            const ma = (rain[i-1].v + rain[i].v + rain[i+1].v) / 3;
            const x = xBase + i * 33 + 11;
            const y = yBase - (ma / 360) * 210;
            maPts.push({ x, y });
          }

          const pathD = maPts.map((p, idx) => `${idx === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');
          const line = document.createElementNS("http://www.w3.org/2000/svg", "path");
          line.setAttribute("d", pathD);
          line.setAttribute("fill", "none");
          line.setAttribute("stroke", "#fbbf24");
          line.setAttribute("stroke-width", "3");
          svg.appendChild(line);

          maPts.forEach(p => {
            const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            c.setAttribute("cx", p.x);
            c.setAttribute("cy", p.y);
            c.setAttribute("r", "4");
            c.setAttribute("fill", "#f59e0b");
            svg.appendChild(c);
          });
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('maStatus').textContent = showMA ? '3-Month Moving Average Active (Golden Line)' : 'Raw Monthly Bars Only';
      }

      window.toggleMA = () => {
        showMA = !showMA;
        document.getElementById('btnToggleMA').className = `sim-btn ${showMA ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 13. Infographics
    function renderInfographicsVisualStoryteller(title, stats, canvas, controls) {
      title.textContent = "Infographics: Pictograms & Standardized Proportional Icons";
      let iconUnit = 50; // 1 icon = 50 liters
      let totalQty = 350;

      stats.innerHTML = `
        <div class="stat-pill">Total Quantity: <strong id="infoTotal">350 Liters</strong></div>
        <div class="stat-pill">Icon Unit Scale: <strong>1 💧 = 50 Liters</strong></div>
        <div class="stat-pill">Icons Displayed: <strong id="infoCount" style="color:#38bdf8;">7 Icons</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Total Water (L):</span>
          <input type="range" class="control-slider" min="100" max="600" step="50" value="350" id="infoSlider">
          <span class="control-val" id="infoValText">350</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const numIcons = totalQty / iconUnit;

        svg.innerHTML = `
          <text x="230" y="60" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">
            VILLAGE WATER HARVESTING AUDIT
          </text>
          <text x="230" y="85" fill="#94a3b8" font-size="12" text-anchor="middle">
            Key: Each Droplet (💧) = 50 Liters
          </text>
        `;

        // Render icons in a clean grid
        for (let i = 0; i < numIcons; i++) {
          const col = i % 6;
          const row = Math.floor(i / 6);
          const x = 70 + col * 55;
          const y = 140 + row * 65;

          // Water droplet SVG path
          svg.innerHTML += `
            <g transform="translate(${x}, ${y})">
              <path d="M 0 -22 C 12 -5 18 8 18 18 C 18 28 10 36 0 36 C -10 36 -18 28 -18 18 C -18 8 -12 -5 0 -22 Z"
                    fill="rgba(6, 182, 212, 0.7)" stroke="#38bdf8" stroke-width="2"/>
            </g>
          `;
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('infoTotal').textContent = `${totalQty} Liters`;
        document.getElementById('infoCount').textContent = `${numIcons} Droplet Icons`;
        document.getElementById('infoValText').textContent = totalQty;
      }

      document.getElementById('infoSlider').oninput = (e) => {
        totalQty = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 14. What can a Strip Say?
    function renderStripChartPercentageSegmenter(title, stats, canvas, controls) {
      title.textContent = "What can a Strip Say? 100% Segmented Strip Charts";
      let sleep = 8;
      let study = 6;
      let play = 4;
      let others = 6; // sum = 24 hours

      stats.innerHTML = `
        <div class="stat-pill">Total: <strong>24 Hours (100%)</strong></div>
        <div class="stat-pill">Sleep: <strong id="strpSleep">33.3%</strong></div>
        <div class="stat-pill">Study: <strong id="strpStudy">25.0%</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Study Hours:</span>
          <input type="range" class="control-slider" min="2" max="10" value="6" id="studySlider">
          <span class="control-val" id="studyVal">6h</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        others = Math.max(1, 24 - (sleep + study + play));
        const total = sleep + study + play + others;

        const pSleep = (sleep / total) * 100;
        const pStudy = (study / total) * 100;
        const pPlay = (play / total) * 100;
        const pOther = (others / total) * 100;

        const stripW = 380;
        const startX = 40;
        const y = 140;

        const wSleep = (pSleep / 100) * stripW;
        const wStudy = (pStudy / 100) * stripW;
        const wPlay = (pPlay / 100) * stripW;
        const wOther = (pOther / 100) * stripW;

        svg.innerHTML = `
          <text x="230" y="80" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">
            STUDENT 24-HOUR DAILY ROUTINE STRIP
          </text>

          <!-- Outer frame -->
          <rect x="${startX}" y="${y}" width="${stripW}" height="60" rx="8" fill="none" stroke="#64748b" stroke-width="2"/>

          <!-- Sleep Segment -->
          <rect x="${startX}" y="${y}" width="${wSleep}" height="60" fill="#6366f1" rx="6"/>
          <text x="${startX + wSleep/2}" y="${y + 35}" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Sleep (${pSleep.toFixed(0)}%)</text>

          <!-- Study Segment -->
          <rect x="${startX + wSleep}" y="${y}" width="${wStudy}" height="60" fill="#06b6d4"/>
          <text x="${startX + wSleep + wStudy/2}" y="${y + 35}" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Study (${pStudy.toFixed(0)}%)</text>

          <!-- Play Segment -->
          <rect x="${startX + wSleep + wStudy}" y="${y}" width="${wPlay}" height="60" fill="#10b981"/>
          <text x="${startX + wSleep + wStudy + wPlay/2}" y="${y + 35}" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Play (${pPlay.toFixed(0)}%)</text>

          <!-- Others Segment -->
          <rect x="${startX + wSleep + wStudy + wPlay}" y="${y}" width="${wOther}" height="60" fill="#f59e0b" rx="6"/>
          <text x="${startX + wSleep + wStudy + wPlay + wOther/2}" y="${y + 35}" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Others</text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('strpSleep').textContent = `${pSleep.toFixed(1)}%`;
        document.getElementById('strpStudy').textContent = `${pStudy.toFixed(1)}%`;
        document.getElementById('studyVal').textContent = `${study}h`;
      }

      document.getElementById('studySlider').oninput = (e) => {
        study = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 15. Sleepy-Deepy Data Story
    function renderSleepyDeepyDataStory(title, stats, canvas, controls) {
      title.textContent = "Data Story: Sleepy-Deepy (Bivariate Scatter & Correlation)";

      const data = [
        { sleep: 4.5, score: 50 },
        { sleep: 5.5, score: 62 },
        { sleep: 6.0, score: 68 },
        { sleep: 7.0, score: 76 },
        { sleep: 7.5, score: 82 },
        { sleep: 8.0, score: 90 },
        { sleep: 8.5, score: 94 },
        { sleep: 9.0, score: 92 }
      ];

      stats.innerHTML = `
        <div class="stat-pill">Surveyed Students: <strong>8</strong></div>
        <div class="stat-pill">Correlation: <strong style="color:#34d399;">Strong Positive (+0.96)</strong></div>
      `;

      controls.innerHTML = `
        <span style="font-size:12px; color:#cbd5e1;">More sleep hours consistently associate with higher classroom alertness scores.</span>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const xBase = 60, yBase = 280;

        // Axes
        svg.innerHTML = `
          <line x1="${xBase}" y1="50" x2="${xBase}" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
          <line x1="${xBase}" y1="${yBase}" x2="420" y2="${yBase}" stroke="#64748b" stroke-width="2"/>
          <text x="240" y="325" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">Night Sleep Duration (Hours)</text>
          <text x="25" y="160" fill="#cbd5e1" font-size="12" font-weight="bold" transform="rotate(-90 25 160)" text-anchor="middle">Alertness Score</text>
        `;

        // Regression line
        svg.innerHTML += `
          <line x1="${xBase + (4.0/10)*340}" y1="${yBase - (45/100)*220}" x2="${xBase + (9.5/10)*340}" y2="${yBase - (98/100)*220}" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5,4"/>
        `;

        // Points
        data.forEach(p => {
          const px = xBase + (p.sleep / 10) * 340;
          const py = yBase - (p.score / 100) * 220;

          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", px);
          dot.setAttribute("cy", py);
          dot.setAttribute("r", "7");
          dot.setAttribute("fill", "#06b6d4");
          dot.setAttribute("stroke", "#e0f2fe");
          dot.setAttribute("stroke-width", "2");
          svg.appendChild(dot);
        });

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      draw();
    }

    // 16. Game of Hex Puzzle Lab
    function renderGameOfHexPuzzleLab(title, stats, canvas, controls) {
      title.textContent = "It's Puzzle Time: The Game of Hex (No Draws Theorem)";
      let grid = {}; // 'r,c' -> 'red' | 'blue' | null
      let currentTurn = 'red';

      stats.innerHTML = `
        <div class="stat-pill">Current Turn: <strong id="hexTurn" style="color:#f43f5e;">Red (Connect North-South)</strong></div>
        <div class="stat-pill">Game Rule: <strong style="color:#38bdf8;">Ties Mathematically Impossible!</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn" onclick="resetHex()">Clear Board</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const R = 22;
        const dx = R * Math.sqrt(3);
        const dy = R * 1.5;

        // Draw 5x5 hex board
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            const cx = 130 + c * dx + r * (dx / 2);
            const cy = 70 + r * dy;
            const key = `${r},${c}`;
            const state = grid[key];

            const hex = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
            const pts = [];
            for (let a = 0; a < 6; a++) {
              const ang = (a * 60 - 30) * (Math.PI / 180);
              pts.push(`${cx + R * Math.cos(ang)},${cy + R * Math.sin(ang)}`);
            }
            hex.setAttribute("points", pts.join(' '));

            let fill = "rgba(255, 255, 255, 0.08)";
            if (state === 'red') fill = "#f43f5e";
            if (state === 'blue') fill = "#38bdf8";

            hex.setAttribute("fill", fill);
            hex.setAttribute("stroke", "#475569");
            hex.setAttribute("stroke-width", "1.5");
            hex.style.cursor = "pointer";

            hex.onclick = () => {
              if (!grid[key]) {
                grid[key] = currentTurn;
                currentTurn = (currentTurn === 'red') ? 'blue' : 'red';
                draw();
              }
            };

            svg.appendChild(hex);
          }
        }

        // Red Borders (North and South)
        svg.innerHTML += `
          <text x="230" y="35" fill="#f43f5e" font-size="13" font-weight="800" text-anchor="middle">▲ RED GOAL (NORTH) ▲</text>
          <text x="320" y="275" fill="#f43f5e" font-size="13" font-weight="800" text-anchor="middle">▼ RED GOAL (SOUTH) ▼</text>
          <text x="60" y="150" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">◄ BLUE</text>
          <text x="400" y="200" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">BLUE ►</text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('hexTurn').textContent = currentTurn === 'red' ? 'Red (North-South)' : 'Blue (East-West)';
        document.getElementById('hexTurn').style.color = currentTurn === 'red' ? '#f43f5e' : '#38bdf8';
      }

      window.resetHex = () => {
        grid = {};
        currentTurn = 'red';
        draw();
      };

      draw();
    }

    // Initial load
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => loadSlide(0));
    } else {
      loadSlide(0);
    }
    window.addEventListener('load', () => {
      triggerMathRender(document.body);
    });
  </script>
</body>
</html>
"""

def build_html():
    slides_json = json.dumps(SLIDES_DATA)
    final_html = TEMPLATE_HTML.replace("%%SLIDES_JSON%%", slides_json)

    out_path = "public/animations/class8-math-data-handling-dots-lines.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Successfully generated {out_path} ({len(final_html)} bytes).")

if __name__ == "__main__":
    build_html()
