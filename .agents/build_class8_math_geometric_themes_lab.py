import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_geometric_themes_data import SLIDES_DATA

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 11: Exploring Geometric Themes (Fractals & Visualising Solids) Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="triggerMathRender(document.body);"></script>

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
      <span class="header-badge">CLASS 8 • MATHEMATICS • CHAPTER 11</span>
      <span class="header-title">Exploring Geometric Themes: Fractals & Visualising Solids Master Lab</span>
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
            <span id="slideIcon">📐</span>
            <span id="slideHeading">Title Here</span>
          </div>
          <div class="slide-subtitle" id="slideSubheading">Subtitle Here</div>
        </div>

        <div class="avatar-box">
          <div class="avatar-icon">🧑‍🏫</div>
          <div class="avatar-text">
            <span class="avatar-name">Mathematics Mentor:</span>
            <span id="mentorBrief">Welcome to Chapter 11. Let us explore the wonders of recursive fractals and 3D spatial solids!</span>
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
            <span id="simTitle">Interactive Geometric Simulator</span>
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
          <p id="quizSubtitle">Answer all 10 questions to master these geometric concepts.</p>
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
        case 'geometric_themes_explorer':
          renderGeometricThemesExplorer(title, stats, canvas, controls);
          break;
        case 'fractal_zoom_engine':
          renderFractalZoomEngine(title, stats, canvas, controls);
          break;
        case 'sierpinski_carpet_lab':
          renderSierpinskiCarpetLab(title, stats, canvas, controls);
          break;
        case 'sierpinski_gasket_lab':
          renderSierpinskiGasketLab(title, stats, canvas, controls);
          break;
        case 'koch_snowflake_studio':
          renderKochSnowflakeStudio(title, stats, canvas, controls);
          break;
        case 'fractals_in_art_heritage':
          renderFractalsInArtHeritage(title, stats, canvas, controls);
          break;
        case 'solids_euler_polyhedra':
          renderSolidsEulerPolyhedra(title, stats, canvas, controls);
          break;
        case 'spatial_cube_builder':
          renderSpatialCubeBuilder(title, stats, canvas, controls);
          break;
        case 'making_solids_inspector':
          renderMakingSolidsInspector(title, stats, canvas, controls);
          break;
        case 'interactive_net_folder':
          renderInteractiveNetFolder(title, stats, canvas, controls);
          break;
        case 'cube_geodesic_unfolder':
          renderCubeGeodesicUnfolder(title, stats, canvas, controls);
          break;
        case 'plane_representation_studio':
          renderPlaneRepresentationStudio(title, stats, canvas, controls);
          break;
        case 'orthographic_projection_rig':
          renderOrthographicProjectionRig(title, stats, canvas, controls);
          break;
        case 'shadow_caster_lab':
          renderShadowCasterLab(title, stats, canvas, controls);
          break;
        case 'isometric_projection_engine':
          renderIsometricProjectionEngine(title, stats, canvas, controls);
          break;
        case 'isometric_grid_drawer':
          renderIsometricGridDrawer(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Interactive Geometric Visualiser';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Geometric Themes Explorer
    function renderGeometricThemesExplorer(title, stats, canvas, controls) {
      title.textContent = "Geometric Themes: Rotational Symmetry & Order";
      let folds = 6;
      let mode = 'mandala';

      stats.innerHTML = `
        <div class="stat-pill">Order of Symmetry: <strong id="symFoldVal">6-Fold</strong></div>
        <div class="stat-pill">Rotational Angle: <strong id="symAngleVal">60°</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Symmetry Folds:</span>
          <input type="range" class="control-slider" min="3" max="12" value="6" id="foldSlider">
        </div>
        <button class="sim-btn active" id="btnMandala" onclick="setMode('mandala')">Geometric Rosette</button>
        <button class="sim-btn" id="btnCrystalline" onclick="setMode('crystal')">Crystal Lattice</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -200 400 400");

        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
        const angleStep = (2 * Math.PI) / folds;

        for (let i = 0; i < folds; i++) {
          const theta = i * angleStep;
          const deg = (i * 360) / folds;

          if (mode === 'mandala') {
            // Petals and nested circles
            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", `M 0 0 C 40 -80, 80 -120, 0 -160 C -80 -120, -40 -80, 0 0 Z`);
            path.setAttribute("fill", `hsla(${(i * 360) / folds}, 80%, 60%, 0.35)`);
            path.setAttribute("stroke", `hsl(${(i * 360) / folds}, 90%, 65%)`);
            path.setAttribute("stroke-width", "2");
            path.setAttribute("transform", `rotate(${deg})`);
            g.appendChild(path);

            const innerCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            innerCircle.setAttribute("cx", 0);
            innerCircle.setAttribute("cy", -70);
            innerCircle.setAttribute("r", 15);
            innerCircle.setAttribute("fill", "rgba(6, 182, 212, 0.4)");
            innerCircle.setAttribute("stroke", "#38bdf8");
            innerCircle.setAttribute("transform", `rotate(${deg})`);
            g.appendChild(innerCircle);
          } else {
            // Crystalline polygons
            const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
            poly.setAttribute("points", "0,-30 40,-100 0,-170 -40,-100");
            poly.setAttribute("fill", `hsla(${(i * 360) / folds + 180}, 75%, 55%, 0.3)`);
            poly.setAttribute("stroke", "#818cf8");
            poly.setAttribute("stroke-width", "2");
            poly.setAttribute("transform", `rotate(${deg})`);
            g.appendChild(poly);
          }
        }

        // Center hub
        const hub = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        hub.setAttribute("cx", 0);
        hub.setAttribute("cy", 0);
        hub.setAttribute("r", 16);
        hub.setAttribute("fill", "#fbbf24");
        hub.setAttribute("stroke", "#f59e0b");
        hub.setAttribute("stroke-width", "3");
        g.appendChild(hub);

        svg.appendChild(g);
        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('symFoldVal').textContent = `${folds}-Fold`;
        document.getElementById('symAngleVal').textContent = `${(360 / folds).toFixed(1)}°`;
      }

      window.setMode = (m) => {
        mode = m;
        document.getElementById('btnMandala').className = `sim-btn ${m === 'mandala' ? 'active' : ''}`;
        document.getElementById('btnCrystalline').className = `sim-btn ${m === 'crystal' ? 'active' : ''}`;
        draw();
      };

      document.getElementById('foldSlider').oninput = (e) => {
        folds = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 2. Fractal Zoom Engine (Recursive Tree)
    function renderFractalZoomEngine(title, stats, canvas, controls) {
      title.textContent = "Fractal Recursion & Binary Tree Branching";
      let depth = 4;
      let angle = 30;

      stats.innerHTML = `
        <div class="stat-pill">Iteration Depth (N): <strong id="fDepthVal">4</strong></div>
        <div class="stat-pill">Total Branches: <strong id="fBranchVal">31</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Recursion Depth:</span>
          <input type="range" class="control-slider" min="1" max="6" value="4" id="depthSlider">
        </div>
        <div class="control-group">
          <span class="control-label">Branch Angle:</span>
          <input type="range" class="control-slider" min="15" max="50" value="30" id="angleSlider">
          <span class="control-val" id="angleValText">30°</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 500 380");

        let totalBranches = 0;

        function drawBranch(x, y, length, currentAngle, currentDepth) {
          if (currentDepth > depth) return;
          totalBranches++;

          const rad = (currentAngle * Math.PI) / 180;
          const xEnd = x + length * Math.sin(rad);
          const yEnd = y - length * Math.cos(rad);

          const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", x);
          line.setAttribute("y1", y);
          line.setAttribute("x2", xEnd);
          line.setAttribute("y2", yEnd);

          const strokeWidth = Math.max(1, (depth - currentDepth + 1) * 1.8);
          line.setAttribute("stroke-width", strokeWidth);
          line.setAttribute("stroke", `hsl(${140 + currentDepth * 35}, 85%, ${65 - currentDepth * 5}%)`);
          line.setAttribute("stroke-linecap", "round");
          svg.appendChild(line);

          drawBranch(xEnd, yEnd, length * 0.72, currentAngle - angle, currentDepth + 1);
          drawBranch(xEnd, yEnd, length * 0.72, currentAngle + angle, currentDepth + 1);
        }

        drawBranch(250, 360, 95, 0, 1);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('fDepthVal').textContent = depth;
        document.getElementById('fBranchVal').textContent = totalBranches;
        document.getElementById('angleValText').textContent = `${angle}°`;
      }

      document.getElementById('depthSlider').oninput = (e) => {
        depth = parseInt(e.target.value);
        draw();
      };
      document.getElementById('angleSlider').oninput = (e) => {
        angle = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 3. Sierpinski Carpet Lab
    function renderSierpinskiCarpetLab(title, stats, canvas, controls) {
      title.textContent = "Sierpinski Carpet: Subdividing Squares";
      let step = 2;

      stats.innerHTML = `
        <div class="stat-pill">Iteration (n): <strong id="scStepVal">2</strong></div>
        <div class="stat-pill">Solid Squares: <strong id="scCountVal">64</strong></div>
        <div class="stat-pill">Remaining Area: <strong id="scAreaVal">79.01%</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Carpet Iteration:</span>
          <input type="range" class="control-slider" min="0" max="3" value="2" id="scSlider">
          <span class="control-val" id="scSliderText">2</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 360 360");

        // Base square
        const bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        bg.setAttribute("x", "30");
        bg.setAttribute("y", "30");
        bg.setAttribute("width", "300");
        bg.setAttribute("height", "300");
        bg.setAttribute("fill", "#6366f1");
        svg.appendChild(bg);

        function punchHoles(x, y, size, currentLevel) {
          if (currentLevel > step) return;
          const sub = size / 3;

          // Remove center
          const hole = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          hole.setAttribute("x", x + sub);
          hole.setAttribute("y", y + sub);
          hole.setAttribute("width", sub);
          hole.setAttribute("height", sub);
          hole.setAttribute("fill", "#030712");
          hole.setAttribute("stroke", "#0f172a");
          hole.setAttribute("stroke-width", "0.5");
          svg.appendChild(hole);

          // Recurse on remaining 8 squares
          for (let dx = 0; dx < 3; dx++) {
            for (let dy = 0; dy < 3; dy++) {
              if (dx === 1 && dy === 1) continue;
              punchHoles(x + dx * sub, y + dy * sub, sub, currentLevel + 1);
            }
          }
        }

        punchHoles(30, 30, 300, 1);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const count = Math.pow(8, step);
        const areaPct = (Math.pow(8/9, step) * 100).toFixed(2);

        document.getElementById('scStepVal').textContent = step;
        document.getElementById('scCountVal').textContent = count;
        document.getElementById('scAreaVal').textContent = `${areaPct}%`;
        document.getElementById('scSliderText').textContent = step;
      }

      document.getElementById('scSlider').oninput = (e) => {
        step = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 4. Sierpinski Gasket Lab
    function renderSierpinskiGasketLab(title, stats, canvas, controls) {
      title.textContent = "Sierpinski Gasket: The Equilateral Triangle Fractal";
      let step = 3;

      stats.innerHTML = `
        <div class="stat-pill">Iteration (n): <strong id="sgStepVal">3</strong></div>
        <div class="stat-pill">Solid Triangles: <strong id="sgCountVal">27</strong></div>
        <div class="stat-pill">Remaining Area: <strong id="sgAreaVal">42.19%</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Iteration Step:</span>
          <input type="range" class="control-slider" min="0" max="4" value="3" id="sgSlider">
          <span class="control-val" id="sgSliderText">3</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 400 360");

        function drawTriangle(p1, p2, p3, currentLevel) {
          if (currentLevel === step) {
            const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
            poly.setAttribute("points", `${p1.x},${p1.y} ${p2.x},${p2.y} ${p3.x},${p3.y}`);
            poly.setAttribute("fill", "#06b6d4");
            poly.setAttribute("stroke", "#0891b2");
            poly.setAttribute("stroke-width", "0.5");
            svg.appendChild(poly);
            return;
          }

          const mid12 = { x: (p1.x + p2.x) / 2, y: (p1.y + p2.y) / 2 };
          const mid23 = { x: (p2.x + p3.x) / 2, y: (p2.y + p3.y) / 2 };
          const mid31 = { x: (p3.x + p1.x) / 2, y: (p3.y + p1.y) / 2 };

          drawTriangle(p1, mid12, mid31, currentLevel + 1);
          drawTriangle(mid12, p2, mid23, currentLevel + 1);
          drawTriangle(mid31, mid23, p3, currentLevel + 1);
        }

        const top = { x: 200, y: 25 };
        const left = { x: 30, y: 335 };
        const right = { x: 370, y: 335 };

        drawTriangle(top, left, right, 0);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const count = Math.pow(3, step);
        const areaPct = (Math.pow(3/4, step) * 100).toFixed(2);

        document.getElementById('sgStepVal').textContent = step;
        document.getElementById('sgCountVal').textContent = count;
        document.getElementById('sgAreaVal').textContent = `${areaPct}%`;
        document.getElementById('sgSliderText').textContent = step;
      }

      document.getElementById('sgSlider').oninput = (e) => {
        step = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 5. Koch Snowflake Studio
    function renderKochSnowflakeStudio(title, stats, canvas, controls) {
      title.textContent = "Koch Snowflake: Finite Area & Infinite Perimeter";
      let step = 2;

      stats.innerHTML = `
        <div class="stat-pill">Iteration (n): <strong id="ksStepVal">2</strong></div>
        <div class="stat-pill">Segments: <strong id="ksSegVal">48</strong></div>
        <div class="stat-pill">Perimeter: <strong id="ksPerimVal">177.8% P₀</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Iteration Step:</span>
          <input type="range" class="control-slider" min="0" max="3" value="2" id="ksSlider">
          <span class="control-val" id="ksSliderText">2</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 400 380");

        function getPoints(p1, p2, currentLevel) {
          if (currentLevel === 0) return [p1];

          const dx = p2.x - p1.x;
          const dy = p2.y - p1.y;

          const pA = { x: p1.x + dx / 3, y: p1.y + dy / 3 };
          const pB = { x: p1.x + 2 * dx / 3, y: p1.y + 2 * dy / 3 };

          // Peak point
          const sin60 = Math.sin(-Math.PI / 3);
          const cos60 = Math.cos(-Math.PI / 3);
          const rx = pB.x - pA.x;
          const ry = pB.y - pA.y;
          const pPeak = {
            x: pA.x + (rx * cos60 - ry * sin60),
            y: pA.y + (rx * sin60 + ry * cos60)
          };

          return [
            ...getPoints(p1, pA, currentLevel - 1),
            ...getPoints(pA, pPeak, currentLevel - 1),
            ...getPoints(pPeak, pB, currentLevel - 1),
            ...getPoints(pB, p2, currentLevel - 1)
          ];
        }

        const top = { x: 200, y: 35 };
        const right = { x: 350, y: 295 };
        const left = { x: 50, y: 295 };

        const pts = [
          ...getPoints(top, right, step),
          ...getPoints(right, left, step),
          ...getPoints(left, top, step)
        ];

        const pathStr = pts.map((p, idx) => `${idx === 0 ? 'M' : 'L'} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' ') + ' Z';

        const poly = document.createElementNS("http://www.w3.org/2000/svg", "path");
        poly.setAttribute("d", pathStr);
        poly.setAttribute("fill", "rgba(56, 189, 248, 0.35)");
        poly.setAttribute("stroke", "#38bdf8");
        poly.setAttribute("stroke-width", "1.5");
        svg.appendChild(poly);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const segments = 3 * Math.pow(4, step);
        const perimPct = (Math.pow(4/3, step) * 100).toFixed(1);

        document.getElementById('ksStepVal').textContent = step;
        document.getElementById('ksSegVal').textContent = segments;
        document.getElementById('ksPerimVal').textContent = `${perimPct}% P₀`;
        document.getElementById('ksSliderText').textContent = step;
      }

      document.getElementById('ksSlider').oninput = (e) => {
        step = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 6. Fractals in Art & Indian Heritage
    function renderFractalsInArtHeritage(title, stats, canvas, controls) {
      title.textContent = "Fractals in Heritage: Temple Shikharas & Kolam";
      let heritageMode = 'temple';

      stats.innerHTML = `
        <div class="stat-pill">Monument Style: <strong id="heritModeVal">Khajuraho Shikhara</strong></div>
        <div class="stat-pill">Self-Similar Spires: <strong id="heritCountVal">84 Urushringas</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnTemple" onclick="setHeritage('temple')">Khajuraho Shikhara</button>
        <button class="sim-btn" id="btnKolam" onclick="setHeritage('kolam')">Recursive Sikku Kolam</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 420 380");

        if (heritageMode === 'temple') {
          // Main central spire
          function drawShikhara(cx, baseY, w, h, fill, stroke) {
            const p = document.createElementNS("http://www.w3.org/2000/svg", "path");
            p.setAttribute("d", `M ${cx - w/2} ${baseY} Q ${cx - w/2} ${baseY - h*0.75}, ${cx} ${baseY - h} Q ${cx + w/2} ${baseY - h*0.75}, ${cx + w/2} ${baseY} Z`);
            p.setAttribute("fill", fill);
            p.setAttribute("stroke", stroke);
            p.setAttribute("stroke-width", "1.5");
            svg.appendChild(p);

            // Amalaka and Kalasha on top
            const amalaka = document.createElementNS("http://www.w3.org/2000/svg", "ellipse");
            amalaka.setAttribute("cx", cx);
            amalaka.setAttribute("cy", baseY - h);
            amalaka.setAttribute("rx", w * 0.15);
            amalaka.setAttribute("ry", w * 0.06);
            amalaka.setAttribute("fill", "#fbbf24");
            amalaka.setAttribute("stroke", "#f59e0b");
            svg.appendChild(amalaka);
          }

          // Tier 3 sub-spires (outer)
          drawShikhara(90, 340, 50, 110, "rgba(245, 158, 11, 0.25)", "#f59e0b");
          drawShikhara(330, 340, 50, 110, "rgba(245, 158, 11, 0.25)", "#f59e0b");

          // Tier 2 sub-spires
          drawShikhara(135, 340, 70, 180, "rgba(245, 158, 11, 0.35)", "#fbbf24");
          drawShikhara(285, 340, 70, 180, "rgba(245, 158, 11, 0.35)", "#fbbf24");

          // Central master shikhara
          drawShikhara(210, 340, 110, 290, "rgba(217, 119, 6, 0.5)", "#fef08a");

          // Base plinth (Adhisthana)
          const plinth = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          plinth.setAttribute("x", "50");
          plinth.setAttribute("y", "340");
          plinth.setAttribute("width", "320");
          plinth.setAttribute("height", "25");
          plinth.setAttribute("fill", "#475569");
          plinth.setAttribute("stroke", "#64748b");
          svg.appendChild(plinth);

        } else {
          // Traditional Kolam / Rangoli grid of dots with continuous looping knots
          const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

          // Grid dots (pulli)
          for (let r = 0; r < 5; r++) {
            for (let c = 0; c < 5; c++) {
              const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
              dot.setAttribute("cx", 110 + c * 50);
              dot.setAttribute("cy", 90 + r * 50);
              dot.setAttribute("r", "3.5");
              dot.setAttribute("fill", "#f43f5e");
              g.appendChild(dot);
            }
          }

          // Recursive knot loops around dots
          const knotPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
          knotPath.setAttribute("d", "M 210 40 Q 260 40 260 90 Q 260 140 310 140 Q 360 140 360 190 Q 360 240 310 240 Q 260 240 260 290 Q 260 340 210 340 Q 160 340 160 290 Q 160 240 110 240 Q 60 240 60 190 Q 60 140 110 140 Q 160 140 160 90 Q 160 40 210 40 Z");
          knotPath.setAttribute("fill", "none");
          knotPath.setAttribute("stroke", "#38bdf8");
          knotPath.setAttribute("stroke-width", "3");
          g.appendChild(knotPath);

          // Inner diamond knot
          const innerKnot = document.createElementNS("http://www.w3.org/2000/svg", "path");
          innerKnot.setAttribute("d", "M 210 90 L 310 190 L 210 290 L 110 190 Z");
          innerKnot.setAttribute("fill", "rgba(56, 189, 248, 0.15)");
          innerKnot.setAttribute("stroke", "#a855f7");
          innerKnot.setAttribute("stroke-width", "2");
          g.appendChild(innerKnot);

          svg.appendChild(g);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('heritModeVal').textContent = heritageMode === 'temple' ? 'Khajuraho Shikhara' : 'Sikku Kolam';
        document.getElementById('heritCountVal').textContent = heritageMode === 'temple' ? '84 Urushringas' : '5×5 Lattice Loops';
      }

      window.setHeritage = (m) => {
        heritageMode = m;
        document.getElementById('btnTemple').className = `sim-btn ${m === 'temple' ? 'active' : ''}`;
        document.getElementById('btnKolam').className = `sim-btn ${m === 'kolam' ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 7. Solids & Euler's Polyhedra
    function renderSolidsEulerPolyhedra(title, stats, canvas, controls) {
      title.textContent = "Euler's Polyhedra Formula: V - E + F = 2";
      let solid = 'cube';

      const polyhedra = {
        cube: { name: 'Regular Cube', V: 8, E: 12, F: 6 },
        tetrahedron: { name: 'Tetrahedron', V: 4, E: 6, F: 4 },
        octahedron: { name: 'Regular Octahedron', V: 6, E: 12, F: 8 },
        tri_prism: { name: 'Triangular Prism', V: 6, E: 9, F: 5 },
        sq_pyramid: { name: 'Square Pyramid', V: 5, E: 8, F: 5 }
      };

      stats.innerHTML = `
        <div class="stat-pill">Solid: <strong id="eulName">Cube</strong></div>
        <div class="stat-pill">V: <strong id="eulV">8</strong>, E: <strong id="eulE">12</strong>, F: <strong id="eulF">6</strong></div>
        <div class="stat-pill">V - E + F = <strong id="eulRes" style="color:#34d399;">2</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnCube" onclick="setSolid('cube')">Cube</button>
        <button class="sim-btn" id="btnTetra" onclick="setSolid('tetrahedron')">Tetrahedron</button>
        <button class="sim-btn" id="btnOcta" onclick="setSolid('octahedron')">Octahedron</button>
        <button class="sim-btn" id="btnTriPrism" onclick="setSolid('tri_prism')">Tri-Prism</button>
        <button class="sim-btn" id="btnSqPyr" onclick="setSolid('sq_pyramid')">Square Pyramid</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-180 -180 360 360");

        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

        if (solid === 'cube') {
          // Front face
          const front = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          front.setAttribute("points", "-60,-30 40,-30 40,70 -60,70");
          front.setAttribute("fill", "rgba(99, 102, 241, 0.4)");
          front.setAttribute("stroke", "#818cf8");
          front.setAttribute("stroke-width", "2");

          // Top face
          const top = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          top.setAttribute("points", "-60,-30 0,-80 100,-80 40,-30");
          top.setAttribute("fill", "rgba(99, 102, 241, 0.6)");
          top.setAttribute("stroke", "#818cf8");
          top.setAttribute("stroke-width", "2");

          // Right side face
          const side = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          side.setAttribute("points", "40,-30 100,-80 100,20 40,70");
          side.setAttribute("fill", "rgba(99, 102, 241, 0.25)");
          side.setAttribute("stroke", "#818cf8");
          side.setAttribute("stroke-width", "2");

          g.appendChild(top);
          g.appendChild(side);
          g.appendChild(front);

        } else if (solid === 'tetrahedron') {
          const f1 = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          f1.setAttribute("points", "0,-100 -80,50 80,50");
          f1.setAttribute("fill", "rgba(16, 185, 129, 0.35)");
          f1.setAttribute("stroke", "#34d399");
          f1.setAttribute("stroke-width", "2");

          const f2 = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          f2.setAttribute("points", "0,-100 80,50 30,-20");
          f2.setAttribute("fill", "rgba(16, 185, 129, 0.55)");
          f2.setAttribute("stroke", "#34d399");
          f2.setAttribute("stroke-width", "2");

          g.appendChild(f1);
          g.appendChild(f2);

        } else if (solid === 'octahedron') {
          const topPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          topPoly.setAttribute("points", "0,-110 -90,0 0,25 90,0");
          topPoly.setAttribute("fill", "rgba(244, 63, 94, 0.45)");
          topPoly.setAttribute("stroke", "#fb7185");
          topPoly.setAttribute("stroke-width", "2");

          const botPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          botPoly.setAttribute("points", "0,110 -90,0 0,25 90,0");
          botPoly.setAttribute("fill", "rgba(244, 63, 94, 0.3)");
          botPoly.setAttribute("stroke", "#fb7185");
          botPoly.setAttribute("stroke-width", "2");

          g.appendChild(topPoly);
          g.appendChild(botPoly);

        } else if (solid === 'tri_prism') {
          const p1 = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          p1.setAttribute("points", "-60,40 20,40 -20,-60");
          p1.setAttribute("fill", "rgba(6, 182, 212, 0.5)");
          p1.setAttribute("stroke", "#38bdf8");
          p1.setAttribute("stroke-width", "2");

          const sideRect = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          sideRect.setAttribute("points", "20,40 80,0 40,-100 -20,-60");
          sideRect.setAttribute("fill", "rgba(6, 182, 212, 0.3)");
          sideRect.setAttribute("stroke", "#38bdf8");
          sideRect.setAttribute("stroke-width", "2");

          g.appendChild(sideRect);
          g.appendChild(p1);

        } else if (solid === 'sq_pyramid') {
          const base = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          base.setAttribute("points", "-80,40 40,40 90,10 -30,10");
          base.setAttribute("fill", "rgba(245, 158, 11, 0.2)");
          base.setAttribute("stroke", "#f59e0b");
          base.setAttribute("stroke-width", "1.5");

          const face1 = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          face1.setAttribute("points", "0,-90 -80,40 40,40");
          face1.setAttribute("fill", "rgba(245, 158, 11, 0.45)");
          face1.setAttribute("stroke", "#f59e0b");
          face1.setAttribute("stroke-width", "2");

          const face2 = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          face2.setAttribute("points", "0,-90 40,40 90,10");
          face2.setAttribute("fill", "rgba(245, 158, 11, 0.6)");
          face2.setAttribute("stroke", "#f59e0b");
          face2.setAttribute("stroke-width", "2");

          g.appendChild(base);
          g.appendChild(face1);
          g.appendChild(face2);
        }

        svg.appendChild(g);
        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const d = polyhedra[solid];
        document.getElementById('eulName').textContent = d.name;
        document.getElementById('eulV').textContent = d.V;
        document.getElementById('eulE').textContent = d.E;
        document.getElementById('eulF').textContent = d.F;
        document.getElementById('eulRes').textContent = `${d.V} - ${d.E} + ${d.F} = ${d.V - d.E + d.F}`;
      }

      window.setSolid = (s) => {
        solid = s;
        ['btnCube','btnTetra','btnOcta','btnTriPrism','btnSqPyr'].forEach(b => {
          document.getElementById(b).classList.remove('active');
        });
        if (s === 'cube') document.getElementById('btnCube').classList.add('active');
        if (s === 'tetrahedron') document.getElementById('btnTetra').classList.add('active');
        if (s === 'octahedron') document.getElementById('btnOcta').classList.add('active');
        if (s === 'tri_prism') document.getElementById('btnTriPrism').classList.add('active');
        if (s === 'sq_pyramid') document.getElementById('btnSqPyr').classList.add('active');
        draw();
      };

      draw();
    }

    // 8. Spatial Cube Builder & Hidden Faces
    function renderSpatialCubeBuilder(title, stats, canvas, controls) {
      title.textContent = "Build it in Your Imagination: Unit Cubes & Paint";
      let n = 3;

      stats.innerHTML = `
        <div class="stat-pill">Cube Dimension: <strong id="cubeDim">${n}×${n}×${n}</strong></div>
        <div class="stat-pill">Total Unit Cubes: <strong id="totCubes">${n*n*n}</strong></div>
        <div class="stat-pill">Zero Faces Painted: <strong id="zeroPainted">${Math.pow(n-2, 3)}</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Cube Size (n):</span>
          <input type="range" class="control-slider" min="2" max="4" value="3" id="cubeSizeSlider">
          <span class="control-val" id="cubeSizeVal">3</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -200 400 400");

        const s = 140 / n;
        const cos30 = Math.cos(Math.PI / 6);
        const sin30 = Math.sin(Math.PI / 6);

        function drawVoxel(gx, gy, gz) {
          const px = (gx - gy) * s * cos30;
          const py = (gx + gy) * s * sin30 - gz * s;

          // Top face
          const top = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          const p1 = `${px},${py - s}`;
          const p2 = `${px + s * cos30},${py - s + s * sin30}`;
          const p3 = `${px},${py - s + 2 * s * sin30}`;
          const p4 = `${px - s * cos30},${py - s + s * sin30}`;
          top.setAttribute("points", `${p1} ${p2} ${p3} ${p4}`);
          top.setAttribute("fill", "#60a5fa");
          top.setAttribute("stroke", "#1e3a8a");
          top.setAttribute("stroke-width", "1");

          // Left front face
          const left = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          const q1 = p4;
          const q2 = p3;
          const q3 = `${px},${py + s * sin30}`;
          const q4 = `${px - s * cos30},${py}`;
          left.setAttribute("points", `${q1} ${q2} ${q3} ${q4}`);
          left.setAttribute("fill", "#2563eb");
          left.setAttribute("stroke", "#1e3a8a");
          left.setAttribute("stroke-width", "1");

          // Right front face
          const right = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          const r1 = p3;
          const r2 = p2;
          const r3 = `${px + s * cos30},${py}`;
          const r4 = `${px},${py + s * sin30}`;
          right.setAttribute("points", `${r1} ${r2} ${r3} ${r4}`);
          right.setAttribute("fill", "#1d4ed8");
          right.setAttribute("stroke", "#1e3a8a");
          right.setAttribute("stroke-width", "1");

          const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
          g.appendChild(top);
          g.appendChild(left);
          g.appendChild(right);
          return g;
        }

        // Draw voxels back to front
        for (let gz = 0; gz < n; gz++) {
          for (let gy = 0; gy < n; gy++) {
            for (let gx = 0; gx < n; gx++) {
              svg.appendChild(drawVoxel(gx, gy, gz));
            }
          }
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        const total = n * n * n;
        const zero = Math.pow(Math.max(0, n - 2), 3);
        const two = 12 * Math.max(0, n - 2);
        const three = 8;

        document.getElementById('cubeDim').textContent = `${n}×${n}×${n}`;
        document.getElementById('totCubes').textContent = total;
        document.getElementById('zeroPainted').textContent = `${zero} hidden`;
        document.getElementById('cubeSizeVal').textContent = n;
      }

      document.getElementById('cubeSizeSlider').oninput = (e) => {
        n = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 9. Making Solids: Prisms vs Pyramids
    function renderMakingSolidsInspector(title, stats, canvas, controls) {
      title.textContent = "Making Solids: Prisms vs Pyramids Systematics";
      let baseSides = 4;
      let solidFamily = 'prism';

      stats.innerHTML = `
        <div class="stat-pill">Type: <strong id="mspType">Prism</strong></div>
        <div class="stat-pill">Base: <strong id="mspBase">4-gon</strong></div>
        <div class="stat-pill">V: <strong id="mspV">8</strong>, E: <strong id="mspE">12</strong>, F: <strong id="mspF">6</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Base Sides (n):</span>
          <input type="range" class="control-slider" min="3" max="6" value="4" id="baseSidesSlider">
          <span class="control-val" id="baseSidesText">4</span>
        </div>
        <button class="sim-btn active" id="btnFamPrism" onclick="setFamily('prism')">Prism</button>
        <button class="sim-btn" id="btnFamPyramid" onclick="setFamily('pyramid')">Pyramid</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-180 -180 360 360");

        const R = 75;
        const pts = [];
        for (let i = 0; i < baseSides; i++) {
          const a = (i * 2 * Math.PI) / baseSides - Math.PI / 2;
          pts.push({ x: R * Math.cos(a), y: 0.4 * R * Math.sin(a) });
        }

        if (solidFamily === 'prism') {
          // Bottom base
          const bPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          bPoly.setAttribute("points", pts.map(p => `${p.x},${p.y + 70}`).join(' '));
          bPoly.setAttribute("fill", "rgba(99, 102, 241, 0.2)");
          bPoly.setAttribute("stroke", "#6366f1");
          svg.appendChild(bPoly);

          // Top base
          const tPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          tPoly.setAttribute("points", pts.map(p => `${p.x},${p.y - 70}`).join(' '));
          tPoly.setAttribute("fill", "rgba(6, 182, 212, 0.4)");
          tPoly.setAttribute("stroke", "#06b6d4");
          tPoly.setAttribute("stroke-width", "2");
          svg.appendChild(tPoly);

          // Lateral edges
          pts.forEach(p => {
            const edge = document.createElementNS("http://www.w3.org/2000/svg", "line");
            edge.setAttribute("x1", p.x);
            edge.setAttribute("y1", p.y - 70);
            edge.setAttribute("x2", p.x);
            edge.setAttribute("y2", p.y + 70);
            edge.setAttribute("stroke", "#818cf8");
            edge.setAttribute("stroke-width", "1.5");
            svg.appendChild(edge);
          });
        } else {
          // Pyramid base
          const bPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          bPoly.setAttribute("points", pts.map(p => `${p.x},${p.y + 50}`).join(' '));
          bPoly.setAttribute("fill", "rgba(245, 158, 11, 0.3)");
          bPoly.setAttribute("stroke", "#f59e0b");
          bPoly.setAttribute("stroke-width", "2");
          svg.appendChild(bPoly);

          // Apex to base vertices
          pts.forEach(p => {
            const edge = document.createElementNS("http://www.w3.org/2000/svg", "line");
            edge.setAttribute("x1", 0);
            edge.setAttribute("y1", -90);
            edge.setAttribute("x2", p.x);
            edge.setAttribute("y2", p.y + 50);
            edge.setAttribute("stroke", "#fbbf24");
            edge.setAttribute("stroke-width", "2");
            svg.appendChild(edge);
          });

          // Apex point
          const apex = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          apex.setAttribute("cx", 0);
          apex.setAttribute("cy", -90);
          apex.setAttribute("r", 5);
          apex.setAttribute("fill", "#f59e0b");
          svg.appendChild(apex);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        let V, E, F;
        if (solidFamily === 'prism') {
          V = 2 * baseSides;
          E = 3 * baseSides;
          F = baseSides + 2;
        } else {
          V = baseSides + 1;
          E = 2 * baseSides;
          F = baseSides + 1;
        }

        document.getElementById('mspType').textContent = solidFamily === 'prism' ? 'Prism' : 'Pyramid';
        document.getElementById('mspBase').textContent = `${baseSides}-gon`;
        document.getElementById('mspV').textContent = V;
        document.getElementById('mspE').textContent = E;
        document.getElementById('mspF').textContent = F;
        document.getElementById('baseSidesText').textContent = baseSides;
      }

      window.setFamily = (f) => {
        solidFamily = f;
        document.getElementById('btnFamPrism').className = `sim-btn ${f === 'prism' ? 'active' : ''}`;
        document.getElementById('btnFamPyramid').className = `sim-btn ${f === 'pyramid' ? 'active' : ''}`;
        draw();
      };

      document.getElementById('baseSidesSlider').oninput = (e) => {
        baseSides = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 10. Interactive Net Folder
    function renderInteractiveNetFolder(title, stats, canvas, controls) {
      title.textContent = "Practical Aspects of Using a Net: Folding 2D to 3D";
      let foldProgress = 0; // 0 to 100%

      stats.innerHTML = `
        <div class="stat-pill">Fold Status: <strong id="foldPct">0% (Flat 2D Net)</strong></div>
        <div class="stat-pill">Faces: <strong id="netFaces">6 Connected Squares</strong></div>
      `;

      controls.innerHTML = `
        <div class="control-group">
          <span class="control-label">Fold 0% to 100%:</span>
          <input type="range" class="control-slider" min="0" max="100" value="0" id="foldSlider">
          <span class="control-val" id="foldValText">0%</span>
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -200 400 400");

        const s = 60;
        const rad = (foldProgress * 90 / 100) * (Math.PI / 180);
        const cosF = Math.cos(rad);
        const sinF = Math.sin(rad);

        // Center base face (stationary)
        const base = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        base.setAttribute("x", -s/2);
        base.setAttribute("y", -s/2);
        base.setAttribute("width", s);
        base.setAttribute("height", s);
        base.setAttribute("fill", "#6366f1");
        base.setAttribute("stroke", "#a5b4fc");
        base.setAttribute("stroke-width", "2");
        svg.appendChild(base);

        // North face folding up
        const north = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        north.setAttribute("points", `${-s/2},${-s/2} ${s/2},${-s/2} ${s/2},${-s/2 - s * cosF} ${-s/2},${-s/2 - s * cosF}`);
        north.setAttribute("fill", "rgba(99, 102, 241, 0.7)");
        north.setAttribute("stroke", "#c7d2fe");
        north.setAttribute("stroke-width", "2");
        svg.appendChild(north);

        // South face folding down
        const south = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        south.setAttribute("points", `${-s/2},${s/2} ${s/2},${s/2} ${s/2},${s/2 + s * cosF} ${-s/2},${s/2 + s * cosF}`);
        south.setAttribute("fill", "rgba(99, 102, 241, 0.7)");
        south.setAttribute("stroke", "#c7d2fe");
        south.setAttribute("stroke-width", "2");
        svg.appendChild(south);

        // West face folding left
        const west = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        west.setAttribute("points", `${-s/2},${-s/2} ${-s/2},${s/2} ${-s/2 - s * cosF},${s/2} ${-s/2 - s * cosF},${-s/2}`);
        west.setAttribute("fill", "rgba(6, 182, 212, 0.7)");
        west.setAttribute("stroke", "#67e8f9");
        west.setAttribute("stroke-width", "2");
        svg.appendChild(west);

        // East face folding right (with top face attached)
        const east = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        east.setAttribute("points", `${s/2},${-s/2} ${s/2},${s/2} ${s/2 + s * cosF},${s/2} ${s/2 + s * cosF},${-s/2}`);
        east.setAttribute("fill", "rgba(6, 182, 212, 0.7)");
        east.setAttribute("stroke", "#67e8f9");
        east.setAttribute("stroke-width", "2");
        svg.appendChild(east);

        // Far top face attached to East
        const topFace = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        const ex = s/2 + s * cosF;
        topFace.setAttribute("points", `${ex},${-s/2} ${ex},${s/2} ${ex + s * cosF * cosF},${s/2} ${ex + s * cosF * cosF},${-s/2}`);
        topFace.setAttribute("fill", "rgba(245, 158, 11, 0.7)");
        topFace.setAttribute("stroke", "#fde68a");
        topFace.setAttribute("stroke-width", "2");
        svg.appendChild(topFace);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('foldPct').textContent = foldProgress === 100 ? '100% (Closed 3D Cube)' : `${foldProgress}% (Folding Net)`;
        document.getElementById('foldValText').textContent = `${foldProgress}%`;
      }

      document.getElementById('foldSlider').oninput = (e) => {
        foldProgress = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 11. Shortest Paths on a Cube (Spider-Fly Geodesic)
    function renderCubeGeodesicUnfolder(title, stats, canvas, controls) {
      title.textContent = "Shortest Paths: Unfolding Geodesics on a Cube";
      let unfolded = false;

      stats.innerHTML = `
        <div class="stat-pill">View: <strong id="geoView">3D Folded Cube</strong></div>
        <div class="stat-pill">Geodesic Distance: <strong id="geoDist">√5 · s ≈ 2.236 s</strong></div>
        <div class="stat-pill">Edge Path: <strong style="color:#f43f5e;">3.000 s</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btn3DBox" onclick="setUnfold(false)">3D Cube View</button>
        <button class="sim-btn" id="btnUnfoldNet" onclick="setUnfold(true)">Unfold into 2D Net</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-180 -180 360 360");

        if (!unfolded) {
          // 3D Isometric box with surface path
          const front = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          front.setAttribute("points", "-60,0 40,0 40,100 -60,100");
          front.setAttribute("fill", "rgba(99, 102, 241, 0.35)");
          front.setAttribute("stroke", "#818cf8");
          front.setAttribute("stroke-width", "2");

          const top = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          top.setAttribute("points", "-60,0 0,-50 100,-50 40,0");
          top.setAttribute("fill", "rgba(99, 102, 241, 0.55)");
          top.setAttribute("stroke", "#818cf8");
          top.setAttribute("stroke-width", "2");

          const side = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
          side.setAttribute("points", "40,0 100,-50 100,50 40,100");
          side.setAttribute("fill", "rgba(99, 102, 241, 0.2)");
          side.setAttribute("stroke", "#818cf8");
          side.setAttribute("stroke-width", "2");

          svg.appendChild(top);
          svg.appendChild(side);
          svg.appendChild(front);

          // Geodesic path across front and right faces
          const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
          path.setAttribute("d", "M -60 100 L 40 50 L 100 -50");
          path.setAttribute("fill", "none");
          path.setAttribute("stroke", "#34d399");
          path.setAttribute("stroke-width", "4");
          path.setAttribute("stroke-dasharray", "6,4");
          svg.appendChild(path);

          // Spider and Fly markers
          const spider = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          spider.setAttribute("cx", -60);
          spider.setAttribute("cy", 100);
          spider.setAttribute("r", 7);
          spider.setAttribute("fill", "#f59e0b");
          svg.appendChild(spider);

          const fly = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          fly.setAttribute("cx", 100);
          fly.setAttribute("cy", -50);
          fly.setAttribute("r", 7);
          fly.setAttribute("fill", "#f43f5e");
          svg.appendChild(fly);

        } else {
          // Unfolded 2D net showing straight line
          const r1 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r1.setAttribute("x", "-120");
          r1.setAttribute("y", "-40");
          r1.setAttribute("width", "100");
          r1.setAttribute("height", "100");
          r1.setAttribute("fill", "rgba(99, 102, 241, 0.3)");
          r1.setAttribute("stroke", "#818cf8");
          r1.setAttribute("stroke-width", "2");

          const r2 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r2.setAttribute("x", "-20");
          r2.setAttribute("y", "-40");
          r2.setAttribute("width", "100");
          r2.setAttribute("height", "100");
          r2.setAttribute("fill", "rgba(6, 182, 212, 0.3)");
          r2.setAttribute("stroke", "#06b6d4");
          r2.setAttribute("stroke-width", "2");

          svg.appendChild(r1);
          svg.appendChild(r2);

          // Straight line geodesic hypotenuse
          const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", -120);
          line.setAttribute("y1", 60);
          line.setAttribute("x2", 80);
          line.setAttribute("y2", -40);
          line.setAttribute("stroke", "#34d399");
          line.setAttribute("stroke-width", "4");
          svg.appendChild(line);

          // Spider & Fly
          const spider = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          spider.setAttribute("cx", -120);
          spider.setAttribute("cy", 60);
          spider.setAttribute("r", 7);
          spider.setAttribute("fill", "#f59e0b");
          svg.appendChild(spider);

          const fly = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          fly.setAttribute("cx", 80);
          fly.setAttribute("cy", -40);
          fly.setAttribute("r", 7);
          fly.setAttribute("fill", "#f43f5e");
          svg.appendChild(fly);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('geoView').textContent = unfolded ? '2D Flat Net (Straight Line)' : '3D Folded Cube Surface';
      }

      window.setUnfold = (u) => {
        unfolded = u;
        document.getElementById('btn3DBox').className = `sim-btn ${!u ? 'active' : ''}`;
        document.getElementById('btnUnfoldNet').className = `sim-btn ${u ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 12. Plane Representation: Oblique Sketches
    function renderPlaneRepresentationStudio(title, stats, canvas, controls) {
      title.textContent = "Oblique Sketching: Cavalier vs Cabinet Projections";
      let projType = 'cabinet';

      stats.innerHTML = `
        <div class="stat-pill">Type: <strong id="oblType">Cabinet (50% Depth)</strong></div>
        <div class="stat-pill">Receding Angle: <strong>45°</strong></div>
        <div class="stat-pill">Front Face: <strong style="color:#38bdf8;">True Square (100%)</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnCabinet" onclick="setProj('cabinet')">Cabinet (50% Foreshortened)</button>
        <button class="sim-btn" id="btnCavalier" onclick="setProj('cavalier')">Cavalier (100% True Depth)</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-180 -180 360 360");

        const s = 110;
        const depthFactor = projType === 'cabinet' ? 0.5 : 1.0;
        const dx = s * depthFactor * Math.cos(Math.PI / 4);
        const dy = s * depthFactor * Math.sin(Math.PI / 4);

        // Front Face (True Square)
        const front = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        front.setAttribute("x", -s/2 - 20);
        front.setAttribute("y", -s/2 + 20);
        front.setAttribute("width", s);
        front.setAttribute("height", s);
        front.setAttribute("fill", "rgba(99, 102, 241, 0.45)");
        front.setAttribute("stroke", "#818cf8");
        front.setAttribute("stroke-width", "2.5");

        // Top Face
        const top = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        const x1 = -s/2 - 20;
        const y1 = -s/2 + 20;
        top.setAttribute("points", `${x1},${y1} ${x1 + s},${y1} ${x1 + s + dx},${y1 - dy} ${x1 + dx},${y1 - dy}`);
        top.setAttribute("fill", "rgba(6, 182, 212, 0.5)");
        top.setAttribute("stroke", "#06b6d4");
        top.setAttribute("stroke-width", "2");

        // Side Face
        const side = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        side.setAttribute("points", `${x1 + s},${y1} ${x1 + s + dx},${y1 - dy} ${x1 + s + dx},${y1 - dy + s} ${x1 + s},${y1 + s}`);
        side.setAttribute("fill", "rgba(6, 182, 212, 0.25)");
        side.setAttribute("stroke", "#06b6d4");
        side.setAttribute("stroke-width", "2");

        svg.appendChild(top);
        svg.appendChild(side);
        svg.appendChild(front);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('oblType').textContent = projType === 'cabinet' ? 'Cabinet (50% Depth)' : 'Cavalier (100% Depth)';
      }

      window.setProj = (p) => {
        projType = p;
        document.getElementById('btnCabinet').className = `sim-btn ${p === 'cabinet' ? 'active' : ''}`;
        document.getElementById('btnCavalier').className = `sim-btn ${p === 'cavalier' ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 13. Orthographic Multi-View Rig
    function renderOrthographicProjectionRig(title, stats, canvas, controls) {
      title.textContent = "Projections: Front, Top & Side Orthographic Views";
      let activeView = 'all';

      stats.innerHTML = `
        <div class="stat-pill">Active View: <strong id="orthoViewText">3D Isometric + Projections</strong></div>
        <div class="stat-pill">Target Solid: <strong style="color:#a855f7;">L-Shaped Block (4 Cubes)</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnAllViews" onclick="setOrtho('all')">All Views</button>
        <button class="sim-btn" id="btnTopView" onclick="setOrtho('top')">Top View (Plan)</button>
        <button class="sim-btn" id="btnFrontView" onclick="setOrtho('front')">Front View (Elevation)</button>
        <button class="sim-btn" id="btnSideView" onclick="setOrtho('side')">Side View (Profile)</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        if (activeView === 'all') {
          // Top View (top-left)
          const gTop = document.createElementNS("http://www.w3.org/2000/svg", "g");
          gTop.innerHTML = `
            <text x="75" y="30" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">TOP VIEW (PLAN)</text>
            <rect x="35" y="45" width="80" height="40" fill="rgba(6, 182, 212, 0.4)" stroke="#38bdf8" stroke-width="2"/>
            <line x1="75" y1="45" x2="75" y2="85" stroke="#38bdf8" stroke-width="1.5"/>
          `;
          svg.appendChild(gTop);

          // Front View (bottom-left)
          const gFront = document.createElementNS("http://www.w3.org/2000/svg", "g");
          gFront.innerHTML = `
            <text x="75" y="140" fill="#a855f7" font-size="12" font-weight="bold" text-anchor="middle">FRONT VIEW (ELEVATION)</text>
            <path d="M 35 155 L 75 155 L 75 195 L 115 195 L 115 235 L 35 235 Z" fill="rgba(168, 85, 247, 0.4)" stroke="#c084fc" stroke-width="2"/>
            <line x1="35" y1="195" x2="75" y2="195" stroke="#c084fc" stroke-width="1.5"/>
            <line x1="75" y1="195" x2="75" y2="235" stroke="#c084fc" stroke-width="1.5"/>
          `;
          svg.appendChild(gFront);

          // Side View (bottom-center)
          const gSide = document.createElementNS("http://www.w3.org/2000/svg", "g");
          gSide.innerHTML = `
            <text x="210" y="140" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">SIDE VIEW (PROFILE)</text>
            <rect x="190" y="155" width="40" height="80" fill="rgba(16, 185, 129, 0.4)" stroke="#34d399" stroke-width="2"/>
            <line x1="190" y1="195" x2="230" y2="195" stroke="#34d399" stroke-width="1.5"/>
          `;
          svg.appendChild(gSide);

          // 3D Isometric View (right)
          const g3D = document.createElementNS("http://www.w3.org/2000/svg", "g");
          g3D.innerHTML = `
            <text x="350" y="50" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">3D SOLID</text>
            <!-- L block isometric drawing -->
            <polygon points="320,110 355,90 355,140 320,160" fill="rgba(168, 85, 247, 0.6)" stroke="#c084fc" stroke-width="1.5"/>
            <polygon points="355,90 390,110 390,160 355,140" fill="rgba(168, 85, 247, 0.35)" stroke="#c084fc" stroke-width="1.5"/>
            <polygon points="320,110 355,90 390,110 355,130" fill="rgba(6, 182, 212, 0.6)" stroke="#38bdf8" stroke-width="1.5"/>
            
            <polygon points="355,140 390,160 390,210 355,190" fill="rgba(168, 85, 247, 0.35)" stroke="#c084fc" stroke-width="1.5"/>
            <polygon points="320,160 355,140 355,190 320,210" fill="rgba(168, 85, 247, 0.6)" stroke="#c084fc" stroke-width="1.5"/>
            <polygon points="355,190 390,210 355,230 320,210" fill="rgba(6, 182, 212, 0.6)" stroke="#38bdf8" stroke-width="1.5"/>

            <polygon points="355,140 390,120 425,140 390,160" fill="rgba(6, 182, 212, 0.6)" stroke="#38bdf8" stroke-width="1.5"/>
            <polygon points="390,160 425,140 425,190 390,210" fill="rgba(168, 85, 247, 0.35)" stroke="#c084fc" stroke-width="1.5"/>
          `;
          svg.appendChild(g3D);

        } else if (activeView === 'top') {
          svg.innerHTML = `
            <text x="230" y="60" fill="#38bdf8" font-size="18" font-weight="bold" text-anchor="middle">TOP VIEW (LOOKING FROM ABOVE)</text>
            <rect x="150" y="110" width="160" height="80" fill="rgba(6, 182, 212, 0.5)" stroke="#38bdf8" stroke-width="3"/>
            <line x1="230" y1="110" x2="230" y2="190" stroke="#38bdf8" stroke-width="2"/>
            <text x="230" y="240" fill="#94a3b8" font-size="14" text-anchor="middle">Shows Width and Depth: 2 Unit Squares Across</text>
          `;
        } else if (activeView === 'front') {
          svg.innerHTML = `
            <text x="230" y="50" fill="#c084fc" font-size="18" font-weight="bold" text-anchor="middle">FRONT VIEW (EYE LEVEL ELEVATION)</text>
            <path d="M 150 100 L 230 100 L 230 170 L 310 170 L 310 240 L 150 240 Z" fill="rgba(168, 85, 247, 0.5)" stroke="#c084fc" stroke-width="3"/>
            <line x1="150" y1="170" x2="230" y2="170" stroke="#c084fc" stroke-width="2"/>
            <line x1="230" y1="170" x2="230" y2="240" stroke="#c084fc" stroke-width="2"/>
            <text x="230" y="280" fill="#94a3b8" font-size="14" text-anchor="middle">Shows the Distinct L-Shape Step Silhouette</text>
          `;
        } else if (activeView === 'side') {
          svg.innerHTML = `
            <text x="230" y="50" fill="#34d399" font-size="18" font-weight="bold" text-anchor="middle">SIDE VIEW (PROFILE FROM RIGHT)</text>
            <rect x="190" y="90" width="80" height="160" fill="rgba(16, 185, 129, 0.5)" stroke="#34d399" stroke-width="3"/>
            <line x1="190" y1="170" x2="270" y2="170" stroke="#34d399" stroke-width="2"/>
            <text x="230" y="290" fill="#94a3b8" font-size="14" text-anchor="middle">Shows 1 Unit Wide by 2 Units High</text>
          `;
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('orthoViewText').textContent = activeView.toUpperCase();
      }

      window.setOrtho = (v) => {
        activeView = v;
        ['btnAllViews', 'btnTopView', 'btnFrontView', 'btnSideView'].forEach(b => {
          document.getElementById(b).classList.remove('active');
        });
        if (v === 'all') document.getElementById('btnAllViews').classList.add('active');
        if (v === 'top') document.getElementById('btnTopView').classList.add('active');
        if (v === 'front') document.getElementById('btnFrontView').classList.add('active');
        if (v === 'side') document.getElementById('btnSideView').classList.add('active');
        draw();
      };

      draw();
    }

    // 14. Shadow Caster Lab
    function renderShadowCasterLab(title, stats, canvas, controls) {
      title.textContent = "Shadows: 2D Silhouettes Cast by 3D Solids";
      let shape = 'cylinder';
      let lightAngle = 90; // 90 = top, 45 = oblique, 0 = side

      stats.innerHTML = `
        <div class="stat-pill">Solid: <strong id="shSolidText">Cylinder</strong></div>
        <div class="stat-pill">Light Direction: <strong id="shAngleText">Directly Overhead (90°)</strong></div>
        <div class="stat-pill">Shadow Shape: <strong id="shShapeText" style="color:#fbbf24;">Circle</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnShCyl" onclick="setShShape('cylinder')">Cylinder</button>
        <button class="sim-btn" id="btnShCone" onclick="setShShape('cone')">Cone</button>
        <button class="sim-btn" id="btnShSphere" onclick="setShShape('sphere')">Sphere</button>
        <button class="sim-btn" id="btnShCube" onclick="setShShape('cube')">Cube</button>
        <div class="control-group" style="margin-left:auto;">
          <span class="control-label">Light Angle:</span>
          <input type="range" class="control-slider" min="15" max="90" value="90" id="lightAngleSlider">
        </div>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -180 400 360");

        // Light bulb source
        const rad = (lightAngle * Math.PI) / 180;
        const lx = -140 * Math.cos(rad);
        const ly = -140 * Math.sin(rad);

        const bulb = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        bulb.setAttribute("cx", lx);
        bulb.setAttribute("cy", ly);
        bulb.setAttribute("r", "12");
        bulb.setAttribute("fill", "#fef08a");
        bulb.setAttribute("stroke", "#f59e0b");
        bulb.setAttribute("stroke-width", "3");
        svg.appendChild(bulb);

        // Ground line
        const ground = document.createElementNS("http://www.w3.org/2000/svg", "line");
        ground.setAttribute("x1", "-180");
        ground.setAttribute("y1", "120");
        ground.setAttribute("x2", "180");
        ground.setAttribute("y2", "120");
        ground.setAttribute("stroke", "#475569");
        ground.setAttribute("stroke-width", "3");
        svg.appendChild(ground);

        // Draw 3D Solid in center
        const gSolid = document.createElementNS("http://www.w3.org/2000/svg", "g");
        if (shape === 'cylinder') {
          gSolid.innerHTML = `
            <ellipse cx="0" cy="90" rx="35" ry="12" fill="rgba(99, 102, 241, 0.4)" stroke="#818cf8" stroke-width="2"/>
            <rect x="-35" y="0" width="70" height="90" fill="rgba(99, 102, 241, 0.6)" stroke="#818cf8" stroke-width="2"/>
            <ellipse cx="0" cy="0" rx="35" ry="12" fill="rgba(165, 180, 252, 0.8)" stroke="#818cf8" stroke-width="2"/>
          `;
        } else if (shape === 'cone') {
          gSolid.innerHTML = `
            <ellipse cx="0" cy="90" rx="40" ry="14" fill="rgba(16, 185, 129, 0.4)" stroke="#34d399" stroke-width="2"/>
            <polygon points="-40,90 0,-10 40,90" fill="rgba(16, 185, 129, 0.6)" stroke="#34d399" stroke-width="2"/>
          `;
        } else if (shape === 'sphere') {
          gSolid.innerHTML = `
            <circle cx="0" cy="45" r="45" fill="rgba(244, 63, 94, 0.6)" stroke="#fb7185" stroke-width="2"/>
          `;
        } else if (shape === 'cube') {
          gSolid.innerHTML = `
            <rect x="-35" y="20" width="70" height="70" fill="rgba(245, 158, 11, 0.6)" stroke="#fbbf24" stroke-width="2"/>
          `;
        }
        svg.appendChild(gSolid);

        // Ground shadow projection
        const shadow = document.createElementNS("http://www.w3.org/2000/svg", "ellipse");
        const shadowOffset = (90 - lightAngle) * 1.5;
        const shadowWidth = shape === 'cylinder' && lightAngle < 45 ? 65 : 45;
        shadow.setAttribute("cx", shadowOffset);
        shadow.setAttribute("cy", "125");
        shadow.setAttribute("rx", shadowWidth + (90 - lightAngle) * 0.4);
        shadow.setAttribute("ry", "10");
        shadow.setAttribute("fill", "rgba(0, 0, 0, 0.65)");
        svg.appendChild(shadow);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        // Update stats
        let shadowResult = "";
        if (shape === 'cylinder') {
          shadowResult = lightAngle > 75 ? "Circular Silhouette" : "Rectangular / Oval Shadow";
        } else if (shape === 'cone') {
          shadowResult = lightAngle > 75 ? "Circular with Center Dot" : "Triangular Shadow";
        } else if (shape === 'sphere') {
          shadowResult = "Always Circular / Elliptical";
        } else if (shape === 'cube') {
          shadowResult = lightAngle > 75 ? "Square Shadow" : "Hexagonal / Trapezoidal";
        }

        document.getElementById('shSolidText').textContent = shape.toUpperCase();
        document.getElementById('shAngleText').textContent = `${lightAngle}° Light Elevation`;
        document.getElementById('shShapeText').textContent = shadowResult;
      }

      window.setShShape = (s) => {
        shape = s;
        ['btnShCyl', 'btnShCone', 'btnShSphere', 'btnShCube'].forEach(b => {
          document.getElementById(b).classList.remove('active');
        });
        if (s === 'cylinder') document.getElementById('btnShCyl').classList.add('active');
        if (s === 'cone') document.getElementById('btnShCone').classList.add('active');
        if (s === 'sphere') document.getElementById('btnShSphere').classList.add('active');
        if (s === 'cube') document.getElementById('btnShCube').classList.add('active');
        draw();
      };

      document.getElementById('lightAngleSlider').oninput = (e) => {
        lightAngle = parseInt(e.target.value);
        draw();
      };

      draw();
    }

    // 15. Isometric Projection Engine
    function renderIsometricProjectionEngine(title, stats, canvas, controls) {
      title.textContent = "Isometric Projections: 30° Axis & 120° Symmetry";
      let showGrid = true;

      stats.innerHTML = `
        <div class="stat-pill">Axis Angles: <strong style="color:#38bdf8;">120° Spacing</strong></div>
        <div class="stat-pill">Receding Baseline: <strong style="color:#fbbf24;">30° to Horizontal</strong></div>
        <div class="stat-pill">Parallel Edges: <strong style="color:#34d399;">Never Converge</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnIsoToggleGrid" onclick="toggleIsoGrid()">Toggle Isometric Grid Lines</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "-200 -200 400 400");

        if (showGrid) {
          const gGrid = document.createElementNS("http://www.w3.org/2000/svg", "g");
          gGrid.setAttribute("stroke", "rgba(255, 255, 255, 0.08)");
          gGrid.setAttribute("stroke-width", "1");

          // Draw triangular isometric lattice lines
          for (let y = -180; y <= 180; y += 30) {
            const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
            l1.setAttribute("x1", -200);
            l1.setAttribute("y1", y);
            l1.setAttribute("x2", 200);
            l1.setAttribute("y2", y + 400 * Math.tan(Math.PI / 6));
            gGrid.appendChild(l1);

            const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
            l2.setAttribute("x1", 200);
            l2.setAttribute("y1", y);
            l2.setAttribute("x2", -200);
            l2.setAttribute("y2", y + 400 * Math.tan(Math.PI / 6));
            gGrid.appendChild(l2);
          }
          svg.appendChild(gGrid);
        }

        // Horizontal baseline
        const base = document.createElementNS("http://www.w3.org/2000/svg", "line");
        base.setAttribute("x1", "-160");
        base.setAttribute("y1", "40");
        base.setAttribute("x2", "160");
        base.setAttribute("y2", "40");
        base.setAttribute("stroke", "#64748b");
        base.setAttribute("stroke-dasharray", "4,4");
        svg.appendChild(base);

        // Three Isometric Axes (Z vertical, X at 30 deg, Y at 150 deg)
        const L = 140;
        const cos30 = Math.cos(Math.PI / 6);
        const sin30 = Math.sin(Math.PI / 6);

        // Z axis (vertical)
        const axisZ = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axisZ.setAttribute("x1", 0);
        axisZ.setAttribute("y1", 40);
        axisZ.setAttribute("x2", 0);
        axisZ.setAttribute("y2", 40 - L);
        axisZ.setAttribute("stroke", "#f43f5e");
        axisZ.setAttribute("stroke-width", "3");
        svg.appendChild(axisZ);

        // X axis (30 deg right)
        const axisX = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axisX.setAttribute("x1", 0);
        axisX.setAttribute("y1", 40);
        axisX.setAttribute("x2", L * cos30);
        axisX.setAttribute("y2", 40 - L * sin30);
        axisX.setAttribute("stroke", "#38bdf8");
        axisX.setAttribute("stroke-width", "3");
        svg.appendChild(axisX);

        // Y axis (30 deg left)
        const axisY = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axisY.setAttribute("x1", 0);
        axisY.setAttribute("y1", 40);
        axisY.setAttribute("x2", -L * cos30);
        axisY.setAttribute("y2", 40 - L * sin30);
        axisY.setAttribute("stroke", "#10b981");
        axisY.setAttribute("stroke-width", "3");
        svg.appendChild(axisY);

        // Arc annotations
        svg.innerHTML += `
          <text x="15" y="-90" fill="#f43f5e" font-size="14" font-weight="bold">Z (Vertical)</text>
          <text x="115" y="-15" fill="#38bdf8" font-size="14" font-weight="bold">X (+30°)</text>
          <text x="-155" y="-15" fill="#10b981" font-size="14" font-weight="bold">Y (+30°)</text>
          <text x="35" y="15" fill="#fbbf24" font-size="12" font-weight="bold">120°</text>
          <text x="-55" y="15" fill="#fbbf24" font-size="12" font-weight="bold">120°</text>
        `;

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      window.toggleIsoGrid = () => {
        showGrid = !showGrid;
        document.getElementById('btnIsoToggleGrid').className = `sim-btn ${showGrid ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // 16. Drawing on Isometric Grids (Dot Paper Studio)
    function renderIsometricGridDrawer(title, stats, canvas, controls) {
      title.textContent = "Isometric Dot Paper: 3D Blocks & Directional Shading";
      let shadeMode = true;

      stats.innerHTML = `
        <div class="stat-pill">Lattice Type: <strong style="color:#06b6d4;">Equilateral Triangular</strong></div>
        <div class="stat-pill">Face Shading: <strong id="shadeStatus">Top (Light), Front (Medium), Side (Dark)</strong></div>
      `;

      controls.innerHTML = `
        <button class="sim-btn active" id="btnToggleShade" onclick="toggleShading()">Toggle 3D Surface Shading</button>
      `;

      function draw() {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 440 380");

        // Triangular isometric dot array
        const gDots = document.createElementNS("http://www.w3.org/2000/svg", "g");
        for (let row = 0; row < 12; row++) {
          const y = 30 + row * 28;
          const xOffset = (row % 2 === 0) ? 20 : 36;
          for (let col = 0; col < 14; col++) {
            const x = xOffset + col * 32;
            const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            dot.setAttribute("cx", x);
            dot.setAttribute("cy", y);
            dot.setAttribute("r", "2");
            dot.setAttribute("fill", "rgba(255, 255, 255, 0.25)");
            gDots.appendChild(dot);
          }
        }
        svg.appendChild(gDots);

        // Stepped Block drawn cleanly along isometric dots
        const gBlock = document.createElementNS("http://www.w3.org/2000/svg", "g");

        // Color definitions based on shading mode
        const topFill = shadeMode ? "#93c5fd" : "none";
        const frontFill = shadeMode ? "#3b82f6" : "none";
        const sideFill = shadeMode ? "#1d4ed8" : "none";

        // Top faces
        gBlock.innerHTML = `
          <!-- Top faces (Light) -->
          <polygon points="180,114 212,96 244,114 212,132" fill="${topFill}" stroke="#60a5fa" stroke-width="2"/>
          <polygon points="212,132 244,114 276,132 244,150" fill="${topFill}" stroke="#60a5fa" stroke-width="2"/>
          <polygon points="244,150 276,132 308,150 276,168" fill="${topFill}" stroke="#60a5fa" stroke-width="2"/>

          <!-- Front Faces (Medium) -->
          <polygon points="180,114 212,132 212,188 180,170" fill="${frontFill}" stroke="#3b82f6" stroke-width="2"/>
          <polygon points="212,188 244,206 244,262 212,244" fill="${frontFill}" stroke="#3b82f6" stroke-width="2"/>
          <polygon points="244,206 276,224 276,280 244,262" fill="${frontFill}" stroke="#3b82f6" stroke-width="2"/>

          <!-- Side Faces (Dark) -->
          <polygon points="276,168 308,150 308,206 276,224" fill="${sideFill}" stroke="#1d4ed8" stroke-width="2"/>
          <polygon points="276,224 308,206 308,262 276,280" fill="${sideFill}" stroke="#1d4ed8" stroke-width="2"/>
        `;
        svg.appendChild(gBlock);

        canvas.innerHTML = '';
        canvas.appendChild(svg);

        document.getElementById('shadeStatus').textContent = shadeMode ? 'Top (Light), Front (Medium), Side (Dark)' : 'Wireframe Only';
      }

      window.toggleShading = () => {
        shadeMode = !shadeMode;
        document.getElementById('btnToggleShade').className = `sim-btn ${shadeMode ? 'active' : ''}`;
        draw();
      };

      draw();
    }

    // Initial load
    window.onload = () => {
      loadSlide(0);
    };
  </script>
</body>
</html>
"""

def build_html():
    slides_json = json.dumps(SLIDES_DATA)
    final_html = TEMPLATE_HTML.replace("%%SLIDES_JSON%%", slides_json)

    out_path = "public/animations/class8-math-geometric-themes-solids.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Successfully generated {out_path} ({len(final_html)} bytes).")

if __name__ == "__main__":
    build_html()
