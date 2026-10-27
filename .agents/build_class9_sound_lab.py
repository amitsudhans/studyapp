# -*- coding: utf-8 -*-
"""
Builder script to generate public/animations/class9-sound.html
Includes:
- Complete 20-slide interactive animated laboratory
- Voiceover teacher avatar (Prof. Sophia) with audio synthesis & mouth movement
- 16 bespoke interactive SVG simulators
- 32 in-slide checkpoints with teacher explanations
- 40 mastery quiz questions with step-by-step pop-up solution modal
- Strict Slide 20 last slide notice and next button hiding
"""

import json
from class9_sound_data import slides_data, quiz_questions

def build_html():
    slides_json = json.dumps(slides_data)
    quizzes_json = json.dumps(quiz_questions)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 9 Science • Chapter 12: Sound</title>
  
  <!-- KaTeX for crisp mathematical formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <style>
    :root {{
      --bg-primary: #0a0e17;
      --bg-secondary: #121826;
      --card-bg: rgba(26, 34, 53, 0.85);
      --card-border: rgba(99, 130, 201, 0.25);
      --accent-cyan: #00e5ff;
      --accent-blue: #3d7eff;
      --accent-purple: #9d4edd;
      --accent-green: #10b981;
      --accent-amber: #f59e0b;
      --accent-red: #ef4444;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --font-stack: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: radial-gradient(circle at 50% 20%, #152038 0%, var(--bg-primary) 80%);
      color: var(--text-main);
      font-family: var(--font-stack);
      line-height: 1.6;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    /* Top Navigation Bar */
    header.top-nav {{
      background: rgba(18, 24, 38, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .nav-badge {{
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
      color: #050b14;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .nav-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
    }}

    .nav-stats {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}

    .slide-indicator {{
      font-size: 0.9rem;
      color: var(--accent-cyan);
      font-weight: 600;
      background: rgba(0, 229, 255, 0.1);
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid rgba(0, 229, 255, 0.3);
    }}

    /* Layout Container */
    .lab-container {{
      max-width: 1440px;
      margin: 20px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: minmax(0, 1fr) 440px;
      gap: 24px;
    }}

    @media (max-width: 1040px) {{
      .lab-container {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Slide Card */
    .slide-viewport {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
      min-height: 640px;
      display: flex;
      flex-direction: column;
      min-width: 0;
      overflow-x: hidden;
      box-sizing: border-box;
      width: 100%;
    }}

    .slide-header {{
      margin-bottom: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 16px;
    }}

    .slide-header h2 {{
      font-size: 1.8rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .slide-header h3 {{
      font-size: 1rem;
      font-weight: 500;
      color: var(--accent-cyan);
      margin-top: 4px;
    }}

    .slide-body {{
      flex: 1;
    }}

    .lead-p {{
      font-size: 1.05rem;
      margin-bottom: 18px;
      color: #cbd5e1;
    }}

    .theory-box {{
      background: rgba(15, 23, 42, 0.6);
      border-left: 4px solid var(--accent-blue);
      padding: 16px 20px;
      border-radius: 0 10px 10px 0;
      margin-bottom: 20px;
    }}

    .theory-box h4 {{
      color: #38bdf8;
      margin-bottom: 8px;
      font-size: 1.1rem;
    }}

    .highlight-eq {{
      background: rgba(0, 229, 255, 0.08);
      border: 1px solid rgba(0, 229, 255, 0.2);
      border-radius: 8px;
      padding: 10px 16px;
      margin: 12px 0;
      text-align: center;
      color: #e0f2fe;
      font-size: 1.15rem;
    }}

    .grid-2col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 20px;
    }}

    .grid-3col {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-bottom: 20px;
    }}

    @media (max-width: 768px) {{
      .grid-2col, .grid-3col {{
        grid-template-columns: 1fr;
      }}
    }}

    .card-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 14px 18px;
    }}

    .card-item h4, .card-item h5 {{
      color: var(--accent-cyan);
      margin-bottom: 6px;
    }}

    /* Checkpoints within slides */
    .checkpoints-section {{
      margin-top: 24px;
      background: rgba(18, 24, 38, 0.7);
      border: 1px solid rgba(99, 130, 201, 0.3);
      border-radius: 12px;
      padding: 20px;
    }}

    .checkpoints-header {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--accent-amber);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .checkpoint-card {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 14px;
    }}

    .checkpoint-card p.q-text {{
      font-weight: 600;
      color: #f8fafc;
      margin-bottom: 10px;
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    @media (max-width: 600px) {{
      .options-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .option-btn {{
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      padding: 8px 12px;
      border-radius: 6px;
      text-align: left;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .option-btn:hover:not(:disabled) {{
      background: rgba(59, 130, 246, 0.2);
      border-color: rgba(59, 130, 246, 0.5);
      color: #fff;
    }}

    .option-btn.correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-green) !important;
      color: #a7f3d0 !important;
      font-weight: 600;
    }}

    .option-btn.wrong {{
      background: rgba(239, 68, 68, 0.25) !important;
      border-color: var(--accent-red) !important;
      color: #fca5a5 !important;
    }}

    .checkpoint-feedback {{
      margin-top: 10px;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 0.88rem;
      display: none;
    }}

    .checkpoint-feedback.show {{
      display: block;
    }}

    .checkpoint-feedback.correct-fb {{
      background: rgba(16, 185, 129, 0.15);
      border-left: 3px solid var(--accent-green);
      color: #6ee7b7;
    }}

    .checkpoint-feedback.wrong-fb {{
      background: rgba(239, 68, 68, 0.15);
      border-left: 3px solid var(--accent-red);
      color: #fca5a5;
    }}

    /* Quiz Slide Styles */
    .quiz-container {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .quiz-item {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 16px;
      transition: border-color 0.2s;
    }}

    .quiz-item:hover {{
      border-color: rgba(99, 130, 201, 0.4);
    }}

    .quiz-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}

    .quiz-num {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-cyan);
      background: rgba(0, 229, 255, 0.1);
      padding: 3px 8px;
      border-radius: 4px;
    }}

    .view-solution-btn {{
      background: transparent;
      border: 1px solid var(--accent-cyan);
      color: var(--accent-cyan);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.82rem;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .view-solution-btn:hover {{
      background: var(--accent-cyan);
      color: #050b14;
    }}

    /* Right Column: Teacher Avatar & Interactive Simulators */
    .interactive-panel {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* Teacher Avatar Box */
    .teacher-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }}

    .avatar-wrapper {{
      width: 120px;
      height: 120px;
      position: relative;
      margin-bottom: 12px;
    }}

    .avatar-svg {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: radial-gradient(circle, #3b82f6 0%, #1e1b4b 100%);
      box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
    }}

    .teacher-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
    }}

    .teacher-role {{
      font-size: 0.82rem;
      color: var(--accent-cyan);
      margin-bottom: 14px;
    }}

    .speech-bubble {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 14px;
      font-size: 0.88rem;
      color: #e2e8f0;
      position: relative;
      line-height: 1.5;
      text-align: left;
      width: 100%;
      min-height: 70px;
    }}

    .voice-controls {{
      margin-top: 12px;
      display: flex;
      gap: 10px;
      width: 100%;
      justify-content: center;
    }}

    .voice-btn {{
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.4);
      color: #93c5fd;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .voice-btn:hover {{
      background: rgba(59, 130, 246, 0.3);
      color: #fff;
    }}

    /* Simulator Panel Box */
    .simulator-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    .simulator-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
    }}

    .sim-canvas-area {{
      background: #060911;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      height: 280px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .sim-controls {{
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .control-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 0.85rem;
      color: #cbd5e1;
    }}

    .control-row input[type="range"] {{
      flex: 1;
      accent-color: var(--accent-cyan);
    }}

    .control-val {{
      font-family: monospace;
      color: var(--accent-cyan);
      min-width: 48px;
      text-align: right;
    }}

    .sim-btn-row {{
      display: flex;
      gap: 8px;
      margin-top: 6px;
    }}

    .sim-action-btn {{
      flex: 1;
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .sim-action-btn:hover {{
      background: rgba(59, 130, 246, 0.3);
      color: #fff;
    }}

    /* Bottom Slide Controls */
    footer.bottom-bar {{
      max-width: 1440px;
      margin: 10px auto 40px;
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .nav-btn {{
      background: linear-gradient(135deg, var(--accent-blue), #1d4ed8);
      border: none;
      color: #fff;
      padding: 10px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
      transition: all 0.2s;
    }}

    .nav-btn:hover:not(:disabled) {{
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(59, 130, 246, 0.6);
    }}

    .nav-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      box-shadow: none;
    }}

    /* Last Slide Notice (Strictly required) */
    .last-slide-notice {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--accent-green);
      color: #6ee7b7;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      margin-top: 20px;
      display: none;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
    }}

    /* Modal for Detailed Step-by-Step Solutions */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-overlay.active {{
      display: flex;
    }}

    .modal-card {{
      background: var(--bg-secondary);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      max-width: 600px;
      width: 100%;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      position: relative;
    }}

    .modal-close {{
      position: absolute;
      top: 16px;
      right: 16px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
    }}

    .modal-close:hover {{
      color: #fff;
    }}

    .modal-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 12px;
    }}

    .modal-body {{
      color: #cbd5e1;
      font-size: 0.95rem;
      line-height: 1.6;
      white-space: pre-wrap;
    }}
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <header class="top-nav">
    <div class="nav-brand">
      <span class="nav-badge">NCERT • Class 9</span>
      <span class="nav-title">Chapter 12: Sound</span>
    </div>
    <div class="nav-stats">
      <span class="slide-indicator" id="slideIndicator">Slide 1 / 20</span>
    </div>
  </header>

  <!-- Main Laboratory Layout -->
  <main class="lab-container">
    
    <!-- Left Column: Slide Viewport -->
    <section class="slide-viewport">
      <div class="slide-header">
        <h2 id="slideTitle">Loading...</h2>
        <h3 id="slideSubtitle">...</h3>
      </div>
      
      <div class="slide-body" id="slideContent">
        <!-- Dynamic content injected here -->
      </div>

      <!-- In-Slide Checkpoints Section -->
      <div class="checkpoints-section" id="checkpointsSection" style="display: none;">
        <div class="checkpoints-header">
          <span>⚡ Interactive In-Slide Concept Checkpoints</span>
        </div>
        <div id="checkpointsList"></div>
      </div>

      <!-- Quiz Questions Section (Slides 17 to 20) -->
      <div id="quizSection" style="display: none;">
        <div class="quiz-container" id="quizList"></div>
      </div>

      <!-- Strict Last Slide Notice -->
      <div id="lastSlideNotice" class="last-slide-notice">
        You have reached the last slide of this chapter
      </div>
    </section>

    <!-- Right Column: Teacher Avatar & Interactive Simulators -->
    <aside class="interactive-panel">
      
      <!-- Teacher Avatar Box -->
      <div class="teacher-box">
        <div class="avatar-wrapper">
          <svg class="avatar-svg" viewBox="0 0 100 100">
            <!-- Neck & Body -->
            <path d="M30 85 C30 70, 70 70, 70 85 Z" fill="#3b82f6" />
            <!-- Head & Face -->
            <circle cx="50" cy="45" r="24" fill="#fed7aa" />
            <!-- Hair -->
            <path d="M26 45 C26 25, 74 25, 74 45 C74 30, 26 30, 26 45 Z" fill="#475569" />
            <!-- Glasses -->
            <rect x="36" y="40" width="10" height="7" rx="2" fill="none" stroke="#0284c7" stroke-width="2" />
            <rect x="54" y="40" width="10" height="7" rx="2" fill="none" stroke="#0284c7" stroke-width="2" />
            <line x1="46" y1="43" x2="54" y2="43" stroke="#0284c7" stroke-width="2" />
            <!-- Eyes -->
            <circle cx="41" cy="43" r="1.5" fill="#0f172a" />
            <circle cx="59" cy="43" r="1.5" fill="#0f172a" />
            <!-- Animated Talking Mouth -->
            <ellipse id="teacherMouth" cx="50" cy="56" rx="4" ry="1.5" fill="#e11d48" />
          </svg>
        </div>
        <div class="teacher-title">Science Mentor</div>
        <div class="teacher-role">Senior Acoustics & Wave Physics Guide</div>
        <div class="speech-bubble" id="teacherSpeech">
          Welcome to the Sound Master Laboratory!
        </div>
        <div class="voice-controls">
          <button class="voice-btn" id="voiceToggleBtn" onclick="toggleSpeech()">
            <span id="voiceIcon">🔊</span> <span id="voiceLabel">Play Voiceover</span>
          </button>
          <button class="voice-btn" onclick="replaySpeech()">
            <span>🔄</span> <span>Replay</span>
          </button>
        </div>
      </div>

      <!-- Interactive Dynamic Simulator -->
      <div class="simulator-box">
        <div class="simulator-title">
          <span id="simTitle">Bespoke Interactive Lab</span>
          <span style="font-size: 0.75rem; color: var(--accent-cyan); font-weight: normal;">LIVE SVG</span>
        </div>
        
        <div class="sim-canvas-area" id="simCanvasArea">
          <svg id="simSvg" width="100%" height="100%" viewBox="0 0 440 280">
            <!-- Dynamic SVG elements injected by simulator renderer -->
          </svg>
        </div>

        <div class="sim-controls" id="simControls">
          <!-- Interactive Sliders / Buttons -->
        </div>
      </div>

    </aside>

  </main>

  <!-- Bottom Navigation Bar -->
  <footer class="bottom-bar">
    <button class="nav-btn" id="prevBtn" onclick="prevSlide()">
      <span>⬅ Previous Slide</span>
    </button>
    <div style="color: var(--text-muted); font-size: 0.9rem;">
      NCERT Science Class 9 • Chapter 12
    </div>
    <button class="nav-btn" id="nextBtn" onclick="nextSlide()">
      <span>Next Slide ➡</span>
    </button>
  </footer>

  <!-- Detailed Solution Pop-up Modal -->
  <div class="modal-overlay" id="solutionModal">
    <div class="modal-card">
      <button class="modal-close" onclick="closeSolutionModal()">&times;</button>
      <div class="modal-title" id="modalTitle">Question Solution</div>
      <div class="modal-body" id="modalBody"></div>
    </div>
  </div>

  <script>
    const slides = {slides_json};
    const quizData = {quizzes_json};

    let currentSlideIndex = 0;
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let currentUtterance = null;
    let mouthInterval = null;

    // Initialize application
    window.addEventListener('DOMContentLoaded', () => {{
      renderSlide(0);
      setupSpeechSynthesis();
    }});

    function setupSpeechSynthesis() {{
      if ('speechSynthesis' in window) {{
        synth.onvoiceschanged = () => {{
          // Voices ready
        }};
      }}
    }}

    function renderSlide(index) {{
      currentSlideIndex = index;
      const slide = slides[index];

      // Update slide indicator
      document.getElementById('slideIndicator').textContent = `Slide ${{index + 1}} / ${{slides.length}}`;
      document.getElementById('slideTitle').textContent = slide.title;
      document.getElementById('slideSubtitle').textContent = slide.subtitle;
      document.getElementById('slideContent').innerHTML = slide.content;

      // Handle Last Slide Notice & Next Button
      const lastSlideNotice = document.getElementById('lastSlideNotice');
      const nextBtn = document.getElementById('nextBtn');
      const prevBtn = document.getElementById('prevBtn');

      prevBtn.disabled = (index === 0);

      if (index === slides.length - 1) {{
        lastSlideNotice.style.display = 'block';
        nextBtn.style.display = 'none';
      }} else {{
        lastSlideNotice.style.display = 'none';
        nextBtn.style.display = 'inline-flex';
      }}

      // Handle Checkpoints vs Quiz Section
      const checkpointsSection = document.getElementById('checkpointsSection');
      const quizSection = document.getElementById('quizSection');

      if (slide.checkpoints && slide.checkpoints.length > 0) {{
        checkpointsSection.style.display = 'block';
        quizSection.style.display = 'none';
        renderCheckpoints(slide.checkpoints);
      }} else if (slide.quiz_range) {{
        checkpointsSection.style.display = 'none';
        quizSection.style.display = 'block';
        renderQuizQuestions(slide.quiz_range[0], slide.quiz_range[1]);
      }} else {{
        checkpointsSection.style.display = 'none';
        quizSection.style.display = 'none';
      }}

      // Update Teacher Speech & Auto-narrate
      document.getElementById('teacherSpeech').textContent = slide.voice;
      speakText(slide.voice);

      // Render Dedicated Bespoke Simulator
      renderSimulator(slide.sim_type);

      // Render KaTeX Math
      if (window.renderMathInElement) {{
        renderMathInElement(document.getElementById('slideContent'), {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ]
        }});
      }}
    }}

    function nextSlide() {{
      if (currentSlideIndex < slides.length - 1) {{
        renderSlide(currentSlideIndex + 1);
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}

    function prevSlide() {{
      if (currentSlideIndex > 0) {{
        renderSlide(currentSlideIndex - 1);
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}

    // Checkpoints Renderer
    function renderCheckpoints(checkpoints) {{
      const container = document.getElementById('checkpointsList');
      container.innerHTML = '';

      checkpoints.forEach((cp, qIdx) => {{
        const card = document.createElement('div');
        card.className = 'checkpoint-card';
        card.innerHTML = `
          <p class="q-text">Q${{qIdx + 1}}: ${{cp.question}}</p>
          <div class="options-grid" id="cp_opts_${{qIdx}}">
            ${{cp.options.map((opt, oIdx) => `
              <button class="option-btn" onclick="checkAnswer(${{qIdx}}, ${{oIdx}}, ${{cp.correct}}, this)">
                ${{String.fromCharCode(65 + oIdx)}}. ${{opt}}
              </button>
            `).join('')}}
          </div>
          <div class="checkpoint-feedback" id="cp_fb_${{qIdx}}"></div>
        `;
        container.appendChild(card);
      }});
    }}

    function checkAnswer(qIdx, selected, correct, btn) {{
      const parent = document.getElementById(`cp_opts_${{qIdx}}`);
      const buttons = parent.querySelectorAll('.option-btn');
      const fb = document.getElementById(`cp_fb_${{qIdx}}`);
      const currentSlide = slides[currentSlideIndex];
      const explanation = currentSlide.checkpoints[qIdx].explanation;

      buttons.forEach(b => b.disabled = true);

      if (selected === correct) {{
        btn.classList.add('correct');
        fb.className = 'checkpoint-feedback show correct-fb';
        fb.innerHTML = `<strong>✓ Correct!</strong> ${{explanation}}`;
      }} else {{
        btn.classList.add('wrong');
        buttons[correct].classList.add('correct');
        fb.className = 'checkpoint-feedback show wrong-fb';
        fb.innerHTML = `<strong>✗ Incorrect.</strong> ${{explanation}}`;
      }}
    }}

    // Quiz Questions Renderer
    function renderQuizQuestions(startNum, endNum) {{
      const container = document.getElementById('quizList');
      container.innerHTML = '';

      const subset = quizData.filter(q => q.num >= startNum && q.num <= endNum);

      subset.forEach(q => {{
        const card = document.createElement('div');
        card.className = 'quiz-item';
        card.innerHTML = `
          <div class="quiz-header">
            <span class="quiz-num">Question ${{q.num}} of 40</span>
            <button class="view-solution-btn" onclick="openSolutionModal(${{q.num}})">View Solution</button>
          </div>
          <p class="q-text" style="font-weight: 600; margin-bottom: 12px; color: #f8fafc;">${{q.question}}</p>
          <div class="options-grid" id="quiz_opts_${{q.num}}">
            ${{q.options.map((opt, oIdx) => `
              <button class="option-btn" onclick="checkQuizAnswer(${{q.num}}, ${{oIdx}}, ${{q.correct}}, this)">
                ${{String.fromCharCode(65 + oIdx)}}. ${{opt}}
              </button>
            `).join('')}}
          </div>
          <div class="checkpoint-feedback" id="quiz_fb_${{q.num}}"></div>
        `;
        container.appendChild(card);
      }});
    }}

    function checkQuizAnswer(qNum, selected, correct, btn) {{
      const parent = document.getElementById(`quiz_opts_${{qNum}}`);
      const buttons = parent.querySelectorAll('.option-btn');
      const fb = document.getElementById(`quiz_fb_${{qNum}}`);

      buttons.forEach(b => b.disabled = true);

      if (selected === correct) {{
        btn.classList.add('correct');
        fb.className = 'checkpoint-feedback show correct-fb';
        fb.innerHTML = `<strong>✓ Correct!</strong> Click 'View Solution' for complete step-by-step mathematical reasoning.`;
      }} else {{
        btn.classList.add('wrong');
        buttons[correct].classList.add('correct');
        fb.className = 'checkpoint-feedback show wrong-fb';
        fb.innerHTML = `<strong>✗ Incorrect.</strong> Click 'View Solution' to examine the complete derivation.`;
      }}
    }}

    // Solution Modal
    function openSolutionModal(qNum) {{
      const item = quizData.find(q => q.num === qNum);
      if (!item) return;

      document.getElementById('modalTitle').textContent = `Step-by-Step Solution • Question ${{item.num}}`;
      document.getElementById('modalBody').textContent = item.solution;
      document.getElementById('solutionModal').classList.add('active');
    }}

    function closeSolutionModal() {{
      document.getElementById('solutionModal').classList.remove('active');
    }}

    // Speech & Teacher Mouth Animation
    function speakText(text) {{
      if (!('speechSynthesis' in window)) return;
      synth.cancel();
      stopMouth();

      const cleanText = text.replace(/\\$/g, '');
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = 1.0;
      utterance.pitch = 1.05;
      utterance.lang = 'en-US';

      const voices = synth.getVoices();
      const preferred = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Female') || v.name.includes('Natural') || v.name.includes('Samantha')));
      if (preferred) utterance.voice = preferred;

      utterance.onstart = () => {{
        isSpeaking = true;
        document.getElementById('voiceLabel').textContent = 'Pause Voiceover';
        startMouth();
      }};

      utterance.onend = () => {{
        isSpeaking = false;
        document.getElementById('voiceLabel').textContent = 'Play Voiceover';
        stopMouth();
      }};

      utterance.onerror = () => {{
        isSpeaking = false;
        document.getElementById('voiceLabel').textContent = 'Play Voiceover';
        stopMouth();
      }};

      currentUtterance = utterance;
      synth.speak(utterance);
    }}

    function toggleSpeech() {{
      if (synth.speaking) {{
        if (synth.paused) {{
          synth.resume();
          document.getElementById('voiceLabel').textContent = 'Pause Voiceover';
          startMouth();
        }} else {{
          synth.pause();
          document.getElementById('voiceLabel').textContent = 'Resume Voiceover';
          stopMouth();
        }}
      }} else {{
        const slide = slides[currentSlideIndex];
        speakText(slide.voice);
      }}
    }}

    function replaySpeech() {{
      const slide = slides[currentSlideIndex];
      speakText(slide.voice);
    }}

    function startMouth() {{
      stopMouth();
      const mouth = document.getElementById('teacherMouth');
      let open = false;
      mouthInterval = setInterval(() => {{
        open = !open;
        mouth.setAttribute('ry', open ? '5' : '1.5');
      }}, 180);
    }}

    function stopMouth() {{
      if (mouthInterval) clearInterval(mouthInterval);
      const mouth = document.getElementById('teacherMouth');
      if (mouth) mouth.setAttribute('ry', '1.5');
    }}

    // 16 Bespoke Interactive SVG Simulators
    function renderSimulator(type) {{
      const svg = document.getElementById('simSvg');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');

      svg.innerHTML = '';
      controls.innerHTML = '';

      switch (type) {{
        case 'tuning_fork_vibration':
          title.textContent = 'Vibrating Tuning Fork & Air Wavefronts';
          renderTuningForkSim(svg, controls);
          break;
        case 'bell_jar_vacuum':
          title.textContent = 'Bell Jar Vacuum Chamber Laboratory';
          renderBellJarSim(svg, controls);
          break;
        case 'longitudinal_slinky_density':
          title.textContent = 'Longitudinal Compressions & Rarefactions';
          renderSlinkySim(svg, controls);
          break;
        case 'density_waveform_plotter':
          title.textContent = 'Density-Pressure to Sinusoidal Wave Plotter';
          renderWavePlotterSim(svg, controls);
          break;
        case 'frequency_period_synthesizer':
          title.textContent = 'Audio Waveform & Pitch Tone Synthesizer';
          renderAudioSynthSim(svg, controls);
          break;
        case 'wave_speed_calculator':
          title.textContent = 'Wave Speed Relationship: v = ν · λ';
          renderWaveSpeedSim(svg, controls);
          break;
        case 'pitch_loudness_timbre_sim':
          title.textContent = 'Pitch (ν), Loudness (A²), & Harmonic Timbre';
          renderPerceptionSim(svg, controls);
          break;
        case 'hearing_spectrum_dial':
          title.textContent = 'Infrasound, Audible Range, & Ultrasound Dial';
          renderHearingSpectrumSim(svg, controls);
          break;
        case 'medium_speed_race':
          title.textContent = 'Speed of Sound Race: Air vs Water vs Steel';
          renderMediumSpeedRaceSim(svg, controls);
          break;
        case 'sound_reflection_goniometer':
          title.textContent = 'Laws of Sound Reflection (∠i = ∠r) Goniometer';
          renderReflectionGoniometerSim(svg, controls);
          break;
        case 'echo_distance_cliff':
          title.textContent = 'Echo Distance & 17.2m Biological Threshold';
          renderEchoCliffSim(svg, controls);
          break;
        case 'auditorium_reverberation':
          title.textContent = 'Auditorium Reverberation & Acoustic Absorption';
          renderAuditoriumSim(svg, controls);
          break;
        case 'submarine_sonar_sim':
          title.textContent = 'Active Marine SONAR Echo Ranging Simulator';
          renderSonarSim(svg, controls);
          break;
        case 'ultrasound_flaw_scanner':
          title.textContent = 'Industrial Ultrasound Flaw & Crack Scanner';
          renderUltrasoundFlawSim(svg, controls);
          break;
        case 'dual_cliff_echo_sim':
          title.textContent = 'Dual Cliff Multi-Echo Kinematic Challenge';
          renderDualCliffSim(svg, controls);
          break;
        case 'gol_gumbaz_raman_sim':
          title.textContent = 'Gol Gumbaz Whispering Gallery & Raman Mridangam';
          renderGolGumbazSim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Mastery Challenge Dashboard';
          renderQuizDashboardSim(svg, controls);
      }}
    }}

    // 1. Tuning Fork Simulator
    function renderTuningForkSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Tuning Fork Body -->
        <path d="M 80 180 L 100 180 L 100 120 L 120 120 L 120 40 L 110 40 L 110 110 L 90 110 L 90 40 L 80 40 Z" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2" />
        <rect x="85" y="180" width="10" height="60" rx="3" fill="#64748b" />
        <!-- Radiating sound arcs -->
        <g id="soundArcs" transform="translate(120, 80)">
          <path d="M 10 -30 A 30 30 0 0 1 10 30" fill="none" stroke="#00e5ff" stroke-width="3" opacity="0.9" />
          <path d="M 30 -50 A 50 50 0 0 1 30 50" fill="none" stroke="#00e5ff" stroke-width="3" opacity="0.7" />
          <path d="M 50 -70 A 70 70 0 0 1 50 70" fill="none" stroke="#00e5ff" stroke-width="3" opacity="0.5" />
          <path d="M 70 -90 A 90 90 0 0 1 70 90" fill="none" stroke="#00e5ff" stroke-width="3" opacity="0.3" />
        </g>
        <text id="forkFrequency" x="260" y="50" fill="#00e5ff" font-size="14" font-weight="bold" text-anchor="middle">Frequency: 512 Hz (512 cycles/sec)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Fork Frequency (Hz):</span>
          <input type="range" id="forkFreqSlider" min="256" max="1024" step="128" value="512">
          <span class="control-val" id="forkFreqVal">512 Hz</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="strikeFork()">🔨 Strike Tuning Fork</button>
        </div>
      `;

      document.getElementById('forkFreqSlider').addEventListener('input', (e) => {{
        const f = e.target.value;
        document.getElementById('forkFreqVal').textContent = `${{f}} Hz`;
        document.getElementById('forkFrequency').textContent = `Frequency: ${{f}} Hz (${{f}} cycles/sec)`;
      }});

      window.strikeFork = () => {{
        const arcs = document.getElementById('soundArcs');
        arcs.style.transition = 'transform 0.1s ease';
        arcs.style.transform = 'translate(130px, 80px)';
        setTimeout(() => {{
          arcs.style.transform = 'translate(120px, 80px)';
        }}, 100);
      }};
    }}

    // 2. Bell Jar Vacuum Simulator
    function renderBellJarSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Table Base -->
        <rect x="100" y="210" width="240" height="15" fill="#334155" />
        <!-- Glass Jar Outline -->
        <path d="M 130 210 L 130 90 A 90 90 0 0 1 310 90 L 310 210 Z" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="3" />
        <!-- Electric Bell Suspension -->
        <rect x="215" y="70" width="10" height="40" fill="#94a3b8" />
        <!-- Bell Gong -->
        <circle cx="220" cy="130" r="24" fill="#f59e0b" stroke="#d97706" stroke-width="2" />
        <!-- Hammer -->
        <circle id="bellHammer" cx="190" cy="130" r="6" fill="#ef4444" />
        <!-- Vacuum Air Molecules -->
        <g id="airParticles">
          ${{Array.from({{length: 24}}, (_, i) => `<circle cx="${{150 + (i % 6) * 25}}" cy="${{100 + Math.floor(i / 6) * 25}}" r="3" fill="#cbd5e1" class="air-mol" />`).join('')}}
        </g>
        <!-- Sound Meter Readout -->
        <rect x="80" y="235" width="280" height="35" rx="6" fill="#1e293b" />
        <text id="vacuumSoundStatus" x="220" y="258" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Pressure: 1.0 atm | Sound: LOUD (Ringing heard)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="evacuateAir()">💨 Turn ON Vacuum Pump</button>
          <button class="sim-action-btn" onclick="restoreAir()">🔄 Re-admit Air (Normal Pressure)</button>
        </div>
      `;

      window.evacuateAir = () => {{
        const particles = document.querySelectorAll('.air-mol');
        particles.forEach(p => p.style.opacity = '0.05');
        const status = document.getElementById('vacuumSoundStatus');
        status.textContent = 'Pressure: 0.001 atm | Sound: SILENT (Cannot travel in vacuum!)';
        status.setAttribute('fill', '#ef4444');
      }};

      window.restoreAir = () => {{
        const particles = document.querySelectorAll('.air-mol');
        particles.forEach(p => p.style.opacity = '1');
        const status = document.getElementById('vacuumSoundStatus');
        status.textContent = 'Pressure: 1.0 atm | Sound: LOUD (Medium restored)';
        status.setAttribute('fill', '#10b981');
      }};
    }}

    // 3. Slinky & Particle Density Simulator
    function renderSlinkySim(svg, controls) {{
      svg.innerHTML = `
        <text x="220" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Longitudinal Wave: Particles oscillate parallel to wave</text>
        <!-- Compressions & Rarefactions visualizer -->
        <g id="slinkyLines" transform="translate(40, 70)">
          ${{Array.from({{length: 28}}, (_, i) => `<line x1="${{i * 12}}" y1="0" x2="${{i * 12}}" y2="60" stroke="#00e5ff" stroke-width="3" class="slinky-coil" />`).join('')}}
        </g>
        <text x="90" y="160" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Compression (C)</text>
        <text x="180" y="160" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Rarefaction (R)</text>
        <text x="270" y="160" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Compression (C)</text>
        <line x1="90" y1="180" x2="270" y2="180" stroke="#10b981" stroke-width="2" />
        <text x="180" y="200" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Wavelength (λ) between two compressions</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="pulseSlinky()">〰️ Send Longitudinal Pulse</button>
        </div>
      `;

      window.pulseSlinky = () => {{
        const coils = document.querySelectorAll('.slinky-coil');
        coils.forEach((c, idx) => {{
          c.style.transition = 'transform 0.4s ease';
          c.style.transform = `translateX(${{Math.sin(idx * 0.5) * 8}}px)`;
          setTimeout(() => {{
            c.style.transform = 'none';
          }}, 500);
        }});
      }};
    }}

    // 4. Waveform Plotter Simulator
    function renderWavePlotterSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Baseline Center -->
        <line x1="30" y1="140" x2="410" y2="140" stroke="#64748b" stroke-width="2" stroke-dasharray="4" />
        <text x="40" y="70" fill="#94a3b8" font-size="10">Pressure (+ΔP, Crest / C)</text>
        <text x="40" y="220" fill="#94a3b8" font-size="10">Pressure (-ΔP, Trough / R)</text>
        <!-- Sine Waveform -->
        <path id="sinePlot" d="M 40 140 Q 85 60 130 140 T 220 140 T 310 140 T 400 140" fill="none" stroke="#00e5ff" stroke-width="4" />
        <circle id="trackerDot" cx="130" cy="140" r="8" fill="#f59e0b" />
        <text id="trackerLabel" x="220" y="35" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">Tracking Crest: Compression (Max Density)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Wave Position Scanner:</span>
          <input type="range" id="wavePos" min="40" max="400" value="130">
          <span class="control-val" id="wavePosVal">130</span>
        </div>
      `;

      document.getElementById('wavePos').addEventListener('input', (e) => {{
        const x = parseFloat(e.target.value);
        document.getElementById('wavePosVal').textContent = x;
        const dot = document.getElementById('trackerDot');
        const label = document.getElementById('trackerLabel');

        const y = 140 - 80 * Math.sin(((x - 40) / 90) * Math.PI);
        dot.setAttribute('cx', x);
        dot.setAttribute('cy', y);

        if (y < 100) {{
          label.textContent = 'At Crest: High Pressure Compression (C)';
          label.setAttribute('fill', '#f59e0b');
        }} else if (y > 180) {{
          label.textContent = 'At Trough: Low Pressure Rarefaction (R)';
          label.setAttribute('fill', '#38bdf8');
        }} else {{
          label.textContent = 'At Zero-Crossing: Normal Equilibrium Density';
          label.setAttribute('fill', '#10b981');
        }}
      }});
    }}

    // 5. Audio Synth Simulator
    function renderAudioSynthSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="40" y="40" width="360" height="180" rx="10" fill="#0f172a" stroke="#334155" />
        <line x1="50" y1="130" x2="390" y2="130" stroke="#475569" />
        <!-- Waveform Path -->
        <path id="synthWave" d="M 50 130 Q 80 80 110 130 T 170 130 T 230 130 T 290 130 T 350 130" fill="none" stroke="#10b981" stroke-width="4" />
        <text id="synthReadout" x="220" y="250" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Frequency: 440 Hz (Note A4) | Amplitude: 50%</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Frequency (Pitch):</span>
          <input type="range" id="synthFreq" min="220" max="880" value="440">
          <span class="control-val" id="synthFreqVal">440 Hz</span>
        </div>
        <div class="control-row">
          <span>Amplitude (Loudness):</span>
          <input type="range" id="synthAmp" min="10" max="80" value="50">
          <span class="control-val" id="synthAmpVal">50</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="playBeepTone()">🔊 Play Audio Pitch Tone</button>
        </div>
      `;

      function updateSynth() {{
        const freq = parseFloat(document.getElementById('synthFreq').value);
        const amp = parseFloat(document.getElementById('synthAmp').value);
        document.getElementById('synthFreqVal').textContent = `${{freq}} Hz`;
        document.getElementById('synthAmpVal').textContent = `${{amp}}`;

        document.getElementById('synthReadout').textContent = `Frequency: ${{freq}} Hz | Amplitude: ${{amp}}%`;

        // Update SVG path
        const wave = document.getElementById('synthWave');
        const wavelength = 34000 / freq; // visual scaling
        let d = 'M 50 130 ';
        for (let x = 50; x < 390; x += 10) {{
          const y = 130 - amp * Math.sin(((x - 50) / wavelength) * 2 * Math.PI);
          d += `L ${{x}} ${{y}} `;
        }}
        wave.setAttribute('d', d);
      }}

      document.getElementById('synthFreq').addEventListener('input', updateSynth);
      document.getElementById('synthAmp').addEventListener('input', updateSynth);

      window.playBeepTone = () => {{
        try {{
          const ctx = new (window.AudioContext || window.webkitAudioContext)();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          const freq = parseFloat(document.getElementById('synthFreq').value);
          const amp = parseFloat(document.getElementById('synthAmp').value) / 100;
          osc.frequency.value = freq;
          gain.gain.value = amp * 0.2;
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          setTimeout(() => {{
            osc.stop();
            ctx.close();
          }}, 500);
        }} catch(e) {{
          console.log(e);
        }}
      }};
      updateSynth();
    }}

    // 6. Wave Speed Simulator
    function renderWaveSpeedSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="60" y="30" width="320" height="90" rx="8" fill="#1e293b" stroke="#00e5ff" />
        <text x="220" y="55" fill="#94a3b8" font-size="11" text-anchor="middle">SPEED FORMULA: v = ν · λ</text>
        <text id="waveFormulaVal" x="220" y="85" fill="#00e5ff" font-size="16" font-weight="bold" text-anchor="middle">v = 500 Hz × 0.68 m = 340.0 m/s</text>
        <text x="220" y="105" fill="#10b981" font-size="11" text-anchor="middle">(Constant Sound Speed in Air at 20°C)</text>

        <!-- Dynamic graphical waveform -->
        <rect x="40" y="140" width="360" height="90" fill="#0f172a" stroke="#334155" />
        <path id="speedWavePath" d="M 40 185 Q 85 145 130 185 T 220 185 T 310 185 T 400 185" fill="none" stroke="#10b981" stroke-width="4" />
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Frequency (ν):</span>
          <input type="range" id="waveNu" min="200" max="1000" step="50" value="500">
          <span class="control-val" id="waveNuVal">500 Hz</span>
        </div>
      `;

      document.getElementById('waveNu').addEventListener('input', (e) => {{
        const nu = parseFloat(e.target.value);
        document.getElementById('waveNuVal').textContent = `${{nu}} Hz`;
        const v = 340.0;
        const lambda = (v / nu).toFixed(2);
        document.getElementById('waveFormulaVal').textContent = `v = ${{nu}} Hz × ${{lambda}} m = 340.0 m/s`;
      }});
    }}

    // 7. Perception Simulator
    function renderPerceptionSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Pitch Box -->
        <rect x="30" y="40" width="180" height="100" rx="8" fill="#1e293b" />
        <text x="120" y="65" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Pitch (Frequency)</text>
        <text id="pitchLabelText" x="120" y="95" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">High Pitch (Shrill)</text>
        <text x="120" y="125" fill="#94a3b8" font-size="10" text-anchor="middle">Whistle / Mosquito / Bird</text>

        <!-- Loudness Box -->
        <rect x="230" y="40" width="180" height="100" rx="8" fill="#1e293b" />
        <text x="320" y="65" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Loudness (Amplitude²)</text>
        <text id="loudLabelText" x="320" y="95" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">60 dB (Normal Talk)</text>
        <text x="320" y="125" fill="#94a3b8" font-size="10" text-anchor="middle">Loudness ∝ A²</text>

        <!-- Timbre Spectrum Box -->
        <rect x="30" y="160" width="380" height="80" rx="8" fill="#0f172a" stroke="#10b981" />
        <text x="220" y="185" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Timbre / Quality: Identical Pitch & Loudness</text>
        <text id="timbreStatus" x="220" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">Flute (Pure Sine) vs Violin (Rich Multi-Harmonics)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setPerceptionMode('shrill')">🦟 Shrill Whistle (High ν)</button>
          <button class="sim-action-btn" onclick="setPerceptionMode('bass')">🦁 Lion Roar (Low ν)</button>
          <button class="sim-action-btn" onclick="setPerceptionMode('loud')">📢 Shout (High Amp)</button>
        </div>
      `;

      window.setPerceptionMode = (mode) => {{
        if (mode === 'shrill') {{
          document.getElementById('pitchLabelText').textContent = 'High Pitch (2500 Hz)';
          document.getElementById('pitchLabelText').setAttribute('fill', '#00e5ff');
        }} else if (mode === 'bass') {{
          document.getElementById('pitchLabelText').textContent = 'Low Bass (80 Hz)';
          document.getElementById('pitchLabelText').setAttribute('fill', '#f59e0b');
        }} else {{
          document.getElementById('loudLabelText').textContent = '95 dB (Loud Shout)';
          document.getElementById('loudLabelText').setAttribute('fill', '#ef4444');
        }}
      }};
    }}

    // 8. Hearing Spectrum Simulator
    function renderHearingSpectrumSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Spectrum Bar -->
        <rect x="40" y="120" width="100" height="40" fill="#f59e0b" />
        <text x="90" y="145" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Infrasound</text>
        <text x="90" y="110" fill="#f59e0b" font-size="10" text-anchor="middle">&lt; 20 Hz</text>

        <rect x="140" y="120" width="160" height="40" fill="#10b981" />
        <text x="220" y="145" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">Audible to Humans</text>
        <text x="220" y="110" fill="#10b981" font-size="10" text-anchor="middle">20 Hz – 20,000 Hz</text>

        <rect x="300" y="120" width="100" height="40" fill="#38bdf8" />
        <text x="350" y="145" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Ultrasound</text>
        <text x="350" y="110" fill="#38bdf8" font-size="10" text-anchor="middle">&gt; 20 kHz</text>

        <!-- Needle Marker -->
        <polygon id="specNeedle" points="220,170 210,195 230,195" fill="#ef4444" />
        <text id="specNeedleText" x="220" y="225" fill="#ef4444" font-size="14" font-weight="bold" text-anchor="middle">Frequency: 1,000 Hz (Audible)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Frequency Slider:</span>
          <input type="range" id="specSlider" min="1" max="100" value="50">
          <span class="control-val" id="specVal">1 kHz</span>
        </div>
      `;

      document.getElementById('specSlider').addEventListener('input', (e) => {{
        const val = parseFloat(e.target.value);
        const needle = document.getElementById('specNeedle');
        const text = document.getElementById('specNeedleText');
        const x = 40 + (val / 100) * 360;
        needle.setAttribute('points', `${{x}},170 ${{x - 10}},195 ${{x + 10}},195`);
        text.setAttribute('x', x);

        if (x < 140) {{
          text.textContent = 'Infrasonic (Elephant / Quake)';
          text.setAttribute('fill', '#f59e0b');
        }} else if (x <= 300) {{
          text.textContent = 'Audible to Humans';
          text.setAttribute('fill', '#10b981');
        }} else {{
          text.textContent = 'Ultrasonic (Bat / Dolphin)';
          text.setAttribute('fill', '#38bdf8');
        }}
      }});
    }}

    // 9. Medium Speed Race Simulator
    function renderMediumSpeedRaceSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Track 1: Steel -->
        <rect x="40" y="60" width="360" height="25" fill="#334155" />
        <text x="50" y="77" fill="#fff" font-size="11" font-weight="bold">Steel Rail (5960 m/s)</text>
        <circle id="steelPulse" cx="200" cy="72" r="8" fill="#10b981" />

        <!-- Track 2: Water -->
        <rect x="40" y="115" width="360" height="25" fill="#0369a1" />
        <text x="50" y="132" fill="#fff" font-size="11" font-weight="bold">Water Pipe (1500 m/s)</text>
        <circle id="waterPulse" cx="200" cy="127" r="8" fill="#38bdf8" />

        <!-- Track 3: Air -->
        <rect x="40" y="170" width="360" height="25" fill="#1e293b" />
        <text x="50" y="187" fill="#fff" font-size="11" font-weight="bold">Air (344 m/s)</text>
        <circle id="airPulse" cx="200" cy="182" r="8" fill="#f59e0b" />

        <text x="220" y="240" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Hierarchy: Solids &gt; Liquids &gt; Gases</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="startMediumRace()">🏁 Race Sound Pulses!</button>
        </div>
      `;

      window.startMediumRace = () => {{
        const s = document.getElementById('steelPulse');
        const w = document.getElementById('waterPulse');
        const a = document.getElementById('airPulse');

        s.style.transition = 'transform 0.15s linear';
        s.style.transform = 'translateX(180px)';

        w.style.transition = 'transform 0.6s linear';
        w.style.transform = 'translateX(180px)';

        a.style.transition = 'transform 2.0s linear';
        a.style.transform = 'translateX(180px)';

        setTimeout(() => {{
          s.style.transform = 'none';
          w.style.transform = 'none';
          a.style.transform = 'none';
        }}, 3000);
      }};
    }}

    // 10. Sound Reflection Goniometer
    function renderReflectionGoniometerSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Reflecting Wall -->
        <rect x="210" y="20" width="20" height="220" fill="#475569" stroke="#94a3b8" />
        <line x1="220" y1="20" x2="220" y2="240" stroke="#cbd5e1" stroke-width="2" />
        <line x1="80" y1="130" x2="360" y2="130" stroke="#64748b" stroke-dasharray="4" />
        <!-- Normal line label -->
        <text x="140" y="125" fill="#94a3b8" font-size="10">Normal</text>

        <!-- Incident Tube -->
        <line id="incTube" x1="100" y1="60" x2="220" y2="130" stroke="#00e5ff" stroke-width="6" />
        <!-- Reflected Tube -->
        <line id="refTube" x1="220" y1="130" x2="100" y2="200" stroke="#f59e0b" stroke-width="6" />

        <text id="gonReadout" x="220" y="260" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Law of Acoustic Reflection: ∠i = 40° = ∠r = 40°</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Incident Angle (∠i):</span>
          <input type="range" id="gonAngle" min="15" max="60" value="40">
          <span class="control-val" id="gonAngleVal">40°</span>
        </div>
      `;

      document.getElementById('gonAngle').addEventListener('input', (e) => {{
        const deg = parseFloat(e.target.value);
        document.getElementById('gonAngleVal').textContent = `${{deg}}°`;
        const rad = (deg * Math.PI) / 180;
        const len = 140;

        const xInc = 220 - len * Math.cos(rad);
        const yInc = 130 - len * Math.sin(rad);
        document.getElementById('incTube').setAttribute('x1', xInc);
        document.getElementById('incTube').setAttribute('y1', yInc);

        const xRef = 220 - len * Math.cos(rad);
        const yRef = 130 + len * Math.sin(rad);
        document.getElementById('refTube').setAttribute('x2', xRef);
        document.getElementById('refTube').setAttribute('y2', yRef);

        document.getElementById('gonReadout').textContent = `Law of Acoustic Reflection: ∠i = ${{deg}}° = ∠r = ${{deg}}°`;
      }});
    }}

    // 11. Echo Distance Simulator
    function renderEchoCliffSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="210" width="400" height="10" fill="#334155" />
        <!-- Observer -->
        <circle cx="60" cy="180" r="10" fill="#00e5ff" />
        <!-- Reflecting Cliff Face -->
        <polygon id="cliffFace" points="260,60 280,60 280,210 260,210" fill="#78350f" stroke="#b45309" stroke-width="2" />
        <!-- Distance Line -->
        <line id="echoDistLine" x1="60" y1="225" x2="260" y2="225" stroke="#f59e0b" stroke-width="3" />
        <text id="echoDistText" x="160" y="245" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Distance: 17.2 m (Threshold)</text>
        <text id="echoVerdict" x="220" y="40" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Echo Heard Distinctly (Round Trip Time = 0.10 s)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Cliff Distance:</span>
          <input type="range" id="cliffSlider" min="5" max="50" value="17.2" step="0.5">
          <span class="control-val" id="cliffVal">17.2 m</span>
        </div>
      `;

      document.getElementById('cliffSlider').addEventListener('input', (e) => {{
        const d = parseFloat(e.target.value);
        document.getElementById('cliffVal').textContent = `${{d}} m`;
        const v = 344;
        const time = ((2 * d) / v).toFixed(3);

        const x = 60 + d * 5;
        document.getElementById('cliffFace').setAttribute('points', `${{x}},60 ${{x + 20}},60 ${{x + 20}},210 ${{x}},210`);
        document.getElementById('echoDistLine').setAttribute('x2', x);
        document.getElementById('echoDistText').setAttribute('x', 60 + (d * 5) / 2);
        document.getElementById('echoDistText').textContent = `Distance: ${{d}} m`;

        const verdict = document.getElementById('echoVerdict');
        if (d >= 17.2) {{
          verdict.textContent = `Echo Heard Distinctly! (Time Delay = ${{time}} s ≥ 0.10 s)`;
          verdict.setAttribute('fill', '#10b981');
        }} else {{
          verdict.textContent = `No Echo! Sound blurs into original (Time = ${{time}} s &lt; 0.10 s)`;
          verdict.setAttribute('fill', '#ef4444');
        }}
      }});
    }}

    // 12. Auditorium Reverberation Simulator
    function renderAuditoriumSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="50" y="40" width="340" height="180" rx="8" fill="#1e293b" stroke="#334155" />
        <!-- Stage Speaker -->
        <circle cx="90" cy="130" r="14" fill="#38bdf8" />
        <!-- Audience -->
        <circle cx="340" cy="130" r="14" fill="#f59e0b" />
        <!-- Acoustic Panels on walls -->
        <rect id="panelTop" x="120" y="42" width="200" height="8" fill="#10b981" />
        <rect id="panelBottom" x="120" y="210" width="200" height="8" fill="#10b981" />
        <!-- Status -->
        <text id="reverbStatus" x="220" y="250" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Acoustic Panels ON: RT60 = 0.8 s (Speech is Crisp & Clear)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="togglePanels(true)">✅ Install Acoustic Curtains/Panels</button>
          <button class="sim-action-btn" onclick="togglePanels(false)">❌ Bare Concrete Walls (High Reverb)</button>
        </div>
      `;

      window.togglePanels = (on) => {{
        const pt = document.getElementById('panelTop');
        const pb = document.getElementById('panelBottom');
        const status = document.getElementById('reverbStatus');
        if (on) {{
          pt.setAttribute('fill', '#10b981');
          pb.setAttribute('fill', '#10b981');
          status.textContent = 'Acoustic Panels ON: RT60 = 0.8 s (Speech is Crisp & Clear)';
          status.setAttribute('fill', '#10b981');
        }} else {{
          pt.setAttribute('fill', '#475569');
          pb.setAttribute('fill', '#475569');
          status.textContent = 'Bare Walls: RT60 = 3.5 s (Excessive Reverberation Blur!)';
          status.setAttribute('fill', '#ef4444');
        }}
      }};
    }}

    // 13. Submarine SONAR Simulator
    function renderSonarSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Ocean Surface -->
        <line x1="20" y1="50" x2="420" y2="50" stroke="#38bdf8" stroke-width="3" />
        <!-- Ship Hull -->
        <polygon points="60,50 140,50 120,80 80,80" fill="#475569" stroke="#94a3b8" />
        <!-- Seabed -->
        <path d="M 20 220 Q 150 200 250 230 T 420 215 L 420 250 L 20 250 Z" fill="#78350f" />
        <!-- SONAR Beam -->
        <line id="sonarBeam" x1="100" y1="80" x2="100" y2="210" stroke="#00e5ff" stroke-width="4" stroke-dasharray="6" />
        <!-- Oscilloscope Box -->
        <rect x="220" y="70" width="180" height="90" rx="8" fill="#0f172a" stroke="#00e5ff" />
        <text x="310" y="95" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">SONAR Depth Scope</text>
        <text id="sonarEchoTime" x="310" y="120" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">Time Delay t = 2.0 s</text>
        <text id="sonarDepthCalc" x="310" y="145" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Depth d = 1,500 m</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Seabed Depth:</span>
          <input type="range" id="sonarSlider" min="500" max="3000" step="100" value="1500">
          <span class="control-val" id="sonarVal">1500 m</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="pingSonar()">📡 Send Ultrasonic Ping</button>
        </div>
      `;

      document.getElementById('sonarSlider').addEventListener('input', (e) => {{
        const d = parseFloat(e.target.value);
        document.getElementById('sonarVal').textContent = `${{d}} m`;
        const v = 1500;
        const t = ((2 * d) / v).toFixed(2);
        document.getElementById('sonarEchoTime').textContent = `Time Delay t = ${{t}} s`;
        document.getElementById('sonarDepthCalc').textContent = `Depth d = ${{d}} m`;
      }});

      window.pingSonar = () => {{
        const beam = document.getElementById('sonarBeam');
        beam.style.stroke = '#f59e0b';
        setTimeout(() => {{
          beam.style.stroke = '#00e5ff';
        }}, 400);
      }};
    }}

    // 14. Ultrasound Flaw Scanner
    function renderUltrasoundFlawSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Aluminum Block -->
        <rect x="80" y="80" width="280" height="110" rx="4" fill="#64748b" stroke="#cbd5e1" stroke-width="2" />
        <!-- Ultrasonic Transducer Probe -->
        <rect id="usProbe" x="140" y="55" width="40" height="25" rx="3" fill="#00e5ff" />
        <!-- Hidden Internal Crack -->
        <ellipse cx="220" cy="135" rx="15" ry="4" fill="#ef4444" />
        <text x="220" y="155" fill="#fca5a5" font-size="10" text-anchor="middle">Hidden Crack</text>
        <!-- Oscilloscope Waveform -->
        <text id="flawScopeText" x="220" y="240" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Scanning: Premature Reflection Echo Detected!</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Probe Position:</span>
          <input type="range" id="probePos" min="90" max="310" value="140">
          <span class="control-val" id="probeVal">140</span>
        </div>
      `;

      document.getElementById('probePos').addEventListener('input', (e) => {{
        const x = parseFloat(e.target.value);
        document.getElementById('probeVal').textContent = x;
        document.getElementById('usProbe').setAttribute('x', x);
        const status = document.getElementById('flawScopeText');
        if (Math.abs(x - 200) < 25) {{
          status.textContent = 'DEFECT FOUND! Crack Echo at depth 5.5 cm!';
          status.setAttribute('fill', '#ef4444');
        }} else {{
          status.textContent = 'Solid Metal: Clear Back-Wall Reflection Echo';
          status.setAttribute('fill', '#10b981');
        }}
      }});
    }}

    // 15. Dual Cliff Echo Simulator
    function renderDualCliffSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Cliff 1 (Left) -->
        <rect x="30" y="40" width="30" height="180" fill="#78350f" />
        <!-- Cliff 2 (Right) -->
        <rect x="380" y="40" width="30" height="180" fill="#78350f" />
        <!-- Shooter in middle -->
        <circle id="cliffShooter" cx="170" cy="180" r="10" fill="#00e5ff" />
        <line x1="60" y1="230" x2="380" y2="230" stroke="#f59e0b" stroke-width="2" />
        <text id="dualCliffStats" x="220" y="255" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Total Distance D = d1 + d2 = 340m + 510m = 850 m</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="fireDualShot()">🔫 Fire Pistol (Echo 1 at 2s, Echo 2 at 3s)</button>
        </div>
      `;

      window.fireDualShot = () => {{
        const s = document.getElementById('cliffShooter');
        s.setAttribute('fill', '#ef4444');
        setTimeout(() => {{
          s.setAttribute('fill', '#00e5ff');
        }}, 300);
      }};
    }}

    // 16. Gol Gumbaz Whispering Gallery Simulator
    function renderGolGumbazSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Circular Dome Perimeter -->
        <circle cx="220" cy="130" r="100" fill="none" stroke="#f59e0b" stroke-width="4" />
        <!-- Tangential multiple reflection path -->
        <polygon points="120,130 149,59 220,30 291,59 320,130 291,201 220,230 149,201" fill="none" stroke="#00e5ff" stroke-width="2" stroke-dasharray="4" />
        <!-- Speaker & Listener -->
        <circle cx="120" cy="130" r="8" fill="#10b981" />
        <text x="100" y="135" fill="#10b981" font-size="11" font-weight="bold">Whisper</text>
        <circle cx="320" cy="130" r="8" fill="#38bdf8" />
        <text x="340" y="135" fill="#38bdf8" font-size="11" font-weight="bold">Audible</text>
        <text x="220" y="255" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Gol Gumbaz Whispering Gallery (Claps echo 10+ times!)</text>
      `;

      controls.innerHTML = `
        <div style="font-size:0.85rem; color:#94a3b8; text-align:center;">
          Tangential reflections along the 44-metre circular dome carry faint whispers across the entire hall!
        </div>
      `;
    }}

    // Quiz Dashboard Sim (For Slides 17 to 20)
    function renderQuizDashboardSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="30" y="30" width="380" height="220" rx="12" fill="#0f172a" stroke="#334155" />
        <circle cx="220" cy="110" r="50" fill="rgba(0, 229, 255, 0.1)" stroke="#00e5ff" stroke-width="3" />
        <text x="220" y="105" fill="#00e5ff" font-size="28" font-weight="bold" text-anchor="middle">40</text>
        <text x="220" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">TOTAL QUESTIONS</text>
        <text x="220" y="195" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">Click 'View Solution' for Step-by-Step Derivations</text>
      `;
      controls.innerHTML = `
        <div style="text-align:center; font-size:0.85rem; color:#94a3b8;">
          All 40 questions feature complete mathematical workings and conceptual justifications.
        </div>
      `;
    }}
  </script>
</body>
</html>
'''

    output_path = 'public/animations/class9-sound.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated {output_path} ({len(html_content)} bytes).")

if __name__ == '__main__':
    build_html()

