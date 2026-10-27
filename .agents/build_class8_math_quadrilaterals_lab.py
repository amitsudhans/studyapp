import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_quadrilaterals_data import slides_data, quiz_questions

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 4: Quadrilaterals Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="triggerMathRender(document.body);"></script>

  <style>
    :root {{
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
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: radial-gradient(circle at top right, #1e1b4b 0%, #070b14 65%);
      color: var(--text-main);
      font-family: var(--font-stack);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* KaTeX equation enhancements */
    .katex {{
      font-size: 1.08em;
      color: inherit;
    }}
    .katex-display {{
      margin: 0.6em 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 4px 0;
    }}
    .katex-display > .katex {{
      white-space: normal;
    }}

    /* Header Nav */
    header {{
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .header-badge {{
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 20px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 700;
      color: #e2e8f0;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .slide-indicator {{
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(99, 102, 241, 0.3);
      padding: 5px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      color: var(--accent-cyan);
    }}

    .speech-btn {{
      background: rgba(99, 102, 241, 0.2);
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
    }}
    .speech-btn:hover {{
      background: rgba(99, 102, 241, 0.35);
      color: #fff;
    }}
    .speech-btn.speaking {{
      background: rgba(244, 63, 94, 0.25);
      border-color: var(--accent-rose);
      color: #fecdd3;
      animation: pulse 1.5s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.03); }}
    }}

    /* Main Container */
    main {{
      flex: 1;
      max-width: 1380px;
      width: 100%;
      margin: 0 auto;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* Slide Header Card */
    .slide-header {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }}

    .slide-tag {{
      color: var(--accent-amber);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }}

    .slide-title {{
      font-size: 26px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 6px;
      line-height: 1.25;
    }}

    .slide-subtitle {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Two Column Layout for Lessons */
    .lesson-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }}
    @media (max-width: 1024px) {{
      .lesson-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Theory Left Column */
    .theory-panel {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .lead-p {{
      font-size: 15px;
      line-height: 1.65;
      color: #cbd5e1;
    }}

    .theory-box {{
      background: rgba(30, 41, 59, 0.7);
      border-left: 4px solid var(--accent-indigo);
      border-radius: 0 12px 12px 0;
      padding: 16px 20px;
    }}
    .theory-box h4 {{
      font-size: 16px;
      font-weight: 700;
      color: #e2e8f0;
      margin-bottom: 8px;
    }}
    .theory-box p, .theory-box li {{
      font-size: 13.5px;
      line-height: 1.6;
      color: #94a3b8;
    }}
    .theory-box ul, .theory-box ol {{
      margin-left: 20px;
      margin-top: 6px;
    }}

    .formula-box {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(6, 182, 212, 0.3);
      border-radius: 12px;
      padding: 18px 20px;
    }}
    .formula-box h4 {{
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .formula-box p, .formula-box li {{
      font-size: 13.5px;
      line-height: 1.6;
      color: #cbd5e1;
    }}

    /* Right Column: Simulator & Checkpoints */
    .sim-panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .sim-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sim-head h3 {{
      font-size: 16px;
      font-weight: 700;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .sim-badge {{
      font-size: 11px;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 3px 8px;
      border-radius: 6px;
    }}

    .sim-viewport {{
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 12px;
      min-height: 300px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 16px;
      position: relative;
      overflow: hidden;
    }}

    .sim-controls {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      justify-content: center;
      padding-top: 6px;
    }}

    .sim-btn {{
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid #475569;
      color: #e2e8f0;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .sim-btn:hover {{
      background: var(--accent-indigo);
      border-color: var(--accent-indigo);
      color: #fff;
    }}
    .sim-btn.active {{
      background: var(--accent-indigo);
      border-color: #818cf8;
      color: #fff;
    }}

    .sim-slider-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12.5px;
      color: #cbd5e1;
    }}
    .sim-slider-group input[type="range"] {{
      accent-color: var(--accent-cyan);
      cursor: pointer;
    }}

    /* In-Slide Checkpoint Section */
    .checkpoint-section {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .checkpoint-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-amber);
    }}

    .checkpoint-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .checkpoint-q {{
      font-size: 13.5px;
      font-weight: 600;
      color: #e2e8f0;
      line-height: 1.45;
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}
    @media (max-width: 640px) {{
      .options-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .opt-btn {{
      background: #1e293b;
      border: 1px solid #475569;
      color: #cbd5e1;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12.5px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
      line-height: 1.35;
    }}
    .opt-btn:hover:not(:disabled) {{
      background: #334155;
      border-color: #64748b;
      color: #fff;
    }}
    .opt-btn.correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #6ee7b7 !important;
      font-weight: 700;
    }}
    .opt-btn.wrong {{
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fda4af !important;
    }}

    .feedback-box {{
      font-size: 12.5px;
      padding: 10px 14px;
      border-radius: 8px;
      display: none;
      line-height: 1.5;
    }}
    .feedback-box.show {{
      display: block;
    }}

    /* Teacher Persona Card */
    .teacher-card {{
      background: linear-gradient(135deg, rgba(30, 27, 75, 0.8), rgba(15, 23, 42, 0.95));
      border: 1px solid rgba(99, 102, 241, 0.4);
      border-radius: 16px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .avatar-wrapper {{
      position: relative;
      width: 68px;
      height: 68px;
      flex-shrink: 0;
    }}

    .avatar-svg {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 2px solid var(--accent-cyan);
      background: #0f172a;
    }}

    .mouth-open {{
      display: none;
    }}
    .speaking .mouth-open {{
      display: block;
    }}
    .speaking .mouth-closed {{
      display: none;
    }}

    .teacher-speech {{
      flex: 1;
      font-size: 13.5px;
      line-height: 1.55;
      color: #e2e8f0;
      font-style: italic;
    }}

    .teacher-role {{
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}

    /* Sticky Bottom Footer */
    footer {{
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--card-border);
      position: sticky;
      bottom: 0;
      z-index: 100;
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .nav-btn {{
      background: var(--accent-indigo);
      border: none;
      color: #fff;
      padding: 10px 22px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .nav-btn:hover:not(:disabled) {{
      background: #4338ca;
      transform: translateY(-1px);
    }}
    .nav-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      background: #334155;
    }}

    .last-slide-notice {{
      display: none;
      color: #f59e0b;
      font-weight: 800;
      font-size: 13.5px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 8px 18px;
      border-radius: 8px;
      animation: pulse 2s infinite;
    }}

    /* Quiz Full-Width Layout (Slides 17 to 20) */
    .quiz-container {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      width: 100%;
    }}

    .quiz-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .quiz-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .quiz-badge {{
      background: rgba(99, 102, 241, 0.2);
      color: #a5b4fc;
      border: 1px solid rgba(99, 102, 241, 0.4);
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
    }}

    .sol-btn {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--accent-amber);
      color: #fcd34d;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .sol-btn:hover {{
      background: rgba(245, 158, 11, 0.3);
      color: #fff;
    }}

    /* Modal Backdrop */
    .modal-backdrop {{
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
    }}
    .hidden {{
      display: none !important;
    }}
  </style>
</head>
<body>

  <!-- Sticky Header -->
  <header>
    <div class="header-left">
      <span class="header-badge">NCERT Class 8</span>
      <h1 class="header-title">Chapter 4: Quadrilaterals Master Lab</h1>
    </div>
    <div class="header-right">
      <span class="slide-indicator" id="slideIndicator">Slide 1 of 20</span>
      <button class="speech-btn" id="speechToggleBtn" onclick="toggleSpeech()">
        <span id="speechIcon">🔊</span>
        <span id="speechLabel">Voiceover</span>
      </button>
    </div>
  </header>

  <!-- Main Body Content -->
  <main>
    <!-- Slide Header Banner -->
    <section class="slide-header">
      <div class="slide-tag" id="slideTag">SECTION 4.1</div>
      <h2 class="slide-title" id="slideTitle">Loading Slide...</h2>
      <p class="slide-subtitle" id="slideSubtitle">Interactive Mathematical Laboratory</p>
    </section>

    <!-- Teacher Persona Avatar Banner -->
    <section class="teacher-card" id="teacherCard">
      <div class="avatar-wrapper" id="avatarWrapper">
        <svg class="avatar-svg" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="48" fill="#1e1b4b"/>
          <!-- Shoulders & Coat -->
          <path d="M 15 95 Q 50 78 85 95 L 85 100 L 15 100 Z" fill="#312e81"/>
          <path d="M 38 82 L 50 96 L 62 82 Z" fill="#6366f1"/>
          <!-- Neck & Face -->
          <rect x="42" y="60" width="16" height="15" fill="#fbcfe8" rx="4"/>
          <ellipse cx="50" cy="46" rx="22" ry="25" fill="#fde047"/>
          <!-- Hair & Cap -->
          <path d="M 26 40 Q 50 12 74 40 Q 50 24 26 40 Z" fill="#1e293b"/>
          <!-- Eyes -->
          <circle cx="41" cy="44" r="3.2" fill="#0f172a"/>
          <circle cx="59" cy="44" r="3.2" fill="#0f172a"/>
          <circle cx="42" cy="43" r="1" fill="#fff"/>
          <circle cx="60" cy="43" r="1" fill="#fff"/>
          <!-- Spectacles -->
          <circle cx="41" cy="44" r="6.5" fill="none" stroke="#67e8f9" stroke-width="1.8"/>
          <circle cx="59" cy="44" r="6.5" fill="none" stroke="#67e8f9" stroke-width="1.8"/>
          <line x1="47.5" y1="44" x2="52.5" y2="44" stroke="#67e8f9" stroke-width="1.8"/>
          <!-- Eyebrows -->
          <path d="M 35 37 Q 41 34 47 37" fill="none" stroke="#1e293b" stroke-width="1.5"/>
          <path d="M 53 37 Q 59 34 65 37" fill="none" stroke="#1e293b" stroke-width="1.5"/>
          <!-- Nose -->
          <path d="M 50 46 L 48 52 L 52 52" fill="none" stroke="#ca8a04" stroke-width="1.4"/>
          <!-- Mouth Closed -->
          <path class="mouth-closed" d="M 43 58 Q 50 63 57 58" fill="none" stroke="#b91c1c" stroke-width="2.2" stroke-linecap="round"/>
          <!-- Mouth Open (Talking) -->
          <ellipse class="mouth-open" cx="50" cy="60" rx="6" ry="4.5" fill="#991b1b"/>
        </svg>
      </div>
      <div>
        <div class="teacher-role">Mathematics Mentor</div>
        <div class="teacher-speech" id="teacherSpeech">
          "Welcome to Chapter 4: Quadrilaterals! We will explore the geometry, properties, angle theorems, and symmetries of four-sided figures."
        </div>
      </div>
    </section>

    <!-- Dynamic Lesson Grid (Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      <!-- Left Column: Theory & Formal Explanations -->
      <div class="theory-panel" id="slideContent">
        <!-- Injected dynamically -->
      </div>

      <!-- Right Column: Interactive Simulator + In-Slide Checkpoints -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <!-- Interactive Simulator Panel -->
        <section class="sim-panel" id="simulatorPanel">
          <div class="sim-head">
            <h3 id="simTitle"><span>⚡</span> Interactive Laboratory Simulator</h3>
            <span class="sim-badge" id="simBadge">Live Interactive Model</span>
          </div>
          <div class="sim-viewport" id="simViewport">
            <!-- Simulator SVG & Canvas injected dynamically -->
          </div>
          <div class="sim-controls" id="simControls">
            <!-- Simulator Interactive Controls -->
          </div>
        </section>

        <!-- In-Slide Conceptual Checkpoints (2 Questions per slide) -->
        <section class="checkpoint-section" id="checkpointContainer">
          <div class="checkpoint-header">
            <span>🎯</span> In-Slide Conceptual Checkpoints (Immediate Feedback)
          </div>
          <div id="checkpointsList" style="display:flex; flex-direction:column; gap:12px;">
            <!-- Checkpoints injected dynamically -->
          </div>
        </section>
      </div>
    </div>

    <!-- Full-Width Quiz Containers (Slides 17 to 20) -->
    <div id="quizSlide17" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 1 • Questions 1 to 10</h4>
        <p>Answer all questions below. Click <strong>💡 View Solution</strong> to inspect the step-by-step mathematical reasoning.</p>
      </div>
      <div id="quizContainer1" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide18" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 2 • Questions 11 to 20</h4>
        <p>Parallelograms, diagonal bisections, and consecutive supplementary angles.</p>
      </div>
      <div id="quizContainer2" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide19" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 3 • Questions 21 to 30</h4>
        <p>Rhombus area, perpendicular diagonals, linkage rigidity, and Varignon's theorem.</p>
      </div>
      <div id="quizContainer3" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide20" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 4 • Questions 31 to 40 (Final Slide)</h4>
        <p>Kites, trapeziums, isosceles symmetry, and the comprehensive quadrilateral family tree.</p>
      </div>
      <div id="quizContainer4" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>
  </main>

  <!-- Sticky Bottom Navigation Footer -->
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
    <div style="background:#0f172a; border:1px solid #6366f1; border-radius:16px; max-width:620px; width:95%; padding:24px; position:relative; box-shadow:0 20px 50px rgba(0,0,0,0.8);">
      <button onclick="closeSolutionModal()" style="position:absolute; top:16px; right:16px; background:#1e293b; color:#94a3b8; border:1px solid #475569; width:32px; height:32px; border-radius:50%; font-weight:bold; cursor:pointer;">✕</button>
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
        <span style="background:rgba(245,158,11,0.2); color:#fbbf24; padding:3px 10px; border-radius:6px; font-size:11px; font-weight:800; text-transform:uppercase;" id="modalQuestionBadge">Solution</span>
        <span style="color:#94a3b8; font-size:12px;" id="modalQuestionNum">Question 1</span>
      </div>
      <h3 style="font-size:15px; font-weight:700; color:#fff; margin-bottom:14px; line-height:1.4;" id="modalQuestionTitle">Question Title</h3>
      <div style="background:#020617; border:1px solid #1e293b; border-radius:10px; padding:16px; font-size:13px; color:#cbd5e1; line-height:1.7; max-height:360px; overflow-y:auto; white-space:pre-line;" id="modalSolutionContent">
        Step-by-step solution derivation will appear here.
      </div>
      <div style="margin-top:16px; text-align:right;">
        <button onclick="closeSolutionModal()" style="background:#4f46e5; color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">
          Got It, Close
        </button>
      </div>
    </div>
  </div>

  <!-- Client-side Logic -->
  <script>
    const slides = {slides_json};
    const quizData = {quiz_json};

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let currentUtterance = null;

    // KaTeX Helper
    function triggerMathRender(el) {{
      if (window.renderMathInElement) {{
        renderMathInElement(el, {{
          delimiters: [
            {{ left: "$$", right: "$$", display: true }},
            {{ left: "$", right: "$", display: false }}
          ],
          throwOnError: false
        }});
      }}
    }}

    function init() {{
      renderSlide(0);
      setupSpeechSynthesis();
    }}

    function renderSlide(index) {{
      currentSlideIndex = index;
      const slide = slides[index];

      // Stop speech when slide changes
      stopSpeech();

      // Update Header Indicator
      document.getElementById('slideIndicator').textContent = `Slide ${{index + 1}} of ${{slides.length}}`;
      document.getElementById('slideTag').textContent = `CLASS 8 • CHAPTER 4 • PART ${{index + 1}}`;
      document.getElementById('slideTitle').textContent = slide.title;
      document.getElementById('slideSubtitle').textContent = slide.subtitle;

      // Update Theory Content
      document.getElementById('slideContent').innerHTML = slide.content;
      triggerMathRender(document.getElementById('slideContent'));

      // Update Speech Bubble
      document.getElementById('teacherSpeech').textContent = slide.voice;

      // Navigation Buttons & Last Slide Terminal Rule
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const lastNotice = document.getElementById('lastSlideNotice');

      prevBtn.disabled = (index === 0);

      if (index === slides.length - 1) {{
        nextBtn.style.display = 'none';
        lastNotice.style.display = 'block';
      }} else {{
        nextBtn.style.display = 'flex';
        lastNotice.style.display = 'none';
      }}

      // Checkpoints vs Quiz Questions
      const checkpointContainer = document.getElementById('checkpointContainer');
      const simPanel = document.getElementById('simulatorPanel');
      const lessonGrid = document.getElementById('lessonGrid');

      const q17 = document.getElementById('quizSlide17');
      const q18 = document.getElementById('quizSlide18');
      const q19 = document.getElementById('quizSlide19');
      const q20 = document.getElementById('quizSlide20');

      q17.style.display = 'none';
      q18.style.display = 'none';
      q19.style.display = 'none';
      q20.style.display = 'none';

      if (index < 16) {{
        lessonGrid.style.display = 'grid';
        checkpointContainer.style.display = 'flex';
        simPanel.style.display = 'flex';
        renderCheckpoints(slide.checkpoints);
        renderSimulator(slide.sim_type);
      }} else {{
        lessonGrid.style.display = 'none';
        const qRange = slide.quiz_range;
        if (index === 16) {{
          q17.style.display = 'block';
          renderQuizQuestions(16, qRange[0], qRange[1]);
        }} else if (index === 17) {{
          q18.style.display = 'block';
          renderQuizQuestions(17, qRange[0], qRange[1]);
        }} else if (index === 18) {{
          q19.style.display = 'block';
          renderQuizQuestions(18, qRange[0], qRange[1]);
        }} else if (index === 19) {{
          q20.style.display = 'block';
          renderQuizQuestions(19, qRange[0], qRange[1]);
        }}
      }}

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function prevSlide() {{
      if (currentSlideIndex > 0) {{
        renderSlide(currentSlideIndex - 1);
      }}
    }}

    function nextSlide() {{
      if (currentSlideIndex < slides.length - 1) {{
        renderSlide(currentSlideIndex + 1);
      }}
    }}

    // Checkpoint Renderer (Slides 1 to 16)
    function renderCheckpoints(checkpoints) {{
      const list = document.getElementById('checkpointsList');
      list.innerHTML = '';
      if (!checkpoints) return;

      checkpoints.forEach((cp, qIdx) => {{
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const qText = document.createElement('div');
        qText.className = 'checkpoint-q';
        qText.textContent = `Q${{qIdx + 1}}: ${{cp.question}}`;
        card.appendChild(qText);

        const grid = document.createElement('div');
        grid.className = 'options-grid';

        const feedback = document.createElement('div');
        feedback.className = 'feedback-box';

        cp.options.forEach((opt, optIdx) => {{
          const btn = document.createElement('button');
          btn.className = 'opt-btn';
          btn.textContent = `${{String.fromCharCode(65 + optIdx)}}. ${{opt}}`;
          btn.onclick = () => {{
            const btns = grid.querySelectorAll('.opt-btn');
            btns.forEach(b => b.disabled = true);
            if (optIdx === cp.correct) {{
              btn.classList.add('correct');
              feedback.style.background = 'rgba(16, 185, 129, 0.2)';
              feedback.style.color = '#34d399';
              feedback.innerHTML = `<strong>✓ Correct!</strong> ${{cp.explanation}}`;
              triggerMathRender(feedback);
            }} else {{
              btn.classList.add('wrong');
              btns[cp.correct].classList.add('correct');
              feedback.style.background = 'rgba(244, 63, 94, 0.2)';
              feedback.style.color = '#fb7185';
              feedback.innerHTML = `<strong>✗ Incorrect.</strong> ${{cp.explanation}}`;
              triggerMathRender(feedback);
            }}
            feedback.classList.add('show');
          }};
          grid.appendChild(btn);
        }});

        card.appendChild(grid);
        card.appendChild(feedback);
        list.appendChild(card);
      }});
      triggerMathRender(list);
    }}

    // Quiz Questions Renderer (Slides 17 to 20)
    function renderQuizQuestions(slideIdx, startNum, endNum) {{
      const containerId = `quizContainer${{slideIdx - 15}}`;
      const container = document.getElementById(containerId);
      if (!container) return;
      container.innerHTML = '';

      const subset = quizData.filter(q => q.num >= startNum && q.num <= endNum);

      subset.forEach(q => {{
        const card = document.createElement('div');
        card.className = 'quiz-card';

        card.innerHTML = `
          <div class="quiz-card-head">
            <span class="quiz-badge">Question ${{q.num}} of 40</span>
            <button class="sol-btn" onclick="openSolutionModal(${{q.num}})">
              <span>💡</span> View Solution
            </button>
          </div>
          <div class="checkpoint-q">${{q.question}}</div>
          <div class="options-grid" id="qGrid${{q.num}}"></div>
          <div class="feedback-box" id="qFeedback${{q.num}}"></div>
        `;

        const grid = card.querySelector(`#qGrid${{q.num}}`);
        const feedback = card.querySelector(`#qFeedback${{q.num}}`);

        q.options.forEach((opt, optIdx) => {{
          const btn = document.createElement('button');
          btn.className = 'opt-btn';
          btn.textContent = `${{String.fromCharCode(65 + optIdx)}}. ${{opt}}`;
          btn.onclick = () => {{
            const btns = grid.querySelectorAll('.opt-btn');
            btns.forEach(b => b.disabled = true);
            if (optIdx === q.correct) {{
              btn.classList.add('correct');
              feedback.style.background = 'rgba(16, 185, 129, 0.2)';
              feedback.style.color = '#34d399';
              feedback.innerHTML = `<strong>✓ Correct!</strong> Click "View Solution" to see full step-by-step mathematical reasoning.`;
              triggerMathRender(feedback);
            }} else {{
              btn.classList.add('wrong');
              btns[q.correct].classList.add('correct');
              feedback.style.background = 'rgba(244, 63, 94, 0.2)';
              feedback.style.color = '#fb7185';
              feedback.innerHTML = `<strong>✗ Incorrect.</strong> Correct answer is (${{String.fromCharCode(65 + q.correct)}}). Inspect "View Solution" for detailed steps.`;
              triggerMathRender(feedback);
            }}
            feedback.classList.add('show');
          }};
          grid.appendChild(btn);
        }});

        container.appendChild(card);
      }});
      triggerMathRender(container);
    }}

    // Solution Pop-up Modal Handlers
    function openSolutionModal(qNum) {{
      const q = quizData.find(item => item.num === qNum);
      if (!q) return;

      document.getElementById('modalQuestionNum').textContent = `Question ${{q.num}} of 40`;
      document.getElementById('modalQuestionTitle').innerHTML = q.question;
      document.getElementById('modalSolutionContent').innerHTML = q.solution;
      document.getElementById('solutionModal').classList.remove('hidden');
      triggerMathRender(document.getElementById('solutionModal'));
    }}

    function closeSolutionModal() {{
      document.getElementById('solutionModal').classList.add('hidden');
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeSolutionModal();
    }});

    // Web Speech API Voiceover & Talking Mouth Animation
    function toggleSpeech() {{
      if (isSpeaking) {{
        stopSpeech();
      }} else {{
        startSpeech();
      }}
    }}

    function startSpeech() {{
      if (!synth) return;
      stopSpeech();

      const text = slides[currentSlideIndex].voice;
      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.rate = 1.0;
      currentUtterance.pitch = 1.05;

      const voices = synth.getVoices();
      const engVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha')));
      if (engVoice) currentUtterance.voice = engVoice;

      currentUtterance.onstart = () => {{
        isSpeaking = true;
        document.getElementById('speechToggleBtn').classList.add('speaking');
        document.getElementById('speechIcon').textContent = '⏹';
        document.getElementById('speechLabel').textContent = 'Stop';
        document.getElementById('avatarWrapper').classList.add('speaking');
      }};

      currentUtterance.onend = () => {{
        stopSpeech();
      }};

      currentUtterance.onerror = () => {{
        stopSpeech();
      }};

      synth.speak(currentUtterance);
    }}

    function stopSpeech() {{
      if (synth && synth.speaking) {{
        synth.cancel();
      }}
      isSpeaking = false;
      const btn = document.getElementById('speechToggleBtn');
      if (btn) btn.classList.remove('speaking');
      const icon = document.getElementById('speechIcon');
      if (icon) icon.textContent = '🔊';
      const label = document.getElementById('speechLabel');
      if (label) label.textContent = 'Voiceover';
      const avatar = document.getElementById('avatarWrapper');
      if (avatar) avatar.classList.remove('speaking');
    }}

    function setupSpeechSynthesis() {{
      if ('speechSynthesis' in window) {{
        window.speechSynthesis.onvoiceschanged = () => {{
          // Voices ready
        }};
      }} else {{
        const btn = document.getElementById('speechToggleBtn');
        if (btn) btn.style.display = 'none';
      }}
    }}

    // ==========================================
    // 16 Bespoke Interactive Laboratory Simulators
    // ==========================================
    function renderSimulator(type) {{
      const vp = document.getElementById('simViewport');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const badge = document.getElementById('simBadge');

      vp.innerHTML = '';
      controls.innerHTML = '';

      switch (type) {{
        case 'rectangle_square_geometry_lab':
          renderSim1(vp, controls, title, badge);
          break;
        case 'diagonal_pythagorean_explorer':
          renderSim2(vp, controls, title, badge);
          break;
        case 'angle_sum_partition_lab':
          renderSim3(vp, controls, title, badge);
          break;
        case 'exterior_angles_rotator':
          renderSim4(vp, controls, title, badge);
          break;
        case 'parallelogram_parallel_sides_lab':
          renderSim5(vp, controls, title, badge);
          break;
        case 'parallelogram_diagonal_bisector':
          renderSim6(vp, controls, title, badge);
          break;
        case 'parallelogram_condition_tester':
          renderSim7(vp, controls, title, badge);
          break;
        case 'rhombus_equilateral_stepper':
          renderSim8(vp, controls, title, badge);
          break;
        case 'rhombus_area_triangle_splitter':
          renderSim9(vp, controls, title, badge);
          break;
        case 'quadrilateral_rigidity_linkage':
          renderSim10(vp, controls, title, badge);
          break;
        case 'varignon_parallelogram_tessellation':
          renderSim11(vp, controls, title, badge);
          break;
        case 'kite_symmetry_explorer':
          renderSim12(vp, controls, title, badge);
          break;
        case 'trapezium_parallel_base_slider':
          renderSim13(vp, controls, title, badge);
          break;
        case 'isosceles_trapezium_area_lab':
          renderSim14(vp, controls, title, badge);
          break;
        case 'quadrilateral_family_tree_matrix':
          renderSim15(vp, controls, title, badge);
          break;
        case 'which_quad_puzzle_game':
          renderSim16(vp, controls, title, badge);
          break;
        default:
          vp.innerHTML = '<div style="color:#64748b;">Simulator loading...</div>';
      }}
    }}

    // Sim 1: Rectangle & Square Morphology Lab
    function renderSim1(vp, controls, title, badge) {{
      title.innerHTML = '<span>📐</span> Rectangle & Square Morphology Lab';
      badge.textContent = 'Equiangular & Regularity Morpher';

      let w = 220;
      let h = 140;

      function updateUI() {{
        const isSquare = (w === h);
        const diag = Math.sqrt(w*w + h*h).toFixed(1);

        const svgW = 480;
        const svgH = 260;
        const startX = (svgW - w) / 2;
        const startY = (svgH - h) / 2;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 ${{svgW}} ${{svgH}}" style="width:100%; height:230px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Grid background -->
              <defs>
                <pattern id="grid1" width="20" height="20" patternUnits="userSpaceOnUse">
                  <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.5"/>
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#grid1)"/>

              <!-- Rectangle Body -->
              <rect x="${{startX}}" y="${{startY}}" width="${{w}}" height="${{h}}"
                    fill="${{isSquare ? 'rgba(16, 185, 129, 0.2)' : 'rgba(99, 102, 241, 0.2)'}}"
                    stroke="${{isSquare ? '#10b981' : '#6366f1'}}" stroke-width="2.5" rx="2"/>

              <!-- Diagonals -->
              <line x1="${{startX}}" y1="${{startY}}" x2="${{startX + w}}" y2="${{startY + h}}"
                    stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
              <line x1="${{startX + w}}" y1="${{startY}}" x2="${{startX}}" y2="${{startY + h}}"
                    stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>

              <!-- 4 Right Angle Square Marks (12x12 px) -->
              <path d="M ${{startX + 12}} ${{startY}} L ${{startX + 12}} ${{startY + 12}} L ${{startX}} ${{startY + 12}}" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
              <path d="M ${{startX + w - 12}} ${{startY}} L ${{startX + w - 12}} ${{startY + 12}} L ${{startX + w}} ${{startY + 12}}" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
              <path d="M ${{startX + 12}} ${{startY + h}} L ${{startX + 12}} ${{startY + h - 12}} L ${{startX}} ${{startY + h - 12}}" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
              <path d="M ${{startX + w - 12}} ${{startY + h}} L ${{startX + w - 12}} ${{startY + h - 12}} L ${{startX + w}} ${{startY + h - 12}}" fill="none" stroke="#38bdf8" stroke-width="1.5"/>

              <!-- Dimension Labels -->
              <text x="${{startX + w/2}}" y="${{startY - 8}}" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Width = ${{w}} px</text>
              <text x="${{startX + w + 14}}" y="${{startY + h/2 + 4}}" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="start">Height = ${{h}} px</text>

              <!-- Vertices A, B, C, D -->
              <text x="${{startX - 10}}" y="${{startY - 6}}" fill="#38bdf8" font-size="13" font-weight="bold">A</text>
              <text x="${{startX + w + 4}}" y="${{startY - 6}}" fill="#38bdf8" font-size="13" font-weight="bold">B</text>
              <text x="${{startX + w + 4}}" y="${{startY + h + 14}}" fill="#38bdf8" font-size="13" font-weight="bold">C</text>
              <text x="${{startX - 10}}" y="${{startY + h + 14}}" fill="#38bdf8" font-size="13" font-weight="bold">D</text>

              <!-- Central Diagonals readout -->
              <rect x="${{startX + w/2 - 50}}" y="${{startY + h/2 - 12}}" width="100" height="24" rx="6" fill="#0f172a" stroke="#334155"/>
              <text x="${{startX + w/2}}" y="${{startY + h/2 + 4}}" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">d = ${{diag}} px</text>
            </svg>

            <div style="margin-top:10px; display:flex; justify-content:center; gap:12px; font-size:12.5px;">
              <span style="color:#38bdf8;">All 4 Angles: <strong>90°</strong></span>
              <span style="color:#a5b4fc;">Diagonal d: <strong>${{diag}}</strong> px</span>
              <span style="color:${{isSquare ? '#34d399' : '#f59e0b'}};">Classification: <strong>${{isSquare ? 'Regular Square' : 'Rectangle'}}</strong></span>
            </div>
            ${{isSquare ? `
              <div style="margin-top:6px; background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:6px; padding:6px; font-size:12px; color:#34d399; font-weight:bold;">
                ✨ Symmetrical Square: All 4 sides equal (${{w}} px) & Diagonals intersect perpendicularly at 90°!
              </div>
            ` : ''}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Width:</span>
          <input type="range" id="wSlider" min="100" max="260" value="${{w}}" step="10">
          <span id="wVal">${{w}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Height:</span>
          <input type="range" id="hSlider" min="100" max="220" value="${{h}}" step="10">
          <span id="hVal">${{h}}</span>
        </div>
        <button class="sim-btn" id="makeSquareBtn">Snap to Square (w = h)</button>
        <button class="sim-btn" id="resetRectBtn">Reset Rectangle</button>
      `;

      const wSlider = document.getElementById('wSlider');
      const hSlider = document.getElementById('hSlider');

      wSlider.oninput = (e) => {{
        w = parseInt(e.target.value);
        document.getElementById('wVal').textContent = w;
        updateUI();
      }};

      hSlider.oninput = (e) => {{
        h = parseInt(e.target.value);
        document.getElementById('hVal').textContent = h;
        updateUI();
      }};

      document.getElementById('makeSquareBtn').onclick = () => {{
        w = 160;
        h = 160;
        wSlider.value = 160;
        hSlider.value = 160;
        document.getElementById('wVal').textContent = 160;
        document.getElementById('hVal').textContent = 160;
        updateUI();
      }};

      document.getElementById('resetRectBtn').onclick = () => {{
        w = 220;
        h = 140;
        wSlider.value = 220;
        hSlider.value = 140;
        document.getElementById('wVal').textContent = 220;
        document.getElementById('hVal').textContent = 140;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 2: Diagonal Pythagorean & SAS Congruence Explorer
    function renderSim2(vp, controls, title, badge) {{
      title.innerHTML = '<span>📏</span> Rectangle Diagonal SAS Congruence Explorer';
      badge.textContent = 'Pythagorean Theorem & Congruence Proof';

      let activeTriangle = 'both'; // 'abc', 'bad', or 'both'
      const l = 240;
      const w = 140;

      function updateUI() {{
        const d = Math.sqrt(l*l + w*w).toFixed(1);
        const svgW = 460;
        const svgH = 240;
        const sx = 90;
        const sy = 50;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 ${{svgW}} ${{svgH}}" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Rectangle boundary -->
              <rect x="${{sx}}" y="${{sy}}" width="${{l}}" height="${{w}}" fill="none" stroke="#334155" stroke-width="2"/>

              <!-- Triangle ABC Fill -->
              ${{activeTriangle === 'abc' || activeTriangle === 'both' ? `
                <polygon points="${{sx}},${{sy}} ${{sx + l}},${{sy}} ${{sx + l}},${{sy + w}}" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="2"/>
              ` : ''}}

              <!-- Triangle BAD Fill -->
              ${{activeTriangle === 'bad' || activeTriangle === 'both' ? `
                <polygon points="${{sx}},${{sy}} ${{sx + l}},${{sy}} ${{sx}},${{sy + w}}" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="2"/>
              ` : ''}}

              <!-- Diagonals AC and BD -->
              <line x1="${{sx}}" y1="${{sy + w}}" x2="${{sx + l}}" y2="${{sy}}" stroke="#06b6d4" stroke-width="2" stroke-dasharray="3,3"/>
              <line x1="${{sx}}" y1="${{sy}}" x2="${{sx + l}}" y2="${{sy + w}}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>

              <!-- Vertices -->
              <text x="${{sx - 14}}" y="${{sy + 4}}" fill="#fff" font-weight="bold">D</text>
              <text x="${{sx + l + 8}}" y="${{sy + 4}}" fill="#fff" font-weight="bold">C</text>
              <text x="${{sx + l + 8}}" y="${{sy + w + 14}}" fill="#fff" font-weight="bold">B</text>
              <text x="${{sx - 14}}" y="${{sy + w + 14}}" fill="#fff" font-weight="bold">A</text>

              <!-- Dimension tags -->
              <text x="${{sx + l/2}}" y="${{sy + w + 20}}" fill="#a5b4fc" font-size="12" text-anchor="middle">Base AB = ${{l}}</text>
              <text x="${{sx + l + 14}}" y="${{sy + w/2}}" fill="#a5b4fc" font-size="12">BC = ${{w}}</text>
              <text x="${{sx - 35}}" y="${{sy + w/2}}" fill="#a5b4fc" font-size="12">AD = ${{w}}</text>

              <!-- Central label -->
              <rect x="${{sx + l/2 - 70}}" y="${{sy + w/2 - 14}}" width="140" height="28" rx="6" fill="#0f172a" stroke="#475569"/>
              <text x="${{sx + l/2}}" y="${{sy + w/2 + 4}}" fill="#fcd34d" font-size="11.5" font-weight="bold" text-anchor="middle">Diagonal d = ${{d}}</text>
            </svg>

            <div style="margin-top:10px; background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:8px 12px; font-size:12px; text-align:left; color:#cbd5e1;">
              <strong>SAS Congruence Proof:</strong> In right $\\triangle ABC$ and right $\\triangle BAD$:
              <br>1. Side $AB$ is common to both ($AB = AB$).
              <br>2. Right angles: $\\angle B = \\angle A = 90^\\circ$.
              <br>3. Opposite sides equal: $BC = AD = ${{w}}.
              <br>Therefore $\\triangle ABC \\cong \\triangle BAD$ by SAS $\\implies$ <strong>Hypotenuse $AC = BD = ${{d}}</strong>!
            </div>
          </div>
        `;
        triggerMathRender(vp);
      }}

      controls.innerHTML = `
        <button class="sim-btn ${{activeTriangle === 'abc' ? 'active' : ''}}" id="tAbcBtn">Show △ABC (Hypotenuse AC)</button>
        <button class="sim-btn ${{activeTriangle === 'bad' ? 'active' : ''}}" id="tBadBtn">Show △BAD (Hypotenuse BD)</button>
        <button class="sim-btn ${{activeTriangle === 'both' ? 'active' : ''}}" id="tBothBtn">Compare Both Overlaid</button>
      `;

      document.getElementById('tAbcBtn').onclick = () => {{ activeTriangle = 'abc'; updateUI(); }};
      document.getElementById('tBadBtn').onclick = () => {{ activeTriangle = 'bad'; updateUI(); }};
      document.getElementById('tBothBtn').onclick = () => {{ activeTriangle = 'both'; updateUI(); }};

      updateUI();
    }}

    // Sim 3: Quadrilateral Triangulation & Angle Sum (360°)
    function renderSim3(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔺</span> Quadrilateral Triangulation & Angle Sum (360°)';
      badge.textContent = 'Angle Sum Partition Theorem';

      let showDiagonal = true;
      let shapeType = 'convex1';

      const shapes = {{
        convex1: {{ A: [80, 70], B: [360, 60], C: [400, 200], D: [110, 210] }},
        trapezoid: {{ A: [140, 60], B: [340, 60], C: [420, 210], D: [60, 210] }},
        kite: {{ A: [240, 40], B: [380, 140], C: [240, 220], D: [100, 140] }}
      }};

      function updateUI() {{
        const pts = shapes[shapeType];
        const polyPoints = `${{pts.A[0]}},${{pts.A[1]}} ${{pts.B[0]}},${{pts.B[1]}} ${{pts.C[0]}},${{pts.C[1]}} ${{pts.D[0]}},${{pts.D[1]}}`;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 250" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Triangles fill -->
              ${{showDiagonal ? `
                <polygon points="${{pts.A[0]}},${{pts.A[1]}} ${{pts.B[0]}},${{pts.B[1]}} ${{pts.C[0]}},${{pts.C[1]}}" fill="rgba(6,182,212,0.2)" stroke="none"/>
                <polygon points="${{pts.A[0]}},${{pts.A[1]}} ${{pts.C[0]}},${{pts.C[1]}} ${{pts.D[0]}},${{pts.D[1]}}" fill="rgba(245,158,11,0.2)" stroke="none"/>
                <!-- Diagonal AC -->
                <line x1="${{pts.A[0]}}" y1="${{pts.A[1]}}" x2="${{pts.C[0]}}" y2="${{pts.C[1]}}" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4"/>
                <text x="${{(pts.A[0]+pts.C[0])/2 + 10}}" y="${{(pts.A[1]+pts.C[1])/2 - 6}}" fill="#38bdf8" font-size="11" font-weight="bold">Diagonal AC</text>
                <!-- Triangle labels -->
                <text x="${{(pts.A[0]+pts.B[0]+pts.C[0])/3}}" y="${{(pts.A[1]+pts.B[1]+pts.C[1])/3}}" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">△ABC (180°)</text>
                <text x="${{(pts.A[0]+pts.C[0]+pts.D[0])/3}}" y="${{(pts.A[1]+pts.C[1]+pts.D[1])/3}}" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">△ACD (180°)</text>
              ` : `
                <polygon points="${{polyPoints}}" fill="rgba(99,102,241,0.2)" stroke="none"/>
              `}}

              <!-- Main polygon outline -->
              <polygon points="${{polyPoints}}" fill="none" stroke="#6366f1" stroke-width="2.5"/>

              <!-- Vertices -->
              <circle cx="${{pts.A[0]}}" cy="${{pts.A[1]}}" r="5" fill="#38bdf8"/>
              <text x="${{pts.A[0] - 12}}" y="${{pts.A[1] - 8}}" fill="#fff" font-weight="bold">A</text>

              <circle cx="${{pts.B[0]}}" cy="${{pts.B[1]}}" r="5" fill="#38bdf8"/>
              <text x="${{pts.B[0] + 10}}" y="${{pts.B[1] - 4}}" fill="#fff" font-weight="bold">B</text>

              <circle cx="${{pts.C[0]}}" cy="${{pts.C[1]}}" r="5" fill="#38bdf8"/>
              <text x="${{pts.C[0] + 10}}" y="${{pts.C[1] + 12}}" fill="#fff" font-weight="bold">C</text>

              <circle cx="${{pts.D[0]}}" cy="${{pts.D[1]}}" r="5" fill="#38bdf8"/>
              <text x="${{pts.D[0] - 14}}" y="${{pts.D[1] + 12}}" fill="#fff" font-weight="bold">D</text>
            </svg>

            <div style="margin-top:8px; background:rgba(99,102,241,0.15); border:1px solid #6366f1; border-radius:8px; padding:10px; font-size:13px; color:#e2e8f0;">
              Total Angle Sum = <strong>(∠A + ∠B + ∠C + ∠D) = 180° + 180° = 360°</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn ${{shapeType === 'convex1' ? 'active' : ''}}" id="sh1">General Convex</button>
        <button class="sim-btn ${{shapeType === 'trapezoid' ? 'active' : ''}}" id="sh2">Trapezium</button>
        <button class="sim-btn ${{shapeType === 'kite' ? 'active' : ''}}" id="sh3">Kite Shape</button>
        <button class="sim-btn" id="diagToggle">${{showDiagonal ? 'Hide Diagonal' : 'Split with Diagonal AC'}}</button>
      `;

      document.getElementById('sh1').onclick = () => {{ shapeType = 'convex1'; updateUI(); }};
      document.getElementById('sh2').onclick = () => {{ shapeType = 'trapezoid'; updateUI(); }};
      document.getElementById('sh3').onclick = () => {{ shapeType = 'kite'; updateUI(); }};
      document.getElementById('diagToggle').onclick = () => {{
        showDiagonal = !showDiagonal;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 4: Exterior Angles & Full 360° Turn Walk
    function renderSim4(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔄</span> Exterior Angles & Full 360° Turn Walk';
      badge.textContent = 'Perimeter Walk & Exterior Turn Invariance';

      let collected = false;

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 250" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              ${{!collected ? `
                <!-- Quadrilateral ABCD with extended rays -->
                <!-- AB extended past B -->
                <line x1="120" y1="80" x2="380" y2="80" stroke="#475569" stroke-dasharray="3,3" stroke-width="1.5"/>
                <!-- BC extended past C -->
                <line x1="320" y1="80" x2="400" y2="240" stroke="#475569" stroke-dasharray="3,3" stroke-width="1.5"/>
                <!-- CD extended past D -->
                <line x1="360" y1="160" x2="80" y2="220" stroke="#475569" stroke-dasharray="3,3" stroke-width="1.5"/>
                <!-- DA extended past A -->
                <line x1="140" y1="190" x2="110" y2="30" stroke="#475569" stroke-dasharray="3,3" stroke-width="1.5"/>

                <!-- Main Quad -->
                <polygon points="120,80 320,80 360,160 140,190" fill="rgba(30,41,59,0.7)" stroke="#6366f1" stroke-width="2.5"/>

                <!-- Exterior Angle Arcs Color Coded -->
                <!-- e1 at A (Indigo) -->
                <circle cx="120" cy="80" r="16" fill="none" stroke="#818cf8" stroke-width="3"/>
                <text x="96" y="65" fill="#818cf8" font-size="11" font-weight="bold">e₁=95°</text>

                <!-- e2 at B (Cyan) -->
                <circle cx="320" cy="80" r="16" fill="none" stroke="#06b6d4" stroke-width="3"/>
                <text x="345" y="70" fill="#06b6d4" font-size="11" font-weight="bold">e₂=70°</text>

                <!-- e3 at C (Amber) -->
                <circle cx="360" cy="160" r="16" fill="none" stroke="#f59e0b" stroke-width="3"/>
                <text x="375" y="195" fill="#f59e0b" font-size="11" font-weight="bold">e₃=105°</text>

                <!-- e4 at D (Emerald) -->
                <circle cx="140" cy="190" r="16" fill="none" stroke="#10b981" stroke-width="3"/>
                <text x="100" y="215" fill="#10b981" font-size="11" font-weight="bold">e₄=90°</text>
              ` : `
                <!-- All 4 angles assembled into a 360 circle at origin (240, 125) -->
                <g transform="translate(240, 125)">
                  <!-- 4 Wedges filling the 360 circle -->
                  <path d="M 0 0 L 70 0 A 70 70 0 0 1 12 69 Z" fill="rgba(6,182,212,0.6)" stroke="#06b6d4" stroke-width="1.5"/>
                  <path d="M 0 0 L 12 69 A 70 70 0 0 1 -70 8 Z" fill="rgba(245,158,11,0.6)" stroke="#f59e0b" stroke-width="1.5"/>
                  <path d="M 0 0 L -70 8 A 70 70 0 0 1 -8 -69 Z" fill="rgba(16,185,129,0.6)" stroke="#10b981" stroke-width="1.5"/>
                  <path d="M 0 0 L -8 -69 A 70 70 0 0 1 70 0 Z" fill="rgba(99,102,241,0.6)" stroke="#818cf8" stroke-width="1.5"/>
                  <circle cx="0" cy="0" r="4" fill="#fff"/>
                  <text x="0" y="5" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">360°</text>
                </g>
                <text x="240" y="225" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">✓ The 4 exterior angles form a complete 360° circle!</text>
              `}}
            </svg>

            <div style="margin-top:8px; display:flex; justify-content:center; gap:10px; font-size:12.5px;">
              <span style="color:#818cf8;">e₁ = 95°</span> +
              <span style="color:#06b6d4;">e₂ = 70°</span> +
              <span style="color:#f59e0b;">e₃ = 105°</span> +
              <span style="color:#10b981;">e₄ = 90°</span> =
              <strong style="color:#fcd34d;">360°</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="sweepBtn">${{collected ? 'View Along Polygon Perimeter' : 'Collect All Angles to Common Origin'}}</button>
      `;

      document.getElementById('sweepBtn').onclick = () => {{
        collected = !collected;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 5: Parallelogram Parallel Rails & Co-Interior Angles
    function renderSim5(vp, controls, title, badge) {{
      title.innerHTML = '<span>🛤️</span> Parallelogram Parallel Rails & Angle Laws';
      badge.textContent = 'Co-Interior Supplementary Angles';

      let a = 200; // base
      let b = 130; // slant
      let angle = 65; // degrees

      function updateUI() {{
        const rad = (angle * Math.PI) / 180;
        const dx = b * Math.cos(rad);
        const dy = b * Math.sin(rad);

        const svgW = 480;
        const svgH = 250;
        const sx = 100;
        const sy = 190;

        // Vertices A=(sx, sy), B=(sx+a, sy), C=(sx+a+dx, sy-dy), D=(sx+dx, sy-dy)
        const A = [sx, sy];
        const B = [sx + a, sy];
        const C = [sx + a + dx, sy - dy];
        const D = [sx + dx, sy - dy];

        const oppAngle = 180 - angle;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 ${{svgW}} ${{svgH}}" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Infinite Parallel Rail Lines -->
              <line x1="20" y1="${{sy}}" x2="460" y2="${{sy}}" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>
              <line x1="20" y1="${{sy - dy}}" x2="460" y2="${{sy - dy}}" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

              <!-- Parallelogram Body -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="rgba(99, 102, 241, 0.2)" stroke="#6366f1" stroke-width="2.5"/>

              <!-- Vertex Labels -->
              <text x="${{A[0] - 12}}" y="${{A[1] + 16}}" fill="#38bdf8" font-weight="bold">A (${{angle}}°)</text>
              <text x="${{B[0] + 6}}" y="${{B[1] + 16}}" fill="#f43f5e" font-weight="bold">B (${{oppAngle}}°)</text>
              <text x="${{C[0] + 8}}" y="${{C[1] - 8}}" fill="#38bdf8" font-weight="bold">C (${{angle}}°)</text>
              <text x="${{D[0] - 20}}" y="${{D[1] - 8}}" fill="#f43f5e" font-weight="bold">D (${{oppAngle}}°)</text>

              <!-- Rail Indicators -->
              <text x="30" y="${{sy - 6}}" fill="#64748b" font-size="10">Railway 1 (AB)</text>
              <text x="30" y="${{sy - dy - 6}}" fill="#64748b" font-size="10">Railway 2 (DC ∥ AB)</text>
            </svg>

            <div style="margin-top:8px; display:flex; justify-content:space-around; font-size:12px; background:#0f172a; padding:8px; border-radius:8px;">
              <span style="color:#38bdf8;">Opposite: ∠A = ∠C = <strong>${{angle}}°</strong></span>
              <span style="color:#f43f5e;">Opposite: ∠B = ∠D = <strong>${{oppAngle}}°</strong></span>
              <span style="color:#34d399;">Consecutive: <strong>${{angle}}° + ${{oppAngle}}° = 180°</strong></span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Angle ∠A:</span>
          <input type="range" id="angSlider" min="40" max="140" value="${{angle}}" step="5">
          <span id="angVal">${{angle}}°</span>
        </div>
        <button class="sim-btn" id="rightAngleBtn">Make 90° (Rectangle)</button>
        <button class="sim-btn" id="skew60Btn">Set to 60°</button>
      `;

      const angSlider = document.getElementById('angSlider');
      angSlider.oninput = (e) => {{
        angle = parseInt(e.target.value);
        document.getElementById('angVal').textContent = `${{angle}}°`;
        updateUI();
      }};

      document.getElementById('rightAngleBtn').onclick = () => {{
        angle = 90;
        angSlider.value = 90;
        document.getElementById('angVal').textContent = `90°`;
        updateUI();
      }};

      document.getElementById('skew60Btn').onclick = () => {{
        angle = 60;
        angSlider.value = 60;
        document.getElementById('angVal').textContent = `60°`;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 6: Parallelogram Diagonal Bisection & Centroid Lab
    function renderSim6(vp, controls, title, badge) {{
      title.innerHTML = '<span>✂️</span> Parallelogram Mutual Diagonal Bisection';
      badge.textContent = 'Midpoint Invariance & Vector Balance';

      let a = 220;
      let b = 130;
      let skew = 50;

      function updateUI() {{
        const sx = 100;
        const sy = 180;
        const h = 110;

        const A = [sx, sy];
        const B = [sx + a, sy];
        const C = [sx + a + skew, sy - h];
        const D = [sx + skew, sy - h];

        // Midpoint O
        const O = [(A[0] + C[0])/2, (A[1] + C[1])/2];

        // Diagonal lengths
        const d1 = Math.hypot(C[0] - A[0], C[1] - A[1]).toFixed(1);
        const d2 = Math.hypot(D[0] - B[0], D[1] - B[1]).toFixed(1);

        const oa = (d1 / 2).toFixed(1);
        const ob = (d2 / 2).toFixed(1);

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 240" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Parallelogram -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="2"/>

              <!-- Diagonal AC (Cyan) -->
              <line x1="${{A[0]}}" y1="${{A[1]}}" x2="${{C[0]}}" y2="${{C[1]}}" stroke="#06b6d4" stroke-width="2"/>
              <!-- Diagonal BD (Amber) -->
              <line x1="${{B[0]}}" y1="${{B[1]}}" x2="${{D[0]}}" y2="${{D[1]}}" stroke="#f59e0b" stroke-width="2"/>

              <!-- Central Midpoint O -->
              <circle cx="${{O[0]}}" cy="${{O[1]}}" r="5" fill="#10b981"/>
              <text x="${{O[0] + 8}}" y="${{O[1] - 8}}" fill="#34d399" font-weight="bold" font-size="13">O (Centroid)</text>

              <!-- Tick marks on OA and OC -->
              <circle cx="${{(A[0]+O[0])/2}}" cy="${{(A[1]+O[1])/2}}" r="3" fill="#06b6d4"/>
              <circle cx="${{(C[0]+O[0])/2}}" cy="${{(C[1]+O[1])/2}}" r="3" fill="#06b6d4"/>

              <!-- Vertices -->
              <text x="${{A[0] - 12}}" y="${{A[1] + 16}}" fill="#fff" font-weight="bold">A</text>
              <text x="${{B[0] + 6}}" y="${{B[1] + 16}}" fill="#fff" font-weight="bold">B</text>
              <text x="${{C[0] + 6}}" y="${{C[1] - 8}}" fill="#fff" font-weight="bold">C</text>
              <text x="${{D[0] - 14}}" y="${{D[1] - 8}}" fill="#fff" font-weight="bold">D</text>
            </svg>

            <div style="margin-top:8px; display:flex; justify-content:space-around; font-size:12px; background:#0f172a; padding:8px; border-radius:8px;">
              <span style="color:#06b6d4;">Diagonal AC = ${{d1}} (OA = OC = <strong>${{oa}}</strong>)</span>
              <span style="color:#f59e0b;">Diagonal BD = ${{d2}} (OB = OD = <strong>${{ob}}</strong>)</span>
            </div>
            <div style="margin-top:4px; font-size:11.5px; color:#94a3b8;">
              ✓ Point O bisects both diagonals simultaneously ($OA = OC$ and $OB = OD$).
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="sNormal">Standard Parallelogram</button>
        <button class="sim-btn" id="sSkew">High Shear Parallelogram</button>
      `;

      document.getElementById('sNormal').onclick = () => {{ skew = 50; updateUI(); }};
      document.getElementById('sSkew').onclick = () => {{ skew = 120; updateUI(); }};

      updateUI();
    }}

    // Sim 7: Parallelogram Diagnostic Test Chamber
    function renderSim7(vp, controls, title, badge) {{
      title.innerHTML = '<span>🧪</span> Parallelogram Diagnostic Test Chamber';
      badge.textContent = 'Sufficient Condition Validator';

      let testCase = 'case3'; // default one pair equal and parallel

      const cases = {{
        case1: {{
          name: '1. Both Pairs Opposite Sides Equal',
          valid: true,
          desc: 'AB = CD and BC = AD. By SSS congruence on diagonal split, opposite angles and parallelism follow automatically.',
          shape: 'polygon points="120,170 320,170 360,70 160,70"'
        }},
        case2: {{
          name: '2. Both Pairs Opposite Angles Equal',
          valid: true,
          desc: '∠A = ∠C and ∠B = ∠D. Since sum = 360°, consecutive angles sum to 180°, establishing parallel rails.',
          shape: 'polygon points="120,170 320,170 360,70 160,70"'
        }},
        case3: {{
          name: '3. One Pair Equal AND Parallel',
          valid: true,
          desc: 'AB ∥ CD and AB = CD. Fastest geometric proof! SAS congruence proves remaining pair must be equal and parallel.',
          shape: 'polygon points="120,170 320,170 360,70 160,70"'
        }},
        case4: {{
          name: '4. Diagonals Bisect Each Other',
          valid: true,
          desc: 'OA = OC and OB = OD. Central vertical ASA congruence guarantees opposite sides are equal and parallel.',
          shape: 'polygon points="120,170 320,170 360,70 160,70"'
        }},
        case5: {{
          name: '5. (TRAP) One Pair Parallel, OTHER Pair Equal',
          valid: false,
          desc: 'TRAP! AB ∥ CD, but non-parallel legs AD = BC. This is an Isosceles Trapezium! It is NOT a parallelogram!',
          shape: 'polygon points="80,170 360,170 300,70 140,70"'
        }}
      }};

      function updateUI() {{
        const c = cases[testCase];

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 440 220" style="width:100%; height:190px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <${{c.shape}}
                fill="${{c.valid ? 'rgba(16,185,129,0.2)' : 'rgba(244,63,94,0.2)'}}"
                stroke="${{c.valid ? '#10b981' : '#f43f5e'}}" stroke-width="2.5"/>
              <text x="220" y="30" fill="${{c.valid ? '#34d399' : '#fb7185'}}" font-size="14" font-weight="bold" text-anchor="middle">
                ${{c.valid ? '✓ GUARANTEED PARALLELOGRAM' : '✗ FAILED TEST (TRAP: ISOSCELES TRAPEZIUM)'}}
              </text>
            </svg>

            <div style="margin-top:10px; background:#0f172a; border:1px solid ${{c.valid ? '#10b981' : '#f43f5e'}}; border-radius:8px; padding:10px 14px; font-size:12.5px; text-align:left; color:#cbd5e1;">
              <strong style="color:${{c.valid ? '#34d399' : '#fb7185'}};">${{c.name}}:</strong> ${{c.desc}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="btnC1">Sides Equal</button>
        <button class="sim-btn" id="btnC2">Angles Equal</button>
        <button class="sim-btn active" id="btnC3">1 Pair = & ∥</button>
        <button class="sim-btn" id="btnC4">Diags Bisect</button>
        <button class="sim-btn" style="border-color:#f43f5e;" id="btnC5">Trap Test</button>
      `;

      document.getElementById('btnC1').onclick = () => {{ testCase = 'case1'; updateUI(); }};
      document.getElementById('btnC2').onclick = () => {{ testCase = 'case2'; updateUI(); }};
      document.getElementById('btnC3').onclick = () => {{ testCase = 'case3'; updateUI(); }};
      document.getElementById('btnC4').onclick = () => {{ testCase = 'case4'; updateUI(); }};
      document.getElementById('btnC5').onclick = () => {{ testCase = 'case5'; updateUI(); }};

      updateUI();
    }}

    // Sim 8: Rhombus Equilateral Symmetry & Perpendicular Diagonals
    function renderSim8(vp, controls, title, badge) {{
      title.innerHTML = '<span>💎</span> Rhombus Equilateral Symmetry & Perpendicular Diagonals';
      badge.textContent = 'd₁ ⊥ d₂ & Vertex Angle Bisection';

      let theta = 60; // acute angle
      const s = 140; // side length

      function updateUI() {{
        const rad = (theta * Math.PI) / 180;
        const halfT = rad / 2;
        // Diagonals d1 and d2
        const d1 = 2 * s * Math.cos(halfT); // horizontal diagonal
        const d2 = 2 * s * Math.sin(halfT); // vertical diagonal

        const cx = 240;
        const cy = 120;

        const A = [cx - d1/2, cy];
        const B = [cx, cy - d2/2];
        const C = [cx + d1/2, cy];
        const D = [cx, cy + d2/2];

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 240" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Rhombus outline -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="rgba(6, 182, 212, 0.18)" stroke="#06b6d4" stroke-width="2.5"/>

              <!-- Perpendicular Diagonals -->
              <line x1="${{A[0]}}" y1="${{A[1]}}" x2="${{C[0]}}" y2="${{C[1]}}" stroke="#f59e0b" stroke-width="2"/>
              <line x1="${{B[0]}}" y1="${{B[1]}}" x2="${{D[0]}}" y2="${{D[1]}}" stroke="#f59e0b" stroke-width="2"/>

              <!-- 90 degree perpendicular marker at center -->
              <rect x="${{cx}}" y="${{cy - 12}}" width="12" height="12" fill="none" stroke="#fcd34d" stroke-width="1.5"/>

              <!-- Equal side hash marks -->
              <circle cx="${{(A[0]+B[0])/2}}" cy="${{(A[1]+B[1])/2}}" r="3" fill="#38bdf8"/>
              <circle cx="${{(B[0]+C[0])/2}}" cy="${{(B[1]+C[1])/2}}" r="3" fill="#38bdf8"/>
              <circle cx="${{(C[0]+D[0])/2}}" cy="${{(C[1]+D[1])/2}}" r="3" fill="#38bdf8"/>
              <circle cx="${{(D[0]+A[0])/2}}" cy="${{(D[1]+A[1])/2}}" r="3" fill="#38bdf8"/>

              <!-- Vertices -->
              <text x="${{A[0] - 16}}" y="${{A[1] + 4}}" fill="#fff" font-weight="bold">A</text>
              <text x="${{B[0] - 4}}" y="${{B[1] - 8}}" fill="#fff" font-weight="bold">B</text>
              <text x="${{C[0] + 8}}" y="${{C[1] + 4}}" fill="#fff" font-weight="bold">C</text>
              <text x="${{D[0] - 4}}" y="${{D[1] + 16}}" fill="#fff" font-weight="bold">D</text>

              <!-- Center label -->
              <text x="${{cx + 16}}" y="${{cy - 14}}" fill="#fcd34d" font-size="11" font-weight="bold">90°</text>
            </svg>

            <div style="margin-top:8px; display:flex; justify-content:space-around; font-size:12px; background:#0f172a; padding:8px; border-radius:8px;">
              <span style="color:#06b6d4;">Side s = <strong>${{s}}</strong> (All 4 Equal)</span>
              <span style="color:#f59e0b;">Diagonals: <strong>d₁ ⊥ d₂ (90°)</strong></span>
              <span style="color:#34d399;">Bisected Corner: <strong>${{(theta/2).toFixed(1)}}°</strong></span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Acute Angle:</span>
          <input type="range" id="thSlider" min="40" max="85" value="${{theta}}" step="5">
          <span id="thVal">${{theta}}°</span>
        </div>
        <button class="sim-btn" id="r60">60° Rhombus</button>
        <button class="sim-btn" id="rSquare">90° (Square Limit)</button>
      `;

      const thSlider = document.getElementById('thSlider');
      thSlider.oninput = (e) => {{
        theta = parseInt(e.target.value);
        document.getElementById('thVal').textContent = `${{theta}}°`;
        updateUI();
      }};

      document.getElementById('r60').onclick = () => {{
        theta = 60;
        thSlider.value = 60;
        document.getElementById('thVal').textContent = `60°`;
        updateUI();
      }};

      document.getElementById('rSquare').onclick = () => {{
        theta = 89;
        thSlider.value = 89;
        document.getElementById('thVal').textContent = `90°`;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 9: Rhombus Area Dissection: (1/2) × d₁ × d₂
    function renderSim9(vp, controls, title, badge) {{
      title.innerHTML = '<span>🧩</span> Rhombus Area Dissection: (1/2) × d₁ × d₂';
      badge.textContent = 'Triangle Dissection & Rectangle Proof';

      let state = 'rhombus'; // 'rhombus' or 'rectangle'
      const d1 = 200;
      const d2 = 120;

      function updateUI() {{
        const area = (0.5 * d1 * d2).toFixed(0);

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 230" style="width:100%; height:200px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              ${{state === 'rhombus' ? `
                <!-- Central Rhombus split into 4 colored right triangles -->
                <g transform="translate(240, 115)">
                  <!-- T1: Top-Right (Cyan) -->
                  <polygon points="0,0 ${{d1/2}},0 0,${{-d2/2}}" fill="rgba(6,182,212,0.6)" stroke="#06b6d4" stroke-width="1.5"/>
                  <!-- T2: Top-Left (Rose) -->
                  <polygon points="0,0 ${{-d1/2}},0 0,${{-d2/2}}" fill="rgba(244,63,94,0.6)" stroke="#f43f5e" stroke-width="1.5"/>
                  <!-- T3: Bottom-Left (Amber) -->
                  <polygon points="0,0 ${{-d1/2}},0 0,${{d2/2}}" fill="rgba(245,158,11,0.6)" stroke="#f59e0b" stroke-width="1.5"/>
                  <!-- T4: Bottom-Right (Emerald) -->
                  <polygon points="0,0 ${{d1/2}},0 0,${{d2/2}}" fill="rgba(16,185,129,0.6)" stroke="#10b981" stroke-width="1.5"/>
                </g>
                <text x="240" y="210" fill="#e2e8f0" font-size="12" text-anchor="middle">Rhombus: 4 congruent right triangles</text>
              ` : `
                <!-- Reassembled into a Rectangle of width d1 and height d2/2 -->
                <g transform="translate(140, 75)">
                  <rect x="0" y="0" width="${{d1}}" height="${{d2/2}}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="4,4"/>
                  <!-- Left half -->
                  <polygon points="0,0 ${{d1/2}},0 0,${{d2/2}}" fill="rgba(244,63,94,0.6)" stroke="#f43f5e" stroke-width="1.5"/>
                  <polygon points="${{d1/2}},0 ${{d1/2}},${{d2/2}} 0,${{d2/2}}" fill="rgba(245,158,11,0.6)" stroke="#f59e0b" stroke-width="1.5"/>
                  <!-- Right half -->
                  <polygon points="${{d1/2}},0 ${{d1}},0 ${{d1/2}},${{d2/2}}" fill="rgba(6,182,212,0.6)" stroke="#06b6d4" stroke-width="1.5"/>
                  <polygon points="${{d1}},0 ${{d1}},${{d2/2}} ${{d1/2}},${{d2/2}}" fill="rgba(16,185,129,0.6)" stroke="#10b981" stroke-width="1.5"/>
                </g>
                <text x="240" y="200" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">
                  Reassembled Rectangle = Length d₁ (${{d1}}) × Height (d₂/2) (${{d2/2}})
                </text>
              `}}
            </svg>

            <div style="margin-top:8px; background:#0f172a; padding:8px 14px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              Formula: $\\text{{Area}} = \\frac{{1}}{{2}} \\times d_1 \\times d_2 = \\frac{{1}}{{2}} \\times ${{d1}} \\times ${{d2}} = <strong style="color:#fcd34d;">${{area}}</strong> sq units
            </div>
          </div>
        `;
        triggerMathRender(vp);
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="toggleReassembleBtn">
          ${{state === 'rhombus' ? 'Rearrange 4 Triangles into Rectangle' : 'Return to Rhombus'}}
        </button>
      `;

      document.getElementById('toggleReassembleBtn').onclick = () => {{
        state = (state === 'rhombus') ? 'rectangle' : 'rhombus';
        updateUI();
      }};

      updateUI();
    }}

    // Sim 10: Quadrilateral Linkage vs. Triangular Bracing
    function renderSim10(vp, controls, title, badge) {{
      title.innerHTML = '<span>🏗️</span> Quadrilateral Linkage vs. Triangular Bracing';
      badge.textContent = 'Degrees of Freedom & Structural Stability';

      let shear = 30; // degrees
      let hasBrace = false;

      function updateUI() {{
        const baseW = 200;
        const sideH = 120;
        const rad = (shear * Math.PI) / 180;
        const dx = sideH * Math.sin(rad);
        const dy = sideH * Math.cos(rad);

        const A = [120, 190];
        const B = [120 + baseW, 190];
        const C = [120 + baseW + dx, 190 - dy];
        const D = [120 + dx, 190 - dy];

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 230" style="width:100%; height:200px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- 4 Bars -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="${{hasBrace ? 'rgba(16,185,129,0.15)' : 'rgba(244,63,94,0.15)'}}"
                       stroke="${{hasBrace ? '#10b981' : '#f43f5e'}}" stroke-width="4" stroke-linejoin="round"/>

              <!-- Diagonal Steel Brace -->
              ${{hasBrace ? `
                <line x1="${{A[0]}}" y1="${{A[1]}}" x2="${{C[0]}}" y2="${{C[1]}}" stroke="#10b981" stroke-width="4.5"/>
                <text x="${{(A[0]+C[0])/2 + 10}}" y="${{(A[1]+C[1])/2 - 10}}" fill="#34d399" font-size="12" font-weight="bold">Diagonal Brace Pin</text>
              ` : ''}}

              <!-- 4 Pin Joints -->
              <circle cx="${{A[0]}}" cy="${{A[1]}}" r="7" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
              <circle cx="${{B[0]}}" cy="${{B[1]}}" r="7" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
              <circle cx="${{C[0]}}" cy="${{C[1]}}" r="7" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
              <circle cx="${{D[0]}}" cy="${{D[1]}}" r="7" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>

              <!-- Status Banner -->
              <text x="240" y="25" fill="${{hasBrace ? '#34d399' : '#fb7185'}}" font-size="13" font-weight="bold" text-anchor="middle">
                ${{hasBrace ? '🔒 RIGID STRUCTURE (0 Degrees of Freedom: Stable Truss)' : '⚠️ FLEXIBLE LINKAGE (1 Degree of Freedom: Deforms Under Force)'}}
              </text>
            </svg>

            <div style="margin-top:8px; font-size:12px; color:#cbd5e1;">
              ${{hasBrace ?
                'With the diagonal installed, the quadrilateral is split into two rigid triangles. By SSS congruence, no angles can change!' :
                'Drag the shear slider below to observe how the four-bar frame deforms without altering any side length!'
              }}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Shear Force:</span>
          <input type="range" id="shSlider" min="-45" max="45" value="${{shear}}" step="5" ${{hasBrace ? 'disabled' : ''}}>
          <span id="shVal">${{shear}}°</span>
        </div>
        <button class="sim-btn ${{hasBrace ? 'active' : ''}}" id="braceBtn">
          ${{hasBrace ? 'Remove Diagonal Brace (Unlock)' : 'Install Diagonal Brace (Lock)'}}
        </button>
      `;

      const shSlider = document.getElementById('shSlider');
      shSlider.oninput = (e) => {{
        if (!hasBrace) {{
          shear = parseInt(e.target.value);
          document.getElementById('shVal').textContent = `${{shear}}°`;
          updateUI();
        }}
      }};

      document.getElementById('braceBtn').onclick = () => {{
        hasBrace = !hasBrace;
        renderSim10(vp, controls, title, badge);
      }};

      updateUI();
    }}

    // Sim 11: Varignon's Theorem & Plane Tessellation
    function renderSim11(vp, controls, title, badge) {{
      title.innerHTML = '<span>✨</span> Varignon\\'s Theorem & Plane Tessellation';
      badge.textContent = 'Midpoint Parallelogram & Gapless Tiling';

      let mode = 'varignon'; // 'varignon' or 'tessellation'

      const A = [100, 50];
      const B = [380, 70];
      const C = [420, 200];
      const D = [80, 180];

      // Midpoints
      const P = [(A[0]+B[0])/2, (A[1]+B[1])/2];
      const Q = [(B[0]+C[0])/2, (B[1]+C[1])/2];
      const R = [(C[0]+D[0])/2, (C[1]+D[1])/2];
      const S = [(D[0]+A[0])/2, (D[1]+A[1])/2];

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 240" style="width:100%; height:220px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              ${{mode === 'varignon' ? `
                <!-- Outer Asymmetric Quadrilateral ABCD -->
                <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                         fill="rgba(30,41,59,0.6)" stroke="#475569" stroke-width="2"/>

                <!-- Varignon Midpoint Parallelogram PQRS -->
                <polygon points="${{P[0]}},${{P[1]}} ${{Q[0]}},${{Q[1]}} ${{R[0]}},${{R[1]}} ${{S[0]}},${{S[1]}}"
                         fill="rgba(245,158,11,0.25)" stroke="#f59e0b" stroke-width="2.5"/>

                <!-- Midpoint dots -->
                <circle cx="${{P[0]}}" cy="${{P[1]}}" r="4" fill="#fbbf24"/>
                <text x="${{P[0]}}" y="${{P[1] - 8}}" fill="#fcd34d" font-size="11" font-weight="bold">P</text>

                <circle cx="${{Q[0]}}" cy="${{Q[1]}}" r="4" fill="#fbbf24"/>
                <text x="${{Q[0] + 8}}" y="${{Q[1]}}" fill="#fcd34d" font-size="11" font-weight="bold">Q</text>

                <circle cx="${{R[0]}}" cy="${{R[1]}}" r="4" fill="#fbbf24"/>
                <text x="${{R[0]}}" y="${{R[1] + 14}}" fill="#fcd34d" font-size="11" font-weight="bold">R</text>

                <circle cx="${{S[0]}}" cy="${{S[1]}}" r="4" fill="#fbbf24"/>
                <text x="${{S[0] - 14}}" y="${{S[1]}}" fill="#fcd34d" font-size="11" font-weight="bold">S</text>

                <text x="240" y="130" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">
                  Varignon ∥gm (Area = 50%)
                </text>
              ` : `
                <!-- 2x2 Tessellation grid demonstrating seamless plane tiling -->
                <g transform="scale(0.5) translate(40, 20)">
                  <!-- 4 identical tiles rotated 180 degrees meeting at center -->
                  <polygon points="100,50 380,70 420,200 80,180" fill="rgba(6,182,212,0.4)" stroke="#06b6d4" stroke-width="2"/>
                  <polygon points="420,200 700,220 740,350 400,330" fill="rgba(244,63,94,0.4)" stroke="#f43f5e" stroke-width="2"/>
                  <polygon points="80,180 420,200 400,330 60,310" fill="rgba(245,158,11,0.4)" stroke="#f59e0b" stroke-width="2"/>
                  <polygon points="400,330 740,350 720,480 380,460" fill="rgba(16,185,129,0.4)" stroke="#10b981" stroke-width="2"/>
                </g>
                <text x="240" y="225" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">
                  Gapless Plane Tiling: 4 angles meet at every vertex = 360°
                </text>
              `}}
            </svg>

            <div style="margin-top:8px; font-size:12px; color:#cbd5e1;">
              <strong>Varignon's Law:</strong> Joining the midpoints of ANY 4-gon always creates a parallelogram whose area is exactly <strong>50%</strong> of the original!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="togVMode">
          ${{mode === 'varignon' ? 'Show Plane Tessellation (Tiling)' : 'Show Varignon Midpoints'}}
        </button>
      `;

      document.getElementById('togVMode').onclick = () => {{
        mode = (mode === 'varignon') ? 'tessellation' : 'varignon';
        updateUI();
      }};

      updateUI();
    }}

    // Sim 12: Kite Bilateral Symmetry & Cross Diagonals
    function renderSim12(vp, controls, title, badge) {{
      title.innerHTML = '<span>🪁</span> Kite Bilateral Symmetry & Axis of Reflection';
      badge.textContent = 'Perpendicular Cross & Equal Wings';

      let topL = 70;
      let botL = 130;
      let wingW = 100;

      function updateUI() {{
        const cx = 240;
        const cy = 110;

        const A = [cx, cy - topL];
        const B = [cx + wingW, cy];
        const C = [cx, cy + botL];
        const D = [cx - wingW, cy];

        const d1 = (topL + botL); // vertical diagonal AC
        const d2 = (2 * wingW);   // horizontal diagonal BD
        const area = (0.5 * d1 * d2).toFixed(0);

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 260" style="width:100%; height:230px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Kite body -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="2.5"/>

              <!-- Axis of symmetry (AC) -->
              <line x1="${{A[0]}}" y1="${{A[1] - 15}}" x2="${{C[0]}}" y2="${{C[1] + 15}}"
                    stroke="#ec4899" stroke-width="2" stroke-dasharray="4,4"/>

              <!-- Cross diagonal (BD) -->
              <line x1="${{D[0]}}" y1="${{D[1]}}" x2="${{B[0]}}" y2="${{B[1]}}"
                    stroke="#38bdf8" stroke-width="2"/>

              <!-- 90 deg right-angle mark at M -->
              <rect x="${{cx}}" y="${{cy - 10}}" width="10" height="10" fill="none" stroke="#fcd34d" stroke-width="1.5"/>

              <!-- Equal wing angles at B and D -->
              <circle cx="${{B[0]}}" cy="${{B[1]}}" r="12" fill="none" stroke="#10b981" stroke-width="2"/>
              <circle cx="${{D[0]}}" cy="${{D[1]}}" r="12" fill="none" stroke="#10b981" stroke-width="2"/>
              <text x="${{B[0] + 14}}" y="${{B[1] + 4}}" fill="#34d399" font-size="11" font-weight="bold">∠B = ∠D</text>

              <!-- Vertices -->
              <text x="${{A[0]}}" y="${{A[1] - 8}}" fill="#fff" font-weight="bold" text-anchor="middle">A</text>
              <text x="${{C[0]}}" y="${{C[1] + 16}}" fill="#fff" font-weight="bold" text-anchor="middle">C</text>
              <text x="${{D[0] - 14}}" y="${{D[1] + 4}}" fill="#fff" font-weight="bold">D</text>
              <text x="${{B[0] + 6}}" y="${{B[1] + 4}}" fill="#fff" font-weight="bold">B</text>
            </svg>

            <div style="margin-top:6px; display:flex; justify-content:space-around; font-size:12px; background:#0f172a; padding:6px; border-radius:8px;">
              <span style="color:#ec4899;">Axis of Symmetry: <strong>AC (d₁ = ${{d1}})</strong></span>
              <span style="color:#38bdf8;">Bisected Cross: <strong>BD (d₂ = ${{d2}})</strong></span>
              <span style="color:#fcd34d;">Area = <strong>${{area}}</strong></span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Wing Width:</span>
          <input type="range" id="wSlider" min="60" max="140" value="${{wingW}}" step="10">
          <span id="wVal">${{wingW}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Tail Length:</span>
          <input type="range" id="tSlider" min="90" max="150" value="${{botL}}" step="10">
          <span id="tVal">${{botL}}</span>
        </div>
      `;

      document.getElementById('wSlider').oninput = (e) => {{
        wingW = parseInt(e.target.value);
        document.getElementById('wVal').textContent = wingW;
        updateUI();
      }};

      document.getElementById('tSlider').oninput = (e) => {{
        botL = parseInt(e.target.value);
        document.getElementById('tVal').textContent = botL;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 13: Trapezium Base Rails & Leg Transversals
    function renderSim13(vp, controls, title, badge) {{
      title.innerHTML = '<span>📏</span> Trapezium Base Rails & Leg Transversals';
      badge.textContent = 'At Least One Parallel Pair (a ∥ b)';

      let topBase = 140;
      let botBase = 260;
      let height = 110;
      let skew = 30;

      function updateUI() {{
        const sx = 110;
        const sy = 190;

        const A = [sx, sy];
        const B = [sx + botBase, sy];
        const C = [sx + skew + topBase, sy - height];
        const D = [sx + skew, sy - height];

        // Angles approximation
        const angleA = Math.round(Math.atan2(height, skew) * 180 / Math.PI);
        const angleD = 180 - angleA;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 240" style="width:100%; height:210px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Infinite Parallel Base Lines -->
              <line x1="20" y1="${{sy}}" x2="460" y2="${{sy}}" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>
              <line x1="20" y1="${{sy - height}}" x2="460" y2="${{sy - height}}" stroke="#334155" stroke-dasharray="4,4" stroke-width="1.5"/>

              <!-- Trapezium Polygon -->
              <polygon points="${{A[0]}},${{A[1]}} ${{B[0]}},${{B[1]}} ${{C[0]}},${{C[1]}} ${{D[0]}},${{D[1]}}"
                       fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>

              <!-- Altitude Line h -->
              <line x1="${{D[0]}}" y1="${{D[1]}}" x2="${{D[0]}}" y2="${{sy}}" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,3"/>
              <rect x="${{D[0]}}" y="${{sy - 10}}" width="10" height="10" fill="none" stroke="#ec4899" stroke-width="1.5"/>
              <text x="${{D[0] + 6}}" y="${{sy - height/2}}" fill="#ec4899" font-size="11" font-weight="bold">h = ${{height}}</text>

              <!-- Dimension tags -->
              <text x="${{(D[0]+C[0])/2}}" y="${{D[1] - 8}}" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Top Base a = ${{topBase}}</text>
              <text x="${{(A[0]+B[0])/2}}" y="${{sy + 18}}" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">Bottom Base b = ${{botBase}}</text>

              <!-- Supplementary angle indicator along leg AD -->
              <text x="${{A[0] - 8}}" y="${{A[1] + 4}}" fill="#38bdf8" font-size="11" font-weight="bold">${{angleA}}°</text>
              <text x="${{D[0] - 12}}" y="${{D[1] - 4}}" fill="#38bdf8" font-size="11" font-weight="bold">${{angleD}}°</text>
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px; border-radius:8px; font-size:12px; color:#cbd5e1;">
              <strong>Consecutive Interior Angles on Leg AD:</strong> ${{angleA}}° + ${{angleD}}° = <strong>180°</strong> (Co-interior angles of parallel bases).
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Top Base a:</span>
          <input type="range" id="tbSlider" min="80" max="180" value="${{topBase}}" step="10">
          <span id="tbVal">${{topBase}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Height h:</span>
          <input type="range" id="hSlider" min="70" max="130" value="${{height}}" step="10">
          <span id="hVal">${{height}}</span>
        </div>
      `;

      document.getElementById('tbSlider').oninput = (e) => {{
        topBase = parseInt(e.target.value);
        document.getElementById('tbVal').textContent = topBase;
        updateUI();
      }};

      document.getElementById('hSlider').oninput = (e) => {{
        height = parseInt(e.target.value);
        document.getElementById('hVal').textContent = height;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 14: Trapezium Area via Rotational Twin Duplication
    function renderSim14(vp, controls, title, badge) {{
      title.innerHTML = '<span>👥</span> Trapezium Area via Rotational Twin Duplication';
      badge.textContent = 'Area = (1/2)(a + b)h Proof';

      let showTwin = false;
      const a = 120; // top base
      const b = 200; // bottom base
      const h = 100;
      const skew = 40;

      function updateUI() {{
        const area = (0.5 * (a + b) * h).toFixed(0);
        const combinedBase = a + b;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <svg viewBox="0 0 480 230" style="width:100%; height:200px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Original Trapezium (Cyan) -->
              <polygon points="60,180 ${{60+b}},180 ${{60+skew+a}},${{180-h}} ${{60+skew}},${{180-h}}"
                       fill="rgba(6,182,212,0.3)" stroke="#06b6d4" stroke-width="2.5"/>
              <text x="${{60 + b/2}}" y="140" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">Original Trapezium</text>

              <!-- Inverted Twin (Amber) -->
              ${{showTwin ? `
                <polygon points="${{60+b}},180 ${{60+b+a}},180 ${{60+skew+a}},${{180-h}} ${{60+b}},180" fill="none"/>
                <polygon points="${{60+b}},180 ${{60+b+a}},180 ${{60+b+a-skew}},${{180-h}} ${{60+skew+a}},${{180-h}}"
                         fill="rgba(245,158,11,0.3)" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="${{60+b+a/2}}" y="140" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">Rotated Twin (180°)</text>

                <!-- Combined Parallelogram Base Bracket -->
                <line x1="60" y1="205" x2="${{60+b+a}}" y2="205" stroke="#fff" stroke-width="1.5"/>
                <text x="${{60 + (b+a)/2}}" y="222" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">
                  Combined Parallelogram Base = a + b (${{combinedBase}})
                </text>
              ` : ''}}
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              ${{showTwin ? `
                Parallelogram Area = $\\text{{Base}} \\times \\text{{Height}} = (a + b)h$.
                <br>One Trapezium = $\\frac{{1}}{{2}}(a + b)h = \\frac{{1}}{{2}}(${{a}} + ${{b}}) \\times ${{h}} =$ <strong style="color:#34d399;">${{area}}</strong> sq units.
              ` : `
                Click the button below to rotate and snap an identical twin trapezium alongside the original!
              `}}
            </div>
          </div>
        `;
        triggerMathRender(vp);
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="twinBtn">
          ${{showTwin ? 'Remove Twin' : 'Duplicate & Rotate Twin 180°'}}
        </button>
      `;

      document.getElementById('twinBtn').onclick = () => {{
        showTwin = !showTwin;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 15: The Grand Quadrilateral Family Tree & Euler-Venn Matrix
    function renderSim15(vp, controls, title, badge) {{
      title.innerHTML = '<span>🌳</span> The Grand Quadrilateral Family Tree';
      badge.textContent = 'Hierarchical Euler-Venn Classification';

      let selectedNode = 'square';

      const taxonomy = {{
        quad: {{
          name: 'Quadrilateral',
          ancestors: ['Quadrilateral'],
          props: 'Any 4-sided closed polygon. Sum of interior angles is always 360°. 4 vertices, 2 diagonals.'
        }},
        trapezium: {{
          name: 'Trapezium',
          ancestors: ['Quadrilateral', 'Trapezium'],
          props: 'At least one pair of parallel sides (bases). Consecutive interior angles along each leg sum to 180°.'
        }},
        kite: {{
          name: 'Kite',
          ancestors: ['Quadrilateral', 'Kite'],
          props: 'Two pairs of adjacent equal sides. Perpendicular diagonals. One diagonal is bisected and acts as an axis of symmetry.'
        }},
        parallelogram: {{
          name: 'Parallelogram',
          ancestors: ['Quadrilateral', 'Trapezium', 'Parallelogram'],
          props: 'Both pairs of opposite sides parallel and equal. Opposite angles equal. Diagonals bisect each other.'
        }},
        rectangle: {{
          name: 'Rectangle',
          ancestors: ['Quadrilateral', 'Trapezium', 'Parallelogram', 'Rectangle'],
          props: 'Parallelogram with four right angles (90°). Diagonals are equal in length and bisect each other.'
        }},
        rhombus: {{
          name: 'Rhombus',
          ancestors: ['Quadrilateral', 'Trapezium', 'Parallelogram', 'Rhombus'],
          props: 'Parallelogram with all 4 sides equal. Diagonals bisect each other at right angles (90°) and bisect corner angles.'
        }},
        square: {{
          name: 'Square (The Royal Regular)',
          ancestors: ['Quadrilateral', 'Trapezium', 'Parallelogram', 'Rectangle', 'Rhombus', 'Square'],
          props: 'SIMULTANEOUSLY a Rectangle AND a Rhombus! 4 equal sides, 4 right angles (90°), equal diagonals intersecting at 90°.'
        }}
      }};

      function updateUI() {{
        const node = taxonomy[selectedNode];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; font-size:12px;">
            <div style="text-align:center; margin-bottom:10px; font-weight:bold; color:#38bdf8; font-size:14px;">
              Selected: <span style="color:#fcd34d;">${{node.name}}</span>
            </div>

            <!-- Interactive Tree Nodes -->
            <div style="display:flex; flex-direction:column; align-items:center; gap:8px;">
              <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Quadrilateral') ? '#10b981' : '#475569'}}; padding:6px 16px; border-radius:6px; font-weight:bold;">
                Quadrilateral (4 Sides, 360°)
              </div>
              <div style="color:#64748b;">↓</div>
              <div style="display:flex; justify-content:center; gap:20px; width:100%;">
                <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Kite') ? '#10b981' : '#475569'}}; padding:6px 14px; border-radius:6px;">
                  Kite (Adj =)
                </div>
                <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Trapezium') ? '#10b981' : '#475569'}}; padding:6px 14px; border-radius:6px;">
                  Trapezium (1 Pair ∥)
                </div>
              </div>
              <div style="color:#64748b;">↓</div>
              <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Parallelogram') ? '#10b981' : '#475569'}}; padding:6px 20px; border-radius:6px; font-weight:bold;">
                Parallelogram (2 Pairs ∥)
              </div>
              <div style="color:#64748b;">↙ ↘</div>
              <div style="display:flex; justify-content:center; gap:16px; width:100%;">
                <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Rectangle') ? '#10b981' : '#475569'}}; padding:6px 14px; border-radius:6px;">
                  Rectangle (4 Right ∠s)
                </div>
                <div style="background:#1e293b; border:1px solid ${{node.ancestors.includes('Rhombus') ? '#10b981' : '#475569'}}; padding:6px 14px; border-radius:6px;">
                  Rhombus (4 Equal Sides)
                </div>
              </div>
              <div style="color:#64748b;">↘ ↙</div>
              <div style="background:rgba(16,185,129,0.2); border:2px solid ${{node.ancestors.includes('Square') ? '#10b981' : '#475569'}}; padding:8px 24px; border-radius:8px; font-weight:bold; color:#34d399;">
                Square (Equilateral + Equiangular)
              </div>
            </div>

            <!-- Properties Box -->
            <div style="margin-top:12px; background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px 14px; text-align:left; line-height:1.5;">
              <strong style="color:#38bdf8;">Inherited Lineage:</strong> ${{node.ancestors.join(' ➔ ')}}
              <br><strong style="color:#fcd34d;">Key Properties:</strong> ${{node.props}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="btnSquare">Square</button>
        <button class="sim-btn" id="btnRect">Rectangle</button>
        <button class="sim-btn" id="btnRhombus">Rhombus</button>
        <button class="sim-btn" id="btnPara">Parallelogram</button>
        <button class="sim-btn" id="btnKite">Kite</button>
        <button class="sim-btn" id="btnTrap">Trapezium</button>
      `;

      document.getElementById('btnSquare').onclick = () => {{ selectedNode = 'square'; updateUI(); }};
      document.getElementById('btnRect').onclick = () => {{ selectedNode = 'rectangle'; updateUI(); }};
      document.getElementById('btnRhombus').onclick = () => {{ selectedNode = 'rhombus'; updateUI(); }};
      document.getElementById('btnPara').onclick = () => {{ selectedNode = 'parallelogram'; updateUI(); }};
      document.getElementById('btnKite').onclick = () => {{ selectedNode = 'kite'; updateUI(); }};
      document.getElementById('btnTrap').onclick = () => {{ selectedNode = 'trapezium'; updateUI(); }};

      updateUI();
    }}

    // Sim 16: Which Quad? Detective Riddle Matrix
    function renderSim16(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔍</span> Which Quad? Detective Riddle Matrix';
      badge.textContent = 'Interactive Deduction Challenge';

      let puzzleIdx = 0;
      let revealed = false;

      const puzzles = [
        {{
          clue: "My diagonals are equal in length and bisect each other at 90° right angles. All my sides are equal.",
          answer: "Square",
          why: "Diagonals bisect at 90° = Rhombus. Diagonals equal = Rectangle. Both together = Square!"
        }},
        {{
          clue: "My diagonals bisect each other and are equal in length, but my adjacent sides are strictly unequal.",
          answer: "Rectangle",
          why: "Diagonals bisect = Parallelogram. Diagonals equal = Rectangle. Unequal adjacent sides = Not a square."
        }},
        {{
          clue: "My diagonals bisect each other at right angles (90°), but they are unequal in length. All 4 of my sides are 8 cm.",
          answer: "Rhombus",
          why: "All sides equal + diagonals perpendicular = Rhombus. Unequal diagonals = Not a square."
        }},
        {{
          clue: "I have two pairs of equal adjacent sides and perpendicular diagonals, but no pairs of parallel opposite sides.",
          answer: "Kite",
          why: "Two pairs of equal adjacent sides + perpendicular diagonals = Kite."
        }}
      ];

      function updateUI() {{
        const p = puzzles[puzzleIdx];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="background:#0f172a; border:1px solid #6366f1; border-radius:12px; padding:16px 20px; text-align:left;">
              <div style="font-size:11px; font-weight:800; color:#38bdf8; text-transform:uppercase; margin-bottom:6px;">
                Mystery Case #${{puzzleIdx + 1}} of ${{puzzles.length}}
              </div>
              <div style="font-size:14px; color:#e2e8f0; font-style:italic; line-height:1.5;">
                "${{p.clue}}"
              </div>
            </div>

            ${{revealed ? `
              <div style="margin-top:14px; background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:10px; padding:12px; color:#34d399; font-size:13px; text-align:left;">
                <strong>Solved Identity: ${{p.answer}}!</strong>
                <br><span style="color:#cbd5e1; font-size:12px;">${{p.why}}</span>
              </div>
            ` : `
              <div style="margin-top:14px; font-size:12.5px; color:#94a3b8;">
                Make your deduction, then click "Reveal Identity" to verify!
              </div>
            `}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="pPrev">← Prev Case</button>
        <button class="sim-btn" id="pRev">Reveal Identity</button>
        <button class="sim-btn" id="pNext">Next Case →</button>
      `;

      document.getElementById('pPrev').onclick = () => {{
        if (puzzleIdx > 0) {{
          puzzleIdx--;
          revealed = false;
          updateUI();
        }}
      }};

      document.getElementById('pNext').onclick = () => {{
        if (puzzleIdx < puzzles.length - 1) {{
          puzzleIdx++;
          revealed = false;
          updateUI();
        }}
      }};

      document.getElementById('pRev').onclick = () => {{
        revealed = true;
        updateUI();
      }};

      updateUI();
    }}

    // Boot on page load
    window.onload = init;
  </script>
</body>
</html>"""
    return html_template

if __name__ == '__main__':
    html = generate_html()
    out_path = 'public/animations/class8-math-quadrilaterals.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {out_path} ({len(html)} bytes)")

