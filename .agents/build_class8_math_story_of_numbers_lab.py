import json
import sys
sys.path.append('.agents')
from class8_math_story_of_numbers_data import slides_data, quiz_questions

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Mathematics • Chapter 3: A Story of Numbers Master Lab</title>
  
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
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .nav-badge {{
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      padding: 4px 10px;
      border-radius: 9999px;
    }}

    .nav-title {{
      font-size: 16px;
      font-weight: 700;
      color: #f1f5f9;
    }}

    .nav-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .slide-indicator {{
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(148, 163, 184, 0.2);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      color: var(--accent-cyan);
    }}

    .speech-btn {{
      background: rgba(99, 102, 241, 0.2);
      border: 1px solid var(--accent-indigo);
      color: #c7d2fe;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
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

    .grid-2col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}
    @media (max-width: 640px) {{
      .grid-2col {{
        grid-template-columns: 1fr;
      }}
    }}

    .card-item {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(148, 163, 184, 0.15);
      border-radius: 12px;
      padding: 14px 16px;
    }}
    .card-item h4 {{
      font-size: 14px;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 8px;
    }}
    .card-item p, .card-item li {{
      font-size: 13px;
      line-height: 1.55;
      color: #94a3b8;
    }}
    .card-item ul {{
      margin-left: 18px;
      margin-top: 6px;
    }}

    .highlight-eq {{
      background: rgba(6, 182, 212, 0.1);
      border: 1px dashed rgba(6, 182, 212, 0.4);
      color: #67e8f9;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      padding: 8px 12px;
      border-radius: 8px;
      margin: 10px 0;
      font-size: 13px;
      text-align: center;
    }}

    /* Teacher Persona Banner */
    .teacher-card {{
      background: linear-gradient(135deg, rgba(30, 27, 75, 0.8), rgba(15, 23, 42, 0.9));
      border: 1px solid rgba(99, 102, 241, 0.3);
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
      font-weight: 700;
      color: var(--accent-amber);
      text-transform: uppercase;
      margin-bottom: 2px;
    }}

    /* Interactive Simulator Panel */
    .sim-panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }}

    .sim-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(148, 163, 184, 0.15);
      padding-bottom: 10px;
    }}
    .sim-head h3 {{
      font-size: 16px;
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .sim-badge {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}

    .sim-viewport {{
      background: #020617;
      border: 1px solid rgba(148, 163, 184, 0.15);
      border-radius: 12px;
      min-height: 280px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
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
      background: #1e293b;
      border: 1px solid #475569;
      color: #e2e8f0;
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .sim-btn:hover {{
      background: #334155;
      color: #fff;
      border-color: var(--accent-cyan);
    }}
    .sim-btn.active {{
      background: var(--accent-indigo);
      border-color: #818cf8;
      color: #fff;
    }}

    .sim-slider-label {{
      font-size: 12px;
      font-weight: 600;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .sim-slider {{
      accent-color: var(--accent-cyan);
      cursor: pointer;
    }}

    /* Checkpoint Section */
    .checkpoint-section {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .checkpoint-head {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-amber);
    }}

    .checkpoint-card {{
      background: #090e1a;
      border: 1px solid rgba(148, 163, 184, 0.12);
      border-radius: 12px;
      padding: 16px;
    }}

    .checkpoint-q {{
      font-size: 13.5px;
      font-weight: 600;
      color: #f1f5f9;
      margin-bottom: 12px;
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}
    @media (max-width: 640px) {{
      .options-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .opt-btn {{
      background: #1e293b;
      border: 1px solid rgba(148, 163, 184, 0.2);
      border-radius: 8px;
      padding: 9px 12px;
      font-size: 12.5px;
      color: #cbd5e1;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .opt-btn:hover:not(:disabled) {{
      background: #334155;
      border-color: var(--accent-cyan);
      color: #fff;
    }}
    .opt-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: var(--accent-emerald) !important;
      color: #34d399 !important;
      font-weight: 700;
    }}
    .opt-btn.wrong {{
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: var(--accent-rose) !important;
      color: #fb7185 !important;
    }}

    .feedback-box {{
      margin-top: 10px;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      line-height: 1.5;
      display: none;
    }}
    .feedback-box.show {{
      display: block;
    }}

    /* Quiz Slides (Slides 17 to 20) */
    .quiz-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-top: 16px;
    }}
    @media (max-width: 900px) {{
      .quiz-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .quiz-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 18px;
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
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}

    .sol-btn {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s ease;
    }}
    .sol-btn:hover {{
      background: rgba(245, 158, 11, 0.3);
      color: #fff;
    }}

    /* Footer Navigation */
    footer {{
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--card-border);
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      bottom: 0;
      z-index: 90;
    }}

    .nav-btn {{
      background: var(--accent-indigo);
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .nav-btn:hover:not(:disabled) {{
      background: #4f46e5;
      transform: translateY(-1px);
    }}
    .nav-btn:disabled {{
      background: #334155;
      color: #64748b;
      cursor: not-allowed;
      transform: none;
    }}

    .last-slide-notice {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
      font-size: 13px;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: 8px;
      display: none;
    }}

    /* Modal Styling */
    .modal-backdrop {{
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(6px);
    }}
    .hidden {{
      display: none !important;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header>
    <div class="nav-brand">
      <span class="nav-badge">Class 8 • NCERT</span>
      <span class="nav-title">A Story of Numbers • Mathematics Chapter 3</span>
    </div>
    <div class="nav-controls">
      <span class="slide-indicator" id="slideProgressIndicator">Slide 1 of 20</span>
      <button class="speech-btn" id="voiceToggleBtn" onclick="toggleSpeech()">
        <span id="speechIcon">🔊</span>
        <span id="speechBtnText">Play Narration</span>
      </button>
    </div>
  </header>

  <!-- Main Content Container -->
  <main>
    <!-- Slide Header -->
    <section class="slide-header">
      <div class="slide-tag" id="slideTag">Lesson 1 of 16</div>
      <h1 class="slide-title" id="slideTitle">3.1 The Genesis of Counting & One-to-One Correspondence</h1>
      <p class="slide-subtitle" id="slideSubtitle">How Early Humans Discovered Numerical Quantity & One-to-One Correspondence (NCERT Section 3.1)</p>
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
          <!-- Hair & Turban -->
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
        <div class="teacher-role">Senior Mathematics Mentor</div>
        <div class="teacher-speech" id="teacherSpeech">
          "Welcome to Chapter 3 of Class 8 Mathematics: A Story of Numbers! Long before number symbols were invented, humans solved real-world problems using one-to-one correspondence. Look at our shepherd simulator: click to release sheep and watch pebbles drop into the pouch. In the evening, match them back! Try it yourself."
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

        <!-- In-Slide Checkpoints (2 Inquiries per Lesson Slide) -->
        <section class="checkpoint-section" id="checkpointContainer">
          <div class="checkpoint-head">
            <span>🎯</span> In-Slide Conceptual Checkpoints
          </div>
          <div id="checkpointsList" style="display:flex; flex-direction:column; gap:12px;">
            <!-- Injected dynamically -->
          </div>
        </section>
      </div>
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
          Close Solution
        </button>
      </div>
    </div>
  </div>

  <!-- Client-side Logic -->
  <script>
    // Data Ingestion
    const slides = {slides_json};
    const quizData = {quiz_json};

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let currentUtterance = null;
    let mouthInterval = null;

    // KaTeX Math Rendering Engine
    function triggerMathRender(target) {{
      const el = target || document.body;
      if (window.renderMathInElement) {{
        try {{
          renderMathInElement(el, {{
            delimiters: [
              {{ left: '$$', right: '$$', display: true }},
              {{ left: '$', right: '$', display: false }},
              {{ left: '\\(', right: '\\)', display: false }},
              {{ left: '\\[', right: '\\]', display: true }}
            ],
            throwOnError: false
          }});
        }} catch (err) {{
          console.warn('KaTeX render warning:', err);
        }}
      }}
    }}

    // Initialize
    window.addEventListener('DOMContentLoaded', () => {{
      renderSlide(0);
      triggerMathRender(document.body);
    }});
    window.addEventListener('load', () => {{
      triggerMathRender(document.body);
    }});

    function renderSlide(index) {{
      if (index < 0 || index >= slides.length) return;
      currentSlideIndex = index;
      stopSpeech();

      const slide = slides[index];

      // Update Nav Indicators
      document.getElementById('slideProgressIndicator').textContent = `Slide ${{index + 1}} of ${{slides.length}}`;
      document.getElementById('slideTag').textContent = index >= 16 ? `Mastery Quiz Challenge ${{index - 15}} of 4` : `Lesson ${{index + 1}} of 16`;
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

      if (index < 16) {{
        checkpointContainer.style.display = 'block';
        simPanel.style.display = 'flex';
        renderCheckpoints(slide.checkpoints);
        renderSimulator(slide.sim_type);
      }} else {{
        checkpointContainer.style.display = 'none';
        simPanel.style.display = 'none';
        const qRange = slide.quiz_range;
        renderQuizQuestions(index, qRange[0], qRange[1]);
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
        document.getElementById('voiceToggleBtn').classList.add('speaking');
        document.getElementById('speechBtnText').textContent = 'Stop Narration';
        document.getElementById('speechIcon').textContent = '⏹️';
        document.getElementById('teacherCard').classList.add('speaking');
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
      const btn = document.getElementById('voiceToggleBtn');
      if (btn) btn.classList.remove('speaking');
      const txt = document.getElementById('speechBtnText');
      if (txt) txt.textContent = 'Play Narration';
      const icon = document.getElementById('speechIcon');
      if (icon) icon.textContent = '🔊';
      const teacher = document.getElementById('teacherCard');
      if (teacher) teacher.classList.remove('speaking');
    }}

    // ==========================================
    // 16 BESPOKE INTERACTIVE SIMULATORS (Slides 1-16)
    // ==========================================
    function renderSimulator(type) {{
      const vp = document.getElementById('simViewport');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const badge = document.getElementById('simBadge');

      vp.innerHTML = '';
      controls.innerHTML = '';

      switch (type) {{
        case 'shepherd_pebble_pouch':
          renderSim1(vp, controls, title, badge);
          break;
        case 'cardinality_invariance_lab':
          renderSim2(vp, controls, title, badge);
          break;
        case 'phalanx_twelve_counter':
          renderSim3(vp, controls, title, badge);
          break;
        case 'ishango_tally_bone_explorer':
          renderSim4(vp, controls, title, badge);
          break;
        case 'gumulgal_binary_word_generator':
          renderSim5(vp, controls, title, badge);
          break;
        case 'roman_numeral_interactive_converter':
          renderSim6(vp, controls, title, badge);
          break;
        case 'multi_base_bundling_lab':
          renderSim7(vp, controls, title, badge);
          break;
        case 'egyptian_hieroglyph_scribe_slate':
          renderSim8(vp, controls, title, badge);
          break;
        case 'greek_attic_vs_egyptian_comparator':
          renderSim9(vp, controls, title, badge);
          break;
        case 'egyptian_doubling_multiplication_lab':
          renderSim10(vp, controls, title, badge);
          break;
        case 'place_value_magnifier_abacus':
          renderSim11(vp, controls, title, badge);
          break;
        case 'babylonian_sexagesimal_builder':
          renderSim12(vp, controls, title, badge);
          break;
        case 'mayan_glyph_stacker_lab':
          renderSim13(vp, controls, title, badge);
          break;
        case 'chinese_rod_numeral_board':
          renderSim14(vp, controls, title, badge);
          break;
        case 'hindu_place_value_sunya_engine':
          renderSim15(vp, controls, title, badge);
          break;
        case 'global_numeral_rosetta_stone':
          renderSim16(vp, controls, title, badge);
          break;
        default:
          vp.innerHTML = '<div style="color:#64748b;">Simulator loading...</div>';
      }}
    }}

    // Sim 1: Shepherd's Pebble Pouch (1-to-1 Correspondence)
    function renderSim1(vp, controls, title, badge) {{
      title.innerHTML = '<span>🐑</span> Shepherd\\'s Pebble Pouch Simulator';
      badge.textContent = '1-to-1 Correspondence (Bijection)';

      let sheepTotal = 6;
      let releasedCount = 0;
      let returnedCount = 0;
      let pebblesInPouch = 0;

      function updateUI() {{
        vp.innerHTML = `
          <div style="display:flex; justify-content:space-around; align-items:center; width:100%; max-width:540px;">
            <!-- Pasture & Pen -->
            <div style="text-align:center;">
              <div style="font-size:12px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">Pasture (Sheep: ${{sheepTotal - releasedCount + returnedCount}} in pen)</div>
              <div style="display:flex; flex-wrap:wrap; gap:8px; max-width:180px; justify-content:center; min-height:80px; background:rgba(30,41,59,0.5); padding:10px; border-radius:10px; border:1px dashed #475569;">
                ${{Array(sheepTotal - releasedCount + returnedCount).fill(0).map(() => '<span style="font-size:24px;">🐑</span>').join('')}}
              </div>
            </div>

            <!-- Gate Arrow -->
            <div style="text-align:center; color:#f59e0b; font-size:20px;">
              ⇄
              <div style="font-size:11px; color:#94a3b8;">Pen Gate</div>
            </div>

            <!-- Leather Pebble Pouch -->
            <div style="text-align:center;">
              <div style="font-size:12px; color:#fbbf24; font-weight:bold; margin-bottom:6px;">Leather Pouch (${{pebblesInPouch}} pebbles)</div>
              <div style="display:flex; flex-wrap:wrap; gap:6px; max-width:180px; justify-content:center; min-height:80px; background:rgba(245,158,11,0.1); padding:10px; border-radius:10px; border:1px dashed #f59e0b;">
                ${{Array(pebblesInPouch).fill(0).map(() => '<span style="font-size:20px;">🪨</span>').join('')}}
                ${{pebblesInPouch === 0 ? '<span style="color:#64748b; font-size:12px; margin-top:25px;">Empty Pouch</span>' : ''}}
              </div>
            </div>
          </div>

          <div style="margin-top:16px; font-size:13px; font-weight:bold; color:${{pebblesInPouch === 0 && releasedCount === 0 ? '#94a3b8' : (pebblesInPouch === 0 && returnedCount === sheepTotal ? '#34d399' : '#38bdf8')}};">
            ${{releasedCount === 0 && returnedCount === 0 ? 'Dawn: All sheep are in the pen. Pouch is empty.' : (pebblesInPouch > 0 && returnedCount === 0 ? `Grazing: ${{releasedCount}} sheep out grazing. ${{pebblesInPouch}} pebbles in pouch.` : (returnedCount === sheepTotal ? '✓ Evening Verification: Pouch is completely empty! All sheep accounted for!' : `Evening: ${{returnedCount}} sheep returned. ${{pebblesInPouch}} pebbles still in pouch.`))}}
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="releaseBtn">Release Sheep (Morning +1)</button>
        <button class="sim-btn" id="returnBtn">Return Sheep (Evening -1)</button>
        <button class="sim-btn" id="resetPouchBtn">Reset Day</button>
      `;

      document.getElementById('releaseBtn').onclick = () => {{
        if (releasedCount < sheepTotal) {{
          releasedCount++;
          pebblesInPouch++;
          updateUI();
        }}
      }};

      document.getElementById('returnBtn').onclick = () => {{
        if (returnedCount < releasedCount && pebblesInPouch > 0) {{
          returnedCount++;
          pebblesInPouch--;
          updateUI();
        }}
      }};

      document.getElementById('resetPouchBtn').onclick = () => {{
        releasedCount = 0;
        returnedCount = 0;
        pebblesInPouch = 0;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 2: Cardinality vs Invariance Lab
    function renderSim2(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔢</span> Cardinality & Order-Irrelevance Tester';
      badge.textContent = 'Permutation Invariance';

      let tokens = ['⭐ Star', '💎 Gem', '🍎 Apple', '🌙 Moon', '⚡ Bolt'];
      let countOrder = [0, 1, 2, 3, 4];

      function updateUI() {{
        vp.innerHTML = `
          <div style="font-size:13px; color:#94a3b8; margin-bottom:12px;">Enumerating Set S with 5 distinct items:</div>
          <div style="display:flex; flex-wrap:wrap; gap:12px; justify-content:center; align-items:center;">
            ${{countOrder.map((idx, step) => `
              <div style="background:#1e293b; border:1px solid #38bdf8; border-radius:10px; padding:12px 16px; text-align:center; min-width:85px;">
                <div style="font-size:24px; margin-bottom:4px;">${{tokens[idx].split(' ')[0]}}</div>
                <div style="font-size:11px; color:#cbd5e1;">${{tokens[idx].split(' ')[1]}}</div>
                <div style="background:#0284c7; color:#fff; font-size:11px; font-weight:bold; border-radius:4px; padding:2px 6px; margin-top:6px;">Ordinal: #${{step + 1}}</div>
              </div>
            `).join('')}}
          </div>
          <div style="margin-top:20px; text-align:center; font-size:14px; color:#34d399; font-weight:bold;">
            Final Cardinality: |S| = 5 &emsp; (Invariant under all 5! = 120 possible counting orders)
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="shuffleBtn">Shuffle Order (Random Permutation)</button>
        <button class="sim-btn" id="reverseBtn">Reverse Counting Order</button>
      `;

      document.getElementById('shuffleBtn').onclick = () => {{
        countOrder = countOrder.sort(() => Math.random() - 0.5);
        updateUI();
      }};

      document.getElementById('reverseBtn').onclick = () => {{
        countOrder.reverse();
        updateUI();
      }};

      updateUI();
    }}

    // Sim 3: Anatomical Phalanx 12-Joint Counter
    function renderSim3(vp, controls, title, badge) {{
      title.innerHTML = '<span>✋</span> Anatomical 12-Phalanx Joint Counter';
      badge.textContent = 'Duodecimal (Base 12) Origin';

      let count = 0;
      const fingerNames = ['Index', 'Middle', 'Ring', 'Little'];
      const jointNames = ['Base Joint', 'Middle Joint', 'Tip Joint'];

      function updateUI() {{
        const fingerIdx = Math.floor((count - 1) / 3);
        const jointIdx = (count - 1) % 3;

        vp.innerHTML = `
          <div style="display:flex; flex-direction:column; align-items:center; gap:12px;">
            <div style="font-size:13px; color:#38bdf8; font-weight:bold;">Current Phalanx Count: <span style="font-size:22px; color:#fbbf24;">${{count}} / 12</span></div>
            <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px; max-width:440px;">
              ${{fingerNames.map((fname, fIdx) => `
                <div style="background:#0f172a; border:1px solid #334155; border-radius:10px; padding:8px; text-align:center;">
                  <div style="font-size:11px; font-weight:bold; color:#a5b4fc; margin-bottom:6px;">${{fname}}</div>
                  <div style="display:flex; flex-direction:column; gap:6px;">
                    ${{[2, 1, 0].map(jIdx => {{
                      const posNumber = fIdx * 3 + jIdx + 1;
                      const isCurrent = (count === posNumber);
                      const isCounted = (count >= posNumber);
                      return `
                        <div style="padding:6px 4px; border-radius:6px; font-size:11px; font-weight:bold; background:${{isCurrent ? '#f59e0b' : (isCounted ? '#10b981' : '#1e293b')}}; color:${{isCurrent || isCounted ? '#fff' : '#64748b'}};">
                          ${{posNumber}} (${{jointNames[jIdx].split(' ')[0]}})
                        </div>
                      `;
                    }}).join('')}}
                  </div>
                </div>
              `).join('')}}
            </div>
            <div style="font-size:12px; color:#94a3b8; text-align:center; max-width:420px;">
              ${{count === 0 ? 'Use thumb to touch the first joint on the index finger.' : `Thumb touching: <strong>${{fingerNames[fingerIdx]}} finger, ${{jointNames[jointIdx]}}</strong> (Count ${{count}}).`}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="nextJointBtn">Next Joint (+1)</button>
        <button class="sim-btn" id="prevJointBtn">Previous Joint (-1)</button>
        <button class="sim-btn" id="resetHandBtn">Reset Hand</button>
      `;

      document.getElementById('nextJointBtn').onclick = () => {{
        if (count < 12) count++;
        updateUI();
      }};
      document.getElementById('prevJointBtn').onclick = () => {{
        if (count > 0) count--;
        updateUI();
      }};
      document.getElementById('resetHandBtn').onclick = () => {{
        count = 0;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 4: Ishango Tally Bone Explorer
    function renderSim4(vp, controls, title, badge) {{
      title.innerHTML = '<span>🦴</span> 20,000 BCE Ishango Bone Notches';
      badge.textContent = 'Paleolithic Prime Patterns';

      let activeCol = 1;

      function updateUI() {{
        vp.innerHTML = `
          <div style="display:flex; gap:20px; align-items:center; justify-content:center; flex-wrap:wrap;">
            <!-- Notched Bone SVG Illustration -->
            <svg width="220" height="150" viewBox="0 0 220 150">
              <path d="M 30 40 Q 110 30 190 40 Q 200 75 190 110 Q 110 120 30 110 Q 20 75 30 40 Z" fill="#78350f" stroke="#b45309" stroke-width="3"/>
              <!-- Column 1 notches (Primes) -->
              <g stroke="${{activeCol === 1 ? '#38bdf8' : '#cbd5e1'}}" stroke-width="2">
                <line x1="50" y1="46" x2="50" y2="62"/>
                <line x1="55" y1="46" x2="55" y2="62"/>
                <line x1="60" y1="46" x2="60" y2="62"/>
                <line x1="75" y1="46" x2="75" y2="62"/>
                <line x1="80" y1="46" x2="80" y2="62"/>
                <line x1="85" y1="46" x2="85" y2="62"/>
                <line x1="90" y1="46" x2="90" y2="62"/>
                <line x1="110" y1="46" x2="110" y2="62"/>
                <line x1="115" y1="46" x2="115" y2="62"/>
                <line x1="120" y1="46" x2="120" y2="62"/>
                <line x1="140" y1="46" x2="140" y2="62"/>
                <line x1="145" y1="46" x2="145" y2="62"/>
                <line x1="150" y1="46" x2="150" y2="62"/>
              </g>
              <!-- Quartz crystal mount tip -->
              <polygon points="190,65 215,75 190,85" fill="#e0f2fe"/>
            </svg>

            <!-- Column Data Info -->
            <div style="max-width:280px; font-size:13px; line-height:1.6;">
              ${{activeCol === 1 ? `
                <div style="color:#38bdf8; font-weight:bold; font-size:15px; margin-bottom:4px;">Column 1: Prime Numbers</div>
                <p>Notches grouped as: <strong>11, 13, 17, 19</strong>.</p>
                <p style="color:#94a3b8; font-size:12px;">These are precisely all prime numbers between 10 and 20! Sum = 60.</p>
              ` : (activeCol === 2 ? `
                <div style="color:#10b981; font-weight:bold; font-size:15px; margin-bottom:4px;">Column 2: Doubling & Halving</div>
                <p>Notches grouped as: <strong>3 & 6, 4 & 8, 5 & 10</strong>.</p>
                <p style="color:#94a3b8; font-size:12px;">Demonstrates deliberate multiplication by 2 (duplation).</p>
              ` : `
                <div style="color:#f59e0b; font-weight:bold; font-size:15px; margin-bottom:4px;">Column 3: Odd Numbers</div>
                <p>Notches grouped as: <strong>9, 11, 19, 21</strong>.</p>
                <p style="color:#94a3b8; font-size:12px;">Decomposed into 10±1 and 20±1 combinations.</p>
              `)}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn ${{activeCol === 1 ? 'active' : ''}}" id="col1Btn">Column 1 (Primes: 11,13,17,19)</button>
        <button class="sim-btn ${{activeCol === 2 ? 'active' : ''}}" id="col2Btn">Column 2 (Doublings: 3→6, 4→8)</button>
        <button class="sim-btn ${{activeCol === 3 ? 'active' : ''}}" id="col3Btn">Column 3 (Odds: 9,11,19,21)</button>
      `;

      document.getElementById('col1Btn').onclick = () => {{ activeCol = 1; updateUI(); }};
      document.getElementById('col2Btn').onclick = () => {{ activeCol = 2; updateUI(); }};
      document.getElementById('col3Btn').onclick = () => {{ activeCol = 3; updateUI(); }};

      updateUI();
    }}

    // Sim 5: Gumulgal Binary Pair-Counting Word Generator
    function renderSim5(vp, controls, title, badge) {{
      title.innerHTML = '<span>🗣️</span> Gumulgal Pair-Counting Word Generator';
      badge.textContent = 'Additive Base-2 Vocabulary';

      let num = 6;

      function getGumulgalName(n) {{
        const twos = Math.floor(n / 2);
        const ones = n % 2;
        let parts = [];
        for (let i = 0; i < twos; i++) parts.push('ukasar');
        if (ones === 1) parts.push('urapun');
        return parts.join('-');
      }}

      function updateUI() {{
        const word = getGumulgalName(num);
        const charCount = word.length;
        const modernCharCount = num.toString().length;

        vp.innerHTML = `
          <div style="text-align:center; max-width:500px;">
            <div style="font-size:14px; color:#94a3b8; margin-bottom:8px;">Target Decimal Number: <span style="font-size:24px; color:#38bdf8; font-weight:bold;">${{num}}</span></div>
            <div style="background:#0f172a; border:1px solid #6366f1; border-radius:12px; padding:16px; margin-bottom:14px;">
              <div style="font-size:11px; color:#a5b4fc; text-transform:uppercase; font-weight:bold; margin-bottom:4px;">Gumulgal Compounded Name</div>
              <div style="font-size:17px; font-weight:bold; color:#fbbf24; word-break:break-all; line-height:1.4;">${{word}}</div>
            </div>
            <div style="display:flex; justify-content:space-around; font-size:12px;">
              <span style="color:#cbd5e1;">Modern Digits: <strong>${{modernCharCount}} char</strong></span>
              <span style="color:#fb7185;">Gumulgal Word: <strong>${{charCount}} chars (${{Math.floor(num/2)}} pairs)</strong></span>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <label class="sim-slider-label">
          Select Quantity:
          <input type="range" class="sim-slider" id="gumulgalSlider" min="1" max="15" value="${{num}}">
          <span id="gumulgalVal">${{num}}</span>
        </label>
      `;

      document.getElementById('gumulgalSlider').oninput = (e) => {{
        num = parseInt(e.target.value);
        document.getElementById('gumulgalVal').textContent = num;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 6: Roman Numeral Converter & Abacus Evaluator
    function renderSim6(vp, controls, title, badge) {{
      title.innerHTML = '<span>🏛️</span> Roman Numeral Assembly & Rule Tester';
      badge.textContent = 'Additive & Subtractive Principles';

      let num = 1984;

      function toRoman(n) {{
        const map = [
          [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
          [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
          [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
        ];
        let res = '';
        let decomp = [];
        let temp = n;
        for (let [val, sym] of map) {{
          while (temp >= val) {{
            res += sym;
            decomp.push(`${{sym}} (${{val}})`);
            temp -= val;
          }}
        }}
        return {{ roman: res, decomp }};
      }}

      function updateUI() {{
        const rData = toRoman(num);
        vp.innerHTML = `
          <div style="text-align:center; max-width:500px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:4px;">Decimal Number: <span style="font-size:22px; color:#38bdf8; font-weight:bold;">${{num}}</span></div>
            <div style="background:#0f172a; border:2px solid #f59e0b; border-radius:12px; padding:14px; margin-bottom:12px;">
              <div style="font-size:11px; color:#a5b4fc; text-transform:uppercase; font-weight:bold;">Roman Glyph String</div>
              <div style="font-size:28px; font-weight:bold; color:#fbbf24; letter-spacing:2px;">${{rData.roman}}</div>
            </div>
            <div style="font-size:12px; color:#cbd5e1; max-height:60px; overflow-y:auto;">
              Additive Breakdown: ${{rData.decomp.join(' + ')}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <label class="sim-slider-label">
          Choose Number (1–2500):
          <input type="range" class="sim-slider" id="romanSlider" min="1" max="2500" value="${{num}}">
          <span id="romanVal">${{num}}</span>
        </label>
        <button class="sim-btn" id="rEx1">1984 (MCMLXXXIV)</button>
        <button class="sim-btn" id="rEx2">444 (CDXLIV)</button>
        <button class="sim-btn" id="rEx3">2026 (MMXXVI)</button>
      `;

      document.getElementById('romanSlider').oninput = (e) => {{
        num = parseInt(e.target.value);
        document.getElementById('romanVal').textContent = num;
        updateUI();
      }};
      document.getElementById('rEx1').onclick = () => {{ num = 1984; document.getElementById('romanSlider').value = 1984; document.getElementById('romanVal').textContent = 1984; updateUI(); }};
      document.getElementById('rEx2').onclick = () => {{ num = 444; document.getElementById('romanSlider').value = 444; document.getElementById('romanVal').textContent = 444; updateUI(); }};
      document.getElementById('rEx3').onclick = () => {{ num = 2026; document.getElementById('romanSlider').value = 2026; document.getElementById('romanVal').textContent = 2026; updateUI(); }};

      updateUI();
    }}

    // Sim 7: Multi-Base Bundle Visualizer
    function renderSim7(vp, controls, title, badge) {{
      title.innerHTML = '<span>📦</span> Multi-Base Unit Bundler';
      badge.textContent = 'Bases 5, 10, 12, 20';

      let totalItems = 37;
      let activeBase = 10;

      function updateUI() {{
        const bundles = Math.floor(totalItems / activeBase);
        const loose = totalItems % activeBase;

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:500px;">
            <div style="font-size:13px; color:#cbd5e1; margin-bottom:10px;">
              Grouping <strong>${{totalItems}} items</strong> in <strong>Base ${{activeBase}}</strong>:
            </div>
            <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; align-items:center;">
              <!-- Bundles -->
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:10px; padding:12px; min-width:140px;">
                <div style="font-size:11px; color:#34d399; font-weight:bold; margin-bottom:6px;">${{bundles}} Bundles of ${{activeBase}}</div>
                <div style="display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
                  ${{Array(bundles).fill(0).map(() => '<span style="font-size:20px;">📦</span>').join('')}}
                </div>
                <div style="font-size:11px; color:#94a3b8; margin-top:4px;">= ${{bundles * activeBase}} items</div>
              </div>
              <!-- Loose -->
              <div style="background:#1e293b; border:1px solid #38bdf8; border-radius:10px; padding:12px; min-width:140px;">
                <div style="font-size:11px; color:#38bdf8; font-weight:bold; margin-bottom:6px;">${{loose}} Loose Units</div>
                <div style="display:flex; gap:4px; justify-content:center; flex-wrap:wrap;">
                  ${{Array(loose).fill(0).map(() => '<span style="font-size:14px;">⚪</span>').join('')}}
                </div>
                <div style="font-size:11px; color:#94a3b8; margin-top:4px;">= ${{loose}} items</div>
              </div>
            </div>
            <div style="margin-top:14px; font-size:14px; font-weight:bold; color:#fbbf24;">
              Mathematical Expression: ${{totalItems}} = ${{bundles}} × ${{activeBase}} + ${{loose}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn ${{activeBase === 5 ? 'active' : ''}}" id="b5Btn">Base 5 (Quinary)</button>
        <button class="sim-btn ${{activeBase === 10 ? 'active' : ''}}" id="b10Btn">Base 10 (Decimal)</button>
        <button class="sim-btn ${{activeBase === 12 ? 'active' : ''}}" id="b12Btn">Base 12 (Duodecimal)</button>
        <button class="sim-btn ${{activeBase === 20 ? 'active' : ''}}" id="b20Btn">Base 20 (Vigesimal)</button>
      `;

      document.getElementById('b5Btn').onclick = () => {{ activeBase = 5; updateUI(); }};
      document.getElementById('b10Btn').onclick = () => {{ activeBase = 10; updateUI(); }};
      document.getElementById('b12Btn').onclick = () => {{ activeBase = 12; updateUI(); }};
      document.getElementById('b20Btn').onclick = () => {{ activeBase = 20; updateUI(); }};

      updateUI();
    }}

    // Sim 8: Egyptian Hieroglyphic Scribe Slate
    function renderSim8(vp, controls, title, badge) {{
      title.innerHTML = '<span>📜</span> Egyptian Hieroglyphic Scribe Slate';
      badge.textContent = 'Purely Additive Base-10 Pictures';

      let num = 2345;

      function updateUI() {{
        const lotus = Math.floor((num % 10000) / 1000);
        const coils = Math.floor((num % 1000) / 100);
        const heels = Math.floor((num % 100) / 10);
        const strokes = num % 10;

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:520px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:6px;">Carving Number: <span style="font-size:22px; color:#38bdf8; font-weight:bold;">${{num}}</span></div>
            <!-- Papyrus Slate -->
            <div style="background:#fef3c7; color:#78350f; border:2px solid #b45309; border-radius:12px; padding:16px; min-height:100px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px;">
              <div style="font-size:26px; display:flex; flex-wrap:wrap; justify-content:center; gap:8px; line-height:1.2;">
                ${{Array(lotus).fill('𓆼').join('')}}
                ${{Array(coils).fill('𓍢').join('')}}
                ${{Array(heels).fill('𓎆').join('')}}
                ${{Array(strokes).fill('𓏺').join('')}}
              </div>
              <div style="font-size:11px; font-weight:bold; color:#92400e; margin-top:6px;">
                ${{lotus}} Lotus (${{lotus * 1000}}) + ${{coils}} Coils (${{coils * 100}}) + ${{heels}} Heels (${{heels * 10}}) + ${{strokes}} Strokes (${{strokes}})
              </div>
            </div>
            <div style="font-size:12px; color:#cbd5e1; margin-top:8px;">
              Total glyphs carved: <strong>${{lotus + coils + heels + strokes}} symbols</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <label class="sim-slider-label">
          Choose Number (1–5000):
          <input type="range" class="sim-slider" id="egSlider" min="1" max="5000" value="${{num}}">
          <span id="egVal">${{num}}</span>
        </label>
        <button class="sim-btn" id="eg999">999 (27 Glyphs!)</button>
        <button class="sim-btn" id="eg2345">2345</button>
      `;

      document.getElementById('egSlider').oninput = (e) => {{
        num = parseInt(e.target.value);
        document.getElementById('egVal').textContent = num;
        updateUI();
      }};
      document.getElementById('eg999').onclick = () => {{ num = 999; document.getElementById('egSlider').value = 999; document.getElementById('egVal').textContent = 999; updateUI(); }};
      document.getElementById('eg2345').onclick = () => {{ num = 2345; document.getElementById('egSlider').value = 2345; document.getElementById('egVal').textContent = 2345; updateUI(); }};

      updateUI();
    }}

    // Sim 9: Additive Symbol Count Comparator
    function renderSim9(vp, controls, title, badge) {{
      title.innerHTML = '<span>⚖️</span> Ancient Additive Systems Efficiency';
      badge.textContent = 'Glyph Count Benchmark';

      let num = 748;

      function updateUI() {{
        // Egyptian glyph count: 7 coils + 4 heels + 8 strokes = 19
        const egCount = 7 + 4 + 8;
        // Roman DCCXLVIII: D(1)+CC(2)+XL(2)+V(1)+III(3) = 9
        const romanStr = 'DCCXLVIII';
        // Modern: 3
        const modernCount = num.toString().length;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; font-size:13px;">
            <div style="text-align:center; font-weight:bold; color:#38bdf8; margin-bottom:12px;">Representing Number: ${{num}}</div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div style="background:#1e293b; padding:10px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
                <span>Egyptian Hieroglyphs:</span>
                <span style="color:#ef4444; font-weight:bold;">19 Glyphs (Excessive labor)</span>
              </div>
              <div style="background:#1e293b; padding:10px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
                <span>Roman Numerals (${{romanStr}}):</span>
                <span style="color:#f59e0b; font-weight:bold;">9 Glyphs</span>
              </div>
              <div style="background:#1e293b; padding:10px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; border:1px solid #10b981;">
                <span>Hindu-Arabic Positional:</span>
                <span style="color:#34d399; font-weight:bold;">3 Digits (6.3x more compact!)</span>
              </div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="cmp748">748 Benchmark</button>
        <button class="sim-btn" id="cmp999">999 Benchmark</button>
      `;

      document.getElementById('cmp748').onclick = () => {{ num = 748; updateUI(); }};
      document.getElementById('cmp999').onclick = () => {{ num = 999; updateUI(); }};

      updateUI();
    }}

    // Sim 10: Egyptian Doubling Multiplication Calculator
    function renderSim10(vp, controls, title, badge) {{
      title.innerHTML = '<span>✖️</span> Egyptian Doubling & Halving Multiplier';
      badge.textContent = 'Ancient Binary Algorithm';

      let a = 23;
      let b = 14;

      function updateUI() {{
        // Decompose a into powers of 2
        let powers = [];
        let p = 1;
        while (p <= a) {{
          powers.push({{ power: p, val: p * b, used: (a & p) !== 0 }});
          p *= 2;
        }}

        const sumVal = a * b;

        vp.innerHTML = `
          <div style="width:100%; max-width:500px; font-size:12.5px;">
            <div style="text-align:center; font-weight:bold; color:#38bdf8; margin-bottom:8px;">Multiplying ${{a}} × ${{b}} = ${{sumVal}}</div>
            <table style="width:100%; border-collapse:collapse; background:#0f172a; border-radius:8px; overflow:hidden;">
              <tr style="border-bottom:1px solid #334155; color:#a5b4fc; text-align:left;">
                <th style="padding:6px;">Select?</th>
                <th style="padding:6px;">Power of 2</th>
                <th style="padding:6px;">Multiple of ${{b}}</th>
              </tr>
              ${{powers.map(row => `
                <tr style="background:${{row.used ? 'rgba(16,185,129,0.15)' : 'transparent'}}; color:${{row.used ? '#34d399' : '#64748b'}};">
                  <td style="padding:5px;">${{row.used ? '✓ USE' : '—'}}</td>
                  <td style="padding:5px;">${{row.power}}</td>
                  <td style="padding:5px; font-weight:bold;">${{row.val}}</td>
                </tr>
              `).join('')}}
            </table>
            <div style="margin-top:10px; font-size:12px; color:#cbd5e1; text-align:center;">
              Summing rows (${{powers.filter(r => r.used).map(r => r.val).join(' + ')}}) = <strong>${{sumVal}}</strong>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="egMul1">23 × 14 (= 322)</button>
        <button class="sim-btn" id="egMul2">13 × 17 (= 221)</button>
      `;

      document.getElementById('egMul1').onclick = () => {{ a = 23; b = 14; updateUI(); }};
      document.getElementById('egMul2').onclick = () => {{ a = 13; b = 17; updateUI(); }};

      updateUI();
    }}

    // Sim 11: Place Value Magnifier Abacus
    function renderSim11(vp, controls, title, badge) {{
      title.innerHTML = '<span>🔎</span> Positional Place-Value Magnifier';
      badge.textContent = 'Face Value vs. Place Value';

      let digit = 5;
      let colPower = 2; // Hundreds

      function updateUI() {{
        const placeMultiplier = Math.pow(10, colPower);
        const colNames = ['Units (10⁰ = 1)', 'Tens (10¹ = 10)', 'Hundreds (10² = 100)', 'Thousands (10³ = 1000)'];

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:500px;">
            <div style="display:flex; justify-content:space-around; gap:8px; margin-bottom:16px;">
              ${{[3, 2, 1, 0].map(p => `
                <div style="flex:1; background:${{colPower === p ? '#4f46e5' : '#1e293b'}}; border:1px solid ${{colPower === p ? '#818cf8' : '#334155'}}; border-radius:10px; padding:10px 4px; text-align:center;">
                  <div style="font-size:10px; color:#cbd5e1;">${{colNames[p].split(' ')[0]}}</div>
                  <div style="font-size:26px; font-weight:bold; color:${{colPower === p ? '#fff' : '#64748b'}}; margin:4px 0;">
                    ${{colPower === p ? digit : 0}}
                  </div>
                  <div style="font-size:10px; color:#94a3b8;">10^${{p}}</div>
                </div>
              `).join('')}}
            </div>
            <div style="background:#0f172a; border:1px solid #10b981; border-radius:10px; padding:12px; font-size:13px; line-height:1.6;">
              <div>Face Value (Intrinsic): <strong style="color:#38bdf8;">${{digit}}</strong></div>
              <div>Position Weight: <strong style="color:#a5b4fc;">${{placeMultiplier}}</strong> (${{colNames[colPower]}})</div>
              <div style="font-size:15px; font-weight:bold; color:#34d399; margin-top:4px;">
                Total Real Place Value = ${{digit}} × ${{placeMultiplier}} = ${{digit * placeMultiplier}}
              </div>
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="shiftLBtn">← Shift Left (×10)</button>
        <button class="sim-btn" id="shiftRBtn">Shift Right (÷10) →</button>
      `;

      document.getElementById('shiftLBtn').onclick = () => {{
        if (colPower < 3) colPower++;
        updateUI();
      }};
      document.getElementById('shiftRBtn').onclick = () => {{
        if (colPower > 0) colPower--;
        updateUI();
      }};

      updateUI();
    }}

    // Sim 12: Babylonian Sexagesimal Cuneiform Decomposer
    function renderSim12(vp, controls, title, badge) {{
      title.innerHTML = '<span>🏛️</span> Babylonian Base-60 Cuneiform Scribe';
      badge.textContent = 'Sexagesimal Positional Hierarchy';

      let num = 131;

      function updateUI() {{
        const c60 = Math.floor(num / 60);
        const c1 = num % 60;

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:500px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:10px;">Decimal Number: <span style="font-size:22px; color:#38bdf8; font-weight:bold;">${{num}}</span></div>
            <div style="display:flex; justify-content:center; gap:24px; align-items:center;">
              <!-- 60s Column -->
              <div style="background:#1e293b; border:1px solid #f59e0b; border-radius:10px; padding:12px 18px; text-align:center; min-width:120px;">
                <div style="font-size:11px; color:#fbbf24; font-weight:bold;">Sixties Column (60¹)</div>
                <div style="font-size:26px; color:#fef08a; margin:6px 0;">${{c60 > 0 ? Array(c60).fill('∇').join('') : '∅'}}</div>
                <div style="font-size:11px; color:#94a3b8;">${{c60}} × 60 = ${{c60 * 60}}</div>
              </div>

              <div style="font-size:20px; color:#64748b;">+</div>

              <!-- 1s Column -->
              <div style="background:#1e293b; border:1px solid #38bdf8; border-radius:10px; padding:12px 18px; text-align:center; min-width:120px;">
                <div style="font-size:11px; color:#38bdf8; font-weight:bold;">Units Column (60⁰)</div>
                <div style="font-size:20px; color:#bae6fd; margin:6px 0;">
                  ${{Math.floor(c1 / 10) > 0 ? Array(Math.floor(c1 / 10)).fill('≺').join('') + ' ' : ''}}
                  ${{Array(c1 % 10).fill('∇').join('')}}
                </div>
                <div style="font-size:11px; color:#94a3b8;">${{c1}} × 1 = ${{c1}}</div>
              </div>
            </div>
            <div style="margin-top:14px; font-size:13.5px; font-weight:bold; color:#34d399;">
              ${{c60 * 60}} + ${{c1}} = ${{num}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="bab131">131 ([2][11])</button>
        <button class="sim-btn" id="bab80">80 ([1][20])</button>
        <button class="sim-btn" id="bab3661">3661 ([1][1][1])</button>
      `;

      document.getElementById('bab131').onclick = () => {{ num = 131; updateUI(); }};
      document.getElementById('bab80').onclick = () => {{ num = 80; updateUI(); }};
      document.getElementById('bab3661').onclick = () => {{ num = 3661; updateUI(); }};

      updateUI();
    }}

    // Sim 13: Mayan Vertical Glyph Stacker
    function renderSim13(vp, controls, title, badge) {{
      title.innerHTML = '<span>🌴</span> Mayan Vertical Vigesimal (Base 20) Stacker';
      badge.textContent = 'Dots, Bars & Sea Shell Zero';

      let num = 47;

      function renderTierGlyph(val) {{
        if (val === 0) return '<span style="font-size:24px; color:#34d399;">🐚 (Shell = 0)</span>';
        const bars = Math.floor(val / 5);
        const dots = val % 5;
        return `
          <div style="display:flex; flex-direction:column; align-items:center; gap:2px;">
            <div style="font-size:16px; color:#38bdf8; letter-spacing:2px;">${{Array(dots).fill('●').join(' ')}}</div>
            ${{Array(bars).fill('<div style="width:36px; height:5px; background:#f59e0b; border-radius:2px; margin:1px 0;"></div>').join('')}}
          </div>
        `;
      }}

      function updateUI() {{
        const t2 = Math.floor(num / 20); // Twenties
        const t1 = num % 20;            // Units

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:440px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">Decimal Number: <span style="font-size:20px; color:#38bdf8; font-weight:bold;">${{num}}</span></div>
            <div style="display:flex; flex-direction:column; gap:8px; align-items:center;">
              <!-- Tier 2 -->
              <div style="background:#1e293b; border:1px solid #6366f1; border-radius:8px; padding:10px; width:200px; text-align:center;">
                <div style="font-size:10px; color:#a5b4fc; font-weight:bold;">Tier 2 (Twenties 20¹)</div>
                ${{renderTierGlyph(t2)}}
                <div style="font-size:11px; color:#94a3b8; margin-top:4px;">${{t2}} × 20 = ${{t2 * 20}}</div>
              </div>
              <!-- Tier 1 -->
              <div style="background:#1e293b; border:1px solid #10b981; border-radius:8px; padding:10px; width:200px; text-align:center;">
                <div style="font-size:10px; color:#34d399; font-weight:bold;">Tier 1 (Units 20⁰)</div>
                ${{renderTierGlyph(t1)}}
                <div style="font-size:11px; color:#94a3b8; margin-top:4px;">${{t1}} × 1 = ${{t1}}</div>
              </div>
            </div>
            <div style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24;">
              Total Mayan Value = ${{t2 * 20}} + ${{t1}} = ${{num}}
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="my47">47 (2 dots over 2 dots + 1 bar)</button>
        <button class="sim-btn" id="my20">20 (1 dot over Shell Zero!)</button>
        <button class="sim-btn" id="my19">19 (4 dots + 3 bars)</button>
      `;

      document.getElementById('my47').onclick = () => {{ num = 47; updateUI(); }};
      document.getElementById('my20').onclick = () => {{ num = 20; updateUI(); }};
      document.getElementById('my19').onclick = () => {{ num = 19; updateUI(); }};

      updateUI();
    }}

    // Sim 14: Chinese Counting Rod Matrix
    function renderSim14(vp, controls, title, badge) {{
      title.innerHTML = '<span>🥢</span> Chinese Bamboo Rod Numeral Board';
      badge.textContent = 'Alternating Vertical & Horizontal Rods';

      let num = 572;
      let isPositive = true;

      function updateUI() {{
        const hundreds = Math.floor(num / 100);
        const tens = Math.floor((num % 100) / 10);
        const units = num % 10;

        const rodColor = isPositive ? '#ef4444' : '#94a3b8';

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:480px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">
              Number: <span style="font-size:22px; color:${{isPositive ? '#ef4444' : '#94a3b8'}}; font-weight:bold;">${{isPositive ? '+' : '-'}}${{num}}</span>
              <span style="font-size:11px; color:#cbd5e1; margin-left:8px;">(${{isPositive ? 'Red = Positive' : 'Black = Negative'}})</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px;">
              <!-- Hundreds (Vertical) -->
              <div style="border-right:1px dashed #334155; padding:4px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:bold;">Hundreds (10²)</div>
                <div style="font-size:11px; color:#64748b; margin-bottom:6px;">Vertical Form</div>
                <div style="font-size:22px; color:${{rodColor}}; font-weight:bold;">${{hundreds}} rods</div>
              </div>
              <!-- Tens (Horizontal) -->
              <div style="border-right:1px dashed #334155; padding:4px;">
                <div style="font-size:10px; color:#f59e0b; font-weight:bold;">Tens (10¹)</div>
                <div style="font-size:11px; color:#64748b; margin-bottom:6px;">Horizontal Form</div>
                <div style="font-size:22px; color:${{rodColor}}; font-weight:bold;">${{tens}} rods</div>
              </div>
              <!-- Units (Vertical) -->
              <div style="padding:4px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:bold;">Units (10⁰)</div>
                <div style="font-size:11px; color:#64748b; margin-bottom:6px;">Vertical Form</div>
                <div style="font-size:22px; color:${{rodColor}}; font-weight:bold;">${{units}} rods</div>
              </div>
            </div>
            <div style="margin-top:12px; font-size:12px; color:#cbd5e1;">
              Alternating forms prevent visual confusion across grid columns without commas or spacers.
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="rodToggleSign">Toggle Positive / Negative (Red vs Black)</button>
        <button class="sim-btn" id="rod572">572</button>
        <button class="sim-btn" id="rod941">941</button>
      `;

      document.getElementById('rodToggleSign').onclick = () => {{
        isPositive = !isPositive;
        updateUI();
      }};
      document.getElementById('rod572').onclick = () => {{ num = 572; updateUI(); }};
      document.getElementById('rod941').onclick = () => {{ num = 941; updateUI(); }};

      updateUI();
    }}

    // Sim 15: Hindu Place-Value Sunya Engine
    function renderSim15(vp, controls, title, badge) {{
      title.innerHTML = '<span>🕉️</span> Hindu Place-Value & Brahmagupta Sunya Engine';
      badge.textContent = 'Decimal Positional Standard';

      let num = 2026;

      function updateUI() {{
        const digits = num.toString().padStart(4, '0').split('');

        vp.innerHTML = `
          <div style="text-align:center; width:100%; max-width:520px;">
            <div style="font-size:13px; color:#94a3b8; margin-bottom:8px;">Hindu Decimal Positional Number: <span style="font-size:24px; color:#34d399; font-weight:bold;">${{num}}</span></div>
            <div style="display:flex; justify-content:center; gap:8px; margin-bottom:14px;">
              ${{digits.map((d, idx) => `
                <div style="background:#1e293b; border:1px solid ${{d === '0' ? '#10b981' : '#6366f1'}}; border-radius:10px; padding:12px 14px; text-align:center; min-width:70px;">
                  <div style="font-size:10px; color:#94a3b8;">10^${{3 - idx}}</div>
                  <div style="font-size:26px; font-weight:bold; color:${{d === '0' ? '#34d399' : '#fff'}}; margin:4px 0;">
                    ${{d === '0' ? '0 (Sunya)' : d}}
                  </div>
                  <div style="font-size:10px; color:#a5b4fc;">${{d * Math.pow(10, 3 - idx)}}</div>
                </div>
              `).join('')}}
            </div>
            <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; border-radius:8px; padding:10px; font-size:12.5px; color:#e2e8f0;">
              Brahmagupta's Law (628 CE): The zero (Sunya) in column 10¹ ensures 2026 does not collapse into 226!
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <button class="sim-btn" id="h2026">2026 (Sunya in tens place)</button>
        <button class="sim-btn" id="h5004">5004 (Dual Sunya placeholders)</button>
      `;

      document.getElementById('h2026').onclick = () => {{ num = 2026; updateUI(); }};
      document.getElementById('h5004').onclick = () => {{ num = 5004; updateUI(); }};

      updateUI();
    }}

    // Sim 16: Global Rosetta Stone Numeral Translator
    function renderSim16(vp, controls, title, badge) {{
      title.innerHTML = '<span>🌍</span> Global Numeral Rosetta Stone';
      badge.textContent = '7 Civilizations Compared Live';

      let num = 75;

      function updateUI() {{
        vp.innerHTML = `
          <div style="width:100%; max-width:540px; font-size:12.5px;">
            <div style="text-align:center; margin-bottom:10px; font-weight:bold; color:#38bdf8; font-size:15px;">
              Input Quantity: ${{num}}
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#94a3b8;">1. Tally Marks:</span><br>
                <span style="color:#cbd5e1;">${{Math.floor(num/5)}} bundles of 5 + ${{num%5}} strokes</span>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#f59e0b;">2. Roman:</span><br>
                <span style="color:#fbbf24; font-weight:bold;">LXXV</span>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#ec4899;">3. Egyptian:</span><br>
                <span style="color:#f472b6;">7 Heel Bones (𓎆) + 5 Strokes (𓏺)</span>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#a855f7;">4. Babylonian (Base 60):</span><br>
                <span style="color:#c084fc;">[1] [15] (1×60 + 15)</span>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#10b981;">5. Mayan (Base 20):</span><br>
                <span style="color:#34d399;">3 twenties + 15 units</span>
              </div>
              <div style="background:#0f172a; padding:8px 12px; border-radius:6px; border:1px solid #334155;">
                <span style="color:#ef4444;">6. Chinese Rod:</span><br>
                <span style="color:#f87171;">7 horizontal rods + 5 vertical rods</span>
              </div>
            </div>
            <div style="margin-top:10px; background:rgba(6,182,212,0.15); border:1px solid #06b6d4; border-radius:6px; padding:8px; text-align:center; font-weight:bold; color:#67e8f9;">
              7. Hindu-Arabic Universal Winner: 75
            </div>
          </div>
        `;
      }}

      controls.innerHTML = `
        <label class="sim-slider-label">
          Translate Quantity:
          <input type="range" class="sim-slider" id="rosettaSlider" min="1" max="100" value="${{num}}">
          <span id="rosettaVal">${{num}}</span>
        </label>
      `;

      document.getElementById('rosettaSlider').oninput = (e) => {{
        num = parseInt(e.target.value);
        document.getElementById('rosettaVal').textContent = num;
        updateUI();
      }};

      updateUI();
    }}
  </script>
</body>
</html>"""

    output_path = "public/animations/class8-math-story-of-numbers.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Successfully generated {output_path} ({len(html_template)} bytes).")

if __name__ == "__main__":
    generate_html()

