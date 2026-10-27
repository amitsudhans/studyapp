# -*- coding: utf-8 -*-
"""
Builder script to generate public/animations/class9-force-and-laws-of-motion.html
Includes:
- Complete 20-slide interactive animated laboratory
- Voiceover teacher avatar (Prof. Sophia) with audio synthesis & mouth movement
- 16 bespoke interactive SVG simulators
- 32 in-slide checkpoints with teacher explanations
- 40 mastery quiz questions with step-by-step pop-up solution modal
- Strict Slide 20 last slide notice and next button hiding
"""

import json
from class9_force_laws_data import slides_data, quiz_questions

def build_html():
    slides_json = json.dumps(slides_data)
    quizzes_json = json.dumps(quiz_questions)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 9 Science • Chapter 10: Force and Laws of Motion</title>
  
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
      grid-template-columns: 1fr 480px;
      gap: 24px;
    }}

    @media (max-width: 1080px) {{
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
      min-height: 720px;
      display: flex;
      flex-direction: column;
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
      <span class="nav-title">Chapter 10: Force and Laws of Motion</span>
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
        <div class="teacher-role">Senior Dynamics & Mechanics Guide</div>
        <div class="speech-bubble" id="teacherSpeech">
          Welcome to the Force and Laws of Motion Laboratory!
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
      NCERT Science Class 9 • Chapter 10
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
        case 'force_vector':
          title.textContent = '2D Vector Tug & Net Force Manipulator';
          renderForceVectorSim(svg, controls);
          break;
        case 'balanced_tug_of_war':
          title.textContent = 'Balanced vs Unbalanced Forces Lab';
          renderBalancedTugSim(svg, controls);
          break;
        case 'friction_breakaway':
          title.textContent = 'Friction & Microscopic Asperities Lab';
          renderFrictionSim(svg, controls);
          break;
        case 'galileo_inclined_planes':
          title.textContent = "Galileo's Double Inclined Plane Lab";
          renderGalileoSim(svg, controls);
          break;
        case 'coin_card_flick':
          title.textContent = 'Inertia of Rest: Coin & Card Experiment';
          renderCoinCardSim(svg, controls);
          break;
        case 'mass_inertia_push':
          title.textContent = 'Mass as Quantitative Measure of Inertia';
          renderMassInertiaSim(svg, controls);
          break;
        case 'momentum_visualizer':
          title.textContent = 'Linear Momentum (p = mv) Comparator';
          renderMomentumSim(svg, controls);
          break;
        case 'newton_second_law_cart':
          title.textContent = "Newton's Second Law Dynamic Cart (F = ma)";
          renderSecondLawSim(svg, controls);
          break;
        case 'impulse_catcher':
          title.textContent = 'Impulse (J = F·Δt) & Cushioning Laboratory';
          renderImpulseSim(svg, controls);
          break;
        case 'spring_balance_pair':
          title.textContent = "Newton's Third Law: Paired Spring Balances";
          renderSpringBalanceSim(svg, controls);
          break;
        case 'rocket_propulsion':
          title.textContent = 'Newtonian Rocket Thrust & Action-Reaction';
          renderRocketSim(svg, controls);
          break;
        case 'collision_carts':
          title.textContent = 'Conservation of Linear Momentum Track';
          renderCollisionSim(svg, controls);
          break;
        case 'cannon_recoil':
          title.textContent = 'Firearm & Cannon Recoil Mechanics';
          renderCannonSim(svg, controls);
          break;
        case 'virtual_air_track':
          title.textContent = 'Linear Air Track & Photogate Verification';
          renderAirTrackSim(svg, controls);
          break;
        case 'elevator_scale':
          title.textContent = 'Apparent Weight inside an Elevator';
          renderElevatorSim(svg, controls);
          break;
        case 'fundamental_forces':
          title.textContent = 'The 4 Fundamental Forces & Relativity Limit';
          renderFundamentalForcesSim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Mastery Challenge Dashboard';
          renderQuizDashboardSim(svg, controls);
      }}
    }}

    // 1. Force Vector Simulator
    function renderForceVectorSim(svg, controls) {{
      svg.innerHTML = `
        <defs>
          <marker id="arrowhead1" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#00e5ff" />
          </marker>
          <marker id="arrowhead2" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#f59e0b" />
          </marker>
          <marker id="arrowheadNet" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
            <polygon points="0 0, 10 4, 0 8" fill="#10b981" />
          </marker>
        </defs>
        <line x1="220" y1="20" x2="220" y2="260" stroke="#1e293b" stroke-width="2" stroke-dasharray="4" />
        <line x1="20" y1="140" x2="420" y2="140" stroke="#1e293b" stroke-width="2" stroke-dasharray="4" />
        <!-- Origin mass -->
        <circle cx="220" cy="140" r="16" fill="#3b82f6" />
        <text x="220" y="145" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">m</text>
        <!-- Vector F1 -->
        <line id="vecF1" x1="220" y1="140" x2="320" y2="140" stroke="#00e5ff" stroke-width="4" marker-end="url(#arrowhead1)" />
        <text id="labelF1" x="325" y="135" fill="#00e5ff" font-size="12" font-weight="bold">F1 = 50 N</text>
        <!-- Vector F2 -->
        <line id="vecF2" x1="220" y1="140" x2="220" y2="60" stroke="#f59e0b" stroke-width="4" marker-end="url(#arrowhead2)" />
        <text id="labelF2" x="225" y="55" fill="#f59e0b" font-size="12" font-weight="bold">F2 = 40 N</text>
        <!-- Resultant Net Force -->
        <line id="vecNet" x1="220" y1="140" x2="320" y2="60" stroke="#10b981" stroke-width="5" marker-end="url(#arrowheadNet)" />
        <text id="labelNet" x="325" y="55" fill="#10b981" font-size="13" font-weight="bold">F_net = 64.0 N</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Horizontal Force F1 (East):</span>
          <input type="range" id="f1Slider" min="-80" max="80" value="50">
          <span class="control-val" id="f1Val">50 N</span>
        </div>
        <div class="control-row">
          <span>Vertical Force F2 (North):</span>
          <input type="range" id="f2Slider" min="-80" max="80" value="40">
          <span class="control-val" id="f2Val">40 N</span>
        </div>
      `;

      function updateVectors() {{
        const f1 = parseFloat(document.getElementById('f1Slider').value);
        const f2 = parseFloat(document.getElementById('f2Slider').value);

        document.getElementById('f1Val').textContent = `${{f1}} N`;
        document.getElementById('f2Val').textContent = `${{f2}} N`;

        const x1 = 220 + f1 * 1.8;
        const y1 = 140;
        document.getElementById('vecF1').setAttribute('x2', x1);
        document.getElementById('vecF1').setAttribute('y2', y1);
        document.getElementById('labelF1').setAttribute('x', x1 + (f1 >= 0 ? 8 : -60));
        document.getElementById('labelF1').setAttribute('y', y1 - 8);
        document.getElementById('labelF1').textContent = `F1 = ${{Math.abs(f1)}} N`;

        const x2 = 220;
        const y2 = 140 - f2 * 1.8;
        document.getElementById('vecF2').setAttribute('x2', x2);
        document.getElementById('vecF2').setAttribute('y2', y2);
        document.getElementById('labelF2').setAttribute('x', x2 + 8);
        document.getElementById('labelF2').setAttribute('y', y2 - 8);
        document.getElementById('labelF2').textContent = `F2 = ${{Math.abs(f2)}} N`;

        const xNet = 220 + f1 * 1.8;
        const yNet = 140 - f2 * 1.8;
        const fNetMag = Math.sqrt(f1 * f1 + f2 * f2).toFixed(1);
        document.getElementById('vecNet').setAttribute('x2', xNet);
        document.getElementById('vecNet').setAttribute('y2', yNet);
        document.getElementById('labelNet').setAttribute('x', xNet + 8);
        document.getElementById('labelNet').setAttribute('y', yNet - 8);
        document.getElementById('labelNet').textContent = `F_net = ${{fNetMag}} N`;
      }}

      document.getElementById('f1Slider').addEventListener('input', updateVectors);
      document.getElementById('f2Slider').addEventListener('input', updateVectors);
    }}

    // 2. Balanced vs Unbalanced Tug-of-War Simulator
    function renderBalancedTugSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="180" width="400" height="12" fill="#334155" />
        <!-- Block -->
        <rect id="tugBlock" x="180" y="120" width="80" height="60" rx="8" fill="#3b82f6" stroke="#60a5fa" stroke-width="2" />
        <text id="tugBlockText" x="220" y="155" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">5 kg</text>
        <!-- Pull Arrows -->
        <line id="arrowLeft" x1="180" y1="150" x2="100" y2="150" stroke="#f43f5e" stroke-width="6" />
        <line id="arrowRight" x1="260" y1="150" x2="340" y2="150" stroke="#10b981" stroke-width="6" />
        <!-- Force Badges -->
        <text id="textLeft" x="90" y="145" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="end">F_left: 50 N</text>
        <text id="textRight" x="350" y="145" fill="#10b981" font-size="13" font-weight="bold">F_right: 50 N</text>
        <!-- State Badge -->
        <rect x="130" y="30" width="180" height="32" rx="6" fill="#1e293b" stroke="#00e5ff" stroke-width="1.5" />
        <text id="balanceStatus" x="220" y="52" fill="#00e5ff" font-size="13" font-weight="bold" text-anchor="middle">BALANCED (ΣF = 0 N)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Left Team Force:</span>
          <input type="range" id="leftForce" min="0" max="100" value="50">
          <span class="control-val" id="leftVal">50 N</span>
        </div>
        <div class="control-row">
          <span>Right Team Force:</span>
          <input type="range" id="rightForce" min="0" max="100" value="50">
          <span class="control-val" id="rightVal">50 N</span>
        </div>
      `;

      let posX = 180;
      let animId = null;

      function updateTug() {{
        const fl = parseFloat(document.getElementById('leftForce').value);
        const fr = parseFloat(document.getElementById('rightForce').value);
        document.getElementById('leftVal').textContent = `${{fl}} N`;
        document.getElementById('rightVal').textContent = `${{fr}} N`;

        document.getElementById('arrowLeft').setAttribute('x2', 180 - fl * 1.2);
        document.getElementById('arrowRight').setAttribute('x2', 260 + fr * 1.2);
        document.getElementById('textLeft').textContent = `F_left: ${{fl}} N`;
        document.getElementById('textRight').textContent = `F_right: ${{fr}} N`;

        const net = fr - fl;
        const status = document.getElementById('balanceStatus');
        if (net === 0) {{
          status.textContent = 'BALANCED (ΣF = 0 N, a = 0)';
          status.setAttribute('fill', '#00e5ff');
        }} else if (net > 0) {{
          const a = (net / 5).toFixed(1);
          status.textContent = `UNBALANCED (Net: +${{net}} N ➡ a = ${{a}} m/s²)`;
          status.setAttribute('fill', '#10b981');
        }} else {{
          const a = (Math.abs(net) / 5).toFixed(1);
          status.textContent = `UNBALANCED (Net: -${{Math.abs(net)}} N ⬅ a = ${{a}} m/s²)`;
          status.setAttribute('fill', '#f43f5e');
        }}
      }}

      document.getElementById('leftForce').addEventListener('input', updateTug);
      document.getElementById('rightForce').addEventListener('input', updateTug);
    }}

    // 3. Friction Simulator
    function renderFrictionSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="190" width="400" height="20" fill="#334155" />
        <!-- Microscopic zoom circle -->
        <circle cx="90" cy="70" r="45" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
        <path d="M55 70 Q65 60 75 70 T95 70 T115 70 T125 70" fill="none" stroke="#60a5fa" stroke-width="3" />
        <path d="M55 72 Q65 82 75 72 T95 72 T115 72 T125 72" fill="none" stroke="#94a3b8" stroke-width="3" />
        <text x="90" y="125" fill="#38bdf8" font-size="10" text-anchor="middle">Microscopic Interlocking</text>
        <!-- Block -->
        <rect id="fricBlock" x="200" y="130" width="80" height="60" rx="6" fill="#d97706" />
        <text x="240" y="165" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">10 kg</text>
        <!-- Pull Force Arrow -->
        <line id="pullLine" x1="280" y1="160" x2="330" y2="160" stroke="#10b981" stroke-width="5" />
        <!-- Friction Arrow -->
        <line id="fricLine" x1="200" y1="160" x2="160" y2="160" stroke="#ef4444" stroke-width="5" />
        <text id="pullText" x="335" y="155" fill="#10b981" font-size="12" font-weight="bold">F_pull: 20 N</text>
        <text id="fricText" x="155" y="155" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="end">f_s: 20 N</text>
        <!-- Gauge -->
        <rect x="200" y="30" width="180" height="24" rx="4" fill="#1e293b" />
        <rect id="gaugeBar" x="200" y="30" width="60" height="24" rx="4" fill="#f59e0b" />
        <text id="gaugeText" x="290" y="47" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Static Limit: 39.2 N</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Applied Pull Force:</span>
          <input type="range" id="pullSlider" min="0" max="80" value="20">
          <span class="control-val" id="pullVal">20 N</span>
        </div>
        <div class="control-row">
          <span>Surface Material:</span>
          <select id="surfaceSelect" style="background:#1e293b; color:#fff; padding:4px 8px; border-radius:4px; border:1px solid #475569;">
            <option value="0.4" selected>Wood on Concrete (μ = 0.4)</option>
            <option value="0.1">Steel on Ice (μ = 0.1)</option>
            <option value="0.7">Rubber on Asphalt (μ = 0.7)</option>
          </select>
        </div>
      `;

      function updateFriction() {{
        const pull = parseFloat(document.getElementById('pullSlider').value);
        const mu = parseFloat(document.getElementById('surfaceSelect').value);
        const normal = 10 * 9.8;
        const fMax = (mu * normal).toFixed(1);

        document.getElementById('pullVal').textContent = `${{pull}} N`;
        document.getElementById('gaugeText').textContent = `Max Limit: ${{fMax}} N`;

        let fActual = 0;
        let isSliding = pull > fMax;

        if (!isSliding) {{
          fActual = pull;
          document.getElementById('fricText').textContent = `f_static: ${{fActual.toFixed(1)}} N`;
          document.getElementById('gaugeBar').setAttribute('width', Math.min(180, (pull / fMax) * 180));
          document.getElementById('gaugeBar').setAttribute('fill', '#f59e0b');
        }} else {{
          fActual = (mu * 0.8 * normal).toFixed(1); // kinetic slightly lower
          document.getElementById('fricText').textContent = `f_kinetic: ${{fActual}} N (SLIDING!)`;
          document.getElementById('gaugeBar').setAttribute('width', 180);
          document.getElementById('gaugeBar').setAttribute('fill', '#10b981');
        }}

        document.getElementById('pullLine').setAttribute('x2', 280 + pull * 1.5);
        document.getElementById('pullText').textContent = `F_pull: ${{pull}} N`;
        document.getElementById('pullText').setAttribute('x', 285 + pull * 1.5);

        document.getElementById('fricLine').setAttribute('x2', 200 - fActual * 1.5);
      }}

      document.getElementById('pullSlider').addEventListener('input', updateFriction);
      document.getElementById('surfaceSelect').addEventListener('change', updateFriction);
    }}

    // 4. Galileo Inclined Plane Simulator
    function renderGalileoSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Left Incline -->
        <line x1="40" y1="60" x2="180" y2="200" stroke="#64748b" stroke-width="4" />
        <!-- Horizontal Base -->
        <line x1="180" y1="200" x2="220" y2="200" stroke="#64748b" stroke-width="4" />
        <!-- Right Incline (Dynamic slope) -->
        <line id="rightIncline" x1="220" y1="200" x2="360" y2="60" stroke="#00e5ff" stroke-width="4" />
        <!-- Initial Release Height Line -->
        <line x1="30" y1="60" x2="410" y2="60" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4" />
        <text x="380" y="52" fill="#f59e0b" font-size="11">Initial Height (h)</text>
        <!-- Marble Ball -->
        <circle id="galileoBall" cx="40" cy="52" r="10" fill="#38bdf8" />
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Opposite Incline Angle:</span>
          <input type="range" id="rampAngle" min="0" max="60" value="45">
          <span class="control-val" id="angleVal">45°</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="animateGalileo()">▶ Release Marble</button>
          <button class="sim-action-btn" onclick="resetGalileo()">↺ Reset</button>
        </div>
      `;

      document.getElementById('rampAngle').addEventListener('input', (e) => {{
        const deg = parseFloat(e.target.value);
        document.getElementById('angleVal').textContent = `${{deg}}°`;
        if (deg === 0) {{
          document.getElementById('rightIncline').setAttribute('x2', 420);
          document.getElementById('rightIncline').setAttribute('y2', 200);
        }} else {{
          const rad = (deg * Math.PI) / 180;
          const deltaY = 140; // 200 - 60
          const deltaX = deltaY / Math.tan(rad);
          document.getElementById('rightIncline').setAttribute('x2', Math.min(420, 220 + deltaX));
          document.getElementById('rightIncline').setAttribute('y2', 60);
        }}
      }});

      window.animateGalileo = () => {{
        const ball = document.getElementById('galileoBall');
        const deg = parseFloat(document.getElementById('rampAngle').value);
        let t = 0;
        const interval = setInterval(() => {{
          t += 0.02;
          if (t <= 1) {{
            // Down first ramp
            const cx = 40 + t * 140;
            const cy = 52 + t * 140;
            ball.setAttribute('cx', cx);
            ball.setAttribute('cy', cy);
          }} else if (t <= 1.2) {{
            // Flat base
            const cx = 180 + (t - 1) * 200;
            ball.setAttribute('cx', Math.min(220, cx));
            ball.setAttribute('cy', 192);
          }} else if (t <= 2.2) {{
            // Up second ramp or horizontal forever
            if (deg === 0) {{
              const cx = 220 + (t - 1.2) * 200;
              ball.setAttribute('cx', cx);
              ball.setAttribute('cy', 192);
            }} else {{
              const progress = (t - 1.2);
              const x2 = parseFloat(document.getElementById('rightIncline').getAttribute('x2'));
              const cx = 220 + progress * (x2 - 220);
              const cy = 192 - progress * 140;
              ball.setAttribute('cx', cx);
              ball.setAttribute('cy', cy);
            }}
          }} else {{
            clearInterval(interval);
          }}
        }}, 20);
      }};

      window.resetGalileo = () => {{
        const ball = document.getElementById('galileoBall');
        ball.setAttribute('cx', 40);
        ball.setAttribute('cy', 52);
      }};
    }}

    // 5. Coin Card Flick Simulator
    function renderCoinCardSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Glass Tumbler -->
        <polygon points="170,120 180,220 260,220 270,120" fill="none" stroke="#38bdf8" stroke-width="3" />
        <!-- Index Card -->
        <rect id="flickCard" x="140" y="112" width="160" height="8" rx="2" fill="#f8fafc" />
        <!-- Five Rupee Coin -->
        <circle id="flickCoin" cx="220" cy="100" r="14" fill="#f59e0b" stroke="#b45309" stroke-width="2" />
        <text id="coinLabel" x="220" y="105" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">₹5</text>
        <text x="220" y="250" fill="#94a3b8" font-size="11" text-anchor="middle">Glass Tumbler</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="flickCardRapidly()">⚡ Rapid Flick (Inertia of Rest)</button>
          <button class="sim-action-btn" onclick="flickCardSlowly()">🐢 Slow Pull (Frictional Drag)</button>
          <button class="sim-action-btn" onclick="resetCoinCard()">↺ Reset</button>
        </div>
      `;

      window.flickCardRapidly = () => {{
        const card = document.getElementById('flickCard');
        const coin = document.getElementById('flickCoin');
        const label = document.getElementById('coinLabel');

        // Card accelerates away to right
        card.style.transition = 'transform 0.15s ease-out';
        card.style.transform = 'translateX(240px)';

        // Coin drops straight down due to inertia of rest
        setTimeout(() => {{
          coin.style.transition = 'transform 0.35s cubic-bezier(.5,0,1,1)';
          coin.style.transform = 'translateY(110px)';
          label.style.transition = 'transform 0.35s cubic-bezier(.5,0,1,1)';
          label.style.transform = 'translateY(110px)';
        }}, 100);
      }};

      window.flickCardSlowly = () => {{
        const card = document.getElementById('flickCard');
        const coin = document.getElementById('flickCoin');
        const label = document.getElementById('coinLabel');

        // Both move together due to static friction
        card.style.transition = 'transform 1s ease-in-out';
        card.style.transform = 'translateX(100px)';
        coin.style.transition = 'transform 1s ease-in-out';
        coin.style.transform = 'translateX(100px)';
        label.style.transition = 'transform 1s ease-in-out';
        label.style.transform = 'translateX(100px)';
      }};

      window.resetCoinCard = () => {{
        const card = document.getElementById('flickCard');
        const coin = document.getElementById('flickCoin');
        const label = document.getElementById('coinLabel');
        card.style.transform = 'none';
        coin.style.transform = 'none';
        label.style.transform = 'none';
      }};
    }}

    // 6. Mass Inertia Push Simulator
    function renderMassInertiaSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Track 1: Light Mass -->
        <rect x="20" y="80" width="400" height="6" fill="#334155" />
        <rect id="cartLight" x="40" y="46" width="40" height="34" rx="4" fill="#00e5ff" />
        <text x="60" y="68" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">1 kg</text>
        <text id="accLight" x="380" y="40" fill="#00e5ff" font-size="12" font-weight="bold" text-anchor="end">a = 20 m/s²</text>

        <!-- Track 2: Heavy Mass -->
        <rect x="20" y="200" width="400" height="6" fill="#334155" />
        <rect id="cartHeavy" x="40" y="150" width="80" height="50" rx="4" fill="#ec4899" />
        <text x="80" y="180" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">10 kg</text>
        <text id="accHeavy" x="380" y="150" fill="#ec4899" font-size="12" font-weight="bold" text-anchor="end">a = 2 m/s²</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Pushing Force Applied to Both:</span>
          <input type="range" id="pushForce" min="5" max="50" value="20">
          <span class="control-val" id="pushVal">20 N</span>
        </div>
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="triggerPusher()">▶ Apply Equal Push Force</button>
        </div>
      `;

      window.triggerPusher = () => {{
        const f = parseFloat(document.getElementById('pushForce').value);
        const a1 = (f / 1).toFixed(1);
        const a2 = (f / 10).toFixed(1);

        document.getElementById('accLight').textContent = `a = ${{a1}} m/s²`;
        document.getElementById('accHeavy').textContent = `a = ${{a2}} m/s²`;

        const c1 = document.getElementById('cartLight');
        const c2 = document.getElementById('cartHeavy');

        c1.style.transition = 'transform 0.4s ease-out';
        c1.style.transform = 'translateX(300px)';

        c2.style.transition = 'transform 1.5s ease-out';
        c2.style.transform = 'translateX(100px)';

        setTimeout(() => {{
          c1.style.transform = 'none';
          c2.style.transform = 'none';
        }}, 2000);
      }};

      document.getElementById('pushForce').addEventListener('input', (e) => {{
        document.getElementById('pushVal').textContent = `${{e.target.value}} N`;
      }});
    }}

    // 7. Momentum Visualizer
    function renderMomentumSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="30" width="400" height="100" rx="8" fill="#1e293b" />
        <rect x="20" y="150" width="400" height="100" rx="8" fill="#1e293b" />
        <!-- Object 1 -->
        <text x="35" y="55" fill="#38bdf8" font-size="12" font-weight="bold">Object 1 (Bullet / Sports Ball)</text>
        <circle id="obj1" cx="60" cy="90" r="15" fill="#38bdf8" />
        <line id="pLine1" x1="60" y1="90" x2="160" y2="90" stroke="#00e5ff" stroke-width="4" />
        <text id="pText1" x="170" y="94" fill="#00e5ff" font-size="12" font-weight="bold">p = 20 kg·m/s</text>

        <!-- Object 2 -->
        <text x="35" y="175" fill="#f59e0b" font-size="12" font-weight="bold">Object 2 (Loaded Truck / Boulder)</text>
        <rect id="obj2" x="45" y="195" width="40" height="30" rx="4" fill="#f59e0b" />
        <line id="pLine2" x1="85" y1="210" x2="285" y2="210" stroke="#f59e0b" stroke-width="6" />
        <text id="pText2" x="295" y="214" fill="#f59e0b" font-size="12" font-weight="bold">p = 80 kg·m/s</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Obj 1 Velocity:</span>
          <input type="range" id="v1Slider" min="1" max="100" value="40">
          <span class="control-val" id="v1Val">40 m/s</span>
        </div>
        <div class="control-row">
          <span>Obj 2 Mass:</span>
          <input type="range" id="m2Slider" min="1" max="50" value="20">
          <span class="control-val" id="m2Val">20 kg</span>
        </div>
      `;

      function updateMomentum() {{
        const v1 = parseFloat(document.getElementById('v1Slider').value);
        const m1 = 0.5; // fixed 0.5 kg
        const p1 = (m1 * v1).toFixed(1);

        const m2 = parseFloat(document.getElementById('m2Slider').value);
        const v2 = 4; // fixed 4 m/s
        const p2 = (m2 * v2).toFixed(1);

        document.getElementById('v1Val').textContent = `${{v1}} m/s`;
        document.getElementById('m2Val').textContent = `${{m2}} kg`;

        document.getElementById('pLine1').setAttribute('x2', 60 + p1 * 3);
        document.getElementById('pText1').setAttribute('x', 65 + p1 * 3);
        document.getElementById('pText1').textContent = `p = ${{p1}} kg·m/s`;

        document.getElementById('pLine2').setAttribute('x2', 85 + p2 * 2.5);
        document.getElementById('pText2').setAttribute('x', 90 + p2 * 2.5);
        document.getElementById('pText2').textContent = `p = ${{p2}} kg·m/s`;
      }}

      document.getElementById('v1Slider').addEventListener('input', updateMomentum);
      document.getElementById('m2Slider').addEventListener('input', updateMomentum);
    }}

    // 8. Newton's Second Law Simulator
    function renderSecondLawSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="190" width="400" height="10" fill="#334155" />
        <!-- Cart on Air Track -->
        <rect id="cartFMA" x="80" y="130" width="90" height="60" rx="8" fill="#10b981" />
        <circle cx="100" cy="190" r="8" fill="#64748b" />
        <circle cx="150" cy="190" r="8" fill="#64748b" />
        <text id="cartLabel" x="125" y="165" fill="#042f2e" font-size="14" font-weight="bold" text-anchor="middle">m = 5 kg</text>
        <!-- Pull Force Cord -->
        <line id="fLine" x1="170" y1="160" x2="260" y2="160" stroke="#f59e0b" stroke-width="4" />
        <text id="fText" x="270" y="165" fill="#f59e0b" font-size="13" font-weight="bold">F = 25 N</text>
        <!-- Real-time HUD -->
        <rect x="120" y="30" width="200" height="50" rx="8" fill="#0f172a" stroke="#10b981" />
        <text x="220" y="52" fill="#94a3b8" font-size="11" text-anchor="middle">ACCELERATION (a = F / m)</text>
        <text id="accDisplay" x="220" y="72" fill="#10b981" font-size="18" font-weight="bold" text-anchor="middle">5.00 m/s²</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Unbalanced Force (F):</span>
          <input type="range" id="forceF" min="5" max="60" value="25">
          <span class="control-val" id="forceVal">25 N</span>
        </div>
        <div class="control-row">
          <span>Cart Mass (m):</span>
          <input type="range" id="massM" min="1" max="15" value="5">
          <span class="control-val" id="massVal">5 kg</span>
        </div>
      `;

      function updateFMA() {{
        const f = parseFloat(document.getElementById('forceF').value);
        const m = parseFloat(document.getElementById('massM').value);
        const a = (f / m).toFixed(2);

        document.getElementById('forceVal').textContent = `${{f}} N`;
        document.getElementById('massVal').textContent = `${{m}} kg`;
        document.getElementById('cartLabel').textContent = `m = ${{m}} kg`;
        document.getElementById('fText').textContent = `F = ${{f}} N`;
        document.getElementById('accDisplay').textContent = `${{a}} m/s²`;
      }}

      document.getElementById('forceF').addEventListener('input', updateFMA);
      document.getElementById('massM').addEventListener('input', updateFMA);
    }}

    // 9. Impulse Simulator
    function renderImpulseSim(svg, controls) {{
      svg.innerHTML = `
        <text x="220" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Impulse: J = F · Δt = Δp</text>
        <!-- Force curve graph -->
        <rect x="50" y="50" width="340" height="150" fill="#0f172a" stroke="#334155" />
        <line x1="60" y1="180" x2="380" y2="180" stroke="#64748b" />
        <line x1="60" y1="60" x2="60" y2="180" stroke="#64748b" />
        <text x="40" y="70" fill="#94a3b8" font-size="10">F (N)</text>
        <text x="370" y="195" fill="#94a3b8" font-size="10">t (s)</text>
        <!-- Peak curve -->
        <path id="curvePath" d="M 120 180 Q 150 70 180 180 Z" fill="rgba(239, 68, 68, 0.4)" stroke="#ef4444" stroke-width="3" />
        <text id="curveLabel" x="220" y="235" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">Stiff Hands: Tiny Δt (0.05s) ⟹ Peak Force = 600 N</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="setStiffHands()">🏏 Stiff Fixed Hands (High Peak Force)</button>
          <button class="sim-action-btn" onclick="setCushionedHands()">🤲 Retreating Hands (Cushioned Impact)</button>
        </div>
      `;

      window.setStiffHands = () => {{
        document.getElementById('curvePath').setAttribute('d', 'M 120 180 Q 140 60 160 180 Z');
        document.getElementById('curvePath').setAttribute('fill', 'rgba(239, 68, 68, 0.4)');
        document.getElementById('curvePath').setAttribute('stroke', '#ef4444');
        document.getElementById('curveLabel').textContent = 'Stiff Hands: Tiny Δt (0.03s) ⟹ Peak Force = 800 N (Ouch!)';
        document.getElementById('curveLabel').setAttribute('fill', '#ef4444');
      }};

      window.setCushionedHands = () => {{
        document.getElementById('curvePath').setAttribute('d', 'M 100 180 Q 200 130 300 180 Z');
        document.getElementById('curvePath').setAttribute('fill', 'rgba(16, 185, 129, 0.4)');
        document.getElementById('curvePath').setAttribute('stroke', '#10b981');
        document.getElementById('curveLabel').textContent = 'Retreating Hands: Large Δt (0.25s) ⟹ Peak Force = 96 N (Safe!)';
        document.getElementById('curveLabel').setAttribute('fill', '#10b981');
      }};
    }}

    // 10. Spring Balance Pair Simulator
    function renderSpringBalanceSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Fixed Wall -->
        <rect x="20" y="80" width="16" height="120" fill="#475569" />
        <line x1="36" y1="140" x2="60" y2="140" stroke="#94a3b8" stroke-width="3" />
        <!-- Spring Balance A -->
        <rect x="60" y="110" width="140" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <text x="130" y="130" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Balance A</text>
        <text id="balADial" x="130" y="155" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">40 N</text>
        <!-- Hook Connection -->
        <circle cx="200" cy="140" r="6" fill="none" stroke="#f59e0b" stroke-width="3" />
        <circle cx="208" cy="140" r="6" fill="none" stroke="#f59e0b" stroke-width="3" />
        <!-- Spring Balance B -->
        <rect x="214" y="110" width="140" height="60" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2" />
        <text x="284" y="130" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Balance B</text>
        <text id="balBDial" x="284" y="155" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">40 N</text>
        <!-- Pull Hand -->
        <line x1="354" y1="140" x2="390" y2="140" stroke="#f59e0b" stroke-width="4" />
        <text x="400" y="145" fill="#f59e0b" font-size="13" font-weight="bold">Pull</text>
        <text x="220" y="220" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">F_AB = -F_BA (Equal and Opposite Readings!)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Pull Force on Balance B:</span>
          <input type="range" id="springPull" min="0" max="100" value="40">
          <span class="control-val" id="springVal">40 N</span>
        </div>
      `;

      document.getElementById('springPull').addEventListener('input', (e) => {{
        const val = e.target.value;
        document.getElementById('springVal').textContent = `${{val}} N`;
        document.getElementById('balADial').textContent = `${{val}} N`;
        document.getElementById('balBDial').textContent = `${{val}} N`;
      }});
    }}

    // 11. Rocket Propulsion Simulator
    function renderRocketSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Launch Pad -->
        <rect x="180" y="240" width="80" height="10" fill="#475569" />
        <!-- Rocket Body -->
        <g id="rocketGroup" transform="translate(0, 0)">
          <path d="M220 50 L240 90 L240 180 L200 180 L200 90 Z" fill="#e2e8f0" stroke="#3b82f6" stroke-width="2" />
          <!-- Fins -->
          <polygon points="200,160 180,185 200,185" fill="#ef4444" />
          <polygon points="240,160 260,185 240,185" fill="#ef4444" />
          <!-- Flame Exhaust -->
          <polygon id="flame" points="210,185 220,230 230,185" fill="#f59e0b" opacity="0.8" />
        </g>
        <text x="100" y="80" fill="#38bdf8" font-size="12">Action: Gases expelled downward</text>
        <text x="100" y="100" fill="#10b981" font-size="12">Reaction: Upward thrust on rocket</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="launchRocket()">🚀 Ignite & Launch</button>
          <button class="sim-action-btn" onclick="resetRocket()">↺ Reset</button>
        </div>
      `;

      window.launchRocket = () => {{
        const rocket = document.getElementById('rocketGroup');
        const flame = document.getElementById('flame');
        flame.setAttribute('opacity', '1');
        rocket.style.transition = 'transform 2s cubic-bezier(.4,0,.2,1)';
        rocket.style.transform = 'translateY(-160px)';
      }};

      window.resetRocket = () => {{
        const rocket = document.getElementById('rocketGroup');
        const flame = document.getElementById('flame');
        flame.setAttribute('opacity', '0.4');
        rocket.style.transform = 'none';
      }};
    }}

    // 12. Collision Carts Simulator
    function renderCollisionSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="180" width="400" height="10" fill="#334155" />
        <!-- Cart 1 -->
        <rect id="colCart1" x="50" y="130" width="60" height="40" rx="4" fill="#00e5ff" />
        <text id="colLabel1" x="80" y="155" fill="#042f2e" font-size="12" font-weight="bold" text-anchor="middle">2 kg</text>
        <!-- Cart 2 -->
        <rect id="colCart2" x="250" y="130" width="80" height="40" rx="4" fill="#f59e0b" />
        <text id="colLabel2" x="290" y="155" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">4 kg</text>
        <!-- HUD -->
        <rect x="70" y="30" width="300" height="45" rx="6" fill="#1e293b" />
        <text id="hudInitialP" x="220" y="50" fill="#00e5ff" font-size="12" font-weight="bold" text-anchor="middle">Initial Momentum: 12.0 kg·m/s</text>
        <text id="hudFinalP" x="220" y="68" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Final Momentum: 12.0 kg·m/s (CONSERVED!)</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="runCollisionInelastic()">💥 Inelastic Collision (Stick Together)</button>
          <button class="sim-action-btn" onclick="resetCollision()">↺ Reset</button>
        </div>
      `;

      window.runCollisionInelastic = () => {{
        const c1 = document.getElementById('colCart1');
        const c2 = document.getElementById('colCart2');

        c1.style.transition = 'transform 0.8s linear';
        c1.style.transform = 'translateX(140px)';

        setTimeout(() => {{
          c1.style.transition = 'transform 1.2s linear';
          c2.style.transition = 'transform 1.2s linear';
          c1.style.transform = 'translateX(240px)';
          c2.style.transform = 'translateX(100px)';
        }}, 800);
      }};

      window.resetCollision = () => {{
        document.getElementById('colCart1').style.transform = 'none';
        document.getElementById('colCart2').style.transform = 'none';
      }};
    }}

    // 13. Cannon Recoil Simulator
    function renderCannonSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="200" width="400" height="10" fill="#334155" />
        <!-- Cannon Mount -->
        <g id="cannonBody" transform="translate(0, 0)">
          <rect x="140" y="140" width="80" height="50" rx="8" fill="#475569" stroke="#94a3b8" />
          <polygon points="200,150 260,140 260,165 200,165" fill="#334155" />
          <circle cx="160" cy="200" r="10" fill="#1e293b" />
          <circle cx="200" cy="200" r="10" fill="#1e293b" />
          <text x="180" y="170" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">M = 500 kg</text>
        </g>
        <!-- Cannonball -->
        <circle id="cannonBall" cx="260" cy="152" r="8" fill="#ef4444" />
        <!-- Readout -->
        <text id="recoilReadout" x="220" y="60" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">0 = m·v + M·V ⟹ Recoil Speed = -0.4 m/s</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="fireCannon()">💣 Fire Cannon!</button>
          <button class="sim-action-btn" onclick="resetCannon()">↺ Reload</button>
        </div>
      `;

      window.fireCannon = () => {{
        const ball = document.getElementById('cannonBall');
        const cannon = document.getElementById('cannonBody');

        ball.style.transition = 'transform 0.4s ease-out';
        ball.style.transform = 'translateX(160px)';

        cannon.style.transition = 'transform 0.3s ease-out';
        cannon.style.transform = 'translateX(-30px)';
      }};

      window.resetCannon = () => {{
        document.getElementById('cannonBall').style.transform = 'none';
        document.getElementById('cannonBody').style.transform = 'none';
      }};
    }}

    // 14. Virtual Air Track Simulator
    function renderAirTrackSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Air Track Rail -->
        <rect x="30" y="160" width="380" height="20" rx="3" fill="#0284c7" />
        <!-- Air jets dots -->
        ${{Array.from({{length: 18}}, (_, i) => `<circle cx="${{45 + i * 20}}" cy="170" r="2" fill="#fff" opacity="0.6"/>`).join('')}}
        <!-- Photogates -->
        <rect x="120" y="110" width="10" height="60" fill="#f59e0b" />
        <rect x="280" y="110" width="10" height="60" fill="#f59e0b" />
        <text x="125" y="100" fill="#f59e0b" font-size="10" text-anchor="middle">Gate 1</text>
        <text x="285" y="100" fill="#f59e0b" font-size="10" text-anchor="middle">Gate 2</text>
        <!-- Glider -->
        <polygon id="airGlider" points="50,158 80,135 110,158" fill="#10b981" />
        <!-- Pulley & Hanging Weight -->
        <circle cx="410" cy="170" r="10" fill="#64748b" />
        <line x1="110" y1="145" x2="410" y2="145" stroke="#e2e8f0" stroke-width="2" />
        <rect x="405" y="175" width="10" height="20" fill="#ef4444" />
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="runAirGlider()">▶ Release Glider</button>
        </div>
      `;

      window.runAirGlider = () => {{
        const g = document.getElementById('airGlider');
        g.style.transition = 'transform 1s cubic-bezier(.4,0,.2,1)';
        g.style.transform = 'translateX(280px)';
        setTimeout(() => {{
          g.style.transform = 'none';
        }}, 2000);
      }};
    }}

    // 15. Elevator Simulator
    function renderElevatorSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Elevator Shaft -->
        <rect x="140" y="30" width="160" height="220" fill="#0f172a" stroke="#334155" stroke-width="2" />
        <!-- Elevator Cabin -->
        <g id="elevatorCabin" transform="translate(0, 40)">
          <rect x="150" y="60" width="140" height="120" fill="#1e293b" stroke="#38bdf8" />
          <!-- Passenger -->
          <circle cx="220" cy="110" r="14" fill="#fed7aa" />
          <line x1="220" y1="124" x2="220" y2="155" stroke="#3b82f6" stroke-width="4" />
          <!-- Scale -->
          <rect x="195" y="160" width="50" height="10" fill="#f59e0b" />
        </g>
        <text id="elevStatus" x="220" y="240" fill="#00e5ff" font-size="12" font-weight="bold" text-anchor="middle">Stationary: N = mg = 588 N</text>
      `;

      controls.innerHTML = `
        <div class="sim-btn-row">
          <button class="sim-action-btn" onclick="elevMove('up')">⬆ Accelerate Up (N = m(g+a))</button>
          <button class="sim-action-btn" onclick="elevMove('down')">⬇ Accelerate Down (N = m(g-a))</button>
          <button class="sim-action-btn" onclick="elevMove('freefall')">⚡ Free Fall (N = 0)</button>
        </div>
      `;

      window.elevMove = (mode) => {{
        const cabin = document.getElementById('elevatorCabin');
        const status = document.getElementById('elevStatus');
        if (mode === 'up') {{
          cabin.style.transition = 'transform 0.8s ease-out';
          cabin.style.transform = 'translateY(10px)';
          status.textContent = 'Accelerating Up (+2 m/s²): N = 708 N (Heavier!)';
          status.setAttribute('fill', '#10b981');
        }} else if (mode === 'down') {{
          cabin.style.transition = 'transform 0.8s ease-out';
          cabin.style.transform = 'translateY(70px)';
          status.textContent = 'Accelerating Down (-2 m/s²): N = 468 N (Lighter!)';
          status.setAttribute('fill', '#f59e0b');
        }} else {{
          cabin.style.transition = 'transform 0.5s ease-in';
          cabin.style.transform = 'translateY(90px)';
          status.textContent = 'FREE FALL (a = g): N = 0 N (WEIGHTLESSNESS!)';
          status.setAttribute('fill', '#ef4444');
        }}
      }};
    }}

    // 16. Fundamental Forces Simulator
    function renderFundamentalForcesSim(svg, controls) {{
      svg.innerHTML = `
        <!-- 4 Circles for Forces -->
        <g transform="translate(60, 70)">
          <circle cx="0" cy="0" r="35" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="2" />
          <text x="0" y="5" fill="#3b82f6" font-size="10" font-weight="bold" text-anchor="middle">Gravitational</text>
        </g>
        <g transform="translate(160, 70)">
          <circle cx="0" cy="0" r="35" fill="rgba(0, 229, 255, 0.2)" stroke="#00e5ff" stroke-width="2" />
          <text x="0" y="5" fill="#00e5ff" font-size="10" font-weight="bold" text-anchor="middle">Electromagnetic</text>
        </g>
        <g transform="translate(260, 70)">
          <circle cx="0" cy="0" r="35" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2" />
          <text x="0" y="5" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Strong Nuclear</text>
        </g>
        <g transform="translate(360, 70)">
          <circle cx="0" cy="0" r="35" fill="rgba(236, 72, 153, 0.2)" stroke="#ec4899" stroke-width="2" />
          <text x="0" y="5" fill="#ec4899" font-size="10" font-weight="bold" text-anchor="middle">Weak Nuclear</text>
        </g>
        <!-- Relativistic graph -->
        <rect x="40" y="140" width="360" height="90" fill="#0f172a" stroke="#334155" />
        <path d="M 50 210 Q 250 200 350 150" fill="none" stroke="#f59e0b" stroke-width="3" />
        <text x="220" y="250" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Relativistic Momentum p = γmv Diverges as v ➡ c</text>
      `;

      controls.innerHTML = `
        <div style="font-size:0.85rem; color:#94a3b8; text-align:center;">
          Everyday contact forces (friction, tension, normal reaction) are fundamentally <strong>Electromagnetic</strong>.
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

    output_path = 'public/animations/class9-force-and-laws-of-motion.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated {output_path} ({len(html_content)} bytes).")

if __name__ == '__main__':
    build_html()

