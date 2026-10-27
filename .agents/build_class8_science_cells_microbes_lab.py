# Class 8 Science Chapter 2: Cell Structure, Variation, and Microorganisms
# Master Builder Script: Compiles 20-slide animated lab into public/animations/class8-science-cells-microbes.html

import json
import sys
sys.path.insert(0, '.agents')
from class8_science_cells_microbes_data import SLIDES_DATA, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 2: Cell Structure & Microorganisms Master Lab</title>
  
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
      --card-border: rgba(16, 185, 129, 0.25);
      --accent-emerald: #10b981;
      --accent-cyan: #06b6d4;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --accent-rose: #f43f5e;
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
      background: radial-gradient(circle at top right, #064e3b 0%, #070d18 70%);
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
      background: linear-gradient(135deg, #10b981, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
    }

    .brand-title {
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(to right, #6ee7b7, #67e8f9);
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
      border-color: var(--accent-emerald);
      transform: translateY(-1px);
    }

    .btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .btn-primary {
      background: linear-gradient(135deg, #059669, #0891b2);
      border-color: #10b981;
    }

    .btn-primary:hover:not(:disabled) {
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
    }

    .slide-badge {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--accent-emerald);
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
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
      color: var(--accent-emerald);
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
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
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
      background: linear-gradient(135deg, #047857, #0e7490);
      border: 2px solid var(--accent-emerald);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }

    .avatar-speaking {
      animation: pulseAvatar 1.4s infinite alternate;
    }

    @keyframes pulseAvatar {
      from { transform: scale(1); box-shadow: 0 0 8px rgba(16, 185, 129, 0.4); }
      to { transform: scale(1.08); box-shadow: 0 0 20px rgba(6, 182, 212, 0.8); }
    }

    .voice-control-btn {
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid var(--accent-emerald);
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
      background: var(--accent-emerald);
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
      color: var(--accent-cyan);
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
      border-color: var(--accent-emerald);
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
      color: var(--accent-emerald);
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
      color: var(--accent-emerald);
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
      accent-color: var(--accent-emerald);
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
      border-color: rgba(16, 185, 129, 0.3);
    }

    .quiz-q-num {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-emerald);
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
      border-color: var(--accent-emerald);
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
      <div class="brand-icon">🔬</div>
      <div>
        <div class="brand-title">Class 8 Science • Chapter 2: Cell Structure & Microorganisms</div>
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
          <span class="panel-tag" id="slideBadgeTag">Cellular History</span>
          <h1 class="panel-title" id="slideHeading">Discovery of Cells</h1>
          <div class="panel-sub" id="slideSubheading">Micrographia, Robert Hooke (1665), and the First Glimpse</div>
        </div>

        <!-- Teacher Voice Avatar -->
        <div class="avatar-card">
          <div class="avatar-wrapper">
            <div class="avatar-face" id="teacherAvatar">👨‍🔬</div>
          </div>
          <div>
            <div style="font-size: 0.85rem; font-weight: 700; color: var(--accent-emerald);">Prof. Raman • Cellular Mentor</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.2rem;" id="narrationSummary">
              Explore the discovery and fundamental architecture of cells and the microbial kingdom.
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
          <h4 style="font-size: 0.85rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase; letter-spacing: 0.05em;">
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
          <div class="sim-title" id="simTitle">🔬 Virtual Microscope Simulator</div>
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
      <p>Congratulations! You have mastered NCERT Class 8 Science Chapter 2: Cell Structure, Variation, and Microorganisms.</p>
    </div>
  </main>

  <!-- Footer Navigation -->
  <footer>
    <div style="font-size: 0.8rem; color: #64748b;">
      Class 8 Science • Chapter 2 • Cell Structure & Microorganisms Master Laboratory
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
        btn.style.background = 'rgba(16, 185, 129, 0.2)';
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
        case 'hooke_cork_microscope_sim':
          renderHookeCorkSim(title, stats, canvas, controls);
          break;
        case 'magnification_evolution_sim':
          renderMagnificationEvolutionSim(title, stats, canvas, controls);
          break;
        case 'cell_triad_anatomy_sim':
          renderCellTriadAnatomySim(title, stats, canvas, controls);
          break;
        case 'membrane_transport_cytoplasm_sim':
          renderMembraneTransportSim(title, stats, canvas, controls);
          break;
        case 'nucleus_command_center_sim':
          renderNucleusCommandSim(title, stats, canvas, controls);
          break;
        case 'plant_vs_animal_organelles_sim':
          renderPlantVsAnimalSim(title, stats, canvas, controls);
          break;
        case 'prokaryote_vs_eukaryote_sim':
          renderProkaryoteVsEukaryoteSim(title, stats, canvas, controls);
          break;
        case 'cell_shapes_specialization_sim':
          renderCellShapesSpecializationSim(title, stats, canvas, controls);
          break;
        case 'cell_size_scale_comparator_sim':
          renderCellSizeScaleSim(title, stats, canvas, controls);
          break;
        case 'biological_hierarchy_ladder_sim':
          renderBiologicalHierarchySim(title, stats, canvas, controls);
          break;
        case 'microbial_ubiquity_habitats_sim':
          renderMicrobialUbiquitySim(title, stats, canvas, controls);
          break;
        case 'biogas_anaerobic_digester_sim':
          renderBiogasDigesterSim(title, stats, canvas, controls);
          break;
        case 'kitchen_fermentation_lab_sim':
          renderKitchenFermentationSim(title, stats, canvas, controls);
          break;
        case 'rhizobium_microalgae_lab_sim':
          renderRhizobiumMicroalgaeSim(title, stats, canvas, controls);
          break;
        case 'oil_spill_bioremediation_sim':
          renderOilSpillBioremediationSim(title, stats, canvas, controls);
          break;
        case 'cells_microbes_master_matrix_sim':
          renderCellsMicrobesMasterMatrixSim(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Laboratory Visualizer';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Hooke Cork Microscope Simulator (1665)
    function renderHookeCorkSim(title, stats, canvas, controls) {
      title.textContent = "Hooke's 1665 Cork Slice & Compound Microscope";
      let focus = 0; // 0 = sharp
      let sliceThickness = 1; // 1 = thin, 2 = medium, 3 = thick

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Year: <strong>1665</strong></div>
          <div class="stat-pill">Magnification: <strong>250×</strong></div>
          <div class="stat-pill">Specimen: <strong>Dead Bottle Cork Bark</strong></div>
        `;

        const blurVal = Math.abs(focus) * 1.2;
        const opacity = sliceThickness === 1 ? 0.9 : sliceThickness === 2 ? 0.6 : 0.35;

        canvas.innerHTML = `
          <div style="position:relative; width:340px; height:340px; border-radius:50%; border:6px solid #334155; box-shadow:0 0 30px rgba(16,185,129,0.2) inset, 0 0 20px rgba(0,0,0,0.8); overflow:hidden; background:#0f172a;">
            <svg width="340" height="340" viewBox="0 0 340 340" style="filter: blur(${blurVal}px); transition: filter 0.2s ease;">
              <defs>
                <pattern id="corkGrid" width="30" height="30" patternUnits="userSpaceOnUse">
                  <rect width="28" height="28" rx="2" fill="none" stroke="#d97706" stroke-width="2.5" opacity="${opacity}"/>
                  <circle cx="14" cy="14" r="1.5" fill="#92400e" opacity="0.6"/>
                </pattern>
              </defs>
              <rect x="0" y="0" width="340" height="340" fill="url(#corkGrid)"/>
            </svg>
            <div style="position:absolute; bottom:14px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:700; color:#fef08a; background:rgba(0,0,0,0.7); padding:3px 10px; border-radius:6px; border:1px solid #78350f;">
              Empty Cellulose Compartments: "Cells"
            </div>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Cork Slice:</span>
          <button class="btn btn-primary" id="thinSlice">Thin (Crisp)</button>
          <button class="btn" id="thickSlice">Thick (Blurry)</button>
        </div>
        <div class="sim-ctrl-group" style="margin-left:auto;">
          <span>Focus Knob:</span>
          <input type="range" class="sim-slider" id="hookeFocus" min="-5" max="5" value="${focus}" style="width:90px;">
        </div>
      `;

      controls.querySelector('#thinSlice').onclick = () => { sliceThickness = 1; update(); };
      controls.querySelector('#thickSlice').onclick = () => { sliceThickness = 3; update(); };
      controls.querySelector('#hookeFocus').oninput = (e) => { focus = parseInt(e.target.value); update(); };

      update();
    }

    // 2. Magnification Evolution Simulator
    function renderMagnificationEvolutionSim(title, stats, canvas, controls) {
      title.textContent = "Optical Powers: Eye to 1,000,000× Electron Microscope";
      let level = 2; // 0=Eye, 1=Leeuwenhoek (300x), 2=Light (1500x), 3=Electron (1,000,000x)

      const levels = [
        { name: "Unaided Eye (1×)", mag: "1×", res: "100 μm (0.1 mm)", view: "Hair strand & needle tip", color: "#94a3b8" },
        { name: "Leeuwenhoek (300×)", mag: "300×", res: "1 μm", view: "Living bacteria & red blood cells", color: "#f59e0b" },
        { name: "Compound Light (1500×)", mag: "1500×", res: "0.2 μm", view: "Cell wall, nucleus, chloroplasts", color: "#10b981" },
        { name: "Electron Microscope (1,000,000×)", mag: "1,000,000×", res: "0.1 nm (0.0001 μm)", view: "Ribosomes, lipid bilayer, virus capsids", color: "#06b6d4" }
      ];

      function update() {
        const cur = levels[level];
        stats.innerHTML = `
          <div class="stat-pill">Tool: <strong style="color:${cur.color}">${cur.name}</strong></div>
          <div class="stat-pill">Limit: <strong>${cur.res}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
            <div style="width:180px; height:180px; border-radius:50%; background:#090e1a; border:4px solid ${cur.color}; display:flex; align-items:center; justify-content:center; box-shadow:0 0 25px ${cur.color}33; margin-bottom:1rem; position:relative; overflow:hidden;">
              <svg width="180" height="180" viewBox="0 0 180 180">
                ${getEvolutionSVG(level, cur.color)}
              </svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:700; color:${cur.color}; margin-bottom:0.25rem;">${cur.name}</h3>
            <p style="font-size:0.85rem; color:#cbd5e1; max-width:380px;">${cur.view}</p>
          </div>
        `;
      }

      function getEvolutionSVG(lvl, color) {
        if (lvl === 0) {
          return `<line x1="20" y1="90" x2="160" y2="90" stroke="${color}" stroke-width="8"/>
                  <text x="90" y="70" text-anchor="middle" fill="#fff" font-size="11">Human Hair (~100 μm)</text>`;
        } else if (lvl === 1) {
          return `<ellipse cx="90" cy="90" rx="35" ry="14" fill="${color}44" stroke="${color}" stroke-width="2.5"/>
                  <circle cx="80" cy="90" r="5" fill="${color}"/>
                  <text x="90" y="55" text-anchor="middle" fill="#fff" font-size="10">Motile Bacterium</text>`;
        } else if (lvl === 2) {
          return `<rect x="35" y="45" width="110" height="90" rx="8" fill="${color}22" stroke="${color}" stroke-width="3"/>
                  <circle cx="90" cy="90" r="22" fill="#a855f7" opacity="0.8"/>
                  <circle cx="60" cy="70" r="10" fill="#22c55e"/>
                  <circle cx="120" cy="110" r="10" fill="#22c55e"/>
                  <text x="90" y="155" text-anchor="middle" fill="#fff" font-size="9">Onion Cell & Nucleus</text>`;
        } else {
          return `<!-- Phospholipid bilayer / DNA helix -->
                  <g transform="translate(40, 50)">
                    ${Array.from({length: 6}).map((_, i) => `
                      <circle cx="${i * 20}" cy="20" r="6" fill="${color}"/>
                      <line x1="${i * 20}" y1="26" x2="${i * 20}" y2="50" stroke="${color}" stroke-width="2"/>
                      <circle cx="${i * 20}" cy="60" r="6" fill="${color}"/>
                    `).join('')}
                    <text x="50" y="95" text-anchor="middle" fill="#fff" font-size="9">Lipid Bilayer (4 nm)</text>
                  </g>`;
        }
      }

      controls.innerHTML = `
        <button class="btn" id="l0">1× Eye</button>
        <button class="btn" id="l1">300× Leeuwenhoek</button>
        <button class="btn btn-primary" id="l2">1500× Light</button>
        <button class="btn" id="l3">1,000,000× Electron</button>
      `;

      controls.querySelector('#l0').onclick = () => { level = 0; update(); };
      controls.querySelector('#l1').onclick = () => { level = 1; update(); };
      controls.querySelector('#l2').onclick = () => { level = 2; update(); };
      controls.querySelector('#l3').onclick = () => { level = 3; update(); };

      update();
    }

    // 3. Cell Triad Anatomy Simulator
    function renderCellTriadAnatomySim(title, stats, canvas, controls) {
      title.textContent = "The Fundamental Cell Triad";
      let highlight = 'all';

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Active View: <strong style="text-transform:capitalize;">${highlight}</strong></div>
          <div class="stat-pill">Universal Architecture: <strong>Animal & Plant</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
            <svg width="340" height="300" viewBox="0 0 340 300">
              <!-- Cell Membrane -->
              <ellipse cx="170" cy="150" rx="130" ry="105" fill="${highlight === 'membrane' || highlight === 'all' ? 'rgba(6, 182, 212, 0.15)' : 'rgba(255,255,255,0.02)'}" stroke="${highlight === 'membrane' ? '#06b6d4' : '#334155'}" stroke-width="${highlight === 'membrane' ? 6 : 3}"/>
              
              <!-- Cytoplasm Area -->
              ${highlight === 'cytoplasm' ? `
                <ellipse cx="170" cy="150" rx="120" ry="95" fill="rgba(16, 185, 129, 0.25)"/>
              ` : ''}

              <!-- Cytoplasmic Organelles -->
              <circle cx="100" cy="120" r="8" fill="#10b981" opacity="0.7"/>
              <circle cx="230" cy="180" r="10" fill="#10b981" opacity="0.7"/>
              <ellipse cx="110" cy="190" rx="14" ry="7" fill="#f59e0b" opacity="0.6"/>
              <ellipse cx="220" cy="110" rx="14" ry="7" fill="#f59e0b" opacity="0.6"/>

              <!-- Nucleus -->
              <circle cx="170" cy="150" r="42" fill="${highlight === 'nucleus' || highlight === 'all' ? 'rgba(168, 85, 247, 0.45)' : '#1e1b4b'}" stroke="${highlight === 'nucleus' ? '#a855f7' : '#6366f1'}" stroke-width="${highlight === 'nucleus' ? 5 : 2}"/>
              <circle cx="170" cy="150" r="14" fill="#a855f7"/>

              <!-- Labels -->
              <text x="170" y="35" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">1. Cell Membrane</text>
              <text x="60" y="240" fill="#6ee7b7" font-size="11" font-weight="700">2. Cytoplasm</text>
              <text x="170" y="154" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">3. Nucleus</text>
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="btnAll">Show All Triad</button>
        <button class="btn" id="btnMem">1. Membrane</button>
        <button class="btn" id="btnCyto">2. Cytoplasm</button>
        <button class="btn" id="btnNuc">3. Nucleus</button>
      `;

      controls.querySelector('#btnAll').onclick = () => { highlight = 'all'; update(); };
      controls.querySelector('#btnMem').onclick = () => { highlight = 'membrane'; update(); };
      controls.querySelector('#btnCyto').onclick = () => { highlight = 'cytoplasm'; update(); };
      controls.querySelector('#btnNuc').onclick = () => { highlight = 'nucleus'; update(); };

      update();
    }

    // 4. Membrane Transport Simulator
    function renderMembraneTransportSim(title, stats, canvas, controls) {
      title.textContent = "Selective Permeability: Influx vs Efflux";
      let state = 'transporting';

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Permeability: <strong>Selectively Porous</strong></div>
          <div class="stat-pill">Admitted: <strong>Glucose, O₂, Salts</strong></div>
          <div class="stat-pill">Expelled: <strong>CO₂, Metabolic Waste</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 300">
            <!-- Membrane boundary -->
            <rect x="210" y="20" width="40" height="260" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
            <text x="230" y="15" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Porous Membrane</text>

            <!-- Outside Area -->
            <rect x="20" y="30" width="180" height="240" rx="8" fill="rgba(255,255,255,0.02)"/>
            <text x="110" y="55" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="700">External Environment</text>

            <!-- Nutrients entering -->
            <g transform="translate(80, 110)">
              <circle cx="0" cy="0" r="10" fill="#10b981"/>
              <text x="0" y="4" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Glu</text>
              <line x1="15" y1="0" x2="140" y2="0" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
              <text x="70" y="-10" text-anchor="middle" fill="#6ee7b7" font-size="9">Nutrient Entry →</text>
            </g>

            <!-- Inside Cytoplasm Area -->
            <rect x="260" y="30" width="180" height="240" rx="8" fill="rgba(16, 185, 129, 0.08)"/>
            <text x="350" y="55" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="700">Cytoplasm (Internal Matrix)</text>

            <!-- Waste exiting -->
            <g transform="translate(380, 200)">
              <circle cx="0" cy="0" r="10" fill="#f43f5e"/>
              <text x="0" y="4" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">CO₂</text>
              <line x1="-15" y1="0" x2="-140" y2="0" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>
              <text x="-70" y="-10" text-anchor="middle" fill="#fda4af" font-size="9">← Waste Exit</text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          The porous plasma membrane admits life-giving nutrients (glucose, ions) and expels metabolic waste (CO₂, urea).
        </div>
      `;

      update();
    }

    // 5. Nucleus Command Center Simulator
    function renderNucleusCommandSim(title, stats, canvas, controls) {
      title.textContent = "Nucleus: Command & Chromatin Condensation";
      let dividing = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Status: <strong>${dividing ? 'Cell Division (Chromosomes Condense)' : 'Resting State (Diffuse Chromatin)'}</strong></div>
          <div class="stat-pill">Envelope: <strong>Double Membrane Pores</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
            <svg width="340" height="280" viewBox="0 0 340 280">
              <!-- Nuclear envelope -->
              <circle cx="170" cy="140" r="100" fill="#1e1b4b" stroke="#a855f7" stroke-width="4" stroke-dasharray="14,6"/>
              
              ${dividing ? `
                <!-- Condensed X-shaped chromosomes -->
                <g transform="translate(140, 110)">
                  <line x1="-15" y1="-20" x2="15" y2="20" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
                  <line x1="15" y1="-20" x2="-15" y2="20" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
                </g>
                <g transform="translate(200, 150)">
                  <line x1="-15" y1="-20" x2="15" y2="20" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
                  <line x1="15" y1="-20" x2="-15" y2="20" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
                </g>
                <text x="170" y="260" text-anchor="middle" fill="#fde047" font-size="11" font-weight="700">Chromatin condensed into Chromosomes</text>
              ` : `
                <!-- Thread-like chromatin network -->
                <path d="M 120 120 Q 150 90 180 130 T 210 150 T 150 170 T 130 140" fill="none" stroke="#c084fc" stroke-width="2.5"/>
                <circle cx="185" cy="120" r="14" fill="#a855f7"/>
                <text x="170" y="260" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="700">Diffuse Chromatin & Nucleolus</text>
              `}
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="toggleDivide">${dividing ? 'Reset to Diffuse Chromatin' : '🔬 Trigger Division: Form Chromosomes'}</button>
      `;

      controls.querySelector('#toggleDivide').onclick = () => {
        dividing = !dividing;
        update();
      };

      update();
    }

    // 6. Plant vs Animal Organelles Simulator
    function renderPlantVsAnimalSim(title, stats, canvas, controls) {
      title.textContent = "Plant Cell (Wall & Plastids) vs Animal Cell";
      let cellType = 'plant'; // 'plant' or 'animal'

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Type: <strong>${cellType === 'plant' ? 'Plant Cell' : 'Animal Cell'}</strong></div>
          <div class="stat-pill">Cell Wall: <strong>${cellType === 'plant' ? 'Cellulose Outer Wall' : 'None (Membrane only)'}</strong></div>
          <div class="stat-pill">Plastids: <strong>${cellType === 'plant' ? 'Chloroplasts Present' : 'Absent'}</strong></div>
        `;

        if (cellType === 'plant') {
          canvas.innerHTML = `
            <svg width="100%" height="100%" viewBox="0 0 420 280">
              <!-- Outer rigid cell wall -->
              <polygon points="50,40 370,40 390,240 30,240" fill="#064e3b" stroke="#10b981" stroke-width="8"/>
              <!-- Inner membrane -->
              <polygon points="58,48 362,48 382,232 38,232" fill="#022c22" stroke="#06b6d4" stroke-width="2"/>
              
              <!-- Giant central vacuole -->
              <ellipse cx="200" cy="140" rx="90" ry="60" fill="rgba(6, 182, 212, 0.3)" stroke="#38bdf8" stroke-width="2"/>
              <text x="200" y="144" text-anchor="middle" fill="#bae6fd" font-size="11" font-weight="700">Large Central Vacuole</text>

              <!-- Green chloroplasts -->
              <ellipse cx="90" cy="90" rx="18" ry="10" fill="#16a34a" stroke="#4ade80"/>
              <ellipse cx="320" cy="90" rx="18" ry="10" fill="#16a34a" stroke="#4ade80"/>
              <ellipse cx="100" cy="200" rx="18" ry="10" fill="#16a34a" stroke="#4ade80"/>
              
              <!-- Pushed peripheral nucleus -->
              <circle cx="320" cy="180" r="22" fill="#7e22ce" stroke="#c084fc"/>
              <text x="320" y="184" text-anchor="middle" fill="#fff" font-size="8">Nucleus</text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg width="100%" height="100%" viewBox="0 0 420 280">
              <!-- Flexible irregular animal membrane -->
              <path d="M 80 80 C 130 30 310 40 340 100 C 370 160 340 240 260 250 C 180 260 70 240 50 170 C 30 110 50 100 80 80 Z" fill="#1e1b4b" stroke="#a855f7" stroke-width="4"/>
              
              <!-- Central nucleus -->
              <circle cx="200" cy="145" r="38" fill="#581c87" stroke="#c084fc" stroke-width="3"/>
              <circle cx="200" cy="145" r="14" fill="#a855f7"/>
              <text x="200" y="149" text-anchor="middle" fill="#fff" font-size="10">Nucleus</text>

              <!-- Small temporary vacuoles -->
              <circle cx="120" cy="110" r="9" fill="rgba(6, 182, 212, 0.4)" stroke="#38bdf8"/>
              <circle cx="280" cy="190" r="10" fill="rgba(6, 182, 212, 0.4)" stroke="#38bdf8"/>
              <text x="200" y="270" text-anchor="middle" fill="#cbd5e1" font-size="10">No cell wall • No chloroplasts</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="btnPlant">🌿 Plant Cell</button>
        <button class="btn" id="btnAnimal">🐾 Animal Cell</button>
      `;

      controls.querySelector('#btnPlant').onclick = () => { cellType = 'plant'; update(); };
      controls.querySelector('#btnAnimal').onclick = () => { cellType = 'animal'; update(); };

      update();
    }

    // 7. Prokaryote vs Eukaryote Simulator
    function renderProkaryoteVsEukaryoteSim(title, stats, canvas, controls) {
      title.textContent = "Bacterial Nucleoid vs Eukaryotic Membrane Nucleus";

      stats.innerHTML = `
        <div class="stat-pill">Bacterium: <strong>Naked Nucleoid (No Membrane)</strong></div>
        <div class="stat-pill">Eukaryote: <strong>Double-Membrane Enclosed Nucleus</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 280">
          <!-- Bacterium Side -->
          <g transform="translate(30, 40)">
            <rect x="0" y="0" width="180" height="190" rx="25" fill="#18181b" stroke="#f59e0b" stroke-width="3"/>
            <text x="90" y="-12" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="700">Bacterium (Prokaryote)</text>
            
            <!-- Tangled circular DNA (Nucleoid) -->
            <path d="M 60 70 Q 90 40 120 70 T 90 120 T 70 80" fill="none" stroke="#ef4444" stroke-width="3"/>
            <text x="90" y="145" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="700">Nucleoid</text>
            <text x="90" y="160" text-anchor="middle" fill="#94a3b8" font-size="8">No nuclear envelope</text>
          </g>

          <!-- Divider -->
          <line x1="230" y1="30" x2="230" y2="250" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>

          <!-- Eukaryote Side -->
          <g transform="translate(250, 40)">
            <ellipse cx="90" cy="95" rx="85" ry="90" fill="#1e1b4b" stroke="#06b6d4" stroke-width="3"/>
            <text x="90" y="-12" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">Eukaryote (Plant/Animal)</text>
            
            <!-- True double membrane nucleus -->
            <circle cx="90" cy="95" r="38" fill="#581c87" stroke="#a855f7" stroke-width="3"/>
            <text x="90" y="99" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">True Nucleus</text>
            <text x="90" y="150" text-anchor="middle" fill="#c084fc" font-size="8">Double nuclear membrane</text>
          </g>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Bacteria lack a nuclear membrane; their DNA floats freely in the nucleoid. Eukaryotes encapsulate genetic DNA inside a true nucleus.
        </div>
      `;
    }

    // 8. Cell Shapes Specialization Simulator
    function renderCellShapesSpecializationSim(title, stats, canvas, controls) {
      title.textContent = "Cell Differentiation: Shape Tailored to Function";
      let activeShape = 'neuron';

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Selected: <strong style="text-transform:capitalize;">${activeShape}</strong></div>
          <div class="stat-pill">Principle: <strong>Form Follows Function</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
            <svg width="400" height="260" viewBox="0 0 400 260">
              ${activeShape === 'neuron' ? `
                <!-- Nerve Cell (Neuron) -->
                <circle cx="90" cy="130" r="26" fill="#1e1b4b" stroke="#06b6d4" stroke-width="3"/>
                <!-- Dendrites -->
                <line x1="90" y1="104" x2="60" y2="70" stroke="#06b6d4" stroke-width="2.5"/>
                <line x1="90" y1="104" x2="100" y2="60" stroke="#06b6d4" stroke-width="2.5"/>
                <line x1="64" y1="130" x2="30" y2="120" stroke="#06b6d4" stroke-width="2.5"/>
                <!-- Long Axon -->
                <line x1="116" y1="130" x2="330" y2="130" stroke="#06b6d4" stroke-width="4"/>
                <!-- Nerve terminals -->
                <line x1="330" y1="130" x2="360" y2="105" stroke="#06b6d4" stroke-width="2.5"/>
                <line x1="330" y1="130" x2="360" y2="155" stroke="#06b6d4" stroke-width="2.5"/>
                <text x="200" y="220" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">Long & Branched: Quick impulse conduction</text>
              ` : activeShape === 'muscle' ? `
                <!-- Spindle-shaped Muscle Cell -->
                <path d="M 50 130 Q 200 80 350 130 Q 200 180 50 130 Z" fill="rgba(244, 63, 94, 0.35)" stroke="#f43f5e" stroke-width="3"/>
                <circle cx="200" cy="130" r="14" fill="#be123c"/>
                <text x="200" y="220" text-anchor="middle" fill="#fda4af" font-size="11" font-weight="700">Spindle-Shaped: Uniaxial contraction & pull</text>
              ` : `
                <!-- Biconcave Red Blood Cell -->
                <ellipse cx="200" cy="130" rx="80" ry="45" fill="#b91c1c" stroke="#ef4444" stroke-width="3"/>
                <ellipse cx="200" cy="130" rx="35" ry="18" fill="#7f1d1d"/>
                <text x="200" y="220" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="700">Biconcave Disc: High surface area for O₂ flux</text>
              `}
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="btnN">⚡ Neuron (Nerve)</button>
        <button class="btn" id="btnM">💪 Muscle (Spindle)</button>
        <button class="btn" id="btnR">🩸 RBC (Biconcave)</button>
      `;

      controls.querySelector('#btnN').onclick = () => { activeShape = 'neuron'; update(); };
      controls.querySelector('#btnM').onclick = () => { activeShape = 'muscle'; update(); };
      controls.querySelector('#btnR').onclick = () => { activeShape = 'rbc'; update(); };

      update();
    }

    // 9. Cell Size Scale & Ostrich Egg Simulator
    function renderCellSizeScaleSim(title, stats, canvas, controls) {
      title.textContent = "Cell Sizes: From 0.1 μm to 170 mm Ostrich Egg";
      let viewEgg = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Smallest: <strong>Mycoplasma (0.1 μm)</strong></div>
          <div class="stat-pill">Largest: <strong>Ostrich Egg Yolk (170 mm)</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
            <svg width="400" height="260" viewBox="0 0 400 260">
              ${viewEgg ? `
                <!-- Giant Ostrich Egg Yolk -->
                <circle cx="200" cy="130" r="105" fill="#f59e0b" stroke="#d97706" stroke-width="4"/>
                <text x="200" y="125" text-anchor="middle" fill="#fff" font-size="16" font-weight="800">Ostrich Egg Yolk</text>
                <text x="200" y="148" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="700">130 mm – 170 mm (~1.5 kg)</text>
                <text x="200" y="170" text-anchor="middle" fill="#78350f" font-size="10">Single Macroscopic Cell!</text>
              ` : `
                <!-- Microscopic Cells -->
                <g transform="translate(60, 130)">
                  <circle cx="0" cy="0" r="2" fill="#ef4444"/>
                  <text x="0" y="25" text-anchor="middle" fill="#fca5a5" font-size="9">Bacteria (2 μm)</text>
                </g>
                <g transform="translate(180, 130)">
                  <circle cx="0" cy="0" r="18" fill="#10b981"/>
                  <text x="0" y="38" text-anchor="middle" fill="#6ee7b7" font-size="9">Human Cell (20 μm)</text>
                </g>
                <g transform="translate(320, 130)">
                  <rect x="-30" y="-30" width="60" height="60" rx="4" fill="#0284c7"/>
                  <text x="0" y="45" text-anchor="middle" fill="#7dd3fc" font-size="9">Plant Cell (100 μm)</text>
                </g>
              `}
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="toggleEgg">${viewEgg ? 'Show Microscopic Cells' : '🥚 View Giant Ostrich Egg (170 mm)'}</button>
      `;

      controls.querySelector('#toggleEgg').onclick = () => {
        viewEgg = !viewEgg;
        update();
      };

      update();
    }

    // 10. Biological Hierarchy Ladder Simulator
    function renderBiologicalHierarchySim(title, stats, canvas, controls) {
      title.textContent = "Levels of Biological Organisation";
      let tier = 1; // 1 to 5

      const tiers = [
        { name: "1. Cell", eg: "Smooth Muscle Cell", desc: "Basic unit of life capable of contraction." },
        { name: "2. Tissue", eg: "Muscular Tissue", desc: "Cooperating sheet of spindle muscle cells." },
        { name: "3. Organ", eg: "Stomach", desc: "Muscle, epithelial, and connective tissues working together." },
        { name: "4. Organ System", eg: "Digestive System", desc: "Esophagus, stomach, intestines, liver digesting food." },
        { name: "5. Organism", eg: "Human / Organism", desc: "Complete living creature with integrated systems." }
      ];

      function update() {
        const cur = tiers[tier - 1];
        stats.innerHTML = `
          <div class="stat-pill">Level: <strong>${cur.name}</strong></div>
          <div class="stat-pill">Example: <strong>${cur.eg}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1rem; text-align:center;">
            <svg width="400" height="220" viewBox="0 0 400 220">
              <!-- Stepped ladder bars -->
              ${tiers.map((t, i) => `
                <rect x="${40 + i * 65}" y="${160 - i * 30}" width="55" height="40" rx="6" fill="${tier === (i+1) ? '#10b981' : '#1e293b'}" stroke="${tier === (i+1) ? '#6ee7b7' : '#475569'}" stroke-width="2"/>
                <text x="${67 + i * 65}" y="${185 - i * 30}" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">${i+1}</text>
              `).join('')}
            </svg>
            <h3 style="font-size:1.1rem; font-weight:700; color:#10b981; margin-top:0.25rem;">${cur.name}: ${cur.eg}</h3>
            <p style="font-size:0.85rem; color:#cbd5e1; max-width:400px;">${cur.desc}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="t1">1. Cell</button>
        <button class="btn" id="t2">2. Tissue</button>
        <button class="btn" id="t3">3. Organ</button>
        <button class="btn" id="t4">4. System</button>
        <button class="btn" id="t5">5. Organism</button>
      `;

      controls.querySelector('#t1').onclick = () => { tier = 1; update(); };
      controls.querySelector('#t2').onclick = () => { tier = 2; update(); };
      controls.querySelector('#t3').onclick = () => { tier = 3; update(); };
      controls.querySelector('#t4').onclick = () => { tier = 4; update(); };
      controls.querySelector('#t5').onclick = () => { tier = 5; update(); };

      update();
    }

    // 11. Microbial Ubiquity Simulator
    function renderMicrobialUbiquitySim(title, stats, canvas, controls) {
      title.textContent = "Microbial Ubiquity & Extreme Habitats";

      stats.innerHTML = `
        <div class="stat-pill">Habitats: <strong>Soil, Water, Air, Hot Springs, Snow</strong></div>
        <div class="stat-pill">Organization: <strong>Unicellular & Multicellular</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 280">
          <!-- Zone 1: Hot Springs -->
          <circle cx="80" cy="80" r="45" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="2"/>
          <text x="80" y="75" text-anchor="middle" fill="#fda4af" font-size="10" font-weight="700">Hot Springs</text>
          <text x="80" y="92" text-anchor="middle" fill="#cbd5e1" font-size="8">&gt; 80°C</text>

          <!-- Zone 2: Polar Snow -->
          <circle cx="230" cy="80" r="45" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="2"/>
          <text x="230" y="75" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Snow & Glaciers</text>
          <text x="230" y="92" text-anchor="middle" fill="#cbd5e1" font-size="8">&lt; 0°C</text>

          <!-- Zone 3: Gut Microbiome -->
          <circle cx="380" cy="80" r="45" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2"/>
          <text x="380" y="75" text-anchor="middle" fill="#fde047" font-size="10" font-weight="700">Animal Gut</text>
          <text x="380" y="92" text-anchor="middle" fill="#cbd5e1" font-size="8">Trillions</text>

          <rect x="40" y="160" width="380" height="80" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
          <text x="230" y="195" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="700">
            Microbes colonize every biosphere from deep oceans to clouds
          </text>
          <text x="230" y="215" text-anchor="middle" fill="#94a3b8" font-size="9">
            Unicellular (Bacteria, Amoeba) • Multicellular (Fungi, Algae) • Acellular (Viruses)
          </text>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Microbes survive thermal extremes, hyper-saline oceans, frozen glaciers, and digestive systems of living animals.
        </div>
      `;
    }

    // 12. Biogas Anaerobic Digester Simulator
    function renderBiogasDigesterSim(title, stats, canvas, controls) {
      title.textContent = "Biogas Plant: Anaerobic Organic Decomposition";
      let flame = true;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Process: <strong>Anaerobic Digestion</strong></div>
          <div class="stat-pill">Fuel: <strong>Methane (CH₄, 65%) + CO₂</strong></div>
          <div class="stat-pill">Stove: <strong style="color:${flame ? '#06b6d4' : '#64748b'}">${flame ? 'Burning Blue Flame' : 'Valve Off'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 280">
            <!-- Ground line -->
            <rect x="0" y="80" width="460" height="200" fill="#18181b"/>
            <line x1="0" y1="80" x2="460" y2="80" stroke="#713f12" stroke-width="3"/>

            <!-- Underground Digester Dome -->
            <path d="M 120 180 C 120 100 280 100 280 180 L 280 250 L 120 250 Z" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
            <text x="200" y="210" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="700">Anaerobic Slurry</text>

            <!-- Gas pipe to stove -->
            <line x1="200" y1="120" x2="200" y2="40" stroke="#38bdf8" stroke-width="4"/>
            <line x1="200" y1="40" x2="360" y2="40" stroke="#38bdf8" stroke-width="4"/>

            <!-- Kitchen Stove Flame -->
            <rect x="340" y="30" width="50" height="15" fill="#475569" rx="3"/>
            ${flame ? `
              <polygon points="365,30 355,5 375,5" fill="#06b6d4"/>
              <text x="365" y="-5" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="700">Clean Blue Flame</text>
            ` : ''}
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="toggleFlame">${flame ? 'Turn Off Stove Valve' : '🔥 Open Biogas Valve'}</button>
      `;

      controls.querySelector('#toggleFlame').onclick = () => { flame = !flame; update(); };
      update();
    }

    // 13. Kitchen Fermentation Simulator
    function renderKitchenFermentationSim(title, stats, canvas, controls) {
      title.textContent = "Culinary Microbiology: Yeast & Lactobacillus";
      let mode = 'bread';

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Fermenter: <strong>${mode === 'bread' ? 'Yeast (Saccharomyces)' : 'Lactobacillus Bacterium'}</strong></div>
          <div class="stat-pill">Product: <strong>${mode === 'bread' ? 'Fluffy Bread Dough' : 'Curd / Idli / Dosa'}</strong></div>
        `;

        if (mode === 'bread') {
          canvas.innerHTML = `
            <svg width="100%" height="100%" viewBox="0 0 460 260">
              <rect x="150" y="70" width="160" height="150" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
              <ellipse cx="230" cy="110" rx="70" ry="45" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
              <circle cx="210" cy="100" r="5" fill="#fff" opacity="0.8"/>
              <circle cx="245" cy="105" r="7" fill="#fff" opacity="0.8"/>
              <text x="230" y="180" text-anchor="middle" fill="#fed7aa" font-size="11" font-weight="700">Yeast Releases CO₂ Gas Bubbles</text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg width="100%" height="100%" viewBox="0 0 460 260">
              <path d="M 140 80 Q 140 220 230 220 Q 320 220 320 80 Z" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
              <ellipse cx="230" cy="80" rx="90" ry="20" fill="#fef9c3" stroke="#d97706" stroke-width="2"/>
              <text x="230" y="160" text-anchor="middle" fill="#92400e" font-size="11" font-weight="700">Lactic Acid Coagulates Milk</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="bBtn">🍞 Bread Dough (Yeast)</button>
        <button class="btn" id="cBtn">🥛 Curd & Batter (Lactobacillus)</button>
      `;

      controls.querySelector('#bBtn').onclick = () => { mode = 'bread'; update(); };
      controls.querySelector('#cBtn').onclick = () => { mode = 'curd'; update(); };

      update();
    }

    // 14. Rhizobium & Microalgae Simulator
    function renderRhizobiumMicroalgaeSim(title, stats, canvas, controls) {
      title.textContent = "Global Life Support: Rhizobium & Microalgae";

      stats.innerHTML = `
        <div class="stat-pill">Rhizobium: <strong>Traps Atmospheric N₂ in Roots</strong></div>
        <div class="stat-pill">Microalgae: <strong>&gt;50% of Earth's Oxygen</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 260">
          <!-- Left: Legume Root Nodule -->
          <g transform="translate(60, 40)">
            <rect width="150" height="180" rx="10" fill="#18181b" stroke="#10b981" stroke-width="2"/>
            <circle cx="75" cy="80" r="18" fill="#f43f5e"/>
            <text x="75" y="85" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">Nodule</text>
            <text x="75" y="130" text-anchor="middle" fill="#a7f3d0" font-size="10" font-weight="700">Rhizobium N₂</text>
            <text x="75" y="148" text-anchor="middle" fill="#94a3b8" font-size="8">Natural Soil Nitrates</text>
          </g>

          <!-- Right: Aquatic Microalgae -->
          <g transform="translate(250, 40)">
            <rect width="150" height="180" rx="10" fill="#032b43" stroke="#06b6d4" stroke-width="2"/>
            <circle cx="75" cy="70" r="6" fill="#fff" opacity="0.8"/>
            <circle cx="95" cy="50" r="8" fill="#fff" opacity="0.8"/>
            <text x="75" y="115" text-anchor="middle" fill="#67e8f9" font-size="10" font-weight="700">Spirulina & Diatoms</text>
            <text x="75" y="135" text-anchor="middle" fill="#a5f3fc" font-size="9">&gt;50% Global O₂</text>
            <text x="75" y="152" text-anchor="middle" fill="#cbd5e1" font-size="8">Protein & Vit B₁₂</text>
          </g>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Symbiotic Rhizobium enriches agricultural soil naturally, while microalgae produce over half the oxygen we breathe.
        </div>
      `;
    }

    // 15. Oil Spill Bioremediation Simulator
    function renderOilSpillBioremediationSim(title, stats, canvas, controls) {
      title.textContent = "Dr. Chakrabarty's Oil-Eating Superbug (1971/1980)";
      let cleaned = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Scientist: <strong>Dr. Ananda Mohan Chakrabarty</strong></div>
          <div class="stat-pill">Organism: <strong>Pseudomonas putida</strong></div>
          <div class="stat-pill">Ocean Status: <strong style="color:${cleaned ? '#10b981' : '#f43f5e'}">${cleaned ? 'Bioremediated (Clean Ocean)' : 'Crude Oil Slick'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 260">
            <!-- Ocean water -->
            <rect x="30" y="40" width="400" height="180" rx="10" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
            <text x="230" y="200" text-anchor="middle" fill="#bae6fd" font-size="11">Marine Ecosystem</text>

            ${!cleaned ? `
              <!-- Black crude oil slick -->
              <ellipse cx="230" cy="110" rx="140" ry="40" fill="#09090b" opacity="0.95" stroke="#27272a"/>
              <text x="230" y="115" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="700">Toxic Crude Oil Spill Slick</text>
            ` : `
              <!-- Cleaned ocean with bubbles and CO2 release -->
              <circle cx="160" cy="100" r="14" fill="#059669" opacity="0.6"/>
              <circle cx="230" cy="90" r="16" fill="#059669" opacity="0.6"/>
              <circle cx="300" cy="105" r="14" fill="#059669" opacity="0.6"/>
              <text x="230" y="100" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="700">✔ Oil Slicks Digested into CO₂ + H₂O</text>
            `}
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="toggleClean">${cleaned ? 'Simulate New Oil Spill' : '🧫 Deploy Chakrabarty Superbug'}</button>
      `;

      controls.querySelector('#toggleClean').onclick = () => { cleaned = !cleaned; update(); };
      update();
    }

    // 16. Cells & Microbes Master Matrix Simulator
    function renderCellsMicrobesMasterMatrixSim(title, stats, canvas, controls) {
      title.textContent = "Master Comparative Synthesis Matrix";

      stats.innerHTML = `
        <div class="stat-pill">Chapter: <strong>Cell Structure & Microorganisms</strong></div>
        <div class="stat-pill">Focus: <strong>Universal Biological Laws</strong></div>
      `;

      canvas.innerHTML = `
        <div style="width:100%; height:100%; overflow-y:auto; padding:0.75rem;">
          <div style="display:grid; grid-template-columns:1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-emerald);">Hooke (1665) & Leeuwenhoek (1670s)</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Coined 'cell' from cork; first saw living bacteria and red blood cells.</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-cyan);">Cell Membrane, Cytoplasm, Nucleus</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Porous barrier, metabolic reaction soup, and master genetic control center.</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-amber);">Plant Specifics vs Bacterial Nucleoid</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Cellulose wall, chloroplasts, giant vacuole vs un-enclosed bacterial nucleoid.</div>
            </div>
            <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.6rem;">
              <strong style="color:var(--accent-purple);">Microbial Ecology & Dr. Chakrabarty</strong>
              <div style="font-size:0.75rem; color:#cbd5e1;">Biogas, yeast bread, lactobacillus curd, Atharvaveda Krimi, and oil-eating superbug patent.</div>
            </div>
          </div>
        </div>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Synthesis matrix unifying historical discovery, organelle functions, and microbial biotechnology applications.
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

out_path = "public/animations/class8-science-cells-microbes.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully generated {out_path} ({len(final_html.encode('utf-8'))} bytes).")

