# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 8 Mathematics Chapter 2:
Introduction to Linear Polynomials (Mathematics Grade 8)
Produces: public/animations/class8-math-linear-polynomials.html
Features:
- 20 Full Slides (16 Comprehensive Interactive Lessons + 4 Dedicated Quiz Slides)
- 32 In-Slide Checkpoints (2 per lesson slide) with immediate teacher feedback
- 40 Comprehensive Quiz Questions (10 per quiz slide) with "View Solution" modal popups
- Prof. Ramanujan Sharma Talking Avatar with Web Speech API audio narration and animated mouth
- 16 High-Fidelity Interactive SVG Simulators covering all syllabus sections (2.1 to 2.6, End Exercises & Summary)
- Strict last-slide notice on slide 20 with hidden nextBtn
- Responsive, robust CSS styling matching all project guidelines
"""

import os
import json
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from class8_math_linear_polynomials_data import slides_data, quiz_questions

def generate_lab_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="triggerMathRender(document.body);"></script>
  <title>NCERT Class 8 Mathematics • Chapter 2: Introduction to Linear Polynomials Master Lab</title>
  
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
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top Navigation */
    .top-nav {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid rgba(99, 102, 241, 0.3);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 40;
      backdrop-filter: blur(10px);
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .badge-class {{
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 9999px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.4);
    }}

    .nav-title {{
      font-size: 15px;
      font-weight: 700;
      color: #f1f5f9;
      letter-spacing: -0.01em;
    }}

    .slide-progress {{
      font-size: 13px;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 4px 12px;
      border-radius: 20px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    /* Main Container */
    .lab-container {{
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      padding: 20px;
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 24px;
      min-width: 0;
    }}

    @media (max-width: 1100px) {{
      .lab-container {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Left / Main Workspace */
    .slide-workspace {{
      display: flex;
      flex-direction: column;
      gap: 20px;
      min-width: 0;
    }}

    .slide-header {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px 24px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }}

    .slide-number-tag {{
      display: inline-block;
      font-size: 12px;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }}

    .slide-title {{
      font-size: 24px;
      font-weight: 800;
      color: #fff;
      line-height: 1.3;
      margin-bottom: 6px;
    }}

    .slide-subtitle {{
      font-size: 14px;
      color: var(--text-muted);
      font-weight: 500;
    }}

    /* Content Cards */
    .slide-body {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
      font-size: 14px;
      color: #cbd5e1;
      min-width: 0;
      overflow-wrap: break-word;
    }}

    /* KaTeX math enhancements */
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

    .lead-p {{
      font-size: 15px;
      line-height: 1.7;
      color: #e2e8f0;
      margin-bottom: 16px;
    }}

    .theory-box {{
      background: rgba(30, 41, 59, 0.6);
      border-left: 4px solid var(--accent-indigo);
      border-radius: 0 12px 12px 0;
      padding: 16px 20px;
      margin-bottom: 20px;
    }}

    .theory-box h4 {{
      color: #a5b4fc;
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 8px;
    }}

    .grid-2col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 20px;
      min-width: 0;
    }}

    @media (max-width: 768px) {{
      .grid-2col {{
        grid-template-columns: 1fr;
      }}
    }}

    .card-item {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 16px;
      min-width: 0;
    }}

    .card-item h4, .card-item h5 {{
      color: #38bdf8;
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
    }}

    .card-item ul, .theory-box ul {{
      padding-left: 20px;
      margin-top: 6px;
      margin-bottom: 6px;
    }}

    .card-item li, .theory-box li {{
      margin-bottom: 5px;
      line-height: 1.5;
    }}

    .highlight-eq {{
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid rgba(99, 102, 241, 0.4);
      color: #c7d2fe;
      padding: 8px 14px;
      border-radius: 8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      font-weight: 600;
      margin: 10px 0;
      text-align: center;
      overflow-x: auto;
    }}

    /* Simulator Panel */
    .sim-panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      gap: 14px;
      min-width: 0;
    }}

    .sim-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sim-title {{
      font-size: 14px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .sim-viewport {{
      width: 100%;
      height: 320px;
      background: #020617;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      overflow: hidden;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .sim-svg {{
      width: 100%;
      height: 100%;
    }}

    .sim-controls {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      background: rgba(15, 23, 42, 0.8);
      padding: 12px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .control-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      width: 100%;
    }}

    .slider-label {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      min-width: 140px;
    }}

    .sim-slider {{
      flex: 1;
      accent-color: var(--accent-indigo);
      cursor: pointer;
    }}

    .slider-val {{
      font-size: 12px;
      font-weight: 700;
      color: #38bdf8;
      min-width: 50px;
      text-align: right;
    }}

    .sim-btn {{
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .sim-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.4);
    }}

    /* Checkpoints Section */
    .checkpoint-section {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }}

    .checkpoint-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      font-weight: 800;
      color: #10b981;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
    }}

    .checkpoint-card {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 14px;
    }}

    .checkpoint-q {{
      font-size: 13px;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 12px;
      line-height: 1.5;
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

    .opt-btn {{
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
    }}

    .opt-btn:hover {{
      background: rgba(51, 65, 85, 0.8);
      border-color: rgba(99, 102, 241, 0.4);
    }}

    .opt-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: #10b981 !important;
      color: #34d399 !important;
    }}

    .opt-btn.wrong {{
      background: rgba(244, 63, 94, 0.2) !important;
      border-color: #f43f5e !important;
      color: #fb7185 !important;
    }}

    .feedback-box {{
      margin-top: 10px;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 12px;
      line-height: 1.5;
      display: none;
    }}

    .feedback-box.show {{
      display: block;
    }}

    /* Dedicated Quiz Questions Grid */
    .quiz-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      margin-top: 14px;
    }}

    .quiz-card {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(99, 102, 241, 0.25);
      border-radius: 12px;
      padding: 18px;
    }}

    .quiz-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .quiz-badge {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(99, 102, 241, 0.2);
      color: #a5b4fc;
    }}

    .sol-btn {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s ease;
    }}

    .sol-btn:hover {{
      background: rgba(245, 158, 11, 0.3);
      transform: translateY(-1px);
    }}

    /* Right Sidebar / Teacher Avatar */
    .teacher-pane {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .avatar-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 20px;
      text-align: center;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }}

    .avatar-frame {{
      width: 120px;
      height: 120px;
      margin: 0 auto 12px;
      background: radial-gradient(circle, #0c4a6e 0%, #0f172a 75%);
      border: 2px solid #0284c7;
      border-radius: 50%;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4);
    }}

    .teacher-title {{
      font-size: 15px;
      font-weight: 800;
      color: #fff;
    }}

    .teacher-role {{
      font-size: 12px;
      color: #38bdf8;
      font-weight: 600;
      margin-bottom: 12px;
    }}

    .speech-bubble {{
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 14px;
      font-size: 13px;
      color: #e2e8f0;
      line-height: 1.5;
      text-align: left;
      position: relative;
      margin-bottom: 14px;
    }}

    .speech-bubble::before {{
      content: "";
      position: absolute;
      top: -8px;
      left: 50%;
      transform: translateX(-50%);
      border-width: 0 8px 8px 8px;
      border-style: solid;
      border-color: transparent transparent rgba(30, 41, 59, 0.8) transparent;
    }}

    .voice-btn {{
      width: 100%;
      background: linear-gradient(135deg, #059669, #10b981);
      color: #fff;
      border: none;
      padding: 10px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
    }}

    .voice-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(16, 185, 129, 0.5);
    }}

    /* Bottom Navigation Bar */
    .bottom-nav {{
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid rgba(99, 102, 241, 0.3);
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      bottom: 0;
      z-index: 40;
      backdrop-filter: blur(10px);
    }}

    .nav-btn {{
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #fff;
      padding: 10px 20px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .nav-btn:hover:not(:disabled) {{
      background: var(--accent-indigo);
      border-color: var(--accent-indigo);
      transform: translateY(-1px);
    }}

    .nav-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .last-slide-notice {{
      display: none;
      color: #10b981;
      font-size: 13px;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.15);
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    /* Solution Pop-up Modal */
    .modal-backdrop {{
      background: rgba(2, 6, 23, 0.85);
      backdrop-filter: blur(8px);
    }}

    .hidden {{
      display: none !important;
    }}
  </style>
</head>
<body>

  <!-- Top Nav -->
  <header class="top-nav">
    <div class="nav-brand">
      <span class="badge-class">Grade 8 • NCERT</span>
      <span class="nav-title">Introduction to Linear Polynomials • Mathematics Chapter 2</span>
    </div>
    <div class="slide-progress" id="slideProgressIndicator">Slide 1 of 20</div>
  </header>

  <!-- Main Container -->
  <main class="lab-container">
    
    <!-- Left: Slide Workspace -->
    <div class="slide-workspace">
      
      <!-- Slide Header -->
      <section class="slide-header">
        <span class="slide-number-tag" id="slideTag">Lesson 1 of 20</span>
        <h1 class="slide-title" id="slideTitle">2.1 Introduction to Algebraic Expressions & Patterns</h1>
        <p class="slide-subtitle" id="slideSubtitle">From Arithmetic Sequences to General Algebraic Formulas</p>
      </section>

      <!-- Slide Main Theory Body -->
      <article class="slide-body" id="slideContent">
        <!-- Injected via JS -->
      </article>

      <!-- Bespoke Simulator Container -->
      <section class="sim-panel" id="simulatorPanel">
        <div class="sim-header">
          <div class="sim-title">
            <span>⚙️</span> <span id="simTitle">Interactive Simulation</span>
          </div>
        </div>
        <div class="sim-viewport">
          <svg class="sim-svg" id="simSvg" viewBox="0 0 600 320"></svg>
        </div>
        <div class="sim-controls" id="simControls">
          <!-- Injected via JS -->
        </div>
      </section>

      <!-- Checkpoint Container (Slides 1-16) -->
      <section class="checkpoint-section" id="checkpointContainer">
        <div class="checkpoint-header">
          <span>🎯</span> In-Slide Checkpoint Questions
        </div>
        <div id="checkpointsList">
          <!-- Injected via JS -->
        </div>
      </section>

    </div>

    <!-- Right: Mentor Talking Avatar -->
    <aside class="teacher-pane">
      <div class="avatar-card">
        <div class="avatar-frame">
          <svg viewBox="0 0 100 100" width="100" height="100">
            <!-- Background Halo -->
            <circle cx="50" cy="50" r="48" fill="#0c4a6e" stroke="#0284c7" stroke-width="2" />
            <!-- Traditional Achkan / Coat -->
            <path d="M20 95 Q50 82 80 95 L85 100 L15 100 Z" fill="#0369a1" />
            <!-- Collar / Scarf -->
            <path d="M42 82 L50 88 L58 82 L50 98 Z" fill="#38bdf8" />
            <!-- Neck -->
            <rect x="44" y="65" width="12" height="18" fill="#fed7aa" rx="3" />
            <!-- Head -->
            <ellipse cx="50" cy="48" rx="22" ry="24" fill="#fed7aa" />
            <!-- Neat Scholar Haircut -->
            <path d="M28 42 C26 22, 74 22, 72 42 C72 32, 28 32, 28 42 Z" fill="#1e293b" />
            <path d="M27 42 C25 55, 30 65, 33 68 C30 58, 28 48, 27 42 Z" fill="#1e293b" />
            <path d="M73 42 C75 55, 70 65, 67 68 C70 58, 72 48, 73 42 Z" fill="#1e293b" />
            <!-- Classic Round Spectacles -->
            <circle cx="41" cy="45" r="6" fill="none" stroke="#d97706" stroke-width="1.8" />
            <circle cx="59" cy="45" r="6" fill="none" stroke="#d97706" stroke-width="1.8" />
            <line x1="47" y1="45" x2="53" y2="45" stroke="#d97706" stroke-width="1.8" />
            <!-- Expressive Eyes -->
            <circle cx="41" cy="45" r="2" fill="#0f172a" />
            <circle cx="59" cy="45" r="2" fill="#0f172a" />
            <!-- Intellectual Eyebrows -->
            <path d="M35 37 Q41 34 47 37" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round" />
            <path d="M53 37 Q59 34 65 37" fill="none" stroke="#1e293b" stroke-width="2" stroke-linecap="round" />
            <!-- Nose -->
            <path d="M50 46 L48 53 L52 53" fill="none" stroke="#d97706" stroke-width="1.5" />
            <!-- Animated Talking Mouth -->
            <ellipse id="teacherMouth" cx="50" cy="60" rx="4" ry="1.5" fill="#be123c" />
          </svg>
        </div>
        <div class="teacher-title">Mathematics Mentor</div>
        <div class="teacher-role">Senior Mathematics Mentor</div>
        <div class="speech-bubble" id="teacherSpeech">
          Welcome to Chapter 2: Introduction to Linear Polynomials! Let us master the dynamic beauty of constant rate of change and straight line algebra!
        </div>
        <button class="voice-btn" id="voiceToggleBtn" onclick="toggleSpeech()">
          <span id="voiceIcon">🔊</span> <span id="voiceLabel">Play Voiceover</span>
        </button>
      </div>
    </aside>

  </main>

  <!-- Bottom Navigation Bar -->
  <footer class="bottom-nav">
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
        <button onclick="closeSolutionModal()" style="background:#0284c7; color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">Close Solution</button>
      </div>
    </div>
  </div>

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
              {{ left: '\(', right: '\)', display: false }},
              {{ left: '\[', right: '\]', display: true }}
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
            }} else {{
              btn.classList.add('wrong');
              btns[q.correct].classList.add('correct');
              feedback.style.background = 'rgba(244, 63, 94, 0.2)';
              feedback.style.color = '#fb7185';
              feedback.innerHTML = `<strong>✗ Incorrect.</strong> Correct answer is (${{String.fromCharCode(65 + q.correct)}}). Inspect "View Solution" for detailed steps.`;
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
      if (!('speechSynthesis' in window)) {{
        alert('Web Speech API is not supported in this browser.');
        return;
      }}
      synth.cancel();

      const text = slides[currentSlideIndex].voice;
      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.lang = 'en-US';
      currentUtterance.rate = 0.95;
      currentUtterance.pitch = 1.0;

      currentUtterance.onstart = () => {{
        isSpeaking = true;
        document.getElementById('voiceIcon').textContent = '⏹️';
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

      svg.innerHTML = '';
      controls.innerHTML = '';

      switch (type) {{
        case 'matchstick_pattern_builder':
          title.textContent = 'Matchstick Geometric Chain & Expression Modeler (3n + 1)';
          renderMatchstickSim(svg, controls);
          break;
        case 'table_difference_analyzer':
          title.textContent = 'Table Sequence First-Difference Detector';
          renderTableDifferenceSim(svg, controls);
          break;
        case 'polynomial_classifier_engine':
          title.textContent = 'Polynomial Degree & Standard Form Classifier';
          renderClassifierSim(svg, controls);
          break;
        case 'standard_form_transformer':
          title.textContent = 'Standard Form ax + b Normalizer & Zero Calculator';
          renderTransformerSim(svg, controls);
          break;
        case 'rate_of_change_stepper':
          title.textContent = 'Constant Rate of Change Step-Ladder Visualizer';
          renderRateStepperSim(svg, controls);
          break;
        case 'real_world_cost_modeler':
          title.textContent = 'Base Fee + Variable Rate Real-World Cost Engine';
          renderCostModelerSim(svg, controls);
          break;
        case 'growth_decay_comparator':
          title.textContent = 'Linear Growth vs Linear Decay Trajectory Comparator';
          renderGrowthDecaySim(svg, controls);
          break;
        case 'tank_drainage_simulator':
          title.textContent = 'Physical Water Tank Depletion & Domain Boundary Sim';
          renderTankDrainSim(svg, controls);
          break;
        case 'ordered_pair_generator':
          title.textContent = 'Dynamic Ordered Pair (x, y) & Intercept Table';
          renderOrderedPairSim(svg, controls);
          break;
        case 'two_point_slope_calculator':
          title.textContent = 'Two-Point Slope & Coordinate Line Equation Deriver';
          renderTwoPointSlopeSim(svg, controls);
          break;
        case 'interactive_line_grapher':
          title.textContent = 'Dynamic Cartesian Line Grapher (y = ax + b)';
          renderLineGrapherSim(svg, controls);
          break;
        case 'break_even_intersection_sim':
          title.textContent = 'Two-Line Graphical Intersection & Break-Even Analyzer';
          renderBreakEvenSim(svg, controls);
          break;
        case 'rectangle_perimeter_solver':
          title.textContent = 'Geometric Rectangle Dimension & Perimeter Constraint Studio';
          renderPerimeterSolverSim(svg, controls);
          break;
        case 'two_digit_reversal_sim':
          title.textContent = 'Two-Digit Place Value Reversal & Algebra Riddle Solver';
          renderDigitReversalSim(svg, controls);
          break;
        case 'chapter_summary_matrix':
          title.textContent = 'Linear Polynomials Universal Concept & Formula Matrix';
          renderSummaryMatrixSim(svg, controls);
          break;
        case 'historical_timeline_stepper':
          title.textContent = 'Historical Timeline: From Rhind Papyrus to Descartes';
          renderHistorySim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Simulation';
          svg.innerHTML = '<text x="300" y="160" fill="#94a3b8" text-anchor="middle">Interactive Demonstration</text>';
      }}
    }}

    // 1. Matchstick Sim
    function renderMatchstickSim(svg, controls) {{
      function draw(n) {{
        const sticks = 3 * n + 1;
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Adjoining Squares Chain: n = ${{n}} | Total Matchsticks = 3(${{n}}) + 1 = ${{sticks}}</text>
        `;
        const size = Math.min(50, 480 / n);
        const startX = 300 - (n * size) / 2;
        const startY = 110;

        for (let i = 0; i < n; i++) {{
          const x = startX + i * size;
          // Left stick (only for first square)
          if (i === 0) {{
            const left = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            left.setAttribute('x1', x); left.setAttribute('y1', startY);
            left.setAttribute('x2', x); left.setAttribute('y2', startY + size);
            left.setAttribute('stroke', '#f59e0b'); left.setAttribute('stroke-width', '4');
            left.setAttribute('stroke-linecap', 'round');
            svg.appendChild(left);
            const head = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            head.setAttribute('cx', x); head.setAttribute('cy', startY); head.setAttribute('r', '4'); head.setAttribute('fill', '#ef4444');
            svg.appendChild(head);
          }}
          // Top stick
          const top = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          top.setAttribute('x1', x); top.setAttribute('y1', startY);
          top.setAttribute('x2', x + size); top.setAttribute('y2', startY);
          top.setAttribute('stroke', '#38bdf8'); top.setAttribute('stroke-width', '4');
          top.setAttribute('stroke-linecap', 'round');
          svg.appendChild(top);
          // Bottom stick
          const bot = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          bot.setAttribute('x1', x); bot.setAttribute('y1', startY + size);
          bot.setAttribute('x2', x + size); bot.setAttribute('y2', startY + size);
          bot.setAttribute('stroke', '#38bdf8'); bot.setAttribute('stroke-width', '4');
          bot.setAttribute('stroke-linecap', 'round');
          svg.appendChild(bot);
          // Right stick
          const right = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          right.setAttribute('x1', x + size); right.setAttribute('y1', startY);
          right.setAttribute('x2', x + size); right.setAttribute('y2', startY + size);
          right.setAttribute('stroke', '#38bdf8'); right.setAttribute('stroke-width', '4');
          right.setAttribute('stroke-linecap', 'round');
          svg.appendChild(right);
        }}

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '300');
        text.setAttribute('y', '250');
        text.setAttribute('fill', '#10b981');
        text.setAttribute('font-size', '14');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('text-anchor', 'middle');
        text.textContent = `Formula: M(n) = 3n + 1 (Constant difference d = 3 sticks per square)`;
        svg.appendChild(text);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Number of Squares (n):</span>
          <input type="range" class="sim-slider" id="matchSlider" min="1" max="8" value="3">
          <span class="slider-val" id="matchVal">n = 3</span>
        </div>
      `;

      draw(3);
      document.getElementById('matchSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('matchVal').textContent = `n = ${{v}}`;
        draw(v);
      }});
    }}

    // 2. Table Difference Sim
    function renderTableDifferenceSim(svg, controls) {{
      function update(d, c) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Sequence Analysis: Formula T(n) = ${{d}}n + ${{c}}</text>
        `;

        const inputs = [1, 2, 3, 4, 5];
        const outputs = inputs.map(n => d * n + c);

        // Draw Table
        const startX = 60;
        const colW = 95;

        // Header Row
        const hr = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        hr.setAttribute('x', startX); hr.setAttribute('y', '65');
        hr.setAttribute('width', colW * 5); hr.setAttribute('height', '36');
        hr.setAttribute('fill', '#1e293b'); hr.setAttribute('stroke', '#6366f1');
        svg.appendChild(hr);

        inputs.forEach((n, idx) => {{
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', startX + idx * colW + colW / 2);
          t.setAttribute('y', '88');
          t.setAttribute('fill', '#38bdf8');
          t.setAttribute('font-size', '13');
          t.setAttribute('font-weight', 'bold');
          t.setAttribute('text-anchor', 'middle');
          t.textContent = `n = ${{n}}`;
          svg.appendChild(t);
        }});

        // Value Row
        const vr = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        vr.setAttribute('x', startX); vr.setAttribute('y', '101');
        vr.setAttribute('width', colW * 5); vr.setAttribute('height', '45');
        vr.setAttribute('fill', '#0f172a'); vr.setAttribute('stroke', '#6366f1');
        svg.appendChild(vr);

        outputs.forEach((val, idx) => {{
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', startX + idx * colW + colW / 2);
          t.setAttribute('y', '129');
          t.setAttribute('fill', '#f8fafc');
          t.setAttribute('font-size', '16');
          t.setAttribute('font-weight', 'bold');
          t.setAttribute('text-anchor', 'middle');
          t.textContent = val;
          svg.appendChild(t);
        }});

        // First Differences Arcs
        for (let i = 0; i < 4; i++) {{
          const x1 = startX + i * colW + colW / 2;
          const x2 = startX + (i + 1) * colW + colW / 2;
          const midX = (x1 + x2) / 2;
          const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path.setAttribute('d', `M ${{x1}} 155 Q ${{midX}} 190 ${{x2}} 155`);
          path.setAttribute('fill', 'none'); path.setAttribute('stroke', '#f59e0b');
          path.setAttribute('stroke-width', '2');
          svg.appendChild(path);

          const dt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          dt.setAttribute('x', midX); dt.setAttribute('y', '195');
          dt.setAttribute('fill', '#f59e0b'); dt.setAttribute('font-size', '12');
          dt.setAttribute('font-weight', 'bold'); dt.setAttribute('text-anchor', 'middle');
          dt.textContent = (d >= 0 ? `+${{d}}` : `${{d}}`);
          svg.appendChild(dt);
        }}

        const expl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        expl.setAttribute('x', '300'); expl.setAttribute('y', '260');
        expl.setAttribute('fill', '#10b981'); expl.setAttribute('font-size', '13');
        expl.setAttribute('font-weight', 'bold'); expl.setAttribute('text-anchor', 'middle');
        expl.textContent = `Constant First Difference d = ${{d}} ⟹ Linear Term is ${{d}}n ⟹ T(n) = ${{d}}n + ${{c}}`;
        svg.appendChild(expl);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Common Difference (d):</span>
          <input type="range" class="sim-slider" id="diffSlider" min="-5" max="8" value="4">
          <span class="slider-val" id="diffVal">d = 4</span>
          <span class="slider-label" style="min-width:60px; margin-left:15px;">Offset (c):</span>
          <input type="range" class="sim-slider" id="offsetSlider" min="0" max="10" value="1">
          <span class="slider-val" id="offsetVal">c = 1</span>
        </div>
      `;

      update(4, 1);
      const ds = document.getElementById('diffSlider');
      const os = document.getElementById('offsetSlider');

      ds.addEventListener('input', (e) => {{
        const d = parseInt(e.target.value);
        document.getElementById('diffVal').textContent = `d = ${{d}}`;
        update(d, parseInt(os.value));
      }});
      os.addEventListener('input', (e) => {{
        const c = parseInt(e.target.value);
        document.getElementById('offsetVal').textContent = `c = ${{c}}`;
        update(parseInt(ds.value), c);
      }});
    }}

    // 3. Classifier Engine
    function renderClassifierSim(svg, controls) {{
      function test(expr, degree, isLinear, reason) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Polynomial Classifier & Degree Inspector</text>

          <rect x="70" y="70" width="460" height="80" rx="12" fill="#1e293b" stroke="#6366f1" />
          <text x="300" y="118" fill="#fff" font-size="24" font-weight="bold" text-anchor="middle">${{expr}}</text>

          <rect x="70" y="170" width="460" height="110" rx="12" fill="${{isLinear ? 'rgba(16, 185, 129, 0.15)' : 'rgba(244, 63, 94, 0.15)'}}" stroke="${{isLinear ? '#10b981' : '#f43f5e'}}" />
          <text x="300" y="205" fill="${{isLinear ? '#34d399' : '#fb7185'}}" font-size="16" font-weight="bold" text-anchor="middle">
            Classification: ${{isLinear ? 'LINEAR POLYNOMIAL (Degree 1)' : 'NOT A LINEAR POLYNOMIAL'}}
          </text>
          <text x="300" y="235" fill="#e2e8f0" font-size="13" text-anchor="middle">Degree: ${{degree}}</text>
          <text x="300" y="260" fill="#a5b4fc" font-size="12" text-anchor="middle">${{reason}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Select Expression:</span>
          <button class="sim-btn" onclick="runClass('5x - 7', '1', true, 'Standard form ax + b with a = 5 ≠ 0')">5x - 7</button>
          <button class="sim-btn" onclick="runClass('-3y + 4', '1', true, 'Single variable y with exponent 1 and a = -3')">-3y + 4</button>
          <button class="sim-btn" style="background:#be123c;" onclick="runClass('2x² + 5x - 1', '2', false, 'Quadratic polynomial (highest exponent is 2)')">2x² + 5x</button>
          <button class="sim-btn" style="background:#be123c;" onclick="runClass('4/x + 3', 'Not a polynomial', false, 'Variable in denominator has negative exponent x⁻¹')">4/x + 3</button>
        </div>
      `;

      window.runClass = test;
      test('5x - 7', '1', true, 'Standard form ax + b with a = 5 ≠ 0');
    }}

    // 4. Transformer Sim
    function renderTransformerSim(svg, controls) {{
      function update(a, b) {{
        const zero = (-b / a).toFixed(2);
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Standard Form ax + b & Zero Determination</text>

          <rect x="70" y="70" width="460" height="90" rx="12" fill="#1e293b" stroke="#38bdf8" />
          <text x="120" y="110" fill="#94a3b8" font-size="12">Standard Linear Form:</text>
          <text x="120" y="140" fill="#fff" font-size="22" font-weight="bold">P(x) = ${{a}}x + (${{b}})</text>
          <text x="380" y="110" fill="#94a3b8" font-size="12">Coefficients:</text>
          <text x="380" y="140" fill="#f59e0b" font-size="18" font-weight="bold">a = ${{a}}, b = ${{b}}</text>

          <rect x="70" y="180" width="460" height="100" rx="12" fill="#0f172a" stroke="#10b981" />
          <text x="120" y="215" fill="#34d399" font-size="14" font-weight="bold">Zero of the Polynomial:</text>
          <text x="120" y="245" fill="#fff" font-size="18" font-weight="bold">x = -b / a = -(${{b}}) / ${{a}} = <tspan fill="#38bdf8">${{zero}}</tspan></text>
          <text x="380" y="245" fill="#cbd5e1" font-size="12">Check: P(${{zero}}) = 0</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Leading Coeff (a):</span>
          <input type="range" class="sim-slider" id="transA" min="-6" max="6" value="2">
          <span class="slider-val" id="transAVal">a = 2</span>
          <span class="slider-label" style="min-width:70px; margin-left:15px;">Constant (b):</span>
          <input type="range" class="sim-slider" id="transB" min="-12" max="12" value="-6">
          <span class="slider-val" id="transBVal">b = -6</span>
        </div>
      `;

      update(2, -6);
      const as = document.getElementById('transA');
      const bs = document.getElementById('transB');

      function refresh() {{
        let a = parseInt(as.value);
        if (a === 0) a = 1;
        const b = parseInt(bs.value);
        document.getElementById('transAVal').textContent = `a = ${{a}}`;
        document.getElementById('transBVal').textContent = `b = ${{b}}`;
        update(a, b);
      }}

      as.addEventListener('input', refresh);
      bs.addEventListener('input', refresh);
    }}

    // 5. Rate Stepper Sim
    function renderRateStepperSim(svg, controls) {{
      function draw(a) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="30" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Step-Ladder: Constant Rate of Change a = ${{a}}</text>
        `;

        const steps = 5;
        const startX = 120;
        const startY = 250;
        const stepW = 70;
        const scaleY = 16;

        for (let i = 0; i < steps; i++) {{
          const x1 = startX + i * stepW;
          const y1 = startY - i * a * scaleY;
          const x2 = startX + (i + 1) * stepW;
          const y2 = startY - (i + 1) * a * scaleY;

          // Horizontal tread
          const hLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          hLine.setAttribute('x1', x1); hLine.setAttribute('y1', y1);
          hLine.setAttribute('x2', x2); hLine.setAttribute('y2', y1);
          hLine.setAttribute('stroke', '#38bdf8'); hLine.setAttribute('stroke-width', '3');
          svg.appendChild(hLine);

          // Vertical riser
          const vLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          vLine.setAttribute('x1', x2); vLine.setAttribute('y1', y1);
          vLine.setAttribute('x2', x2); vLine.setAttribute('y2', y2);
          vLine.setAttribute('stroke', '#f59e0b'); vLine.setAttribute('stroke-width', '3');
          svg.appendChild(vLine);

          // Label
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', x2 + 10);
          t.setAttribute('y', (y1 + y2) / 2 + 4);
          t.setAttribute('fill', '#f59e0b');
          t.setAttribute('font-size', '11');
          t.textContent = `+${{a}}`;
          svg.appendChild(t);
        }}

        const expl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        expl.setAttribute('x', '300'); expl.setAttribute('y', '290');
        expl.setAttribute('fill', '#10b981'); expl.setAttribute('font-size', '12');
        expl.setAttribute('font-weight', 'bold'); expl.setAttribute('text-anchor', 'middle');
        expl.textContent = `Every horizontal step of 1 unit produces an identical vertical rise of ${{a}} units.`;
        svg.appendChild(expl);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Riser Height (Rate a):</span>
          <input type="range" class="sim-slider" id="rateSlider" min="1" max="4" value="2">
          <span class="slider-val" id="rateVal">a = 2</span>
        </div>
      `;

      draw(2);
      document.getElementById('rateSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('rateVal').textContent = `a = ${{v}}`;
        draw(v);
      }});
    }}

    // 6. Cost Modeler
    function renderCostModelerSim(svg, controls) {{
      function update(km) {{
        const base = 30;
        const rate = 15;
        const cost = rate * km + base;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Real-World Taxi Fare Modeler: C(k) = 15k + 30</text>

          <rect x="60" y="70" width="480" height="100" rx="12" fill="#1e293b" stroke="#f59e0b" />
          <text x="100" y="105" fill="#a5b4fc" font-size="12">Distance Traveled:</text>
          <text x="100" y="140" fill="#fff" font-size="24" font-weight="bold">${{km}} km</text>
          
          <text x="320" y="105" fill="#a5b4fc" font-size="12">Total Auto Fare:</text>
          <text x="320" y="140" fill="#34d399" font-size="26" font-weight="bold">₹${{cost}}</text>

          <rect x="60" y="190" width="480" height="90" rx="12" fill="#0f172a" stroke="#6366f1" />
          <text x="90" y="225" fill="#cbd5e1" font-size="12">Calculation Breakdown:</text>
          <text x="90" y="255" fill="#38bdf8" font-size="13" font-weight="bold">₹30 (Base Flag-down) + (15 × ${{km}}) = ₹30 + ₹${{15 * km}} = ₹${{cost}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Travel Distance (km):</span>
          <input type="range" class="sim-slider" id="kmSlider" min="0" max="30" value="8">
          <span class="slider-val" id="kmVal">8 km</span>
        </div>
      `;

      update(8);
      document.getElementById('kmSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('kmVal').textContent = `${{v}} km`;
        update(v);
      }});
    }}

    // 7. Growth Decay Comparator
    function renderGrowthDecaySim(svg, controls) {{
      function update(mode) {{
        const isGrowth = (mode === 'growth');
        const a = isGrowth ? 3 : -3;
        const b = isGrowth ? 10 : 80;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="${{isGrowth ? '#34d399' : '#fb7185'}}" font-size="15" font-weight="bold" text-anchor="middle">
            Trajectory: ${{isGrowth ? 'LINEAR GROWTH (a > 0)' : 'LINEAR DECAY (a < 0)'}}
          </text>

          <!-- Axes -->
          <line x1="100" y1="260" x2="520" y2="260" stroke="#475569" stroke-width="2" />
          <line x1="100" y1="60" x2="100" y2="260" stroke="#475569" stroke-width="2" />
          <text x="525" y="265" fill="#94a3b8" font-size="11">Time / Input (x)</text>
          <text x="100" y="50" fill="#94a3b8" font-size="11" text-anchor="middle">Output P(x)</text>

          <!-- Line -->
          <line x1="100" y1="${{isGrowth ? 220 : 80}}" x2="480" y2="${{isGrowth ? 80 : 240}}" stroke="${{isGrowth ? '#10b981' : '#f43f5e'}}" stroke-width="4" stroke-linecap="round" />

          <!-- Arrow & Description -->
          <text x="300" y="295" fill="#e2e8f0" font-size="12" text-anchor="middle">
            ${{isGrowth ? 'Positive Slope a = +3 ⟹ Quantity accumulates steadily over time' : 'Negative Slope a = -3 ⟹ Quantity steadily depletes toward zero'}}
          </text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Select Mode:</span>
          <button class="sim-btn" onclick="updateMode('growth')">Linear Growth (a > 0)</button>
          <button class="sim-btn" style="background:#be123c;" onclick="updateMode('decay')">Linear Decay (a < 0)</button>
        </div>
      `;

      window.updateMode = update;
      update('growth');
    }}

    // 8. Tank Drain Sim
    function renderTankDrainSim(svg, controls) {{
      function update(mins) {{
        const initial = 1200;
        const rate = 40;
        const current = Math.max(0, initial - rate * mins);
        const pct = (current / initial) * 100;
        const emptyMin = initial / rate;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Overhead Water Tank Drainage: V(t) = -40t + 1200</text>

          <!-- Tank Graphic -->
          <rect x="100" y="70" width="160" height="180" rx="8" fill="#0f172a" stroke="#475569" stroke-width="2" />
          <rect x="105" y="${{245 - (pct * 1.7)}}" width="150" height="${{pct * 1.7}}" rx="4" fill="#0284c7" opacity="0.8" />
          <text x="180" y="${{240 - (pct * 0.85)}}" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">${{current}} L</text>

          <!-- Stats -->
          <rect x="300" y="70" width="240" height="180" rx="10" fill="#1e293b" stroke="#38bdf8" />
          <text x="320" y="105" fill="#94a3b8" font-size="12">Elapsed Time:</text>
          <text x="320" y="130" fill="#fff" font-size="18" font-weight="bold">${{mins}} minutes</text>
          <text x="320" y="165" fill="#94a3b8" font-size="12">Remaining Water:</text>
          <text x="320" y="190" fill="#34d399" font-size="20" font-weight="bold">${{current}} / 1200 L</text>
          <text x="320" y="225" fill="${{current === 0 ? '#f43f5e' : '#f59e0b'}}" font-size="12" font-weight="bold">
            ${{current === 0 ? 'TANK IS COMPLETELY EMPTY!' : `Empty in ${{emptyMin - mins}} mins`}}
          </text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Drainage Time (minutes):</span>
          <input type="range" class="sim-slider" id="tankSlider" min="0" max="30" value="10">
          <span class="slider-val" id="tankVal">10 min</span>
        </div>
      `;

      update(10);
      document.getElementById('tankSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('tankVal').textContent = `${{v}} min`;
        update(v);
      }});
    }}

    // 9. Ordered Pair Sim
    function renderOrderedPairSim(svg, controls) {{
      function update(a, b) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Ordered Pairs (x, y) for y = ${{a}}x + (${{b}})</text>
        `;

        const xs = [-2, -1, 0, 1, 2, 3];
        const ys = xs.map(x => a * x + b);

        const startX = 60;
        const colW = 80;

        // X Row
        const xr = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        xr.setAttribute('x', startX); xr.setAttribute('y', '70');
        xr.setAttribute('width', colW * 6); xr.setAttribute('height', '40');
        xr.setAttribute('fill', '#1e293b'); xr.setAttribute('stroke', '#6366f1');
        svg.appendChild(xr);

        xs.forEach((x, i) => {{
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', startX + i * colW + colW / 2);
          t.setAttribute('y', '95');
          t.setAttribute('fill', '#38bdf8');
          t.setAttribute('font-size', '14');
          t.setAttribute('font-weight', 'bold');
          t.setAttribute('text-anchor', 'middle');
          t.textContent = `x = ${{x}}`;
          svg.appendChild(t);
        }});

        // Y Row
        const yr = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        yr.setAttribute('x', startX); yr.setAttribute('y', '110');
        yr.setAttribute('width', colW * 6); yr.setAttribute('height', '45');
        yr.setAttribute('fill', '#0f172a'); yr.setAttribute('stroke', '#6366f1');
        svg.appendChild(yr);

        ys.forEach((y, i) => {{
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', startX + i * colW + colW / 2);
          t.setAttribute('y', '138');
          t.setAttribute('fill', '#34d399');
          t.setAttribute('font-size', '16');
          t.setAttribute('font-weight', 'bold');
          t.setAttribute('text-anchor', 'middle');
          t.textContent = `y = ${{y}}`;
          svg.appendChild(t);
        }});

        // Intercepts
        const yInt = `(0, ${{b}})`;
        const xInt = `(${{(-b/a).toFixed(1)}}, 0)`;

        const card = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        card.setAttribute('x', startX); card.setAttribute('y', '180');
        card.setAttribute('width', colW * 6); card.setAttribute('height', '80');
        card.setAttribute('rx', '10');
        card.setAttribute('fill', '#1e293b'); card.setAttribute('stroke', '#f59e0b');
        svg.appendChild(card);

        const it = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        it.setAttribute('x', '300'); it.setAttribute('y', '215');
        it.setAttribute('fill', '#f59e0b'); it.setAttribute('font-size', '13');
        it.setAttribute('font-weight', 'bold'); it.setAttribute('text-anchor', 'middle');
        it.textContent = `y-intercept (x = 0): ${{yInt}}  |  x-intercept (y = 0): ${{xInt}}`;
        svg.appendChild(it);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Slope a:</span>
          <input type="range" class="sim-slider" id="opA" min="-4" max="4" value="2">
          <span class="slider-val" id="opAVal">a = 2</span>
          <span class="slider-label" style="min-width:60px; margin-left:15px;">Intercept b:</span>
          <input type="range" class="sim-slider" id="opB" min="-6" max="6" value="1">
          <span class="slider-val" id="opBVal">b = 1</span>
        </div>
      `;

      update(2, 1);
      const as = document.getElementById('opA');
      const bs = document.getElementById('opB');

      function refresh() {{
        let a = parseInt(as.value);
        if (a === 0) a = 1;
        const b = parseInt(bs.value);
        document.getElementById('opAVal').textContent = `a = ${{a}}`;
        document.getElementById('opBVal').textContent = `b = ${{b}}`;
        update(a, b);
      }}

      as.addEventListener('input', refresh);
      bs.addEventListener('input', refresh);
    }}

    // 10. Two Point Slope Sim
    function renderTwoPointSlopeSim(svg, controls) {{
      function calc(x1, y1, x2, y2) {{
        const dy = y2 - y1;
        const dx = x2 - x1;
        const a = (dy / dx).toFixed(2);
        const b = (y1 - (dy / dx) * x1).toFixed(2);

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Two-Point Line Deriver: P₁(${{x1}}, ${{y1}}) & P₂(${{x2}}, ${{y2}})</text>

          <rect x="60" y="65" width="480" height="100" rx="12" fill="#1e293b" stroke="#6366f1" />
          <text x="100" y="105" fill="#a5b4fc" font-size="12">Vertical Change (Δy):</text>
          <text x="100" y="135" fill="#fff" font-size="18" font-weight="bold">${{y2}} - ${{y1}} = ${{dy}}</text>
          <text x="320" y="105" fill="#a5b4fc" font-size="12">Horizontal Change (Δx):</text>
          <text x="320" y="135" fill="#fff" font-size="18" font-weight="bold">${{x2}} - ${{x1}} = ${{dx}}</text>

          <rect x="60" y="180" width="480" height="100" rx="12" fill="#0f172a" stroke="#10b981" />
          <text x="300" y="215" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">Slope a = Δy / Δx = ${{dy}} / ${{dx}} = ${{a}}</text>
          <text x="300" y="250" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">Line Equation: y = ${{a}}x + (${{b}})</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Preset Two Points:</span>
          <button class="sim-btn" onclick="runPts(2, 7, 5, 16)">(2,7) & (5,16)</button>
          <button class="sim-btn" onclick="runPts(1, 3, 4, 15)">(1,3) & (4,15)</button>
          <button class="sim-btn" onclick="runPts(-2, 4, 2, -4)">(-2,4) & (2,-4)</button>
        </div>
      `;

      window.runPts = calc;
      calc(2, 7, 5, 16);
    }}

    // 11. Interactive Line Grapher
    function renderLineGrapherSim(svg, controls) {{
      function draw(a, b) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Cartesian Graph: y = ${{a}}x + (${{b}})</text>

          <!-- Grid Lines -->
          <g stroke="#1e293b" stroke-width="1">
            <line x1="100" y1="160" x2="500" y2="160" />
            <line x1="300" y1="50" x2="300" y2="270" />
          </g>
          <!-- Axes -->
          <line x1="100" y1="160" x2="500" y2="160" stroke="#64748b" stroke-width="2" />
          <line x1="300" y1="50" x2="300" y2="270" stroke="#64748b" stroke-width="2" />
          <text x="505" y="165" fill="#94a3b8" font-size="12">x</text>
          <text x="300" y="42" fill="#94a3b8" font-size="12" text-anchor="middle">y</text>
        `;

        const originX = 300;
        const originY = 160;
        const scale = 20;

        const x1 = -8;
        const y1 = a * x1 + b;
        const x2 = 8;
        const y2 = a * x2 + b;

        const px1 = originX + x1 * scale;
        const py1 = originY - y1 * scale;
        const px2 = originX + x2 * scale;
        const py2 = originY - y2 * scale;

        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', px1); line.setAttribute('y1', py1);
        line.setAttribute('x2', px2); line.setAttribute('y2', py2);
        line.setAttribute('stroke', '#38bdf8'); line.setAttribute('stroke-width', '3');
        svg.appendChild(line);

        // y-intercept dot
        const pyInt = originY - b * scale;
        const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        dot.setAttribute('cx', originX); dot.setAttribute('cy', pyInt);
        dot.setAttribute('r', '5'); dot.setAttribute('fill', '#f59e0b');
        svg.appendChild(dot);

        const lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        lbl.setAttribute('x', originX + 10); lbl.setAttribute('y', pyInt - 8);
        lbl.setAttribute('fill', '#f59e0b'); lbl.setAttribute('font-size', '11');
        lbl.textContent = `(0, ${{b}})`;
        svg.appendChild(lbl);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Slope a (tilt):</span>
          <input type="range" class="sim-slider" id="graphA" min="-3" max="3" value="1" step="0.5">
          <span class="slider-val" id="graphAVal">a = 1</span>
          <span class="slider-label" style="min-width:70px; margin-left:15px;">Intercept b:</span>
          <input type="range" class="sim-slider" id="graphB" min="-4" max="4" value="2">
          <span class="slider-val" id="graphBVal">b = 2</span>
        </div>
      `;

      draw(1, 2);
      const as = document.getElementById('graphA');
      const bs = document.getElementById('graphB');

      function refresh() {{
        const a = parseFloat(as.value);
        const b = parseInt(bs.value);
        document.getElementById('graphAVal').textContent = `a = ${{a}}`;
        document.getElementById('graphBVal').textContent = `b = ${{b}}`;
        draw(a, b);
      }}

      as.addEventListener('input', refresh);
      bs.addEventListener('input', refresh);
    }}

    // 12. Break Even Sim
    function renderBreakEvenSim(svg, controls) {{
      function update(gb) {{
        const costA = 2 * gb + 10;
        const costB = 1 * gb + 20;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Break-Even Analysis: Plan A ($2x+10) vs Plan B ($1x+20)</text>

          <rect x="60" y="70" width="220" height="150" rx="12" fill="#1e293b" stroke="#38bdf8" />
          <text x="170" y="105" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Plan Alpha: 2x + 10</text>
          <text x="170" y="145" fill="#fff" font-size="28" font-weight="bold" text-anchor="middle">₹${{costA}}</text>
          <text x="170" y="185" fill="${{costA < costB ? '#10b981' : '#cbd5e1'}}" font-size="12" font-weight="bold" text-anchor="middle">
            ${{costA < costB ? '★ CHEAPER OPTION' : (costA === costB ? 'EQUAL COST' : 'MORE EXPENSIVE')}}
          </text>

          <rect x="320" y="70" width="220" height="150" rx="12" fill="#1e293b" stroke="#10b981" />
          <text x="430" y="105" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">Plan Beta: 1x + 20</text>
          <text x="430" y="145" fill="#fff" font-size="28" font-weight="bold" text-anchor="middle">₹${{costB}}</text>
          <text x="430" y="185" fill="${{costB < costA ? '#10b981' : '#cbd5e1'}}" font-size="12" font-weight="bold" text-anchor="middle">
            ${{costB < costA ? '★ CHEAPER OPTION' : (costA === costB ? 'EQUAL COST' : 'MORE EXPENSIVE')}}
          </text>

          <text x="300" y="260" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">
            Break-Even Point: x = 10 GB (Both cost exactly ₹30)
          </text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Data Usage (x GB):</span>
          <input type="range" class="sim-slider" id="breakSlider" min="0" max="25" value="6">
          <span class="slider-val" id="breakVal">6 GB</span>
        </div>
      `;

      update(6);
      document.getElementById('breakSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('breakVal').textContent = `${{v}} GB`;
        update(v);
      }});
    }}

    // 13. Rectangle Perimeter Solver
    function renderPerimeterSolverSim(svg, controls) {{
      function update(w) {{
        const l = 2 * w + 5;
        const p = 2 * (l + w);

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Rectangle Dimensions: Length = 2w + 5 | Perimeter = 6w + 10</text>

          <rect x="180" y="80" width="${{w * 16}}" height="${{w * 8}}" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2" />
          <text x="${{180 + w * 8}}" y="70" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Length = ${{l}} cm</text>
          <text x="160" y="${{80 + w * 4}}" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="end">Width = ${{w}} cm</text>

          <rect x="80" y="210" width="440" height="80" rx="10" fill="#0f172a" stroke="#10b981" />
          <text x="300" y="240" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">
            Perimeter = 2(${{l}} + ${{w}}) = 2(${{l + w}}) = ${{p}} cm
          </text>
          <text x="300" y="268" fill="#cbd5e1" font-size="12" text-anchor="middle">
            Formula Check: 6w + 10 = 6(${{w}}) + 10 = ${{p}} cm
          </text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Width (w cm):</span>
          <input type="range" class="sim-slider" id="rectSlider" min="2" max="10" value="6">
          <span class="slider-val" id="rectVal">w = 6 cm</span>
        </div>
      `;

      update(6);
      document.getElementById('rectSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('rectVal').textContent = `w = ${{v}} cm`;
        update(v);
      }});
    }}

    // 14. Digit Reversal Sim
    function renderDigitReversalSim(svg, controls) {{
      function update(t) {{
        const u = 9 - t;
        const orig = 10 * t + u;
        const rev = 10 * u + t;
        const diff = rev - orig;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Two-Digit Number Reversal Riddle (Sum of Digits = 9)</text>

          <rect x="60" y="70" width="220" height="130" rx="12" fill="#1e293b" stroke="#38bdf8" />
          <text x="170" y="105" fill="#a5b4fc" font-size="12" text-anchor="middle">Original Number 10t + u</text>
          <text x="170" y="150" fill="#fff" font-size="36" font-weight="bold" text-anchor="middle">${{orig}}</text>
          <text x="170" y="180" fill="#38bdf8" font-size="12" text-anchor="middle">t = ${{t}}, u = ${{u}}</text>

          <rect x="320" y="70" width="220" height="130" rx="12" fill="#1e293b" stroke="#10b981" />
          <text x="430" y="105" fill="#a5b4fc" font-size="12" text-anchor="middle">Reversed Number 10u + t</text>
          <text x="430" y="150" fill="#34d399" font-size="36" font-weight="bold" text-anchor="middle">${{rev}}</text>
          <text x="430" y="180" fill="#10b981" font-size="12" text-anchor="middle">Digits Swapped</text>

          <rect x="60" y="220" width="480" height="70" rx="10" fill="#0f172a" stroke="#f59e0b" />
          <text x="300" y="250" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">
            Reversed - Original = ${{rev}} - ${{orig}} = ${{diff}}
          </text>
          <text x="300" y="272" fill="${{diff === 27 ? '#34d399' : '#cbd5e1'}}" font-size="12" text-anchor="middle">
            ${{diff === 27 ? '★ EXACT SOLUTION TO NCERT RIDDLE (Difference is 27)!' : 'Riddle condition: looking for difference = 27'}}
          </text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Tens Digit (t):</span>
          <input type="range" class="sim-slider" id="digitSlider" min="1" max="8" value="3">
          <span class="slider-val" id="digitVal">t = 3</span>
        </div>
      `;

      update(3);
      document.getElementById('digitSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('digitVal').textContent = `t = ${{v}}`;
        update(v);
      }});
    }}

    // 15. Summary Matrix Sim
    function renderSummaryMatrixSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="0" y="0" width="600" height="320" fill="#090d16" />
        <text x="300" y="30" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Linear Polynomials: Core Formula Matrix</text>

        <rect x="40" y="60" width="240" height="100" rx="10" fill="#1e293b" stroke="#6366f1" />
        <text x="160" y="90" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Standard Form & Degree</text>
        <text x="160" y="120" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">P(x) = ax + b (a ≠ 0)</text>
        <text x="160" y="145" fill="#38bdf8" font-size="11" text-anchor="middle">Degree is strictly 1</text>

        <rect x="320" y="60" width="240" height="100" rx="10" fill="#1e293b" stroke="#10b981" />
        <text x="440" y="90" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Unique Real Zero</text>
        <text x="440" y="120" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">x = -b / a</text>
        <text x="440" y="145" fill="#6ee7b7" font-size="11" text-anchor="middle">Root where P(x) = 0</text>

        <rect x="40" y="180" width="240" height="100" rx="10" fill="#1e293b" stroke="#f59e0b" />
        <text x="160" y="210" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Constant Difference</text>
        <text x="160" y="240" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">P(x+1) - P(x) = a</text>
        <text x="160" y="265" fill="#fde68a" font-size="11" text-anchor="middle">Constant step rate</text>

        <rect x="320" y="180" width="240" height="100" rx="10" fill="#1e293b" stroke="#ec4899" />
        <text x="440" y="210" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Geometric Graph</text>
        <text x="440" y="240" fill="#f472b6" font-size="16" font-weight="bold" text-anchor="middle">Straight Line</text>
        <text x="440" y="265" fill="#fbcfe8" font-size="11" text-anchor="middle">Slope a, y-intercept b</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span style="color:#94a3b8; font-size:12px;">Universal synthesis of all theoretical and geometric tools for Class 8 Chapter 2.</span>
        </div>
      `;
    }}

    // 16. Historical Timeline Sim
    function renderHistorySim(svg, controls) {{
      svg.innerHTML = `
        <rect x="0" y="0" width="600" height="320" fill="#090d16" />
        <text x="300" y="30" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">Milestones in the Historical Evolution of Algebra</text>

        <!-- Timeline Bar -->
        <line x1="60" y1="160" x2="540" y2="160" stroke="#475569" stroke-width="4" />

        <!-- 1650 BCE -->
        <circle cx="90" cy="160" r="8" fill="#38bdf8" />
        <text x="90" y="135" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1650 BCE</text>
        <text x="90" y="195" fill="#cbd5e1" font-size="10" text-anchor="middle">Rhind Papyrus</text>
        <text x="90" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Egypt 'Aha'</text>

        <!-- 250 CE -->
        <circle cx="210" cy="160" r="8" fill="#a855f7" />
        <text x="210" y="135" fill="#a855f7" font-size="11" font-weight="bold" text-anchor="middle">250 CE</text>
        <text x="210" y="195" fill="#cbd5e1" font-size="10" text-anchor="middle">Diophantus</text>
        <text x="210" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Arithmetica</text>

        <!-- 628 CE -->
        <circle cx="330" cy="160" r="8" fill="#10b981" />
        <text x="330" y="135" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">628 CE</text>
        <text x="330" y="195" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Brahmagupta</text>
        <text x="330" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Zero & Negatives</text>

        <!-- 820 CE -->
        <circle cx="430" cy="160" r="8" fill="#f59e0b" />
        <text x="430" y="135" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">820 CE</text>
        <text x="430" y="195" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Al-Khwarizmi</text>
        <text x="430" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Al-Jabr (Algebra)</text>

        <!-- 1637 CE -->
        <circle cx="510" cy="160" r="8" fill="#f43f5e" />
        <text x="510" y="135" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">1637 CE</text>
        <text x="510" y="195" fill="#fb7185" font-size="10" font-weight="bold" text-anchor="middle">Descartes</text>
        <text x="510" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Cartesian Graph</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span style="color:#94a3b8; font-size:12px;">Spanning 3300 years of global mathematical synthesis.</span>
        </div>
      `;
    }}
  </script>
</body>
</html>
"""

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public', 'animations', 'class8-math-linear-polynomials.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Successfully generated {output_path} ({len(html_template)} bytes).")

if __name__ == '__main__':
    generate_lab_html()
