# Class 8 Science Chapter 1: Microbes and Health
# Master Builder Script: Compiles 20-slide animated lab into public/animations/class8-science-microbes-health.html

import json
import sys
sys.path.insert(0, '.agents')
from class8_science_microbes_health_data import SLIDES_DATA, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 1: Microbes and Health Master Lab</title>
  
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
      --accent-indigo: #6366f1;
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
      background: radial-gradient(circle at top right, #082f49 0%, #070d18 70%);
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
      background: linear-gradient(135deg, #06b6d4, #10b981);
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
      background: linear-gradient(to right, #67e8f9, #a7f3d0);
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
      background: linear-gradient(135deg, #0891b2, #059669);
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
      background: linear-gradient(135deg, #0e7490, #047857);
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
      to { transform: scale(1.08); box-shadow: 0 0 20px rgba(16, 185, 129, 0.8); }
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
      <div class="brand-icon">🔬</div>
      <div>
        <div class="brand-title">Class 8 Science • Chapter 1: Microbes and Health</div>
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
          <span class="panel-tag" id="slideBadgeTag">Microbiology Foundations</span>
          <h1 class="panel-title" id="slideHeading">The Unseen World</h1>
          <div class="panel-sub" id="slideSubheading">Discovering Tiny Organisms in Water Drop</div>
        </div>

        <!-- Teacher Voice Avatar -->
        <div class="avatar-card">
          <div class="avatar-wrapper">
            <div class="avatar-face" id="teacherAvatar">👩‍🏫</div>
          </div>
          <div>
            <div style="font-size: 0.85rem; font-weight: 700; color: var(--accent-cyan);">Dr. Ananya • Microbial Mentor</div>
            <p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.2rem;" id="narrationSummary">
              Explore the invisible world of microbes living all around and within us.
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
      <p>Congratulations! You have mastered NCERT Class 8 Science Chapter 1: Microbes and Health.</p>
    </div>
  </main>

  <!-- Footer Navigation -->
  <footer>
    <div style="font-size: 0.8rem; color: #64748b;">
      Class 8 Science • Chapter 1 • Microbes and Health Master Laboratory
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
        case 'microscope_water_drop_sim':
          renderMicroscopeWaterDropSim(title, stats, canvas, controls);
          break;
        case 'microbe_classification_morphology_sim':
          renderMicrobeClassificationSim(title, stats, canvas, controls);
          break;
        case 'pond_water_micro_ecosystem_sim':
          renderPondWaterEcosystemSim(title, stats, canvas, controls);
          break;
        case 'fermentation_lactic_alcohol_sim':
          renderFermentationSim(title, stats, canvas, controls);
          break;
        case 'nitrogen_fixation_nodule_sim':
          renderNitrogenFixationSim(title, stats, canvas, controls);
          break;
        case 'biodegradation_compost_sim':
          renderBiodegradationCompostSim(title, stats, canvas, controls);
          break;
        case 'pathogen_transmission_routes_sim':
          renderPathogenTransmissionSim(title, stats, canvas, controls);
          break;
        case 'bacterial_vs_viral_infection_sim':
          renderBacterialViralInfectionSim(title, stats, canvas, controls);
          break;
        case 'malaria_vector_life_cycle_sim':
          renderMalariaLifeCycleSim(title, stats, canvas, controls);
          break;
        case 'food_preservation_pasteurizer_sim':
          renderFoodPreservationSim(title, stats, canvas, controls);
          break;
        case 'innate_immunity_phagocytosis_sim':
          renderInnatePhagocytosisSim(title, stats, canvas, controls);
          break;
        case 'antigen_antibody_lock_key_sim':
          renderAntigenAntibodyLockKeySim(title, stats, canvas, controls);
          break;
        case 'vaccine_immune_memory_sim':
          renderVaccineImmuneMemorySim(title, stats, canvas, controls);
          break;
        case 'antibiotic_kirby_bauer_sim':
          renderAntibioticKirbyBauerSim(title, stats, canvas, controls);
          break;
        case 'lifestyle_immune_defense_sim':
          renderLifestyleImmuneDefenseSim(title, stats, canvas, controls);
          break;
        case 'microbes_health_matrix_sim':
          renderMicrobesHealthMatrixSim(title, stats, canvas, controls);
          break;
        default:
          title.textContent = 'Laboratory Visualizer';
          canvas.innerHTML = '<div style="color:#94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Virtual Microscope Water Drop Sim
    function renderMicroscopeWaterDropSim(title, stats, canvas, controls) {
      title.textContent = "Virtual Compound Microscope: Water Drop Safari";
      let mag = 400;
      let focus = 10; // 0 = perfectly sharp

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Objective: <strong>${mag}×</strong></div>
          <div class="stat-pill">Resolution: <strong>${(1000/mag).toFixed(1)} μm</strong></div>
          <div class="stat-pill">Clarity: <strong>${focus === 0 ? "Perfect" : (10 - Math.abs(focus))*10 + "%"}</strong></div>
        `;

        const blurVal = Math.abs(focus) * 0.7;

        canvas.innerHTML = `
          <div style="position:relative; width:340px; height:340px; border-radius:50%; border:6px solid #1e293b; box-shadow:0 0 30px rgba(6,182,212,0.3) inset, 0 0 20px rgba(0,0,0,0.8); overflow:hidden; background:radial-gradient(circle at center, #0284c7 0%, #032b43 70%, #02121e 100%);">
            <svg width="340" height="340" viewBox="0 0 340 340" style="filter: blur(${blurVal}px); transition: filter 0.2s ease;">
              <!-- Swimming Paramecium -->
              <g transform="translate(170, 150) rotate(-25)">
                <ellipse cx="0" cy="0" rx="42" ry="16" fill="rgba(240, 253, 250, 0.85)" stroke="#06b6d4" stroke-width="2"/>
                <ellipse cx="-10" cy="0" rx="8" ry="6" fill="#0891b2"/>
                <circle cx="20" cy="-4" r="5" fill="#f43f5e" opacity="0.8"/>
                <circle cx="-25" cy="3" r="5" fill="#f43f5e" opacity="0.8"/>
                <path d="M -42 0 Q -45 5 -42 10" stroke="#a5f3fc" stroke-width="1.5" fill="none"/>
                <!-- Cilia ring -->
                <ellipse cx="0" cy="0" rx="46" ry="20" fill="none" stroke="#67e8f9" stroke-width="1" stroke-dasharray="3,3"/>
              </g>

              <!-- Amoeba with pseudopodia -->
              <g transform="translate(90, 80)">
                <path d="M 0 0 C 20 -20 50 -10 60 10 C 70 30 50 60 30 50 C 10 40 -10 50 -20 30 C -30 10 -20 20 0 0 Z" fill="rgba(167, 243, 208, 0.75)" stroke="#10b981" stroke-width="2"/>
                <circle cx="25" cy="20" r="7" fill="#047857"/>
                <circle cx="10" cy="35" r="4" fill="#065f46"/>
              </g>

              <!-- Spirogyra green ribbon -->
              <g transform="translate(60, 220)">
                <rect x="0" y="0" width="220" height="26" rx="4" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
                <path d="M 0 13 Q 20 0 40 13 T 80 13 T 120 13 T 160 13 T 200 13" fill="none" stroke="#22c55e" stroke-width="4"/>
              </g>

              <!-- Rod bacteria -->
              <g transform="translate(240, 90)">
                <rect x="0" y="0" width="16" height="6" rx="3" fill="#fbbf24"/>
                <rect x="25" y="15" width="16" height="6" rx="3" fill="#fbbf24"/>
                <rect x="10" y="30" width="14" height="5" rx="2.5" fill="#fbbf24"/>
              </g>
            </svg>
            <!-- Eyepiece reticle & scale -->
            <div style="position:absolute; inset:0; pointer-events:none; border-radius:50%; box-shadow: inset 0 0 25px rgba(0,0,0,0.6);">
              <div style="position:absolute; bottom:18px; left:50%; transform:translateX(-50%); font-size:10px; font-weight:700; color:#cbd5e1; background:rgba(0,0,0,0.6); padding:2px 8px; border-radius:4px; border:1px solid #64748b;">
                Scale: 50 μm
              </div>
            </div>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Objective Turret:</span>
          <button class="btn" id="mag100" style="padding:0.25rem 0.6rem; font-size:0.75rem;">100×</button>
          <button class="btn btn-primary" id="mag400" style="padding:0.25rem 0.6rem; font-size:0.75rem;">400×</button>
          <button class="btn" id="mag1000" style="padding:0.25rem 0.6rem; font-size:0.75rem;">1000×</button>
        </div>
        <div class="sim-ctrl-group" style="margin-left:auto;">
          <span>Fine Focus Knob:</span>
          <input type="range" class="sim-slider" id="focusSlider" min="-10" max="10" value="${focus}" style="width:110px;">
          <button class="btn" id="autoFocusBtn" style="padding:0.25rem 0.6rem; font-size:0.75rem;">🎯 Auto-Focus</button>
        </div>
      `;

      controls.querySelector('#mag100').onclick = () => { mag = 100; update(); };
      controls.querySelector('#mag400').onclick = () => { mag = 400; update(); };
      controls.querySelector('#mag1000').onclick = () => { mag = 1000; update(); };
      controls.querySelector('#focusSlider').oninput = (e) => { focus = parseInt(e.target.value); update(); };
      controls.querySelector('#autoFocusBtn').onclick = () => {
        focus = 0;
        controls.querySelector('#focusSlider').value = 0;
        update();
      };

      update();
    }

    // 2. Microbe Classification & Morphology
    function renderMicrobeClassificationSim(title, stats, canvas, controls) {
      title.textContent = "Microbial Taxonomy: 5 Major Groups";
      let activeGroup = 'bacteria';

      const groups = {
        bacteria: {
          name: "Bacteria (Prokaryotes)",
          traits: "Single-celled • Peptidoglycan cell wall • No nucleus • 0.5–5 μm",
          desc: "Shapes: Rod-shaped (Bacilli), Spherical (Cocci), Spiral (Spirilla). Divide rapidly by binary fission.",
          color: "#f59e0b"
        },
        fungi: {
          name: "Fungi (Heterotrophs)",
          traits: "Chitin cell wall • Non-photosynthetic • Unicellular (Yeast) or Molds (Rhizopus)",
          desc: "Decompose organic material via extracellular enzymes; reproduce via airborne microscopic spores.",
          color: "#f43f5e"
        },
        protozoa: {
          name: "Protozoa (Animal-like)",
          traits: "Unicellular eukaryotes • Heterotrophic • Motile via cilia, flagella, pseudopodia",
          desc: "Includes Amoeba, Paramecium, and parasites like Plasmodium (malaria) and Entamoeba.",
          color: "#06b6d4"
        },
        algae: {
          name: "Algae (Autotrophs)",
          traits: "Chlorophyll-bearing • Cellulose cell walls • Oxygenic photosynthesis",
          desc: "Includes unicellular Chlamydomonas and filamentous green Spirogyra ribbons.",
          color: "#10b981"
        },
        virus: {
          name: "Viruses (Acellular)",
          traits: "Genetic material (DNA/RNA) in protein capsid • 20–300 nm • Non-living outside host",
          desc: "Obligate intracellular parasites. Hijack host cell ribosomes to manufacture new virions.",
          color: "#a855f7"
        }
      };

      function update() {
        const g = groups[activeGroup];
        stats.innerHTML = `
          <div class="stat-pill">Selected: <strong style="color:${g.color}">${g.name}</strong></div>
          <div class="stat-pill">${g.traits}</div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem; text-align:center;">
            <div style="width:140px; height:140px; border-radius:50%; background:rgba(255,255,255,0.03); border:3px solid ${g.color}; display:flex; align-items:center; justify-content:center; box-shadow:0 0 25px ${g.color}33; margin-bottom:1rem;">
              <svg width="120" height="120" viewBox="0 0 120 120">
                ${getGroupSVG(activeGroup, g.color)}
              </svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:700; color:${g.color}; margin-bottom:0.35rem;">${g.name}</h3>
            <p style="font-size:0.85rem; color:#cbd5e1; max-width:380px; line-height:1.45;">${g.desc}</p>
          </div>
        `;
      }

      function getGroupSVG(grp, color) {
        if (grp === 'bacteria') {
          return `
            <rect x="25" y="45" width="70" height="28" rx="14" fill="${color}33" stroke="${color}" stroke-width="3"/>
            <path d="M 95 59 C 110 50 115 70 125 60" fill="none" stroke="${color}" stroke-width="2"/>
            <circle cx="50" cy="59" r="6" fill="${color}"/>
            <circle cx="70" cy="59" r="6" fill="${color}"/>
          `;
        } else if (grp === 'fungi') {
          return `
            <path d="M 60 70 L 60 110" stroke="${color}" stroke-width="4"/>
            <circle cx="60" cy="50" r="28" fill="${color}44" stroke="${color}" stroke-width="3"/>
            <circle cx="52" cy="45" r="4" fill="${color}"/>
            <circle cx="68" cy="48" r="4" fill="${color}"/>
            <circle cx="60" cy="62" r="4" fill="${color}"/>
          `;
        } else if (grp === 'protozoa') {
          return `
            <ellipse cx="60" cy="60" rx="46" ry="22" fill="${color}33" stroke="${color}" stroke-width="3" transform="rotate(-15, 60, 60)"/>
            <circle cx="50" cy="55" r="8" fill="${color}88"/>
            <circle cx="75" cy="58" r="5" fill="#f43f5e"/>
          `;
        } else if (grp === 'algae') {
          return `
            <rect x="20" y="40" width="80" height="40" rx="6" fill="${color}22" stroke="${color}" stroke-width="3"/>
            <path d="M 20 60 Q 40 45 60 60 T 100 60" fill="none" stroke="${color}" stroke-width="4"/>
          `;
        } else {
          return `
            <!-- icosahedral capsid & tail fibers -->
            <polygon points="60,20 80,35 80,60 60,75 40,60 40,35" fill="${color}44" stroke="${color}" stroke-width="3"/>
            <line x1="60" y1="75" x2="60" y2="95" stroke="${color}" stroke-width="4"/>
            <line x1="60" y1="95" x2="45" y2="115" stroke="${color}" stroke-width="2"/>
            <line x1="60" y1="95" x2="75" y2="115" stroke="${color}" stroke-width="2"/>
            <line x1="60" y1="95" x2="60" y2="115" stroke="${color}" stroke-width="2"/>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" data-grp="bacteria">Bacteria</button>
        <button class="btn" data-grp="fungi">Fungi</button>
        <button class="btn" data-grp="protozoa">Protozoa</button>
        <button class="btn" data-grp="algae">Algae</button>
        <button class="btn" data-grp="virus">Viruses</button>
      `;

      controls.querySelectorAll('button').forEach(btn => {
        btn.onclick = () => {
          controls.querySelectorAll('button').forEach(b => b.className = 'btn');
          btn.className = 'btn btn-primary';
          activeGroup = btn.getAttribute('data-grp');
          update();
        };
      });

      update();
    }

    // 3. Pond Water Ecosystem
    function renderPondWaterEcosystemSim(title, stats, canvas, controls) {
      title.textContent = "Pond Micro-Ecosystem Simulator";
      let light = 80;
      let temp = 25;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Light: <strong>${light}%</strong></div>
          <div class="stat-pill">Water Temp: <strong>${temp}°C</strong></div>
          <div class="stat-pill">Algal Photosynthesis: <strong>${(light * 0.9).toFixed(0)}%</strong></div>
        `;

        canvas.innerHTML = `
          <div style="position:relative; width:100%; height:100%; min-height:360px; background:radial-gradient(ellipse at bottom, #022c22 0%, #031c24 60%, #020d18 100%); overflow:hidden; border-radius:12px;">
            <svg width="100%" height="100%" viewBox="0 0 460 340">
              <!-- Amoeba capturing prey -->
              <g transform="translate(100, 120)">
                <path d="M 0 0 C 30 -25 70 -10 90 20 C 105 45 80 85 45 75 C 20 70 -15 80 -30 50 C -45 20 -30 25 0 0 Z" fill="rgba(16, 185, 129, 0.45)" stroke="#10b981" stroke-width="2"/>
                <circle cx="35" cy="30" r="12" fill="#047857"/>
                <!-- Engulfed food particle -->
                <circle cx="65" cy="25" r="5" fill="#f59e0b"/>
                <text x="0" y="-12" fill="#6ee7b7" font-size="11" font-weight="700">Amoeba (Phagocytosis)</text>
              </g>

              <!-- Paramecium darting -->
              <g transform="translate(300, 80) rotate(20)">
                <ellipse cx="0" cy="0" rx="55" ry="18" fill="rgba(6, 182, 212, 0.55)" stroke="#06b6d4" stroke-width="2"/>
                <circle cx="-15" cy="0" r="8" fill="#0e7490"/>
                <text x="-35" y="-24" fill="#67e8f9" font-size="11" font-weight="700">Paramecium (Cilia)</text>
              </g>

              <!-- Oxygen bubbles rising from Spirogyra -->
              ${Array.from({length: 6}).map((_, i) => `
                <circle cx="${180 + i * 40}" cy="${220 - (light * 1.5 + i * 20) % 180}" r="${3 + (i % 3)}" fill="rgba(255,255,255,0.7)"/>
              `).join('')}

              <!-- Spirogyra ribbon at bottom -->
              <rect x="40" y="260" width="380" height="30" rx="6" fill="rgba(34, 197, 94, 0.25)" stroke="#22c55e" stroke-width="2"/>
              <path d="M 40 275 Q 70 262 100 275 T 160 275 T 220 275 T 280 275 T 340 275 T 400 275" fill="none" stroke="#16a34a" stroke-width="4"/>
              <text x="50" y="310" fill="#86efac" font-size="11" font-weight="700">Spirogyra (Green Filamentous Alga)</text>
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Sunlight Intensity:</span>
          <input type="range" class="sim-slider" id="lightSl" min="10" max="100" value="${light}" style="width:100px;">
        </div>
        <div class="sim-ctrl-group" style="margin-left:auto;">
          <span>Water Temp:</span>
          <input type="range" class="sim-slider" id="tempSl" min="10" max="45" value="${temp}" style="width:100px;">
        </div>
      `;

      controls.querySelector('#lightSl').oninput = (e) => { light = parseInt(e.target.value); update(); };
      controls.querySelector('#tempSl').oninput = (e) => { temp = parseInt(e.target.value); update(); };

      update();
    }

    // 4. Fermentation Simulator
    function renderFermentationSim(title, stats, canvas, controls) {
      title.textContent = "Fermentation Lab: Curd & Bread Yeast";
      let mode = 'curd'; // 'curd' or 'bread'
      let temp = 37;

      function update() {
        const isOptimal = (temp >= 32 && temp <= 40);
        stats.innerHTML = `
          <div class="stat-pill">Process: <strong>${mode === 'curd' ? 'Lactic Acid (Lactobacillus)' : 'Alcoholic (Yeast)'}</strong></div>
          <div class="stat-pill">Temp: <strong>${temp}°C</strong></div>
          <div class="stat-pill">Enzyme Rate: <strong style="color:${isOptimal ? '#10b981' : '#f59e0b'}">${isOptimal ? 'Optimal (100%)' : temp > 50 ? 'Denatured (0%)' : 'Sluggish'}</strong></div>
        `;

        if (mode === 'curd') {
          canvas.innerHTML = `
            <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem;">
              <svg width="340" height="260" viewBox="0 0 340 260">
                <!-- Milk/Curd Pot -->
                <path d="M 70 80 Q 70 220 170 220 Q 270 220 270 80 Z" fill="rgba(254, 243, 199, 0.85)" stroke="#d97706" stroke-width="4"/>
                <ellipse cx="170" cy="80" rx="100" ry="24" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
                
                <!-- Lactobacillus rods -->
                ${Array.from({length: 8}).map((_, i) => `
                  <rect x="${110 + (i * 22) % 120}" y="${120 + (i * 18) % 70}" width="18" height="6" rx="3" fill="#059669" transform="rotate(${i * 25}, ${110 + (i * 22) % 120}, ${120 + (i * 18) % 70})"/>
                `).join('')}

                <text x="170" y="245" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="700">
                  Lactose → Lactic Acid (pH drops from 6.6 to 4.5)
                </text>
              </svg>
            </div>
          `;
        } else {
          canvas.innerHTML = `
            <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem;">
              <svg width="340" height="260" viewBox="0 0 340 260">
                <!-- Mixing bowl -->
                <path d="M 60 120 C 60 220 280 220 280 120 Z" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
                <!-- Rising Dough Dome -->
                <ellipse cx="170" cy="130" rx="90" ry="${isOptimal ? 55 : 30}" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
                <!-- CO2 Bubbles -->
                <circle cx="140" cy="120" r="5" fill="#fff" opacity="0.8"/>
                <circle cx="180" cy="115" r="7" fill="#fff" opacity="0.8"/>
                <circle cx="205" cy="130" r="4" fill="#fff" opacity="0.8"/>
                <text x="170" y="245" text-anchor="middle" fill="#fed7aa" font-size="12" font-weight="700">
                  Glucose → Ethanol + CO₂ Gas (Trapped Bubbles Expand Dough)
                </text>
              </svg>
            </div>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="curdBtn">🥛 Curd (Lactobacillus)</button>
        <button class="btn" id="breadBtn">🍞 Bread Dough (Yeast)</button>
        <div class="sim-ctrl-group" style="margin-left:auto;">
          <span>Incubator Temp:</span>
          <input type="range" class="sim-slider" id="tempSl" min="10" max="60" value="${temp}" style="width:100px;">
        </div>
      `;

      controls.querySelector('#curdBtn').onclick = () => { mode = 'curd'; update(); };
      controls.querySelector('#breadBtn').onclick = () => { mode = 'bread'; update(); };
      controls.querySelector('#tempSl').oninput = (e) => { temp = parseInt(e.target.value); update(); };

      update();
    }

    // 5. Nitrogen Fixation Root Nodule
    function renderNitrogenFixationSim(title, stats, canvas, controls) {
      title.textContent = "Legume Root Nodule & Nitrogen Fixation";
      let fixedRate = 85;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Symbiont: <strong>Rhizobium Leguminosarum</strong></div>
          <div class="stat-pill">Atmospheric N₂: <strong>78%</strong></div>
          <div class="stat-pill">Nitrate Output: <strong>${fixedRate} kg/hectare</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 340">
            <!-- Soil line -->
            <rect x="0" y="40" width="460" height="300" fill="#18181b"/>
            <line x1="0" y1="40" x2="460" y2="40" stroke="#713f12" stroke-width="4"/>
            <text x="20" y="30" fill="#a1a1aa" font-size="11">Atmosphere (N₂ Reservoir)</text>

            <!-- Main Root -->
            <path d="M 230 40 Q 225 150 230 300" stroke="#fef08a" stroke-width="8" fill="none"/>
            <path d="M 230 110 Q 150 140 100 180" stroke="#fef08a" stroke-width="5" fill="none"/>
            <path d="M 230 160 Q 310 190 360 240" stroke="#fef08a" stroke-width="5" fill="none"/>

            <!-- Swollen Root Nodules (Pink from leghemoglobin) -->
            <circle cx="160" cy="140" r="16" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>
            <circle cx="280" cy="180" r="18" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>
            <circle cx="230" cy="220" r="15" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>

            <!-- Chemical labels -->
            <text x="145" y="145" fill="#fff" font-size="10" font-weight="700">Nodule</text>
            <text x="265" y="185" fill="#fff" font-size="10" font-weight="700">Nodule</text>

            <g transform="translate(40, 260)">
              <rect width="380" height="50" rx="8" fill="#090e1a" stroke="#06b6d4" stroke-width="1.5"/>
              <text x="190" y="24" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="700">
                N₂ (gas) + 8H⁺ + 8e⁻ → 2NH₃ (Ammonia) → NO₃⁻ (Nitrates)
              </text>
              <text x="190" y="40" text-anchor="middle" fill="#94a3b8" font-size="10">
                Absorbed by legume roots for synthesis of plant proteins
              </text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Soil Inoculation Level:</span>
          <input type="range" class="sim-slider" id="inocSl" min="20" max="150" value="${fixedRate}" style="width:120px;">
        </div>
      `;

      controls.querySelector('#inocSl').oninput = (e) => { fixedRate = parseInt(e.target.value); update(); };
      update();
    }

    // 6. Biodegradation Compost Lab
    function renderBiodegradationCompostSim(title, stats, canvas, controls) {
      title.textContent = "Composting & Biodegradability Simulator";
      let days = 1;

      function update() {
        const organicDecomposed = Math.min(100, days * 1.8);
        stats.innerHTML = `
          <div class="stat-pill">Timeline: <strong>Day ${days} of 60</strong></div>
          <div class="stat-pill">Organic Humus: <strong style="color:#10b981">${organicDecomposed.toFixed(0)}%</strong></div>
          <div class="stat-pill">Plastic Degradation: <strong style="color:#f43f5e">0.0%</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 340">
            <!-- Chamber A: Organic Peels -->
            <rect x="30" y="50" width="185" height="230" rx="10" fill="#1e1b18" stroke="#10b981" stroke-width="2"/>
            <text x="122" y="40" text-anchor="middle" fill="#86efac" font-size="12" font-weight="700">Pit A: Organic Veg Waste</text>
            
            <!-- Degraded soil color transitions from green/yellow to dark humus brown -->
            <rect x="45" y="${120 + (100 - organicDecomposed) * 0.8}" width="155" height="${140 - (100 - organicDecomposed) * 0.8}" rx="6" fill="${organicDecomposed > 70 ? '#1c1917' : '#854d0e'}"/>
            <text x="122" y="270" text-anchor="middle" fill="#fef08a" font-size="11">
              ${organicDecomposed > 80 ? '✔ Converted to Rich Humus' : 'Decomposing by Saprophytes...'}
            </text>

            <!-- Chamber B: Synthetic Plastic -->
            <rect x="245" y="50" width="185" height="230" rx="10" fill="#1e1b18" stroke="#f43f5e" stroke-width="2"/>
            <text x="337" y="40" text-anchor="middle" fill="#fda4af" font-size="12" font-weight="700">Pit B: Plastic Polythene</text>
            
            <rect x="260" y="120" width="155" height="140" rx="6" fill="#0284c7" opacity="0.85"/>
            <text x="337" y="270" text-anchor="middle" fill="#fecdd3" font-size="11">
              ✖ 0% Degradation (Non-biodegradable)
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Advance Compost Days:</span>
          <input type="range" class="sim-slider" id="daysSl" min="1" max="60" value="${days}" style="width:180px;">
          <span style="font-weight:700; color:var(--accent-cyan);" id="dayVal">Day ${days}</span>
        </div>
      `;

      controls.querySelector('#daysSl').oninput = (e) => {
        days = parseInt(e.target.value);
        controls.querySelector('#dayVal').textContent = `Day ${days}`;
        update();
      };

      update();
    }

    // 7. Pathogen Transmission Routes
    function renderPathogenTransmissionSim(title, stats, canvas, controls) {
      title.textContent = "Modes of Disease Transmission & Barrier Shields";
      let maskOn = false;
      let boilWater = false;
      let netOn = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Mask: <strong>${maskOn ? 'Active (Blocked)' : 'Inactive'}</strong></div>
          <div class="stat-pill">Boiled Water: <strong>${boilWater ? 'Active (Blocked)' : 'Inactive'}</strong></div>
          <div class="stat-pill">Bed Nets: <strong>${netOn ? 'Active (Blocked)' : 'Inactive'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 340">
            <!-- Infected Person -->
            <g transform="translate(60, 140)">
              <circle cx="0" cy="0" r="26" fill="#e11d48"/>
              <text x="0" y="5" text-anchor="middle" fill="#fff" font-size="20">🤧</text>
              <text x="0" y="42" text-anchor="middle" fill="#fda4af" font-size="11" font-weight="700">Infected Host</text>
            </g>

            <!-- Healthy Host -->
            <g transform="translate(400, 140)">
              <circle cx="0" cy="0" r="26" fill="#059669"/>
              <text x="0" y="5" text-anchor="middle" fill="#fff" font-size="20">😊</text>
              <text x="0" y="42" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="700">Healthy Host</text>
            </g>

            <!-- Route 1: Droplet Spray -->
            <path d="M 86 130 Q 230 70 374 130" stroke="${maskOn ? '#10b981' : '#f43f5e'}" stroke-width="${maskOn ? 1.5 : 3.5}" stroke-dasharray="${maskOn ? '4,4' : 'none'}" fill="none"/>
            <text x="230" y="85" text-anchor="middle" fill="${maskOn ? '#6ee7b7' : '#fda4af'}" font-size="10" font-weight="700">
              ${maskOn ? '🛡 Droplets Blocked by Mask' : 'Airborne Droplets (Cold, TB, Flu)'}
            </text>

            <!-- Route 2: Waterborne -->
            <path d="M 86 160 Q 230 230 374 160" stroke="${boilWater ? '#10b981' : '#0284c7'}" stroke-width="${boilWater ? 1.5 : 3.5}" stroke-dasharray="${boilWater ? '4,4' : 'none'}" fill="none"/>
            <text x="230" y="225" text-anchor="middle" fill="${boilWater ? '#6ee7b7' : '#7dd3fc'}" font-size="10" font-weight="700">
              ${boilWater ? '🛡 Water Purified by Boiling' : 'Waterborne Pathogens (Cholera, Typhoid)'}
            </text>

            <!-- Route 3: Vector Mosquito -->
            <path d="M 86 145 L 374 145" stroke="${netOn ? '#10b981' : '#f59e0b'}" stroke-width="${netOn ? 1.5 : 3.5}" stroke-dasharray="${netOn ? '4,4' : 'none'}" fill="none"/>
            <text x="230" y="140" text-anchor="middle" fill="${netOn ? '#6ee7b7' : '#fde047'}" font-size="10" font-weight="700">
              ${netOn ? '🛡 Vector Blocked by Mosquito Net' : 'Mosquito Vector (Malaria, Dengue)'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="maskToggle">😷 Toggle Mask</button>
        <button class="btn" id="waterToggle">🚰 Toggle Boiled Water</button>
        <button class="btn" id="netToggle">🛏 Toggle Mosquito Net</button>
      `;

      controls.querySelector('#maskToggle').onclick = () => { maskOn = !maskOn; update(); };
      controls.querySelector('#waterToggle').onclick = () => { boilWater = !boilWater; update(); };
      controls.querySelector('#netToggle').onclick = () => { netOn = !netOn; update(); };

      update();
    }

    // 8. Bacterial vs Viral Infection
    function renderBacterialViralInfectionSim(title, stats, canvas, controls) {
      title.textContent = "Bacterial Binary Fission vs Viral Lytic Takeover";
      let activeTab = 'bacteria';

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Type: <strong>${activeTab === 'bacteria' ? 'Cellular Binary Fission' : 'Acellular Lytic Hijack'}</strong></div>
          <div class="stat-pill">Replication: <strong>${activeTab === 'bacteria' ? 'Independent' : 'Host-dependent'}</strong></div>
        `;

        if (activeTab === 'bacteria') {
          canvas.innerHTML = `
            <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <svg width="400" height="260" viewBox="0 0 400 260">
                <!-- Step 1: Single bacterium -->
                <rect x="30" y="100" width="70" height="28" rx="14" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
                <text x="65" y="150" text-anchor="middle" fill="#fed7aa" font-size="10">1. Elongation</text>
                
                <text x="120" y="118" fill="#fbbf24" font-size="18">→</text>

                <!-- Step 2: Pinching septum -->
                <g transform="translate(150, 95)">
                  <path d="M 0 16 C 0 5 15 0 35 0 C 55 0 70 5 70 16 C 70 25 60 30 50 24 C 40 18 30 18 20 24 C 10 30 0 25 0 16 Z" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
                  <text x="35" y="55" text-anchor="middle" fill="#fed7aa" font-size="10">2. Septum Form</text>
                </g>

                <text x="240" y="118" fill="#fbbf24" font-size="18">→</text>

                <!-- Step 3: Two distinct daughters -->
                <g transform="translate(270, 80)">
                  <rect x="0" y="0" width="60" height="24" rx="12" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
                  <rect x="0" y="35" width="60" height="24" rx="12" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
                  <text x="30" y="80" text-anchor="middle" fill="#fed7aa" font-size="10">3. Two Daughters</text>
                </g>
              </svg>
            </div>
          `;
        } else {
          canvas.innerHTML = `
            <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <svg width="420" height="260" viewBox="0 0 420 260">
                <!-- Host cell outline -->
                <rect x="50" y="80" width="320" height="130" rx="20" fill="rgba(15, 23, 42, 0.6)" stroke="#a855f7" stroke-width="2.5"/>
                <text x="210" y="105" text-anchor="middle" fill="#c084fc" font-size="12" font-weight="700">Host Cell (Human/Bacterial Cell)</text>

                <!-- 1. Virus attachment -->
                <circle cx="80" cy="55" r="14" fill="#9333ea" stroke="#d8b4fe" stroke-width="2"/>
                <text x="80" y="32" text-anchor="middle" fill="#e9d5ff" font-size="9">1. Attach & Inject</text>

                <!-- 2. Viral replication inside -->
                <g transform="translate(190, 130)">
                  <circle cx="-25" cy="0" r="10" fill="#9333ea"/>
                  <circle cx="0" cy="-10" r="10" fill="#9333ea"/>
                  <circle cx="25" cy="0" r="10" fill="#9333ea"/>
                  <text x="0" y="28" text-anchor="middle" fill="#e9d5ff" font-size="9">2. Commandeer Ribosomes</text>
                </g>

                <!-- 3. Cell lysis burst -->
                <g transform="translate(340, 130)">
                  <circle cx="15" cy="-20" r="10" fill="#9333ea"/>
                  <circle cx="20" cy="20" r="10" fill="#9333ea"/>
                  <text x="10" y="45" text-anchor="middle" fill="#e9d5ff" font-size="9">3. Lysis & Release</text>
                </g>
              </svg>
            </div>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="bactTab">🧫 Bacteria: Binary Fission</button>
        <button class="btn" id="virusTab">🧬 Virus: Lytic Takeover</button>
      `;

      controls.querySelector('#bactTab').onclick = () => { activeTab = 'bacteria'; update(); };
      controls.querySelector('#virusTab').onclick = () => { activeTab = 'virus'; update(); };

      update();
    }

    // 9. Malaria Vector Life Cycle
    function renderMalariaLifeCycleSim(title, stats, canvas, controls) {
      title.textContent = "Plasmodium Malaria Life Cycle";
      let stage = 1;

      const stages = [
        { title: "Stage 1: Mosquito Inoculation", desc: "Female Anopheles bites human and injects motile sporozoites with saliva." },
        { title: "Stage 2: Liver Schizogony", desc: "Sporozoites travel to the liver, invade hepatocytes, and multiply into merozoites." },
        { title: "Stage 3: Red Blood Cell Lysis", desc: "Merozoites invade RBCs, replicate, and burst cells, releasing toxic hemozoin." },
        { title: "Stage 4: Chills & Fever Cycle", desc: "Hemozoin release triggers recurring spikes of high fever and shivering chills." }
      ];

      function update() {
        const cur = stages[stage - 1];
        stats.innerHTML = `
          <div class="stat-pill">Current: <strong>${cur.title}</strong></div>
          <div class="stat-pill">Primary Host: <strong>Human & Mosquito</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1rem; text-align:center;">
            <svg width="400" height="230" viewBox="0 0 400 230">
              <!-- Circular progression ring -->
              <circle cx="200" cy="115" r="85" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="4"/>
              
              <!-- 4 node markers -->
              <circle cx="200" cy="30" r="${stage === 1 ? 18 : 12}" fill="${stage === 1 ? '#f43f5e' : '#475569'}"/>
              <text x="200" y="35" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">1</text>

              <circle cx="285" cy="115" r="${stage === 2 ? 18 : 12}" fill="${stage === 2 ? '#f43f5e' : '#475569'}"/>
              <text x="285" y="120" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">2</text>

              <circle cx="200" cy="200" r="${stage === 3 ? 18 : 12}" fill="${stage === 3 ? '#f43f5e' : '#475569'}"/>
              <text x="200" y="205" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">3</text>

              <circle cx="115" cy="115" r="${stage === 4 ? 18 : 12}" fill="${stage === 4 ? '#f43f5e' : '#475569'}"/>
              <text x="115" y="120" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">4</text>

              <!-- Center descriptive graphic -->
              <circle cx="200" cy="115" r="45" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
              <text x="200" y="112" text-anchor="middle" fill="#fda4af" font-size="11" font-weight="700">Plasmodium</text>
              <text x="200" y="128" text-anchor="middle" fill="#94a3b8" font-size="9">Hemozoin Toxin</text>
            </svg>
            <p style="font-size:0.85rem; color:#fecdd3; margin-top:0.5rem; max-width:400px;">${cur.desc}</p>
          </div>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="s1">1. Mosquito Bite</button>
        <button class="btn" id="s2">2. Liver Invasion</button>
        <button class="btn" id="s3">3. RBC Rupture</button>
        <button class="btn" id="s4">4. Hemozoin Fever</button>
      `;

      controls.querySelector('#s1').onclick = () => { stage = 1; update(); };
      controls.querySelector('#s2').onclick = () => { stage = 2; update(); };
      controls.querySelector('#s3').onclick = () => { stage = 3; update(); };
      controls.querySelector('#s4').onclick = () => { stage = 4; update(); };

      update();
    }

    // 10. Food Preservation Pasteurizer
    function renderFoodPreservationSim(title, stats, canvas, controls) {
      title.textContent = "Food Preservation: Pasteurization Thermal Shock";
      let method = 'pasteur'; // 'pasteur' or 'salt'

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Technique: <strong>${method === 'pasteur' ? 'Pasteurization (HTST)' : 'Osmotic Salt Dehydration'}</strong></div>
          <div class="stat-pill">Bacteria Kill: <strong>99.9%</strong></div>
        `;

        if (method === 'pasteur') {
          canvas.innerHTML = `
            <svg width="100%" height="100%" viewBox="0 0 460 300">
              <!-- Heating Zone 72C -->
              <rect x="40" y="60" width="160" height="180" rx="12" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="2"/>
              <text x="120" y="90" text-anchor="middle" fill="#fda4af" font-size="12" font-weight="700">Rapid Heat: 70°C–72°C</text>
              <text x="120" y="110" text-anchor="middle" fill="#cbd5e1" font-size="10">Duration: 15–30 Seconds</text>
              <text x="120" y="160" text-anchor="middle" fill="#f43f5e" font-size="28">🔥</text>
              <text x="120" y="210" text-anchor="middle" fill="#fecdd3" font-size="10">Kills Vegetative Pathogens</text>

              <line x1="210" y1="150" x2="250" y2="150" stroke="#fff" stroke-width="4" stroke-dasharray="4,4"/>

              <!-- Sudden Chilling Zone 4C -->
              <rect x="260" y="60" width="160" height="180" rx="12" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="2"/>
              <text x="340" y="90" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="700">Instant Chill: &lt; 10°C</text>
              <text x="340" y="110" text-anchor="middle" fill="#cbd5e1" font-size="10">Shock Preservation</text>
              <text x="340" y="160" text-anchor="middle" fill="#06b6d4" font-size="28">❄️</text>
              <text x="340" y="210" text-anchor="middle" fill="#a5f3fc" font-size="10">Stops Spore Germination</text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <svg width="400" height="240" viewBox="0 0 400 240">
                <!-- Hypertonic salt solution -->
                <rect x="50" y="30" width="300" height="180" rx="14" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
                <text x="200" y="55" text-anchor="middle" fill="#bae6fd" font-size="12" font-weight="700">Hypertonic Saline Environment (Pickles)</text>
                
                <!-- Shriveling bacterial cell (Plasmolysis) -->
                <rect x="150" y="90" width="100" height="50" rx="20" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="3,3"/>
                <rect x="165" y="100" width="70" height="30" rx="12" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
                
                <!-- Water exiting arrows -->
                <path d="M 180 95 L 180 75" stroke="#38bdf8" stroke-width="2"/>
                <path d="M 220 95 L 220 75" stroke="#38bdf8" stroke-width="2"/>
                <text x="200" y="70" text-anchor="middle" fill="#38bdf8" font-size="9">H₂O Exosmosis</text>

                <text x="200" y="180" text-anchor="middle" fill="#fed7aa" font-size="11" font-weight="700">
                  Plasmolysis: Cell dehydrates & stops metabolism
                </text>
              </svg>
            </div>
          `;
        }
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="pBtn">🥛 Pasteurization</button>
        <button class="btn" id="sBtn">🧂 Salt Plasmolysis (Pickles)</button>
      `;

      controls.querySelector('#pBtn').onclick = () => { method = 'pasteur'; update(); };
      controls.querySelector('#sBtn').onclick = () => { method = 'salt'; update(); };

      update();
    }

    // 11. Innate Immunity & Phagocytosis
    function renderInnatePhagocytosisSim(title, stats, canvas, controls) {
      title.textContent = "Innate Immunity: Macrophage Phagocytosis";
      let step = 1;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Immune Cell: <strong>Macrophage (Phagocyte)</strong></div>
          <div class="stat-pill">Target: <strong>Bacterial Pathogen</strong></div>
          <div class="stat-pill">Step: <strong>${step} of 4</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 300">
            <!-- Macrophage cell body -->
            <g transform="translate(180, 150)">
              ${step === 1 ? `
                <circle cx="0" cy="0" r="65" fill="rgba(16, 185, 129, 0.4)" stroke="#10b981" stroke-width="3"/>
                <!-- Separate bacterium -->
                <rect x="90" y="-8" width="22" height="12" rx="6" fill="#f59e0b"/>
                <text x="0" y="95" text-anchor="middle" fill="#6ee7b7" font-size="12">1. Chemotaxis: Detecting Foreign Pathogen</text>
              ` : step === 2 ? `
                <!-- Extending pseudopodia -->
                <path d="M -50 -30 C -20 -70 40 -60 70 -20 C 85 0 95 15 80 30 C 65 40 40 60 -10 65 C -50 60 -70 20 -50 -30 Z" fill="rgba(16, 185, 129, 0.5)" stroke="#10b981" stroke-width="3"/>
                <rect x="60" y="-5" width="20" height="10" rx="5" fill="#f59e0b"/>
                <text x="0" y="95" text-anchor="middle" fill="#6ee7b7" font-size="12">2. Pseudopodia Engulfing Bacterium</text>
              ` : step === 3 ? `
                <circle cx="0" cy="0" r="65" fill="rgba(16, 185, 129, 0.5)" stroke="#10b981" stroke-width="3"/>
                <!-- Enclosed inside phagosome -->
                <circle cx="20" cy="0" r="16" fill="none" stroke="#fff" stroke-width="1.5"/>
                <rect x="12" y="-4" width="16" height="8" rx="4" fill="#f59e0b"/>
                <text x="0" y="95" text-anchor="middle" fill="#6ee7b7" font-size="12">3. Phagosome Fusion with Lysosome</text>
              ` : `
                <circle cx="0" cy="0" r="65" fill="rgba(16, 185, 129, 0.5)" stroke="#10b981" stroke-width="3"/>
                <!-- Degraded fragments -->
                <circle cx="15" cy="-5" r="3" fill="#94a3b8"/>
                <circle cx="25" cy="5" r="2.5" fill="#94a3b8"/>
                <text x="0" y="95" text-anchor="middle" fill="#6ee7b7" font-size="12">4. Acid Hydrolases Digest Pathogen</text>
              `}
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn" id="p1">1. Approach</button>
        <button class="btn" id="p2">2. Engulf</button>
        <button class="btn" id="p3">3. Phagosome</button>
        <button class="btn" id="p4">4. Digestion</button>
      `;

      controls.querySelector('#p1').onclick = () => { step = 1; update(); };
      controls.querySelector('#p2').onclick = () => { step = 2; update(); };
      controls.querySelector('#p3').onclick = () => { step = 3; update(); };
      controls.querySelector('#p4').onclick = () => { step = 4; update(); };

      update();
    }

    // 12. Antigen Antibody Lock-and-Key
    function renderAntigenAntibodyLockKeySim(title, stats, canvas, controls) {
      title.textContent = "Antigen-Antibody Specificity";
      let bound = false;

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Weapon: <strong>Y-Shaped Immunoglobulin (IgG)</strong></div>
          <div class="stat-pill">Binding: <strong style="color:${bound ? '#10b981' : '#f59e0b'}">${bound ? 'Locked & Neutralized' : 'Free Unbound'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 300">
            <!-- Bacterium with specific surface antigens -->
            <g transform="translate(120, 150)">
              <rect x="-40" y="-20" width="80" height="40" rx="20" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
              <!-- Triangle epitope on surface -->
              <polygon points="40,-5 55,0 40,5" fill="#f43f5e"/>
              <text x="0" y="38" text-anchor="middle" fill="#fef08a" font-size="11" font-weight="700">Antigen Epitope</text>
            </g>

            <!-- Y-shaped antibody moving in -->
            <g transform="translate(${bound ? 175 : 300}, 150) transition: transform 0.4s ease;">
              <!-- Stem -->
              <line x1="0" y1="0" x2="40" y2="0" stroke="#06b6d4" stroke-width="5"/>
              <!-- Y forks -->
              <line x1="0" y1="0" x2="-25" y2="-20" stroke="#06b6d4" stroke-width="5"/>
              <line x1="0" y1="0" x2="-25" y2="20" stroke="#06b6d4" stroke-width="5"/>
              <!-- Binding clefts -->
              <polygon points="-25,-20 -35,-25 -30,-15" fill="#10b981"/>
              <polygon points="-25,20 -35,25 -30,15" fill="#10b981"/>
              <text x="20" y="-15" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="700">Antibody (IgG)</text>
            </g>

            <text x="230" y="260" text-anchor="middle" fill="#94a3b8" font-size="11">
              ${bound ? '✔ Neutralization Complete: Blocks pathogen from docking onto host tissue receptors' : 'Click "Engage Neutralization" to dock antibody into matching epitope'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn btn-primary" id="bindToggle">${bound ? 'Release Antibody' : '🔒 Engage Neutralization'}</button>
      `;

      controls.querySelector('#bindToggle').onclick = () => {
        bound = !bound;
        update();
      };

      update();
    }

    // 13. Vaccine & Herd Immunity
    function renderVaccineImmuneMemorySim(title, stats, canvas, controls) {
      title.textContent = "Vaccine Titer Curve & Herd Immunity";
      let herdPct = 90;

      function update() {
        const isProtected = herdPct >= 85;
        stats.innerHTML = `
          <div class="stat-pill">Immunized: <strong>${herdPct}%</strong></div>
          <div class="stat-pill">Community Status: <strong style="color:${isProtected ? '#10b981' : '#f43f5e'}">${isProtected ? 'Protected by Herd Immunity' : 'Vulnerable to Epidemic Outbreak'}</strong></div>
        `;

        canvas.innerHTML = `
          <svg width="100%" height="100%" viewBox="0 0 460 300">
            <!-- Grid population dots -->
            <g transform="translate(60, 40)">
              ${Array.from({length: 40}).map((_, i) => {
                const isVaccinated = i < (herdPct * 0.4);
                const col = i % 8;
                const row = Math.floor(i / 8);
                return `
                  <circle cx="${col * 42}" cy="${row * 35}" r="12" fill="${isVaccinated ? '#10b981' : '#f43f5e'}" opacity="0.85"/>
                  <text x="${col * 42}" y="${row * 35 + 4}" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">${isVaccinated ? '✔' : '!'}</text>
                `;
              }).join('')}
            </g>

            <rect x="60" y="230" width="340" height="40" rx="8" fill="#0f172a" stroke="${isProtected ? '#10b981' : '#f43f5e'}" stroke-width="1.5"/>
            <text x="230" y="255" text-anchor="middle" fill="${isProtected ? '#6ee7b7' : '#fda4af'}" font-size="11" font-weight="700">
              ${isProtected ? 'Threshold >85%: Pathogen cannot find transmission chain' : 'Threshold <85%: Virus spreads rapidly to unprotected individuals'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Vaccinated Percentage:</span>
          <input type="range" class="sim-slider" id="herdSl" min="20" max="100" value="${herdPct}" style="width:140px;">
          <span style="font-weight:700; color:var(--accent-cyan);">${herdPct}%</span>
        </div>
      `;

      controls.querySelector('#herdSl').oninput = (e) => { herdPct = parseInt(e.target.value); update(); };
      update();
    }

    // 14. Antibiotic Kirby-Bauer Disc Diffusion
    function renderAntibioticKirbyBauerSim(title, stats, canvas, controls) {
      title.textContent = "Kirby-Bauer Antibiotic Sensitivity Test";

      stats.innerHTML = `
        <div class="stat-pill">Plate: <strong>Nutrient Agar Lawn</strong></div>
        <div class="stat-pill">Zone of Inhibition: <strong>Halo indicates bacterial death</strong></div>
      `;

      canvas.innerHTML = `
        <svg width="100%" height="100%" viewBox="0 0 460 300">
          <!-- Petri dish -->
          <circle cx="230" cy="150" r="115" fill="#fef3c7" opacity="0.3" stroke="#cbd5e1" stroke-width="4"/>
          <!-- Bacterial lawn texture -->
          <circle cx="230" cy="150" r="110" fill="#fef08a" opacity="0.6"/>

          <!-- Disc 1: Penicillin (Large zone) -->
          <circle cx="170" cy="110" r="32" fill="#070d18" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
          <circle cx="170" cy="110" r="12" fill="#fff" stroke="#64748b"/>
          <text x="170" y="114" text-anchor="middle" fill="#0f172a" font-size="8" font-weight="700">PEN</text>
          <text x="170" y="70" text-anchor="middle" fill="#67e8f9" font-size="9" font-weight="700">Zone: 28 mm (Sensitive)</text>

          <!-- Disc 2: Streptomycin (Medium zone) -->
          <circle cx="290" cy="110" r="22" fill="#070d18" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3,3"/>
          <circle cx="290" cy="110" r="12" fill="#fff" stroke="#64748b"/>
          <text x="290" y="114" text-anchor="middle" fill="#0f172a" font-size="8" font-weight="700">STR</text>

          <!-- Disc 3: Resistant Strain (No zone) -->
          <circle cx="230" cy="200" r="12" fill="#fff" stroke="#64748b"/>
          <text x="230" y="204" text-anchor="middle" fill="#0f172a" font-size="8" font-weight="700">TET</text>
          <text x="230" y="225" text-anchor="middle" fill="#f43f5e" font-size="9" font-weight="700">Zone: 0 mm (Resistant Superbug)</text>
        </svg>
      `;

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Clear halo zones represent effective bacterial destruction. Disc with 0mm zone demonstrates antibiotic resistance.
        </div>
      `;
    }

    // 15. Lifestyle Defense
    function renderLifestyleImmuneDefenseSim(title, stats, canvas, controls) {
      title.textContent = "Lifestyle Immune Strength Dashboard";
      let nutrition = 80;
      let sleep = 80;
      let hygiene = 90;

      function update() {
        const score = Math.round((nutrition * 0.35) + (sleep * 0.3) + (hygiene * 0.35));
        stats.innerHTML = `
          <div class="stat-pill">Immune Readiness: <strong style="color:${score > 75 ? '#10b981' : '#f59e0b'}">${score}%</strong></div>
          <div class="stat-pill">Protection Level: <strong>${score > 75 ? 'Fortress Grade' : 'Vulnerable'}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1.5rem;">
            <svg width="340" height="220" viewBox="0 0 340 220">
              <!-- Radial Meter -->
              <circle cx="170" cy="130" r="80" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="16"/>
              <circle cx="170" cy="130" r="80" fill="none" stroke="${score > 75 ? '#10b981' : '#f59e0b'}" stroke-width="16" stroke-dasharray="502" stroke-dashoffset="${502 - (score / 100) * 251}" transform="rotate(-180, 170, 130)"/>
              
              <text x="170" y="125" text-anchor="middle" fill="#fff" font-size="32" font-weight="800">${score}%</text>
              <text x="170" y="150" text-anchor="middle" fill="#94a3b8" font-size="11">Immune Competence</text>
            </svg>
          </div>
        `;
      }

      controls.innerHTML = `
        <div class="sim-ctrl-group">
          <span>Diet (Proteins & Vit C):</span>
          <input type="range" class="sim-slider" id="nutSl" min="20" max="100" value="${nutrition}" style="width:70px;">
        </div>
        <div class="sim-ctrl-group">
          <span>Sleep (8 hrs):</span>
          <input type="range" class="sim-slider" id="slpSl" min="20" max="100" value="${sleep}" style="width:70px;">
        </div>
        <div class="sim-ctrl-group">
          <span>Hand Hygiene:</span>
          <input type="range" class="sim-slider" id="hygSl" min="20" max="100" value="${hygiene}" style="width:70px;">
        </div>
      `;

      controls.querySelector('#nutSl').oninput = (e) => { nutrition = parseInt(e.target.value); update(); };
      controls.querySelector('#slpSl').oninput = (e) => { sleep = parseInt(e.target.value); update(); };
      controls.querySelector('#hygSl').oninput = (e) => { hygiene = parseInt(e.target.value); update(); };

      update();
    }

    // 16. Microbes Health Matrix Sim
    function renderMicrobesHealthMatrixSim(title, stats, canvas, controls) {
      title.textContent = "Interactive Master Synthesis Matrix";
      let filter = 'all';

      const items = [
        { grp: "Bacteria", role: "Curd (Lactobacillus), BNF (Rhizobium)", dis: "TB, Cholera, Typhoid", treat: "Antibiotics & Vaccines" },
        { grp: "Fungi", role: "Yeast (Baking), Penicillin mold", dis: "Ringworm, Athlete's foot", treat: "Antifungals & Dryness" },
        { grp: "Protozoa", role: "Aquatic food chain baseline", dis: "Malaria, Dysentery", treat: "Vector control, Antimalarials" },
        { grp: "Viruses", role: "Biotechnology & Phage therapy", dis: "Polio, Flu, Dengue", treat: "Vaccines, Soap & Water" }
      ];

      function update() {
        stats.innerHTML = `
          <div class="stat-pill">Filter: <strong>${filter.toUpperCase()}</strong></div>
          <div class="stat-pill">Total Categories: <strong>${items.length}</strong></div>
        `;

        canvas.innerHTML = `
          <div style="width:100%; height:100%; overflow-y:auto; padding:1rem;">
            <div style="display:grid; grid-template-columns:1fr; gap:0.6rem;">
              ${items.map(it => `
                <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:0.75rem;">
                  <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem;">
                    <strong style="color:var(--accent-cyan); font-size:0.9rem;">${it.grp}</strong>
                    <span style="font-size:0.75rem; color:#10b981;">Defense: ${it.treat}</span>
                  </div>
                  <div style="font-size:0.75rem; color:#cbd5e1;">Beneficial: ${it.role}</div>
                  <div style="font-size:0.75rem; color:#fca5a5;">Infections: ${it.dis}</div>
                </div>
              `).join('')}
            </div>
          </div>
        `;
      }

      controls.innerHTML = `
        <div style="font-size:0.75rem; color:#94a3b8;">
          Matrix correlates microbial kingdoms with industrial benefits, human diseases, and clinical defenses.
        </div>
      `;

      update();
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

out_path = "public/animations/class8-science-microbes-health.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully generated {out_path} ({len(final_html.encode('utf-8'))} bytes).")

