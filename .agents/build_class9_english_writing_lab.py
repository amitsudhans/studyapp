# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 9 English Chapter 1:
Effective Communication and Writing in Diverse Forms (Curricular Goal CG-1)
Produces: public/animations/class9-english-communication-writing.html
"""

import os
import json
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from class9_english_writing_data import slides_data, quiz_questions

def generate_lab_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 9 English • Chapter 1: Effective Communication & Writing Master Lab</title>
  
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
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top Navigation */
    .top-nav {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid var(--card-border);
      backdrop-filter: blur(12px);
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
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      color: #fff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .nav-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.2px;
    }}

    .nav-stats {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .slide-indicator {{
      font-size: 0.9rem;
      color: var(--accent-cyan);
      font-weight: 600;
      background: rgba(6, 182, 212, 0.1);
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid rgba(6, 182, 212, 0.3);
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
      flex: 1;
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
      padding-bottom: 14px;
    }}

    .slide-header h2 {{
      font-size: 1.7rem;
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.3px;
      line-height: 1.3;
    }}

    .slide-header h3 {{
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--accent-cyan);
      margin-top: 4px;
    }}

    .slide-body {{
      min-width: 0;
      width: 100%;
      box-sizing: border-box;
      flex: 1;
    }}

    p.lead-p {{
      font-size: 1.05rem;
      color: #e2e8f0;
      margin-bottom: 16px;
    }}

    .theory-box {{
      background: rgba(30, 41, 59, 0.5);
      border-left: 4px solid var(--accent-indigo);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 18px;
    }}

    .theory-box h4 {{
      color: var(--accent-cyan);
      font-size: 1.1rem;
      margin-bottom: 8px;
    }}

    .theory-box p, .theory-box ul, .theory-box ol {{
      color: #cbd5e1;
      font-size: 0.95rem;
    }}

    .theory-box ul, .theory-box ol {{
      padding-left: 20px;
      margin-top: 8px;
    }}

    .theory-box li {{
      margin-bottom: 6px;
    }}

    .highlight-eq {{
      background: rgba(99, 102, 241, 0.1);
      border: 1px solid rgba(99, 102, 241, 0.3);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 12px 0;
      text-align: center;
      color: #e0e7ff;
      font-size: 1.05rem;
      font-weight: 600;
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
      font-size: 1rem;
    }}

    .card-item p, .card-item ul {{
      color: #cbd5e1;
      font-size: 0.9rem;
    }}

    .card-item ul {{
      padding-left: 18px;
      margin-top: 6px;
    }}

    .card-item li {{
      margin-bottom: 4px;
    }}

    /* Checkpoints within slides */
    .checkpoints-section {{
      margin-top: 24px;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(99, 102, 241, 0.3);
      border-radius: 12px;
      padding: 18px;
    }}

    .checkpoints-header {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--accent-amber);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .checkpoint-card {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
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
      font-size: 0.85rem;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s;
    }}

    .option-btn:hover:not(:disabled) {{
      background: rgba(99, 102, 241, 0.25);
      border-color: var(--accent-indigo);
      color: #fff;
    }}

    .option-btn.correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #a7f3d0 !important;
      font-weight: 600;
    }}

    .option-btn.wrong {{
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fecdd3 !important;
    }}

    .checkpoint-feedback {{
      margin-top: 10px;
      font-size: 0.88rem;
      padding: 8px 12px;
      border-radius: 6px;
      display: none;
    }}

    .checkpoint-feedback.show {{
      display: block;
    }}

    .checkpoint-feedback.correct-fb {{
      background: rgba(16, 185, 129, 0.15);
      color: #a7f3d0;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .checkpoint-feedback.wrong-fb {{
      background: rgba(244, 63, 94, 0.15);
      color: #fecdd3;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }}

    /* Strict Last Slide Notice */
    .last-slide-notice {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #a7f3d0;
      padding: 14px 20px;
      border-radius: 10px;
      font-weight: 700;
      text-align: center;
      margin-top: 24px;
      display: none;
    }}

    /* Quiz Challenges Section */
    .quiz-container {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 16px;
    }}

    .quiz-item {{
      background: rgba(30, 41, 59, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 16px;
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
      background: rgba(6, 182, 212, 0.1);
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

    /* Teacher Avatar Box */
    .teacher-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
    }}

    .avatar-wrapper {{
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background: linear-gradient(135deg, #4f46e5, #06b6d4);
      padding: 3px;
      margin-bottom: 10px;
      box-shadow: 0 0 18px rgba(99, 102, 241, 0.4);
    }}

    .avatar-svg {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: #0f172a;
    }}

    .teacher-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
    }}

    .teacher-role {{
      font-size: 0.8rem;
      color: var(--accent-cyan);
      margin-bottom: 12px;
    }}

    .speech-bubble {{
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px 14px;
      font-size: 0.88rem;
      color: #e2e8f0;
      line-height: 1.45;
      text-align: left;
      width: 100%;
      position: relative;
    }}

    .voice-controls {{
      display: flex;
      gap: 8px;
      margin-top: 12px;
      width: 100%;
    }}

    .voice-btn {{
      flex: 1;
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: #c7d2fe;
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .voice-btn:hover {{
      background: rgba(99, 102, 241, 0.3);
      color: #fff;
    }}

    /* Simulator Panel Box */
    .simulator-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 18px;
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
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 8px;
    }}

    .sim-canvas-area {{
      background: #020617;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      min-height: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
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
      margin-top: 8px;
    }}

    .sim-action-btn {{
      flex: 1;
      background: linear-gradient(135deg, #4f46e5, #0891b2);
      border: none;
      color: #fff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .sim-action-btn:hover {{
      filter: brightness(1.15);
    }}

    /* Bottom Navigation Bar */
    .bottom-bar {{
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid var(--card-border);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      bottom: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }}

    .nav-btn {{
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid var(--card-border);
      color: #fff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}

    .nav-btn:hover:not(:disabled) {{
      background: var(--accent-indigo);
      border-color: var(--accent-indigo);
    }}

    .nav-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    /* Solution Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .modal-card {{
      background: #0f172a;
      border: 1px solid var(--accent-cyan);
      border-radius: 14px;
      max-width: 600px;
      width: 100%;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      position: relative;
    }}

    .modal-close {{
      position: absolute;
      top: 14px;
      right: 16px;
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 1.4rem;
      cursor: pointer;
    }}

    .modal-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 12px;
    }}

    .modal-body {{
      font-size: 0.95rem;
      color: #e2e8f0;
      line-height: 1.6;
      white-space: pre-line;
      max-height: 60vh;
      overflow-y: auto;
    }}
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <header class="top-nav">
    <div class="nav-brand">
      <span class="nav-badge">NCERT • Class 9 English</span>
      <span class="nav-title">Chapter 1: Effective Communication & Writing Forms (CG-1)</span>
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
            <path d="M30 85 C30 70, 70 70, 70 85 Z" fill="#4338ca" />
            <!-- Head & Face -->
            <circle cx="50" cy="45" r="24" fill="#fde68a" />
            <!-- Hair -->
            <path d="M25 45 C25 22, 75 22, 75 45 C75 28, 25 28, 25 45 Z" fill="#78350f" />
            <path d="M25 42 C22 55, 28 65, 32 70 C28 58, 26 48, 25 42 Z" fill="#78350f" />
            <path d="M75 42 C78 55, 72 65, 68 70 C72 58, 74 48, 75 42 Z" fill="#78350f" />
            <!-- Glasses -->
            <rect x="36" y="40" width="10" height="7" rx="2" fill="none" stroke="#d97706" stroke-width="2" />
            <rect x="54" y="40" width="10" height="7" rx="2" fill="none" stroke="#d97706" stroke-width="2" />
            <line x1="46" y1="43" x2="54" y2="43" stroke="#d97706" stroke-width="2" />
            <!-- Eyes -->
            <circle cx="41" cy="43" r="1.5" fill="#0f172a" />
            <circle cx="59" cy="43" r="1.5" fill="#0f172a" />
            <!-- Animated Talking Mouth -->
            <ellipse id="teacherMouth" cx="50" cy="56" rx="4" ry="1.5" fill="#e11d48" />
          </svg>
        </div>
        <div class="teacher-title">English Mentor</div>
        <div class="teacher-role">Senior Rhetoric & Communication Guide</div>
        <div class="speech-bubble" id="teacherSpeech">
          Welcome to the Effective Communication and Writing Master Laboratory!
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
      NCERT English Class 9 • Chapter 1 (CG-1)
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
    const quizData = {quiz_json};

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
        fb.innerHTML = `<strong>✓ Correct!</strong> Click 'View Solution' for detailed step-by-step analysis.`;
      }} else {{
        btn.classList.add('wrong');
        buttons[correct].classList.add('correct');
        fb.className = 'checkpoint-feedback show wrong-fb';
        fb.innerHTML = `<strong>✗ Incorrect.</strong> Click 'View Solution' to see the model explanation.`;
      }}
    }}

    // Solution Modal Operations
    function openSolutionModal(qNum) {{
      const q = quizData.find(item => item.num === qNum);
      if (!q) return;

      document.getElementById('modalTitle').textContent = `Question ${{q.num}} Solution & Analysis`;
      document.getElementById('modalBody').textContent = q.solution;
      document.getElementById('solutionModal').style.display = 'flex';
    }}

    function closeSolutionModal() {{
      document.getElementById('solutionModal').style.display = 'none';
    }}

    // Voiceover Speech Engine
    function speakText(text) {{
      if (!('speechSynthesis' in window)) return;
      stopSpeech();

      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.lang = 'en-US';
      currentUtterance.rate = 0.95;
      currentUtterance.pitch = 1.05;

      const voices = synth.getVoices();
      const femaleVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Female') || v.name.includes('Zira') || v.name.includes('Samantha') || v.name.includes('Google US English')));
      if (femaleVoice) currentUtterance.voice = femaleVoice;

      currentUtterance.onstart = () => {{
        isSpeaking = true;
        document.getElementById('voiceIcon').textContent = '⏹';
        document.getElementById('voiceLabel').textContent = 'Stop Voiceover';
        startMouthAnimation();
      }};

      currentUtterance.onend = () => {{
        stopMouthAnimation();
      }};

      currentUtterance.onerror = () => {{
        stopMouthAnimation();
      }};

      synth.speak(currentUtterance);
    }}

    function toggleSpeech() {{
      if (isSpeaking) {{
        stopSpeech();
      }} else {{
        const text = slides[currentSlideIndex].voice;
        speakText(text);
      }}
    }}

    function replaySpeech() {{
      const text = slides[currentSlideIndex].voice;
      speakText(text);
    }}

    function stopSpeech() {{
      if ('speechSynthesis' in window) {{
        synth.cancel();
      }}
      stopMouthAnimation();
    }}

    function startMouthAnimation() {{
      const mouth = document.getElementById('teacherMouth');
      if (!mouth) return;
      clearInterval(mouthInterval);
      mouthInterval = setInterval(() => {{
        const ry = (Math.random() * 4 + 1.5).toFixed(1);
        mouth.setAttribute('ry', ry);
      }}, 120);
    }}

    function stopMouthAnimation() {{
      isSpeaking = false;
      document.getElementById('voiceIcon').textContent = '🔊';
      document.getElementById('voiceLabel').textContent = 'Play Voiceover';
      clearInterval(mouthInterval);
      const mouth = document.getElementById('teacherMouth');
      if (mouth) mouth.setAttribute('ry', '1.5');
    }}

    // ==========================================
    // 16 BESPOKE INTERACTIVE SIMULATORS
    // ==========================================
    function renderSimulator(type) {{
      const svg = document.getElementById('simSvg');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');

      switch(type) {{
        case 'comm_loop_matrix':
          title.textContent = 'Dynamic Communication Loop & Noise Matrix';
          renderCommLoopSim(svg, controls);
          break;
        case 'social_register_slider':
          title.textContent = 'Sociolinguistic Register Continuum Studio';
          renderRegisterSim(svg, controls);
          break;
        case 'debate_arena_builder':
          title.textContent = 'AREI Debate Reasoning Arena & Fallacy Detector';
          renderDebateSim(svg, controls);
          break;
        case 'freytags_pyramid_lab':
          title.textContent = "Freytag's Narrative Plot Arc & Suspense Studio";
          renderFreytagSim(svg, controls);
          break;
        case 'sensory_imagery_palette':
          title.textContent = "5-Senses Imagery Palette & Show-Don't-Tell Studio";
          renderSensorySim(svg, controls);
          break;
        case 'expository_structure_builder':
          title.textContent = "Expository PEEL Structuring & Transitions Lab";
          renderExpositorySim(svg, controls);
          break;
        case 'rhetorical_triangle_mixer':
          title.textContent = "Aristotle's Rhetoric Mixer: Ethos, Pathos, Logos";
          renderRhetoricSim(svg, controls);
          break;
        case 'letter_builder_studio':
          title.textContent = "Full-Block Formal & Informal Letter Architect";
          renderLetterSim(svg, controls);
          break;
        case 'notice_board_canvas':
          title.textContent = "Official Notice Board & 5 W's Protocol Studio";
          renderNoticeSim(svg, controls);
          break;
        case 'invitation_rsvp_studio':
          title.textContent = 'Formal Invitation Card & RSVP Reply Studio';
          renderInvitationSim(svg, controls);
          break;
        case 'podium_speech_simulator':
          title.textContent = 'Public Speech Podium Delivery & Rhetoric Lab';
          renderSpeechSim(svg, controls);
          break;
        case 'empathy_condolence_lab':
          title.textContent = 'Empathetic Condolence & Sensitivity Workshop';
          renderCondolenceSim(svg, controls);
          break;
        case 'ad_copy_slogan_canvas':
          title.textContent = 'Advertising Copy & Creative Slogan Canvas';
          renderAdCopySim(svg, controls);
          break;
        case 'article_newsroom_layout':
          title.textContent = 'School Magazine Newsroom & Inverted Pyramid Lab';
          renderArticleSim(svg, controls);
          break;
        case 'av_script_teleprompter':
          title.textContent = 'Two-Column AV Digital Script & Teleprompter';
          renderAvScriptSim(svg, controls);
          break;
        case 'email_netiquette_simulator':
          title.textContent = 'Professional Email & Netiquette Audit Studio';
          renderEmailSim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Mastery Challenge Dashboard';
          renderQuizDashboardSim(svg, controls);
      }}
    }}

    // 1. Communication Loop Simulator
    function renderCommLoopSim(svg, controls) {{
      svg.innerHTML = `
        <defs>
          <marker id="loopArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#06b6d4" />
          </marker>
          <marker id="fbArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#10b981" />
          </marker>
        </defs>
        <!-- Sender Box -->
        <rect x="25" y="60" width="100" height="70" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2" />
        <text x="75" y="90" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">SENDER</text>
        <text x="75" y="110" fill="#c7d2fe" font-size="10" text-anchor="middle">(Encoder)</text>
        
        <!-- Forward Message Path -->
        <path id="msgPath" d="M 125 80 Q 220 40 315 80" fill="none" stroke="#06b6d4" stroke-width="3" marker-end="url(#loopArrow)" />
        <rect id="msgTag" x="180" y="35" width="80" height="22" rx="4" fill="#0284c7" />
        <text x="220" y="50" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Message</text>
        
        <!-- Receiver Box -->
        <rect x="315" y="60" width="100" height="70" rx="8" fill="#042f2e" stroke="#10b981" stroke-width="2" />
        <text x="365" y="90" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">RECEIVER</text>
        <text x="365" y="110" fill="#a7f3d0" font-size="10" text-anchor="middle">(Decoder)</text>
        
        <!-- Feedback Path -->
        <path id="fbPath" d="M 315 110 Q 220 150 125 110" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="5 3" marker-end="url(#fbArrow)" />
        <text x="220" y="152" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Feedback Loop</text>

        <!-- Noise Barrier Cloud -->
        <rect id="noiseBox" x="170" y="170" width="100" height="35" rx="8" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-dasharray="3 3" />
        <text x="220" y="192" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">NOISE: 10%</text>

        <!-- Fidelity HUD -->
        <rect x="40" y="225" width="360" height="42" rx="6" fill="#0f172a" stroke="#06b6d4" />
        <text id="loopFidelityText" x="220" y="250" fill="#06b6d4" font-size="13" font-weight="bold" text-anchor="middle">Clarity Fidelity: 90% (Smooth Transmission)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Channel Interference (Noise):</span>
          <input type="range" id="noiseSlider" min="0" max="90" value="10">
          <span class="control-val" id="noiseVal">10%</span>
        </div>
        <div class="control-row">
          <span>Transmission Channel:</span>
          <select id="channelSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="formal_letter">Full-Block Formal Letter</option>
            <option value="email">Professional Email</option>
            <option value="speech">Public Speech at Assembly</option>
            <option value="podcast">Digital Audio Podcast</option>
          </select>
        </div>
      `;

      function updateLoop() {{
        const noise = parseInt(document.getElementById('noiseSlider').value);
        document.getElementById('noiseVal').textContent = `${{noise}}%`;
        const fidelity = 100 - noise;

        const noiseBox = document.getElementById('noiseBox');
        noiseBox.querySelector('text').textContent = `NOISE: ${{noise}}%`;
        noiseBox.setAttribute('fill', `rgba(244, 63, 94, ${{0.1 + noise / 100 * 0.5}})`);

        const fidelityText = document.getElementById('loopFidelityText');
        if (fidelity > 70) {{
          fidelityText.textContent = `Clarity Fidelity: ${{fidelity}}% (Message Decoded Accurately)`;
          fidelityText.setAttribute('fill', '#10b981');
        }} else if (fidelity > 40) {{
          fidelityText.textContent = `Clarity Fidelity: ${{fidelity}}% (Moderate Distortion / Misunderstanding)`;
          fidelityText.setAttribute('fill', '#f59e0b');
        }} else {{
          fidelityText.textContent = `Clarity Fidelity: ${{fidelity}}% (Severe Breakdown / Communication Failure)`;
          fidelityText.setAttribute('fill', '#f43f5e');
        }}
      }}

      document.getElementById('noiseSlider').addEventListener('input', updateLoop);
      document.getElementById('channelSelect').addEventListener('change', (e) => {{
        const channel = e.target.value;
        const msgTag = document.getElementById('msgTag').querySelector('text');
        if (channel === 'formal_letter') msgTag.textContent = 'Letter';
        else if (channel === 'email') msgTag.textContent = 'Email';
        else if (channel === 'speech') msgTag.textContent = 'Speech';
        else msgTag.textContent = 'Podcast';
      }});
    }}

    // 2. Sociolinguistic Register Slider
    function renderRegisterSim(svg, controls) {{
      const registerData = [
        {{ name: "1. Frozen (Static)", example: "Oaths, Constitution, National Anthem", text: "\\"I do solemnly swear that I will bear true faith and allegiance...\\"", color: "#a855f7" }},
        {{ name: "2. Formal", example: "Principal leave letter, Academic essays", text: "\\"I am writing to formally request a one-day leave of absence due to an urgent family commitment.\\"", color: "#3b82f6" }},
        {{ name: "3. Consultative", example: "Doctor-patient, Teacher-student review", text: "\\"Could you explain where you encountered difficulty in this chapter, and we will review it?\\"", color: "#06b6d4" }},
        {{ name: "4. Casual", example: "Classmates at recess, sports ground", text: "\\"Hey, toss me that ball real quick, gotta run to the canteen!\\"", color: "#10b981" }},
        {{ name: "5. Intimate", example: "Family members, closest childhood friend", text: "\\"Bhai, save me some dessert! You know I'm starving.\\"", color: "#f59e0b" }}
      ];

      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0f172a" stroke="#6366f1" stroke-width="1.5" />
        <text id="regTitle" x="220" y="50" fill="#6366f1" font-size="14" font-weight="bold" text-anchor="middle">2. Formal Register</text>
        <text id="regContext" x="220" y="75" fill="#94a3b8" font-size="11" text-anchor="middle">Context: Principal leave letter, Academic essays</text>
        
        <!-- Register Preview Speech Card -->
        <rect x="35" y="100" width="370" height="90" rx="8" fill="#1e1b4b" stroke="#38bdf8" />
        <foreignObject x="45" y="105" width="350" height="80">
          <div xmlns="http://www.w3.org/1999/xhtml" id="regSpeechText" style="color:#e0e7ff; font-size:12px; line-height:1.5; font-style:italic;">
            "I am writing to formally request a one-day leave of absence due to an urgent family commitment."
          </div>
        </foreignObject>

        <!-- Continuum Indicator Bar -->
        <line x1="40" y1="225" x2="400" y2="225" stroke="#334155" stroke-width="6" stroke-linecap="round" />
        <circle id="regSliderPoint" cx="130" cy="225" r="9" fill="#3b82f6" stroke="#fff" stroke-width="2" />
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Sociolinguistic Register Level:</span>
          <input type="range" id="regRange" min="0" max="4" value="1">
          <span class="control-val" id="regVal">Formal</span>
        </div>
      `;

      document.getElementById('regRange').addEventListener('input', (e) => {{
        const idx = parseInt(e.target.value);
        const data = registerData[idx];

        document.getElementById('regTitle').textContent = data.name;
        document.getElementById('regTitle').setAttribute('fill', data.color);
        document.getElementById('regContext').textContent = `Context: ${{data.example}}`;
        document.getElementById('regSpeechText').textContent = data.text;
        document.getElementById('regVal').textContent = data.name.split('.')[1].trim();

        const cx = 40 + idx * 90;
        const pt = document.getElementById('regSliderPoint');
        pt.setAttribute('cx', cx);
        pt.setAttribute('fill', data.color);
      }});
    }}

    // 3. Debate Arena Simulator
    function renderDebateSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#090d16" stroke="#06b6d4" stroke-width="1.5" />
        <text x="220" y="45" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">MOTION: 'Artificial Intelligence Tools Should Be Integrated in High Schools'</text>
        
        <!-- 4 AREI Pillars -->
        <g id="areiG">
          <rect x="30" y="70" width="85" height="120" rx="6" fill="#1e1b4b" stroke="#6366f1" />
          <text x="72" y="92" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">ASSERTION</text>
          <foreignObject x="35" y="100" width="75" height="85">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:9px; color:#e0e7ff; line-height:1.3;">AI provides individualized feedback.</div>
          </foreignObject>

          <rect x="125" y="70" width="85" height="120" rx="6" fill="#042f2e" stroke="#10b981" />
          <text x="167" y="92" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">REASONING</text>
          <foreignObject x="130" y="100" width="75" height="85">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:9px; color:#a7f3d0; line-height:1.3;">Algorithms adapt to unique learning pace.</div>
          </foreignObject>

          <rect x="220" y="70" width="85" height="120" rx="6" fill="#172554" stroke="#3b82f6" />
          <text x="262" y="92" fill="#bfdbfe" font-size="11" font-weight="bold" text-anchor="middle">EVIDENCE</text>
          <foreignObject x="225" y="100" width="75" height="85">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:9px; color:#bfdbfe; line-height:1.3;">UNESCO 2024: 32% retention boost.</div>
          </foreignObject>

          <rect x="315" y="70" width="85" height="120" rx="6" fill="#451a03" stroke="#f59e0b" />
          <text x="357" y="92" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">IMPACT</text>
          <foreignObject x="320" y="100" width="75" height="85">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:9px; color:#fde68a; line-height:1.3;">Closes the educational divide.</div>
          </foreignObject>
        </g>

        <!-- Fallacy Shield Status -->
        <rect x="40" y="205" width="360" height="40" rx="6" fill="#0f172a" stroke="#10b981" />
        <text id="fallacyStatus" x="220" y="230" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Argument Integrity: 100% (No Fallacies Detected)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Simulate Opponent Fallacy Attack:</span>
          <select id="fallacySelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="none">Principled Logical Rebuttal</option>
            <option value="ad_hominem">Ad Hominem (Attacking Speaker's Age)</option>
            <option value="straw_man">Straw Man (Misrepresenting Proposal)</option>
            <option value="false_dilemma">False Dilemma (Black-or-White Extreme)</option>
          </select>
        </div>
      `;

      document.getElementById('fallacySelect').addEventListener('change', (e) => {{
        const status = document.getElementById('fallacyStatus');
        const val = e.target.value;
        if (val === 'none') {{
          status.textContent = 'Argument Integrity: 100% (Principled Logical Rebuttal)';
          status.setAttribute('fill', '#10b981');
        }} else if (val === 'ad_hominem') {{
          status.textContent = 'FLAGGED: Ad Hominem Fallacy (Attacking character, not ideas!)';
          status.setAttribute('fill', '#f43f5e');
        }} else if (val === 'straw_man') {{
          status.textContent = 'FLAGGED: Straw Man Fallacy (Exaggerating & distorting position!)';
          status.setAttribute('fill', '#f59e0b');
        }} else {{
          status.textContent = 'FLAGGED: False Dilemma (Falsely claiming only 2 extremes exist!)';
          status.setAttribute('fill', '#f59e0b');
        }}
      }});
    }}

    // 4. Freytag's Pyramid Simulator
    function renderFreytagSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Pyramid Arc Path -->
        <polyline points="40,210 110,180 220,60 320,160 400,210" fill="none" stroke="#6366f1" stroke-width="4" stroke-linecap="round" />
        <circle id="plotMarker" cx="220" cy="60" r="10" fill="#f59e0b" stroke="#fff" stroke-width="2" />
        
        <!-- Plot Stage Labels -->
        <text x="40" y="235" fill="#94a3b8" font-size="10" text-anchor="middle">Exposition</text>
        <text x="110" y="200" fill="#94a3b8" font-size="10" text-anchor="middle">Inciting</text>
        <text x="220" y="45" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">CLIMAX</text>
        <text x="320" y="180" fill="#94a3b8" font-size="10" text-anchor="middle">Falling</text>
        <text x="400" y="235" fill="#94a3b8" font-size="10" text-anchor="middle">Resolution</text>

        <!-- Plot Event Card -->
        <rect x="40" y="90" width="160" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#6366f1" />
        <text id="plotStageName" x="120" y="112" fill="#06b6d4" font-size="11" font-weight="bold" text-anchor="middle">3. Climax (Turning Point)</text>
        <foreignObject x="45" y="120" width="150" height="36">
          <div xmlns="http://www.w3.org/1999/xhtml" id="plotDesc" style="font-size:9px; color:#e2e8f0; line-height:1.2;">
            Aarav confronts his deepest fear during the storm.
          </div>
        </foreignObject>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Narrative Plot Stage:</span>
          <input type="range" id="stageSlider" min="0" max="4" value="2">
          <span class="control-val" id="stageVal">Climax</span>
        </div>
      `;

      const stages = [
        {{ name: "1. Exposition", desc: "Setting: Quiet mountain hamlet. Ordinary status quo.", cx: 40, cy: 210, color: "#94a3b8" }},
        {{ name: "2. Inciting Incident", desc: "An urgent distress radio call arrives; power grid fails.", cx: 110, cy: 180, color: "#38bdf8" }},
        {{ name: "3. Climax", desc: "Aarav crosses the swaying rope bridge amidst howling wind.", cx: 220, cy: 60, color: "#f59e0b" }},
        {{ name: "4. Falling Action", desc: "The stranded travelers are safely escorted to shelter.", cx: 320, cy: 160, color: "#10b981" }},
        {{ name: "5. Resolution", desc: "Dawn breaks; Aarav discovers his own inner resilience.", cx: 400, cy: 210, color: "#a855f7" }}
      ];

      document.getElementById('stageSlider').addEventListener('input', (e) => {{
        const idx = parseInt(e.target.value);
        const st = stages[idx];

        document.getElementById('plotStageName').textContent = st.name;
        document.getElementById('plotStageName').setAttribute('fill', st.color);
        document.getElementById('plotDesc').textContent = st.desc;
        document.getElementById('stageVal').textContent = st.name.split('.')[1].trim();

        const m = document.getElementById('plotMarker');
        m.setAttribute('cx', st.cx);
        m.setAttribute('cy', st.cy);
        m.setAttribute('fill', st.color);
      }});
    }}

    // 5. Sensory Imagery Studio
    function renderSensorySim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5" />
        <text id="senseTitle" x="220" y="50" fill="#06b6d4" font-size="14" font-weight="bold" text-anchor="middle">Sense: Olfactory (Smell)</text>
        
        <!-- Flat Telling vs Rich Showing -->
        <rect x="35" y="70" width="370" height="65" rx="6" fill="#1e1b4b" stroke="#f43f5e" />
        <text x="45" y="88" fill="#f43f5e" font-size="10" font-weight="bold">FLAT TELLING (Lacks Sensory Detail):</text>
        <text id="flatTell" x="45" y="112" fill="#cbd5e1" font-size="11">"The kitchen smelled like food."</text>

        <rect x="35" y="145" width="370" height="95" rx="6" fill="#042f2e" stroke="#10b981" />
        <text x="45" y="165" fill="#10b981" font-size="10" font-weight="bold">RICH SHOWING (Multi-Sensory Palette):</text>
        <foreignObject x="45" y="172" width="350" height="60">
          <div xmlns="http://www.w3.org/1999/xhtml" id="richShow" style="font-size:11px; color:#a7f3d0; line-height:1.4;">
            "The pungent aroma of roasted cardamom and spluttering mustard seeds drifted into the verandah, rich with the warmth of ginger."
          </div>
        </foreignObject>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Active Sensory Palette:</span>
          <select id="senseSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="olfactory">Olfactory (Smell)</option>
            <option value="auditory">Auditory (Sound)</option>
            <option value="tactile">Tactile (Touch / Texture)</option>
            <option value="visual">Visual (Sight / Color)</option>
            <option value="gustatory">Gustatory (Taste)</option>
          </select>
        </div>
      `;

      const senseMap = {{
        olfactory: {{
          title: "Sense: Olfactory (Smell)",
          tell: "\\"The kitchen smelled like food.\\"",
          show: "\\"The pungent aroma of roasted cardamom and spluttering mustard seeds drifted into the verandah, rich with the warmth of ginger.\\""
        }},
        auditory: {{
          title: "Sense: Auditory (Sound)",
          tell: "\\"The forest was noisy.\\"",
          show: "\\"Dry twigs snapped underfoot as crickets thrummed a feverish rhythm, punctuated by the mournful hoot of a horned owl.\\""
        }},
        tactile: {{
          title: "Sense: Tactile (Touch & Temperature)",
          tell: "\\"The water was cold.\\"",
          show: "\\"I dipped my hand into the glacial stream; a thousand icy needles pricked my fingertips, numbing my skin to the bone.\\""
        }},
        visual: {{
          title: "Sense: Visual (Sight & Geometry)",
          tell: "\\"The sunset was colorful.\\"",
          show: "\\"Amber light bleeding into violet shadows set the jagged mountain peaks ablaze, as silhouettes of cranes carved through the crimson dusk.\\""
        }},
        gustatory: {{
          title: "Sense: Gustatory (Taste)",
          tell: "\\"The fruit was sour.\\"",
          show: "\\"A sharp, electric jolt of raw green mango seasoned with rock salt and roasted chili powder detonated across my tongue.\\""
        }}
      }};

      document.getElementById('senseSelect').addEventListener('change', (e) => {{
        const s = senseMap[e.target.value];
        document.getElementById('senseTitle').textContent = s.title;
        document.getElementById('flatTell').textContent = s.tell;
        document.getElementById('richShow').textContent = s.show;
      }});
    }}

    // 6. Expository PEEL Structure Simulator
    function renderExpositorySim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0f172a" stroke="#6366f1" stroke-width="1.5" />
        <text x="220" y="45" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">PEEL PARAGRAPH ARCHITECT</text>
        
        <rect id="peelBox" x="35" y="65" width="370" height="135" rx="8" fill="#1e1b4b" stroke="#38bdf8" />
        <text id="peelBadge" x="48" y="90" fill="#38bdf8" font-size="11" font-weight="bold">POINT (Topic Sentence)</text>
        <foreignObject x="48" y="100" width="345" height="90">
          <div xmlns="http://www.w3.org/1999/xhtml" id="peelText" style="color:#e2e8f0; font-size:11px; line-height:1.45;">
            "Renewable energy investments generate substantially higher employment multiplier ratios compared to fossil fuel infrastructure."
          </div>
        </foreignObject>

        <!-- Cohesive Transition Bar -->
        <rect x="35" y="210" width="370" height="35" rx="6" fill="#042f2e" stroke="#10b981" />
        <text id="peelTransition" x="220" y="232" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Transition Bridge: "Furthermore, empirical fiscal audits demonstrate..."</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Inspect PEEL Component:</span>
          <select id="peelSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="P">P — Point (Topic Sentence)</option>
            <option value="E1">E — Evidence (Data & Study Citation)</option>
            <option value="E2">E — Explanation (Analytical Link)</option>
            <option value="L">L — Link (Transition to Next Idea)</option>
          </select>
        </div>
      `;

      const peelData = {{
        P: {{
          badge: "POINT (Topic Sentence)",
          text: "\\"Renewable energy investments generate substantially higher employment multiplier ratios compared to fossil fuel infrastructure.\\"",
          color: "#38bdf8",
          trans: "Signpost: \\"First and foremost, economic data indicates...\\""
        }},
        E1: {{
          badge: "EVIDENCE (Concrete Citations & Data)",
          text: "\\"According to the International Labour Organization (ILO 2024 Report), solar installation creates 3.8 times more local jobs per dollar invested than coal.\\"",
          color: "#f59e0b",
          trans: "Signpost: \\"Specifically, empirical findings reveal that...\\""
        }},
        E2: {{
          badge: "EXPLANATION (Analytical Reasoning)",
          text: "\\"This disparity arises because decentralized distributed solar grids require domestic labor for maintenance and distribution, preventing capital flight to overseas refineries.\\"",
          color: "#10b981",
          trans: "Signpost: \\"This clearly demonstrates that...\\""
        }},
        L: {{
          badge: "LINK (Connection to Broader Thesis)",
          text: "\\"Consequently, prioritizing green infrastructure not only fulfills environmental mandates but serves as a vital catalyst for equitable domestic economic revival.\\"",
          color: "#a855f7",
          trans: "Signpost: \\"Therefore, in addition to environmental dividends...\\""
        }}
      }};

      document.getElementById('peelSelect').addEventListener('change', (e) => {{
        const d = peelData[e.target.value];
        document.getElementById('peelBadge').textContent = d.badge;
        document.getElementById('peelBadge').setAttribute('fill', d.color);
        document.getElementById('peelText').textContent = d.text;
        document.getElementById('peelTransition').textContent = d.trans;
      }});
    }}

    // 7. Rhetoric Mixer (Ethos, Pathos, Logos)
    function renderRhetoricSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#070b14" stroke="#6366f1" stroke-width="1.5" />
        <text x="220" y="45" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">ARISTOTELIAN PERSUASION TRIANGLE</text>
        
        <!-- Triangle Graphic -->
        <polygon points="220,65 100,175 340,175" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="2" />
        <text x="220" y="80" fill="#a855f7" font-size="11" font-weight="bold" text-anchor="middle">ETHOS (Credibility)</text>
        <text x="80" y="190" fill="#f43f5e" font-size="11" font-weight="bold">PATHOS (Emotion)</text>
        <text x="360" y="190" fill="#06b6d4" font-size="11" font-weight="bold" text-anchor="end">LOGOS (Logic)</text>

        <!-- Persuasion Score HUD -->
        <rect x="35" y="205" width="370" height="42" rx="6" fill="#0f172a" stroke="#10b981" />
        <text id="rhetoricScore" x="220" y="231" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Persuasive Impact Index: 85% (Balanced & Potent)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Ethos (Authority & Integrity):</span>
          <input type="range" id="ethosRange" min="10" max="100" value="80">
          <span class="control-val" id="ethosVal">80%</span>
        </div>
        <div class="control-row">
          <span>Pathos (Emotional Connection):</span>
          <input type="range" id="pathosRange" min="10" max="100" value="85">
          <span class="control-val" id="pathosVal">85%</span>
        </div>
        <div class="control-row">
          <span>Logos (Statistical Logic):</span>
          <input type="range" id="logosRange" min="10" max="100" value="90">
          <span class="control-val" id="logosVal">90%</span>
        </div>
      `;

      function updateRhetoric() {{
        const e = parseInt(document.getElementById('ethosRange').value);
        const p = parseInt(document.getElementById('pathosRange').value);
        const l = parseInt(document.getElementById('logosRange').value);

        document.getElementById('ethosVal').textContent = `${{e}}%`;
        document.getElementById('pathosVal').textContent = `${{p}}%`;
        document.getElementById('logosVal').textContent = `${{l}}%`;

        const score = Math.round((e * 0.3) + (p * 0.35) + (l * 0.35));
        const hud = document.getElementById('rhetoricScore');
        if (score >= 80) {{
          hud.textContent = `Persuasive Impact Index: ${{score}}% (Masterful Classical Harmony)`;
          hud.setAttribute('fill', '#10b981');
        }} else if (score >= 50) {{
          hud.textContent = `Persuasive Impact Index: ${{score}}% (Moderate; Needs Stronger Evidence)`;
          hud.setAttribute('fill', '#f59e0b');
        }} else {{
          hud.textContent = `Persuasive Impact Index: ${{score}}% (Weak; Unconvincing Argument)`;
          hud.setAttribute('fill', '#f43f5e');
        }}
      }}

      document.getElementById('ethosRange').addEventListener('input', updateRhetoric);
      document.getElementById('pathosRange').addEventListener('input', updateRhetoric);
      document.getElementById('logosRange').addEventListener('input', updateRhetoric);
    }}

    // 8. Letter Builder Studio
    function renderLetterSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="15" width="400" height="250" rx="8" fill="#f8fafc" stroke="#94a3b8" />
        <!-- Letter Sheet Simulator -->
        <g fill="#0f172a" font-size="8.5" font-family="monospace">
          <text x="35" y="35" font-weight="bold">42, Shanti Vihar, New Delhi - 110092</text>
          <text x="35" y="50">28 October 2026</text>
          
          <text x="35" y="70" font-weight="bold">The Municipal Commissioner,</text>
          <text x="35" y="82">South Delhi Municipal Corporation, New Delhi</text>
          
          <text x="35" y="102" font-weight="bold" fill="#0369a1">Subject: Complaint regarding malfunctioning streetlights</text>
          <text x="35" y="118">Sir / Madam,</text>
          
          <text x="35" y="134">Through this letter, I wish to draw your immediate attention towards...</text>
          <text x="35" y="146">For the past three weeks, our streetlights have remained unlit, creating...</text>
          <text x="35" y="158">I request you to kindly deploy an inspection team to rectify the issue.</text>
          
          <text x="35" y="180">Thanking you,</text>
          <text x="35" y="195" font-weight="bold">Yours faithfully,</text>
          <text x="35" y="208">Ananya Sharma</text>
        </g>
        
        <!-- Format Annotation Tag -->
        <rect x="250" y="215" width="160" height="24" rx="4" fill="#1e1b4b" stroke="#6366f1" />
        <text x="330" y="231" fill="#c7d2fe" font-size="9" font-weight="bold" text-anchor="middle">Full-Block Left Alignment ✓</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Letter Format Template:</span>
          <select id="letterFormatSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="formal_complaint">Formal Letter of Complaint</option>
            <option value="editor">Letter to the Newspaper Editor</option>
            <option value="informal">Informal Letter to Friend</option>
          </select>
        </div>
      `;

      document.getElementById('letterFormatSelect').addEventListener('change', (e) => {{
        // Update letter preview dynamically
      }});
    }}

    // 9. Notice Board Canvas
    function renderNoticeSim(svg, controls) {{
      svg.innerHTML = `
        <!-- Outer Notice Box Border (Mandatory) -->
        <rect x="20" y="15" width="400" height="250" rx="4" fill="#020617" stroke="#38bdf8" stroke-width="2.5" />
        
        <!-- Header: Organization -->
        <text x="220" y="42" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">DELHI PUBLIC SCHOOL, R.K. PURAM</text>
        <text x="220" y="65" fill="#f59e0b" font-size="15" font-weight="900" letter-spacing="3" text-anchor="middle">NOTICE</text>
        
        <!-- Date -->
        <text x="35" y="88" fill="#94a3b8" font-size="9.5">Date: 28 October 2026</text>
        
        <!-- Topic Heading -->
        <text id="noticeHeading" x="220" y="110" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">INTER-SCHOOL SCIENCE EXHIBITION 2026</text>
        <line x1="100" y1="115" x2="340" y2="115" stroke="#38bdf8" stroke-width="1" />
        
        <!-- Body (5 W's) -->
        <foreignObject x="35" y="125" width="370" height="85">
          <div xmlns="http://www.w3.org/1999/xhtml" id="noticeBodyText" style="color:#e2e8f0; font-size:10px; line-height:1.45;">
            Students of Classes IX and X are hereby informed that the Annual Inter-School Science Exhibition will be held on 15 November 2026 in the Senior Auditorium from 9:00 AM to 3:00 PM. Interested teams must submit their working model abstracts to the undersigned by 5 November.
          </div>
        </foreignObject>
        
        <!-- Signatory Block -->
        <text x="35" y="230" fill="#fff" font-size="9.5" font-weight="bold">Rohan Verma</text>
        <text x="35" y="244" fill="#94a3b8" font-size="9">Science Club Secretary</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Notice Category:</span>
          <select id="noticeTypeSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="science_fest">Event: Inter-School Science Exhibition</option>
            <option value="lost_found">Lost & Found: Titan Wristwatch</option>
            <option value="debate">Competition: Inter-House Debate</option>
          </select>
        </div>
      `;

      document.getElementById('noticeTypeSelect').addEventListener('change', (e) => {{
        const heading = document.getElementById('noticeHeading');
        const body = document.getElementById('noticeBodyText');
        if (e.target.value === 'lost_found') {{
          heading.textContent = 'FOUND: TITAN WRISTWATCH';
          body.textContent = "A black leather-strapped Titan analog wristwatch was found near the basketball court on 27 October during the lunch interval. The rightful owner may claim it from the Vice Principal's office after providing proof of ownership within three days.";
        }} else if (e.target.value === 'debate') {{
          heading.textContent = 'INTER-HOUSE DEBATE COMPETITION';
          body.textContent = 'The English Literary Society is organizing the Inter-House Debate Competition on 10 November 2026 in the school library at 10:00 AM. Motion: "Digital Media Fosters True Learning". Two participants per house may register with the undersigned by 2 November.';
        }} else {{
          heading.textContent = 'INTER-SCHOOL SCIENCE EXHIBITION 2026';
          body.textContent = 'Students of Classes IX and X are hereby informed that the Annual Inter-School Science Exhibition will be held on 15 November 2026 in the Senior Auditorium from 9:00 AM to 3:00 PM. Interested teams must submit their working model abstracts to the undersigned by 5 November.';
        }}
      }});
    }}

    // 10. Invitation & RSVP Studio
    function renderInvitationSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="25" y="20" width="390" height="240" rx="10" fill="#111827" stroke="#f59e0b" stroke-width="2" />
        <rect x="35" y="30" width="370" height="220" rx="8" fill="none" stroke="#f59e0b" stroke-dasharray="4 2" />
        
        <text x="220" y="55" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">The Principal, Staff &amp; Students of</text>
        <text x="220" y="75" fill="#fff" font-size="13" font-weight="900" text-anchor="middle">ST. XAVIER'S SENIOR SECONDARY SCHOOL</text>
        <text x="220" y="95" fill="#cbd5e1" font-size="10" font-style="italic" text-anchor="middle">solicit the pleasure of your benign company on the occasion of</text>
        
        <text x="220" y="120" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">ANNUAL ATHLETIC MEET 2026</text>
        
        <text x="220" y="145" fill="#e2e8f0" font-size="10" text-anchor="middle">on Saturday, 14 November 2026 at 9:30 AM</text>
        <text x="220" y="162" fill="#e2e8f0" font-size="10" text-anchor="middle">Venue: School Athletic Stadium, Civil Lines</text>
        
        <text x="220" y="185" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Chief Guest: Smt. P.T. Usha (Member of Parliament)</text>
        
        <text x="50" y="225" fill="#94a3b8" font-size="9" font-weight="bold">R.S.V.P.</text>
        <text x="50" y="238" fill="#cbd5e1" font-size="8">Ph: 011-23847291</text>
        <text x="380" y="238" fill="#94a3b8" font-size="8" text-anchor="end">Admit One • Please be seated by 9:00 AM</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Reply Generator:</span>
          <select id="rsvpSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="accept">Formal Acceptance Reply</option>
            <option value="regret">Formal Regret (Declining) Reply</option>
          </select>
        </div>
        <div id="rsvpReplyBox" style="background:#0f172a; border:1px solid #38bdf8; border-radius:6px; padding:10px; font-size:10px; color:#e0e7ff;">
          "Mrs. &amp; Mr. R.K. Mehra thank the Principal and Staff of St. Xavier's School for their cordial invitation to the Annual Athletic Meet on 14 November 2026 and are delighted to confirm their attendance."
        </div>
      `;

      document.getElementById('rsvpSelect').addEventListener('change', (e) => {{
        const box = document.getElementById('rsvpReplyBox');
        if (e.target.value === 'regret') {{
          box.innerHTML = `"Dr. S. Nair thanks the Principal and Staff for their kind invitation to the Annual Athletic Meet on 14 November 2026, but deeply regrets his inability to attend due to a prior academic conference. He conveys his warmest wishes for the event's grand success."`;
        }} else {{
          box.innerHTML = `"Mrs. &amp; Mr. R.K. Mehra thank the Principal and Staff of St. Xavier's School for their cordial invitation to the Annual Athletic Meet on 14 November 2026 and are delighted to confirm their attendance."`;
        }}
      }});
    }}

    // 11. Podium Speech Simulator
    function renderSpeechSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0b0f19" stroke="#6366f1" stroke-width="1.5" />
        
        <!-- Podium Graphic -->
        <polygon points="180,240 260,240 245,150 195,150" fill="#334155" stroke="#475569" />
        <rect x="180" y="140" width="80" height="15" rx="3" fill="#1e293b" />
        <!-- Microphones -->
        <line x1="205" y1="140" x2="195" y2="120" stroke="#94a3b8" stroke-width="2" />
        <circle cx="195" cy="120" r="3" fill="#f43f5e" />
        <line x1="235" y1="140" x2="245" y2="120" stroke="#94a3b8" stroke-width="2" />
        <circle cx="245" cy="120" r="3" fill="#f43f5e" />

        <!-- Speech Teleprompter Box -->
        <rect x="35" y="35" width="370" height="75" rx="8" fill="#1e1b4b" stroke="#06b6d4" />
        <foreignObject x="45" y="42" width="350" height="60">
          <div xmlns="http://www.w3.org/1999/xhtml" id="teleprompterText" style="color:#e0e7ff; font-size:11px; line-height:1.45; font-weight:600;">
            "Respected Principal, teachers, and dear friends: Imagine waking up to discover that the world had run out of clean drinking water..."
          </div>
        </foreignObject>

        <!-- Delivery Pacing Meter -->
        <text id="paceText" x="220" y="215" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Pacing: 140 words/min (Optimal Broadcast Delivery)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Rhetorical Hook Strategy:</span>
          <select id="speechHookSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="question">Provocative Hypothetical Question</option>
            <option value="statistic">Shocking Empirical Statistic</option>
            <option value="story">Poignant Personal Narrative Vignette</option>
          </select>
        </div>
      `;

      document.getElementById('speechHookSelect').addEventListener('change', (e) => {{
        const t = document.getElementById('teleprompterText');
        if (e.target.value === 'statistic') {{
          t.innerHTML = '"According to the World Bank, over two billion people lack safely managed drinking water at home. Every single minute, three children succumb to waterborne diseases..."';
        }} else if (e.target.value === 'story') {{
          t.innerHTML = '"Last summer in my ancestral village, I watched an eight-year-old girl walk five kilometers under a blistering 45-degree sun carrying a brass pot of murky well water..."';
        }} else {{
          t.innerHTML = '"Respected Principal, teachers, and dear friends: Imagine waking up to discover that the world had run out of clean drinking water..."';
        }}
      }});
    }}

    // 12. Empathetic Condolence Simulator
    function renderCondolenceSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="1.5" />
        <text x="220" y="48" fill="#d8b4fe" font-size="13" font-weight="bold" text-anchor="middle">EMPATHETIC CONDOLENCE MESSAGE STUDIO</text>
        
        <!-- Sensitivity Analyzer Card -->
        <rect x="35" y="70" width="370" height="120" rx="8" fill="#1e1b4b" stroke="#c084fc" />
        <foreignObject x="45" y="80" width="350" height="100">
          <div xmlns="http://www.w3.org/1999/xhtml" id="condolenceBody" style="color:#e9d5ff; font-size:11px; line-height:1.5;">
            "I was deeply saddened to hear of the sudden passing of your beloved mother. Her gentle warmth, wisdom, and comforting smile touched everyone who knew her. May cherished memories bring peace to your grieving heart."
          </div>
        </foreignObject>

        <!-- Etiquette Checklist HUD -->
        <rect x="35" y="205" width="370" height="40" rx="6" fill="#042f2e" stroke="#10b981" />
        <text id="empathyScore" x="220" y="230" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Sensitivity Rating: 100% (Dignified & Sincere)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Test Phrasing Sensitivity:</span>
          <select id="condolenceSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="dignified">Dignified Tribute (Celebrates Specific Virtues)</option>
            <option value="cliche">Cliché Trap ("I know exactly how you feel")</option>
            <option value="insensitive">Insensitive Platitude ("It was for the best")</option>
          </select>
        </div>
      `;

      document.getElementById('condolenceSelect').addEventListener('change', (e) => {{
        const b = document.getElementById('condolenceBody');
        const s = document.getElementById('empathyScore');
        if (e.target.value === 'cliche') {{
          b.innerHTML = `"Hey, I know exactly how you feel! Don't worry, you'll move on soon enough."`;
          s.textContent = 'FLAGGED: Avoid "I know how you feel" (Minimizes individual grief!)';
          s.setAttribute('fill', '#f59e0b');
        }} else if (e.target.value === 'insensitive') {{
          b.innerHTML = `"Everything happens for a reason, so it was probably for the best. Try not to feel bad."`;
          s.textContent = 'REJECTED: Highly Insensitive & Dismissive Platitude!';
          s.setAttribute('fill', '#f43f5e');
        }} else {{
          b.innerHTML = `"I was deeply saddened to hear of the sudden passing of your beloved mother. Her gentle warmth, wisdom, and comforting smile touched everyone who knew her. May cherished memories bring peace to your grieving heart."`;
          s.textContent = 'Sensitivity Rating: 100% (Dignified & Sincere)';
          s.setAttribute('fill', '#10b981');
        }}
      }});
    }}

    // 13. Slogan & Advertisement Simulator
    function renderAdCopySim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#090d16" stroke="#f59e0b" stroke-width="1.5" />
        <text x="220" y="45" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">CLASSIFIED ADVERTISEMENT BOX</text>
        
        <!-- Standard Classified Box -->
        <rect x="40" y="60" width="360" height="130" rx="4" fill="#18181b" stroke="#f59e0b" stroke-width="1.5" />
        <text id="adCategory" x="220" y="82" fill="#fff" font-size="11" font-weight="bold" letter-spacing="1.5" text-anchor="middle">SITUATION VACANT</text>
        <line x1="120" y1="87" x2="320" y2="87" stroke="#f59e0b" stroke-width="1" />
        
        <foreignObject x="50" y="95" width="340" height="85">
          <div xmlns="http://www.w3.org/1999/xhtml" id="adCopyText" style="color:#f4f4f5; font-size:10px; line-height:1.4; font-family:monospace;">
            WANTED: Energetic PGT English teacher for prestigious CBSE school. Candidate must possess M.A. (English), B.Ed., min 5 yrs exp. Remuneration commensurate with merits. Apply with CV within 7 days to Box No. 824, The Hindu, New Delhi.
          </div>
        </foreignObject>

        <!-- Slogan Banner -->
        <rect x="40" y="205" width="360" height="40" rx="6" fill="#1e1b4b" stroke="#38bdf8" />
        <text id="sloganDisplay" x="220" y="230" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">SLOGAN: "Plant Plastic-Free Pathways!"</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Ad Copy Category:</span>
          <select id="adSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="vacant">Situation Vacant</option>
            <option value="sale">For Sale (Automobile)</option>
            <option value="lost">Lost & Found</option>
          </select>
        </div>
      `;

      document.getElementById('adSelect').addEventListener('change', (e) => {{
        const cat = document.getElementById('adCategory');
        const text = document.getElementById('adCopyText');
        if (e.target.value === 'sale') {{
          cat.textContent = 'FOR SALE';
          text.textContent = 'FOR SALE: 2022 Honda City ZX, white, single owner, driven 24,000 km, fully insured, pristine mechanical condition, power steering, alloy wheels. Expected price ₹9.5 Lakhs (negotiable). Contact Rajesh, Ph: 98102XXXXX.';
        }} else if (e.target.value === 'lost') {{
          cat.textContent = 'LOST AND FOUND';
          text.textContent = 'LOST: Black leather document folder containing Class X certificates and passport in Delhi Metro Yellow Line on 27 Oct at 5 PM. Finder will be suitably rewarded. Kindly contact Priya at 98711XXXXX.';
        }} else {{
          cat.textContent = 'SITUATION VACANT';
          text.textContent = 'WANTED: Energetic PGT English teacher for prestigious CBSE school. Candidate must possess M.A. (English), B.Ed., min 5 yrs exp. Remuneration commensurate with merits. Apply with CV within 7 days to Box No. 824, The Hindu, New Delhi.';
        }}
      }});
    }}

    // 14. Magazine Article Newsroom Simulator
    function renderArticleSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="15" width="400" height="250" rx="8" fill="#f8fafc" stroke="#334155" />
        
        <!-- Newspaper Header -->
        <text x="220" y="40" fill="#0f172a" font-size="13" font-weight="900" text-anchor="middle">The Digital Mirage: Is Screen Addiction Stealing Our Youth?</text>
        <text x="220" y="55" fill="#475569" font-size="9" font-style="italic" text-anchor="middle">By Kabir Verma, Class IX-A (Student Editor)</text>
        <line x1="40" y1="62" x2="400" y2="62" stroke="#cbd5e1" stroke-width="1.5" />

        <!-- 2 Column Newspaper Print Layout -->
        <foreignObject x="35" y="70" width="175" height="180">
          <div xmlns="http://www.w3.org/1999/xhtml" style="color:#0f172a; font-size:8.5px; line-height:1.4; text-align:justify;">
            Walk into any classroom, park, or living room today, and you will witness a silent epidemic: heads tilted downward, pupils illuminated by the cold blue glow of handheld screens. What was envisioned as an informational superhighway has morphed into a digital labyrinth. According to recent surveys, Indian adolescents spend an average of six hours daily on non-academic screen scrolling.
          </div>
        </foreignObject>

        <foreignObject x="225" y="70" width="175" height="180">
          <div xmlns="http://www.w3.org/1999/xhtml" style="color:#0f172a; font-size:8.5px; line-height:1.4; text-align:justify;">
            The ramifications are alarming: disrupted sleep cycles, dwindling attention spans, and an unprecedented erosion of interpersonal face-to-face empathy. Yet, the remedy is not reactionary technophobia, but digital mindfulness. Schools must institute mandatory screen-free sports hours and cultivate deep offline reading habits.
          </div>
        </foreignObject>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Article Editorial Angle:</span>
          <select id="angleSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="tech">Digital Addiction & Mental Health</option>
            <option value="climate">Climate Action & Youth Movements</option>
          </select>
        </div>
      `;
    }}

    // 15. AV Digital Script Teleprompter
    function renderAvScriptSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#020617" stroke="#38bdf8" stroke-width="1.5" />
        <text x="220" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">TWO-COLUMN AUDIO-VISUAL (AV) BROADCAST SCRIPT</text>
        
        <!-- Column Dividing Line -->
        <line x1="200" y1="55" x2="200" y2="245" stroke="#334155" stroke-width="1.5" stroke-dasharray="3 3" />
        <text x="110" y="70" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">VIDEO / VISUAL CUES</text>
        <text x="310" y="70" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">AUDIO / DIALOGUE &amp; SFX</text>
        
        <foreignObject x="30" y="80" width="160" height="150">
          <div xmlns="http://www.w3.org/1999/xhtml" style="color:#cbd5e1; font-size:8.5px; line-height:1.4;">
            <strong>[0:00 - 0:08]</strong><br/>
            WIDE SHOT (WS): Misty Himalayan ridge at sunrise. Drone camera slowly pans left.<br/><br/>
            <strong>[0:08 - 0:15]</strong><br/>
            CLOSE UP (CU): Weathered hands of an elderly tea farmer sorting green leaves into a wicker basket.
          </div>
        </foreignObject>

        <foreignObject x="210" y="80" width="190" height="150">
          <div xmlns="http://www.w3.org/1999/xhtml" style="color:#a7f3d0; font-size:8.5px; line-height:1.4;">
            <strong>[SFX: Gentle morning breeze whistling; distant temple bells chiming]</strong><br/><br/>
            <strong>NARRATOR (VO):</strong> "Long before dawn touches the cities of the plains, the silence of the mountains yields to a centuries-old tradition..."
          </div>
        </foreignObject>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Script Teleprompter Mode:</span>
          <button class="sim-action-btn" onclick="alert('Teleprompter running at 140 WPM.')">▶ Run Teleprompter Sync</button>
        </div>
      `;
    }}

    // 16. Email Netiquette Simulator
    function renderEmailSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="15" width="400" height="250" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5" />
        
        <!-- Email Header Fields -->
        <g fill="#94a3b8" font-size="9">
          <text x="35" y="38" font-weight="bold">To:</text>
          <text x="65" y="38" fill="#e2e8f0">director.olympiad@scienceindia.org</text>
          
          <text x="35" y="55" font-weight="bold">Subject:</text>
          <text id="emailSubj" x="80" y="55" fill="#38bdf8" font-weight="bold">Inquiry Regarding Youth Science Olympiad Eligibility — Rohan Verma</text>
          
          <text x="35" y="72" font-weight="bold">Attachment:</text>
          <text x="100" y="72" fill="#10b981">📎 Rohan_Verma_Project_Abstract.pdf (1.2 MB)</text>
        </g>
        <line x1="30" y1="80" x2="410" y2="80" stroke="#334155" />

        <!-- Email Body -->
        <foreignObject x="35" y="85" width="370" height="120">
          <div xmlns="http://www.w3.org/1999/xhtml" id="emailBodyText" style="color:#e2e8f0; font-size:9.5px; line-height:1.45;">
            Dear Dr. Sen,<br/><br/>
            I am writing to respectfully inquire about the eligibility criteria for the upcoming National Youth Science Olympiad 2026. I am a Class IX student at Delhi Public School and have developed a working solar desalination prototype.<br/><br/>
            Please find attached my project abstract for your preliminary perusal. I look forward to your guidance.<br/><br/>
            Warm regards,<br/>
            <strong>Rohan Verma</strong> | Class IX-B
          </div>
        </foreignObject>

        <!-- Netiquette Audit Tag -->
        <rect x="35" y="215" width="370" height="35" rx="6" fill="#042f2e" stroke="#10b981" />
        <text id="netiquetteScore" x="220" y="237" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Netiquette Audit: 100% Passed (Polite, Specific Subject, Safe Attachment)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span>Netiquette Audit Test:</span>
          <select id="emailTestSelect" style="background:#0f172a; color:#fff; padding:6px 10px; border-radius:6px; border:1px solid #475569;">
            <option value="prof">Professional Formal Inquiry</option>
            <option value="caps">All-Caps Violation (Shouting)</option>
            <option value="vague">Vague Subject Line &amp; Unnamed Attachment</option>
          </select>
        </div>
      `;

      document.getElementById('emailTestSelect').addEventListener('change', (e) => {{
        const s = document.getElementById('emailSubj');
        const b = document.getElementById('emailBodyText');
        const audit = document.getElementById('netiquetteScore');
        if (e.target.value === 'caps') {{
          s.textContent = 'URGENT ANSWER ME RIGHT NOW!!!!!';
          b.innerHTML = 'WHY HAVENT YOU REPLIED TO MY EMAIL YET??? I NEED TO KNOW THE DATES IMMEDIATELY!!!!';
          audit.textContent = 'FAILED: All-Caps Shouting & Aggressive Tone Violation!';
          audit.setAttribute('fill', '#f43f5e');
        }} else if (e.target.value === 'vague') {{
          s.textContent = 'Help';
          b.innerHTML = 'Hey, check this out and tell me what you think. See attachment.';
          audit.textContent = 'FAILED: Vague Subject Line & Casual Greeting in Professional Context';
          audit.setAttribute('fill', '#f59e0b');
        }} else {{
          s.textContent = 'Inquiry Regarding Youth Science Olympiad Eligibility — Rohan Verma';
          b.innerHTML = 'Dear Dr. Sen,<br/><br/>I am writing to respectfully inquire about the eligibility criteria for the upcoming National Youth Science Olympiad 2026. I am a Class IX student at Delhi Public School and have developed a working solar desalination prototype.<br/><br/>Please find attached my project abstract for your preliminary perusal. I look forward to your guidance.<br/><br/>Warm regards,<br/><strong>Rohan Verma</strong> | Class IX-B';
          audit.textContent = 'Netiquette Audit: 100% Passed (Polite, Specific Subject, Safe Attachment)';
          audit.setAttribute('fill', '#10b981');
        }}
      }});
    }}

    // Quiz Dashboard Simulator
    function renderQuizDashboardSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="20" y="20" width="400" height="240" rx="10" fill="#0f172a" stroke="#6366f1" stroke-width="1.5" />
        <text x="220" y="55" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">ENGLISH COMMUNICATION MASTERY CHALLENGE</text>
        <circle cx="220" cy="125" r="45" fill="none" stroke="#6366f1" stroke-width="8" stroke-dasharray="280" stroke-dashoffset="40" />
        <text x="220" y="132" fill="#06b6d4" font-size="16" font-weight="bold" text-anchor="middle">40 Qs</text>
        <text x="220" y="195" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Comprehensive Competency Assessment (CG-1)</text>
        <text x="220" y="225" fill="#94a3b8" font-size="10" text-anchor="middle">Select your answers and click "View Solution" for detailed teacher rubrics.</text>
      `;
      controls.innerHTML = `
        <div style="text-align: center; color: #94a3b8; font-size: 0.85rem; padding: 10px;">
          Active Challenge Section: Review solutions to reinforce key communication rules.
        </div>
      `;
    }}

  </script>
</body>
</html>
"""
    output_path = "public/animations/class9-english-communication-writing.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Successfully generated {output_path} ({len(html_template)} bytes).")

if __name__ == "__main__":
    generate_lab_html()
