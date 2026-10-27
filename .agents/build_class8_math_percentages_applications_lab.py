import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_percentages_applications_data import slides_data, quiz_questions

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 8: Comparing Quantities — Percentages & Applications Lab</title>
  
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
      <span class="header-badge">CLASS 8 • MATHEMATICS • CHAPTER 8</span>
      <span class="header-title">Comparing Quantities: Percentages & Applications Lab</span>
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
      <div class="slide-tag" id="slideTag">CHAPTER 8 • SLIDE 1 OF 20</div>
      <h1 class="slide-title" id="slideTitle">Hidden Fractions</h1>
      <p class="slide-subtitle" id="slideSubtitle">Unmasking Parts of a Whole & Hundredths</p>
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
          Welcome to our laboratory on percentages and practical applications!
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
      document.getElementById('slideTag').textContent = `CHAPTER 8 • SLIDE ${index + 1} OF 20`;
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
        case 'hidden_fractions_grid_scanner':
          renderSim1(vp, controls, title, badge);
          break;
        case 'fraction_to_percent_morpher':
          renderSim2(vp, controls, title, badge);
          break;
        case 'everyday_percentages_dashboard':
          renderSim3(vp, controls, title, badge);
          break;
        case 'mental_benchmark_decomposer':
          renderSim4(vp, controls, title, badge);
          break;
        case 'fdp_trinity_converter':
          renderSim5(vp, controls, title, badge);
          break;
        case 'beyond_hundred_stack_visualizer':
          renderSim6(vp, controls, title, badge);
          break;
        case 'proportion_normalizer_scale':
          renderSim7(vp, controls, title, badge);
          break;
        case 'gold_purity_kyc_scanner':
          renderSim8(vp, controls, title, badge);
          break;
        case 'percentage_change_elevator':
          renderSim9(vp, controls, title, badge);
          break;
        case 'profit_loss_trading_counter':
          renderSim10(vp, controls, title, badge);
          break;
        case 'invoice_gst_generator':
          renderSim11(vp, controls, title, badge);
          break;
        case 'compounding_exponential_growth_tree':
          renderSim12(vp, controls, title, badge);
          break;
        case 'asset_depreciation_decay_curve':
          renderSim13(vp, controls, title, badge);
          break;
        case 'percentage_paradox_investigator':
          renderSim14(vp, controls, title, badge);
          break;
        case 'base_blunder_debugger_matrix':
          renderSim15(vp, controls, title, badge);
          break;
        case 'peaceful_knights_chessboard_lab':
          renderSim16(vp, controls, title, badge);
          break;
      }
      triggerMathRender(vp);
    }

    // -------------------------------------------------------------
    // Simulator 1: Hidden Fractions Grid Scanner
    // -------------------------------------------------------------
    function renderSim1(vp, controls, title, badge) {
      title.innerHTML = '<span>🔍</span> Hidden Fractions Grid Scanner';
      badge.textContent = 'Fractional Part Unmasker';

      let den = 10;
      let num = 3;

      function update() {
        const pct = ((num / den) * 100).toFixed(1);
        const dec = (num / den).toFixed(3);

        let gridCells = '';
        for (let i = 0; i < den; i++) {
          const filled = i < num;
          gridCells += `<div style="flex:1; min-width:${Math.max(16, 280/den)}px; height:45px; background:${filled ? 'linear-gradient(135deg, #06b6d4, #6366f1)' : '#1e293b'}; border:1px solid ${filled ? '#38bdf8' : '#334155'}; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; color:${filled ? '#fff' : '#64748b'}; transition:all 0.2s;">${i+1}</div>`;
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">Partition of Whole: <strong>${num} out of ${den} equal pieces</strong></div>
            <div style="display:flex; flex-wrap:wrap; gap:4px; justify-content:center; max-width:360px; margin:0 auto 16px auto;">
              ${gridCells}
            </div>

            <!-- Mathematical Unmasking -->
            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:12px; font-size:13px; line-height:1.6;">
              <div style="color:#38bdf8; font-weight:bold; font-size:15px; margin-bottom:4px;">
                Fraction: $\\frac{${num}}{${den}}$ $\\implies$ <strong>${pct}%</strong>
              </div>
              <div style="color:#cbd5e1;">
                Decimal value: <strong>${dec}</strong> | Scaling to 100: $\\frac{${num}}{${den}} \\times 100\\% = \\mathbf{${pct}\\%}$
              </div>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Denominator:</span>
            <select id="denSelect" style="background:#0f172a; color:#fff; border:1px solid #6366f1; border-radius:6px; padding:4px 8px; font-size:12px;">
              <option value="4" ${den===4?'selected':''}>4 pieces (quarters)</option>
              <option value="5" ${den===5?'selected':''}>5 pieces (fifths)</option>
              <option value="8" ${den===8?'selected':''}>8 pieces (eighths)</option>
              <option value="10" ${den===10?'selected':''}>10 pieces (tenths)</option>
              <option value="20" ${den===20?'selected':''}>20 pieces (twentieths)</option>
              <option value="25" ${den===25?'selected':''}>25 pieces</option>
            </select>
          </div>
          <div class="sim-slider-group">
            <span>Numerator (${num}):</span>
            <input type="range" id="numRange" min="0" max="${den}" value="${num}">
          </div>
        `;

        document.getElementById('denSelect').onchange = (e) => {
          den = parseInt(e.target.value);
          if (num > den) num = den;
          update();
        };
        document.getElementById('numRange').oninput = (e) => {
          num = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 2: Fraction to Percent Morpher (100-Bead Grid)
    // -------------------------------------------------------------
    function renderSim2(vp, controls, title, badge) {
      title.innerHTML = '<span>⚡</span> Fraction to Percent Morpher';
      badge.textContent = '100-Bead Grid Matrix';

      let currentA = 3;
      let currentB = 5;

      const presets = [
        { a: 1, b: 2, label: '1/2' },
        { a: 1, b: 4, label: '1/4' },
        { a: 3, b: 4, label: '3/4' },
        { a: 2, b: 5, label: '2/5' },
        { a: 3, b: 5, label: '3/5' },
        { a: 7, b: 10, label: '7/10' },
        { a: 3, b: 8, label: '3/8' },
        { a: 17, b: 25, label: '17/25' }
      ];

      function update() {
        const pct = ((currentA / currentB) * 100);
        const roundedBeads = Math.round(pct);

        let beads = '';
        for (let i = 0; i < 100; i++) {
          const on = i < roundedBeads;
          beads += `<div style="width:16px; height:16px; border-radius:50%; background:${on ? '#10b981' : '#1e293b'}; border:1px solid ${on ? '#34d399' : '#334155'}; box-shadow:${on ? '0 0 6px #10b981' : 'none'}; transition:all 0.15s;"></div>`;
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:grid; grid-template-columns:repeat(10, 16px); gap:6px; justify-content:center; margin-bottom:14px;">
              ${beads}
            </div>

            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:12px; font-size:13px;">
              <div style="color:#6ee7b7; font-weight:bold; font-size:15px; margin-bottom:4px;">
                $$\\frac{${currentA}}{${currentB}} \\times 100\\% = \\frac{${currentA * 100}}{${currentB}}\\% = \\mathbf{${pct.toFixed(1)}\\%}$$
              </div>
              <div style="color:#94a3b8;">
                Exactly <strong>${roundedBeads}</strong> out of 100 beads illuminated.
              </div>
            </div>
          </div>
        `;

        let btnHtml = presets.map((p, idx) => `
          <button class="sim-btn ${p.a===currentA && p.b===currentB ? 'active' : ''}" onclick="selectPreset(${idx})" style="padding:5px 10px; font-size:11px;">
            ${p.label}
          </button>
        `).join('');

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Select Fraction to Morph:</div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
            ${btnHtml}
          </div>
        `;

        window.selectPreset = (idx) => {
          currentA = presets[idx].a;
          currentB = presets[idx].b;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 3: Everyday Percentages Dashboard
    // -------------------------------------------------------------
    function renderSim3(vp, controls, title, badge) {
      title.innerHTML = '<span>📱</span> Everyday Percentages Dashboard';
      badge.textContent = 'Real-World Meters';

      let mode = 'battery'; // battery, marks, storage
      let val = 75;

      function update() {
        if (mode === 'battery') {
          const col = val > 30 ? '#10b981' : (val > 15 ? '#f59e0b' : '#f43f5e');
          const hoursLeft = ((val / 100) * 16).toFixed(1);
          vp.innerHTML = `
            <div style="width:100%; text-align:center;">
              <div style="font-size:14px; font-weight:700; color:#38bdf8; margin-bottom:10px;">Smartphone Battery Gauge</div>
              <div style="width:180px; height:85px; border:4px solid #475569; border-radius:12px; margin:0 auto; position:relative; padding:6px; display:flex; align-items:center;">
                <!-- Battery Tip -->
                <div style="position:absolute; right:-14px; top:28px; width:10px; height:26px; background:#475569; border-radius:0 4px 4px 0;"></div>
                <div style="height:100%; width:${val}%; background:${col}; border-radius:6px; transition:width 0.2s ease, background 0.2s; display:flex; align-items:center; justify-content:center; color:#0f172a; font-weight:bold; font-size:16px;">
                  ${val}%
                </div>
              </div>
              <div style="margin-top:14px; background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
                Battery Level: <strong>${val}%</strong> | Estimated remaining runtime: <strong>${hoursLeft} hours</strong>
                <br><span style="color:#94a3b8; font-size:11.5px;">Remaining charge fraction: ${val}/100 = ${(val/100).toFixed(2)}</span>
              </div>
            </div>
          `;
        } else if (mode === 'marks') {
          const maxMarks = 80;
          const marks = Math.round((val / 100) * maxMarks);
          const pct = ((marks / maxMarks) * 100).toFixed(1);
          const grade = pct >= 90 ? 'A+ (Outstanding)' : (pct >= 75 ? 'A (Excellent)' : (pct >= 60 ? 'B (Good)' : (pct >= 40 ? 'C (Pass)' : 'F (Needs Improvement)')));

          vp.innerHTML = `
            <div style="width:100%; text-align:center;">
              <div style="font-size:14px; font-weight:700; color:#38bdf8; margin-bottom:10px;">Exam Marks Normalizer (Out of ${maxMarks})</div>
              <div style="font-size:26px; font-weight:bold; color:#a5b4fc; margin-bottom:6px;">
                ${marks} / ${maxMarks}
              </div>
              <div style="width:80%; height:20px; background:#1e293b; border-radius:10px; margin:0 auto 12px auto; overflow:hidden;">
                <div style="height:100%; width:${pct}%; background:linear-gradient(90deg, #6366f1, #06b6d4); border-radius:10px; transition:width 0.2s;"></div>
              </div>
              <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
                Calculation: $\\frac{${marks}}{${maxMarks}} \\times 100\\% = \\mathbf{${pct}\\%}$
                <br>Grade Bracket: <strong style="color:#fcd34d;">${grade}</strong>
              </div>
            </div>
          `;
        } else {
          const totalGB = 128;
          const usedGB = Math.round((val / 100) * totalGB);
          const freeGB = totalGB - usedGB;
          vp.innerHTML = `
            <div style="width:100%; text-align:center;">
              <div style="font-size:14px; font-weight:700; color:#38bdf8; margin-bottom:10px;">Phone Storage Breakdown (128 GB)</div>
              <div style="display:flex; height:26px; width:85%; border-radius:8px; overflow:hidden; margin:0 auto 14px auto; border:1px solid #475569;">
                <div style="width:${val}%; background:#f43f5e; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#fff;">Used ${val}%</div>
                <div style="width:${100-val}%; background:#10b981; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#fff;">Free ${100-val}%</div>
              </div>
              <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
                Used: <strong style="color:#fda4af;">${usedGB} GB</strong> (${val}%) | Available: <strong style="color:#6ee7b7;">${freeGB} GB</strong> (${100-val}%)
              </div>
            </div>
          `;
        }

        controls.innerHTML = `
          <div style="display:flex; gap:8px; justify-content:center; margin-bottom:8px;">
            <button class="sim-btn ${mode==='battery'?'active':''}" onclick="setDashboardMode('battery')">🔋 Battery</button>
            <button class="sim-btn ${mode==='marks'?'active':''}" onclick="setDashboardMode('marks')">📝 Test Marks</button>
            <button class="sim-btn ${mode==='storage'?'active':''}" onclick="setDashboardMode('storage')">💾 Storage Quota</button>
          </div>
          <div class="sim-slider-group">
            <span>Adjust Level:</span>
            <input type="range" id="dashRange" min="0" max="100" value="${val}">
            <span style="font-weight:bold; color:#38bdf8;">${val}%</span>
          </div>
        `;

        document.getElementById('dashRange').oninput = (e) => {
          val = parseInt(e.target.value);
          update();
        };

        window.setDashboardMode = (m) => {
          mode = m;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 4: Mental Benchmark Decomposer
    // -------------------------------------------------------------
    function renderSim4(vp, controls, title, badge) {
      title.innerHTML = '<span>🧠</span> Mental Benchmark Decomposer';
      badge.textContent = 'Mental Math Shortcuts';

      let baseVal = 480;
      let targetPct = 15;

      function update() {
        const b50 = baseVal * 0.5;
        const b10 = baseVal * 0.1;
        const b5 = b10 * 0.5;
        const b1 = baseVal * 0.01;
        const result = (baseVal * (targetPct / 100)).toFixed(2);

        let decompositionHtml = '';
        if (targetPct === 15) {
          decompositionHtml = `15% = 10% + 5% = ${b10} + ${b5} = <strong>${b10 + b5}</strong>`;
        } else if (targetPct === 25) {
          decompositionHtml = `25% = 50% ÷ 2 = ${b50} ÷ 2 = <strong>${b50 / 2}</strong>`;
        } else if (targetPct === 35) {
          decompositionHtml = `35% = 3 × 10% + 5% = 3(${b10}) + ${b5} = ${3*b10} + ${b5} = <strong>${3*b10 + b5}</strong>`;
        } else if (targetPct === 65) {
          decompositionHtml = `65% = 50% + 10% + 5% = ${b50} + ${b10} + ${b5} = <strong>${b50 + b10 + b5}</strong>`;
        } else if (targetPct === 2) {
          decompositionHtml = `2% = 2 × 1% = 2 × ${b1} = <strong>${2 * b1}</strong>`;
        } else {
          decompositionHtml = `${targetPct}% of ${baseVal} = ${result}`;
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:14px; color:#94a3b8; margin-bottom:8px;">Base Number: <strong style="color:#38bdf8; font-size:16px;">₹${baseVal}</strong></div>
            
            <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; margin-bottom:14px;">
              <div style="background:#1e293b; border:1px solid #475569; border-radius:8px; padding:8px;">
                <div style="font-size:11px; color:#a5b4fc;">50% (Half)</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">₹${b50}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #475569; border-radius:8px; padding:8px;">
                <div style="font-size:11px; color:#38bdf8;">10% (÷10)</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">₹${b10}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #475569; border-radius:8px; padding:8px;">
                <div style="font-size:11px; color:#fcd34d;">5% (10% ÷ 2)</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">₹${b5}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #475569; border-radius:8px; padding:8px;">
                <div style="font-size:11px; color:#f43f5e;">1% (÷100)</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">₹${b1}</div>
              </div>
            </div>

            <!-- Target Breakdown -->
            <div style="background:#0f172a; border:1px solid #6366f1; border-radius:10px; padding:12px; font-size:13px; line-height:1.6;">
              <div style="color:#a5b4fc; font-weight:bold; font-size:15px; margin-bottom:4px;">
                Calculating ${targetPct}% of ₹${baseVal}:
              </div>
              <div style="color:#34d399; font-size:14px;">
                ${decompositionHtml}
              </div>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Base Value:</span>
            <input type="range" id="baseRange" min="50" max="1200" step="10" value="${baseVal}">
            <span style="font-weight:bold; color:#38bdf8;">₹${baseVal}</span>
          </div>
          <div style="font-size:12px; color:#94a3b8; margin-top:4px;">Preset Percentages:</div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
            <button class="sim-btn ${targetPct===15?'active':''}" onclick="setTargetPct(15)">15%</button>
            <button class="sim-btn ${targetPct===25?'active':''}" onclick="setTargetPct(25)">25%</button>
            <button class="sim-btn ${targetPct===35?'active':''}" onclick="setTargetPct(35)">35%</button>
            <button class="sim-btn ${targetPct===65?'active':''}" onclick="setTargetPct(65)">65%</button>
            <button class="sim-btn ${targetPct===2?'active':''}" onclick="setTargetPct(2)">2%</button>
          </div>
        `;

        document.getElementById('baseRange').oninput = (e) => {
          baseVal = parseInt(e.target.value);
          update();
        };

        window.setTargetPct = (p) => {
          targetPct = p;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 5: The FDP Trinity Converter
    // -------------------------------------------------------------
    function renderSim5(vp, controls, title, badge) {
      title.innerHTML = '<span>🔄</span> The FDP Trinity Converter';
      badge.textContent = 'Fractions • Decimals • Percentages';

      let pct = 40;

      function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
      }

      function update() {
        const dec = (pct / 100).toFixed(2);
        const g = gcd(pct, 100);
        const num = pct / g;
        const den = 100 / g;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <!-- Triple Card Trinity -->
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:16px;">
              <div style="background:#1e293b; border:1px solid #38bdf8; border-radius:10px; padding:12px;">
                <div style="font-size:11px; color:#38bdf8; font-weight:700;">FRACTION</div>
                <div style="font-size:20px; font-weight:bold; color:#fff; margin-top:4px;">$$\\frac{${num}}{${den}}$$</div>
              </div>
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:10px; padding:12px;">
                <div style="font-size:11px; color:#10b981; font-weight:700;">DECIMAL</div>
                <div style="font-size:22px; font-weight:bold; color:#fff; margin-top:4px;">${dec}</div>
              </div>
              <div style="background:#1e293b; border:1px solid #f59e0b; border-radius:10px; padding:12px;">
                <div style="font-size:11px; color:#f59e0b; font-weight:700;">PERCENTAGE</div>
                <div style="font-size:22px; font-weight:bold; color:#fff; margin-top:4px;">${pct}%</div>
              </div>
            </div>

            <!-- Visual Bar Scale -->
            <div style="width:90%; height:24px; background:#0f172a; border-radius:12px; margin:0 auto 10px auto; overflow:hidden; border:1px solid #334155; position:relative;">
              <div style="height:100%; width:${pct}%; background:linear-gradient(90deg, #6366f1, #06b6d4, #10b981); border-radius:12px; transition:width 0.2s;"></div>
            </div>

            <div style="font-size:12px; color:#94a3b8;">
              Conversion path: $\\frac{${num}}{${den}} \\times 100\\% = \\mathbf{${pct}\\%} \\implies \\mathbf{${dec}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Slide Value:</span>
            <input type="range" id="fdpRange" min="1" max="100" value="${pct}">
            <span style="font-weight:bold; color:#38bdf8;">${pct}%</span>
          </div>
        `;

        document.getElementById('fdpRange').oninput = (e) => {
          pct = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 6: Percentages Beyond 100%
    // -------------------------------------------------------------
    function renderSim6(vp, controls, title, badge) {
      title.innerHTML = '<span>📈</span> Percentages Beyond 100%';
      badge.textContent = 'Improper Multiples & Overflow';

      let pct = 175;

      function update() {
        const fullBars = Math.floor(pct / 100);
        const remainder = pct % 100;
        const multiplier = (pct / 100).toFixed(2);

        let barsHtml = '';
        for (let i = 0; i < fullBars; i++) {
          barsHtml += `
            <div style="width:100%; background:#059669; border:1px solid #34d399; border-radius:8px; padding:6px 12px; display:flex; justify-content:space-between; align-items:center; font-size:12px; font-weight:bold; color:#fff;">
              <span>Unit Whole #${i+1}</span>
              <span>100% (Full)</span>
            </div>
          `;
        }
        if (remainder > 0) {
          barsHtml += `
            <div style="width:100%; background:#1e293b; border:1px solid #475569; border-radius:8px; padding:4px; overflow:hidden; position:relative;">
              <div style="width:${remainder}%; height:26px; background:linear-gradient(90deg, #6366f1, #06b6d4); border-radius:6px; display:flex; align-items:center; padding-left:8px; font-size:11px; font-weight:bold; color:#fff;">
                Overflow: +${remainder}%
              </div>
            </div>
          `;
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="font-size:24px; font-weight:bold; color:#38bdf8; margin-bottom:4px;">
              ${pct}%
            </div>
            <div style="font-size:13px; color:#94a3b8; margin-bottom:12px;">
              Scaling Multiplier: <strong style="color:#fff;">${multiplier}×</strong> of original base
            </div>

            <div style="display:flex; flex-direction:column; gap:6px; max-width:320px; margin:0 auto 14px auto;">
              ${barsHtml}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              As improper fraction: $\\frac{${pct}}{100} = ${(pct/25).toFixed(0)}/4 = ${(pct/100).toFixed(2)}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Percentage:</span>
            <input type="range" id="overRange" min="100" max="300" step="5" value="${pct}">
            <span style="font-weight:bold; color:#38bdf8;">${pct}%</span>
          </div>
        `;

        document.getElementById('overRange').oninput = (e) => {
          pct = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 7: Proportion Normalizer Scale
    // -------------------------------------------------------------
    function renderSim7(vp, controls, title, badge) {
      title.innerHTML = '<span>⚖️</span> Proportion Normalizer Scale';
      badge.textContent = 'Comparing Disparate Bases';

      let aNum = 18, aDen = 25; // 72%
      let bNum = 21, bDen = 30; // 70%

      function update() {
        const pctA = ((aNum / aDen) * 100).toFixed(1);
        const pctB = ((bNum / bDen) * 100).toFixed(1);
        const aWins = parseFloat(pctA) > parseFloat(pctB);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <!-- Contender A -->
            <div style="background:#1e293b; border:1px solid ${aWins ? '#10b981' : '#475569'}; border-radius:10px; padding:10px; margin-bottom:10px;">
              <div style="display:flex; justify-content:space-between; font-size:12.5px; margin-bottom:4px;">
                <span style="font-weight:bold; color:#38bdf8;">Candidate A: ${aNum} / ${aDen}</span>
                <span style="font-weight:bold; color:#fff;">Normalized: ${pctA}%</span>
              </div>
              <div style="width:100%; height:14px; background:#0f172a; border-radius:6px; overflow:hidden;">
                <div style="width:${pctA}%; height:100%; background:#38bdf8;"></div>
              </div>
            </div>

            <!-- Contender B -->
            <div style="background:#1e293b; border:1px solid ${!aWins ? '#10b981' : '#475569'}; border-radius:10px; padding:10px; margin-bottom:14px;">
              <div style="display:flex; justify-content:space-between; font-size:12.5px; margin-bottom:4px;">
                <span style="font-weight:bold; color:#a855f7;">Candidate B: ${bNum} / ${bDen}</span>
                <span style="font-weight:bold; color:#fff;">Normalized: ${pctB}%</span>
              </div>
              <div style="width:100%; height:14px; background:#0f172a; border-radius:6px; overflow:hidden;">
                <div style="width:${pctB}%; height:100%; background:#a855f7;"></div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              <strong>Verdict:</strong> ${aWins ? '<span style="color:#34d399;">Candidate A has higher rate</span>' : '<span style="color:#a855f7;">Candidate B has higher rate</span>'}
              (${pctA}% vs ${pctB}%). Percentages bring both to a common base of 100!
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Candidate A (${aNum}/${aDen}):</span>
            <input type="range" id="aRange" min="5" max="${aDen}" value="${aNum}">
          </div>
          <div class="sim-slider-group">
            <span>Candidate B (${bNum}/${bDen}):</span>
            <input type="range" id="bRange" min="5" max="${bDen}" value="${bNum}">
          </div>
        `;

        document.getElementById('aRange').oninput = (e) => {
          aNum = parseInt(e.target.value);
          update();
        };
        document.getElementById('bRange').oninput = (e) => {
          bNum = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 8: Content Purity & KYC Scanner
    // -------------------------------------------------------------
    function renderSim8(vp, controls, title, badge) {
      title.innerHTML = '<span>🏆</span> Content Purity & KYC Scanner';
      badge.textContent = 'Gold Karats & Nutrition KYC';

      let karat = 22;

      function update() {
        const purityPct = ((karat / 24) * 100).toFixed(2);
        const alloyPct = (100 - purityPct).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <!-- Gold Ingot Graphic -->
            <div style="width:220px; height:70px; background:linear-gradient(135deg, #f59e0b, #d97706); border-radius:8px; margin:0 auto 12px auto; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 6px 16px rgba(245, 158, 11, 0.3); border:2px solid #fcd34d;">
              <div style="font-size:18px; font-weight:900; color:#451a03; letter-spacing:1px;">${karat} KARAT GOLD</div>
              <div style="font-size:11px; font-weight:700; color:#78350f;">HALLMARK 916 / KYC PURITY</div>
            </div>

            <!-- Two-tone purity composition bar -->
            <div style="display:flex; height:24px; width:85%; border-radius:6px; overflow:hidden; margin:0 auto 12px auto; border:1px solid #475569;">
              <div style="width:${purityPct}%; background:#f59e0b; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#0f172a;">Pure Gold ${purityPct}%</div>
              <div style="width:${alloyPct}%; background:#64748b; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:bold; color:#fff;">Alloy ${alloyPct}%</div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Formula: $\\text{Purity } \\% = \\frac{${karat}}{24} \\times 100\\% = \\mathbf{${purityPct}\\%}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Select Karat Standard:</div>
          <div style="display:flex; gap:8px; justify-content:center;">
            <button class="sim-btn ${karat===24?'active':''}" onclick="setKarat(24)">24K (Pure)</button>
            <button class="sim-btn ${karat===22?'active':''}" onclick="setKarat(22)">22K (Jewellery)</button>
            <button class="sim-btn ${karat===18?'active':''}" onclick="setKarat(18)">18K</button>
            <button class="sim-btn ${karat===14?'active':''}" onclick="setKarat(14)">14K</button>
          </div>
        `;

        window.setKarat = (k) => {
          karat = k;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 9: Percentage Change Elevator (Increase/Decrease)
    // -------------------------------------------------------------
    function renderSim9(vp, controls, title, badge) {
      title.innerHTML = '<span>📶</span> Percentage Change Elevator';
      badge.textContent = 'Increase & Decrease Dynamics';

      let v0 = 80;
      let v1 = 100;

      function update() {
        const diff = v1 - v0;
        const isUp = diff >= 0;
        const pctChange = ((Math.abs(diff) / v0) * 100).toFixed(1);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:space-around; align-items:center; margin-bottom:14px;">
              <div style="background:#1e293b; border-radius:10px; padding:12px 18px; border:1px solid #475569;">
                <div style="font-size:11px; color:#94a3b8;">Initial Base ($V_0$)</div>
                <div style="font-size:22px; font-weight:bold; color:#fff;">₹${v0}</div>
              </div>
              <div style="font-size:24px; color:${isUp ? '#10b981' : '#f43f5e'}; font-weight:bold;">
                ${isUp ? '▲' : '▼'}
              </div>
              <div style="background:#1e293b; border-radius:10px; padding:12px 18px; border:1px solid #475569;">
                <div style="font-size:11px; color:#94a3b8;">Final Value ($V_1$)</div>
                <div style="font-size:22px; font-weight:bold; color:#fff;">₹${v1}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid ${isUp ? '#10b981' : '#f43f5e'}; border-radius:10px; padding:12px; font-size:13px;">
              <div style="font-size:15px; font-weight:bold; color:${isUp ? '#34d399' : '#fda4af'}; margin-bottom:4px;">
                ${isUp ? 'Percentage Increase' : 'Percentage Decrease'}: ${pctChange}%
              </div>
              <div style="color:#cbd5e1;">
                $$\\frac{|${v1} - ${v0}|}{${v0}} \\times 100\\% = \\frac{${Math.abs(diff)}}{${v0}} \\times 100\\% = \\mathbf{${pctChange}\\%}$$
              </div>
              <div style="font-size:11px; color:#94a3b8; margin-top:4px;">
                *Notice: The denominator is always the <strong>initial baseline (${v0})</strong>.
              </div>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Initial (Base):</span>
            <input type="range" id="v0Range" min="20" max="200" step="5" value="${v0}">
            <span style="font-weight:bold; color:#38bdf8;">₹${v0}</span>
          </div>
          <div class="sim-slider-group">
            <span>Final Value:</span>
            <input type="range" id="v1Range" min="20" max="200" step="5" value="${v1}">
            <span style="font-weight:bold; color:#38bdf8;">₹${v1}</span>
          </div>
        `;

        document.getElementById('v0Range').oninput = (e) => {
          v0 = parseInt(e.target.value);
          update();
        };
        document.getElementById('v1Range').oninput = (e) => {
          v1 = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 10: Profit and Loss Trading Counter
    // -------------------------------------------------------------
    function renderSim10(vp, controls, title, badge) {
      title.innerHTML = '<span>💰</span> Profit and Loss Trading Counter';
      badge.textContent = 'Merchant Ledger & Margins';

      let cp = 500;
      let sp = 650;

      function update() {
        const diff = sp - cp;
        const isProfit = diff >= 0;
        const marginPct = ((Math.abs(diff) / cp) * 100).toFixed(1);

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div>
                <span style="font-size:11px; color:#94a3b8;">Cost Price (CP)</span>
                <div style="font-size:20px; font-weight:bold; color:#fff;">₹${cp}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#94a3b8;">Selling Price (SP)</span>
                <div style="font-size:20px; font-weight:bold; color:#38bdf8;">₹${sp}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#94a3b8;">Status</span>
                <div style="font-size:18px; font-weight:bold; color:${isProfit ? '#10b981' : '#f43f5e'};">
                  ${isProfit ? 'PROFIT' : 'LOSS'}
                </div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid ${isProfit ? '#10b981' : '#f43f5e'}; border-radius:10px; padding:12px; font-size:13px;">
              <div style="font-size:16px; font-weight:bold; color:${isProfit ? '#34d399' : '#fda4af'}; margin-bottom:4px;">
                ${isProfit ? 'Profit' : 'Loss'} Amount: ₹${Math.abs(diff)} (${marginPct}%)
              </div>
              <div style="color:#cbd5e1;">
                Formula: $\\frac{\\text{${isProfit ? 'Profit' : 'Loss'}}}{\\text{CP}} \\times 100\\% = \\frac{${Math.abs(diff)}}{${cp}} \\times 100\\% = \\mathbf{${marginPct}\\%}$
              </div>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Cost Price (CP):</span>
            <input type="range" id="cpRange" min="100" max="1500" step="50" value="${cp}">
            <span style="font-weight:bold; color:#fff;">₹${cp}</span>
          </div>
          <div class="sim-slider-group">
            <span>Selling Price (SP):</span>
            <input type="range" id="spRange" min="100" max="1500" step="50" value="${sp}">
            <span style="font-weight:bold; color:#38bdf8;">₹${sp}</span>
          </div>
        `;

        document.getElementById('cpRange').oninput = (e) => {
          cp = parseInt(e.target.value);
          update();
        };
        document.getElementById('spRange').oninput = (e) => {
          sp = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 11: Invoice & GST Generator
    // -------------------------------------------------------------
    function renderSim11(vp, controls, title, badge) {
      title.innerHTML = '<span>🧾</span> Invoice & GST Generator';
      badge.textContent = 'Tax Invoice & Discount Engine';

      let mp = 2000;
      let discPct = 10;
      let gstSlab = 18;

      function update() {
        const discAmt = mp * (discPct / 100);
        const taxableSP = mp - discAmt;
        const gstAmt = taxableSP * (gstSlab / 100);
        const cgst = (gstAmt / 2).toFixed(2);
        const sgst = (gstAmt / 2).toFixed(2);
        const totalBill = (taxableSP + gstAmt).toFixed(2);

        vp.innerHTML = `
          <div style="width:100%; text-align:left; background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; font-family:monospace; font-size:12.5px; color:#cbd5e1; max-width:340px; margin:0 auto;">
            <div style="text-align:center; font-weight:bold; color:#fcd34d; margin-bottom:8px; font-size:13px; border-bottom:1px dashed #475569; padding-bottom:6px;">
              TAX INVOICE / CASH MEMO
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
              <span>Marked Price (MP):</span>
              <span>₹${mp.toFixed(2)}</span>
            </div>
            <div style="display:flex; justify-content:space-between; color:#34d399; margin-bottom:4px;">
              <span>Less: Discount (${discPct}%):</span>
              <span>-₹${discAmt.toFixed(2)}</span>
            </div>
            <div style="display:flex; justify-content:space-between; font-weight:bold; color:#fff; border-top:1px solid #334155; padding-top:4px; margin-bottom:6px;">
              <span>Taxable Selling Price:</span>
              <span>₹${taxableSP.toFixed(2)}</span>
            </div>
            <div style="display:flex; justify-content:space-between; color:#a5b4fc; margin-bottom:2px;">
              <span>CGST (${gstSlab/2}%):</span>
              <span>+₹${cgst}</span>
            </div>
            <div style="display:flex; justify-content:space-between; color:#a5b4fc; margin-bottom:6px;">
              <span>SGST (${gstSlab/2}%):</span>
              <span>+₹${sgst}</span>
            </div>
            <div style="display:flex; justify-content:space-between; font-weight:bold; font-size:14px; color:#38bdf8; border-top:1px dashed #475569; padding-top:6px;">
              <span>TOTAL INVOICE BILL:</span>
              <span>₹${totalBill}</span>
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Marked Price:</span>
            <input type="range" id="mpRange" min="500" max="5000" step="100" value="${mp}">
            <span style="font-weight:bold; color:#fff;">₹${mp}</span>
          </div>
          <div class="sim-slider-group">
            <span>Discount %:</span>
            <input type="range" id="discRange" min="0" max="40" step="5" value="${discPct}">
            <span style="font-weight:bold; color:#34d399;">${discPct}%</span>
          </div>
          <div style="display:flex; gap:6px; justify-content:center; margin-top:4px;">
            <span style="font-size:12px; color:#94a3b8; align-self:center;">GST Slab:</span>
            <button class="sim-btn ${gstSlab===5?'active':''}" onclick="setGst(5)">5%</button>
            <button class="sim-btn ${gstSlab===12?'active':''}" onclick="setGst(12)">12%</button>
            <button class="sim-btn ${gstSlab===18?'active':''}" onclick="setGst(18)">18%</button>
            <button class="sim-btn ${gstSlab===28?'active':''}" onclick="setGst(28)">28%</button>
          </div>
        `;

        document.getElementById('mpRange').oninput = (e) => {
          mp = parseInt(e.target.value);
          update();
        };
        document.getElementById('discRange').oninput = (e) => {
          discPct = parseInt(e.target.value);
          update();
        };
        window.setGst = (g) => {
          gstSlab = g;
          update();
        };
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 12: Compounding Exponential Growth Tree
    // -------------------------------------------------------------
    function renderSim12(vp, controls, title, badge) {
      title.innerHTML = '<span>🌱</span> Compounding Growth Tree';
      badge.textContent = 'CI vs Simple Interest Engine';

      let P = 10000;
      let r = 10;
      let n = 3;

      function update() {
        const si = P + (P * r * n) / 100;
        const ci = P * Math.pow(1 + r / 100, n);
        const diff = ci - si;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div style="background:#1e293b; border-radius:8px; padding:8px 14px; border:1px solid #475569;">
                <div style="font-size:11px; color:#94a3b8;">Simple Interest (SI)</div>
                <div style="font-size:16px; font-weight:bold; color:#cbd5e1;">₹${si.toFixed(0)}</div>
              </div>
              <div style="background:#1e293b; border-radius:8px; padding:8px 14px; border:1px solid #10b981;">
                <div style="font-size:11px; color:#10b981;">Compound Interest (CI)</div>
                <div style="font-size:16px; font-weight:bold; color:#34d399;">₹${ci.toFixed(0)}</div>
              </div>
            </div>

            <!-- Visual Bar Comparison -->
            <div style="width:90%; margin:0 auto 12px auto; display:flex; flex-direction:column; gap:6px;">
              <div style="text-align:left; font-size:11px; color:#94a3b8;">SI Growth:</div>
              <div style="height:14px; width:${Math.min(100, (si / (P * 2)) * 100)}%; background:#64748b; border-radius:4px;"></div>
              <div style="text-align:left; font-size:11px; color:#34d399;">CI Exponential Growth:</div>
              <div style="height:14px; width:${Math.min(100, (ci / (P * 2)) * 100)}%; background:#10b981; border-radius:4px;"></div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Compounding Bonus (Interest-on-Interest): <strong style="color:#fcd34d;">+₹${diff.toFixed(0)}</strong>
              <br>Formula: $A = P\\left(1 + \\frac{r}{100}\\right)^n = ${P}(1.${r < 10 ? '0'+r : r})^${n} = \\mathbf{₹${ci.toFixed(0)}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Principal ($P$):</span>
            <input type="range" id="pRange" min="2000" max="25000" step="1000" value="${P}">
            <span style="font-weight:bold; color:#fff;">₹${P}</span>
          </div>
          <div class="sim-slider-group">
            <span>Rate ($r\\%$):</span>
            <input type="range" id="rRange" min="5" max="20" step="1" value="${r}">
            <span style="font-weight:bold; color:#38bdf8;">${r}%</span>
          </div>
          <div class="sim-slider-group">
            <span>Years ($n$):</span>
            <input type="range" id="nRange" min="1" max="5" step="1" value="${n}">
            <span style="font-weight:bold; color:#fcd34d;">${n} yrs</span>
          </div>
        `;

        document.getElementById('pRange').oninput = (e) => {
          P = parseInt(e.target.value);
          update();
        };
        document.getElementById('rRange').oninput = (e) => {
          r = parseInt(e.target.value);
          update();
        };
        document.getElementById('nRange').oninput = (e) => {
          n = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 13: Asset Depreciation & Decay Curve
    // -------------------------------------------------------------
    function renderSim13(vp, controls, title, badge) {
      title.innerHTML = '<span>📉</span> Asset Depreciation Curve';
      badge.textContent = 'Wear & Value Loss Modeler';

      let V0 = 50000;
      let rate = 10;
      let years = 3;

      function update() {
        const Vn = V0 * Math.pow(1 - rate / 100, years);
        const lost = V0 - Vn;

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div>
                <span style="font-size:11px; color:#94a3b8;">Original Cost</span>
                <div style="font-size:18px; font-weight:bold; color:#fff;">₹${V0}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#fda4af;">Value Lost</span>
                <div style="font-size:18px; font-weight:bold; color:#f43f5e;">-₹${lost.toFixed(0)}</div>
              </div>
              <div>
                <span style="font-size:11px; color:#34d399;">Residual Value</span>
                <div style="font-size:18px; font-weight:bold; color:#38bdf8;">₹${Vn.toFixed(0)}</div>
              </div>
            </div>

            <!-- Step-down decay steps -->
            <div style="display:flex; gap:6px; justify-content:center; align-items:flex-end; height:90px; margin-bottom:12px;">
              ${Array.from({length: years + 1}, (_, yr) => {
                const val = V0 * Math.pow(1 - rate / 100, yr);
                const h = Math.max(14, (val / V0) * 80);
                return `
                  <div style="display:flex; flex-direction:column; align-items:center; gap:4px;">
                    <div style="width:36px; height:${h}px; background:#4f46e5; border-radius:4px 4px 0 0;"></div>
                    <span style="font-size:10px; color:#94a3b8;">Yr ${yr}</span>
                  </div>
                `;
              }).join('')}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              Depreciation Formula: $V_n = V_0\\left(1 - \\frac{r}{100}\\right)^n = ${V0}(1 - 0.${rate < 10 ? '0'+rate : rate})^${years} = \\mathbf{₹${Vn.toFixed(0)}}$
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div class="sim-slider-group">
            <span>Depreciation Rate:</span>
            <input type="range" id="depRate" min="5" max="25" step="1" value="${rate}">
            <span style="font-weight:bold; color:#f43f5e;">${rate}% / yr</span>
          </div>
          <div class="sim-slider-group">
            <span>Years Elapsed:</span>
            <input type="range" id="depYears" min="1" max="5" step="1" value="${years}">
            <span style="font-weight:bold; color:#38bdf8;">${years} years</span>
          </div>
        `;

        document.getElementById('depRate').oninput = (e) => {
          rate = parseInt(e.target.value);
          update();
        };
        document.getElementById('depYears').oninput = (e) => {
          years = parseInt(e.target.value);
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 14: Percentage Paradox Investigator
    // -------------------------------------------------------------
    function renderSim14(vp, controls, title, badge) {
      title.innerHTML = '<span>⚡</span> Percentage Paradox Investigator';
      badge.textContent = 'Reversibility & Asymmetric Base Trap';

      let mode = 'asymmetric'; // reversibility or asymmetric
      let pVal = 20;

      function update() {
        if (mode === 'asymmetric') {
          const afterUp = 100 * (1 + pVal / 100);
          const afterDown = afterUp * (1 - pVal / 100);
          const netLoss = (100 - afterDown).toFixed(2);

          vp.innerHTML = `
            <div style="width:100%; text-align:center;">
              <div style="font-size:14px; font-weight:bold; color:#fcd34d; margin-bottom:8px;">
                The Asymmetric Base Trap: +${pVal}% followed by -${pVal}%
              </div>
              <div style="display:flex; justify-content:space-around; align-items:center; margin-bottom:12px;">
                <div>
                  <div style="font-size:11px; color:#94a3b8;">Start Base</div>
                  <div style="font-size:18px; font-weight:bold; color:#fff;">100</div>
                </div>
                <div style="color:#10b981; font-size:13px; font-weight:bold;">+${pVal}% ➔</div>
                <div>
                  <div style="font-size:11px; color:#94a3b8;">After Increase</div>
                  <div style="font-size:18px; font-weight:bold; color:#34d399;">${afterUp}</div>
                </div>
                <div style="color:#f43f5e; font-size:13px; font-weight:bold;">-${pVal}% ➔</div>
                <div>
                  <div style="font-size:11px; color:#94a3b8;">Final Value</div>
                  <div style="font-size:18px; font-weight:bold; color:#fda4af;">${afterDown.toFixed(1)}</div>
                </div>
              </div>

              <div style="background:#0f172a; border:1px solid #f43f5e; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
                <strong>Paradox Revealed:</strong> You do NOT end at 100!
                <br>You suffer a net <strong>${netLoss}% loss</strong> because the 20% drop was applied to a <em>larger base</em> (${afterUp})!
                <br>Formula: Net Multiplier $= (1 + x)(1 - x) = 1 - x^2 = 1 - ${(pVal/100)**2}$.
              </div>
            </div>
          `;
        } else {
          // Reversibility
          const x = pVal;
          const y = 50;
          const ans = (x * y) / 100;
          vp.innerHTML = `
            <div style="width:100%; text-align:center;">
              <div style="font-size:14px; font-weight:bold; color:#38bdf8; margin-bottom:8px;">
                Reversibility Principle: $x\\% \\text{ of } y = y\\% \\text{ of } x$
              </div>
              <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
                <div style="background:#1e293b; border-radius:8px; padding:10px; border:1px solid #475569;">
                  <div style="font-size:12px; color:#a5b4fc;">${x}% of ${y}</div>
                  <div style="font-size:18px; font-weight:bold; color:#fff;">= ${ans}</div>
                </div>
                <div style="align-self:center; font-size:20px; color:#fcd34d;">≡</div>
                <div style="background:#1e293b; border-radius:8px; padding:10px; border:1px solid #475569;">
                  <div style="font-size:12px; color:#38bdf8;">${y}% of ${x} (Half of ${x})</div>
                  <div style="font-size:18px; font-weight:bold; color:#fff;">= ${ans}</div>
                </div>
              </div>
              <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
                Finding 16% of 50 is tricky in your head, but finding 50% (half) of 16 is instantly <strong>8</strong>!
              </div>
            </div>
          `;
        }

        controls.innerHTML = `
          <div style="display:flex; gap:8px; justify-content:center; margin-bottom:8px;">
            <button class="sim-btn ${mode==='asymmetric'?'active':''}" onclick="setParadoxMode('asymmetric')">Asymmetric Base Trap</button>
            <button class="sim-btn ${mode==='reversibility'?'active':''}" onclick="setParadoxMode('reversibility')">Reversibility Principle</button>
          </div>
          <div class="sim-slider-group">
            <span>Percentage Value:</span>
            <input type="range" id="paradoxRange" min="5" max="50" step="5" value="${pVal}">
            <span style="font-weight:bold; color:#38bdf8;">${pVal}%</span>
          </div>
        `;

        document.getElementById('paradoxRange').oninput = (e) => {
          pVal = parseInt(e.target.value);
          update();
        };

        window.setParadoxMode = (m) => {
          mode = m;
          update();
        };
        triggerMathRender(vp);
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 15: Base Blunder Debugger Matrix
    // -------------------------------------------------------------
    function renderSim15(vp, controls, title, badge) {
      title.innerHTML = '<span>🛠️</span> Base Blunder Debugger Matrix';
      badge.textContent = 'Common Traps & Formula Matrix';

      let activeTab = 0;
      const cases = [
        {
          title: 'The Selling Price Blunder',
          myth: 'Merchant made 20% profit on SP ₹1200, so CP = ₹1200 - 20% = ₹960?',
          debunk: 'NO! Profit is 20% of COST PRICE, not SP. SP is 120% of CP. So CP = 1200 / 1.2 = ₹1000!'
        },
        {
          title: 'Successive Discount Trap',
          myth: 'A store gives 20% off and an extra 20% off. Is that 40% discount?',
          debunk: 'NO! The second 20% applies to the remaining 80%. Multiplier: 0.8 × 0.8 = 0.64 ➔ Net discount is 36%!'
        },
        {
          title: 'Inclusive Tax Reversal',
          myth: 'A restaurant bill is ₹1180 including 18% GST. Is tax 18% of 1180?',
          debunk: 'NO! 1180 = 1.18 × Base. Base = 1180 / 1.18 = ₹1000. Tax is ₹180, NOT ₹212.40!'
        },
        {
          title: 'Restoring a Reduced Salary',
          myth: 'Salary was cut by 25%. To restore it, give a 25% raise?',
          debunk: 'NO! If ₹100 falls to ₹75, you need +₹25 on a base of ₹75. That requires a 33.33% raise!'
        }
      ];

      function update() {
        const c = cases[activeTab];
        vp.innerHTML = `
          <div style="width:100%; text-align:left;">
            <div style="font-size:14px; font-weight:bold; color:#fcd34d; margin-bottom:6px; border-bottom:1px solid #334155; padding-bottom:4px;">
              Case #${activeTab+1}: ${c.title}
            </div>
            <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:8px; padding:10px; margin-bottom:10px; font-size:12.5px; color:#fda4af;">
              <strong>⚠️ Common Blunder:</strong> ${c.myth}
            </div>
            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px; font-size:12.5px; color:#6ee7b7; line-height:1.5;">
              <strong>✓ Correct Mathematical Reality:</strong> ${c.debunk}
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">Select Case Study:</div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
            ${cases.map((cs, i) => `
              <button class="sim-btn ${activeTab===i?'active':''}" onclick="setCaseTab(${i})" style="font-size:11px; padding:6px 10px;">
                Case ${i+1}
              </button>
            `).join('')}
          </div>
        `;

        window.setCaseTab = (idx) => {
          activeTab = idx;
          update();
        };
      }
      update();
    }

    // -------------------------------------------------------------
    // Simulator 16: Peaceful Knights Chessboard Lab
    // -------------------------------------------------------------
    function renderSim16(vp, controls, title, badge) {
      title.innerHTML = '<span>♟️</span> Peaceful Knights Chessboard Lab';
      badge.textContent = '8×8 Bipartite Maximum Coverage';

      // 8x8 Board state (64 booleans)
      let board = new Array(64).fill(false);

      // Pre-set to 32 knights on light squares
      for (let i = 0; i < 64; i++) {
        const r = Math.floor(i / 8);
        const c = i % 8;
        if ((r + c) % 2 === 0) board[i] = true;
      }

      function getKnightMoves(r, c) {
        const deltas = [
          [-2, -1], [-2, 1], [-1, -2], [-1, 2],
          [1, -2], [1, 2], [2, -1], [2, 1]
        ];
        return deltas
          .map(([dr, dc]) => [r + dr, c + dc])
          .filter(([nr, nc]) => nr >= 0 && nr < 8 && nc >= 0 && nc < 8);
      }

      function checkConflicts() {
        const conflicts = new Set();
        for (let i = 0; i < 64; i++) {
          if (!board[i]) continue;
          const r = Math.floor(i / 8);
          const c = i % 8;
          const moves = getKnightMoves(r, c);
          for (let [nr, nc] of moves) {
            const targetIdx = nr * 8 + nc;
            if (board[targetIdx]) {
              conflicts.add(i);
              conflicts.add(targetIdx);
            }
          }
        }
        return conflicts;
      }

      function update() {
        const conflicts = checkConflicts();
        const knightCount = board.filter(Boolean).length;
        const coveragePct = ((knightCount / 64) * 100).toFixed(1);

        let squaresHtml = '';
        for (let i = 0; i < 64; i++) {
          const r = Math.floor(i / 8);
          const c = i % 8;
          const isLightSquare = (r + c) % 2 === 0;
          const hasKnight = board[i];
          const inConflict = conflicts.has(i);

          let bg = isLightSquare ? '#334155' : '#1e293b';
          if (inConflict) bg = '#ef4444';

          squaresHtml += `
            <div onclick="toggleKnight(${i})" style="width:30px; height:30px; background:${bg}; display:flex; align-items:center; justify-content:center; font-size:18px; cursor:pointer; user-select:none; transition:background 0.15s; border:${inConflict ? '1px solid #fecdd3' : 'none'};">
              ${hasKnight ? '♞' : ''}
            </div>
          `;
        }

        vp.innerHTML = `
          <div style="width:100%; text-align:center;">
            <div style="display:grid; grid-template-columns:repeat(8, 30px); gap:1px; justify-content:center; background:#0f172a; padding:4px; border:2px solid #6366f1; border-radius:6px; margin:0 auto 10px auto; width:fit-content;">
              ${squaresHtml}
            </div>

            <!-- Stats Bar -->
            <div style="display:flex; justify-content:space-around; background:#1e293b; border-radius:8px; padding:6px 12px; margin-bottom:8px; font-size:12px;">
              <div>Knights: <strong style="color:#fff;">${knightCount}/64</strong></div>
              <div>Conflicts: <strong style="color:${conflicts.size > 0 ? '#f43f5e' : '#10b981'};">${conflicts.size > 0 ? conflicts.size + ' Attack!' : '0 (Peaceful)'}</strong></div>
              <div>Coverage: <strong style="color:#38bdf8;">${coveragePct}%</strong></div>
            </div>

            <div style="font-size:11.5px; color:#94a3b8; line-height:1.4;">
              Every knight move changes square colour (Light ↔ Dark). By placing all knights on the same colour, <strong>no two knights can ever attack each other</strong>! Maximum = 32 knights (50%).
            </div>
          </div>
        `;

        controls.innerHTML = `
          <div style="display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
            <button class="sim-btn" onclick="solveKnights('light')">Solve: 32 Light Squares (50%)</button>
            <button class="sim-btn" onclick="solveKnights('dark')">Solve: 32 Dark Squares (50%)</button>
            <button class="sim-btn" onclick="clearKnights()" style="background:#475569;">Clear Board</button>
          </div>
        `;

        window.toggleKnight = (idx) => {
          board[idx] = !board[idx];
          update();
        };

        window.solveKnights = (type) => {
          board = new Array(64).fill(false);
          for (let i = 0; i < 64; i++) {
            const r = Math.floor(i / 8);
            const c = i % 8;
            if (type === 'light' && (r + c) % 2 === 0) board[i] = true;
            if (type === 'dark' && (r + c) % 2 !== 0) board[i] = true;
          }
          update();
        };

        window.clearKnights = () => {
          board = new Array(64).fill(false);
          update();
        };
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
    
    # Save template file as well
    template_path = os.path.join(os.path.dirname(__file__), "template_class8_math_percentages_applications.html")
    with open(template_path, "w", encoding="utf-8") as tf:
        tf.write(TEMPLATE)
    print(f"Saved template: {template_path}")

    # Generate public animation HTML
    output_path = os.path.join(os.path.dirname(__file__), "..", "public", "animations", "class8-math-percentages-applications.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Generated {output_path} ({len(html_output)} bytes)")
