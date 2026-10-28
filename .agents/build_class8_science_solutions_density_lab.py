# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-solutions-density.html
Class 8 Science - Chapter 9: Solutions, Solubility, and Density
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Dr. Asima Chatterjee)
- 16 bespoke interactive SVG simulators with live controls, gauges, and rich animations
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
from class8_science_solutions_density_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 9: Solutions, Solubility, and Density Master Lab</title>
  
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
      --bg-primary: #060e1a;
      --bg-secondary: #0c182c;
      --card-bg: rgba(12, 24, 44, 0.92);
      --card-border: rgba(56, 189, 248, 0.28);
      --accent-sky: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-emerald: #10b981;
      --accent-purple: #c084fc;
      --accent-teal: #14b8a6;
      --accent-indigo: #818cf8;
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
        radial-gradient(circle at 10% 20%, rgba(56, 189, 248, 0.14) 0%, transparent 45%),
        radial-gradient(circle at 90% 70%, rgba(20, 184, 166, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.06) 0%, transparent 60%);
    }

    /* Header & Navigation Bar */
    .lab-header {
      background: rgba(12, 24, 44, 0.96);
      backdrop-filter: blur(14px);
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
      background: linear-gradient(135deg, #0284c7, #10b981);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 18px rgba(56, 189, 248, 0.45);
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
      background: linear-gradient(90deg, #38bdf8, #10b981, #f59e0b);
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
      background: rgba(20, 36, 62, 0.75);
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
      background: linear-gradient(135deg, #0284c7, #10b981);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      position: relative;
      flex-shrink: 0;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--accent-emerald);
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
      color: var(--accent-emerald);
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
      background: rgba(12, 24, 44, 0.85);
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
      background: rgba(12, 24, 44, 0.92);
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
      background: rgba(20, 36, 62, 0.6);
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
      background: rgba(12, 24, 44, 0.75);
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
      background: rgba(6, 14, 26, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.22);
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
      background: rgba(20, 36, 62, 0.55);
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
      background: linear-gradient(135deg, rgba(20, 36, 62, 0.95), rgba(12, 24, 44, 0.95));
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
      background: rgba(20, 36, 62, 0.6);
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
      background: #0c182c;
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
      <div class="lab-icon">🧪</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 9</div>
        <h1>Solutions, Solubility, and Density</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Solution Fundamentals</span>
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
      <span>👩‍🔬</span>
      <div class="avatar-speaking-pulse" id="avatarPulse"></div>
    </div>
    <div class="avatar-dialogue-box">
      <div class="avatar-name-row">
        <span class="avatar-name">Dr. Asima Chatterjee • Pioneering Chemist & Natural Drug Researcher</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Welcome to the Solutions, Solubility, and Density Laboratory! Let us investigate how substances dissolve into uniform solutions and discover the physics governing density and flotation.
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
          <span class="slide-tag" id="slideBadge">Solution Fundamentals</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Defining Solutions & Solvents</h2>

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
            <span id="simIcon">🥣</span>
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
    // 16 BESPOKE DYNAMIC SIMULATORS
    // ==========================================

    function renderSimulator(simId) {
      const canvas = document.getElementById('simCanvas');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const icon = document.getElementById('simIcon');

      canvas.innerHTML = '';
      controls.innerHTML = '';

      switch (simId) {
        case 'solution_solute_solvent_sim':
          simSolutionSoluteSolvent(canvas, controls, title, icon);
          break;
        case 'chashni_liquid_solutions_sim':
          simChashniLiquidSolutions(canvas, controls, title, icon);
          break;
        case 'ayurvedic_solvents_sim':
          simAyurvedicSolvents(canvas, controls, title, icon);
          break;
        case 'asima_chatterjee_lab_sim':
          simAsimaChatterjeeLab(canvas, controls, title, icon);
          break;
        case 'manipur_salt_wells_sim':
          simManipurSaltWells(canvas, controls, title, icon);
          break;
        case 'saturated_unsaturated_sim':
          simSaturatedUnsaturated(canvas, controls, title, icon);
          break;
        case 'solution_concentration_sim':
          simSolutionConcentration(canvas, controls, title, icon);
          break;
        case 'solubility_temperature_sim':
          simSolubilityTemperature(canvas, controls, title, icon);
          break;
        case 'gas_solubility_temp_sim':
          simGasSolubilityTemp(canvas, controls, title, icon);
          break;
        case 'density_mass_volume_sim':
          simDensityMassVolume(canvas, controls, title, icon);
          break;
        case 'mass_volume_measurement_sim':
          simMassVolumeMeasurement(canvas, controls, title, icon);
          break;
        case 'meniscus_reading_lab_sim':
          simMeniscusReadingLab(canvas, controls, title, icon);
          break;
        case 'water_displacement_volume_sim':
          simWaterDisplacementVolume(canvas, controls, title, icon);
          break;
        case 'temp_pressure_density_sim':
          simTempPressureDensity(canvas, controls, title, icon);
          break;
        case 'water_ice_anomalous_sim':
          simWaterIceAnomalous(canvas, controls, title, icon);
          break;
        case 'earth_density_layers_sim':
          simEarthDensityLayers(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = '<div style="color: #94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Solution: Solute, Solvent & Non-Uniform Comparison
    function simSolutionSoluteSolvent(canvas, controls, title, icon) {
      title.textContent = 'Uniform Solution vs Non-Uniform Mixture';
      icon.textContent = '🥣';
      let mode = 'salt'; // 'salt' or 'sand'
      let isStirring = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Glass Beaker -->
            <rect x="120" y="60" width="220" height="210" rx="8" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
            <!-- Water Liquid Base -->
            <rect x="124" y="110" width="212" height="156" rx="4" fill="rgba(14, 165, 233, 0.25)" />
            
            <!-- Graduations -->
            <line x1="120" y1="140" x2="140" y2="140" stroke="#38bdf8" stroke-width="1.5" />
            <text x="145" y="144" fill="#38bdf8" font-size="9">200 mL</text>
            <line x1="120" y1="180" x2="140" y2="180" stroke="#38bdf8" stroke-width="1.5" />
            <text x="145" y="184" fill="#38bdf8" font-size="9">100 mL</text>

            <!-- Glass Stirring Rod -->
            <line x1="${isStirring ? '210' : '230'}" y1="30" x2="${isStirring ? '250' : '230'}" y2="240" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round" opacity="0.8" />

            ${mode === 'salt' ? `
              <!-- Uniform Dissolved Salt Ions Na+ and Cl- -->
              <g>
                <!-- Na+ (Blue small) -->
                <circle cx="160" cy="150" r="7" fill="#0284c7" stroke="#38bdf8" stroke-width="1"><animate attributeName="cy" values="150;154;150" dur="2s" repeatCount="indefinite"/></circle>
                <text x="160" y="153" fill="#fff" font-size="6" font-weight="bold" text-anchor="middle">Na⁺</text>

                <circle cx="210" cy="190" r="7" fill="#0284c7" stroke="#38bdf8" stroke-width="1"><animate attributeName="cy" values="190;186;190" dur="2.4s" repeatCount="indefinite"/></circle>
                <text x="210" y="193" fill="#fff" font-size="6" font-weight="bold" text-anchor="middle">Na⁺</text>

                <circle cx="280" cy="140" r="7" fill="#0284c7" stroke="#38bdf8" stroke-width="1"><animate attributeName="cy" values="140;144;140" dur="1.8s" repeatCount="indefinite"/></circle>
                <text x="280" y="143" fill="#fff" font-size="6" font-weight="bold" text-anchor="middle">Na⁺</text>

                <circle cx="260" cy="220" r="7" fill="#0284c7" stroke="#38bdf8" stroke-width="1"><animate attributeName="cy" values="220;223;220" dur="2.1s" repeatCount="indefinite"/></circle>
                <text x="260" y="223" fill="#fff" font-size="6" font-weight="bold" text-anchor="middle">Na⁺</text>

                <!-- Cl- (Emerald medium) -->
                <circle cx="190" cy="135" r="10" fill="#059669" stroke="#34d399" stroke-width="1"><animate attributeName="cy" values="135;131;135" dur="2.2s" repeatCount="indefinite"/></circle>
                <text x="190" y="139" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">Cl⁻</text>

                <circle cx="240" cy="165" r="10" fill="#059669" stroke="#34d399" stroke-width="1"><animate attributeName="cy" values="165;169;165" dur="1.9s" repeatCount="indefinite"/></circle>
                <text x="240" y="169" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">Cl⁻</text>

                <circle cx="170" cy="225" r="10" fill="#059669" stroke="#34d399" stroke-width="1"><animate attributeName="cy" values="225;221;225" dur="2.5s" repeatCount="indefinite"/></circle>
                <text x="170" y="229" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">Cl⁻</text>

                <circle cx="300" cy="195" r="10" fill="#059669" stroke="#34d399" stroke-width="1"><animate attributeName="cy" values="195;198;195" dur="2.3s" repeatCount="indefinite"/></circle>
                <text x="300" y="199" fill="#fff" font-size="7" font-weight="bold" text-anchor="middle">Cl⁻</text>
              </g>
              <!-- Info Tag -->
              <rect x="80" y="15" width="300" height="35" rx="6" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="1" />
              <text x="230" y="32" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Uniform (Homogeneous) Solution</text>
              <text x="230" y="44" fill="#cbd5e1" font-size="9" text-anchor="middle">Solute (Salt) dissolved molecularly in Solvent (Water) • Never settles!</text>
            ` : `
              <!-- Sand settled at bottom & turbid suspension -->
              <!-- Settled Sand Pile -->
              <path d="M 125 264 Q 230 240 335 264 Z" fill="#d97706" />
              <!-- Turbid grains -->
              <g fill="#b45309">
                <circle cx="160" cy="245" r="3" /><circle cx="180" cy="252" r="3.5" /><circle cx="210" cy="248" r="4" />
                <circle cx="240" cy="254" r="3" /><circle cx="270" cy="250" r="3.5" /><circle cx="300" cy="255" r="4" />
                <circle cx="170" cy="210" r="2.5" opacity="0.6" /><circle cx="280" cy="200" r="2.5" opacity="0.6" />
              </g>
              <!-- Info Tag -->
              <rect x="80" y="15" width="300" height="35" rx="6" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1" />
              <text x="230" y="32" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">Non-Uniform (Heterogeneous) Mixture</text>
              <text x="230" y="44" fill="#cbd5e1" font-size="9" text-anchor="middle">Insoluble sand grains settle at the bottom with visible boundary layers.</text>
            `}

            <rect x="30" y="280" width="400" height="25" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="296" fill="#cbd5e1" font-size="9.5" text-anchor="middle">
              ${mode === 'salt' ? 'Oral Rehydration Solution (ORS) & salt-water are true solutions.' : 'Sawdust, chalk powder, and sand form heterogeneous suspensions.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${mode === 'salt' ? 'active' : ''}" id="btnSimSalt">🧂 Salt in Water (Homogeneous Solution)</button>
          <button class="btn-sim ${mode === 'sand' ? 'active' : ''}" id="btnSimSand">🏖️ Sand in Water (Non-Uniform Mixture)</button>
          <button class="btn-sim" id="btnStir">🔄 Stir with Glass Rod</button>
        </div>
      `;

      document.getElementById('btnSimSalt').onclick = () => { mode = 'salt'; updateSim(); };
      document.getElementById('btnSimSand').onclick = () => { mode = 'sand'; updateSim(); };
      document.getElementById('btnStir').onclick = () => {
        isStirring = !isStirring;
        updateSim();
        setTimeout(() => { isStirring = false; updateSim(); }, 800);
      };

      updateSim();
    }

    // 2. Chashni of Gulab Jamun & Liquid-Liquid Solutions
    function simChashniLiquidSolutions(canvas, controls, title, icon) {
      title.textContent = 'Gulab Jamun Chashni & Liquid-Liquid Solute Rules';
      icon.textContent = '🍯';
      let view = 'chashni'; // 'chashni' or 'liquids'
      let alcoholVol = 30; // mL in 100 mL mixture

      function updateSim() {
        if (view === 'chashni') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Golden Kadai Pan -->
              <ellipse cx="230" cy="220" rx="160" ry="60" fill="#78350f" stroke="#d97706" stroke-width="2" />
              <!-- Golden Viscous Sugar Syrup (Chashni) -->
              <ellipse cx="230" cy="215" rx="145" ry="50" fill="#b45309" opacity="0.9" />

              <!-- Simmering Steam / Bubbles -->
              <circle cx="160" cy="205" r="5" fill="#fde68a" opacity="0.7"><animate attributeName="cy" values="205;190;205" dur="1.5s" repeatCount="indefinite"/></circle>
              <circle cx="210" cy="215" r="6" fill="#fde68a" opacity="0.7"><animate attributeName="cy" values="215;198;215" dur="1.8s" repeatCount="indefinite"/></circle>
              <circle cx="280" cy="210" r="5" fill="#fde68a" opacity="0.7"><animate attributeName="cy" values="210;192;210" dur="1.6s" repeatCount="indefinite"/></circle>

              <!-- Golden Brown Gulab Jamuns Soaking -->
              <circle cx="180" cy="210" r="18" fill="#451a03" stroke="#92400e" stroke-width="1.5" />
              <ellipse cx="175" cy="205" rx="5" ry="3" fill="#b45309" opacity="0.6" />

              <circle cx="240" cy="200" r="20" fill="#451a03" stroke="#92400e" stroke-width="1.5" />
              <ellipse cx="235" cy="195" rx="6" ry="3.5" fill="#b45309" opacity="0.6" />

              <circle cx="295" cy="215" r="17" fill="#451a03" stroke="#92400e" stroke-width="1.5" />
              <ellipse cx="290" cy="210" rx="5" ry="3" fill="#b45309" opacity="0.6" />

              <!-- Rising Aromatic Steam -->
              <path d="M 180 180 Q 170 140 190 120" stroke="#fde68a" stroke-width="2" fill="none" opacity="0.4"><animate attributeName="d" values="M 180 180 Q 170 140 190 120; M 180 180 Q 190 140 170 120; M 180 180 Q 170 140 190 120" dur="3s" repeatCount="indefinite"/></path>
              <path d="M 240 170 Q 250 130 235 110" stroke="#fde68a" stroke-width="2" fill="none" opacity="0.4"><animate attributeName="d" values="M 240 170 Q 250 130 235 110; M 240 170 Q 230 130 245 110; M 240 170 Q 250 130 235 110" dur="2.8s" repeatCount="indefinite"/></path>

              <!-- Paradox Explanatory Card -->
              <rect x="50" y="20" width="360" height="75" rx="10" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5" />
              <text x="230" y="42" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle">Gulab Jamun Chashni: The Solute-Solvent Paradox</text>
              <text x="230" y="60" fill="#e2e8f0" font-size="9.5" text-anchor="middle">Sugar mass = 150 g (SOLUTE) dissolved in Water = 100 mL (SOLVENT)</text>
              <text x="230" y="77" fill="#38bdf8" font-size="9" text-anchor="middle">Water remains the solvent because it provides the continuous liquid phase!</text>
            </svg>
          `;
        } else {
          // Liquid-Liquid Solute/Solvent Rule
          const waterVol = 100 - alcoholVol;
          const isAlcoholSolute = alcoholVol < 50;
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Graduated Mixing Beaker -->
              <rect x="150" y="60" width="160" height="200" rx="8" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              
              <!-- Total Liquid Fill -->
              <rect x="154" y="100" width="152" height="156" rx="4" fill="rgba(99, 102, 241, 0.25)" />
              
              <!-- Color Split Visualization -->
              <rect x="154" y="100" width="152" height="${alcoholVol * 1.56}" fill="rgba(244, 63, 94, 0.35)" />
              <rect x="154" y="${100 + alcoholVol * 1.56}" width="152" height="${waterVol * 1.56}" fill="rgba(14, 165, 233, 0.35)" />

              <!-- Text Indicators -->
              <text x="230" y="85" fill="#e2e8f0" font-size="11" font-weight="bold" text-anchor="middle">100 mL Miscible Liquid Solution</text>
              
              <!-- Left Callout (Alcohol) -->
              <text x="140" y="${110 + (alcoholVol * 0.78)}" fill="#fb7185" font-size="10" font-weight="bold" text-anchor="end">
                Alcohol: ${alcoholVol} mL ${alcoholVol < 50 ? '(SOLUTE)' : alcoholVol === 50 ? '(EQUAL)' : '(SOLVENT)'}
              </text>
              
              <!-- Right Callout (Water) -->
              <text x="320" y="${110 + alcoholVol * 1.56 + (waterVol * 0.78)}" fill="#38bdf8" font-size="10" font-weight="bold">
                Water: ${waterVol} mL ${waterVol < 50 ? '(SOLUTE)' : waterVol === 50 ? '(EQUAL)' : '(SOLVENT)'}
              </text>

              <!-- Rule Card -->
              <rect x="40" y="265" width="380" height="45" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#818cf8" stroke-width="1.5" />
              <text x="230" y="283" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">Liquid-Liquid Rule: Smaller volume = Solute | Larger volume = Solvent</text>
              <text x="230" y="298" fill="#cbd5e1" font-size="8.5" text-anchor="middle">
                Current: ${isAlcoholSolute ? 'Alcohol is SOLUTE (<50%) and Water is SOLVENT (>50%)' : alcoholVol === 50 ? 'Equal amounts: Either liquid can be considered solvent' : 'Alcohol is SOLVENT (>50%) and Water is SOLUTE (<50%)'}
              </text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${view === 'chashni' ? 'active' : ''}" id="btnChashni">🍯 Gulab Jamun Chashni</button>
          <button class="btn-sim ${view === 'liquids' ? 'active' : ''}" id="btnLiquids">🧪 Liquid-Liquid Volume Rule</button>
        </div>
        ${view === 'liquids' ? `
          <div class="control-row" style="margin-top: 0.5rem;">
            <span class="control-label"><span>🍷</span> Alcohol Volume:</span>
            <input type="range" class="sim-slider" id="alcSlider" min="5" max="95" value="${alcoholVol}">
            <span class="control-value" id="alcValText">${alcoholVol} mL (Water: ${100 - alcoholVol} mL)</span>
          </div>
        ` : ''}
      `;

      document.getElementById('btnChashni').onclick = () => { view = 'chashni'; updateSim(); };
      document.getElementById('btnLiquids').onclick = () => { view = 'liquids'; updateSim(); };

      if (view === 'liquids') {
        const slider = document.getElementById('alcSlider');
        slider.oninput = (e) => {
          alcoholVol = parseInt(e.target.value);
          document.getElementById('alcValText').textContent = `${alcoholVol} mL (Water: ${100 - alcoholVol} mL)`;
          updateSim();
        };
      }

      updateSim();
    }

    // 3. Ayurveda & Siddha Natural Solvents
    function simAyurvedicSolvents(canvas, controls, title, icon) {
      title.textContent = 'Traditional Ayurvedic Pharmacology & Natural Solvents';
      icon.textContent = '🌿';
      let solventType = 'water'; // 'water', 'alcohol', 'ghee'

      function updateSim() {
        let name = '', action = '', actives = '', vesselColor = '';
        if (solventType === 'water') {
          name = 'Aqueous Solvent: Kwatha / Kashaya';
          action = 'Boiling herbs in water extracts water-soluble polar phytonutrients.';
          actives = 'Tannins, Flavonoids, Glycosides, Water-Soluble Minerals';
          vesselColor = '#0284c7';
        } else if (solventType === 'alcohol') {
          name = 'Hydro-Alcoholic Solvent: Asava & Arishta';
          action = 'Natural fermentation creates dual-polarity solvent, self-preserving for years.';
          actives = 'Resins, Alkaloids, Essential Aromatic Oils';
          vesselColor = '#a855f7';
        } else {
          name = 'Lipophilic Lipid Solvent: Sneha Kalpana (Ghee & Oil)';
          action = 'Cow\'s Ghee (Ghrita) & Sesame Oil dissolve fat-soluble compounds crossing cell barriers.';
          actives = 'Lipophilic Alkaloids, Sterols, Brain-Targeting Phytomolecules';
          vesselColor = '#f59e0b';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Traditional Clay / Copper Boiling Vessel -->
            <path d="M 160 120 L 170 240 Q 230 260 290 240 L 300 120 Z" fill="rgba(30, 41, 59, 0.7)" stroke="${vesselColor}" stroke-width="2.5" />
            <!-- Liquid Fill inside Vessel -->
            <path d="M 165 150 L 172 235 Q 230 252 288 235 L 295 150 Z" fill="${vesselColor}" opacity="0.35" />

            <!-- Herb Leaves floating & dissolving -->
            <g transform="translate(190, 160)">
              <ellipse cx="20" cy="30" rx="12" ry="6" fill="#16a34a" transform="rotate(-30 20 30)" />
              <ellipse cx="60" cy="45" rx="14" ry="7" fill="#15803d" transform="rotate(25 60 45)" />
              <ellipse cx="35" cy="65" rx="11" ry="5" fill="#16a34a" transform="rotate(40 35 65)" />
            </g>

            <!-- Molecular Solute Radiance Particles -->
            <circle cx="210" cy="180" r="3" fill="#fbbf24"><animate attributeName="cy" values="180;150;180" dur="2s" repeatCount="indefinite"/></circle>
            <circle cx="245" cy="200" r="3.5" fill="#fbbf24"><animate attributeName="cy" values="200;165;200" dur="2.4s" repeatCount="indefinite"/></circle>
            <circle cx="230" cy="225" r="2.5" fill="#fbbf24"><animate attributeName="cy" values="225;185;225" dur="1.9s" repeatCount="indefinite"/></circle>

            <!-- Aromatic Steam Tendrils -->
            <path d="M 210 110 Q 200 80 215 60" stroke="#cbd5e1" stroke-width="2" fill="none" opacity="0.5"><animate attributeName="d" values="M 210 110 Q 200 80 215 60; M 210 110 Q 220 80 205 60; M 210 110 Q 200 80 215 60" dur="3s" repeatCount="indefinite"/></path>
            <path d="M 250 110 Q 260 80 245 60" stroke="#cbd5e1" stroke-width="2" fill="none" opacity="0.5"><animate attributeName="d" values="M 250 110 Q 260 80 245 60; M 250 110 Q 240 80 255 60; M 250 110 Q 260 80 245 60" dur="2.7s" repeatCount="indefinite"/></path>

            <!-- Header Title -->
            <rect x="40" y="15" width="380" height="42" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${vesselColor}" stroke-width="1.5" />
            <text x="230" y="34" fill="${vesselColor}" font-size="11" font-weight="bold" text-anchor="middle">${name}</text>
            <text x="230" y="47" fill="#cbd5e1" font-size="9" text-anchor="middle">${action}</text>

            <!-- Bioactive Tag -->
            <rect x="50" y="268" width="360" height="36" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#cbd5e1" stroke-width="1" />
            <text x="230" y="284" fill="#fbbf24" font-size="9.5" font-weight="bold" text-anchor="middle">Target Solutes Extracted:</text>
            <text x="230" y="297" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${actives}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${solventType === 'water' ? 'active' : ''}" id="btnSolvWater">💧 Water (Kwatha / Kashaya)</button>
          <button class="btn-sim ${solventType === 'alcohol' ? 'active' : ''}" id="btnSolvAlc">🍇 Hydro-Alcoholic (Asava)</button>
          <button class="btn-sim ${solventType === 'ghee' ? 'active' : ''}" id="btnSolvGhee">🧈 Cow's Ghee & Oil (Sneha Kalpana)</button>
        </div>
      `;

      document.getElementById('btnSolvWater').onclick = () => { solventType = 'water'; updateSim(); };
      document.getElementById('btnSolvAlc').onclick = () => { solventType = 'alcohol'; updateSim(); };
      document.getElementById('btnSolvGhee').onclick = () => { solventType = 'ghee'; updateSim(); };

      updateSim();
    }

    // 4. Asima Chatterjee Botanical Extraction Lab
    function simAsimaChatterjeeLab(canvas, controls, title, icon) {
      title.textContent = 'Prof. Asima Chatterjee: Fractional Solvent Extraction Lab';
      icon.textContent = '🔬';
      let stage = 'funnel'; // 'funnel' or 'crystals'

      function updateSim() {
        if (stage === 'funnel') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Separatory Funnel Stand -->
              <rect x="195" y="40" width="8" height="230" fill="#475569" />
              <rect x="140" y="260" width="120" height="12" rx="3" fill="#334155" />
              <rect x="175" y="100" width="48" height="8" rx="2" fill="#64748b" />

              <!-- Separatory Glass Funnel -->
              <!-- Top Bulge -->
              <ellipse cx="230" cy="110" rx="38" ry="45" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              <!-- Bottom Conical Stem -->
              <path d="M 200 135 L 225 210 L 225 240 L 235 240 L 235 210 L 260 135 Z" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              
              <!-- Stopcock Tap -->
              <rect x="220" y="215" width="20" height="6" rx="1" fill="#f59e0b" />

              <!-- Immiscible Two-Phase Solvent Extraction Layers -->
              <!-- Upper Organic Ether Layer (Yellow Phyto-Extract) -->
              <path d="M 194 105 Q 230 115 266 105 L 266 80 Q 230 65 194 80 Z" fill="#facc15" opacity="0.6" />
              <text x="320" y="95" fill="#fde68a" font-size="9" font-weight="bold">Upper Organic Solvent</text>
              <text x="320" y="107" fill="#94a3b8" font-size="8">Dissolved Alkaloids</text>

              <!-- Lower Aqueous Layer (Blue Polar Phase) -->
              <path d="M 194 105 Q 230 115 266 105 L 255 150 Q 230 170 205 150 Z" fill="#0284c7" opacity="0.5" />
              <text x="320" y="145" fill="#38bdf8" font-size="9" font-weight="bold">Lower Aqueous Solvent</text>
              <text x="320" y="157" fill="#94a3b8" font-size="8">Polar impurities</text>

              <!-- Conical Flask Collecting Isolated Phase Below -->
              <path d="M 215 245 L 200 280 L 260 280 L 245 245 Z" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="1.5" />
              <path d="M 204 270 L 200 280 L 260 280 L 256 270 Z" fill="#0284c7" opacity="0.6" />

              <!-- Heritage Profile Card -->
              <rect x="25" y="20" width="150" height="130" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#c084fc" stroke-width="1.5" />
              <text x="100" y="42" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">Prof. Asima Chatterjee</text>
              <text x="100" y="58" fill="#cbd5e1" font-size="8" text-anchor="middle">1917–2006 • Calcutta Univ</text>
              <text x="100" y="74" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">D.Sc. (1944) • Padma Bhushan</text>
              <text x="100" y="92" fill="#94a3b8" font-size="7.5" text-anchor="middle">Mastered solvent systems</text>
              <text x="100" y="105" fill="#94a3b8" font-size="7.5" text-anchor="middle">to isolate pure plant</text>
              <text x="100" y="118" fill="#34d399" font-size="7.5" font-weight="bold" text-anchor="middle">alkaloids & Ayush-56</text>

              <rect x="30" y="285" width="400" height="25" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1" />
              <text x="230" y="301" fill="#cbd5e1" font-size="9" text-anchor="middle">Differential solubility allows target alkaloids to transfer into the optimal solvent layer.</text>
            </svg>
          `;
        } else {
          // Crystallized Pure Alkaloids
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <rect x="25" y="25" width="410" height="270" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5" />
              <text x="230" y="50" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Isolated Medicinal Crystals: Ayush-56 (Anti-Epileptic Drug)</text>
              
              <!-- Glass Petri Dish -->
              <ellipse cx="230" cy="155" rx="120" ry="50" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="2" />
              
              <!-- Sparkling White/Golden Alkaloid Needle Crystals -->
              <g stroke="#fde68a" stroke-width="2" stroke-linecap="round">
                <line x1="180" y1="150" x2="200" y2="135" />
                <line x1="195" y1="160" x2="225" y2="150" />
                <line x1="210" y1="140" x2="235" y2="165" />
                <line x1="240" y1="155" x2="270" y2="140" />
                <line x1="220" y1="170" x2="250" y2="165" />
                <line x1="170" y1="165" x2="190" y2="175" />
                <line x1="255" y1="160" x2="280" y2="170" />
              </g>

              <rect x="50" y="235" width="360" height="45" rx="8" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1" />
              <text x="230" y="254" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Pure Bioactive Alkaloid Compound Successfully Isolated</text>
              <text x="230" y="269" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Extracted from Marsilea minuta • Commercialized as modern anti-epileptic treatment</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${stage === 'funnel' ? 'active' : ''}" id="btnLabFunnel">🧪 Separatory Funnel Solvent Extraction</button>
          <button class="btn-sim ${stage === 'crystals' ? 'active' : ''}" id="btnLabCrystals">✨ Isolated Pure Alkaloid Crystals (Ayush-56)</button>
        </div>
      `;

      document.getElementById('btnLabFunnel').onclick = () => { stage = 'funnel'; updateSim(); };
      document.getElementById('btnLabCrystals').onclick = () => { stage = 'crystals'; updateSim(); };

      updateSim();
    }

    // 5. Ningel Salt Wells & Traditional Salt Cakes
    function simManipurSaltWells(canvas, controls, title, icon) {
      title.textContent = 'Indigenous Science: Ningel Salt Wells of Manipur';
      icon.textContent = '🧂';
      let boilStage = 0; // 0: Raw Saline Brine, 1: Boiling Pan (Evaporation), 2: Traditional Salt Cakes

      function updateSim() {
        let titleText = '', subText = '';
        if (boilStage === 0) {
          titleText = 'Subterranean Saline Wells (Ningel, Thoubal District)';
          subText = 'Village women draw highly concentrated natural salty brine from deep stone wells.';
        } else if (boilStage === 1) {
          titleText = 'Thermal Pan Boiling (Solvent Evaporation)';
          subText = 'Water evaporates rapidly as steam, driving the solution past saturation into crystallization.';
        } else {
          titleText = 'Traditional Salt Cakes (Thum) Wrapped in Banana Leaves';
          subText = 'Precipitated salt is molded into flat circular cakes, dried, and tied for trade and rituals.';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            ${boilStage === 0 ? `
              <!-- Ningel Well Graphic -->
              <rect x="150" y="100" width="160" height="140" rx="10" fill="#334155" stroke="#94a3b8" stroke-width="2" />
              <ellipse cx="230" cy="100" rx="80" ry="25" fill="#1e293b" stroke="#94a3b8" stroke-width="2" />
              <!-- Saline Water Inside Well -->
              <ellipse cx="230" cy="115" rx="70" ry="20" fill="rgba(14, 165, 233, 0.4)" />
              <text x="230" y="120" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Natural Saline Brine Well</text>
              <!-- Wooden Pulley Beam -->
              <line x1="160" y1="100" x2="160" y2="40" stroke="#78350f" stroke-width="6" />
              <line x1="300" y1="100" x2="300" y2="40" stroke="#78350f" stroke-width="6" />
              <line x1="150" y1="45" x2="310" y2="45" stroke="#78350f" stroke-width="6" />
              <circle cx="230" cy="45" r="10" fill="#a16207" />
              <line x1="230" y1="55" x2="230" y2="105" stroke="#cbd5e1" stroke-width="2" />
              <!-- Bucket -->
              <rect x="220" y="105" width="20" height="20" fill="#d97706" rx="2" />
            ` : boilStage === 1 ? `
              <!-- Large Boiling Metal Pan -->
              <ellipse cx="230" cy="180" rx="160" ry="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
              <ellipse cx="230" cy="176" rx="145" ry="42" fill="rgba(245, 158, 11, 0.3)" />

              <!-- Crystallizing Salt Grains -->
              <g fill="#ffffff">
                <circle cx="160" cy="175" r="4" /><circle cx="200" cy="182" r="5" />
                <circle cx="240" cy="172" r="4.5" /><circle cx="270" cy="185" r="5" />
                <circle cx="220" cy="190" r="4" /><circle cx="180" cy="188" r="4.5" />
              </g>

              <!-- Rising Steam Clouds -->
              <ellipse cx="180" cy="120" rx="25" ry="15" fill="rgba(255, 255, 255, 0.25)"><animate attributeName="cy" values="120;90;120" dur="2.5s" repeatCount="indefinite"/></ellipse>
              <ellipse cx="240" cy="110" rx="30" ry="18" fill="rgba(255, 255, 255, 0.25)"><animate attributeName="cy" values="110;80;110" dur="2.2s" repeatCount="indefinite"/></ellipse>
              <ellipse cx="290" cy="125" rx="25" ry="15" fill="rgba(255, 255, 255, 0.25)"><animate attributeName="cy" values="125;95;125" dur="2.7s" repeatCount="indefinite"/></ellipse>
              <text x="230" y="70" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Water (Solvent) Evaporates as Steam ↑</text>

              <!-- Wood Fire Beneath Pan -->
              <g transform="translate(190, 220)">
                <path d="M 20 20 Q 10 -15 20 -30 Q 30 -15 20 20 Z" fill="#ef4444" />
                <path d="M 40 20 Q 30 -20 40 -35 Q 50 -20 40 20 Z" fill="#f59e0b" />
                <path d="M 60 20 Q 50 -15 60 -30 Q 70 -15 60 20 Z" fill="#ef4444" />
                <!-- Wood logs -->
                <rect x="0" y="20" width="80" height="8" rx="2" fill="#78350f" transform="rotate(-10 40 24)" />
                <rect x="0" y="20" width="80" height="8" rx="2" fill="#78350f" transform="rotate(10 40 24)" />
              </g>
            ` : `
              <!-- Traditional Manipuri Salt Cakes (Thum) -->
              <!-- Banana Leaf Base -->
              <ellipse cx="230" cy="180" rx="170" ry="55" fill="#15803d" stroke="#16a34a" stroke-width="2" />
              <!-- Leaf Veins -->
              <line x1="70" y1="180" x2="390" y2="180" stroke="#166534" stroke-width="2" />
              
              <!-- Circular Solidified Salt Cakes -->
              <circle cx="160" cy="175" r="32" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
              <text x="160" y="179" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Thum Cake</text>

              <circle cx="235" cy="165" r="36" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
              <text x="235" y="169" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Salt Cake</text>

              <circle cx="310" cy="180" r="30" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
              <text x="310" y="184" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Thum</text>
            `}

            <!-- Information Card -->
            <rect x="40" y="15" width="380" height="42" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5" />
            <text x="230" y="32" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">${titleText}</text>
            <text x="230" y="47" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${subText}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${boilStage === 0 ? 'active' : ''}" id="btnStageWell">💧 1. Drawing Saline Well Water</button>
          <button class="btn-sim ${boilStage === 1 ? 'active' : ''}" id="btnStageBoil">🔥 2. Thermal Pan Evaporation</button>
          <button class="btn-sim ${boilStage === 2 ? 'active' : ''}" id="btnStageCake">🌿 3. Traditional Salt Cakes (Thum)</button>
        </div>
      `;

      document.getElementById('btnStageWell').onclick = () => { boilStage = 0; updateSim(); };
      document.getElementById('btnStageBoil').onclick = () => { boilStage = 1; updateSim(); };
      document.getElementById('btnStageCake').onclick = () => { boilStage = 2; updateSim(); };

      updateSim();
    }

    // 6. Saturated vs Unsaturated Dynamic Spoonful Simulator
    function simSaturatedUnsaturated(canvas, controls, title, icon) {
      title.textContent = 'Solute Saturation Limit: Spoon-by-Spoon Dissolution';
      icon.textContent = '🥄';
      let spoons = 2; // 0 to 8 spoons (each spoon = 6 g in 100 mL, saturation limit = 6 spoons = 36 g)

      function updateSim() {
        const mass = spoons * 6;
        const isSaturated = spoons >= 6;
        const excessGrams = Math.max(0, mass - 36);

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Beaker with 100 mL Water -->
            <rect x="130" y="60" width="200" height="200" rx="8" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
            <rect x="134" y="110" width="192" height="146" rx="4" fill="rgba(14, 165, 233, 0.25)" />

            <!-- Dissolved Solute Particles in liquid -->
            <g fill="#38bdf8" opacity="0.8">
              ${(() => {
                let p = '';
                const count = Math.min(spoons, 6) * 7;
                for (let i = 0; i < count; i++) {
                  const cx = 145 + ((i * 23) % 170);
                  const cy = 125 + ((i * 19) % 115);
                  p += `<circle cx="${cx}" cy="${cy}" r="3.5" />`;
                }
                return p;
              })()}
            </g>

            <!-- Settled Undissolved Precipitate at Bottom if Saturated -->
            ${isSaturated && excessGrams > 0 ? `
              <path d="M 140 256 Q 230 ${256 - excessGrams * 2.5} 320 256 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
              <text x="230" y="${250 - excessGrams * 1.5}" fill="#0f172a" font-size="8.5" font-weight="bold" text-anchor="middle">
                ${excessGrams}g Undissolved Salt
              </text>
            ` : ''}

            <!-- Animated Spoon Dropping Salt -->
            <g transform="translate(230, 40)">
              <ellipse cx="0" cy="15" rx="16" ry="7" fill="#cbd5e1" />
              <line x1="0" y1="15" x2="60" y2="0" stroke="#94a3b8" stroke-width="4" stroke-linecap="round" />
              <!-- Grains falling -->
              <circle cx="-5" cy="30" r="2" fill="#fff" opacity="0.8"><animate attributeName="cy" values="30;60;30" dur="1s" repeatCount="indefinite"/></circle>
              <circle cx="2" cy="40" r="2" fill="#fff" opacity="0.8"><animate attributeName="cy" values="40;70;40" dur="1.2s" repeatCount="indefinite"/></circle>
            </g>

            <!-- Status Card -->
            <rect x="40" y="15" width="130" height="85" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${isSaturated ? '#f59e0b' : '#10b981'}" stroke-width="1.5" />
            <text x="105" y="35" fill="${isSaturated ? '#fbbf24' : '#34d399'}" font-size="10" font-weight="bold" text-anchor="middle">
              ${isSaturated ? 'SATURATED' : 'UNSATURATED'}
            </text>
            <text x="105" y="52" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Added: ${mass} g / 100 mL</text>
            <text x="105" y="68" fill="#38bdf8" font-size="8.5" text-anchor="middle">Dissolved: ${Math.min(mass, 36)} g</text>
            <text x="105" y="85" fill="${excessGrams > 0 ? '#fb7185' : '#34d399'}" font-size="8.5" font-weight="bold" text-anchor="middle">
              ${excessGrams > 0 ? `Excess: ${excessGrams} g` : 'Can dissolve more!'}
            </text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${isSaturated 
                ? 'Saturation reached at 36g! All solvent interparticle voids are full; excess settles at the bottom.' 
                : 'Unsaturated solution: Solvent interparticle gaps are still vacant and can dissolve more solute.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🥄</span> Spoons of Salt Added (6g each in 100 mL):</span>
          <input type="range" class="sim-slider" id="spoonSlider" min="0" max="8" value="${spoons}">
          <span class="control-value" id="spoonValText">${spoons} spoons (${spoons * 6}g)</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnSp1">1 Spoon (6g - Unsaturated)</button>
          <button class="btn-sim" id="btnSp6">6 Spoons (36g - Exact Saturation)</button>
          <button class="btn-sim" id="btnSp8">8 Spoons (48g - Saturated + Residue)</button>
        </div>
      `;

      const slider = document.getElementById('spoonSlider');
      slider.oninput = (e) => {
        spoons = parseInt(e.target.value);
        document.getElementById('spoonValText').textContent = `${spoons} spoons (${spoons * 6}g)`;
        updateSim();
      };

      document.getElementById('btnSp1').onclick = () => { spoons = 1; slider.value = 1; document.getElementById('spoonValText').textContent = '1 spoons (6g)'; updateSim(); };
      document.getElementById('btnSp6').onclick = () => { spoons = 6; slider.value = 6; document.getElementById('spoonValText').textContent = '6 spoons (36g)'; updateSim(); };
      document.getElementById('btnSp8').onclick = () => { spoons = 8; slider.value = 8; document.getElementById('spoonValText').textContent = '8 spoons (48g)'; updateSim(); };

      updateSim();
    }

    // 7. Solution Concentration & Dilution Gauge
    function simSolutionConcentration(canvas, controls, title, icon) {
      title.textContent = 'Concentration Spectrum: Dilute to Highly Concentrated';
      icon.textContent = '🧃';
      let soluteGrams = 5; // grams of KMnO4 in 200 mL
      let waterVolume = 200; // mL

      function updateSim() {
        const concPct = ((soluteGrams / waterVolume) * 100).toFixed(1);
        const opacity = Math.min(0.95, Math.max(0.15, (concPct / 8)));

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Beaker Container -->
            <rect x="130" y="60" width="200" height="200" rx="8" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
            
            <!-- Potassium Permanganate Liquid with Dynamic Color Density -->
            <rect x="134" y="${260 - (waterVolume * 0.75)}" width="192" height="${waterVolume * 0.75}" rx="4" fill="rgba(192, 132, 252, ${opacity})" />

            <!-- Graduations -->
            <line x1="130" y1="110" x2="150" y2="110" stroke="#38bdf8" stroke-width="1.5" />
            <text x="155" y="114" fill="#38bdf8" font-size="9">200 mL</text>
            <line x1="130" y1="185" x2="150" y2="185" stroke="#38bdf8" stroke-width="1.5" />
            <text x="155" y="189" fill="#38bdf8" font-size="9">100 mL</text>

            <!-- Dilution Water Tap -->
            <g transform="translate(215, 10)">
              <rect x="0" y="0" width="30" height="15" fill="#64748b" rx="2" />
              <path d="M 15 15 L 15 45" stroke="#38bdf8" stroke-width="5" stroke-linecap="round" />
              <!-- Water Stream Falling -->
              <line x1="15" y1="45" x2="15" y2="110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3" opacity="0.7" />
            </g>

            <!-- Concentration Meter Card -->
            <rect x="40" y="70" width="80" height="150" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#c084fc" stroke-width="1.5" />
            <text x="80" y="90" fill="#c084fc" font-size="9" font-weight="bold" text-anchor="middle">Concentration</text>
            <text x="80" y="115" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">${concPct}%</text>
            <text x="80" y="130" fill="#94a3b8" font-size="8" text-anchor="middle">(w/v)</text>

            <rect x="50" y="145" width="60" height="8" rx="4" fill="rgba(255, 255, 255, 0.1)" />
            <rect x="50" y="145" width="${Math.min(60, concPct * 7.5)}" height="8" rx="4" fill="#c084fc" />

            <text x="80" y="175" fill="${concPct < 2.5 ? '#34d399' : concPct < 6 ? '#fbbf24' : '#f43f5e'}" font-size="8.5" font-weight="bold" text-anchor="middle">
              ${concPct < 2.5 ? 'Very Dilute' : concPct < 6 ? 'Moderate' : 'Concentrated'}
            </text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Formula: (Solute Mass ${soluteGrams}g ÷ Solution Volume ${waterVolume}mL) × 100 = ${concPct}%
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🟣</span> Solute Added (g):</span>
          <input type="range" class="sim-slider" id="soluteSlider" min="1" max="25" value="${soluteGrams}">
          <span class="control-value" id="soluteValText">${soluteGrams} g</span>
        </div>
        <div class="control-row">
          <span class="control-label"><span>💧</span> Solvent Water Volume (mL):</span>
          <input type="range" class="sim-slider" id="volSlider" min="80" max="250" value="${waterVolume}">
          <span class="control-value" id="volValText">${waterVolume} mL</span>
        </div>
      `;

      const sSlider = document.getElementById('soluteSlider');
      sSlider.oninput = (e) => {
        soluteGrams = parseInt(e.target.value);
        document.getElementById('soluteValText').textContent = `${soluteGrams} g`;
        updateSim();
      };

      const vSlider = document.getElementById('volSlider');
      vSlider.oninput = (e) => {
        waterVolume = parseInt(e.target.value);
        document.getElementById('volValText').textContent = `${waterVolume} mL`;
        updateSim();
      };

      updateSim();
    }

    // 8. Solubility & Temperature Dynamics
    function simSolubilityTemperature(canvas, controls, title, icon) {
      title.textContent = 'Effect of Temperature on Solid Solubility';
      icon.textContent = '🌡️';
      let temp = 20; // 0 to 90 deg C

      function updateSim() {
        // Sugar solubility roughly 180g at 0C to 420g at 90C per 100 mL
        const solubility = Math.round(180 + (temp * 2.7));
        const flameHeight = Math.max(0, (temp - 20) * 0.8);

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Beaker with Solution -->
            <rect x="140" y="50" width="180" height="170" rx="8" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
            <rect x="144" y="90" width="172" height="126" rx="4" fill="rgba(14, 165, 233, 0.25)" />

            <!-- Dissolved Solute Particles Agitating with Heat -->
            <g fill="#38bdf8">
              ${(() => {
                let dots = '';
                const count = Math.round(solubility / 15);
                for (let i = 0; i < count; i++) {
                  const cx = 155 + ((i * 17) % 150);
                  const cy = 100 + ((i * 13) % 105);
                  dots += `<circle cx="${cx}" cy="${cy}" r="2.5" />`;
                }
                return dots;
              })()}
            </g>

            <!-- Thermometer dipping into Beaker -->
            <rect x="180" y="20" width="10" height="160" rx="5" fill="#f8fafc" stroke="#64748b" stroke-width="1" />
            <rect x="182" y="${180 - (temp * 1.5)}" width="6" height="${temp * 1.5}" fill="#ef4444" />
            <circle cx="185" cy="175" r="7" fill="#ef4444" />

            <!-- Bunsen Burner Flame Beneath -->
            ${temp > 20 ? `
              <g transform="translate(230, 240)">
                <path d="M 0 0 Q -15 -${flameHeight} 0 -${flameHeight * 1.4} Q 15 -${flameHeight} 0 0 Z" fill="#38bdf8" opacity="0.8" />
                <path d="M 0 0 Q -8 -${flameHeight * 0.6} 0 -${flameHeight} Q 8 -${flameHeight * 0.6} 0 0 Z" fill="#fbbf24" />
                <rect x="-12" y="0" width="24" height="25" fill="#475569" />
              </g>
            ` : `
              <rect x="218" y="240" width="24" height="25" fill="#475569" />
            `}

            <!-- Live Solubility Gauge Card -->
            <rect x="330" y="60" width="115" height="150" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5" />
            <text x="387" y="82" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Solubility Curve</text>
            <text x="387" y="105" fill="#38bdf8" font-size="16" font-weight="900" text-anchor="middle">${solubility} g</text>
            <text x="387" y="120" fill="#cbd5e1" font-size="8" text-anchor="middle">per 100 mL Water</text>
            
            <rect x="345" y="135" width="85" height="1" fill="rgba(255, 255, 255, 0.15)" />
            <text x="387" y="155" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Temperature:</text>
            <text x="387" y="175" fill="#ef4444" font-size="14" font-weight="bold" text-anchor="middle">${temp}°C</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              As temperature rises (${temp}°C), solvent molecules spread, increasing solubility to ${solubility} g/100 mL!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🔥</span> Solvent Temperature (°C):</span>
          <input type="range" class="sim-slider" id="solTempSlider" min="0" max="90" value="${temp}">
          <span class="control-value" id="solTempValText">${temp}°C</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnCoolTemp">❄️ Ice Cold (5°C)</button>
          <button class="btn-sim" id="btnRoomTemp">Room Temp (20°C)</button>
          <button class="btn-sim" id="btnHotTemp">🔥 Boiling Hot (85°C)</button>
        </div>
      `;

      const tSlider = document.getElementById('solTempSlider');
      tSlider.oninput = (e) => {
        temp = parseInt(e.target.value);
        document.getElementById('solTempValText').textContent = `${temp}°C`;
        updateSim();
      };

      document.getElementById('btnCoolTemp').onclick = () => { temp = 5; tSlider.value = 5; document.getElementById('solTempValText').textContent = '5°C'; updateSim(); };
      document.getElementById('btnRoomTemp').onclick = () => { temp = 20; tSlider.value = 20; document.getElementById('solTempValText').textContent = '20°C'; updateSim(); };
      document.getElementById('btnHotTemp').onclick = () => { temp = 85; tSlider.value = 85; document.getElementById('solTempValText').textContent = '85°C'; updateSim(); };

      updateSim();
    }

    // 9. Gas Solubility & Dissolved Oxygen Ecology
    function simGasSolubilityTemp(canvas, controls, title, icon) {
      title.textContent = 'Solubility of Gases: Dissolved Oxygen & Aquatic Respiration';
      icon.textContent = '🐟';
      let waterTemp = 10; // 5C to 40C

      function updateSim() {
        // DO drops from ~13 mg/L at 5C to ~6.5 mg/L at 40C
        const doValue = (14.2 - (waterTemp * 0.2)).toFixed(1);
        const fishHappy = waterTemp < 28;

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Aquarium Tank -->
            <rect x="40" y="40" width="380" height="220" rx="10" fill="rgba(14, 165, 233, ${waterTemp < 20 ? '0.35' : '0.15'})" stroke="#38bdf8" stroke-width="2" />
            
            <!-- Dissolved Oxygen Bubbles (More in cold, fewer in hot) -->
            <g fill="#e0f2fe">
              ${(() => {
                let bubs = '';
                const count = Math.round(doValue * 3);
                for (let i = 0; i < count; i++) {
                  const cx = 60 + ((i * 37) % 340);
                  const cy = 70 + ((i * 29) % 160);
                  const r = 2 + (i % 3);
                  bubs += `<circle cx="${cx}" cy="${cy}" r="${r}" opacity="0.75" />`;
                }
                return bubs;
              })()}
            </g>

            <!-- Swimming Fish -->
            <g transform="translate(${fishHappy ? '180, 130' : '280, 70'})">
              <!-- Fish Body -->
              <ellipse cx="40" cy="20" rx="30" ry="16" fill="${fishHappy ? '#f97316' : '#94a3b8'}" />
              <!-- Tail Fin -->
              <polygon points="10,20 -10,5 -10,35" fill="${fishHappy ? '#ea580c' : '#64748b'}" />
              <!-- Eye -->
              <circle cx="58" cy="16" r="3" fill="#ffffff" />
              <circle cx="59" cy="16" r="1.5" fill="#000000" />
              <!-- Gill Filaments -->
              <path d="M 48 10 Q 52 20 48 30" stroke="#fff" stroke-width="2" fill="none" opacity="0.6" />
            </g>

            <!-- Floating Escaping Gas Bubbles at Surface if Warm -->
            ${waterTemp >= 25 ? `
              <circle cx="150" cy="45" r="4" fill="#38bdf8" opacity="0.8"><animate attributeName="cy" values="45;20;45" dur="1.5s" repeatCount="indefinite"/></circle>
              <circle cx="230" cy="42" r="5" fill="#38bdf8" opacity="0.8"><animate attributeName="cy" values="42;15;42" dur="1.8s" repeatCount="indefinite"/></circle>
              <circle cx="310" cy="46" r="4.5" fill="#38bdf8" opacity="0.8"><animate attributeName="cy" values="46;22;46" dur="1.6s" repeatCount="indefinite"/></circle>
              <text x="230" y="30" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">O₂ Gas Escaping into Atmosphere! ↑</text>
            ` : ''}

            <!-- Dissolved Oxygen Gauge Card -->
            <rect x="55" y="55" width="130" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${fishHappy ? '#10b981' : '#ef4444'}" stroke-width="1.5" />
            <text x="120" y="73" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Dissolved Oxygen (DO)</text>
            <text x="120" y="96" fill="${fishHappy ? '#34d399' : '#f87171'}" font-size="16" font-weight="900" text-anchor="middle">${doValue} mg/L</text>
            <text x="120" y="114" fill="#cbd5e1" font-size="8" text-anchor="middle">Water Temp: ${waterTemp}°C</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${fishHappy 
                ? 'Cold water holds abundant dissolved oxygen (~' + doValue + ' mg/L); aquatic life breathes easily!' 
                : 'Thermal pollution! As water warms (' + waterTemp + '°C), gas solubility drops, depriving fish of oxygen.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>🌡️</span> River / Stream Water Temperature:</span>
          <input type="range" class="sim-slider" id="gasTempSlider" min="5" max="38" value="${waterTemp}">
          <span class="control-value" id="gasTempValText">${waterTemp}°C</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnStreamCold">🏔️ Cold Alpine Stream (8°C)</button>
          <button class="btn-sim" id="btnStreamWarm">☀️ Summer Pond (24°C)</button>
          <button class="btn-sim" id="btnStreamHot">🏭 Thermal Effluent (36°C)</button>
        </div>
      `;

      const slider = document.getElementById('gasTempSlider');
      slider.oninput = (e) => {
        waterTemp = parseInt(e.target.value);
        document.getElementById('gasTempValText').textContent = `${waterTemp}°C`;
        updateSim();
      };

      document.getElementById('btnStreamCold').onclick = () => { waterTemp = 8; slider.value = 8; document.getElementById('gasTempValText').textContent = '8°C'; updateSim(); };
      document.getElementById('btnStreamWarm').onclick = () => { waterTemp = 24; slider.value = 24; document.getElementById('gasTempValText').textContent = '24°C'; updateSim(); };
      document.getElementById('btnStreamHot').onclick = () => { waterTemp = 36; slider.value = 36; document.getElementById('gasTempValText').textContent = '36°C'; updateSim(); };

      updateSim();
    }

    // 10. Density: Mass per Unit Volume Simulator
    function simDensityMassVolume(canvas, controls, title, icon) {
      title.textContent = 'Density Lab: Mass ÷ Volume & Flotation Testing';
      icon.textContent = '⚖️';
      let mat = 'iron'; // 'iron', 'wood', 'alum', 'gold'

      function updateSim() {
        let name = '', mass = 0, vol = 20, density = 0, color = '', floats = false;
        if (mat === 'iron') {
          name = 'Iron (Fe)';
          vol = 20;
          mass = 157.4;
          density = 7.87;
          color = '#64748b';
          floats = false;
        } else if (mat === 'wood') {
          name = 'Pine Wood';
          vol = 20;
          mass = 12.0;
          density = 0.60;
          color = '#d97706';
          floats = true;
        } else if (mat === 'alum') {
          name = 'Aluminium (Al)';
          vol = 20;
          mass = 54.0;
          density = 2.70;
          color = '#94a3b8';
          floats = false;
        } else {
          name = '24K Gold (Au)';
          vol = 20;
          mass = 386.0;
          density = 19.30;
          color = '#f59e0b';
          floats = false;
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Left: Solid Block & Digital Scale -->
            <g transform="translate(60, 60)">
              <!-- Material Cube (20 cm3) -->
              <rect x="40" y="30" width="50" height="50" rx="4" fill="${color}" stroke="#ffffff" stroke-width="1.5" />
              <text x="65" y="60" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">${mat.toUpperCase()}</text>
              <text x="65" y="95" fill="#38bdf8" font-size="9" text-anchor="middle">Volume = 20 cm³</text>

              <!-- Digital Analytical Balance -->
              <rect x="15" y="110" width="100" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
              <rect x="25" y="118" width="80" height="24" rx="3" fill="#0f172a" />
              <text x="65" y="135" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">${mass} g</text>
            </g>

            <!-- Center Arrow -->
            <path d="M 200 130 L 235 130" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)" />

            <!-- Right: Water Immersion Tank -->
            <g transform="translate(250, 40)">
              <rect x="0" y="20" width="140" height="170" rx="6" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
              <!-- Water Level (Density = 1.0 g/cm3) -->
              <rect x="4" y="60" width="132" height="126" fill="rgba(14, 165, 233, 0.3)" />
              <text x="70" y="55" fill="#38bdf8" font-size="8.5" text-anchor="middle">Water (1.0 g/cm³)</text>

              <!-- Block Flotation / Sinking Behavior -->
              ${floats ? `
                <!-- Floating Wood Block at Surface -->
                <rect x="45" y="48" width="50" height="40" rx="3" fill="${color}" stroke="#ffffff" stroke-width="1.5" />
                <text x="70" y="72" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">FLOATS!</text>
              ` : `
                <!-- Sunken Block at Bottom -->
                <rect x="45" y="145" width="50" height="38" rx="3" fill="${color}" stroke="#ffffff" stroke-width="1.5" />
                <text x="70" y="168" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">SINKS!</text>
              `}
            </g>

            <!-- Formula Summary Card -->
            <rect x="30" y="235" width="400" height="65" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="255" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">
              ${name}: Density = Mass ÷ Volume = ${mass}g ÷ 20cm³ = ${density} g/cm³
            </text>
            <text x="230" y="272" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Relative Density = ${density} (Dimensionless) • ${floats ? 'Density < 1.0 g/cm³ (Floats on water)' : 'Density > 1.0 g/cm³ (Sinks in water)'}
            </text>
            <text x="230" y="288" fill="#94a3b8" font-size="8" text-anchor="middle">SI Unit Equivalent: ${Math.round(density * 1000)} kg/m³</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${mat === 'wood' ? 'active' : ''}" id="btnMatWood">🪵 Pine Wood (0.60 g/cm³)</button>
          <button class="btn-sim ${mat === 'alum' ? 'active' : ''}" id="btnMatAlum">🥫 Aluminium (2.70 g/cm³)</button>
          <button class="btn-sim ${mat === 'iron' ? 'active' : ''}" id="btnMatIron">🔩 Iron (7.87 g/cm³)</button>
          <button class="btn-sim ${mat === 'gold' ? 'active' : ''}" id="btnMatGold">🥇 Pure Gold (19.30 g/cm³)</button>
        </div>
      `;

      document.getElementById('btnMatWood').onclick = () => { mat = 'wood'; updateSim(); };
      document.getElementById('btnMatAlum').onclick = () => { mat = 'alum'; updateSim(); };
      document.getElementById('btnMatIron').onclick = () => { mat = 'iron'; updateSim(); };
      document.getElementById('btnMatGold').onclick = () => { mat = 'gold'; updateSim(); };

      updateSim();
    }

    // 11. Measuring Mass & Volume Precision
    function simMassVolumeMeasurement(canvas, controls, title, icon) {
      title.textContent = 'Laboratory Precision: Mass (g) vs Gravitational Weight (N)';
      icon.textContent = '⚖️';
      let environment = 'earth'; // 'earth' or 'moon'

      function updateSim() {
        const massGrams = 120; // invariant mass
        const massKg = 0.12;
        const gEarth = 9.8;
        const gMoon = 1.62;
        const weightN = (environment === 'earth' ? massKg * gEarth : massKg * gMoon).toFixed(2);

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Digital Balance Display -->
            <g transform="translate(60, 60)">
              <!-- Balance Platform -->
              <rect x="20" y="50" width="140" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
              <!-- Specimen -->
              <ellipse cx="90" cy="40" rx="30" ry="12" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5" />
              <!-- Digital Screen -->
              <rect x="35" y="85" width="110" height="35" rx="4" fill="#0f172a" />
              <text x="90" y="108" fill="#34d399" font-size="16" font-weight="900" text-anchor="middle">${massGrams}.00 g</text>
              <text x="90" y="130" fill="#94a3b8" font-size="8" text-anchor="middle">Invariant Mass (m)</text>
            </g>

            <!-- Spring Balance Measuring Weight (N) -->
            <g transform="translate(260, 40)">
              <!-- Outer Cylinder -->
              <rect x="40" y="20" width="40" height="150" rx="4" fill="rgba(30, 41, 59, 0.7)" stroke="#f59e0b" stroke-width="2" />
              <!-- Internal Spring -->
              <path d="M 60 40 Q 50 50 60 60 Q 70 70 60 80 Q 50 90 60 100" stroke="#fde68a" stroke-width="2.5" fill="none" />
              <!-- Scale pointer -->
              <line x1="40" y1="${environment === 'earth' ? '120' : '65'}" x2="80" y2="${environment === 'earth' ? '120' : '65'}" stroke="#ef4444" stroke-width="3" />
              <!-- Hook and hanging load -->
              <line x1="60" y1="${environment === 'earth' ? '120' : '65'}" x2="60" y2="190" stroke="#cbd5e1" stroke-width="2" />
              <circle cx="60" cy="205" r="14" fill="#f59e0b" />
              
              <!-- Weight Readout -->
              <text x="60" y="235" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">${weightN} N</text>
              <text x="60" y="248" fill="#94a3b8" font-size="8" text-anchor="middle">Gravitational Weight (W = mg)</text>
            </g>

            <!-- Environment Badge -->
            <rect x="30" y="270" width="400" height="35" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="287" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">
              ${environment === 'earth' ? 'Location: Earth (g = 9.8 N/kg)' : 'Location: Moon (g = 1.62 N/kg - 1/6th gravity)'}
            </text>
            <text x="230" y="299" fill="#cbd5e1" font-size="8.5" text-anchor="middle">
              Mass is constant (${massGrams} g) everywhere in the universe! Weight changes with gravity.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${environment === 'earth' ? 'active' : ''}" id="btnEnvEarth">🌍 Measure on Earth (g = 9.8 N/kg)</button>
          <button class="btn-sim ${environment === 'moon' ? 'active' : ''}" id="btnEnvMoon">🌕 Measure on Moon (g = 1.62 N/kg)</button>
        </div>
      `;

      document.getElementById('btnEnvEarth').onclick = () => { environment = 'earth'; updateSim(); };
      document.getElementById('btnEnvMoon').onclick = () => { environment = 'moon'; updateSim(); };

      updateSim();
    }

    // 12. Meniscus Reading Accuracy & Parallax Avoidance
    function simMeniscusReadingLab(canvas, controls, title, icon) {
      title.textContent = 'Meniscus Reading Protocols & Parallax Elimination';
      icon.textContent = '👁️';
      let eyePos = 'level'; // 'above', 'level', 'below'
      let liquidType = 'colorless'; // 'colorless' or 'colored'

      function updateSim() {
        let eyeY = 150;
        let readVal = 50.0;
        if (eyePos === 'above') {
          eyeY = 90;
          readVal = 52.5; // Overestimate
        } else if (eyePos === 'below') {
          eyeY = 210;
          readVal = 47.5; // Underestimate
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Glass Cylinder Section (Zoomed View) -->
            <rect x="140" y="50" width="120" height="210" rx="4" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2.5" />
            
            <!-- Liquid Fill inside cylinder -->
            <rect x="143" y="150" width="114" height="107" fill="${liquidType === 'colorless' ? 'rgba(14, 165, 233, 0.25)' : 'rgba(147, 51, 234, 0.7)'}" />

            <!-- Meniscus Surface Curve -->
            ${liquidType === 'colorless' ? `
              <!-- Concave Meniscus (Water curves down in middle) -->
              <path d="M 143 145 Q 200 155 257 145 L 257 155 Q 200 165 143 155 Z" fill="rgba(56, 189, 248, 0.4)" />
              <line x1="140" y1="150" x2="260" y2="150" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 2" />
            ` : `
              <!-- Colored Meniscus (Top surface line read) -->
              <line x1="140" y1="145" x2="260" y2="145" stroke="#f59e0b" stroke-width="2" />
            `}

            <!-- Calibration Marks -->
            <line x1="140" y1="110" x2="160" y2="110" stroke="#38bdf8" stroke-width="2" />
            <text x="130" y="113" fill="#38bdf8" font-size="9" text-anchor="end">60 mL</text>

            <line x1="140" y1="130" x2="155" y2="130" stroke="#38bdf8" stroke-width="1.5" />
            <text x="130" y="133" fill="#38bdf8" font-size="8" text-anchor="end">55 mL</text>

            <line x1="140" y1="150" x2="165" y2="150" stroke="#38bdf8" stroke-width="2.5" />
            <text x="130" y="153" fill="#34d399" font-size="10" font-weight="bold" text-anchor="end">50 mL</text>

            <line x1="140" y1="170" x2="155" y2="170" stroke="#38bdf8" stroke-width="1.5" />
            <text x="130" y="173" fill="#38bdf8" font-size="8" text-anchor="end">45 mL</text>

            <line x1="140" y1="190" x2="160" y2="190" stroke="#38bdf8" stroke-width="2" />
            <text x="130" y="193" fill="#38bdf8" font-size="9" text-anchor="end">40 mL</text>

            <!-- Line of Sight Sightline -->
            <line x1="330" y1="${eyeY}" x2="200" y2="150" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3" />

            <!-- Human Eye Graphic -->
            <g transform="translate(330, ${eyeY - 15})">
              <!-- Eyeball -->
              <path d="M 0 15 Q 25 0 50 15 Q 25 30 0 15 Z" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
              <!-- Iris & Pupil -->
              <circle cx="25" cy="15" r="8" fill="#0284c7" />
              <circle cx="25" cy="15" r="4" fill="#0f172a" />
            </g>

            <!-- Reading Output Card -->
            <rect x="290" y="200" width="150" height="65" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="${eyePos === 'level' ? '#10b981' : '#f43f5e'}" stroke-width="1.5" />
            <text x="365" y="218" fill="${eyePos === 'level' ? '#34d399' : '#fb7185'}" font-size="10" font-weight="bold" text-anchor="middle">
              ${eyePos === 'level' ? 'CORRECT EYE LEVEL' : 'PARALLAX ERROR!'}
            </text>
            <text x="365" y="238" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">${readVal} mL</text>
            <text x="365" y="254" fill="#cbd5e1" font-size="8" text-anchor="middle">
              ${eyePos === 'level' ? 'Exact True Value' : eyePos === 'above' ? 'Overestimated (+2.5 mL)' : 'Underestimated (-2.5 mL)'}
            </text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${liquidType === 'colorless' ? 'Rule: Read at bottom of concave meniscus at eye level.' : 'Colored solutions: Read at top boundary of meniscus.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${eyePos === 'above' ? 'active' : ''}" id="btnEyeAbove">⬆️ Look from Above (Parallax High)</button>
          <button class="btn-sim ${eyePos === 'level' ? 'active' : ''}" id="btnEyeLevel">👁️ Exact Eye Level (Accurate)</button>
          <button class="btn-sim ${eyePos === 'below' ? 'active' : ''}" id="btnEyeBelow">⬇️ Look from Below (Parallax Low)</button>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim ${liquidType === 'colorless' ? 'active' : ''}" id="btnLiqColorless">💧 Colorless Liquid (Water - Read Bottom)</button>
          <button class="btn-sim ${liquidType === 'colored' ? 'active' : ''}" id="btnLiqColored">🟣 Colored Solution (KMnO₄ - Read Top)</button>
        </div>
      `;

      document.getElementById('btnEyeAbove').onclick = () => { eyePos = 'above'; updateSim(); };
      document.getElementById('btnEyeLevel').onclick = () => { eyePos = 'level'; updateSim(); };
      document.getElementById('btnEyeBelow').onclick = () => { eyePos = 'below'; updateSim(); };

      document.getElementById('btnLiqColorless').onclick = () => { liquidType = 'colorless'; updateSim(); };
      document.getElementById('btnLiqColored').onclick = () => { liquidType = 'colored'; updateSim(); };

      updateSim();
    }

    // 13. Regular Geometric Shapes vs Water Displacement
    function simWaterDisplacementVolume(canvas, controls, title, icon) {
      title.textContent = 'Water Displacement Method for Irregular Solids';
      icon.textContent = '🪨';
      let submerged = false;

      function updateSim() {
        const vInitial = 50;
        const stoneVol = 18;
        const vFinal = submerged ? vInitial + stoneVol : vInitial;

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Graduated Measuring Cylinder -->
            <rect x="180" y="40" width="80" height="230" rx="6" fill="rgba(30, 41, 59, 0.4)" stroke="#38bdf8" stroke-width="2" />
            
            <!-- Water Column -->
            <rect x="183" y="${266 - (vFinal * 2.8)}" width="74" height="${vFinal * 2.8}" fill="rgba(14, 165, 233, 0.35)" />
            
            <!-- Scale Markings -->
            <line x1="180" y1="${266 - (50 * 2.8)}" x2="200" y2="${266 - (50 * 2.8)}" stroke="#38bdf8" stroke-width="2" />
            <text x="175" y="${266 - (50 * 2.8) + 3}" fill="#38bdf8" font-size="8" text-anchor="end">50 mL (V₁)</text>

            <line x1="180" y1="${266 - (68 * 2.8)}" x2="200" y2="${266 - (68 * 2.8)}" stroke="#f59e0b" stroke-width="2" />
            <text x="175" y="${266 - (68 * 2.8) + 3}" fill="#fbbf24" font-size="8" text-anchor="end">68 mL (V₂)</text>

            <!-- Suspended Irregular Stone on Thread -->
            <g transform="translate(220, ${submerged ? '210' : '50'})">
              <!-- Thin Thread -->
              <line x1="0" y1="${submerged ? '-170' : '-10'}" x2="0" y2="0" stroke="#cbd5e1" stroke-width="1.5" />
              <!-- Irregular Stone Shape -->
              <path d="M -15 -10 Q -5 -18 12 -12 Q 18 5 10 15 Q -10 18 -16 5 Z" fill="#64748b" stroke="#94a3b8" stroke-width="1.5" />
            </g>

            <!-- Water Splashes if Submerged -->
            ${submerged ? `
              <circle cx="210" cy="74" r="2.5" fill="#38bdf8" opacity="0.8" />
              <circle cx="230" cy="72" r="3" fill="#38bdf8" opacity="0.8" />
            ` : ''}

            <!-- Calculation Protocol Card -->
            <rect x="285" y="60" width="150" height="150" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="360" y="82" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Displacement Law</text>
            
            <text x="300" y="105" fill="#cbd5e1" font-size="8.5">Initial Vol (V₁): 50 mL</text>
            <text x="300" y="125" fill="#fbbf24" font-size="8.5">Final Vol (V₂): ${vFinal} mL</text>
            <line x1="300" y1="135" x2="420" y2="135" stroke="rgba(255,255,255,0.15)" />

            <text x="300" y="155" fill="#34d399" font-size="9" font-weight="bold">Stone Volume:</text>
            <text x="360" y="180" fill="#34d399" font-size="16" font-weight="900" text-anchor="middle">
              ${submerged ? stoneVol + ' cm³' : '---'}
            </text>
            <text x="360" y="195" fill="#94a3b8" font-size="7.5" text-anchor="middle">(V₂ - V₁ = 68 - 50)</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${submerged ? 'Submerged solid displaces a volume of liquid exactly equal to its own physical volume!' : 'Lower the irregular stone into water to measure its displaced volume.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${submerged ? 'active' : ''}" id="btnSubmergeStone">
            ${submerged ? '⬆️ Lift Stone Out of Water' : '⬇️ Lower Stone into Water (Displace)'}
          </button>
        </div>
      `;

      document.getElementById('btnSubmergeStone').onclick = () => { submerged = !submerged; updateSim(); };

      updateSim();
    }

    // 14. Temperature & Pressure Effects on Density (Hot Air Balloon)
    function simTempPressureDensity(canvas, controls, title, icon) {
      title.textContent = 'Thermal & Pressure Influence on Density: Hot Air Balloon';
      icon.textContent = '🎈';
      let heatOn = true;

      function updateSim() {
        const densityVal = heatOn ? '0.92 kg/m³' : '1.25 kg/m³';
        const balloonY = heatOn ? 60 : 150;

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Morning Sky Background with Clouds -->
            <rect x="20" y="20" width="420" height="240" rx="10" fill="#07192f" />
            
            <!-- Drifting Clouds -->
            <ellipse cx="90" cy="70" rx="35" ry="14" fill="rgba(255, 255, 255, 0.15)" />
            <ellipse cx="360" cy="110" rx="45" ry="18" fill="rgba(255, 255, 255, 0.15)" />

            <!-- Hot Air Balloon -->
            <g transform="translate(230, ${balloonY})">
              <!-- Balloon Envelope -->
              <path d="M 0 -50 C -45 -50 -55 0 -20 30 L -12 45 L 12 45 L 20 30 C 55 0 45 -50 0 -50 Z" fill="${heatOn ? '#f97316' : '#64748b'}" stroke="#fbbf24" stroke-width="2" />
              <!-- Decorative Stripes -->
              <path d="M 0 -50 C -20 -50 -25 0 -12 45" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.6" />
              <path d="M 0 -50 C 20 -50 25 0 12 45" stroke="#ffffff" stroke-width="1.5" fill="none" opacity="0.6" />

              <!-- Propane Burner Flame -->
              ${heatOn ? `
                <path d="M 0 48 Q -6 38 0 28 Q 6 38 0 48 Z" fill="#38bdf8" />
                <path d="M 0 48 Q -3 40 0 32 Q 3 40 0 48 Z" fill="#fbbf24" />
              ` : ''}

              <!-- Rigging Wires & Basket -->
              <line x1="-10" y1="45" x2="-8" y2="60" stroke="#cbd5e1" stroke-width="1" />
              <line x1="10" y1="45" x2="8" y2="60" stroke="#cbd5e1" stroke-width="1" />
              <rect x="-10" y="60" width="20" height="15" rx="2" fill="#78350f" stroke="#a16207" stroke-width="1" />
            </g>

            <!-- Density Readout Pill -->
            <rect x="50" y="40" width="130" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${heatOn ? '#f59e0b' : '#38bdf8'}" stroke-width="1.5" />
            <text x="115" y="58" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Internal Air Density:</text>
            <text x="115" y="80" fill="${heatOn ? '#fbbf24' : '#38bdf8'}" font-size="14" font-weight="900" text-anchor="middle">${densityVal}</text>
            <text x="115" y="96" fill="#94a3b8" font-size="7.5" text-anchor="middle">Ambient Air: 1.20 kg/m³</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${heatOn ? 'Burner expands internal air molecules • Density decreases below ambient air • Balloon ascends!' : 'Burner OFF: Internal air cools, density rises, balloon descends toward ground.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${heatOn ? 'active' : ''}" id="btnBurnerToggle">
            ${heatOn ? '🔥 Propane Burner ON (Lower Density → Ascend)' : '❄️ Propane Burner OFF (Higher Density → Descend)'}
          </button>
        </div>
      `;

      document.getElementById('btnBurnerToggle').onclick = () => { heatOn = !heatOn; updateSim(); };

      updateSim();
    }

    // 15. Anomalous Expansion of Water & Floating Ice
    function simWaterIceAnomalous(canvas, controls, title, icon) {
      title.textContent = 'Anomalous Expansion of Water: Maximum Density at 4°C';
      icon.textContent = '🧊';
      let season = 'winter'; // 'winter' or 'room'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Winter Lake Cross-Section -->
            <rect x="30" y="30" width="400" height="235" rx="10" fill="#07172b" stroke="#38bdf8" stroke-width="2" />
            
            ${season === 'winter' ? `
              <!-- Sub-Zero Atmosphere -->
              <rect x="32" y="32" width="396" height="50" fill="rgba(148, 163, 184, 0.2)" />
              <text x="230" y="55" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Freezing Winter Air (-15°C)</text>

              <!-- Floating Surface Ice Sheet (Density = 0.92 g/cm3) -->
              <rect x="32" y="82" width="396" height="35" fill="rgba(241, 245, 249, 0.85)" stroke="#93c5fd" stroke-width="1.5" />
              <text x="230" y="104" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">
                Floating Ice Layer (0°C • Density ~0.92 g/cm³)
              </text>

              <!-- Insulated Liquid Water Layer (Density = 1.0 g/cm3) -->
              <rect x="32" y="117" width="396" height="146" fill="rgba(14, 165, 233, 0.3)" />
              <text x="80" y="145" fill="#38bdf8" font-size="9">Water at 1°C</text>
              <text x="80" y="185" fill="#38bdf8" font-size="9">Water at 2°C</text>
              
              <!-- Lake Bottom: Densest Water at 4°C -->
              <rect x="32" y="225" width="396" height="38" fill="rgba(2, 132, 199, 0.4)" />
              <text x="230" y="247" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">
                Densest Water at Lake Bottom (4°C • Max Density 1.000 g/cm³)
              </text>

              <!-- Happy Fish Swimming Protected at Lake Bottom -->
              <g transform="translate(300, 215)">
                <ellipse cx="25" cy="12" rx="20" ry="10" fill="#f97316" />
                <polygon points="5,12 -8,2 -8,22" fill="#ea580c" />
                <circle cx="37" cy="10" r="2" fill="#ffffff" />
              </g>
            ` : `
              <!-- Warm Summer Season -->
              <rect x="32" y="32" width="396" height="231" fill="rgba(14, 165, 233, 0.25)" />
              <text x="230" y="70" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Summer Lake: Uniform Liquid State (22°C)</text>
              <g transform="translate(210, 150)">
                <ellipse cx="25" cy="12" rx="22" ry="11" fill="#f97316" />
                <polygon points="5,12 -8,2 -8,22" fill="#ea580c" />
                <circle cx="37" cy="10" r="2" fill="#ffffff" />
              </g>
            `}

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${season === 'winter' ? 'Ice floats because open hexagonal crystal cages expand volume by 9% • Insulates fish underneath!' : 'Liquid water attains its absolute maximum density at 4°C due to hydrogen bonding dynamics.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${season === 'winter' ? 'active' : ''}" id="btnSeasonWinter">❄️ Freezing Winter (-15°C Air → Floating Ice)</button>
          <button class="btn-sim ${season === 'room' ? 'active' : ''}" id="btnSeasonRoom">☀️ Warm Summer (22°C)</button>
        </div>
      `;

      document.getElementById('btnSeasonWinter').onclick = () => { season = 'winter'; updateSim(); };
      document.getElementById('btnSeasonRoom').onclick = () => { season = 'room'; updateSim(); };

      updateSim();
    }

    // 16. Earth's Planetary Density Stratification
    function simEarthDensityLayers(canvas, controls, title, icon) {
      title.textContent = 'Planetary Geology: Earth\'s Density Stratification';
      icon.textContent = '🌍';
      let selectedLayer = 'core'; // 'crust', 'mantle', 'outer', 'core'

      function updateSim() {
        let name = '', densityRange = '', comp = '', depth = '';
        if (selectedLayer === 'crust') {
          name = 'Crust (Outer Solid Shell)';
          densityRange = '2.7 to 3.0 g/cm³';
          comp = 'Granitic & Basaltic Silicates (Si, Al, Mg, O)';
          depth = '0 to 35 km depth';
        } else if (selectedLayer === 'mantle') {
          name = 'Mantle (Dense Silicate Rock)';
          densityRange = '3.3 to 5.7 g/cm³';
          comp = 'Peridotite & Dense Magnesium-Iron Silicates';
          depth = '35 to 2,890 km depth';
        } else if (selectedLayer === 'outer') {
          name = 'Outer Core (Liquid Metal)';
          densityRange = '9.9 to 12.2 g/cm³';
          comp = 'Molten Iron (Fe) & Nickel (Ni) Alloy';
          depth = '2,890 to 5,150 km depth';
        } else {
          name = 'Inner Core (Solid Metallic Sphere)';
          densityRange = '12.8 to 13.1 g/cm³';
          comp = 'Crystalline Solid Iron-Nickel under 3.6 Million atm';
          depth = '5,150 to 6,371 km depth (Center)';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Concentric Earth Shells Cross-Section -->
            <g transform="translate(160, 150)">
              <!-- Crust Layer -->
              <circle cx="0" cy="0" r="110" fill="#334155" stroke="#38bdf8" stroke-width="2" />
              <!-- Mantle Layer -->
              <circle cx="0" cy="0" r="95" fill="#d97706" stroke="#f59e0b" stroke-width="1.5" />
              <!-- Outer Core Layer -->
              <circle cx="0" cy="0" r="55" fill="#ea580c" stroke="#fbbf24" stroke-width="1.5" />
              <!-- Inner Core Layer -->
              <circle cx="0" cy="0" r="25" fill="#fef08a" stroke="#ffffff" stroke-width="1.5">
                <animate attributeName="r" values="25;27;25" dur="3s" repeatCount="indefinite" />
              </circle>
            </g>

            <!-- Layer Information Card -->
            <rect x="280" y="45" width="155" height="190" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="357" y="70" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">${name.split(' ')[0]}</text>
            
            <text x="290" y="95" fill="#cbd5e1" font-size="8">Density Range:</text>
            <text x="357" y="115" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">${densityRange}</text>

            <rect x="290" y="125" width="135" height="1" fill="rgba(255, 255, 255, 0.15)" />
            <text x="290" y="142" fill="#cbd5e1" font-size="8">Composition:</text>
            <text x="290" y="156" fill="#fbbf24" font-size="7.5">${comp}</text>

            <text x="290" y="178" fill="#cbd5e1" font-size="8">Depth:</text>
            <text x="290" y="192" fill="#94a3b8" font-size="7.5">${depth}</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Planetary Differentiation: Heavy iron sank to core (~13 g/cm³); light silicates floated to crust (~2.7 g/cm³).
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${selectedLayer === 'crust' ? 'active' : ''}" id="btnLayerCrust">🪨 Crust (2.7 g/cm³)</button>
          <button class="btn-sim ${selectedLayer === 'mantle' ? 'active' : ''}" id="btnLayerMantle">🌋 Mantle (4.5 g/cm³)</button>
          <button class="btn-sim ${selectedLayer === 'outer' ? 'active' : ''}" id="btnLayerOuter">🔥 Outer Core (11 g/cm³)</button>
          <button class="btn-sim ${selectedLayer === 'core' ? 'active' : ''}" id="btnLayerCore">⚡ Inner Core (13.1 g/cm³)</button>
        </div>
      `;

      document.getElementById('btnLayerCrust').onclick = () => { selectedLayer = 'crust'; updateSim(); };
      document.getElementById('btnLayerMantle').onclick = () => { selectedLayer = 'mantle'; updateSim(); };
      document.getElementById('btnLayerOuter').onclick = () => { selectedLayer = 'outer'; updateSim(); };
      document.getElementById('btnLayerCore').onclick = () => { selectedLayer = 'core'; updateSim(); };

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-solutions-density.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

