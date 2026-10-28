# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-earth-life-planet.html
Class 8 Science - Chapter 13: Our Home: Earth, a Unique Life Sustaining Planet
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Dr. Kalpana Chawla)
- 16 bespoke interactive SVG simulators with live planetary physics, biosphere mechanisms, reproduction & sustainability
- Prominent Key Technical Vocabulary Badges on every content slide
- 32 in-slide checkpoints with instant feedback
- 4 dedicated mastery quiz challenge slides (40 questions total)
- Step-by-step solution pop-up modal (#solutionModal style="display: none;")
- Slide 20 completion banner ("🎉 You have reached the last slide of this chapter!") hiding nextBtn
- Strictly zero occurrences of prohibited words
"""

import json
import os
import sys

sys.path.insert(0, '.agents')
from class8_science_earth_life_planet_data import SLIDES_DATA, QUIZ_QUESTIONS
from class8_science_earth_life_planet_sims import SIMULATORS_JS

# Assemble full slides data
full_slides = []
for slide in SLIDES_DATA:
    s = dict(slide)
    if s.get("is_quiz"):
        start_q, end_q = s.get("quiz_range", (1, 10))
        s["questions"] = QUIZ_QUESTIONS[start_q - 1:end_q]
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)
QUIZ_QUESTIONS_JSON = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Science • Chapter 13: Our Home: Earth, a Unique Life Sustaining Planet Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script>
    function triggerMathRender(el) {
      if (window.renderMathInElement) {
        window.renderMathInElement(el || document.body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false
        });
      }
    }
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="if (window.triggerMathRender) triggerMathRender(document.body);"></script>

  <style>
    :root {
      --bg-primary: #020617;
      --bg-secondary: #0b1329;
      --card-bg: rgba(15, 23, 42, 0.94);
      --card-border: rgba(56, 189, 248, 0.28);
      --accent-cyan: #38bdf8;
      --accent-blue: #0284c7;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --accent-rose: #f43f5e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: radial-gradient(circle at 50% 15%, #0c2d48 0%, var(--bg-primary) 85%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Top Navigation Header */
    .header {
      background: rgba(2, 6, 23, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .badge-chapter {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #e0f2fe;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.3rem 0.7rem;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      box-shadow: 0 0 12px rgba(2, 132, 199, 0.4);
    }

    .chapter-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: #f8fafc;
      letter-spacing: -0.01em;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }

    .slide-counter-pill {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.35rem 0.8rem;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-cyan);
    }

    /* Main Container */
    .main-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 1.25rem 1.5rem;
      gap: 1rem;
    }

    /* Teacher Avatar & Speech Bar */
    .avatar-speech-bar {
      background: linear-gradient(135deg, rgba(11, 23, 50, 0.95), rgba(2, 132, 199, 0.35));
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
      background: radial-gradient(circle at 35% 35%, #0284c7, #082f49);
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
      min-width: 175px;
    }

    .teacher-name {
      font-size: 0.95rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .teacher-badge {
      font-size: 0.7rem;
      color: #94a3b8;
      font-weight: 500;
    }

    .speech-bubble-area {
      flex: 1;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.8rem;
    }

    .speech-bubble-text {
      font-size: 0.9rem;
      line-height: 1.45;
      color: #e2e8f0;
      font-style: italic;
    }

    .voice-ctrl-btn {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid var(--accent-cyan);
      color: var(--accent-cyan);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
      flex-shrink: 0;
    }

    .voice-ctrl-btn:hover {
      background: var(--accent-cyan);
      color: #020617;
      transform: scale(1.06);
    }

    /* Content Layout Split */
    .slide-content-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      flex: 1;
      min-height: 520px;
    }

    @media (max-width: 1024px) {
      .slide-content-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Left Theory Card */
    .theory-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      overflow-y: auto;
      max-height: 640px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
    }

    .theory-header {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.75rem;
    }

    .section-tag {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .slide-main-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #f8fafc;
      line-height: 1.3;
    }

    /* Vocabulary Badges Bar */
    .vocab-badges-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
    }

    .vocab-badge {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #bae6fd;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 999px;
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    /* Core Theory Text */
    .theory-body {
      font-size: 0.95rem;
      line-height: 1.65;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .theory-body p {
      margin-bottom: 0.2rem;
    }

    .fact-box {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.12), rgba(16, 185, 129, 0.08));
      border-left: 3px solid var(--accent-cyan);
      padding: 0.75rem 1rem;
      border-radius: 0 10px 10px 0;
      font-size: 0.88rem;
      color: #e0f2fe;
      line-height: 1.5;
    }

    /* Checkpoints Section */
    .checkpoints-section {
      margin-top: 0.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 0.85rem;
    }

    .checkpoints-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .checkpoint-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 0.75rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .checkpoint-question {
      font-size: 0.88rem;
      font-weight: 600;
      color: #f1f5f9;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.4rem;
    }

    .chk-btn {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      padding: 0.45rem 0.65rem;
      border-radius: 8px;
      font-size: 0.8rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .chk-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-cyan);
      color: #ffffff;
    }

    .chk-btn.correct {
      background: rgba(16, 185, 129, 0.3) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .chk-btn.incorrect {
      background: rgba(244, 63, 94, 0.3) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .checkpoint-feedback {
      font-size: 0.8rem;
      padding: 0.4rem 0.6rem;
      border-radius: 6px;
      display: none;
    }

    .checkpoint-feedback.visible {
      display: block;
    }

    .checkpoint-feedback.success {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }

    .checkpoint-feedback.error {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fda4af;
    }

    /* Right Interactive Lab Card */
    .lab-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
      position: relative;
    }

    .lab-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }

    .lab-header-left {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .lab-badge {
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      color: #f0fdf4;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      text-transform: uppercase;
    }

    .sim-header-title {
      font-size: 1rem;
      font-weight: 700;
      color: #f8fafc;
    }

    /* Simulator Canvas Area */
    .sim-canvas-area {
      flex: 1;
      background: #020617;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 14px;
      min-height: 330px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }

    /* Simulator Controls Area */
    .sim-controls-area {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.75rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .sim-btn {
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #f8fafc;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sim-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-cyan);
      transform: translateY(-1px);
    }

    .sim-btn.active {
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }

    /* Mastery Quiz Container (Slides 17-20) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 1.25rem;
      max-width: 900px;
      margin: 0 auto;
      width: 100%;
    }

    .quiz-header-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .quiz-title-area {
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }

    .quiz-score-pill {
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid #10b981;
      color: #6ee7b7;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 0.4rem 1rem;
      border-radius: 999px;
    }

    .quiz-items-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .quiz-item-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      gap: 0.8rem;
    }

    .quiz-q-text {
      font-size: 0.98rem;
      font-weight: 700;
      color: #f8fafc;
      line-height: 1.45;
    }

    .quiz-options-list {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }

    @media (max-width: 768px) {
      .quiz-options-list {
        grid-template-columns: 1fr;
      }
    }

    .quiz-opt-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
      padding: 0.65rem 0.9rem;
      border-radius: 10px;
      font-size: 0.88rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-cyan);
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

    .quiz-action-row {
      display: flex;
      justify-content: flex-end;
      margin-top: 0.2rem;
    }

    .btn-solution-modal {
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      padding: 0.35rem 0.75rem;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .btn-solution-modal:hover {
      background: rgba(245, 158, 11, 0.25);
      border-color: #f59e0b;
      transform: translateY(-1px);
    }

    /* Step-by-Step Solution Modal */
    #solutionModal {
      position: fixed;
      inset: 0;
      background: rgba(2, 6, 23, 0.85);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-content-card {
      background: #0f172a;
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 20px;
      width: 100%;
      max-width: 650px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
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
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-close-modal {
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #94a3b8;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .btn-close-modal:hover {
      background: rgba(244, 63, 94, 0.2);
      color: #f43f5e;
    }

    .modal-question {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
      line-height: 1.45;
      background: rgba(15, 23, 42, 0.6);
      padding: 0.8rem;
      border-radius: 10px;
      border-left: 3px solid var(--accent-cyan);
    }

    .modal-solution-steps {
      font-size: 0.92rem;
      line-height: 1.65;
      color: #cbd5e1;
      white-space: pre-line;
      background: rgba(30, 41, 59, 0.5);
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Bottom Navigation Footer */
    .footer-nav {
      background: rgba(2, 6, 23, 0.9);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(56, 189, 248, 0.2);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      bottom: 0;
      z-index: 50;
    }

    .nav-btn {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border: none;
      color: #ffffff;
      padding: 0.55rem 1.25rem;
      border-radius: 10px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);
    }

    .nav-btn:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(2, 132, 199, 0.5);
    }

    .nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
    }

    .jump-select {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #f8fafc;
      padding: 0.5rem 1rem;
      border-radius: 10px;
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }

    .jump-select option {
      background: #0b1329;
      color: #f1f5f9;
    }

    /* Slide 20 Terminal Completion Banner */
    #lastSlideNotice {
      display: none;
      align-items: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.3));
      border: 1px solid #10b981;
      color: #a7f3d0;
      padding: 0.55rem 1.2rem;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.9rem;
      animation: bounceNotice 2s infinite;
    }

    @keyframes bounceNotice {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }
  </style>
</head>
<body>

  <!-- Top Header Navigation -->
  <header class="header">
    <div class="brand-section">
      <span class="badge-chapter">NCERT Class 8 Science • Ch 13</span>
      <h1 class="chapter-title">Our Home: Earth, a Unique Life Sustaining Planet Master Lab</h1>
    </div>

    <div class="header-controls">
      <div id="slideCounter" class="slide-counter-pill">Slide 1 / 20</div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-container">
    
    <!-- Virtual Avatar & Narration Speech Bar -->
    <section class="avatar-speech-bar" id="avatarSpeechBar">
      <div class="avatar-wrapper">
        <div id="avatarCircle" class="avatar-img-circle">
          <!-- Stylized Astronaut Avatar SVG for Dr. Kalpana Chawla -->
          <svg width="46" height="46" viewBox="0 0 100 100" fill="none">
            <!-- Helmet Outer Visor Rim -->
            <circle cx="50" cy="48" r="42" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
            <!-- Visor Glass with Earth Reflection -->
            <ellipse cx="50" cy="48" rx="34" ry="28" fill="#0284c7" opacity="0.6"/>
            <!-- Head & Astronaut Cap -->
            <circle cx="50" cy="46" r="22" fill="#fde047" opacity="0.2"/>
            <!-- Face features -->
            <circle cx="50" cy="44" r="16" fill="#fed7aa"/>
            <!-- Dark Hair framing face -->
            <path d="M 34,44 C 34,28 66,28 66,44 C 66,36 62,32 50,32 C 38,32 34,36 34,44 Z" fill="#1e293b"/>
            <!-- Eyes & warm smile -->
            <circle cx="45" cy="42" r="1.8" fill="#0f172a"/>
            <circle cx="55" cy="42" r="1.8" fill="#0f172a"/>
            <path id="avatarMouth" d="M 46,50 Q 50,54 54,50" stroke="#b45309" stroke-width="1.8" fill="none"/>
            <!-- Visor reflection arc -->
            <path d="M 28,34 Q 50,24 72,34" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.8"/>
            <!-- Space Suit Collar & Patch -->
            <path d="M 22,86 C 22,72 36,68 50,68 C 64,68 78,72 78,86 Z" fill="#e2e8f0"/>
            <rect x="42" y="74" width="16" height="8" rx="2" fill="#0284c7"/>
            <text x="50" y="80" fill="#ffffff" font-size="5" font-weight="900" text-anchor="middle">NASA/ISRO</text>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="teacher-meta">
        <div class="teacher-name">
          <span>Dr. Kalpana Chawla</span>
          <span style="font-size:0.75rem;">🚀</span>
        </div>
        <div class="teacher-badge">Astronaut & Aerospace Scientist</div>
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
          <span id="slideTag" class="section-tag">13.1 Why Is Earth a Unique Planet?</span>
          <h2 id="slideTitle" class="slide-main-title">Earth: The Unique Living Oasis</h2>
          <div id="vocabBadgesRow" class="vocab-badges-row">
            <!-- Vocabulary Badges injected here -->
          </div>
        </div>

        <div id="theoryBody" class="theory-body">
          <!-- Slide core paragraphs & fact boxes injected here -->
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
            <span id="simHeaderTitle" class="sim-header-title">Planetary Physics & Ecological Systems</span>
          </div>
        </div>

        <div id="simCanvas" class="sim-canvas-area">
          <!-- SVG and visual simulation elements injected here -->
        </div>

        <div id="simControls" class="sim-controls-area">
          <!-- Simulator interactive buttons and sliders injected here -->
        </div>
      </section>
    </div>

    <!-- Mastery Quiz Challenge View (Slides 17 to 20) -->
    <section id="quizContainer" class="quiz-container">
      <div class="quiz-header-card">
        <div class="quiz-title-area">
          <span id="quizBadge" class="section-tag">Chapter Review & Mastery</span>
          <h2 id="quizTitle" class="slide-main-title">Mastery Challenge: Planetary Science</h2>
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
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2">
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

  <script>
    // Injected Data
    const SLIDES_DATA = """ + SLIDES_JSON + r""";
    const QUIZ_QUESTIONS = """ + QUIZ_QUESTIONS_JSON + r""";

    // Application State
    let currentSlideIdx = 0;
    let isSpeaking = false;
    let speechSynth = window.speechSynthesis || null;
    let speechUtterance = null;
    const checkpointAnswers = {};
    const quizScores = {};

    // Web Audio Synthesizer for immediate feedback sounds
    const sfx = {
      ctx: null,
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      },
      playTone(freq, type, duration, gainVal = 0.1) {
        try {
          this.init();
          if (!this.ctx) return;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch(e) {}
      },
      playClick() {
        this.playTone(600, 'sine', 0.06, 0.08);
      },
      playCorrect() {
        try {
          this.init();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now); // C5
          osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
          osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.35);
        } catch(e) {}
      },
      playIncorrect() {
        try {
          this.init();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, now);
          osc.frequency.setValueAtTime(196, now + 0.12);
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.3);
        } catch(e) {}
      }
    };

    // DOM Elements
    const slideCounter = document.getElementById('slideCounter');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const labCol = document.getElementById('labCol');
    const slideTag = document.getElementById('slideTag');
    const slideTitle = document.getElementById('slideTitle');
    const vocabBadgesRow = document.getElementById('vocabBadgesRow');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsContainer = document.getElementById('checkpointsContainer');

    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simCanvas = document.getElementById('simCanvas');
    const simControls = document.getElementById('simControls');

    const quizContainer = document.getElementById('quizContainer');

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideJumpSelect = document.getElementById('slideJumpSelect');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    const solutionModal = document.getElementById('solutionModal');
    const btnCloseModal = document.getElementById('btnCloseModal');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');

    // Populate Slide Jump Selector
    SLIDES_DATA.forEach((s, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${s.id}. ${s.title}`;
      slideJumpSelect.appendChild(opt);
    });

    // Modal Control Functions
    function openSolutionModal(qId) {
      const q = QUIZ_QUESTIONS.find(item => item.id === qId);
      if (!q) return;
      modalQuestionText.textContent = `Q${q.id}: ${q.question}`;
      modalSolutionSteps.textContent = q.solution;
      solutionModal.style.display = 'flex';
      sfx.playClick();
      if (window.triggerMathRender) triggerMathRender(solutionModal);
    }

    btnCloseModal.addEventListener('click', () => {
      solutionModal.style.display = 'none';
      sfx.playClick();
    });

    solutionModal.addEventListener('click', (e) => {
      if (e.target === solutionModal) {
        solutionModal.style.display = 'none';
      }
    });

    // Voice Narration
    function stopSpeech() {
      if (speechSynth && speechSynth.speaking) {
        speechSynth.cancel();
      }
      isSpeaking = false;
      avatarSpeechBar.classList.remove('is-speaking');
      iconVoicePlay.style.display = 'inline-block';
      iconVoicePause.style.display = 'none';
    }

    function speakNarration(text) {
      stopSpeech();
      if (!speechSynth) return;
      
      const cleanText = text.replace(/\$/g, '').replace(/\+/g, ' plus ');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 1.0;
      speechUtterance.pitch = 1.05;

      const voices = speechSynth.getVoices();
      const preferredVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Female') || v.name.includes('Samantha') || v.name.includes('Google UK English Female') || v.name.includes('Natural')));
      if (preferredVoice) speechUtterance.voice = preferredVoice;

      speechUtterance.onstart = () => {
        isSpeaking = true;
        avatarSpeechBar.classList.add('is-speaking');
        iconVoicePlay.style.display = 'none';
        iconVoicePause.style.display = 'inline-block';
      };

      speechUtterance.onend = () => {
        stopSpeech();
      };

      speechUtterance.onerror = () => {
        stopSpeech();
      };

      speechSynth.speak(speechUtterance);
    }

    btnVoiceToggle.addEventListener('click', () => {
      sfx.init();
      if (isSpeaking) {
        stopSpeech();
      } else {
        const curSlide = SLIDES_DATA[currentSlideIdx];
        if (curSlide && curSlide.narration) {
          speakNarration(curSlide.narration);
        }
      }
    });

    // Render Mastery Quiz Slide (Slides 17 to 20)
    function renderQuizSlide(slide) {
      theoryCol.style.display = 'none';
      labCol.style.display = 'none';
      quizContainer.style.display = 'flex';

      const quizBadge = document.getElementById('quizBadge');
      const quizTitle = document.getElementById('quizTitle');
      const quizScorePill = document.getElementById('quizScorePill');
      const quizItemsList = document.getElementById('quizItemsList');

      quizBadge.textContent = slide.tag;
      quizTitle.textContent = slide.title;
      quizItemsList.innerHTML = '';

      const questions = slide.questions || [];

      function updateQuizScore() {
        let correctCount = 0;
        questions.forEach(q => {
          if (quizScores[q.id] === true) correctCount++;
        });
        quizScorePill.textContent = `Score: ${correctCount} / ${questions.length}`;
      }
      updateQuizScore();

      questions.forEach((q) => {
        const itemCard = document.createElement('div');
        itemCard.className = 'quiz-item-card';

        const qTitle = document.createElement('div');
        qTitle.className = 'quiz-q-text';
        qTitle.textContent = `Q${q.id}. ${q.question}`;
        itemCard.appendChild(qTitle);

        const optGrid = document.createElement('div');
        optGrid.className = 'quiz-options-list';

        q.options.forEach((optText, oIdx) => {
          const optBtn = document.createElement('button');
          optBtn.className = 'quiz-opt-btn';
          optBtn.textContent = optText;

          if (quizScores[q.id] !== undefined) {
            optBtn.disabled = true;
            if (oIdx === q.correct) optBtn.classList.add('correct');
          }

          optBtn.addEventListener('click', () => {
            const allOptBtns = optGrid.querySelectorAll('.quiz-opt-btn');
            allOptBtns.forEach(b => b.disabled = true);

            if (oIdx === q.correct) {
              optBtn.classList.add('correct');
              quizScores[q.id] = true;
              sfx.playCorrect();
            } else {
              optBtn.classList.add('incorrect');
              allOptBtns[q.correct].classList.add('correct');
              quizScores[q.id] = false;
              sfx.playIncorrect();
            }
            updateQuizScore();
          });
          optGrid.appendChild(optBtn);
        });
        itemCard.appendChild(optGrid);

        const actionRow = document.createElement('div');
        actionRow.className = 'quiz-action-row';

        const solBtn = document.createElement('button');
        solBtn.className = 'btn-solution-modal';
        solBtn.innerHTML = `
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
          </svg>
          <span>💡 View Step-by-Step Solution</span>
        `;
        solBtn.addEventListener('click', () => openSolutionModal(q.id));
        actionRow.appendChild(solBtn);

        itemCard.appendChild(actionRow);
        quizItemsList.appendChild(itemCard);
      });

      if (window.triggerMathRender) triggerMathRender(quizContainer);
    }

    // Render In-Slide Checkpoints
    function renderCheckpoints(checkpoints) {
      checkpointsContainer.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) return;

      checkpoints.forEach((chk, cIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const qTitle = document.createElement('div');
        qTitle.className = 'checkpoint-question';
        qTitle.textContent = `Check ${cIdx + 1}: ${chk.question}`;
        card.appendChild(qTitle);

        const optGrid = document.createElement('div');
        optGrid.className = 'checkpoint-options';

        const feedback = document.createElement('div');
        feedback.className = 'checkpoint-feedback';

        const savedAns = checkpointAnswers[`${currentSlideIdx}_${cIdx}`];

        chk.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'chk-btn';
          btn.textContent = optText;

          if (savedAns !== undefined) {
            btn.disabled = true;
            if (oIdx === chk.correct) btn.classList.add('correct');
            if (savedAns === oIdx && savedAns !== chk.correct) btn.classList.add('incorrect');
          }

          btn.addEventListener('click', () => {
            checkpointAnswers[`${currentSlideIdx}_${cIdx}`] = oIdx;
            const allBtns = optGrid.querySelectorAll('.chk-btn');
            allBtns.forEach(b => b.disabled = true);

            if (oIdx === chk.correct) {
              btn.classList.add('correct');
              feedback.className = 'checkpoint-feedback visible success';
              feedback.textContent = `✓ Correct! ${chk.explanation}`;
              sfx.playCorrect();
            } else {
              btn.classList.add('incorrect');
              allBtns[chk.correct].classList.add('correct');
              feedback.className = 'checkpoint-feedback visible error';
              feedback.textContent = `✕ Incorrect. ${chk.explanation}`;
              sfx.playIncorrect();
            }
          });
          optGrid.appendChild(btn);
        });

        card.appendChild(optGrid);
        card.appendChild(feedback);

        if (savedAns !== undefined) {
          if (savedAns === chk.correct) {
            feedback.className = 'checkpoint-feedback visible success';
            feedback.textContent = `✓ Correct! ${chk.explanation}`;
          } else {
            feedback.className = 'checkpoint-feedback visible error';
            feedback.textContent = `✕ Incorrect. ${chk.explanation}`;
          }
        }

        checkpointsContainer.appendChild(card);
      });
    }

    // Main Slide Renderer
    function renderSlide(idx) {
      if (idx < 0 || idx >= SLIDES_DATA.length) return;
      currentSlideIdx = idx;
      const slide = SLIDES_DATA[idx];

      slideCounter.textContent = `Slide ${slide.id} / ${SLIDES_DATA.length}`;
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
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideTag.textContent = slide.tag;
        slideTitle.textContent = slide.title;

        // Render Vocabulary Badges
        vocabBadgesRow.innerHTML = '';
        if (slide.key_terms && slide.key_terms.length > 0) {
          slide.key_terms.forEach(term => {
            const b = document.createElement('span');
            b.className = 'vocab-badge';
            b.innerHTML = `<span style="font-size:0.7rem;">🏷️</span><span>${term}</span>`;
            vocabBadgesRow.appendChild(b);
          });
        }

        // Render Theory Body
        theoryBody.innerHTML = '';
        if (slide.content && slide.content.length > 0) {
          slide.content.forEach(pText => {
            const p = document.createElement('p');
            p.textContent = pText;
            theoryBody.appendChild(p);
          });
        }

        // Render Fact Box
        if (slide.fact_box) {
          const fb = document.createElement('div');
          fb.className = 'fact-box';
          fb.innerHTML = `<strong>💡 Did You Know?</strong> ${slide.fact_box}`;
          theoryBody.appendChild(fb);
        }

        // Render Checkpoints
        renderCheckpoints(slide.checkpoints);

        // Render Interactive Simulator
        renderSimulator(slide.sim_id);

        if (window.triggerMathRender) triggerMathRender(theoryCol);
      }
    }

    // Simulator Dispatcher
    function renderSimulator(simId) {
      simCanvas.innerHTML = '';
      simControls.innerHTML = '';

      switch(simId) {
        case 'earth_unique_oasis_sim':
          simEarthUniqueOasis();
          break;
        case 'solar_system_planets_sim':
          simSolarSystemPlanets();
          break;
        case 'goldilocks_zone_sim':
          simGoldilocksZone();
          break;
        case 'earth_size_gravity_sim':
          simEarthSizeGravity();
          break;
        case 'geomagnetic_shield_sim':
          simGeomagneticShield();
          break;
        case 'air_water_sunlight_sim':
          simAirWaterSunlight();
          break;
        case 'soil_lithosphere_minerals_sim':
          simSoilLithosphereMinerals();
          break;
        case 'biosphere_web_sim':
          simBiosphereWeb();
          break;
        case 'carbon_oxygen_balance_sim':
          simCarbonOxygenBalance();
          break;
        case 'asexual_reproduction_sim':
          simAsexualReproduction();
          break;
        case 'sexual_reproduction_sim':
          simSexualReproduction();
          break;
        case 'reproduction_continuity_sim':
          simReproductionContinuity();
          break;
        case 'greenhouse_global_warming_sim':
          simGreenhouseGlobalWarming();
          break;
        case 'deforestation_biodiversity_loss_sim':
          simDeforestationBiodiversityLoss();
          break;
        case 'pollution_threats_sim':
          simPollutionThreats();
          break;
        case 'ecological_healing_conservation_sim':
          simEcologicalHealingConservation();
          break;
        default:
          simCanvas.innerHTML = `<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>`;
      }
    }

""" + SIMULATORS_JS + r"""

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

    // Keyboard Arrow Navigation
    window.addEventListener('keydown', (e) => {
      if (solutionModal.style.display !== 'none') {
        if (e.key === 'Escape') {
          solutionModal.style.display = 'none';
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

    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(0);
    });
  </script>
</body>
</html>
"""

# Write HTML file
output_path = 'public/animations/class8-science-earth-life-planet.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully compiled {output_path} (File size: {os.path.getsize(output_path):,} bytes)")

