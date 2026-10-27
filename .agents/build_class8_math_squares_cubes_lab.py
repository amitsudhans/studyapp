# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 8 Mathematics Chapter 1:
A Square and A Cube (Mathematics Grade 8)
Produces: public/animations/class8-math-square-and-cube.html
Features:
- 20 Full Slides (16 Comprehensive Interactive Lessons + 4 Dedicated Quiz Slides)
- 32 In-Slide Checkpoints (2 per lesson slide) with immediate teacher feedback
- 40 Comprehensive Quiz Questions (10 per quiz slide) with "View Solution" modal popups
- Prof. Ramanujan Sharma Talking Avatar with Web Speech API audio narration and animated mouth
- 16 High-Fidelity Interactive SVG Simulators with sliders, buttons, and visual math representations
- Strict last-slide notice on slide 20 with hidden nextBtn
- Responsive, robust CSS styling matching all project guidelines
"""

import os
import json
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from class8_math_squares_cubes_data import slides_data, quiz_questions

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
  <title>NCERT Class 8 Mathematics • Chapter 1: A Square and A Cube Master Lab</title>
  
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
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 9999px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.4);
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
      color: #f59e0b;
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
      min-width: 130px;
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
      min-width: 45px;
      text-align: right;
    }}

    .sim-btn {{
      background: linear-gradient(135deg, #4f46e5, #6366f1);
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
      box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
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
      background: radial-gradient(circle, #312e81 0%, #0f172a 75%);
      border: 2px solid #6366f1;
      border-radius: 50%;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
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
      <span class="nav-title">A Square and A Cube • Mathematics Chapter 1</span>
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
        <h1 class="slide-title" id="slideTitle">1.1 Square Numbers & The Geometry of Area</h1>
        <p class="slide-subtitle" id="slideSubtitle">Definition of Square Numbers, Geometric Arrays and Notation n²</p>
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
            <circle cx="50" cy="50" r="48" fill="#1e1b4b" stroke="#6366f1" stroke-width="2" />
            <!-- Traditional Achkan / Coat -->
            <path d="M20 95 Q50 82 80 95 L85 100 L15 100 Z" fill="#0284c7" />
            <!-- Collar / Scarf -->
            <path d="M42 82 L50 88 L58 82 L50 98 Z" fill="#f59e0b" />
            <!-- Neck -->
            <rect x="44" y="65" width="12" height="18" fill="#fbcfe8" rx="3" />
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
          Welcome to Chapter 1: A Square and A Cube! Let us explore the geometric and arithmetic magic of powers and roots!
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
        <button onclick="closeSolutionModal()" style="background:#4f46e5; color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:12px; font-weight:700; cursor:pointer;">Close Solution</button>
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
        case 'square_grid_builder':
          title.textContent = 'Dynamic Square Tile Array & Area Modeler';
          renderSquareGridSim(svg, controls);
          break;
        case 'locker_factor_matrix':
          title.textContent = '100 Lockers & Factor Pair Parity Analyzer';
          renderLockerSim(svg, controls);
          break;
        case 'units_digit_analyzer':
          title.textContent = 'Units Digit Law & Square Disqualification Studio';
          renderUnitsDigitSim(svg, controls);
          break;
        case 'zero_parity_tester':
          title.textContent = 'Trailing Zero Doubling & Parity Invariance Engine';
          renderZeroParitySim(svg, controls);
          break;
        case 'odd_sum_gnomon_animator':
          title.textContent = 'Gnomon Inverted-L & Successive Odd Sum Animator';
          renderGnomonSim(svg, controls);
          break;
        case 'repeated_subtraction_stepper':
          title.textContent = 'Repeated Odd Subtraction Step-By-Step Decision Tree';
          renderSubtractionSim(svg, controls);
          break;
        case 'between_squares_counter':
          title.textContent = '2n Non-Square Theorem & Interval Explorer';
          renderBetweenSquaresSim(svg, controls);
          break;
        case 'triangular_square_merger':
          title.textContent = 'Consecutive Triangular Numbers Tessellation (T_{{n-1}} + T_{{n}} = n²)';
          renderTriangularSim(svg, controls);
          break;
        case 'square_root_inverter':
          title.textContent = 'Square vs Square Root Bi-Directional Transformer';
          renderSquareRootSim(svg, controls);
          break;
        case 'prime_factor_pairer':
          title.textContent = 'Prime Factor Pairing & Square Root Factoriser';
          renderPrimeFactorSim(svg, controls);
          break;
        case 'cube_volume_builder':
          title.textContent = '3D Cubic Stacking & Volume Layering Studio (n × n × n)';
          renderCubeVolumeSim(svg, controls);
          break;
        case 'cube_digit_mapper':
          title.textContent = 'Cubic Units Digit & Terminal Zero Tripling Engine';
          renderCubeDigitSim(svg, controls);
          break;
        case 'ramanujan_taxicab_sim':
          title.textContent = 'Hardy–Ramanujan 1729 Dual Cube Visualizer';
          renderTaxicabSim(svg, controls);
          break;
        case 'nicomachus_pyramid_animator':
          title.textContent = "Nicomachus's Consecutive Odd Number Cube Pyramid";
          renderNicomachusSim(svg, controls);
          break;
        case 'cube_root_triplet_sim':
          title.textContent = 'Cube Root Extraction by Prime Factor Triplets';
          renderCubeRootTripletSim(svg, controls);
          break;
        case 'finite_difference_cascade':
          title.textContent = 'Successive Differences Cascade & Aryabhata Mula Laboratory';
          renderFiniteDifferenceSim(svg, controls);
          break;
        default:
          title.textContent = 'Interactive Simulation';
          svg.innerHTML = '<text x="300" y="160" fill="#94a3b8" text-anchor="middle">Interactive Demonstration</text>';
      }}
    }}

    // 1. Square Grid Builder
    function renderSquareGridSim(svg, controls) {{
      function draw(n) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Sidelength n = ${{n}} | Area = ${{n}} × ${{n}} = ${{n * n}} sq units</text>
        `;
        const size = Math.min(200, 200 / n * n);
        const cellSize = 190 / n;
        const startX = 300 - (n * cellSize) / 2;
        const startY = 60;

        for (let r = 0; r < n; r++) {{
          for (let c = 0; c < n; c++) {{
            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', startX + c * cellSize);
            rect.setAttribute('y', startY + r * cellSize);
            rect.setAttribute('width', cellSize - 1.5);
            rect.setAttribute('height', cellSize - 1.5);
            rect.setAttribute('rx', Math.max(1, 4 - n * 0.2));
            rect.setAttribute('fill', ((r + c) % 2 === 0) ? '#6366f1' : '#4f46e5');
            rect.setAttribute('stroke', '#a5b4fc');
            rect.setAttribute('stroke-width', '0.5');
            svg.appendChild(rect);
          }}
        }}

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '300');
        text.setAttribute('y', '285');
        text.setAttribute('fill', '#f59e0b');
        text.setAttribute('font-size', '13');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('text-anchor', 'middle');
        text.textContent = `${{n}}² = ${{n * n}} perfect square tiles in array`;
        svg.appendChild(text);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Square Side Length (n):</span>
          <input type="range" class="sim-slider" id="gridSlider" min="1" max="10" value="4">
          <span class="slider-val" id="gridVal">n = 4</span>
        </div>
      `;

      draw(4);
      document.getElementById('gridSlider').addEventListener('input', (e) => {{
        const val = parseInt(e.target.value);
        document.getElementById('gridVal').textContent = `n = ${{val}}`;
        draw(val);
      }});
    }}

    // 2. Locker Simulator
    function renderLockerSim(svg, controls) {{
      function draw(num) {{
        // Find factors
        const factors = [];
        for (let i = 1; i <= num; i++) {{
          if (num % i === 0) factors.push(i);
        }}
        const isSquare = factors.length % 2 === 1;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="35" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Locker #${{num}} Factor Analysis</text>
          
          <!-- Locker Graphic -->
          <rect x="100" y="70" width="130" height="190" rx="10" fill="${{isSquare ? '#065f46' : '#881337'}}" stroke="${{isSquare ? '#10b981' : '#f43f5e'}}" stroke-width="2.5" />
          <circle cx="210" cy="165" r="7" fill="#f59e0b" />
          <text x="165" y="125" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">#${{num}}</text>
          <text x="165" y="225" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">${{isSquare ? 'OPEN' : 'CLOSED'}}</text>
          
          <!-- Factors List -->
          <text x="260" y="85" fill="#f8fafc" font-size="13" font-weight="bold">Factors of ${{num}} (${{factors.length}} factors):</text>
          <text x="260" y="115" fill="#a5b4fc" font-size="12">${{factors.join(', ')}}</text>
          
          <rect x="260" y="140" width="310" height="90" rx="8" fill="#1e293b" stroke="#475569" />
          <text x="275" y="165" fill="${{isSquare ? '#34d399' : '#fb7185'}}" font-size="12" font-weight="bold">Parity: ${{factors.length}} is an ${{isSquare ? 'ODD' : 'EVEN'}} number</text>
          <text x="275" y="190" fill="#cbd5e1" font-size="11">${{isSquare ? `Pair ${{Math.sqrt(num)}} × ${{Math.sqrt(num)}} pairs with itself!` : 'Every factor has a distinct partner factor.'}}</text>
          <text x="275" y="212" fill="#38bdf8" font-size="11">Result: Locker stays ${{isSquare ? 'OPEN at the end!' : 'CLOSED at the end.'}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Test Locker Number:</span>
          <input type="range" class="sim-slider" id="lockerSlider" min="1" max="100" value="36">
          <span class="slider-val" id="lockerVal">#36</span>
        </div>
      `;

      draw(36);
      document.getElementById('lockerSlider').addEventListener('input', (e) => {{
        const val = parseInt(e.target.value);
        document.getElementById('lockerVal').textContent = `#${{val}}`;
        draw(val);
      }});
    }}

    // 3. Units Digit Law Simulator
    function renderUnitsDigitSim(svg, controls) {{
      function test(num) {{
        const u = num % 10;
        const sq = num * num;
        const sqU = sq % 10;
        const isImpossible = [2, 3, 7, 8].includes(u);

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="35" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Units Digit Law & Non-Square Detector</text>
          
          <!-- Number Card -->
          <rect x="50" y="70" width="220" height="180" rx="12" fill="#1e293b" stroke="#6366f1" stroke-width="1.5" />
          <text x="160" y="105" fill="#94a3b8" font-size="12" text-anchor="middle">Base Number n</text>
          <text x="160" y="145" fill="#fff" font-size="28" font-weight="bold" text-anchor="middle">${{num}}</text>
          <text x="160" y="180" fill="#38bdf8" font-size="13" text-anchor="middle">Units Digit: <tspan fill="#f59e0b" font-weight="bold">${{u}}</tspan></text>
          <text x="160" y="220" fill="${{isImpossible ? '#f43f5e' : '#10b981'}}" font-size="11" font-weight="bold" text-anchor="middle">
            ${{isImpossible ? 'CANNOT BE A SQUARE!' : 'Could be a square'}}
          </text>

          <!-- Square Card -->
          <rect x="330" y="70" width="220" height="180" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
          <text x="440" y="105" fill="#94a3b8" font-size="12" text-anchor="middle">Square n²</text>
          <text x="440" y="145" fill="#34d399" font-size="24" font-weight="bold" text-anchor="middle">${{sq}}</text>
          <text x="440" y="180" fill="#38bdf8" font-size="13" text-anchor="middle">Units Digit: <tspan fill="#f59e0b" font-weight="bold">${{sqU}}</tspan></text>
          <text x="440" y="220" fill="#cbd5e1" font-size="11" text-anchor="middle">(${{u}} × ${{u}} = ${{u*u}} ends in ${{sqU}})</text>
          
          <text x="300" y="285" fill="#e2e8f0" font-size="12" text-anchor="middle">Permitted Square Units Digits: {{0, 1, 4, 5, 6, 9}} | Forbidden: {{2, 3, 7, 8}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Test Base Integer:</span>
          <input type="range" class="sim-slider" id="digitSlider" min="1" max="50" value="17">
          <span class="slider-val" id="digitVal">17</span>
        </div>
      `;

      test(17);
      document.getElementById('digitSlider').addEventListener('input', (e) => {{
        const val = parseInt(e.target.value);
        document.getElementById('digitVal').textContent = val;
        test(val);
      }});
    }}

    // 4. Zero & Parity Simulator
    function renderZeroParitySim(svg, controls) {{
      function update(base, zeros) {{
        const num = base * Math.pow(10, zeros);
        const sqZeros = zeros * 2;
        const sq = (base * base) * Math.pow(10, sqZeros);
        const isEven = (base % 2 === 0);

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Trailing Zero Doubling & Parity Law</text>
          
          <rect x="50" y="60" width="500" height="100" rx="10" fill="#1e293b" stroke="#3b82f6" />
          <text x="75" y="95" fill="#94a3b8" font-size="12">Given Integer:</text>
          <text x="75" y="130" fill="#fff" font-size="22" font-weight="bold">${{num.toLocaleString()}}</text>
          <text x="350" y="95" fill="#38bdf8" font-size="12">Trailing Zeros: <tspan font-weight="bold" fill="#f59e0b">${{zeros}}</tspan></text>
          <text x="350" y="130" fill="${{isEven ? '#10b981' : '#f59e0b'}}" font-size="13" font-weight="bold">Parity: ${{isEven ? 'EVEN' : 'ODD'}}</text>

          <rect x="50" y="180" width="500" height="105" rx="10" fill="#1e293b" stroke="#10b981" />
          <text x="75" y="215" fill="#94a3b8" font-size="12">Its Square:</text>
          <text x="75" y="250" fill="#34d399" font-size="20" font-weight="bold">${{sq.toLocaleString()}}</text>
          <text x="350" y="215" fill="#38bdf8" font-size="12">Square Trailing Zeros: <tspan font-weight="bold" fill="#f59e0b">${{sqZeros}} (2 × ${{zeros}})</tspan></text>
          <text x="350" y="250" fill="${{isEven ? '#10b981' : '#f59e0b'}}" font-size="13" font-weight="bold">Square Parity: ${{isEven ? 'EVEN' : 'ODD'}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Base Number:</span>
          <select id="parityBase" style="background:#0f172a; color:#fff; padding:4px 8px; border-radius:6px; border:1px solid #475569;">
            <option value="2">2 (Even)</option>
            <option value="3">3 (Odd)</option>
            <option value="4">4 (Even)</option>
            <option value="7">7 (Odd)</option>
          </select>
          <span class="slider-label" style="min-width:90px; margin-left:15px;">Trailing Zeros:</span>
          <input type="range" class="sim-slider" id="zeroSlider" min="1" max="4" value="2">
          <span class="slider-val" id="zeroVal">2 zeros</span>
        </div>
      `;

      update(2, 2);
      const sel = document.getElementById('parityBase');
      const sld = document.getElementById('zeroSlider');

      sel.addEventListener('change', () => {{
        update(parseInt(sel.value), parseInt(sld.value));
      }});
      sld.addEventListener('input', (e) => {{
        const z = parseInt(e.target.value);
        document.getElementById('zeroVal').textContent = `${{z}} zeros`;
        update(parseInt(sel.value), z);
      }});
    }}

    // 5. Gnomon Simulator
    function renderGnomonSim(svg, controls) {{
      function draw(n) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="30" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Inverted-L Gnomon: Sum of First ${{n}} Odd Numbers = ${{n}}²</text>
        `;

        const colors = ['#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#6366f1', '#a855f7', '#ec4899'];
        const cellSize = 16;
        const startX = 220;
        const startY = 60;

        for (let layer = 1; layer <= n; layer++) {{
          const col = colors[(layer - 1) % colors.length];
          // Top row of this gnomon
          for (let c = 0; c < layer; c++) {{
            const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', startX + c * cellSize);
            circle.setAttribute('cy', startY + (layer - 1) * cellSize);
            circle.setAttribute('r', '5.5');
            circle.setAttribute('fill', col);
            svg.appendChild(circle);
          }}
          // Right column of this gnomon
          for (let r = 0; r < layer - 1; r++) {{
            const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', startX + (layer - 1) * cellSize);
            circle.setAttribute('cy', startY + r * cellSize);
            circle.setAttribute('r', '5.5');
            circle.setAttribute('fill', col);
            svg.appendChild(circle);
          }}
        }}

        // Odd terms formula
        const oddTerms = [];
        for (let k = 1; k <= n; k++) oddTerms.push(2 * k - 1);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '300');
        text.setAttribute('y', '270');
        text.setAttribute('fill', '#f59e0b');
        text.setAttribute('font-size', '13');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('text-anchor', 'middle');
        text.textContent = `${{oddTerms.join(' + ')}} = ${{n * n}} = ${{n}}²`;
        svg.appendChild(text);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Number of Odd Terms (n):</span>
          <input type="range" class="sim-slider" id="gnomonSlider" min="1" max="7" value="4">
          <span class="slider-val" id="gnomonVal">n = 4</span>
        </div>
      `;

      draw(4);
      document.getElementById('gnomonSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('gnomonVal').textContent = `n = ${{v}}`;
        draw(v);
      }});
    }}

    // 6. Repeated Subtraction Simulator
    function renderSubtractionSim(svg, controls) {{
      function test(num) {{
        let rem = num;
        let odd = 1;
        let step = 0;
        const steps = [];

        while (rem > 0 && step < 12) {{
          step++;
          const prev = rem;
          rem = rem - odd;
          steps.push({{ step, prev, odd, rem }});
          odd += 2;
        }}

        const isSquare = (rem === 0);

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Testing ${{num}} by Repeated Odd Subtraction</text>
        `;

        let y = 60;
        steps.slice(0, 6).forEach(s => {{
          const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
          t.setAttribute('x', '100');
          t.setAttribute('y', y);
          t.setAttribute('fill', '#cbd5e1');
          t.setAttribute('font-size', '12');
          t.textContent = `Step ${{s.step}}: ${{s.prev}} - ${{s.odd}} = ${{s.rem}}`;
          svg.appendChild(t);
          y += 24;
        }});

        if (steps.length > 6) {{
          y = 60;
          steps.slice(6, 12).forEach(s => {{
            const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            t.setAttribute('x', '350');
            t.setAttribute('y', y);
            t.setAttribute('fill', '#cbd5e1');
            t.setAttribute('font-size', '12');
            t.textContent = `Step ${{s.step}}: ${{s.prev}} - ${{s.odd}} = ${{s.rem}}`;
            svg.appendChild(t);
            y += 24;
          }});
        }}

        const resultBox = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        resultBox.setAttribute('x', '80');
        resultBox.setAttribute('y', '225');
        resultBox.setAttribute('width', '440');
        resultBox.setAttribute('height', '70');
        resultBox.setAttribute('rx', '8');
        resultBox.setAttribute('fill', isSquare ? 'rgba(16, 185, 129, 0.15)' : 'rgba(244, 63, 94, 0.15)');
        resultBox.setAttribute('stroke', isSquare ? '#10b981' : '#f43f5e');
        svg.appendChild(resultBox);

        const resText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        resText.setAttribute('x', '300');
        resText.setAttribute('y', '255');
        resText.setAttribute('fill', isSquare ? '#34d399' : '#fb7185');
        resText.setAttribute('font-size', '13');
        resText.setAttribute('font-weight', 'bold');
        resText.setAttribute('text-anchor', 'middle');
        resText.textContent = isSquare ? `SUCCESS: Reached 0 in ${{steps.length}} steps! √${{num}} = ${{steps.length}}` : `FAILED: Crossed 0 without landing on 0. ${{num}} is NOT a square!`;
        svg.appendChild(resText);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Select Number to Test:</span>
          <button class="sim-btn" onclick="document.getElementById('subVal').value=25; runSub(25);">25 (Square)</button>
          <button class="sim-btn" onclick="document.getElementById('subVal').value=49; runSub(49);">49 (Square)</button>
          <button class="sim-btn" onclick="document.getElementById('subVal').value=81; runSub(81);">81 (Square)</button>
          <button class="sim-btn" style="background:#be123c;" onclick="document.getElementById('subVal').value=38; runSub(38);">38 (Non-Square)</button>
          <input type="hidden" id="subVal" value="49">
        </div>
      `;

      window.runSub = test;
      test(49);
    }}

    // 7. Between Squares Simulator
    function renderBetweenSquaresSim(svg, controls) {{
      function draw(n) {{
        const sq1 = n * n;
        const sq2 = (n + 1) * (n + 1);
        const count = 2 * n;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="35" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">2n Non-Square Theorem: ${{n}}² vs (${{n}}+1)²</text>

          <rect x="50" y="80" width="130" height="110" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="2" />
          <text x="115" y="115" fill="#94a3b8" font-size="12" text-anchor="middle">Lower Square</text>
          <text x="115" y="145" fill="#fff" font-size="20" font-weight="bold" text-anchor="middle">${{n}}² = ${{sq1}}</text>

          <rect x="420" y="80" width="130" height="110" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2" />
          <text x="485" y="115" fill="#94a3b8" font-size="12" text-anchor="middle">Next Square</text>
          <text x="485" y="145" fill="#fff" font-size="20" font-weight="bold" text-anchor="middle">${{n+1}}² = ${{sq2}}</text>

          <path d="M190 135 L410 135" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4" />
          <polygon points="410,135 400,130 400,140" fill="#f59e0b" />

          <rect x="210" y="100" width="180" height="70" rx="8" fill="#020617" stroke="#f59e0b" />
          <text x="300" y="125" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Non-Squares Trapped:</text>
          <text x="300" y="152" fill="#fff" font-size="18" font-weight="bold" text-anchor="middle">2 × ${{n}} = ${{count}}</text>

          <text x="300" y="240" fill="#cbd5e1" font-size="12" text-anchor="middle">Algebraic Proof: (${{n}}+1)² - ${{n}}² - 1 = (${{sq2}} - ${{sq1}} - 1) = ${{count}}</text>
          <text x="300" y="270" fill="#a5b4fc" font-size="12" text-anchor="middle">For n = 16: exactly 32 non-squares | For n = 99: exactly 198 non-squares</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Base Integer (n):</span>
          <input type="range" class="sim-slider" id="betweenSlider" min="1" max="30" value="7">
          <span class="slider-val" id="betweenVal">n = 7</span>
        </div>
      `;

      draw(7);
      document.getElementById('betweenSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('betweenVal').textContent = `n = ${{v}}`;
        draw(v);
      }});
    }}

    // 8. Triangular Numbers Merger
    function renderTriangularSim(svg, controls) {{
      function draw(n) {{
        const t1 = (n - 1) * n / 2;
        const t2 = n * (n + 1) / 2;
        const total = t1 + t2;

        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="30" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">T_{{${{n-1}}}} + T_{{${{n}}}} = ${{t1}} + ${{t2}} = ${{total}} = ${{n}}²</text>
        `;

        const startX = 220;
        const startY = 60;
        const cellSize = 180 / n;

        for (let r = 0; r < n; r++) {{
          for (let c = 0; c < n; c++) {{
            const isLower = (c <= r);
            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('x', startX + c * cellSize);
            rect.setAttribute('y', startY + r * cellSize);
            rect.setAttribute('width', cellSize - 1.5);
            rect.setAttribute('height', cellSize - 1.5);
            rect.setAttribute('rx', '3');
            rect.setAttribute('fill', isLower ? '#10b981' : '#6366f1');
            svg.appendChild(rect);
          }}
        }}

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', '300');
        text.setAttribute('y', '280');
        text.setAttribute('fill', '#f59e0b');
        text.setAttribute('font-size', '13');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('text-anchor', 'middle');
        text.textContent = `Green: T_{{${{n}}}} (${{t2}} dots) + Purple: T_{{${{n-1}}}} (${{t1}} dots) = ${{n}}² (${{n*n}} dots)`;
        svg.appendChild(text);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Square Side (n):</span>
          <input type="range" class="sim-slider" id="triSlider" min="2" max="6" value="4">
          <span class="slider-val" id="triVal">n = 4</span>
        </div>
      `;

      draw(4);
      document.getElementById('triSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('triVal').textContent = `n = ${{v}}`;
        draw(v);
      }});
    }}

    // 9. Square Root Inverter
    function renderSquareRootSim(svg, controls) {{
      function update(n) {{
        const sq = n * n;
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="35" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Bi-Directional Square & Square Root Engine</text>

          <rect x="70" y="80" width="160" height="150" rx="12" fill="#1e293b" stroke="#6366f1" stroke-width="2" />
          <text x="150" y="115" fill="#94a3b8" font-size="12" text-anchor="middle">Root (Side Length)</text>
          <text x="150" y="165" fill="#fff" font-size="36" font-weight="bold" text-anchor="middle">${{n}}</text>
          <text x="150" y="205" fill="#a5b4fc" font-size="12" text-anchor="middle">Dual: ±${{n}}</text>

          <rect x="370" y="80" width="160" height="150" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2" />
          <text x="450" y="115" fill="#94a3b8" font-size="12" text-anchor="middle">Square (Area)</text>
          <text x="450" y="165" fill="#34d399" font-size="36" font-weight="bold" text-anchor="middle">${{sq}}</text>
          <text x="450" y="205" fill="#6ee7b7" font-size="12" text-anchor="middle">${{sq}} sq units</text>

          <path d="M245 130 Q300 110 355 130" fill="none" stroke="#f59e0b" stroke-width="2.5" />
          <polygon points="355,130 345,123 347,135" fill="#f59e0b" />
          <text x="300" y="105" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Square (n²)</text>

          <path d="M355 175 Q300 195 245 175" fill="none" stroke="#38bdf8" stroke-width="2.5" />
          <polygon points="245,175 255,182 253,170" fill="#38bdf8" />
          <text x="300" y="215" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Square Root (√)</text>

          <text x="300" y="275" fill="#cbd5e1" font-size="13" text-anchor="middle">√${{sq}} = ${{n}} &emsp;|&emsp; (-${{n}})² = +${{sq}}</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Root Value (n):</span>
          <input type="range" class="sim-slider" id="rootSlider" min="1" max="25" value="9">
          <span class="slider-val" id="rootVal">n = 9</span>
        </div>
      `;

      update(9);
      document.getElementById('rootSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('rootVal').textContent = `n = ${{v}}`;
        update(v);
      }});
    }}

    // 10. Prime Factor Pairer
    function renderPrimeFactorSim(svg, controls) {{
      function test(num) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Prime Factor Pairing for ${{num}}</text>
        `;

        let factorStr = "";
        let rootStr = "";
        if (num === 324) {{
          factorStr = "324 = (2 × 2) × (3 × 3) × (3 × 3)";
          rootStr = "√324 = 2 × 3 × 3 = 18 (All factors paired!)";
        }} else if (num === 156) {{
          factorStr = "156 = (2 × 2) × 3 × 13";
          rootStr = "3 and 13 are UNPAIRED ⟹ NOT a square!";
        }} else if (num === 9408) {{
          factorStr = "9408 = 2⁶ × 3¹ × 7² = (2³ × 7)² × 3";
          rootStr = "Multiply by 3 to pair ⟹ √(9408 × 3) = 168";
        }}

        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', '60');
        rect.setAttribute('y', '70');
        rect.setAttribute('width', '480');
        rect.setAttribute('height', '180');
        rect.setAttribute('rx', '12');
        rect.setAttribute('fill', '#1e293b');
        rect.setAttribute('stroke', '#6366f1');
        rect.setAttribute('stroke-width', '1.5');
        svg.appendChild(rect);

        const t1 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t1.setAttribute('x', '300');
        t1.setAttribute('y', '125');
        t1.setAttribute('fill', '#fff');
        t1.setAttribute('font-size', '16');
        t1.setAttribute('font-weight', 'bold');
        t1.setAttribute('text-anchor', 'middle');
        t1.textContent = factorStr;
        svg.appendChild(t1);

        const t2 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t2.setAttribute('x', '300');
        t2.setAttribute('y', '175');
        t2.setAttribute('fill', '#10b981');
        t2.setAttribute('font-size', '14');
        t2.setAttribute('font-weight', 'bold');
        t2.setAttribute('text-anchor', 'middle');
        t2.textContent = rootStr;
        svg.appendChild(t2);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Inspect Sample:</span>
          <button class="sim-btn" onclick="runPrime(324)">324 (Square)</button>
          <button class="sim-btn" style="background:#be123c;" onclick="runPrime(156)">156 (Non-Square)</button>
          <button class="sim-btn" style="background:#0284c7;" onclick="runPrime(9408)">9408 (Make Square)</button>
        </div>
      `;

      window.runPrime = test;
      test(324);
    }}

    // 11. Cube Volume Builder
    function renderCubeVolumeSim(svg, controls) {{
      function draw(n) {{
        const vol = n * n * n;
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Solid Cube: Side = ${{n}} | Volume = ${{n}}³ = ${{vol}} unit blocks</text>
          
          <rect x="70" y="70" width="460" height="190" rx="12" fill="#1e293b" stroke="#8b5cf6" />
          <text x="120" y="115" fill="#a5b4fc" font-size="13">Horizontal Layers: <tspan fill="#fff" font-weight="bold">${{n}} layers</tspan></text>
          <text x="120" y="145" fill="#a5b4fc" font-size="13">Blocks per Layer: <tspan fill="#fff" font-weight="bold">${{n}} × ${{n}} = ${{n * n}} blocks</tspan></text>
          <text x="120" y="175" fill="#a5b4fc" font-size="13">Total Volume: <tspan fill="#34d399" font-weight="bold">${{n}} × (${{n * n}}) = ${{vol}} unit cubes</tspan></text>
          
          <rect x="350" y="100" width="130" height="130" rx="8" fill="#4c1d95" stroke="#a78bfa" stroke-width="2" />
          <text x="415" y="170" fill="#fff" font-size="22" font-weight="bold" text-anchor="middle">${{n}}³ = ${{vol}}</text>
          <text x="300" y="290" fill="#cbd5e1" font-size="12" text-anchor="middle">Geometric 3D multiplication: Length × Width × Height</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Cube Side Length (n):</span>
          <input type="range" class="sim-slider" id="cubeVolSlider" min="1" max="8" value="3">
          <span class="slider-val" id="cubeVolVal">n = 3</span>
        </div>
      `;

      draw(3);
      document.getElementById('cubeVolSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('cubeVolVal').textContent = `n = ${{v}}`;
        draw(v);
      }});
    }}

    // 12. Cube Digit Mapper
    function renderCubeDigitSim(svg, controls) {{
      function update(d) {{
        const cubeD = (d * d * d) % 10;
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Cubic Units Digit Mapping (All 0–9 Possible!)</text>

          <rect x="70" y="70" width="200" height="180" rx="12" fill="#1e293b" stroke="#6366f1" />
          <text x="170" y="110" fill="#94a3b8" font-size="12" text-anchor="middle">Base Integer Ends In</text>
          <text x="170" y="160" fill="#38bdf8" font-size="44" font-weight="bold" text-anchor="middle">...${{d}}</text>

          <rect x="330" y="70" width="200" height="180" rx="12" fill="#1e293b" stroke="#10b981" />
          <text x="430" y="110" fill="#94a3b8" font-size="12" text-anchor="middle">Cube Power Ends In</text>
          <text x="430" y="160" fill="#34d399" font-size="44" font-weight="bold" text-anchor="middle">...${{cubeD}}</text>

          <path d="M280 150 L320 150" stroke="#f59e0b" stroke-width="3" />
          <polygon points="320,150 310,144 310,156" fill="#f59e0b" />

          <text x="300" y="280" fill="#e2e8f0" font-size="12" text-anchor="middle">Reciprocal Pairs: 2 ↔ 8 (sum 10) &emsp;|&emsp; 3 ↔ 7 (sum 10)</text>
        `;
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Units Digit of Number:</span>
          <input type="range" class="sim-slider" id="cubeDigitSlider" min="0" max="9" value="7">
          <span class="slider-val" id="cubeDigitVal">ends in 7</span>
        </div>
      `;

      update(7);
      document.getElementById('cubeDigitSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('cubeDigitVal').textContent = `ends in ${{v}}`;
        update(v);
      }});
    }}

    // 13. Taxicab Simulator
    function renderTaxicabSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="0" y="0" width="600" height="320" fill="#090d16" />
        <text x="300" y="32" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">The Hardy–Ramanujan Number: 1729</text>

        <!-- Way 1 -->
        <rect x="60" y="70" width="220" height="180" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
        <text x="170" y="105" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Representation 1</text>
        <text x="170" y="145" fill="#fff" font-size="20" font-weight="bold" text-anchor="middle">1³ + 12³</text>
        <text x="170" y="180" fill="#a5b4fc" font-size="13" text-anchor="middle">1 + 1728 = 1729</text>
        <text x="170" y="215" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Small cube + Big cube</text>

        <!-- Way 2 -->
        <rect x="320" y="70" width="220" height="180" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
        <text x="430" y="105" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Representation 2</text>
        <text x="430" y="145" fill="#fff" font-size="20" font-weight="bold" text-anchor="middle">9³ + 10³</text>
        <text x="430" y="180" fill="#a5b4fc" font-size="13" text-anchor="middle">729 + 1000 = 1729</text>
        <text x="430" y="215" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Balanced pair</text>

        <text x="300" y="280" fill="#e2e8f0" font-size="12" text-anchor="middle">Smallest integer expressible as sum of two positive cubes in TWO different ways</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Explore More Taxicab Numbers:</span>
          <button class="sim-btn" onclick="showTaxi(1729)">1729</button>
          <button class="sim-btn" onclick="showTaxi(4104)">4104</button>
          <button class="sim-btn" onclick="showTaxi(13832)">13832</button>
        </div>
      `;

      window.showTaxi = (num) => {{
        if (num === 4104) {{
          svg.querySelector('text').textContent = 'Taxicab Number: 4104';
          svg.querySelectorAll('rect')[1].nextElementSibling.nextElementSibling.textContent = '2³ + 16³';
          svg.querySelectorAll('rect')[1].nextElementSibling.nextElementSibling.nextElementSibling.textContent = '8 + 4096 = 4104';
          svg.querySelectorAll('rect')[2].nextElementSibling.nextElementSibling.textContent = '9³ + 15³';
          svg.querySelectorAll('rect')[2].nextElementSibling.nextElementSibling.nextElementSibling.textContent = '729 + 3375 = 4104';
        }} else if (num === 13832) {{
          svg.querySelector('text').textContent = 'Taxicab Number: 13832';
          svg.querySelectorAll('rect')[1].nextElementSibling.nextElementSibling.textContent = '2³ + 24³';
          svg.querySelectorAll('rect')[1].nextElementSibling.nextElementSibling.nextElementSibling.textContent = '8 + 13824 = 13832';
          svg.querySelectorAll('rect')[2].nextElementSibling.nextElementSibling.textContent = '18³ + 20³';
          svg.querySelectorAll('rect')[2].nextElementSibling.nextElementSibling.nextElementSibling.textContent = '5832 + 8000 = 13832';
        }} else {{
          renderTaxicabSim(svg, controls);
        }}
      }};
    }}

    // 14. Nicomachus Pyramid
    function renderNicomachusSim(svg, controls) {{
      function draw(row) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Nicomachus Odd Pyramid: Row ${{row}} Sum = ${{row}}³</text>
        `;

        const startOdd = row * (row - 1) + 1;
        const odds = [];
        for (let i = 0; i < row; i++) odds.push(startOdd + i * 2);
        const sum = row * row * row;

        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', '40');
        rect.setAttribute('y', '65');
        rect.setAttribute('width', '520');
        rect.setAttribute('height', '180');
        rect.setAttribute('rx', '12');
        rect.setAttribute('fill', '#1e293b');
        rect.setAttribute('stroke', '#f59e0b');
        rect.setAttribute('stroke-width', '1.5');
        svg.appendChild(rect);

        const t1 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t1.setAttribute('x', '300');
        t1.setAttribute('y', '110');
        t1.setAttribute('fill', '#a5b4fc');
        t1.setAttribute('font-size', '13');
        t1.setAttribute('text-anchor', 'middle');
        t1.textContent = `${{row}} Consecutive Odd Numbers:`;
        svg.appendChild(t1);

        const t2 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t2.setAttribute('x', '300');
        t2.setAttribute('y', '155');
        t2.setAttribute('fill', '#fff');
        t2.setAttribute('font-size', '15');
        t2.setAttribute('font-weight', 'bold');
        t2.setAttribute('text-anchor', 'middle');
        t2.textContent = odds.join(' + ');
        svg.appendChild(t2);

        const t3 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t3.setAttribute('x', '300');
        t3.setAttribute('y', '205');
        t3.setAttribute('fill', '#34d399');
        t3.setAttribute('font-size', '20');
        t3.setAttribute('font-weight', 'bold');
        t3.setAttribute('text-anchor', 'middle');
        t3.textContent = `= ${{sum}} = ${{row}}³`;
        svg.appendChild(t3);

        const t4 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t4.setAttribute('x', '300');
        t4.setAttribute('y', '280');
        t4.setAttribute('fill', '#cbd5e1');
        t4.setAttribute('font-size', '12');
        t4.setAttribute('text-anchor', 'middle');
        t4.textContent = `First odd number formula: n² - n + 1 = ${{row}}² - ${{row}} + 1 = ${{startOdd}}`;
        svg.appendChild(t4);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Pyramid Row (n):</span>
          <input type="range" class="sim-slider" id="nicoSlider" min="1" max="6" value="3">
          <span class="slider-val" id="nicoVal">Row 3</span>
        </div>
      `;

      draw(3);
      document.getElementById('nicoSlider').addEventListener('input', (e) => {{
        const v = parseInt(e.target.value);
        document.getElementById('nicoVal').textContent = `Row ${{v}}`;
        draw(v);
      }});
    }}

    // 15. Cube Root Triplet Simulator
    function renderCubeRootTripletSim(svg, controls) {{
      function test(num) {{
        svg.innerHTML = `
          <rect x="0" y="0" width="600" height="320" fill="#090d16" />
          <text x="300" y="32" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Cube Root Extraction by Prime Factor Triplets</text>
        `;

        let fStr = "";
        let rStr = "";
        if (num === 3375) {{
          fStr = "3375 = (3 × 3 × 3) × (5 × 5 × 5) = 3³ × 5³";
          rStr = "∛3375 = 3 × 5 = 15 (Complete Triplets)";
        }} else if (num === 1323) {{
          fStr = "1323 = (3 × 3 × 3) × (7 × 7) = 3³ × 7²";
          rStr = "7 is missing one factor! Multiply by 7 ⟹ 9261 = 21³";
        }} else if (num === 500) {{
          fStr = "500 = (2 × 2) × (5 × 5 × 5) = 2² × 5³";
          rStr = "2 occurs only twice ⟹ Divide by 4 (leaves 125=5³) or multiply by 2 (1000=10³)";
        }}

        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', '60');
        rect.setAttribute('y', '75');
        rect.setAttribute('width', '480');
        rect.setAttribute('height', '180');
        rect.setAttribute('rx', '12');
        rect.setAttribute('fill', '#1e293b');
        rect.setAttribute('stroke', '#a855f7');
        rect.setAttribute('stroke-width', '1.5');
        svg.appendChild(rect);

        const t1 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t1.setAttribute('x', '300');
        t1.setAttribute('y', '130');
        t1.setAttribute('fill', '#fff');
        t1.setAttribute('font-size', '15');
        t1.setAttribute('font-weight', 'bold');
        t1.setAttribute('text-anchor', 'middle');
        t1.textContent = fStr;
        svg.appendChild(t1);

        const t2 = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        t2.setAttribute('x', '300');
        t2.setAttribute('y', '180');
        t2.setAttribute('fill', '#34d399');
        t2.setAttribute('font-size', '13');
        t2.setAttribute('font-weight', 'bold');
        t2.setAttribute('text-anchor', 'middle');
        t2.textContent = rStr;
        svg.appendChild(t2);
      }}

      controls.innerHTML = `
        <div class="control-row">
          <span class="slider-label">Inspect Sample:</span>
          <button class="sim-btn" onclick="runTrip(3375)">3375 (Cube)</button>
          <button class="sim-btn" style="background:#be123c;" onclick="runTrip(1323)">1323 (Multiply 7)</button>
          <button class="sim-btn" style="background:#0284c7;" onclick="runTrip(500)">500 (Divide 4 / Mul 2)</button>
        </div>
      `;

      window.runTrip = test;
      test(3375);
    }}

    // 16. Finite Difference Cascade
    function renderFiniteDifferenceSim(svg, controls) {{
      svg.innerHTML = `
        <rect x="0" y="0" width="600" height="320" fill="#090d16" />
        <text x="300" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Successive Differences Cascade</text>

        <!-- Squares -->
        <rect x="50" y="55" width="240" height="200" rx="10" fill="#1e293b" stroke="#3b82f6" />
        <text x="170" y="85" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Perfect Squares (Degree 2)</text>
        <text x="170" y="115" fill="#fff" font-size="11" text-anchor="middle">1,  4,  9,  16,  25,  36</text>
        <text x="170" y="150" fill="#f59e0b" font-size="11" text-anchor="middle">Δ¹: 3,  5,  7,  9,  11 (Odds)</text>
        <text x="170" y="185" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Δ²: 2,  2,  2,  2 (Constant 2! = 2)</text>

        <!-- Cubes -->
        <rect x="310" y="55" width="240" height="200" rx="10" fill="#1e293b" stroke="#a855f7" />
        <text x="430" y="85" fill="#a855f7" font-size="13" font-weight="bold" text-anchor="middle">Perfect Cubes (Degree 3)</text>
        <text x="430" y="115" fill="#fff" font-size="11" text-anchor="middle">1,  8,  27,  64,  125,  216</text>
        <text x="430" y="145" fill="#f59e0b" font-size="11" text-anchor="middle">Δ¹: 7,  19,  37,  61,  91</text>
        <text x="430" y="175" fill="#38bdf8" font-size="11" text-anchor="middle">Δ²: 12,  18,  24,  30</text>
        <text x="430" y="205" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Δ³: 6,  6,  6 (Constant 3! = 6)</text>

        <text x="300" y="285" fill="#e2e8f0" font-size="12" text-anchor="middle">Aryabhata (499 CE): Varga (Square), Ghana (Cube), Mula (Root / Origin)</text>
      `;

      controls.innerHTML = `
        <div class="control-row">
          <span style="color:#94a3b8; font-size:12px;">The k-th finite difference of a polynomial of degree k is always constant and equals k!</span>
        </div>
      `;
    }}
  </script>
</body>
</html>
"""

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public', 'animations', 'class8-math-square-and-cube.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Successfully generated {output_path} ({len(html_template)} bytes).")

if __name__ == '__main__':
    generate_lab_html()
