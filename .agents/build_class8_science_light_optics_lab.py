# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-light-optics.html
Class 8 Science - Chapter 10: Light and Optics
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Acharya Bhāskara II)
- 16 bespoke interactive SVG simulators with live controls, ray tracing, and rich animations
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
from class8_science_light_optics_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 10: Light and Optics Master Lab</title>
  
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
      --bg-primary: #060b14;
      --bg-secondary: #0b1424;
      --card-bg: rgba(11, 20, 36, 0.92);
      --card-border: rgba(56, 189, 248, 0.28);
      --accent-sky: #38bdf8;
      --accent-amber: #f59e0b;
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
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 75%, rgba(245, 158, 11, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(192, 132, 252, 0.05) 0%, transparent 60%);
    }

    /* Header & Navigation Bar */
    .lab-header {
      background: rgba(11, 20, 36, 0.96);
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
      background: linear-gradient(135deg, #f59e0b, #0284c7);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 18px rgba(245, 158, 11, 0.45);
    }

    .header-text h1 {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.01em;
    }

    .header-text .sub-badge {
      font-size: 0.72rem;
      color: var(--accent-amber);
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
      background: linear-gradient(90deg, #f59e0b, #38bdf8, #10b981);
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
      background: rgba(18, 30, 52, 0.8);
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
      background: linear-gradient(135deg, #f59e0b, #0284c7);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      position: relative;
      flex-shrink: 0;
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--accent-amber);
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
      color: var(--accent-amber);
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
      color: var(--accent-amber);
      background: rgba(245, 158, 11, 0.12);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(245, 158, 11, 0.3);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .slide-number-pill {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-sky);
      background: rgba(56, 189, 248, 0.12);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .slide-title {
      font-size: 1.55rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.25;
      background: linear-gradient(135deg, #ffffff, #fbbf24);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Vocabulary Box */
    .vocab-box {
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.35);
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
      color: var(--accent-amber);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .vocab-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.6rem;
    }

    .vocab-chip {
      background: rgba(11, 20, 36, 0.85);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 8px;
      padding: 0.55rem 0.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .vocab-word {
      font-size: 0.82rem;
      font-weight: 700;
      color: #fbbf24;
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
      color: #fbbf24;
    }

    /* Checkpoints Section */
    .checkpoints-card {
      background: rgba(11, 20, 36, 0.92);
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
      background: rgba(18, 30, 52, 0.6);
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
      background: rgba(11, 20, 36, 0.75);
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
      background: rgba(245, 158, 11, 0.15);
      border-color: var(--accent-amber);
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
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
      font-weight: 600;
    }

    .sim-canvas {
      width: 100%;
      min-height: 380px;
      background: rgba(5, 10, 18, 0.95);
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
      background: rgba(18, 30, 52, 0.55);
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
      color: #fbbf24;
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
      background: #fbbf24;
      cursor: pointer;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.8);
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
      background: linear-gradient(135deg, rgba(18, 30, 52, 0.95), rgba(11, 20, 36, 0.95));
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
      color: var(--accent-amber);
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
      background: rgba(18, 30, 52, 0.6);
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
      background: rgba(245, 158, 11, 0.15);
      border-color: var(--accent-amber);
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
      background: #0b1424;
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
      <div class="lab-icon">🔭</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 10</div>
        <h1>Light and Optics</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Mirror Foundations</span>
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
      <span>🔭</span>
      <div class="avatar-speaking-pulse" id="avatarPulse"></div>
    </div>
    <div class="avatar-dialogue-box">
      <div class="avatar-name-row">
        <span class="avatar-name">Acharya Bhāskara II • Classical Astronomer & Master of Light Optics</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Welcome to the Light & Optics Laboratory! Let us peer into the behavior of spherical mirrors, discover the geometry of reflection, and harness lenses that expand human vision across the cosmos.
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
          <span class="slide-tag" id="slideBadge">Mirror Foundations</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Spherical Mirrors Anatomy</h2>

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
            <span id="simIcon">🪞</span>
            <span id="simTitle">Interactive Optics Simulator</span>
          </div>
          <span class="sim-badge" id="simBadge">Live Ray-Tracing Lab</span>
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
        case 'spherical_mirror_anatomy_sim':
          simSphericalMirrorAnatomy(canvas, controls, title, icon);
          break;
        case 'concave_mirror_image_sim':
          simConcaveMirrorImage(canvas, controls, title, icon);
          break;
        case 'convex_mirror_fov_sim':
          simConvexMirrorFov(canvas, controls, title, icon);
          break;
        case 'lateral_inversion_sim':
          simLateralInversion(canvas, controls, title, icon);
          break;
        case 'concave_uses_sim':
          simConcaveUses(canvas, controls, title, icon);
          break;
        case 'convex_safety_mirrors_sim':
          simConvexSafetyMirrors(canvas, controls, title, icon);
          break;
        case 'laws_of_reflection_sim':
          simLawsOfReflection(canvas, controls, title, icon);
          break;
        case 'parallel_beams_mirrors_sim':
          simParallelBeamsMirrors(canvas, controls, title, icon);
          break;
        case 'solar_concentrator_sim':
          simSolarConcentrator(canvas, controls, title, icon);
          break;
        case 'lens_basics_sim':
          simLensBasics(canvas, controls, title, icon);
          break;
        case 'convex_lens_converging_sim':
          simConvexLensConverging(canvas, controls, title, icon);
          break;
        case 'concave_lens_diverging_sim':
          simConcaveLensDiverging(canvas, controls, title, icon);
          break;
        case 'convex_lens_imaging_sim':
          simConvexLensImaging(canvas, controls, title, icon);
          break;
        case 'concave_lens_imaging_sim':
          simConcaveLensImaging(canvas, controls, title, icon);
          break;
        case 'eye_optical_instruments_sim':
          simEyeOpticalInstruments(canvas, controls, title, icon);
          break;
        case 'bhaskara_water_optics_sim':
          simBhaskaraWaterOptics(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = '<div style="color: #94a3b8;">Simulator loading...</div>';
      }
    }

    // 1. Spherical Mirror Anatomy: Imaginary Hollow Sphere
    function simSphericalMirrorAnatomy(canvas, controls, title, icon) {
      title.textContent = 'Curvature Geometry: Hollow Sphere to Curved Mirror';
      icon.textContent = '🌐';
      let mirrorType = 'concave'; // 'concave' or 'convex'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Center of Curvature & Imaginary Hollow Sphere -->
            <circle cx="210" cy="160" r="110" fill="none" stroke="rgba(255, 255, 255, 0.15)" stroke-dasharray="5 5" />
            <circle cx="210" cy="160" r="4" fill="#f59e0b" />
            <text x="210" y="150" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Center of Curvature (C)</text>

            <!-- Radius Line -->
            <line x1="210" y1="160" x2="${mirrorType === 'concave' ? '320' : '100'}" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3" />
            <text x="${mirrorType === 'concave' ? '265' : '155'}" y="155" fill="#f59e0b" font-size="8.5" text-anchor="middle">Radius (R)</text>

            ${mirrorType === 'concave' ? `
              <!-- Concave Curved Section: Reflecting surface curves INWARD (facing left C) -->
              <path d="M 305 70 A 110 110 0 0 1 305 250" fill="none" stroke="#38bdf8" stroke-width="4" />
              <!-- Outer Shading (Non-reflecting back) -->
              <g stroke="#64748b" stroke-width="1.5">
                <line x1="305" y1="70" x2="315" y2="65" />
                <line x1="312" y1="95" x2="322" y2="90" />
                <line x1="318" y1="125" x2="328" y2="120" />
                <line x1="320" y1="160" x2="330" y2="160" />
                <line x1="318" y1="195" x2="328" y2="200" />
                <line x1="312" y1="225" x2="322" y2="230" />
                <line x1="305" y1="250" x2="315" y2="255" />
              </g>

              <!-- Inward Shiny Polish Indicator -->
              <text x="275" y="100" fill="#38bdf8" font-size="9" font-weight="bold">Reflecting Surface (Inward)</text>
              <path d="M 270 105 L 295 120" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrow)" />
            ` : `
              <!-- Convex Curved Section: Reflecting surface curves OUTWARD (facing left) -->
              <path d="M 115 70 A 110 110 0 0 1 115 250" fill="none" stroke="#38bdf8" stroke-width="4" />
              <!-- Inner Shading (Non-reflecting back on right side facing C) -->
              <g stroke="#64748b" stroke-width="1.5">
                <line x1="115" y1="70" x2="125" y2="75" />
                <line x1="108" y1="95" x2="118" y2="100" />
                <line x1="102" y1="125" x2="112" y2="128" />
                <line x1="100" y1="160" x2="110" y2="160" />
                <line x1="102" y1="195" x2="112" y2="192" />
                <line x1="108" y1="225" x2="118" y2="220" />
                <line x1="115" y1="250" x2="125" y2="245" />
              </g>

              <!-- Outward Shiny Polish Indicator -->
              <text x="60" y="100" fill="#38bdf8" font-size="9" font-weight="bold">Reflecting Surface (Outward)</text>
              <path d="M 70 105 L 98 120" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrow)" />
            `}

            <!-- Principal Axis -->
            <line x1="40" y1="160" x2="420" y2="160" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 2" />
            <text x="415" y="155" fill="#94a3b8" font-size="8" text-anchor="end">Principal Axis</text>

            <!-- Card Header -->
            <rect x="40" y="15" width="380" height="38" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="230" y="32" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">
              ${mirrorType === 'concave' ? 'Concave Mirror: Reflecting surface curves INWARDS (Outer back shaded)' : 'Convex Mirror: Reflecting surface curves OUTWARDS (Inner back shaded)'}
            </text>
            <text x="230" y="46" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Ground and polished from optical flat glass to match the hollow sphere curve.</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mirrorType === 'concave' ? 'active' : ''}" id="btnAnatConcave">🥣 Concave Mirror (Curves Inward)</button>
          <button class="btn-sim ${mirrorType === 'convex' ? 'active' : ''}" id="btnAnatConvex">🌐 Convex Mirror (Curves Outward)</button>
        </div>
      `;

      document.getElementById('btnAnatConcave').onclick = () => { mirrorType = 'concave'; updateSim(); };
      document.getElementById('btnAnatConvex').onclick = () => { mirrorType = 'convex'; updateSim(); };

      updateSim();
    }

    // 2. Concave Mirror Image Dynamics: Close vs Far
    function simConcaveMirrorImage(canvas, controls, title, icon) {
      title.textContent = 'Concave Mirror Dynamics: Erect/Enlarged to Inverted/Diminished';
      icon.textContent = '🕯️';
      let objDist = 8; // cm (4 to 35 cm) Focus at 15 cm

      function updateSim() {
        const isClose = objDist < 15; // inside focus: erect and magnified
        // Scale image height
        let imgHeight = 40;
        let isErect = true;
        let status = '';

        if (isClose) {
          isErect = true;
          imgHeight = Math.round(50 + (15 - objDist) * 5); // 50 to 90px
          status = 'Close (Inside Focus): Erect & Enlarged (Virtual Image - Dentist View)';
        } else {
          isErect = false;
          imgHeight = Math.max(15, Math.round(80 - (objDist - 15) * 2.8)); // 80 to 20px
          status = 'Distant (Beyond Focus): Inverted (Upside Down) & Diminishing';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Optical Bench Axis -->
            <line x1="30" y1="180" x2="430" y2="180" stroke="#64748b" stroke-width="1.5" />
            
            <!-- Concave Mirror on Right -->
            <path d="M 370 70 A 180 180 0 0 1 370 290" fill="none" stroke="#38bdf8" stroke-width="4" />
            <!-- Back shading -->
            <g stroke="#64748b" stroke-width="1.5">
              <line x1="370" y1="80" x2="380" y2="75" />
              <line x1="376" y1="110" x2="386" y2="105" />
              <line x1="380" y1="145" x2="390" y2="142" />
              <line x1="382" y1="180" x2="392" y2="180" />
              <line x1="380" y1="215" x2="390" y2="218" />
              <line x1="376" y1="250" x2="386" y2="255" />
              <line x1="370" y1="280" x2="380" y2="285" />
            </g>

            <!-- Focus Mark (F) at 15 cm (x = 240) -->
            <circle cx="250" cy="180" r="3" fill="#f59e0b" />
            <text x="250" y="196" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Focus (F)</text>

            <!-- Real Candle Object on Axis -->
            <g transform="translate(${380 - objDist * 9}, 180)">
              <!-- Candle Body -->
              <rect x="-6" y="-35" width="12" height="35" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
              <!-- Flame -->
              <path d="M 0 -35 Q -5 -45 0 -55 Q 5 -45 0 -35 Z" fill="#f59e0b">
                <animate attributeName="d" values="M 0 -35 Q -5 -45 0 -55 Q 5 -45 0 -35 Z; M 0 -35 Q -6 -47 0 -57 Q 4 -43 0 -35 Z; M 0 -35 Q -5 -45 0 -55 Q 5 -45 0 -35 Z" dur="0.8s" repeatCount="indefinite" />
              </path>
              <text x="0" y="15" fill="#e2e8f0" font-size="8" text-anchor="middle">Object</text>
            </g>

            <!-- Reflected Image -->
            ${isErect ? `
              <!-- Virtual Erect Image behind mirror -->
              <g transform="translate(410, 180)" opacity="0.85">
                <rect x="-${imgHeight*0.1}" y="-${imgHeight*0.7}" width="${imgHeight*0.2}" height="${imgHeight*0.7}" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-dasharray="3 2" />
                <path d="M 0 -${imgHeight*0.7} Q -${imgHeight*0.1} -${imgHeight*0.85} 0 -${imgHeight} Q ${imgHeight*0.1} -${imgHeight*0.85} 0 -${imgHeight*0.7} Z" fill="#38bdf8" />
                <text x="0" y="20" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Erect Image</text>
              </g>
            ` : `
              <!-- Real Inverted Image in front of mirror -->
              <g transform="translate(${Math.max(60, 250 - (objDist - 15) * 5)}, 180)">
                <!-- Inverted Candle (Pointing Downwards!) -->
                <rect x="-${imgHeight*0.1}" y="0" width="${imgHeight*0.2}" height="${imgHeight*0.7}" fill="#f59e0b" opacity="0.6" stroke="#fbbf24" stroke-width="1" />
                <path d="M 0 ${imgHeight*0.7} Q -${imgHeight*0.1} ${imgHeight*0.85} 0 ${imgHeight} Q ${imgHeight*0.1} ${imgHeight*0.85} 0 ${imgHeight*0.7} Z" fill="#ef4444" />
                <text x="0" y="-10" fill="#f87171" font-size="8.5" font-weight="bold" text-anchor="middle">Inverted Image</text>
              </g>
            `}

            <!-- Top Indicator Bar -->
            <rect x="30" y="15" width="400" height="38" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${isErect ? '#10b981' : '#f59e0b'}" stroke-width="1.5" />
            <text x="230" y="32" fill="${isErect ? '#34d399' : '#fbbf24'}" font-size="10.5" font-weight="bold" text-anchor="middle">${status}</text>
            <text x="230" y="46" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Object Distance: ${objDist} cm (Focus at 15 cm)</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>📏</span> Object Distance from Mirror:</span>
          <input type="range" class="sim-slider" id="objDistSlider" min="5" max="32" value="${objDist}">
          <span class="control-value" id="objDistValText">${objDist} cm</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnConcClose">🔍 Close Up (8 cm - Erect Dentist View)</button>
          <button class="btn-sim" id="btnConcFar">🕯️ Far Away (25 cm - Inverted Projection)</button>
        </div>
      `;

      const slider = document.getElementById('objDistSlider');
      slider.oninput = (e) => {
        objDist = parseInt(e.target.value);
        document.getElementById('objDistValText').textContent = `${objDist} cm`;
        updateSim();
      };

      document.getElementById('btnConcClose').onclick = () => { objDist = 8; slider.value = 8; document.getElementById('objDistValText').textContent = '8 cm'; updateSim(); };
      document.getElementById('btnConcFar').onclick = () => { objDist = 25; slider.value = 25; document.getElementById('objDistValText').textContent = '25 cm'; updateSim(); };

      updateSim();
    }

    // 3. Convex Mirror Field of View vs Plane Mirror
    function simConvexMirrorFov(canvas, controls, title, icon) {
      title.textContent = 'Convex Mirror Panoramic Field of View vs Plane Mirror';
      icon.textContent = '🚗';
      let mirrorMode = 'convex'; // 'convex' or 'plane'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Highway Scene with Multiple Traffic Cars -->
            <rect x="25" y="20" width="410" height="150" rx="10" fill="#1e293b" />
            <line x1="25" y1="95" x2="435" y2="95" stroke="#f59e0b" stroke-width="2" stroke-dasharray="8 6" />

            <!-- Three Traffic Cars Behind -->
            <!-- Car 1 (Left Lane Red) -->
            <g transform="translate(60, 45)">
              <rect x="0" y="0" width="45" height="25" rx="4" fill="#ef4444" />
              <rect x="10" y="4" width="20" height="17" fill="#38bdf8" opacity="0.6" />
              <circle cx="10" cy="25" r="4" fill="#000" /><circle cx="35" cy="25" r="4" fill="#000" />
            </g>

            <!-- Car 2 (Center Lane Green) -->
            <g transform="translate(200, 110)">
              <rect x="0" y="0" width="50" height="28" rx="4" fill="#10b981" />
              <rect x="12" y="5" width="22" height="18" fill="#38bdf8" opacity="0.6" />
              <circle cx="12" cy="28" r="4.5" fill="#000" /><circle cx="38" cy="28" r="4.5" fill="#000" />
            </g>

            <!-- Car 3 (Right Lane Yellow) -->
            <g transform="translate(340, 50)">
              <rect x="0" y="0" width="45" height="25" rx="4" fill="#facc15" />
              <rect x="10" y="4" width="20" height="17" fill="#38bdf8" opacity="0.6" />
              <circle cx="10" cy="25" r="4" fill="#000" /><circle cx="35" cy="25" r="4" fill="#000" />
            </g>

            <!-- Driver's Side Mirror Frame Below -->
            <g transform="translate(170, 185)">
              <rect x="0" y="0" width="120" height="75" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
              
              ${mirrorMode === 'convex' ? `
                <!-- Convex Mirror: Captures ALL 3 CARS in wide, compact view! -->
                <rect x="6" y="6" width="108" height="63" rx="8" fill="rgba(56, 189, 248, 0.25)" />
                <!-- Mini Red Car -->
                <rect x="16" y="25" width="20" height="12" rx="2" fill="#ef4444" />
                <!-- Mini Green Car -->
                <rect x="48" y="32" width="22" height="14" rx="2" fill="#10b981" />
                <!-- Mini Yellow Car -->
                <rect x="80" y="22" width="20" height="12" rx="2" fill="#facc15" />

                <!-- Wide Angle Ray Lines -->
                <path d="M 60 0 L -80 -80" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2" />
                <path d="M 60 0 L 200 -80" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2" />
              ` : `
                <!-- Plane Mirror: Narrow Field of View (Captures only Center Green Car!) -->
                <rect x="6" y="6" width="108" height="63" rx="8" fill="rgba(255, 255, 255, 0.2)" />
                <!-- Only Center Green Car Visible! Others in Blind Spot -->
                <rect x="42" y="24" width="34" height="20" rx="3" fill="#10b981" />
                <text x="60" y="58" fill="#fca5a5" font-size="7.5" font-weight="bold" text-anchor="middle">Cars 1 & 3 in BLIND SPOT!</text>

                <!-- Narrow Angle Rays -->
                <path d="M 60 0 L 20 -80" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 2" />
                <path d="M 60 0 L 100 -80" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 2" />
              `}
            </g>

            <!-- Bottom Evaluation Card -->
            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${mirrorMode === 'convex' ? 'Convex mirror provides an expansive panoramic view, capturing all 3 highway lanes simultaneously!' : 'Plane mirror has narrow view: side vehicles vanish into dangerous blind spots.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mirrorMode === 'convex' ? 'active' : ''}" id="btnFovConvex">🌐 Convex Wing Mirror (Wide View - All Cars)</button>
          <button class="btn-sim ${mirrorMode === 'plane' ? 'active' : ''}" id="btnFovPlane">🪞 Flat Plane Mirror (Narrow View - Blind Spots)</button>
        </div>
      `;

      document.getElementById('btnFovConvex').onclick = () => { mirrorMode = 'convex'; updateSim(); };
      document.getElementById('btnFovPlane').onclick = () => { mirrorMode = 'plane'; updateSim(); };

      updateSim();
    }

    // 4. Lateral Inversion: Hand & Ambulance Lettering
    function simLateralInversion(canvas, controls, title, icon) {
      title.textContent = 'Lateral Inversion: Horizontal Left-Right Reversal';
      icon.textContent = '🚑';
      let mode = 'ambulance'; // 'ambulance' or 'person'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Mirror Dividing Plane Down Center -->
            <line x1="230" y1="40" x2="230" y2="260" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 3" />
            <text x="230" y="32" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Mirror Plane</text>

            ${mode === 'ambulance' ? `
              <!-- Left Side: Actual Ambulance Front Hood Text (Reversed Lettering) -->
              <g transform="translate(40, 110)">
                <rect x="0" y="0" width="160" height="70" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2" />
                <text x="80" y="32" fill="#ef4444" font-size="16" font-weight="900" text-anchor="middle" letter-spacing="3">ƎƆИA⅃UBMA</text>
                <text x="80" y="55" fill="#cbd5e1" font-size="8" text-anchor="middle">Painted on Ambulance Hood</text>
              </g>

              <!-- Reflection Arrow -->
              <path d="M 195 145 L 215 145" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)" />

              <!-- Right Side: Virtual Reflection in Rear-View Mirror (Readable!) -->
              <g transform="translate(260, 110)">
                <rect x="0" y="0" width="160" height="70" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2" />
                <text x="80" y="32" fill="#34d399" font-size="16" font-weight="900" text-anchor="middle" letter-spacing="3">AMBULANCE</text>
                <text x="80" y="55" fill="#34d399" font-size="8.5" font-weight="bold" text-anchor="middle">Seen in Driver's Rear-View Mirror!</text>
              </g>
            ` : `
              <!-- Left Side: Real Person Raising Right Hand -->
              <g transform="translate(100, 100)">
                <circle cx="40" cy="25" r="16" fill="#fde047" stroke="#ca8a04" stroke-width="1.5" />
                <line x1="40" y1="41" x2="40" y2="95" stroke="#38bdf8" stroke-width="4" />
                <!-- Left arm down -->
                <line x1="40" y1="55" x2="15" y2="85" stroke="#38bdf8" stroke-width="3" />
                <!-- Right arm RAISED UP -->
                <line x1="40" y1="55" x2="70" y2="25" stroke="#ef4444" stroke-width="3.5" />
                <circle cx="70" cy="25" r="5" fill="#ef4444" />
                <text x="40" y="115" fill="#cbd5e1" font-size="8.5" font-weight="bold" text-anchor="middle">Raises RIGHT Hand</text>
              </g>

              <!-- Right Side: Reflected Figure Raising Left Hand! -->
              <g transform="translate(280, 100)">
                <circle cx="40" cy="25" r="16" fill="#fde047" stroke="#ca8a04" stroke-width="1.5" opacity="0.8" />
                <line x1="40" y1="41" x2="40" y2="95" stroke="#38bdf8" stroke-width="4" opacity="0.8" />
                <!-- Right arm down -->
                <line x1="40" y1="55" x2="65" y2="85" stroke="#38bdf8" stroke-width="3" opacity="0.8" />
                <!-- Left arm RAISED UP in mirror view -->
                <line x1="40" y1="55" x2="10" y2="25" stroke="#ef4444" stroke-width="3.5" opacity="0.8" />
                <circle cx="10" cy="25" r="5" fill="#ef4444" opacity="0.8" />
                <text x="40" y="115" fill="#fb7185" font-size="8.5" font-weight="bold" text-anchor="middle">Appears as LEFT Hand!</text>
              </g>
            `}

            <!-- Rule Card -->
            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Lateral inversion flips horizontal coordinates across plane, concave, and convex mirrors identically!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mode === 'ambulance' ? 'active' : ''}" id="btnLatAmb">🚑 Ambulance Reversal Signage</button>
          <button class="btn-sim ${mode === 'person' ? 'active' : ''}" id="btnLatPerson">🙋 Person Raising Right Hand</button>
        </div>
      `;

      document.getElementById('btnLatAmb').onclick = () => { mode = 'ambulance'; updateSim(); };
      document.getElementById('btnLatPerson').onclick = () => { mode = 'person'; updateSim(); };

      updateSim();
    }

    // 5. Concave Mirror Practical Applications
    function simConcaveUses(canvas, controls, title, icon) {
      title.textContent = 'Practical Engineering: Headlights, Dental & Telescope Optics';
      icon.textContent = '🔦';
      let useTab = 'headlight'; // 'headlight', 'dental', 'telescope'

      function updateSim() {
        if (useTab === 'headlight') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Vehicle Headlight Reflector Housing -->
              <path d="M 170 70 Q 70 160 170 250" fill="none" stroke="#38bdf8" stroke-width="5" />
              <!-- Filament Bulb positioned at Focus F -->
              <circle cx="120" cy="160" r="10" fill="#fde047" stroke="#eab308" stroke-width="2">
                <animate attributeName="r" values="10;12;10" dur="1s" repeatCount="indefinite" />
              </circle>
              <text x="120" y="185" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Bulb at Focus</text>

              <!-- Diverging rays from bulb striking reflector and reflecting PARALLEL forward! -->
              <g stroke="#fef08a" stroke-width="2" opacity="0.8">
                <!-- Ray 1 -->
                <line x1="120" y1="160" x2="135" y2="95" />
                <line x1="135" y1="95" x2="420" y2="95" stroke-dasharray="6 3" />
                <!-- Ray 2 -->
                <line x1="120" y1="160" x2="105" y2="130" />
                <line x1="105" y1="130" x2="420" y2="130" stroke-dasharray="6 3" />
                <!-- Center Ray -->
                <line x1="120" y1="160" x2="420" y2="160" stroke-dasharray="6 3" />
                <!-- Ray 4 -->
                <line x1="120" y1="160" x2="105" y2="190" />
                <line x1="105" y1="190" x2="420" y2="190" stroke-dasharray="6 3" />
                <!-- Ray 5 -->
                <line x1="120" y1="160" x2="135" y2="225" />
                <line x1="135" y1="225" x2="420" y2="225" stroke-dasharray="6 3" />
              </g>

              <rect x="250" y="30" width="180" height="42" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5" />
              <text x="340" y="48" fill="#fbbf24" font-size="9.5" font-weight="bold" text-anchor="middle">Powerful Parallel Forward Beam</text>
              <text x="340" y="62" fill="#cbd5e1" font-size="8" text-anchor="middle">Illuminates distant road hazards clearly.</text>
            </svg>
          `;
        } else if (useTab === 'dental') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Dentist Examination Handle & Concave Mirror -->
              <line x1="80" y1="260" x2="180" y2="160" stroke="#94a3b8" stroke-width="8" stroke-linecap="round" />
              <ellipse cx="205" cy="135" rx="35" ry="30" fill="rgba(30, 41, 59, 0.5)" stroke="#38bdf8" stroke-width="3" />
              
              <!-- Reflected Molar Tooth (Magnified 3x Inside Mirror!) -->
              <g transform="translate(195, 115)">
                <!-- Big Molar Tooth Crown -->
                <path d="M 0 10 Q 5 -10 15 0 Q 25 -10 30 10 L 25 35 L 5 35 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
                <!-- Cavity dot magnified -->
                <circle cx="15" cy="10" r="3.5" fill="#ef4444" />
                <text x="15" y="48" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Magnified Cavity!</text>
              </g>

              <!-- Actual Tiny Tooth Outside -->
              <g transform="translate(320, 160)">
                <path d="M 0 5 Q 2 -3 6 0 Q 10 -3 12 5 L 10 18 L 2 18 Z" fill="#ffffff" />
                <circle cx="6" cy="5" r="1" fill="#ef4444" />
                <text x="6" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Actual Tiny Tooth</text>
              </g>

              <rect x="50" y="25" width="360" height="45" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#10b981" stroke-width="1.5" />
              <text x="230" y="44" fill="#34d399" font-size="10.5" font-weight="bold" text-anchor="middle">Dentist Concave Mirror</text>
              <text x="230" y="58" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Produces an erect, enlarged virtual image to inspect hidden cavities safely.</text>
            </svg>
          `;
        } else {
          // Reflecting Astronomical Telescope
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Telescope Tube Body -->
              <rect x="80" y="70" width="280" height="150" fill="rgba(15, 23, 42, 0.85)" stroke="#64748b" stroke-width="2" />
              
              <!-- Primary Giant Concave Mirror at Base (Left) -->
              <path d="M 90 75 Q 115 145 90 215" fill="none" stroke="#38bdf8" stroke-width="6" />
              <text x="90" y="235" fill="#38bdf8" font-size="8.5" font-weight="bold">Primary Concave Mirror</text>

              <!-- Secondary Diagonal Flat Mirror in center -->
              <line x1="280" y1="130" x2="300" y2="160" stroke="#f59e0b" stroke-width="3" />

              <!-- Eyepiece Tube at Top -->
              <rect x="275" y="35" width="30" height="35" fill="#334155" stroke="#94a3b8" stroke-width="1" />
              <text x="290" y="28" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="middle">Eyepiece</text>

              <!-- Parallel Starlight Rays Entering from Right -->
              <g stroke="#fde047" stroke-width="1.5" opacity="0.75">
                <line x1="360" y1="90" x2="95" y2="90" />
                <line x1="95" y1="90" x2="288" y2="142" />
                <line x1="288" y1="142" x2="290" y2="40" />

                <line x1="360" y1="200" x2="95" y2="200" />
                <line x1="95" y1="200" x2="292" y2="148" />
                <line x1="292" y1="148" x2="290" y2="40" />
              </g>

              <rect x="50" y="260" width="360" height="40" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1" />
              <text x="230" y="278" fill="#38bdf8" font-size="9.5" font-weight="bold" text-anchor="middle">Newtonian Reflecting Astronomical Telescope</text>
              <text x="230" y="291" fill="#cbd5e1" font-size="8" text-anchor="middle">Large concave mirror gathers parallel starlight without color-distortion (chromatic aberration).</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${useTab === 'headlight' ? 'active' : ''}" id="btnTabHeadlight">🔦 Torch / Headlight (Parallel Beam)</button>
          <button class="btn-sim ${useTab === 'dental' ? 'active' : ''}" id="btnTabDental">🦷 Dental Inspection Mirror (Magnification)</button>
          <button class="btn-sim ${useTab === 'telescope' ? 'active' : ''}" id="btnTabTelescope">🔭 Reflecting Telescope (Starlight Focus)</button>
        </div>
      `;

      document.getElementById('btnTabHeadlight').onclick = () => { useTab = 'headlight'; updateSim(); };
      document.getElementById('btnTabDental').onclick = () => { useTab = 'dental'; updateSim(); };
      document.getElementById('btnTabTelescope').onclick = () => { useTab = 'telescope'; updateSim(); };

      updateSim();
    }

    // 6. Convex Safety Mirrors: Blind Intersections
    function simConvexSafetyMirrors(canvas, controls, title, icon) {
      title.textContent = 'Collision Prevention: Blind Intersections & Security';
      icon.textContent = '🛡️';
      let hasMirror = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Blind T-Junction Roadway -->
            <rect x="30" y="30" width="400" height="235" rx="8" fill="#0f172a" />
            <!-- Vertical Road -->
            <rect x="180" y="30" width="90" height="235" fill="#1e293b" />
            <!-- Horizontal Road -->
            <rect x="30" y="110" width="400" height="85" fill="#1e293b" />

            <!-- Blind Wall Blocking Direct Line of Sight -->
            <rect x="30" y="30" width="150" height="80" fill="#78350f" stroke="#a16207" stroke-width="2" />
            <text x="105" y="75" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">BLIND WALL</text>

            <!-- Blue Car A (Moving East) -->
            <g transform="translate(120, 135)">
              <rect x="0" y="0" width="35" height="22" rx="3" fill="#0284c7" />
              <circle cx="8" cy="22" r="3" fill="#000" /><circle cx="27" cy="22" r="3" fill="#000" />
              <text x="17" y="14" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Car A</text>
            </g>

            <!-- Red Car B (Moving South) -->
            <g transform="translate(205, 50)">
              <rect x="0" y="0" width="22" height="35" rx="3" fill="#ef4444" />
              <circle cx="0" cy="8" r="3" fill="#000" /><circle cx="0" cy="27" r="3" fill="#000" />
              <text x="11" y="20" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">B</text>
            </g>

            <!-- Convex Safety Mirror at Corner -->
            ${hasMirror ? `
              <circle cx="180" cy="110" r="16" fill="rgba(56, 189, 248, 0.4)" stroke="#f59e0b" stroke-width="2.5" />
              <!-- Reflection Lines connecting Car A and Car B -->
              <line x1="140" y1="145" x2="180" y2="110" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2" />
              <line x1="180" y1="110" x2="215" y2="70" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2" />
              <text x="210" y="105" fill="#34d399" font-size="8.5" font-weight="bold">Visible via Convex Mirror! ✓</text>
            ` : `
              <!-- Blind Collision Risk! -->
              <line x1="140" y1="145" x2="215" y2="70" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3" opacity="0.3" />
              <text x="180" y="105" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">NO VISIBILITY! ❌</text>
            `}

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${hasMirror ? 'Convex mirror reflects around the blind wall, alerting both drivers in advance!' : 'Without convex mirror, neither driver can see the cross-traffic around the blind corner.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${hasMirror ? 'active' : ''}" id="btnToggleSafetyMirror">
            ${hasMirror ? '🛡️ Convex Safety Mirror Installed (Safe View)' : '⚠️ Remove Mirror (Blind Collision Hazard)'}
          </button>
        </div>
      `;

      document.getElementById('btnToggleSafetyMirror').onclick = () => { hasMirror = !hasMirror; updateSim(); };

      updateSim();
    }

    // 7. Universal Laws of Reflection Simulator
    function simLawsOfReflection(canvas, controls, title, icon) {
      title.textContent = 'Universal Laws of Reflection: i = r Interactive Ray Tracer';
      icon.textContent = '📐';
      let angleI = 40; // 0 to 75 deg

      function updateSim() {
        const rad = (angleI * Math.PI) / 180;
        const rayLen = 140;
        // Point of incidence at (230, 200)
        const inX = 230 - rayLen * Math.sin(rad);
        const inY = 200 - rayLen * Math.cos(rad);
        const refX = 230 + rayLen * Math.sin(rad);
        const refY = 200 - rayLen * Math.cos(rad);

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Mirror Surface Line -->
            <line x1="60" y1="200" x2="400" y2="200" stroke="#38bdf8" stroke-width="3" />
            <!-- Mirror Back Shading -->
            <g stroke="#64748b" stroke-width="1.5">
              ${(() => {
                let s = '';
                for (let x = 65; x <= 395; x += 15) {
                  s += `<line x1="${x}" y1="200" x2="${x - 10}" y2="215" />`;
                }
                return s;
              })()}
            </g>

            <!-- Normal (Perpendicular Line at 90 deg) -->
            <line x1="230" y1="50" x2="230" y2="200" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="5 3" />
            <text x="235" y="65" fill="#cbd5e1" font-size="9" font-weight="bold">Normal (90°)</text>

            <!-- Incident Ray (Red/Yellow Laser) -->
            <line x1="${inX}" y1="${inY}" x2="230" y2="200" stroke="#ef4444" stroke-width="3" />
            <circle cx="${inX}" cy="${inY}" r="4" fill="#ef4444" />
            <text x="${inX - 10}" y="${inY - 5}" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="end">Incident Ray</text>

            <!-- Reflected Ray (Emerald Green Laser) -->
            <line x1="230" y1="200" x2="${refX}" y2="${refY}" stroke="#10b981" stroke-width="3" />
            <circle cx="${refX}" cy="${refY}" r="4" fill="#10b981" />
            <text x="${refX + 10}" y="${refY - 5}" fill="#6ee7b7" font-size="9" font-weight="bold">Reflected Ray</text>

            <!-- Angle Arcs -->
            <path d="M 230 150 A 50 50 0 0 0 ${230 - 50 * Math.sin(rad)} ${200 - 50 * Math.cos(rad)}" fill="none" stroke="#f43f5e" stroke-width="2" />
            <text x="${220 - 25 * Math.sin(rad/2)}" y="${175 - 25 * Math.cos(rad/2)}" fill="#f43f5e" font-size="10" font-weight="bold">i = ${angleI}°</text>

            <path d="M 230 150 A 50 50 0 0 1 ${230 + 50 * Math.sin(rad)} ${200 - 50 * Math.cos(rad)}" fill="none" stroke="#10b981" stroke-width="2" />
            <text x="${240 + 25 * Math.sin(rad/2)}" y="${175 - 25 * Math.cos(rad/2)}" fill="#10b981" font-size="10" font-weight="bold">r = ${angleI}°</text>

            <!-- Result Card -->
            <rect x="120" y="235" width="220" height="60" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5" />
            <text x="230" y="255" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">First Law: ∠i = ∠r</text>
            <text x="230" y="272" fill="#34d399" font-size="13" font-weight="900" text-anchor="middle">∠i (${angleI}°) = ∠r (${angleI}°)</text>
            <text x="230" y="287" fill="#cbd5e1" font-size="8" text-anchor="middle">Second Law: Incident, Normal, & Reflected rays are coplanar.</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>📐</span> Angle of Incidence (∠i):</span>
          <input type="range" class="sim-slider" id="angleSlider" min="5" max="75" value="${angleI}">
          <span class="control-value" id="angleValText">${angleI}°</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnAng30">30° Incident Angle</button>
          <button class="btn-sim" id="btnAng45">45° Incident Angle</button>
          <button class="btn-sim" id="btnAng60">60° Incident Angle</button>
        </div>
      `;

      const slider = document.getElementById('angleSlider');
      slider.oninput = (e) => {
        angleI = parseInt(e.target.value);
        document.getElementById('angleValText').textContent = `${angleI}°`;
        updateSim();
      };

      document.getElementById('btnAng30').onclick = () => { angleI = 30; slider.value = 30; document.getElementById('angleValText').textContent = '30°'; updateSim(); };
      document.getElementById('btnAng45').onclick = () => { angleI = 45; slider.value = 45; document.getElementById('angleValText').textContent = '45°'; updateSim(); };
      document.getElementById('btnAng60').onclick = () => { angleI = 60; slider.value = 60; document.getElementById('angleValText').textContent = '60°'; updateSim(); };

      updateSim();
    }

    // 8. Parallel Beams on Plane, Concave, and Convex Mirrors
    function simParallelBeamsMirrors(canvas, controls, title, icon) {
      title.textContent = 'Behavior of Parallel Light Beams Across Mirror Geometries';
      icon.textContent = '⚡';
      let mirrorType = 'concave'; // 'plane', 'concave', 'convex'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Incoming Parallel Laser Rake (Yellow) from Left -->
            <g stroke="#fef08a" stroke-width="2">
              <line x1="40" y1="80" x2="280" y2="80" />
              <line x1="40" y1="120" x2="295" y2="120" />
              <line x1="40" y1="160" x2="300" y2="160" />
              <line x1="40" y1="200" x2="295" y2="200" />
              <line x1="40" y1="240" x2="280" y2="240" />
            </g>

            ${mirrorType === 'plane' ? `
              <!-- Flat Plane Mirror -->
              <line x1="300" y1="60" x2="300" y2="260" stroke="#38bdf8" stroke-width="4" />
              <!-- Reflected Beams Remain PARALLEL! -->
              <g stroke="#38bdf8" stroke-width="2" stroke-dasharray="6 3">
                <line x1="300" y1="80" x2="40" y2="80" />
                <line x1="300" y1="120" x2="40" y2="120" />
                <line x1="300" y1="160" x2="40" y2="160" />
                <line x1="300" y1="200" x2="40" y2="200" />
                <line x1="300" y1="240" x2="40" y2="240" />
              </g>
              <text x="230" y="40" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Plane Mirror: Reflected Rays Remain Parallel</text>
            ` : mirrorType === 'concave' ? `
              <!-- Concave Mirror (Curves Inward) -->
              <path d="M 280 60 A 150 150 0 0 1 280 260" fill="none" stroke="#38bdf8" stroke-width="4" />
              <!-- Converging Reflected Rays Meeting at Focus (180, 160) -->
              <g stroke="#10b981" stroke-width="2.5">
                <line x1="280" y1="80" x2="180" y2="160" />
                <line x1="295" y1="120" x2="180" y2="160" />
                <line x1="300" y1="160" x2="180" y2="160" />
                <line x1="295" y1="200" x2="180" y2="160" />
                <line x1="280" y1="240" x2="180" y2="160" />
              </g>
              <!-- Bright Converged Focus Spot -->
              <circle cx="180" cy="160" r="6" fill="#fde047">
                <animate attributeName="r" values="6;8;6" dur="0.8s" repeatCount="indefinite" />
              </circle>
              <text x="180" y="145" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Focus (F)</text>
              <text x="230" y="40" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Concave Mirror: CONVERGES Rays to Focus</text>
            ` : `
              <!-- Convex Mirror (Curves Outward) -->
              <path d="M 300 60 A 150 150 0 0 0 300 260" fill="none" stroke="#38bdf8" stroke-width="4" />
              <!-- Diverging Reflected Rays Spreading Outwards! -->
              <g stroke="#f43f5e" stroke-width="2.5">
                <line x1="285" y1="80" x2="100" y2="20" />
                <line x1="295" y1="120" x2="100" y2="80" />
                <line x1="300" y1="160" x2="100" y2="160" />
                <line x1="295" y1="200" x2="100" y2="240" />
                <line x1="285" y1="240" x2="100" y2="300" />
              </g>
              <text x="230" y="40" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">Convex Mirror: DIVERGES Rays Outward</text>
            `}

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${mirrorType === 'plane' ? 'Plane: No convergence or divergence.' : mirrorType === 'concave' ? 'Concave is a CONVERGING mirror (powers solar cookers and torches).' : 'Convex is a DIVERGING mirror (spreads light for wide-angle view).'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
          <button class="btn-sim ${mirrorType === 'plane' ? 'active' : ''}" id="btnBeamPlane">🪞 Plane Mirror (Parallel)</button>
          <button class="btn-sim ${mirrorType === 'concave' ? 'active' : ''}" id="btnBeamConcave">🥣 Concave Mirror (Converges)</button>
          <button class="btn-sim ${mirrorType === 'convex' ? 'active' : ''}" id="btnBeamConvex">🌐 Convex Mirror (Diverges)</button>
        </div>
      `;

      document.getElementById('btnBeamPlane').onclick = () => { mirrorType = 'plane'; updateSim(); };
      document.getElementById('btnBeamConcave').onclick = () => { mirrorType = 'concave'; updateSim(); };
      document.getElementById('btnBeamConvex').onclick = () => { mirrorType = 'convex'; updateSim(); };

      updateSim();
    }

    // 9. Solar Concentrators & High-Temperature Furnaces
    function simSolarConcentrator(canvas, controls, title, icon) {
      title.textContent = 'Renewable Solar Thermal Concentration & Furnaces';
      icon.textContent = '☀️';
      let mode = 'cooker'; // 'cooker' or 'furnace'

      function updateSim() {
        const tempVal = mode === 'cooker' ? '180°C' : '3,200°C';

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Concentrating Curved Parabolic Dish -->
            <path d="M 80 50 Q 230 180 380 50" fill="none" stroke="#38bdf8" stroke-width="5" />
            
            <!-- Sunlight Rays Converging to Central Focal Pot -->
            <g stroke="#fde047" stroke-width="2" opacity="0.8">
              <line x1="100" y1="20" x2="100" y2="70" />
              <line x1="100" y1="70" x2="230" y2="120" />

              <line x1="170" y1="20" x2="170" y2="120" />
              <line x1="170" y1="120" x2="230" y2="120" />

              <line x1="290" y1="20" x2="290" y2="120" />
              <line x1="290" y1="120" x2="230" y2="120" />

              <line x1="360" y1="20" x2="360" y2="70" />
              <line x1="360" y1="70" x2="230" y2="120" />
            </g>

            <!-- Focal Cooking Pot or Melting Crucible -->
            <g transform="translate(230, 120)">
              <!-- Glowing Thermal Focal Spot -->
              <circle cx="0" cy="0" r="14" fill="#ef4444">
                <animate attributeName="r" values="14;16;14" dur="0.8s" repeatCount="indefinite" />
              </circle>
              <!-- Crucible Vessel -->
              <rect x="-15" y="-12" width="30" height="24" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
              <!-- Steam Clouds rising from boiling water or molten metal -->
              <ellipse cx="0" cy="-25" rx="10" ry="6" fill="rgba(255, 255, 255, 0.4)"><animate attributeName="cy" values="-25;-45;-25" dur="1.5s" repeatCount="indefinite"/></ellipse>
              <ellipse cx="6" cy="-35" rx="12" ry="7" fill="rgba(255, 255, 255, 0.4)"><animate attributeName="cy" values="-35;-55;-35" dur="1.8s" repeatCount="indefinite"/></ellipse>
            </g>

            <!-- Temperature Meter Card -->
            <rect x="50" y="195" width="130" height="65" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#ef4444" stroke-width="1.5" />
            <text x="115" y="215" fill="#fca5a5" font-size="8.5" font-weight="bold" text-anchor="middle">Focal Temperature</text>
            <text x="115" y="238" fill="#f87171" font-size="16" font-weight="900" text-anchor="middle">${tempVal}</text>
            <text x="115" y="252" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Zero Fuel Pollution!</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${mode === 'cooker' ? 'Solar Cooker: Concentrated sunlight boils water and cooks food sustainably.' : 'Solar Furnace: Concentrated solar radiation melts high-grade steel without carbon emissions.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mode === 'cooker' ? 'active' : ''}" id="btnSolCooker">🍲 Solar Cooker (180°C Steam)</button>
          <button class="btn-sim ${mode === 'furnace' ? 'active' : ''}" id="btnSolFurnace">🏭 Industrial Solar Furnace (3,200°C Steel Melting)</button>
        </div>
      `;

      document.getElementById('btnSolCooker').onclick = () => { mode = 'cooker'; updateSim(); };
      document.getElementById('btnSolFurnace').onclick = () => { mode = 'furnace'; updateSim(); };

      updateSim();
    }

    // 10. Lens Basics: Convex vs Concave Cross-Sections
    function simLensBasics(canvas, controls, title, icon) {
      title.textContent = 'Transparent Lenses: Convex (Converging) vs Concave (Diverging)';
      icon.textContent = '🔍';
      let lens = 'convex'; // 'convex' or 'concave'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            ${lens === 'convex' ? `
              <!-- Convex Lens Geometry: Thicker at Middle -->
              <path d="M 230 50 Q 280 160 230 270 Q 180 160 230 50 Z" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="3" />
              <!-- Middle Thickness Dimension -->
              <line x1="205" y1="160" x2="255" y2="160" stroke="#fbbf24" stroke-width="2" />
              <text x="230" y="150" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">THICK</text>
              <!-- Edge Thinness Dimension -->
              <text x="230" y="42" fill="#38bdf8" font-size="8.5" text-anchor="middle">Thin Rim</text>
              <text x="230" y="285" fill="#38bdf8" font-size="8.5" text-anchor="middle">Thin Rim</text>

              <rect x="50" y="75" width="130" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5" />
              <text x="115" y="95" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Convex Lens</text>
              <text x="115" y="112" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Thicker at Center</text>
              <text x="115" y="128" fill="#34d399" font-size="8.5" font-weight="bold" text-anchor="middle">CONVERGING</text>
            ` : `
              <!-- Concave Lens Geometry: Thicker at Edges -->
              <path d="M 210 50 L 250 50 Q 235 160 250 270 L 210 270 Q 225 160 210 50 Z" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="3" />
              <!-- Edge Thickness Dimension -->
              <line x1="210" y1="50" x2="250" y2="50" stroke="#fbbf24" stroke-width="2" />
              <text x="230" y="42" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="middle">THICK RIM</text>
              <!-- Middle Thinness -->
              <text x="230" y="165" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">THIN</text>

              <rect x="50" y="75" width="130" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5" />
              <text x="115" y="95" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Concave Lens</text>
              <text x="115" y="112" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Thicker at Edges</text>
              <text x="115" y="128" fill="#fb7185" font-size="8.5" font-weight="bold" text-anchor="middle">DIVERGING</text>
            `}

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              ${lens === 'convex' ? 'Convex lenses converge light rays inward toward the thicker optical center.' : 'Concave lenses diverge light rays outward toward the thicker perimeter rims.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${lens === 'convex' ? 'active' : ''}" id="btnLensConvex">🔍 Convex Lens (Thick Center • Converging)</button>
          <button class="btn-sim ${lens === 'concave' ? 'active' : ''}" id="btnLensConcave">👓 Concave Lens (Thick Edges • Diverging)</button>
        </div>
      `;

      document.getElementById('btnLensConvex').onclick = () => { lens = 'convex'; updateSim(); };
      document.getElementById('btnLensConcave').onclick = () => { lens = 'concave'; updateSim(); };

      updateSim();
    }

    // 11. Convex Lens Converging Optics: Real Focus
    function simConvexLensConverging(canvas, controls, title, icon) {
      title.textContent = 'Convex Lens: Refraction & Convergence to Real Focus';
      icon.textContent = '🔥';

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Principal Axis -->
            <line x1="30" y1="160" x2="430" y2="160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 2" />

            <!-- Transparent Convex Lens in Center -->
            <path d="M 210 60 Q 250 160 210 260 Q 170 160 210 60 Z" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2.5" />
            <circle cx="210" cy="160" r="3" fill="#ffffff" />
            <text x="210" y="175" fill="#cbd5e1" font-size="8" text-anchor="middle">O</text>

            <!-- Incoming Parallel Rays from Sun (Left) -->
            <g stroke="#fde047" stroke-width="2">
              <line x1="40" y1="90" x2="200" y2="90" />
              <line x1="40" y1="125" x2="208" y2="125" />
              <line x1="40" y1="160" x2="210" y2="160" />
              <line x1="40" y1="195" x2="208" y2="195" />
              <line x1="40" y1="230" x2="200" y2="230" />
            </g>

            <!-- Refracted Converging Rays Intersecting at Focus F (340, 160) -->
            <g stroke="#10b981" stroke-width="2.5">
              <line x1="200" y1="90" x2="340" y2="160" />
              <line x1="208" y1="125" x2="340" y2="160" />
              <line x1="210" y1="160" x2="420" y2="160" />
              <line x1="208" y1="195" x2="340" y2="160" />
              <line x1="200" y1="230" x2="340" y2="160" />
            </g>

            <!-- Real Focal Spot F -->
            <circle cx="340" cy="160" r="6" fill="#f59e0b">
              <animate attributeName="r" values="6;8;6" dur="0.8s" repeatCount="indefinite" />
            </circle>
            <text x="340" y="180" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Principal Focus (F)</text>

            <!-- Focal Length Indicator Bracket -->
            <line x1="210" y1="240" x2="340" y2="240" stroke="#f59e0b" stroke-width="1.5" />
            <text x="275" y="255" fill="#fbbf24" font-size="9" text-anchor="middle">Focal Length (f)</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Convex lens bends parallel rays inward, concentrating radiant solar energy onto a burning focal spot!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
          Incoming sunlight rays refract toward the thicker glass center, meeting at the real principal focus (F).
        </div>
      `;

      updateSim();
    }

    // 12. Concave Lens Diverging Optics: Virtual Focus
    function simConcaveLensDiverging(canvas, controls, title, icon) {
      title.textContent = 'Concave Lens: Refraction & Divergence to Virtual Focus';
      icon.textContent = '👓';

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Principal Axis -->
            <line x1="30" y1="160" x2="430" y2="160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 2" />

            <!-- Transparent Concave Lens in Center -->
            <path d="M 215 60 L 245 60 Q 235 160 245 260 L 215 260 Q 225 160 215 60 Z" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2.5" />
            <circle cx="230" cy="160" r="3" fill="#ffffff" />
            <text x="230" y="175" fill="#cbd5e1" font-size="8" text-anchor="middle">O</text>

            <!-- Incoming Parallel Light Rays (Left) -->
            <g stroke="#fde047" stroke-width="2">
              <line x1="40" y1="90" x2="218" y2="90" />
              <line x1="40" y1="125" x2="225" y2="125" />
              <line x1="40" y1="160" x2="230" y2="160" />
              <line x1="40" y1="195" x2="225" y2="195" />
              <line x1="40" y1="230" x2="218" y2="230" />
            </g>

            <!-- Diverging Rays Exiting on Right -->
            <g stroke="#f43f5e" stroke-width="2.5">
              <line x1="242" y1="90" x2="420" y2="35" />
              <line x1="235" y1="125" x2="420" y2="100" />
              <line x1="230" y1="160" x2="420" y2="160" />
              <line x1="235" y1="195" x2="420" y2="220" />
              <line x1="242" y1="230" x2="420" y2="285" />
            </g>

            <!-- Virtual Dotted Extensions Traced Backward to Virtual Focus F (120, 160) -->
            <g stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 2">
              <line x1="242" y1="90" x2="120" y2="160" />
              <line x1="235" y1="125" x2="120" y2="160" />
              <line x1="235" y1="195" x2="120" y2="160" />
              <line x1="242" y1="230" x2="120" y2="160" />
            </g>

            <!-- Virtual Focus F -->
            <circle cx="120" cy="160" r="5" fill="#f59e0b" />
            <text x="120" y="180" fill="#fbbf24" font-size="9.5" font-weight="bold" text-anchor="middle">Virtual Focus (F)</text>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Concave lens bends rays outward; backward extensions meet at an imaginary virtual focus point.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
          Refracted rays diverge and never physically meet; tracing them backward reveals the virtual focus (F).
        </div>
      `;

      updateSim();
    }

    // 13. Convex Lens Image Dynamics: Magnifying Glass vs Projection
    function simConvexLensImaging(canvas, controls, title, icon) {
      title.textContent = 'Convex Lens Imaging: Close Magnification vs Far Projection';
      icon.textContent = '🖼️';
      let objDist = 8; // cm (4 to 35 cm, Focus at 15 cm)

      function updateSim() {
        const isClose = objDist < 15;
        let imgHeight = 40;
        let isErect = true;
        let status = '';

        if (isClose) {
          isErect = true;
          imgHeight = Math.round(50 + (15 - objDist) * 4);
          status = 'Close Object (Magnifying Glass): Erect & Enlarged Virtual View';
        } else {
          isErect = false;
          imgHeight = Math.max(18, Math.round(80 - (objDist - 15) * 2.8));
          status = 'Distant Object: Inverted & Diminished Real Image Projected on Screen';
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Optical Axis -->
            <line x1="30" y1="180" x2="430" y2="180" stroke="#64748b" stroke-width="1.5" />

            <!-- Convex Lens at x = 200 -->
            <path d="M 200 70 Q 225 180 200 290 Q 175 180 200 70 Z" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2.5" />
            <circle cx="200" cy="180" r="3" fill="#fff" />

            <!-- Focus Marks (x = 100 on left, x = 300 on right) -->
            <circle cx="100" cy="180" r="3" fill="#f59e0b" />
            <text x="100" y="195" fill="#fbbf24" font-size="8" text-anchor="middle">F₁</text>
            <circle cx="300" cy="180" r="3" fill="#f59e0b" />
            <text x="300" y="195" fill="#fbbf24" font-size="8" text-anchor="middle">F₂</text>

            <!-- Real Candle Object on Left Axis -->
            <g transform="translate(${200 - objDist * 6.5}, 180)">
              <rect x="-5" y="-35" width="10" height="35" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
              <path d="M 0 -35 Q -4 -45 0 -55 Q 4 -45 0 -35 Z" fill="#f59e0b" />
              <text x="0" y="15" fill="#cbd5e1" font-size="8" text-anchor="middle">Object</text>
            </g>

            <!-- Reflected/Refracted Image -->
            ${isErect ? `
              <!-- Virtual Magnified Erect Image on Same Side as Object -->
              <g transform="translate(60, 180)" opacity="0.8">
                <rect x="-${imgHeight*0.1}" y="-${imgHeight*0.7}" width="${imgHeight*0.2}" height="${imgHeight*0.7}" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-dasharray="3 2" />
                <path d="M 0 -${imgHeight*0.7} Q -${imgHeight*0.1} -${imgHeight*0.85} 0 -${imgHeight} Q ${imgHeight*0.1} -${imgHeight*0.85} 0 -${imgHeight*0.7} Z" fill="#38bdf8" />
                <text x="0" y="20" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Magnified Text View</text>
              </g>
            ` : `
              <!-- Real Inverted Image on Opposite Side (Can be captured on screen!) -->
              <g transform="translate(${Math.min(410, 300 + (objDist - 15) * 4)}, 180)">
                <!-- White Paper Screen Behind Lens -->
                <rect x="5" y="-60" width="6" height="120" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
                <text x="8" y="-65" fill="#ffffff" font-size="8" text-anchor="middle">Screen</text>

                <!-- Inverted Candle Image -->
                <rect x="-${imgHeight*0.1}" y="0" width="${imgHeight*0.2}" height="${imgHeight*0.7}" fill="#f59e0b" opacity="0.7" stroke="#fbbf24" stroke-width="1" />
                <path d="M 0 ${imgHeight*0.7} Q -${imgHeight*0.1} ${imgHeight*0.85} 0 ${imgHeight} Q ${imgHeight*0.1} ${imgHeight*0.85} 0 ${imgHeight*0.7} Z" fill="#ef4444" />
                <text x="0" y="-10" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Real Inverted</text>
              </g>
            `}

            <!-- Top Indicator Bar -->
            <rect x="30" y="15" width="400" height="38" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="${isErect ? '#10b981' : '#f59e0b'}" stroke-width="1.5" />
            <text x="230" y="32" fill="${isErect ? '#34d399' : '#fbbf24'}" font-size="10" font-weight="bold" text-anchor="middle">${status}</text>
            <text x="230" y="46" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Object Distance: ${objDist} cm (Focal Length = 15 cm)</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label"><span>📏</span> Object Distance from Convex Lens:</span>
          <input type="range" class="sim-slider" id="cvLensSlider" min="5" max="30" value="${objDist}">
          <span class="control-value" id="cvLensValText">${objDist} cm</span>
        </div>
        <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.4rem;">
          <button class="btn-sim" id="btnCvMag">🔍 Hand Magnifying Glass (8 cm)</button>
          <button class="btn-sim" id="btnCvProj">🖼️ Project Inverted Image on Paper Screen (24 cm)</button>
        </div>
      `;

      const slider = document.getElementById('cvLensSlider');
      slider.oninput = (e) => {
        objDist = parseInt(e.target.value);
        document.getElementById('cvLensValText').textContent = `${objDist} cm`;
        updateSim();
      };

      document.getElementById('btnCvMag').onclick = () => { objDist = 8; slider.value = 8; document.getElementById('cvLensValText').textContent = '8 cm'; updateSim(); };
      document.getElementById('btnCvProj').onclick = () => { objDist = 24; slider.value = 24; document.getElementById('cvLensValText').textContent = '24 cm'; updateSim(); };

      updateSim();
    }

    // 14. Concave Lens Image Dynamics: Door Security Peephole
    function simConcaveLensImaging(canvas, controls, title, icon) {
      title.textContent = 'Concave Lens Optics: Door Security Peephole';
      icon.textContent = '🚪';

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Front Wooden Door -->
            <rect x="180" y="30" width="100" height="235" fill="#78350f" stroke="#a16207" stroke-width="2" />
            <circle cx="270" cy="150" r="4" fill="#fbbf24" />

            <!-- Brass Door Peephole Barrel -->
            <circle cx="230" cy="130" r="28" fill="#ca8a04" stroke="#eab308" stroke-width="3" />
            <!-- Concave Lens Glass Inside Peephole -->
            <circle cx="230" cy="130" r="22" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="1.5" />

            <!-- Miniature Erect View of Visitor Outside Door -->
            <g transform="translate(230, 130)">
              <!-- Visitor Miniature Figure (Diminished, Erect) -->
              <circle cx="0" cy="-8" r="4" fill="#fde047" />
              <rect x="-4" y="-3" width="8" height="15" rx="2" fill="#ef4444" />
              <line x1="-3" y1="12" x2="-3" y2="20" stroke="#1e293b" stroke-width="2" />
              <line x1="3" y1="12" x2="3" y2="20" stroke="#1e293b" stroke-width="2" />
              <text x="0" y="-14" fill="#34d399" font-size="7" font-weight="bold" text-anchor="middle">Erect & Small</text>
            </g>

            <!-- Actual Tall Visitor Outside Door (Left) -->
            <g transform="translate(90, 80)">
              <circle cx="0" cy="20" r="14" fill="#fde047" />
              <rect x="-12" y="35" width="24" height="60" rx="4" fill="#ef4444" />
              <line x1="-8" y1="95" x2="-8" y2="150" stroke="#1e293b" stroke-width="4" />
              <line x1="8" y1="95" x2="8" y2="150" stroke="#1e293b" stroke-width="4" />
              <text x="0" y="170" fill="#cbd5e1" font-size="9" text-anchor="middle">Actual Visitor (6 ft)</text>
            </g>

            <rect x="30" y="275" width="400" height="28" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1" />
            <text x="230" y="293" fill="#cbd5e1" font-size="9" text-anchor="middle">
              Concave lens always forms an erect, diminished virtual image, revealing the entire visitor safely!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
          The diverging concave lens captures a wide angle outside the door, forming a tiny, upright image inside the peephole.
        </div>
      `;

      updateSim();
    }

    // 15. Optical Instruments: The Human Eye & Microscope
    function simEyeOpticalInstruments(canvas, controls, title, icon) {
      title.textContent = 'Optical Biology: Flexible Eye Lens & Compound Microscope';
      icon.textContent = '👁️';
      let view = 'eye'; // 'eye' or 'microscope'

      function updateSim() {
        if (view === 'eye') {
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Eyeball Contour -->
              <ellipse cx="230" cy="150" rx="100" ry="85" fill="rgba(30, 41, 59, 0.7)" stroke="#38bdf8" stroke-width="2.5" />
              
              <!-- Cornea Front Bulge -->
              <path d="M 140 100 Q 110 150 140 200" fill="none" stroke="#38bdf8" stroke-width="3" />
              <text x="110" y="95" fill="#38bdf8" font-size="9" font-weight="bold">Cornea</text>

              <!-- Flexible Crystalline Convex Lens -->
              <ellipse cx="165" cy="150" rx="12" ry="35" fill="rgba(253, 224, 71, 0.5)" stroke="#facc15" stroke-width="2" />
              <text x="165" y="105" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Eye Lens (Convex)</text>

              <!-- Retina Layer at Back of Eyeball -->
              <path d="M 310 90 A 85 85 0 0 1 310 210" fill="none" stroke="#ef4444" stroke-width="5" />
              <text x="340" y="150" fill="#f87171" font-size="9.5" font-weight="bold">Retina</text>

              <!-- Real Inverted Image on Retina -->
              <g transform="translate(315, 150)">
                <line x1="0" y1="0" x2="0" y2="20" stroke="#f59e0b" stroke-width="2.5" />
                <polygon points="-4,20 4,20 0,26" fill="#f59e0b" />
                <text x="10" y="24" fill="#cbd5e1" font-size="7">Inverted Image</text>
              </g>

              <rect x="50" y="25" width="360" height="42" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5" />
              <text x="230" y="44" fill="#fbbf24" font-size="10.5" font-weight="bold" text-anchor="middle">Natural Human Eye Optics</text>
              <text x="230" y="58" fill="#cbd5e1" font-size="8.5" text-anchor="middle">The flexible convex lens forms a real, inverted image on the retina; the brain perceives it upright!</text>
            </svg>
          `;
        } else {
          // Compound Microscope
          canvas.innerHTML = `
            <svg viewBox="0 0 460 320" width="100%" height="320">
              <!-- Microscope Tube -->
              <rect x="200" y="50" width="60" height="180" fill="rgba(30, 41, 59, 0.8)" stroke="#64748b" stroke-width="2" />
              
              <!-- Eyepiece Convex Lens (Top) -->
              <ellipse cx="230" cy="65" rx="25" ry="8" fill="rgba(56, 189, 248, 0.5)" stroke="#38bdf8" stroke-width="2" />
              <text x="280" y="70" fill="#38bdf8" font-size="9" font-weight="bold">Eyepiece Lens</text>

              <!-- Objective Convex Lens (Bottom) -->
              <ellipse cx="230" cy="215" rx="18" ry="6" fill="rgba(56, 189, 248, 0.5)" stroke="#38bdf8" stroke-width="2" />
              <text x="280" y="220" fill="#38bdf8" font-size="9" font-weight="bold">Objective Lens</text>

              <!-- Specimen Slide on Stage Below -->
              <line x1="160" y1="245" x2="300" y2="245" stroke="#94a3b8" stroke-width="4" />
              <circle cx="230" cy="245" r="3" fill="#10b981" />
              <text x="230" y="260" fill="#34d399" font-size="8.5" font-weight="bold" text-anchor="middle">Biological Cell Specimen</text>

              <rect x="50" y="15" width="360" height="30" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#10b981" stroke-width="1" />
              <text x="230" y="34" fill="#34d399" font-size="9.5" font-weight="bold" text-anchor="middle">Two Convex Lenses Combine to Produce Massive Magnification!</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${view === 'eye' ? 'active' : ''}" id="btnViewEye">👁️ Human Eye (Natural Flexible Convex Lens)</button>
          <button class="btn-sim ${view === 'microscope' ? 'active' : ''}" id="btnViewMicro">🔬 Laboratory Compound Microscope</button>
        </div>
      `;

      document.getElementById('btnViewEye').onclick = () => { view = 'eye'; updateSim(); };
      document.getElementById('btnViewMicro').onclick = () => { view = 'microscope'; updateSim(); };

      updateSim();
    }

    // 16. Bhāskara II & Ancient Indian Observational Astronomy
    function simBhaskaraWaterOptics(canvas, controls, title, icon) {
      title.textContent = 'Indian Scientific Heritage: Bhāskara II Celestial Water Optics';
      icon.textContent = '🌌';

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 460 320" width="100%" height="320">
            <!-- Midnight Starry Sky Background -->
            <rect x="25" y="20" width="410" height="245" rx="10" fill="#040914" />
            
            <!-- Twinkling Stars -->
            <g fill="#ffffff">
              <circle cx="80" cy="50" r="1.5" /><circle cx="140" cy="35" r="2" />
              <circle cx="210" cy="65" r="1.5" /><circle cx="310" cy="40" r="2.5" />
              <circle cx="380" cy="70" r="1.5" /><circle cx="270" cy="85" r="1.5" />
            </g>

            <!-- Bright Star Sirius / Planet Venus in Nocturnal Sky -->
            <circle cx="340" cy="55" r="5" fill="#fde047">
              <animate attributeName="r" values="5;7;5" dur="1.2s" repeatCount="indefinite" />
            </circle>
            <text x="340" y="42" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Planet / Target Star</text>

            <!-- Shallow Dark Bronze Basin with Calm Water -->
            <ellipse cx="230" cy="210" rx="90" ry="25" fill="#78350f" stroke="#d97706" stroke-width="2" />
            <!-- Calm Water Liquid Mirror -->
            <ellipse cx="230" cy="207" rx="80" ry="20" fill="rgba(14, 165, 233, 0.45)" />
            <text x="230" y="212" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Calm Water Basin (Optically Flat Mirror)</text>

            <!-- Starlight Ray Reflecting into Water Basin -->
            <line x1="340" y1="55" x2="230" y2="207" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2" />

            <!-- Reflected Ray Sighted Through Sighting Tube (Nālikā Yantra) -->
            <line x1="230" y1="207" x2="120" y2="120" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2" />

            <!-- Indian Astronomer's Calibrated Observation Tube (Nālikā) -->
            <line x1="150" y1="140" x2="105" y2="105" stroke="#ca8a04" stroke-width="6" stroke-linecap="round" />
            <circle cx="105" cy="105" r="6" fill="#fde047" />
            <text x="100" y="90" fill="#fde68a" font-size="8.5" font-weight="bold">Nālikā Sighting Tube</text>

            <!-- Heritage Info Card -->
            <rect x="40" y="272" width="380" height="35" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#f59e0b" stroke-width="1.5" />
            <text x="230" y="288" fill="#fbbf24" font-size="9.5" font-weight="bold" text-anchor="middle">Bhāskara II (1114–1185 CE) • Siddhānta Śiromaṇi</text>
            <text x="230" y="300" fill="#cbd5e1" font-size="8" text-anchor="middle">Over 800 years ago, still water provided a level plane mirror to calculate exact celestial coordinates.</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="text-align: center; color: #cbd5e1; font-size: 0.85rem;">
          Gravity levels still water into an optically perfect horizontal mirror, reflecting celestial bodies into sighting tubes.
        </div>
      `;

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-light-optics.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

