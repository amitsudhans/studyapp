# Class 8 Science Chapter 3: Health, Diseases, and Prevention
# Master Builder Script: Compiles 20-slide animated lab into public/animations/class8-science-health-disease.html

import json
import sys
sys.path.insert(0, '.agents')
from class8_science_health_disease_data import SLIDES_DATA, QUIZ_QUESTIONS

# Assemble full slides data
full_slides = []
for slide in SLIDES_DATA:
    s = dict(slide)
    if s.get("is_quiz_slide"):
        q_range = s.get("quiz_range", "1–10")
        if q_range == "1–10":
            s["questions"] = QUIZ_QUESTIONS[0:10]
        elif q_range == "11–20":
            s["questions"] = QUIZ_QUESTIONS[10:20]
        elif q_range == "21–30":
            s["questions"] = QUIZ_QUESTIONS[20:30]
        elif q_range == "31–40":
            s["questions"] = QUIZ_QUESTIONS[30:40]
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Science • Chapter 3: Health, Diseases & Prevention Master Lab</title>
  
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
      --bg-primary: #070d18;
      --bg-secondary: #0f172a;
      --card-bg: rgba(15, 23, 42, 0.88);
      --card-border: rgba(6, 182, 212, 0.25);
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
      --accent-blue: #3b82f6;
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
      background: radial-gradient(circle at top right, #083344 0%, #070d18 70%);
      color: var(--text-main);
      font-family: var(--font-stack);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    header {
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .brand-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: linear-gradient(135deg, #06b6d4, #3b82f6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
    }

    .brand-title {
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(to right, #67e8f9, #93c5fd);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-main);
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
      user-select: none;
    }

    .btn:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.14);
      border-color: var(--accent-cyan);
      transform: translateY(-1px);
    }

    .btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .btn-primary {
      background: linear-gradient(135deg, #0891b2, #2563eb);
      border-color: #06b6d4;
    }

    .btn-primary:hover:not(:disabled) {
      box-shadow: 0 0 16px rgba(6, 182, 212, 0.4);
    }

    .slide-badge {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.12);
      border: 1px solid rgba(6, 182, 212, 0.3);
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      letter-spacing: 0.03em;
    }

    main {
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    /* Lesson Grid Layout */
    .lesson-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 1.5rem;
      align-items: start;
    }

    @media (max-width: 1024px) {
      .lesson-grid {
        grid-template-columns: 1fr;
      }
    }

    .panel {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
      position: relative;
      overflow: hidden;
    }

    .panel-header {
      margin-bottom: 1.25rem;
    }

    .panel-tag {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 0.25rem;
      display: block;
    }

    .panel-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.25;
    }

    .panel-sub {
      font-size: 0.9rem;
      color: #94a3b8;
      margin-top: 0.35rem;
    }

    /* Avatar & Narration Box */
    .avatar-card {
      background: rgba(6, 182, 212, 0.08);
      border: 1px solid rgba(6, 182, 212, 0.25);
      border-radius: 14px;
      padding: 1rem;
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }

    .avatar-wrapper {
      position: relative;
      width: 52px;
      height: 52px;
      flex-shrink: 0;
    }

    .avatar-face {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: linear-gradient(135deg, #0e7490, #1d4ed8);
      border: 2px solid var(--accent-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.4);
    }

    .avatar-speaking {
      animation: pulseAvatar 1.4s infinite alternate;
    }

    @keyframes pulseAvatar {
      from { transform: scale(1); box-shadow: 0 0 8px rgba(6, 182, 212, 0.4); }
      to { transform: scale(1.08); box-shadow: 0 0 20px rgba(59, 130, 246, 0.8); }
    }

    .voice-control-btn {
      background: rgba(6, 182, 212, 0.2);
      border: 1px solid var(--accent-cyan);
      color: #fff;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      margin-top: 0.5rem;
      transition: all 0.2s ease;
    }

    .voice-control-btn:hover {
      background: var(--accent-cyan);
      color: #070d18;
    }

    /* Key points / Takeaways */
    .takeaway-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-top: 1rem;
    }

    .takeaway-list li {
      position: relative;
      padding-left: 1.6rem;
      font-size: 0.85rem;
      line-height: 1.5;
      color: #e2e8f0;
    }

    .takeaway-list li::before {
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--accent-emerald);
      font-weight: bold;
    }

    /* In-Slide Checkpoints */
    .checkpoint-box {
      margin-top: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .checkpoint-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
    }

    .checkpoint-title {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-amber);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .checkpoint-item {
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 0.85rem;
      margin-bottom: 0.75rem;
    }

    .checkpoint-q {
      font-size: 0.85rem;
      font-weight: 600;
      color: #f1f5f9;
      margin-bottom: 0.6rem;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.4rem;
    }

    .cp-opt-btn {
      text-align: left;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      padding: 0.45rem 0.75rem;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .cp-opt-btn:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.09);
      border-color: var(--accent-cyan);
    }

    .cp-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 600;
    }

    .cp-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .cp-feedback {
      margin-top: 0.5rem;
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      font-size: 0.75rem;
      line-height: 1.4;
      display: none;
    }

    .cp-feedback.show-correct {
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }

    .cp-feedback.show-incorrect {
      display: block;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fda4af;
    }

    /* Simulator Panel */
    .sim-panel {
      background: #090e1a;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      min-height: 540px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }

    .sim-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.75rem;
      margin-bottom: 0.75rem;
    }

    .sim-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-cyan);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .sim-stats {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .stat-pill {
      font-size: 0.75rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      color: #cbd5e1;
    }

    .stat-pill strong {
      color: var(--accent-cyan);
    }

    .sim-canvas-wrapper {
      flex: 1;
      min-height: 380px;
      background: #040711;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .sim-controls {
      margin-top: 0.85rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      align-items: center;
    }

    .sim-ctrl-group {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.75rem;
      color: #94a3b8;
    }

    .sim-slider {
      accent-color: var(--accent-cyan);
      cursor: pointer;
    }

    /* Quiz Slides (17 to 20) */
    .quiz-container {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      max-width: 1000px;
      margin: 0 auto;
      width: 100%;
    }

    .quiz-card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 1.25rem;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
      transition: all 0.2s ease;
    }

    .quiz-card:hover {
      border-color: rgba(6, 182, 212, 0.3);
    }

    .quiz-q-num {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }

    .quiz-q-text {
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 0.85rem;
      line-height: 1.45;
    }

    .quiz-opts {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }

    @media (min-width: 640px) {
      .quiz-opts {
        grid-template-columns: 1fr 1fr;
      }
    }

    .quiz-opt-btn {
      text-align: left;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      padding: 0.6rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(255, 255, 255, 0.09);
      border-color: var(--accent-cyan);
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 600;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .quiz-btn-solution {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      padding: 0.4rem 0.85rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }

    .quiz-btn-solution:hover {
      background: rgba(245, 158, 11, 0.3);
      border-color: #f59e0b;
    }

    /* Solution Modal */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-card {
      background: #0b1329;
      border: 1px solid var(--accent-amber);
      border-radius: 16px;
      max-width: 650px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.75rem;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
      position: relative;
    }

    .modal-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.5rem;
    }

    .modal-close-btn {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
    }

    .modal-close-btn:hover {
      background: rgba(244, 63, 94, 0.5);
    }

    .modal-solution-text {
      font-size: 0.9rem;
      line-height: 1.6;
      color: #e2e8f0;
      white-space: pre-line;
      margin-top: 1rem;
      background: rgba(0, 0, 0, 0.3);
      padding: 1rem;
      border-radius: 10px;
      border-left: 3px solid var(--accent-amber);
    }

    /* Terminal Slide Banner */
    .last-slide-banner {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15));
      border: 1px solid var(--accent-emerald);
      border-radius: 12px;
      padding: 1.25rem;
      text-align: center;
      display: none;
      margin-top: 1.5rem;
    }

    .last-slide-banner h3 {
      color: #6ee7b7;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
    }

    .last-slide-banner p {
      color: #cbd5e1;
      font-size: 0.85rem;
    }

    /* Footer Navigation */
    footer {
      background: rgba(15, 23, 42, 0.9);
      border-top: 1px solid var(--card-border);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(10px);
    }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <header>
    <div class="brand">
      <div class="brand-icon">🩺</div>
      <div>
        <div class="brand-title">Class 8 Science • Chapter 3: Health, Diseases & Prevention</div>
        <div class="brand-sub">NCERT Interactive Laboratory & Animated Concept Studio</div>
      </div>
    </div>
    <div class="nav-controls">
      <span class="slide-badge" id="slideNumDisplay">Slide 1 of 20</span>
      <button class="btn" id="prevBtn" onclick="prevSlide()" disabled>← Previous</button>
      <button class="btn btn-primary" id="nextBtn" onclick="nextSlide()">Next →</button>
    </div>
  </header>

  <!-- Main Slide Container -->
  <main>
    <!-- Lesson Grid (Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      <!-- Left Column: Theory & Narrative -->
      <div class="panel">
        <div class="panel-header">
          <span class="panel-tag" id="slideBadgeTag">Holistic Wellness</span>
          <h1 class="panel-title" id="slideHeading">Defining True Health</h1>
          <div class="panel-sub" id="slideSubheading">WHO Definition: Beyond the Mere Absence of Disease</div>
        </div>

        <!-- Teacher Voice Avatar -->
        <div class="avatar-card">
          <div class="avatar-wrapper">
            <div class="avatar-face" id="teacherAvatar">👩‍⚕️</div>
          </div>
          <div>
            <div style="font-size: 0.85rem; font-weight: 700; color: var(--accent-cyan);">Dr. Meera • Public Health Mentor</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.2rem;" id="narrationSummary">
              Explore the holistic dimensions of health, disease prevention, vaccines, and medical breakthroughs.
            </p>
            <button class="voice-control-btn" id="voiceToggleBtn" onclick="toggleVoice()">
              <span id="voiceIcon">🔊</span> <span id="voiceBtnText">Listen to Teacher Explanation</span>
            </button>
          </div>
        </div>

        <!-- Core Theory Text -->
        <div id="theoryContent"></div>

        <!-- Key Takeaways -->
        <div style="margin-top: 1.25rem;">
          <h4 style="font-size: 0.85rem; font-weight: 700; color: var(--accent-emerald); text-transform: uppercase; letter-spacing: 0.05em;">
            Key Scientific Takeaways
          </h4>
          <ul class="takeaway-list" id="keyTakeawaysList"></ul>
        </div>

        <!-- In-Slide Checkpoints (2 Questions with Solutions) -->
        <div class="checkpoint-box" id="checkpointContainer">
          <div class="checkpoint-header">
            <div class="checkpoint-title">⚡ Checkpoint Inquiries (2 Concept Checks)</div>
          </div>
          <div id="checkpointsList"></div>
        </div>
      </div>

      <!-- Right Column: Interactive Bespoke Simulator -->
      <div class="sim-panel">
        <div class="sim-header">
          <div class="sim-title" id="simTitle">🩺 Health & Wellness Simulator</div>
          <div class="sim-stats" id="simStats"></div>
        </div>
        <div class="sim-canvas-wrapper" id="simCanvas"></div>
        <div class="sim-controls" id="simControls"></div>
      </div>
    </div>

    <!-- Quiz Container (Slides 17 to 20) -->
    <div class="quiz-container" id="quizContainer" style="display: none;">
      <div class="panel">
        <div class="panel-header" style="text-align: center;">
          <span class="panel-tag" style="color: var(--accent-amber);">Mastery Assessment Series</span>
          <h1 class="panel-title" id="quizTitle">Mastery Challenge</h1>
          <div class="panel-sub" id="quizSubtitle">Answer all 10 questions to test your conceptual clarity.</div>
          <div style="margin-top: 0.75rem;">
            <span class="slide-badge" style="background: rgba(245, 158, 11, 0.15); border-color: #f59e0b; color: #fbbf24;" id="quizScoreBadge">
              Score: 0 / 10
            </span>
          </div>
        </div>
        <div id="quizQuestionsGrid" style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1rem;"></div>
      </div>
    </div>

    <!-- Terminal Slide Notice -->
    <div class="last-slide-banner" id="lastSlideNotice" style="display: none;">
      <h3>🎉 You have reached the last slide of this chapter!</h3>
      <p>Congratulations! You have mastered NCERT Class 8 Science Chapter 3: Health, Diseases, and Prevention.</p>
    </div>
  </main>

  <!-- Footer Navigation -->
  <footer>
    <div style="font-size: 0.8rem; color: #64748b;">
      Class 8 Science • Chapter 3 • Health, Diseases & Prevention Master Laboratory
    </div>
    <div class="nav-controls">
      <button class="btn" onclick="prevSlide()">← Back</button>
      <button class="btn btn-primary" id="footerNextBtn" onclick="nextSlide()">Continue Next →</button>
    </div>
  </footer>

  <!-- Pop-Up Solution Modal -->
  <div class="modal-backdrop" id="solutionModal" style="display: none;">
    <div class="modal-card">
      <button class="modal-close-btn" onclick="closeSolutionModal()">✕</button>
      <div class="modal-title">
        <span>💡</span> Step-by-Step Scientific Solution
      </div>
      <div id="modalQuestionText" style="font-size: 0.95rem; font-weight: 600; color: #fff; margin-bottom: 0.5rem;"></div>
      <div class="modal-solution-text" id="modalSolutionBody"></div>
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
        // Content Slide
        lessonGrid.style.display = 'grid';
        quizContainer.style.display = 'none';

        document.getElementById('slideBadgeTag').textContent = slide.badge || "Scientific Concept";
        document.getElementById('slideHeading').textContent = slide.title;
        document.getElementById('slideSubheading').textContent = slide.subtitle;
        document.getElementById('theoryContent').innerHTML = slide.theory;
        document.getElementById('narrationSummary').textContent = slide.narration.substring(0, 160) + '...';

        const takeaways = document.getElementById('keyTakeawaysList');
        takeaways.innerHTML = '';
        (slide.key_points || []).forEach(pt => {
          const li = document.createElement('li');
          li.textContent = pt;
          takeaways.appendChild(li);
        });

        renderCheckpoints(slide.checkpoints);
        renderSimulator(slide.sim_id);
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

    // In-Slide Checkpoints Renderer
    function renderCheckpoints(checkpoints) {
      const list = document.getElementById('checkpointsList');
      list.innerHTML = '';

      if (!checkpoints || checkpoints.length === 0) {
        document.getElementById('checkpointContainer').style.display = 'none';
        return;
      }
      document.getElementById('checkpointContainer').style.display = 'block';

      checkpoints.forEach((cp, cpIdx) => {
        const item = document.createElement('div');
        item.className = 'checkpoint-item';

        const qText = document.createElement('div');
        qText.className = 'checkpoint-q';
        qText.innerHTML = `<strong>Q${cpIdx + 1}:</strong> ${cp.question}`;
        item.appendChild(qText);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'checkpoint-options';

        const fbDiv = document.createElement('div');
        fbDiv.className = 'cp-feedback';

        cp.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'cp-opt-btn';
          btn.innerHTML = optText;

          btn.onclick = () => {
            const allBtns = optsDiv.querySelectorAll('.cp-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('correct');
              fbDiv.className = 'cp-feedback show-correct';
              fbDiv.innerHTML = `<strong>✔ Correct!</strong> ${cp.explanation}`;
            } else {
              btn.classList.add('incorrect');
              allBtns[cp.correct].classList.add('correct');
              fbDiv.className = 'cp-feedback show-incorrect';
              fbDiv.innerHTML = `<strong>✖ Not quite.</strong> ${cp.explanation}`;
            }
          };

          optsDiv.appendChild(btn);
        });

        item.appendChild(optsDiv);
        item.appendChild(fbDiv);
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
        solBtn.innerHTML = '💡 View Step-by-Step Solution';
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
            solBtn.style.display = 'inline-flex';
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
            solBtn.style.display = 'inline-flex';
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
      const utterText = `${slide.title}. ${slide.subtitle}. ${slide.narration}`;

      const utter = new SpeechSynthesisUtterance(utterText);
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
      const text = document.getElementById('voiceBtnText');
      const face = document.getElementById('teacherAvatar');

      if (isSpeaking) {
        icon.textContent = '⏹';
        text.textContent = 'Stop Narration';
        btn.style.background = '#e11d48';
        face.classList.add('avatar-speaking');
      } else {
        icon.textContent = '🔊';
        text.textContent = 'Listen to Teacher Explanation';
        btn.style.background = 'rgba(6, 182, 212, 0.2)';
        face.classList.remove('avatar-speaking');
      }
    }

    // Simulator Dispatcher
    function renderSimulator(simType) {
      const title = document.getElementById('simTitle');
      const stats = document.getElementById('simStats');
      const canvas = document.getElementById('simCanvas');
      const controls = document.getElementById('simControls');

      canvas.innerHTML = '';
      controls.innerHTML = '';
      stats.innerHTML = '';

      switch (simType) {
        case 'who_triad_health_sim':
          renderWhoTriadHealthSim(title, stats, canvas, controls);
          break;
        case 'ayurveda_dinacharya_clock_sim':
          renderAyurvedaClockSim(title, stats, canvas, controls);
          break;
        case 'lifestyle_balance_meter_sim':
          renderLifestyleBalanceMeterSim(title, stats, canvas, controls);
          break;
        case 'aqi_environmental_health_sim':
          renderAqiEnvironmentalHealthSim(title, stats, canvas, controls);
          break;
        case 'symptoms_vs_signs_clinician_sim':
          renderSymptomsVsSignsSim(title, stats, canvas, controls);
          break;
        case 'disease_classification_tree_sim':
          renderDiseaseClassificationTreeSim(title, stats, canvas, controls);
          break;
        case 'pathogen_gallery_communicable_sim':
          renderPathogenGallerySim(title, stats, canvas, controls);
          break;
        case 'ncd_deficiency_disease_lab_sim':
          renderNcdDeficiencyLabSim(title, stats, canvas, controls);
          break;
        case 'transmission_routes_epidemic_sim':
          renderTransmissionRoutesSim(title, stats, canvas, controls);
          break;
        case 'sanitation_barrier_hygiene_sim':
          renderSanitationBarrierSim(title, stats, canvas, controls);
          break;
        case 'immune_system_patrol_sim':
          renderImmuneSystemPatrolSim(title, stats, canvas, controls);
          break;
        case 'vaccine_mechanism_trainer_sim':
          renderVaccineMechanismSim(title, stats, canvas, controls);
          break;
        case 'vaccine_milestones_india_sim':
          renderVaccineMilestonesIndiaSim(title, stats, canvas, controls);
          break;
        case 'fleming_penicillin_petri_sim':
          renderFlemingPenicillinSim(title, stats, canvas, controls);
          break;
        case 'antibiotic_resistance_superbug_sim':
          renderAntibioticResistanceSim(title, stats, canvas, controls);
          break;
        case 'health_disease_master_matrix_sim':
          renderHealthDiseaseMasterMatrixSim(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Laboratory Visualizer';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. WHO Triad Health Simulator
    function renderWhoTriadHealthSim(title, stats, canvas, controls) {
      title.textContent = "WHO Holistic Health Triangle: 3 Pillars";
      let phys = 90;
      let ment = 85;
      let soc = 80;

      function update() {
        const total = Math.round((phys + ment + soc) / 3);
        stats.innerHTML = `
          <div class="stat-pill">Physical: <strong>${phys}%</strong></div>
          <div class="stat-pill">Mental: <strong>${ment}%</strong></div>
          <div class="stat-pill">Social: <strong>${soc}%</strong></div>
          <div class="stat-pill">Holistic Health: <strong style="color:${total > 75 ? '#10b981' : '#f59e0b'}">${total}%</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
            <svg width="360" height="280" viewBox="0 0 360 280">
              <!-- Outer reference triangle -->
              <polygon points="180,30 50,230 310,230" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2" stroke-dasharray="4,4"/>
              
              <!-- Dynamic user health polygon -->
              <polygon points="180,${30 + (100 - ment) * 0.8} ${50 + (100 - phys) * 0.7},${230 - (100 - phys) * 0.4} ${310 - (100 - soc) * 0.7},${230 - (100 - soc) * 0.4}" fill="rgba(6, 182, 212, 0.35)" stroke="#06b6d4" stroke-width="3"/>
              
              <!-- Vertex Labels -->
              <circle cx="180" cy="30" r="14" fill="#a855f7"/>
              <text x="180" y="34" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">🧠</text>
              <text x="180" y="15" text-anchor="middle" fill="#c084fc" font-size="10" font-weight="700">Mental (${ment}%)</text>

              <circle cx="50" cy="230" r="14" fill="#10b981"/>
              <text x="50" y="234" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">💪</text>
              <text x="50" y="255" text-anchor="middle" fill="#6ee7b7" font-size="10" font-weight="700">Physical (${phys}%)</text>

              <circle cx="310" cy="230" r="14" fill="#3b82f6"/>
              <text x="310" y="234" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">🤝</text>
              <text x="310" y="255" text-anchor="middle" fill="#93c5fd" font-size="10" font-weight="700">Social (${soc}%)</text>

              <text x="180" y="150" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">${total}%</text>
              <text x="180" y="170" text-anchor="middle" fill="#cbd5e1" font-size="9">Well-being Score</text>
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Physical:</span>
          <input type="range" class="sim-slider" id="slPhys" min="30" max="100" value="${phys}" style="width:70px;">
        </div>
        <div class="sim-ctrl-group">
          <span>Mental:</span>
          <input type="range" class="sim-slider" id="slMent" min="30" max="100" value="${ment}" style="width:70px;">
        </div>
        <div class="sim-ctrl-group">
          <span>Social:</span>
          <input type="range" class="sim-slider" id="slSoc" min="30" max="100" value="${soc}" style="width:70px;">
        </div>
      `;

      controls.querySelector('#slPhys').oninput = (e) => { phys = parseInt(e.target.value); update(); };
      controls.querySelector('#slMent').oninput = (e) => { ment = parseInt(e.target.value); update(); };
      controls.querySelector('#slSoc').oninput = (e) => { soc = parseInt(e.target.value); update(); };

      update();
    }

    // 2. Ayurveda Dinacharya & Ritucharya Simulator
    function renderAyurvedaClockSim(title, stats, canvas, controls) {
      title.textContent = "Ayurvedic 24-Hour Biological Rhythm Clock";
      let hour = 6; // 6 AM

      const routineMap = {
        4: { time: "4:30 AM", phase: "Brahma Muhurta", act: "Wake before dawn, prayer, deep meditation, clear mind." },
        6: { time: "6:00 AM", phase: "Shaucha & Vyayama", act: "Oral hygiene, tongue cleaning, oil pulling, warm water, morning walk." },
        8: { time: "8:00 AM", phase: "Yoga & Pranayama", act: "Surya Namaskar, breath regulation, mindful energizing." },
        12: { time: "12:30 PM", phase: "Madhyahna (Peak Agni)", act: "Primary balanced meal tailored to body constitution (Prakriti)." },
        18: { time: "6:30 PM", phase: "Sandhya (Evening Calm)", act: "Light wholesome dinner, family conversation, relaxing walk." },
        22: { time: "10:00 PM", phase: "Nidra (Restorative Sleep)", act: "Unplug screens, calm darkness, 8 hours deep tissue cellular recovery." }
      };

      function update() {
        const cur = routineMap[hour] || routineMap[6];
        stats.innerHTML = `
          <div class="stat-pill">Time: <strong>${cur.time}</strong></div>
          <div class="stat-pill">Cycle: <strong>${cur.phase}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1rem; text-align:center;">
            <svg width="220" height="220" viewBox="0 0 220 220">
              <circle cx="110" cy="110" r="95" fill="#0f172a" stroke="#d97706" stroke-width="4"/>
              
              <!-- 6 hour ticks -->
              <circle cx="110" cy="25" r="10" fill="${hour === 4 ? '#f59e0b' : '#334155'}"/>
              <text x="110" y="29" text-anchor="middle" fill="#fff" font-size="8">4AM</text>

              <circle cx="170" cy="60" r="10" fill="${hour === 6 ? '#f59e0b' : '#334155'}"/>
              <text x="170" y="64" text-anchor="middle" fill="#fff" font-size="8">6AM</text>

              <circle cx="195" cy="110" r="10" fill="${hour === 8 ? '#f59e0b' : '#334155'}"/>
              <text x="195" y="114" text-anchor="middle" fill="#fff" font-size="8">8AM</text>

              <circle cx="110" cy="195" r="10" fill="${hour === 12 ? '#f59e0b' : '#334155'}"/>
              <text x="110" y="199" text-anchor="middle" fill="#fff" font-size="8">12PM</text>

              <circle cx="25" cy="110" r="10" fill="${hour === 18 ? '#f59e0b' : '#334155'}"/>
              <text x="25" y="114" text-anchor="middle" fill="#fff" font-size="8">6PM</text>

              <circle cx="50" cy="60" r="10" fill="${hour === 22 ? '#f59e0b' : '#334155'}"/>
              <text x="50" y="64" text-anchor="middle" fill="#fff" font-size="8">10PM</text>

              <!-- Center hub -->
              <circle cx="110" cy="110" r="38" fill="#18181b" stroke="#f59e0b" stroke-width="2"/>
              <text x="110" y="108" text-anchor="middle" fill="#fde047" font-size="11" font-weight="700">Dinacharya</text>
              <text x="110" y="122" text-anchor="middle" fill="#94a3b8" font-size="8">Routines</text>
            </svg>
            <h4 style="color:#fbbf24; margin-top:0.5rem; font-size:1rem;">${cur.phase} (${cur.time})</h4>
            <p style="font-size:0.8rem; color:#cbd5e1; max-width:380px;">${cur.act}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="h4">4:30 AM</button>
        <button class="btn btn-primary" id="h6">6:00 AM</button>
        <button class="btn" id="h8">8:00 AM</button>
        <button class="btn" id="h12">12:30 PM</button>
        <button class="btn" id="h18">6:30 PM</button>
        <button class="btn" id="h22">10:00 PM</button>
      `;

      controls.querySelector('#h4').onclick = () => { hour = 4; update(); };
      controls.querySelector('#h6').onclick = () => { hour = 6; update(); };
      controls.querySelector('#h8').onclick = () => { hour = 8; update(); };
      controls.querySelector('#h12').onclick = () => { hour = 12; update(); };
      controls.querySelector('#h18').onclick = () => { hour = 18; update(); };
      controls.querySelector('#h22').onclick = () => { hour = 22; update(); };

      update();
    }

    // 3. Lifestyle Balance Meter Simulator
    function renderLifestyleBalanceMeterSim(title, stats, canvas, controls) {
      title.textContent = "Lifestyle Health Dashboard & Risk Analyzer";
      let exercise = 60; // mins
      let screen = 2; // hours
      let noSubstances = true;

      function update() {
        const score = Math.min(100, Math.round((exercise / 60) * 40 + (screen <= 2 ? 30 : Math.max(0, 30 - (screen - 2) * 8)) + (noSubstances ? 30 : 0)));
        stats.innerHTML = `
          <div class="stat-pill">Activity: <strong>${exercise} mins</strong></div>
          <div class="stat-pill">Screen Time: <strong>${screen} hrs</strong></div>
          <div class="stat-pill">Toxins: <strong>${noSubstances ? 'Strictly Rejected' : 'Danger Present'}</strong></div>
          <div class="stat-pill">Lifestyle Vitality: <strong style="color:${score > 75 ? '#10b981' : '#f43f5e'}">${score}%</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <svg width="340" height="220" viewBox="0 0 340 220">
              <circle cx="170" cy="130" r="80" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="16"/>
              <circle cx="170" cy="130" r="80" fill="none" stroke="${score > 75 ? '#10b981' : score > 50 ? '#f59e0b' : '#f43f5e'}" stroke-width="16" stroke-dasharray="502" stroke-dashoffset="${502 - (score / 100) * 251}" transform="rotate(-180, 170, 130)"/>
              
              <text x="170" y="125" text-anchor="middle" fill="#fff" font-size="32" font-weight="800">${score}%</text>
              <text x="170" y="150" text-anchor="middle" fill="#94a3b8" font-size="11">Habit Vitality Index</text>
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Exercise (mins):</span>
          <input type="range" class="sim-slider" id="exSl" min="10" max="90" value="${exercise}" style="width:70px;">
        </div>
        <div class="sim-ctrl-group">
          <span>Screen Time (hrs):</span>
          <input type="range" class="sim-slider" id="scSl" min="1" max="8" value="${screen}" style="width:70px;">
        </div>
        <button class="btn ${noSubstances ? 'btn-primary' : ''}" id="toxBtn">${noSubstances ? '🚫 Firm NO to Tobacco/Drugs' : '⚠️ Substances Consumed'}</button>
      `;

      controls.querySelector('#exSl').oninput = (e) => { exercise = parseInt(e.target.value); update(); };
      controls.querySelector('#scSl').oninput = (e) => { screen = parseInt(e.target.value); update(); };
      controls.querySelector('#toxBtn').onclick = () => { noSubstances = !noSubstances; update(); };

      update();
    }

    // 4. AQI & Environmental Health Simulator
    function renderAqiEnvironmentalHealthSim(title, stats, canvas, controls) {
      title.textContent = "Air Quality Index (AQI) & Respiratory Health";
      let aqi = 45; // Good

      function update() {
        const cat = aqi <= 50 ? { label: "Good (0–50)", color: "#10b981", effect: "Air quality satisfactory, minimal health risk." }
                  : aqi <= 100 ? { label: "Moderate (51–100)", color: "#f59e0b", effect: "Acceptable; sensitive individuals may cough." }
                  : aqi <= 200 ? { label: "Poor (101–200)", color: "#f97316", effect: "Breathing discomfort to people with lung/heart disease." }
                  : { label: "Severe (>200)", color: "#f43f5e", effect: "Health emergency! Respiratory illness to general public." };

        stats.innerHTML = `
          <div class="stat-pill">AQI Level: <strong style="color:${cat.color}">${aqi}</strong></div>
          <div class="stat-pill">Category: <strong>${cat.label}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
            <svg width="340" height="180" viewBox="0 0 340 180">
              <!-- AQI Gauge arc -->
              <path d="M 50 140 A 120 120 0 0 1 290 140" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="18"/>
              <path d="M 50 140 A 120 120 0 0 1 290 140" fill="none" stroke="${cat.color}" stroke-width="18" stroke-dasharray="377" stroke-dashoffset="${377 - (aqi / 350) * 377}"/>
              
              <text x="170" y="125" text-anchor="middle" fill="#fff" font-size="28" font-weight="800">AQI ${aqi}</text>
              <text x="170" y="148" text-anchor="middle" fill="${cat.color}" font-size="12" font-weight="700">${cat.label}</text>
            </svg>
            <p style="font-size:0.85rem; color:#cbd5e1; max-width:380px;">${cat.effect}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="aGood">Clean Air (45)</button>
        <button class="btn" id="aMod">Moderate (85)</button>
        <button class="btn" id="aPoor">Poor (160)</button>
        <button class="btn" id="aSev">Severe Smog (320)</button>
      `;

      controls.querySelector('#aGood').onclick = () => { aqi = 45; update(); };
      controls.querySelector('#aMod').onclick = () => { aqi = 85; update(); };
      controls.querySelector('#aPoor').onclick = () => { aqi = 160; update(); };
      controls.querySelector('#aSev').onclick = () => { aqi = 320; update(); };

      update();
    }

    // 5. Symptoms vs Signs Clinical Simulator
    function renderSymptomsVsSignsSim(title, stats, canvas, controls) {
      title.textContent = "Clinical Diagnosis: Symptoms vs Signs";

      stats.innerHTML = `
        <div class="stat-pill">Patient: <strong>Subjective Symptoms</strong></div>
        <div class="stat-pill">Doctor: <strong>Objective Measurable Signs</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 280">
          <!-- Patient Box (Symptoms) -->
          <g transform="translate(30, 40)">
            <rect width="185" height="190" rx="12" fill="#18181b" stroke="#f59e0b" stroke-width="2"/>
            <text x="92" y="30" text-anchor="middle" fill="#fde047" font-size="12" font-weight="700">Symptoms (Patient Feels)</text>
            <text x="20" y="70" fill="#cbd5e1" font-size="11">• "My head throbs with pain"</text>
            <text x="20" y="100" fill="#cbd5e1" font-size="11">• "I feel dizzy & nauseous"</text>
            <text x="20" y="130" fill="#cbd5e1" font-size="11">• "Extreme fatigue & chills"</text>
            <text x="92" y="170" text-anchor="middle" fill="#94a3b8" font-size="9">Subjective Experiences</text>
          </g>

          <!-- Doctor Box (Signs) -->
          <g transform="translate(245, 40)">
            <rect width="185" height="190" rx="12" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
            <text x="92" y="30" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="700">Signs (Doctor Measures)</text>
            <text x="20" y="70" fill="#cbd5e1" font-size="11">• Temp: 102.5°F (Thermometer)</text>
            <text x="20" y="100" fill="#cbd5e1" font-size="11">• BP: 140/90 mmHg (Cuff)</text>
            <text x="20" y="130" fill="#cbd5e1" font-size="11">• Red erythematous skin rash</text>
            <text x="92" y="170" text-anchor="middle" fill="#94a3b8" font-size="9">Objective Clinical Tests</text>
          </g>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Symptoms are subjective internal feelings reported by the patient; signs are objective indicators tested and verified by medical tools.
        </div>
      `;
    }

    // 6. Disease Classification Tree Simulator
    function renderDiseaseClassificationTreeSim(title, stats, canvas, controls) {
      title.textContent = "Classification: Communicable vs Non-Communicable";

      stats.innerHTML = `
        <div class="stat-pill">Infectious: <strong>Pathogen Transmission</strong></div>
        <div class="stat-pill">NCDs: <strong>Lifestyle, Genetics, Aging</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 280">
          <!-- Root -->
          <rect x="170" y="20" width="120" height="35" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
          <text x="230" y="42" text-anchor="middle" fill="#e9d5ff" font-size="11" font-weight="700">DISEASES</text>

          <!-- Lines -->
          <line x1="230" y1="55" x2="110" y2="100" stroke="#64748b" stroke-width="2"/>
          <line x1="230" y1="55" x2="350" y2="100" stroke="#64748b" stroke-width="2"/>

          <!-- Branch 1: Communicable -->
          <rect x="30" y="100" width="160" height="130" rx="10" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="2"/>
          <text x="110" y="125" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">Communicable (Infectious)</text>
          <text x="45" y="150" fill="#cbd5e1" font-size="10">• Caused by pathogens</text>
          <text x="45" y="170" fill="#cbd5e1" font-size="10">• Spreads person-to-person</text>
          <text x="45" y="195" fill="#a5f3fc" font-size="9">TB, Flu, Cholera, Dengue</text>

          <!-- Branch 2: NCDs -->
          <rect x="270" y="100" width="160" height="130" rx="10" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="2"/>
          <text x="350" y="125" text-anchor="middle" fill="#fda4af" font-size="11" font-weight="700">Non-Communicable (NCDs)</text>
          <text x="285" y="150" fill="#cbd5e1" font-size="10">• Non-infectious</text>
          <text x="285" y="170" fill="#cbd5e1" font-size="10">• Chronic (>3 months)</text>
          <text x="285" y="195" fill="#fecdd3" font-size="9">Diabetes, Asthma, Cancer</text>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Communicable diseases spread via microbes. Chronic NCDs persist for over 3 months and account for over 60% of annual mortality in India.
        </div>
      `;
    }

    // 7. Pathogen Gallery Simulator
    function renderPathogenGallerySim(title, stats, canvas, controls) {
      title.textContent = "Pathogen Classes: Bacteria, Viruses, Protozoa & Worms";
      let pClass = 'bacteria';

      const pathogens = {
        bacteria: { name: "Bacteria", eg: "Tuberculosis, Cholera, Typhoid", treat: "Curable with specific antibiotics", color: "#f59e0b" },
        virus: { name: "Viruses", eg: "Common Cold, Flu, Measles, Dengue, Polio", treat: "Prevented by vaccines; antibiotics useless", color: "#a855f7" },
        protozoa: { name: "Protozoa", eg: "Malaria (Plasmodium), Amoebic Dysentery", treat: "Antimalarial drugs; mosquito net barriers", color: "#06b6d4" },
        worm: { name: "Parasitic Worms (Helminths)", eg: "Ascariasis (Intestinal Roundworms)", treat: "Anti-helminthic deworming tablets", color: "#10b981" }
      };

      function update() {
        const cur = pathogens[pClass];
        stats.innerHTML = `
          <div class="stat-pill">Class: <strong style="color:${cur.color}">${cur.name}</strong></div>
          <div class="stat-pill">Diseases: <strong>${cur.eg}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
            <div style="width:120px; height:120px; border-radius:50%; background:#0f172a; border:3px solid ${cur.color}; display:flex; align-items:center; justify-content:center; margin-bottom:1rem; box-shadow:0 0 20px ${cur.color}44;">
              <span style="font-size:2.5rem;">${pClass === 'bacteria' ? '🧫' : pClass === 'virus' ? '🧬' : pClass === 'protozoa' ? '🔬' : '🪱'}</span>
            </div>
            <h3 style="color:${cur.color}; font-size:1.2rem; font-weight:700;">${cur.name}</h3>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-top:0.35rem; max-width:400px;"><strong>Examples:</strong> ${cur.eg}</p>
            <p style="color:#6ee7b7; font-size:0.8rem; margin-top:0.25rem;"><strong>Treatment/Control:</strong> ${cur.treat}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="pBact">Bacteria</button>
        <button class="btn" id="pVir">Viruses</button>
        <button class="btn" id="pProt">Protozoa</button>
        <button class="btn" id="pWorm">Parasitic Worms</button>
      `;

      controls.querySelector('#pBact').onclick = () => { pClass = 'bacteria'; update(); };
      controls.querySelector('#pVir').onclick = () => { pClass = 'virus'; update(); };
      controls.querySelector('#pProt').onclick = () => { pClass = 'protozoa'; update(); };
      controls.querySelector('#pWorm').onclick = () => { pClass = 'worm'; update(); };

      update();
    }

    // 8. NCD & Deficiency Diseases Simulator
    function renderNcdDeficiencyLabSim(title, stats, canvas, controls) {
      title.textContent = "Deficiency Diseases: Scurvy, Anaemia & Goitre";
      let def = 'scurvy';

      const defMap = {
        scurvy: { name: "Scurvy", cause: "Vitamin C Deficiency", sym: "Bleeding gums, fragile skin capillaries, delayed wound healing.", remedy: "Citrus fruits, amla, oranges, lemons.", color: "#f59e0b" },
        anaemia: { name: "Anaemia", cause: "Iron Deficiency", sym: "Low hemoglobin, pale skin/eyes, extreme fatigue, breathlessness.", remedy: "Green leafy spinach, jaggery, lentils, iron supplements.", color: "#f43f5e" },
        goitre: { name: "Goitre", cause: "Iodine Deficiency", sym: "Enlargement of the thyroid gland creating swollen neck mass.", remedy: "Iodized table salt, seafood.", color: "#06b6d4" }
      };

      function update() {
        const cur = defMap[def];
        stats.innerHTML = `
          <div class="stat-pill">Deficiency: <strong style="color:${cur.color}">${cur.name}</strong></div>
          <div class="stat-pill">Missing Nutrient: <strong>${cur.cause}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
            <div style="width:110px; height:110px; border-radius:50%; background:#1e1b4b; border:3px solid ${cur.color}; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
              <span style="font-size:2.5rem;">${def === 'scurvy' ? '🍋' : def === 'anaemia' ? '🩸' : '🧂'}</span>
            </div>
            <h3 style="color:${cur.color}; font-size:1.2rem; font-weight:700;">${cur.name} (${cur.cause})</h3>
            <p style="color:#fecdd3; font-size:0.85rem; margin-top:0.35rem; max-width:400px;"><strong>Clinical Signs:</strong> ${cur.sym}</p>
            <p style="color:#6ee7b7; font-size:0.8rem; margin-top:0.35rem;"><strong>Dietary Remedy:</strong> ${cur.remedy}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="dSc">🍋 Scurvy (Vit C)</button>
        <button class="btn" id="dAn">🩸 Anaemia (Iron)</button>
        <button class="btn" id="dGo">🧂 Goitre (Iodine)</button>
      `;

      controls.querySelector('#dSc').onclick = () => { def = 'scurvy'; update(); };
      controls.querySelector('#dAn').onclick = () => { def = 'anaemia'; update(); };
      controls.querySelector('#dGo').onclick = () => { def = 'goitre'; update(); };

      update();
    }

    // 9. Transmission Routes Simulator
    function renderTransmissionRoutesSim(title, stats, canvas, controls) {
      title.textContent = "5 Primary Modes of Disease Transmission";

      stats.innerHTML = `
        <div class="stat-pill">Vectors: <strong>Mosquitoes & Houseflies</strong></div>
        <div class="stat-pill">Vehicles: <strong>Air, Water, Fomites, Contact</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 280">
          <circle cx="230" cy="140" r="45" fill="#e11d48"/>
          <text x="230" y="145" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">Infected Host</text>

          <!-- 5 routes branching out -->
          <g transform="translate(90, 60)">
            <rect width="90" height="40" rx="6" fill="#0f172a" stroke="#06b6d4"/>
            <text x="45" y="24" text-anchor="middle" fill="#67e8f9" font-size="9" font-weight="700">1. Air Droplets</text>
          </g>

          <g transform="translate(280, 60)">
            <rect width="90" height="40" rx="6" fill="#0f172a" stroke="#10b981"/>
            <text x="45" y="24" text-anchor="middle" fill="#6ee7b7" font-size="9" font-weight="700">2. Direct Contact</text>
          </g>

          <g transform="translate(330, 160)">
            <rect width="90" height="40" rx="6" fill="#0f172a" stroke="#f59e0b"/>
            <text x="45" y="24" text-anchor="middle" fill="#fde047" font-size="9" font-weight="700">3. Fomites (Towels)</text>
          </g>

          <g transform="translate(185, 220)">
            <rect width="90" height="40" rx="6" fill="#0f172a" stroke="#3b82f6"/>
            <text x="45" y="24" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700">4. Food & Water</text>
          </g>

          <g transform="translate(40, 160)">
            <rect width="90" height="40" rx="6" fill="#0f172a" stroke="#ec4899"/>
            <text x="45" y="24" text-anchor="middle" fill="#fbcfe8" font-size="9" font-weight="700">5. Vectors (Mosquito)</text>
          </g>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Infectious microbes spread via airborne aerosols, physical skin contact, shared towels (fomites), contaminated food/water, and insect vectors.
        </div>
      `;
    }

    // 10. Sanitation Barrier Simulator
    function renderSanitationBarrierSim(title, stats, canvas, controls) {
      title.textContent = "Multi-Barrier Public Health Shields";
      let soap = true;
      let sanitation = true;
      let net = true;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Soap Washing: <strong>${soap ? 'Ruptures Viral Lipids' : 'Off'}</strong></div>
          <div class="stat-pill">Toilets: <strong>${sanitation ? 'Protects Water Aquifers' : 'Off'}</strong></div>
          <div class="stat-pill">Bed Nets: <strong>${net ? 'Blocks Nocturnal Vectors' : 'Off'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 260">
            <!-- Barrier 1 -->
            <g transform="translate(40, 50)">
              <rect width="110" height="150" rx="10" fill="${soap ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255,255,255,0.02)'}" stroke="${soap ? '#10b981' : '#475569'}" stroke-width="2"/>
              <text x="55" y="40" text-anchor="middle" font-size="24">🧼</text>
              <text x="55" y="80" text-anchor="middle" fill="#a7f3d0" font-size="10" font-weight="700">20s Handwash</text>
              <text x="55" y="110" text-anchor="middle" fill="#cbd5e1" font-size="8">${soap ? 'Viral Lipid Rupture' : 'Germs Transmitted'}</text>
            </g>

            <!-- Barrier 2 -->
            <g transform="translate(175, 50)">
              <rect width="110" height="150" rx="10" fill="${sanitation ? 'rgba(6, 182, 212, 0.2)' : 'rgba(255,255,255,0.02)'}" stroke="${sanitation ? '#06b6d4' : '#475569'}" stroke-width="2"/>
              <text x="55" y="40" text-anchor="middle" font-size="24">🚻</text>
              <text x="55" y="80" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Sanitary Toilets</text>
              <text x="55" y="110" text-anchor="middle" fill="#cbd5e1" font-size="8">${sanitation ? 'No Fecal Runoff' : 'Contaminates Wells'}</text>
            </g>

            <!-- Barrier 3 -->
            <g transform="translate(310, 50)">
              <rect width="110" height="150" rx="10" fill="${net ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255,255,255,0.02)'}" stroke="${net ? '#f59e0b' : '#475569'}" stroke-width="2"/>
              <text x="55" y="40" text-anchor="middle" font-size="24">🛏</text>
              <text x="55" y="80" text-anchor="middle" fill="#fde047" font-size="10" font-weight="700">Mosquito Nets</text>
              <text x="55" y="110" text-anchor="middle" fill="#cbd5e1" font-size="8">${net ? 'Blocks Malaria' : 'Vector Biting'}</text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="tSoap">🧼 Handwash</button>
        <button class="btn" id="tSan">🚻 Toilets</button>
        <button class="btn" id="tNet">🛏 Bed Nets</button>
      `;

      controls.querySelector('#tSoap').onclick = () => { soap = !soap; update(); };
      controls.querySelector('#tSan').onclick = () => { sanitation = !sanitation; update(); };
      controls.querySelector('#tNet').onclick = () => { net = !net; update(); };

      update();
    }

    // 11. Immune System Patrol Simulator
    function renderImmuneSystemPatrolSim(title, stats, canvas, controls) {
      title.textContent = "White Blood Cell Patrol & Phagocytosis";
      let active = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Defense: <strong>Innate Phagocytes & B-Cells</strong></div>
          <div class="stat-pill">Status: <strong style="color:${active ? '#10b981' : '#f59e0b'}">${active ? 'Pathogen Engulfed & Neutralized' : 'Patrolling Bloodstream'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 260">
            <!-- Blood vessel -->
            <rect x="20" y="60" width="420" height="140" rx="12" fill="#450a0a" stroke="#b91c1c" stroke-width="3"/>
            <text x="230" y="50" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="700">Capillary Lumen</text>

            <!-- Red Blood Cells -->
            <ellipse cx="80" cy="110" rx="16" ry="10" fill="#dc2626"/>
            <ellipse cx="380" cy="140" rx="16" ry="10" fill="#dc2626"/>

            <!-- Macrophage Phagocyte -->
            <g transform="translate(${active ? 200 : 150}, 130) transition: transform 0.4s ease;">
              <circle cx="0" cy="0" r="32" fill="rgba(16, 185, 129, 0.6)" stroke="#10b981" stroke-width="3"/>
              <text x="0" y="4" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">WBC</text>
            </g>

            <!-- Bacteria -->
            <g transform="translate(240, 130)">
              <rect x="0" y="-8" width="24" height="14" rx="7" fill="${active ? '#64748b' : '#f59e0b'}"/>
              <text x="12" y="24" text-anchor="middle" fill="${active ? '#94a3b8' : '#fed7aa'}" font-size="9">Bacteria</text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="tEngulf">${active ? 'Reset Patrol' : '🔬 Launch Phagocytosis Attack'}</button>
      `;

      controls.querySelector('#tEngulf').onclick = () => { active = !active; update(); };
      update();
    }

    // 12. Vaccine Mechanism Simulator
    function renderVaccineMechanismSim(title, stats, canvas, controls) {
      title.textContent = "Vaccine Target Practice: Creating Memory Cells";
      let stage = 1;

      const stages = [
        { title: "1. Weakened Antigen Inoculated", desc: "Harmless components enter bloodstream; cannot cause disease." },
        { title: "2. B-Cells Synthesize Antibodies", desc: "Immune system custom-manufactures Y-shaped IgG antibodies." },
        { title: "3. Memory Cells Formed", desc: "Long-lived memory B-cells store genetic blueprint for decades." },
        { title: "4. Rapid Secondary Immunity", desc: "Upon wild germ contact, explosive antibody release kills pathogen instantly." }
      ];

      function update() {
        const cur = stages[stage - 1];
        stats.innerHTML = `
          <div class="stat-pill">Phase: <strong>${cur.title}</strong></div>
          <div class="stat-pill">Status: <strong>Strictly Preventive</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1rem; text-align:center;">
            <svg width="400" height="200" viewBox="0 0 400 200">
              <!-- Timeline line -->
              <line x1="50" y1="100" x2="350" y2="100" stroke="#334155" stroke-width="4"/>
              
              ${stages.map((_, i) => `
                <circle cx="${50 + i * 100}" cy="100" r="${stage === (i+1) ? 18 : 12}" fill="${stage === (i+1) ? '#06b6d4' : '#1e293b'}" stroke="${stage === (i+1) ? '#67e8f9' : '#64748b'}" stroke-width="2"/>
                <text x="${50 + i * 100}" y="104" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">${i+1}</text>
              `).join('')}
            </svg>
            <h4 style="color:#67e8f9; font-size:1.1rem; margin-top:0.25rem;">${cur.title}</h4>
            <p style="color:#cbd5e1; font-size:0.85rem; max-width:400px;">${cur.desc}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="v1">1. Inject</button>
        <button class="btn" id="v2">2. Antibodies</button>
        <button class="btn" id="v3">3. Memory</button>
        <button class="btn" id="v4">4. Shield</button>
      `;

      controls.querySelector('#v1').onclick = () => { stage = 1; update(); };
      controls.querySelector('#v2').onclick = () => { stage = 2; update(); };
      controls.querySelector('#v3').onclick = () => { stage = 3; update(); };
      controls.querySelector('#v4').onclick = () => { stage = 4; update(); };

      update();
    }

    // 13. Vaccine Milestones India Simulator
    function renderVaccineMilestonesIndiaSim(title, stats, canvas, controls) {
      title.textContent = "Vaccine Milestones: Jenner to Vaccine Maitri";

      stats.innerHTML = `
        <div class="stat-pill">Jenner: <strong>1796 Cowpox / Smallpox</strong></div>
        <div class="stat-pill">Eradication: <strong>1979 Smallpox Gone</strong></div>
        <div class="stat-pill">Dr. M.K. Bhan: <strong>Rotavirus Rotavac</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 260">
          <g transform="translate(30, 40)">
            <rect width="185" height="180" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
            <text x="92" y="30" text-anchor="middle" fill="#fde047" font-size="11" font-weight="700">Historical Foundations</text>
            <text x="15" y="65" fill="#cbd5e1" font-size="9">• Indian Teekedaars (Variolation)</text>
            <text x="15" y="95" fill="#cbd5e1" font-size="9">• Edward Jenner (1796 Cowpox)</text>
            <text x="15" y="125" fill="#10b981" font-size="9" font-weight="700">• 1979: Smallpox Eradicated!</text>
          </g>

          <g transform="translate(245, 40)">
            <rect width="185" height="180" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
            <text x="92" y="30" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">Indian Global Leadership</text>
            <text x="15" y="65" fill="#cbd5e1" font-size="9">• >60% World Childhood Doses</text>
            <text x="15" y="95" fill="#cbd5e1" font-size="9">• Vaccine Maitri to 100+ nations</text>
            <text x="15" y="125" fill="#67e8f9" font-size="9" font-weight="700">• Dr. M.K. Bhan (Rotavac 116E)</text>
          </g>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          From Jenner's 1796 smallpox vaccine to India's Vaccine Maitri and Dr. M.K. Bhan's Rotavirus vaccine, immunization shields human civilization.
        </div>
      `;
    }

    // 14. Fleming Penicillin Simulator
    function renderFlemingPenicillinSim(title, stats, canvas, controls) {
      title.textContent = "Alexander Fleming's 1928 Penicillin Discovery";

      stats.innerHTML = `
        <div class="stat-pill">Mold: <strong>Penicillium notatum</strong></div>
        <div class="stat-pill">Bacteria: <strong>Staphylococcus lysed</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 260">
          <circle cx="230" cy="130" r="105" fill="#0f172a" stroke="#cbd5e1" stroke-width="4"/>
          <!-- Bacterial lawn -->
          <circle cx="230" cy="130" r="100" fill="#fef08a" opacity="0.6"/>

          <!-- Clear Zone of Inhibition -->
          <circle cx="230" cy="130" r="50" fill="#070d18" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4,4"/>

          <!-- Central Mold Colony -->
          <circle cx="230" cy="130" r="18" fill="#047857" stroke="#34d399" stroke-width="2"/>
          <text x="230" y="134" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Mold</text>

          <text x="230" y="70" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Zone of Bacterial Lysis (Penicillin)</text>
          <text x="230" y="210" text-anchor="middle" fill="#713f12" font-size="9">Staphylococcus Bacterial Lawn</text>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Fleming noticed the green mold Penicillium secreted a compound that dissolved surrounding bacteria. Penicillin targets peptidoglycan cell walls.
        </div>
      `;
    }

    // 15. Antibiotic Resistance Simulator
    function renderAntibioticResistanceSim(title, stats, canvas, controls) {
      title.textContent = "Antibiotic Resistance & Dr. Kamal Ranadive";
      let day = 1;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Timeline: <strong>Day ${day}</strong></div>
          <div class="stat-pill">Threat: <strong>${day === 7 ? 'Mutant Superbug Outbreak' : 'Normal Infection'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 260">
            <!-- Left: Resistance progression -->
            <g transform="translate(30, 30)">
              <rect width="200" height="200" rx="10" fill="#18181b" stroke="${day === 7 ? '#f43f5e' : '#f59e0b'}" stroke-width="2"/>
              <text x="100" y="25" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">Bacterial Population</text>
              
              ${day === 1 ? `
                <circle cx="50" cy="70" r="12" fill="#10b981"/>
                <circle cx="100" cy="70" r="12" fill="#10b981"/>
                <circle cx="150" cy="70" r="12" fill="#10b981"/>
                <circle cx="75" cy="120" r="12" fill="#10b981"/>
                <circle cx="125" cy="120" r="12" fill="#f43f5e"/>
                <text x="100" y="170" text-anchor="middle" fill="#cbd5e1" font-size="8">Sensitive (Green) vs 1 Mutant (Red)</text>
              ` : day === 3 ? `
                <circle cx="100" cy="80" r="14" fill="#f43f5e"/>
                <circle cx="130" cy="120" r="14" fill="#f43f5e"/>
                <text x="100" y="170" text-anchor="middle" fill="#fde047" font-size="8">Patient Stops Medicine Early!</text>
              ` : `
                <circle cx="50" cy="60" r="14" fill="#f43f5e"/>
                <circle cx="100" cy="60" r="14" fill="#f43f5e"/>
                <circle cx="150" cy="60" r="14" fill="#f43f5e"/>
                <circle cx="75" cy="110" r="14" fill="#f43f5e"/>
                <circle cx="125" cy="110" r="14" fill="#f43f5e"/>
                <text x="100" y="170" text-anchor="middle" fill="#fda4af" font-size="9" font-weight="700">100% Resistant Superbug Colony</text>
              `}
            </g>

            <!-- Right: Dr. Kamal Ranadive Cancer Research -->
            <g transform="translate(250, 30)">
              <rect width="180" height="200" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
              <text x="90" y="25" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Dr. Kamal Ranadive (1917–2001)</text>
              <text x="15" y="65" fill="#cbd5e1" font-size="8">• Founded 1st Tissue Culture Lab</text>
              <text x="15" y="95" fill="#cbd5e1" font-size="8">• Cancer Research Centre, Mumbai</text>
              <text x="15" y="125" fill="#cbd5e1" font-size="8">• Linked Tobacco & Viruses to Cancer</text>
              <text x="90" y="170" text-anchor="middle" fill="#a7f3d0" font-size="9" font-weight="700">Biomedical Pioneer</text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="d1">Day 1: Start</button>
        <button class="btn" id="d3">Day 3: Miss Dose</button>
        <button class="btn" id="d7">Day 7: Superbug</button>
      `;

      controls.querySelector('#d1').onclick = () => { day = 1; update(); };
      controls.querySelector('#d3').onclick = () => { day = 3; update(); };
      controls.querySelector('#d7').onclick = () => { day = 7; update(); };

      update();
    }

    // 16. Health & Disease Master Matrix Simulator
    function renderHealthDiseaseMasterMatrixSim(title, stats, canvas, controls) {
      title.textContent = "Master Comparative Synthesis Matrix";

      stats.innerHTML = `
        <div class="stat-pill">Chapter: <strong>Health, Diseases & Prevention</strong></div>
        <div class="stat-pill">Scope: <strong>Curative & Preventive Medicine</strong></div>
      `;

      canvas.innerHTML = `
        <div style="width:100%; height:100%; overflow-y:auto; padding:0.75rem;">
          <div style="display:grid; grid-template-columns:1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-emerald);">WHO Health & Ayurvedic Wisdom</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Physical, mental, social wellness. Dinacharya routines, Ritucharya seasonal shifts, Yoga, Pranayama.</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-amber);">Symptoms vs Signs & Disease Classes</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Subjective feelings vs objective clinical measurements. Communicable (germs) vs NCDs (diabetes, asthma, scurvy).</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-cyan);">Vaccines & National Milestones</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Preventive training of memory B-cells. Jenner 1796, Smallpox 1979 eradication, Vaccine Maitri, Dr. M.K. Bhan.</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-rose);">Antibiotics, Superbugs & Dr. Ranadive</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Fleming Penicillin 1928, ineffectiveness on viruses, resistance crisis, and Dr. Kamal Ranadive cancer oncology.</div>
            </div>
          </div>
        </div>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Synthesis matrix connecting holistic lifestyle, clinical diagnostics, disease classes, and pharmaceutical milestones.
        </div>
      `;
    }

    // Initialize on page load
    window.addEventListener('DOMContentLoaded', () => {
      loadSlide(0);
    });
  </script>
</body>
</html>
"""

# Embed slides json
final_html = HTML_CONTENT.replace("%%SLIDES_JSON%%", SLIDES_JSON)

out_path = "public/animations/class8-science-health-disease.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully generated {out_path} ({len(final_html.encode('utf-8'))} bytes).")

