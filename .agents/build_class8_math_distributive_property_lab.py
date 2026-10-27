import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_distributive_property_data import slides_data, quiz_questions

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 6: We Distribute, Yet Things Multiply Master Lab</title>
  
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
      <h1 class="header-title">Chapter 6: We Distribute, Yet Things Multiply Master Lab</h1>
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
      <div class="slide-tag" id="slideTag">SECTION 6.1</div>
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
          "Welcome to Chapter 6: We Distribute, Yet Things Multiply! We will explore the geometric area model of distribution, the three landmark algebraic identities, and discover how to mend common algebraic mistakes."
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
        <p>Landmark algebraic identities: (a+b)², (a-b)², and difference of squares.</p>
      </div>
      <div id="quizContainer2" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide19" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 3 • Questions 21 to 30</h4>
        <p>Mental math patterns, base-100 deviations, and mending algebraic mistakes.</p>
      </div>
      <div id="quizContainer3" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide20" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 4 • Questions 31 to 40 (Final Slide)</h4>
        <p>Factoring by grouping, common monomials, and mystery detective riddles.</p>
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
      document.getElementById('slideTag').textContent = `CLASS 8 • CHAPTER 6 • PART ${{index + 1}}`;
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
        case 'distributive_rectangle_area_splitter':
          renderSim1(vp, controls, title, badge);
          break;
        case 'product_increment_visualizer':
          renderSim2(vp, controls, title, badge);
          break;
        case 'mental_math_distributive_speed_lab':
          renderSim3(vp, controls, title, badge);
          break;
        case 'four_quadrant_binomial_grid':
          renderSim4(vp, controls, title, badge);
          break;
        case 'square_of_sum_geometric_prover':
          renderSim5(vp, controls, title, badge);
          break;
        case 'square_of_difference_overlap_lab':
          renderSim6(vp, controls, title, badge);
          break;
        case 'difference_of_squares_animator':
          renderSim7(vp, controls, title, badge);
          break;
        case 'vedic_pattern_one_explorer':
          renderSim8(vp, controls, title, badge);
          break;
        case 'base_hundred_deviation_slider':
          renderSim9(vp, controls, title, badge);
          break;
        case 'consecutive_gap_square_lab':
          renderSim10(vp, controls, title, badge);
          break;
        case 'algebraic_mistake_mender':
          renderSim11(vp, controls, title, badge);
          break;
        case 'multiple_pathways_convergence_engine':
          renderSim12(vp, controls, title, badge);
          break;
        case 'common_factor_extractor_lab':
          renderSim13(vp, controls, title, badge);
          break;
        case 'grouping_terms_algebra_workbench':
          renderSim14(vp, controls, title, badge);
          break;
        case 'algebraic_identity_master_matrix':
          renderSim15(vp, controls, title, badge);
          break;
        case 'algebraic_puzzle_detective_room':
          renderSim16(vp, controls, title, badge);
          break;
        default:
          vp.innerHTML = '<div style="color:#64748b;">Simulator loading...</div>';
      }}
    }}

    // Sim 1: Distributive Rectangle Area Splitter
    function renderSim1(vp, controls, title, badge) {{
      title.innerHTML = '<span>📐</span> Distributive Rectangle Area Splitter';
      badge.textContent = "Geometric Proof: a(b + c) = ab + ac";

      let a = 8;
      let b = 12;
      let c = 6;

      function updateUI() {{
        const area1 = a * b;
        const area2 = a * c;
        const totalArea = a * (b + c);

        const scale = 14;
        const hPx = Math.min(a * scale, 130);
        const w1Px = Math.min(b * scale, 180);
        const w2Px = Math.min(c * scale, 120);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 460 200" style="width:100%; height:170px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <g transform="translate(70, 35)">
                <!-- Left Rectangle: a x b (Cyan) -->
                <rect x="0" y="0" width="${{w1Px}}" height="${{hPx}}" fill="rgba(6, 182, 212, 0.3)" stroke="#06b6d4" stroke-width="2"/>
                <text x="${{w1Px / 2}}" y="${{hPx / 2 + 5}}" fill="#67e8f9" font-size="13" font-weight="bold" text-anchor="middle">ab = ${{area1}}</text>
                <text x="${{w1Px / 2}}" y="-8" fill="#38bdf8" font-size="11" text-anchor="middle">Width b = ${{b}}</text>

                <!-- Right Rectangle: a x c (Amber) -->
                <rect x="${{w1Px}}" y="0" width="${{w2Px}}" height="${{hPx}}" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
                <text x="${{w1Px + w2Px / 2}}" y="${{hPx / 2 + 5}}" fill="#fcd34d" font-size="13" font-weight="bold" text-anchor="middle">ac = ${{area2}}</text>
                <text x="${{w1Px + w2Px / 2}}" y="-8" fill="#f59e0b" font-size="11" text-anchor="middle">Width c = ${{c}}</text>

                <!-- Height a label -->
                <text x="-12" y="${{hPx / 2 + 4}}" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="end">Height a = ${{a}}</text>
              </g>
            </svg>

            <div style="margin-top:8px; background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:13px; color:#cbd5e1;">
              Total Area = ${{a}} × (${{b}} + ${{c}}) = ${{a}}(${{b + c}}) = <strong style="color:#34d399; font-size:15px;">${{totalArea}}</strong>
              <br>Sum of Parts = ${{a}}(${{b}}) + ${{a}}(${{c}}) = ${{area1}} + ${{area2}} = <strong style="color:#34d399; font-size:15px;">${{totalArea}}</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Height (a):</span>
          <input type="range" id="a1Slider" min="4" max="10" value="${{a}}">
          <span id="a1Val">${{a}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Width (b):</span>
          <input type="range" id="b1Slider" min="6" max="15" value="${{b}}">
          <span id="b1Val">${{b}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Width (c):</span>
          <input type="range" id="c1Slider" min="3" max="10" value="${{c}}">
          <span id="c1Val">${{c}}</span>
        </div>
      `;

      document.getElementById('a1Slider').oninput = (e) => {{ a = parseInt(e.target.value); document.getElementById('a1Val').textContent = a; updateUI(); }};
      document.getElementById('b1Slider').oninput = (e) => {{ b = parseInt(e.target.value); document.getElementById('b1Val').textContent = b; updateUI(); }};
      document.getElementById('c1Slider').oninput = (e) => {{ c = parseInt(e.target.value); document.getElementById('c1Val').textContent = c; updateUI(); }};

      updateUI();
    }}

    // Sim 2: Increments in Products Visualizer
    function renderSim2(vp, controls, title, badge) {{
      title.innerHTML = '<span>📈</span> Increments in Products: (a + 1)(b + 1)';
      badge.textContent = "Growth = a + b + 1";

      let a = 8;
      let b = 5;

      function updateUI() {{
        const origProd = a * b;
        const newProd = (a + 1) * (b + 1);
        const diff = newProd - origProd;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 460 210" style="width:100%; height:170px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <g transform="translate(110, 30)">
                <!-- Base Rectangle ab (Indigo) -->
                <rect x="0" y="0" width="180" height="110" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="2"/>
                <text x="90" y="60" fill="#a5b4fc" font-size="14" font-weight="bold" text-anchor="middle">Original ab = ${{origProd}}</text>

                <!-- Right Strip: 1 x b (Emerald) -->
                <rect x="180" y="0" width="30" height="110" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
                <text x="195" y="60" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">b = ${{b}}</text>

                <!-- Bottom Strip: a x 1 (Amber) -->
                <rect x="0" y="110" width="180" height="30" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
                <text x="90" y="130" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">a = ${{a}}</text>

                <!-- Corner 1 x 1 Square (Rose) -->
                <rect x="180" y="110" width="30" height="30" fill="rgba(244, 63, 94, 0.4)" stroke="#f43f5e" stroke-width="2"/>
                <text x="195" y="130" fill="#fda4af" font-size="12" font-weight="bold" text-anchor="middle">1</text>
              </g>
            </svg>

            <div style="margin-top:8px; background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              New Product: (${{a}} + 1)(${{b}} + 1) = ${{a + 1}} × ${{b + 1}} = <strong style="color:#38bdf8;">${{newProd}}</strong>
              <br>Increase: a + b + 1 = ${{a}} + ${{b}} + 1 = <strong style="color:#fcd34d;">${{diff}}</strong> (${{origProd}} + ${{diff}} = ${{newProd}})
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Dimension a:</span>
          <input type="range" id="a2Slider" min="4" max="14" value="${{a}}">
          <span id="a2Val">${{a}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Dimension b:</span>
          <input type="range" id="b2Slider" min="3" max="10" value="${{b}}">
          <span id="b2Val">${{b}}</span>
        </div>
      `;

      document.getElementById('a2Slider').oninput = (e) => {{ a = parseInt(e.target.value); document.getElementById('a2Val').textContent = a; updateUI(); }};
      document.getElementById('b2Slider').oninput = (e) => {{ b = parseInt(e.target.value); document.getElementById('b2Val').textContent = b; updateUI(); }};

      updateUI();
    }}

    // Sim 3: Mental Math Distributive Speed Lab
    function renderSim3(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚡</span> Mental Math Distributive Speed Lab';
      badge.textContent = "Friendly Round-Base Splits";

      let problem = '43x99';

      const problems = {{
        '43x99': {{
          title: '43 × 99',
          split: '43 × (100 - 1)',
          steps: '43 × 100 - 43 × 1 = 4300 - 43 = 4257',
          ans: 4257
        }},
        '25x48': {{
          title: '25 × 48',
          split: '25 × (50 - 2)',
          steps: '25 × 50 - 25 × 2 = 1250 - 50 = 1200',
          ans: 1200
        }},
        '32x105': {{
          title: '32 × 105',
          split: '32 × (100 + 5)',
          steps: '32 × 100 + 32 × 5 = 3200 + 160 = 3360',
          ans: 3360
        }},
        '56x98': {{
          title: '56 × 98',
          split: '56 × (100 - 2)',
          steps: '56 × 100 - 56 × 2 = 5600 - 112 = 5488',
          ans: 5488
        }}
      }};

      function updateUI() {{
        const p = problems[problem];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="text-align:center; font-size:22px; color:#38bdf8; font-weight:bold; margin-bottom:12px;">
              ${{p.title}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; margin-bottom:10px;">
              <div style="font-size:12px; color:#94a3b8;">Strategic Distributive Split:</div>
              <div style="font-size:16px; color:#fcd34d; font-weight:bold; margin:6px 0;">= ${{p.split}}</div>
              <div style="font-size:14px; color:#e2e8f0; margin-top:8px;">${{p.steps}}</div>
            </div>

            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px; text-align:center; color:#34d399; font-size:16px; font-weight:bold;">
              Lightning Mental Result: ${{p.ans}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn active" id="b43x99">43 × 99</button>
        <button class="sim-btn" id="b25x48">25 × 48</button>
        <button class="sim-btn" id="b32x105">32 × 105</button>
        <button class="sim-btn" id="b56x98">56 × 98</button>
      `;

      document.getElementById('b43x99').onclick = () => {{ problem = '43x99'; updateUI(); }};
      document.getElementById('b25x48').onclick = () => {{ problem = '25x48'; updateUI(); }};
      document.getElementById('b32x105').onclick = () => {{ problem = '32x105'; updateUI(); }};
      document.getElementById('b56x98').onclick = () => {{ problem = '56x98'; updateUI(); }};

      updateUI();
    }}

    // Sim 4: Four-Quadrant Binomial Grid
    function renderSim4(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔲</span> Four-Quadrant Binomial Grid: (a + b)(c + d)';
      badge.textContent = "ac + ad + bc + bd Area Model";

      let a = 'x';
      let b = 4;
      let c = 'x';
      let d = 5;

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 440 210" style="width:100%; height:180px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <g transform="translate(90, 30)">
                <!-- Q1 Top-Left: a x c -->
                <rect x="0" y="0" width="130" height="75" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="2"/>
                <text x="65" y="42" fill="#67e8f9" font-size="14" font-weight="bold" text-anchor="middle">x²</text>

                <!-- Q2 Top-Right: a x d -->
                <rect x="130" y="0" width="90" height="75" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2"/>
                <text x="175" y="42" fill="#fcd34d" font-size="14" font-weight="bold" text-anchor="middle">5x</text>

                <!-- Q3 Bottom-Left: b x c -->
                <rect x="0" y="75" width="130" height="60" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
                <text x="65" y="110" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">4x</text>

                <!-- Q4 Bottom-Right: b x d -->
                <rect x="130" y="75" width="90" height="60" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="2"/>
                <text x="175" y="110" fill="#fda4af" font-size="14" font-weight="bold" text-anchor="middle">20</text>

                <!-- Labels -->
                <text x="65" y="-8" fill="#38bdf8" font-size="12" text-anchor="middle">x</text>
                <text x="175" y="-8" fill="#f59e0b" font-size="12" text-anchor="middle">+ 5</text>
                <text x="-12" y="42" fill="#38bdf8" font-size="12" text-anchor="end">x</text>
                <text x="-12" y="110" fill="#10b981" font-size="12" text-anchor="end">+ 4</text>
              </g>
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              (x + 4)(x + 5) = x² + 5x + 4x + 20 = <strong style="color:#34d399;">x² + 9x + 20</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bEg1">(x + 4)(x + 5) = x² + 9x + 20</button>
        <button class="sim-btn" id="bEg2">(2x + 3)(x + 4) = 2x² + 11x + 12</button>
      `;

      document.getElementById('bEg1').onclick = () => {{ updateUI(); }};
      document.getElementById('bEg2').onclick = () => {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:14px; text-align:left;">
              <strong style="color:#38bdf8;">(2x + 3)(x + 4) Expansion:</strong>
              <br>• Quadrant 1: 2x × x = <span style="color:#06b6d4; font-weight:bold;">2x²</span>
              <br>• Quadrant 2: 2x × 4 = <span style="color:#f59e0b; font-weight:bold;">8x</span>
              <br>• Quadrant 3: 3 × x = <span style="color:#10b981; font-weight:bold;">3x</span>
              <br>• Quadrant 4: 3 × 4 = <span style="color:#f43f5e; font-weight:bold;">12</span>
              <br><strong style="color:#34d399; margin-top:6px; display:inline-block;">Sum: 2x² + 11x + 12</strong>
            </div>
          </div>
        `;
      }};

      updateUI();
    }}

    // Sim 5: Square of the Sum Geometric Prover (a + b)²
    function renderSim5(vp, controls, title, badge) {{
      title.innerHTML = '<span>🟦</span> Square of the Sum Prover: (a + b)²';
      badge.textContent = "Identity I: a² + 2ab + b²";

      let a = 120;
      let b = 50;

      function updateUI() {{
        const totalSide = a + b;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 420 220" style="width:100%; height:180px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <g transform="translate(100, 20)">
                <!-- a^2 Square (Indigo) -->
                <rect x="0" y="0" width="${{a}}" height="${{a}}" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="2"/>
                <text x="${{a/2}}" y="${{a/2 + 5}}" fill="#a5b4fc" font-size="14" font-weight="bold" text-anchor="middle">a²</text>

                <!-- Top-Right ab Strip (Cyan) -->
                <rect x="${{a}}" y="0" width="${{b}}" height="${{a}}" fill="rgba(6, 182, 212, 0.3)" stroke="#06b6d4" stroke-width="2"/>
                <text x="${{a + b/2}}" y="${{a/2 + 5}}" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">ab</text>

                <!-- Bottom-Left ab Strip (Cyan) -->
                <rect x="0" y="${{a}}" width="${{a}}" height="${{b}}" fill="rgba(6, 182, 212, 0.3)" stroke="#06b6d4" stroke-width="2"/>
                <text x="${{a/2}}" y="${{a + b/2 + 5}}" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">ab</text>

                <!-- Bottom-Right b^2 Square (Amber) -->
                <rect x="${{a}}" y="${{a}}" width="${{b}}" height="${{b}}" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
                <text x="${{a + b/2}}" y="${{a + b/2 + 5}}" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">b²</text>

                <!-- Outer boundary -->
                <rect x="0" y="0" width="${{totalSide}}" height="${{totalSide}}" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="3,3"/>
              </g>
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              (a + b)² = <span style="color:#a5b4fc; font-weight:bold;">a²</span> + <span style="color:#67e8f9; font-weight:bold;">2ab</span> + <span style="color:#fcd34d; font-weight:bold;">b²</span>
              <br><strong style="color:#fb7185;">Notice the two cyan strips (2ab) that students often forget!</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bSquare32">Calculate 32² = (30 + 2)² = 1024</button>
        <button class="sim-btn" id="bSquare55">Calculate 55² = (50 + 5)² = 3025</button>
      `;

      document.getElementById('bSquare32').onclick = () => {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:14px;">
              <strong style="color:#38bdf8; font-size:15px;">32² using Identity I:</strong>
              <br>• a = 30, b = 2
              <br>• a² = 30² = 900
              <br>• 2ab = 2 × 30 × 2 = 120
              <br>• b² = 2² = 4
              <br><strong style="color:#34d399; font-size:16px; margin-top:6px; display:inline-block;">Total = 900 + 120 + 4 = 1024</strong>
            </div>
          </div>
        `;
      }};

      document.getElementById('bSquare55').onclick = () => {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:14px;">
              <strong style="color:#38bdf8; font-size:15px;">55² using Identity I:</strong>
              <br>• a = 50, b = 5
              <br>• a² = 50² = 2500
              <br>• 2ab = 2 × 50 × 5 = 500
              <br>• b² = 5² = 25
              <br><strong style="color:#34d399; font-size:16px; margin-top:6px; display:inline-block;">Total = 2500 + 500 + 25 = 3025</strong>
            </div>
          </div>
        `;
      }};

      updateUI();
    }}

    // Sim 6: Square of the Difference Overlap Lab (a - b)²
    function renderSim6(vp, controls, title, badge) {{
      title.innerHTML = '<span>✂️</span> Square of the Difference: (a - b)²';
      badge.textContent = "Identity II: a² - 2ab + b²";

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 420 220" style="width:100%; height:180px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <g transform="translate(100, 20)">
                <!-- Large Square a^2 -->
                <rect x="0" y="0" width="170" height="170" fill="none" stroke="#475569" stroke-width="2"/>

                <!-- Left-over (a - b)^2 (Emerald) -->
                <rect x="0" y="0" width="120" height="120" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
                <text x="60" y="65" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">(a - b)²</text>

                <!-- Subtracted Strip 1 (Top right) -->
                <rect x="120" y="0" width="50" height="170" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-dasharray="3,3"/>
                <text x="145" y="85" fill="#fb7185" font-size="11" text-anchor="middle">-ab</text>

                <!-- Subtracted Strip 2 (Bottom) -->
                <rect x="0" y="120" width="170" height="50" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-dasharray="3,3"/>
                <text x="60" y="150" fill="#fb7185" font-size="11" text-anchor="middle">-ab</text>

                <!-- Overlapping Corner (+b^2 restored) -->
                <rect x="120" y="120" width="50" height="50" fill="rgba(245, 158, 11, 0.5)" stroke="#f59e0b" stroke-width="2"/>
                <text x="145" y="150" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">+b²</text>
              </g>
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              Why +b²? Because subtracting two strips of area $ab$ removes the corner square <strong>twice</strong>! Adding $+b^2$ restores it.
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bSquare99">Calculate 99² = (100 - 1)² = 9801</button>
        <button class="sim-btn" id="bSquare48">Calculate 48² = (50 - 2)² = 2304</button>
      `;

      document.getElementById('bSquare99').onclick = () => {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:14px;">
              <strong style="color:#38bdf8; font-size:15px;">99² using Identity II:</strong>
              <br>• a = 100, b = 1
              <br>• a² = 100² = 10000
              <br>• -2ab = -2(100)(1) = -200
              <br>• +b² = +1² = +1
              <br><strong style="color:#34d399; font-size:16px; margin-top:6px; display:inline-block;">Total = 10000 - 200 + 1 = 9801</strong>
            </div>
          </div>
        `;
      }};

      document.getElementById('bSquare48').onclick = () => {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:14px;">
              <strong style="color:#38bdf8; font-size:15px;">48² using Identity II:</strong>
              <br>• a = 50, b = 2
              <br>• a² = 50² = 2500
              <br>• -2ab = -2(50)(2) = -200
              <br>• +b² = +2² = +4
              <br><strong style="color:#34d399; font-size:16px; margin-top:6px; display:inline-block;">Total = 2500 - 200 + 4 = 2304</strong>
            </div>
          </div>
        `;
      }};

      updateUI();
    }}

    // Sim 7: Difference of Two Squares Animator (a + b)(a - b) = a² - b²
    function renderSim7(vp, controls, title, badge) {{
      title.innerHTML = '<span>✂️</span> Difference of Two Squares: a² - b²';
      badge.textContent = "Identity III: (a + b)(a - b)";

      let isRearranged = false;

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 460 210" style="width:100%; height:180px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              ${{!isRearranged ? `
                <g transform="translate(130, 20)">
                  <!-- Large Square a^2 (160x160) -->
                  <polygon points="0,0 160,0 160,110 110,110 110,160 0,160" fill="rgba(6,182,212,0.3)" stroke="#06b6d4" stroke-width="2"/>
                  <!-- Missing Corner b^2 -->
                  <rect x="110" y="110" width="50" height="50" fill="none" stroke="#f43f5e" stroke-dasharray="3,3" stroke-width="2"/>
                  <text x="135" y="140" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">-b²</text>
                  <text x="55" y="85" fill="#67e8f9" font-size="15" font-weight="bold" text-anchor="middle">Area = a² - b²</text>
                </g>
              ` : `
                <g transform="translate(50, 40)">
                  <!-- Rearranged into rectangle of length (a+b) and width (a-b) -->
                  <rect x="0" y="0" width="220" height="110" fill="rgba(16,185,129,0.3)" stroke="#10b981" stroke-width="2"/>
                  <text x="110" y="60" fill="#34d399" font-size="15" font-weight="bold" text-anchor="middle">
                    Rearranged Rectangle = (a + b) × (a - b)
                  </text>
                  <text x="110" y="-8" fill="#38bdf8" font-size="12" text-anchor="middle">Length = a + b</text>
                  <text x="-12" y="60" fill="#38bdf8" font-size="12" text-anchor="end">Width = a - b</text>
                </g>
              `}}
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              <strong>Theorem:</strong> Cutting corner $b^2$ from square $a^2$ yields an L-shape that reshapes into a rectangle of dimensions $(a + b) \\times (a - b)$!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bRearrange">
          ${{isRearranged ? 'Return to L-Shape (a² - b²)' : 'Reshape L-Shape into Rectangle'}}
        </button>
      `;

      document.getElementById('bRearrange').onclick = () => {{
        isRearranged = !isRearranged;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 8: Vedic Pattern 1 Explorer: Same Tens & Units Sum = 10
    function renderSim8(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚡</span> Investigating Pattern 1: Same Tens & Units Sum = 10';
      badge.textContent = "T(T + 1) in Hundreds & u₁u₂ in Units";

      let T = 7;
      let u1 = 3;
      let u2 = 7;

      function updateUI() {{
        const left = T * (T + 1);
        const right = (u1 * u2).toString().padStart(2, '0');
        const num1 = 10 * T + u1;
        const num2 = 10 * T + u2;
        const ans = left * 100 + (u1 * u2);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:22px; color:#fff; font-weight:bold; margin-bottom:10px;">
              ${{num1}} × ${{num2}}
            </div>

            <div style="display:flex; justify-content:center; gap:16px; margin-bottom:12px;">
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:10px; padding:12px 18px;">
                <div style="font-size:11px; color:#94a3b8;">Left Part: T × (T + 1)</div>
                <div style="font-size:22px; font-weight:bold; color:#34d399;">${{T}} × ${{T+1}} = ${{left}}</div>
              </div>

              <div style="background:#1e293b; border:1px solid #f59e0b; border-radius:10px; padding:12px 18px;">
                <div style="font-size:11px; color:#94a3b8;">Right Part: u₁ × u₂</div>
                <div style="font-size:22px; font-weight:bold; color:#fcd34d;">${{u1}} × ${{u2}} = ${{right}}</div>
              </div>
            </div>

            <div style="background:rgba(6,182,212,0.15); border:1px solid #06b6d4; border-radius:8px; padding:10px; font-size:16px; color:#67e8f9; font-weight:bold;">
              Instant Answer: ${{left}}${{right}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bP1_73">73 × 77</button>
        <button class="sim-btn" id="bP1_34">34 × 36</button>
        <button class="sim-btn" id="bP1_82">82 × 88</button>
        <button class="sim-btn" id="bP1_45">45 × 45</button>
      `;

      document.getElementById('bP1_73').onclick = () => {{ T = 7; u1 = 3; u2 = 7; updateUI(); }};
      document.getElementById('bP1_34').onclick = () => {{ T = 3; u1 = 4; u2 = 6; updateUI(); }};
      document.getElementById('bP1_82').onclick = () => {{ T = 8; u1 = 2; u2 = 8; updateUI(); }};
      document.getElementById('bP1_45').onclick = () => {{ T = 4; u1 = 5; u2 = 5; updateUI(); }};

      updateUI();
    }}

    // Sim 9: Pattern 2: Numbers Near 100 (Base-100 Deviations)
    function renderSim9(vp, controls, title, badge) {{
      title.innerHTML = '<span>💯</span> Pattern 2: Base-100 Deviation Method';
      badge.textContent = "Cross-Addition & Deviation Products";

      let n1 = 104;
      let n2 = 107;

      function updateUI() {{
        const d1 = n1 - 100;
        const d2 = n2 - 100;
        const cross = n1 + d2;
        const prodDev = d1 * d2;
        const ans = n1 * n2;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:22px; color:#fff; font-weight:bold; margin-bottom:10px;">
              ${{n1}} × ${{n2}}
            </div>

            <div style="display:flex; justify-content:space-around; margin-bottom:12px;">
              <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px 14px;">
                <span style="color:#94a3b8;">${{n1}} deviation:</span> <strong style="color:${{d1 >= 0 ? '#34d399' : '#fb7185'}};">${{d1 >= 0 ? '+' : ''}}${{d1}}</strong>
              </div>
              <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px 14px;">
                <span style="color:#94a3b8;">${{n2}} deviation:</span> <strong style="color:${{d2 >= 0 ? '#34d399' : '#fb7185'}};">${{d2 >= 0 ? '+' : ''}}${{d2}}</strong>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:13px; color:#cbd5e1; margin-bottom:8px;">
              • Left Part (Cross-add): ${{n1}} + (${{d2}}) = <strong style="color:#38bdf8;">${{cross}}</strong>
              <br>• Right Part (Deviations product): (${{d1}}) × (${{d2}}) = <strong style="color:#fcd34d;">${{prodDev.toString().padStart(2, '0')}}</strong>
            </div>

            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:8px; color:#34d399; font-size:16px; font-weight:bold;">
              Product: ${{ans}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bP2_104x107">104 × 107</button>
        <button class="sim-btn" id="bP2_96x94">96 × 94 (Below 100)</button>
        <button class="sim-btn" id="bP2_108x103">108 × 103</button>
      `;

      document.getElementById('bP2_104x107').onclick = () => {{ n1 = 104; n2 = 107; updateUI(); }};
      document.getElementById('bP2_96x94').onclick = () => {{ n1 = 96; n2 = 94; updateUI(); }};
      document.getElementById('bP2_108x103').onclick = () => {{ n1 = 108; n2 = 103; updateUI(); }};

      updateUI();
    }}

    // Sim 10: Consecutive Product Patterns: n(n + 2) + 1 = (n + 1)²
    function renderSim10(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔢</span> Consecutive Product Pattern: n(n + 2) + 1 = (n + 1)²';
      badge.textContent = "Square Completion of Gap Products";

      let n = 9;

      function updateUI() {{
        const prod = n * (n + 2);
        const square = prod + 1;
        const middle = n + 1;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:20px; color:#fff; font-weight:bold; margin-bottom:10px;">
              ${{n}} × ${{n + 2}} + 1
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; margin-bottom:10px;">
              <div style="font-size:14px; color:#e2e8f0;">
                Product: ${{n}} × ${{n + 2}} = <strong style="color:#f59e0b;">${{prod}}</strong>
              </div>
              <div style="font-size:16px; color:#34d399; font-weight:bold; margin-top:6px;">
                Adding 1: ${{prod}} + 1 = ${{square}} = <span style="font-size:22px; color:#fcd34d;">${{middle}}²</span>
              </div>
            </div>

            <div style="font-size:12.5px; color:#94a3b8;">
              Algebra: n(n + 2) + 1 = n² + 2n + 1 = <strong>(n + 1)²</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bN9">n = 9 (9 × 11 + 1 = 100)</button>
        <button class="sim-btn" id="bN19">n = 19 (19 × 21 + 1 = 400)</button>
        <button class="sim-btn" id="bN49">n = 49 (49 × 51 + 1 = 2500)</button>
      `;

      document.getElementById('bN9').onclick = () => {{ n = 9; updateUI(); }};
      document.getElementById('bN19').onclick = () => {{ n = 19; updateUI(); }};
      document.getElementById('bN49').onclick = () => {{ n = 49; updateUI(); }};

      updateUI();
    }}

    // Sim 11: Algebraic Mistake Mender
    function renderSim11(vp, controls, title, badge) {{
      title.innerHTML = '<span>🛠️</span> Mind the Mistake, Mend the Mistake';
      badge.textContent = "Diagnostic Algebraic Repairs";

      let caseId = 'trap1';

      const traps = {{
        trap1: {{
          title: "Trap 1: The Freshman's Dream",
          wrong: "(x + 5)² = x² + 25",
          fix: "Powers do not distribute over addition! You must include the cross-term 2ab: (x + 5)² = x² + 2(x)(5) + 25 = x² + 10x + 25."
        }},
        trap2: {{
          title: "Trap 2: Distributing Negative Signs",
          wrong: "-(3x - 7) = -3x - 7",
          fix: "The negative sign multiplies every term: -(3x - 7) = -1(3x) + (-1)(-7) = -3x + 7."
        }},
        trap3: {{
          title: "Trap 3: Distribution over Multiplication",
          wrong: "2(3 × 4) = 6 × 8 = 48",
          fix: "Multiplication does NOT distribute over multiplication! 2(3 × 4) = 2 × 12 = 24."
        }},
        trap4: {{
          title: "Trap 4: Squaring Negatives",
          wrong: "(-3x)² = -9x²",
          fix: "A negative squared becomes positive: (-3x)² = (-3x) × (-3x) = +9x²."
        }}
      }};

      function updateUI() {{
        const t = traps[caseId];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="font-size:16px; color:#38bdf8; font-weight:bold; margin-bottom:10px;">
              ${{t.title}}
            </div>

            <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:8px; padding:10px; margin-bottom:10px;">
              <span style="color:#fb7185; font-size:11px; font-weight:bold; text-transform:uppercase;">Common Mistake:</span>
              <div style="color:#fecdd3; font-size:15px; font-weight:bold; margin-top:4px;">${{t.wrong}}</div>
            </div>

            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px;">
              <span style="color:#34d399; font-size:11px; font-weight:bold; text-transform:uppercase;">Mending the Mistake:</span>
              <div style="color:#cbd5e1; font-size:13px; line-height:1.5; margin-top:4px;">${{t.fix}}</div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bTrap1">Trap 1: (a + b)²</button>
        <button class="sim-btn" id="bTrap2">Trap 2: Signs</button>
        <button class="sim-btn" id="bTrap3">Trap 3: a(bc)</button>
        <button class="sim-btn" id="bTrap4">Trap 4: (-x)²</button>
      `;

      document.getElementById('bTrap1').onclick = () => {{ caseId = 'trap1'; updateUI(); }};
      document.getElementById('bTrap2').onclick = () => {{ caseId = 'trap2'; updateUI(); }};
      document.getElementById('bTrap3').onclick = () => {{ caseId = 'trap3'; updateUI(); }};
      document.getElementById('bTrap4').onclick = () => {{ caseId = 'trap4'; updateUI(); }};

      updateUI();
    }}

    // Sim 12: Multiple Pathways Convergence Engine (6.4 All Ways Lead to the Bay)
    function renderSim12(vp, controls, title, badge) {{
      title.innerHTML = '<span>⛵</span> All Ways Lead to the Bay: Equivalent Pathways';
      badge.textContent = "Path Invariance & Reverse Factoring";

      let k = 37;
      let x = 68;
      let y = 32;

      function updateUI() {{
        const path1 = k * (x + y);
        const prod1 = k * x;
        const prod2 = k * y;
        const path2 = prod1 + prod2;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="text-align:center; font-size:18px; color:#fff; font-weight:bold; margin-bottom:10px;">
              ${{k}} × ${{x}} + ${{k}} × ${{y}}
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:10px;">
              <div style="background:#0f172a; border:1px solid #06b6d4; border-radius:8px; padding:10px;">
                <div style="color:#06b6d4; font-size:11px; font-weight:bold;">Pathway A: Factor First</div>
                <div style="font-size:13px; color:#e2e8f0; margin-top:4px;">
                  = ${{k}} × (${{x}} + ${{y}})
                  <br>= ${{k}} × ${{x + y}}
                  <br><strong style="color:#34d399; font-size:16px;">= ${{path1}}</strong>
                </div>
              </div>

              <div style="background:#0f172a; border:1px solid #f59e0b; border-radius:8px; padding:10px;">
                <div style="color:#f59e0b; font-size:11px; font-weight:bold;">Pathway B: Multiply First</div>
                <div style="font-size:13px; color:#e2e8f0; margin-top:4px;">
                  = ${{prod1}} + ${{prod2}}
                  <br><strong style="color:#34d399; font-size:16px;">= ${{path2}}</strong>
                </div>
              </div>
            </div>

            <div style="background:rgba(99,102,241,0.15); border:1px solid #6366f1; border-radius:8px; padding:8px; text-align:center; font-size:12.5px; color:#c7d2fe;">
              ✓ Both pathways arrive at the exact same bay: <strong>${{path1}}</strong>! Factoring first makes it effortless.
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bEgP1">37 × 68 + 37 × 32</button>
        <button class="sim-btn" id="bEgP2">84 × 73 + 84 × 27</button>
        <button class="sim-btn" id="bEgP3">25 × 199 + 25 × 1</button>
      `;

      document.getElementById('bEgP1').onclick = () => {{ k = 37; x = 68; y = 32; updateUI(); }};
      document.getElementById('bEgP2').onclick = () => {{ k = 84; x = 73; y = 27; updateUI(); }};
      document.getElementById('bEgP3').onclick = () => {{ k = 25; x = 199; y = 1; updateUI(); }};

      updateUI();
    }}

    // Sim 13: Common Factor Extractor Lab
    function renderSim13(vp, controls, title, badge) {{
      title.innerHTML = '<span>📦</span> Common Factor Extractor Workbench';
      badge.textContent = "Greatest Common Monomial Factoring";

      let currentEx = 'ex1';

      const exs = {{
        ex1: {{
          orig: "12x²y + 18xy²",
          gcf: "6xy",
          rest: "(2x + 3y)",
          steps: "GCF of (12, 18) = 6. Common powers: x¹ and y¹. Dividing each term: 12x²y ÷ 6xy = 2x, 18xy² ÷ 6xy = 3y."
        }},
        ex2: {{
          orig: "15a³b² - 25a²b³",
          gcf: "5a²b²",
          rest: "(3a - 5b)",
          steps: "GCF of (15, 25) = 5. Common powers: a² and b². Dividing: 15a³b² ÷ 5a²b² = 3a, -25a²b³ ÷ 5a²b² = -5b."
        }}
      }};

      function updateUI() {{
        const item = exs[currentEx];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="font-size:18px; color:#38bdf8; font-weight:bold; margin-bottom:8px;">
              Original: ${{item.orig}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:12px; margin-bottom:10px; font-size:13px; color:#cbd5e1;">
              ${{item.steps}}
            </div>

            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px; text-align:center;">
              <span style="color:#94a3b8; font-size:12px;">Completely Factored Form:</span>
              <div style="font-size:20px; font-weight:bold; color:#34d399; margin-top:4px;">
                <span style="color:#fcd34d;">${{item.gcf}}</span>${{item.rest}}
              </div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bEx1">12x²y + 18xy²</button>
        <button class="sim-btn" id="bEx2">15a³b² - 25a²b³</button>
      `;

      document.getElementById('bEx1').onclick = () => {{ currentEx = 'ex1'; updateUI(); }};
      document.getElementById('bEx2').onclick = () => {{ currentEx = 'ex2'; updateUI(); }};

      updateUI();
    }}

    // Sim 14: Grouping Terms Algebra Workbench
    function renderSim14(vp, controls, title, badge) {{
      title.innerHTML = '<span>🧩</span> Factoring by Grouping Terms (4-Term Polynomials)';
      badge.textContent = "Pairwise Binomial Factorization";

      let currentCase = 'c1';

      const cases = {{
        c1: {{
          poly: "ax + ay + bx + by",
          step1: "(ax + ay) + (bx + by)",
          step2: "a(x + y) + b(x + y)",
          final: "(a + b)(x + y)"
        }},
        c2: {{
          poly: "15xy - 6x + 5y - 2",
          step1: "(15xy - 6x) + (5y - 2)",
          step2: "3x(5y - 2) + 1(5y - 2)",
          final: "(3x + 1)(5y - 2)"
        }}
      }};

      function updateUI() {{
        const c = cases[currentCase];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="font-size:18px; color:#fff; font-weight:bold; margin-bottom:8px;">
              Polynomial: ${{c.poly}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:12px; display:flex; flex-direction:column; gap:6px; font-size:13px; color:#cbd5e1; margin-bottom:8px;">
              <div><strong>Step 1 (Group pairs):</strong> ${{c.step1}}</div>
              <div><strong>Step 2 (Factor monomials):</strong> ${{c.step2}}</div>
              <div><strong>Step 3 (Factor shared binomial):</strong> <span style="color:#34d399; font-weight:bold; font-size:15px;">${{c.final}}</span></div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bGrp1">ax + ay + bx + by</button>
        <button class="sim-btn" id="bGrp2">15xy - 6x + 5y - 2</button>
      `;

      document.getElementById('bGrp1').onclick = () => {{ currentCase = 'c1'; updateUI(); }};
      document.getElementById('bGrp2').onclick = () => {{ currentCase = 'c2'; updateUI(); }};

      updateUI();
    }}

    // Sim 15: Algebraic Identity Master Matrix
    function renderSim15(vp, controls, title, badge) {{
      title.innerHTML = '<span>🏛️</span> Master Algebraic Identity Matrix';
      badge.textContent = "The 4 Pillar Identities";

      let idKey = 'id1';

      const ids = {{
        id1: {{
          name: "Identity I: Square of a Sum",
          formula: "(a + b)² = a² + 2ab + b²",
          example: "(2x + 3y)² = 4x² + 12xy + 9y²",
          geo: "Square of side (a+b) dissected into 2 squares (a², b²) and 2 rectangles (2ab)."
        }},
        id2: {{
          name: "Identity II: Square of a Difference",
          formula: "(a - b)² = a² - 2ab + b²",
          example: "(3x - 5y)² = 9x² - 30xy + 25y²",
          geo: "Square of side a with two strips ab removed and doubly-subtracted corner b² restored."
        }},
        id3: {{
          name: "Identity III: Difference of Two Squares",
          formula: "(a + b)(a - b) = a² - b²",
          example: "(4x + 7)(4x - 7) = 16x² - 49",
          geo: "L-shaped region a² - b² reshaped into a rectangle of (a+b) × (a-b)."
        }},
        id4: {{
          name: "Identity IV: Common Variable Binomial",
          formula: "(x + a)(x + b) = x² + (a + b)x + ab",
          example: "(x + 4)(x + 7) = x² + 11x + 28",
          geo: "Rectangle of length (x+a) and width (x+b) divided into x², ax, bx, and ab."
        }}
      }};

      function updateUI() {{
        const item = ids[idKey];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="font-size:16px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">
              ${{item.name}}
            </div>

            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:12px; margin-bottom:8px;">
              <div style="font-size:18px; color:#fcd34d; font-weight:bold;">${{item.formula}}</div>
              <div style="font-size:13px; color:#cbd5e1; margin-top:6px;">Example: ${{item.example}}</div>
            </div>

            <div style="font-size:12px; color:#94a3b8; background:rgba(30,41,59,0.5); padding:8px; border-radius:6px;">
              <strong>Geometric Meaning:</strong> ${{item.geo}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bId1">(a + b)²</button>
        <button class="sim-btn" id="bId2">(a - b)²</button>
        <button class="sim-btn" id="bId3">(a + b)(a - b)</button>
        <button class="sim-btn" id="bId4">(x + a)(x + b)</button>
      `;

      document.getElementById('bId1').onclick = () => {{ idKey = 'id1'; updateUI(); }};
      document.getElementById('bId2').onclick = () => {{ idKey = 'id2'; updateUI(); }};
      document.getElementById('bId3').onclick = () => {{ idKey = 'id3'; updateUI(); }};
      document.getElementById('bId4').onclick = () => {{ idKey = 'id4'; updateUI(); }};

      updateUI();
    }}

    // Sim 16: Algebraic Puzzle Detective Room
    function renderSim16(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔍</span> Algebraic Puzzle Detective Room';
      badge.textContent = "Mystery Coefficients & Area Puzzles";

      let caseNum = 0;
      let solved = false;

      const cases = [
        {{
          clue: "If (x + 5)(x + A) = x² + Bx + 35, find the secret integers A and B.",
          answer: "A = 7, B = 12",
          reason: "Constant term: 5 × A = 35 ➔ A = 7. Middle coefficient: B = 5 + A = 5 + 7 = 12!"
        }},
        {{
          clue: "Find K so that 4x² + Kx + 25 is a perfect square trinomial (2x + 5)².",
          answer: "K = 20",
          reason: "(2x + 5)² = 4x² + 2(2x)(5) + 25 = 4x² + 20x + 25. Therefore K = 20."
        }},
        {{
          clue: "What is the exact numerical value of (1001² - 999²) / 4000 without using a calculator?",
          answer: "1",
          reason: "Difference of squares: 1001² - 999² = (1001 + 999)(1001 - 999) = 2000 × 2 = 4000. 4000 ÷ 4000 = 1!"
        }}
      ];

      function updateUI() {{
        const c = cases[caseNum];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="background:#0f172a; border:1px solid #6366f1; border-radius:12px; padding:16px 20px; text-align:left;">
              <div style="font-size:11px; font-weight:800; color:#38bdf8; text-transform:uppercase; margin-bottom:6px;">
                Mystery Case #${{caseNum + 1}} of ${{cases.length}}
              </div>
              <div style="font-size:14px; color:#e2e8f0; font-style:italic; line-height:1.5;">
                "${{c.clue}}"
              </div>
            </div>

            ${{solved ? `
              <div style="margin-top:14px; background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:10px; padding:12px; color:#34d399; font-size:13px; text-align:left;">
                <strong>Solved Deduction: ${{c.answer}}!</strong>
                <br><span style="color:#cbd5e1; font-size:12px;">${{c.reason}}</span>
              </div>
            ` : `
              <div style="margin-top:14px; font-size:12.5px; color:#94a3b8;">
                Solve in your head, then click "Reveal Deduction" to verify!
              </div>
            `}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="cPrev">← Prev Case</button>
        <button class="sim-btn" id="cSolve">Reveal Deduction</button>
        <button class="sim-btn" id="cNext">Next Case →</button>
      `;

      document.getElementById('cPrev').onclick = () => {{
        if (caseNum > 0) {{
          caseNum--;
          solved = false;
          updateUI();
        }}
      }};

      document.getElementById('cNext').onclick = () => {{
        if (caseNum < cases.length - 1) {{
          caseNum++;
          solved = false;
          updateUI();
        }}
      }};

      document.getElementById('cSolve').onclick = () => {{
        solved = true;
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
    out_path = 'public/animations/class8-math-distributive-property.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {out_path} ({len(html)} bytes)")
