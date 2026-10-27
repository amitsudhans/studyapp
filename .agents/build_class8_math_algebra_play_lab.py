# Class 8 Mathematics Chapter 13: Algebra Play
# Master Builder Script: Compiles 20-slide laboratory into public/animations/class8-math-algebra-play.html

import json
import sys
sys.path.insert(0, '.agents')
from class8_math_algebra_play_data import SLIDES_DATA

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 13: Algebra Play Master Lab</title>
  
  <!-- KaTeX CSS & JS with safe early trigger definition -->
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
      overflow-x: hidden;
    }

    /* Top Navigation Header */
    header.lab-header {
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(99, 102, 241, 0.25);
      padding: 12px 24px;
      position: sticky;
      top: 0;
      z-index: 50;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .brand-area {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 0 15px rgba(99, 102, 241, 0.4);
    }

    .brand-title h1 {
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(to right, #ffffff, #c7d2fe);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-title p {
      font-size: 11px;
      color: var(--accent-cyan);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .slide-badge {
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid rgba(99, 102, 241, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      color: #c7d2fe;
    }

    .btn-nav {
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-main);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .btn-nav:hover:not(:disabled) {
      background: var(--accent-indigo);
      border-color: var(--accent-indigo);
      transform: translateY(-1px);
    }

    .btn-nav:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    /* Main Container */
    main.lab-container {
      flex: 1;
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    /* Two-column Lesson Grid */
    .lesson-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 24px;
      align-items: start;
    }

    @media (max-width: 1024px) {
      .lesson-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Theory Card */
    .theory-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .slide-header {
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 14px;
    }

    .slide-title {
      font-size: 22px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.3;
    }

    .slide-subtitle {
      font-size: 13px;
      color: var(--accent-cyan);
      font-weight: 600;
      margin-top: 4px;
    }

    .avatar-narrator {
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(6, 182, 212, 0.15));
      border: 1px solid rgba(99, 102, 241, 0.3);
      border-radius: 12px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .avatar-icon {
      font-size: 28px;
      animation: floatAvatar 3s ease-in-out infinite;
    }

    @keyframes floatAvatar {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }

    .avatar-text {
      flex: 1;
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .avatar-btn {
      background: var(--accent-indigo);
      border: none;
      color: white;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: background 0.2s;
    }

    .avatar-btn:hover {
      background: #4f46e5;
    }

    .theory-body {
      font-size: 14px;
      color: #cbd5e1;
      line-height: 1.65;
    }

    .theory-body p {
      margin-bottom: 10px;
    }

    .formula-banner {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(6, 182, 212, 0.3);
      border-radius: 10px;
      padding: 14px;
      text-align: center;
      margin: 8px 0;
      box-shadow: inset 0 0 15px rgba(6, 182, 212, 0.05);
    }

    .takeaways-card {
      background: rgba(30, 41, 59, 0.5);
      border-left: 3px solid var(--accent-amber);
      border-radius: 0 8px 8px 0;
      padding: 12px 16px;
    }

    .takeaways-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }

    .takeaways-list {
      list-style-type: none;
      font-size: 12.5px;
      color: #94a3b8;
    }

    .takeaways-list li {
      position: relative;
      padding-left: 18px;
      margin-bottom: 6px;
    }

    .takeaways-list li::before {
      content: "•";
      position: absolute;
      left: 6px;
      color: var(--accent-amber);
      font-weight: bold;
    }

    /* Conceptual Checkpoints */
    .checkpoint-section {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 14px;
      margin-top: 6px;
    }

    .checkpoint-header {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 10px;
    }

    .checkpoint-item {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 12px;
    }

    .checkpoint-q {
      font-size: 13px;
      font-weight: 600;
      color: #f1f5f9;
      margin-bottom: 8px;
    }

    .checkpoint-opts {
      display: grid;
      grid-template-columns: 1fr;
      gap: 6px;
    }

    .opt-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 12px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .opt-btn:hover:not(:disabled) {
      background: rgba(99, 102, 241, 0.2);
      border-color: var(--accent-indigo);
    }

    .opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
    }

    .opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fca5a5 !important;
    }

    .checkpoint-exp {
      font-size: 12px;
      padding: 8px 10px;
      border-radius: 6px;
      margin-top: 8px;
      display: none;
      line-height: 1.5;
    }

    /* Simulator Right Card */
    .sim-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .sim-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
      flex-wrap: wrap;
      gap: 8px;
    }

    .sim-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sim-stats-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .stat-pill {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 11px;
      color: #cbd5e1;
    }

    .stat-pill strong {
      color: #38bdf8;
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
      flex-direction: column;
      gap: 10px;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 12px;
    }

    .control-row {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .control-label {
      font-size: 12px;
      font-weight: 600;
      color: #cbd5e1;
      min-width: 90px;
    }

    .control-slider {
      flex: 1;
      accent-color: var(--accent-indigo);
      cursor: pointer;
    }

    .control-val {
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-cyan);
      min-width: 35px;
      text-align: right;
    }

    .sim-btn {
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(99, 102, 241, 0.4);
      color: #e2e8f0;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .sim-btn:hover {
      background: var(--accent-indigo);
      border-color: var(--accent-indigo);
      transform: translateY(-1px);
    }

    .sim-btn.active {
      background: var(--accent-indigo);
      border-color: #818cf8;
      box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
    }

    /* Dedicated Quiz Slide Layout (Slides 17 to 20) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 20px;
      width: 100%;
    }

    .quiz-header-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .quiz-title-area h2 {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
    }

    .quiz-title-area p {
      font-size: 12px;
      color: var(--accent-cyan);
      margin-top: 2px;
    }

    .quiz-score-badge {
      background: rgba(99, 102, 241, 0.2);
      border: 1px solid var(--accent-indigo);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 700;
      color: #c7d2fe;
    }

    .quiz-questions-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 16px;
    }

    @media (max-width: 640px) {
      .quiz-questions-grid {
        grid-template-columns: 1fr;
      }
    }

    .quiz-card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }

    .quiz-q-num {
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .quiz-q-text {
      font-size: 13.5px;
      font-weight: 600;
      color: #f8fafc;
      line-height: 1.5;
    }

    .quiz-opts {
      display: grid;
      grid-template-columns: 1fr;
      gap: 6px;
    }

    .quiz-opt-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 12px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(99, 102, 241, 0.2);
      border-color: var(--accent-indigo);
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fca5a5 !important;
    }

    .quiz-btn-solution {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fcd34d;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      align-self: flex-start;
      margin-top: 4px;
      display: none;
      transition: all 0.2s;
    }

    .quiz-btn-solution:hover {
      background: rgba(245, 158, 11, 0.3);
    }

    /* Modal Backdrop and Box */
    .modal-backdrop {
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
    }

    /* Footer Navigation */
    footer.lab-footer {
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
    }

    .footer-left {
      font-size: 12px;
      color: var(--text-muted);
    }

    .footer-notice {
      font-size: 13px;
      color: #f59e0b;
      font-weight: 700;
      display: none;
    }
  </style>
</head>
<body>

  <!-- Top Lab Header -->
  <header class="lab-header">
    <div class="brand-area">
      <div class="brand-icon">🎮</div>
      <div class="brand-title">
        <h1>Algebra Play • Master Laboratory</h1>
        <p>NCERT Class 8 Mathematics • Chapter 13</p>
      </div>
    </div>

    <div class="nav-controls">
      <div class="slide-badge" id="slideNumDisplay">Slide 1 of 20</div>
      <button class="btn-nav" id="prevBtn" onclick="prevSlide()" disabled>
        <span>←</span> Prev
      </button>
      <button class="btn-nav" id="nextBtn" onclick="nextSlide()">
        Next <span>→</span>
      </button>
    </div>
  </header>

  <!-- Main Container -->
  <main class="lab-container">
    
    <!-- Lesson View (Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      
      <!-- Left Column: Theory & Interactive Checkpoints -->
      <div class="theory-card">
        <div class="slide-header">
          <h2 class="slide-title" id="slideHeading">Algebra Play</h2>
          <div class="slide-subtitle" id="slideSubheading">The Art of Generalized Arithmetic & Variables</div>
        </div>

        <div class="avatar-narrator">
          <div class="avatar-icon">🧙‍♂️</div>
          <div class="avatar-text" id="avatarText">
            Welcome to Algebra Play! Here we uncover the secret algebraic machinery powering mental math tricks, number pyramids, and calendar mysteries.
          </div>
          <button class="avatar-btn" id="voiceToggleBtn" onclick="toggleVoice()">
            <span id="voiceIcon">🔊</span> <span id="voiceTxt">Listen</span>
          </button>
        </div>

        <div class="theory-body" id="theoryContent">
          <!-- Dynamic Theory Injected Here -->
        </div>

        <div class="formula-banner" id="formulaBanner">
          <!-- Dynamic Formula Injected Here -->
        </div>

        <div class="takeaways-card">
          <div class="takeaways-title">Key Core Takeaways</div>
          <ul class="takeaways-list" id="keyTakeawaysList">
            <!-- Dynamic Takeaways Injected Here -->
          </ul>
        </div>

        <div class="checkpoint-section" id="checkpointContainer">
          <div class="checkpoint-header">
            <span>⚡</span> Quick Conceptual Checkpoints
          </div>
          <div id="checkpointsList">
            <!-- Dynamic Checkpoints Injected Here -->
          </div>
        </div>
      </div>

      <!-- Right Column: Bespoke Interactive SVG Simulator -->
      <div class="sim-card">
        <div class="sim-header">
          <div class="sim-title">
            <span>🔬</span>
            <span id="simTitle">Interactive Algebraic Simulator</span>
          </div>
          <div class="sim-stats-bar" id="simStatsBar">
            <!-- Dynamic Stats Injected Here -->
          </div>
        </div>

        <div class="sim-canvas-area" id="simCanvasArea">
          <!-- Dynamic SVG Simulator Canvas Injected Here -->
        </div>

        <div class="sim-controls" id="simControls">
          <!-- Dynamic Controls Injected Here -->
        </div>
      </div>
    </div>

    <!-- Quiz Slide View (Slides 17 to 20) -->
    <div class="quiz-container" id="quizContainer">
      <div class="quiz-header-card">
        <div class="quiz-title-area">
          <h2 id="quizTitle">Mastery Quiz Challenge</h2>
          <p id="quizSubtitle">Answer all 10 questions to master these algebraic concepts.</p>
        </div>
        <div class="quiz-score-badge" id="quizScoreBadge">
          Score: 0 / 10
        </div>
      </div>

      <div class="quiz-questions-grid" id="quizQuestionsGrid">
        <!-- 10 Quiz Cards Injected Here -->
      </div>
    </div>

  </main>

  <!-- Footer Navigation -->
  <footer class="lab-footer">
    <div class="footer-left">
      Interactive STEM Curriculum Lab • Grade 8 Mathematics • Chapter 13
    </div>
    <div class="footer-notice" id="lastSlideNotice">
      🎉 You have reached the last slide of this chapter!
    </div>
    <button class="btn-nav" id="footerNextBtn" onclick="nextSlide()">
      Next <span>→</span>
    </button>
  </footer>

  <!-- Step-by-Step Solution Modal -->
  <div id="solutionModal" style="position:fixed; top:0; left:0; width:100vw; height:100vh; display:none; align-items:center; justify-content:center; z-index:1000;" class="modal-backdrop">
    <div style="background:#0f172a; border:1px solid rgba(245, 158, 11, 0.4); border-radius:16px; max-width:600px; width:90%; padding:24px; box-shadow:0 25px 50px -12px rgba(0,0,0,0.8); position:relative;">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:12px; margin-bottom:16px;">
        <div style="font-size:16px; font-weight:800; color:#fbbf24; display:flex; align-items:center; gap:8px;">
          <span>💡</span> Step-by-Step Mathematical Solution
        </div>
        <button onclick="closeSolutionModal()" style="background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer;">✕</button>
      </div>
      <div id="modalQuestionText" style="font-size:13.5px; color:#e2e8f0; margin-bottom:14px; font-weight:600;"></div>
      <div id="modalSolutionBody" style="font-size:13px; color:#cbd5e1; line-height:1.6; background:rgba(15,23,42,0.8); padding:14px; border-radius:10px; border:1px solid rgba(255,255,255,0.05);"></div>
    </div>
  </div>

  <script>
    const SLIDES = %%SLIDES_JSON%%;

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let quizScores = {};

    function loadSlide(index) {
      if (index < 0 || index >= SLIDES.length) return;
      currentSlideIndex = index;
      stopSpeech();

      const slide = SLIDES[index];
      const indicator = document.getElementById('slideNumDisplay');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const footerNextBtn = document.getElementById('footerNextBtn');
      const lastNotice = document.getElementById('lastSlideNotice');
      const lessonGrid = document.getElementById('lessonGrid');
      const quizContainer = document.getElementById('quizContainer');

      indicator.textContent = `Slide ${index + 1} of ${SLIDES.length}`;
      prevBtn.disabled = (index === 0);

      if (index === SLIDES.length - 1) {
        nextBtn.style.display = 'none';
        footerNextBtn.style.display = 'none';
        lastNotice.style.display = 'block';
      } else {
        nextBtn.style.display = 'inline-flex';
        footerNextBtn.style.display = 'inline-flex';
        lastNotice.style.display = 'none';
      }

      if (index < 16) {
        // Lesson Slides (1 to 16)
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
        // Quiz Slides (17 to 20)
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

    // In-Slide Checkpoints
    function renderCheckpoints(checkpoints) {
      const list = document.getElementById('checkpointsList');
      list.innerHTML = '';

      if (!checkpoints || checkpoints.length === 0) {
        document.getElementById('checkpointContainer').style.display = 'none';
        return;
      }
      document.getElementById('checkpointContainer').style.display = 'block';

      checkpoints.forEach((cp, qIdx) => {
        const item = document.createElement('div');
        item.className = 'checkpoint-item';

        const qTitle = document.createElement('div');
        qTitle.className = 'checkpoint-q';
        qTitle.innerHTML = `<strong>Q${qIdx + 1}:</strong> ${cp.question}`;
        item.appendChild(qTitle);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'checkpoint-opts';

        const expDiv = document.createElement('div');
        expDiv.className = 'checkpoint-exp';
        expDiv.innerHTML = `<strong>Explanation:</strong> ${cp.explanation}`;

        cp.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'opt-btn';
          btn.innerHTML = optText;
          btn.onclick = () => {
            const btns = optsDiv.querySelectorAll('.opt-btn');
            btns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('correct');
              expDiv.style.display = 'block';
              expDiv.style.background = 'rgba(16, 185, 129, 0.15)';
              expDiv.style.border = '1px solid rgba(16, 185, 129, 0.3)';
              expDiv.style.color = '#6ee7b7';
            } else {
              btn.classList.add('incorrect');
              btns[cp.correct].classList.add('correct');
              expDiv.style.display = 'block';
              expDiv.style.background = 'rgba(244, 63, 94, 0.15)';
              expDiv.style.border = '1px solid rgba(244, 63, 94, 0.3)';
              expDiv.style.color = '#fca5a5';
            }
            triggerMathRender(expDiv);
          };
          optsDiv.appendChild(btn);
        });

        item.appendChild(optsDiv);
        item.appendChild(expDiv);
        list.appendChild(item);
      });
    }

    // Quiz Slide Renderer
    function renderQuizSlide(questions) {
      const grid = document.getElementById('quizQuestionsGrid');
      grid.innerHTML = '';
      quizScores[currentSlideIndex] = quizScores[currentSlideIndex] || {};

      questions.forEach((q, idx) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';

        const qNum = document.createElement('div');
        qNum.className = 'quiz-q-num';
        qNum.textContent = `Question ${idx + 1} of 10`;
        card.appendChild(qNum);

        const qText = document.createElement('div');
        qText.className = 'quiz-q-text';
        qText.innerHTML = q.question;
        card.appendChild(qText);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'quiz-opts';

        const solBtn = document.createElement('button');
        solBtn.className = 'quiz-btn-solution';
        solBtn.textContent = '💡 View Step-by-Step Solution';
        solBtn.onclick = () => openSolutionModal(currentSlideIndex, idx);

        q.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.innerHTML = optText;

          if (quizScores[currentSlideIndex][idx] !== undefined) {
            btn.disabled = true;
            if (optIdx === q.correct) btn.classList.add('correct');
            if (quizScores[currentSlideIndex][idx] === optIdx && optIdx !== q.correct) {
              btn.classList.add('incorrect');
            }
            solBtn.style.display = 'inline-block';
          }

          btn.onclick = () => {
            const allBtns = optsDiv.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => b.disabled = true);
            quizScores[currentSlideIndex][idx] = optIdx;

            if (optIdx === q.correct) {
              btn.classList.add('correct');
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
            }
            solBtn.style.display = 'inline-block';
            updateQuizScore();
          };

          optsDiv.appendChild(btn);
        });

        card.appendChild(optsDiv);
        card.appendChild(solBtn);
        grid.appendChild(card);
      });

      updateQuizScore();
    }

    function updateQuizScore() {
      const scores = quizScores[currentSlideIndex] || {};
      const answered = Object.keys(scores).length;
      let correctCount = 0;
      const questions = SLIDES[currentSlideIndex].questions;

      for (let idx in scores) {
        if (scores[idx] === questions[idx].correct) correctCount++;
      }

      document.getElementById('quizScoreBadge').textContent = `Score: ${correctCount} / 10`;
    }

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
      const slide = SLIDES[currentSlideIndex];
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = slide.content;
      const cleanText = `${slide.title}. ${slide.subtitle}. ${tempDiv.textContent || tempDiv.innerText || ''}`;

      const utter = new SpeechSynthesisUtterance(cleanText);
      utter.rate = 0.95;
      utter.pitch = 1.0;

      utter.onend = () => {
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
      const icon = document.getElementById('voiceIcon');
      const txt = document.getElementById('voiceTxt');
      if (isSpeaking) {
        btn.style.background = 'var(--accent-rose)';
        btn.style.borderColor = 'var(--accent-rose)';
        icon.textContent = '⏹';
        txt.textContent = 'Stop';
      } else {
        btn.style.background = 'var(--accent-indigo)';
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
        case 'algebra_play_pattern_machine':
          renderAlgebraPlayPatternMachine(title, stats, canvas, controls);
          break;
        case 'think_of_number_trick_revealer':
          renderThinkOfNumberTrickRevealer(title, stats, canvas, controls);
          break;
        case 'reverse_engineering_solver':
          renderReverseEngineeringSolver(title, stats, canvas, controls);
          break;
        case 'number_pyramid_3tier_builder':
          renderNumberPyramid3TierBuilder(title, stats, canvas, controls);
          break;
        case 'number_pyramid_4tier_solver':
          renderNumberPyramid4TierSolver(title, stats, canvas, controls);
          break;
        case 'grid_diagonal_product_lab':
          renderGridDiagonalProductLab(title, stats, canvas, controls);
          break;
        case 'magic_grid_3x3_explorer':
          renderMagicGrid3x3Explorer(title, stats, canvas, controls);
          break;
        case 'calendar_magic_2x2_window':
          renderCalendarMagic2x2Window(title, stats, canvas, controls);
          break;
        case 'calendar_magic_3x3_revealer':
          renderCalendarMagic3x3Revealer(title, stats, canvas, controls);
          break;
        case 'calendar_cross_plus_shape':
          renderCalendarCrossPlusShape(title, stats, canvas, controls);
          break;
        case 'algebra_grid_area_multiplication':
          renderAlgebraGridAreaMultiplication(title, stats, canvas, controls);
          break;
        case 'visual_identities_square_geometry':
          renderVisualIdentitiesSquareGeometry(title, stats, canvas, controls);
          break;
        case 'largest_product_fixed_sum_slider':
          renderLargestProductFixedSumSlider(title, stats, canvas, controls);
          break;
        case 'partitioning_product_optimizer':
          renderPartitioningProductOptimizer(title, stats, canvas, controls);
          break;
        case 'divisibility_9_decimal_expander':
          renderDivisibility9DecimalExpander(title, stats, canvas, controls);
          break;
        case 'divisibility_11_alternating_canceller':
          renderDivisibility11AlternatingCanceller(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Algebraic Visualiser';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Algebra Play: Pattern Machine
    function renderAlgebraPlayPatternMachine(title, stats, canvas, controls) {
      title.textContent = "Pattern Machine: Concrete Arithmetic vs Generalized Algebra";
      let n = 5;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Input (n): <strong id="inpN">${n}</strong></div>
          <div class="stat-pill">Arithmetic Output: <strong id="numOut" style="color:#10b981;">${2 * (n + 3) - 4}</strong></div>
          <div class="stat-pill">Algebraic Rule: <strong style="color:#a855f7;">2n + 2</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Background guide tracks
        const pathConcrete = document.createElementNS("http://www.w3.org/2000/svg", "path");
        pathConcrete.setAttribute("d", "M 50 110 L 410 110");
        pathConcrete.setAttribute("stroke", "#334155");
        pathConcrete.setAttribute("stroke-width", "4");
        pathConcrete.setAttribute("stroke-dasharray", "6,6");
        svg.appendChild(pathConcrete);

        const pathAlgebra = document.createElementNS("http://www.w3.org/2000/svg", "path");
        pathAlgebra.setAttribute("d", "M 50 250 L 410 250");
        pathAlgebra.setAttribute("stroke", "#334155");
        pathAlgebra.setAttribute("stroke-width", "4");
        pathAlgebra.setAttribute("stroke-dasharray", "6,6");
        svg.appendChild(pathAlgebra);

        // Titles for tracks
        const t1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        t1.setAttribute("x", "40");
        t1.setAttribute("y", "50");
        t1.setAttribute("fill", "#38bdf8");
        t1.setAttribute("font-size", "13");
        t1.setAttribute("font-weight", "bold");
        t1.textContent = "CONCRETE ARITHMETIC TRACK (Specific n = " + n + ")";
        svg.appendChild(t1);

        const t2 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        t2.setAttribute("x", "40");
        t2.setAttribute("y", "190");
        t2.setAttribute("fill", "#c084fc");
        t2.setAttribute("font-size", "13");
        t2.setAttribute("font-weight", "bold");
        t2.textContent = "GENERALIZED ALGEBRA TRACK (Universal Variable n)";
        svg.appendChild(t2);

        // Steps definitions
        const steps = [
          { name: "Start", cVal: `${n}`, aVal: "n", x: 70 },
          { name: "+ 3", cVal: `${n + 3}`, aVal: "n + 3", x: 170 },
          { name: "× 2", cVal: `${2 * (n + 3)}`, aVal: "2n + 6", x: 270 },
          { name: "- 4", cVal: `${2 * (n + 3) - 4}`, aVal: "2n + 2", x: 380 }
        ];

        steps.forEach((st, idx) => {
          // Concrete box
          const cBox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          cBox.setAttribute("x", st.x - 30);
          cBox.setAttribute("y", "85");
          cBox.setAttribute("width", "60");
          cBox.setAttribute("height", "50");
          cBox.setAttribute("rx", "8");
          cBox.setAttribute("fill", "#0f172a");
          cBox.setAttribute("stroke", idx === 3 ? "#10b981" : "#38bdf8");
          cBox.setAttribute("stroke-width", "2");
          svg.appendChild(cBox);

          const cTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          cTxt.setAttribute("x", st.x);
          cTxt.setAttribute("y", "116");
          cTxt.setAttribute("fill", idx === 3 ? "#34d399" : "#e2e8f0");
          cTxt.setAttribute("font-size", "16");
          cTxt.setAttribute("font-weight", "bold");
          cTxt.setAttribute("text-anchor", "middle");
          cTxt.textContent = st.cVal;
          svg.appendChild(cTxt);

          const cSub = document.createElementNS("http://www.w3.org/2000/svg", "text");
          cSub.setAttribute("x", st.x);
          cSub.setAttribute("y", "75");
          cSub.setAttribute("fill", "#94a3b8");
          cSub.setAttribute("font-size", "11");
          cSub.setAttribute("text-anchor", "middle");
          cSub.textContent = st.name;
          svg.appendChild(cSub);

          // Algebra box
          const aBox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          aBox.setAttribute("x", st.x - 34);
          aBox.setAttribute("y", "225");
          aBox.setAttribute("width", "68");
          aBox.setAttribute("height", "50");
          aBox.setAttribute("rx", "8");
          aBox.setAttribute("fill", "#0f172a");
          aBox.setAttribute("stroke", idx === 3 ? "#a855f7" : "#818cf8");
          aBox.setAttribute("stroke-width", "2");
          svg.appendChild(aBox);

          const aTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          aTxt.setAttribute("x", st.x);
          aTxt.setAttribute("y", "256");
          aTxt.setAttribute("fill", idx === 3 ? "#e879f9" : "#e2e8f0");
          aTxt.setAttribute("font-size", "13.5");
          aTxt.setAttribute("font-weight", "bold");
          aTxt.setAttribute("text-anchor", "middle");
          aTxt.textContent = st.aVal;
          svg.appendChild(aTxt);

          // Connector arrows
          if (idx < 3) {
            const nextX = steps[idx + 1].x;
            const cArr = document.createElementNS("http://www.w3.org/2000/svg", "text");
            cArr.setAttribute("x", (st.x + nextX) / 2);
            cArr.setAttribute("y", "115");
            cArr.setAttribute("fill", "#64748b");
            cArr.setAttribute("font-size", "14");
            cArr.setAttribute("text-anchor", "middle");
            cArr.textContent = "➔";
            svg.appendChild(cArr);

            const aArr = document.createElementNS("http://www.w3.org/2000/svg", "text");
            aArr.setAttribute("x", (st.x + nextX) / 2);
            aArr.setAttribute("y", "255");
            aArr.setAttribute("fill", "#64748b");
            aArr.setAttribute("font-size", "14");
            aArr.setAttribute("text-anchor", "middle");
            aArr.textContent = "➔";
            svg.appendChild(aArr);
          }
        });

        // Bottom takeaway note
        const note = document.createElementNS("http://www.w3.org/2000/svg", "text");
        note.setAttribute("x", "230");
        note.setAttribute("y", "330");
        note.setAttribute("fill", "#38bdf8");
        note.setAttribute("font-size", "12");
        note.setAttribute("font-weight", "bold");
        note.setAttribute("text-anchor", "middle");
        note.textContent = `For n = ${n}: Arithmetic gives 2(${n}) + 2 = ${2 * n + 2} ✓ Exact match!`;
        svg.appendChild(note);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Choose n:</span>
          <input type="range" class="control-slider" min="1" max="20" value="${n}" id="sliderN">
          <span class="control-val" id="valN">${n}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="setN(Math.floor(Math.random()*20)+1)">🎲 Random n</button>
          <button class="sim-btn" onclick="setN(1)">n = 1</button>
          <button class="sim-btn" onclick="setN(10)">n = 10</button>
          <button class="sim-btn" onclick="setN(20)">n = 20</button>
        </div>
      `;

      document.getElementById('sliderN').oninput = (e) => {
        n = parseInt(e.target.value);
        document.getElementById('valN').textContent = n;
        update();
      };

      window.setN = (newVal) => {
        n = newVal;
        document.getElementById('sliderN').value = n;
        document.getElementById('valN').textContent = n;
        update();
      };

      update();
    }

    // 2. Think of a Number Trick Revealer
    function renderThinkOfNumberTrickRevealer(title, stats, canvas, controls) {
      title.textContent = "The Mind Reader: Unmasking the Disappearing Variable";
      let x = 7;
      let step = 0;

      const steps = [
        { label: "Step 0: Secret Mystery Number", formula: "x", calc: x, desc: "Think of any secret number x" },
        { label: "Step 1: Add 5", formula: "x + 5", calc: x + 5, desc: "Add 5 to your secret number" },
        { label: "Step 2: Multiply by 2", formula: "2(x + 5) = 2x + 10", calc: 2 * (x + 5), desc: "Double the total" },
        { label: "Step 3: Add 10", formula: "2x + 10 + 10 = 2x + 20", calc: 2 * (x + 5) + 10, desc: "Add 10 more to the sum" },
        { label: "Step 4: Divide by 2", formula: "\\frac{2x + 20}{2} = x + 10", calc: (2 * (x + 5) + 10) / 2, desc: "Divide everything in half" },
        { label: "Step 5: Subtract original x", formula: "(x + 10) - x = 10", calc: 10, desc: "Subtract your original secret number: x cancels out!" }
      ];

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Secret (x): <strong>${x}</strong></div>
          <div class="stat-pill">Current Step: <strong>${step} / 5</strong></div>
          <div class="stat-pill">Value: <strong style="color:#10b981;">${steps[step].calc}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Mystery chest / box graphic
        const box = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        box.setAttribute("x", "155");
        box.setAttribute("y", "45");
        box.setAttribute("width", "150");
        box.setAttribute("height", "110");
        box.setAttribute("rx", "16");
        box.setAttribute("fill", "#1e1b4b");
        box.setAttribute("stroke", step === 5 ? "#10b981" : "#818cf8");
        box.setAttribute("stroke-width", "3");
        svg.appendChild(box);

        const icon = document.createElementNS("http://www.w3.org/2000/svg", "text");
        icon.setAttribute("x", "230");
        icon.setAttribute("y", "90");
        icon.setAttribute("font-size", "28");
        icon.setAttribute("text-anchor", "middle");
        icon.textContent = step === 5 ? "🎯" : "🎁";
        svg.appendChild(icon);

        const valTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        valTxt.setAttribute("x", "230");
        valTxt.setAttribute("y", "130");
        valTxt.setAttribute("fill", step === 5 ? "#34d399" : "#38bdf8");
        valTxt.setAttribute("font-size", "22");
        valTxt.setAttribute("font-weight", "bold");
        valTxt.setAttribute("text-anchor", "middle");
        valTxt.textContent = `Result = ${steps[step].calc}`;
        svg.appendChild(valTxt);

        // Step description card
        const card = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        card.setAttribute("x", "50");
        card.setAttribute("y", "180");
        card.setAttribute("width", "360");
        card.setAttribute("height", "130");
        card.setAttribute("rx", "12");
        card.setAttribute("fill", "#0f172a");
        card.setAttribute("stroke", "rgba(99, 102, 241, 0.3)");
        card.setAttribute("stroke-width", "1.5");
        svg.appendChild(card);

        const lbl = document.createElementNS("http://www.w3.org/2000/svg", "text");
        lbl.setAttribute("x", "70");
        lbl.setAttribute("y", "212");
        lbl.setAttribute("fill", "#f59e0b");
        lbl.setAttribute("font-size", "13");
        lbl.setAttribute("font-weight", "bold");
        lbl.textContent = steps[step].label;
        svg.appendChild(lbl);

        const desc = document.createElementNS("http://www.w3.org/2000/svg", "text");
        desc.setAttribute("x", "70");
        desc.setAttribute("y", "240");
        desc.setAttribute("fill", "#cbd5e1");
        desc.setAttribute("font-size", "13");
        desc.textContent = steps[step].desc;
        svg.appendChild(desc);

        const alg = document.createElementNS("http://www.w3.org/2000/svg", "text");
        alg.setAttribute("x", "70");
        alg.setAttribute("y", "275");
        alg.setAttribute("fill", "#a855f7");
        alg.setAttribute("font-size", "15");
        alg.setAttribute("font-weight", "bold");
        alg.textContent = `Algebra: ${steps[step].formula}`;
        svg.appendChild(alg);

        // Strike through in step 5
        if (step === 5) {
          const banner = document.createElementNS("http://www.w3.org/2000/svg", "text");
          banner.setAttribute("x", "230");
          banner.setAttribute("y", "335");
          banner.setAttribute("fill", "#10b981");
          banner.setAttribute("font-size", "13");
          banner.setAttribute("font-weight", "bold");
          banner.setAttribute("text-anchor", "middle");
          banner.textContent = "✨ Variable Cancelled: Secret x is eliminated! Result is ALWAYS 10! ✨";
          svg.appendChild(banner);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Secret x:</span>
          <input type="range" class="control-slider" min="1" max="50" value="${x}" id="sliderTrickX">
          <span class="control-val" id="valTrickX">${x}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="prevStep()" ${step === 0 ? 'disabled' : ''}>◀ Prev Step</button>
          <button class="sim-btn active" onclick="nextStep()" ${step === 5 ? 'disabled' : ''}>Next Step ▶</button>
          <button class="sim-btn" onclick="resetTrick()">🔄 Reset Trick</button>
        </div>
      `;

      document.getElementById('sliderTrickX').oninput = (e) => {
        x = parseInt(e.target.value);
        document.getElementById('valTrickX').textContent = x;
        update();
      };

      window.nextStep = () => {
        if (step < 5) { step++; update(); }
      };
      window.prevStep = () => {
        if (step > 0) { step--; update(); }
      };
      window.resetTrick = () => {
        step = 0; update();
      };

      update();
    }

    // 3. Reversing Steps Solver
    function renderReverseEngineeringSolver(title, stats, canvas, controls) {
      title.textContent = "Inverse Operations: Reverse-Engineering Secret Numbers";
      let a = 3;
      let b = 7;
      let secret = 8;

      function update() {
        const result = a * secret + b;
        stats.innerHTML = `
          <div class="stat-pill">Final Number (R): <strong style="color:#f59e0b;">${result}</strong></div>
          <div class="stat-pill">Multiplier (a): <strong>${a}</strong></div>
          <div class="stat-pill">Addend (b): <strong>${b}</strong></div>
          <div class="stat-pill">Unmasked Secret (x): <strong style="color:#10b981;">${secret}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Forward Track (Top)
        const t1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        t1.setAttribute("x", "40");
        t1.setAttribute("y", "45");
        t1.setAttribute("fill", "#38bdf8");
        t1.setAttribute("font-size", "13");
        t1.setAttribute("font-weight", "bold");
        t1.textContent = "FORWARD PIPELINE: x ➔ Multiply by a ➔ Add b ➔ Result";
        svg.appendChild(t1);

        // Boxes for forward
        const fBoxes = [
          { label: "Secret x", val: `${secret}`, x: 80, y: 80 },
          { label: `× ${a}`, val: `${a * secret}`, x: 220, y: 80 },
          { label: `+ ${b}`, val: `${result}`, x: 360, y: 80 }
        ];

        fBoxes.forEach((bx, idx) => {
          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", bx.x - 35);
          r.setAttribute("y", bx.y - 25);
          r.setAttribute("width", "70");
          r.setAttribute("height", "50");
          r.setAttribute("rx", "8");
          r.setAttribute("fill", "#0f172a");
          r.setAttribute("stroke", idx === 0 ? "#10b981" : (idx === 2 ? "#f59e0b" : "#38bdf8"));
          r.setAttribute("stroke-width", "2");
          svg.appendChild(r);

          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", bx.x);
          txt.setAttribute("y", bx.y + 6);
          txt.setAttribute("fill", "#f8fafc");
          txt.setAttribute("font-size", "16");
          txt.setAttribute("font-weight", "bold");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = bx.val;
          svg.appendChild(txt);

          const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
          sub.setAttribute("x", bx.x);
          sub.setAttribute("y", bx.y - 32);
          sub.setAttribute("fill", "#94a3b8");
          sub.setAttribute("font-size", "11");
          sub.setAttribute("text-anchor", "middle");
          sub.textContent = bx.label;
          svg.appendChild(sub);

          if (idx < 2) {
            const arr = document.createElementNS("http://www.w3.org/2000/svg", "text");
            arr.setAttribute("x", (bx.x + fBoxes[idx + 1].x) / 2);
            arr.setAttribute("y", bx.y + 6);
            arr.setAttribute("fill", "#64748b");
            arr.setAttribute("font-size", "16");
            arr.setAttribute("text-anchor", "middle");
            arr.textContent = "➔";
            svg.appendChild(arr);
          }
        });

        // Reverse Detective Track (Bottom)
        const t2 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        t2.setAttribute("x", "40");
        t2.setAttribute("y", "195");
        t2.setAttribute("fill", "#c084fc");
        t2.setAttribute("font-size", "13");
        t2.setAttribute("font-weight", "bold");
        t2.textContent = "REVERSE INVERSION: Result ➔ Subtract b ➔ Divide by a ➔ Secret x";
        svg.appendChild(t2);

        const rBoxes = [
          { label: "Given R", val: `${result}`, x: 360, y: 240 },
          { label: `- ${b}`, val: `${result - b}`, x: 220, y: 240 },
          { label: `÷ ${a}`, val: `${(result - b) / a}`, x: 80, y: 240 }
        ];

        rBoxes.forEach((bx, idx) => {
          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", bx.x - 35);
          r.setAttribute("y", bx.y - 25);
          r.setAttribute("width", "70");
          r.setAttribute("height", "50");
          r.setAttribute("rx", "8");
          r.setAttribute("fill", "#0f172a");
          r.setAttribute("stroke", idx === 2 ? "#10b981" : "#a855f7");
          r.setAttribute("stroke-width", "2");
          svg.appendChild(r);

          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", bx.x);
          txt.setAttribute("y", bx.y + 6);
          txt.setAttribute("fill", idx === 2 ? "#34d399" : "#f8fafc");
          txt.setAttribute("font-size", "16");
          txt.setAttribute("font-weight", "bold");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = bx.val;
          svg.appendChild(txt);

          const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
          sub.setAttribute("x", bx.x);
          sub.setAttribute("y", bx.y + 40);
          sub.setAttribute("fill", "#94a3b8");
          sub.setAttribute("font-size", "11");
          sub.setAttribute("text-anchor", "middle");
          sub.textContent = bx.label;
          svg.appendChild(sub);

          if (idx < 2) {
            const arr = document.createElementNS("http://www.w3.org/2000/svg", "text");
            arr.setAttribute("x", (bx.x + rBoxes[idx + 1].x) / 2);
            arr.setAttribute("y", bx.y + 6);
            arr.setAttribute("fill", "#64748b");
            arr.setAttribute("font-size", "16");
            arr.setAttribute("text-anchor", "middle");
            arr.textContent = "➔";
            svg.appendChild(arr);
          }
        });

        const mathNotice = document.createElementNS("http://www.w3.org/2000/svg", "text");
        mathNotice.setAttribute("x", "230");
        mathNotice.setAttribute("y", "335");
        mathNotice.setAttribute("fill", "#cbd5e1");
        mathNotice.setAttribute("font-size", "12");
        mathNotice.setAttribute("text-anchor", "middle");
        mathNotice.textContent = `Formula: x = (R - b) / a = (${result} - ${b}) / ${a} = ${result - b} / ${a} = ${secret}`;
        svg.appendChild(mathNotice);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Secret x:</span>
          <input type="range" class="control-slider" min="1" max="15" value="${secret}" id="sliderSec">
          <span class="control-val" id="valSec">${secret}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Multiplier a:</span>
          <input type="range" class="control-slider" min="2" max="6" value="${a}" id="sliderA">
          <span class="control-val" id="valA">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Addend b:</span>
          <input type="range" class="control-slider" min="1" max="20" value="${b}" id="sliderB">
          <span class="control-val" id="valB">${b}</span>
        </div>
      `;

      document.getElementById('sliderSec').oninput = (e) => {
        secret = parseInt(e.target.value);
        document.getElementById('valSec').textContent = secret;
        update();
      };
      document.getElementById('sliderA').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valA').textContent = a;
        update();
      };
      document.getElementById('sliderB').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valB').textContent = b;
        update();
      };

      update();
    }

    // 4. Number Pyramid: 3-Tier Builder
    function renderNumberPyramid3TierBuilder(title, stats, canvas, controls) {
      title.textContent = "3-Tier Addition Pyramid: Center Brick Weighting Invariant";
      let a = 3, b = 7, c = 4;

      function update() {
        const midL = a + b;
        const midR = b + c;
        const apex = midL + midR; // a + 2b + c

        stats.innerHTML = `
          <div class="stat-pill">Base [a, b, c]: <strong>[${a}, ${b}, ${c}]</strong></div>
          <div class="stat-pill">Center Brick (b): <strong style="color:#f59e0b;">${b} (counted twice!)</strong></div>
          <div class="stat-pill">Apex Sum: <strong style="color:#38bdf8;">${apex}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        function drawBrick(x, y, w, h, text, subText, color, highlight) {
          const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", x);
          rect.setAttribute("y", y);
          rect.setAttribute("width", w);
          rect.setAttribute("height", h);
          rect.setAttribute("rx", "10");
          rect.setAttribute("fill", highlight ? "rgba(99, 102, 241, 0.25)" : "#0f172a");
          rect.setAttribute("stroke", color);
          rect.setAttribute("stroke-width", highlight ? "2.5" : "1.5");
          g.appendChild(rect);

          const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
          t.setAttribute("x", x + w / 2);
          t.setAttribute("y", y + h / 2 + 5);
          t.setAttribute("fill", color);
          t.setAttribute("font-size", "17");
          t.setAttribute("font-weight", "bold");
          t.setAttribute("text-anchor", "middle");
          t.textContent = text;
          g.appendChild(t);

          if (subText) {
            const st = document.createElementNS("http://www.w3.org/2000/svg", "text");
            st.setAttribute("x", x + w / 2);
            st.setAttribute("y", y + h - 6);
            st.setAttribute("fill", "#94a3b8");
            st.setAttribute("font-size", "10");
            st.setAttribute("text-anchor", "middle");
            st.textContent = subText;
            g.appendChild(st);
          }

          svg.appendChild(g);
        }

        // Tier 3 (Apex): 1 brick
        drawBrick(170, 40, 120, 60, `${apex}`, "Apex = a + 2b + c", "#38bdf8", true);

        // Tier 2 (Middle): 2 bricks
        drawBrick(105, 125, 110, 55, `${midL}`, `a + b = ${a}+${b}`, "#a855f7", false);
        drawBrick(245, 125, 110, 55, `${midR}`, `b + c = ${b}+${c}`, "#a855f7", false);

        // Tier 1 (Base): 3 bricks
        drawBrick(45, 205, 105, 55, `${a}`, "Left Base (a)", "#cbd5e1", false);
        drawBrick(175, 205, 110, 55, `${b}`, "Center Base (b)", "#f59e0b", true);
        drawBrick(310, 205, 105, 55, `${c}`, "Right Base (c)", "#cbd5e1", false);

        // Explanatory breakdown text
        const note = document.createElementNS("http://www.w3.org/2000/svg", "text");
        note.setAttribute("x", "230");
        note.setAttribute("y", "310");
        note.setAttribute("fill", "#cbd5e1");
        note.setAttribute("font-size", "13");
        note.setAttribute("font-weight", "600");
        note.setAttribute("text-anchor", "middle");
        note.textContent = `Formula: ${a} + 2(${b}) + ${c} = ${a} + ${2 * b} + ${c} = ${apex}`;
        svg.appendChild(note);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "335");
        tip.setAttribute("fill", "#f59e0b");
        tip.setAttribute("font-size", "11.5");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "💡 Put the largest number in the center brick (b) to maximize the apex sum!";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Base a:</span>
          <input type="range" class="control-slider" min="1" max="15" value="${a}" id="pyrA">
          <span class="control-val" id="valPyrA">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Center b:</span>
          <input type="range" class="control-slider" min="1" max="15" value="${b}" id="pyrB">
          <span class="control-val" id="valPyrB">${b}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Base c:</span>
          <input type="range" class="control-slider" min="1" max="15" value="${c}" id="pyrC">
          <span class="control-val" id="valPyrC">${c}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="maximizeApex()">⚡ Maximize Apex</button>
          <button class="sim-btn" onclick="randomizePyr()">🎲 Randomize</button>
        </div>
      `;

      document.getElementById('pyrA').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valPyrA').textContent = a;
        update();
      };
      document.getElementById('pyrB').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valPyrB').textContent = b;
        update();
      };
      document.getElementById('pyrC').oninput = (e) => {
        c = parseInt(e.target.value);
        document.getElementById('valPyrC').textContent = c;
        update();
      };

      window.maximizeApex = () => {
        const sorted = [a, b, c].sort((x, y) => x - y);
        // Largest in middle
        a = sorted[0];
        b = sorted[2];
        c = sorted[1];
        document.getElementById('pyrA').value = a;
        document.getElementById('pyrB').value = b;
        document.getElementById('pyrC').value = c;
        document.getElementById('valPyrA').textContent = a;
        document.getElementById('valPyrB').textContent = b;
        document.getElementById('valPyrC').textContent = c;
        update();
      };

      window.randomizePyr = () => {
        a = Math.floor(Math.random() * 12) + 1;
        b = Math.floor(Math.random() * 12) + 1;
        c = Math.floor(Math.random() * 12) + 1;
        document.getElementById('pyrA').value = a;
        document.getElementById('pyrB').value = b;
        document.getElementById('pyrC').value = c;
        document.getElementById('valPyrA').textContent = a;
        document.getElementById('valPyrB').textContent = b;
        document.getElementById('valPyrC').textContent = c;
        update();
      };

      update();
    }

    // 5. Higher Pyramids: 4-Tier Solver
    function renderNumberPyramid4TierSolver(title, stats, canvas, controls) {
      title.textContent = "4-Tier Pyramid: Pascal Coefficients (1, 3, 3, 1) & Missing Bricks";
      let a = 2, b = 1, c = 4, d = 3;

      function update() {
        const apex = a + 3 * b + 3 * c + d;

        stats.innerHTML = `
          <div class="stat-pill">Base: <strong>[${a}, ${b}, ${c}, ${d}]</strong></div>
          <div class="stat-pill">Pascal Weights: <strong style="color:#a855f7;">1, 3, 3, 1</strong></div>
          <div class="stat-pill">Apex Value: <strong style="color:#10b981;">${apex}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        function drawB(x, y, w, h, val, coeff, col) {
          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", x);
          r.setAttribute("y", y);
          r.setAttribute("width", w);
          r.setAttribute("height", h);
          r.setAttribute("rx", "8");
          r.setAttribute("fill", "#0f172a");
          r.setAttribute("stroke", col);
          r.setAttribute("stroke-width", "1.5");
          svg.appendChild(r);

          const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
          t.setAttribute("x", x + w / 2);
          t.setAttribute("y", y + h / 2 + 5);
          t.setAttribute("fill", col);
          t.setAttribute("font-size", "14");
          t.setAttribute("font-weight", "bold");
          t.setAttribute("text-anchor", "middle");
          t.textContent = val;
          svg.appendChild(t);

          if (coeff) {
            const cTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
            cTxt.setAttribute("x", x + w / 2);
            cTxt.setAttribute("y", y + h - 5);
            cTxt.setAttribute("fill", "#94a3b8");
            cTxt.setAttribute("font-size", "9.5");
            cTxt.setAttribute("text-anchor", "middle");
            cTxt.textContent = `wt: ×${coeff}`;
            svg.appendChild(cTxt);
          }
        }

        // Apex (Tier 4)
        drawB(185, 30, 90, 48, `${apex}`, null, "#38bdf8");

        // Tier 3
        const t3_1 = a + 2 * b + c;
        const t3_2 = b + 2 * c + d;
        drawB(135, 95, 90, 45, `${t3_1}`, null, "#818cf8");
        drawB(235, 95, 90, 45, `${t3_2}`, null, "#818cf8");

        // Tier 2
        const t2_1 = a + b;
        const t2_2 = b + c;
        const t2_3 = c + d;
        drawB(85, 155, 90, 45, `${t2_1}`, null, "#c084fc");
        drawB(185, 155, 90, 45, `${t2_2}`, null, "#c084fc");
        drawB(285, 155, 90, 45, `${t2_3}`, null, "#c084fc");

        // Tier 1 (Base)
        drawB(35, 215, 90, 50, `${a}`, 1, "#e2e8f0");
        drawB(135, 215, 90, 50, `${b}`, 3, "#f59e0b");
        drawB(235, 215, 90, 50, `${c}`, 3, "#f59e0b");
        drawB(335, 215, 90, 50, `${d}`, 1, "#e2e8f0");

        // Linear formula banner
        const eq = document.createElementNS("http://www.w3.org/2000/svg", "text");
        eq.setAttribute("x", "230");
        eq.setAttribute("y", "310");
        eq.setAttribute("fill", "#cbd5e1");
        eq.setAttribute("font-size", "12");
        eq.setAttribute("font-weight", "600");
        eq.setAttribute("text-anchor", "middle");
        eq.textContent = `Apex = 1(${a}) + 3(${b}) + 3(${c}) + 1(${d}) = ${a} + ${3 * b} + ${3 * c} + ${d} = ${apex}`;
        svg.appendChild(eq);

        const pascal = document.createElementNS("http://www.w3.org/2000/svg", "text");
        pascal.setAttribute("x", "230");
        pascal.setAttribute("y", "335");
        pascal.setAttribute("fill", "#38bdf8");
        pascal.setAttribute("font-size", "11");
        pascal.setAttribute("text-anchor", "middle");
        pascal.textContent = "Row 3 of Pascal's Triangle: (x+y)³ coefficients = 1, 3, 3, 1";
        svg.appendChild(pascal);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Base a:</span>
          <input type="range" class="control-slider" min="1" max="10" value="${a}" id="pyr4A">
          <span class="control-val" id="valPyr4A">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Inner b:</span>
          <input type="range" class="control-slider" min="1" max="10" value="${b}" id="pyr4B">
          <span class="control-val" id="valPyr4B">${b}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Inner c:</span>
          <input type="range" class="control-slider" min="1" max="10" value="${c}" id="pyr4C">
          <span class="control-val" id="valPyr4C">${c}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Base d:</span>
          <input type="range" class="control-slider" min="1" max="10" value="${d}" id="pyr4D">
          <span class="control-val" id="valPyr4D">${d}</span>
        </div>
      `;

      document.getElementById('pyr4A').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valPyr4A').textContent = a;
        update();
      };
      document.getElementById('pyr4B').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valPyr4B').textContent = b;
        update();
      };
      document.getElementById('pyr4C').oninput = (e) => {
        c = parseInt(e.target.value);
        document.getElementById('valPyr4C').textContent = c;
        update();
      };
      document.getElementById('pyr4D').oninput = (e) => {
        d = parseInt(e.target.value);
        document.getElementById('valPyr4D').textContent = d;
        update();
      };

      update();
    }

    // 6. Grid Invariants: 2x2 Diagonal Products
    function renderGridDiagonalProductLab(title, stats, canvas, controls) {
      title.textContent = "2x2 Grid Invariant: Diagonal Product Difference = Step (d)";
      let row = 3;
      let col = 4;
      const step = 10; // 10 columns

      function update() {
        const n = (row - 1) * step + col;
        const p1 = (n + 1) * (n + step);
        const p2 = n * (n + step + 1);
        const diff = p1 - p2;

        stats.innerHTML = `
          <div class="stat-pill">Top-Left (n): <strong>${n}</strong></div>
          <div class="stat-pill">Diag 1 [n+1][n+10]: <strong>${p1}</strong></div>
          <div class="stat-pill">Diag 2 [n][n+11]: <strong>${p2}</strong></div>
          <div class="stat-pill">Product Difference: <strong style="color:#10b981;">${diff} (Always = 10!)</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Draw 10x8 mini grid background
        const cellW = 38;
        const cellH = 26;
        const startX = 40;
        const startY = 30;

        for (let r = 1; r <= 8; r++) {
          for (let c = 1; c <= 10; c++) {
            const num = (r - 1) * 10 + c;
            const x = startX + (c - 1) * cellW;
            const y = startY + (r - 1) * cellH;

            const isSelected = (r === row && c === col) || (r === row && c === col + 1) ||
                               (r === row + 1 && c === col) || (r === row + 1 && c === col + 1);

            const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            rect.setAttribute("x", x);
            rect.setAttribute("y", y);
            rect.setAttribute("width", cellW);
            rect.setAttribute("height", cellH);
            rect.setAttribute("fill", isSelected ? "rgba(99, 102, 241, 0.35)" : "#0f172a");
            rect.setAttribute("stroke", isSelected ? "#38bdf8" : "rgba(255,255,255,0.06)");
            rect.setAttribute("stroke-width", isSelected ? "2" : "1");
            rect.style.cursor = "pointer";
            rect.onclick = () => {
              if (r < 8 && c < 10) {
                row = r;
                col = c;
                update();
              }
            };
            svg.appendChild(rect);

            const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
            txt.setAttribute("x", x + cellW / 2);
            txt.setAttribute("y", y + cellH / 2 + 4);
            txt.setAttribute("fill", isSelected ? "#ffffff" : "#64748b");
            txt.setAttribute("font-size", isSelected ? "11.5" : "10");
            txt.setAttribute("font-weight", isSelected ? "bold" : "normal");
            txt.setAttribute("text-anchor", "middle");
            txt.textContent = num;
            txt.style.pointerEvents = "none";
            svg.appendChild(txt);
          }
        }

        // Highlight 2x2 window frame
        const wx = startX + (col - 1) * cellW;
        const wy = startY + (row - 1) * cellH;
        const frame = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        frame.setAttribute("x", wx);
        frame.setAttribute("y", wy);
        frame.setAttribute("width", cellW * 2);
        frame.setAttribute("height", cellH * 2);
        frame.setAttribute("fill", "none");
        frame.setAttribute("stroke", "#f59e0b");
        frame.setAttribute("stroke-width", "2.5");
        frame.setAttribute("rx", "4");
        svg.appendChild(frame);

        // Lower calculation panel
        const note = document.createElementNS("http://www.w3.org/2000/svg", "text");
        note.setAttribute("x", "230");
        note.setAttribute("y", "280");
        note.setAttribute("fill", "#cbd5e1");
        note.setAttribute("font-size", "13");
        note.setAttribute("font-weight", "600");
        note.setAttribute("text-anchor", "middle");
        note.textContent = `Window: [${n}, ${n+1}], [${n+10}, ${n+11}]`;
        svg.appendChild(note);

        const alg = document.createElementNS("http://www.w3.org/2000/svg", "text");
        alg.setAttribute("x", "230");
        alg.setAttribute("y", "310");
        alg.setAttribute("fill", "#38bdf8");
        alg.setAttribute("font-size", "12.5");
        alg.setAttribute("font-weight", "bold");
        alg.setAttribute("text-anchor", "middle");
        alg.textContent = `(${n+1} × ${n+10}) - (${n} × ${n+11}) = ${p1} - ${p2} = 10 (Strict Invariant!)`;
        svg.appendChild(alg);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "335");
        tip.setAttribute("fill", "#94a3b8");
        tip.setAttribute("font-size", "11");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "👆 Click anywhere on the grid or use controls to move the 2×2 window!";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <button class="sim-btn" onclick="moveGrid(-1, 0)">▲ Move Up</button>
          <button class="sim-btn" onclick="moveGrid(1, 0)">▼ Move Down</button>
          <button class="sim-btn" onclick="moveGrid(0, -1)">◀ Move Left</button>
          <button class="sim-btn" onclick="moveGrid(0, 1)">▶ Move Right</button>
          <button class="sim-btn" onclick="randomGrid()">🎲 Random Location</button>
        </div>
      `;

      window.moveGrid = (dr, dc) => {
        if (row + dr >= 1 && row + dr <= 7) row += dr;
        if (col + dc >= 1 && col + dc <= 9) col += dc;
        update();
      };

      window.randomGrid = () => {
        row = Math.floor(Math.random() * 7) + 1;
        col = Math.floor(Math.random() * 9) + 1;
        update();
      };

      update();
    }

    // 7. 3x3 Grids: Centroid & Balance Explorer
    function renderMagicGrid3x3Explorer(title, stats, canvas, controls) {
      title.textContent = "3x3 Grid Explorer: Centroid Symmetry & 9c Total Sum";
      let centerNum = 45;
      const step = 10;

      function update() {
        const c = centerNum;
        const totalSum = 9 * c;

        stats.innerHTML = `
          <div class="stat-pill">Center (c): <strong style="color:#f59e0b;">${c}</strong></div>
          <div class="stat-pill">Total Sum of 9 cells: <strong style="color:#10b981;">${totalSum}</strong></div>
          <div class="stat-pill">Mean of 9 cells: <strong>${c} (Sum / 9)</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // 3x3 cells layout
        const cellOffsets = [
          [-step - 1, -step, -step + 1],
          [-1, 0, 1],
          [step - 1, step, step + 1]
        ];

        const cellW = 80;
        const cellH = 55;
        const startX = 110;
        const startY = 40;

        for (let r = 0; r < 3; r++) {
          for (let col = 0; col < 3; col++) {
            const offset = cellOffsets[r][col];
            const val = c + offset;
            const x = startX + col * (cellW + 8);
            const y = startY + r * (cellH + 8);
            const isCenter = (r === 1 && col === 1);

            const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            rect.setAttribute("x", x);
            rect.setAttribute("y", y);
            rect.setAttribute("width", cellW);
            rect.setAttribute("height", cellH);
            rect.setAttribute("rx", "10");
            rect.setAttribute("fill", isCenter ? "rgba(245, 158, 11, 0.25)" : "#0f172a");
            rect.setAttribute("stroke", isCenter ? "#f59e0b" : "#38bdf8");
            rect.setAttribute("stroke-width", isCenter ? "2.5" : "1.5");
            svg.appendChild(rect);

            const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
            txt.setAttribute("x", x + cellW / 2);
            txt.setAttribute("y", y + cellH / 2 + 5);
            txt.setAttribute("fill", isCenter ? "#fbbf24" : "#f8fafc");
            txt.setAttribute("font-size", "16");
            txt.setAttribute("font-weight", "bold");
            txt.setAttribute("text-anchor", "middle");
            txt.textContent = val;
            svg.appendChild(txt);

            const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
            sub.setAttribute("x", x + cellW / 2);
            sub.setAttribute("y", y + cellH - 7);
            sub.setAttribute("fill", "#94a3b8");
            sub.setAttribute("font-size", "9.5");
            sub.setAttribute("text-anchor", "middle");
            sub.textContent = isCenter ? "Center [c]" : (offset > 0 ? `c + ${offset}` : `c - ${Math.abs(offset)}`);
            svg.appendChild(sub);
          }
        }

        // Symmetry note
        const note = document.createElementNS("http://www.w3.org/2000/svg", "text");
        note.setAttribute("x", "230");
        note.setAttribute("y", "260");
        note.setAttribute("fill", "#cbd5e1");
        note.setAttribute("font-size", "12.5");
        note.setAttribute("font-weight", "600");
        note.setAttribute("text-anchor", "middle");
        note.textContent = "Opposite pairs around center balance: (c - k) + (c + k) = 2c";
        svg.appendChild(note);

        const sumEq = document.createElementNS("http://www.w3.org/2000/svg", "text");
        sumEq.setAttribute("x", "230");
        sumEq.setAttribute("y", "290");
        sumEq.setAttribute("fill", "#38bdf8");
        sumEq.setAttribute("font-size", "13.5");
        sumEq.setAttribute("font-weight", "bold");
        sumEq.setAttribute("text-anchor", "middle");
        sumEq.textContent = `Total Sum = 4(2c) + c = 9c = 9 × ${c} = ${totalSum}`;
        svg.appendChild(sumEq);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "325");
        tip.setAttribute("fill", "#f59e0b");
        tip.setAttribute("font-size", "11.5");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "Corner sum = 4c • Edge sum = 4c • Total = 9c strictly!";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Center c:</span>
          <input type="range" class="control-slider" min="15" max="85" value="${centerNum}" id="sliderGridC">
          <span class="control-val" id="valGridC">${centerNum}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="setCenter(25)">c = 25</button>
          <button class="sim-btn" onclick="setCenter(50)">c = 50</button>
          <button class="sim-btn" onclick="setCenter(75)">c = 75</button>
          <button class="sim-btn" onclick="setCenter(Math.floor(Math.random()*60)+20)">🎲 Random Center</button>
        </div>
      `;

      document.getElementById('sliderGridC').oninput = (e) => {
        centerNum = parseInt(e.target.value);
        document.getElementById('valGridC').textContent = centerNum;
        update();
      };

      window.setCenter = (val) => {
        centerNum = val;
        document.getElementById('sliderGridC').value = centerNum;
        document.getElementById('valGridC').textContent = centerNum;
        update();
      };

      update();
    }

    // 8. Calendar Magic: 2x2 Window
    function renderCalendarMagic2x2Window(title, stats, canvas, controls) {
      title.textContent = "Calendar Magic: 2x2 Window & Equal Diagonal Sums";
      let startDay = 8; // Top-left date

      function update() {
        const n = startDay;
        const d1_sum = n + (n + 8);
        const d2_sum = (n + 1) + (n + 7);
        const prod_diff = (n + 1) * (n + 7) - n * (n + 8);

        stats.innerHTML = `
          <div class="stat-pill">Top-Left Date (n): <strong>${n}</strong></div>
          <div class="stat-pill">Diagonal 1 [${n} + ${n+8}]: <strong>${d1_sum}</strong></div>
          <div class="stat-pill">Diagonal 2 [${n+1} + ${n+7}]: <strong>${d2_sum}</strong></div>
          <div class="stat-pill">Product Difference: <strong style="color:#10b981;">${prod_diff} (Always = 7!)</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Calendar Day Headers
        const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        const cellW = 44;
        const cellH = 34;
        const startX = 75;
        const startY = 35;

        days.forEach((d, idx) => {
          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", startX + idx * cellW + cellW / 2);
          txt.setAttribute("y", startY - 8);
          txt.setAttribute("fill", idx === 0 ? "#f43f5e" : "#94a3b8");
          txt.setAttribute("font-size", "11");
          txt.setAttribute("font-weight", "bold");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = d;
          svg.appendChild(txt);
        });

        // Draw month dates (1 to 31)
        for (let dt = 1; dt <= 31; dt++) {
          const r = Math.floor((dt - 1) / 7);
          const c = (dt - 1) % 7;
          const x = startX + c * cellW;
          const y = startY + r * cellH;

          const isSelected = (dt === n || dt === n + 1 || dt === n + 7 || dt === n + 8);

          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", x);
          rect.setAttribute("y", y);
          rect.setAttribute("width", cellW);
          rect.setAttribute("height", cellH);
          rect.setAttribute("fill", isSelected ? "rgba(99, 102, 241, 0.35)" : "#0f172a");
          rect.setAttribute("stroke", isSelected ? "#38bdf8" : "rgba(255,255,255,0.08)");
          rect.setAttribute("stroke-width", isSelected ? "2" : "1");
          rect.setAttribute("rx", "6");
          rect.style.cursor = "pointer";
          rect.onclick = () => {
            if (dt % 7 !== 0 && dt <= 23) {
              startDay = dt;
              update();
            }
          };
          svg.appendChild(rect);

          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", x + cellW / 2);
          txt.setAttribute("y", y + cellH / 2 + 5);
          txt.setAttribute("fill", isSelected ? "#ffffff" : "#cbd5e1");
          txt.setAttribute("font-size", "12");
          txt.setAttribute("font-weight", isSelected ? "bold" : "normal");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = dt;
          txt.style.pointerEvents = "none";
          svg.appendChild(txt);
        }

        // Highlight frame
        const selR = Math.floor((n - 1) / 7);
        const selC = (n - 1) % 7;
        const fx = startX + selC * cellW;
        const fy = startY + selR * cellH;

        const frame = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        frame.setAttribute("x", fx);
        frame.setAttribute("y", fy);
        frame.setAttribute("width", cellW * 2);
        frame.setAttribute("height", cellH * 2);
        frame.setAttribute("fill", "none");
        frame.setAttribute("stroke", "#f59e0b");
        frame.setAttribute("stroke-width", "2.5");
        frame.setAttribute("rx", "6");
        svg.appendChild(frame);

        // Lower math verification
        const mathTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        mathTxt.setAttribute("x", "230");
        mathTxt.setAttribute("y", "265");
        mathTxt.setAttribute("fill", "#cbd5e1");
        mathTxt.setAttribute("font-size", "13");
        mathTxt.setAttribute("font-weight", "600");
        mathTxt.setAttribute("text-anchor", "middle");
        mathTxt.textContent = `Diagonal Sums: ${n} + ${n+8} = ${d1_sum}  and  ${n+1} + ${n+7} = ${d2_sum}`;
        svg.appendChild(mathTxt);

        const diffTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        diffTxt.setAttribute("x", "230");
        diffTxt.setAttribute("y", "295");
        diffTxt.setAttribute("fill", "#10b981");
        diffTxt.setAttribute("font-size", "13");
        diffTxt.setAttribute("font-weight", "bold");
        diffTxt.setAttribute("text-anchor", "middle");
        diffTxt.textContent = `Product Diff: (${n+1} × ${n+7}) - (${n} × ${n+8}) = 7 (Row Step d = 7!)`;
        svg.appendChild(diffTxt);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "330");
        tip.setAttribute("fill", "#38bdf8");
        tip.setAttribute("font-size", "11.5");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "Click any valid date on the calendar to position the 2×2 magic window!";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <button class="sim-btn" onclick="stepCal(-1)">◀ Prev Day</button>
          <button class="sim-btn" onclick="stepCal(1)">Next Day ▶</button>
          <button class="sim-btn" onclick="stepCal(-7)">▲ Up 1 Week</button>
          <button class="sim-btn" onclick="stepCal(7)">▼ Down 1 Week</button>
          <button class="sim-btn" onclick="randCal()">🎲 Random Window</button>
        </div>
      `;

      window.stepCal = (delta) => {
        const next = startDay + delta;
        if (next >= 1 && next <= 23 && next % 7 !== 0) {
          startDay = next;
          update();
        }
      };

      window.randCal = () => {
        const valid = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19];
        startDay = valid[Math.floor(Math.random() * valid.length)];
        update();
      };

      update();
    }

    // 9. Calendar Magic: 3x3 Revealer (Sum/9)
    function renderCalendarMagic3x3Revealer(title, stats, canvas, controls) {
      title.textContent = "3x3 Calendar Mind Reader: Sum / 9 Secret Revealer";
      let centerDate = 16;
      let maskCenter = false;

      function update() {
        const c = centerDate;
        const sum = 9 * c;

        stats.innerHTML = `
          <div class="stat-pill">Volunteer's Sum: <strong style="color:#f59e0b;">${sum}</strong></div>
          <div class="stat-pill">Predicted Center: <strong style="color:#10b981;">${maskCenter ? '??' : c} (Sum ÷ 9)</strong></div>
          <div class="stat-pill">Smallest Date: <strong>${maskCenter ? '??' : c - 8}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        const offsets = [
          [-8, -7, -6],
          [-1, 0, 1],
          [6, 7, 8]
        ];

        const cellW = 85;
        const cellH = 55;
        const startX = 100;
        const startY = 40;

        for (let r = 0; r < 3; r++) {
          for (let col = 0; col < 3; col++) {
            const off = offsets[r][col];
            const dateVal = c + off;
            const x = startX + col * (cellW + 8);
            const y = startY + r * (cellH + 8);
            const isCenter = (r === 1 && col === 1);

            const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            rect.setAttribute("x", x);
            rect.setAttribute("y", y);
            rect.setAttribute("width", cellW);
            rect.setAttribute("height", cellH);
            rect.setAttribute("rx", "10");
            rect.setAttribute("fill", isCenter ? (maskCenter ? "#1e1b4b" : "rgba(16, 185, 129, 0.25)") : "#0f172a");
            rect.setAttribute("stroke", isCenter ? "#10b981" : "#38bdf8");
            rect.setAttribute("stroke-width", isCenter ? "2.5" : "1.5");
            svg.appendChild(rect);

            const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
            txt.setAttribute("x", x + cellW / 2);
            txt.setAttribute("y", y + cellH / 2 + 5);
            txt.setAttribute("fill", isCenter ? "#34d399" : "#f8fafc");
            txt.setAttribute("font-size", isCenter && maskCenter ? "24" : "16");
            txt.setAttribute("font-weight", "bold");
            txt.setAttribute("text-anchor", "middle");
            txt.textContent = (isCenter && maskCenter) ? "❓" : dateVal;
            svg.appendChild(txt);

            const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
            sub.setAttribute("x", x + cellW / 2);
            sub.setAttribute("y", y + cellH - 7);
            sub.setAttribute("fill", "#94a3b8");
            sub.setAttribute("font-size", "9.5");
            sub.setAttribute("text-anchor", "middle");
            sub.textContent = isCenter ? "Center (c)" : (off > 0 ? `c + ${off}` : `c - ${Math.abs(off)}`);
            svg.appendChild(sub);
          }
        }

        // Explanation text
        const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
        t.setAttribute("x", "230");
        t.setAttribute("y", "265");
        t.setAttribute("fill", "#cbd5e1");
        t.setAttribute("font-size", "13");
        t.setAttribute("font-weight", "bold");
        t.setAttribute("text-anchor", "middle");
        t.textContent = maskCenter ? "Mind Reader Challenge: Can you find the hidden center from the sum?" : `Mind Reader Equation: c = Sum / 9 = ${sum} / 9 = ${c}`;
        svg.appendChild(t);

        const subT = document.createElementNS("http://www.w3.org/2000/svg", "text");
        subT.setAttribute("x", "230");
        subT.setAttribute("y", "295");
        subT.setAttribute("fill", "#f59e0b");
        subT.setAttribute("font-size", "12");
        subT.setAttribute("text-anchor", "middle");
        subT.textContent = `Min Date: ${c - 8}th • Max Date: ${c + 8}th • Symmetric Offset Sum = 0`;
        svg.appendChild(subT);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Center Date:</span>
          <input type="range" class="control-slider" min="10" max="22" value="${centerDate}" id="sliderCalC">
          <span class="control-val" id="valCalC">${centerDate}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="toggleMaskCenter()">${maskCenter ? '👁 Reveal Center' : '🎭 Mask Center'}</button>
          <button class="sim-btn" onclick="setCalC(15)">Center = 15th</button>
          <button class="sim-btn" onclick="setCalC(18)">Center = 18th</button>
          <button class="sim-btn" onclick="setCalC(Math.floor(Math.random()*12)+10)">🎲 Random Square</button>
        </div>
      `;

      document.getElementById('sliderCalC').oninput = (e) => {
        centerDate = parseInt(e.target.value);
        document.getElementById('valCalC').textContent = centerDate;
        update();
      };

      window.toggleMaskCenter = () => {
        maskCenter = !maskCenter;
        update();
      };

      window.setCalC = (v) => {
        centerDate = v;
        document.getElementById('sliderCalC').value = centerDate;
        document.getElementById('valCalC').textContent = centerDate;
        update();
      };

      update();
    }

    // 10. Calendar Cross Plus Shape
    function renderCalendarCrossPlusShape(title, stats, canvas, controls) {
      title.textContent = "Calendar Plus (+) Cross: 5-Date Centroid Invariant";
      let center = 17;
      let shapeType = 'plus'; // 'plus' or 'x_shape'

      function update() {
        const c = center;
        const sum = 5 * c;

        stats.innerHTML = `
          <div class="stat-pill">Center Date (c): <strong>${c}</strong></div>
          <div class="stat-pill">Pattern: <strong>${shapeType === 'plus' ? 'Plus (+)' : 'Diagonal (X)'}</strong></div>
          <div class="stat-pill">5-Date Sum: <strong style="color:#10b981;">${sum} (Always = 5c!)</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Coordinates in 3x3 local grid
        const positions = shapeType === 'plus' ? [
          { r: 0, col: 1, off: -7, lbl: "Top (c-7)" },
          { r: 1, col: 0, off: -1, lbl: "Left (c-1)" },
          { r: 1, col: 1, off: 0, lbl: "Center (c)" },
          { r: 1, col: 2, off: 1, lbl: "Right (c+1)" },
          { r: 2, col: 1, off: 7, lbl: "Bottom (c+7)" }
        ] : [
          { r: 0, col: 0, off: -8, lbl: "Top-L (c-8)" },
          { r: 0, col: 2, off: -6, lbl: "Top-R (c-6)" },
          { r: 1, col: 1, off: 0, lbl: "Center (c)" },
          { r: 2, col: 0, off: 6, lbl: "Bot-L (c+6)" },
          { r: 2, col: 2, off: 8, lbl: "Bot-R (c+8)" }
        ];

        const cellW = 80;
        const cellH = 50;
        const startX = 110;
        const startY = 35;

        positions.forEach(pos => {
          const x = startX + pos.col * (cellW + 10);
          const y = startY + pos.r * (cellH + 10);
          const isC = (pos.off === 0);

          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", x);
          rect.setAttribute("y", y);
          rect.setAttribute("width", cellW);
          rect.setAttribute("height", cellH);
          rect.setAttribute("rx", "10");
          rect.setAttribute("fill", isC ? "rgba(245, 158, 11, 0.25)" : "#0f172a");
          rect.setAttribute("stroke", isC ? "#f59e0b" : "#38bdf8");
          rect.setAttribute("stroke-width", isC ? "2.5" : "1.5");
          svg.appendChild(rect);

          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", x + cellW / 2);
          txt.setAttribute("y", y + cellH / 2 + 5);
          txt.setAttribute("fill", isC ? "#fbbf24" : "#f8fafc");
          txt.setAttribute("font-size", "16");
          txt.setAttribute("font-weight", "bold");
          txt.setAttribute("text-anchor", "middle");
          txt.textContent = c + pos.off;
          svg.appendChild(txt);

          const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
          sub.setAttribute("x", x + cellW / 2);
          sub.setAttribute("y", y + cellH - 5);
          sub.setAttribute("fill", "#94a3b8");
          sub.setAttribute("font-size", "9.5");
          sub.setAttribute("text-anchor", "middle");
          sub.textContent = pos.lbl;
          svg.appendChild(sub);
        });

        // Math cancellation text
        const algTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        algTxt.setAttribute("x", "230");
        algTxt.setAttribute("y", "265");
        algTxt.setAttribute("fill", "#cbd5e1");
        algTxt.setAttribute("font-size", "12.5");
        algTxt.setAttribute("font-weight", "600");
        algTxt.setAttribute("text-anchor", "middle");
        if (shapeType === 'plus') {
          algTxt.textContent = `Sum = (${c}-7) + (${c}+7) + (${c}-1) + (${c}+1) + ${c} = 5c`;
        } else {
          algTxt.textContent = `Sum = (${c}-8) + (${c}+8) + (${c}-6) + (${c}+6) + ${c} = 5c`;
        }
        svg.appendChild(algTxt);

        const sumTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        sumTxt.setAttribute("x", "230");
        sumTxt.setAttribute("y", "295");
        sumTxt.setAttribute("fill", "#10b981");
        sumTxt.setAttribute("font-size", "14");
        sumTxt.setAttribute("font-weight", "bold");
        sumTxt.setAttribute("text-anchor", "middle");
        sumTxt.textContent = `Total 5-Date Sum = 5 × ${c} = ${sum}`;
        svg.appendChild(sumTxt);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "330");
        tip.setAttribute("fill", "#38bdf8");
        tip.setAttribute("font-size", "11.5");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "✨ All deviations cancel out symmetrically to zero! Center c = Sum / 5";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Center Date:</span>
          <input type="range" class="control-slider" min="9" max="23" value="${center}" id="sliderCrossC">
          <span class="control-val" id="valCrossC">${center}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn ${shapeType === 'plus' ? 'active' : ''}" onclick="setShape('plus')">✚ Plus Shape (+)</button>
          <button class="sim-btn ${shapeType === 'x_shape' ? 'active' : ''}" onclick="setShape('x_shape')">✖ Diagonal Cross (X)</button>
          <button class="sim-btn" onclick="randCross()">🎲 Random Center</button>
        </div>
      `;

      document.getElementById('sliderCrossC').oninput = (e) => {
        center = parseInt(e.target.value);
        document.getElementById('valCrossC').textContent = center;
        update();
      };

      window.setShape = (st) => {
        shapeType = st;
        update();
      };

      window.randCross = () => {
        center = Math.floor(Math.random() * 15) + 9;
        document.getElementById('sliderCrossC').value = center;
        document.getElementById('valCrossC').textContent = center;
        update();
      };

      update();
    }

    // 11. Algebra Grid: Area Model for (x+a)(x+b)
    function renderAlgebraGridAreaMultiplication(title, stats, canvas, controls) {
      title.textContent = "Algebra Grid: Geometric Area Multiplication (x + a)(x + b)";
      let x = 4;
      let a = 3;
      let b = 2;

      function update() {
        const areaX2 = x * x;
        const areaAX = a * x;
        const areaBX = b * x;
        const areaAB = a * b;
        const totalArea = (x + a) * (x + b);

        stats.innerHTML = `
          <div class="stat-pill">Dimensions: <strong>(${x} + ${a}) × (${x} + ${b})</strong></div>
          <div class="stat-pill">Total Area: <strong style="color:#10b981;">${totalArea}</strong></div>
          <div class="stat-pill">Polynomial: <strong style="color:#a855f7;">x² + ${a+b}x + ${ab}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Scale visual pixels
        const scaleX = 220 / (x + a);
        const scaleY = 180 / (x + b);

        const wX = x * scaleX;
        const wA = a * scaleX;
        const hX = x * scaleY;
        const hB = b * scaleY;

        const startX = 80;
        const startY = 60;

        function drawQuad(qx, qy, qw, qh, color, label, mathVal) {
          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", qx);
          r.setAttribute("y", qy);
          r.setAttribute("width", qw);
          r.setAttribute("height", qh);
          r.setAttribute("fill", color);
          r.setAttribute("stroke", "#ffffff");
          r.setAttribute("stroke-width", "1.5");
          svg.appendChild(r);

          const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
          t.setAttribute("x", qx + qw / 2);
          t.setAttribute("y", qy + qh / 2 + 4);
          t.setAttribute("fill", "#ffffff");
          t.setAttribute("font-size", "14");
          t.setAttribute("font-weight", "bold");
          t.setAttribute("text-anchor", "middle");
          t.textContent = `${label} = ${mathVal}`;
          svg.appendChild(t);
        }

        // Top-Left: x * x = x² (Blue)
        drawQuad(startX, startY, wX, hX, "rgba(59, 130, 246, 0.6)", "x²", areaX2);

        // Top-Right: a * x = ax (Cyan)
        drawQuad(startX + wX, startY, wA, hX, "rgba(6, 182, 212, 0.6)", `${a}x`, areaAX);

        // Bottom-Left: b * x = bx (Amber)
        drawQuad(startX, startY + hX, wX, hB, "rgba(245, 158, 11, 0.6)", `${b}x`, areaBX);

        // Bottom-Right: a * b = ab (Emerald)
        drawQuad(startX + wX, startY + hX, wA, hB, "rgba(16, 185, 129, 0.6)", `${a}×${b}`, areaAB);

        // Dimension labels
        const topW = document.createElementNS("http://www.w3.org/2000/svg", "text");
        topW.setAttribute("x", startX + wX / 2);
        topW.setAttribute("y", startY - 10);
        topW.setAttribute("fill", "#60a5fa");
        topW.setAttribute("font-size", "13");
        topW.setAttribute("font-weight", "bold");
        topW.setAttribute("text-anchor", "middle");
        topW.textContent = `x = ${x}`;
        svg.appendChild(topW);

        const topA = document.createElementNS("http://www.w3.org/2000/svg", "text");
        topA.setAttribute("x", startX + wX + wA / 2);
        topA.setAttribute("y", startY - 10);
        topA.setAttribute("fill", "#22d3ee");
        topA.setAttribute("font-size", "13");
        topA.setAttribute("font-weight", "bold");
        topA.setAttribute("text-anchor", "middle");
        topA.textContent = `a = ${a}`;
        svg.appendChild(topA);

        const leftH = document.createElementNS("http://www.w3.org/2000/svg", "text");
        leftH.setAttribute("x", startX - 15);
        leftH.setAttribute("y", startY + hX / 2);
        leftH.setAttribute("fill", "#60a5fa");
        leftH.setAttribute("font-size", "13");
        leftH.setAttribute("font-weight", "bold");
        leftH.setAttribute("text-anchor", "end");
        leftH.textContent = `x = ${x}`;
        svg.appendChild(leftH);

        const leftB = document.createElementNS("http://www.w3.org/2000/svg", "text");
        leftB.setAttribute("x", startX - 15);
        leftB.setAttribute("y", startY + hX + hB / 2);
        leftB.setAttribute("fill", "#fbbf24");
        leftB.setAttribute("font-size", "13");
        leftB.setAttribute("font-weight", "bold");
        leftB.setAttribute("text-anchor", "end");
        leftB.textContent = `b = ${b}`;
        svg.appendChild(leftB);

        // Formula conclusion
        const f1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        f1.setAttribute("x", "230");
        f1.setAttribute("y", "295");
        f1.setAttribute("fill", "#cbd5e1");
        f1.setAttribute("font-size", "13.5");
        f1.setAttribute("font-weight", "bold");
        f1.setAttribute("text-anchor", "middle");
        f1.textContent = `(x + ${a})(x + ${b}) = x² + (${a} + ${b})x + (${a} × ${b})`;
        svg.appendChild(f1);

        const f2 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        f2.setAttribute("x", "230");
        f2.setAttribute("y", "325");
        f2.setAttribute("fill", "#10b981");
        f2.setAttribute("font-size", "13");
        f2.setAttribute("font-weight", "bold");
        f2.setAttribute("text-anchor", "middle");
        f2.textContent = `Numerical: ${areaX2} + ${areaAX} + ${areaBX} + ${areaAB} = ${totalArea} sq units`;
        svg.appendChild(f2);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Variable x:</span>
          <input type="range" class="control-slider" min="2" max="8" value="${x}" id="sliderGridX">
          <span class="control-val" id="valGridX">${x}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Constant a:</span>
          <input type="range" class="control-slider" min="1" max="6" value="${a}" id="sliderGridA">
          <span class="control-val" id="valGridA">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Constant b:</span>
          <input type="range" class="control-slider" min="1" max="6" value="${b}" id="sliderGridB">
          <span class="control-val" id="valGridB">${b}</span>
        </div>
      `;

      document.getElementById('sliderGridX').oninput = (e) => {
        x = parseInt(e.target.value);
        document.getElementById('valGridX').textContent = x;
        update();
      };
      document.getElementById('sliderGridA').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valGridA').textContent = a;
        update();
      };
      document.getElementById('sliderGridB').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valGridB').textContent = b;
        update();
      };

      update();
    }

    // 12. Visual Identities: Square Geometry
    function renderVisualIdentitiesSquareGeometry(title, stats, canvas, controls) {
      title.textContent = "Geometric Proof of Identities: (a + b)² and (a - b)²";
      let a = 5;
      let b = 3;
      let mode = 'plus'; // 'plus' or 'minus'

      function update() {
        const areaTotal = mode === 'plus' ? (a + b) * (a + b) : (a - b) * (a - b);

        stats.innerHTML = `
          <div class="stat-pill">Identity: <strong>${mode === 'plus' ? '(a + b)²' : '(a - b)²'}</strong></div>
          <div class="stat-pill">Dimensions: <strong>a = ${a}, b = ${b}</strong></div>
          <div class="stat-pill">Total Area: <strong style="color:#10b981;">${areaTotal}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        if (mode === 'plus') {
          // Dissection of (a + b)²
          const startX = 110;
          const startY = 40;
          const scale = 220 / (a + b);
          const wA = a * scale;
          const wB = b * scale;

          function drawBlock(x, y, w, h, col, txt) {
            const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            r.setAttribute("x", x);
            r.setAttribute("y", y);
            r.setAttribute("width", w);
            r.setAttribute("height", h);
            r.setAttribute("fill", col);
            r.setAttribute("stroke", "#ffffff");
            r.setAttribute("stroke-width", "1.5");
            svg.appendChild(r);

            const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
            t.setAttribute("x", x + w / 2);
            t.setAttribute("y", y + h / 2 + 5);
            t.setAttribute("fill", "#ffffff");
            t.setAttribute("font-size", "14");
            t.setAttribute("font-weight", "bold");
            t.setAttribute("text-anchor", "middle");
            t.textContent = txt;
            svg.appendChild(t);
          }

          // a² (Indigo)
          drawBlock(startX, startY, wA, wA, "rgba(99, 102, 241, 0.7)", `a² = ${a * a}`);
          // ab (Cyan)
          drawBlock(startX + wA, startY, wB, wA, "rgba(6, 182, 212, 0.6)", `ab = ${a * b}`);
          // ab (Cyan)
          drawBlock(startX, startY + wA, wA, wB, "rgba(6, 182, 212, 0.6)", `ab = ${a * b}`);
          // b² (Amber)
          drawBlock(startX + wA, startY + wA, wB, wB, "rgba(245, 158, 11, 0.7)", `b² = ${b * b}`);

          const eq = document.createElementNS("http://www.w3.org/2000/svg", "text");
          eq.setAttribute("x", "230");
          eq.setAttribute("y", "295");
          eq.setAttribute("fill", "#cbd5e1");
          eq.setAttribute("font-size", "13.5");
          eq.setAttribute("font-weight", "bold");
          eq.setAttribute("text-anchor", "middle");
          eq.textContent = `(${a} + ${b})² = ${a}² + 2(${a})(${b}) + ${b}² = ${a*a} + ${2*a*b} + ${b*b} = ${areaTotal}`;
          svg.appendChild(eq);

          const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
          tip.setAttribute("x", "230");
          tip.setAttribute("y", "325");
          tip.setAttribute("fill", "#38bdf8");
          tip.setAttribute("font-size", "11.5");
          tip.setAttribute("text-anchor", "middle");
          tip.textContent = "Notice the two identical rectangular regions (2ab)! That is why (a+b)² ≠ a² + b².";
          svg.appendChild(tip);

        } else {
          // Geometric proof of (a - b)²
          const startX = 110;
          const startY = 40;
          const scale = 220 / a;
          const wA = a * scale;
          const wB = b * scale;
          const wDiff = (a - b) * scale;

          // Full a² square
          const baseSq = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          baseSq.setAttribute("x", startX);
          baseSq.setAttribute("y", startY);
          baseSq.setAttribute("width", wA);
          baseSq.setAttribute("height", wA);
          baseSq.setAttribute("fill", "rgba(99, 102, 241, 0.2)");
          baseSq.setAttribute("stroke", "#6366f1");
          baseSq.setAttribute("stroke-width", "2");
          svg.appendChild(baseSq);

          // (a-b)² inner square
          const innerSq = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          innerSq.setAttribute("x", startX);
          innerSq.setAttribute("y", startY);
          innerSq.setAttribute("width", wDiff);
          innerSq.setAttribute("height", wDiff);
          innerSq.setAttribute("fill", "rgba(16, 185, 129, 0.6)");
          innerSq.setAttribute("stroke", "#10b981");
          innerSq.setAttribute("stroke-width", "2");
          svg.appendChild(innerSq);

          const inTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          inTxt.setAttribute("x", startX + wDiff / 2);
          inTxt.setAttribute("y", startY + wDiff / 2 + 5);
          inTxt.setAttribute("fill", "#ffffff");
          inTxt.setAttribute("font-size", "14");
          inTxt.setAttribute("font-weight", "bold");
          inTxt.setAttribute("text-anchor", "middle");
          inTxt.textContent = `(a - b)² = ${areaTotal}`;
          svg.appendChild(inTxt);

          // Subtracted corners
          const cutTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          cutTxt.setAttribute("x", startX + wDiff + wB / 2);
          cutTxt.setAttribute("y", startY + wDiff + wB / 2 + 5);
          cutTxt.setAttribute("fill", "#f43f5e");
          cutTxt.setAttribute("font-size", "13");
          cutTxt.setAttribute("font-weight", "bold");
          cutTxt.setAttribute("text-anchor", "middle");
          cutTxt.textContent = `+ b²`;
          svg.appendChild(cutTxt);

          const eq = document.createElementNS("http://www.w3.org/2000/svg", "text");
          eq.setAttribute("x", "230");
          eq.setAttribute("y", "295");
          eq.setAttribute("fill", "#cbd5e1");
          eq.setAttribute("font-size", "13.5");
          eq.setAttribute("font-weight", "bold");
          eq.setAttribute("text-anchor", "middle");
          eq.textContent = `(${a} - ${b})² = a² - 2ab + b² = ${a*a} - ${2*a*b} + ${b*b} = ${areaTotal}`;
          svg.appendChild(eq);

          const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
          tip.setAttribute("x", "230");
          tip.setAttribute("y", "325");
          tip.setAttribute("fill", "#f59e0b");
          tip.setAttribute("font-size", "11.5");
          tip.setAttribute("text-anchor", "middle");
          tip.textContent = "Corner b² was subtracted twice (once with each ab stripe), so we must add it back!";
          svg.appendChild(tip);
        }

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Dimension a:</span>
          <input type="range" class="control-slider" min="4" max="8" value="${a}" id="sliderIdA">
          <span class="control-val" id="valIdA">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Dimension b:</span>
          <input type="range" class="control-slider" min="1" max="3" value="${b}" id="sliderIdB">
          <span class="control-val" id="valIdB">${b}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn ${mode === 'plus' ? 'active' : ''}" onclick="setIdMode('plus')">📐 (a + b)² Addition</button>
          <button class="sim-btn ${mode === 'minus' ? 'active' : ''}" onclick="setIdMode('minus')">✂️ (a - b)² Subtraction</button>
        </div>
      `;

      document.getElementById('sliderIdA').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valIdA').textContent = a;
        update();
      };
      document.getElementById('sliderIdB').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valIdB').textContent = b;
        update();
      };

      window.setIdMode = (m) => {
        mode = m;
        update();
      };

      update();
    }

    // 13. Largest Product: Fixed Sum Slider
    function renderLargestProductFixedSumSlider(title, stats, canvas, controls) {
      title.textContent = "Largest Product: Fixed Sum (S = 20) & The Square Maximizer";
      let x = 10;
      const S = 20;

      function update() {
        const y = S - x;
        const product = x * y;
        const maxProd = (S / 2) * (S / 2);
        const isMax = (x === y);

        stats.innerHTML = `
          <div class="stat-pill">Sum: <strong>${x} + ${y} = ${S}</strong></div>
          <div class="stat-pill">Product (x × y): <strong style="color:${isMax ? '#10b981' : '#38bdf8'};">${product}</strong></div>
          <div class="stat-pill">Global Max: <strong style="color:#10b981;">100 (Square 10×10)</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Left: Geometric Rectangle representation
        const rectW = x * 8;
        const rectH = y * 8;
        const rX = 40 + (160 - rectW) / 2;
        const rY = 50 + (160 - rectH) / 2;

        const geomR = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        geomR.setAttribute("x", rX);
        geomR.setAttribute("y", rY);
        geomR.setAttribute("width", rectW);
        geomR.setAttribute("height", rectH);
        geomR.setAttribute("fill", isMax ? "rgba(16, 185, 129, 0.35)" : "rgba(99, 102, 241, 0.35)");
        geomR.setAttribute("stroke", isMax ? "#10b981" : "#818cf8");
        geomR.setAttribute("stroke-width", "2");
        geomR.setAttribute("rx", "6");
        svg.appendChild(geomR);

        const rTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        rTxt.setAttribute("x", rX + rectW / 2);
        rTxt.setAttribute("y", rY + rectH / 2 + 5);
        rTxt.setAttribute("fill", "#ffffff");
        rTxt.setAttribute("font-size", "14");
        rTxt.setAttribute("font-weight", "bold");
        rTxt.setAttribute("text-anchor", "middle");
        rTxt.textContent = `${x} × ${y} = ${product}`;
        svg.appendChild(rTxt);

        // Right: Parabola Curve P(x) = x(20 - x)
        const pStartX = 240;
        const pStartY = 200;
        const pW = 180;
        const pH = 150;

        // Axes
        const axisX = document.createElementNS("http://www.w3.org/2000/svg", "line");
        axisX.setAttribute("x1", pStartX);
        axisX.setAttribute("y1", pStartY);
        axisX.setAttribute("x2", pStartX + pW);
        axisX.setAttribute("y2", pStartY);
        axisX.setAttribute("stroke", "#64748b");
        axisX.setAttribute("stroke-width", "2");
        svg.appendChild(axisX);

        // Plot parabola curve points
        const pts = [];
        for (let px = 0; px <= 20; px++) {
          const py = px * (20 - px); // 0 to 100
          const cx = pStartX + (px / 20) * pW;
          const cy = pStartY - (py / 100) * pH;
          pts.push(`${cx},${cy}`);
        }

        const curve = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
        curve.setAttribute("points", pts.join(' '));
        curve.setAttribute("fill", "none");
        curve.setAttribute("stroke", "#38bdf8");
        curve.setAttribute("stroke-width", "2.5");
        svg.appendChild(curve);

        // Current point marker on parabola
        const curX = pStartX + (x / 20) * pW;
        const curY = pStartY - (product / 100) * pH;

        const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        dot.setAttribute("cx", curX);
        dot.setAttribute("cy", curY);
        dot.setAttribute("r", "6");
        dot.setAttribute("fill", isMax ? "#10b981" : "#f59e0b");
        dot.setAttribute("stroke", "#ffffff");
        dot.setAttribute("stroke-width", "2");
        svg.appendChild(dot);

        // Peak line
        if (isMax) {
          const peakLbl = document.createElementNS("http://www.w3.org/2000/svg", "text");
          peakLbl.setAttribute("x", curX);
          peakLbl.setAttribute("y", curY - 12);
          peakLbl.setAttribute("fill", "#10b981");
          peakLbl.setAttribute("font-size", "11");
          peakLbl.setAttribute("font-weight", "bold");
          peakLbl.setAttribute("text-anchor", "middle");
          peakLbl.textContent = "PEAK: (10, 100)";
          svg.appendChild(peakLbl);
        }

        // Explanatory text below
        const f = document.createElementNS("http://www.w3.org/2000/svg", "text");
        f.setAttribute("x", "230");
        f.setAttribute("y", "260");
        f.setAttribute("fill", "#cbd5e1");
        f.setAttribute("font-size", "13");
        f.setAttribute("font-weight", "bold");
        f.setAttribute("text-anchor", "middle");
        f.textContent = `Product: P(x) = x(20 - x) = 100 - (x - 10)²`;
        svg.appendChild(f);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "295");
        tip.setAttribute("fill", isMax ? "#10b981" : "#f59e0b");
        tip.setAttribute("font-size", "12");
        tip.setAttribute("font-weight", "600");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = isMax ? "🎉 Maximum Reached: A square (10 × 10) encloses greatest area!" : `Move the slider to x = 10 to reach the maximum product 100!`;
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Split x:</span>
          <input type="range" class="control-slider" min="1" max="19" value="${x}" id="sliderMaxX">
          <span class="control-val" id="valMaxX">${x}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="setMaxX(10)">⭐ Set Square (x = 10)</button>
          <button class="sim-btn" onclick="setMaxX(5)">x = 5</button>
          <button class="sim-btn" onclick="setMaxX(15)">x = 15</button>
          <button class="sim-btn" onclick="setMaxX(1)">Extreme (x = 1)</button>
        </div>
      `;

      document.getElementById('sliderMaxX').oninput = (e) => {
        x = parseInt(e.target.value);
        document.getElementById('valMaxX').textContent = x;
        update();
      };

      window.setMaxX = (v) => {
        x = v;
        document.getElementById('sliderMaxX').value = x;
        document.getElementById('valMaxX').textContent = x;
        update();
      };

      update();
    }

    // 14. Partitioning Product Optimizer (Rule of 3s)
    function renderPartitioningProductOptimizer(title, stats, canvas, controls) {
      title.textContent = "Integer Partition Product Maximizer: The Power of 3s";
      let N = 10;

      function getOptimalPartition(n) {
        if (n <= 3) return [n];
        let parts = [];
        let rem = n;
        while (rem > 4) {
          parts.push(3);
          rem -= 3;
        }
        if (rem === 4) {
          parts.push(2, 2);
        } else {
          parts.push(rem);
        }
        return parts;
      }

      function update() {
        const optParts = getOptimalPartition(N);
        const optProd = optParts.reduce((a, b) => a * b, 1);

        stats.innerHTML = `
          <div class="stat-pill">Number (N): <strong>${N}</strong></div>
          <div class="stat-pill">Optimal Partition: <strong>${optParts.join(' + ')}</strong></div>
          <div class="stat-pill">Max Product: <strong style="color:#10b981;">${optProd}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Comparison partitions for N
        const candidatePartitions = [];
        candidatePartitions.push({ name: "Optimal (Power of 3s)", parts: optParts });

        if (N % 2 === 0) {
          const twos = Array(N / 2).fill(2);
          candidatePartitions.push({ name: "All 2s", parts: twos });
        }
        const halves = [Math.floor(N / 2), Math.ceil(N / 2)];
        candidatePartitions.push({ name: "Two Halves", parts: halves });

        let startY = 40;
        candidatePartitions.forEach((cand, idx) => {
          const prod = cand.parts.reduce((a, b) => a * b, 1);
          const isBest = (prod === optProd);

          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", "40");
          r.setAttribute("y", startY);
          r.setAttribute("width", "380");
          r.setAttribute("height", "60");
          r.setAttribute("rx", "10");
          r.setAttribute("fill", isBest ? "rgba(16, 185, 129, 0.15)" : "#0f172a");
          r.setAttribute("stroke", isBest ? "#10b981" : "rgba(255,255,255,0.1)");
          r.setAttribute("stroke-width", isBest ? "2" : "1");
          svg.appendChild(r);

          const titleT = document.createElementNS("http://www.w3.org/2000/svg", "text");
          titleT.setAttribute("x", "55");
          titleT.setAttribute("y", startY + 24);
          titleT.setAttribute("fill", isBest ? "#34d399" : "#cbd5e1");
          titleT.setAttribute("font-size", "12.5");
          titleT.setAttribute("font-weight", "bold");
          titleT.textContent = cand.name;
          svg.appendChild(titleT);

          const sumT = document.createElementNS("http://www.w3.org/2000/svg", "text");
          sumT.setAttribute("x", "55");
          sumT.setAttribute("y", startY + 45);
          sumT.setAttribute("fill", "#94a3b8");
          sumT.setAttribute("font-size", "11.5");
          sumT.textContent = `${cand.parts.join(' + ')} = ${N}`;
          svg.appendChild(sumT);

          const prodT = document.createElementNS("http://www.w3.org/2000/svg", "text");
          prodT.setAttribute("x", "390");
          prodT.setAttribute("y", startY + 35);
          prodT.setAttribute("fill", isBest ? "#34d399" : "#38bdf8");
          prodT.setAttribute("font-size", "16");
          prodT.setAttribute("font-weight", "bold");
          prodT.setAttribute("text-anchor", "end");
          prodT.textContent = `Product = ${prod} ${isBest ? '👑' : ''}`;
          svg.appendChild(prodT);

          startY += 75;
        });

        // Theorem of 3s takeaway
        const note = document.createElementNS("http://www.w3.org/2000/svg", "text");
        note.setAttribute("x", "230");
        note.setAttribute("y", "290");
        note.setAttribute("fill", "#cbd5e1");
        note.setAttribute("font-size", "12.5");
        note.setAttribute("font-weight", "bold");
        note.setAttribute("text-anchor", "middle");
        note.textContent = "Why 3? The optimal real base is e ≈ 2.718. The closest integer is 3!";
        svg.appendChild(note);

        const tip = document.createElementNS("http://www.w3.org/2000/svg", "text");
        tip.setAttribute("x", "230");
        tip.setAttribute("y", "320");
        tip.setAttribute("fill", "#f59e0b");
        tip.setAttribute("font-size", "11.5");
        tip.setAttribute("text-anchor", "middle");
        tip.textContent = "Break into 3s! If remainder is 1, use 2×2=4 instead of 3×1=3.";
        svg.appendChild(tip);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Integer N:</span>
          <input type="range" class="control-slider" min="4" max="24" value="${N}" id="sliderPartN">
          <span class="control-val" id="valPartN">${N}</span>
        </div>
        <div class="control-row">
          <button class="sim-btn" onclick="setNPart(8)">N = 8</button>
          <button class="sim-btn" onclick="setNPart(10)">N = 10</button>
          <button class="sim-btn" onclick="setNPart(12)">N = 12</button>
          <button class="sim-btn" onclick="setNPart(15)">N = 15</button>
          <button class="sim-btn" onclick="setNPart(20)">N = 20</button>
        </div>
      `;

      document.getElementById('sliderPartN').oninput = (e) => {
        N = parseInt(e.target.value);
        document.getElementById('valPartN').textContent = N;
        update();
      };

      window.setNPart = (v) => {
        N = v;
        document.getElementById('sliderPartN').value = N;
        document.getElementById('valPartN').textContent = N;
        update();
      };

      update();
    }

    // 15. Divisibility: 9 & 3 Decimal Expander
    function renderDivisibility9DecimalExpander(title, stats, canvas, controls) {
      title.textContent = "Divisibility by 9 & 3: Place Value Decomposition Lab";
      let a = 4, b = 7, c = 2; // Number 472

      function update() {
        const num = a * 100 + b * 10 + c;
        const digitSum = a + b + c;
        const isDiv9 = (num % 9 === 0);
        const isDiv3 = (num % 3 === 0);

        stats.innerHTML = `
          <div class="stat-pill">Number: <strong>${num}</strong></div>
          <div class="stat-pill">Sum of Digits: <strong>${a} + ${b} + ${c} = ${digitSum}</strong></div>
          <div class="stat-pill">Divisible by 9: <strong style="color:${isDiv9 ? '#10b981' : '#f43f5e'};">${isDiv9 ? 'YES (Rem 0)' : 'NO (Rem ' + (num % 9) + ')'}</strong></div>
          <div class="stat-pill">Divisible by 3: <strong style="color:${isDiv3 ? '#10b981' : '#f43f5e'};">${isDiv3 ? 'YES' : 'NO'}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Step by step breakdown cards
        const rows = [
          { place: "Hundreds", val: `${a} × 100`, exp: `${a} × (99 + 1)`, split: `${a} × 99  +  ${a}` },
          { place: "Tens", val: `${b} × 10`, exp: `${b} × (9 + 1)`, split: `${b} × 9  +  ${b}` },
          { place: "Units", val: `${c} × 1`, exp: `${c} × 1`, split: `0  +  ${c}` }
        ];

        let startY = 35;
        rows.forEach((r, idx) => {
          const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          rect.setAttribute("x", "40");
          rect.setAttribute("y", startY);
          rect.setAttribute("width", "380");
          rect.setAttribute("height", "50");
          rect.setAttribute("rx", "8");
          rect.setAttribute("fill", "#0f172a");
          rect.setAttribute("stroke", "rgba(99, 102, 241, 0.25)");
          rect.setAttribute("stroke-width", "1.5");
          svg.appendChild(rect);

          const pTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          pTxt.setAttribute("x", "55");
          pTxt.setAttribute("y", startY + 30);
          pTxt.setAttribute("fill", "#38bdf8");
          pTxt.setAttribute("font-size", "12");
          pTxt.setAttribute("font-weight", "bold");
          pTxt.textContent = r.place + ":";
          svg.appendChild(pTxt);

          const expTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          expTxt.setAttribute("x", "140");
          expTxt.setAttribute("y", startY + 30);
          expTxt.setAttribute("fill", "#cbd5e1");
          expTxt.setAttribute("font-size", "12");
          expTxt.textContent = `${r.val} = ${r.exp} = ${r.split}`;
          svg.appendChild(expTxt);

          startY += 60;
        });

        // Regrouped algebraic sum
        const reg1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        reg1.setAttribute("x", "230");
        reg1.setAttribute("y", "230");
        reg1.setAttribute("fill", "#a855f7");
        reg1.setAttribute("font-size", "13");
        reg1.setAttribute("font-weight", "bold");
        reg1.setAttribute("text-anchor", "middle");
        reg1.textContent = `Regrouped: 9(11 × ${a} + ${b})  +  (${a} + ${b} + ${c})`;
        svg.appendChild(reg1);

        const reg2 = document.createElementNS("http://www.w3.org/2000/svg", "text");
        reg2.setAttribute("x", "230");
        reg2.setAttribute("y", "260");
        reg2.setAttribute("fill", "#cbd5e1");
        reg2.setAttribute("font-size", "12.5");
        reg2.setAttribute("text-anchor", "middle");
        reg2.textContent = `= 9(${11 * a + b})  +  ${digitSum}  =  ${9 * (11 * a + b)} + ${digitSum} = ${num}`;
        svg.appendChild(reg2);

        // Final verdict
        const verd = document.createElementNS("http://www.w3.org/2000/svg", "text");
        verd.setAttribute("x", "230");
        verd.setAttribute("y", "300");
        verd.setAttribute("fill", isDiv9 ? "#10b981" : "#f59e0b");
        verd.setAttribute("font-size", "13.5");
        verd.setAttribute("font-weight", "bold");
        verd.setAttribute("text-anchor", "middle");
        verd.textContent = isDiv9 ? `✓ Digit sum ${digitSum} is divisible by 9 ➔ ${num} is divisible by 9!` : `✗ Digit sum ${digitSum} leaves remainder ${digitSum % 9} ➔ ${num} is not divisible by 9`;
        svg.appendChild(verd);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Hundreds (a):</span>
          <input type="range" class="control-slider" min="1" max="9" value="${a}" id="sliderDivA">
          <span class="control-val" id="valDivA">${a}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Tens (b):</span>
          <input type="range" class="control-slider" min="0" max="9" value="${b}" id="sliderDivB">
          <span class="control-val" id="valDivB">${b}</span>
        </div>
        <div class="control-row">
          <span class="control-label">Units (c):</span>
          <input type="range" class="control-slider" min="0" max="9" value="${c}" id="sliderDivC">
          <span class="control-val" id="valDivC">${c}</span>
        </div>
      `;

      document.getElementById('sliderDivA').oninput = (e) => {
        a = parseInt(e.target.value);
        document.getElementById('valDivA').textContent = a;
        update();
      };
      document.getElementById('sliderDivB').oninput = (e) => {
        b = parseInt(e.target.value);
        document.getElementById('valDivB').textContent = b;
        update();
      };
      document.getElementById('sliderDivC').oninput = (e) => {
        c = parseInt(e.target.value);
        document.getElementById('valDivC').textContent = c;
        update();
      };

      update();
    }

    // 16. Divisibility: 11 Alternating Canceller
    function renderDivisibility11AlternatingCanceller(title, stats, canvas, controls) {
      title.textContent = "Divisibility by 11: Alternating Remainder Seesaw";
      let d3 = 7, d2 = 3, d1 = 8, d0 = 1; // 7381

      function update() {
        const num = d3 * 1000 + d2 * 100 + d1 * 10 + d0;
        const altSum = d0 - d1 + d2 - d3;
        const isDiv11 = (altSum % 11 === 0);

        stats.innerHTML = `
          <div class="stat-pill">4-Digit Number: <strong>${num}</strong></div>
          <div class="stat-pill">Alternating Sum: <strong>(${d0} - ${d1} + ${d2} - ${d3}) = ${altSum}</strong></div>
          <div class="stat-pill">Divisible by 11: <strong style="color:${isDiv11 ? '#10b981' : '#f43f5e'};">${isDiv11 ? 'YES (Multiple of 11)' : 'NO'}</strong></div>
        `;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "100%");
        svg.setAttribute("height", "100%");
        svg.setAttribute("viewBox", "0 0 460 360");

        // Powers of 10 modulo 11 display
        const powers = [
          { name: "d3 (10³ = 1000)", mod: "-1", digit: d3, sign: -1, x: 70 },
          { name: "d2 (10² = 100)", mod: "+1", digit: d2, sign: 1, x: 175 },
          { name: "d1 (10¹ = 10)", mod: "-1", digit: d1, sign: -1, x: 280 },
          { name: "d0 (10⁰ = 1)", mod: "+1", digit: d0, sign: 1, x: 385 }
        ];

        powers.forEach(p => {
          const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
          r.setAttribute("x", p.x - 45);
          r.setAttribute("y", "40");
          r.setAttribute("width", "90");
          r.setAttribute("height", "75");
          r.setAttribute("rx", "10");
          r.setAttribute("fill", "#0f172a");
          r.setAttribute("stroke", p.sign === 1 ? "#10b981" : "#f43f5e");
          r.setAttribute("stroke-width", "2");
          svg.appendChild(r);

          const dt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          dt.setAttribute("x", p.x);
          dt.setAttribute("y", "72");
          dt.setAttribute("fill", "#ffffff");
          dt.setAttribute("font-size", "22");
          dt.setAttribute("font-weight", "bold");
          dt.setAttribute("text-anchor", "middle");
          dt.textContent = p.digit;
          svg.appendChild(dt);

          const mt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          mt.setAttribute("x", p.x);
          mt.setAttribute("y", "98");
          mt.setAttribute("fill", p.sign === 1 ? "#34d399" : "#fca5a5");
          mt.setAttribute("font-size", "11");
          mt.setAttribute("font-weight", "bold");
          mt.setAttribute("text-anchor", "middle");
          mt.textContent = `rem: ${p.mod}`;
          svg.appendChild(mt);
        });

        // Seesaw balance graphic
        const fulcrumX = 230;
        const fulcrumY = 240;

        // Angle tilt based on altSum
        const tiltDeg = Math.max(-15, Math.min(15, altSum * 2));
        const plankL = 140;

        const baseTriangle = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        baseTriangle.setAttribute("points", `${fulcrumX},${fulcrumY} ${fulcrumX - 25},${fulcrumY + 40} ${fulcrumX + 25},${fulcrumY + 40}`);
        baseTriangle.setAttribute("fill", "#64748b");
        svg.appendChild(baseTriangle);

        const plank = document.createElementNS("http://www.w3.org/2000/svg", "line");
        const rad = (tiltDeg * Math.PI) / 180;
        const dx = plankL * Math.cos(rad);
        const dy = plankL * Math.sin(rad);

        plank.setAttribute("x1", fulcrumX - dx);
        plank.setAttribute("y1", fulcrumY - dy);
        plank.setAttribute("x2", fulcrumX + dx);
        plank.setAttribute("y2", fulcrumY + dy);
        plank.setAttribute("stroke", isDiv11 ? "#10b981" : "#f59e0b");
        plank.setAttribute("stroke-width", "5");
        plank.setAttribute("stroke-linecap", "round");
        svg.appendChild(plank);

        // Pans
        const posSum = d0 + d2;
        const negSum = d1 + d3;

        const txtL = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txtL.setAttribute("x", fulcrumX - dx);
        txtL.setAttribute("y", fulcrumY - dy - 15);
        txtL.setAttribute("fill", "#fca5a5");
        txtL.setAttribute("font-size", "13");
        txtL.setAttribute("font-weight", "bold");
        txtL.setAttribute("text-anchor", "middle");
        txtL.textContent = `Odd places: ${negSum}`;
        svg.appendChild(txtL);

        const txtR = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txtR.setAttribute("x", fulcrumX + dx);
        txtR.setAttribute("y", fulcrumY + dy - 15);
        txtR.setAttribute("fill", "#6ee7b7");
        txtR.setAttribute("font-size", "13");
        txtR.setAttribute("font-weight", "bold");
        txtR.setAttribute("text-anchor", "middle");
        txtR.textContent = `Even places: ${posSum}`;
        svg.appendChild(txtR);

        // Verification banner
        const resTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        resTxt.setAttribute("x", "230");
        resTxt.setAttribute("y", "325");
        resTxt.setAttribute("fill", isDiv11 ? "#10b981" : "#cbd5e1");
        resTxt.setAttribute("font-size", "13.5");
        resTxt.setAttribute("font-weight", "bold");
        resTxt.setAttribute("text-anchor", "middle");
        resTxt.textContent = isDiv11 ? `✓ Balanced modulo 11: Difference ${altSum} is divisible by 11 (${num} = 11 × ${num/11})` : `Difference = ${posSum} - ${negSum} = ${altSum} (not a multiple of 11)`;
        svg.appendChild(resTxt);

        canvas.innerHTML = '';
        canvas.appendChild(svg);
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">d3 (1000s):</span>
          <input type="range" class="control-slider" min="1" max="9" value="${d3}" id="sliderD3">
          <span class="control-val" id="valD3">${d3}</span>
        </div>
        <div class="control-row">
          <span class="control-label">d2 (100s):</span>
          <input type="range" class="control-slider" min="0" max="9" value="${d2}" id="sliderD2">
          <span class="control-val" id="valD2">${d2}</span>
        </div>
        <div class="control-row">
          <span class="control-label">d1 (10s):</span>
          <input type="range" class="control-slider" min="0" max="9" value="${d1}" id="sliderD1">
          <span class="control-val" id="valD1">${d1}</span>
        </div>
        <div class="control-row">
          <span class="control-label">d0 (1s):</span>
          <input type="range" class="control-slider" min="0" max="9" value="${d0}" id="sliderD0">
          <span class="control-val" id="valD0">${d0}</span>
        </div>
      `;

      document.getElementById('sliderD3').oninput = (e) => {
        d3 = parseInt(e.target.value);
        document.getElementById('valD3').textContent = d3;
        update();
      };
      document.getElementById('sliderD2').oninput = (e) => {
        d2 = parseInt(e.target.value);
        document.getElementById('valD2').textContent = d2;
        update();
      };
      document.getElementById('sliderD1').oninput = (e) => {
        d1 = parseInt(e.target.value);
        document.getElementById('valD1').textContent = d1;
        update();
      };
      document.getElementById('sliderD0').oninput = (e) => {
        d0 = parseInt(e.target.value);
        document.getElementById('valD0').textContent = d0;
        update();
      };

      update();
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

    out_path = "public/animations/class8-math-algebra-play.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Successfully generated {out_path} ({len(final_html)} bytes).")

if __name__ == "__main__":
    build_html()

