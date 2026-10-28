# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-nature-harmony.html
Class 8 Science - Chapter 12: How Nature Works in Harmony
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Prof. Ramdeo Misra)
- 16 bespoke interactive SVG simulators with live ecological mechanisms, food webs, and animations
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
from class8_science_nature_harmony_data import SLIDES_DATA, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 12: How Nature Works in Harmony Master Lab</title>
  
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
      --bg-primary: #061109;
      --bg-secondary: #0a1f11;
      --card-bg: rgba(10, 31, 17, 0.92);
      --card-border: rgba(52, 211, 153, 0.28);
      --accent-emerald: #10b981;
      --accent-green: #22c55e;
      --accent-amber: #f59e0b;
      --accent-sky: #38bdf8;
      --accent-lime: #a3e635;
      --accent-rose: #f43f5e;
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
      background: radial-gradient(circle at 50% 20%, #0d2e18 0%, var(--bg-primary) 85%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Top Navigation Header */
    .header {
      background: rgba(6, 17, 9, 0.88);
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
      background: linear-gradient(135deg, #065f46, #059669);
      color: #ecfdf5;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border: 1px solid rgba(52, 211, 153, 0.4);
    }

    .chapter-title {
      font-size: 1.05rem;
      font-weight: 700;
      background: linear-gradient(to right, #a7f3d0, #34d399, #10b981);
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
      background: linear-gradient(90deg, #10b981, #34d399);
      width: 5%;
      transition: width 0.3s ease;
    }

    .slide-counter {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent-emerald);
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
      background: linear-gradient(135deg, rgba(6, 30, 16, 0.95), rgba(6, 78, 59, 0.35));
      border: 1px solid rgba(52, 211, 153, 0.35);
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
      background: radial-gradient(circle at 35% 35%, #059669, #022c22);
      border: 2px solid var(--accent-emerald);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
      transition: transform 0.3s;
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 2px solid #10b981;
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
      color: #6ee7b7;
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
      background: rgba(6, 78, 59, 0.6);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: #6ee7b7;
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
      background: rgba(16, 185, 129, 0.8);
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
      color: #34d399;
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
      background: rgba(6, 26, 14, 0.6);
      border-left: 3px solid #10b981;
      border-radius: 0 8px 8px 0;
      padding: 0.7rem 0.9rem;
    }

    .concept-point-title {
      font-weight: 700;
      color: #a7f3d0;
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
      color: #6ee7b7;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .checkpoint-box {
      background: rgba(6, 26, 14, 0.75);
      border: 1px solid rgba(52, 211, 153, 0.2);
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
      background: rgba(15, 45, 24, 0.6);
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
      background: rgba(16, 185, 129, 0.25);
      border-color: rgba(52, 211, 153, 0.4);
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
      color: #6ee7b7;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .sim-canvas-container {
      flex: 1;
      min-height: 340px;
      background: radial-gradient(circle at 50% 50%, #0c2b16 0%, #041007 100%);
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
      background: rgba(6, 26, 14, 0.55);
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
      color: #34d399;
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
      background: #10b981;
      cursor: pointer;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
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
      background: rgba(15, 45, 24, 0.7);
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
      background: rgba(16, 185, 129, 0.3);
      border-color: rgba(52, 211, 153, 0.5);
    }

    .sim-toggle-btn.active {
      background: linear-gradient(135deg, #059669, #10b981);
      border-color: #6ee7b7;
      color: #ffffff;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
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
      background: rgba(6, 26, 14, 0.65);
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
      background: rgba(15, 45, 24, 0.6);
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
      background: rgba(16, 185, 129, 0.25);
      border-color: rgba(52, 211, 153, 0.4);
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
      background: rgba(4, 16, 7, 0.8);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-content-card {
      background: #082412;
      border: 1px solid #10b981;
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
      color: #a7f3d0;
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
      background: rgba(6, 26, 14, 0.6);
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }

    .modal-solution-steps {
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.55;
      white-space: pre-line;
      background: rgba(6, 26, 14, 0.4);
      padding: 1rem;
      border-radius: 8px;
      border-left: 3px solid #10b981;
    }

    /* Bottom Navigation Bar */
    .bottom-nav {
      background: rgba(6, 17, 9, 0.88);
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
      background: linear-gradient(135deg, #065f46, #059669);
      border: 1px solid rgba(52, 211, 153, 0.4);
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
      background: linear-gradient(135deg, #059669, #10b981);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
    }

    .nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }

    .jump-selector {
      background: rgba(6, 26, 14, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #a7f3d0;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }

    .jump-selector option {
      background: #061109;
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
      <span class="badge-chapter">NCERT Class 8 Science • Ch 12</span>
      <h1 class="chapter-title">How Nature Works in Harmony Master Lab</h1>
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
          <!-- Stylized Ecologist Avatar SVG -->
          <svg width="44" height="44" viewBox="0 0 100 100" fill="none">
            <!-- Background circle aura -->
            <circle cx="50" cy="50" r="45" fill="#065f46"/>
            <!-- Head & hair -->
            <circle cx="50" cy="42" r="20" fill="#fde68a"/>
            <path d="M30 38 C30 18 70 18 70 38 C70 28 65 22 50 22 C35 22 30 28 30 38 Z" fill="#94a3b8"/>
            <!-- Glasses / Naturalist Eyes -->
            <rect x="36" y="38" width="11" height="7" rx="2" stroke="#34d399" stroke-width="2" fill="none"/>
            <rect x="53" y="38" width="11" height="7" rx="2" stroke="#34d399" stroke-width="2" fill="none"/>
            <line x1="47" y1="41" x2="53" y2="41" stroke="#34d399" stroke-width="2"/>
            <!-- Smile / speaking mouth -->
            <path id="avatarMouth" d="M45 53 Q50 57 55 53" stroke="#b45309" stroke-width="2" fill="none"/>
            <!-- Shoulders / Safari Academic Coat -->
            <path d="M22 84 C22 66 36 62 50 62 C64 62 78 66 78 84 Z" fill="#1e293b"/>
            <!-- Binoculars strap -->
            <path d="M38 62 L48 76 L52 76 L62 62" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="speech-content">
        <div class="teacher-name-tag">
          <span>Prof. Ramdeo Misra</span>
          <span style="font-size: 0.72rem; color: #34d399; font-weight: 500;">• Father of Indian Ecology & Naturalist</span>
        </div>
        <p id="speechBubbleText" class="speech-bubble-text">
          Loading ecology lesson...
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
          <span id="slideTag" class="slide-badge">12.1 Interpreting Surroundings</span>
          <h2 id="slideTitle" class="slide-heading">Experiencing Our Natural Surroundings</h2>
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
          <span id="factText">Ecology fact loading...</span>
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
            <svg id="simIcon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            </svg>
            <span id="simHeaderTitle">Ecological Systems Simulator</span>
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
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2);
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
        osc.frequency.setValueAtTime(700, now);
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
    let quizScores = {};
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
      
      const cleanText = text.replace(/\$/g, '').replace(/\+/g, ' plus ');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 1.0;
      speechUtterance.pitch = 1.0;

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

      prevBtn.disabled = (currentSlideIdx === 0);

      // Slide 20 Terminal Rule: Hide Next Button, Show Notice
      if (currentSlideIdx === totalSlides - 1) {
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

        factText.textContent = slide.fact || '';

        if (slide.checkpoints && slide.checkpoints.length >= 2) {
          renderCheckpoint(0, slide.checkpoints[0], chk1Question, chk1Options, chk1Feedback);
          renderCheckpoint(1, slide.checkpoints[1], chk2Question, chk2Options, chk2Feedback);
        }

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
        case 'biotic_abiotic_sim':
          simBioticAbiotic();
          break;
        case 'interdependence_sim':
          simInterdependence();
          break;
        case 'ecological_hierarchy_sim':
          simEcologicalHierarchy();
          break;
        case 'habitat_niche_sim':
          simHabitatNiche();
          break;
        case 'keystone_species_sim':
          simKeystoneSpecies();
          break;
        case 'biodiversity_resilience_sim':
          simBiodiversityResilience();
          break;
        case 'mutualism_sim':
          simMutualism();
          break;
        case 'symbiotic_spectrum_sim':
          simSymbioticSpectrum();
          break;
        case 'food_chain_energy_sim':
          simFoodChainEnergy();
          break;
        case 'food_web_interactive_sim':
          simFoodWebInteractive();
          break;
        case 'decomposers_recycling_sim':
          simDecomposersRecycling();
          break;
        case 'nutrient_cycles_sim':
          simNutrientCycles();
          break;
        case 'trophic_cascade_sim':
          simTrophicCascade();
          break;
        case 'ecological_succession_sim':
          simEcologicalSuccession();
          break;
        case 'predator_prey_balance_sim':
          simPredatorPreyBalance();
          break;
        case 'ecosystem_services_sim':
          simEcosystemServices();
          break;
        default:
          simCanvas.innerHTML = '<div style="color: #94a3b8; padding: 2rem;">Simulator loading...</div>';
      }
    }

    // 1. Biotic & Abiotic Components Simulator
    function simBioticAbiotic() {
      simHeaderTitle.textContent = "Biotic vs. Abiotic Component Filter";
      let filterMode = "all";

      simCanvas.innerHTML = `
        <svg id="bioAbioSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sky & Abiotic Sun -->
          <rect x="0" y="0" width="500" height="180" fill="#0c1d2e"/>
          
          <!-- Sun (Abiotic) -->
          <g id="abioSun" class="abio-elem">
            <circle cx="80" cy="50" r="28" fill="#f59e0b"/>
            <line x1="80" y1="50" x2="200" y2="150" stroke="#fde047" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
            <line x1="80" y1="50" x2="120" y2="200" stroke="#fde047" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
            <text x="80" y="95" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Sunlight (Abiotic)</text>
          </g>

          <!-- Mountain & Soil Layers (Abiotic) -->
          <g id="abioSoil" class="abio-elem">
            <polygon points="180,180 260,70 340,180" fill="#334155"/>
            <rect x="0" y="180" width="500" height="140" fill="#1e180e"/>
            <text x="50" y="295" fill="#a16207" font-size="10" font-weight="700">Soil Minerals & Rock (Abiotic)</text>
          </g>

          <!-- River Stream (Abiotic Water) -->
          <g id="abioWater" class="abio-elem">
            <path d="M 340 180 Q 300 240 370 320 L 460 320 Q 380 240 400 180 Z" fill="#0284c7"/>
            <text x="430" y="270" fill="#bae6fd" font-size="9.5" font-weight="700">Water (Abiotic)</text>
          </g>

          <!-- Forest Trees (Biotic) -->
          <g id="bioTrees" class="bio-elem">
            <!-- Tree 1 -->
            <rect x="95" y="140" width="16" height="50" fill="#78350f"/>
            <circle cx="103" cy="130" r="35" fill="#15803d"/>
            <circle cx="90" cy="115" r="25" fill="#16a34a"/>
            <text x="103" y="135" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">Trees</text>

            <!-- Tree 2 -->
            <rect x="175" y="150" width="12" height="40" fill="#78350f"/>
            <circle cx="181" cy="140" r="28" fill="#15803d"/>
          </g>

          <!-- Animals (Biotic) -->
          <g id="bioAnimals" class="bio-elem">
            <!-- Spotted Deer -->
            <ellipse cx="230" cy="220" rx="18" ry="12" fill="#d97706"/>
            <circle cx="245" cy="210" r="7" fill="#d97706"/>
            <line x1="220" y1="230" x2="220" y2="250" stroke="#d97706" stroke-width="2.5"/>
            <line x1="240" y1="230" x2="240" y2="250" stroke="#d97706" stroke-width="2.5"/>
            <text x="230" y="265" fill="#fef08a" font-size="9" font-weight="700" text-anchor="middle">Deer (Biotic)</text>

            <!-- Fish in River -->
            <ellipse cx="365" cy="240" rx="8" ry="4" fill="#f97316"/>
            <polygon points="357,240 352,236 352,244" fill="#f97316"/>
            <text x="365" y="255" fill="#ffffff" font-size="8" text-anchor="middle">Fish</text>
          </g>

          <!-- Soil Microorganisms (Biotic) -->
          <g id="bioMicrobes" class="bio-elem">
            <circle cx="120" cy="230" r="3" fill="#a3e635"/>
            <circle cx="135" cy="245" r="4" fill="#a3e635"/>
            <circle cx="110" cy="255" r="3" fill="#a3e635"/>
            <text x="120" y="275" fill="#bef264" font-size="8" text-anchor="middle">Microbes & Fungi</text>
          </g>

          <!-- Overlay readout -->
          <rect x="20" y="10" width="460" height="35" rx="6" fill="rgba(6, 26, 14, 0.85)" stroke="rgba(52, 211, 153, 0.3)"/>
          <text id="bioStatusText" x="250" y="32" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Mode: Full Ecosystem (Biotic Organisms + Abiotic Environment)</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-m="all">🌿 Full Integrated Landscape</button>
          <button class="sim-toggle-btn" data-m="biotic">🐾 Isolate BIOTIC Factors (Living)</button>
          <button class="sim-toggle-btn" data-m="abiotic">☀️ Isolate ABIOTIC Factors (Physical)</button>
        </div>
      `;

      const status = document.getElementById('bioStatusText');
      const bioElems = simCanvas.querySelectorAll('.bio-elem');
      const abioElems = simCanvas.querySelectorAll('.abio-elem');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateFilter(m) {
        filterMode = m;
        btns.forEach(b => b.classList.toggle('active', b.dataset.m === m));

        if (m === 'all') {
          bioElems.forEach(el => el.style.opacity = '1');
          abioElems.forEach(el => el.style.opacity = '1');
          status.textContent = "Mode: Full Ecosystem (Biotic Organisms + Abiotic Physical Surroundings)";
          status.setAttribute('fill', '#34d399');
        } else if (m === 'biotic') {
          bioElems.forEach(el => el.style.opacity = '1');
          abioElems.forEach(el => el.style.opacity = '0.15');
          status.textContent = "BIOTIC Only: Trees, Deer, Fish, Soil Microbes & Fungi (All living organisms)";
          status.setAttribute('fill', '#a7f3d0');
        } else {
          bioElems.forEach(el => el.style.opacity = '0.15');
          abioElems.forEach(el => el.style.opacity = '1');
          status.textContent = "ABIOTIC Only: Solar Light, Ambient Temperature, River Water, Soil Minerals & Air";
          status.setAttribute('fill', '#38bdf8');
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateFilter(b.dataset.m)));
      updateFilter(filterMode);
    }

    // 2. Interdependence & Microclimate Simulator
    function simInterdependence() {
      simHeaderTitle.textContent = "Banyan Tree Ecological Exchange & Microclimate Machine";
      let isForested = true;

      simCanvas.innerHTML = `
        <svg id="interdepSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Sky -->
          <rect id="interSky" x="0" y="0" width="500" height="200" fill="#0f291e"/>

          <!-- Soil Base -->
          <rect id="interSoil" x="0" y="200" width="500" height="120" fill="#1c1917"/>

          <!-- Banyan Tree Group -->
          <g id="interTreeGrp">
            <!-- Roots in soil -->
            <path d="M 230 200 Q 180 260 140 280 M 250 200 Q 250 270 240 300 M 270 200 Q 310 250 360 280" stroke="#78350f" stroke-width="4" fill="none"/>
            <!-- Aerial Prop Roots -->
            <line x1="160" y1="130" x2="160" y2="200" stroke="#92400e" stroke-width="3"/>
            <line x1="340" y1="130" x2="340" y2="200" stroke="#92400e" stroke-width="3"/>
            <!-- Trunk -->
            <rect x="235" y="120" width="30" height="85" fill="#78350f"/>
            <!-- Giant Canopy -->
            <ellipse cx="250" cy="95" rx="120" ry="55" fill="#15803d"/>
            <ellipse cx="210" cy="80" rx="70" ry="40" fill="#16a34a"/>
            <ellipse cx="290" cy="80" rx="70" ry="40" fill="#16a34a"/>
          </g>

          <!-- Dynamic Ecological Exchange Arrows -->
          <g id="interExchangeArrows">
            <!-- Sun input -->
            <path d="M 60 40 L 160 70" stroke="#fde047" stroke-width="2.5" marker-end="url(#arrow)"/>
            <text x="80" y="35" fill="#fde047" font-size="9" font-weight="700">Sunlight (Photosynthesis)</text>

            <!-- CO2 intake -->
            <path d="M 380 40 L 320 70" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="3 2"/>
            <text x="360" y="35" fill="#cbd5e1" font-size="9">CO₂ Absorbed</text>

            <!-- O2 & Transpiration cooling output -->
            <path d="M 250 40 Q 250 15 280 15" stroke="#34d399" stroke-width="2"/>
            <text x="250" y="25" fill="#6ee7b7" font-size="9" font-weight="700" text-anchor="middle">O₂ Released + 400L Transpiration Vapor</text>

            <!-- Water & mineral absorption from roots -->
            <path d="M 140 280 L 230 200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
            <text x="130" y="260" fill="#38bdf8" font-size="9">Water & Minerals</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="interCardTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Healthy Forest: Robust Soil Conservation & Microclimate</text>
          <text id="interCardDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Extensive roots lock soil grains against heavy monsoons; transpiration cools local air by 3–5°C.</text>
          <text id="interCardSub" x="45" y="296" fill="#fde047" font-size="9.5">Fallen leaf litter breaks down into rich organic humus, recharging groundwater.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnForested" class="sim-toggle-btn active">🌳 Healthy Forested State (Root Binding & Cooling)</button>
          <button id="btnDeforested" class="sim-toggle-btn">⚠️ Deforested Hillside (Severe Soil Erosion)</button>
        </div>
      `;

      const tree = document.getElementById('interTreeGrp');
      const arrows = document.getElementById('interExchangeArrows');
      const sky = document.getElementById('interSky');
      const soil = document.getElementById('interSoil');
      const title = document.getElementById('interCardTitle');
      const desc = document.getElementById('interCardDesc');
      const sub = document.getElementById('interCardSub');
      const btnF = document.getElementById('btnForested');
      const btnD = document.getElementById('btnDeforested');

      function updateInter(isF) {
        isForested = isF;
        btnF.classList.toggle('active', isF);
        btnD.classList.toggle('active', !isF);

        if (isF) {
          tree.style.display = 'block';
          arrows.style.display = 'block';
          sky.setAttribute('fill', '#0f291e');
          soil.setAttribute('fill', '#1c1917');
          title.textContent = "Healthy Forest: Robust Soil Conservation & Microclimate";
          title.setAttribute('fill', '#34d399');
          desc.textContent = "Extensive roots lock soil grains against heavy monsoons; transpiration cools local air by 3–5°C.";
          sub.textContent = "Fallen leaf litter breaks down into rich organic humus, recharging groundwater.";
        } else {
          tree.style.display = 'none';
          arrows.style.display = 'none';
          sky.setAttribute('fill', '#331e10'); // Harsh scorching sun
          soil.setAttribute('fill', '#78350f'); // Eroded gullying dirt
          title.textContent = "⚠️ Deforested State: Rapid Topsoil Erosion & Microclimate Collapse";
          title.setAttribute('fill', '#f43f5e');
          desc.textContent = "Without protective canopy and root tensile network, monsoon rain strips away fertile topsoil.";
          sub.textContent = "Ground temperature surges, moisture evaporates instantly, and flash flooding devastates valleys.";
        }
      }

      btnF.addEventListener('click', () => updateInter(true));
      btnD.addEventListener('click', () => updateInter(false));
      updateInter(isForested);
    }

    // 3. Nested Ecological Hierarchy Simulator
    function simEcologicalHierarchy() {
      simHeaderTitle.textContent = "Nested Ecological Hierarchy (Organism ➔ Biosphere)";
      let hierLevel = 3; // Community initially

      const levels = [
        { name: "Level 1: Organism", title: "Single Individual Entity", desc: "One Bengal Tiger roaming the forest floor.", color: "#f59e0b" },
        { name: "Level 2: Population", title: "Same Species Assemblage", desc: "All Bengal Tigers coexisting and breeding in Jim Corbett National Park.", color: "#f97316" },
        { name: "Level 3: Biological Community", title: "Interacting Multi-Species Assemblage", desc: "Tigers, spotted deer, wild boars, peacocks, sal trees, grass, and soil fungi sharing the habitat.", color: "#10b981" },
        { name: "Level 4: Ecosystem", title: "Community + Abiotic Environment", desc: "The biological community interacting with river hydrology, soil minerals, sunlight, and air.", color: "#06b6d4" },
        { name: "Level 5: Biosphere", title: "Global Planetary Sum", desc: "The entire living planetary zone of Earth where life flourishes, from deep oceans to high atmosphere.", color: "#3b82f6" }
      ];

      simCanvas.innerHTML = `
        <svg id="hierSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Concentric Russian Doll Circles -->
          <!-- Level 5: Biosphere -->
          <circle cx="250" cy="140" r="115" fill="none" stroke="#3b82f6" stroke-width="4" stroke-dasharray="6 3" opacity="0.3"/>
          
          <!-- Level 4: Ecosystem -->
          <circle cx="250" cy="140" r="92" fill="none" stroke="#06b6d4" stroke-width="4" opacity="0.4"/>

          <!-- Level 3: Community -->
          <circle cx="250" cy="140" r="68" fill="none" stroke="#10b981" stroke-width="4" opacity="0.6"/>

          <!-- Level 2: Population -->
          <circle cx="250" cy="140" r="44" fill="none" stroke="#f97316" stroke-width="4" opacity="0.75"/>

          <!-- Level 1: Organism -->
          <circle cx="250" cy="140" r="22" fill="#f59e0b"/>
          <text x="250" y="144" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">🐅</text>

          <!-- Dynamic Highlight Ring -->
          <circle id="hierHighlight" cx="250" cy="140" r="68" fill="rgba(16, 185, 129, 0.15)" stroke="#6ee7b7" stroke-width="3"/>

          <!-- Readout Card -->
          <rect x="25" y="240" width="450" height="70" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="hierLevelName" x="45" y="262" fill="#34d399" font-size="12" font-weight="700">Level 3: Biological Community</text>
          <text id="hierLevelDesc" x="45" y="282" fill="#cbd5e1" font-size="10.5">Tigers, spotted deer, wild boars, sal trees, and soil fungi sharing the habitat.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">🔍 Zoom Hierarchy Level:</span>
          <span id="hierValLabel" class="control-value">Community (Level 3)</span>
        </div>
        <input type="range" id="sliderHier" class="sim-slider" min="1" max="5" value="${hierLevel}">
        <div class="sim-btn-group" style="justify-content: center; margin-top: 0.5rem;">
          <button class="sim-toggle-btn" data-l="1">Organism</button>
          <button class="sim-toggle-btn" data-l="2">Population</button>
          <button class="sim-toggle-btn active" data-l="3">Community</button>
          <button class="sim-toggle-btn" data-l="4">Ecosystem</button>
          <button class="sim-toggle-btn" data-l="5">Biosphere</button>
        </div>
      `;

      const slider = document.getElementById('sliderHier');
      const valLabel = document.getElementById('hierValLabel');
      const ring = document.getElementById('hierHighlight');
      const lName = document.getElementById('hierLevelName');
      const lDesc = document.getElementById('hierLevelDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateHier(lvl) {
        hierLevel = lvl;
        slider.value = lvl;
        valLabel.textContent = levels[lvl - 1].name;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.l) === lvl));

        const rValues = [22, 44, 68, 92, 115];
        const curR = rValues[lvl - 1];
        ring.setAttribute('r', curR);
        ring.setAttribute('stroke', levels[lvl - 1].color);

        lName.textContent = `${levels[lvl - 1].name} — ${levels[lvl - 1].title}`;
        lName.setAttribute('fill', levels[lvl - 1].color);
        lDesc.textContent = levels[lvl - 1].desc;
      }

      slider.addEventListener('input', (e) => updateHier(parseInt(e.target.value)));
      btns.forEach(b => b.addEventListener('click', () => updateHier(parseInt(b.dataset.l))));
      updateHier(hierLevel);
    }

    // 4. Habitat vs. Ecological Niche Partitioning Simulator
    function simHabitatNiche() {
      simHeaderTitle.textContent = "Tree Habitat & Niche Partitioning Multi-Story Explorer";
      let selectedNiche = "canopy";

      const nicheData = {
        canopy: {
          title: "High Canopy Niche (Sunbirds & Flycatchers)",
          zone: "Top foliage exposed to full tropical sunlight",
          role: "Sip floral nectar and catch airborne flying insects; perform critical cross-pollination.",
          yPos: 65,
          color: "#f59e0b"
        },
        middle: {
          title: "Mid-Story Niche (Langurs & Fruit Bats)",
          zone: "Dense branches with shelter from raptors",
          role: "Consume ripe wild figs and tender shoots; disperse undigested seeds across the forest.",
          yPos: 125,
          color: "#10b981"
        },
        trunk: {
          title: "Trunk & Bark Niche (Woodpeckers & Tree Creepers)",
          zone: "Vertical bark fissures and wood channels",
          role: "Drill into dead wood to extract destructive wood-boring beetle larvae, protecting tree health.",
          yPos: 175,
          color: "#06b6d4"
        },
        floor: {
          title: "Forest Floor Niche (Earthworms & Spotted Deer)",
          zone: "Humus layer, leaf litter, and subterranean root zone",
          role: "Browse fallen leaves and fruits; earthworms digest and aerate decaying detritus.",
          yPos: 220,
          color: "#a3e635"
        }
      };

      simCanvas.innerHTML = `
        <svg id="nicheSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Multi-story Tree Graphic -->
          <rect x="235" y="100" width="30" height="130" fill="#78350f"/>
          <ellipse cx="250" cy="70" rx="130" ry="45" fill="#15803d"/>
          <ellipse cx="250" cy="120" rx="100" ry="35" fill="#16a34a"/>
          <rect x="0" y="230" width="500" height="90" fill="#1e180e"/>

          <!-- Target Highlight Pointer -->
          <g id="nicheTargetPointer" transform="translate(250, 65)">
            <circle cx="0" cy="0" r="24" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4 2"/>
            <circle cx="0" cy="0" r="5" fill="#f59e0b"/>
          </g>

          <!-- Shared Habitat Banner -->
          <text x="25" y="30" fill="#94a3b8" font-size="10" font-weight="700">SHARED HABITAT: Ancient Sal Forest Tree</text>

          <!-- Readout Box -->
          <rect x="25" y="240" width="450" height="70" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="nicheTitleText" x="45" y="262" fill="#f59e0b" font-size="12" font-weight="700">High Canopy Niche (Sunbirds)</text>
          <text id="nicheDescText" x="45" y="282" fill="#cbd5e1" font-size="10.5">Sip floral nectar and catch airborne flying insects; cross-pollinates canopy flowers.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-n="canopy">🌺 High Canopy (Sunbirds)</button>
          <button class="sim-toggle-btn" data-n="middle">🐒 Mid-Story (Langurs/Bats)</button>
          <button class="sim-toggle-btn" data-n="trunk">🪵 Tree Trunk (Woodpeckers)</button>
          <button class="sim-toggle-btn" data-n="floor">🪱 Forest Floor (Earthworms)</button>
        </div>
      `;

      const ptr = document.getElementById('nicheTargetPointer');
      const nTitle = document.getElementById('nicheTitleText');
      const nDesc = document.getElementById('nicheDescText');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateNiche(k) {
        selectedNiche = k;
        btns.forEach(b => b.classList.toggle('active', b.dataset.n === k));
        const d = nicheData[k];
        ptr.setAttribute('transform', `translate(250, ${d.yPos})`);
        ptr.querySelector('circle').setAttribute('stroke', d.color);
        ptr.querySelectorAll('circle')[1].setAttribute('fill', d.color);

        nTitle.textContent = d.title;
        nTitle.setAttribute('fill', d.color);
        nDesc.textContent = `${d.zone} • ${d.role}`;
      }

      btns.forEach(b => b.addEventListener('click', () => updateNiche(b.dataset.n)));
      updateNiche(selectedNiche);
    }

    // 5. Keystone Species: Sea Otter & Kelp Barrens
    function simKeystoneSpecies() {
      simHeaderTitle.textContent = "Keystone Species: Sea Otter & Kelp Forest Balance";
      let ottersPresent = true;

      simCanvas.innerHTML = `
        <svg id="keystoneSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Ocean Background -->
          <rect x="0" y="0" width="500" height="320" fill="#042f2e"/>
          
          <!-- Kelp Forest Group -->
          <g id="kelpForestGrp">
            <!-- Giant Kelp fronds -->
            <path d="M 80 320 Q 90 200 60 80 Q 90 140 100 320" fill="#15803d"/>
            <path d="M 140 320 Q 120 180 150 60 Q 170 160 160 320" fill="#16a34a"/>
            <path d="M 220 320 Q 240 190 210 50 Q 250 150 240 320" fill="#15803d"/>
            <path d="M 320 320 Q 300 170 340 70 Q 350 180 340 320" fill="#16a34a"/>
            <path d="M 420 320 Q 430 190 400 60 Q 440 150 440 320" fill="#15803d"/>
          </g>

          <!-- Sea Urchins Group -->
          <g id="seaUrchinsGrp" transform="translate(0, 270)">
            <!-- Few urchins if otters present, hordes if otters absent -->
            <circle cx="90" cy="30" r="9" fill="#9333ea"/>
            <circle cx="230" cy="30" r="9" fill="#9333ea"/>
            <circle cx="330" cy="30" r="9" fill="#9333ea"/>
            
            <!-- Extra urchins for overpopulation -->
            <g id="urchinOverpop" style="display: none;">
              <circle cx="60" cy="30" r="10" fill="#9333ea"/>
              <circle cx="120" cy="30" r="10" fill="#9333ea"/>
              <circle cx="150" cy="30" r="10" fill="#9333ea"/>
              <circle cx="190" cy="30" r="10" fill="#9333ea"/>
              <circle cx="270" cy="30" r="10" fill="#9333ea"/>
              <circle cx="370" cy="30" r="10" fill="#9333ea"/>
              <circle cx="410" cy="30" r="10" fill="#9333ea"/>
              <circle cx="450" cy="30" r="10" fill="#9333ea"/>
            </g>
          </g>

          <!-- Sea Otter (Keystone) Floating at Surface -->
          <g id="seaOtterGrp" transform="translate(250, 40)">
            <ellipse cx="0" cy="0" rx="22" ry="10" fill="#78350f"/>
            <circle cx="18" cy="-2" r="7" fill="#a16207"/>
            <text x="0" y="24" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Sea Otter (Keystone)</text>
          </g>

          <!-- Readout Banner -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="keyTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Healthy Keystone Balance: Sea Otters Present</text>
          <text id="keyDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Otters keep herbivorous urchins in check; giant kelp forest provides habitat for hundreds of fish species.</text>
          <text id="keySub" x="45" y="296" fill="#fde047" font-size="9.5">Result: High biodiversity, productive coastal carbon sink, and resilient marine life.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnOttersOn" class="sim-toggle-btn active">🦦 Keystone Otters Present (Healthy Kelp)</button>
          <button id="btnOttersOff" class="sim-toggle-btn">⚠️ Remove Otters (Urchin Barrens Collapse)</button>
        </div>
      `;

      const kelp = document.getElementById('kelpForestGrp');
      const otter = document.getElementById('seaOtterGrp');
      const urchins = document.getElementById('urchinOverpop');
      const title = document.getElementById('keyTitle');
      const desc = document.getElementById('keyDesc');
      const sub = document.getElementById('keySub');
      const btnOn = document.getElementById('btnOttersOn');
      const btnOff = document.getElementById('btnOttersOff');

      function updateOtters(on) {
        ottersPresent = on;
        btnOn.classList.toggle('active', on);
        btnOff.classList.toggle('active', !on);

        if (on) {
          otter.style.display = 'block';
          urchins.style.display = 'none';
          kelp.style.opacity = '1';
          title.textContent = "Healthy Keystone Balance: Sea Otters Present";
          title.setAttribute('fill', '#34d399');
          desc.textContent = "Otters keep herbivorous urchins in check; giant kelp forest provides habitat for hundreds of fish.";
          sub.textContent = "Result: High biodiversity, productive coastal carbon sink, and resilient marine life.";
        } else {
          otter.style.display = 'none';
          urchins.style.display = 'block';
          kelp.style.opacity = '0.08'; // Kelp devoured
          title.textContent = "⚠️ Ecosystem Collapse: 'Urchin Barren' Desert";
          title.setAttribute('fill', '#f43f5e');
          desc.textContent = "Without apex otters, sea urchin populations explode and hyper-graze all kelp holdfasts.";
          sub.textContent = "Result: Kelp forest vanishes, fish nurseries disappear, and the marine community collapses!";
        }
      }

      btnOn.addEventListener('click', () => updateOtters(true));
      btnOff.addEventListener('click', () => updateOtters(false));
      updateOtters(ottersPresent);
    }

    // 6. Biodiversity Resilience Stress-Test
    function simBiodiversityResilience() {
      simHeaderTitle.textContent = "Resilience Stress-Test: Monoculture vs. Biodiverse Forest";
      let stressInjected = false;

      simCanvas.innerHTML = `
        <svg id="resilienceSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Left Half: Monoculture Plantation -->
          <rect x="10" y="10" width="235" height="215" rx="8" fill="rgba(15, 23, 42, 0.6)" stroke="rgba(255, 255, 255, 0.1)"/>
          <text x="127" y="32" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">MONOCULTURE (Single Clone)</text>
          
          <g id="monoTrees">
            <!-- 4 identical cloned trees -->
            <rect x="40" y="100" width="8" height="30" fill="#78350f"/>
            <polygon class="mono-leaf" points="44,55 30,100 58,100" fill="#15803d"/>

            <rect x="90" y="100" width="8" height="30" fill="#78350f"/>
            <polygon class="mono-leaf" points="94,55 80,100 108,100" fill="#15803d"/>

            <rect x="140" y="100" width="8" height="30" fill="#78350f"/>
            <polygon class="mono-leaf" points="144,55 130,100 158,100" fill="#15803d"/>

            <rect x="190" y="100" width="8" height="30" fill="#78350f"/>
            <polygon class="mono-leaf" points="194,55 180,100 208,100" fill="#15803d"/>
          </g>
          <text id="monoScore" x="127" y="180" fill="#cbd5e1" font-size="10" font-weight="700" text-anchor="middle">Healthy: 100% Survival</text>

          <!-- Right Half: Natural Biodiverse Forest -->
          <rect x="255" y="10" width="235" height="215" rx="8" fill="rgba(15, 23, 42, 0.6)" stroke="rgba(52, 211, 153, 0.25)"/>
          <text x="372" y="32" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">BIODIVERSE FOREST (Mixed Species)</text>

          <g id="polyTrees">
            <!-- Oak Tree -->
            <rect x="280" y="110" width="8" height="30" fill="#78350f"/>
            <circle cx="284" cy="95" r="22" fill="#15803d"/>

            <!-- Pine Tree -->
            <rect x="330" y="100" width="8" height="35" fill="#78350f"/>
            <polygon points="334,55 320,100 348,100" fill="#166534"/>

            <!-- Flowering Neem -->
            <rect x="380" y="105" width="8" height="30" fill="#78350f"/>
            <ellipse cx="384" cy="90" rx="18" ry="24" fill="#10b981"/>

            <!-- Shrub Layer with Bees & Birds -->
            <circle cx="435" cy="120" r="14" fill="#84cc16"/>
          </g>
          <text id="polyScore" x="372" y="180" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Healthy: 100% Survival</text>

          <!-- Comparison Verdict Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="stressTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Baseline: Both ecosystems stable before environmental shock</text>
          <text id="stressDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Click 'Inject Pest / Drought Epidemic' below to test ecosystem resilience!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnInjectStress" class="sim-toggle-btn active">⚡ Inject Fungal Blight / Severe Drought</button>
          <button id="btnResetStress" class="sim-toggle-btn">🔄 Reset Ecosystem Health</button>
        </div>
      `;

      const monoLeaves = simCanvas.querySelectorAll('.mono-leaf');
      const monoScore = document.getElementById('monoScore');
      const polyScore = document.getElementById('polyScore');
      const title = document.getElementById('stressTitle');
      const desc = document.getElementById('stressDesc');

      document.getElementById('btnInjectStress').addEventListener('click', () => {
        stressInjected = true;
        // Monoculture completely succumbs
        monoLeaves.forEach(l => l.setAttribute('fill', '#991b1b')); // withered dead brown/red
        monoScore.textContent = "CRITICAL FAILURE: 0% Survival (Total Blight Wipeout)";
        monoScore.setAttribute('fill', '#ef4444');

        // Biodiverse forest survives
        polyScore.textContent = "RESILIENT: 85% Survival (Natural Predators & Resistance)";
        polyScore.setAttribute('fill', '#34d399');

        title.textContent = "Result: Genetic Monoculture Collapses vs. Biodiverse Forest Thrives";
        title.setAttribute('fill', '#f59e0b');
        desc.textContent = "Because the monoculture shared identical genes, one fungus killed all. The diverse forest had natural barriers and varied resistance!";
      });

      document.getElementById('btnResetStress').addEventListener('click', () => {
        stressInjected = false;
        monoLeaves.forEach(l => l.setAttribute('fill', '#15803d'));
        monoScore.textContent = "Healthy: 100% Survival";
        monoScore.setAttribute('fill', '#cbd5e1');
        polyScore.textContent = "Healthy: 100% Survival";
        polyScore.setAttribute('fill', '#34d399');
        title.textContent = "Baseline: Both ecosystems stable before environmental shock";
        title.setAttribute('fill', '#34d399');
        desc.textContent = "Click 'Inject Pest / Drought Epidemic' below to test ecosystem resilience!";
      });
    }

    // 7. Mutualism Explorer: Lichens, Mycorrhizae & Pollinators
    function simMutualism() {
      simHeaderTitle.textContent = "Mutualism (+/+): Win-Win Cooperation in Nature";
      let mode = "lichen";

      simCanvas.innerHTML = `
        <svg id="mutSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Lichen View Container -->
          <g id="lichenView">
            <!-- Bare Rock -->
            <rect x="60" y="160" width="380" height="60" fill="#334155" rx="6"/>
            <text x="250" y="195" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Bare Granite Rock Substrate</text>

            <!-- Fungal Hyphae Matrix (Shelter & Minerals) -->
            <path d="M 100 160 Q 120 110 160 160 Q 190 90 230 160 Q 280 100 320 160 Q 360 110 400 160" stroke="#fde047" stroke-width="8" fill="none" opacity="0.6"/>
            
            <!-- Green Algal Cells Embedded (Photobiont) -->
            <circle cx="150" cy="135" r="10" fill="#10b981"/>
            <circle cx="210" cy="120" r="10" fill="#10b981"/>
            <circle cx="270" cy="130" r="10" fill="#10b981"/>
            <circle cx="340" cy="135" r="10" fill="#10b981"/>

            <!-- Resource exchange badges -->
            <rect x="70" y="50" width="160" height="40" rx="6" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
            <text x="150" y="66" fill="#6ee7b7" font-size="9" font-weight="700" text-anchor="middle">Alga (Photobiont)</text>
            <text x="150" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Produces Sugars (Photosynthesis)</text>

            <rect x="270" y="50" width="160" height="40" rx="6" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b"/>
            <text x="350" y="66" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Fungus (Mycobiont)</text>
            <text x="350" y="80" fill="#cbd5e1" font-size="8" text-anchor="middle">Provides Water, Minerals & Shelter</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="mutTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Lichen: Masterwork Mutualism (+/+) between Fungus and Alga</text>
          <text id="mutDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Neither can survive alone on barren rock, but together they thrive across continents!</text>
          <text id="mutSub" x="45" y="296" fill="#fde047" font-size="9.5">Fungus absorbs moisture & etches minerals; alga feeds both with photosynthetic glucose.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-m="lichen">🪨 Lichen (Fungus + Alga)</button>
          <button class="sim-toggle-btn" data-m="bee">🐝 Pollinator (Bee + Apple Blossom)</button>
          <button class="sim-toggle-btn" data-m="coral">🪸 Coral Reef (Polyp + Zooxanthellae)</button>
        </div>
      `;

      const title = document.getElementById('mutTitle');
      const desc = document.getElementById('mutDesc');
      const sub = document.getElementById('mutSub');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateMut(m) {
        mode = m;
        btns.forEach(b => b.classList.toggle('active', b.dataset.m === m));

        if (m === 'lichen') {
          title.textContent = "Lichen: Masterwork Mutualism (+/+) between Fungus and Alga";
          desc.textContent = "Neither can survive alone on bare rock, but together they thrive across continents!";
          sub.textContent = "Fungus absorbs moisture & etches minerals; alga feeds both with photosynthetic glucose.";
        } else if (m === 'bee') {
          title.textContent = "Pollination: Honeybee & Flowering Plants (+/+)";
          desc.textContent = "Honeybee receives nutrient-rich sweet nectar and protein-packed pollen.";
          sub.textContent = "The plant achieves essential cross-pollination to fertilize seeds and produce fruit!";
        } else {
          title.textContent = "Coral Reef: Coral Animal Polyp & Zooxanthellae (+/+)";
          desc.textContent = "Microscopic algae living inside coral tissues furnish 90% of the animal's energy via sunlight.";
          sub.textContent = "The coral polyp provides mineral nutrients ($CO_2$, nitrogen) and calcium carbonate protection!";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateMut(b.dataset.m)));
      updateMut(mode);
    }

    // 8. Symbiotic Spectrum Dial (+/+, +/0, +/-, -/-)
    function simSymbioticSpectrum() {
      simHeaderTitle.textContent = "The Symbiotic Spectrum: From Mutualism to Parasitism";
      let interactionType = "parasitism";

      const data = {
        mutualism: {
          name: "Mutualism (+/+)",
          tag: "Both species derive distinct benefits",
          example: "Lichens (Fungus + Alga) & Mycorrhizal Plant Roots",
          effect: "Partner A: Benefit (+) • Partner B: Benefit (+)",
          color: "#34d399"
        },
        commensalism: {
          name: "Commensalism (+/0)",
          tag: "One species benefits; the other is unaffected",
          example: "Epiphytic Orchids on Mango Trees & Barnacles on Whales",
          effect: "Partner A: Benefit (+) • Partner B: No Effect (0)",
          color: "#38bdf8"
        },
        parasitism: {
          name: "Parasitism (+/-)",
          tag: "Parasite gains nutrients while harming the host",
          example: "Cuscuta (Amarbel) draining host trees with haustoria",
          effect: "Parasite: Benefit (+) • Host: Harmed & Stunted (-)",
          color: "#f43f5e"
        },
        competition: {
          name: "Competition (-/-)",
          tag: "Both contenders expend vital energy over scarce resources",
          example: "Two stags battling over territory or plants competing for canopy sunlight",
          effect: "Contender A: Depleted (-) • Contender B: Depleted (-)",
          color: "#f59e0b"
        }
      };

      simCanvas.innerHTML = `
        <svg id="specSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- 4 Quadrant Visual Wheel -->
          <g transform="translate(250, 120)">
            <circle cx="0" cy="0" r="85" fill="#062612" stroke="rgba(255, 255, 255, 0.15)" stroke-width="2"/>
            
            <!-- Dial Needle -->
            <line id="specNeedle" x1="0" y1="0" x2="0" y2="-65" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
            <circle cx="0" cy="0" r="8" fill="#ffffff"/>

            <!-- 4 Badges around perimeter -->
            <text x="0" y="-95" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Mutualism (+/+)</text>
            <text x="110" y="5" fill="#38bdf8" font-size="10" font-weight="700">Commensalism (+/0)</text>
            <text x="0" y="105" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Parasitism (+/-)</text>
            <text x="-110" y="5" fill="#f59e0b" font-size="10" font-weight="700" text-anchor="end">Competition (-/-)</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#f43f5e"/>
          <text id="specCardTitle" x="45" y="258" fill="#f43f5e" font-size="12.5" font-weight="700">Parasitism (+/-): Cuscuta (Amarbel) & Host Plant</text>
          <text id="specCardExample" x="45" y="278" fill="#cbd5e1" font-size="10.5">The non-green vine pierces host vessels with haustoria to steal water and sugars.</text>
          <text id="specCardEffect" x="45" y="296" fill="#fde047" font-size="9.5">Parasite: Benefit (+) • Host: Weakened & stunted (-)</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn" data-t="mutualism">💚 Mutualism (+/+)</button>
          <button class="sim-toggle-btn" data-t="commensalism">💙 Commensalism (+/0)</button>
          <button class="sim-toggle-btn active" data-t="parasitism">❤️ Parasitism (+/-)</button>
          <button class="sim-toggle-btn" data-t="competition">🧡 Competition (-/-)</button>
        </div>
      `;

      const needle = document.getElementById('specNeedle');
      const title = document.getElementById('specCardTitle');
      const ex = document.getElementById('specCardExample');
      const eff = document.getElementById('specCardEffect');
      const card = simCanvas.querySelector('rect[stroke="#f43f5e"]');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateSpec(t) {
        interactionType = t;
        btns.forEach(b => b.classList.toggle('active', b.dataset.t === t));
        const d = data[t];

        const angles = { mutualism: 0, commensalism: 90, parasitism: 180, competition: 270 };
        needle.setAttribute('transform', `rotate(${angles[t]})`);
        needle.setAttribute('stroke', d.color);

        title.textContent = `${d.name}: ${d.tag}`;
        title.setAttribute('fill', d.color);
        ex.textContent = `Example: ${d.example}`;
        eff.textContent = d.effect;
        card.setAttribute('stroke', d.color);
      }

      btns.forEach(b => b.addEventListener('click', () => updateSpec(b.dataset.t)));
      updateSpec(interactionType);
    }

    // 9. Lindeman's 10% Energy Transfer Law Simulator
    function simFoodChainEnergy() {
      simHeaderTitle.textContent = "Lindeman's 10% Law & Trophic Energy Dissipation";
      let solarInput = 10000; // Joules

      simCanvas.innerHTML = `
        <svg id="energySvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Funnel / Pyramidal Trophic Blocks -->
          <!-- Level 1: Producers (Grass) -->
          <rect x="80" y="180" width="340" height="35" rx="5" fill="#15803d"/>
          <text id="lblP1" x="250" y="202" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">1. PRODUCERS (Grass): 10,000 J (100%)</text>

          <!-- Level 2: Primary Consumers (Herbivores) -->
          <rect x="130" y="135" width="240" height="35" rx="5" fill="#16a34a"/>
          <text id="lblP2" x="250" y="157" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">2. HERBIVORES (Deer): 1,000 J (10%)</text>

          <!-- Level 3: Secondary Consumers (Carnivores) -->
          <rect x="180" y="90" width="140" height="35" rx="5" fill="#d97706"/>
          <text id="lblP3" x="250" y="112" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle">3. CARNIVORES: 100 J (1%)</text>

          <!-- Level 4: Apex Predator (Tiger) -->
          <rect x="215" y="45" width="70" height="35" rx="5" fill="#b91c1c"/>
          <text id="lblP4" x="250" y="67" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">4. APEX: 10 J</text>

          <!-- 90% Heat Dissipation Waves -->
          <path d="M 430 195 Q 460 185 490 195 M 380 150 Q 420 140 460 150 M 330 105 Q 370 95 410 105" stroke="#f43f5e" stroke-width="2" fill="none" stroke-dasharray="3 2"/>
          <text x="450" y="130" fill="#f43f5e" font-size="8.5" font-weight="700" text-anchor="middle">~90% Energy Lost as Heat</text>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="nrgCardTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Thermodynamic Limit: Why Apex Predators are Rare</text>
          <text id="nrgCardDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">With 90% dissipated in respiration and motion at each step, barely 0.1% reaches apex tigers.</text>
          <text x="45" y="296" fill="#fde047" font-size="9.5">This thermodynamic constraint strictly caps food chain length to 4 or 5 levels.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⚡ Solar Energy Trapped by Plants:</span>
          <span id="solarValLabel" class="control-value">${solarInput.toLocaleString()} Joules</span>
        </div>
        <input type="range" id="sliderSolar" class="sim-slider" min="5000" max="50000" step="1000" value="${solarInput}">
      `;

      const slider = document.getElementById('sliderSolar');
      const valLabel = document.getElementById('solarValLabel');
      const p1 = document.getElementById('lblP1');
      const p2 = document.getElementById('lblP2');
      const p3 = document.getElementById('lblP3');
      const p4 = document.getElementById('lblP4');

      function updateEnergy(j) {
        solarInput = j;
        valLabel.textContent = `${j.toLocaleString()} Joules`;
        const e2 = j * 0.1;
        const e3 = e2 * 0.1;
        const e4 = e3 * 0.1;

        p1.textContent = `1. PRODUCERS: ${j.toLocaleString()} J (100%)`;
        p2.textContent = `2. HERBIVORES: ${e2.toLocaleString()} J (10%)`;
        p3.textContent = `3. CARNIVORES: ${e3.toLocaleString()} J (1%)`;
        p4.textContent = `4. APEX: ${e4.toFixed(1)} J (0.1%)`;
      }

      slider.addEventListener('input', (e) => updateEnergy(parseInt(e.target.value)));
      updateEnergy(solarInput);
    }

    // 10. Interconnected Food Web & Redundancy Stability
    function simFoodWebInteractive() {
      simHeaderTitle.textContent = "Interconnected Food Web & Dietary Redundancy Stability";
      let rabbitDiseased = false;

      simCanvas.innerHTML = `
        <svg id="webSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Food Web Nodes -->
          <!-- Base: Grass (Producer) -->
          <circle cx="150" cy="240" r="22" fill="#15803d"/>
          <text x="150" y="244" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">Grass</text>

          <!-- Base: Berry Bush (Producer) -->
          <circle cx="350" cy="240" r="22" fill="#16a34a"/>
          <text x="350" y="244" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">Berries</text>

          <!-- Middle: Grasshopper -->
          <circle cx="80" cy="150" r="18" fill="#65a30d"/>
          <text x="80" y="154" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">Insect</text>

          <!-- Middle: Rabbit -->
          <circle id="nodeRabbit" cx="250" cy="150" r="20" fill="#a16207"/>
          <text id="nodeRabbitText" x="250" y="154" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">Rabbit</text>

          <!-- Middle: Field Mouse -->
          <circle cx="420" cy="150" r="18" fill="#78350f"/>
          <text x="420" y="154" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">Mouse</text>

          <!-- Top: Frog -->
          <circle cx="100" cy="65" r="18" fill="#059669"/>
          <text x="100" y="69" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">Frog</text>

          <!-- Top: Snake -->
          <circle cx="250" cy="65" r="18" fill="#d97706"/>
          <text x="250" y="69" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">Snake</text>

          <!-- Top: Hawk (Apex) -->
          <circle cx="400" cy="65" r="20" fill="#b91c1c"/>
          <text x="400" y="69" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">Hawk</text>

          <!-- Dynamic Linking Energy Lines -->
          <g id="webEnergyLines" stroke="#34d399" stroke-width="2" opacity="0.6">
            <line x1="150" y1="218" x2="80" y2="168"/>
            <line x1="150" y1="218" x2="250" y2="170"/>
            <line x1="350" y1="218" x2="250" y2="170"/>
            <line x1="350" y1="218" x2="420" y2="168"/>
            
            <line x1="80" y1="132" x2="100" y2="83"/>
            <line x1="100" y1="65" x2="232" y2="65"/>
            <line id="lineRabbitSnake" x1="250" y1="130" x2="250" y2="85"/>
            <line id="lineRabbitHawk" x1="250" y1="130" x2="400" y2="85"/>
            <line id="lineMouseHawk" x1="420" y1="132" x2="400" y2="85" stroke-width="2"/>
            <line x1="268" y1="65" x2="380" y2="65"/>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="240" width="450" height="70" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="webCardTitle" x="45" y="262" fill="#34d399" font-size="12" font-weight="700">Balanced Food Web: Multiple Feeding Channels</text>
          <text id="webCardDesc" x="45" y="282" fill="#cbd5e1" font-size="10.5">Click 'Simulate Disease Outbreak on Rabbits' below to witness food web resilience!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnDiseaseRabbit" class="sim-toggle-btn active">⚡ Simulate Viral Outbreak in Rabbits</button>
          <button id="btnResetRabbit" class="sim-toggle-btn">🔄 Restore Rabbit Population</button>
        </div>
      `;

      const rabbit = document.getElementById('nodeRabbit');
      const rText = document.getElementById('nodeRabbitText');
      const lRS = document.getElementById('lineRabbitSnake');
      const lRH = document.getElementById('lineRabbitHawk');
      const lMH = document.getElementById('lineMouseHawk');
      const title = document.getElementById('webCardTitle');
      const desc = document.getElementById('webCardDesc');

      document.getElementById('btnDiseaseRabbit').addEventListener('click', () => {
        rabbitDiseased = true;
        rabbit.setAttribute('fill', '#991b1b');
        rText.textContent = "Crash";
        lRS.style.opacity = '0.1';
        lRH.style.opacity = '0.1';
        lMH.setAttribute('stroke-width', '4'); // Hawk switches to mice

        title.textContent = "Food Web Resilience: Hawk & Snake Switch to Mice & Frogs!";
        title.setAttribute('fill', '#f59e0b');
        desc.textContent = "In an isolated food chain, predators would starve. In a Food Web, alternative prey prevents collapse!";
      });

      document.getElementById('btnResetRabbit').addEventListener('click', () => {
        rabbitDiseased = false;
        rabbit.setAttribute('fill', '#a16207');
        rText.textContent = "Rabbit";
        lRS.style.opacity = '0.6';
        lRH.style.opacity = '0.6';
        lMH.setAttribute('stroke-width', '2');

        title.textContent = "Balanced Food Web: Multiple Feeding Channels";
        title.setAttribute('fill', '#34d399');
        desc.textContent = "Click 'Simulate Viral Outbreak in Rabbits' below to witness food web resilience!";
      });
    }

    // 11. Decomposers & Nature's Zero-Waste Chamber
    function simDecomposersRecycling() {
      simHeaderTitle.textContent = "Decomposers: Nature's Closed-Loop Nutrient Recycling";
      let dayElapsed = 30;

      simCanvas.innerHTML = `
        <svg id="decompSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Soil Horizon -->
          <rect x="0" y="160" width="500" height="160" fill="#1c1917"/>
          <line x1="0" y1="160" x2="500" y2="160" stroke="#78350f" stroke-width="2"/>

          <!-- Organic Leaf Litter / Fallen Leaf -->
          <g id="decompLeafGrp" transform="translate(250, 150)">
            <ellipse id="decompLeaf" cx="0" cy="0" rx="60" ry="25" fill="#ca8a04"/>
            <line x1="-55" y1="0" x2="55" y2="0" stroke="#713f12" stroke-width="2"/>
          </g>

          <!-- Microscopic Decomposers (Fungal Hyphae & Soil Bacteria) -->
          <g id="decompMicrobes" transform="translate(250, 160)">
            <!-- Fungal mycelium threads -->
            <path d="M -40 0 Q -30 30 -50 50 M 0 0 Q 10 40 20 60 M 40 0 Q 30 30 50 50" stroke="#fef08a" stroke-width="2" fill="none" opacity="0.7"/>
            <!-- Bacterial colonies -->
            <circle cx="-25" cy="25" r="4" fill="#a3e635"/>
            <circle cx="15" cy="35" r="5" fill="#a3e635"/>
            <circle cx="35" cy="20" r="4" fill="#a3e635"/>
          </g>

          <!-- Mineral Ions Released into Root Zone (Nitrates, Phosphates) -->
          <g id="decompNutrients" transform="translate(250, 220)">
            <text x="-80" y="0" fill="#38bdf8" font-size="9" font-weight="700">NO₃⁻ (Nitrates)</text>
            <text x="30" y="0" fill="#fde047" font-size="9" font-weight="700">PO₄³⁻ (Phosphates)</text>
            <text x="-20" y="20" fill="#34d399" font-size="9" font-weight="700">K⁺ (Potassium)</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="245" width="450" height="65" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="decompDayTitle" x="45" y="270" fill="#34d399" font-size="12" font-weight="700">Day 30: Fungal Hyphae & Bacteria Dissolving Cellulose</text>
          <text id="decompDayDesc" x="45" y="292" fill="#cbd5e1" font-size="10.5">Microbes secrete extracellular enzymes, returning locked minerals back into topsoil.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⏳ Decomposition Timeline (0 to 60 Days):</span>
          <span id="decompValLabel" class="control-value">Day ${dayElapsed}</span>
        </div>
        <input type="range" id="sliderDecomp" class="sim-slider" min="0" max="60" value="${dayElapsed}">
        <div class="sim-btn-group" style="justify-content: center; margin-top: 0.5rem;">
          <button class="sim-toggle-btn" data-d="0">Day 0 (Fresh Leaf)</button>
          <button class="sim-toggle-btn" data-d="15">Day 15 (Fragmentation)</button>
          <button class="sim-toggle-btn active" data-d="30">Day 30 (Microbial Decay)</button>
          <button class="sim-toggle-btn" data-d="60">Day 60 (Complete Humus)</button>
        </div>
      `;

      const slider = document.getElementById('sliderDecomp');
      const valLabel = document.getElementById('decompValLabel');
      const leaf = document.getElementById('decompLeaf');
      const title = document.getElementById('decompDayTitle');
      const desc = document.getElementById('decompDayDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateDecomp(d) {
        dayElapsed = d;
        slider.value = d;
        valLabel.textContent = `Day ${d}`;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.d) === d));

        if (d === 0) {
          leaf.setAttribute('fill', '#15803d'); // Fresh green
          leaf.setAttribute('rx', '60');
          title.textContent = "Day 0: Fresh Fallen Leaf (Intact Organic Matter)";
          desc.textContent = "Organic carbon, nitrogen, and energy remain locked in intact plant cells.";
        } else if (d < 25) {
          leaf.setAttribute('fill', '#ca8a04'); // Yellow/brown
          leaf.setAttribute('rx', '50');
          title.textContent = `Day ${d}: Detritivores (Earthworms) Fragmenting Litter`;
          desc.textContent = "Physical chewing increases surface area for microscopic bacterial colonization.";
        } else if (d < 50) {
          leaf.setAttribute('fill', '#713f12'); // Dark rotting
          leaf.setAttribute('rx', '35');
          title.textContent = `Day ${d}: Saprophytic Fungi & Bacteria Secreting Enzymes`;
          desc.textContent = "Complex cellulose polymers are enzymatically hydrolyzed into simple mineral ions.";
        } else {
          leaf.setAttribute('fill', '#292524'); // Rich black humus
          leaf.setAttribute('rx', '15');
          title.textContent = "Day 60: Complete Conversion into Rich Dark Humus";
          desc.textContent = "Zero waste! 100% of minerals returned to the soil to nourish the next generation of trees.";
        }
      }

      slider.addEventListener('input', (e) => updateDecomp(parseInt(e.target.value)));
      btns.forEach(b => b.addEventListener('click', () => updateDecomp(parseInt(b.dataset.d))));
      updateDecomp(dayElapsed);
    }

    // 12. Biogeochemical Closed-Loop Cycles
    function simNutrientCycles() {
      simHeaderTitle.textContent = "Biogeochemical Cycles: Carbon & Nitrogen Closed Loops";
      let cycleKey = "carbon";

      simCanvas.innerHTML = `
        <svg id="cycleSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Atmospheric Reservoir -->
          <rect x="50" y="20" width="400" height="45" rx="8" fill="rgba(6, 78, 59, 0.4)" stroke="#34d399"/>
          <text id="cycleAtmText" x="250" y="47" fill="#6ee7b7" font-size="12" font-weight="700" text-anchor="middle">Atmospheric Reservoir: CO₂ Gas</text>

          <!-- Flow Arrow 1: Atmosphere to Plants -->
          <path d="M 120 65 L 120 150" stroke="#10b981" stroke-width="3" stroke-dasharray="4 2"/>
          <text id="cycleFlow1" x="110" y="110" fill="#a7f3d0" font-size="9" text-anchor="end">Photosynthesis</text>

          <!-- Terrestrial Organisms (Tree & Animal) -->
          <g transform="translate(160, 160)">
            <ellipse cx="0" cy="0" rx="35" ry="25" fill="#15803d"/>
            <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">Plants</text>
          </g>

          <g transform="translate(340, 160)">
            <ellipse cx="0" cy="0" rx="35" ry="25" fill="#d97706"/>
            <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">Animals</text>
          </g>

          <!-- Flow Arrow 2: Plants to Animals -->
          <line x1="195" y1="160" x2="305" y2="160" stroke="#fde047" stroke-width="2.5"/>
          <text x="250" y="152" fill="#fde047" font-size="8.5" text-anchor="middle">Feeding</text>

          <!-- Flow Arrow 3: Return to Atmosphere via Respiration / Decay -->
          <path d="M 340 135 L 340 65" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4 2"/>
          <text id="cycleFlow3" x="350" y="105" fill="#fca5a5" font-size="9">Respiration / Decay</text>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="cycleCardTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">The Carbon Cycle: Biological Closed Loop</text>
          <text id="cycleCardDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Photosynthesis fixes inorganic CO₂ into organic biomass; respiration and decay return it to air.</text>
          <text x="45" y="296" fill="#fde047" font-size="9.5">Every atom of carbon is perpetually recycled across geological time!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn active" data-c="carbon">🔄 The Carbon Cycle</button>
          <button class="sim-toggle-btn" data-c="nitrogen">⚡ The Nitrogen Cycle (Rhizobium)</button>
        </div>
      `;

      const atm = document.getElementById('cycleAtmText');
      const f1 = document.getElementById('cycleFlow1');
      const f3 = document.getElementById('cycleFlow3');
      const title = document.getElementById('cycleCardTitle');
      const desc = document.getElementById('cycleCardDesc');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateCycle(c) {
        cycleKey = c;
        btns.forEach(b => b.classList.toggle('active', b.dataset.c === c));

        if (c === 'carbon') {
          atm.textContent = "Atmospheric Reservoir: CO₂ Gas (0.04% of Air)";
          f1.textContent = "Photosynthesis";
          f3.textContent = "Respiration / Decay";
          title.textContent = "The Carbon Cycle: Biological Closed Loop";
          desc.textContent = "Photosynthesis fixes inorganic CO₂ into organic biomass; respiration and decay return it to air.";
        } else {
          atm.textContent = "Atmospheric Reservoir: N₂ Gas (78% of Air)";
          f1.textContent = "Nitrogen Fixation (Rhizobium)";
          f3.textContent = "Denitrifying Bacteria";
          title.textContent = "The Nitrogen Cycle: Bacterial Biogeochemical Wizardry";
          desc.textContent = "Rhizobium in legume root nodules breaks N≡N bonds to create nitrates, cycling into crops and back.";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateCycle(b.dataset.c)));
      updateCycle(cycleKey);
    }

    // 13. Trophic Cascades & Yellowstone Wolf / Tiger Watershed
    function simTrophicCascade() {
      simHeaderTitle.textContent = "Trophic Cascades: How Predators Transform Geography";
      let cascadeStep = 2; // Step 2 (Wolves present)

      simCanvas.innerHTML = `
        <svg id="cascadeSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- River Channel Graphic -->
          <path id="cascadeRiver" d="M 0 160 Q 250 140 500 160 L 500 220 Q 250 200 0 220 Z" fill="#0284c7"/>
          <text x="250" y="190" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">STABILIZED DEEP RIVER</text>

          <!-- Riverbank Willows / Aspens -->
          <g id="cascadeTrees">
            <circle cx="80" cy="130" r="18" fill="#15803d"/>
            <circle cx="160" cy="120" r="22" fill="#16a34a"/>
            <circle cx="340" cy="125" r="20" fill="#15803d"/>
            <circle cx="420" cy="130" r="18" fill="#16a34a"/>
          </g>

          <!-- Beaver Dam in River -->
          <rect id="cascadeDam" x="235" y="165" width="30" height="15" fill="#78350f" rx="3"/>
          <text id="cascadeDamText" x="250" y="177" fill="#fde047" font-size="7" font-weight="700" text-anchor="middle">Dam</text>

          <!-- Apex Predator (Wolf / Tiger) -->
          <g id="cascadeApex" transform="translate(60, 60)">
            <ellipse cx="0" cy="0" rx="16" ry="10" fill="#334155"/>
            <text x="0" y="20" fill="#f87171" font-size="8.5" font-weight="700" text-anchor="middle">Apex Wolf</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="cascadeTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Trophic Cascade in Action: Rivers Re-Engineered</text>
          <text id="cascadeDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Wolves hunt elk $\rightarrow$ Elk avoid rivers $\rightarrow$ Trees regrow $\rightarrow$ Roots stop erosion $\rightarrow$ Beavers build dams!</text>
          <text x="45" y="296" fill="#fde047" font-size="9.5">In India, protecting tigers in 53 reserves secures freshwater watersheds for 300+ rivers!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnNoPred" class="sim-toggle-btn">⚠️ Step 1: Apex Predator Absent (Overgrazing & Erosion)</button>
          <button id="btnWithPred" class="sim-toggle-btn active">🐺 Step 2: Predator Reintroduced (Rivers Stabilize!)</button>
        </div>
      `;

      const river = document.getElementById('cascadeRiver');
      const trees = document.getElementById('cascadeTrees');
      const dam = document.getElementById('cascadeDam');
      const damText = document.getElementById('cascadeDamText');
      const apex = document.getElementById('cascadeApex');
      const title = document.getElementById('cascadeTitle');
      const desc = document.getElementById('cascadeDesc');
      const btnNo = document.getElementById('btnNoPred');
      const btnYes = document.getElementById('btnWithPred');

      function updateCascade(withPred) {
        btnNo.classList.toggle('active', !withPred);
        btnYes.classList.toggle('active', withPred);

        if (withPred) {
          apex.style.display = 'block';
          trees.style.display = 'block';
          dam.style.display = 'block';
          damText.style.display = 'block';
          river.setAttribute('fill', '#0284c7');
          title.textContent = "Trophic Cascade in Action: Rivers Re-Engineered!";
          title.setAttribute('fill', '#34d399');
          desc.textContent = "Wolves hunt elk $\\rightarrow$ Trees regrow along riverbanks $\\rightarrow$ Roots lock soil $\\rightarrow$ Rivers stabilize!";
        } else {
          apex.style.display = 'none';
          trees.style.display = 'none'; // Overbrowsed away
          dam.style.display = 'none';
          damText.style.display = 'none';
          river.setAttribute('fill', '#92400e'); // Muddy, wide, eroded river
          title.textContent = "⚠️ Predator Absent: Severe Riverbank Erosion & Muddy Flooding";
          title.setAttribute('fill', '#f43f5e');
          desc.textContent = "Unchecked elk herds devoured all streamside saplings; unanchored banks collapsed into the water.";
        }
      }

      btnNo.addEventListener('click', () => updateCascade(false));
      btnYes.addEventListener('click', () => updateCascade(true));
      updateCascade(true);
    }

    // 14. Ecological Succession: Nature's Rebuilding
    function simEcologicalSuccession() {
      simHeaderTitle.textContent = "Primary vs. Secondary Ecological Succession";
      let successionStage = 4; // Climax forest

      const stages = [
        { name: "Stage 1: Pioneer Lichens (0-50 yrs)", title: "Crustose Lichens on Bare Rock", desc: "Chemical acid etching creates first microscopic grains of mineral soil.", fill: "#334155" },
        { name: "Stage 2: Mosses & Herbs (50-150 yrs)", title: "Primitive Plants & Soil Accumulation", desc: "Mosses trap dust and moisture; organic humus layer deepens.", fill: "#65a30d" },
        { name: "Stage 3: Perennial Grasses & Shrubs (150-300 yrs)", title: "Shrub Layer Colonization", desc: "Fast-growing woody shrubs establish; birds and small rodents arrive.", fill: "#16a34a" },
        { name: "Stage 4: Climax Sal-Oak Forest (500+ yrs)", title: "Stable Mature Equilibrium", desc: "Majestic self-sustaining forest community in dynamic equilibrium with regional climate.", fill: "#15803d" }
      ];

      simCanvas.innerHTML = `
        <svg id="succSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Ground Base Layer (Soil deepening) -->
          <rect id="succGround" x="0" y="180" width="500" height="140" fill="#1e180e"/>
          
          <!-- Climax Forest Group -->
          <g id="succForestGrp">
            <rect x="70" y="110" width="14" height="75" fill="#78350f"/>
            <circle cx="77" cy="95" r="32" fill="#15803d"/>

            <rect x="180" y="90" width="18" height="95" fill="#78350f"/>
            <ellipse cx="189" cy="80" rx="42" ry="32" fill="#16a34a"/>

            <rect x="310" y="100" width="16" height="85" fill="#78350f"/>
            <circle cx="318" cy="85" r="35" fill="#15803d"/>

            <rect x="420" y="120" width="12" height="65" fill="#78350f"/>
            <ellipse cx="426" cy="105" rx="28" ry="24" fill="#16a34a"/>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="240" width="450" height="70" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="succTitleText" x="45" y="262" fill="#34d399" font-size="12" font-weight="700">Stage 4: Climax Sal-Oak Forest (500+ Years)</text>
          <text id="succDescText" x="45" y="282" fill="#cbd5e1" font-size="10.5">Majestic self-sustaining forest in dynamic equilibrium with the regional climate.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⏳ Ecological Succession Stage:</span>
          <span id="succValLabel" class="control-value">Climax Forest (Stage 4)</span>
        </div>
        <input type="range" id="sliderSucc" class="sim-slider" min="1" max="4" value="${successionStage}">
        <div class="sim-btn-group" style="justify-content: center; margin-top: 0.5rem;">
          <button class="sim-toggle-btn" data-s="1">Pioneer Lichens</button>
          <button class="sim-toggle-btn" data-s="2">Mosses & Herbs</button>
          <button class="sim-toggle-btn" data-s="3">Shrubs Layer</button>
          <button class="sim-toggle-btn active" data-s="4">Climax Forest</button>
        </div>
      `;

      const slider = document.getElementById('sliderSucc');
      const valLabel = document.getElementById('succValLabel');
      const forest = document.getElementById('succForestGrp');
      const title = document.getElementById('succTitleText');
      const desc = document.getElementById('succDescText');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateSucc(st) {
        successionStage = st;
        slider.value = st;
        valLabel.textContent = stages[st - 1].name;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.s) === st));

        if (st === 1) {
          forest.style.display = 'none';
          title.textContent = stages[0].title;
          title.setAttribute('fill', '#94a3b8');
          desc.textContent = stages[0].desc;
        } else if (st === 2) {
          forest.style.display = 'none';
          title.textContent = stages[1].title;
          title.setAttribute('fill', '#a3e635');
          desc.textContent = stages[1].desc;
        } else if (st === 3) {
          forest.style.display = 'block';
          forest.style.opacity = '0.5';
          title.textContent = stages[2].title;
          title.setAttribute('fill', '#34d399');
          desc.textContent = stages[2].desc;
        } else {
          forest.style.display = 'block';
          forest.style.opacity = '1';
          title.textContent = stages[3].title;
          title.setAttribute('fill', '#34d399');
          desc.textContent = stages[3].desc;
        }
      }

      slider.addEventListener('input', (e) => updateSucc(parseInt(e.target.value)));
      btns.forEach(b => b.addEventListener('click', () => updateSucc(parseInt(b.dataset.s))));
      updateSucc(successionStage);
    }

    // 15. Predator-Prey Lotka-Volterra Dynamic Balance
    function simPredatorPreyBalance() {
      simHeaderTitle.textContent = "Predator-Prey Negative Feedback & Carrying Capacity";
      let timeStep = 3;

      simCanvas.innerHTML = `
        <svg id="lvSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Graph Grid -->
          <rect x="40" y="30" width="420" height="190" fill="#061f10" stroke="rgba(255, 255, 255, 0.1)"/>
          
          <!-- Carrying Capacity Line (K) -->
          <line x1="40" y1="90" x2="460" y2="90" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"/>
          <text x="450" y="84" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="end">Carrying Capacity (K)</text>

          <!-- Prey Curve (Spotted Deer - Green) -->
          <path d="M 50 150 Q 120 40 190 150 Q 260 210 330 150 Q 400 40 460 150" fill="none" stroke="#10b981" stroke-width="3"/>
          
          <!-- Predator Curve (Leopards - Red, Lagging behind) -->
          <path d="M 50 180 Q 150 180 220 80 Q 290 180 360 180 Q 430 80 460 140" fill="none" stroke="#f43f5e" stroke-width="3"/>

          <!-- Animated Indicator Dot -->
          <circle id="lvPreyDot" cx="190" cy="150" r="6" fill="#10b981"/>
          <circle id="lvPredDot" cx="220" cy="80" r="6" fill="#f43f5e"/>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="lvTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Lotka-Volterra Rhythmic Oscillation</text>
          <text id="lvDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Prey surges $\rightarrow$ Predator food increases $\rightarrow$ Predators rise $\rightarrow$ Prey hunted down $\rightarrow$ Balance preserved!</text>
          <text x="45" y="296" fill="#fde047" font-size="9.5">Negative feedback loops prevent herbivores from depleting plants and carnivores from starvation.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="control-row">
          <span class="control-label">⏳ Cycle Phase:</span>
          <span id="lvValLabel" class="control-value">Phase 2: Predator Peak</span>
        </div>
        <div class="sim-btn-group" style="justify-content: center;">
          <button class="sim-toggle-btn" data-p="1">1. Prey Surge</button>
          <button class="sim-toggle-btn active" data-p="2">2. Predator Follow-Up</button>
          <button class="sim-toggle-btn" data-p="3">3. Prey Decline</button>
          <button class="sim-toggle-btn" data-p="4">4. Recovery Cycle</button>
        </div>
      `;

      const pDot = document.getElementById('lvPreyDot');
      const predDot = document.getElementById('lvPredDot');
      const title = document.getElementById('lvTitle');
      const desc = document.getElementById('lvDesc');
      const valLabel = document.getElementById('lvValLabel');
      const btns = simControls.querySelectorAll('.sim-toggle-btn');

      function updateLV(p) {
        timeStep = p;
        btns.forEach(b => b.classList.toggle('active', parseInt(b.dataset.p) === p));

        if (p === 1) {
          pDot.setAttribute('cx', '120'); pDot.setAttribute('cy', '60');
          predDot.setAttribute('cx', '120'); predDot.setAttribute('cy', '180');
          valLabel.textContent = "Phase 1: Prey Population Surge";
          title.textContent = "Phase 1: Abundant Grass Sparks Deer Boom";
          desc.textContent = "Deer multiply rapidly; plenty of forage pushes prey population towards carrying capacity.";
        } else if (p === 2) {
          pDot.setAttribute('cx', '190'); pDot.setAttribute('cy', '150');
          predDot.setAttribute('cx', '220'); predDot.setAttribute('cy', '80');
          valLabel.textContent = "Phase 2: Predator Peak";
          title.textContent = "Phase 2: Plentiful Prey Multiplies Predators";
          desc.textContent = "With ample food, leopards successfully breed and their numbers surge, increasing hunting pressure.";
        } else if (p === 3) {
          pDot.setAttribute('cx', '260'); pDot.setAttribute('cy', '200');
          predDot.setAttribute('cx', '290'); predDot.setAttribute('cy', '170');
          valLabel.textContent = "Phase 3: Prey Decline";
          title.textContent = "Phase 3: High Predation Causes Deer Dip";
          desc.textContent = "Heavy hunting causes deer numbers to decline, subsequently reducing available predator food.";
        } else {
          pDot.setAttribute('cx', '330'); pDot.setAttribute('cy', '150');
          predDot.setAttribute('cx', '360'); predDot.setAttribute('cy', '180');
          valLabel.textContent = "Phase 4: Predator Dip & Prey Recovery";
          title.textContent = "Phase 4: Predator Decline Allows Prey to Recover";
          desc.textContent = "Leopard numbers drop, relieving predation pressure and allowing deer to replenish the cycle!";
        }
      }

      btns.forEach(b => b.addEventListener('click', () => updateLV(parseInt(b.dataset.p))));
      updateLV(timeStep);
    }

    // 16. Ecosystem Services & Agroecosystem Allies
    function simEcosystemServices() {
      simHeaderTitle.textContent = "Ecosystem Services: How Natural Ecosystems Serve Farms";
      let ecoMode = "healthy";

      simCanvas.innerHTML = `
        <svg id="ecoFarmSvg" viewBox="0 0 500 320" width="100%" height="100%">
          <!-- Farm Orchard / Crop Field -->
          <rect x="0" y="160" width="500" height="160" fill="#14532d"/>
          
          <!-- Crop Rows -->
          <line x1="30" y1="220" x2="470" y2="220" stroke="#16a34a" stroke-width="4"/>
          <line x1="30" y1="260" x2="470" y2="260" stroke="#16a34a" stroke-width="4"/>

          <!-- Surrounding Natural Forest Barrier -->
          <rect x="0" y="0" width="150" height="160" fill="#052e16"/>
          <text x="75" y="40" fill="#6ee7b7" font-size="9" font-weight="700" text-anchor="middle">Wild Forest Sanctuary</text>

          <!-- Natural Allies Working on the Farm -->
          <g id="ecoAllies">
            <!-- Honeybee pollinating -->
            <circle cx="220" cy="190" r="5" fill="#fde047"/>
            <text x="220" y="175" fill="#fde047" font-size="8" font-weight="700" text-anchor="middle">🐝 Wild Bee (Pollination)</text>

            <!-- Ladybug preying on aphids -->
            <circle cx="340" cy="220" r="6" fill="#ef4444"/>
            <text x="340" y="240" fill="#fca5a5" font-size="8" font-weight="700" text-anchor="middle">🐞 Ladybug (Pest Control)</text>

            <!-- Barn Owl guarding silo -->
            <circle cx="430" cy="120" r="14" fill="#a16207"/>
            <text x="430" y="100" fill="#fef08a" font-size="8" font-weight="700" text-anchor="middle">🦉 Barn Owl (Rodent Control)</text>
          </g>

          <!-- Readout Card -->
          <rect x="25" y="235" width="450" height="75" rx="8" fill="rgba(6, 26, 14, 0.95)" stroke="#10b981"/>
          <text id="farmTitle" x="45" y="258" fill="#34d399" font-size="12" font-weight="700">Healthy Agroecosystem Supported by Natural Ecosystem Services</text>
          <text id="farmDesc" x="45" y="278" fill="#cbd5e1" font-size="10.5">Wild bees boost fruit set by 40%; ladybugs devour crop-destroying aphids for free!</text>
          <text id="farmSub" x="45" y="296" fill="#fde047" font-size="9.5">Barn owls consume 1,000–3,000 crop-eating rodents per family, eliminating toxic chemical poisons.</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div class="sim-btn-group" style="justify-content: center;">
          <button id="btnEcoFarm" class="sim-toggle-btn active">🌿 Ecological Farm with Natural Allies</button>
          <button id="btnMonoFarm" class="sim-toggle-btn">⚠️ Chemical Monoculture (Natural Allies Wiped Out)</button>
        </div>
      `;

      const allies = document.getElementById('ecoAllies');
      const title = document.getElementById('farmTitle');
      const desc = document.getElementById('farmDesc');
      const sub = document.getElementById('farmSub');
      const btnE = document.getElementById('btnEcoFarm');
      const btnM = document.getElementById('btnMonoFarm');

      function updateFarm(isE) {
        btnE.classList.toggle('active', isE);
        btnM.classList.toggle('active', !isE);

        if (isE) {
          allies.style.display = 'block';
          title.textContent = "Healthy Agroecosystem Supported by Natural Ecosystem Services";
          title.setAttribute('fill', '#34d399');
          desc.textContent = "Wild bees boost fruit set by 40%; ladybugs devour crop-destroying aphids for free!";
          sub.textContent = "Barn owls consume 1,000–3,000 crop-eating rodents per family, eliminating toxic chemical poisons.";
        } else {
          allies.style.display = 'none';
          title.textContent = "⚠️ Chemical Monoculture: High Input Costs & Pest Resistance";
          title.setAttribute('fill', '#f43f5e');
          desc.textContent = "Insecticides kill beneficial bees and ladybugs; pests develop resistance, requiring costly sprays.";
          sub.textContent = "Without natural predators, rodent and aphid outbreaks devastate yields and poison groundwater.";
        }
      }

      btnE.addEventListener('click', () => updateFarm(true));
      btnM.addEventListener('click', () => updateFarm(false));
      updateFarm(true);
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

output_path = 'public/animations/class8-science-nature-harmony.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print(f"Successfully generated {output_path} ({len(rendered_html)} bytes).")

