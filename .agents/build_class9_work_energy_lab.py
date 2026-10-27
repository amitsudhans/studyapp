# -*- coding: utf-8 -*-
"""
Builder script to generate public/animations/class9-work-energy-simple-machines.html
Includes:
- Complete 20-slide interactive animated laboratory
- Voiceover teacher avatar (Prof. Sophia) with audio synthesis & mouth movement
- 16 bespoke interactive SVG simulators
- 32 in-slide checkpoints with teacher explanations
- 40 mastery quiz questions with step-by-step pop-up solution modal
- Strict Slide 20 last slide notice and next button hiding
"""

import json
from class9_work_energy_data import slides_data, quiz_questions

def build_html():
    slides_json = json.dumps(slides_data)
    quizzes_json = json.dumps(quiz_questions)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 9 Science • Chapter 11: Work, Energy and Simple Machines</title>
  
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
      margin: 16px auto;
      padding: 0 16px;
      display: grid;
      grid-template-columns: minmax(0, 1fr) 440px;
      gap: 20px;
      box-sizing: border-box;
      width: 100%;
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
      padding: 24px;
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

    .slide-body {{
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
    }}

    .highlight-eq {{
      background: rgba(0, 229, 255, 0.08);
      border: 1px solid rgba(0, 229, 255, 0.2);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 12px 0;
      text-align: center;
      color: #e0f2fe;
      font-size: 1.05rem;
      overflow-x: auto;
      max-width: 100%;
      box-sizing: border-box;
    }}

    .grid-2col {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
    }}

    .grid-3col {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-bottom: 20px;
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
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
      padding: 14px 16px;
      min-width: 0;
      box-sizing: border-box;
      overflow-x: auto;
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
      min-width: 0;
      box-sizing: border-box;
      width: 100%;
    }}

    .katex-display {{
      overflow-x: auto;
      overflow-y: hidden;
      max-width: 100%;
      padding: 4px 0;
      box-sizing: border-box;
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
      <span class="nav-title">Chapter 11: Work, Energy and Simple Machines</span>
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
        <div class="teacher-role">Senior Dynamics & Energy Guide</div>
        <div class="speech-bubble" id="teacherSpeech">
          Welcome to the Work, Energy and Simple Machines Laboratory!
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
      NCERT Science Class 9 • Chapter 11
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
        case 'work_vector_pull':
          title.textContent = '2D Force Vector Pull & Work Done (W = F·s·cos θ)';
          renderWorkVectorSim(svg, controls);
          break;
        case 'work_sign_angles':
          title.textContent = 'Positive, Zero, & Negative Work Regimes';
          renderWorkSignSim(svg, controls);
          break;
        case 'energy_transducer_chain':
          title.textContent = 'Energy Transformations & Transducer Chains';
          renderEnergyChainSim(svg, controls);
          break;
        case 'kinetic_energy_scaling':
          title.textContent = 'Kinetic Energy & Quadratic Velocity Scaling';
          renderKineticSim(svg, controls);
          break;
        case 'work_energy_braking':
          title.textContent = 'Work-Energy Theorem Braking Laboratory';
          renderWorkEnergyBrakingSim(svg, controls);
          break;
        case 'path_independence_ramp':
          title.textContent = 'Gravitational Potential Energy & Path Independence';
          renderPathIndependenceSim(svg, controls);
          break;
        case 'free_fall_energy_tower':
          title.textContent = 'Free Fall Energy Conversion & Invariance (E = K + U)';
          renderFreeFallTowerSim(svg, controls);
          break;
        case 'pendulum_energy_exchange':
          title.textContent = 'Simple Pendulum Mechanical Energy Oscillation';
          renderPendulumSim(svg, controls);
          break;
        case 'power_stair_climb':
          title.textContent = 'Rate of Doing Work: Stair Climb Power Comparator';
          renderPowerStairsSim(svg, controls);
          break;
        case 'electric_meter_bill':
          title.textContent = 'Commercial Energy Meter & kWh Cost Calculator';
          renderElectricMeterSim(svg, controls);
          break;
        case 'machine_ma_efficiency':
          title.textContent = 'Simple Machine MA, VR, and Efficiency Analyzer';
          renderMachineEfficiencySim(svg, controls);
          break;
        case 'lever_three_classes':
          title.textContent = 'Interactive 3-Class Lever & Principle of Moments';
          renderLeverSim(svg, controls);
          break;
        case 'inclined_plane_ramp':
          title.textContent = 'The Inclined Plane as a Force Multiplier (MA = L/h)';
          renderInclinedPlaneSim(svg, controls);
          break;
        case 'pulley_rig_system':
          title.textContent = 'Pulley Systems: Fixed, Movable, & Block and Tackle';
          renderPulleySim(svg, controls);
          break;
        case 'borewell_pump_calc':
          title.textContent = 'Agricultural Borewell Pump Power & Work Lab';
          renderBorewellSim(svg, controls);
          break;
        case 'thanjavur_ramp_sim':
          title.textContent = 'Ancient Thanjavur Megalithic Earth Ramp Lab';
          renderThanjavurRampSim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Mastery Challenge Dashboard';
          renderQuizDashboardSim(svg, controls);
      }}
    }}

    // 1. Work Vector Pull Simulator
    function renderWorkVectorSim(svg, controls) {{
      svg.innerHTML = `
        <defs>
          <marker id="forceArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#00e5ff" />
          </marker>
        </defs>
        <line x1="20" y1="210" x2="420" y2="210" stroke="#334155" stroke-width="4" />
        <!-- Crate -->
        <rect id="pullCrate" x="140" y="150" width="80" height="60" rx="6" fill="#3b82f6" stroke="#60a5fa" stroke-width="2" />
        <text x="180" y="185" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">10 kg</text>
        <!-- Horizontal Reference Dash Line -->
        <line x1="220" y1="180" x2="340" y2="180" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3" />
        <!-- Pull Rope & Vector -->
        <line id="pullVector" x1="220" y1="180" x2="310" y2="135" stroke="#00e5ff" stroke-width="4" marker-end="url(#forceArrow)" />
        <!-- Angle Arc -->
        <path id="angleArc" d="M 255 180 A 35 35 0 0 0 250 162" fill="none" stroke="#f59e0b" stroke-width="2" />
        <text id="angleLabel" x="268" y="170" fill="#f59e0b" font-size="12" font-weight="bold">θ = 30°</text>
        <!-- Real-time HUD -->
        <rect x="30" y="20" width="380" height="54" rx="8" fill="#0f172a" stroke="#00e5ff" stroke-width="1.5" />
        <text x="220" y="40" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle">WORK DONE: W = F · s · cos(θ)</text>
        <text id="workValueDisplay" x="220" y="62" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">W = 50 N × 5 m × cos(30°) = 216.5 J</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Pull Force (F):</span>
          <input type="range" id="fSlider" min="10" max="80" value="50">
          <span class="control-val" id="fVal">50 N</span>
        </div>
        <div class="control-row">
          <span>Pull Angle (θ):</span>
          <input type="range" id="thetaSlider" min="0" max="180" value="30">
          <span class="control-val" id="thetaVal">30°</span>
        </div>
        <div class="control-row">
          <span>Displacement (s):</span>
          <input type="range" id="sSlider" min="1" max="10" value="5">
          <span class="control-val" id="sVal">5 m</span>
        </div>
      `;

      function updateWork() {{
        const f = parseFloat(document.getElementById('fSlider').value);
        const thetaDeg = parseFloat(document.getElementById('thetaSlider').value);
        const s = parseFloat(document.getElementById('sSlider').value);

        document.getElementById('fVal').textContent = `${{f}} N`;
        document.getElementById('thetaVal').textContent = `${{thetaDeg}}°`;
        document.getElementById('sVal').textContent = `${{s}} m`;

        const thetaRad = (thetaDeg * Math.PI) / 180;
        const work = (f * s * Math.cos(thetaRad)).toFixed(1);

        document.getElementById('workValueDisplay').textContent = `W = ${{f}} N × ${{s}} m × cos(${{thetaDeg}}°) = ${{work}} J`;
        if (work > 0) document.getElementById('workValueDisplay').setAttribute('fill', '#10b981');
        else if (work < 0) document.getElementById('workValueDisplay').setAttribute('fill', '#ef4444');
        else document.getElementById('workValueDisplay').setAttribute('fill', '#f59e0b');

        // Update vector graphic
        const len = Math.min(100, Math.max(30, f * 1.3));
        const x2 = 220 + len * Math.cos(thetaRad);
        const y2 = 180 - len * Math.sin(thetaRad);
        document.getElementById('pullVector').setAttribute('x2', x2.toFixed(1));
        document.getElementById('pullVector').setAttribute('y2', y2.toFixed(1));
        document.getElementById('angleLabel').textContent = `θ = ${{thetaDeg}}°`;

        // Dynamic Arc
        if (thetaDeg > 2) {{
          const arcR = 36;
          const arcEndX = 220 + arcR * Math.cos(thetaRad);
          const arcEndY = 180 - arcR * Math.sin(thetaRad);
          const largeArc = thetaDeg > 180 ? 1 : 0;
          document.getElementById('angleArc').setAttribute('d', `M ${{220 + arcR}} 180 A ${{arcR}} ${{arcR}} 0 ${{largeArc}} 0 ${{arcEndX.toFixed(1)}} ${{arcEndY.toFixed(1)}}`);
          document.getElementById('angleArc').style.display = 'block';
          
          const labelR = 48;
          const labelX = 220 + labelR * Math.cos(thetaRad / 2);
          const labelY = 180 - labelR * Math.sin(thetaRad / 2);
          document.getElementById('angleLabel').setAttribute('x', labelX.toFixed(1));
          document.getElementById('angleLabel').setAttribute('y', (labelY - 2).toFixed(1));
        }} else {{
          document.getElementById('angleArc').style.display = 'none';
          document.getElementById('angleLabel').setAttribute('x', '265');
          document.getElementById('angleLabel').setAttribute('y', '175');
        }}
      }}

      document.getElementById('fSlider').addEventListener('input', updateWork);
      document.getElementById('thetaSlider').addEventListener('input', updateWork);
      document.getElementById('sSlider').addEventListener('input', updateWork);
      updateWork();
    }}

    // 2. Work Sign & Regimes Simulator
    function renderWorkSignSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="200" width="400" height="10" fill="#334155" />
        <!-- Scenario Visualizer Container -->
        <g id="scenarioG" transform="translate(0, 0)">
          <!-- Porter walking -->
          <circle cx="120" cy="110" r="14" fill="#fed7aa" />
          <line x1="120" y1="124" x2="120" y2="165" stroke="#3b82f6" stroke-width="4" />
          <line x1="120" y1="165" x2="110" y2="200" stroke="#3b82f6" stroke-width="3" />
          <line x1="120" y1="165" x2="130" y2="200" stroke="#3b82f6" stroke-width="3" />
          <!-- Luggage on head -->
          <rect x="95" y="80" width="50" height="20" rx="3" fill="#d97706" />
          <!-- Force upward arrow -->
          <line x1="120" y1="80" x2="120" y2="40" stroke="#00e5ff" stroke-width="4" />
          <text x="120" y="32" fill="#00e5ff" font-size="11" font-weight="bold" text-anchor="middle">N (Upward)</text>
          <!-- Horizontal displacement arrow -->
          <line x1="150" y1="150" x2="220" y2="150" stroke="#10b981" stroke-width="4" />
          <text x="185" y="142" fill="#10b981" font-size="11" font-weight="bold">s (Horizontal)</text>
          <text x="140" y="70" fill="#f59e0b" font-size="12" font-weight="bold">θ = 90° ⟹ W = 0 J</text>
        </g>
        <rect x="70" y="225" width="300" height="40" rx="6" fill="#1e293b" />
        <text id="scenarioStatus" x="220" y="250" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">Scenario: Porter Walking Horizontally (W = 0)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setScenario('positive')">⬆ Lifting Crate (W > 0)</button>
          <button class="sim-action-btn" onclick="setScenario('zero')">🚶 Porter Walking (W = 0)</button>
          <button class="sim-action-btn" onclick="setScenario('negative')">🛑 Friction Braking (W < 0)</button>
        </div>
      `;

      window.setScenario = (mode) => {{
        const status = document.getElementById('scenarioStatus');
        if (mode === 'positive') {{
          status.textContent = 'Positive Work: Force & Displacement parallel (θ = 0°, W = +mgh)';
          status.setAttribute('fill', '#10b981');
        }} else if (mode === 'zero') {{
          status.textContent = 'Zero Work: Force ⟂ Displacement (θ = 90°, cos 90° = 0)';
          status.setAttribute('fill', '#00e5ff');
        }} else {{
          status.textContent = 'Negative Work: Friction opposes displacement (θ = 180°, W = -fs)';
          status.setAttribute('fill', '#ef4444');
        }}
      }};
    }}

    // 3. Energy Chain Transformer
    function renderEnergyChainSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Source -->
        <rect x="30" y="80" width="90" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
        <circle id="sourceIcon" cx="75" cy="115" r="22" fill="#f59e0b" />
        <text id="sourceName" x="75" y="155" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Solar Energy</text>

        <!-- Arrow 1 -->
        <line x1="125" y1="125" x2="165" y2="125" stroke="#94a3b8" stroke-width="3" />

        <!-- Transducer -->
        <rect x="170" y="80" width="100" height="90" rx="8" fill="#1e293b" stroke="#00e5ff" stroke-width="2" />
        <rect cx="185" cy="95" x="185" y="95" width="70" height="40" rx="4" fill="#0284c7" />
        <text id="transName" x="220" y="155" fill="#00e5ff" font-size="11" font-weight="bold" text-anchor="middle">Solar Cell</text>

        <!-- Arrow 2 -->
        <line x1="275" y1="125" x2="315" y2="125" stroke="#94a3b8" stroke-width="3" />

        <!-- Load -->
        <rect x="320" y="80" width="90" height="90" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2" />
        <circle id="loadIcon" cx="365" cy="115" r="20" fill="#e2e8f0" />
        <text id="loadName" x="365" y="155" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Fan (Mech)</text>

        <!-- Energy Formula Output -->
        <text id="chainFormula" x="220" y="230" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Solar Radiant Energy ➡ Electrical Energy ➡ Mechanical Energy</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setChain('solar')">☀️ Solar ➡ Cell ➡ Fan</button>
          <button class="sim-action-btn" onclick="setChain('hydro')">💧 Hydro ➡ Turbine ➡ Light</button>
          <button class="sim-action-btn" onclick="setChain('wind')">💨 Wind ➡ Generator ➡ Heat</button>
        </div>
      `;

      window.setChain = (type) => {{
        if (type === 'solar') {{
          document.getElementById('sourceIcon').setAttribute('fill', '#f59e0b');
          document.getElementById('sourceName').textContent = 'Solar Radiant';
          document.getElementById('transName').textContent = 'Solar Cell';
          document.getElementById('loadName').textContent = 'Fan (Mech)';
          document.getElementById('chainFormula').textContent = 'Solar Radiant Energy ➡ Electrical Energy ➡ Mechanical Motion';
        }} else if (type === 'hydro') {{
          document.getElementById('sourceIcon').setAttribute('fill', '#38bdf8');
          document.getElementById('sourceName').textContent = 'Gravitational PE';
          document.getElementById('transName').textContent = 'Water Turbine';
          document.getElementById('loadName').textContent = 'Electric Bulb';
          document.getElementById('chainFormula').textContent = 'Gravitational PE ➡ Turbine Kinetic ➡ Electrical ➡ Light & Heat';
        }} else {{
          document.getElementById('sourceIcon').setAttribute('fill', '#a7f3d0');
          document.getElementById('sourceName').textContent = 'Wind Kinetic';
          document.getElementById('transName').textContent = 'Turbine Gen';
          document.getElementById('loadName').textContent = 'Electric Heater';
          document.getElementById('chainFormula').textContent = 'Wind Kinetic Energy ➡ Electrical Energy ➡ Thermal Heat';
        }}
      }};
    }}

    // 4. Kinetic Energy Scaling
    function renderKineticSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="190" width="400" height="10" fill="#334155" />
        <!-- Clay block target -->
        <rect x="330" y="110" width="70" height="80" rx="4" fill="#78350f" stroke="#b45309" stroke-width="2" />
        <text x="365" y="155" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Clay Target</text>
        <!-- Penetration mark -->
        <rect id="penetrationSlot" x="330" y="145" width="10" height="10" fill="#ef4444" />
        <!-- Moving Projectile -->
        <rect id="keProjectile" x="50" y="135" width="40" height="30" rx="4" fill="#00e5ff" />
        <text id="keLabel" x="70" y="155" fill="#042f2e" font-size="11" font-weight="bold" text-anchor="middle">2 kg</text>
        <!-- Energy HUD -->
        <rect x="80" y="30" width="280" height="50" rx="8" fill="#0f172a" stroke="#00e5ff" />
        <text x="220" y="50" fill="#94a3b8" font-size="11" text-anchor="middle">KINETIC ENERGY: K = ½ m v²</text>
        <text id="keValueDisplay" x="220" y="70" fill="#00e5ff" font-size="16" font-weight="bold" text-anchor="middle">K = 100.0 J | Depth = 1.0 cm</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Speed (v):</span>
          <input type="range" id="keVSlider" min="5" max="30" value="10">
          <span class="control-val" id="keVVal">10 m/s</span>
        </div>
        <div class="control-row">
          <span>Mass (m):</span>
          <input type="range" id="keMSlider" min="1" max="10" value="2">
          <span class="control-val" id="keMVal">2 kg</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="fireKeProjectile()">🎯 Fire into Clay Block</button>
        </div>
      `;

      function updateKE() {{
        const v = parseFloat(document.getElementById('keVSlider').value);
        const m = parseFloat(document.getElementById('keMSlider').value);
        document.getElementById('keVVal').textContent = `${{v}} m/s`;
        document.getElementById('keMVal').textContent = `${{m}} kg`;
        document.getElementById('keLabel').textContent = `${{m}} kg`;

        const ke = 0.5 * m * v * v;
        const depth = (ke / 100).toFixed(1); // proportional
        document.getElementById('keValueDisplay').textContent = `K = ${{ke.toFixed(1)}} J | Depth = ${{depth}} cm`;
        document.getElementById('penetrationSlot').setAttribute('width', Math.min(60, depth * 8));
      }}

      document.getElementById('keVSlider').addEventListener('input', updateKE);
      document.getElementById('keMSlider').addEventListener('input', updateKE);

      window.fireKeProjectile = () => {{
        const p = document.getElementById('keProjectile');
        p.style.transition = 'transform 0.3s cubic-bezier(.4,0,.2,1)';
        p.style.transform = 'translateX(240px)';
        setTimeout(() => {{
          p.style.transform = 'none';
        }}, 1200);
      }};
      updateKE();
    }}

    // 5. Work-Energy Braking Simulator
    function renderWorkEnergyBrakingSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="190" width="400" height="10" fill="#334155" />
        <!-- Skidding Car -->
        <g id="brakingCar" transform="translate(0, 0)">
          <rect x="50" y="145" width="70" height="35" rx="6" fill="#3b82f6" />
          <circle cx="65" cy="180" r="7" fill="#64748b" />
          <circle cx="105" cy="180" r="7" fill="#64748b" />
          <text x="85" y="167" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Car</text>
        </g>
        <!-- Braking Distance Mark -->
        <line id="stoppingLine" x1="50" y1="215" x2="250" y2="215" stroke="#ef4444" stroke-width="4" />
        <text id="stopText" x="150" y="235" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Braking Distance: 25.0 m</text>
        <!-- HUD -->
        <rect x="60" y="30" width="320" height="50" rx="8" fill="#0f172a" stroke="#10b981" />
        <text x="220" y="50" fill="#94a3b8" font-size="11" text-anchor="middle">W_net = ΔK = 0 - ½ m u² ⟹ d ∝ u²</text>
        <text id="brakeCalcText" x="220" y="70" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">u = 20 m/s ⟹ Initial K = 200 kJ</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Initial Speed (u):</span>
          <input type="range" id="speedU" min="10" max="40" value="20">
          <span class="control-val" id="speedVal">20 m/s</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="animateBrake()">🛑 Slam Brakes!</button>
        </div>
      `;

      function updateBrake() {{
        const u = parseFloat(document.getElementById('speedU').value);
        document.getElementById('speedVal').textContent = `${{u}} m/s`;
        const m = 1000;
        const fb = 4000; // 4000 N brake force
        const d = (0.5 * m * u * u / fb).toFixed(1);
        const ke = (0.5 * m * u * u / 1000).toFixed(0);

        document.getElementById('stopText').textContent = `Braking Distance: ${{d}} m`;
        document.getElementById('stoppingLine').setAttribute('x2', 50 + d * 3.5);
        document.getElementById('brakeCalcText').textContent = `u = ${{u}} m/s ⟹ Initial K = ${{ke}} kJ`;
      }}

      document.getElementById('speedU').addEventListener('input', updateBrake);

      window.animateBrake = () => {{
        const u = parseFloat(document.getElementById('speedU').value);
        const car = document.getElementById('brakingCar');
        const m = 1000;
        const fb = 4000;
        const d = (0.5 * m * u * u / fb);
        car.style.transition = 'transform 1s cubic-bezier(.1,.7,1,.1)';
        car.style.transform = `translateX(${{d * 3.5}}px)`;
        setTimeout(() => {{
          car.style.transform = 'none';
        }}, 2000);
      }};
      updateBrake();
    }}

    // 6. Path Independence Simulator
    function renderPathIndependenceSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Reference Ground -->
        <line x1="20" y1="220" x2="420" y2="220" stroke="#334155" stroke-width="3" />
        <!-- Top Platform (Height h = 120px) -->
        <rect x="300" y="70" width="120" height="15" fill="#475569" />
        <line x1="30" y1="70" x2="420" y2="70" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4" />
        <text x="360" y="60" fill="#f59e0b" font-size="11" font-weight="bold">Height h = 10 m</text>
        
        <!-- Path 1: Straight Vertical -->
        <line x1="80" y1="220" x2="80" y2="70" stroke="#00e5ff" stroke-width="3" />
        <text x="80" y="240" fill="#00e5ff" font-size="11" text-anchor="middle">Path 1: Vertical</text>

        <!-- Path 2: Ramp -->
        <line x1="140" y1="220" x2="300" y2="70" stroke="#10b981" stroke-width="3" />
        <text x="210" y="240" fill="#10b981" font-size="11" text-anchor="middle">Path 2: Ramp</text>

        <!-- Test Mass -->
        <circle id="pathMass" cx="80" cy="210" r="12" fill="#38bdf8" />
        
        <!-- Output HUD -->
        <text id="pathHud" x="220" y="35" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Work Done along any path: W = mgh = 490 J</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="animatePath(1)">Path 1: Direct Vertical Lift</button>
          <button class="sim-action-btn" onclick="animatePath(2)">Path 2: Gentle Inclined Ramp</button>
        </div>
      `;

      window.animatePath = (p) => {{
        const mass = document.getElementById('pathMass');
        if (p === 1) {{
          mass.style.transition = 'transform 1s ease-in-out';
          mass.style.transform = 'translateY(-140px)';
        }} else {{
          mass.style.transition = 'transform 1.5s ease-in-out';
          mass.style.transform = 'translate(160px, -140px)';
        }}
        setTimeout(() => {{
          mass.style.transform = 'none';
        }}, 2500);
      }};
    }}

    // 7. Free Fall Energy Tower
    function renderFreeFallTowerSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Tower Height Scale -->
        <line x1="60" y1="40" x2="60" y2="240" stroke="#64748b" stroke-width="3" />
        <circle id="freeBall" cx="60" cy="40" r="12" fill="#38bdf8" />
        <text x="90" y="45" fill="#94a3b8" font-size="11">Height H = 20 m</text>
        <text x="90" y="245" fill="#94a3b8" font-size="11">Ground (h = 0)</text>

        <!-- Dynamic Energy Bar Graph -->
        <rect x="220" y="40" width="40" height="180" fill="#1e293b" rx="4" />
        <rect id="peBar" x="220" y="40" width="40" height="180" fill="#f59e0b" rx="4" />
        <text x="240" y="235" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">PE (U)</text>

        <rect x="290" y="40" width="40" height="180" fill="#1e293b" rx="4" />
        <rect id="keBar" x="290" y="220" width="40" height="0" fill="#00e5ff" rx="4" />
        <text x="310" y="235" fill="#00e5ff" font-size="11" font-weight="bold" text-anchor="middle">KE (K)</text>

        <!-- Total Energy Banner -->
        <rect x="360" y="40" width="40" height="180" fill="#10b981" rx="4" />
        <text x="380" y="235" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Total E</text>

        <!-- Values Display -->
        <text id="peValText" x="240" y="32" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">400 J</text>
        <text id="keValText" x="310" y="32" fill="#00e5ff" font-size="11" font-weight="bold" text-anchor="middle">0 J</text>
        <text id="totValText" x="380" y="32" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">400 J</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Drop Height Position:</span>
          <input type="range" id="fallSlider" min="0" max="100" value="0">
          <span class="control-val" id="fallVal">0%</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="animateFreeFall()">▶ Drop Ball</button>
        </div>
      `;

      function updateFreeFall(pct) {{
        document.getElementById('fallVal').textContent = `${{pct}}%`;
        const y = 40 + (pct / 100) * 190;
        document.getElementById('freeBall').setAttribute('cy', y);

        const totalE = 400;
        const pe = totalE * (1 - pct / 100);
        const ke = totalE * (pct / 100);

        const peH = (pe / totalE) * 180;
        document.getElementById('peBar').setAttribute('height', peH);
        document.getElementById('peBar').setAttribute('y', 220 - peH);
        document.getElementById('peValText').textContent = `${{pe.toFixed(0)}} J`;

        const keH = (ke / totalE) * 180;
        document.getElementById('keBar').setAttribute('height', keH);
        document.getElementById('keBar').setAttribute('y', 220 - keH);
        document.getElementById('keValText').textContent = `${{ke.toFixed(0)}} J`;
      }}

      document.getElementById('fallSlider').addEventListener('input', (e) => {{
        updateFreeFall(parseFloat(e.target.value));
      }});

      window.animateFreeFall = () => {{
        let p = 0;
        const interval = setInterval(() => {{
          p += 2;
          if (p <= 100) {{
            document.getElementById('fallSlider').value = p;
            updateFreeFall(p);
          }} else {{
            clearInterval(interval);
          }}
        }}, 20);
      }};
    }}

    // 8. Pendulum Simulator
    function renderPendulumSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Pivot Point -->
        <circle cx="220" cy="40" r="6" fill="#64748b" />
        <!-- String & Bob -->
        <g id="pendulumArm" transform="rotate(0, 220, 40)">
          <line x1="220" y1="40" x2="220" y2="180" stroke="#cbd5e1" stroke-width="2" />
          <circle cx="220" cy="180" r="16" fill="#38bdf8" />
        </g>
        <text id="pendulumState" x="220" y="235" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Center: Maximum Kinetic Energy (U = 0)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="swingPendulum()">🔄 Start Oscillation</button>
          <button class="sim-action-btn" onclick="stopPendulum()">⏹ Halt</button>
        </div>
      `;

      let pendInterval = null;
      window.swingPendulum = () => {{
        if (pendInterval) clearInterval(pendInterval);
        const arm = document.getElementById('pendulumArm');
        const state = document.getElementById('pendulumState');
        let angle = 0;
        let t = 0;
        pendInterval = setInterval(() => {{
          t += 0.05;
          angle = 45 * Math.sin(t * 3);
          arm.setAttribute('transform', `rotate(${{angle}}, 220, 40)`);
          if (Math.abs(angle) > 40) {{
            state.textContent = 'Extreme Arc: All Potential Energy (K = 0)';
            state.setAttribute('fill', '#f59e0b');
          }} else if (Math.abs(angle) < 10) {{
            state.textContent = 'Mean Center: Maximum Kinetic Energy (U = min)';
            state.setAttribute('fill', '#10b981');
          }}
        }}, 30);
      }};

      window.stopPendulum = () => {{
        if (pendInterval) clearInterval(pendInterval);
        document.getElementById('pendulumArm').setAttribute('transform', 'rotate(0, 220, 40)');
      }};
    }}

    // 9. Power Stairs Simulator
    function renderPowerStairsSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Stairs Profile -->
        <path d="M 50 220 L 100 220 L 100 180 L 150 180 L 150 140 L 200 140 L 200 100 L 250 100" fill="none" stroke="#64748b" stroke-width="4" />
        <!-- Climber A -->
        <circle id="climberA" cx="75" cy="205" r="10" fill="#00e5ff" />
        <text x="75" y="190" fill="#00e5ff" font-size="10" font-weight="bold" text-anchor="middle">A</text>
        <!-- Climber B -->
        <circle id="climberB" cx="75" cy="205" r="10" fill="#f59e0b" />
        <text x="75" y="190" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">B</text>
        <!-- Output HUD -->
        <rect x="270" y="70" width="150" height="90" rx="8" fill="#1e293b" />
        <text x="345" y="95" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Power Output</text>
        <text id="pClimbA" x="345" y="120" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">Climber A: 500 W</text>
        <text id="pClimbB" x="345" y="145" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">Climber B: 250 W</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Climber A Time:</span>
          <input type="range" id="timeA" min="5" max="30" value="10">
          <span class="control-val" id="timeAVal">10 s</span>
        </div>
        <div class="control-row">
          <span>Climber B Time:</span>
          <input type="range" id="timeB" min="10" max="60" value="20">
          <span class="control-val" id="timeBVal">20 s</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="raceClimbers()">🏃 Race to Summit!</button>
        </div>
      `;

      window.raceClimbers = () => {{
        const ta = parseFloat(document.getElementById('timeA').value);
        const tb = parseFloat(document.getElementById('timeB').value);

        const work = 50 * 10 * 10; // 5000 J
        const pa = (work / ta).toFixed(0);
        const pb = (work / tb).toFixed(0);

        document.getElementById('pClimbA').textContent = `Climber A: ${{pa}} W`;
        document.getElementById('pClimbB').textContent = `Climber B: ${{pb}} W`;

        const a = document.getElementById('climberA');
        const b = document.getElementById('climberB');

        a.style.transition = `transform ${{ta * 0.1}}s ease-out`;
        a.style.transform = 'translate(175px, -120px)';

        b.style.transition = `transform ${{tb * 0.1}}s ease-out`;
        b.style.transform = 'translate(175px, -120px)';

        setTimeout(() => {{
          a.style.transform = 'none';
          b.style.transform = 'none';
        }}, 3000);
      }};

      document.getElementById('timeA').addEventListener('input', (e) => {{
        document.getElementById('timeAVal').textContent = `${{e.target.value}} s`;
      }});
      document.getElementById('timeB').addEventListener('input', (e) => {{
        document.getElementById('timeBVal').textContent = `${{e.target.value}} s`;
      }});
    }}

    // 10. Commercial Meter Simulator
    function renderElectricMeterSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Electric Meter Casing -->
        <rect x="80" y="30" width="280" height="200" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <!-- Digital Counter -->
        <rect x="120" y="60" width="200" height="40" rx="6" fill="#0f172a" stroke="#475569" />
        <text id="meterDigits" x="220" y="87" fill="#00e5ff" font-size="20" font-family="monospace" font-weight="bold" text-anchor="middle">00245.5 kWh</text>
        <!-- Rotating Aluminium Disc -->
        <g id="meterDiscGroup" transform="translate(220, 150)">
          <ellipse cx="0" cy="0" rx="60" ry="15" fill="#64748b" stroke="#cbd5e1" stroke-width="2" />
          <line id="discMark" x1="-60" y1="0" x2="60" y2="0" stroke="#ef4444" stroke-width="3" />
        </g>
        <text id="liveLoadPower" x="220" y="200" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Active Load: 2500 Watts (2.5 kW)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Active Home Appliances:</span>
          <select id="loadPreset" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="500">Lighting + Fan (500 W)</option>
            <option value="1500" selected>Iron + TV (1500 W)</option>
            <option value="3500">Air Conditioner + Geyser (3500 W)</option>
          </select>
        </div>
      `;

      document.getElementById('loadPreset').addEventListener('change', (e) => {{
        const watts = e.target.value;
        document.getElementById('liveLoadPower').textContent = `Active Load: ${{watts}} Watts (${{watts / 1000}} kW)`;
      }});
    }}

    // 11. Machine Efficiency Simulator
    function renderMachineEfficiencySim(svg, controls) {{
      svg.innerHTML = `
        <rect x="50" y="30" width="340" height="150" rx="12" fill="#0f172a" stroke="#334155" />
        <text x="220" y="60" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Mechanical Efficiency (η)</text>
        <text id="effMA" x="120" y="100" fill="#00e5ff" font-size="13" font-weight="bold">MA = 3.2</text>
        <text id="effVR" x="220" y="100" fill="#f59e0b" font-size="13" font-weight="bold">VR = 4.0</text>
        <text id="effPercent" x="320" y="100" fill="#10b981" font-size="14" font-weight="bold">η = 80.0%</text>
        <!-- Bar representation -->
        <rect x="80" y="130" width="280" height="24" rx="6" fill="#1e293b" />
        <rect id="effBar" x="80" y="130" width="224" height="24" rx="6" fill="#10b981" />
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Load (L):</span>
          <input type="range" id="loadSlider" min="200" max="1000" value="480">
          <span class="control-val" id="loadVal">480 N</span>
        </div>
        <div class="control-row">
          <span>Effort (E):</span>
          <input type="range" id="effortSlider" min="50" max="300" value="150">
          <span class="control-val" id="effortVal">150 N</span>
        </div>
      `;

      function updateEff() {{
        const l = parseFloat(document.getElementById('loadSlider').value);
        const e = parseFloat(document.getElementById('effortSlider').value);
        document.getElementById('loadVal').textContent = `${{l}} N`;
        document.getElementById('effortVal').textContent = `${{e}} N`;

        const ma = (l / e).toFixed(2);
        const vr = 4.0;
        const eta = Math.min(100, (ma / vr) * 100).toFixed(1);

        document.getElementById('effMA').textContent = `MA = ${{ma}}`;
        document.getElementById('effVR').textContent = `VR = ${{vr}}`;
        document.getElementById('effPercent').textContent = `η = ${{eta}}%`;
        document.getElementById('effBar').setAttribute('width', (eta / 100) * 280);
      }}

      document.getElementById('loadSlider').addEventListener('input', updateEff);
      document.getElementById('effortSlider').addEventListener('input', updateEff);
    }}

    // 12. 3-Class Lever Simulator
    function renderLeverSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Fulcrum Triangle -->
        <polygon id="leverFulcrum" points="220,180 205,210 235,210" fill="#f59e0b" />
        <!-- Beam -->
        <rect id="leverBeam" x="40" y="172" width="360" height="12" rx="3" fill="#94a3b8" />
        <!-- Load Box -->
        <rect id="leverLoad" x="80" y="132" width="40" height="40" rx="4" fill="#3b82f6" />
        <text id="loadLabel" x="100" y="157" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">L</text>
        <!-- Effort Arrow -->
        <line id="leverEffort" x1="360" y1="130" x2="360" y2="170" stroke="#10b981" stroke-width="5" />
        <text id="effortLabel" x="360" y="120" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Effort</text>
        <!-- Lever Class Banner -->
        <text id="leverClassName" x="220" y="45" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Class 1 Lever: Fulcrum in Middle (FLE Rule)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setLeverClass(1)">Class 1 (Seesaw/Crowbar)</button>
          <button class="sim-action-btn" onclick="setLeverClass(2)">Class 2 (Wheelbarrow)</button>
          <button class="sim-action-btn" onclick="setLeverClass(3)">Class 3 (Tweezers/Arm)</button>
        </div>
      `;

      window.setLeverClass = (c) => {{
        const title = document.getElementById('leverClassName');
        const fulcrum = document.getElementById('leverFulcrum');
        const load = document.getElementById('leverLoad');
        const effort = document.getElementById('leverEffort');
        const effortLabel = document.getElementById('effortLabel');

        if (c === 1) {{
          title.textContent = 'Class 1: Fulcrum in the middle (MA can be > 1, = 1, or < 1)';
          fulcrum.setAttribute('points', '220,180 205,210 235,210');
          load.setAttribute('x', '80');
          effort.setAttribute('x1', '360');
          effort.setAttribute('x2', '360');
          effortLabel.setAttribute('x', '360');
        }} else if (c === 2) {{
          title.textContent = 'Class 2: Load in the middle (Always MA > 1, Force Multiplier)';
          fulcrum.setAttribute('points', '50,180 35,210 65,210');
          load.setAttribute('x', '200');
          effort.setAttribute('x1', '360');
          effort.setAttribute('x2', '360');
          effortLabel.setAttribute('x', '360');
        }} else {{
          title.textContent = 'Class 3: Effort in the middle (Always MA < 1, Speed Multiplier)';
          fulcrum.setAttribute('points', '50,180 35,210 65,210');
          load.setAttribute('x', '340');
          effort.setAttribute('x1', '200');
          effort.setAttribute('x2', '200');
          effortLabel.setAttribute('x', '200');
        }}
      }};
    }}

    // 13. Inclined Plane Simulator
    function renderInclinedPlaneSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Ground Line -->
        <line x1="40" y1="210" x2="380" y2="210" stroke="#334155" stroke-width="4" />
        <!-- Ramp Triangle -->
        <polygon id="rampPoly" points="60,210 360,210 360,110" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="3" />
        <text x="375" y="160" fill="#f59e0b" font-size="11" font-weight="bold">h = 2 m</text>
        <text x="200" y="140" fill="#00e5ff" font-size="11" font-weight="bold">L = 6 m</text>
        <!-- Crate on Ramp -->
        <rect id="rampCrate" x="160" y="150" width="36" height="26" rx="4" fill="#f59e0b" transform="rotate(-18, 160, 150)" />
        <!-- HUD -->
        <text id="rampMA" x="220" y="45" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">MA = L / h = 6.0 / 2.0 = 3.0 (Required Effort = Load / 3)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Ramp Length (L):</span>
          <input type="range" id="rampLen" min="3" max="10" value="6">
          <span class="control-val" id="rampLenVal">6 m</span>
        </div>
      `;

      document.getElementById('rampLen').addEventListener('input', (e) => {{
        const l = parseFloat(e.target.value);
        document.getElementById('rampLenVal').textContent = `${{l}} m`;
        const h = 2.0;
        const ma = (l / h).toFixed(1);
        document.getElementById('rampMA').textContent = `MA = L / h = ${{l}} / 2.0 = ${{ma}} (Effort = Load / ${{ma}})`;
      }});
    }}

    // 14. Pulley System Simulator
    function renderPulleySim(svg, controls) {{
      svg.innerHTML = `
        <!-- Ceiling -->
        <rect x="60" y="30" width="320" height="8" fill="#475569" />
        <!-- Fixed Pulley 1 -->
        <circle cx="160" cy="70" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="3" />
        <!-- Fixed Pulley 2 -->
        <circle cx="280" cy="70" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="3" />
        <!-- Movable Pulley -->
        <circle id="movPulley" cx="220" cy="160" r="22" fill="#1e293b" stroke="#10b981" stroke-width="3" />
        <!-- Load Hanging from Movable Pulley -->
        <rect id="pulleyLoad" x="200" y="195" width="40" height="30" rx="4" fill="#3b82f6" />
        <text x="220" y="215" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">400 N</text>
        <text id="pulleyText" x="220" y="260" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Block & Tackle: 4 Strands ⟹ Effort = 400 / 4 = 100 N</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setPulleyMode('fixed')">Fixed Pulley (MA = 1)</button>
          <button class="sim-action-btn" onclick="setPulleyMode('movable')">Movable Pulley (MA = 2)</button>
          <button class="sim-action-btn" onclick="setPulleyMode('block')">Block & Tackle (MA = 4)</button>
        </div>
      `;

      window.setPulleyMode = (m) => {{
        const txt = document.getElementById('pulleyText');
        if (m === 'fixed') {{
          txt.textContent = 'Single Fixed Pulley: Direction Inverter (MA = 1, Effort = 400 N)';
        }} else if (m === 'movable') {{
          txt.textContent = 'Single Movable Pulley: 2 Strands (MA = 2, Effort = 200 N)';
        }} else {{
          txt.textContent = 'Block & Tackle (4 Pulleys): MA = 4, Effort = 100 N!';
        }}
      }};
    }}

    // 15. Borewell Pump Simulator
    function renderBorewellSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Ground Level -->
        <line x1="20" y1="80" x2="420" y2="80" stroke="#10b981" stroke-width="4" />
        <text x="40" y="70" fill="#10b981" font-size="11" font-weight="bold">Ground Surface</text>
        <!-- Deep Borewell Pipe -->
        <rect x="180" y="80" width="20" height="160" fill="#0f172a" stroke="#475569" />
        <!-- Submersible Pump at bottom -->
        <rect x="175" y="210" width="30" height="30" rx="4" fill="#00e5ff" />
        <!-- Rising Water Column -->
        <rect x="184" y="80" width="12" height="130" fill="rgba(56, 189, 248, 0.6)" />
        <!-- HUD -->
        <rect x="230" y="100" width="180" height="110" rx="8" fill="#1e293b" />
        <text x="320" y="125" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Pump Power Stats</text>
        <text id="pumpHeadText" x="320" y="150" fill="#f59e0b" font-size="12" text-anchor="middle">Depth: 30 m</text>
        <text id="pumpPowerText" x="320" y="175" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">Power: 5.88 kW</text>
        <text id="pumpHpText" x="320" y="195" fill="#10b981" font-size="11" text-anchor="middle">(7.88 Horsepower)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Well Depth (h):</span>
          <input type="range" id="depthSlider" min="10" max="60" value="30">
          <span class="control-val" id="depthVal">30 m</span>
        </div>
      `;

      document.getElementById('depthSlider').addEventListener('input', (e) => {{
        const h = parseFloat(e.target.value);
        document.getElementById('depthVal').textContent = `${{h}} m`;
        const flowPerSec = 20; // 20 kg/s
        const pKw = (flowPerSec * 9.8 * h / 1000).toFixed(2);
        const hp = (pKw * 1000 / 746).toFixed(2);

        document.getElementById('pumpHeadText').textContent = `Depth: ${{h}} m`;
        document.getElementById('pumpPowerText').textContent = `Power: ${{pKw}} kW`;
        document.getElementById('pumpHpText').textContent = `(${{hp}} Horsepower)`;
      }});
    }}

    // 16. Thanjavur Giant Ramp Simulator
    function renderThanjavurRampSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Temple Tower Base -->
        <rect x="330" y="60" width="70" height="160" fill="#b45309" stroke="#d97706" />
        <polygon points="320,60 365,20 410,60" fill="#78350f" />
        <!-- Giant Earth Ramp (6 km scale) -->
        <polygon points="40,220 330,220 330,60" fill="rgba(217, 119, 6, 0.25)" stroke="#d97706" stroke-width="2" />
        <!-- 80-tonne Granite Kumbam Capstone -->
        <circle id="graniteCapstone" cx="120" cy="175" r="16" fill="#64748b" stroke="#cbd5e1" stroke-width="2" />
        <text x="120" y="180" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">80T</text>
        <text x="200" y="245" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">6-Kilometer Gradual Inclined Plane Earthen Ramp</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="haulStone()">🐘 Haul Stone to Summit</button>
        </div>
      `;

      window.haulStone = () => {{
        const stone = document.getElementById('graniteCapstone');
        stone.style.transition = 'transform 2.5s ease-in-out';
        stone.style.transform = 'translate(240px, -115px)';
        setTimeout(() => {{
          stone.style.transform = 'none';
        }}, 4000);
      }};
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

    output_path = 'public/animations/class9-work-energy-simple-machines.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated {output_path} ({len(html_content)} bytes).")

if __name__ == '__main__':
    build_html()

