import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_baudhayana_pythagoras_data import slides_data, quiz_questions

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 9: The Baudhāyana-Pythagoras Theorem Master Lab</title>
  
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
      gap: 14px;
    }

    .header-badge {
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      padding: 4px 10px;
      border-radius: 20px;
      text-transform: uppercase;
    }

    .header-title {
      font-size: 15px;
      font-weight: 700;
      color: #f1f5f9;
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .slide-indicator {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      background: rgba(30, 41, 59, 0.6);
      padding: 4px 12px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .speech-btn {
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid var(--accent-indigo);
      color: #c7d2fe;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12.5px;
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
    .speech-btn.active {
      background: #10b981;
      border-color: #10b981;
      color: #fff;
    }

    /* Main Container */
    main {
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Slide Header Card */
    .slide-header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .slide-tag {
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .slide-title {
      font-size: 24px;
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.5px;
    }

    .slide-subtitle {
      font-size: 14px;
      color: var(--text-muted);
    }

    /* Mentor Voice Avatar Bar */
    .mentor-bar {
      background: rgba(30, 41, 59, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .mentor-avatar {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #1e293b;
      border: 2px solid var(--accent-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      position: relative;
    }

    .mentor-avatar svg {
      width: 28px;
      height: 28px;
    }

    .avatar-mouth {
      transform-origin: 50px 65px;
    }
    .speaking .avatar-mouth {
      animation: mouthTalk 0.25s infinite alternate ease-in-out;
    }
    @keyframes mouthTalk {
      0% { transform: scaleY(1); }
      100% { transform: scaleY(2.2); }
    }

    .mentor-name {
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .mentor-text {
      font-size: 13.5px;
      color: #e2e8f0;
      font-style: italic;
    }

    /* Lesson Slide Layout: 2 Columns */
    .lesson-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 24px;
      align-items: start;
    }

    @media (max-width: 960px) {
      .lesson-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Left Column: Theory & In-Slide Checkpoints */
    .theory-panel {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .theory-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      line-height: 1.65;
      font-size: 14.5px;
      color: #cbd5e1;
    }

    .theory-card h4 {
      color: #fff;
      font-size: 16px;
      margin-top: 14px;
      margin-bottom: 8px;
    }

    .theory-card p {
      margin-bottom: 12px;
    }

    .theory-card ul, .theory-card ol {
      margin-left: 20px;
      margin-bottom: 12px;
    }

    .theory-card li {
      margin-bottom: 6px;
    }

    /* Checkpoints Box */
    .checkpoints-container {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 16px;
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .checkpoint-header {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--accent-amber);
      font-weight: 700;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .checkpoint-card {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 16px;
    }

    .checkpoint-q {
      font-size: 13.5px;
      font-weight: 600;
      color: #f1f5f9;
      margin-bottom: 12px;
      line-height: 1.45;
    }

    .options-grid {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .option-btn {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 13px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }

    .option-btn:hover:not(:disabled) {
      background: rgba(99, 102, 241, 0.15);
      border-color: var(--accent-indigo);
      color: #fff;
    }

    .option-btn.correct {
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--accent-emerald) !important;
      color: #a7f3d0 !important;
      font-weight: 600;
    }

    .option-btn.incorrect {
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: var(--accent-rose) !important;
      color: #fecdd3 !important;
    }

    .feedback-box {
      margin-top: 10px;
      font-size: 12.5px;
      padding: 10px 14px;
      border-radius: 8px;
      line-height: 1.4;
      display: none;
    }
    .feedback-box.show {
      display: block;
    }
    .feedback-box.correct-box {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--accent-emerald);
      color: #6ee7b7;
    }
    .feedback-box.incorrect-box {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid var(--accent-rose);
      color: #fda4af;
    }

    /* Right Column: Simulator & Controls */
    .sim-panel {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: sticky;
      top: 80px;
    }

    .sim-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 12px;
    }

    .sim-head h3 {
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sim-badge {
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(99, 102, 241, 0.2);
      color: #a5b4fc;
      font-weight: 600;
    }

    .sim-viewport {
      background: #090e1a;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      min-height: 330px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px;
      position: relative;
      overflow: hidden;
    }

    .sim-controls {
      display: flex;
      flex-direction: column;
      gap: 12px;
      background: rgba(30, 41, 59, 0.5);
      border-radius: 12px;
      padding: 14px;
    }

    .sim-btn {
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .sim-btn:hover {
      opacity: 0.9;
      transform: translateY(-1px);
    }
    .sim-btn.active {
      background: linear-gradient(135deg, #10b981, #06b6d4);
    }

    .sim-slider-group {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12.5px;
      color: #cbd5e1;
    }
    .sim-slider-group span:first-child {
      min-width: 90px;
    }
    .sim-slider-group input[type="range"] {
      flex: 1;
      accent-color: var(--accent-cyan);
      cursor: pointer;
    }

    /* Quiz Slides: 4 Dedicated Slides (10 questions each) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 20px;
    }

    .quiz-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    .quiz-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
    }

    .quiz-card-head {
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
      <span class="header-badge">CLASS 8 • MATHEMATICS • CHAPTER 9</span>
      <span class="header-title">The Baudhāyana-Pythagoras Theorem Master Lab</span>
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
    <!-- Slide Header Card -->
    <section class="slide-header">
      <div class="slide-tag" id="slideTag">CHAPTER 9 • SLIDE 1 OF 20</div>
      <h1 class="slide-title" id="slideTitle">The Baudhāyana-Pythagoras Theorem</h1>
      <p class="slide-subtitle" id="slideSubtitle">Universal Law of Right-Angled Triangles</p>
    </section>

    <!-- Mentor Bar with Synchronized Talking Avatar -->
    <section class="mentor-bar" id="mentorContainer">
      <div class="mentor-avatar" id="mentorAvatar">
        <svg viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="44" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
          <circle cx="35" cy="42" r="5" fill="#38bdf8"/>
          <circle cx="65" cy="42" r="5" fill="#38bdf8"/>
          <path class="avatar-mouth" d="M 38 66 Q 50 74 62 66" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        </svg>
      </div>
      <div>
        <div class="mentor-name">Mathematics Mentor</div>
        <div class="mentor-text" id="mentorVoiceText">
          Welcome to our laboratory on the Baudhāyana-Pythagoras Theorem!
        </div>
      </div>
    </section>

    <!-- Lesson Slide Layout: 2 Columns (Used for Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      <!-- Left Column: Rich Theory & In-Slide Checkpoints -->
      <div class="theory-panel">
        <div class="theory-card" id="theoryContent">
          <!-- Populated dynamically -->
        </div>

        <!-- In-Slide Conceptual Checkpoints (2 per lesson slide) -->
        <div class="checkpoints-container" id="checkpointContainer">
          <div class="checkpoint-header">
            <span>⚡</span> Conceptual Checkpoints (Test Your Understanding)
          </div>
          <div id="checkpointsList" style="display:flex; flex-direction:column; gap:14px;">
            <!-- Populated dynamically -->
          </div>
        </div>
      </div>

      <!-- Right Column: Interactive Simulator Panel -->
      <section class="sim-panel" id="simulatorPanel">
        <div class="sim-head">
          <h3 id="simTitle">
            <span>🔬</span> Interactive Lab Simulator
          </h3>
          <span class="sim-badge" id="simBadge">Live Explorer</span>
        </div>
        <div class="sim-viewport" id="simViewport">
          <!-- Canvas / SVG Visuals Populated Dynamically -->
        </div>
        <div class="sim-controls" id="simControls">
          <!-- Sliders and Buttons Populated Dynamically -->
        </div>
      </section>
    </div>

    <!-- Quiz Challenge Slides Container (Slides 17 to 20: 10 questions each) -->
    <div class="quiz-container" id="quizContainer">
      <!-- 10 Questions for the current quiz slide -->
      <div class="quiz-grid" id="quizGrid"></div>
    </div>
  </main>

  <!-- Sticky Navigation Footer -->
  <footer>
    <button class="nav-btn" id="prevBtn" onclick="prevSlide()" disabled>
      ← Previous Slide
    </button>
    <div id="lastSlideNotice" class="last-slide-notice">
      You have reached the last slide of this chapter
    </div>
    <button class="nav-btn" id="nextBtn" onclick="nextSlide()">
      Next Slide →
    </button>
  </footer>

  <!-- Universal Pop-up Solution Modal -->
  <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop" style="position:fixed; top:0; left:0; width:100vw; height:100vh; display:none; align-items:center; justify-content:center; z-index:1000;">
    <div style="background:#0f172a; border:1px solid #6366f1; border-radius:16px; max-width:620px; width:95%; padding:24px; position:relative; box-shadow:0 20px 35px -5px rgba(0,0,0,0.8);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:10px;">
        <h3 id="modalTitle" style="color:#fcd34d; font-size:16px; font-weight:700; display:flex; align-items:center; gap:8px;">
          <span>💡</span> Detailed Mathematical Solution
        </h3>
        <button onclick="closeSolutionModal()" style="background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px;">✕</button>
      </div>
      <div id="modalBody" style="font-size:14px; line-height:1.65; color:#e2e8f0; max-height:60vh; overflow-y:auto; padding-right:8px;">
        <!-- Solution math and explanation -->
      </div>
      <div style="margin-top:16px; text-align:right;">
        <button onclick="closeSolutionModal()" style="background:#4f46e5; color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">Close Solution</button>
      </div>
    </div>
  </div>

  <script>
    // Injected Data
    const slides = __SLIDES_JSON__;
    const quizQuestions = __QUIZ_JSON__;

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let currentUtterance = null;

    // Helper: Trigger KaTeX Rendering
    function triggerMathRender(element) {
      if (window.renderMathInElement) {
        renderMathInElement(element || document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ],
          throwOnError: false
        });
      }
    }

    // ==========================================
    // Slide Navigation & State Management
    // ==========================================
    function loadSlide(index) {
      if (index < 0 || index >= slides.length) return;
      currentSlideIndex = index;
      stopVoice();

      const slide = slides[index];

      // Update Header & Metas
      document.getElementById('slideNumDisplay').textContent = `Slide ${index + 1} of ${slides.length}`;
      document.getElementById('slideTag').textContent = `CHAPTER 9 • SLIDE ${index + 1} OF 20`;
      document.getElementById('slideTitle').textContent = slide.title;
      document.getElementById('slideSubtitle').textContent = slide.subtitle;
      document.getElementById('mentorVoiceText').textContent = slide.voice;

      const lessonGrid = document.getElementById('lessonGrid');
      const quizContainer = document.getElementById('quizContainer');
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const lastNotice = document.getElementById('lastSlideNotice');

      prevBtn.disabled = (index === 0);

      if (index === slides.length - 1) {
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

        document.getElementById('theoryContent').innerHTML = slide.content;
        renderCheckpoints(slide.checkpoints);
        renderSimulator(slide.sim_type);
      } else {
        // Dedicated Quiz Slide (Slides 17 to 20)
        lessonGrid.style.display = 'none';
        quizContainer.style.display = 'flex';

        renderQuizSlide(slide.quiz_range);
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
      if (currentSlideIndex < slides.length - 1) {
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
          <div class="checkpoint-q"><strong>Q${cpIdx + 1}:</strong> ${cp.q}</div>
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

            if (optIdx === cp.ans) {
              btn.classList.add('correct');
              feedback.className = 'feedback-box show correct-box';
              feedback.innerHTML = `<strong>✓ Correct!</strong> ${cp.feedback}`;
            } else {
              btn.classList.add('incorrect');
              allBtns[cp.ans].classList.add('correct');
              feedback.className = 'feedback-box show incorrect-box';
              feedback.innerHTML = `<strong>✗ Incorrect.</strong> ${cp.feedback}`;
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
    function renderQuizSlide(range) {
      const grid = document.getElementById('quizGrid');
      grid.innerHTML = '';

      if (!range) return;
      const [startNum, endNum] = range;
      const questions = quizQuestions.filter(q => q.num >= startNum && q.num <= endNum);

      questions.forEach((q) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';
        card.innerHTML = `
          <div class="quiz-card-head">
            <span class="q-num-badge">Question ${q.num} of 40</span>
            <button class="sol-btn" onclick="openSolutionModal(${q.num})">
              <span>💡</span> View Solution
            </button>
          </div>
          <div class="checkpoint-q">${q.question}</div>
          <div class="options-grid" id="qGrid${q.num}"></div>
          <div class="feedback-box" id="qFeedback${q.num}"></div>
        `;

        const optGrid = card.querySelector(`#qGrid${q.num}`);
        const feedback = card.querySelector(`#qFeedback${q.num}`);

        q.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'option-btn';
          btn.innerHTML = `<span style="font-weight:700; color:#38bdf8;">${String.fromCharCode(65 + optIdx)}.</span> <span>${optText}</span>`;
          btn.onclick = () => {
            const allBtns = optGrid.querySelectorAll('.option-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === q.correct) {
              btn.classList.add('correct');
              feedback.className = 'feedback-box show correct-box';
              feedback.innerHTML = `<strong>✓ Excellent!</strong> Correct Answer. Click "View Solution" to inspect the complete proof.`;
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
              feedback.className = 'feedback-box show incorrect-box';
              feedback.innerHTML = `<strong>✗ Not quite.</strong> Option (${String.fromCharCode(65 + q.correct)}) is correct. Click "View Solution" for detailed reasoning.`;
            }
          };
          optGrid.appendChild(btn);
        });

        grid.appendChild(card);
      });
    }

    // ==========================================
    // Solution Modal
    // ==========================================
    function openSolutionModal(qNum) {
      const q = quizQuestions.find(item => item.num === qNum);
      if (!q) return;

      const modal = document.getElementById('solutionModal');
      document.getElementById('modalTitle').innerHTML = `<span>💡</span> Solution: Question ${q.num} of 40`;
      document.getElementById('modalBody').innerHTML = `
        <div style="margin-bottom:12px; font-weight:600; color:#94a3b8;">${q.question}</div>
        <div style="background:rgba(30,41,59,0.7); border:1px solid #334155; border-radius:10px; padding:16px;">
          ${q.solution}
        </div>
      `;
      modal.style.display = 'flex';
      setTimeout(() => {
        triggerMathRender(document.getElementById('modalBody'));
      }, 50);
    }

    function closeSolutionModal() {
      document.getElementById('solutionModal').style.display = 'none';
    }

    // ==========================================
    // Voice Narration (Web Speech API)
    // ==========================================
    function toggleVoice() {
      if (isSpeaking) {
        stopVoice();
      } else {
        startVoice();
      }
    }

    function startVoice() {
      if (!('speechSynthesis' in window)) {
        alert("Your browser does not support text-to-speech audio narration.");
        return;
      }
      stopVoice();

      const text = document.getElementById('mentorVoiceText').textContent.trim();
      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.rate = 0.95;
      currentUtterance.pitch = 1.0;

      const voices = synth.getVoices();
      const engVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('India') || v.name.includes('Male')));
      if (engVoice) currentUtterance.voice = engVoice;

      currentUtterance.onstart = () => {
        isSpeaking = true;
        document.getElementById('mentorAvatar').classList.add('speaking');
        document.getElementById('voiceToggleBtn').classList.add('active');
        document.getElementById('voiceStatusText').textContent = 'Pause';
      };

      currentUtterance.onend = currentUtterance.onerror = () => {
        stopVoice();
      };

      synth.speak(currentUtterance);
    }

    function stopVoice() {
      if (synth && synth.speaking) {
        synth.cancel();
      }
      isSpeaking = false;
      const avatar = document.getElementById('mentorAvatar');
      if (avatar) avatar.classList.remove('speaking');
      const btn = document.getElementById('voiceToggleBtn');
      if (btn) {
        btn.classList.remove('active');
        document.getElementById('voiceStatusText').textContent = 'Listen';
      }
    }

    // =========================================================
    // 16 Bespoke Interactive Mathematical Simulators (Slides 1-16)
    // =========================================================
    function renderSimulator(type) {
      const vp = document.getElementById('simViewport');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const badge = document.getElementById('simBadge');

      vp.innerHTML = '';
      controls.innerHTML = '';

      switch (type) {
        case 'baudhayana_pythagoras_theater':
          renderSim1(vp, controls, title, badge);
          break;
        case 'square_doubler_diagonal_grid':
          renderSim2(vp, controls, title, badge);
          break;
        case 'square_halver_origami_lab':
          renderSim3(vp, controls, title, badge);
          break;
        case 'isosceles_right_hypotenuse_explorer':
          renderSim4(vp, controls, title, badge);
          break;
        case 'root2_baudhayana_approximation_dial':
          renderSim5(vp, controls, title, badge);
          break;
        case 'general_dissection_proof_animator':
          renderSim6(vp, controls, title, badge);
          break;
        case 'two_squares_area_combiner':
          renderSim7(vp, controls, title, badge);
          break;
        case 'paper_folding_pythagoras_jigsaw':
          renderSim8(vp, controls, title, badge);
          break;
        case 'baudhayana_altitude_ladder_workbench':
          renderSim9(vp, controls, title, badge);
          break;
        case 'pythagorean_triples_generator':
          renderSim10(vp, controls, title, badge);
          break;
        case 'euler_brick_open_problem_explorer':
          renderSim11(vp, controls, title, badge);
          break;
        case 'three_d_space_diagonal_scanner':
          renderSim12(vp, controls, title, badge);
          break;
        case 'converse_triangle_classifier':
          renderSim13(vp, controls, title, badge);
          break;
        case 'sulbasutra_rope_altar_builder':
          renderSim14(vp, controls, title, badge);
          break;
        case 'baudhayana_master_formula_matrix':
          renderSim15(vp, controls, title, badge);
          break;
        case 'find_the_colours_puzzle_room':
          renderSim16(vp, controls, title, badge);
          break;
      }
      triggerMathRender(vp);
    }

    // -------------------------------------------------------------
    // Simulator 1: Baudhāyana-Pythagoras Theater
    // -------------------------------------------------------------
    function renderSim1(vp, controls, title, badge) {
      title.innerHTML = '<span>📐</span> Baudhāyana-Pythagoras Theater';
      badge.textContent = '3 Squares on Triangle Sides';

      let a = 3;
      let b = 4;

      function update() {
        const c = Math.sqrt(a * a + b * b);
        const a2 = a * a;
        const b2 = b * b;
        const c2 = a2 + b2;

        const scale = 14;
        const ox = 150;
        const oy = 210;

        const pA = { x: ox, y: oy };
        const pB = { x: ox + b * scale, y: oy };
        const pC = { x: ox, y: oy - a * scale };

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 380 270" style="max-width:360px; width:100%;">
              <!-- Square on leg a (vertical, left) -->
              <rect x="${ox - a * scale}" y="${pC.y}" width="${a * scale}" height="${a * scale}" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="2"/>
              <text x="${ox - (a * scale) / 2}" y="${pC.y + (a * scale) / 2 + 4}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">a² = ${a2}</text>

              <!-- Square on leg b (horizontal, bottom) -->
              <rect x="${ox}" y="${oy}" width="${b * scale}" height="${b * scale}" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
              <text x="${ox + (b * scale) / 2}" y="${oy + (b * scale) / 2 + 4}" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">b² = ${b2}</text>

              <!-- Right Triangle ABC -->
              <polygon points="${pA.x},${pA.y} ${pB.x},${pB.y} ${pC.x},${pC.y}" fill="#312e81" stroke="#818cf8" stroke-width="2.5"/>
              
              <!-- Right angle symbol -->
              <rect x="${ox}" y="${oy - 12}" width="12" height="12" fill="none" stroke="#fcd34d" stroke-width="1.5"/>

              <!-- Labels on Triangle Sides -->
              <text x="${ox - 6}" y="${oy - (a * scale) / 2}" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="end">a = ${a}</text>
              <text x="${ox + (b * scale) / 2}" y="${oy - 4}" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">b = ${b}</text>
              <text x="${ox + (b * scale) / 2 + 10}" y="${oy - (a * scale) / 2 - 6}" fill="#fcd34d" font-size="12" font-weight="bold">c = ${c.toFixed(2)}</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:13px; line-height:1.5;">
              <span style="color:#38bdf8;">$a^2 (${a2})$</span> + 
              <span style="color:#34d399;">$b^2 (${b2})$</span> = 
              <strong style="color:#fcd34d;">$c^2 (${c2})$</strong> 
              $\\implies c = \\mathbf{${c.toFixed(2)}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Leg a (${a}):</span>
            <input type="range" id="aLeg" min="2" max="8" value="${a}">
          </div>
          <div class="sim-slider-group">
            <span>Leg b (${b}):</span>
            <input type="range" id="bLeg" min="2" max="8" value="${b}">
          </div>
        `;

        document.getElementById('aLeg').oninput = (e) => {
          a = parseInt(e.target.value);
          update();
        };
        document.getElementById('bLeg').oninput = (e) => {
          b = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 2: Square Doubler (Diagonal Grid)
    // -------------------------------------------------------------
    function renderSim2(vp, controls, title, badge) {
      title.innerHTML = '<span>⚡</span> Doubling a Square';
      badge.textContent = 'Diagonal Area Expansion';

      let side = 4;

      function update() {
        const a1 = side * side;
        const diag = (side * Math.SQRT2).toFixed(2);
        const a2 = a1 * 2;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 300 220" style="max-width:280px; width:100%;">
              <!-- Tilted Doubled Square -->
              <polygon points="150,20 250,110 150,200 50,110" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2.5"/>
              
              <!-- Original Square -->
              <rect x="100" y="65" width="100" height="90" fill="rgba(99, 102, 241, 0.35)" stroke="#6366f1" stroke-width="2"/>
              
              <!-- Diagonal Line connecting corners -->
              <line x1="100" y1="155" x2="200" y2="65" stroke="#fcd34d" stroke-width="2" stroke-dasharray="4"/>

              <!-- Labels -->
              <text x="150" y="115" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Base: ${a1} sq units</text>
              <text x="150" y="42" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Doubled Square = ${a2} sq units</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Original: Side = <strong>${side}</strong>, Area = $${side}^2 = \\mathbf{${a1}}$
              <br>Diagonal $d = ${side}\\sqrt{2} \\approx \\mathbf{${diag}}$
              <br>Area of Square on Diagonal: $d^2 = 2 \\times ${a1} = \\mathbf{${a2}\\text{ sq units}}$ (Exactly 2×!)
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Base Side ($s$):</span>
            <input type="range" id="sRange" min="2" max="10" value="${side}">
            <span style="font-weight:bold; color:#38bdf8;">${side}</span>
          </div>
        `;

        document.getElementById('sRange').oninput = (e) => {
          side = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 3: Square Halver (Midpoint Origami Lab)
    // -------------------------------------------------------------
    function renderSim3(vp, controls, title, badge) {
      title.innerHTML = '<span>✂️</span> Halving a Square';
      badge.textContent = 'Midpoint Inscribed Square';

      let size = 8;
      let foldProgress = 0; // 0 to 1

      function update() {
        const areaOrig = size * size;
        const areaHalf = areaOrig / 2;
        const innerSide = (size / Math.SQRT2).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 260 220" style="max-width:250px; width:100%;">
              <!-- Outer Square -->
              <rect x="30" y="20" width="200" height="180" fill="#1e293b" stroke="#64748b" stroke-width="2"/>

              <!-- 4 Folded Corner Triangles -->
              <polygon points="30,20 130,20 30,110" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="1.5"/>
              <polygon points="130,20 230,20 230,110" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="1.5"/>
              <polygon points="230,110 230,200 130,200" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="1.5"/>
              <polygon points="130,200 30,200 30,110" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="1.5"/>

              <!-- Inner Inscribed Square connecting Midpoints -->
              <polygon points="130,20 230,110 130,200 30,110" fill="rgba(16, 185, 129, 0.35)" stroke="#10b981" stroke-width="2.5"/>

              <!-- Midpoint Dots -->
              <circle cx="130" cy="20" r="4" fill="#fcd34d"/>
              <circle cx="230" cy="110" r="4" fill="#fcd34d"/>
              <circle cx="130" cy="200" r="4" fill="#fcd34d"/>
              <circle cx="30" cy="110" r="4" fill="#fcd34d"/>

              <text x="130" y="115" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Inscribed = ${areaHalf}</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Outer Square: $s = ${size} \\implies \\text{Area} = \\mathbf{${areaOrig}}$
              <br>Each corner triangle area $= \\frac{1}{2}(${size/2})(${size/2}) = ${(areaOrig/8).toFixed(1)}$
              <br>Inscribed Square: Area $= ${areaOrig} - 4(${(areaOrig/8).toFixed(1)}) = \\mathbf{${areaHalf}}$ (Half Area!)
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Outer Square Side:</span>
            <input type="range" id="sizeRange" min="4" max="16" step="2" value="${size}">
            <span style="font-weight:bold; color:#38bdf8;">${size}</span>
          </div>
        `;

        document.getElementById('sizeRange').oninput = (e) => {
          size = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 4: Isosceles Right Hypotenuse Explorer
    // -------------------------------------------------------------
    function renderSim4(vp, controls, title, badge) {
      title.innerHTML = '<span>📐</span> Isosceles Right Triangle (45°-45°-90°)';
      badge.textContent = 'Universal √2 Ratio';

      let s = 5;

      function update() {
        const hypExact = `${s}\\sqrt{2}`;
        const hypDec = (s * Math.SQRT2).toFixed(3);
        const area = (0.5 * s * s).toFixed(1);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 280 200" style="max-width:260px; width:100%;">
              <polygon points="50,170 210,170 50,30" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="2.5"/>
              <rect x="50" y="152" width="18" height="18" fill="none" stroke="#fcd34d" stroke-width="1.5"/>

              <!-- Labels -->
              <text x="35" y="105" fill="#38bdf8" font-size="12" font-weight="bold">s = ${s}</text>
              <text x="130" y="188" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">s = ${s}</text>
              <text x="145" y="90" fill="#fcd34d" font-size="12" font-weight="bold">c = ${s}√2</text>
              <text x="80" y="160" fill="#94a3b8" font-size="10">45°</text>
              <text x="58" y="65" fill="#94a3b8" font-size="10">45°</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #6366f1; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Legs: $a = b = ${s}$ | Area: $\\frac{1}{2}(${s})(${s}) = \\mathbf{${area}}$
              <br>Hypotenuse: $c = \\sqrt{${s}^2 + ${s}^2} = \\sqrt{${2*s*s}} = \\mathbf{${hypExact}} \\approx \\mathbf{${hypDec}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Leg Length ($s$):</span>
            <input type="range" id="legRange" min="1" max="15" value="${s}">
            <span style="font-weight:bold; color:#38bdf8;">${s}</span>
          </div>
        `;

        document.getElementById('legRange').oninput = (e) => {
          s = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 5: Root 2 Baudhāyana Approximation Dial
    // -------------------------------------------------------------
    function renderSim5(vp, controls, title, badge) {
      title.innerHTML = "<span>📜</span> Baudhāyana's √2 Formula Dial";
      badge.textContent = 'Ancient Śulbasūtra Precision';

      let step = 4;

      function update() {
        let val = 1;
        let terms = '1';

        if (step >= 2) {
          val += 1/3;
          terms += ' + 1/3';
        }
        if (step >= 3) {
          val += 1/12;
          terms += ' + 1/12';
        }
        if (step >= 4) {
          val -= 1/408;
          terms += ' - 1/408';
        }

        const trueRoot2 = Math.SQRT2;
        const diff = Math.abs(val - trueRoot2).toFixed(7);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:16px; font-weight:bold; color:#fcd34d; margin-bottom:6px;">
              Baudhāyana Śulbasūtra Formula
            </div>
            <div style="background:#1e293b; border:1px solid #475569; border-radius:8px; padding:8px 12px; margin-bottom:12px; font-size:13px; color:#38bdf8;">
              $$\\sqrt{2} \\approx 1 + \\frac{1}{3} + \\frac{1}{3 \\times 4} - \\frac{1}{3 \\times 4 \\times 34} = \\mathbf{\\frac{577}{408}}$$
            </div>

            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div style="background:#0f172a; border:1px solid #10b981; border-radius:8px; padding:10px 14px;">
                <div style="font-size:11px; color:#10b981;">Baudhāyana (577/408)</div>
                <div style="font-size:18px; font-weight:bold; color:#fff;">${val.toFixed(7)}</div>
              </div>
              <div style="background:#0f172a; border:1px solid #38bdf8; border-radius:8px; padding:10px 14px;">
                <div style="font-size:11px; color:#38bdf8;">True Value of √2</div>
                <div style="font-size:18px; font-weight:bold; color:#fff;">${trueRoot2.toFixed(7)}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px; font-size:12px; color:#cbd5e1;">
              Difference: <strong style="color:#fcd34d;">${diff}</strong> | Accuracy: <strong style="color:#34d399;">99.99985%</strong> (2800 years ago!)
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Add Terms Step-by-Step:</div>
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn ${step===1?'active':''}" onclick="setStep(1)">Term 1 (1)</button>
            <button class="sim-btn ${step===2?'active':''}" onclick="setStep(2)">+ 1/3</button>
            <button class="sim-btn ${step===3?'active':''}" onclick="setStep(3)">+ 1/12</button>
            <button class="sim-btn ${step===4?'active':''}" onclick="setStep(4)">- 1/408 (Full)</button>
          </div>
        `;

        window.setStep = (st) => {
          step = st;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 6: General Dissection Proof Animator
    // -------------------------------------------------------------
    function renderSim6(vp, controls, title, badge) {
      title.innerHTML = '<span>🧩</span> General Dissection Proof';
      badge.textContent = '4 Triangles Rearrangement';

      let a = 3;
      let b = 4;

      function update() {
        const c = Math.sqrt(a * a + b * b);
        const totalSide = a + b;
        const outerArea = totalSide * totalSide;
        const triArea = 0.5 * a * b;
        const fourTris = 4 * triArea;
        const c2 = a * a + b * b;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 240 220" style="max-width:220px; width:100%;">
              <!-- Outer Square (a+b) x (a+b) -->
              <rect x="20" y="20" width="200" height="180" fill="#0f172a" stroke="#6366f1" stroke-width="2"/>

              <!-- 4 Congruent Right Triangles around perimeter -->
              <!-- Top-Left Triangle -->
              <polygon points="20,20 140,20 20,80" fill="rgba(6,182,212,0.3)" stroke="#06b6d4" stroke-width="1.5"/>
              <!-- Top-Right Triangle -->
              <polygon points="220,20 220,140 160,20" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="1.5"/>
              <!-- Bottom-Right Triangle -->
              <polygon points="220,200 100,200 220,140" fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="1.5"/>
              <!-- Bottom-Left Triangle -->
              <polygon points="20,200 20,80 80,200" fill="rgba(244,63,94,0.3)" stroke="#f43f5e" stroke-width="1.5"/>

              <!-- Central Tilted Square c^2 -->
              <polygon points="140,20 220,140 100,200 20,80" fill="rgba(99,102,241,0.4)" stroke="#818cf8" stroke-width="2"/>
              <text x="120" y="115" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">c² = ${c2}</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Outer Square: $(a+b)^2 = (${a}+${b})^2 = \\mathbf{${outerArea}}$
              <br>4 Triangles: $4 \\times \\frac{1}{2}(${a})(${b}) = \\mathbf{${fourTris}}$
              <br>Inner Square: $c^2 = ${outerArea} - ${fourTris} = \\mathbf{${c2}} = ${a}^2 + ${b}^2$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Leg a:</span>
            <input type="range" id="daRange" min="2" max="6" value="${a}">
            <span style="font-weight:bold; color:#38bdf8;">${a}</span>
          </div>
          <div class="sim-slider-group">
            <span>Leg b:</span>
            <input type="range" id="dbRange" min="2" max="6" value="${b}">
            <span style="font-weight:bold; color:#38bdf8;">${b}</span>
          </div>
        `;

        document.getElementById('daRange').oninput = (e) => {
          a = parseInt(e.target.value);
          update();
        };
        document.getElementById('dbRange').oninput = (e) => {
          b = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 7: Combining Two Different Squares
    // -------------------------------------------------------------
    function renderSim7(vp, controls, title, badge) {
      title.innerHTML = '<span>➕</span> Combining Two Different Squares';
      badge.textContent = 'Area Addition: a² + b² = c²';

      let a = 3;
      let b = 4;

      function update() {
        const a2 = a * a;
        const b2 = b * b;
        const c2 = a2 + b2;
        const c = Math.sqrt(c2).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:center; align-items:center; gap:12px; margin-bottom:12px;">
              <div style="background:#06b6d4; width:${a*12}px; height:${a*12}px; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#0f172a;">
                ${a2}
              </div>
              <span style="font-size:20px; font-weight:bold; color:#cbd5e1;">+</span>
              <div style="background:#10b981; width:${b*12}px; height:${b*12}px; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#0f172a;">
                ${b2}
              </div>
              <span style="font-size:20px; font-weight:bold; color:#cbd5e1;">=</span>
              <div style="background:#f59e0b; width:${Math.sqrt(c2)*12}px; height:${Math.sqrt(c2)*12}px; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:bold; color:#0f172a;">
                ${c2}
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Square 1 ($a = ${a}$): Area = <strong>${a2}</strong>
              <br>Square 2 ($b = ${b}$): Area = <strong>${b2}</strong>
              <br>Combined Single Square: Side $c = \\sqrt{${a2} + ${b2}} = \\mathbf{${c}}$, Area = $\\mathbf{${c2}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Square 1 Side ($a$):</span>
            <input type="range" id="c1Range" min="2" max="6" value="${a}">
            <span style="font-weight:bold; color:#38bdf8;">${a}</span>
          </div>
          <div class="sim-slider-group">
            <span>Square 2 Side ($b$):</span>
            <input type="range" id="c2Range" min="2" max="6" value="${b}">
            <span style="font-weight:bold; color:#10b981;">${b}</span>
          </div>
        `;

        document.getElementById('c1Range').oninput = (e) => {
          a = parseInt(e.target.value);
          update();
        };
        document.getElementById('c2Range').oninput = (e) => {
          b = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 8: Paper Folding & Jigsaw Cutting
    // -------------------------------------------------------------
    function renderSim8(vp, controls, title, badge) {
      title.innerHTML = '<span>📄</span> Combining Two Squares Using Paper';
      badge.textContent = 'Origami Jigsaw Transformation';

      let state = 'cut'; // placed, cut, assembled

      function update() {
        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 280 180" style="max-width:260px; width:100%;">
              ${state === 'assembled' ? `
                <!-- Assembled single big square -->
                <polygon points="140,20 230,90 160,170 70,100" fill="rgba(16, 185, 129, 0.4)" stroke="#10b981" stroke-width="2.5"/>
                <text x="150" y="100" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">Assembled c²</text>
              ` : `
                <!-- Two adjacent paper squares with cut lines -->
                <rect x="50" y="80" width="70" height="70" fill="rgba(6, 182, 212, 0.3)" stroke="#06b6d4" stroke-width="2"/>
                <rect x="120" y="50" width="100" height="100" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
                <text x="85" y="120" fill="#38bdf8" font-size="12" font-weight="bold">a²</text>
                <text x="170" y="105" fill="#fcd34d" font-size="12" font-weight="bold">b²</text>
                ${state === 'cut' ? `
                  <line x1="50" y1="80" x2="190" y2="50" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4"/>
                  <line x1="120" y1="150" x2="220" y2="50" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4"/>
                ` : ''}
              `}
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              ${state === 'assembled' 
                ? '<strong>Step 3:</strong> The cut pieces fit perfectly into a <strong>single square of side $c$</strong> without gap or overlap!'
                : '<strong>Step 1 & 2:</strong> Place two paper squares side-by-side. Cut along lines of length $c = \\sqrt{a^2+b^2}$.'
              }
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn ${state==='cut'?'active':''}" onclick="setJigsawState('cut')">Show Cut Lines</button>
            <button class="sim-btn ${state==='assembled'?'active':''}" onclick="setJigsawState('assembled')">Reassemble to c²</button>
          </div>
        `;

        window.setJigsawState = (st) => {
          state = st;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 9: Baudhāyana Altitude & Ladder Workbench
    // -------------------------------------------------------------
    function renderSim9(vp, controls, title, badge) {
      title.innerHTML = '<span>🪜</span> Leaning Ladder & Tree Heights';
      badge.textContent = 'Real-World Distance Workbench';

      let ladder = 13;
      let dist = 5;

      function update() {
        const height = Math.sqrt(ladder * ladder - dist * dist).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 280 200" style="max-width:260px; width:100%;">
              <!-- Wall -->
              <line x1="60" y1="20" x2="60" y2="180" stroke="#64748b" stroke-width="4"/>
              <text x="45" y="100" fill="#94a3b8" font-size="11" transform="rotate(-90 45,100)">Vertical Wall</text>

              <!-- Ground -->
              <line x1="40" y1="180" x2="240" y2="180" stroke="#334155" stroke-width="3"/>
              
              <!-- Ladder -->
              <line x1="60" y1="${180 - height * 11}" x2="${60 + dist * 14}" y2="180" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>

              <!-- Measurements -->
              <text x="${60 + (dist * 14)/2}" y="195" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">d = ${dist} m</text>
              <text x="${60 + (dist * 14)/2 + 10}" y="${180 - (height * 11)/2}" fill="#fcd34d" font-size="11" font-weight="bold">L = ${ladder} m</text>
              <text x="75" y="${180 - (height * 11)/2}" fill="#34d399" font-size="11" font-weight="bold">h = ${height} m</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Ladder Length ($L$): <strong>${ladder} m</strong> | Base Distance ($d$): <strong>${dist} m</strong>
              <br>Height reached on wall: $h = \\sqrt{${ladder}^2 - ${dist}^2} = \\sqrt{${ladder*ladder - dist*dist}} = \\mathbf{${height}\\text{ m}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Ladder Length:</span>
            <input type="range" id="lRange" min="10" max="25" value="${ladder}">
            <span style="font-weight:bold; color:#f59e0b;">${ladder} m</span>
          </div>
          <div class="sim-slider-group">
            <span>Base Distance:</span>
            <input type="range" id="dRange" min="3" max="${ladder-2}" value="${dist}">
            <span style="font-weight:bold; color:#38bdf8;">${dist} m</span>
          </div>
        `;

        document.getElementById('lRange').oninput = (e) => {
          ladder = parseInt(e.target.value);
          if (dist >= ladder) dist = ladder - 2;
          update();
        };
        document.getElementById('dRange').oninput = (e) => {
          dist = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 10: Pythagorean Triples Generator
    // -------------------------------------------------------------
    function renderSim10(vp, controls, title, badge) {
      title.innerHTML = '<span>🔢</span> Pythagorean Triples Generator';
      badge.textContent = 'Parametric Identity Engine';

      let m = 3;
      let n = 2;

      function update() {
        const a = m * m - n * n;
        const b = 2 * m * n;
        const c = m * m + n * n;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">
              Generating Triple with $m = ${m}$ and $n = ${n}$:
            </div>

            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; margin-bottom:12px;">
              <div style="background:#1e293b; border:1px solid #06b6d4; border-radius:8px; padding:10px;">
                <div style="font-size:11px; color:#06b6d4;">$a = m^2 - n^2$</div>
                <div style="font-size:20px; font-weight:bold; color:#fff;">${a}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:8px; padding:10px;">
                <div style="font-size:11px; color:#10b981;">$b = 2mn$</div>
                <div style="font-size:20px; font-weight:bold; color:#fff;">${b}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #f59e0b; border-radius:8px; padding:10px;">
                <div style="font-size:11px; color:#f59e0b;">$c = m^2 + n^2$</div>
                <div style="font-size:20px; font-weight:bold; color:#fff;">${c}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:13px;">
              Verification: $${a}^2 + ${b}^2 = ${a*a} + ${b*b} = \\mathbf{${a*a + b*b}} = ${c}^2$ ✓
              <br><span style="color:#38bdf8; font-weight:bold;">Primitive Triple: (${a}, ${b}, ${c})</span>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Parameter m:</span>
            <input type="range" id="mParam" min="2" max="6" value="${m}">
            <span style="font-weight:bold; color:#38bdf8;">${m}</span>
          </div>
          <div class="sim-slider-group">
            <span>Parameter n:</span>
            <input type="range" id="nParam" min="1" max="${m-1}" value="${n}">
            <span style="font-weight:bold; color:#10b981;">${n}</span>
          </div>
        `;

        document.getElementById('mParam').oninput = (e) => {
          m = parseInt(e.target.value);
          if (n >= m) n = m - 1;
          update();
        };
        document.getElementById('nParam').oninput = (e) => {
          n = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 11: Euler's Brick Open Problem Explorer
    // -------------------------------------------------------------
    function renderSim11(vp, controls, title, badge) {
      title.innerHTML = "<span>🧱</span> Euler's Brick & Perfect Cuboid";
      badge.textContent = 'Unsolved 3D Mathematics';

      let a = 44, b = 117, c = 240; // Smallest Euler Brick

      function update() {
        const d1 = Math.sqrt(a * a + b * b);
        const d2 = Math.sqrt(b * b + c * c);
        const d3 = Math.sqrt(c * c + a * a);
        const spaceD = Math.sqrt(a * a + b * b + c * c);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:14px; font-weight:bold; color:#fcd34d; margin-bottom:8px;">
              Halcke\'s Euler Brick (1719): (44, 117, 240)
            </div>

            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px; margin-bottom:10px;">
              <div style="background:#1e293b; padding:8px; border-radius:6px; border:1px solid #10b981;">
                <div style="font-size:10px; color:#10b981;">Face Diagonal 1</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">d₁ = ${d1}</div>
              </div>
              <div style="background:#1e293b; padding:8px; border-radius:6px; border:1px solid #10b981;">
                <div style="font-size:10px; color:#10b981;">Face Diagonal 2</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">d₂ = ${d2}</div>
              </div>
              <div style="background:#1e293b; padding:8px; border-radius:6px; border:1px solid #10b981;">
                <div style="font-size:10px; color:#10b981;">Face Diagonal 3</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">d₃ = ${d3}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #f43f5e; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Space Interior Diagonal: $\\sqrt{44^2 + 117^2 + 240^2} = \\mathbf{${spaceD.toFixed(3)}}$ (Irrational!)
              <br><strong style="color:#fda4af;">The Open Mystery:</strong> Does a cuboid exist where all 3 edges, all 3 face diagonals, AND the space diagonal are all whole numbers? Unsolved for over 300 years!
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Euler Brick Presets:</div>
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn active">Halcke Brick (44, 117, 240)</button>
          </div>
        `;
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 12: 3D Space Diagonal Scanner
    // -------------------------------------------------------------
    function renderSim12(vp, controls, title, badge) {
      title.innerHTML = '<span>📦</span> 3D Space Diagonal Scanner';
      badge.textContent = 'Room Diagonal: √(l² + w² + h²)';

      let l = 12;
      let w = 4;
      let h = 3;

      function update() {
        const floorD = Math.sqrt(l * l + w * w).toFixed(2);
        const spaceD = Math.sqrt(l * l + w * w + h * h).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div>
                <span style="font-size:11px; color:#94a3b8;">Dimensions (l × w × h)</span>
                <div style="font-size:18px; font-weight:bold; color:#fff;">${l} × ${w} × ${h}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#38bdf8;">Floor Diagonal</span>
                <div style="font-size:18px; font-weight:bold; color:#38bdf8;">${floorD}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#fcd34d;">3D Space Diagonal</span>
                <div style="font-size:18px; font-weight:bold; color:#fcd34d;">${spaceD}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Step 1 (Floor): $d_\\text{floor} = \\sqrt{${l}^2 + ${w}^2} = \\sqrt{${l*l + w*w}} = \\mathbf{${floorD}}$
              <br>Step 2 (3D Space): $D = \\sqrt{d_\\text{floor}^2 + ${h}^2} = \\sqrt{${l*l + w*w + h*h}} = \\mathbf{${spaceD}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Length (l):</span>
            <input type="range" id="lBox" min="4" max="16" value="${l}">
            <span style="font-weight:bold; color:#fff;">${l}</span>
          </div>
          <div class="sim-slider-group">
            <span>Width (w):</span>
            <input type="range" id="wBox" min="2" max="10" value="${w}">
            <span style="font-weight:bold; color:#fff;">${w}</span>
          </div>
          <div class="sim-slider-group">
            <span>Height (h):</span>
            <input type="range" id="hBox" min="2" max="10" value="${h}">
            <span style="font-weight:bold; color:#fff;">${h}</span>
          </div>
        `;

        document.getElementById('lBox').oninput = (e) => {
          l = parseInt(e.target.value);
          update();
        };
        document.getElementById('wBox').oninput = (e) => {
          w = parseInt(e.target.value);
          update();
        };
        document.getElementById('hBox').oninput = (e) => {
          h = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 13: Converse Triangle Classifier
    // -------------------------------------------------------------
    function renderSim13(vp, controls, title, badge) {
      title.innerHTML = '<span>🔍</span> Converse Triangle Classifier';
      badge.textContent = 'Acute, Right, or Obtuse Decision';

      let a = 6;
      let b = 8;
      let c = 10;

      function update() {
        const sum2 = a * a + b * b;
        const c2 = c * c;

        let classification = '';
        let color = '';

        if (sum2 === c2) {
          classification = 'RIGHT-ANGLED TRIANGLE (a² + b² = c²)';
          color = '#10b981';
        } else if (sum2 > c2) {
          classification = 'ACUTE-ANGLED TRIANGLE (a² + b² > c²)';
          color = '#06b6d4';
        } else {
          classification = 'OBTUSE-ANGLED TRIANGLE (a² + b² < c²)';
          color = '#f43f5e';
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:16px; font-weight:bold; color:${color}; margin-bottom:10px;">
              ${classification}
            </div>

            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div style="background:#1e293b; padding:10px 16px; border-radius:8px;">
                <div style="font-size:11px; color:#94a3b8;">a² + b²</div>
                <div style="font-size:18px; font-weight:bold; color:#38bdf8;">${a*a} + ${b*b} = ${sum2}</div>
              </div>
              <div style="align-self:center; font-size:22px; font-weight:bold; color:${color};">
                ${sum2 === c2 ? '=' : (sum2 > c2 ? '>' : '<')}
              </div>
              <div style="background:#1e293b; padding:10px 16px; border-radius:8px;">
                <div style="font-size:11px; color:#94a3b8;">c² (Longest side)</div>
                <div style="font-size:18px; font-weight:bold; color:#fcd34d;">${c}^2 = ${c2}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Sides: $a = ${a}, b = ${b}, c = ${c}$.
              <br>Converse Rule: If $a^2+b^2=c^2 \\implies$ Right. If $> \\implies$ Acute. If $< \\implies$ Obtuse.
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Side a:</span>
            <input type="range" id="caRange" min="3" max="10" value="${a}">
            <span style="font-weight:bold; color:#38bdf8;">${a}</span>
          </div>
          <div class="sim-slider-group">
            <span>Side b:</span>
            <input type="range" id="cbRange" min="3" max="10" value="${b}">
            <span style="font-weight:bold; color:#38bdf8;">${b}</span>
          </div>
          <div class="sim-slider-group">
            <span>Longest Side c:</span>
            <input type="range" id="ccRange" min="${Math.max(a,b)}" max="15" value="${c}">
            <span style="font-weight:bold; color:#fcd34d;">${c}</span>
          </div>
        `;

        document.getElementById('caRange').oninput = (e) => {
          a = parseInt(e.target.value);
          if (c < Math.max(a, b)) c = Math.max(a, b);
          update();
        };
        document.getElementById('cbRange').oninput = (e) => {
          b = parseInt(e.target.value);
          if (c < Math.max(a, b)) c = Math.max(a, b);
          update();
        };
        document.getElementById('ccRange').oninput = (e) => {
          c = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 14: Sulbasūtra Knotted Rope Altar Builder
    // -------------------------------------------------------------
    function renderSim14(vp, controls, title, badge) {
      title.innerHTML = "<span>🪢</span> Baudhāyana's Knotted Rope Altar";
      badge.textContent = 'Ancient Cord Geometry (Śulba)';

      let triple = '345'; // 345 or 51213

      function update() {
        const a = triple === '345' ? 3 : 5;
        const b = triple === '345' ? 4 : 12;
        const c = triple === '345' ? 5 : 13;
        const total = a + b + c;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <svg viewBox="0 0 280 180" style="max-width:260px; width:100%;">
              <!-- Ground Base line with pegs -->
              <line x1="40" y1="150" x2="240" y2="150" stroke="#475569" stroke-width="2"/>
              
              <!-- Knotted Cord forming right triangle -->
              <polygon points="60,150 ${60 + b*13},150 60,${150 - a*13}" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="3" stroke-linejoin="round"/>

              <!-- Pegs (Dots at Vertices) -->
              <circle cx="60" cy="150" r="5" fill="#f43f5e"/>
              <circle cx="${60 + b*13}" cy="150" r="5" fill="#f43f5e"/>
              <circle cx="60" cy="${150 - a*13}" r="5" fill="#f43f5e"/>

              <!-- Knots illustration -->
              <text x="60" y="166" fill="#fcd34d" font-size="10" text-anchor="middle">Peg A (0°)</text>
              <text x="${60 + b*13}" y="166" fill="#fcd34d" font-size="10" text-anchor="middle">Peg B</text>
              <text x="50" y="${150 - a*13}" fill="#fcd34d" font-size="10" text-anchor="end">Peg C (90°)</text>
            </svg>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Knotted Cord Segments: <strong>${a} : ${b} : ${c}</strong> (Total rope = ${total} units)
              <br>When pulled taut between the three pegs, the corner at Peg A is strictly an <strong>exact 90° right angle</strong> without any optical instruments!
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Select Knotted Cord:</div>
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn ${triple==='345'?'active':''}" onclick="setTriple('345')">12-Knot Rope (3, 4, 5)</button>
            <button class="sim-btn ${triple==='51213'?'active':''}" onclick="setTriple('51213')">30-Knot Rope (5, 12, 13)</button>
          </div>
        `;

        window.setTriple = (tr) => {
          triple = tr;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 15: Baudhāyana Master Formula Matrix
    // -------------------------------------------------------------
    function renderSim15(vp, controls, title, badge) {
      title.innerHTML = '<span>📋</span> Master Formula Matrix';
      badge.textContent = 'Formula & Identity Repository';

      let activeTab = 0;
      const matrix = [
        {
          name: 'Right Triangle Hypotenuse',
          eq: 'c = \\\\sqrt{a^2 + b^2}',
          desc: 'Calculates the longest side given legs a and b.'
        },
        {
          name: 'Square Diagonal Law',
          eq: 'd = s\\\\sqrt{2}',
          desc: 'Diagonal of any square of side s. Doubles area: d² = 2s².'
        },
        {
          name: '3D Space Diagonal',
          eq: 'D = \\\\sqrt{l^2 + w^2 + h^2}',
          desc: 'Interior diagonal across opposite vertices of a room or box.'
        },
        {
          name: 'Equilateral Triangle Altitude',
          eq: 'h = \\\\frac{\\\\sqrt{3}}{2}s',
          desc: 'Height of an equilateral triangle of side s.'
        }
      ];

      function update() {
        const item = matrix[activeTab];
        vp.innerHTML = `
          <div style="width:100%; text-align:left;">
            <div style="font-size:15px; font-weight:bold; color:#fcd34d; margin-bottom:8px; border-bottom:1px solid #334155; padding-bottom:4px;">
              ${item.name}
            </div>
            <div style="background:#1e293b; border:1px solid #6366f1; border-radius:8px; padding:12px; margin-bottom:10px; font-size:18px; color:#38bdf8; text-align:center;">
              $$${item.eq}$$
            </div>
            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px; font-size:12.5px; color:#6ee7b7;">
              ${item.desc}
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
            ${matrix.map((m, i) => `
              <button class="sim-btn ${activeTab===i?'active':''}" onclick="setMatrixTab(${i})" style="font-size:11px; padding:5px 8px;">
                ${m.name.split(' ')[0]}
              </button>
            `).join('')}
          </div>
        `;

        window.setMatrixTab = (i) => {
          activeTab = i;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 16: Find the Colours Puzzle Room
    // -------------------------------------------------------------
    function renderSim16(vp, controls, title, badge) {
      title.innerHTML = '<span>🎨</span> Find the Colours! Puzzle Room';
      badge.textContent = 'Hypotenuse Distance √5 Geometry';

      // 5x5 grid of nodes
      let colors = new Array(25).fill(0); // 0 to 4
      const palette = ['#6366f1', '#10b981', '#f59e0b', '#f43f5e', '#06b6d4'];

      function checkConflicts() {
        let count = 0;
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            const idx = r * 5 + c;
            const deltas = [[1, 2], [2, 1], [-1, 2], [-2, 1]];
            for (let [dr, dc] of deltas) {
              const nr = r + dr;
              const nc = c + dc;
              if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5) {
                const nIdx = nr * 5 + nc;
                if (colors[idx] === colors[nIdx]) count++;
              }
            }
          }
        }
        return count;
      }

      function update() {
        const conflicts = checkConflicts();

        let gridNodes = '';
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            const idx = r * 5 + c;
            gridNodes += `
              <div onclick="cycleColor(${idx})" style="width:32px; height:32px; border-radius:50%; background:${palette[colors[idx]]}; border:2px solid #fff; cursor:pointer; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:bold; color:#0f172a; transition:all 0.15s;">
                ${colors[idx]+1}
              </div>
            `;
          }
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:grid; grid-template-columns:repeat(5, 34px); gap:8px; justify-content:center; margin-bottom:12px;">
              ${gridNodes}
            </div>

            <div style="background:#0f172a; border:1px solid ${conflicts>0 ? '#f43f5e' : '#10b981'}; border-radius:10px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Points at Knight-Move Distance $\\sqrt{2^2 + 1^2} = \\mathbf{\\sqrt{5}}$ cannot share the same color.
              <br>Conflicts: <strong style="color:${conflicts>0 ? '#fda4af' : '#6ee7b7'};">${conflicts === 0 ? '0 (Perfect 5-Coloring!)' : conflicts + ' Conflicts Detected'}</strong>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn" onclick="autoSolveColours()">Auto-Solve (Valid 5-Coloring)</button>
            <button class="sim-btn" onclick="resetColours()" style="background:#475569;">Reset All</button>
          </div>
        `;

        window.cycleColor = (idx) => {
          colors[idx] = (colors[idx] + 1) % 5;
          update();
        };

        window.autoSolveColours = () => {
          // Standard knight graph periodic 5-coloring: (2r + c) % 5
          for (let r = 0; r < 5; r++) {
            for (let c = 0; c < 5; c++) {
              colors[r * 5 + c] = (2 * r + c) % 5;
            }
          }
          update();
        };

        window.resetColours = () => {
          colors = new Array(25).fill(0);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // ==========================================
    // Page Initializer
    // ==========================================
    window.addEventListener('DOMContentLoaded', () => {
      loadSlide(0);
    });
  </script>
</body>
</html>
"""

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html = TEMPLATE.replace("__SLIDES_JSON__", slides_json).replace("__QUIZ_JSON__", quiz_json)
    return html

if __name__ == "__main__":
    html_output = generate_html()
    
    # Save template file
    template_path = os.path.join(os.path.dirname(__file__), "template_class8_math_baudhayana_pythagoras.html")
    with open(template_path, "w", encoding="utf-8") as tf:
        tf.write(TEMPLATE)
    print(f"Saved template: {template_path}")

    # Generate public animation HTML
    output_path = os.path.join(os.path.dirname(__file__), "..", "public", "animations", "class8-math-baudhayana-pythagoras.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Generated {output_path} ({len(html_output)} bytes)")
