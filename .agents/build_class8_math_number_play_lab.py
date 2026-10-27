import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_number_play_data import slides_data, quiz_questions

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 5: Number Play Master Lab</title>
  
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
      <h1 class="header-title">Chapter 5: Number Play Master Lab</h1>
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
      <div class="slide-tag" id="slideTag">SECTION 5.1</div>
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
          "Welcome to Chapter 5: Number Play! We will discover multiples, parity invariants, rapid divisibility shortcuts, and solve digits in disguise."
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
        <p>Divisibility shortcuts for 9, 3, and 11 with place-value proofs.</p>
      </div>
      <div id="quizContainer2" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide19" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 3 • Questions 21 to 30</h4>
        <p>Composite divisibility, powers of 2 & 5, and digital roots.</p>
      </div>
      <div id="quizContainer3" style="display:flex; flex-direction:column; gap:16px;"></div>
    </div>

    <div id="quizSlide20" style="display:none;" class="quiz-container">
      <div class="theory-box" style="margin-bottom:8px;">
        <h4>Mastery Challenge 4 • Questions 31 to 40 (Final Slide)</h4>
        <p>Cryptarithms, alphametics, and detective number puzzles.</p>
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
      document.getElementById('slideTag').textContent = `CLASS 8 • CHAPTER 5 • PART ${{index + 1}}`;
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
        case 'multiples_number_line_hopper':
          renderSim1(vp, controls, title, badge);
          break;
        case 'consecutive_sum_builder':
          renderSim2(vp, controls, title, badge);
          break;
        case 'parity_algebra_matrix':
          renderSim3(vp, controls, title, badge);
          break;
        case 'breaking_even_parity_game':
          renderSim4(vp, controls, title, badge);
          break;
        case 'pairs_to_make_fours_lab':
          renderSim5(vp, controls, title, badge);
          break;
        case 'always_sometimes_never_tester':
          renderSim6(vp, controls, title, badge);
          break;
        case 'division_clock_modular_lab':
          renderSim7(vp, controls, title, badge);
          break;
        case 'figurate_dot_pattern_engine':
          renderSim8(vp, controls, title, badge);
          break;
        case 'divisibility_by_9_decomposer':
          renderSim9(vp, controls, title, badge);
          break;
        case 'divisibility_by_3_scanner':
          renderSim10(vp, controls, title, badge);
          break;
        case 'divisibility_by_11_balance_scale':
          renderSim11(vp, controls, title, badge);
          break;
        case 'power_of_two_and_five_explorer':
          renderSim12(vp, controls, title, badge);
          break;
        case 'composite_coprime_rule_matrix':
          renderSim13(vp, controls, title, badge);
          break;
        case 'digital_root_cast_out_nines_calculator':
          renderSim14(vp, controls, title, badge);
          break;
        case 'cryptarithm_solver_workbench':
          renderSim15(vp, controls, title, badge);
          break;
        case 'number_detective_puzzle_room':
          renderSim16(vp, controls, title, badge);
          break;
        default:
          vp.innerHTML = '<div style="color:#64748b;">Simulator loading...</div>';
      }}
    }}

    // Sim 1: Multiples on the Number Line Hopper
    function renderSim1(vp, controls, title, badge) {{
      title.innerHTML = '<span>🦘</span> Multiples Number Line Hopper';
      badge.textContent = 'Division Algorithm & Zero Remainder';

      let d = 4; // hop size
      let target = 24;

      function updateUI() {{
        const q = Math.floor(target / d);
        const r = target % d;
        const isMultiple = (r === 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 500 180" style="width:100%; height:160px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Number line axis (0 to 36) -->
              <line x1="30" y1="130" x2="470" y2="130" stroke="#475569" stroke-width="2"/>
              <!-- Ticks and labels -->
              ${{Array.from({{length: 10}}).map((_, i) => {{
                const val = i * 4;
                const x = 30 + (val / 36) * 440;
                return `
                  <line x1="${{x}}" y1="125" x2="${{x}}" y2="135" stroke="#64748b" stroke-width="1.5"/>
                  <text x="${{x}}" y="148" fill="#94a3b8" font-size="10" text-anchor="middle">${{val}}</text>
                `;
              }}).join('')}}

              <!-- Hops arcs of size d -->
              ${{Array.from({{length: Math.min(Math.floor(36/d) + 1, 10)}}).map((_, i) => {{
                if (i === 0) return '';
                const prevX = 30 + ((i-1)*d / 36) * 440;
                const curX = 30 + (i*d / 36) * 440;
                const midX = (prevX + curX) / 2;
                return `
                  <path d="M ${{prevX}} 128 Q ${{midX}} ${{128 - d*6}} ${{curX}} 128" fill="none" stroke="#6366f1" stroke-width="2"/>
                  <circle cx="${{curX}}" cy="128" r="3.5" fill="#a5b4fc"/>
                `;
              }}).join('')}}

              <!-- Target Marker -->
              ${{(() => {{
                const tx = 30 + (target / 36) * 440;
                return `
                  <circle cx="${{tx}}" cy="128" r="6" fill="${{isMultiple ? '#10b981' : '#f43f5e'}}"/>
                  <text x="${{tx}}" y="100" fill="${{isMultiple ? '#34d399' : '#fb7185'}}" font-size="12" font-weight="bold" text-anchor="middle">
                    Target: ${{target}}
                  </text>
                  <line x1="${{tx}}" y1="105" x2="${{tx}}" y2="122" stroke="${{isMultiple ? '#10b981' : '#f43f5e'}}" stroke-width="1.5"/>
                `;
              }})()}}
            </svg>

            <div style="margin-top:10px; background:#0f172a; border:1px solid ${{isMultiple ? '#10b981' : '#334155'}}; border-radius:8px; padding:10px; font-size:12.5px; color:#cbd5e1;">
              <strong>Division Statement:</strong> ${{target}} = ${{d}} × ${{q}} + <span style="color:${{isMultiple ? '#34d399' : '#fb7185'}}; font-weight:bold;">${{r}} (Remainder)</span>
              <br><span style="color:${{isMultiple ? '#34d399' : '#f59e0b'}};">
                ${{isMultiple ? `✓ ${{target}} lands exactly on hop #${{q}}! It is a MULTIPLE of ${{d}}.` : `✗ ${{target}} falls between hops with remainder ${{r}}. Not a multiple.`}}
              </span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Hop Size (d):</span>
          <input type="range" id="dSlider" min="2" max="9" value="${{d}}">
          <span id="dVal">${{d}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Target (N):</span>
          <input type="range" id="tSlider" min="4" max="36" value="${{target}}">
          <span id="tVal">${{target}}</span>
        </div>
      `;

      document.getElementById('dSlider').oninput = (e) => {{
        d = parseInt(e.target.value);
        document.getElementById('dVal').textContent = d;
        updateUI();
      }};

      document.getElementById('tSlider').oninput = (e) => {{
        target = parseInt(e.target.value);
        document.getElementById('tVal').textContent = target;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 2: Consecutive Number Partition Builder
    function renderSim2(vp, controls, title, badge) {{
      title.innerHTML = '<span>➕</span> Sum of Consecutive Numbers Builder';
      badge.textContent = 'Integer Partitions & Powers of 2';

      let N = 15;

      function findPartitions(num) {{
        const parts = [];
        for (let m = 2; m * (m + 1) / 2 <= num; m++) {{
          const numMinusTri = num - m * (m - 1) / 2;
          if (numMinusTri % m === 0) {{
            const k = numMinusTri / m;
            if (k > 0) {{
              const seq = [];
              for (let i = 0; i < m; i++) seq.push(k + i);
              parts.push(seq);
            }}
          }}
        }}
        return parts;
      }}

      function updateUI() {{
        const partitions = findPartitions(N);
        const isPowerOf2 = (N & (N - 1)) === 0 && N > 0;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:16px; font-weight:bold; color:#38bdf8; margin-bottom:8px;">
              Decomposing Target: <span style="font-size:24px; color:#fcd34d;">${{N}}</span>
            </div>

            ${{isPowerOf2 ? `
              <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:10px; padding:16px; color:#fecdd3; font-size:13px; line-height:1.6;">
                <strong>🚫 The Powers of 2 Theorem:</strong>
                <br>${{N}} = 2^${{Math.log2(N)}} has <em>NO odd prime factors</em>!
                <br>Because every consecutive sum partition requires at least one odd divisor, ${{N}} can <strong>NEVER</strong> be expressed as a sum of consecutive positive integers!
              </div>
            ` : `
              <div style="display:flex; flex-direction:column; gap:8px; max-height:160px; overflow-y:auto; padding:4px;">
                ${{partitions.map((seq, idx) => `
                  <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px 12px; font-size:13px; display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#94a3b8; font-size:11px;">${{seq.length}} consecutive terms:</span>
                    <span style="color:#34d399; font-weight:bold;">${{seq.join(' + ')}} = ${{N}}</span>
                  </div>
                `).join('')}}
              </div>
            `}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Number N:</span>
          <input type="range" id="nSlider" min="3" max="36" value="${{N}}">
          <span id="nVal">${{N}}</span>
        </div>
        <button class="sim-btn" id="btnP15">Set 15 (3 Partitions)</button>
        <button class="sim-btn" id="btnP16" style="border-color:#f43f5e;">Set 16 (Power of 2)</button>
      `;

      document.getElementById('nSlider').oninput = (e) => {{
        N = parseInt(e.target.value);
        document.getElementById('nVal').textContent = N;
        updateUI();
      }};

      document.getElementById('btnP15').onclick = () => {{
        N = 15;
        document.getElementById('nSlider').value = 15;
        document.getElementById('nVal').textContent = 15;
        updateUI();
      }};

      document.getElementById('btnP16').onclick = () => {{
        N = 16;
        document.getElementById('nSlider').value = 16;
        document.getElementById('nVal').textContent = 16;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 3: Parity Algebra Matrix
    function renderSim3(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚡</span> Parity Algebra & Modulo 3 Matrix';
      badge.textContent = 'Odd-Even Symmetries & Residues';

      let op = 'add'; // 'add' or 'mul'

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:500px; text-align:center;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">
              Active Operation: <strong style="color:#38bdf8;">${{op === 'add' ? 'Addition (+)' : 'Multiplication (×)'}}</strong>
            </div>

            <table style="width:100%; border-collapse:collapse; background:#0f172a; border:1px solid #334155; border-radius:8px; overflow:hidden; font-size:12.5px;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; border-bottom:1px solid #334155;">
                  <th style="padding:8px;">Input A</th>
                  <th style="padding:8px;">Input B</th>
                  <th style="padding:8px;">Algebraic Expression</th>
                  <th style="padding:8px;">Result Parity</th>
                </tr>
              </thead>
              <tbody>
                ${{op === 'add' ? `
                  <tr style="border-bottom:1px solid #1e293b;">
                    <td style="padding:6px; color:#34d399;">Even (2a)</td>
                    <td style="color:#34d399;">Even (2b)</td>
                    <td style="color:#94a3b8;">2(a + b)</td>
                    <td><span style="color:#34d399; font-weight:bold;">EVEN</span></td>
                  </tr>
                  <tr style="border-bottom:1px solid #1e293b;">
                    <td style="padding:6px; color:#f43f5e;">Odd (2a+1)</td>
                    <td style="color:#f43f5e;">Odd (2b+1)</td>
                    <td style="color:#94a3b8;">2(a + b + 1)</td>
                    <td><span style="color:#34d399; font-weight:bold;">EVEN</span></td>
                  </tr>
                  <tr>
                    <td style="padding:6px; color:#34d399;">Even (2a)</td>
                    <td style="color:#f43f5e;">Odd (2b+1)</td>
                    <td style="color:#94a3b8;">2(a + b) + 1</td>
                    <td><span style="color:#f43f5e; font-weight:bold;">ODD</span></td>
                  </tr>
                ` : `
                  <tr style="border-bottom:1px solid #1e293b;">
                    <td style="padding:6px; color:#34d399;">Even (2a)</td>
                    <td style="color:#34d399;">Even (2b)</td>
                    <td style="color:#94a3b8;">4ab = 2(2ab)</td>
                    <td><span style="color:#34d399; font-weight:bold;">EVEN</span></td>
                  </tr>
                  <tr style="border-bottom:1px solid #1e293b;">
                    <td style="padding:6px; color:#f43f5e;">Odd (2a+1)</td>
                    <td style="color:#f43f5e;">Odd (2b+1)</td>
                    <td style="color:#94a3b8;">2(2ab+a+b) + 1</td>
                    <td><span style="color:#f43f5e; font-weight:bold;">ODD</span></td>
                  </tr>
                  <tr>
                    <td style="padding:6px; color:#34d399;">Even (2a)</td>
                    <td style="color:#f43f5e;">Odd (2b+1)</td>
                    <td style="color:#94a3b8;">2a(2b+1)</td>
                    <td><span style="color:#34d399; font-weight:bold;">EVEN</span></td>
                  </tr>
                `}}
              </tbody>
            </table>

            <div style="margin-top:10px; background:rgba(6,182,212,0.15); border:1px solid #06b6d4; border-radius:8px; padding:8px; font-size:12px; color:#67e8f9;">
              Key Insight: Odd × Odd is the ONLY multiplication that produces an Odd number!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn ${{op === 'add' ? 'active' : ''}}" id="bAdd">Addition (+)</button>
        <button class="sim-btn ${{op === 'mul' ? 'active' : ''}}" id="bMul">Multiplication (×)</button>
      `;

      document.getElementById('bAdd').onclick = () => {{ op = 'add'; updateUI(); }};
      document.getElementById('bMul').onclick = () => {{ op = 'mul'; updateUI(); }};

      updateUI();
    }}

    // Sim 4: Breaking Even & Parity Invariant Game
    function renderSim4(vp, controls, title, badge) {{
      title.innerHTML = '<span>🪙</span> Parity Invariance & 15 Coins Puzzle';
      badge.textContent = 'Conservation of Parity Invariant';

      let heads = 7;
      const total = 15;

      function updateUI() {{
        const tails = total - heads;
        const isHeadsOdd = (heads % 2 !== 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="display:flex; justify-content:space-around; align-items:center; margin-bottom:12px;">
              <div style="background:#0f172a; border:1px solid #38bdf8; border-radius:10px; padding:10px 16px;">
                <div style="font-size:11px; color:#94a3b8;">Heads (Target: 0 or 15)</div>
                <div style="font-size:26px; font-weight:bold; color:#38bdf8;">${{heads}}</div>
                <div style="font-size:11px; color:${{isHeadsOdd ? '#34d399' : '#f43f5e'}};">${{isHeadsOdd ? 'Parity: ODD' : 'Parity: EVEN'}}</div>
              </div>

              <div style="background:#0f172a; border:1px solid #f59e0b; border-radius:10px; padding:10px 16px;">
                <div style="font-size:11px; color:#94a3b8;">Tails</div>
                <div style="font-size:26px; font-weight:bold; color:#f59e0b;">${{tails}}</div>
                <div style="font-size:11px; color:#94a3b8;">Total = 15</div>
              </div>
            </div>

            <!-- Coin Grid -->
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:6px; max-width:320px; margin:0 auto 10px;">
              ${{Array.from({{length: total}}).map((_, i) => `
                <div style="width:34px; height:34px; border-radius:50%; background:${{i < heads ? '#0284c7' : '#d97706'}}; border:2px solid #fff; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:13px; color:#fff;">
                  ${{i < heads ? 'H' : 'T'}}
                </div>
              `).join('')}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px 12px; font-size:12px; color:#cbd5e1;">
              Flipping 2 coins changes Heads count by <strong>+2, 0, or -2</strong>. The parity of Heads is an <em>INVARIANT</em> (always stays Odd)!
              <br><span style="color:#fb7185; font-weight:bold;">Reaching 0 Heads (even) is mathematically impossible!</span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="flip2T" ${{heads >= total - 1 ? 'disabled' : ''}}>Flip 2 Tails ➔ Heads (+2)</button>
        <button class="sim-btn" id="flip2H" ${{heads <= 1 ? 'disabled' : ''}}>Flip 2 Heads ➔ Tails (-2)</button>
        <button class="sim-btn" id="flip1H1T">Flip 1H & 1T (0 change)</button>
        <button class="sim-btn" id="rstCoins">Reset (7H, 8T)</button>
      `;

      document.getElementById('flip2T').onclick = () => {{ if (heads + 2 <= total) heads += 2; updateUI(); }};
      document.getElementById('flip2H').onclick = () => {{ if (heads - 2 >= 0) heads -= 2; updateUI(); }};
      document.getElementById('flip1H1T').onclick = () => {{ updateUI(); }};
      document.getElementById('rstCoins').onclick = () => {{ heads = 7; updateUI(); }};

      updateUI();
    }}

    // Sim 5: Pairs to Make Fours Lab
    function renderSim5(vp, controls, title, badge) {{
      title.innerHTML = '<span>🧱</span> Pairs to Make Fours & 100-Split Lab';
      badge.textContent = '100 = 4 × 25 Divisibility Proof';

      let num = 7428;

      function updateUI() {{
        const hundreds = Math.floor(num / 100);
        const lastTwo = num % 100;
        const isDiv4 = (lastTwo % 4 === 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:14px; color:#94a3b8; margin-bottom:8px;">
              Analyzing Number: <span style="font-size:24px; color:#38bdf8; font-weight:bold;">${{num}}</span>
            </div>

            <!-- Base 10 Block Deconstruction -->
            <div style="display:flex; justify-content:center; gap:12px; margin-bottom:12px;">
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:10px; padding:12px; min-width:160px;">
                <div style="font-size:11px; color:#94a3b8;">Hundreds Part</div>
                <div style="font-size:20px; font-weight:bold; color:#34d399;">${{hundreds}}00</div>
                <div style="font-size:11px; color:#a7f3d0; margin-top:4px;">= 4 × (${{hundreds * 25}})</div>
                <div style="font-size:10px; color:#10b981; font-weight:bold;">ALWAYS DIVISIBLE BY 4</div>
              </div>

              <div style="font-size:24px; font-weight:bold; color:#64748b; align-self:center;">+</div>

              <div style="background:#1e293b; border:1px solid ${{isDiv4 ? '#10b981' : '#f43f5e'}}; border-radius:10px; padding:12px; min-width:160px;">
                <div style="font-size:11px; color:#94a3b8;">Last 2 Digits</div>
                <div style="font-size:20px; font-weight:bold; color:${{isDiv4 ? '#34d399' : '#fb7185'}};">${{lastTwo.toString().padStart(2, '0')}}</div>
                <div style="font-size:11px; color:#cbd5e1; margin-top:4px;">${{lastTwo}} = 4 × ${{Math.floor(lastTwo/4)}} + ${{lastTwo%4}}</div>
                <div style="font-size:10px; color:${{isDiv4 ? '#34d399' : '#fb7185'}}; font-weight:bold;">
                  ${{isDiv4 ? '✓ MULTIPLE OF 4' : '✗ NOT MULTIPLE OF 4'}}
                </div>
              </div>
            </div>

            <div style="background:rgba(99,102,241,0.15); border:1px solid #6366f1; border-radius:8px; padding:8px 12px; font-size:12.5px; color:#cbd5e1;">
              Conclusion: ${{num}} is <strong style="color:${{isDiv4 ? '#34d399' : '#fb7185'}};">${{isDiv4 ? 'DIVISIBLE BY 4' : 'NOT DIVISIBLE BY 4'}}</strong> because its last 2 digits (${{lastTwo}}) determine the remainder!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="b7428">7,428 (Ends in 28)</button>
        <button class="sim-btn" id="b9134">9,134 (Ends in 34)</button>
        <button class="sim-btn" id="b5072">5,072 (Ends in 72)</button>
      `;

      document.getElementById('b7428').onclick = () => {{ num = 7428; updateUI(); }};
      document.getElementById('b9134').onclick = () => {{ num = 9134; updateUI(); }};
      document.getElementById('b5072').onclick = () => {{ num = 5072; updateUI(); }};

      updateUI();
    }}

    // Sim 6: Always, Sometimes, Never Conjecture Engine
    function renderSim6(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚖️</span> Always, Sometimes, Never Conjecture Tester';
      badge.textContent = 'Universal Truth vs Counterexamples';

      let claimIdx = 0;

      const claims = [
        {{
          statement: "The sum of 3 consecutive integers is a multiple of 3.",
          verdict: "ALWAYS TRUE",
          color: "#10b981",
          proof: "(n - 1) + n + (n + 1) = 3n. Since n is an integer, 3n is universally a multiple of 3 for all integers."
        }},
        {{
          statement: "A multiple of 4 is a multiple of 8.",
          verdict: "SOMETIMES TRUE",
          color: "#f59e0b",
          proof: "True for 16, 24, 32... but FALSE for 12, 20, 28! Counterexample: 12 is 4 × 3, but not a multiple of 8."
        }},
        {{
          statement: "The sum of two odd numbers is odd.",
          verdict: "NEVER TRUE",
          color: "#f43f5e",
          proof: "(2a + 1) + (2b + 1) = 2(a + b + 1). The result is always divisible by 2 (even)."
        }},
        {{
          statement: "The square of an odd number leaves remainder 1 when divided by 8.",
          verdict: "ALWAYS TRUE",
          color: "#10b981",
          proof: "(2k + 1)² = 4k(k + 1) + 1. Since k(k+1) is a product of 2 consecutive integers, it is even (2m), giving 4(2m)+1 = 8m+1!"
        }}
      ];

      function updateUI() {{
        const c = claims[claimIdx];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="background:#0f172a; border:1px solid #475569; border-radius:10px; padding:16px 20px; margin-bottom:12px; text-align:left;">
              <div style="font-size:11px; color:#38bdf8; font-weight:bold; text-transform:uppercase;">Conjecture #${{claimIdx + 1}} of ${{claims.length}}</div>
              <div style="font-size:15px; color:#fff; font-weight:600; margin:6px 0;">"${{c.statement}}"</div>
            </div>

            <div style="background:rgba(30,41,59,0.8); border:2px solid ${{c.color}}; border-radius:10px; padding:12px; margin-bottom:10px;">
              <div style="font-size:18px; font-weight:800; color:${{c.color}};">${{c.verdict}}</div>
              <div style="font-size:12.5px; color:#cbd5e1; margin-top:6px; line-height:1.5;">${{c.proof}}</div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="cPrev">← Prev Conjecture</button>
        <button class="sim-btn" id="cNext">Next Conjecture →</button>
      `;

      document.getElementById('cPrev').onclick = () => {{
        if (claimIdx > 0) claimIdx--;
        updateUI();
      }};

      document.getElementById('cNext').onclick = () => {{
        if (claimIdx < claims.length - 1) claimIdx++;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 7: What Remains? Circular Clock Modular Lab
    function renderSim7(vp, controls, title, badge) {{
      title.innerHTML = '<span>⏰</span> What Remains? Circular Modulo Clock';
      badge.textContent = "Euclid's Division Lemma & Periodic Remainders";

      let mod = 7;
      let val = 23;

      function updateUI() {{
        const rem = val % mod;
        const q = Math.floor(val / mod);

        const svgW = 480;
        const svgH = 220;
        const cx = 150;
        const cy = 110;
        const r = 70;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 ${{svgW}} ${{svgH}}" style="width:100%; height:190px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              <!-- Circular Dial -->
              <circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="none" stroke="#334155" stroke-width="3"/>

              <!-- Modulo Ticks around dial -->
              ${{Array.from({{length: mod}}).map((_, i) => {{
                const ang = (i / mod) * 2 * Math.PI - Math.PI / 2;
                const tx = cx + (r - 14) * Math.cos(ang);
                const ty = cy + (r - 14) * Math.sin(ang);
                const dotX = cx + r * Math.cos(ang);
                const dotY = cy + r * Math.sin(ang);
                const isCurrent = (i === rem);
                return `
                  <circle cx="${{dotX}}" cy="${{dotY}}" r="${{isCurrent ? 6 : 3}}" fill="${{isCurrent ? '#f59e0b' : '#64748b'}}"/>
                  <text x="${{tx}}" y="${{ty + 4}}" fill="${{isCurrent ? '#fcd34d' : '#94a3b8'}}" font-size="${{isCurrent ? '13' : '11'}}" font-weight="${{isCurrent ? 'bold' : 'normal'}}" text-anchor="middle">
                    ${{i}}
                  </text>
                `;
              }}).join('')}}

              <!-- Clock Hand pointing to Remainder -->
              ${{(() => {{
                const ang = (rem / mod) * 2 * Math.PI - Math.PI / 2;
                const hx = cx + (r - 28) * Math.cos(ang);
                const hy = cy + (r - 28) * Math.sin(ang);
                return `
                  <line x1="${{cx}}" y1="${{cy}}" x2="${{hx}}" y2="${{hy}}" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                  <circle cx="${{cx}}" cy="${{cy}}" r="4" fill="#fff"/>
                `;
              }})()}}

              <!-- Right Equation Box -->
              <g transform="translate(260, 40)">
                <rect x="0" y="0" width="200" height="130" rx="8" fill="#0f172a" stroke="#334155"/>
                <text x="100" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Division Theorem</text>
                <text x="100" y="55" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">
                  ${{val}} = ${{mod}} × ${{q}} + <tspan fill="#f59e0b">${{rem}}</tspan>
                </text>
                <text x="100" y="82" fill="#94a3b8" font-size="11" text-anchor="middle">Quotient q = ${{q}} full loops</text>
                <text x="100" y="104" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Remainder r = ${{rem}}</text>
              </g>
            </svg>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Modulus (d):</span>
          <input type="range" id="modSlider" min="3" max="12" value="${{mod}}">
          <span id="modVal">${{mod}}</span>
        </div>
        <div class="sim-slider-group">
          <span>Input (N):</span>
          <input type="range" id="valSlider" min="0" max="60" value="${{val}}">
          <span id="valVal">${{val}}</span>
        </div>
      `;

      document.getElementById('modSlider').oninput = (e) => {{
        mod = parseInt(e.target.value);
        document.getElementById('modVal').textContent = mod;
        updateUI();
      }};

      document.getElementById('valSlider').oninput = (e) => {{
        val = parseInt(e.target.value);
        document.getElementById('valVal').textContent = val;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 8: Figurate Numbers & Dot Arrays
    function renderSim8(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔘</span> Figurate Dot Arrays: Tₙ₋₁ + Tₙ = n²';
      badge.textContent = 'Geometric Number Theory Proof';

      let n = 4;
      let fused = false;

      function updateUI() {{
        const Tn = (n * (n + 1)) / 2;
        const Tprev = ((n - 1) * n) / 2;
        const square = n * n;

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <svg viewBox="0 0 480 200" style="width:100%; height:180px; background:#090d16; border-radius:10px; border:1px solid #1e293b;">
              ${{!fused ? `
                <!-- Left: T_n-1 (Cyan) -->
                <g transform="translate(60, 40)">
                  <text x="50" y="0" fill="#06b6d4" font-size="12" font-weight="bold" text-anchor="middle">T_${{n-1}} = ${{Tprev}}</text>
                  ${{Array.from({{length: n - 1}}).map((_, r) =>
                    Array.from({{length: r + 1}}).map((_, c) => `
                      <circle cx="${{30 + c*20}}" cy="${{25 + r*20}}" r="6" fill="#06b6d4"/>
                    `).join('')
                  ).join('')}}
                </g>

                <text x="200" y="100" fill="#fff" font-size="22" font-weight="bold">+</text>

                <!-- Right: T_n (Amber) -->
                <g transform="translate(240, 40)">
                  <text x="60" y="0" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">T_${{n}} = ${{Tn}}</text>
                  ${{Array.from({{length: n}}).map((_, r) =>
                    Array.from({{length: r + 1}}).map((_, c) => `
                      <circle cx="${{30 + c*20}}" cy="${{25 + r*20}}" r="6" fill="#f59e0b"/>
                    `).join('')
                  ).join('')}}
                </g>
              ` : `
                <!-- Fused into an n x n Square Grid -->
                <g transform="translate(160, 30)">
                  <text x="${{n*11}}" y="0" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">
                    Fused Square Grid: ${{n}} × ${{n}} = ${{square}} dots
                  </text>
                  ${{Array.from({{length: n}}).map((_, r) =>
                    Array.from({{length: n}}).map((_, c) => `
                      <circle cx="${{20 + c*22}}" cy="${{25 + r*22}}" r="6.5"
                              fill="${{c <= r ? '#f59e0b' : '#06b6d4'}}"/>
                    `).join('')
                  ).join('')}}
                </g>
              `}}
            </svg>

            <div style="margin-top:6px; background:#0f172a; padding:8px 12px; border-radius:8px; font-size:12.5px; color:#cbd5e1;">
              <strong>Theorem:</strong> T_${{n-1}} (${{Tprev}}) + T_${{n}} (${{Tn}}) = <strong>${{square}} = ${{n}}²</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <div class="sim-slider-group">
          <span>Level n:</span>
          <input type="range" id="nFigSlider" min="2" max="6" value="${{n}}">
          <span id="nFigVal">${{n}}</span>
        </div>
        <button class="sim-btn" id="fuseBtn">${{fused ? 'Separate into Triangles' : 'Fuse into Square (n²)'}}</button>
      `;

      document.getElementById('nFigSlider').oninput = (e) => {{
        n = parseInt(e.target.value);
        document.getElementById('nFigVal').textContent = n;
        updateUI();
      }};

      document.getElementById('fuseBtn').onclick = () => {{
        fused = !fused;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 9: Divisibility by 9 Decomposer
    function renderSim9(vp, controls, title, badge) {{
      title.innerHTML = '<span>9️⃣</span> Divisibility by 9 Place-Value Unwrapper';
      badge.textContent = '10^k = 99...9 + 1 Proof';

      let num = 4374;

      function updateUI() {{
        const digits = num.toString().split('').map(Number);
        const sumDigits = digits.reduce((a, b) => a + b, 0);
        const isDiv9 = (sumDigits % 9 === 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; font-size:12.5px; text-align:left;">
            <div style="text-align:center; font-size:14px; color:#94a3b8; margin-bottom:8px;">
              Target Number: <span style="font-size:22px; color:#38bdf8; font-weight:bold;">${{num}}</span>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px 14px; margin-bottom:8px; line-height:1.6;">
              <strong>Place-Value Expansion:</strong>
              <br>${{digits.map((d, i) => {{
                const p = Math.pow(10, digits.length - 1 - i);
                const nines = p - 1;
                return nines > 0 ?
                  `<span style="color:#a5b4fc;">${{d}} × (${{nines}} + 1)</span>` :
                  `<span style="color:#fcd34d;">${{d}}</span>`;
              }}).join(' + ')}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px 14px; margin-bottom:8px; line-height:1.6;">
              <strong>Grouping Multiples of 9:</strong>
              <br><span style="color:#10b981;">[Grouped Nines Multiple: 9 × K]</span> + <span style="color:#f59e0b; font-weight:bold;">[Digit Sum: ${{digits.join(' + ')}} = ${{sumDigits}}]</span>
            </div>

            <div style="background:${{isDiv9 ? 'rgba(16,185,129,0.15)' : 'rgba(244,63,94,0.15)'}}; border:1px solid ${{isDiv9 ? '#10b981' : '#f43f5e'}}; border-radius:8px; padding:8px 12px; text-align:center; color:${{isDiv9 ? '#34d399' : '#fb7185'}}; font-weight:bold;">
              ${{isDiv9 ? `✓ Digit sum ${{sumDigits}} is divisible by 9 (9 × ${{sumDigits/9}}). Thus, ${{num}} is DIVISIBLE by 9!` : `✗ Digit sum ${{sumDigits}} is not divisible by 9. Remainder = ${{sumDigits%9}}.`}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="b4374">4,374 (Sum = 18)</button>
        <button class="sim-btn" id="b7829">7,829 (Sum = 26)</button>
        <button class="sim-btn" id="b9990">9,990 (Sum = 27)</button>
      `;

      document.getElementById('b4374').onclick = () => {{ num = 4374; updateUI(); }};
      document.getElementById('b7829').onclick = () => {{ num = 7829; updateUI(); }};
      document.getElementById('b9990').onclick = () => {{ num = 9990; updateUI(); }};

      updateUI();
    }}

    // Sim 10: Divisibility by 3 Scanner
    function renderSim10(vp, controls, title, badge) {{
      title.innerHTML = '<span>3️⃣</span> Divisibility by 3 Digit-Sum Scanner';
      badge.textContent = 'Inherited Factor of 9';

      let num = 5823;

      function updateUI() {{
        const digits = num.toString().split('').map(Number);
        const sum = digits.reduce((a, b) => a + b, 0);
        const isDiv3 = (sum % 3 === 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:14px; color:#94a3b8; margin-bottom:10px;">
              Scanning Digits of: <span style="font-size:24px; color:#38bdf8; font-weight:bold;">${{num}}</span>
            </div>

            <!-- Digit Cards -->
            <div style="display:flex; justify-content:center; gap:8px; margin-bottom:12px;">
              ${{digits.map((d, i) => `
                <div style="background:#1e293b; border:1px solid #6366f1; border-radius:8px; padding:10px 14px; min-width:48px;">
                  <div style="font-size:10px; color:#94a3b8;">D${{i+1}}</div>
                  <div style="font-size:22px; font-weight:bold; color:#fcd34d;">${{d}}</div>
                </div>
              `).join('')}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; font-size:13px; color:#cbd5e1; margin-bottom:10px;">
              Accumulated Digit Sum: ${{digits.join(' + ')}} = <strong style="color:#fcd34d; font-size:16px;">${{sum}}</strong>
              <br>${{sum}} = 3 × ${{Math.floor(sum/3)}} + <span style="color:${{isDiv3 ? '#34d399' : '#fb7185'}}; font-weight:bold;">${{sum%3}} (Remainder)</span>
            </div>

            <div style="background:${{isDiv3 ? 'rgba(16,185,129,0.15)' : 'rgba(244,63,94,0.15)'}}; border:1px solid ${{isDiv3 ? '#10b981' : '#f43f5e'}}; border-radius:8px; padding:8px; color:${{isDiv3 ? '#34d399' : '#fb7185'}}; font-weight:bold; font-size:13px;">
              ${{isDiv3 ? `✓ ${{num}} is DIVISIBLE by 3!` : `✗ ${{num}} is NOT divisible by 3.`}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="b5823">5,823 (Sum = 18)</button>
        <button class="sim-btn" id="b6142">6,142 (Sum = 13)</button>
        <button class="sim-btn" id="b9015">9,015 (Sum = 15)</button>
      `;

      document.getElementById('b5823').onclick = () => {{ num = 5823; updateUI(); }};
      document.getElementById('b6142').onclick = () => {{ num = 6142; updateUI(); }};
      document.getElementById('b9015').onclick = () => {{ num = 9015; updateUI(); }};

      updateUI();
    }}

    // Sim 11: Divisibility by 11 Balance Scale
    function renderSim11(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚖️</span> Divisibility by 11 Alternating Balance Scale';
      badge.textContent = 'Odd vs Even Position Difference';

      let num = 85976;

      function updateUI() {{
        const digits = num.toString().split('').map(Number).reverse(); // from right: 0 is 1st, 1 is 2nd...
        let oddSum = 0;
        let evenSum = 0;
        const oddDigits = [];
        const evenDigits = [];

        digits.forEach((d, idx) => {{
          if (idx % 2 === 0) {{
            oddSum += d;
            oddDigits.push(d);
          }} else {{
            evenSum += d;
            evenDigits.push(d);
          }}
        }});

        const diff = Math.abs(oddSum - evenSum);
        const isDiv11 = (diff % 11 === 0);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:14px; color:#94a3b8; margin-bottom:8px;">
              Testing: <span style="font-size:24px; color:#38bdf8; font-weight:bold;">${{num}}</span>
            </div>

            <!-- Two Balance Pans -->
            <div style="display:flex; justify-content:space-around; align-items:center; margin-bottom:12px;">
              <!-- Left Pan: Odd Positions -->
              <div style="background:#0f172a; border:2px solid #06b6d4; border-radius:10px; padding:10px 14px; width:45%;">
                <div style="font-size:11px; color:#06b6d4; font-weight:bold;">Odd Places (from right: 1st, 3rd...)</div>
                <div style="font-size:13px; color:#e2e8f0; margin:4px 0;">${{oddDigits.join(' + ')}}</div>
                <div style="font-size:22px; font-weight:bold; color:#38bdf8;">${{oddSum}}</div>
              </div>

              <div style="font-size:20px; font-weight:bold; color:#64748b;">VS</div>

              <!-- Right Pan: Even Positions -->
              <div style="background:#0f172a; border:2px solid #ec4899; border-radius:10px; padding:10px 14px; width:45%;">
                <div style="font-size:11px; color:#ec4899; font-weight:bold;">Even Places (2nd, 4th...)</div>
                <div style="font-size:13px; color:#e2e8f0; margin:4px 0;">${{evenDigits.join(' + ')}}</div>
                <div style="font-size:22px; font-weight:bold; color:#f472b6;">${{evenSum}}</div>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:8px 12px; font-size:12.5px; color:#cbd5e1; margin-bottom:8px;">
              Difference: |${{oddSum}} - ${{evenSum}}| = <strong style="color:#fcd34d; font-size:16px;">${{diff}}</strong>
            </div>

            <div style="background:${{isDiv11 ? 'rgba(16,185,129,0.15)' : 'rgba(244,63,94,0.15)'}}; border:1px solid ${{isDiv11 ? '#10b981' : '#f43f5e'}}; border-radius:8px; padding:8px; color:${{isDiv11 ? '#34d399' : '#fb7185'}}; font-weight:bold; font-size:13px;">
              ${{isDiv11 ? `✓ Difference ${{diff}} is a multiple of 11! ${{num}} is DIVISIBLE by 11.` : `✗ Difference ${{diff}} is not a multiple of 11. Not divisible.`}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="b85976">85,976 (Diff = 11)</button>
        <button class="sim-btn" id="b91839">91,839 (Diff = 22)</button>
        <button class="sim-btn" id="b1331">1,331 (Diff = 0)</button>
        <button class="sim-btn" id="b74251">74,251 (Diff = 1)</button>
      `;

      document.getElementById('b85976').onclick = () => {{ num = 85976; updateUI(); }};
      document.getElementById('b91839').onclick = () => {{ num = 91839; updateUI(); }};
      document.getElementById('b1331').onclick = () => {{ num = 1331; updateUI(); }};
      document.getElementById('b74251').onclick = () => {{ num = 74251; updateUI(); }};

      updateUI();
    }}

    // Sim 12: Powers of 2 and 5 Explorer
    function renderSim12(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚡</span> Powers of 2 & 5 Terminal Digits Architecture';
      badge.textContent = '10 = 2 × 5 Geometric Hierarchy';

      let testPower = '8'; // '2', '4', '8', '5', '25'
      const sampleNum = "58,924,168";

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:520px; font-size:12.5px; text-align:left;">
            <div style="text-align:center; font-size:14px; color:#94a3b8; margin-bottom:8px;">
              Test Number: <span style="font-size:22px; color:#38bdf8; font-weight:bold;">${{sampleNum}}</span>
            </div>

            <table style="width:100%; border-collapse:collapse; background:#0f172a; border:1px solid #334155; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; border-bottom:1px solid #334155;">
                  <th style="padding:6px;">Divisor</th>
                  <th style="padding:6px;">Place Absorbed</th>
                  <th style="padding:6px;">Digits Examined</th>
                  <th style="padding:6px;">Sample Evaluation</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1;">
                <tr style="border-bottom:1px solid #1e293b; background:${{testPower === '2' ? 'rgba(99,102,241,0.2)' : 'transparent'}};">
                  <td style="padding:6px; font-weight:bold;">2 (2¹)</td><td>10¹ = 10</td><td>Last 1 digit</td>
                  <td>Ends in <strong>8</strong> (Even: ✓ Divisible)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:${{testPower === '4' ? 'rgba(99,102,241,0.2)' : 'transparent'}};">
                  <td style="padding:6px; font-weight:bold;">4 (2²)</td><td>10² = 100</td><td>Last 2 digits</td>
                  <td>Last two = <strong>68</strong> (4 × 17: ✓ Divisible)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:${{testPower === '8' ? 'rgba(99,102,241,0.2)' : 'transparent'}};">
                  <td style="padding:6px; font-weight:bold;">8 (2³)</td><td>10³ = 1000</td><td>Last 3 digits</td>
                  <td>Last three = <strong>168</strong> (8 × 21: ✓ Divisible)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:${{testPower === '5' ? 'rgba(99,102,241,0.2)' : 'transparent'}};">
                  <td style="padding:6px; font-weight:bold;">5 (5¹)</td><td>10¹ = 10</td><td>Last 1 digit</td>
                  <td>Ends in 8 (Not 0 or 5: ✗ Not Divisible)</td>
                </tr>
                <tr style="background:${{testPower === '25' ? 'rgba(99,102,241,0.2)' : 'transparent'}};">
                  <td style="padding:6px; font-weight:bold;">25 (5²)</td><td>10² = 100</td><td>Last 2 digits</td>
                  <td>Ends in 68 (Not 00,25,50,75: ✗ Not Divisible)</td>
                </tr>
              </tbody>
            </table>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="p2">Div by 2 (1 digit)</button>
        <button class="sim-btn" id="p4">Div by 4 (2 digits)</button>
        <button class="sim-btn" id="p8">Div by 8 (3 digits)</button>
        <button class="sim-btn" id="p5">Div by 5 (1 digit)</button>
        <button class="sim-btn" id="p25">Div by 25 (2 digits)</button>
      `;

      document.getElementById('p2').onclick = () => {{ testPower = '2'; updateUI(); }};
      document.getElementById('p4').onclick = () => {{ testPower = '4'; updateUI(); }};
      document.getElementById('p8').onclick = () => {{ testPower = '8'; updateUI(); }};
      document.getElementById('p5').onclick = () => {{ testPower = '5'; updateUI(); }};
      document.getElementById('p25').onclick = () => {{ testPower = '25'; updateUI(); }};

      updateUI();
    }}

    // Sim 13: Composite Coprime Rule Matrix
    function renderSim13(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔗</span> Composite Divisibility & Coprime Splitter';
      badge.textContent = 'gcd(a, b) = 1 Factorization Rule';

      let selected = '12';

      const data = {{
        '6': {{ factors: '2 and 3', gcd: 1, valid: true, rule: 'Must be EVEN (div by 2) AND sum of digits div by 3.' }},
        '12': {{ factors: '3 and 4', gcd: 1, valid: true, rule: 'Sum of digits div by 3 AND last two digits div by 4.' }},
        '15': {{ factors: '3 and 5', gcd: 1, valid: true, rule: 'Ends in 0 or 5 AND sum of digits div by 3.' }},
        '18': {{ factors: '2 and 9', gcd: 1, valid: true, rule: 'Must be EVEN AND sum of digits div by 9.' }},
        'trap12': {{ factors: '2 and 6', gcd: 2, valid: false, rule: 'TRAP! gcd(2, 6) = 2 ≠ 1. Counterexample: 18 is div by 2 and 6, but NOT by 12!' }},
        'trap24': {{ factors: '4 and 6', gcd: 2, valid: false, rule: 'TRAP! gcd(4, 6) = 2 ≠ 1. Counterexample: 12 is div by 4 and 6, but NOT by 24! (Must use 3 and 8).' }}
      }};

      function updateUI() {{
        const item = data[selected];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:center;">
            <div style="font-size:16px; font-weight:bold; color:#38bdf8; margin-bottom:8px;">
              Testing Rule for Composite: <span style="font-size:24px; color:#fcd34d;">${{selected.replace('trap', '')}}</span>
            </div>

            <div style="background:#0f172a; border:1px solid ${{item.valid ? '#10b981' : '#f43f5e'}}; border-radius:10px; padding:14px; text-align:left;">
              <div style="font-size:13px; color:#94a3b8;">Chosen Factors: <strong style="color:#fff;">${{item.factors}}</strong></div>
              <div style="font-size:13px; color:#94a3b8; margin:4px 0;">Greatest Common Divisor: <strong style="color:${{item.valid ? '#34d399' : '#fb7185'}};">gcd = ${{item.gcd}}</strong></div>
              <div style="margin-top:8px; font-size:13px; color:${{item.valid ? '#a7f3d0' : '#fecdd3'}}; line-height:1.5;">
                ${{item.rule}}
              </div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bC6">6 (2 × 3)</button>
        <button class="sim-btn active" id="bC12">12 (3 × 4)</button>
        <button class="sim-btn" id="bC15">15 (3 × 5)</button>
        <button class="sim-btn" id="bC18">18 (2 × 9)</button>
        <button class="sim-btn" style="border-color:#f43f5e;" id="bTrap12">Trap: 12 as 2 × 6</button>
        <button class="sim-btn" style="border-color:#f43f5e;" id="bTrap24">Trap: 24 as 4 × 6</button>
      `;

      document.getElementById('bC6').onclick = () => {{ selected = '6'; updateUI(); }};
      document.getElementById('bC12').onclick = () => {{ selected = '12'; updateUI(); }};
      document.getElementById('bC15').onclick = () => {{ selected = '15'; updateUI(); }};
      document.getElementById('bC18').onclick = () => {{ selected = '18'; updateUI(); }};
      document.getElementById('bTrap12').onclick = () => {{ selected = 'trap12'; updateUI(); }};
      document.getElementById('bTrap24').onclick = () => {{ selected = 'trap24'; updateUI(); }};

      updateUI();
    }}

    // Sim 14: Digital Root & Casting Out Nines
    function renderSim14(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔮</span> Digital Roots & Casting Out Nines';
      badge.textContent = 'Arithmetic Verification Hash';

      let A = 437;
      let B = 28;

      function calcDR(num) {{
        let s = num;
        while (s >= 10) {{
          s = s.toString().split('').reduce((acc, d) => acc + parseInt(d), 0);
        }}
        return s;
      }}

      function updateUI() {{
        const prod = A * B;
        const drA = calcDR(A);
        const drB = calcDR(B);
        const expectedDR = calcDR(drA * drB);
        const actualDR = calcDR(prod);
        const isMatch = (expectedDR === actualDR);

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; font-size:12.5px; text-align:left;">
            <div style="text-align:center; font-size:15px; color:#fff; font-weight:bold; margin-bottom:8px;">
              Equation: ${{A}} × ${{B}} = ${{prod}}
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
              <div style="background:#0f172a; padding:8px 12px; border-radius:8px; border:1px solid #334155;">
                <span style="color:#94a3b8;">dr(${{A}}):</span> <strong style="color:#38bdf8;">${{drA}}</strong>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:8px; border:1px solid #334155;">
                <span style="color:#94a3b8;">dr(${{B}}):</span> <strong style="color:#38bdf8;">${{drB}}</strong>
              </div>
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:10px; margin-bottom:8px; text-align:center;">
              Expected Product Digital Root: dr(${{drA}} × ${{drB}}) = <strong style="color:#fcd34d;">${{expectedDR}}</strong>
              <br>Actual Result Digital Root: dr(${{prod}}) = <strong style="color:#fcd34d;">${{actualDR}}</strong>
            </div>

            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:8px; text-align:center; color:#34d399; font-weight:bold;">
              ✓ Digital roots match (${{expectedDR}} = ${{actualDR}})! The multiplication passes the casting out nines verification!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bPair1">437 × 28</button>
        <button class="sim-btn" id="bPair2">347 × 45</button>
        <button class="sim-btn" id="bPair3">892 × 15</button>
      `;

      document.getElementById('bPair1').onclick = () => {{ A = 437; B = 28; updateUI(); }};
      document.getElementById('bPair2').onclick = () => {{ A = 347; B = 45; updateUI(); }};
      document.getElementById('bPair3').onclick = () => {{ A = 892; B = 15; updateUI(); }};

      updateUI();
    }}

    // Sim 15: Cryptarithm Solver Workbench
    function renderSim15(vp, controls, title, badge) {{
      title.innerHTML = '<span>🕵️</span> Cryptarithm Solver Workbench';
      badge.textContent = 'Alphametics & Column Constraints';

      let puzzle = 'p1';

      const puzzles = {{
        p1: {{
          title: 'A + A + A = BA',
          steps: [
            '1. Equation: 3 × A = 10B + A',
            '2. Subtract A from both sides: 2A = 10B ➔ A = 5B',
            '3. B is the leading digit of BA, so B ≥ 1. If B = 1, A = 5. (If B ≥ 2, A ≥ 10, impossible).',
            '4. Solution: A = 5, B = 1 (5 + 5 + 5 = 15)'
          ]
        }},
        p2: {{
          title: '3A + 25 = B2',
          steps: [
            '1. Units column: A + 5 must end in 2.',
            '2. A + 5 = 12 ➔ A = 7 (produces a carry of 1 to tens).',
            '3. Tens column: 1 (carry) + 3 + 2 = B ➔ B = 6.',
            '4. Solution: A = 7, B = 6 (37 + 25 = 62)'
          ]
        }},
        p3: {{
          title: '1A × A = 9A',
          steps: [
            '1. Equation: (10 + A) × A = 90 + A',
            '2. Expand: 10A + A² = 90 + A ➔ A² + 9A - 90 = 0',
            '3. Factor quadratic: (A + 15)(A - 6) = 0',
            '4. Since A is a positive digit: A = 6 (16 × 6 = 96)'
          ]
        }}
      }};

      function updateUI() {{
        const p = puzzles[puzzle];

        vp.innerHTML = `
          <div style="width:100%; max-width:520px; text-align:left;">
            <div style="text-align:center; font-size:18px; color:#fcd34d; font-weight:bold; margin-bottom:10px;">
              ${{p.title}}
            </div>

            <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; display:flex; flex-direction:column; gap:8px;">
              ${{p.steps.map(s => `
                <div style="font-size:12.5px; color:#cbd5e1; line-height:1.5;">${{s}}</div>
              `).join('')}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bP1">A + A + A = BA</button>
        <button class="sim-btn" id="bP2">3A + 25 = B2</button>
        <button class="sim-btn" id="bP3">1A × A = 9A</button>
      `;

      document.getElementById('bP1').onclick = () => {{ puzzle = 'p1'; updateUI(); }};
      document.getElementById('bP2').onclick = () => {{ puzzle = 'p2'; updateUI(); }};
      document.getElementById('bP3').onclick = () => {{ puzzle = 'p3'; updateUI(); }};

      updateUI();
    }}

    // Sim 16: Number Detective Puzzle Room
    function renderSim16(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔍</span> Number Detective Puzzle Room';
      badge.textContent = 'Deductive Mystery Matrix';

      let caseNum = 0;
      let solved = false;

      const cases = [
        {{
          clue: "I am a 3-digit number. I am divisible by 5 and by 9. My hundreds digit is 4, and I am smaller than 480.",
          answer: "450",
          deduction: "Div by 5 ➔ ends in 0 or 5. Starts with 4. If 4X0, digit sum 4+X=9 ➔ X=5 (450). If 4X5, sum 9+X=18 ➔ X=9 (495). Since number < 480, answer is 450!"
        }},
        {{
          clue: "I am a 3-digit multiple of 6. My digits are 5, X, and 2 in order (5X2). What is my smallest value?",
          answer: "522",
          deduction: "Div by 6 requires Even (ends in 2: yes) and Sum divisible by 3. 5 + X + 2 = 7 + X. Smallest X makes 7 + X = 9 ➔ X = 2. Number is 522!"
        }},
        {{
          clue: "I am the smallest 4-digit number divisible by 2, 3, 4, 5, and 6.",
          answer: "1020",
          deduction: "LCM(2, 3, 4, 5, 6) = 60. Smallest 4-digit number is 1000. 1000 ÷ 60 = 16.66. Smallest integer multiple is 60 × 17 = 1020!"
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
                <strong>Mystery Solved: Number is ${{c.answer}}!</strong>
                <br><span style="color:#cbd5e1; font-size:12px;">${{c.deduction}}</span>
              </div>
            ` : `
              <div style="margin-top:14px; font-size:12.5px; color:#94a3b8;">
                Analyze the clues, then click "Solve Mystery" to verify your deduction!
              </div>
            `}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="casePrev">← Prev Case</button>
        <button class="sim-btn" id="caseSolve">Solve Mystery</button>
        <button class="sim-btn" id="caseNext">Next Case →</button>
      `;

      document.getElementById('casePrev').onclick = () => {{
        if (caseNum > 0) {{
          caseNum--;
          solved = false;
          updateUI();
        }}
      }};

      document.getElementById('caseNext').onclick = () => {{
        if (caseNum < cases.length - 1) {{
          caseNum++;
          solved = false;
          updateUI();
        }}
      }};

      document.getElementById('caseSolve').onclick = () => {{
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
    out_path = 'public/animations/class8-math-number-play.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {out_path} ({len(html)} bytes)")

