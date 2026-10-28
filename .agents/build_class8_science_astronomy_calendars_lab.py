# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-astronomy-calendars.html
Class 8 Science - Chapter 11: Astronomy and Calendars
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Prof. Meghnad Saha)
- 16 bespoke interactive SVG simulators with live controls, orbital mechanics, and rich animations
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
from class8_science_astronomy_calendars_data import SLIDES_DATA, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 11: Astronomy and Calendars Master Lab</title>
  
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
      --bg-primary: #050814;
      --bg-secondary: #0a1128;
      --card-bg: rgba(10, 17, 40, 0.92);
      --card-border: rgba(96, 165, 250, 0.28);
      --accent-sky: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-indigo: #818cf8;
      --accent-rose: #f43f5e;
      --accent-emerald: #10b981;
      --accent-purple: #c084fc;
      --accent-yellow: #fde047;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: radial-gradient(circle at 50% 20%, #0d1b3e 0%, var(--bg-primary) 85%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Top Navigation Header */
    .header {
      background: rgba(5, 8, 20, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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
      background: linear-gradient(135deg, #1e3a8a, #3b82f6);
      color: #eff6ff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border: 1px solid rgba(96, 165, 250, 0.4);
    }

    .chapter-title {
      font-size: 1.05rem;
      font-weight: 700;
      background: linear-gradient(to right, #93c5fd, #60a5fa, #38bdf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .slide-progress-container {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .progress-bar-wrap {
      width: 140px;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #3b82f6, #38bdf8);
      width: 5%;
      transition: width 0.3s ease;
    }

    .slide-counter {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent-sky);
      min-width: 90px;
      text-align: right;
    }

    /* Main Workspace Layout */
    .main-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      max-width: 1540px;
      width: 100%;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      gap: 1rem;
    }

    /* Teacher Avatar & Speech Bar */
    .avatar-speech-bar {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 58, 138, 0.35));
      border: 1px solid rgba(96, 165, 250, 0.35);
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
      background: radial-gradient(circle at 35% 35%, #2563eb, #0f172a);
      border: 2px solid var(--accent-sky);
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

    .speech-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .teacher-name-tag {
      font-size: 0.8rem;
      font-weight: 700;
      color: #93c5fd;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .speech-bubble-text {
      font-size: 0.95rem;
      line-height: 1.45;
      color: #f1f5f9;
    }

    .audio-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-audio {
      background: rgba(30, 58, 138, 0.6);
      border: 1px solid rgba(96, 165, 250, 0.4);
      color: #93c5fd;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-audio:hover {
      background: rgba(59, 130, 246, 0.8);
      color: #ffffff;
      transform: scale(1.05);
    }

    /* Slide Grid Layout */
    .slide-viewport {
      flex: 1;
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 1.25rem;
      min-height: 580px;
    }

    @media (max-width: 1024px) {
      .slide-viewport {
        grid-template-columns: 1fr;
      }
    }

    /* Left Card: Theory & In-Slide Checkpoints */
    .theory-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      overflow-y: auto;
      max-height: calc(100vh - 240px);
    }

    .slide-badge {
      font-size: 0.75rem;
      font-weight: 700;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .slide-heading {
      font-size: 1.45rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
    }

    .concept-points-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .concept-point-item {
      background: rgba(15, 23, 42, 0.6);
      border-left: 3px solid #3b82f6;
      border-radius: 0 8px 8px 0;
      padding: 0.7rem 0.9rem;
    }

    .concept-point-title {
      font-weight: 700;
      color: #bfdbfe;
      font-size: 0.9rem;
      margin-bottom: 0.2rem;
    }

    .concept-point-desc {
      font-size: 0.85rem;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .fact-box {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(217, 119, 6, 0.05));
      border: 1px dashed rgba(245, 158, 11, 0.4);
      border-radius: 10px;
      padding: 0.75rem 1rem;
      display: flex;
      gap: 0.75rem;
      align-items: flex-start;
      font-size: 0.85rem;
      color: #fde68a;
      line-height: 1.4;
    }

    .checkpoints-section {
      margin-top: 0.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 1rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .checkpoints-title {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      color: #93c5fd;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .checkpoint-box {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(96, 165, 250, 0.2);
      border-radius: 12px;
      padding: 0.9rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .checkpoint-question {
      font-size: 0.88rem;
      font-weight: 600;
      color: #f1f5f9;
      line-height: 1.35;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.45rem;
    }

    .chk-option-btn {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      padding: 0.5rem 0.75rem;
      border-radius: 8px;
      font-size: 0.82rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .chk-option-btn:hover:not(:disabled) {
      background: rgba(59, 130, 246, 0.25);
      border-color: rgba(96, 165, 250, 0.4);
      color: #ffffff;
    }

    .chk-option-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .chk-option-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .chk-feedback {
      font-size: 0.8rem;
      line-height: 1.35;
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      display: none;
    }

    .chk-feedback.show-correct {
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }

    .chk-feedback.show-incorrect {
      display: block;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fda4af;
    }

    /* Right Card: Interactive Laboratory Simulator */
    .lab-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      position: relative;
      overflow: hidden;
    }

    .sim-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.6rem;
    }

    .sim-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #93c5fd;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .sim-canvas-container {
      flex: 1;
      min-height: 340px;
      background: radial-gradient(circle at 50% 50%, #0d1733 0%, #050917 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }

    .sim-controls {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      background: rgba(15, 23, 42, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 1rem;
    }

    .control-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      font-size: 0.85rem;
      flex-wrap: wrap;
    }

    .control-label {
      color: #94a3b8;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .control-value {
      color: #38bdf8;
      font-weight: 700;
    }

    .sim-slider {
      flex: 1;
      height: 6px;
      -webkit-appearance: none;
      appearance: none;
      background: rgba(255, 255, 255, 0.15);
      border-radius: 999px;
      outline: none;
    }

    .sim-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #38bdf8;
      cursor: pointer;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
      transition: transform 0.1s;
    }

    .sim-slider::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    .sim-btn-group {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .sim-toggle-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sim-toggle-btn:hover {
      background: rgba(59, 130, 246, 0.3);
      border-color: rgba(96, 165, 250, 0.5);
    }

    .sim-toggle-btn.active {
      background: linear-gradient(135deg, #1d4ed8, #2563eb);
      border-color: #60a5fa;
      color: #ffffff;
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.4);
    }

    /* Mastery Quiz Layout (Slides 17 to 20) */
    .quiz-container {
      grid-column: 1 / -1;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      max-height: calc(100vh - 220px);
      overflow-y: auto;
    }

    .quiz-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.8rem;
    }

    .quiz-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #ffffff;
    }

    .quiz-score-pill {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #34d399;
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.85rem;
    }

    .quiz-items-grid {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .quiz-item-card {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 1.15rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .quiz-q-text {
      font-size: 0.95rem;
      font-weight: 600;
      color: #f8fafc;
      line-height: 1.4;
    }

    .quiz-options-list {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
    }

    @media (max-width: 768px) {
      .quiz-options-list {
        grid-template-columns: 1fr;
      }
    }

    .quiz-opt-btn {
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      padding: 0.65rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(59, 130, 246, 0.25);
      border-color: rgba(96, 165, 250, 0.4);
      color: #ffffff;
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fecdd3 !important;
    }

    .quiz-action-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 0.4rem;
    }

    .btn-solution-modal {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .btn-solution-modal:hover {
      background: rgba(245, 158, 11, 0.3);
      color: #fef08a;
    }

    /* Modal for Step-by-Step Solutions */
    #solutionModal {
      position: fixed;
      inset: 0;
      background: rgba(5, 8, 20, 0.8);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-content-card {
      background: #0d1733;
      border: 1px solid #3b82f6;
      border-radius: 16px;
      max-width: 650px;
      width: 100%;
      padding: 1.5rem;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
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
      font-size: 1.1rem;
      font-weight: 700;
      color: #93c5fd;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-close-modal {
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #94a3b8;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      transition: all 0.2s;
    }

    .btn-close-modal:hover {
      background: rgba(244, 63, 94, 0.2);
      color: #f43f5e;
    }

    .modal-question {
      font-size: 0.95rem;
      font-weight: 600;
      color: #f8fafc;
      background: rgba(15, 23, 42, 0.6);
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }

    .modal-solution-steps {
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.55;
      white-space: pre-line;
      background: rgba(15, 23, 42, 0.4);
      padding: 1rem;
      border-radius: 8px;
      border-left: 3px solid #38bdf8;
    }

    /* Bottom Navigation Bar */
    .bottom-nav {
      background: rgba(5, 8, 20, 0.85);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      bottom: 0;
      z-index: 50;
    }

    .nav-btn {
      background: linear-gradient(135deg, #1e3a8a, #2563eb);
      border: 1px solid rgba(96, 165, 250, 0.4);
      color: #ffffff;
      font-size: 0.9rem;
      font-weight: 700;
      padding: 0.55rem 1.25rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
    }

    .nav-btn:hover:not(:disabled) {
      background: linear-gradient(135deg, #2563eb, #3b82f6);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    .nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }

    .jump-selector {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #93c5fd;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }

    .jump-selector option {
      background: #0f172a;
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
      <span class="badge-chapter">NCERT Class 8 Science • Ch 11</span>
      <h1 class="chapter-title">Astronomy and Calendars Master Lab</h1>
    </div>

    <div class="slide-progress-container">
      <div class="progress-bar-wrap">
        <div id="progressBarFill" class="progress-bar-fill"></div>
      </div>
      <span id="slideCounterText" class="slide-counter">Slide 1 of 20</span>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-container">
    
    <!-- Virtual Teacher Avatar & Speech Bar -->
    <section id="avatarSpeechBar" class="avatar-speech-bar">
      <div class="avatar-wrapper">
        <div id="avatarCircle" class="avatar-img-circle">
          <!-- Stylized Astrophysicist Avatar SVG -->
          <svg width="44" height="44" viewBox="0 0 100 100" fill="none">
            <!-- Background circle aura -->
            <circle cx="50" cy="50" r="45" fill="#1e3a8a"/>
            <!-- Head & hair -->
            <circle cx="50" cy="42" r="20" fill="#fbcfe8"/>
            <path d="M30 38 C30 20 70 20 70 38 C70 30 65 24 50 24 C35 24 30 30 30 38 Z" fill="#64748b"/>
            <!-- Glasses -->
            <rect x="37" y="38" width="10" height="7" rx="2" stroke="#38bdf8" stroke-width="2" fill="none"/>
            <rect x="53" y="38" width="10" height="7" rx="2" stroke="#38bdf8" stroke-width="2" fill="none"/>
            <line x1="47" y1="41" x2="53" y2="41" stroke="#38bdf8" stroke-width="2"/>
            <!-- Gentle smile / speaking mouth -->
            <path id="avatarMouth" d="M45 52 Q50 56 55 52" stroke="#be185d" stroke-width="2" fill="none"/>
            <!-- Shoulders / Academic Coat -->
            <path d="M22 84 C22 66 36 62 50 62 C64 62 78 66 78 84 Z" fill="#1e293b"/>
            <path d="M42 62 L50 78 L58 62 Z" fill="#38bdf8"/>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="speech-content">
        <div class="teacher-name-tag">
          <span>Prof. Meghnad Saha</span>
          <span style="font-size: 0.72rem; color: #60a5fa; font-weight: 500;">• Calendar Reform Chairman & Astrophysicist</span>
        </div>
        <p id="speechBubbleText" class="speech-bubble-text">
          Loading astronomy lesson...
        </p>
      </div>

      <div class="audio-controls">
        <button id="btnVoiceToggle" class="btn-audio" title="Play / Pause Voice Narration">
          <svg id="iconVoicePlay" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="5 3 19 12 5 21 5 3"/>
          </svg>
          <svg id="iconVoicePause" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;">
            <rect x="6" y="4" width="4" height="16"/>
            <rect x="14" y="4" width="4" height="16"/>
          </svg>
        </button>
      </div>
    </section>

    <!-- Slide Viewport (Two Columns for content, Full Width for Quiz) -->
    <div id="slideViewport" class="slide-viewport">
      <!-- Left: Theory & Checkpoints -->
      <div id="theoryCol" class="theory-card">
        <div>
          <span id="slideTag" class="slide-badge">11.1 The Moon's Appearance</span>
          <h2 id="slideTitle" class="slide-heading">Moon's Illuminated Hemisphere & Reflection</h2>
        </div>

        <div id="conceptPointsList" class="concept-points-list">
          <!-- Dynamic concept points -->
        </div>

        <div id="factBox" class="fact-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;">
            <circle cx="12" cy="12" r="10"/>
            <line x1="12" y1="16" x2="12" y2="12"/>
            <line x1="12" y1="8" x2="12.01" y2="8"/>
          </svg>
          <span id="factText">Moon reflection fact loading...</span>
        </div>

        <!-- 2 In-slide checkpoints -->
        <div id="checkpointsSection" class="checkpoints-section">
          <div class="checkpoints-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 11l3 3L22 4"/>
              <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
            </svg>
            <span>Interactive In-Slide Inquiries</span>
          </div>

          <!-- Checkpoint 1 -->
          <div id="chk1Box" class="checkpoint-box">
            <p id="chk1Question" class="checkpoint-question">Q1 Question loading...</p>
            <div id="chk1Options" class="checkpoint-options"></div>
            <div id="chk1Feedback" class="chk-feedback"></div>
          </div>

          <!-- Checkpoint 2 -->
          <div id="chk2Box" class="checkpoint-box">
            <p id="chk2Question" class="checkpoint-question">Q2 Question loading...</p>
            <div id="chk2Options" class="checkpoint-options"></div>
            <div id="chk2Feedback" class="chk-feedback"></div>
          </div>
        </div>
      </div>

      <!-- Right: Interactive Laboratory Simulator -->
      <div id="labCol" class="lab-card">
        <div class="sim-header">
          <div class="sim-title">
            <svg id="simIcon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <span id="simHeaderTitle">Celestial Mechanics Simulator</span>
          </div>
        </div>

        <div id="simCanvas" class="sim-canvas-container">
          <!-- Dynamic SVG Simulators Injected Here -->
        </div>

        <div id="simControls" class="sim-controls">
          <!-- Dynamic Controls Injected Here -->
        </div>
      </div>

      <!-- Mastery Quiz Container (Activated on Slides 17-20) -->
      <div id="quizContainer" class="quiz-container" style="display: none;">
        <div class="quiz-header">
          <div>
            <span id="quizBadge" class="slide-badge">Mastery Assessment</span>
            <h2 id="quizTitle" class="quiz-title">Mastery Challenge • Part I</h2>
          </div>
          <div id="quizScorePill" class="quiz-score-pill">Score: 0 / 10</div>
        </div>

        <div id="quizItemsList" class="quiz-items-grid">
          <!-- 10 Quiz Questions per Quiz Slide -->
        </div>
      </div>
    </div>
  </main>

  <!-- Step-by-Step Solution Modal (#solutionModal style="display: none;") -->
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
  <footer class="bottom-nav">
    <button id="prevBtn" class="nav-btn">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="15 18 9 12 15 6"/>
      </svg>
      <span>Previous</span>
    </button>

    <div style="display: flex; align-items: center; gap: 0.75rem;">
      <select id="slideJumpSelect" class="jump-selector" title="Jump directly to slide"></select>
      
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

  <!-- Sound Synthesis via Web Audio API -->
  <script>
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
      playCorrect() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1); // E5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2); // G5
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      }
      playIncorrect() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.linearRampToValueAtTime(160, now + 0.25);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        osc.start(now);
        osc.stop(now + 0.25);
      }
      playClick() {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, now);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.05);
      }
    }
    const sfx = new SoundFX();
  </script>

  <!-- Inject Dataset -->
  <script>
    const SLIDES = __SLIDES_JSON__;
    const QUIZ_QUESTIONS = __QUIZ_QUESTIONS_JSON__;
  </script>

  <!-- Main Controller Logic & 16 Simulators -->
  <script>
    let currentSlideIdx = 0;
    const totalSlides = SLIDES.length;
    let quizScores = {}; // Tracks scores per question id
    let isSpeaking = false;
    let speechSynth = window.speechSynthesis;
    let speechUtterance = null;

    // DOM Elements
    const progressBarFill = document.getElementById('progressBarFill');
    const slideCounterText = document.getElementById('slideCounterText');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const avatarCircle = document.getElementById('avatarCircle');
    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const theoryCol = document.getElementById('theoryCol');
    const labCol = document.getElementById('labCol');
    const quizContainer = document.getElementById('quizContainer');

    const slideTag = document.getElementById('slideTag');
    const slideTitle = document.getElementById('slideTitle');
    const conceptPointsList = document.getElementById('conceptPointsList');
    const factText = document.getElementById('factText');

    const chk1Question = document.getElementById('chk1Question');
    const chk1Options = document.getElementById('chk1Options');
    const chk1Feedback = document.getElementById('chk1Feedback');
    const chk2Question = document.getElementById('chk2Question');
    const chk2Options = document.getElementById('chk2Options');
    const chk2Feedback = document.getElementById('chk2Feedback');

    const simCanvas = document.getElementById('simCanvas');
    const simControls = document.getElementById('simControls');
    const simHeaderTitle = document.getElementById('simHeaderTitle');

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideJumpSelect = document.getElementById('slideJumpSelect');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    const solutionModal = document.getElementById('solutionModal');
    const btnCloseModal = document.getElementById('btnCloseModal');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');

    // Populate Jump Selector
    function initJumpSelector() {
      slideJumpSelect.innerHTML = '';
      SLIDES.forEach((s, idx) => {
        const opt = document.createElement('option');
        opt.value = idx;
        opt.textContent = `${idx + 1}. ${s.title}`;
        slideJumpSelect.appendChild(opt);
      });
      slideJumpSelect.addEventListener('change', (e) => {
        goToSlide(parseInt(e.target.value));
      });
    }

    // Modal Handlers
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
      
      // Clean math formatting for clean speech
      const cleanText = text.replace(/\$/g, '').replace(/\^\\circ/g, ' degrees');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 1.0;
      speechUtterance.pitch = 1.05;

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
      sfx.playClick();
      if (isSpeaking) {
        stopSpeech();
      } else {
        const slide = SLIDES[currentSlideIdx];
        if (slide && slide.narration) {
          speakNarration(slide.narration);
        }
      }
    });

    // Render In-Slide Checkpoint
    function renderCheckpoint(chkIndex, chkData, questionEl, optionsEl, feedbackEl) {
      questionEl.textContent = chkData.question;
      optionsEl.innerHTML = '';
      feedbackEl.className = 'chk-feedback';
      feedbackEl.style.display = 'none';

      chkData.options.forEach((optText, optIdx) => {
        const btn = document.createElement('button');
        btn.className = 'chk-option-btn';
        btn.textContent = optText;
        btn.addEventListener('click', () => {
          // Disable options in this checkpoint
          const allBtns = optionsEl.querySelectorAll('.chk-option-btn');
          allBtns.forEach(b => b.disabled = true);

          if (optIdx === chkData.correct) {
            btn.classList.add('correct');
            feedbackEl.textContent = `✓ Correct! ${chkData.explanation}`;
            feedbackEl.className = 'chk-feedback show-correct';
            sfx.playCorrect();
          } else {
            btn.classList.add('incorrect');
            allBtns[chkData.correct].classList.add('correct');
            feedbackEl.textContent = `✗ Not quite. ${chkData.explanation}`;
            feedbackEl.className = 'chk-feedback show-incorrect';
            sfx.playIncorrect();
          }
        });
        optionsEl.appendChild(btn);
      });
    }

    // Render Mastery Quiz Slide
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
      let currentSectionAnswered = 0;
      let currentSectionCorrect = 0;

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

        // Action row: Solution button
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

    // Go To Slide
    function goToSlide(slideIdx) {
      if (slideIdx < 0 || slideIdx >= totalSlides) return;
      currentSlideIdx = slideIdx;
      const slide = SLIDES[currentSlideIdx];

      // Update Header Progress
      const progressPercent = ((currentSlideIdx + 1) / totalSlides) * 100;
      progressBarFill.style.width = `${progressPercent}%`;
      slideCounterText.textContent = `Slide ${currentSlideIdx + 1} of ${totalSlides}`;
      slideJumpSelect.value = currentSlideIdx;

      // Update Prev / Next buttons
      prevBtn.disabled = (currentSlideIdx === 0);

      // Slide 20 Terminal Rule: Hide Next Button, Show Notice
      if (currentSlideIdx === totalSlides - 1) {
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'inline-flex';
      } else {
        nextBtn.style.display = 'inline-flex';
        lastSlideNotice.style.display = 'none';
      }

      // Update Narration Speech Bubble
      speechBubbleText.textContent = slide.narration || '';
      speakNarration(slide.narration || '');

      // Check if it's a Quiz Slide (Slides 17 to 20)
      if (slide.is_quiz) {
        renderQuizSlide(slide);
      } else {
        // Standard Content Slide (Slides 1 to 16)
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideTag.textContent = slide.tag;
        slideTitle.textContent = slide.title;

        // Render concept points
        conceptPointsList.innerHTML = '';
        (slide.points || []).forEach(([pTitle, pDesc]) => {
          const item = document.createElement('div');
          item.className = 'concept-point-item';
          item.innerHTML = `
            <div class="concept-point-title">${pTitle}</div>
            <div class="concept-point-desc">${pDesc}</div>
          `;
          conceptPointsList.appendChild(item);
        });

        // Fact text
        factText.textContent = slide.fact || '';

        // Render 2 checkpoints
        if (slide.checkpoints && slide.checkpoints.length >= 2) {
          renderCheckpoint(0, slide.checkpoints[0], chk1Question, chk1Options, chk1Feedback);
          renderCheckpoint(1, slide.checkpoints[1], chk2Question, chk2Options, chk2Feedback);
        }

        // Render bespoke interactive simulator
        renderSimulator(slide.sim_id);

        if (window.triggerMathRender) triggerMathRender(theoryCol);
      }
    }

    prevBtn.addEventListener('click', () => {
      sfx.playClick();
      goToSlide(currentSlideIdx - 1);
    });

    nextBtn.addEventListener('click', () => {
      sfx.playClick();
      goToSlide(currentSlideIdx + 1);
    });

    // ==========================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS
    // ==========================================
    function renderSimulator(simId) {
      simCanvas.innerHTML = '';
      simControls.innerHTML = '';

      switch(simId) {
        case 'moon_illumination_sim':
          simMoonIllumination();
          break;
        case 'eight_moon_phases_sim':
          simEightMoonPhases();
          break;
        case 'synodic_vs_sidereal_sim':
          simSynodicVsSidereal();
          break;
        case 'locating_moon_sky_sim':
          simLocatingMoonSky();
          break;
        case 'orbital_geometry_sim':
          simOrbitalGeometry();
          break;
        case 'synchronous_rotation_sim':
          simSynchronousRotation();
          break;
        case 'eclipses_geometry_sim':
          simEclipsesGeometry();
          break;
        case 'lunar_calendar_drift_sim':
          simLunarCalendarDrift();
          break;
        case 'solar_calendar_seasons_sim':
          simSolarCalendarSeasons();
          break;
        case 'lunisolar_adhik_maas_sim':
          simLunisolarAdhikMaas();
          break;
        case 'indian_national_calendar_sim':
          simIndianNationalCalendar();
          break;
        case 'festival_astronomy_sim':
          simFestivalAstronomy();
          break;
        case 'newton_orbital_cannon_sim':
          simNewtonOrbitalCannon();
          break;
        case 'satellite_orbits_navic_sim':
          simSatelliteOrbitsNavic();
          break;
        case 'remote_sensing_space_sim':
          simRemoteSensingSpace();
          break;
        case 'jantar_mantar_sundial_sim':
          simJantarMantarSundial();
          break;
        default:
          simCanvas.innerHTML = '<div style="color: #94a3b8; padding: 2rem;">Simulator loading...</div>';
      }
    }

    // 1. Moon Illumination Simulator (50% Constant Sunlit Hemisphere)
    function simMoonIllumination() {
      simHeaderTitle.textContent = "Moon's Constant 50% Sunlit Hemisphere Simulator";
      let orbitAngle = 45; // degrees

      simCanvas.innerHTML = `
        <svg id="moonIllumSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <defs>
            <linearGradient id="sunbeamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#fde047" stop-opacity="0.8"/>
              <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.1"/>
            </linearGradient>
            <radialGradient id="earthGrad" cx="40%" cy="40%" r="60%">
              <stop offset="0%" stop-color="#60a5fa"/>
              <stop offset="60%" stop-color="#1d4ed8"/>
              <stop offset="100%" stop-color="#0f172a"/>
            </radialGradient>
          </defs>

          <!-- Star background dots -->
          <circle cx="40" cy="50" r="1" fill="#ffffff" opacity="0.6"/>
          <circle cx="120" cy="280" r="1.5" fill="#ffffff" opacity="0.8"/>
          <circle cx="380" cy="40" r="1.2" fill="#ffffff" opacity="0.5"/>
          <circle cx="460" cy="270" r="1" fill="#ffffff" opacity="0.7"/>

          <!-- Incident Sunlight Rays from Left -->
          <path d="M 0 40 L 150 40 M 0 100 L 150 100 M 0 160 L 150 160 M 0 220 L 150 220 M 0 280 L 150 280" stroke="#fde047" stroke-width="2" stroke-dasharray="8 4" opacity="0.7"/>
          <text x="15" y="25" fill="#fde047" font-size="12" font-weight="700">☀️ PARALLEL SUNLIGHT RAYS</text>

          <!-- Orbital Track -->
          <circle cx="280" cy="160" r="100" fill="none" stroke="rgba(96, 165, 250, 0.25)" stroke-dasharray="4 4" stroke-width="1.5"/>

          <!-- Earth at Center -->
          <circle cx="280" cy="160" r="32" fill="url(#earthGrad)"/>
          <!-- Earth Day/Night Terminator -->
          <path d="M 280 128 A 32 32 0 0 1 280 192 Z" fill="#090d16" opacity="0.85"/>
          <text x="280" y="164" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">EARTH</text>

          <!-- Moon Group -->
          <g id="illumMoonGroup" transform="translate(350, 90)">
            <!-- Sunlit hemisphere (facing left toward sun) -->
            <path d="M 0 -18 A 18 18 0 0 0 0 18 Z" fill="#fef08a"/>
            <!-- Dark hemisphere (facing right) -->
            <path d="M 0 -18 A 18 18 0 0 1 0 18 Z" fill="#1e293b"/>
            <!-- Moon outline -->
            <circle cx="0" cy="0" r="18" fill="none" stroke="#fde047" stroke-width="1.5"/>
            <!-- Center marker -->
            <circle cx="0" cy="0" r="2" fill="#ef4444"/>
          </g>

          <!-- Inset: Earth Observer's View -->
          <rect x="360" y="210" width="125" height="95" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="422" y="228" fill="#93c5fd" font-size="10" font-weight="700" text-anchor="middle">EARTH VIEW</text>
          <circle cx="422" cy="260" r="20" fill="#1e293b"/>
          <path id="earthViewPhase" d="M 422 240 A 20 20 0 0 1 422 280 A 10 20 0 0 0 422 240" fill="#fde047"/>
          <text id="illumPhaseName" x="422" y="295" fill="#fde047" font-size="9.5" font-weight="700" text-anchor="middle">Waxing Crescent</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🌙 Moon Orbital Angle around Earth:</span>
          <span id="orbitAngleVal" class="control-value">${orbitAngle}°</span>
        </div>
        <input type="range" id="sliderOrbitAngle" class="sim-slider" min="0" max="360" value="${orbitAngle}">
        <div class="control-row" style="font-size: 0.82rem; color: #94a3b8;">
          <span>💡 Notice: The left hemisphere of the Moon is <strong>always 100% illuminated</strong> by the Sun! Our changing view is an optical perspective from Earth.</span>
        </div>
      `;

      const slider = document.getElementById('sliderOrbitAngle');
      const valLabel = document.getElementById('orbitAngleVal');
      const moonGroup = document.getElementById('illumMoonGroup');
      const earthViewPhase = document.getElementById('earthViewPhase');
      const phaseNameText = document.getElementById('illumPhaseName');

      function updateIllum(angle) {
        orbitAngle = angle;
        valLabel.textContent = `${angle}°`;
        const rad = (angle * Math.PI) / 180;
        const cx = 280 + 100 * Math.cos(rad);
        const cy = 160 + 100 * Math.sin(rad);
        moonGroup.setAttribute('transform', `translate(${cx}, ${cy})`);

        // Compute phase name
        let name = "New Moon";
        if (angle > 15 && angle < 75) name = "Waxing Crescent";
        else if (angle >= 75 && angle <= 105) name = "First Quarter";
        else if (angle > 105 && angle < 165) name = "Waxing Gibbous";
        else if (angle >= 165 && angle <= 195) name = "Full Moon";
        else if (angle > 195 && angle < 255) name = "Waning Gibbous";
        else if (angle >= 255 && angle <= 285) name = "Third Quarter";
        else if (angle > 285 && angle < 345) name = "Waning Crescent";

        phaseNameText.textContent = name;

        // Inset phase curve math
        const normAngle = angle % 360;
        const r = 20;
        if (normAngle <= 180) {
          // Waxing (lit on right in Northern Hemisphere)
          const rx = Math.abs(r * Math.cos(rad));
          const sweep = normAngle > 90 ? 1 : 0;
          earthViewPhase.setAttribute('d', `M 422 ${260 - r} A ${r} ${r} 0 0 1 422 ${260 + r} A ${rx} ${r} 0 0 ${sweep} 422 ${260 - r}`);
        } else {
          // Waning (lit on left)
          const rx = Math.abs(r * Math.cos(rad));
          const sweep = normAngle > 270 ? 0 : 1;
          earthViewPhase.setAttribute('d', `M 422 ${260 - r} A ${r} ${r} 0 0 0 422 ${260 + r} A ${rx} ${r} 0 0 ${sweep} 422 ${260 - r}`);
        }
      }

      slider.addEventListener('input', (e) => updateIllum(parseInt(e.target.value)));
      updateIllum(orbitAngle);
    }

    // 2. The Eight Classical Moon Phases Simulator
    function simEightMoonPhases() {
      simHeaderTitle.textContent = "Interactive Eight Classical Lunar Phases";
      let phaseIndex = 4; // Full Moon initially

      const phases = [
        { name: "1. New Moon (Amavasya)", illum: "0%", paksha: "Shukla Paksha begins", rise: "6:00 AM (Sunrise)", set: "6:00 PM (Sunset)", day: "Day 0" },
        { name: "2. Waxing Crescent", illum: "25%", paksha: "Shukla Paksha (Bright)", rise: "9:00 AM", set: "9:00 PM", day: "Day 3.7" },
        { name: "3. First Quarter", illum: "50%", paksha: "Shukla Paksha (Bright)", rise: "12:00 PM (Noon)", set: "12:00 AM (Midnight)", day: "Day 7.4" },
        { name: "4. Waxing Gibbous", illum: "75%", paksha: "Shukla Paksha (Bright)", rise: "3:00 PM", set: "3:00 AM", day: "Day 11.1" },
        { name: "5. Full Moon (Purnima)", illum: "100%", paksha: "Krishna Paksha begins", rise: "6:00 PM (Sunset)", set: "6:00 AM (Sunrise)", day: "Day 14.8" },
        { name: "6. Waning Gibbous", illum: "75%", paksha: "Krishna Paksha (Dark)", rise: "9:00 PM", set: "9:00 AM", day: "Day 18.5" },
        { name: "7. Third Quarter", illum: "50%", paksha: "Krishna Paksha (Dark)", rise: "12:00 AM (Midnight)", set: "12:00 PM (Noon)", day: "Day 22.1" },
        { name: "8. Waning Crescent", illum: "25%", paksha: "Krishna Paksha (Dark)", rise: "3:00 AM", set: "3:00 PM", day: "Day 25.8" }
      ];

      simCanvas.innerHTML = `
        <svg id="eightPhaseSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Moon Sphere -->
          <circle cx="250" cy="140" r="90" fill="#1e293b" stroke="rgba(255, 255, 255, 0.2)" stroke-width="2"/>
          
          <!-- Craters on base dark disk -->
          <circle cx="220" cy="110" r="14" fill="#0f172a" opacity="0.6"/>
          <circle cx="270" cy="160" r="22" fill="#0f172a" opacity="0.6"/>
          <circle cx="210" cy="170" r="10" fill="#0f172a" opacity="0.5"/>
          <circle cx="290" cy="100" r="12" fill="#0f172a" opacity="0.5"/>

          <!-- Dynamic Sunlit Mask/Path -->
          <path id="phaseSunlitPath" d="M 250 50 A 90 90 0 0 1 250 230 A 90 90 0 0 1 250 50" fill="#fef08a"/>

          <!-- Craters on lit area -->
          <g id="litCraters" opacity="0.35">
            <circle cx="220" cy="110" r="14" fill="#d97706"/>
            <circle cx="270" cy="160" r="22" fill="#d97706"/>
            <circle cx="210" cy="170" r="10" fill="#d97706"/>
            <circle cx="290" cy="100" r="12" fill="#d97706"/>
          </g>

          <!-- Outer glow ring -->
          <circle cx="250" cy="140" r="92" fill="none" stroke="#fde047" stroke-width="2" opacity="0.5"/>

          <!-- Phase Data Overlay -->
          <rect x="50" y="245" width="400" height="65" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(96, 165, 250, 0.3)"/>
          <text id="pNameText" x="250" y="268" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">Full Moon (Purnima)</text>
          <text id="pDetailsText" x="250" y="292" fill="#93c5fd" font-size="11.5" text-anchor="middle">Illumination: 100% • Shukla Paksha ends • Day 14.8</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn" data-p="0">New Moon</button>
          <button class="sim-toggle-btn" data-p="1">Waxing Crescent</button>
          <button class="sim-toggle-btn" data-p="2">1st Quarter</button>
          <button class="sim-toggle-btn" data-p="3">Waxing Gibbous</button>
          <button class="sim-toggle-btn active" data-p="4">Full Moon</button>
          <button class="sim-toggle-btn" data-p="5">Waning Gibbous</button>
          <button class="sim-toggle-btn" data-p="6">3rd Quarter</button>
          <button class="sim-toggle-btn" data-p="7">Waning Crescent</button>
        </div>
      `;

      const path = document.getElementById('phaseSunlitPath');
      const pName = document.getElementById('pNameText');
      const pDetails = document.getElementById('pDetailsText');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updatePhase(idx) {
        phaseIndex = idx;
        btns.forEach((b, i) => b.classList.toggle('active', i === idx));
        const p = phases[idx];
        pName.textContent = p.name;
        pDetails.textContent = `Illumination: ${p.illum} • ${p.paksha} • ${p.day} • Rises: ${p.rise}`;

        // SVG shape geometry
        const r = 90;
        const cy = 140;
        const cx = 250;
        if (idx === 0) { // New Moon (no light)
          path.setAttribute('d', 'M 250 50 Z');
        } else if (idx === 1) { // Waxing Crescent (crescent on right)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 1 ${cx} ${cy + r} A ${r * 0.5} ${r} 0 0 0 ${cx} ${cy - r}`);
        } else if (idx === 2) { // 1st Quarter (right half lit)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 1 ${cx} ${cy + r} Z`);
        } else if (idx === 3) { // Waxing Gibbous (3/4 right lit)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 1 ${cx} ${cy + r} A ${r * 0.5} ${r} 0 0 1 ${cx} ${cy - r}`);
        } else if (idx === 4) { // Full Moon (all lit)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 1 ${cx} ${cy + r} A ${r} ${r} 0 0 1 ${cx} ${cy - r}`);
        } else if (idx === 5) { // Waning Gibbous (3/4 left lit)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 0 ${cx} ${cy + r} A ${r * 0.5} ${r} 0 0 0 ${cx} ${cy - r}`);
        } else if (idx === 6) { // 3rd Quarter (left half lit)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 0 ${cx} ${cy + r} Z`);
        } else if (idx === 7) { // Waning Crescent (crescent on left)
          path.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 0 ${cx} ${cy + r} A ${r * 0.5} ${r} 0 0 1 ${cx} ${cy - r}`);
        }
      }

      btns.forEach((btn, i) => {
        btn.addEventListener('click', () => {
          sfx.playClick();
          updatePhase(i);
        });
      });
      updatePhase(phaseIndex);
    }

    // 3. Synodic vs Sidereal Month Runner (27.3 vs 29.5 Days)
    function simSynodicVsSidereal() {
      simHeaderTitle.textContent = "Synodic (29.5 d) vs. Sidereal (27.3 d) Month Mechanics";
      let dayProgress = 29.5;

      simCanvas.innerHTML = `
        <svg id="synodicSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sun at Left -->
          <circle cx="30" cy="160" r="45" fill="#f59e0b"/>
          <circle cx="30" cy="160" r="55" fill="none" stroke="#fde047" stroke-width="2" stroke-dasharray="6 4"/>
          <text x="30" y="165" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">SUN</text>

          <!-- Earth Position 1 (Day 0) -->
          <g opacity="0.4">
            <circle cx="200" cy="160" r="16" fill="#3b82f6"/>
            <text x="200" y="195" fill="#94a3b8" font-size="9" text-anchor="middle">Earth (Day 0)</text>
            <circle cx="245" cy="160" r="7" fill="#fde047"/>
            <line x1="30" y1="160" x2="260" y2="160" stroke="#fde047" stroke-width="1" stroke-dasharray="2 2"/>
          </g>

          <!-- Earth Orbit Arc -->
          <path d="M 200 160 A 250 250 0 0 1 360 250" fill="none" stroke="rgba(96, 165, 250, 0.3)" stroke-width="2"/>

          <!-- Dynamic Moving Earth & Moon System -->
          <g id="dynEarthSystem" transform="translate(320, 225)">
            <!-- Earth -->
            <circle cx="0" cy="0" r="18" fill="#3b82f6"/>
            <text x="0" y="4" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">EARTH</text>
            
            <!-- Moon Orbit circle -->
            <circle cx="0" cy="0" r="50" fill="none" stroke="rgba(255, 255, 255, 0.2)" stroke-dasharray="3 3"/>

            <!-- Line to Distant Star (Sidereal Marker: 0° Angle) -->
            <line x1="0" y1="0" x2="60" y2="0" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4 2"/>
            <text x="65" y="4" fill="#c084fc" font-size="8" font-weight="700">★ Fixed Star (27.3 d)</text>

            <!-- Line to Sun (Synodic Alignment) -->
            <line id="lineEarthSun" x1="0" y1="0" x2="-290" y2="-65" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3 3"/>

            <!-- Moving Moon -->
            <circle id="dynMoon" cx="50" cy="0" r="8" fill="#fde047"/>
            <text id="dynMoonLabel" x="50" y="-12" fill="#fde047" font-size="8" font-weight="700" text-anchor="middle">MOON</text>
          </g>

          <!-- Explanatory Box -->
          <rect x="20" y="245" width="240" height="65" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8"/>
          <text id="synodicStatus" x="30" y="268" fill="#38bdf8" font-size="11" font-weight="700">Day 29.5: Synodic Month Complete!</text>
          <text x="30" y="285" fill="#cbd5e1" font-size="9.5">Moon realigns with Sun after travelling an extra</text>
          <text x="30" y="299" fill="#fde047" font-size="9.5" font-weight="700">27° (taking 2.2 extra days) to reset phase.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⏳ Lunar Cycle Progression (Days):</span>
          <span id="synDayVal" class="control-value">${dayProgress} Days</span>
        </div>
        <input type="range" id="sliderSynDay" class="sim-slider" min="0" max="29.5" step="0.5" value="${dayProgress}">
        <div class="sim-btn-group" style="margin-top: 0.5rem;">
          <button id="btnSynDay27" class="sim-toggle-btn">Step to Day 27.3 (Sidereal)</button>
          <button id="btnSynDay29" class="sim-toggle-btn active">Step to Day 29.5 (Synodic)</button>
        </div>
      `;

      const slider = document.getElementById('sliderSynDay');
      const dayVal = document.getElementById('synDayVal');
      const moon = document.getElementById('dynMoon');
      const moonLabel = document.getElementById('dynMoonLabel');
      const statusText = document.getElementById('synodicStatus');
      const dynSystem = document.getElementById('dynEarthSystem');

      function updateSynodic(day) {
        dayProgress = day;
        dayVal.textContent = `${day} Days`;
        slider.value = day;

        // Earth moves along its orbit
        const frac = day / 29.5;
        const earthX = 200 + (320 - 200) * frac;
        const earthY = 160 + (225 - 160) * frac;
        dynSystem.setAttribute('transform', `translate(${earthX}, ${earthY})`);

        // Moon angle: at day 27.3, angle is 360° (back at fixed star line).
        // At day 29.5, angle is 360° + 27° = 387° (aligned with Sun line).
        const moonAngleDeg = (day / 27.32) * 360;
        const rad = (moonAngleDeg * Math.PI) / 180;
        const mx = 50 * Math.cos(rad);
        const my = 50 * Math.sin(rad);
        moon.setAttribute('cx', mx);
        moon.setAttribute('cy', my);
        moonLabel.setAttribute('x', mx);
        moonLabel.setAttribute('y', my - 10);

        if (day < 26.5) {
          statusText.textContent = `Day ${day}: Moon revolving around Earth...`;
          statusText.setAttribute('fill', '#94a3b8');
        } else if (day >= 26.5 && day <= 28) {
          statusText.textContent = `Day 27.3: 360° Sidereal Orbit Complete!`;
          statusText.setAttribute('fill', '#c084fc');
        } else {
          statusText.textContent = `Day 29.5: Synodic Month Complete (Realigned with Sun)!`;
          statusText.setAttribute('fill', '#38bdf8');
        }
      }

      slider.addEventListener('input', (e) => updateSynodic(parseFloat(e.target.value)));
      document.getElementById('btnSynDay27').addEventListener('click', () => updateSynodic(27.3));
      document.getElementById('btnSynDay29').addEventListener('click', () => updateSynodic(29.5));
      updateSynodic(dayProgress);
    }

    // 4. Locating the Moon in the Daily Sky (~50 min Delay)
    function simLocatingMoonSky() {
      simHeaderTitle.textContent = "Locating the Moon: 50-Minute Daily Rising Delay";
      let lunarDay = 7; // First Quarter initially

      simCanvas.innerHTML = `
        <svg id="skyDomeSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Ground Horizon -->
          <rect x="0" y="240" width="500" height="80" fill="#091322"/>
          <line x1="0" y1="240" x2="500" y2="240" stroke="#38bdf8" stroke-width="2"/>
          <text x="30" y="260" fill="#38bdf8" font-size="12" font-weight="800">EAST (Horizon)</text>
          <text x="250" y="260" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">SOUTH (Zenith)</text>
          <text x="470" y="260" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="end">WEST (Horizon)</text>

          <!-- Sky Dome Arc -->
          <path d="M 40 240 A 210 210 0 0 1 460 240" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-width="2" stroke-dasharray="6 4"/>

          <!-- Observer on Ground -->
          <circle cx="250" cy="235" r="5" fill="#fbcfe8"/>
          <line x1="250" y1="235" x2="250" y2="240" stroke="#fbcfe8" stroke-width="2"/>
          <text x="250" y="280" fill="#cbd5e1" font-size="10" text-anchor="middle">Observer on Earth</text>

          <!-- Sun at Sunset (18:00) -->
          <circle cx="450" cy="235" r="16" fill="#f59e0b"/>
          <text x="450" y="212" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">Sun (Sunset)</text>

          <!-- Moving Moon on Dome -->
          <g id="skyMoonGroup" transform="translate(250, 60)">
            <circle cx="0" cy="0" r="14" fill="#1e293b" stroke="#fde047" stroke-width="1.5"/>
            <path id="skyMoonLit" d="M 0 -14 A 14 14 0 0 1 0 14 Z" fill="#fef08a"/>
            <text id="skyMoonText" x="0" y="-18" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Moon</text>
          </g>

          <!-- Data Card -->
          <rect x="20" y="20" width="220" height="85" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(96, 165, 250, 0.3)"/>
          <text id="skyCardDay" x="30" y="42" fill="#38bdf8" font-size="12" font-weight="700">Lunar Day 7 (First Quarter)</text>
          <text id="skyCardRise" x="30" y="62" fill="#cbd5e1" font-size="10.5">Moonrise Time: ~12:00 PM (Noon)</text>
          <text id="skyCardPos" x="30" y="80" fill="#fde047" font-size="10.5">Position at Sunset: High at Zenith!</text>
          <text x="30" y="96" fill="#94a3b8" font-size="9">Daily delay: ~50 mins later each day</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">📅 Day of Lunar Month (1 to 28 Days):</span>
          <span id="lunarDayVal" class="control-value">Day ${lunarDay}</span>
        </div>
        <input type="range" id="sliderLunarDay" class="sim-slider" min="1" max="28" value="${lunarDay}">
        <div class="control-row" style="margin-top: 0.5rem; font-size: 0.82rem; color: #94a3b8;">
          <span>Notice: On Day 14 (Full Moon), the Moon rises in the <strong>East</strong> exactly when the Sun sets in the <strong>West</strong>!</span>
        </div>
      `;

      const slider = document.getElementById('sliderLunarDay');
      const valText = document.getElementById('lunarDayVal');
      const moonGrp = document.getElementById('skyMoonGroup');
      const moonLit = document.getElementById('skyMoonLit');
      const cDay = document.getElementById('skyCardDay');
      const cRise = document.getElementById('skyCardRise');
      const cPos = document.getElementById('skyCardPos');

      function updateSky(day) {
        lunarDay = day;
        valText.textContent = `Day ${day}`;

        // At sunset: Day 1 (New) is near West (450, 235). Day 7 is at Zenith (250, 60). Day 14 is at East (50, 235).
        const angleOnDome = ((day - 1) / 14) * Math.PI; // 0 to PI
        const cx = 450 - 200 * Math.sin(angleOnDome);
        const cy = 235 - 175 * Math.sin(angleOnDome);

        if (day <= 15) {
          moonGrp.setAttribute('transform', `translate(${cx}, ${cy})`);
          moonGrp.style.display = 'block';
        } else {
          // Rises after sunset, below horizon at 18:00
          moonGrp.setAttribute('transform', `translate(50, 260)`);
          moonGrp.style.display = 'none';
        }

        // Calculate approximate rise time (rises ~50 min later each day from 6:00 AM)
        const totalMinutes = 6 * 60 + (day - 1) * 50;
        const hr = Math.floor((totalMinutes / 60) % 24);
        const mn = Math.floor(totalMinutes % 60);
        const ampm = hr >= 12 ? 'PM' : 'AM';
        const displayHr = hr % 12 === 0 ? 12 : hr % 12;
        const timeStr = `${displayHr}:${mn < 10 ? '0' : ''}${mn} ${ampm}`;

        cDay.textContent = `Lunar Day ${day}`;
        cRise.textContent = `Moonrise Time: ~${timeStr}`;

        if (day === 1) {
          cPos.textContent = "Position at Sunset: Setting with the Sun";
        } else if (day >= 6 && day <= 8) {
          cPos.textContent = "Position at Sunset: High at Southern Zenith";
        } else if (day >= 13 && day <= 15) {
          cPos.textContent = "Position at Sunset: Rising on Eastern Horizon!";
        } else if (day > 15) {
          cPos.textContent = "Position at Sunset: Below horizon (rises at night)";
        } else {
          cPos.textContent = "Position at Sunset: Visible in southwest sky";
        }
      }

      slider.addEventListener('input', (e) => updateSky(parseInt(e.target.value)));
      updateSky(lunarDay);
    }

    // 5. Sun-Earth-Moon Dual Spatial Geometry
    function simOrbitalGeometry() {
      simHeaderTitle.textContent = "Dual-View Sun-Earth-Moon Orbital Geometry";
      let elAngle = 90; // First Quarter

      simCanvas.innerHTML = `
        <svg id="geomSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Left Half: Space Overhead View -->
          <rect x="10" y="10" width="280" height="300" rx="10" fill="rgba(15, 23, 42, 0.6)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text x="150" y="32" fill="#93c5fd" font-size="11" font-weight="700" text-anchor="middle">TOP-DOWN SPACE VIEW</text>

          <!-- Sun Rays -->
          <line x1="20" y1="160" x2="70" y2="160" stroke="#fde047" stroke-width="3"/>
          <polygon points="70,156 80,160 70,164" fill="#fde047"/>
          <text x="35" y="150" fill="#fde047" font-size="9" font-weight="700">SUNLIGHT</text>

          <!-- Earth at Center -->
          <circle cx="160" cy="160" r="22" fill="#3b82f6"/>
          <!-- Orbit -->
          <circle cx="160" cy="160" r="80" fill="none" stroke="rgba(96, 165, 250, 0.25)" stroke-dasharray="4 3"/>

          <!-- Line of Sight from Earth to Moon -->
          <line id="geomLosLine" x1="160" y1="160" x2="160" y2="80" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3"/>

          <!-- Moon in Orbit -->
          <g id="geomMoonGrp" transform="translate(160, 80)">
            <circle cx="0" cy="0" r="12" fill="#1e293b"/>
            <!-- Left half always lit by sun -->
            <path d="M 0 -12 A 12 12 0 0 0 0 12 Z" fill="#fef08a"/>
          </g>

          <!-- Right Half: Earth Telescope View -->
          <rect x="305" y="10" width="185" height="300" rx="10" fill="rgba(15, 23, 42, 0.6)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text x="397" y="32" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">TELESCOPE VIEW FROM EARTH</text>

          <circle cx="397" cy="140" r="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
          <!-- Dynamic Moon disk in telescope -->
          <path id="geomTelePath" d="M 397 80 A 60 60 0 0 1 397 200 Z" fill="#fef08a"/>

          <!-- Angle Indicator Readout -->
          <rect x="315" y="225" width="165" height="70" rx="8" fill="rgba(10, 17, 40, 0.9)" stroke="rgba(56, 189, 248, 0.4)"/>
          <text id="geomAngleText" x="397" y="248" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Elongation: 90°</text>
          <text id="geomPhaseText" x="397" y="268" fill="#fde047" font-size="11" font-weight="700" text-anchor="middle">First Quarter (50% Lit)</text>
          <text x="397" y="285" fill="#94a3b8" font-size="9" text-anchor="middle">Separation between Sun & Moon</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">📐 Sun-Earth-Moon Elongation Angle:</span>
          <span id="geomAngleVal" class="control-value">${elAngle}°</span>
        </div>
        <input type="range" id="sliderGeomAngle" class="sim-slider" min="0" max="360" value="${elAngle}">
        <div class="sim-btn-group" style="margin-top: 0.5rem;">
          <button class="sim-toggle-btn" data-a="0">0° (New Moon)</button>
          <button class="sim-toggle-btn active" data-a="90">90° (1st Quarter)</button>
          <button class="sim-toggle-btn" data-a="180">180° (Full Moon)</button>
          <button class="sim-toggle-btn" data-a="270">270° (3rd Quarter)</button>
        </div>
      `;

      const slider = document.getElementById('sliderGeomAngle');
      const valLabel = document.getElementById('geomAngleVal');
      const moonGrp = document.getElementById('geomMoonGrp');
      const losLine = document.getElementById('geomLosLine');
      const telePath = document.getElementById('geomTelePath');
      const angleText = document.getElementById('geomAngleText');
      const phaseText = document.getElementById('geomPhaseText');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateGeom(ang) {
        elAngle = ang;
        valLabel.textContent = `${ang}°`;
        slider.value = ang;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.a) === ang));

        const rad = (ang * Math.PI) / 180;
        const mx = 160 + 80 * Math.cos(rad);
        const my = 160 + 80 * Math.sin(rad);
        moonGrp.setAttribute('transform', `translate(${mx}, ${my})`);
        losLine.setAttribute('x2', mx);
        losLine.setAttribute('y2', my);

        angleText.textContent = `Elongation: ${ang}°`;

        // Update telescope view
        const r = 60;
        const cx = 397;
        const cy = 140;
        const norm = ang % 360;
        const rx = Math.abs(r * Math.cos(rad));

        if (norm >= 0 && norm <= 180) {
          const sweep = norm > 90 ? 1 : 0;
          telePath.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 1 ${cx} ${cy + r} A ${rx} ${r} 0 0 ${sweep} ${cx} ${cy - r}`);
        } else {
          const sweep = norm > 270 ? 0 : 1;
          telePath.setAttribute('d', `M ${cx} ${cy - r} A ${r} ${r} 0 0 0 ${cx} ${cy + r} A ${rx} ${r} 0 0 ${sweep} ${cx} ${cy - r}`);
        }

        if (ang === 0 || ang === 360) phaseText.textContent = "New Moon (0% Lit)";
        else if (ang === 90) phaseText.textContent = "First Quarter (50% Lit)";
        else if (ang === 180) phaseText.textContent = "Full Moon (100% Lit)";
        else if (ang === 270) phaseText.textContent = "Third Quarter (50% Lit)";
        else if (ang < 90) phaseText.textContent = "Waxing Crescent";
        else if (ang < 180) phaseText.textContent = "Waxing Gibbous";
        else if (ang < 270) phaseText.textContent = "Waning Gibbous";
        else phaseText.textContent = "Waning Crescent";
      }

      slider.addEventListener('input', (e) => updateGeom(parseInt(e.target.value)));
      btns.forEach(b => b.addEventListener('click', () => updateGeom(parseInt(b.dataset.a))));
      updateGeom(elAngle);
    }

    // 6. Synchronous Rotation & Tidal Locking Simulator
    function simSynchronousRotation() {
      simHeaderTitle.textContent = "Tidal Locking & Synchronous Rotation Simulator";
      let isTidallyLocked = true;
      let orbitPos = 0; // 0 to 360

      simCanvas.innerHTML = `
        <svg id="syncSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Earth at Center -->
          <circle cx="250" cy="160" r="30" fill="#3b82f6"/>
          <text x="250" y="165" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">EARTH</text>

          <!-- Moon Orbit Track -->
          <circle cx="250" cy="160" r="105" fill="none" stroke="rgba(96, 165, 250, 0.3)" stroke-width="1.5" stroke-dasharray="4 4"/>

          <!-- Orbiting Moon System -->
          <g id="syncMoonGrp" transform="translate(355, 160)">
            <!-- Moon sphere -->
            <circle cx="0" cy="0" r="22" fill="#334155" stroke="#fde047" stroke-width="1.5"/>
            <!-- Near Side Marker (Red flag facing Earth) -->
            <circle cx="-16" cy="0" r="5" fill="#ef4444"/>
            <text x="-16" y="3" fill="#ffffff" font-size="6" font-weight="900" text-anchor="middle">N</text>
            <!-- Far Side Marker (Blue flag) -->
            <circle cx="16" cy="0" r="5" fill="#3b82f6"/>
            <text x="16" y="3" fill="#ffffff" font-size="6" font-weight="900" text-anchor="middle">F</text>
          </g>

          <!-- Sight Line from Earth to Moon Near Side -->
          <line id="syncSightLine" x1="250" y1="160" x2="339" y2="160" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3"/>

          <!-- Legend Box -->
          <rect x="20" y="240" width="460" height="70" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255, 255, 255, 0.1)"/>
          <circle cx="35" cy="260" r="6" fill="#ef4444"/>
          <text x="50" y="264" fill="#fecaca" font-size="10.5" font-weight="700">Near Side (N): Permanently faces Earth in Synchronous Rotation</text>
          <circle cx="35" cy="285" r="6" fill="#3b82f6"/>
          <text x="50" y="289" fill="#bfdbfe" font-size="10.5" font-weight="700">Far Side (F): Never visible from Earth (First imaged by Soviet Luna 3 in 1959)</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🔄 Moon Orbital Position:</span>
          <span id="syncPosVal" class="control-value">${orbitPos}°</span>
        </div>
        <input type="range" id="sliderSyncPos" class="sim-slider" min="0" max="360" value="${orbitPos}">
        <div class="sim-btn-group" style="margin-top: 0.5rem;">
          <button id="btnLockToggle" class="sim-toggle-btn active">Mode: Tidally Locked (1 Orbit = 1 Rotation)</button>
          <button id="btnNoLockToggle" class="sim-toggle-btn">Hypothetical: No Axial Rotation</button>
        </div>
      `;

      const slider = document.getElementById('sliderSyncPos');
      const valLabel = document.getElementById('syncPosVal');
      const moonGrp = document.getElementById('syncMoonGrp');
      const sightLine = document.getElementById('syncSightLine');
      const btnLock = document.getElementById('btnLockToggle');
      const btnNoLock = document.getElementById('btnNoLockToggle');

      function updateSync(pos) {
        orbitPos = pos;
        valLabel.textContent = `${pos}°`;
        const rad = (pos * Math.PI) / 180;
        const mx = 250 + 105 * Math.cos(rad);
        const my = 160 + 105 * Math.sin(rad);

        // Rotation angle
        const rot = isTidallyLocked ? pos : 0;
        moonGrp.setAttribute('transform', `translate(${mx}, ${my}) rotate(${rot})`);

        sightLine.setAttribute('x2', mx);
        sightLine.setAttribute('y2', my);
      }

      slider.addEventListener('input', (e) => updateSync(parseInt(e.target.value)));

      btnLock.addEventListener('click', () => {
        isTidallyLocked = true;
        btnLock.classList.add('active');
        btnNoLock.classList.remove('active');
        updateSync(orbitPos);
      });

      btnNoLock.addEventListener('click', () => {
        isTidallyLocked = false;
        btnNoLock.classList.add('active');
        btnLock.classList.remove('active');
        updateSync(orbitPos);
      });

      updateSync(orbitPos);
    }

    // 7. Eclipses & The 5.14° Orbital Tilt Simulator
    function simEclipsesGeometry() {
      simHeaderTitle.textContent = "Eclipses & The 5.14° Orbital Tilt Simulator";
      let eclipseType = "solar"; // "solar" or "lunar"
      let isTilted = false; // 0° vs 5.14°

      simCanvas.innerHTML = `
        <svg id="eclipseSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sun on Left -->
          <circle cx="40" cy="160" r="35" fill="#f59e0b"/>
          <text x="40" y="165" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">SUN</text>

          <!-- Shadow Cones -->
          <polygon id="penumbraCone" points="40,125 460,80 460,240 40,195" fill="rgba(56, 189, 248, 0.08)"/>
          <polygon id="umbraCone" points="40,140 380,160 40,180" fill="rgba(15, 23, 42, 0.75)"/>

          <!-- Body 1 (Earth or Moon) -->
          <g id="eclBody1" transform="translate(200, 160)">
            <circle cx="0" cy="0" r="14" fill="#334155" stroke="#fde047" stroke-width="1.5"/>
            <text id="eclBody1Text" x="0" y="24" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Moon</text>
          </g>

          <!-- Body 2 (Target: Earth or Moon) -->
          <g id="eclBody2" transform="translate(360, 160)">
            <circle cx="0" cy="0" r="24" fill="#3b82f6"/>
            <text id="eclBody2Text" x="0" y="38" fill="#93c5fd" font-size="10" font-weight="700" text-anchor="middle">Earth</text>
          </g>

          <!-- Status Indicator -->
          <rect x="50" y="245" width="400" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(96, 165, 250, 0.3)"/>
          <text id="eclStatus" x="250" y="270" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Solar Eclipse: Moon casts Umbral shadow onto Earth</text>
          <text id="eclSubStatus" x="250" y="292" fill="#cbd5e1" font-size="10" text-anchor="middle">Only happens during New Moon when crossing orbital nodes</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnSolarEcl" class="sim-toggle-btn active">Solar Eclipse (Surya Grahan)</button>
          <button id="btnLunarEcl" class="sim-toggle-btn">Lunar Eclipse (Chandra Grahan)</button>
        </div>
        <div class="sim-btn-group" style="justify-content: center; margin-top: 0.5rem;">
          <button id="btnTilt0" class="sim-toggle-btn active">Aligned at Node (Eclipse Occurs)</button>
          <button id="btnTilt5" class="sim-toggle-btn">5.14° Orbit Tilt (Shadow Misses Target!)</button>
        </div>
      `;

      const b1 = document.getElementById('eclBody1');
      const b2 = document.getElementById('eclBody2');
      const b1Text = document.getElementById('eclBody1Text');
      const b2Text = document.getElementById('eclBody2Text');
      const umbra = document.getElementById('umbraCone');
      const penumbra = document.getElementById('penumbraCone');
      const status = document.getElementById('eclStatus');
      const subStatus = document.getElementById('eclSubStatus');

      function updateEcl() {
        const yOffset = isTilted ? -45 : 0;

        if (eclipseType === 'solar') {
          // Moon between Sun and Earth
          b1.setAttribute('transform', `translate(220, ${160 + yOffset})`);
          b1.querySelector('circle').setAttribute('r', '12');
          b1.querySelector('circle').setAttribute('fill', '#334155');
          b1Text.textContent = "Moon";

          b2.setAttribute('transform', `translate(370, 160)`);
          b2.querySelector('circle').setAttribute('r', '24');
          b2.querySelector('circle').setAttribute('fill', '#3b82f6');
          b2Text.textContent = "Earth";

          umbra.setAttribute('points', `40,140 370,${160 + yOffset} 40,180`);

          if (isTilted) {
            status.textContent = "⚠️ No Eclipse! Moon's shadow passes ABOVE Earth due to 5.14° tilt";
            status.setAttribute('fill', '#f59e0b');
            subStatus.textContent = "This is why solar eclipses do not occur at every New Moon!";
          } else {
            status.textContent = "🌑 Total Solar Eclipse: Moon's Umbra strikes Earth";
            status.setAttribute('fill', '#38bdf8');
            subStatus.textContent = "Occurs only during New Moon near orbital nodes (Amavasya)";
          }
        } else {
          // Earth between Sun and Moon
          b1.setAttribute('transform', `translate(220, 160)`);
          b1.querySelector('circle').setAttribute('r', '24');
          b1.querySelector('circle').setAttribute('fill', '#3b82f6');
          b1Text.textContent = "Earth";

          b2.setAttribute('transform', `translate(380, ${160 + yOffset})`);
          b2.querySelector('circle').setAttribute('r', '12');
          b2.querySelector('circle').setAttribute('fill', isTilted ? '#334155' : '#b91c1c'); // Blood red if in shadow
          b2Text.textContent = "Moon";

          umbra.setAttribute('points', '40,140 450,160 40,180');

          if (isTilted) {
            status.textContent = "⚠️ No Eclipse! Moon passes ABOVE Earth's shadow cone";
            status.setAttribute('fill', '#f59e0b');
            subStatus.textContent = "Moon receives direct sunlight, appearing as normal Full Moon";
          } else {
            status.textContent = "🌕 Total Lunar Eclipse: Moon enters Earth's Umbra (Blood Moon)";
            status.setAttribute('fill', '#f87171');
            subStatus.textContent = "Earth's atmosphere refracts red wavelengths, turning Moon coppery red";
          }
        }
      }

      document.getElementById('btnSolarEcl').addEventListener('click', (e) => {
        eclipseType = 'solar';
        e.target.classList.add('active');
        document.getElementById('btnLunarEcl').classList.remove('active');
        updateEcl();
      });

      document.getElementById('btnLunarEcl').addEventListener('click', (e) => {
        eclipseType = 'lunar';
        e.target.classList.add('active');
        document.getElementById('btnSolarEcl').classList.remove('active');
        updateEcl();
      });

      document.getElementById('btnTilt0').addEventListener('click', (e) => {
        isTilted = false;
        e.target.classList.add('active');
        document.getElementById('btnTilt5').classList.remove('active');
        updateEcl();
      });

      document.getElementById('btnTilt5').addEventListener('click', (e) => {
        isTilted = true;
        e.target.classList.add('active');
        document.getElementById('btnTilt0').classList.remove('active');
        updateEcl();
      });

      updateEcl();
    }

    // 8. Pure Lunar Calendar & 11-Day Annual Drift
    function simLunarCalendarDrift() {
      simHeaderTitle.textContent = "Pure Lunar Calendar: 11-Day Annual Seasonal Drift";
      let yearCount = 1;

      simCanvas.innerHTML = `
        <svg id="driftSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Solar Year Timeline (Fixed 365.25 Days) -->
          <rect x="30" y="40" width="440" height="50" rx="8" fill="rgba(59, 130, 246, 0.15)" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="45" y="60" fill="#93c5fd" font-size="11" font-weight="700">TROPICAL SOLAR YEAR: 365.25 Days (Seasons Locked)</text>
          
          <!-- Seasonal Blocks in Solar Year -->
          <rect x="45" y="68" width="95" height="15" fill="#3b82f6" opacity="0.6"/>
          <text x="92" y="79" fill="#ffffff" font-size="8" text-anchor="middle">WINTER</text>
          <rect x="145" y="68" width="95" height="15" fill="#10b981" opacity="0.6"/>
          <text x="192" y="79" fill="#ffffff" font-size="8" text-anchor="middle">SPRING</text>
          <rect x="245" y="68" width="95" height="15" fill="#f59e0b" opacity="0.6"/>
          <text x="292" y="79" fill="#ffffff" font-size="8" text-anchor="middle">SUMMER</text>
          <rect x="345" y="68" width="115" height="15" fill="#8b5cf6" opacity="0.6"/>
          <text x="402" y="79" fill="#ffffff" font-size="8" text-anchor="middle">AUTUMN</text>

          <!-- Pure Lunar Year Timeline (12 x 29.53 = 354 Days) -->
          <rect x="30" y="125" width="440" height="50" rx="8" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="45" y="145" fill="#fde047" font-size="11" font-weight="700">PURE LUNAR YEAR: 354 Days (12 Synodic Months)</text>
          
          <!-- 354 Day Fill Bar -->
          <rect x="45" y="153" width="390" height="15" fill="#f59e0b" opacity="0.7"/>
          <!-- 11 Day Deficit Gap -->
          <rect x="435" y="153" width="25" height="15" fill="#ef4444" opacity="0.8"/>
          <text x="447" y="164" fill="#ffffff" font-size="7.5" font-weight="700" text-anchor="middle">-11d</text>

          <!-- 33-Year Cycle Wheel / Indicator -->
          <rect x="30" y="200" width="440" height="105" rx="10" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text id="driftYearTitle" x="50" y="228" fill="#38bdf8" font-size="13" font-weight="700">After Year 1: Cumulative Deficit = 11 Days</text>
          <text id="driftFestivalDesc" x="50" y="252" fill="#cbd5e1" font-size="11">Festival Month shifts ~11 days earlier in the solar season.</text>
          <text id="driftCycleInfo" x="50" y="274" fill="#fde047" font-size="10.5">Over ~33 solar years, lunar festivals cycle through all 4 seasons completely!</text>
          <text x="50" y="294" fill="#94a3b8" font-size="9.5">Example: The holy month of Ramadan returns to the exact same season every 33 years.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⏳ Elapsed Years (1 to 33 Years):</span>
          <span id="driftYearVal" class="control-value">Year ${yearCount}</span>
        </div>
        <input type="range" id="sliderDriftYear" class="sim-slider" min="1" max="33" value="${yearCount}">
      `;

      const slider = document.getElementById('sliderDriftYear');
      const valLabel = document.getElementById('driftYearVal');
      const yTitle = document.getElementById('driftYearTitle');
      const fDesc = document.getElementById('driftFestivalDesc');
      const cInfo = document.getElementById('driftCycleInfo');

      function updateDrift(yr) {
        yearCount = yr;
        valLabel.textContent = `Year ${yr}`;
        const totalDeficit = Math.round(yr * 10.875);
        yTitle.textContent = `After Year ${yr}: Cumulative Deficit = ${totalDeficit} Days (~${(totalDeficit / 30).toFixed(1)} Months)`;

        if (yr === 1) {
          fDesc.textContent = "Festival Month shifts ~11 days earlier against Gregorian solar calendar.";
        } else if (yr === 16 || yr === 17) {
          fDesc.textContent = "Festival Month has shifted by ~6 months: Celebrated in opposite season (e.g. Summer to Winter)!";
        } else if (yr === 33) {
          fDesc.textContent = "Full 33-Year Cycle Complete! Festival returns to original seasonal start date.";
        } else {
          fDesc.textContent = `Festival month has advanced by ~${totalDeficit} days across the solar seasons.`;
        }
      }

      slider.addEventListener('input', (e) => updateDrift(parseInt(e.target.value)));
      updateDrift(yearCount);
    }

    // 9. Solar Calendars & The 400-Year Leap Rule
    function simSolarCalendarSeasons() {
      simHeaderTitle.textContent = "Tropical Solar Year & Gregorian 400-Year Leap Rule";
      let testYear = 2024;

      simCanvas.innerHTML = `
        <svg id="seasonsSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sun at Center -->
          <circle cx="250" cy="130" r="28" fill="#f59e0b"/>
          <text x="250" y="134" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">SUN</text>

          <!-- Earth Elliptical Orbit -->
          <ellipse cx="250" cy="130" rx="170" ry="75" fill="none" stroke="rgba(96, 165, 250, 0.25)" stroke-width="1.5"/>

          <!-- 4 Solstices / Equinoxes -->
          <!-- Vernal Equinox (March 21) -->
          <circle cx="250" cy="55" r="10" fill="#3b82f6"/>
          <text x="250" y="40" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">Vernal Equinox (Mar 21)</text>

          <!-- Summer Solstice (June 21) -->
          <circle cx="80" cy="130" r="10" fill="#10b981"/>
          <text x="80" y="152" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">Summer Solstice (Jun 21)</text>

          <!-- Autumnal Equinox (Sept 23) -->
          <circle cx="250" cy="205" r="10" fill="#8b5cf6"/>
          <text x="250" y="224" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle">Autumnal Equinox (Sep 23)</text>

          <!-- Winter Solstice (Dec 22) -->
          <circle cx="420" cy="130" r="10" fill="#f59e0b"/>
          <text x="420" y="152" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">Winter Solstice (Dec 22)</text>

          <!-- Gregorian Rule Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text id="leapVerdict" x="45" y="260" fill="#38bdf8" font-size="12" font-weight="700">Year 2024: LEAP YEAR (366 Days)</text>
          <text id="leapReason" x="45" y="280" fill="#cbd5e1" font-size="10">Divisible by 4 (2024 ÷ 4 = 506). February has 29 days.</text>
          <text x="45" y="298" fill="#94a3b8" font-size="9">Tropical Year = 365.2422 days. Rule: Div by 4, but century must be div by 400!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🔍 Test Any Gregorian Year:</span>
          <input type="number" id="inputTestYear" value="${testYear}" style="background: #0f172a; border: 1px solid #38bdf8; color: #fff; padding: 0.35rem 0.6rem; border-radius: 6px; font-weight: 700; width: 100px;">
          <div class="sim-btn-group">
            <button class="sim-toggle-btn" data-y="1900">1900</button>
            <button class="sim-toggle-btn" data-y="2000">2000</button>
            <button class="sim-toggle-btn active" data-y="2024">2024</button>
            <button class="sim-toggle-btn" data-y="2100">2100</button>
          </div>
        </div>
      `;

      const input = document.getElementById('inputTestYear');
      const vText = document.getElementById('leapVerdict');
      const rText = document.getElementById('leapReason');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function testLeap(yr) {
        testYear = yr;
        input.value = yr;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.y) === yr));

        let isLeap = false;
        let explanation = "";

        if (yr % 4 !== 0) {
          isLeap = false;
          explanation = `Not divisible by 4. Common year with 365 days.`;
        } else if (yr % 100 !== 0) {
          isLeap = true;
          explanation = `Divisible by 4 and not a century year (${yr} ÷ 4 = ${yr / 4}). Leap year with 366 days!`;
        } else if (yr % 400 === 0) {
          isLeap = true;
          explanation = `Century year divisible by 400 (${yr} ÷ 400 = ${yr / 400}). Rare Century Leap Year!`;
        } else {
          isLeap = false;
          explanation = `Century year NOT divisible by 400 (${yr} ÷ 400 = ${(yr / 400).toFixed(2)}). Century exception: NOT a leap year!`;
        }

        if (isLeap) {
          vText.textContent = `Year ${yr}: LEAP YEAR (366 Days)`;
          vText.setAttribute('fill', '#34d399');
        } else {
          vText.textContent = `Year ${yr}: COMMON YEAR (365 Days)`;
          vText.setAttribute('fill', '#f87171');
        }
        rText.textContent = explanation;
      }

      input.addEventListener('change', (e) => testLeap(parseInt(e.target.value) || 2024));
      btns.forEach(b => b.addEventListener('click', () => testLeap(parseInt(b.dataset.y))));
      testLeap(testYear);
    }

    // 10. Luni-Solar Calendars & Adhik Maas Synchronization
    function simLunisolarAdhikMaas() {
      simHeaderTitle.textContent = "Luni-Solar Harmony & Adhik Maas Insertion Simulator";
      let cycleYear = 3;

      simCanvas.innerHTML = `
        <svg id="lunisolarSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Outer Ring: Solar Seasons (Vasant, Grishma, Varsha, Sharad, Hemant, Shishir) -->
          <circle cx="250" cy="150" r="110" fill="none" stroke="#3b82f6" stroke-width="8" opacity="0.4"/>
          <text x="250" y="32" fill="#93c5fd" font-size="11" font-weight="700" text-anchor="middle">OUTER: Solar Seasons (365 Days / Year)</text>

          <!-- Inner Ring: Lunar Months (Chaitra, Vaisakha...) -->
          <circle cx="250" cy="150" r="80" fill="none" stroke="#f59e0b" stroke-width="8" opacity="0.6"/>
          <text x="250" y="145" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">LUNI-SOLAR</text>
          <text x="250" y="162" fill="#fde047" font-size="10" font-weight="700" text-anchor="middle">ENGINE</text>

          <!-- Deficit Accumulator Bar -->
          <rect x="50" y="235" width="400" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text id="adhikTitle" x="70" y="260" fill="#38bdf8" font-size="12" font-weight="700">Year 3: Accumulated Deficit = 33 Days (~1.1 Lunar Months)</text>
          <text id="adhikAction" x="70" y="280" fill="#34d399" font-size="11" font-weight="700">⚡ Adhik Maas (Intercalary 13th Month) INSERTED!</text>
          <text id="adhikDesc" x="70" y="298" fill="#cbd5e1" font-size="9.5">Reconciles Moon with Sun: Diwali stays in Autumn, Holi stays in Spring!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">📅 Luni-Solar Cycle Year:</span>
          <span id="adhikYearVal" class="control-value">Year ${cycleYear}</span>
        </div>
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn" data-y="1">Year 1 (Deficit: 11 d)</button>
          <button class="sim-toggle-btn" data-y="2">Year 2 (Deficit: 22 d)</button>
          <button class="sim-toggle-btn active" data-y="3">Year 3 (⚡ Adhik Maas Added!)</button>
          <button class="sim-toggle-btn" data-y="4">Year 4 (Resynchronized)</button>
        </div>
      `;

      const title = document.getElementById('adhikTitle');
      const action = document.getElementById('adhikAction');
      const desc = document.getElementById('adhikDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');
      const valLabel = document.getElementById('adhikYearVal');

      function updateAdhik(yr) {
        cycleYear = yr;
        valLabel.textContent = `Year ${yr}`;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.y) === yr));

        if (yr === 1) {
          title.textContent = "Year 1: Accumulated Deficit = 11 Days";
          action.textContent = "Normal Year (12 Lunar Months = 354 Days)";
          action.setAttribute('fill', '#94a3b8');
          desc.textContent = "Lunar calendar trails solar seasons by 11 days.";
        } else if (yr === 2) {
          title.textContent = "Year 2: Accumulated Deficit = 22 Days";
          action.textContent = "Normal Year (12 Lunar Months = 354 Days)";
          action.setAttribute('fill', '#f59e0b');
          desc.textContent = "Gap approaching one full lunar month (29.5 days).";
        } else if (yr === 3) {
          title.textContent = "Year 3: Accumulated Deficit = 33 Days (~1.1 Lunar Months)";
          action.textContent = "⚡ Adhik Maas (Intercalary 13th Month) INSERTED!";
          action.setAttribute('fill', '#34d399');
          desc.textContent = "Resynchronizes Moon with Sun: Diwali stays in Autumn, Holi in Spring!";
        } else {
          title.textContent = "Year 4: Reset & Synchronized";
          action.textContent = "Cycle restarts with near-zero seasonal deviation.";
          action.setAttribute('fill', '#38bdf8');
          desc.textContent = "Over 19 solar years, exactly 7 Adhik Maas months are inserted.";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateAdhik(parseInt(b.dataset.y))));
      updateAdhik(cycleYear);
    }

    // 11. The Indian National Calendar (Saka Samvat)
    function simIndianNationalCalendar() {
      simHeaderTitle.textContent = "Indian National Calendar (Saka Era) Architecture";
      let gregYear = 2026;

      simCanvas.innerHTML = `
        <svg id="sakaSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- 12 Months Grid -->
          <rect x="20" y="20" width="460" height="175" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(96, 165, 250, 0.3)"/>
          <text x="250" y="42" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">THE 12 MONTHS OF THE INDIAN NATIONAL CALENDAR</text>

          <!-- Row 1: Months 1-6 (31 days, Chaitra 30/31) -->
          <g transform="translate(35, 60)" font-size="9.5">
            <rect x="0" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.25)" stroke="#3b82f6"/>
            <text x="32" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">1. Chaitra</text>
            <text x="32" y="32" fill="#93c5fd" text-anchor="middle">30/31 d</text>

            <rect x="72" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6"/>
            <text x="104" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">2. Vaisakha</text>
            <text x="104" y="32" fill="#93c5fd" text-anchor="middle">31 d</text>

            <rect x="144" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6"/>
            <text x="176" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">3. Jyeshtha</text>
            <text x="176" y="32" fill="#93c5fd" text-anchor="middle">31 d</text>

            <rect x="216" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6"/>
            <text x="248" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">4. Ashadha</text>
            <text x="248" y="32" fill="#93c5fd" text-anchor="middle">31 d</text>

            <rect x="288" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6"/>
            <text x="320" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">5. Shravana</text>
            <text x="320" y="32" fill="#93c5fd" text-anchor="middle">31 d</text>

            <rect x="360" y="0" width="65" height="40" rx="5" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6"/>
            <text x="392" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">6. Bhadra</text>
            <text x="392" y="32" fill="#93c5fd" text-anchor="middle">31 d</text>
          </g>

          <!-- Row 2: Months 7-12 (30 days each) -->
          <g transform="translate(35, 115)" font-size="9.5">
            <rect x="0" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="32" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">7. Ashvina</text>
            <text x="32" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>

            <rect x="72" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="104" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">8. Kartika</text>
            <text x="104" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>

            <rect x="144" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="176" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">9. Agrahayana</text>
            <text x="176" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>

            <rect x="216" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="248" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">10. Pausha</text>
            <text x="248" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>

            <rect x="288" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="320" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">11. Magha</text>
            <text x="320" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>

            <rect x="360" y="0" width="65" height="40" rx="5" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="392" y="16" fill="#ffffff" font-weight="700" text-anchor="middle">12. Phalguna</text>
            <text x="392" y="32" fill="#a7f3d0" text-anchor="middle">30 d</text>
          </g>

          <text x="250" y="180" fill="#cbd5e1" font-size="9" text-anchor="middle">Adopted on March 22, 1957 (Chaitra 1, 1879 Saka) following Saha Committee Report</text>

          <!-- Conversion Display Card -->
          <rect x="20" y="210" width="460" height="95" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8"/>
          <text id="sakaYearText" x="250" y="238" fill="#fde047" font-size="14" font-weight="700" text-anchor="middle">2026 CE = 1948 Saka Era (Saka = Gregorian - 78)</text>
          <text x="250" y="262" fill="#93c5fd" font-size="11" text-anchor="middle">New Year (Chaitra 1) coincides with Vernal Equinox: March 22 (March 21 in Leap Year)</text>
          <text x="250" y="285" fill="#a7f3d0" font-size="10" text-anchor="middle">Official calendar of Government of India, All India Radio, and Gazette publications</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🔄 Convert Gregorian Year to Saka Year:</span>
          <span id="sakaValLabel" class="control-value">${gregYear} CE ➔ ${gregYear - 78} Saka</span>
        </div>
        <input type="range" id="sliderSakaYear" class="sim-slider" min="1957" max="2050" value="${gregYear}">
      `;

      const slider = document.getElementById('sliderSakaYear');
      const valLabel = document.getElementById('sakaValLabel');
      const yearText = document.getElementById('sakaYearText');

      function updateSaka(yr) {
        gregYear = yr;
        const saka = yr - 78;
        valLabel.textContent = `${yr} CE ➔ ${saka} Saka`;
        yearText.textContent = `${yr} CE = ${saka} Saka Era (Saka = Gregorian - 78)`;
      }

      slider.addEventListener('input', (e) => updateSaka(parseInt(e.target.value)));
      updateSaka(gregYear);
    }

    // 12. Astronomical Origins of Cultural Festivals
    function simFestivalAstronomy() {
      simHeaderTitle.textContent = "Astronomical Alignment of Cultural Festivals";
      let festKey = "diwali";

      const festData = {
        diwali: {
          title: "Diwali (Deepavali) • Festival of Lights",
          astro: "Kartika Amavasya (New Moon) — Darkest Night of the Month",
          desc: "Clay lamps (diyas) illuminate the pitch-black night, symbolizing the triumph of light and inner wisdom over darkness.",
          color: "#f59e0b",
          moonPhase: 0 // New Moon
        },
        holi: {
          title: "Holi • Festival of Colors & Spring Arrival",
          astro: "Phalguna Purnima (Full Moon) — Vernal Awakening",
          desc: "Celebrated on the radiant full moon of Phalguna, marking the end of winter cold and welcoming agricultural renewal.",
          color: "#ec4899",
          moonPhase: 180 // Full Moon
        },
        eid: {
          title: "Eid-ul-Fitr • Concluding Ramadan Fast",
          astro: "Sighting of the Hilal (Waxing Crescent Moon) of Shawwal",
          desc: "The celebratory festival begins strictly upon the physical visual sighting of the delicate crescent moon marking month 10.",
          color: "#10b981",
          moonPhase: 30 // Crescent
        },
        sankranti: {
          title: "Makar Sankranti & Pongal • Solar Harvest",
          astro: "Solar Transit (Sankranti) into Capricorn (Makara) on Jan 14/15",
          desc: "Governed directly by the solar calendar! Marks Uttarayan—the start of the Sun's six-month northward journey.",
          color: "#38bdf8",
          moonPhase: -1 // Solar
        }
      };

      simCanvas.innerHTML = `
        <svg id="festSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Night Sky background -->
          <circle cx="50" cy="50" r="1.5" fill="#fff"/>
          <circle cx="150" cy="80" r="1" fill="#fff"/>
          <circle cx="350" cy="40" r="1.5" fill="#fff"/>
          <circle cx="450" cy="90" r="1.2" fill="#fff"/>

          <!-- Celestial Center Visual -->
          <g id="festVisualGrp" transform="translate(250, 120)">
            <circle cx="0" cy="0" r="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
            <path id="festMoonPath" d="M 0 0 Z" fill="#fde047"/>
            <text id="festAstroBadge" x="0" y="70" fill="#fde047" font-size="11" font-weight="700" text-anchor="middle">Kartika Amavasya (New Moon)</text>
          </g>

          <!-- Festival Details Card -->
          <rect x="25" y="215" width="450" height="90" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255, 255, 255, 0.15)"/>
          <text id="festCardTitle" x="45" y="242" fill="#fbbf24" font-size="13" font-weight="700">Diwali • Festival of Lights</text>
          <text id="festCardAstro" x="45" y="264" fill="#93c5fd" font-size="11">Celestial Alignment: Kartika Amavasya</text>
          <text id="festCardDesc" x="45" y="286" fill="#cbd5e1" font-size="10">Clay lamps illuminate the darkest night of the year.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-f="diwali">🪔 Diwali</button>
          <button class="sim-toggle-btn" data-f="holi">🎨 Holi</button>
          <button class="sim-toggle-btn" data-f="eid">🌙 Eid-ul-Fitr</button>
          <button class="sim-toggle-btn" data-f="sankranti">☀️ Makar Sankranti</button>
        </div>
      `;

      const mPath = document.getElementById('festMoonPath');
      const badge = document.getElementById('festAstroBadge');
      const title = document.getElementById('festCardTitle');
      const astro = document.getElementById('festCardAstro');
      const desc = document.getElementById('festCardDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateFest(key) {
        festKey = key;
        btns.forEach(b => b.classList.toggle('active', b.dataset.f === key));
        const f = festData[key];
        title.textContent = f.title;
        title.setAttribute('fill', f.color);
        astro.textContent = `Celestial Alignment: ${f.astro}`;
        desc.textContent = f.desc;
        badge.textContent = f.astro;

        if (f.moonPhase === 0) { // New Moon
          mPath.setAttribute('d', 'M 0 0 Z');
        } else if (f.moonPhase === 180) { // Full Moon
          mPath.setAttribute('d', 'M 0 -50 A 50 50 0 1 1 0 50 A 50 50 0 1 1 0 -50');
        } else if (f.moonPhase === 30) { // Crescent
          mPath.setAttribute('d', 'M 0 -50 A 50 50 0 0 1 0 50 A 30 50 0 0 0 0 -50');
        } else { // Solar transit (Sun)
          mPath.setAttribute('d', 'M 0 -50 A 50 50 0 1 1 0 50 A 50 50 0 1 1 0 -50');
          mPath.setAttribute('fill', '#f59e0b');
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateFest(b.dataset.f)));
      updateFest(festKey);
    }

    // 13. Newton's Orbital Cannon & Orbital Velocity
    function simNewtonOrbitalCannon() {
      simHeaderTitle.textContent = "Newton's Orbital Cannon & Orbital Speed";
      let velocity = 7.9; // km/s (LEO)

      simCanvas.innerHTML = `
        <svg id="cannonSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Earth Globe -->
          <circle cx="250" cy="180" r="100" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
          <text x="250" y="210" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">EARTH</text>

          <!-- Mountain Peak on Top -->
          <polygon points="245,80 250,65 255,80" fill="#64748b"/>
          <!-- Cannon -->
          <rect x="250" y="63" width="12" height="5" fill="#fde047" rx="1"/>

          <!-- Trajectory Path -->
          <path id="cannonPath" d="M 262 65 A 115 115 0 1 1 261 65" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 3"/>

          <!-- Orbit Status Readout -->
          <rect x="20" y="245" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8"/>
          <text id="cannonVerdict" x="40" y="270" fill="#34d399" font-size="13" font-weight="700">Velocity: 7.9 km/s ➔ STABLE CIRCULAR ORBIT (LEO)!</text>
          <text id="cannonDesc" x="40" y="292" fill="#cbd5e1" font-size="10.5">The cannonball falls toward Earth at the exact rate Earth curves away!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🚀 Horizontal Cannon Launch Speed:</span>
          <span id="cannonSpeedVal" class="control-value">${velocity} km/s</span>
        </div>
        <input type="range" id="sliderCannonSpeed" class="sim-slider" min="3" max="12" step="0.1" value="${velocity}">
        <div class="sim-btn-group" style="margin-top: 0.5rem;">
          <button class="sim-toggle-btn" data-v="5.0">5.0 km/s (Crashes)</button>
          <button class="sim-toggle-btn active" data-v="7.9">7.9 km/s (LEO Circular)</button>
          <button class="sim-toggle-btn" data-v="9.5">9.5 km/s (Elliptical)</button>
          <button class="sim-toggle-btn" data-v="11.2">11.2 km/s (Escape Velocity)</button>
        </div>
      `;

      const slider = document.getElementById('sliderCannonSpeed');
      const valLabel = document.getElementById('cannonSpeedVal');
      const path = document.getElementById('cannonPath');
      const verdict = document.getElementById('cannonVerdict');
      const desc = document.getElementById('cannonDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateCannon(v) {
        velocity = v;
        valLabel.textContent = `${v.toFixed(1)} km/s (${Math.round(v * 3600)} km/h)`;
        slider.value = v;
        btns.forEach(b => b.classList.toggle('active', parseFloat(b.dataset.v) === v));

        if (v < 7.5) {
          // Crashes
          path.setAttribute('d', 'M 262 65 Q 350 80 320 140');
          path.setAttribute('stroke', '#ef4444');
          verdict.textContent = `Velocity: ${v.toFixed(1)} km/s ➔ SUB-ORBITAL CRASH`;
          verdict.setAttribute('fill', '#ef4444');
          desc.textContent = "Forward speed insufficient; gravity pulls projectile back into the ground.";
        } else if (v >= 7.5 && v <= 8.5) {
          // Circular LEO
          path.setAttribute('d', 'M 262 65 A 115 115 0 1 1 261 65');
          path.setAttribute('stroke', '#10b981');
          verdict.textContent = `Velocity: ${v.toFixed(1)} km/s ➔ STABLE CIRCULAR ORBIT (LEO)!`;
          verdict.setAttribute('fill', '#34d399');
          desc.textContent = "Forward speed balances gravity; satellite enters permanent free-fall around Earth.";
        } else if (v > 8.5 && v < 11.2) {
          // Elliptical
          path.setAttribute('d', 'M 262 65 A 160 115 0 1 1 261 65');
          path.setAttribute('stroke', '#38bdf8');
          verdict.textContent = `Velocity: ${v.toFixed(1)} km/s ➔ ELLIPTICAL ORBIT`;
          verdict.setAttribute('fill', '#38bdf8');
          desc.textContent = "High speed expands orbit into an elongated ellipse with distinct apogee and perigee.";
        } else {
          // Escape
          path.setAttribute('d', 'M 262 65 Q 400 30 500 10');
          path.setAttribute('stroke', '#f59e0b');
          verdict.textContent = `Velocity: ${v.toFixed(1)} km/s ➔ ESCAPE VELOCITY ACHIEVED!`;
          verdict.setAttribute('fill', '#fbbf24');
          desc.textContent = "Breaks free of Earth's gravity entirely and ventures into interplanetary space!";
        }
      }

      slider.addEventListener('input', (e) => updateCannon(parseFloat(e.target.value)));
      btns.forEach(b => b.addEventListener('click', () => updateCannon(parseFloat(b.dataset.v))));
      updateCannon(velocity);
    }

    // 14. Satellite Orbital Highways & NavIC Constellation
    function simSatelliteOrbitsNavic() {
      simHeaderTitle.textContent = "Satellite Orbital Highways & India's NavIC Constellation";
      let selectedOrbit = "navic";

      simCanvas.innerHTML = `
        <svg id="satSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Earth at Center -->
          <circle cx="250" cy="160" r="26" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
          <text x="250" y="164" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">EARTH</text>

          <!-- LEO (Low Earth Orbit ~400 km) -->
          <circle cx="250" cy="160" r="45" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3 3"/>
          <text x="250" y="110" fill="#38bdf8" font-size="8" text-anchor="middle">LEO (400 km • ISS)</text>

          <!-- MEO (GPS ~20,200 km) -->
          <circle cx="250" cy="160" r="85" fill="none" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="4 4"/>
          <text x="250" y="70" fill="#c084fc" font-size="8" text-anchor="middle">MEO (20,200 km • GPS)</text>

          <!-- GEO (Geostationary ~35,786 km) -->
          <circle cx="250" cy="160" r="130" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="250" y="24" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">GEOSTATIONARY ORBIT (35,786 km • 24h Period)</text>

          <!-- NavIC 7-Satellite Beams (Cones over India) -->
          <g id="navicGrp">
            <!-- 3 GEO Satellites -->
            <circle cx="340" cy="70" r="5" fill="#10b981"/>
            <circle cx="380" cy="160" r="5" fill="#10b981"/>
            <circle cx="340" cy="250" r="5" fill="#10b981"/>
            <!-- Coverage Cone to Earth -->
            <polygon points="380,160 250,140 250,180" fill="rgba(16, 185, 129, 0.25)"/>
          </g>

          <!-- Info Box -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981"/>
          <text id="satInfoTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">NavIC (Navigation with Indian Constellation)</text>
          <text id="satInfoDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">ISRO's 7-satellite regional constellation (3 GEO + 4 inclined GSO).</text>
          <text id="satInfoSpec" x="45" y="296" fill="#93c5fd" font-size="9.5">Covers all of India + 1,500 km beyond borders with sub-5 meter positioning accuracy!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn" data-s="leo">Low Earth Orbit (LEO)</button>
          <button class="sim-toggle-btn" data-s="meo">Medium Earth Orbit (MEO)</button>
          <button class="sim-toggle-btn" data-s="geo">Geostationary (GEO)</button>
          <button class="sim-toggle-btn active" data-s="navic">🛰️ NavIC Constellation</button>
        </div>
      `;

      const sTitle = document.getElementById('satInfoTitle');
      const sDesc = document.getElementById('satInfoDesc');
      const sSpec = document.getElementById('satInfoSpec');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateSat(s) {
        selectedOrbit = s;
        btns.forEach(b => b.classList.toggle('active', b.dataset.s === s));

        if (s === 'leo') {
          sTitle.textContent = "Low Earth Orbit (LEO: 160 – 2,000 km)";
          sTitle.setAttribute('fill', '#38bdf8');
          sDesc.textContent = "Hosts the International Space Station (ISS) and Earth observation sensors.";
          sSpec.textContent = "High speed: ~7.8 km/s; completes one full orbit around Earth in just 90 minutes!";
        } else if (s === 'meo') {
          sTitle.textContent = "Medium Earth Orbit (MEO: 2,000 – 35,786 km)";
          sTitle.setAttribute('fill', '#c084fc');
          sDesc.textContent = "Primary orbital highway for global navigation satellite systems (GPS, Galileo).";
          sSpec.textContent = "Typical altitude: ~20,200 km; completes one orbit in approximately 12 hours.";
        } else if (s === 'geo') {
          sTitle.textContent = "Geostationary Orbit (GEO: Exactly 35,786 km above Equator)";
          sTitle.setAttribute('fill', '#fbbf24');
          sDesc.textContent = "Orbital period is exactly 24 hours, perfectly matching Earth's rotation.";
          sSpec.textContent = "Appears completely stationary from the ground. Ideal for weather & telecommunications!";
        } else {
          sTitle.textContent = "NavIC (Navigation with Indian Constellation)";
          sTitle.setAttribute('fill', '#34d399');
          sDesc.textContent = "ISRO's autonomous regional navigation constellation composed of 7 operational satellites.";
          sSpec.textContent = "Covers all of India + 1,500 km region with dedicated civilian & strategic security channels.";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateSat(b.dataset.s)));
      updateSat(selectedOrbit);
    }

    // 15. Earth Remote Sensing & Deep Space (Chandrayaan & Aditya-L1)
    function simRemoteSensingSpace() {
      simHeaderTitle.textContent = "Multispectral Remote Sensing & Deep Space Missions";
      let mode = "aditya"; // "remote", "chandra", "aditya"

      simCanvas.innerHTML = `
        <svg id="remoteSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Visual Dynamic Container -->
          <g id="remoteDisplay">
            <!-- Sun at Left -->
            <circle cx="30" cy="160" r="35" fill="#f59e0b"/>
            <!-- Solar flares / Corona -->
            <path d="M 65 140 Q 85 145 70 160 Q 90 175 65 180" fill="none" stroke="#fde047" stroke-width="2"/>
            
            <!-- Earth at Right -->
            <circle cx="440" cy="160" r="22" fill="#3b82f6"/>
            <text x="440" y="195" fill="#93c5fd" font-size="9" text-anchor="middle">Earth</text>

            <!-- Lagrange Point L1 Marker (1.5 Million km from Earth) -->
            <line x1="30" y1="160" x2="440" y2="160" stroke="rgba(255, 255, 255, 0.15)" stroke-dasharray="3 3"/>
            <circle cx="370" cy="160" r="4" fill="#ef4444"/>
            <text x="370" y="145" fill="#f87171" font-size="9" font-weight="700" text-anchor="middle">Lagrange Point L1</text>

            <!-- Aditya-L1 Satellite in Halo Orbit -->
            <ellipse cx="370" cy="160" rx="15" ry="35" fill="none" stroke="#38bdf8" stroke-dasharray="3 2"/>
            <circle cx="385" cy="160" r="6" fill="#fde047"/>
            <text x="385" y="180" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Aditya-L1</text>
          </g>

          <!-- Mission Card -->
          <rect x="25" y="225" width="450" height="85" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8"/>
          <text id="missionTitle" x="45" y="248" fill="#38bdf8" font-size="12.5" font-weight="700">ISRO's Aditya-L1 Solar Observatory</text>
          <text id="missionDesc" x="45" y="268" fill="#cbd5e1" font-size="10.5">Stationed in halo orbit at Sun-Earth L1 point (1.5 million km from Earth).</text>
          <text id="missionHighlight" x="45" y="288" fill="#34d399" font-size="9.5">Uninterrupted 24/7 view of the Sun without eclipses, studying solar coronal mass ejections!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-m="aditya">☀️ Aditya-L1 Solar Mission</button>
          <button class="sim-toggle-btn" data-m="chandra">🌕 Chandrayaan-3 Moon Landing</button>
          <button class="sim-toggle-btn" data-m="remote">🌾 Earth Remote Sensing (IRS)</button>
        </div>
      `;

      const mTitle = document.getElementById('missionTitle');
      const mDesc = document.getElementById('missionDesc');
      const mHighlight = document.getElementById('missionHighlight');
      const disp = document.getElementById('remoteDisplay');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateMission(m) {
        mode = m;
        btns.forEach(b => b.classList.toggle('active', b.dataset.m === m));

        if (m === 'aditya') {
          mTitle.textContent = "ISRO's Aditya-L1 Solar Observatory";
          mDesc.textContent = "Stationed in halo orbit at Sun-Earth L1 point (1.5 million km from Earth).";
          mHighlight.textContent = "Uninterrupted 24/7 view of the Sun without eclipses, studying solar coronal mass ejections!";
        } else if (m === 'chandra') {
          mTitle.textContent = "Chandrayaan-3: Historic Lunar South Pole Landing";
          mDesc.textContent = "Touched down on August 23, 2023, making India the 1st nation near lunar South Pole!";
          mHighlight.textContent = "Vikram lander & Pragyan rover discovered sulfur, confirmed surface temperatures, and explored water ice.";
        } else {
          mTitle.textContent = "Indian Remote Sensing (IRS) & Cartosat Satellites";
          mDesc.textContent = "Multispectral cameras photograph Earth across visible, near-infrared, and radar spectrums.";
          mHighlight.textContent = "Calculates NDVI crop health, maps deforestation, monitors water bodies, and assists disaster rescue!";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateMission(b.dataset.m)));
      updateMission(mode);
    }

    // 16. Jantar Mantar Samrat Yantra Sundial Simulator
    function simJantarMantarSundial() {
      simHeaderTitle.textContent = "Jantar Mantar: Vrihat Samrat Yantra Sundial";
      let solarHour = 14; // 2:00 PM

      simCanvas.innerHTML = `
        <svg id="sundialSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sky & Horizon -->
          <rect x="0" y="240" width="500" height="80" fill="#0b1329"/>
          
          <!-- Sun Position -->
          <circle id="dialSun" cx="350" cy="70" r="18" fill="#f59e0b"/>
          <text id="dialSunLabel" x="350" y="45" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Sun (2:00 PM)</text>

          <!-- 3D Isometric View of Samrat Yantra -->
          <!-- Triangular Gnomon (Tilted at 26.9° for Jaipur Latitude) -->
          <polygon points="170,240 250,90 250,240" fill="#d97706" stroke="#b45309" stroke-width="2"/>
          <text x="200" y="180" fill="#ffffff" font-size="8.5" font-weight="700">GNOMON (27m)</text>

          <!-- Curved Marble Quadrants -->
          <path d="M 120 240 Q 180 200 250 240 Q 320 200 380 240" fill="none" stroke="#e2e8f0" stroke-width="8"/>
          <text x="130" y="235" fill="#94a3b8" font-size="7">Morning Scale</text>
          <text x="360" y="235" fill="#94a3b8" font-size="7">Afternoon Scale</text>

          <!-- Cast Shadow of Gnomon -->
          <polygon id="gnomonShadow" points="250,90 250,240 310,240" fill="rgba(15, 23, 42, 0.75)"/>

          <!-- Readout Card -->
          <rect x="25" y="250" width="450" height="60" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8"/>
          <text id="dialSolarTime" x="45" y="272" fill="#38bdf8" font-size="12" font-weight="700">Local Solar Time: 02:00 PM (14:00)</text>
          <text x="45" y="292" fill="#cbd5e1" font-size="9.5">Built by Sawai Jai Singh II (1734 CE) • Gnomon shadow moves at 1 mm/sec to measure time to 2 seconds!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">☀️ Solar Hour of the Day (06:00 to 18:00):</span>
          <span id="dialHourVal" class="control-value">${solarHour}:00</span>
        </div>
        <input type="range" id="sliderDialHour" class="sim-slider" min="6" max="18" step="0.5" value="${solarHour}">
      `;

      const slider = document.getElementById('sliderDialHour');
      const valLabel = document.getElementById('dialHourVal');
      const sun = document.getElementById('dialSun');
      const sunLabel = document.getElementById('dialSunLabel');
      const shadow = document.getElementById('gnomonShadow');
      const timeText = document.getElementById('dialSolarTime');

      function updateDial(hr) {
        solarHour = hr;
        const frac = (hr - 6) / 12; // 0 to 1
        const sunX = 80 + 340 * frac;
        const sunY = 140 - 80 * Math.sin(frac * Math.PI);
        sun.setAttribute('cx', sunX);
        sun.setAttribute('cy', sunY);

        const intHr = Math.floor(hr);
        const mn = (hr % 1) * 60;
        const ampm = hr >= 12 ? 'PM' : 'AM';
        const displayHr = intHr > 12 ? intHr - 12 : intHr;
        const timeStr = `${displayHr}:${mn === 0 ? '00' : '30'} ${ampm}`;

        valLabel.textContent = `${timeStr} (Local Solar Time)`;
        sunLabel.setAttribute('x', sunX);
        sunLabel.setAttribute('y', sunY - 18);
        sunLabel.textContent = `Sun (${timeStr})`;
        timeText.textContent = `Local Solar Time: ${timeStr} (Shadow precision: 2 sec)`;

        // Shadow moves opposite to sun
        const shadowTipX = 250 + (hr - 12) * 22;
        shadow.setAttribute('points', `250,90 250,240 ${shadowTipX},240`);
      }

      slider.addEventListener('input', (e) => updateDial(parseFloat(e.target.value)));
      updateDial(solarHour);
    }

    // Initialize Page
    window.addEventListener('DOMContentLoaded', () => {
      initJumpSelector();
      goToSlide(0);
    });
  </script>
</body>
</html>
"""

# Replace placeholders
rendered_html = HTML_CONTENT.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-astronomy-calendars.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print(f"Successfully generated {output_path} ({len(rendered_html)} bytes).")

