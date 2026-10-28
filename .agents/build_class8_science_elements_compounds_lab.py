# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-elements-compounds.html
Class 8 Science - Chapter 8: Elements, Compounds, and Mixtures
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Rasacharya Dr. Nagarjuna)
- 16 bespoke interactive SVG simulators with live controls, gauges, and animations
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
from class8_science_elements_compounds_data import SLIDES, QUIZ_QUESTIONS

# Assemble full slides data
full_slides = []
for slide in SLIDES:
    s = dict(slide)
    if s.get("is_quiz_slide"):
        start_idx = s.get("quiz_start_idx", 1) - 1
        count = s.get("quiz_count", 10)
        s["questions"] = QUIZ_QUESTIONS[start_idx:start_idx + count]
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)
QUIZ_QUESTIONS_JSON = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 8 Science • Chapter 8: Elements, Compounds, and Mixtures Master Lab</title>
  
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
      --bg-primary: #060d17;
      --bg-secondary: #0c1524;
      --card-bg: rgba(12, 21, 36, 0.9);
      --card-border: rgba(56, 189, 248, 0.25);
      --accent-sky: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-emerald: #10b981;
      --accent-purple: #c084fc;
      --accent-teal: #14b8a6;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 12% 18%, rgba(56, 189, 248, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 88% 75%, rgba(192, 132, 252, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(20, 184, 166, 0.05) 0%, transparent 60%);
    }

    /* Header & Navigation Bar */
    .lab-header {
      background: rgba(12, 21, 36, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      padding: 0.75rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .header-branding {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .lab-icon {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, #0284c7, #14b8a6);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
    }

    .header-text h1 {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.01em;
    }

    .header-text .sub-badge {
      font-size: 0.72rem;
      color: var(--accent-sky);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .progress-section {
      flex: 1;
      max-width: 450px;
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }

    .progress-bar-container {
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #14b8a6, #c084fc);
      width: 5%;
      transition: width 0.3s ease;
    }

    .progress-stats {
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: var(--text-muted);
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-nav {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .btn-nav:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-sky);
      color: var(--accent-sky);
    }

    .btn-nav:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .btn-primary {
      background: #0284c7;
      border-color: #38bdf8;
    }

    .btn-primary:hover:not(:disabled) {
      background: #0369a1;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.5);
    }

    /* Teacher Avatar Bar */
    .avatar-bar {
      background: rgba(20, 32, 54, 0.75);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding: 0.6rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
      backdrop-filter: blur(8px);
    }

    .avatar-frame {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, #0284c7, #14b8a6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      position: relative;
      flex-shrink: 0;
      box-shadow: 0 0 12px rgba(20, 184, 166, 0.4);
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--accent-teal);
      animation: pulse-ring 1.5s infinite;
      display: none;
    }

    @keyframes pulse-ring {
      0% { transform: scale(0.95); opacity: 0.8; }
      100% { transform: scale(1.3); opacity: 0; }
    }

    .avatar-dialogue-box {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .avatar-name-row {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .avatar-name {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent-teal);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .speech-status-pill {
      font-size: 0.65rem;
      padding: 0.1rem 0.5rem;
      border-radius: 999px;
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
      display: none;
    }

    .avatar-speech-text {
      font-size: 0.92rem;
      color: #e2e8f0;
      line-height: 1.4;
      font-style: italic;
    }

    .audio-controls {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .btn-audio {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      width: 34px;
      height: 34px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1rem;
      transition: all 0.2s;
    }

    .btn-audio:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-sky);
      color: var(--accent-sky);
    }

    /* Main Container */
    .lab-main {
      flex: 1;
      padding: 1.5rem;
      max-width: 1440px;
      margin: 0 auto;
      width: 100%;
    }

    /* Lesson Grid */
    .lesson-grid {
      display: grid;
      grid-template-columns: 1.05fr 1.15fr;
      gap: 1.5rem;
      align-items: start;
    }

    @media (max-width: 1024px) {
      .lesson-grid {
        grid-template-columns: 1fr;
      }
    }

    .glass-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    /* Theory Header */
    .slide-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .slide-tag {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-sky);
      background: rgba(56, 189, 248, 0.12);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.3);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .slide-number-pill {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-amber);
      background: rgba(245, 158, 11, 0.12);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .slide-title {
      font-size: 1.55rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.25;
      background: linear-gradient(135deg, #ffffff, #38bdf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Vocabulary Box */
    .vocab-box {
      background: rgba(14, 165, 233, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .vocab-header {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent-sky);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .vocab-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.6rem;
    }

    .vocab-chip {
      background: rgba(12, 21, 36, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 0.55rem 0.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .vocab-word {
      font-size: 0.82rem;
      font-weight: 700;
      color: #38bdf8;
    }

    .vocab-def {
      font-size: 0.75rem;
      color: #cbd5e1;
      line-height: 1.35;
    }

    /* Theory Body */
    .theory-content {
      color: #cbd5e1;
      font-size: 0.92rem;
      line-height: 1.65;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .theory-content h3 {
      font-size: 1.15rem;
      color: #38bdf8;
      margin-top: 0.25rem;
    }

    .theory-content h4 {
      font-size: 0.98rem;
      color: #f59e0b;
      margin-top: 0.4rem;
    }

    .theory-content ul, .theory-content ol {
      padding-left: 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }

    .theory-content strong {
      color: #fff;
    }

    .theory-content em {
      color: #38bdf8;
    }

    /* Checkpoints Section */
    .checkpoints-card {
      background: rgba(12, 21, 36, 0.92);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 14px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .checkpoints-header {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--accent-emerald);
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .checkpoint-item {
      background: rgba(20, 32, 54, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .checkpoint-q {
      font-size: 0.88rem;
      color: #f1f5f9;
      line-height: 1.45;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.45rem;
    }

    .cp-opt-btn {
      background: rgba(12, 21, 36, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #cbd5e1;
      padding: 0.55rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .cp-opt-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--accent-sky);
      color: #fff;
    }

    .cp-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #34d399 !important;
      font-weight: 700;
    }

    .cp-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fb7185 !important;
    }

    .cp-feedback {
      display: none;
      padding: 0.6rem 0.85rem;
      border-radius: 8px;
      font-size: 0.8rem;
      line-height: 1.4;
    }

    .cp-feedback.show-correct {
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }

    .cp-feedback.show-incorrect {
      display: block;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fda4af;
    }

    /* Simulator Panel */
    .simulator-container {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .sim-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding-bottom: 0.75rem;
    }

    .sim-title {
      font-size: 1.1rem;
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .sim-badge {
      font-size: 0.7rem;
      padding: 0.2rem 0.5rem;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.15);
      color: #7dd3fc;
      border: 1px solid rgba(56, 189, 248, 0.3);
      font-weight: 600;
    }

    .sim-canvas {
      width: 100%;
      min-height: 380px;
      background: rgba(6, 13, 23, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 1rem;
    }

    .sim-controls {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      background: rgba(20, 32, 54, 0.55);
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
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.8);
    }

    .btn-sim {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #fff;
      padding: 0.5rem 0.95rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .btn-sim:hover {
      background: rgba(56, 189, 248, 0.3);
      border-color: #38bdf8;
    }

    .btn-sim.active {
      background: #0284c7;
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.5);
    }

    /* Quiz Container */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 1.5rem;
    }

    .quiz-header-card {
      background: linear-gradient(135deg, rgba(20, 32, 54, 0.95), rgba(12, 21, 36, 0.95));
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 16px;
      padding: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .quiz-title-area h2 {
      font-size: 1.5rem;
      color: #fbbf24;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .quiz-title-area p {
      color: #cbd5e1;
      font-size: 0.88rem;
      margin-top: 0.25rem;
    }

    .quiz-score-badge {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      padding: 0.6rem 1.25rem;
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .quiz-score-num {
      font-size: 1.6rem;
      font-weight: 800;
      color: #fbbf24;
    }

    .quiz-score-lbl {
      font-size: 0.72rem;
      color: #cbd5e1;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .quiz-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 1.25rem;
    }

    @media (max-width: 640px) {
      .quiz-grid {
        grid-template-columns: 1fr;
      }
    }

    .quiz-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      backdrop-filter: blur(12px);
    }

    .quiz-q-num {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-sky);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .quiz-q-text {
      font-size: 0.92rem;
      font-weight: 600;
      color: #f8fafc;
      line-height: 1.45;
    }

    .quiz-opts {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }

    .quiz-opt-btn {
      background: rgba(20, 32, 54, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      padding: 0.6rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--accent-sky);
      color: #fff;
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #34d399 !important;
      font-weight: 700;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fb7185 !important;
    }

    .quiz-btn-solution {
      display: none;
      align-self: flex-start;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      margin-top: 0.35rem;
      transition: all 0.2s;
    }

    .quiz-btn-solution:hover {
      background: rgba(245, 158, 11, 0.3);
      border-color: #f59e0b;
      transform: translateY(-1px);
    }

    /* Modal Backdrop & Pop-up Dialog */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(10px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-content {
      background: #0c1524;
      border: 1px solid rgba(245, 158, 11, 0.5);
      border-radius: 18px;
      max-width: 650px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.75rem;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(245, 158, 11, 0.2);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
    }

    .modal-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-close-modal {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #cbd5e1;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .btn-close-modal:hover {
      background: rgba(244, 63, 94, 0.2);
      border-color: var(--accent-rose);
      color: #fff;
    }

    .modal-body {
      color: #cbd5e1;
      font-size: 0.92rem;
      line-height: 1.6;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .modal-body ol {
      padding-left: 1.4rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    /* Last Slide Notice */
    #lastSlideNotice {
      display: none;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(56, 189, 248, 0.2));
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #a7f3d0;
      padding: 0.9rem 1.5rem;
      border-radius: 12px;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
      margin-top: 1rem;
    }
  </style>
</head>
<body>

  <!-- Header Navigation -->
  <header class="lab-header">
    <div class="header-branding">
      <div class="lab-icon">⚗️</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 8</div>
        <h1>Elements, Compounds, and Mixtures</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Mixture Fundamentals</span>
      </div>
    </div>

    <div class="header-controls">
      <button class="btn-nav" id="prevBtn" onclick="prevSlide()" disabled>
        <span>◀</span> Previous
      </button>
      <button class="btn-nav btn-primary" id="nextBtn" onclick="nextSlide()">
        Next <span>▶</span>
      </button>
    </div>
  </header>

  <!-- Teacher Avatar Bar -->
  <div class="avatar-bar">
    <div class="avatar-frame">
      <span>👨‍🔬</span>
      <div class="avatar-speaking-pulse" id="avatarPulse"></div>
    </div>
    <div class="avatar-dialogue-box">
      <div class="avatar-name-row">
        <span class="avatar-name">Rasacharya Dr. Nagarjuna • Ancient Metallurgist & Modern Chemist</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Welcome to the Chemical Synthesis & Material Purity Laboratory! Let us examine how physical combinations yield mixtures while chemical bonding crafts entirely new compounds.
      </div>
    </div>
    <div class="audio-controls">
      <button class="btn-audio" id="btnAudioToggle" title="Play / Pause Audio Narration" onclick="toggleSpeech()">
        🔊
      </button>
      <button class="btn-audio" id="btnAudioReplay" title="Replay Narration" onclick="replaySpeech()">
        🔄
      </button>
    </div>
  </div>

  <!-- Main Laboratory Workspace -->
  <main class="lab-main">
    
    <!-- Standard Lesson Layout (Slides 1 to 16) -->
    <div class="lesson-grid" id="lessonGrid">
      
      <!-- Left Column: Theory & In-Slide Checkpoints -->
      <div class="glass-card">
        <div class="slide-badge-row">
          <span class="slide-tag" id="slideBadge">Mixture Fundamentals</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Defining Mixtures</h2>

        <!-- Key Technical Vocabulary Section -->
        <div class="vocab-box" id="vocabBox">
          <div class="vocab-header">
            <span>📚</span> Key Technical Vocabulary
          </div>
          <div class="vocab-grid" id="vocabGrid">
            <!-- Dynamically Populated -->
          </div>
        </div>

        <!-- Theory Section -->
        <div class="theory-content" id="theoryContent">
          <!-- Dynamically Injected -->
        </div>

        <!-- In-Slide Checkpoints -->
        <div class="checkpoints-card" id="checkpointContainer">
          <div class="checkpoints-header">
            <span>🎯</span> In-Slide Checkpoints
          </div>
          <div id="checkpointsList" style="display: flex; flex-direction: column; gap: 0.85rem;">
            <!-- Checkpoint Questions Dynamically Populated -->
          </div>
        </div>
      </div>

      <!-- Right Column: Interactive Bespoke Simulator -->
      <div class="glass-card simulator-container">
        <div class="sim-header">
          <div class="sim-title">
            <span id="simIcon">🥗</span>
            <span id="simTitle">Interactive Chemistry Simulator</span>
          </div>
          <span class="sim-badge" id="simBadge">Live Dynamic Lab</span>
        </div>

        <!-- Simulator Canvas Area -->
        <div class="sim-canvas" id="simCanvas">
          <!-- Dynamically Injected SVG Canvas -->
        </div>

        <!-- Simulator Controls -->
        <div class="sim-controls" id="simControls">
          <!-- Dynamically Injected Controls -->
        </div>
      </div>
    </div>

    <!-- Quiz Mastery Challenge Layout (Slides 17 to 20) -->
    <div class="quiz-container" id="quizContainer">
      <div class="quiz-header-card">
        <div class="quiz-title-area">
          <h2 id="quizTitle">Mastery Challenge • Part I</h2>
          <p id="quizSubtitle">Answer all 10 conceptual inquiries below. Click on any solution button to view the full step-by-step breakdown.</p>
        </div>
        <div class="quiz-score-badge">
          <div class="quiz-score-num" id="quizScoreNum">0 / 10</div>
          <div class="quiz-score-lbl">Score Achieved</div>
        </div>
      </div>

      <div class="quiz-grid" id="quizQuestionsGrid">
        <!-- 10 Quiz Cards Dynamically Populated -->
      </div>
    </div>

    <!-- Terminal Last Slide Notice -->
    <div id="lastSlideNotice">
      🎉 You have reached the last slide of this chapter!
    </div>

  </main>

  <!-- Step-by-Step Pop-up Solution Modal (Always Initialized Hidden) -->
  <div class="modal-backdrop" id="solutionModal" style="display: none;">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">
          <span>💡</span> <span id="modalQuestionTitle">Question Solution</span>
        </div>
        <button class="btn-close-modal" onclick="closeSolutionModal()">✕</button>
      </div>
      <div class="modal-body" id="modalSolutionBody">
        <!-- Injected Solution Content -->
      </div>
    </div>
  </div>

  <!-- Data Script -->
  <script>
    const SLIDES = __SLIDES_JSON__;
    const ALL_QUIZ_QUESTIONS = __QUIZ_QUESTIONS_JSON__;
  </script>

  <!-- Main Laboratory Controller & Simulator Logic -->
  <script>
    let currentSlideIndex = 0;
    let quizScores = {};
    let synth = window.speechSynthesis;
    let currentUtterance = null;
    let isSpeaking = false;

    // Initialize Lab
    window.addEventListener('DOMContentLoaded', () => {
      loadSlide(0);
      setupSpeech();
    });

    // Slide Loading Engine
    function loadSlide(index) {
      if (index < 0 || index >= SLIDES.length) return;
      currentSlideIndex = index;
      const slide = SLIDES[index];

      // Update Nav Buttons
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const lastSlideNotice = document.getElementById('lastSlideNotice');

      prevBtn.disabled = (index === 0);

      // Terminal Slide 20 Handling
      if (index === SLIDES.length - 1) {
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'block';
      } else {
        nextBtn.style.display = 'flex';
        lastSlideNotice.style.display = 'none';
      }

      // Update Progress
      const pct = ((index + 1) / SLIDES.length) * 100;
      document.getElementById('progressBarFill').style.width = pct + '%';
      document.getElementById('slideIndicator').textContent = `Slide ${index + 1} of ${SLIDES.length}`;
      document.getElementById('slideTagIndicator').textContent = slide.title;

      // Update Avatar Dialogue & Narration
      document.getElementById('avatarSpeechText').textContent = slide.avatar_dialogue;
      speakText(slide.avatar_dialogue);

      const lessonGrid = document.getElementById('lessonGrid');
      const quizContainer = document.getElementById('quizContainer');

      if (!slide.is_quiz_slide) {
        // Content Slide (1 to 16)
        lessonGrid.style.display = 'grid';
        quizContainer.style.display = 'none';

        document.getElementById('slideBadge').textContent = slide.tag;
        document.getElementById('slideNumberPill').textContent = `Slide ${index + 1} of 20`;
        document.getElementById('slideHeading').textContent = slide.title;
        document.getElementById('theoryContent').innerHTML = slide.theory;

        // Render Vocabulary
        renderVocabulary(slide.vocabulary);

        // Render Checkpoints
        renderCheckpoints(slide.checkpoints);

        // Render Simulator
        renderSimulator(slide.sim_id);

      } else {
        // Quiz Slide (17 to 20)
        lessonGrid.style.display = 'none';
        quizContainer.style.display = 'flex';

        document.getElementById('quizTitle').textContent = slide.title;
        document.getElementById('quizSubtitle').textContent = `Mastery Challenge Part ${index - 15}: Review Questions ${(index - 16)*10 + 1} to ${(index - 15)*10}`;
        renderQuizSlide(slide.questions);
      }

      setTimeout(() => {
        triggerMathRender(document.body);
      }, 50);
    }

    function prevSlide() {
      if (currentSlideIndex > 0) {
        loadSlide(currentSlideIndex - 1);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function nextSlide() {
      if (currentSlideIndex < SLIDES.length - 1) {
        loadSlide(currentSlideIndex + 1);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // Vocabulary Renderer
    function renderVocabulary(vocabList) {
      const container = document.getElementById('vocabGrid');
      container.innerHTML = '';
      if (!vocabList || vocabList.length === 0) {
        document.getElementById('vocabBox').style.display = 'none';
        return;
      }
      document.getElementById('vocabBox').style.display = 'flex';

      vocabList.forEach(item => {
        const chip = document.createElement('div');
        chip.className = 'vocab-chip';
        chip.innerHTML = `
          <div class="vocab-word">${item.word}</div>
          <div class="vocab-def">${item.definition}</div>
        `;
        container.appendChild(chip);
      });
    }

    // Checkpoints Renderer
    function renderCheckpoints(checkpoints) {
      const container = document.getElementById('checkpointsList');
      container.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) return;

      checkpoints.forEach((cp, qIdx) => {
        const item = document.createElement('div');
        item.className = 'checkpoint-item';

        const qText = document.createElement('div');
        qText.className = 'checkpoint-q';
        qText.innerHTML = `<strong>Q${qIdx + 1}:</strong> ${cp.question}`;

        const optsDiv = document.createElement('div');
        optsDiv.className = 'checkpoint-options';

        const feedback = document.createElement('div');
        feedback.className = 'cp-feedback';
        feedback.id = `cpFeedback_${currentSlideIndex}_${qIdx}`;

        cp.options.forEach((opt, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'cp-opt-btn';
          btn.innerHTML = opt;
          btn.onclick = () => {
            const allBtns = optsDiv.querySelectorAll('.cp-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('correct');
              feedback.className = 'cp-feedback show-correct';
              feedback.innerHTML = `<strong>✓ Brilliant!</strong> ${cp.explanation}`;
            } else {
              btn.classList.add('incorrect');
              allBtns[cp.correct].classList.add('correct');
              feedback.className = 'cp-feedback show-incorrect';
              feedback.innerHTML = `<strong>✗ Not quite:</strong> ${cp.explanation}`;
            }
            triggerMathRender(feedback);
          };
          optsDiv.appendChild(btn);
        });

        item.appendChild(qText);
        item.appendChild(optsDiv);
        item.appendChild(feedback);
        container.appendChild(item);
      });
    }

    // Quiz Slide Renderer
    function renderQuizSlide(questions) {
      const container = document.getElementById('quizQuestionsGrid');
      container.innerHTML = '';
      let correctCount = 0;
      const slideKey = currentSlideIndex;

      questions.forEach((q, idx) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';

        const qNum = document.createElement('div');
        qNum.className = 'quiz-q-num';
        qNum.textContent = `Question ${q.id} • ${q.concept}`;

        const qText = document.createElement('div');
        qText.className = 'quiz-q-text';
        qText.innerHTML = q.question;

        const opts = document.createElement('div');
        opts.className = 'quiz-opts';

        const solBtn = document.createElement('button');
        solBtn.className = 'quiz-btn-solution';
        solBtn.innerHTML = `💡 View Step-by-Step Solution`;
        solBtn.onclick = () => openSolutionModal(q);

        q.options.forEach((opt, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.innerHTML = opt;
          btn.onclick = () => {
            const allBtns = opts.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === q.correct) {
              btn.classList.add('correct');
              if (!quizScores[`${slideKey}_${idx}`]) {
                quizScores[`${slideKey}_${idx}`] = true;
              }
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
            }

            solBtn.style.display = 'inline-flex';
            updateQuizScore(questions.length);
          };
          opts.appendChild(btn);
        });

        card.appendChild(qNum);
        card.appendChild(qText);
        card.appendChild(opts);
        card.appendChild(solBtn);
        container.appendChild(card);
      });

      updateQuizScore(questions.length);
    }

    function updateQuizScore(totalQuestions) {
      let count = 0;
      for (let i = 0; i < totalQuestions; i++) {
        if (quizScores[`${currentSlideIndex}_${i}`]) count++;
      }
      document.getElementById('quizScoreNum').textContent = `${count} / ${totalQuestions}`;
    }

    // Modal Handling
    function openSolutionModal(question) {
      document.getElementById('modalQuestionTitle').textContent = `Question ${question.id}: Solution Breakdown`;
      document.getElementById('modalSolutionBody').innerHTML = `
        <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 0.75rem 1rem; border-radius: 6px; margin-bottom: 0.75rem;">
          <strong style="color: #fbbf24;">Inquiry:</strong> ${question.question}
        </div>
        <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 0.75rem 1rem; border-radius: 6px; margin-bottom: 0.75rem;">
          <strong style="color: #34d399;">Correct Answer:</strong> ${question.options[question.correct]}
        </div>
        <div style="line-height: 1.6; color: #cbd5e1;">
          ${question.solution}
        </div>
      `;
      document.getElementById('solutionModal').style.display = 'flex';
      triggerMathRender(document.getElementById('modalSolutionBody'));
    }

    function closeSolutionModal() {
      document.getElementById('solutionModal').style.display = 'none';
    }

    // Audio Speech Synthesis
    function setupSpeech() {
      if (!('speechSynthesis' in window)) {
        document.getElementById('btnAudioToggle').style.display = 'none';
        document.getElementById('btnAudioReplay').style.display = 'none';
      }
    }

    function speakText(text) {
      if (!('speechSynthesis' in window)) return;
      synth.cancel();
      isSpeaking = false;
      document.getElementById('avatarPulse').style.display = 'none';
      document.getElementById('speechStatusPill').style.display = 'none';

      // Clean HTML tags and math symbols for smooth speech
      const cleanText = text.replace(/<[^>]*>/g, '').replace(/\$+/g, '').replace(/\\text\{([^}]+)\}/g, '$1');
      currentUtterance = new SpeechSynthesisUtterance(cleanText);
      currentUtterance.rate = 0.95;
      currentUtterance.pitch = 1.0;

      currentUtterance.onstart = () => {
        isSpeaking = true;
        document.getElementById('avatarPulse').style.display = 'block';
        document.getElementById('speechStatusPill').style.display = 'inline-block';
        document.getElementById('btnAudioToggle').textContent = '⏸️';
      };

      currentUtterance.onend = () => {
        isSpeaking = false;
        document.getElementById('avatarPulse').style.display = 'none';
        document.getElementById('speechStatusPill').style.display = 'none';
        document.getElementById('btnAudioToggle').textContent = '🔊';
      };

      currentUtterance.onerror = () => {
        isSpeaking = false;
        document.getElementById('avatarPulse').style.display = 'none';
        document.getElementById('speechStatusPill').style.display = 'none';
        document.getElementById('btnAudioToggle').textContent = '🔊';
      };

      synth.speak(currentUtterance);
    }

    function toggleSpeech() {
      if (!synth) return;
      if (synth.speaking && !synth.paused) {
        synth.pause();
        document.getElementById('btnAudioToggle').textContent = '▶️';
        document.getElementById('speechStatusPill').textContent = 'Paused';
      } else if (synth.paused) {
        synth.resume();
        document.getElementById('btnAudioToggle').textContent = '⏸️';
        document.getElementById('speechStatusPill').textContent = 'Speaking...';
      } else {
        const slide = SLIDES[currentSlideIndex];
        speakText(slide.avatar_dialogue);
      }
    }

    function replaySpeech() {
      if (!synth) return;
      const slide = SLIDES[currentSlideIndex];
      speakText(slide.avatar_dialogue);
    }

    // ==========================================
    // BESPOKE INTERACTIVE SIMULATORS (SLIDES 1-16)
    // ==========================================

    function renderSimulator(simId) {
      const canvas = document.getElementById('simCanvas');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const icon = document.getElementById('simIcon');

      canvas.innerHTML = '';
      controls.innerHTML = '';

      switch (simId) {
        case 'mixture_salad_solution_sim':
          simMixtureSaladSolution(canvas, controls, title, icon);
          break;
        case 'alloys_mishraloha_kamsya_sim':
          simAlloysMishralohaKamsya(canvas, controls, title, icon);
          break;
        case 'air_gaseous_mixture_sim':
          simAirGaseousMixture(canvas, controls, title, icon);
          break;
        case 'limewater_co2_milky_sim':
          simLimewaterCO2Milky(canvas, controls, title, icon);
          break;
        case 'aqi_pollutants_monitor_sim':
          simAqiPollutantsMonitor(canvas, controls, title, icon);
          break;
        case 'pure_substance_particles_sim':
          simPureSubstanceParticles(canvas, controls, title, icon);
          break;
        case 'elements_periodic_blocks_sim':
          simElementsPeriodicBlocks(canvas, controls, title, icon);
          break;
        case 'element_classification_triad_sim':
          simElementClassificationTriad(canvas, controls, title, icon);
          break;
        case 'room_temp_liquid_elements_sim':
          simRoomTempLiquidElements(canvas, controls, title, icon);
          break;
        case 'compounds_fixed_ratio_sim':
          simCompoundsFixedRatio(canvas, controls, title, icon);
          break;
        case 'water_electrolysis_hofmann_sim':
          simWaterElectrolysisHofmann(canvas, controls, title, icon);
          break;
        case 'sugar_charring_decomposition_sim':
          simSugarCharringDecomposition(canvas, controls, title, icon);
          break;
        case 'iron_sulfur_mixture_magnet_sim':
          simIronSulfurMixtureMagnet(canvas, controls, title, icon);
          break;
        case 'iron_sulfide_compound_reaction_sim':
          simIronSulfideCompoundReaction(canvas, controls, title, icon);
          break;
        case 'native_compound_minerals_sim':
          simNativeCompoundMinerals(canvas, controls, title, icon);
          break;
        case 'advanced_graphene_dhokra_sim':
          simAdvancedGrapheneDhokra(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = '<div style="color: #94a3b8;">Simulator under development.</div>';
      }
    }

    // 1. Sprout Salad vs Homogeneous Solution Sim
    function simMixtureSaladSolution(canvas, controls, title, icon) {
      title.textContent = 'Heterogeneous Sprout Salad vs Homogeneous Salt Solution';
      icon.textContent = '🥗';
      let mode = 'salad'; // 'salad' or 'solution'
      let zoomLevel = 1;

      function updateSim() {
        if (mode === 'salad') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <defs>
                <radialGradient id="bowlGrad" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stop-color="#1e293b" />
                  <stop offset="90%" stop-color="#0f172a" />
                  <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.5" />
                </radialGradient>
              </defs>

              <!-- Glass Bowl -->
              <ellipse cx="230" cy="240" rx="170" ry="60" fill="url(#bowlGrad)" stroke="#38bdf8" stroke-width="2" />
              <path d="M 60 240 Q 230 330 400 240 Q 400 130 230 130 Q 60 130 60 240 Z" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              
              <!-- Heterogeneous Ingredients Visibly Separated -->
              <!-- Green Gram Sprouts -->
              <g transform="translate(10, 0)">
                <ellipse cx="140" cy="180" rx="14" ry="7" fill="#4ade80" transform="rotate(-25 140 180)" />
                <path d="M 152 180 Q 165 170 170 185" stroke="#bbf7d0" stroke-width="2" fill="none" />

                <ellipse cx="200" cy="210" rx="13" ry="6" fill="#22c55e" transform="rotate(35 200 210)" />
                <path d="M 212 210 Q 225 220 230 210" stroke="#bbf7d0" stroke-width="2" fill="none" />

                <ellipse cx="280" cy="175" rx="15" ry="7" fill="#4ade80" transform="rotate(-15 280 175)" />
                <path d="M 294 175 Q 310 165 315 180" stroke="#bbf7d0" stroke-width="2" fill="none" />

                <ellipse cx="320" cy="215" rx="13" ry="6" fill="#16a34a" transform="rotate(45 320 215)" />
                <path d="M 332 215 Q 345 225 350 215" stroke="#bbf7d0" stroke-width="2" fill="none" />
              </g>

              <!-- Brown Chickpeas -->
              <circle cx="160" cy="225" r="13" fill="#b45309" stroke="#d97706" stroke-width="1.5" />
              <circle cx="250" cy="195" r="14" fill="#92400e" stroke="#d97706" stroke-width="1.5" />
              <circle cx="215" cy="245" r="12" fill="#b45309" stroke="#f59e0b" stroke-width="1.5" />
              <circle cx="300" cy="235" r="13" fill="#92400e" stroke="#d97706" stroke-width="1.5" />

              <!-- Red Diced Tomatoes -->
              <rect x="180" y="160" width="16" height="16" rx="2" fill="#ef4444" stroke="#f87171" stroke-width="1" transform="rotate(20 188 168)" />
              <rect x="260" y="220" width="18" height="18" rx="2" fill="#dc2626" stroke="#f87171" stroke-width="1" transform="rotate(-15 269 229)" />
              <rect x="130" cy="190" width="15" height="15" rx="2" fill="#ef4444" stroke="#f87171" stroke-width="1" transform="rotate(35 137 197)" />

              <!-- Purple Diced Onions -->
              <path d="M 220 170 Q 235 160 245 175 Q 235 185 220 170 Z" fill="#a855f7" stroke="#c084fc" stroke-width="1.5" />
              <path d="M 285 195 Q 300 185 305 200 Q 295 210 285 195 Z" fill="#9333ea" stroke="#c084fc" stroke-width="1.5" />

              <!-- Distinct Boundary Label -->
              <rect x="90" y="25" width="280" height="42" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#f43f5e" stroke-width="1.5" />
              <text x="230" y="44" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">Non-Uniform (Heterogeneous) Mixture</text>
              <text x="230" y="59" fill="#94a3b8" font-size="10" text-anchor="middle">Components visibly segregated • Physical handpicking possible</text>
            </svg>
          `;
        } else {
          // Homogeneous Salt Solution
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <defs>
                <linearGradient id="beakerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="rgba(56, 189, 248, 0.3)" />
                  <stop offset="50%" stop-color="rgba(56, 189, 248, 0.15)" />
                  <stop offset="100%" stop-color="rgba(56, 189, 248, 0.3)" />
                </linearGradient>
              </defs>

              <!-- Beaker Container -->
              <rect x="130" y="70" width="200" height="210" rx="8" fill="url(#beakerGrad)" stroke="#38bdf8" stroke-width="2" />
              <!-- Water Fill -->
              <rect x="134" y="110" width="192" height="166" rx="4" fill="rgba(14, 165, 233, 0.25)" />
              
              <!-- Graduations -->
              <line x1="130" y1="140" x2="150" y2="140" stroke="#38bdf8" stroke-width="2" />
              <text x="156" y="144" fill="#38bdf8" font-size="10">200 mL</text>
              <line x1="130" y1="180" x2="150" y2="180" stroke="#38bdf8" stroke-width="2" />
              <text x="156" y="184" fill="#38bdf8" font-size="10">100 mL</text>
              <line x1="130" y1="220" x2="150" y2="220" stroke="#38bdf8" stroke-width="2" />
              <text x="156" y="224" fill="#38bdf8" font-size="10">50 mL</text>

              <!-- Uniformly dispersed Na+ and Cl- ions -->
              <!-- Water Molecules H2O -->
              <g fill="#94a3b8" opacity="0.6">
                <circle cx="160" cy="130" r="4" /><circle cx="156" cy="126" r="2.5" /><circle cx="164" cy="126" r="2.5" />
                <circle cx="220" cy="150" r="4" /><circle cx="216" cy="146" r="2.5" /><circle cx="224" cy="146" r="2.5" />
                <circle cx="280" cy="135" r="4" /><circle cx="276" cy="131" r="2.5" /><circle cx="284" cy="131" r="2.5" />
                <circle cx="170" cy="210" r="4" /><circle cx="166" cy="206" r="2.5" /><circle cx="174" cy="206" r="2.5" />
                <circle cx="240" cy="230" r="4" /><circle cx="236" cy="226" r="2.5" /><circle cx="244" cy="226" r="2.5" />
                <circle cx="300" cy="215" r="4" /><circle cx="296" cy="211" r="2.5" /><circle cx="304" cy="211" r="2.5" />
              </g>

              <!-- Dispersed Na+ (Blue) and Cl- (Emerald) -->
              <g>
                <circle cx="180" cy="155" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                <text x="180" y="158" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Na⁺</text>

                <circle cx="260" cy="165" r="12" fill="#059669" stroke="#34d399" stroke-width="1.5" />
                <text x="260" y="169" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Cl⁻</text>

                <circle cx="210" cy="190" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                <text x="210" y="193" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Na⁺</text>

                <circle cx="160" cy="245" r="12" fill="#059669" stroke="#34d399" stroke-width="1.5" />
                <text x="160" y="249" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Cl⁻</text>

                <circle cx="280" cy="245" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                <text x="280" y="248" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Na⁺</text>
              </g>

              <!-- Uniform Badge -->
              <rect x="90" y="18" width="280" height="42" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#10b981" stroke-width="1.5" />
              <text x="230" y="37" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Uniform (Homogeneous) Solution</text>
              <text x="230" y="52" fill="#94a3b8" font-size="10" text-anchor="middle">Single transparent phase • Zero visible boundaries</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mode === 'salad' ? 'active' : ''}" id="btnSalad">🥗 Sprout Salad (Heterogeneous)</button>
          <button class="btn-sim ${mode === 'solution' ? 'active' : ''}" id="btnSolution">🧂 Salt in Water (Homogeneous)</button>
        </div>
        <div style="font-size: 0.8rem; color: #cbd5e1; text-align: center; margin-top: 0.4rem;">
          ${mode === 'salad' 
            ? 'Each ingredient (sprout, chickpea, tomato) retains its distinct physical colour, shape, and taste.' 
            : 'Salt ions are sub-microscopically distributed within interparticle spaces; every single drop tastes equally salty!'}
        </div>
      `;

      document.getElementById('btnSalad').onclick = () => { mode = 'salad'; updateSim(); };
      document.getElementById('btnSolution').onclick = () => { mode = 'solution'; updateSim(); };

      updateSim();
    }

    // 2. Alloys & Ancient Mishraloha Simulator
    function simAlloysMishralohaKamsya(canvas, controls, title, icon) {
      title.textContent = 'Alloys & Ancient Indian Metallurgy (Mishraloha)';
      icon.textContent = '🛡️';
      let alloy = 'bronze'; // 'bronze', 'brass', 'steel'

      function updateSim() {
        let name = '', cuPct = 0, otherName = '', otherPct = 0, colorPrimary = '', colorSecondary = '', heritage = '';
        if (alloy === 'bronze') {
          name = 'Bronze (Kamsya • कांस्य)';
          cuPct = 80;
          otherName = 'Tin (Vanga - Sn)';
          otherPct = 20;
          colorPrimary = '#ea580c'; // Copper
          colorSecondary = '#94a3b8'; // Tin
          heritage = 'Ancient Sushruta & Charaka Samhita: "Kamsya (4 parts Tamra + 1 part Vanga) balances Pitta and purifies food."';
        } else if (alloy === 'brass') {
          name = 'Brass (Pital • पीतल)';
          cuPct = 70;
          otherName = 'Zinc (Yashada - Zn)';
          otherPct = 30;
          colorPrimary = '#d97706';
          colorSecondary = '#cbd5e1';
          heritage = 'Revered for resonant temple bells and lustrous golden corrosion-resistant utensils.';
        } else {
          name = 'Stainless Steel';
          cuPct = 73; // Iron
          otherName = 'Cr (18%) + Ni (8%) + C (1%)';
          otherPct = 27;
          colorPrimary = '#64748b'; // Iron
          colorSecondary = '#38bdf8'; // Cr/Ni
          heritage = 'Chromium creates a self-healing micro-thin oxide film that stops rust permanently!';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Metallic Lattice Illustration -->
            <rect x="25" y="25" width="250" height="230" rx="12" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="150" y="48" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Metallic Solid Solution Lattice</text>

            <!-- Regular Grid of Primary Metal Atoms + Interspersed Solute Atoms -->
            <g transform="translate(45, 60)">
              ${(() => {
                let atoms = '';
                const rows = 4, cols = 5;
                for (let r = 0; r < rows; r++) {
                  for (let c = 0; c < cols; c++) {
                    const cx = c * 42 + 20;
                    const cy = r * 42 + 20;
                    const isSolute = (r + c * 2) % 4 === 1;
                    const fill = isSolute ? colorSecondary : colorPrimary;
                    const rad = isSolute ? 15 : 18;
                    const label = isSolute ? (alloy === 'bronze' ? 'Sn' : alloy === 'brass' ? 'Zn' : 'Cr') : (alloy === 'steel' ? 'Fe' : 'Cu');
                    atoms += `
                      <circle cx="${cx}" cy="${cy}" r="${rad}" fill="${fill}" stroke="#ffffff" stroke-opacity="0.4" stroke-width="1.5" />
                      <text x="${cx}" y="${cy + 4}" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">${label}</text>
                    `;
                  }
                }
                return atoms;
              })()}
            </g>

            <!-- Dislocation Pinning Arrow -->
            <path d="M 60 235 L 240 235" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3" />
            <text x="150" y="250" fill="#f43f5e" font-size="9" text-anchor="middle">Diff-sized solute atoms lock layers • High Hardness!</text>

            <!-- Heritage & Stats Card -->
            <rect x="290" y="25" width="150" height="230" rx="12" fill="rgba(30, 41, 59, 0.8)" stroke="#f59e0b" stroke-width="1.5" />
            <text x="365" y="50" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">${name.split(' ')[0]}</text>
            
            <circle cx="330" cy="85" r="10" fill="${colorPrimary}" />
            <text x="350" y="89" fill="#cbd5e1" font-size="10">${alloy === 'steel' ? 'Fe' : 'Cu'}: ${cuPct}%</text>

            <circle cx="330" cy="115" r="9" fill="${colorSecondary}" />
            <text x="350" y="119" fill="#cbd5e1" font-size="10">${alloy === 'steel' ? 'Alloy' : otherName.split(' ')[0]}: ${otherPct}%</text>

            <rect x="302" y="140" width="126" height="1" fill="rgba(255, 255, 255, 0.15)" />
            <text x="365" y="160" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Uniform Solid Mixture</text>
            <text x="365" y="178" fill="#94a3b8" font-size="9" text-anchor="middle">Non-Separable by Filter</text>
            <text x="365" y="195" fill="#94a3b8" font-size="9" text-anchor="middle">Resistant to Oxidation</text>
            <text x="365" y="215" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Retains Properties</text>

            <!-- Ancient Heritage Citation -->
            <rect x="25" y="265" width="415" height="45" rx="8" fill="rgba(245, 158, 11, 0.1)" stroke="#f59e0b" stroke-width="1" />
            <text x="232" y="285" fill="#fde68a" font-size="9.5" text-anchor="middle">${heritage}</text>
            <text x="232" y="300" fill="#94a3b8" font-size="8.5" text-anchor="middle">Alloys are homogeneous mixtures of metals to amplify mechanical resilience and prevent decay.</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${alloy === 'bronze' ? 'active' : ''}" id="btnBronze">🥉 Bronze (Kamsya - Cu + Sn)</button>
          <button class="btn-sim ${alloy === 'brass' ? 'active' : ''}" id="btnBrass">🎷 Brass (Cu + Zn)</button>
          <button class="btn-sim ${alloy === 'steel' ? 'active' : ''}" id="btnSteel">⚔️ Stainless Steel (Fe + Cr + Ni)</button>
        </div>
      `;

      document.getElementById('btnBronze').onclick = () => { alloy = 'bronze'; updateSim(); };
      document.getElementById('btnBrass').onclick = () => { alloy = 'brass'; updateSim(); };
      document.getElementById('btnSteel').onclick = () => { alloy = 'steel'; updateSim(); };

      updateSim();
    }

    // 3. Air as Gaseous Mixture Sim
    function simAirGaseousMixture(canvas, controls, title, icon) {
      title.textContent = 'Earth\'s Atmosphere: A Homogeneous Gaseous Mixture';
      icon.textContent = '💨';
      let activeFilter = 'all'; // 'all', 'n2', 'o2', 'ar', 'co2'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Gas Container Chamber -->
            <rect x="25" y="25" width="260" height="270" rx="12" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="155" y="48" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Atmospheric Gas Envelope</text>

            <!-- Bouncing Gas Molecules (N2 = 78%, O2 = 21%, Ar = 0.9%, CO2 = 0.04%) -->
            <g transform="translate(30, 55)">
              <!-- N2 Diatomic Blue -->
              <g opacity="${activeFilter === 'all' || activeFilter === 'n2' ? '1' : '0.1'}">
                <ellipse cx="30" cy="40" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="38" cy="40" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="80" cy="90" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="88" cy="90" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="150" cy="60" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="158" cy="60" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="200" cy="110" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="208" cy="110" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="60" cy="160" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="68" cy="160" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="140" cy="180" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="148" cy="180" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="190" cy="210" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="198" cy="210" rx="6" ry="4" fill="#38bdf8" />
                <ellipse cx="110" cy="130" rx="6" ry="4" fill="#38bdf8" /><ellipse cx="118" cy="130" rx="6" ry="4" fill="#38bdf8" />
              </g>

              <!-- O2 Diatomic Red -->
              <g opacity="${activeFilter === 'all' || activeFilter === 'o2' ? '1' : '0.1'}">
                <ellipse cx="40" cy="110" rx="7" ry="5" fill="#ef4444" /><ellipse cx="50" cy="110" rx="7" ry="5" fill="#ef4444" />
                <ellipse cx="160" cy="120" rx="7" ry="5" fill="#ef4444" /><ellipse cx="170" cy="120" rx="7" ry="5" fill="#ef4444" />
                <ellipse cx="100" cy="200" rx="7" ry="5" fill="#ef4444" /><ellipse cx="110" cy="200" rx="7" ry="5" fill="#ef4444" />
              </g>

              <!-- Ar Monoatomic Green -->
              <g opacity="${activeFilter === 'all' || activeFilter === 'ar' ? '1' : '0.1'}">
                <circle cx="215" cy="50" r="7" fill="#10b981" />
              </g>

              <!-- CO2 Triatomic Purple -->
              <g opacity="${activeFilter === 'all' || activeFilter === 'co2' ? '1' : '0.1'}">
                <circle cx="70" cy="50" r="4.5" fill="#c084fc" />
                <circle cx="62" cy="50" r="3" fill="#f43f5e" /><circle cx="78" cy="50" r="3" fill="#f43f5e" />
              </g>
            </g>

            <!-- Atmosphere Breakdown Card -->
            <rect x="295" y="25" width="145" height="270" rx="12" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="367" y="48" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Air Composition</text>

            <!-- Percentage Bars -->
            <g transform="translate(305, 65)">
              <text x="0" y="12" fill="#38bdf8" font-size="10" font-weight="bold">Nitrogen (N₂)</text>
              <text x="125" y="12" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="end">78%</text>
              <rect x="0" y="18" width="125" height="6" rx="3" fill="rgba(255, 255, 255, 0.1)" />
              <rect x="0" y="18" width="97.5" height="6" rx="3" fill="#38bdf8" />

              <text x="0" y="47" fill="#ef4444" font-size="10" font-weight="bold">Oxygen (O₂)</text>
              <text x="125" y="47" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="end">21%</text>
              <rect x="0" y="53" width="125" height="6" rx="3" fill="rgba(255, 255, 255, 0.1)" />
              <rect x="0" y="53" width="26.2" height="6" rx="3" fill="#ef4444" />

              <text x="0" y="82" fill="#10b981" font-size="10" font-weight="bold">Argon (Ar)</text>
              <text x="125" y="82" fill="#10b981" font-size="10" font-weight="bold" text-anchor="end">0.9%</text>
              <rect x="0" y="88" width="125" height="6" rx="3" fill="rgba(255, 255, 255, 0.1)" />
              <rect x="0" y="88" width="8" height="6" rx="3" fill="#10b981" />

              <text x="0" y="117" fill="#c084fc" font-size="10" font-weight="bold">Carbon Dioxide (CO₂)</text>
              <text x="125" y="117" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="end">0.04%</text>
              <rect x="0" y="123" width="125" height="6" rx="3" fill="rgba(255, 255, 255, 0.1)" />
              <rect x="0" y="123" width="3" height="6" rx="3" fill="#c084fc" />

              <text x="0" y="152" fill="#94a3b8" font-size="9">Water vapor & others: variable</text>

              <rect x="0" y="175" width="125" height="42" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
              <text x="62" y="193" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Physical Mixture Proof</text>
              <text x="62" y="207" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Separated via fractional distillation</text>
            </g>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${activeFilter === 'all' ? 'active' : ''}" id="btnAirAll">All Gases</button>
          <button class="btn-sim ${activeFilter === 'n2' ? 'active' : ''}" id="btnAirN2">🔵 N₂ (78%)</button>
          <button class="btn-sim ${activeFilter === 'o2' ? 'active' : ''}" id="btnAirO2">🔴 O₂ (21%)</button>
          <button class="btn-sim ${activeFilter === 'ar' ? 'active' : ''}" id="btnAirAr">🟢 Ar (0.9%)</button>
          <button class="btn-sim ${activeFilter === 'co2' ? 'active' : ''}" id="btnAirCO2">🟣 CO₂ (0.04%)</button>
        </div>
      `;

      document.getElementById('btnAirAll').onclick = () => { activeFilter = 'all'; updateSim(); };
      document.getElementById('btnAirN2').onclick = () => { activeFilter = 'n2'; updateSim(); };
      document.getElementById('btnAirO2').onclick = () => { activeFilter = 'o2'; updateSim(); };
      document.getElementById('btnAirAr').onclick = () => { activeFilter = 'ar'; updateSim(); };
      document.getElementById('btnAirCO2').onclick = () => { activeFilter = 'co2'; updateSim(); };

      updateSim();
    }

    // 4. Lime Water CO2 Milky Precipitate Sim
    function simLimewaterCO2Milky(canvas, controls, title, icon) {
      title.textContent = 'The Carbon Dioxide Lime Water Confirmation Test';
      icon.textContent = '🧪';
      let state = 'clear'; // 'clear', 'milky', 'excess'

      function updateSim() {
        let liquidColor = 'rgba(56, 189, 248, 0.15)';
        let statusTitle = 'Fresh Clear Lime Water';
        let statusSub = 'Ca(OH)₂ (aq) solution is completely transparent';
        let equation = 'Ca(OH)₂ (aq) [Calcium Hydroxide]';

        if (state === 'milky') {
          liquidColor = 'rgba(255, 255, 255, 0.85)';
          statusTitle = 'Milky Precipitate Formed!';
          statusSub = 'Insoluble CaCO₃ suspended micro-crystals turn liquid milky white';
          equation = 'Ca(OH)₂ + CO₂ → CaCO₃ ↓ (white insoluble ppt) + H₂O';
        } else if (state === 'excess') {
          liquidColor = 'rgba(56, 189, 248, 0.2)';
          statusTitle = 'Milkiness Disappears with Excess CO₂!';
          statusSub = 'Insoluble CaCO₃ converts into soluble Calcium Bicarbonate Ca(HCO₃)₂';
          equation = 'CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂ (aq) [Soluble Bicarbonate]';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Test Tube Stand -->
            <rect x="70" y="270" width="140" height="15" rx="3" fill="#475569" />
            <rect x="135" y="100" width="10" height="170" fill="#475569" />
            <rect x="120" y="130" width="40" height="8" rx="2" fill="#64748b" />

            <!-- Test Tube -->
            <path d="M 160 80 L 160 230 A 25 25 0 0 0 210 230 L 210 80 Z" fill="rgba(30, 41, 59, 0.3)" stroke="#38bdf8" stroke-width="2" />
            
            <!-- Liquid Fill inside tube -->
            <path d="M 162 140 L 162 230 A 23 23 0 0 0 208 230 L 208 140 Z" fill="${liquidColor}" />

            <!-- Delivery Straw (Blowing in) -->
            <path d="M 230 30 L 185 90 L 185 220" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round" />
            
            <!-- Rising Gas Bubbles -->
            ${state !== 'clear' ? `
              <circle cx="185" cy="210" r="3" fill="#ffffff" opacity="0.8" />
              <circle cx="178" cy="180" r="4" fill="#ffffff" opacity="0.8" />
              <circle cx="192" cy="155" r="3.5" fill="#ffffff" opacity="0.8" />
            ` : ''}

            <!-- Exhaled breath indicator -->
            <text x="260" y="45" fill="#f59e0b" font-size="11" font-weight="bold">Exhaled Breath (CO₂)</text>
            <path d="M 255 48 L 235 48" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)" />

            <!-- Reaction Card -->
            <rect x="235" y="80" width="205" height="180" rx="10" fill="rgba(15, 23, 42, 0.9)" stroke="${state === 'milky' ? '#10b981' : '#38bdf8'}" stroke-width="1.5" />
            <text x="337" y="105" fill="${state === 'milky' ? '#34d399' : '#38bdf8'}" font-size="11" font-weight="bold" text-anchor="middle">${statusTitle}</text>
            
            <foreignObject x="245" y="118" width="185" height="130">
              <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 0.78rem; color: #cbd5e1; line-height: 1.4;">
                <p style="margin-bottom: 0.5rem;">${statusSub}</p>
                <div style="background: rgba(0,0,0,0.4); padding: 0.4rem; border-radius: 6px; font-size: 0.72rem; color: #fbbf24; font-family: monospace;">
                  ${equation}
                </div>
              </div>
            </foreignObject>

            <rect x="30" y="295" width="400" height="20" rx="4" fill="rgba(15, 23, 42, 0.7)" />
            <text x="230" y="309" fill="#94a3b8" font-size="9" text-anchor="middle">Standard test to distinguish Carbon Dioxide from other atmospheric gases.</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${state === 'clear' ? 'active' : ''}" id="btnLTFresh">Clear Lime Water</button>
          <button class="btn-sim ${state === 'milky' ? 'active' : ''}" id="btnLTExhale">🌬️ Bubble Exhaled CO₂ (Milky)</button>
          <button class="btn-sim ${state === 'excess' ? 'active' : ''}" id="btnLTExcess">Excess CO₂ (Clear Again)</button>
        </div>
      `;

      document.getElementById('btnLTFresh').onclick = () => { state = 'clear'; updateSim(); };
      document.getElementById('btnLTExhale').onclick = () => { state = 'milky'; updateSim(); };
      document.getElementById('btnLTExcess').onclick = () => { state = 'excess'; updateSim(); };

      updateSim();
    }

    // 5. Air Quality Index (AQI) & Pollutant Monitor Sim
    function simAqiPollutantsMonitor(canvas, controls, title, icon) {
      title.textContent = 'Air Quality Index (AQI) & Particulate Pollutant Monitor';
      icon.textContent = '🌫️';
      let aqiValue = 45; // 0 to 500

      function updateSim() {
        let category = '', catColor = '', advisory = '', pm25 = Math.round(aqiValue * 0.4);
        if (aqiValue <= 50) {
          category = 'Good (0–50)';
          catColor = '#10b981';
          advisory = 'Air quality is satisfactory; air pollution poses little or no risk for outdoor sports.';
        } else if (aqiValue <= 100) {
          category = 'Satisfactory (51–100)';
          catColor = '#84cc16';
          advisory = 'Minor breathing discomfort to sensitive people; overall clean.';
        } else if (aqiValue <= 200) {
          category = 'Moderate (101–200)';
          catColor = '#f59e0b';
          advisory = 'Breathing discomfort to people with lungs, asthma, and heart diseases.';
        } else if (aqiValue <= 300) {
          category = 'Poor (201–300)';
          catColor = '#f97316';
          advisory = 'Breathing discomfort to most people on prolonged exposure; avoid heavy exertion.';
        } else if (aqiValue <= 400) {
          category = 'Very Poor (301–400)';
          catColor = '#ef4444';
          advisory = 'Respiratory illness on prolonged exposure; vulnerable groups must stay indoors.';
        } else {
          category = 'Severe (401–500)';
          catColor = '#7f1d1d';
          advisory = 'Affects healthy people and seriously impacts those with existing diseases; use N95 masks.';
        }

        const angle = (aqiValue / 500) * 180 - 90; // -90 deg to +90 deg

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Cityscape Background with haze intensity -->
            <rect x="25" y="25" width="410" height="130" rx="10" fill="#0f172a" />
            <!-- Buildings -->
            <rect x="50" y="70" width="40" height="85" fill="#1e293b" />
            <rect x="100" y="50" width="55" height="105" fill="#334155" />
            <rect x="170" y="80" width="45" height="75" fill="#1e293b" />
            <rect x="230" y="40" width="60" height="115" fill="#334155" />
            <rect x="305" y="75" width="50" height="80" fill="#1e293b" />
            <rect x="370" y="60" width="45" height="95" fill="#334155" />

            <!-- Haze Overlayer based on AQI -->
            <rect x="25" y="25" width="410" height="130" rx="10" fill="rgba(120, 113, 108, ${aqiValue / 650})" />

            <!-- AQI Semi-Circle Speedometer Gauge -->
            <g transform="translate(230, 240)">
              <!-- Arc Background -->
              <path d="M -110 0 A 110 110 0 0 1 110 0" fill="none" stroke="rgba(255, 255, 255, 0.1)" stroke-width="20" stroke-linecap="round" />
              <!-- Color Bands -->
              <path d="M -110 0 A 110 110 0 0 1 -77 -77" fill="none" stroke="#10b981" stroke-width="20" />
              <path d="M -77 -77 A 110 110 0 0 1 -34 -104" fill="none" stroke="#84cc16" stroke-width="20" />
              <path d="M -34 -104 A 110 110 0 0 1 34 -104" fill="none" stroke="#f59e0b" stroke-width="20" />
              <path d="M 34 -104 A 110 110 0 0 1 77 -77" fill="none" stroke="#f97316" stroke-width="20" />
              <path d="M 77 -77 A 110 110 0 0 1 110 0" fill="none" stroke="#ef4444" stroke-width="20" />

              <!-- Needle Pointer -->
              <g transform="rotate(${angle})">
                <line x1="0" y1="0" x2="0" y2="-95" stroke="#ffffff" stroke-width="3" stroke-linecap="round" />
                <circle cx="0" cy="0" r="8" fill="#38bdf8" />
              </g>

              <text x="0" y="-30" fill="${catColor}" font-size="28" font-weight="900" text-anchor="middle">${aqiValue}</text>
              <text x="0" y="-12" fill="#cbd5e1" font-size="10" text-anchor="middle">AQI Score</text>
            </g>

            <!-- Pollutant & Advisory Card -->
            <rect x="25" y="255" width="410" height="55" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${catColor}" stroke-width="1.5" />
            <text x="38" y="275" fill="${catColor}" font-size="12" font-weight="bold">${category}</text>
            <text x="38" y="295" fill="#cbd5e1" font-size="9.5">${advisory}</text>
            <text x="420" y="275" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="end">PM₂.₅: ${pm25} µg/m³</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🎚️</span> Air Quality Index (AQI):</span>
          <input type="range" class="sim-slider" id="aqiSlider" min="10" max="490" value="${aqiValue}">
          <span class="control-value" id="aqiValText">${aqiValue}</span>
        </div>
        <div style="display: flex; gap: 0.4rem; justify-content: center; margin-top: 0.3rem;">
          <button class="btn-sim" id="btnAQIClean">Clean Hills (30)</button>
          <button class="btn-sim" id="btnAQIUrban">Urban Day (120)</button>
          <button class="btn-sim" id="btnAQISmog">Smog Inversion (360)</button>
        </div>
      `;

      const slider = document.getElementById('aqiSlider');
      slider.oninput = (e) => {
        aqiValue = parseInt(e.target.value);
        document.getElementById('aqiValText').textContent = aqiValue;
        updateSim();
      };

      document.getElementById('btnAQIClean').onclick = () => { aqiValue = 30; slider.value = 30; document.getElementById('aqiValText').textContent = 30; updateSim(); };
      document.getElementById('btnAQIUrban').onclick = () => { aqiValue = 120; slider.value = 120; document.getElementById('aqiValText').textContent = 120; updateSim(); };
      document.getElementById('btnAQISmog').onclick = () => { aqiValue = 360; slider.value = 360; document.getElementById('aqiValText').textContent = 360; updateSim(); };

      updateSim();
    }

    // 6. Pure Substances: Everyday Adulteration vs Scientific Purity
    function simPureSubstanceParticles(canvas, controls, title, icon) {
      title.textContent = 'Scientific Pure Substances vs Everyday Adulteration';
      icon.textContent = '🥛';
      let mode = 'milk'; // 'milk' or 'gold' or 'water'

      function updateSim() {
        if (mode === 'milk') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Everyday Milk Packet vs Microscopic Reality -->
              <rect x="25" y="25" width="180" height="270" rx="12" fill="rgba(30, 41, 59, 0.7)" stroke="#38bdf8" stroke-width="1.5" />
              <text x="115" y="52" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Market "Pure" Milk</text>
              
              <!-- Milk Pouch Graphic -->
              <rect x="55" y="80" width="120" height="150" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="2" />
              <text x="115" y="125" fill="#0284c7" font-size="14" font-weight="900" text-anchor="middle">PURE MILK</text>
              <text x="115" y="145" fill="#64748b" font-size="9" text-anchor="middle">100% Unadulterated</text>
              <text x="115" y="185" fill="#10b981" font-size="9" font-weight="bold" text-anchor="middle">Everyday Meaning: No added water</text>

              <!-- Microscope Magnification Arrow -->
              <path d="M 210 155 L 245 155" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)" />
              <text x="228" y="145" fill="#f59e0b" font-size="8" text-anchor="middle">Zoom</text>

              <!-- Sub-Microscopic Reality (Mixture!) -->
              <rect x="255" y="25" width="180" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#ef4444" stroke-width="1.5" />
              <text x="345" y="52" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Scientific View: Mixture!</text>

              <!-- Multi-particle chaos inside milk -->
              <!-- Water particles (blue small) -->
              <circle cx="280" cy="80" r="4" fill="#38bdf8" /><circle cx="310" cy="95" r="4" fill="#38bdf8" />
              <circle cx="350" cy="75" r="4" fill="#38bdf8" /><circle cx="380" cy="90" r="4" fill="#38bdf8" />
              <circle cx="300" cy="180" r="4" fill="#38bdf8" /><circle cx="370" cy="210" r="4" fill="#38bdf8" />
              
              <!-- Fat Globules (yellow large) -->
              <circle cx="335" cy="130" r="18" fill="#facc15" stroke="#eab308" stroke-width="2" />
              <text x="335" y="134" fill="#713f12" font-size="8" font-weight="bold" text-anchor="middle">Fat</text>

              <circle cx="285" cy="220" r="14" fill="#facc15" stroke="#eab308" stroke-width="2" />
              <text x="285" y="224" fill="#713f12" font-size="7" font-weight="bold" text-anchor="middle">Fat</text>

              <!-- Protein Casein Micelles (red/purple) -->
              <circle cx="290" cy="135" r="10" fill="#c084fc" />
              <text x="290" y="139" fill="#3b0764" font-size="7" font-weight="bold" text-anchor="middle">Prot</text>

              <circle cx="385" cy="160" r="11" fill="#c084fc" />
              <text x="385" y="164" fill="#3b0764" font-size="7" font-weight="bold" text-anchor="middle">Prot</text>

              <!-- Minerals / Lactose -->
              <circle cx="350" cy="245" r="7" fill="#4ade80" />

              <rect x="265" y="255" width="160" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)" />
              <text x="345" y="274" fill="#fca5a5" font-size="8.5" font-weight="bold" text-anchor="middle">NOT a Pure Substance!</text>
            </svg>
          `;
        } else {
          // Scientifically Pure Substance (Gold or Distilled Water)
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5" />
              <text x="230" y="52" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">
                ${mode === 'gold' ? '24-Karat Gold (Au) • 100% Identical Constituent Atoms' : 'Pure Distilled Water (H₂O) • 100% Identical Molecules'}
              </text>

              <!-- Orderly Single-Type Particle Lattice -->
              <g transform="translate(65, 75)">
                ${(() => {
                  let str = '';
                  for (let r = 0; r < 4; r++) {
                    for (let c = 0; c < 8; c++) {
                      const cx = c * 42 + 20;
                      const cy = r * 38 + 20;
                      if (mode === 'gold') {
                        str += `
                          <circle cx="${cx}" cy="${cy}" r="16" fill="#f59e0b" stroke="#fde68a" stroke-width="1.5" />
                          <text x="${cx}" y="${cy + 4}" fill="#78350f" font-size="8.5" font-weight="bold" text-anchor="middle">Au</text>
                        `;
                      } else {
                        str += `
                          <circle cx="${cx}" cy="${cy}" r="9" fill="#0284c7" />
                          <circle cx="${cx - 8}" cy="${cy - 7}" r="5" fill="#e0f2fe" />
                          <circle cx="${cx + 8}" cy="${cy - 7}" r="5" fill="#e0f2fe" />
                        `;
                      }
                    }
                  }
                  return str;
                })()}
              </g>

              <rect x="45" y="245" width="370" height="38" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1" />
              <text x="230" y="262" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Scientifically Pure: Single constituent particle type throughout</text>
              <text x="230" y="276" fill="#94a3b8" font-size="9" text-anchor="middle">Has sharp, invariant melting point, fixed boiling point, and uniform density.</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mode === 'milk' ? 'active' : ''}" id="btnMilk">🥛 Milk (Everyday Pure vs Science Mixture)</button>
          <button class="btn-sim ${mode === 'gold' ? 'active' : ''}" id="btnGold">🥇 24K Gold Element (Scientific Pure)</button>
          <button class="btn-sim ${mode === 'water' ? 'active' : ''}" id="btnWater">💧 Distilled Water Compound (Scientific Pure)</button>
        </div>
      `;

      document.getElementById('btnMilk').onclick = () => { mode = 'milk'; updateSim(); };
      document.getElementById('btnGold').onclick = () => { mode = 'gold'; updateSim(); };
      document.getElementById('btnWater').onclick = () => { mode = 'water'; updateSim(); };

      updateSim();
    }

    // 7. Elements: Periodic Table & Fundamental Units
    function simElementsPeriodicBlocks(canvas, controls, title, icon) {
      title.textContent = 'Elements: 118 Fundamental Chemical Building Blocks';
      icon.textContent = '🧱';
      let elemType = 'mono'; // 'mono', 'di', 'poly'

      function updateSim() {
        let titleText = '', formula = '', desc = '';
        if (elemType === 'mono') {
          titleText = 'Monoatomic Elements (Noble Gases)';
          formula = 'Helium (He), Argon (Ar), Neon (Ne)';
          desc = 'Exist as isolated individual atoms without bonding to each other.';
        } else if (elemType === 'di') {
          titleText = 'Diatomic Molecules of Elements';
          formula = 'Oxygen (O₂), Hydrogen (H₂), Nitrogen (N₂)';
          desc = 'Two identical atoms chemically bound into stable diatomic pairs.';
        } else {
          titleText = 'Polyatomic Molecules of Elements';
          formula = 'Sulfur (S₈ crown ring), Phosphorus (P₄ tetrahedron)';
          desc = 'Eight identical sulfur atoms bond in a puckered 8-membered crown ring.';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="52" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">${titleText}</text>
            <text x="230" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">${formula}</text>

            <g transform="translate(45, 95)">
              ${elemType === 'mono' ? `
                <!-- Helium Monoatomic Atoms -->
                <circle cx="80" cy="50" r="18" fill="#38bdf8" stroke="#7dd3fc" stroke-width="2" />
                <text x="80" y="55" fill="#0c4a6e" font-size="11" font-weight="bold" text-anchor="middle">He</text>

                <circle cx="190" cy="80" r="18" fill="#38bdf8" stroke="#7dd3fc" stroke-width="2" />
                <text x="190" y="85" fill="#0c4a6e" font-size="11" font-weight="bold" text-anchor="middle">He</text>

                <circle cx="300" cy="45" r="18" fill="#38bdf8" stroke="#7dd3fc" stroke-width="2" />
                <text x="300" y="50" fill="#0c4a6e" font-size="11" font-weight="bold" text-anchor="middle">He</text>

                <circle cx="130" cy="120" r="18" fill="#38bdf8" stroke="#7dd3fc" stroke-width="2" />
                <text x="130" y="125" fill="#0c4a6e" font-size="11" font-weight="bold" text-anchor="middle">He</text>

                <circle cx="260" cy="115" r="18" fill="#38bdf8" stroke="#7dd3fc" stroke-width="2" />
                <text x="260" y="120" fill="#0c4a6e" font-size="11" font-weight="bold" text-anchor="middle">He</text>
              ` : elemType === 'di' ? `
                <!-- Oxygen Diatomic Pairs -->
                <g transform="translate(60, 40)">
                  <circle cx="0" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <circle cx="22" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <text x="11" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">O₂</text>
                </g>

                <g transform="translate(230, 40)">
                  <circle cx="0" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <circle cx="22" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <text x="11" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">O₂</text>
                </g>

                <g transform="translate(150, 100)">
                  <circle cx="0" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <circle cx="22" cy="0" r="16" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5" />
                  <text x="11" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">O₂</text>
                </g>
              ` : `
                <!-- Sulfur S8 Crown Ring -->
                <g transform="translate(185, 80)">
                  <!-- 8 Sulfur atoms in crown arrangement -->
                  <circle cx="-50" cy="-20" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="-30" cy="20" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="0" cy="-25" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="30" cy="20" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="50" cy="-20" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="35" cy="-45" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="0" cy="-10" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <circle cx="-35" cy="-45" r="13" fill="#eab308" stroke="#fef08a" stroke-width="1.5" />
                  <!-- Bonds -->
                  <path d="M -50 -20 L -30 20 L 0 -10 L 30 20 L 50 -20 L 35 -45 L 0 -25 L -35 -45 Z" stroke="#facc15" stroke-width="2.5" fill="none" opacity="0.6" />
                  <text x="0" y="55" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Octasulfur Ring (S₈)</text>
                </g>
              `}
            </g>

            <rect x="45" y="245" width="370" height="38" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="262" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">${desc}</text>
            <text x="230" y="276" fill="#cbd5e1" font-size="8.5" text-anchor="middle">All molecules contain ONLY ONE TYPE of atom — confirming their identity as Elements!</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${elemType === 'mono' ? 'active' : ''}" id="btnMono">🎈 Monoatomic (He, Ar)</button>
          <button class="btn-sim ${elemType === 'di' ? 'active' : ''}" id="btnDi">💨 Diatomic (O₂, H₂, N₂)</button>
          <button class="btn-sim ${elemType === 'poly' ? 'active' : ''}" id="btnPoly">👑 Polyatomic (S₈ Crown, P₄)</button>
        </div>
      `;

      document.getElementById('btnMono').onclick = () => { elemType = 'mono'; updateSim(); };
      document.getElementById('btnDi').onclick = () => { elemType = 'di'; updateSim(); };
      document.getElementById('btnPoly').onclick = () => { elemType = 'poly'; updateSim(); };

      updateSim();
    }

    // 8. Element Classification: Metals, Non-Metals, Metalloid Circuit
    function simElementClassificationTriad(canvas, controls, title, icon) {
      title.textContent = 'Conductivity Circuit: Metals, Non-Metals & Metalloids';
      icon.textContent = '💡';
      let mat = 'metal'; // 'metal' (Copper), 'nonmetal' (Sulfur), 'metalloid' (Silicon)
      let temp = 25; // deg C

      function updateSim() {
        let bulbOn = false, bulbBrightness = 0, current = 0, matName = '', matClass = '';
        if (mat === 'metal') {
          bulbOn = true;
          bulbBrightness = Math.max(0.4, 1.0 - (temp - 25) * 0.002);
          current = (250 - temp * 0.3).toFixed(1);
          matName = 'Copper (Cu) • Lustrous Metal';
          matClass = 'Conductor (High free electrons; resistance rises slightly with heat)';
        } else if (mat === 'nonmetal') {
          bulbOn = false;
          bulbBrightness = 0;
          current = 0.0;
          matName = 'Sulfur (S) • Brittle Non-Metal';
          matClass = 'Insulator (Zero free electrons; circuit remains broken)';
        } else {
          // Metalloid (Silicon)
          bulbOn = temp > 40;
          bulbBrightness = Math.min(1.0, (temp / 120));
          current = (temp * 1.5).toFixed(1);
          matName = 'Silicon (Si) • Metalloid';
          matClass = 'Semiconductor (Conductivity increases dramatically with temperature!)';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Circuit Diagram -->
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="50" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">${matName}</text>
            
            <!-- Battery -->
            <rect x="60" y="130" width="30" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
            <line x1="75" y1="120" x2="75" y2="130" stroke="#ef4444" stroke-width="3" />
            <line x1="75" y1="180" x2="75" y2="190" stroke="#38bdf8" stroke-width="3" />
            <text x="50" y="160" fill="#f87171" font-size="12" font-weight="bold">9V</text>

            <!-- Test Material Rod -->
            <g transform="translate(190, 85)">
              <rect x="0" y="0" width="80" height="20" rx="4" 
                fill="${mat === 'metal' ? '#f59e0b' : mat === 'nonmetal' ? '#eab308' : '#64748b'}" 
                stroke="#ffffff" stroke-width="1.5" />
              <text x="40" y="14" fill="#000" font-size="9" font-weight="bold" text-anchor="middle">
                ${mat === 'metal' ? 'Copper' : mat === 'nonmetal' ? 'Sulfur' : 'Silicon'}
              </text>
            </g>

            <!-- Test Clips -->
            <circle cx="190" cy="95" r="5" fill="#38bdf8" />
            <circle cx="270" cy="95" r="5" fill="#38bdf8" />

            <!-- Light Bulb -->
            <g transform="translate(340, 140)">
              <circle cx="20" cy="20" r="22" 
                fill="${bulbOn ? `rgba(250, 204, 21, ${bulbBrightness})` : 'rgba(100, 116, 139, 0.2)'}" 
                stroke="${bulbOn ? '#facc15' : '#475569'}" stroke-width="2" />
              ${bulbOn ? `
                <!-- Glowing Rays -->
                <line x1="20" y1="-8" x2="20" y2="-18" stroke="#facc15" stroke-width="2" />
                <line x1="45" y1="20" x2="55" y2="20" stroke="#facc15" stroke-width="2" />
                <line x1="38" y1="3" x2="46" y2="-5" stroke="#facc15" stroke-width="2" />
              ` : ''}
              <path d="M 12 25 Q 20 10 28 25" stroke="#ffffff" stroke-width="1.5" fill="none" />
              <rect x="13" y="38" width="14" height="10" fill="#64748b" />
            </g>

            <!-- Connecting Wires -->
            <path d="M 75 120 L 75 95 L 190 95" stroke="#38bdf8" stroke-width="2.5" fill="none" />
            <path d="M 270 95 L 360 95 L 360 140" stroke="#38bdf8" stroke-width="2.5" fill="none" />
            <path d="M 360 188 L 360 215 L 75 215 L 75 190" stroke="#38bdf8" stroke-width="2.5" fill="none" />

            <!-- Ammeter Gauge -->
            <rect x="175" y="185" width="110" height="50" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#10b981" stroke-width="1.5" />
            <text x="230" y="205" fill="#cbd5e1" font-size="9" text-anchor="middle">Ammeter Reading</text>
            <text x="230" y="225" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">${current} mA</text>

            <!-- Classification Note -->
            <rect x="45" y="250" width="370" height="35" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="267" fill="#38bdf8" font-size="9.5" font-weight="bold" text-anchor="middle">${matClass}</text>
            <text x="230" y="280" fill="#94a3b8" font-size="8.5" text-anchor="middle">Temperature: ${temp}°C</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mat === 'metal' ? 'active' : ''}" id="btnMatMetal">⚡ Copper (Metal)</button>
          <button class="btn-sim ${mat === 'nonmetal' ? 'active' : ''}" id="btnMatNonMetal">🚫 Sulfur (Non-Metal)</button>
          <button class="btn-sim ${mat === 'metalloid' ? 'active' : ''}" id="btnMatMetalloid">🔬 Silicon (Metalloid)</button>
        </div>
        <div class="control-row" style="margin-top: 0.5rem;">
          <span class="control-label"><span>🌡️</span> Material Temperature:</span>
          <input type="range" class="sim-slider" id="tempSlider" min="0" max="120" value="${temp}">
          <span class="control-value" id="tempValText">${temp}°C</span>
        </div>
      `;

      document.getElementById('btnMatMetal').onclick = () => { mat = 'metal'; updateSim(); };
      document.getElementById('btnMatNonMetal').onclick = () => { mat = 'nonmetal'; updateSim(); };
      document.getElementById('btnMatMetalloid').onclick = () => { mat = 'metalloid'; updateSim(); };

      const tSlider = document.getElementById('tempSlider');
      tSlider.oninput = (e) => {
        temp = parseInt(e.target.value);
        document.getElementById('tempValText').textContent = `${temp}°C`;
        updateSim();
      };

      updateSim();
    }

    // 9. Room Temperature Liquid Elements Sim
    function simRoomTempLiquidElements(canvas, controls, title, icon) {
      title.textContent = 'Room-Temperature Liquids & Palm-Melting Gallium';
      icon.textContent = '💧';
      let temp = 25; // ambient temperature (0 to 45 deg C)

      function updateSim() {
        const gaMelts = temp >= 30; // Gallium melting point 29.76 C

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="50" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Physical States of 118 Elements (at ${temp}°C)</text>

            <!-- Flask 1: Mercury Hg (Liquid Metal) -->
            <g transform="translate(60, 75)">
              <path d="M 20 20 L 20 60 L 5 110 L 65 110 L 50 60 L 50 20 Z" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="1.5" />
              <!-- Liquid Silvery Pool -->
              <path d="M 9 100 Q 35 95 61 100 L 65 110 L 5 110 Z" fill="#94a3b8" />
              <text x="35" y="130" fill="#e2e8f0" font-size="10" font-weight="bold" text-anchor="middle">Mercury (Hg)</text>
              <text x="35" y="145" fill="#38bdf8" font-size="8.5" text-anchor="middle">Liquid Metal</text>
              <text x="35" y="158" fill="#94a3b8" font-size="8" text-anchor="middle">mp: -38.8°C</text>
            </g>

            <!-- Flask 2: Bromine Br2 (Liquid Non-Metal) -->
            <g transform="translate(195, 75)">
              <path d="M 20 20 L 20 60 L 5 110 L 65 110 L 50 60 L 50 20 Z" fill="rgba(30, 41, 59, 0.4)" stroke="#ef4444" stroke-width="1.5" />
              <!-- Liquid Reddish Brown Pool + Vapor -->
              <path d="M 9 100 Q 35 95 61 100 L 65 110 L 5 110 Z" fill="#7f1d1d" />
              <!-- Reddish Vapor -->
              <ellipse cx="35" cy="70" rx="15" ry="12" fill="rgba(185, 28, 28, 0.35)" />
              <text x="35" y="130" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Bromine (Br₂)</text>
              <text x="35" y="145" fill="#ef4444" font-size="8.5" text-anchor="middle">Liquid Non-Metal</text>
              <text x="35" y="158" fill="#94a3b8" font-size="8" text-anchor="middle">mp: -7.2°C</text>
            </g>

            <!-- Petri Dish 3: Gallium Ga (Palm Melter) -->
            <g transform="translate(330, 75)">
              <!-- Human Hand / Dish -->
              <ellipse cx="35" cy="95" rx="35" ry="15" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="1.5" />
              ${!gaMelts ? `
                <!-- Solid Gallium Cube -->
                <rect x="22" y="75" width="26" height="20" rx="2" fill="#cbd5e1" stroke="#ffffff" stroke-width="1.5" />
                <text x="35" y="88" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Ga</text>
              ` : `
                <!-- Liquid Puddle -->
                <ellipse cx="35" cy="94" rx="25" ry="8" fill="#94a3b8" stroke="#ffffff" stroke-width="1" />
                <text x="35" y="97" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">Liquid Ga</text>
              `}
              <text x="35" y="130" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Gallium (Ga)</text>
              <text x="35" y="145" fill="${gaMelts ? '#34d399' : '#f59e0b'}" font-size="8.5" font-weight="bold" text-anchor="middle">
                ${gaMelts ? 'Melts on Palm! 🖐️' : 'Solid (mp: 29.8°C)'}
              </text>
              <text x="35" y="158" fill="#94a3b8" font-size="8" text-anchor="middle">Body: 37°C</text>
            </g>

            <!-- State Breakdown Summary -->
            <rect x="45" y="245" width="370" height="40" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="262" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Out of 118 Elements: Only 2 are Liquid at 25°C (Hg & Br₂)!</text>
            <text x="230" y="278" fill="#cbd5e1" font-size="8.5" text-anchor="middle">11 are Gases (H₂, N₂, O₂, F₂, Cl₂, He, Ne, Ar, Kr, Xe, Rn) • All other 105 are Solids!</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🌡️</span> Ambient / Contact Temperature:</span>
          <input type="range" class="sim-slider" id="liqTempSlider" min="0" max="45" value="${temp}">
          <span class="control-value" id="liqTempValText">${temp}°C</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.3rem;">
          <button class="btn-sim" id="btnTempCool">❄️ Ice Bath (5°C)</button>
          <button class="btn-sim" id="btnTempRoom">Room Temp (25°C)</button>
          <button class="btn-sim" id="btnTempPalm">🖐️ Human Palm (37°C)</button>
        </div>
      `;

      const lSlider = document.getElementById('liqTempSlider');
      lSlider.oninput = (e) => {
        temp = parseInt(e.target.value);
        document.getElementById('liqTempValText').textContent = `${temp}°C`;
        updateSim();
      };

      document.getElementById('btnTempCool').onclick = () => { temp = 5; lSlider.value = 5; document.getElementById('liqTempValText').textContent = '5°C'; updateSim(); };
      document.getElementById('btnTempRoom').onclick = () => { temp = 25; lSlider.value = 25; document.getElementById('liqTempValText').textContent = '25°C'; updateSim(); };
      document.getElementById('btnTempPalm').onclick = () => { temp = 37; lSlider.value = 37; document.getElementById('liqTempValText').textContent = '37°C'; updateSim(); };

      updateSim();
    }

    // 10. Compounds: Synthesis & Emergent Properties
    function simCompoundsFixedRatio(canvas, controls, title, icon) {
      title.textContent = 'Chemical Synthesis of Table Salt (NaCl): Emergent Properties';
      icon.textContent = '🧂';
      let synthesized = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="50" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
              ${synthesized ? 'Chemical Compound: Sodium Chloride (NaCl)' : 'Constituent Elements Before Chemical Reaction'}
            </text>

            ${!synthesized ? `
              <!-- Reactant 1: Sodium (Na) -->
              <g transform="translate(65, 80)">
                <rect x="0" y="0" width="130" height="135" rx="8" fill="rgba(30, 41, 59, 0.8)" stroke="#f43f5e" stroke-width="1.5" />
                <circle cx="65" cy="45" r="22" fill="#94a3b8" stroke="#f43f5e" stroke-width="2" />
                <text x="65" y="50" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">Na</text>
                <text x="65" y="85" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">Sodium Metal</text>
                <text x="65" y="102" fill="#cbd5e1" font-size="8" text-anchor="middle">Soft, highly explosive</text>
                <text x="65" y="116" fill="#fca5a5" font-size="7.5" text-anchor="middle">Reacts violently with water!</text>
              </g>

              <text x="230" y="150" fill="#fbbf24" font-size="24" font-weight="bold" text-anchor="middle">+</text>

              <!-- Reactant 2: Chlorine Gas (Cl2) -->
              <g transform="translate(265, 80)">
                <rect x="0" y="0" width="130" height="135" rx="8" fill="rgba(30, 41, 59, 0.8)" stroke="#84cc16" stroke-width="1.5" />
                <ellipse cx="55" cy="45" rx="14" ry="12" fill="#84cc16" />
                <ellipse cx="75" cy="45" rx="14" ry="12" fill="#84cc16" />
                <text x="65" y="49" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Cl₂</text>
                <text x="65" y="85" fill="#a3e635" font-size="10" font-weight="bold" text-anchor="middle">Chlorine Gas</text>
                <text x="65" y="102" fill="#cbd5e1" font-size="8" text-anchor="middle">Suffocating yellow gas</text>
                <text x="65" y="116" fill="#bef264" font-size="7.5" text-anchor="middle">Deadly poison / choking agent!</text>
              </g>
            ` : `
              <!-- Synthesized Product: NaCl Crystals -->
              <g transform="translate(145, 75)">
                <rect x="0" y="0" width="170" height="145" rx="10" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2" />
                
                <!-- Sparkling Cubic NaCl Lattice -->
                <rect x="55" y="25" width="60" height="50" rx="4" fill="rgba(255, 255, 255, 0.9)" stroke="#38bdf8" stroke-width="2" />
                <line x1="55" y1="50" x2="115" y2="50" stroke="#94a3b8" />
                <line x1="85" y1="25" x2="85" y2="75" stroke="#94a3b8" />
                <circle cx="55" cy="25" r="4" fill="#0284c7" /><circle cx="85" cy="25" r="5" fill="#10b981" />
                <circle cx="115" cy="25" r="4" fill="#0284c7" /><circle cx="55" cy="50" r="5" fill="#10b981" />
                <circle cx="85" cy="50" r="4" fill="#0284c7" /><circle cx="115" cy="50" r="5" fill="#10b981" />

                <text x="85" y="98" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Table Salt (NaCl)</text>
                <text x="85" y="114" fill="#e2e8f0" font-size="8.5" text-anchor="middle">Completely Harmless & Edible!</text>
                <text x="85" y="128" fill="#cbd5e1" font-size="8" text-anchor="middle">Essential nutrient for nerve signals</text>
              </g>
            `}

            <!-- Emergent Property Takeaway -->
            <rect x="45" y="235" width="370" height="50" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="254" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">
              ${synthesized ? '2 Na (s) + Cl₂ (g) → 2 NaCl (s) [Exothermic Synthesis]' : 'Click "Trigger Chemical Reaction" to bond elements'}
            </text>
            <text x="230" y="272" fill="#cbd5e1" font-size="8.5" text-anchor="middle">
              ${synthesized 
                ? 'Emergent Properties: The compound possesses totally new properties different from its toxic elements!' 
                : 'Elements combine in a fixed 1:1 atomic ratio (Mass ratio Na : Cl = 23 : 35.5).'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${!synthesized ? 'active' : ''}" id="btnElemState">Hazardous Separate Elements (Na + Cl₂)</button>
          <button class="btn-sim ${synthesized ? 'active' : ''}" id="btnSynthReact">⚡ Trigger Chemical Reaction (Synthesize NaCl)</button>
        </div>
      `;

      document.getElementById('btnElemState').onclick = () => { synthesized = false; updateSim(); };
      document.getElementById('btnSynthReact').onclick = () => { synthesized = true; updateSim(); };

      updateSim();
    }

    // 11. Water Electrolysis Hofmann Voltameter Sim
    function simWaterElectrolysisHofmann(canvas, controls, title, icon) {
      title.textContent = 'Hofmann Voltameter: Water Electrolysis (2 : 1 Gas Ratio)';
      icon.textContent = '⚡';
      let powerOn = true;
      let flameTested = null; // 'cathode' or 'anode'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="48" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Hofmann Voltameter Apparatus</text>

            <!-- Connected Glass Columns (H-shape) -->
            <!-- Left Tube: Cathode (-) collecting H2 (double volume) -->
            <rect x="110" y="75" width="35" height="150" rx="4" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="1.5" />
            <!-- Right Tube: Anode (+) collecting O2 (single volume) -->
            <rect x="215" y="75" width="35" height="150" rx="4" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="1.5" />
            <!-- Reservoir Middle Tube -->
            <rect x="160" y="55" width="40" height="170" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="1" />
            <!-- Cross bridge connection -->
            <rect x="125" y="195" width="110" height="20" fill="rgba(14, 165, 233, 0.25)" />

            <!-- Water fill levels -->
            <!-- Cathode: H2 gas pushes water down by 80px -->
            <rect x="112" y="155" width="31" height="70" fill="rgba(14, 165, 233, 0.35)" />
            <!-- Gas pocket H2 -->
            <rect x="112" y="77" width="31" height="78" fill="rgba(56, 189, 248, 0.2)" />
            <text x="127" y="115" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">2 V</text>
            <text x="127" y="130" fill="#38bdf8" font-size="8.5" text-anchor="middle">(H₂)</text>

            <!-- Anode: O2 gas pushes water down by 40px -->
            <rect x="217" y="115" width="31" height="110" fill="rgba(14, 165, 233, 0.35)" />
            <!-- Gas pocket O2 -->
            <rect x="217" y="77" width="31" height="38" fill="rgba(239, 68, 68, 0.2)" />
            <text x="232" y="95" fill="#ef4444" font-size="10" font-weight="900" text-anchor="middle">1 V</text>
            <text x="232" y="108" fill="#ef4444" font-size="8" text-anchor="middle">(O₂)</text>

            <!-- Bubbles when power is ON -->
            ${powerOn ? `
              <circle cx="127" cy="215" r="2.5" fill="#38bdf8" />
              <circle cx="124" cy="190" r="3" fill="#38bdf8" />
              <circle cx="130" cy="170" r="2.5" fill="#38bdf8" />

              <circle cx="232" cy="215" r="2" fill="#ef4444" />
              <circle cx="230" cy="150" r="2.5" fill="#ef4444" />
            ` : ''}

            <!-- Electrodes -->
            <rect x="124" y="220" width="6" height="20" fill="#64748b" />
            <text x="127" y="255" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Cathode (-)</text>

            <rect x="229" y="220" width="6" height="20" fill="#64748b" />
            <text x="232" y="255" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">Anode (+)</text>

            <!-- Test Splint Results Card -->
            <rect x="280" y="75" width="145" height="150" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#f59e0b" stroke-width="1" />
            <text x="352" y="95" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Gas Identification Test</text>

            <foreignObject x="288" y="105" width="130" height="115">
              <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35;">
                <p><strong style="color: #38bdf8;">Cathode Gas:</strong> Ignites with a characteristic <em>"POP!"</em> sound, confirming <strong>Hydrogen (H₂)</strong>.</p>
                <p style="margin-top: 0.4rem;"><strong style="color: #ef4444;">Anode Gas:</strong> Rekindles a glowing wooden splint into flame, confirming <strong>Oxygen (O₂)</strong>.</p>
              </div>
            </foreignObject>

            <rect x="45" y="270" width="370" height="20" rx="4" fill="rgba(0, 0, 0, 0.4)" />
            <text x="230" y="284" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">
              Volume Ratio Collected: Exactly 2 Parts H₂ to 1 Part O₂ (Formula H₂O)!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${powerOn ? 'active' : ''}" id="btnElPower">⚡ DC Current: ${powerOn ? 'ON (Decomposing)' : 'OFF'}</button>
          <button class="btn-sim" id="btnTestH2">🔥 Test Cathode Gas ("Pop" Sound)</button>
          <button class="btn-sim" id="btnTestO2">🕯️ Test Anode Gas (Rekindles Splint)</button>
        </div>
      `;

      document.getElementById('btnElPower').onclick = () => { powerOn = !powerOn; updateSim(); };
      document.getElementById('btnTestH2').onclick = () => { alert('💥 POP! The cathode gas ignites with a characteristic sharp pop sound, proving it is combustible Hydrogen (H₂) gas!'); };
      document.getElementById('btnTestO2').onclick = () => { alert('✨ The glowing wooden splint bursts vigorously into bright flame, proving the anode gas is combustion supporter Oxygen (O₂)!'); };

      updateSim();
    }

    // 12. Sugar Thermal Decomposition Sim
    function simSugarCharringDecomposition(canvas, controls, title, icon) {
      title.textContent = 'Thermal Decomposition of Sugar: Carbon Charcoal & Water';
      icon.textContent = '🔥';
      let heatStage = 0; // 0: White crystals, 1: Melted brown caramel, 2: Black carbon charcoal + steam

      function updateSim() {
        let titleStage = 'Stage 1: Solid Sugar Crystals (C₁₂H₂₂O₁₁)';
        let descStage = 'White crystalline pure compound resting in a dry boiling tube.';

        if (heatStage === 1) {
          titleStage = 'Stage 2: Caramelization (Melting)';
          descStage = 'Sugar melts into amber brown liquid caramel as bonds begin to vibrate.';
        } else if (heatStage === 2) {
          titleStage = 'Stage 3: Chemical Decomposition Complete!';
          descStage = 'Water evolves as steam droplets; residual spongy black charcoal (Carbon) remains.';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="48" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">${titleStage}</text>

            <!-- Boiling Tube -->
            <g transform="translate(140, 65)">
              <rect x="20" y="0" width="45" height="150" rx="6" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              
              <!-- Contents at bottom -->
              ${heatStage === 0 ? `
                <!-- White granulated sugar -->
                <ellipse cx="42" cy="135" rx="18" ry="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
                <circle cx="36" cy="132" r="1.5" fill="#94a3b8" /><circle cx="48" cy="134" r="1.5" fill="#94a3b8" />
              ` : heatStage === 1 ? `
                <!-- Brown liquid caramel -->
                <ellipse cx="42" cy="135" rx="18" ry="10" fill="#b45309" />
              ` : `
                <!-- Black Carbon Charcoal Residue -->
                <path d="M 23 145 Q 42 120 62 145 Z" fill="#09090b" stroke="#27272a" stroke-width="2" />
                <!-- Water Droplets Condensed on cooler upper rim -->
                <circle cx="28" cy="25" r="2.5" fill="#38bdf8" opacity="0.9" />
                <circle cx="56" cy="35" r="3" fill="#38bdf8" opacity="0.9" />
                <circle cx="26" cy="50" r="2" fill="#38bdf8" opacity="0.9" />
                <circle cx="58" cy="65" r="2.5" fill="#38bdf8" opacity="0.9" />
                <text x="85" y="40" fill="#38bdf8" font-size="8.5" font-weight="bold">Water Droplets</text>
              `}
            </g>

            <!-- Bunsen Burner Flame -->
            ${heatStage > 0 ? `
              <g transform="translate(170, 220)">
                <path d="M 12 15 Q 6 -5 12 -25 Q 18 -5 12 15 Z" fill="#38bdf8" opacity="0.8" />
                <path d="M 12 15 Q 8 2 12 -12 Q 16 2 12 15 Z" fill="#fbbf24" />
                <!-- Burner base -->
                <rect x="4" y="15" width="16" height="30" fill="#475569" />
              </g>
            ` : ''}

            <!-- Equation Card -->
            <rect x="250" y="80" width="170" height="135" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#f59e0b" stroke-width="1.5" />
            <text x="335" y="105" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Decomposition Reaction</text>
            <foreignObject x="258" y="115" width="155" height="95">
              <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.4;">
                <p style="background: rgba(0,0,0,0.5); padding: 0.35rem; border-radius: 4px; color: #34d399; font-family: monospace;">
                  C₁₂H₂₂O₁₁ (s) ➔ 12 C (s) + 11 H₂O (g)
                </p>
                <p style="margin-top: 0.4rem;">Water turns anhydrous copper sulfate blue, confirming steam.</p>
              </div>
            </foreignObject>

            <rect x="45" y="270" width="370" height="20" rx="4" fill="rgba(0, 0, 0, 0.4)" />
            <text x="230" y="284" fill="#cbd5e1" font-size="9" text-anchor="middle">${descStage}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${heatStage === 0 ? 'active' : ''}" id="btnHeat0">White Sugar Crystals</button>
          <button class="btn-sim ${heatStage === 1 ? 'active' : ''}" id="btnHeat1">🔥 Gentle Heat (Caramel)</button>
          <button class="btn-sim ${heatStage === 2 ? 'active' : ''}" id="btnHeat2">🔥🔥 Strong Heat (Black Charcoal)</button>
        </div>
      `;

      document.getElementById('btnHeat0').onclick = () => { heatStage = 0; updateSim(); };
      document.getElementById('btnHeat1').onclick = () => { heatStage = 1; updateSim(); };
      document.getElementById('btnHeat2').onclick = () => { heatStage = 2; updateSim(); };

      updateSim();
    }

    // 13. Iron & Sulfur Physical Mixture (Sample A)
    function simIronSulfurMixtureMagnet(canvas, controls, title, icon) {
      title.textContent = 'Sample A: Physical Mixture of Iron and Sulfur';
      icon.textContent = '🧲';
      let magnetNear = false;
      let acidAdded = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="48" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Sample A: Unheated Iron Filings + Yellow Sulfur Powder</text>

            <!-- Watch Glass Dish -->
            <ellipse cx="170" cy="180" rx="90" ry="35" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="2" />
            
            <!-- Sulfur Powder Layer (Yellow) -->
            <ellipse cx="170" cy="182" rx="70" ry="25" fill="#facc15" opacity="0.8" />

            <!-- Iron Filings (Dark Grey specs) -->
            ${!magnetNear ? `
              <!-- Mixed in dish -->
              <g fill="#475569">
                <circle cx="130" cy="180" r="2.5" /><circle cx="150" cy="175" r="3" />
                <circle cx="175" cy="185" r="2.5" /><circle cx="195" cy="178" r="3" />
                <circle cx="160" cy="190" r="2.5" /><circle cx="210" cy="182" r="2.5" />
              </g>
            ` : `
              <!-- Filings attracted up to the magnet -->
              <g fill="#475569">
                <circle cx="165" cy="115" r="3" /><circle cx="175" cy="118" r="3" />
                <circle cx="185" cy="114" r="3" /><circle cx="170" cy="122" r="2.5" />
                <circle cx="180" cy="122" r="2.5" />
              </g>
            `}

            <!-- Bar Magnet -->
            <g transform="translate(${magnetNear ? '150, 70' : '150, 20'})">
              <rect x="0" y="0" width="25" height="40" fill="#ef4444" rx="2" />
              <text x="12" y="25" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">N</text>
              <rect x="25" y="0" width="25" height="40" fill="#0284c7" rx="2" />
              <text x="37" y="25" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">S</text>
            </g>

            <!-- Observation Card -->
            <rect x="285" y="70" width="140" height="155" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1" />
            <text x="355" y="90" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Physical Properties</text>
            <foreignObject x="292" y="100" width="125" height="120">
              <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35;">
                <p><strong style="color: #f59e0b;">Magnetism:</strong> Iron retains its magnetism and clings to the magnet.</p>
                <p style="margin-top: 0.4rem;"><strong style="color: #34d399;">Acid Reaction:</strong> Adding dilute HCl yields <strong>odorless H₂ gas</strong> (burns with a pop sound!).</p>
              </div>
            </foreignObject>

            <rect x="45" y="270" width="370" height="20" rx="4" fill="rgba(0, 0, 0, 0.4)" />
            <text x="230" y="284" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${magnetNear ? 'Magnet completely separates iron from sulfur! Physical separation works.' : 'Iron and sulfur retain their separate physical identities.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${magnetNear ? 'active' : ''}" id="btnMixMagnet">🧲 ${magnetNear ? 'Remove Magnet' : 'Bring Magnet Close'}</button>
          <button class="btn-sim" id="btnMixAcid">🧪 Add Dilute HCl (Odorless H₂ Gas Pop)</button>
        </div>
      `;

      document.getElementById('btnMixMagnet').onclick = () => { magnetNear = !magnetNear; updateSim(); };
      document.getElementById('btnMixAcid').onclick = () => { 
        alert('💥 Reaction: Fe + 2 HCl ➔ FeCl₂ + H₂ ↑\nOdorless hydrogen gas bubbles evolve, burning with a sharp POP sound! Sulfur remains unreacted at the bottom.'); 
      };

      updateSim();
    }

    // 14. Iron Sulfide Chemical Compound (Sample B)
    function simIronSulfideCompoundReaction(canvas, controls, title, icon) {
      title.textContent = 'Sample B: Iron Sulfide (FeS) Chemical Compound';
      icon.textContent = '🥚';
      let magnetTested = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#ef4444" stroke-width="1.5" />
            <text x="230" y="48" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">Sample B: Strongly Heated Iron + Sulfur Mass (Iron Sulfide - FeS)</text>

            <!-- Crucible / Mortar Dish -->
            <ellipse cx="170" cy="180" rx="80" ry="32" fill="rgba(30, 41, 59, 0.5)" stroke="#ef4444" stroke-width="2" />
            
            <!-- Black Solid FeS Mass (No yellow sulfur visible!) -->
            <path d="M 120 180 Q 170 160 220 180 Q 170 200 120 180 Z" fill="#18181b" stroke="#3f3f46" stroke-width="2" />
            <text x="170" y="184" fill="#a1a1aa" font-size="10" font-weight="bold" text-anchor="middle">Black FeS Compound</text>

            <!-- Magnet (Fails to attract!) -->
            <g transform="translate(150, ${magnetTested ? '110' : '50'})">
              <rect x="0" y="0" width="20" height="35" fill="#ef4444" rx="2" />
              <text x="10" y="22" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">N</text>
              <rect x="20" y="0" width="20" height="35" fill="#0284c7" rx="2" />
              <text x="30" y="22" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">S</text>
            </g>

            ${magnetTested ? `
              <text x="170" y="98" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">NO ATTRACTION! ❌</text>
            ` : ''}

            <!-- Rotten Egg Gas Odor Card -->
            <rect x="285" y="70" width="140" height="155" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#ef4444" stroke-width="1" />
            <text x="355" y="90" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">Chemical Transformation</text>
            <foreignObject x="292" y="100" width="125" height="120">
              <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 0.72rem; color: #cbd5e1; line-height: 1.35;">
                <p><strong style="color: #f87171;">Non-Magnetic:</strong> Iron has bonded with sulfur; magnetism is permanently lost!</p>
                <p style="margin-top: 0.4rem;"><strong style="color: #fbbf24;">Add HCl:</strong> Releases <strong>Hydrogen Sulfide (H₂S)</strong> gas with a foul <em>rotten-egg odor</em>!</p>
              </div>
            </foreignObject>

            <rect x="45" y="270" width="370" height="20" rx="4" fill="rgba(0, 0, 0, 0.4)" />
            <text x="230" y="284" fill="#34d399" font-size="9" text-anchor="middle">
              Fe + S ➔ FeS (Compound) | FeS + 2 HCl ➔ FeCl₂ + H₂S ↑ (Rotten Egg Gas)
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${magnetTested ? 'active' : ''}" id="btnCompMagnet">🧲 Test with Magnet</button>
          <button class="btn-sim" id="btnCompAcid">🧪 Add Dilute HCl (Foul Rotten-Egg H₂S Gas)</button>
        </div>
      `;

      document.getElementById('btnCompMagnet').onclick = () => { magnetTested = !magnetTested; updateSim(); };
      document.getElementById('btnCompAcid').onclick = () => {
        alert('🤢 FOUL ODOR: FeS + 2 HCl ➔ FeCl₂ + H₂S ↑\nReleases toxic Hydrogen Sulfide (H₂S) gas with a suffocating, unmistakable smell of ROTTEN EGGS! It turns lead acetate paper black.');
      };

      updateSim();
    }

    // 15. Native vs Compound Minerals Sim
    function simNativeCompoundMinerals(canvas, controls, title, icon) {
      title.textContent = 'Earth\'s Crust: Native Elements vs Compound Minerals';
      icon.textContent = '💎';
      let mineral = 'gold'; // 'gold', 'copper', 'quartz', 'calcite'

      function updateSim() {
        let name = '', category = '', formula = '', crystalDesc = '', color = '';
        if (mineral === 'gold') {
          name = 'Native Gold (Au)';
          category = 'Native Element (Uncombined)';
          formula = 'Pure Au Atoms';
          crystalDesc = 'Glittering yellow metallic luster; found uncombined due to extreme chemical nobility.';
          color = '#f59e0b';
        } else if (mineral === 'copper') {
          name = 'Native Copper (Cu)';
          category = 'Native Element (Uncombined)';
          formula = 'Pure Cu Atoms';
          crystalDesc = 'Reddish-orange dendritic branch nuggets formed in volcanic hydrothermal cavities.';
          color = '#ea580c';
        } else if (mineral === 'quartz') {
          name = 'Quartz (Silicon Dioxide)';
          category = 'Compound Mineral';
          formula = 'SiO₂ (1 Silicon : 2 Oxygen)';
          crystalDesc = 'Hexagonal prismatic crystals; continuous framework of SiO₄ silicon-oxygen tetrahedra.';
          color = '#38bdf8';
        } else {
          name = 'Calcite (Calcium Carbonate)';
          category = 'Compound Mineral';
          formula = 'CaCO₃ (1 Ca : 1 C : 3 O)';
          crystalDesc = 'Rhombohedral crystals exhibiting strong optical double refraction (birefringence).';
          color = '#10b981';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="48" fill="${color}" font-size="12" font-weight="bold" text-anchor="middle">${name}</text>
            <text x="230" y="65" fill="#94a3b8" font-size="9.5" text-anchor="middle">${category} • ${formula}</text>

            <!-- 3D Crystalline Specimen Representation -->
            <g transform="translate(140, 85)">
              <!-- Faceted mineral crystal block -->
              <polygon points="75,20 135,50 135,115 75,145 15,115 15,50" fill="${color}" fill-opacity="0.3" stroke="${color}" stroke-width="2" />
              <polygon points="75,20 135,50 75,80 15,50" fill="${color}" fill-opacity="0.5" stroke="${color}" stroke-width="2" />
              <polygon points="75,80 135,50 135,115 75,145" fill="${color}" fill-opacity="0.25" stroke="${color}" stroke-width="1.5" />
              
              <!-- Sparkle highlights -->
              <line x1="75" y1="20" x2="75" y2="80" stroke="#ffffff" stroke-width="1.5" />
              <circle cx="75" cy="50" r="3" fill="#ffffff" />
            </g>

            <rect x="45" y="245" width="370" height="40" rx="6" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="262" fill="#cbd5e1" font-size="9.5" text-anchor="middle">${crystalDesc}</text>
            <text x="230" y="276" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">
              ${mineral === 'gold' || mineral === 'copper' ? 'Native elements exist free in nature without bonding to other elements.' : 'Compound minerals consist of two or more elements chemically locked in fixed geometric ratios.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${mineral === 'gold' ? 'active' : ''}" id="btnMinGold">🥇 Native Gold (Au)</button>
          <button class="btn-sim ${mineral === 'copper' ? 'active' : ''}" id="btnMinCopper">🥉 Native Copper (Cu)</button>
          <button class="btn-sim ${mineral === 'quartz' ? 'active' : ''}" id="btnMinQuartz">🔮 Quartz (SiO₂)</button>
          <button class="btn-sim ${mineral === 'calcite' ? 'active' : ''}" id="btnMinCalcite">💎 Calcite (CaCO₃)</button>
        </div>
      `;

      document.getElementById('btnMinGold').onclick = () => { mineral = 'gold'; updateSim(); };
      document.getElementById('btnMinCopper').onclick = () => { mineral = 'copper'; updateSim(); };
      document.getElementById('btnMinQuartz').onclick = () => { mineral = 'quartz'; updateSim(); };
      document.getElementById('btnMinCalcite').onclick = () => { mineral = 'calcite'; updateSim(); };

      updateSim();
    }

    // 16. Modern Tech, Graphene Aerogel & Dhokra Art
    function simAdvancedGrapheneDhokra(canvas, controls, title, icon) {
      title.textContent = 'Modern Tech, Graphene Aerogels & Ancient Dhokra Art';
      icon.textContent = '📱';
      let tab = 'phone'; // 'phone', 'aerogel', 'dhokra'

      function updateSim() {
        if (tab === 'phone') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
              <text x="230" y="48" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Over 45 Distinct Chemical Elements in a Smartphone!</text>

              <!-- Smartphone Schematic -->
              <rect x="70" y="65" width="100" height="180" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
              <rect x="78" y="75" width="84" height="150" rx="6" fill="#0f172a" />
              <circle cx="120" cy="235" r="4" fill="#38bdf8" />

              <!-- Callout Tags for Smartphone Elements -->
              <g transform="translate(185, 75)" font-size="9" fill="#cbd5e1">
                <text x="0" y="10" fill="#38bdf8" font-weight="bold">Touchscreen: In, Sn, O (Indium Tin Oxide)</text>
                <text x="0" y="32" fill="#facc15" font-weight="bold">Battery: Li, Co, C (Graphite), Al</text>
                <text x="0" y="54" fill="#4ade80" font-weight="bold">Microprocessor: Si (Silicon), P, B, As</text>
                <text x="0" y="76" fill="#f43f5e" font-weight="bold">Vibration & Speakers: Nd, Dy, Fe, B (Magnets)</text>
                <text x="0" y="98" fill="#c084fc" font-weight="bold">Wiring & Circuit Board: Cu, Au, Ag, Ta</text>
                <text x="0" y="120" fill="#94a3b8">Casing: Al, Mg alloys, Plastics</text>
              </g>

              <rect x="45" y="260" width="370" height="25" rx="4" fill="rgba(56, 189, 248, 0.1)" />
              <text x="230" y="276" fill="#38bdf8" font-size="9" text-anchor="middle">Modern electronics combine elements into engineered compounds and alloys!</text>
            </svg>
          `;
        } else if (tab === 'aerogel') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5" />
              <text x="230" y="48" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Graphene Aerogel: Lightest Solid on Earth</text>
              
              <!-- Delicate Flower Petal Holding Aerogel -->
              <path d="M 170 200 Q 230 170 290 200 Q 230 220 170 200 Z" fill="#f472b6" stroke="#db2777" stroke-width="1.5" />
              
              <!-- Aerogel Cube Resting Weightlessly on Petal -->
              <rect x="200" y="140" width="60" height="50" rx="4" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="1.5" />
              <text x="230" y="168" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Graphene</text>
              <text x="230" y="180" fill="#7dd3fc" font-size="7.5" text-anchor="middle">Density 0.16 mg/cm³</text>

              <!-- Oil Spill Sponge Simulation -->
              <rect x="50" y="225" width="360" height="35" rx="6" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="1" />
              <text x="230" y="242" fill="#fde68a" font-size="9.5" font-weight="bold" text-anchor="middle">Absorbs up to 900× its own weight in spilled petroleum oil!</text>
              <text x="230" y="254" fill="#94a3b8" font-size="8.5" text-anchor="middle">Pure elemental carbon allotrope structured into microscopic porous air pockets.</text>
            </svg>
          `;
        } else {
          // Dhokra Lost-Wax Bell Metal Art
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#f59e0b" stroke-width="1.5" />
              <text x="230" y="48" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Tribal Dhokra Lost-Wax Bell Metal Casting (Bihar & Odisha)</text>

              <!-- Dhokra Figurine Graphic -->
              <g transform="translate(170, 70)">
                <ellipse cx="60" cy="80" rx="40" ry="25" fill="#d97706" stroke="#fbbf24" stroke-width="2" />
                <circle cx="95" cy="55" r="15" fill="#d97706" stroke="#fbbf24" stroke-width="2" />
                <line x1="35" y1="100" x2="35" y2="140" stroke="#fbbf24" stroke-width="4" />
                <line x1="85" y1="100" x2="85" y2="140" stroke="#fbbf24" stroke-width="4" />
                <!-- Traditional Lost-Wax Thread Patterns -->
                <path d="M 40 75 Q 60 65 80 75" stroke="#fef08a" stroke-width="1.5" fill="none" />
                <path d="M 40 85 Q 60 75 80 85" stroke="#fef08a" stroke-width="1.5" fill="none" />
              </g>

              <rect x="45" y="235" width="370" height="48" rx="6" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="1" />
              <text x="230" y="254" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">4,000-Year Heritage of Indigenous Metallurgy</text>
              <text x="230" y="270" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Wax core enveloped in clay mold; molten bronze alloy displaces wax with extreme precision.</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${tab === 'phone' ? 'active' : ''}" id="btnTabPhone">📱 45+ Elements in Smartphone</button>
          <button class="btn-sim ${tab === 'aerogel' ? 'active' : ''}" id="btnTabAerogel">🪶 Graphene Aerogel (900× Oil Absorption)</button>
          <button class="btn-sim ${tab === 'dhokra' ? 'active' : ''}" id="btnTabDhokra">🏺 Dhokra Lost-Wax Bell Metal</button>
        </div>
      `;

      document.getElementById('btnTabPhone').onclick = () => { tab = 'phone'; updateSim(); };
      document.getElementById('btnTabAerogel').onclick = () => { tab = 'aerogel'; updateSim(); };
      document.getElementById('btnTabDhokra').onclick = () => { tab = 'dhokra'; updateSim(); };

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-elements-compounds.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

