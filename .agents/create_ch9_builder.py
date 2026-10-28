# -*- coding: utf-8 -*-
"""
Script to create .agents/build_class7_math_geometric_twins_lab.py
"""

code = r'''# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class7-math-geometric-twins.html
Class 7 Mathematics - Chapter 9: Geometric Twins (Congruence)
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Acharya Varāhamihira)
- 16 bespoke interactive SVG simulators
- Prominent Key Technical Vocabulary Badges on every content slide
- 32 in-slide checkpoints with instant feedback
- 4 dedicated mastery quiz challenge slides (40 questions total)
- Step-by-step solution pop-up modal (#solutionModal style="display: none;" with z-index: 99999 !important;)
- Slide 20 completion banner ("🎉 You have reached the last slide of this chapter!") hiding nextBtn
- Strictly zero occurrences of prohibited textbook titles
"""

import json
import os
import sys

sys.path.insert(0, '.agents')
from class7_math_geometric_twins_data import SLIDES_DATA, QUIZ_QUESTIONS
from class7_math_geometric_twins_sims import SIMULATORS
from class7_math_geometric_twins_js import SIMULATORS_JS

# Assemble full slides data
full_slides = []
for slide in SLIDES_DATA:
    s = dict(slide)
    if s.get("quiz_range"):
        start_q, end_q = s["quiz_range"]
        s["questions"] = QUIZ_QUESTIONS[start_q - 1:end_q]
        s["is_quiz"] = True
    else:
        s["is_quiz"] = False
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)
QUIZ_QUESTIONS_JSON = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)
SIMULATORS_JSON = json.dumps(SIMULATORS, ensure_ascii=False)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Mathematics • Chapter 9: Geometric Twins (Congruence) Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script>
    function triggerMathRender(el) {
      const target = el || document.body;
      if (typeof renderMathInElement === 'function') {
        try {
          renderMathInElement(target, {
            delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\[', right: '\\]', display: true},
              {left: '\\(', right: '\\)', display: false}
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
          });
        } catch (e) {
          console.warn('KaTeX render error:', e);
        }
      } else {
        setTimeout(() => triggerMathRender(target), 80);
      }
    }
    window.triggerMathRender = triggerMathRender;
  </script>

  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-dark: #070d19;
      --card-bg: rgba(15, 23, 42, 0.85);
      --border-glow: rgba(56, 189, 248, 0.25);
      --accent-cyan: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
    }

    * {
      box-sizing: border-box;
      user-select: none;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.5) 0px, transparent 100%);
      background-attachment: fixed;
      color: #f8fafc;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Custom Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(15, 23, 42, 0.6);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(56, 189, 248, 0.3);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(56, 189, 248, 0.5);
    }

    /* Top Navigation Bar */
    .top-header {
      background: rgba(11, 19, 38, 0.85);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .brand-title {
      font-weight: 800;
      font-size: 1.05rem;
      background: linear-gradient(135deg, #38bdf8 0%, #fbbf24 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .slide-badge-pill {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #7dd3fc;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.03em;
    }

    /* Main Container */
    .main-container {
      flex: 1;
      max-width: 1560px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      padding: 1rem 1.5rem;
      gap: 1rem;
    }

    /* Teacher Avatar & Speech Bar */
    .avatar-speech-bar {
      background: linear-gradient(135deg, rgba(12, 21, 39, 0.95), rgba(30, 58, 138, 0.35));
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 16px;
      padding: 0.85rem 1.25rem;
      display: flex;
      align-items: center;
      gap: 1.2rem;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
    }

    .avatar-wrapper {
      position: relative;
      flex-shrink: 0;
    }

    .avatar-img-circle {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #1e3a8a, #070d19);
      border: 2px solid var(--accent-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
      transition: transform 0.3s;
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 2px solid #38bdf8;
      animation: avatarPulse 1.5s infinite;
      opacity: 0;
      pointer-events: none;
    }

    .is-speaking .avatar-speaking-pulse {
      opacity: 1;
    }

    @keyframes avatarPulse {
      0% { transform: scale(1); opacity: 0.8; }
      100% { transform: scale(1.25); opacity: 0; }
    }

    .teacher-meta {
      flex-shrink: 0;
      min-width: 220px;
    }

    .teacher-name {
      font-size: 0.95rem;
      font-weight: 800;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .teacher-badge {
      font-size: 0.75rem;
      color: #94a3b8;
      font-weight: 600;
    }

    .speech-bubble-area {
      flex: 1;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .speech-bubble-text {
      font-size: 0.88rem;
      line-height: 1.45;
      color: #e2e8f0;
      font-weight: 500;
    }

    .voice-ctrl-btn {
      flex-shrink: 0;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .voice-ctrl-btn:hover {
      background: rgba(56, 189, 248, 0.28);
      transform: scale(1.05);
    }

    /* Slide Grid Layout (Slides 1 to 16) */
    .slide-content-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      flex: 1;
      min-height: 0;
    }

    @media (max-width: 1024px) {
      .slide-content-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Left Theory Card */
    .theory-card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 1.25rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      overflow-y: auto;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      max-height: 680px;
    }

    .theory-header {
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.75rem;
    }

    .section-tag {
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-amber);
      display: block;
      margin-bottom: 0.25rem;
    }

    .slide-main-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.25;
    }

    .theory-body {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #cbd5e1;
    }

    /* In-Slide Checkpoints Section */
    .checkpoints-section {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 1rem;
      margin-top: auto;
    }

    .checkpoints-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .checkpoint-card {
      background: rgba(12, 21, 39, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 0.75rem;
      margin-bottom: 0.6rem;
    }

    .checkpoint-card:last-child {
      margin-bottom: 0;
    }

    .checkpoint-question {
      font-size: 0.88rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 0.6rem;
      line-height: 1.4;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }

    @media (max-width: 600px) {
      .checkpoint-options {
        grid-template-columns: 1fr;
      }
    }

    .chk-btn {
      background: rgba(30, 41, 59, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #e2e8f0;
      border-radius: 8px;
      padding: 0.5rem 0.65rem;
      font-size: 0.82rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .chk-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-1px);
    }

    .chk-btn.correct {
      background: rgba(16, 185, 129, 0.28) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 700;
    }

    .chk-btn.incorrect {
      background: rgba(244, 63, 94, 0.28) !important;
      border-color: #f43f5e !important;
      color: #fda4af !important;
    }

    .checkpoint-feedback {
      margin-top: 0.5rem;
      font-size: 0.8rem;
      border-radius: 6px;
      padding: 0.4rem 0.6rem;
      display: none;
    }

    .checkpoint-feedback.visible {
      display: block;
    }

    .checkpoint-feedback.success {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
    }

    .checkpoint-feedback.error {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fb7185;
    }

    /* Right Lab Simulator Card */
    .lab-card {
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      max-height: 680px;
      overflow-y: auto;
    }

    .lab-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.75rem;
    }

    .lab-header-left {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .lab-badge {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #34d399;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .sim-header-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
    }

    /* Mastery Quiz Container (Slides 17 to 20) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 1rem;
      background: var(--card-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 1.5rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      max-height: 700px;
      overflow-y: auto;
    }

    .quiz-header-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 1rem;
      margin-bottom: 0.5rem;
    }

    .quiz-score-pill {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.4rem 1rem;
      border-radius: 9999px;
    }

    .quiz-items-list {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .quiz-item-card {
      background: rgba(12, 21, 39, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 1rem 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .quiz-item-qtext {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
      line-height: 1.45;
    }

    .quiz-options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
    }

    @media (max-width: 640px) {
      .quiz-options-grid {
        grid-template-columns: 1fr;
      }
    }

    .quiz-opt-btn {
      background: rgba(30, 41, 59, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      border-radius: 10px;
      padding: 0.65rem 0.85rem;
      font-size: 0.88rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      transition: all 0.2s;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      color: #ffffff;
      transform: translateY(-1px);
    }

    .quiz-opt-btn.selected {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      color: #ffffff;
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.3) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.3) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .quiz-actions-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 0.35rem;
      padding-top: 0.6rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      gap: 0.75rem;
    }

    .btn-submit-quiz {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.82rem;
      padding: 0.45rem 1rem;
      border-radius: 8px;
      border: 1px solid rgba(56, 189, 248, 0.4);
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-submit-quiz:hover:not(:disabled) {
      background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
      transform: translateY(-1px);
    }

    .btn-submit-quiz:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    .btn-show-solution {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      font-weight: 700;
      font-size: 0.82rem;
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .btn-show-solution:hover {
      background: rgba(245, 158, 11, 0.28);
      transform: translateY(-1px);
    }

    /* Step-by-Step Solution Pop-Up Modal (#solutionModal) */
    #solutionModal {
      position: fixed;
      inset: 0;
      z-index: 99999 !important;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }

    #solutionModal.is-active {
      display: flex !important;
    }

    .modal-content-card {
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 20px;
      max-width: 680px;
      width: 100%;
      padding: 1.5rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-height: 85vh;
      overflow-y: auto;
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
    }

    .modal-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-close-modal {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #94a3b8;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      transition: all 0.2s;
    }

    .btn-close-modal:hover {
      background: rgba(244, 63, 94, 0.2);
      border-color: #f43f5e;
      color: #f43f5e;
    }

    .modal-question {
      font-size: 0.95rem;
      font-weight: 700;
      color: #e2e8f0;
      background: rgba(15, 23, 42, 0.7);
      padding: 0.85rem;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .modal-solution-steps {
      font-size: 0.9rem;
      line-height: 1.6;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    /* Footer Navigation */
    .footer-nav {
      background: rgba(11, 19, 38, 0.85);
      backdrop-filter: blur(16px);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      position: sticky;
      bottom: 0;
      z-index: 50;
    }

    .nav-btn {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #f8fafc;
      padding: 0.6rem 1.25rem;
      border-radius: 10px;
      font-weight: 700;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
      transition: all 0.2s;
    }

    .nav-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      transform: translateY(-1px);
    }

    .nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .jump-select {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #f8fafc;
      padding: 0.55rem 0.85rem;
      border-radius: 10px;
      font-size: 0.88rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }

    .jump-select option {
      background: #0f172a;
      color: #f8fafc;
    }

    #lastSlideNotice {
      display: none;
      align-items: center;
      gap: 0.4rem;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.45rem 1rem;
      border-radius: 10px;
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="top-header">
    <div class="brand-title">
      <span>📐</span>
      <span>NCERT Class 7 Maths • Chapter 9: Geometric Twins (Congruence)</span>
    </div>

    <div style="display:flex; align-items:center; gap:0.75rem;">
      <span id="slideCounter" class="slide-badge-pill">Slide 1 / 20</span>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-container">
    
    <!-- Virtual Avatar & Narration Speech Bar -->
    <section class="avatar-speech-bar" id="avatarSpeechBar">
      <div class="avatar-wrapper">
        <div id="avatarCircle" class="avatar-img-circle">
          <!-- Stylized Ancient Indian Scholar Avatar SVG for Acharya Varāhamihira -->
          <svg width="48" height="48" viewBox="0 0 100 100" fill="none">
            <!-- Aura Background Circle -->
            <circle cx="50" cy="50" r="44" fill="#1e3a8a"/>
            <!-- Celestial Geometric Radiance -->
            <polygon points="50,10 62,38 92,38 68,56 77,84 50,67 23,84 32,56 8,38 38,38" stroke="#f59e0b" stroke-width="1.2" fill="none" opacity="0.6"/>
            <!-- Head & Torso -->
            <circle cx="50" cy="38" r="16" fill="#fed7aa"/>
            <!-- Tilak mark on forehead -->
            <line x1="50" y1="28" x2="50" y2="34" stroke="#dc2626" stroke-width="2"/>
            <circle cx="50" cy="35" r="1" fill="#f59e0b"/>
            <!-- Saffron Robe / Shawl -->
            <path d="M 24,78 C 24,56 40,54 50,54 C 60,54 76,56 76,78 Z" fill="#d97706"/>
            <!-- Yajnopavita / Sacred Cord -->
            <line x1="38" y1="54" x2="64" y2="78" stroke="#fef08a" stroke-width="2" stroke-dasharray="2 1"/>
            <!-- Astrological / Geometric Twin Symbols on Shawl -->
            <circle cx="42" cy="66" r="3" stroke="#38bdf8" stroke-width="1" fill="none"/>
            <circle cx="58" cy="66" r="3" stroke="#38bdf8" stroke-width="1" fill="none"/>
            <!-- Beard & Moustache -->
            <path d="M 43,47 Q 50,58 57,47 Q 50,52 43,47 Z" fill="#475569"/>
            <!-- Serene Eyes -->
            <circle cx="44" cy="38" r="1.5" fill="#0f172a"/>
            <circle cx="56" cy="38" r="1.5" fill="#0f172a"/>
            <!-- Smiling mouth -->
            <path id="avatarMouth" d="M 47,48 Q 50,51 53,48" stroke="#92400e" stroke-width="1.5" fill="none"/>
            <!-- Hand holding Geometric Compass / Divider -->
            <line x1="72" y1="62" x2="67" y2="76" stroke="#fde047" stroke-width="2"/>
            <line x1="72" y1="62" x2="77" y2="76" stroke="#fde047" stroke-width="2"/>
            <circle cx="72" cy="62" r="2.5" fill="#b45309"/>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="teacher-meta">
        <div class="teacher-name">
          <span>Acharya Varāhamihira</span>
          <span style="font-size:0.75rem;">📐</span>
        </div>
        <div class="teacher-badge">Master of Geometric Symmetry & Celestial Harmonies</div>
      </div>

      <div class="speech-bubble-area">
        <div id="speechBubbleText" class="speech-bubble-text">Loading classroom narration...</div>
        <button id="btnVoiceToggle" class="voice-ctrl-btn" title="Toggle Audio Narration">
          <svg id="iconVoicePlay" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
          </svg>
          <svg id="iconVoicePause" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;">
            <rect x="6" y="4" width="4" height="16"/>
            <rect x="14" y="4" width="4" height="16"/>
          </svg>
        </button>
      </div>
    </section>

    <!-- Normal Slide Grid Layout (Slides 1 to 16) -->
    <div id="slideContentGrid" class="slide-content-grid">
      
      <!-- Left: Theory & Checkpoints -->
      <section class="theory-card" id="theoryCol">
        <div class="theory-header">
          <span id="slideTag" class="section-tag">9.1 Introduction</span>
          <h2 id="slideTitle" class="slide-main-title">Geometric Twins & Superposition</h2>
        </div>

        <div id="theoryBody" class="theory-body">
          <!-- Slide theory injected here -->
        </div>

        <!-- In-Slide Checkpoints -->
        <div class="checkpoints-section" id="checkpointsSection">
          <div class="checkpoints-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
            </svg>
            <span>Interactive Concept Checkpoints</span>
          </div>
          <div id="checkpointsContainer" style="display:flex; flex-direction:column; gap:0.6rem;">
            <!-- 2 Checkpoints injected here -->
          </div>
        </div>
      </section>

      <!-- Right: Interactive Laboratory Simulator -->
      <section class="lab-card" id="labCol">
        <div class="lab-header">
          <div class="lab-header-left">
            <span class="lab-badge">Live Interactive Simulator</span>
            <span id="simHeaderTitle" class="sim-header-title">Geometric Twins Lab</span>
          </div>
        </div>

        <div id="simContainer" class="w-full">
          <!-- Simulator HTML injected here -->
        </div>
      </section>
    </div>

    <!-- Mastery Quiz Challenge View (Slides 17 to 20) -->
    <section id="quizContainer" class="quiz-container">
      <div class="quiz-header-card">
        <div class="quiz-title-area">
          <span id="quizBadge" class="section-tag">Chapter Review & Mastery</span>
          <h2 id="quizTitle" class="slide-main-title">Mastery Challenge: Geometric Twins</h2>
        </div>
        <div id="quizScorePill" class="quiz-score-pill">Score: 0 / 10</div>
      </div>

      <div id="quizItemsList" class="quiz-items-list">
        <!-- 10 Questions injected here -->
      </div>
    </section>

  </main>

  <!-- Step-by-Step Solution Pop-Up Modal (#solutionModal style="display: none;") -->
  <div id="solutionModal" style="display: none;">
    <div class="modal-content-card">
      <div class="modal-header">
        <div class="modal-title">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 16v-4"/>
            <path d="M12 8h.01"/>
          </svg>
          <span id="modalTitleText">Step-by-Step Solution</span>
        </div>
        <button id="btnCloseModal" class="btn-close-modal" title="Close Solution">✕</button>
      </div>

      <div id="modalQuestionText" class="modal-question">Question text here...</div>
      <div id="modalSolutionSteps" class="modal-solution-steps">Solution derivation here...</div>
    </div>
  </div>

  <!-- Bottom Navigation Footer -->
  <footer class="footer-nav">
    <button id="prevBtn" class="nav-btn" disabled>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="15 18 9 12 15 6"/>
      </svg>
      <span>Previous</span>
    </button>

    <div style="display:flex; align-items:center; gap:0.8rem;">
      <select id="slideJumpSelect" class="jump-select">
        <!-- 20 options dynamically generated -->
      </select>

      <!-- Terminal Slide 20 Notice -->
      <div id="lastSlideNotice">
        <span>🎉 You have reached the last slide of this chapter!</span>
      </div>
    </div>

    <button id="nextBtn" class="nav-btn">
      <span>Next</span>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="9 18 15 12 9 6"/>
      </svg>
    </button>
  </footer>

  <!-- Application Logic & Interactive Engines -->
  <script>
    const SLIDES_DATA = """ + SLIDES_JSON + r""";
    const QUIZ_QUESTIONS = """ + QUIZ_QUESTIONS_JSON + r""";
    const SIMULATORS = """ + SIMULATORS_JSON + r""";

    let currentSlideIdx = 0;
    let quizSelectedAnswers = {};
    let quizSubmittedStatus = {};
    let isSpeaking = false;
    let speechSynth = window.speechSynthesis;
    let speechUtterance = null;

    // Web Audio API Synthesis
    class SoundFX {
      constructor() {
        this.ctx = null;
      }
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      }
      playChime() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(1046.50, now + 0.35);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.35);
      }
      playBuzzer() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, now);
        osc.frequency.linearRampToValueAtTime(110, now + 0.28);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.28);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.28);
      }
      playClick() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, now);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.05);
      }
    }
    const sfx = new SoundFX();

    // DOM Elements
    const slideCounter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');
    const slideJumpSelect = document.getElementById('slideJumpSelect');

    const avatarCircle = document.getElementById('avatarCircle');
    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const slideTag = document.getElementById('slideTag');
    const slideTitle = document.getElementById('slideTitle');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsContainer = document.getElementById('checkpointsContainer');

    const labCol = document.getElementById('labCol');
    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simContainer = document.getElementById('simContainer');

    const quizContainer = document.getElementById('quizContainer');
    const quizBadge = document.getElementById('quizBadge');
    const quizTitle = document.getElementById('quizTitle');
    const quizScorePill = document.getElementById('quizScorePill');
    const quizItemsList = document.getElementById('quizItemsList');

    const solutionModal = document.getElementById('solutionModal');
    const btnCloseModal = document.getElementById('btnCloseModal');
    const modalTitleText = document.getElementById('modalTitleText');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');

    // Populate Jump Select
    SLIDES_DATA.forEach((s, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${s.slide_num}. ${s.title}`;
      slideJumpSelect.appendChild(opt);
    });

    // Voice Synthesis Controls
    function stopNarration() {
      if (speechSynth && speechSynth.speaking) {
        speechSynth.cancel();
      }
      isSpeaking = false;
      avatarSpeechBar.classList.remove('is-speaking');
      iconVoicePlay.style.display = 'block';
      iconVoicePause.style.display = 'none';
    }

    function speakNarration(text) {
      stopNarration();
      if (!('speechSynthesis' in window)) return;
      if (!text) return;

      const cleanText = text.replace(/<[^>]+>/g, '').replace(/\$+/g, '').replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1 over $2');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 0.95;
      speechUtterance.pitch = 1.0;

      speechUtterance.onstart = () => {
        isSpeaking = true;
        avatarSpeechBar.classList.add('is-speaking');
        iconVoicePlay.style.display = 'none';
        iconVoicePause.style.display = 'block';
      };

      speechUtterance.onend = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechUtterance.onerror = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechSynth.speak(speechUtterance);
    }

    btnVoiceToggle.addEventListener('click', () => {
      sfx.playClick();
      if (isSpeaking) {
        stopNarration();
      } else {
        const slide = SLIDES_DATA[currentSlideIdx];
        if (slide && slide.narration) {
          speakNarration(slide.narration);
        }
      }
    });

    // Render Checkpoints
    function renderCheckpoints(checkpoints) {
      checkpointsContainer.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) return;

      checkpoints.forEach((chk, cIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const qTitle = document.createElement('div');
        qTitle.className = 'checkpoint-question';
        qTitle.innerHTML = `<strong>CP ${chk.id}:</strong> ${chk.question}`;
        card.appendChild(qTitle);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'checkpoint-options';

        const feedback = document.createElement('div');
        feedback.className = 'checkpoint-feedback';
        card.appendChild(optsDiv);
        card.appendChild(feedback);

        chk.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'chk-btn';
          btn.innerHTML = `<span>${String.fromCharCode(65 + oIdx)}.</span> <span>${optText}</span>`;
          btn.addEventListener('click', () => {
            sfx.playClick();
            handleCheckpointChoice(chk, oIdx, optsDiv, feedback);
          });
          optsDiv.appendChild(btn);
        });

        checkpointsContainer.appendChild(card);
      });
    }

    function handleCheckpointChoice(chk, chosenIdx, optsDiv, feedback) {
      const buttons = optsDiv.querySelectorAll('button');
      buttons.forEach(b => b.disabled = true);

      if (chosenIdx === chk.correct) {
        sfx.playChime();
        buttons[chosenIdx].classList.add('correct');
        feedback.className = 'checkpoint-feedback visible success';
        feedback.textContent = `✓ Correct! ${chk.explanation}`;
      } else {
        sfx.playBuzzer();
        buttons[chosenIdx].classList.add('incorrect');
        buttons[chk.correct].classList.add('correct');
        feedback.className = 'checkpoint-feedback visible error';
        feedback.textContent = `✕ Incorrect. ${chk.explanation}`;
      }
    }

    // Render Simulator
    function renderSimulator(simId) {
      if (!simContainer) return;
      simContainer.innerHTML = SIMULATORS[simId] || '';

      // Initialize simulator logic
      switch(simId) {
        case 'sim-superposition-flipper':
          if (typeof updateSuperposition === 'function') updateSuperposition();
          break;
        case 'sim-simple-figures-congruence':
          if (typeof setSimpleFigureMode === 'function') setSimpleFigureMode('lines');
          break;
        case 'sim-triangle-correspondence':
          if (typeof renderTriangleCorrespondence === 'function') renderTriangleCorrespondence('A');
          break;
        case 'sim-sss-congruence':
          if (typeof updateSSS === 'function') updateSSS();
          break;
        case 'sim-sas-congruence':
          if (typeof updateSAS === 'function') updateSAS();
          break;
        case 'sim-included-angle-trap':
          if (typeof setTrapMode === 'function') setTrapMode('included');
          break;
        case 'sim-asa-congruence':
          if (typeof updateASA === 'function') updateASA();
          break;
        case 'sim-aas-congruence':
          if (typeof updateAAS === 'function') updateAAS();
          break;
        case 'sim-rhs-congruence':
          if (typeof updateRHS === 'function') updateRHS();
          break;
        case 'sim-aaa-counterexample':
          if (typeof updateAAA === 'function') updateAAA();
          break;
        case 'sim-ssa-ambiguous-case':
          if (typeof renderSSAPendulum === 'function') renderSSAPendulum();
          break;
        case 'sim-isosceles-base-angles':
          if (typeof updateIsosceles === 'function') updateIsosceles();
          break;
        case 'sim-equilateral-60deg':
          if (typeof updateEquilateral === 'function') updateEquilateral();
          break;
        case 'sim-congruence-criteria-sorter':
          if (typeof resetSorterGame === 'function') resetSorterGame();
          break;
        case 'sim-real-world-twins':
          if (typeof setRwMode === 'function') setRwMode('bridge');
          break;
        case 'sim-congruence-puzzle-lab':
          if (typeof resetCpctcPuzzle === 'function') resetCpctcPuzzle();
          break;
      }
    }

    // Modal Solution Opener & Closer (Globally attached to window)
    function openSolutionModal(qOrId) {
      sfx.playClick();
      let q = (typeof qOrId === 'object' && qOrId !== null) ? qOrId : QUIZ_QUESTIONS.find(item => item.id === Number(qOrId));
      if (!q) {
        console.warn('Question not found for solution modal:', qOrId);
        return;
      }

      if (modalTitleText) modalTitleText.textContent = `Question ${q.id} Detailed Solution`;
      if (modalQuestionText) modalQuestionText.innerHTML = `<strong>Q${q.id}:</strong> ${q.question}`;
      
      const correctOptText = (q.options && q.options[q.correct] !== undefined) ? q.options[q.correct] : '';
      const solutionContent = q.solution || (q.solution_steps ? q.solution_steps.join('<br>') : '') || q.explanation || 'Detailed step-by-step derivation provided above.';

      if (modalSolutionSteps) {
        modalSolutionSteps.innerHTML = `
          <div style="font-weight:800; color:#34d399; margin-bottom:0.6rem; font-size:0.95rem;">
            ✓ Correct Answer: Option ${String.fromCharCode(65 + q.correct)} (${correctOptText})
          </div>
          <div style="color:#e2e8f0; line-height:1.6;">${solutionContent}</div>
        `;
      }

      if (solutionModal) {
        solutionModal.style.setProperty('display', 'flex', 'important');
        solutionModal.classList.add('is-active');
      }
      if (window.triggerMathRender) triggerMathRender(solutionModal);
    }
    window.openSolutionModal = openSolutionModal;

    function closeSolutionModal() {
      sfx.playClick();
      if (solutionModal) {
        solutionModal.style.setProperty('display', 'none', 'important');
        solutionModal.classList.remove('is-active');
      }
    }
    window.closeSolutionModal = closeSolutionModal;

    if (btnCloseModal) btnCloseModal.addEventListener('click', closeSolutionModal);
    if (solutionModal) {
      solutionModal.addEventListener('click', (e) => {
        if (e.target === solutionModal) {
          closeSolutionModal();
        }
      });
    }

    // Render Quiz Slide
    function renderQuizSlide(slide) {
      slideContentGrid.style.display = 'none';
      quizContainer.style.display = 'flex';

      quizBadge.textContent = slide.badge || 'Chapter Review';
      quizTitle.textContent = slide.title;

      const questions = slide.questions || [];
      quizItemsList.innerHTML = '';

      let score = 0;
      let answeredCount = 0;

      questions.forEach((q, qIndex) => {
        const qCard = document.createElement('div');
        qCard.className = 'quiz-item-card';

        const hasSubmitted = quizSubmittedStatus[q.id];
        const selected = quizSelectedAnswers[q.id];

        let optsHtml = '';
        q.options.forEach((optText, optIdx) => {
          let btnClass = 'quiz-opt-btn';
          if (hasSubmitted) {
            if (optIdx === q.correct) btnClass += ' correct';
            else if (optIdx === selected) btnClass += ' incorrect';
          } else if (selected === optIdx) {
            btnClass += ' selected';
          }
          optsHtml += `<button class="${btnClass}" onclick="selectQuizOption(${q.id}, ${optIdx})" ${hasSubmitted ? 'disabled' : ''}>
            <span style="font-weight:700; width:20px;">${String.fromCharCode(65 + optIdx)}.</span>
            <span>${optText}</span>
          </button>`;
        });

        qCard.innerHTML = `
          <div class="quiz-item-qtext">Q${q.id}. ${q.question}</div>
          <div class="quiz-options-grid">${optsHtml}</div>
          <div class="quiz-actions-row">
            <button class="btn-submit-quiz" onclick="submitQuizAnswer(${q.id}, ${q.correct})" ${hasSubmitted || selected === undefined ? 'disabled' : ''}>
              ${hasSubmitted ? 'Answered' : 'Submit Answer'}
            </button>
            <button type="button" class="btn-show-solution">
              <span>💡 View Step-by-Step Solution</span>
            </button>
          </div>
        `;

        // Direct robust event listener for solution modal
        const btnSol = qCard.querySelector('.btn-show-solution');
        if (btnSol) {
          btnSol.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            openSolutionModal(q);
          });
        }

        if (hasSubmitted) {
          answeredCount++;
          if (selected === q.correct) score++;
        }

        quizItemsList.appendChild(qCard);
      });

      quizScorePill.textContent = `Score: ${score} / ${questions.length}`;
      if (window.triggerMathRender) triggerMathRender(quizContainer);
    }

    function selectQuizOption(qId, optIdx) {
      sfx.playClick();
      quizSelectedAnswers[qId] = optIdx;
      renderQuizSlide(SLIDES_DATA[currentSlideIdx]);
    }
    window.selectQuizOption = selectQuizOption;

    function submitQuizAnswer(qId, correctIdx) {
      const selected = quizSelectedAnswers[qId];
      if (selected === undefined) return;
      quizSubmittedStatus[qId] = true;

      if (selected === correctIdx) {
        sfx.playChime();
      } else {
        sfx.playBuzzer();
      }

      renderQuizSlide(SLIDES_DATA[currentSlideIdx]);
    }
    window.submitQuizAnswer = submitQuizAnswer;

    // Main Slide Renderer
    function renderSlide(idx) {
      if (idx < 0 || idx >= SLIDES_DATA.length) return;
      currentSlideIdx = idx;
      const slide = SLIDES_DATA[idx];

      slideCounter.textContent = `Slide ${slide.slide_num} / ${SLIDES_DATA.length}`;
      slideJumpSelect.value = idx;

      // Update Navigation Buttons & Slide 20 Terminal Rule
      prevBtn.disabled = (idx === 0);
      
      if (currentSlideIdx === SLIDES_DATA.length - 1) {
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'inline-flex';
      } else {
        nextBtn.style.display = 'inline-flex';
        lastSlideNotice.style.display = 'none';
      }

      speechBubbleText.textContent = slide.narration || '';
      speakNarration(slide.narration || '');

      if (slide.is_quiz) {
        renderQuizSlide(slide);
      } else {
        slideContentGrid.style.display = 'grid';
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideTag.textContent = `${slide.section} ${slide.badge}`;
        slideTitle.textContent = slide.title;
        theoryBody.innerHTML = slide.theory || '';

        // Render Checkpoints
        renderCheckpoints(slide.checkpoints);

        // Render Simulator
        renderSimulator(slide.sim_id);

        if (window.triggerMathRender) triggerMathRender(document.getElementById('slideContentGrid') || document.body);
      }
    }
    window.renderSlide = renderSlide;

    // Navigation Event Listeners
    prevBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx > 0) renderSlide(currentSlideIdx - 1);
    });

    nextBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx < SLIDES_DATA.length - 1) renderSlide(currentSlideIdx + 1);
    });

    slideJumpSelect.addEventListener('change', (e) => {
      sfx.playClick();
      renderSlide(parseInt(e.target.value));
    });

    // Keyboard Arrow Navigation & Modal Esc Key
    window.addEventListener('keydown', (e) => {
      if (solutionModal && (solutionModal.classList.contains('is-active') || solutionModal.style.display !== 'none')) {
        if (e.key === 'Escape') {
          closeSolutionModal();
        }
        return;
      }
      if (e.key === 'ArrowRight' && currentSlideIdx < SLIDES_DATA.length - 1) {
        sfx.playClick();
        renderSlide(currentSlideIdx + 1);
      } else if (e.key === 'ArrowLeft' && currentSlideIdx > 0) {
        sfx.playClick();
        renderSlide(currentSlideIdx - 1);
      }
    });

""" + SIMULATORS_JS + r"""

    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(0);
    });
  </script>
</body>
</html>
"""

# Write HTML file
output_path = 'public/animations/class7-math-geometric-twins.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Compiled {output_path} successfully! Size: {os.path.getsize(output_path)} bytes")
'''

with open('.agents/build_class7_math_geometric_twins_lab.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Created .agents/build_class7_math_geometric_twins_lab.py")
