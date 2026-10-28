# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-electric-current.html
Class 8 Science - Chapter 4: Electric Current: Magnetic & Heating Effects, and Chemical Cells
Features:
- 20 animated slides with Web Speech API audio narration and teacher avatar
- 16 bespoke interactive SVG simulators with live controls, gauges, and animations
- Prominent Vocabulary Badges on every content slide
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
from class8_science_electric_current_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 4: Electric Current & Chemical Cells Master Lab</title>
  
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
      --bg-primary: #070d18;
      --bg-secondary: #0f172a;
      --card-bg: rgba(15, 23, 42, 0.88);
      --card-border: rgba(56, 189, 248, 0.25);
      --accent-sky: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-emerald: #10b981;
      --accent-purple: #a855f7;
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
        radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(245, 158, 11, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.05) 0%, transparent 60%);
    }

    /* Header & Navigation Bar */
    .lab-header {
      background: rgba(15, 23, 42, 0.92);
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
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: linear-gradient(135deg, #38bdf8, #f59e0b);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }

    .header-text h1 {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .header-text .sub-badge {
      font-size: 0.72rem;
      color: var(--accent-sky);
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .progress-section {
      flex: 1;
      max-width: 420px;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .progress-bar-container {
      width: 100%;
      height: 7px;
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
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .btn-nav {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #fff;
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      font-size: 0.85rem;
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
      transform: translateY(-1px);
    }

    .btn-nav:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .btn-nav.btn-primary {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border: 1px solid #38bdf8;
    }

    .btn-nav.btn-primary:hover:not(:disabled) {
      background: linear-gradient(135deg, #0369a1, #0284c7);
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }

    /* Teacher Avatar Bar */
    .avatar-bar {
      background: linear-gradient(90deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.9));
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding: 0.65rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .avatar-frame {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      border: 2px solid #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
      flex-shrink: 0;
      position: relative;
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 2px solid #38bdf8;
      opacity: 0;
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
      color: var(--accent-sky);
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
      font-size: 1.6rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.25;
      background: linear-gradient(135deg, #ffffff, #93c5fd);
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
      background: rgba(15, 23, 42, 0.8);
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
      background: rgba(15, 23, 42, 0.9);
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
      background: rgba(30, 41, 59, 0.6);
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
      background: rgba(15, 23, 42, 0.7);
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
      background: rgba(7, 13, 24, 0.9);
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
      background: rgba(30, 41, 59, 0.5);
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
      padding: 0.5rem 1rem;
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
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95));
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
      background: rgba(30, 41, 59, 0.6);
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
      background: #0f172a;
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
      <div class="lab-icon">⚡</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 4</div>
        <h1>Electric Current, Magnetism & Cells</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Oersted's Discovery</span>
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
      <span>👨‍🏫</span>
      <div class="avatar-speaking-pulse" id="avatarPulse"></div>
    </div>
    <div class="avatar-dialogue-box">
      <div class="avatar-name-row">
        <span class="avatar-name">Prof. Faraday • Virtual Mentor</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Loading classroom session...
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
          <span class="slide-tag" id="slideBadge">Magnetic Effect</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Oersted's Discovery</h2>

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
            <span id="simIcon">⚡</span>
            <span id="simTitle">Interactive Circuit Simulator</span>
          </div>
          <span class="sim-badge" id="simBadge">Live Physics Lab</span>
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

    // Render Vocabulary Box
    function renderVocabulary(vocabList) {
      const grid = document.getElementById('vocabGrid');
      grid.innerHTML = '';
      if (!vocabList || vocabList.length === 0) {
        document.getElementById('vocabBox').style.display = 'none';
        return;
      }
      document.getElementById('vocabBox').style.display = 'flex';
      vocabList.forEach(item => {
        const chip = document.createElement('div');
        chip.className = 'vocab-chip';
        chip.innerHTML = `<span class="vocab-word">⚡ ${item.word}:</span><span class="vocab-def">${item.definition}</span>`;
        grid.appendChild(chip);
      });
    }

    // Render In-Slide Checkpoints
    function renderCheckpoints(checkpoints) {
      const list = document.getElementById('checkpointsList');
      list.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) {
        document.getElementById('checkpointContainer').style.display = 'none';
        return;
      }
      document.getElementById('checkpointContainer').style.display = 'flex';

      checkpoints.forEach((cp, cpIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-item';

        const qTitle = document.createElement('div');
        qTitle.className = 'checkpoint-q';
        qTitle.innerHTML = `<strong>Q${cpIdx + 1}:</strong> ${cp.question}`;
        card.appendChild(qTitle);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'checkpoint-options';

        const fbDiv = document.createElement('div');
        fbDiv.className = 'cp-feedback';

        cp.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'cp-opt-btn';
          btn.innerHTML = optText;

          btn.onclick = () => {
            const allBtns = optsDiv.querySelectorAll('.cp-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {
              btn.classList.add('correct');
              fbDiv.className = 'cp-feedback show-correct';
              fbDiv.innerHTML = `<strong>✔ Correct!</strong> ${cp.explanation}`;
            } else {
              btn.classList.add('incorrect');
              allBtns[cp.correct].classList.add('correct');
              fbDiv.className = 'cp-feedback show-incorrect';
              fbDiv.innerHTML = `<strong>✖ Not quite.</strong> ${cp.explanation}`;
            }
          };

          optsDiv.appendChild(btn);
        });

        card.appendChild(optsDiv);
        card.appendChild(fbDiv);
        list.appendChild(card);
      });
    }

    // Render Quiz Challenge Slide
    function renderQuizSlide(questions) {
      const grid = document.getElementById('quizQuestionsGrid');
      grid.innerHTML = '';
      quizScores[currentSlideIndex] = quizScores[currentSlideIndex] || {};

      questions.forEach((q, idx) => {
        const card = document.createElement('div');
        card.className = 'quiz-card';

        const qNum = document.createElement('div');
        qNum.className = 'quiz-q-num';
        qNum.textContent = `Question ${q.id} of 40`;
        card.appendChild(qNum);

        const qText = document.createElement('div');
        qText.className = 'quiz-q-text';
        qText.innerHTML = q.question;
        card.appendChild(qText);

        const optsDiv = document.createElement('div');
        optsDiv.className = 'quiz-opts';

        const solBtn = document.createElement('button');
        solBtn.className = 'quiz-btn-solution';
        solBtn.innerHTML = '💡 View Step-by-Step Solution';
        solBtn.onclick = () => openSolutionModal(q);

        q.options.forEach((optText, optIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.innerHTML = optText;

          if (quizScores[currentSlideIndex][idx] !== undefined) {
            btn.disabled = true;
            if (optIdx === q.correct) btn.classList.add('correct');
            if (quizScores[currentSlideIndex][idx] === optIdx && optIdx !== q.correct) {
              btn.classList.add('incorrect');
            }
            solBtn.style.display = 'inline-flex';
          }

          btn.onclick = () => {
            const allBtns = optsDiv.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => b.disabled = true);
            quizScores[currentSlideIndex][idx] = optIdx;

            if (optIdx === q.correct) {
              btn.classList.add('correct');
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
            }
            solBtn.style.display = 'inline-flex';
            updateQuizScore();
          };

          optsDiv.appendChild(btn);
        });

        card.appendChild(optsDiv);
        card.appendChild(solBtn);
        grid.appendChild(card);
      });

      updateQuizScore();
    }

    function updateQuizScore() {
      const currentScores = quizScores[currentSlideIndex] || {};
      const slide = SLIDES[currentSlideIndex];
      if (!slide || !slide.questions) return;

      let correctCount = 0;
      slide.questions.forEach((q, idx) => {
        if (currentScores[idx] === q.correct) {
          correctCount++;
        }
      });
      document.getElementById('quizScoreNum').textContent = `${correctCount} / 10`;
    }

    // Modal Solution System
    function openSolutionModal(questionObj) {
      document.getElementById('modalQuestionTitle').textContent = `Question ${questionObj.id} • Step-by-Step Solution`;
      document.getElementById('modalSolutionBody').innerHTML = `
        <div style="font-weight: 700; color: #fff; margin-bottom: 0.5rem;">${questionObj.question}</div>
        <div style="color: #38bdf8; font-weight: 600; margin-bottom: 0.75rem;">Correct Answer: ${questionObj.options[questionObj.correct]}</div>
        <hr style="border: none; border-top: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 0.75rem;">
        ${questionObj.solution}
      `;
      document.getElementById('solutionModal').style.display = 'flex';
      triggerMathRender(document.getElementById('modalSolutionBody'));
    }

    function closeSolutionModal() {
      document.getElementById('solutionModal').style.display = 'none';
    }

    window.addEventListener('click', (e) => {
      const modal = document.getElementById('solutionModal');
      if (e.target === modal) {
        closeSolutionModal();
      }
    });

    // Web Speech API Integration
    function setupSpeech() {
      if (!('speechSynthesis' in window)) {
        document.querySelector('.audio-controls').style.display = 'none';
      }
    }

    function speakText(text) {
      if (!('speechSynthesis' in window)) return;
      synth.cancel();

      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.rate = 0.95;
      currentUtterance.pitch = 1.0;

      const voices = synth.getVoices();
      const engVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Google') || v.name.includes('Natural') || v.name.includes('Male')));
      if (engVoice) currentUtterance.voice = engVoice;

      const pulse = document.getElementById('avatarPulse');
      const pill = document.getElementById('speechStatusPill');

      currentUtterance.onstart = () => {
        isSpeaking = true;
        pulse.style.display = 'block';
        pill.style.display = 'inline-block';
        document.getElementById('btnAudioToggle').textContent = '⏸';
      };

      currentUtterance.onend = () => {
        isSpeaking = false;
        pulse.style.display = 'none';
        pill.style.display = 'none';
        document.getElementById('btnAudioToggle').textContent = '🔊';
      };

      synth.speak(currentUtterance);
    }

    function toggleSpeech() {
      if (!synth) return;
      if (synth.speaking && !synth.paused) {
        synth.pause();
        document.getElementById('btnAudioToggle').textContent = '▶';
        document.getElementById('avatarPulse').style.display = 'none';
      } else if (synth.paused) {
        synth.resume();
        document.getElementById('btnAudioToggle').textContent = '⏸';
        document.getElementById('avatarPulse').style.display = 'block';
      } else {
        const slide = SLIDES[currentSlideIndex];
        speakText(slide.avatar_dialogue);
      }
    }

    function replaySpeech() {
      const slide = SLIDES[currentSlideIndex];
      speakText(slide.avatar_dialogue);
    }
  </script>

  <!-- 16 BESPOKE INTERACTIVE SVG SIMULATORS -->
  <script>
    function renderSimulator(simId) {
      const canvas = document.getElementById('simCanvas');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const icon = document.getElementById('simIcon');

      canvas.innerHTML = '';
      controls.innerHTML = '';

      switch (simId) {
        case 'oersted_compass_sim':
          simOerstedCompass(canvas, controls, title, icon);
          break;
        case 'wire_field_lines_sim':
          simWireFieldLines(canvas, controls, title, icon);
          break;
        case 'electromagnet_anatomy_sim':
          simElectromagnetAnatomy(canvas, controls, title, icon);
          break;
        case 'electromagnet_strength_sim':
          simElectromagnetStrength(canvas, controls, title, icon);
          break;
        case 'scrap_crane_sim':
          simScrapCrane(canvas, controls, title, icon);
          break;
        case 'earth_magnetism_sim':
          simEarthMagnetism(canvas, controls, title, icon);
          break;
        case 'electron_collision_sim':
          simElectronCollision(canvas, controls, title, icon);
          break;
        case 'nichrome_copper_sim':
          simNichromeCopper(canvas, controls, title, icon);
          break;
        case 'joule_heating_sim':
          simJouleHeating(canvas, controls, title, icon);
          break;
        case 'appliance_fuse_sim':
          simApplianceFuse(canvas, controls, title, icon);
          break;
        case 'arc_furnace_safety_sim':
          simArcFurnaceSafety(canvas, controls, title, icon);
          break;
        case 'galvani_volta_sim':
          simGalvaniVolta(canvas, controls, title, icon);
          break;
        case 'lemon_cell_sim':
          simLemonCell(canvas, controls, title, icon);
          break;
        case 'dry_cell_cutaway_sim':
          simDryCellCutaway(canvas, controls, title, icon);
          break;
        case 'lithium_ion_sim':
          simLithiumIon(canvas, controls, title, icon);
          break;
        case 'solid_state_ewaste_sim':
          simSolidStateEwaste(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = `<div style="color: #94a3b8;">Simulator ready.</div>`;
      }
    }

    // 1. OERSTED COMPASS DEFLECTION SIMULATOR
    function simOerstedCompass(canvas, controls, title, icon) {
      title.textContent = "Oersted's Compass Deflection Lab";
      icon.textContent = "🧭";

      let isSwitchClosed = false;
      let currentDirection = 1; // 1 = South to North, -1 = North to South
      let currentAmps = 2.0;

      function updateSim() {
        const deflectionAngle = isSwitchClosed ? currentDirection * Math.min(65, currentAmps * 18) : 0;
        
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <defs>
              <linearGradient id="wireGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b45309" />
                <stop offset="50%" stop-color="#f59e0b" />
                <stop offset="100%" stop-color="#b45309" />
              </linearGradient>
              <filter id="glow">
                <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                <feMerge>
                  <feMergeNode in="coloredBlur"/>
                  <feMergeNode in="SourceGraphic"/>
                </feMerge>
              </filter>
            </defs>

            <!-- Tabletop Bench -->
            <rect x="30" y="220" width="440" height="70" rx="8" fill="#1e293b" stroke="#334155" stroke-width="2"/>
            <text x="50" y="250" fill="#64748b" font-size="12" font-family="monospace">Physics Lecture Bench (1820)</text>

            <!-- Geographic North Compass Background Dial -->
            <g transform="translate(250, 150)">
              <circle r="65" fill="#0f172a" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
              <circle r="60" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="3,3"/>
              <text x="0" y="-45" fill="#ef4444" font-weight="bold" font-size="12" text-anchor="middle">N</text>
              <text x="0" y="55" fill="#38bdf8" font-weight="bold" font-size="12" text-anchor="middle">S</text>
              <text x="48" y="4" fill="#94a3b8" font-size="10" text-anchor="middle">E</text>
              <text x="-48" y="4" fill="#94a3b8" font-size="10" text-anchor="middle">W</text>
              
              <!-- Compass Needle -->
              <g transform="rotate(${deflectionAngle})" style="transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);">
                <!-- North Pointer (Red) -->
                <polygon points="0,-52 8,0 0,-6" fill="#ef4444" />
                <!-- South Pointer (Blue) -->
                <polygon points="0,52 8,0 0,6" fill="#38bdf8" />
                <!-- Pivot Center -->
                <circle r="5" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
              </g>
            </g>

            <!-- Heavy Copper Conducting Wire Passing Directly Over Compass -->
            <path d="M 60 70 L 60 150 L 440 150 L 440 70" fill="none" stroke="url(#wireGrad)" stroke-width="6" stroke-linecap="round"/>
            <text x="250" y="130" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">
              Copper Wire (Directly Over Compass)
            </text>

            <!-- Circuit Top Elements: Battery & Switch -->
            <!-- Battery -->
            <g transform="translate(140, 50)">
              <rect x="0" y="0" width="60" height="36" rx="4" fill="#334155" stroke="#475569" stroke-width="2"/>
              <rect x="60" y="10" width="6" height="16" rx="2" fill="#94a3b8"/>
              <text x="30" y="23" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">
                ${currentDirection === 1 ? '+ BAT -' : '- BAT +'}
              </text>
            </g>

            <!-- Knife Switch -->
            <g transform="translate(310, 48)">
              <circle cx="10" cy="20" r="4" fill="#94a3b8"/>
              <circle cx="50" cy="20" r="4" fill="#94a3b8"/>
              <!-- Switch Blade -->
              <line x1="10" y1="20" x2="50" y2="${isSwitchClosed ? 20 : -5}" 
                    stroke="${isSwitchClosed ? '#10b981' : '#f43f5e'}" stroke-width="5" stroke-linecap="round"
                    style="transition: all 0.2s;" />
              <text x="30" y="38" fill="#cbd5e1" font-size="10" text-anchor="middle">
                Switch: ${isSwitchClosed ? 'CLOSED (ON)' : 'OPEN (OFF)'}
              </text>
            </g>

            <!-- Connecting Top Wires -->
            <line x1="60" y1="70" x2="140" y2="70" stroke="#f59e0b" stroke-width="3"/>
            <line x1="206" y1="70" x2="310" y2="70" stroke="#f59e0b" stroke-width="3"/>
            <line x1="360" y1="70" x2="440" y2="70" stroke="#f59e0b" stroke-width="3"/>

            <!-- Current Flow Indicator Particles -->
            ${isSwitchClosed ? `
              <g filter="url(#glow)">
                <circle cx="${currentDirection === 1 ? 180 : 320}" cy="150" r="4" fill="#38bdf8">
                  <animate attributeName="cx" from="${currentDirection === 1 ? 70 : 430}" to="${currentDirection === 1 ? 430 : 70}" dur="${2.5 / currentAmps}s" repeatCount="indefinite"/>
                </circle>
                <circle cx="${currentDirection === 1 ? 300 : 200}" cy="150" r="4" fill="#38bdf8">
                  <animate attributeName="cx" from="${currentDirection === 1 ? 70 : 430}" to="${currentDirection === 1 ? 430 : 70}" dur="${2.5 / currentAmps}s" repeatCount="indefinite"/>
                </circle>
              </g>
              <text x="250" y="175" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">
                Current Flow: ${currentDirection === 1 ? '➡ South to North' : '⬅ North to South'} (${currentAmps} A)
              </text>
            ` : `
              <text x="250" y="175" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">
                Circuit Open: No Current Flow • Needle Aligns to Earth's North
              </text>
            `}

            <!-- Deflection Gauge Callout -->
            <rect x="340" y="235" width="120" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="400" y="252" fill="#94a3b8" font-size="10" text-anchor="middle">Needle Deflection</text>
            <text x="400" y="270" fill="${isSwitchClosed ? '#38bdf8' : '#94a3b8'}" font-size="14" font-weight="bold" text-anchor="middle">
              ${isSwitchClosed ? (deflectionAngle > 0 ? `+${deflectionAngle.toFixed(1)}° (East)` : `${deflectionAngle.toFixed(1)}° (West)`) : '0.0° (Rest)'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button class="btn-sim ${isSwitchClosed ? 'active' : ''}" id="btnSwitch">
            ⚡ Switch Circuit: ${isSwitchClosed ? 'Turn OFF' : 'Turn ON'}
          </button>
          <button class="btn-sim" id="btnReverse">
            🔄 Reverse Battery Current
          </button>
        </div>
        <div class="control-row" style="margin-top: 0.5rem;">
          <span class="control-label">Current Intensity:</span>
          <input type="range" class="sim-slider" id="sliderAmps" min="0.5" max="4.0" step="0.5" value="${currentAmps}">
          <span class="control-value" id="valAmps">${currentAmps} A</span>
        </div>
      `;

      document.getElementById('btnSwitch').onclick = () => {
        isSwitchClosed = !isSwitchClosed;
        document.getElementById('btnSwitch').textContent = `⚡ Switch Circuit: ${isSwitchClosed ? 'Turn OFF' : 'Turn ON'}`;
        document.getElementById('btnSwitch').classList.toggle('active', isSwitchClosed);
        updateSim();
      };

      document.getElementById('btnReverse').onclick = () => {
        currentDirection *= -1;
        updateSim();
      };

      document.getElementById('sliderAmps').oninput = (e) => {
        currentAmps = parseFloat(e.target.value);
        document.getElementById('valAmps').textContent = `${currentAmps} A`;
        updateSim();
      };

      updateSim();
    }

    // 2. MAGNETIC FIELD LINES AROUND WIRE SIMULATOR
    function simWireFieldLines(canvas, controls, title, icon) {
      title.textContent = "Magnetic Field Lines & Right-Hand Rule";
      icon.textContent = "🌀";

      let directionUp = true;
      let currentAmps = 3.0;

      function updateSim() {
        const rotDir = directionUp ? 1 : -1;
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <defs>
              <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1e293b" />
                <stop offset="100%" stop-color="#0f172a" />
              </linearGradient>
            </defs>

            <!-- Cardboard Plane (Isometric tilt) -->
            <polygon points="120,70 420,70 380,250 80,250" fill="url(#cardGrad)" stroke="#38bdf8" stroke-width="1.5" opacity="0.9"/>
            <text x="140" y="95" fill="#64748b" font-size="11" font-weight="600">Cardboard Plane (Perpendicular)</text>

            <!-- Concentric Circular Magnetic Field Lines -->
            <g transform="translate(250, 160) scale(1, 0.45)">
              <!-- Ring 1 (Inner, Dense) -->
              <circle r="45" fill="none" stroke="#38bdf8" stroke-width="${currentAmps * 0.8}" stroke-dasharray="6,4"/>
              <!-- Ring 2 (Middle) -->
              <circle r="85" fill="none" stroke="#0ea5e9" stroke-width="${currentAmps * 0.6}" stroke-dasharray="8,5"/>
              <!-- Ring 3 (Outer, Fainter) -->
              <circle r="130" fill="none" stroke="#0284c7" stroke-width="${currentAmps * 0.4}" stroke-dasharray="10,6" opacity="0.7"/>

              <!-- Circulating Direction Arrows -->
              <g transform="rotate(${rotDir > 0 ? 30 : -30})">
                <polygon points="45,-6 53,0 45,6" fill="#38bdf8" />
                <polygon points="-45,6 -53,0 -45,-6" fill="#38bdf8" />
                <polygon points="85,-7 95,0 85,7" fill="#0ea5e9" />
                <polygon points="-85,7 -95,0 -85,-7" fill="#0ea5e9" />
                <polygon points="130,-8 142,0 130,8" fill="#0284c7" />
              </g>
            </g>

            <!-- Straight Copper Conductor Penetrating Board -->
            <!-- Lower half of wire (behind board) -->
            <line x1="250" y1="160" x2="250" y2="295" stroke="#f59e0b" stroke-width="7" stroke-linecap="round"/>
            <!-- Hole on cardboard -->
            <ellipse cx="250" cy="160" rx="8" ry="4" fill="#0284c7"/>
            <!-- Upper half of wire (above board) -->
            <line x1="250" y1="25" x2="250" y2="160" stroke="#f59e0b" stroke-width="7" stroke-linecap="round"/>

            <!-- Current Vector Arrow on Wire -->
            <g transform="translate(250, ${directionUp ? 80 : 100})">
              <polygon points="0,${directionUp ? -20 : 20} -8,${directionUp ? 0 : 0} 8,${directionUp ? 0 : 0}" fill="#ef4444" />
              <text x="25" y="5" fill="#ef4444" font-size="12" font-weight="bold">
                I (${directionUp ? 'UPWARD' : 'DOWNWARD'})
              </text>
            </g>

            <!-- Right-Hand Rule Visual Legend -->
            <rect x="20" y="20" width="180" height="45" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.15)"/>
            <text x="30" y="38" fill="#38bdf8" font-size="11" font-weight="bold">Right-Hand Thumb Rule:</text>
            <text x="30" y="54" fill="#cbd5e1" font-size="10">
              Field rotates: ${directionUp ? 'Counter-Clockwise' : 'Clockwise'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn-sim active" id="btnToggleDir">
            🔄 Reverse Current: ${directionUp ? 'Flow UP' : 'Flow DOWN'}
          </button>
        </div>
        <div class="control-row" style="margin-top: 0.5rem;">
          <span class="control-label">Current Intensity (I):</span>
          <input type="range" class="sim-slider" id="sliderAmps" min="1.0" max="5.0" step="0.5" value="${currentAmps}">
          <span class="control-value" id="valAmps">${currentAmps} A</span>
        </div>
      `;

      document.getElementById('btnToggleDir').onclick = () => {
        directionUp = !directionUp;
        document.getElementById('btnToggleDir').textContent = `🔄 Reverse Current: ${directionUp ? 'Flow UP' : 'Flow DOWN'}`;
        updateSim();
      };

      document.getElementById('sliderAmps').oninput = (e) => {
        currentAmps = parseFloat(e.target.value);
        document.getElementById('valAmps').textContent = `${currentAmps} A`;
        updateSim();
      };

      updateSim();
    }

    // 3. ELECTROMAGNET ANATOMY SIMULATOR
    function simElectromagnetAnatomy(canvas, controls, title, icon) {
      title.textContent = "Electromagnet Anatomy & Core Lab";
      icon.textContent = "🧲";

      let coreType = 'iron'; // iron, steel, air
      let isPowered = true;

      function updateSim() {
        let coreColor = '#94a3b8';
        let coreLabel = 'Soft Iron Core';
        let fieldLines = 6;
        let clipsLifted = 8;

        if (coreType === 'steel') {
          coreColor = '#64748b';
          coreLabel = 'Hard Steel Core';
          fieldLines = 4;
          clipsLifted = 5;
        } else if (coreType === 'air') {
          coreColor = 'transparent';
          coreLabel = 'Empty Air Core';
          fieldLines = 1;
          clipsLifted = 0;
        }

        if (!isPowered) {
          if (coreType === 'steel') {
            // Steel retains residual magnetism
            clipsLifted = 2;
            fieldLines = 2;
          } else {
            clipsLifted = 0;
            fieldLines = 0;
          }
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Magnetic Field Loops around Solenoid -->
            ${fieldLines > 0 ? `
              <g fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.75">
                <ellipse cx="250" cy="150" rx="190" ry="110"/>
                <ellipse cx="250" cy="150" rx="160" ry="85"/>
                <ellipse cx="250" cy="150" rx="130" ry="60"/>
              </g>
              <!-- Polarity Badges -->
              <circle cx="100" cy="150" r="22" fill="#ef4444" stroke="#f8fafc" stroke-width="2"/>
              <text x="100" y="157" fill="#fff" font-size="18" font-weight="bold" text-anchor="middle">N</text>
              <circle cx="400" cy="150" r="22" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
              <text x="400" y="157" fill="#fff" font-size="18" font-weight="bold" text-anchor="middle">S</text>
            ` : ''}

            <!-- Core Rod (Inside Coil) -->
            ${coreType !== 'air' ? `
              <rect x="110" y="125" width="280" height="50" rx="6" fill="${coreColor}" stroke="#475569" stroke-width="2"/>
              <text x="250" y="155" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">
                ${coreLabel}
              </text>
            ` : `
              <rect x="110" y="125" width="280" height="50" rx="6" fill="rgba(255,255,255,0.03)" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
              <text x="250" y="155" fill="#64748b" font-size="13" font-style="italic" text-anchor="middle">
                Empty Air Core (Hollow Coil)
              </text>
            `}

            <!-- Solenoid Copper Wire Turns Wrapped Around Core -->
            <g fill="none" stroke="#f59e0b" stroke-width="6" stroke-linecap="round">
              <path d="M 130 115 Q 145 150 130 185" />
              <path d="M 160 115 Q 175 150 160 185" />
              <path d="M 190 115 Q 205 150 190 185" />
              <path d="M 220 115 Q 235 150 220 185" />
              <path d="M 250 115 Q 265 150 250 185" />
              <path d="M 280 115 Q 295 150 280 185" />
              <path d="M 310 115 Q 325 150 310 185" />
              <path d="M 340 115 Q 355 150 340 185" />
              <path d="M 370 115 Q 385 150 370 185" />
            </g>

            <!-- Paperclip Tray -->
            <rect x="70" y="240" width="360" height="40" rx="6" fill="#1e293b" stroke="#334155"/>
            <text x="250" y="265" fill="#cbd5e1" font-size="12" text-anchor="middle">
              Steel Paperclips Attracted: <strong>${clipsLifted} clips</strong>
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button class="btn-sim ${isPowered ? 'active' : ''}" id="btnPower">
            ⚡ Power: ${isPowered ? 'Switch OFF' : 'Switch ON'}
          </button>
          <button class="btn-sim ${coreType === 'iron' ? 'active' : ''}" id="btnIron">Soft Iron Core</button>
          <button class="btn-sim ${coreType === 'steel' ? 'active' : ''}" id="btnSteel">Steel Core</button>
          <button class="btn-sim ${coreType === 'air' ? 'active' : ''}" id="btnAir">Air Core</button>
        </div>
      `;

      document.getElementById('btnPower').onclick = () => {
        isPowered = !isPowered;
        document.getElementById('btnPower').textContent = `⚡ Power: ${isPowered ? 'Switch OFF' : 'Switch ON'}`;
        document.getElementById('btnPower').classList.toggle('active', isPowered);
        updateSim();
      };

      document.getElementById('btnIron').onclick = () => { coreType = 'iron'; updateBtnStates(); updateSim(); };
      document.getElementById('btnSteel').onclick = () => { coreType = 'steel'; updateBtnStates(); updateSim(); };
      document.getElementById('btnAir').onclick = () => { coreType = 'air'; updateBtnStates(); updateSim(); };

      function updateBtnStates() {
        document.getElementById('btnIron').classList.toggle('active', coreType === 'iron');
        document.getElementById('btnSteel').classList.toggle('active', coreType === 'steel');
        document.getElementById('btnAir').classList.toggle('active', coreType === 'air');
      }

      updateSim();
    }

    // 4. ELECTROMAGNET STRENGTH TUNER SIMULATOR
    function simElectromagnetStrength(canvas, controls, title, icon) {
      title.textContent = "Electromagnet Strength & Flux Tuner";
      icon.textContent = "⚙️";

      let turns = 40;
      let amps = 2.0;

      function updateSim() {
        const fluxB = (turns * amps * 0.05).toFixed(2);
        const clips = Math.round(turns * amps * 0.15);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Solenoid on Nail -->
            <rect x="80" y="110" width="340" height="40" rx="4" fill="#94a3b8" stroke="#475569" stroke-width="2"/>
            <polygon points="420,110 450,130 420,150" fill="#94a3b8" />
            <rect x="60" y="95" width="20" height="70" rx="2" fill="#64748b"/>

            <!-- Coil Windings (Density depends on turns) -->
            <g fill="none" stroke="#f59e0b" stroke-width="4">
              ${Array.from({length: Math.min(25, Math.floor(turns / 3))}).map((_, i) => `
                <line x1="${100 + i * 12}" y1="105" x2="${100 + i * 12}" y2="155"/>
              `).join('')}
            </g>

            <!-- Magnetic Flux Lines -->
            <g fill="none" stroke="#38bdf8" stroke-width="${Math.min(5, amps * 1.2)}" stroke-dasharray="4,4">
              <ellipse cx="250" cy="130" rx="${120 + turns}" ry="${50 + amps * 8}" opacity="0.8"/>
            </g>

            <!-- Lifted Paperclips Clustered at Nail Tip -->
            <g transform="translate(435, 145)">
              ${Array.from({length: Math.min(18, clips)}).map((_, i) => `
                <path d="M ${-10 + (i%3)*6} ${i * 4} q 8 12 0 16 q -8 -12 0 -16" 
                      fill="none" stroke="#cbd5e1" stroke-width="2" />
              `).join('')}
            </g>

            <!-- Live Formula Callout Box -->
            <rect x="40" y="210" width="420" height="85" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="60" y="235" fill="#38bdf8" font-size="12" font-weight="bold">Lifting Performance Calculator ($B \\propto N \\cdot I$):</text>
            <text x="60" y="260" fill="#cbd5e1" font-size="12">
              Turns: <strong>${turns}</strong> | Current: <strong>${amps} A</strong>
            </text>
            <text x="60" y="280" fill="#f59e0b" font-size="13" font-weight="bold">
              Magnetic Flux Density (B): ≈ ${fluxB} Tesla | Steel Clips Lifted: ${clips} clips
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Number of Turns (N):</span>
          <input type="range" class="sim-slider" id="sliderTurns" min="10" max="100" step="10" value="${turns}">
          <span class="control-value" id="valTurns">${turns} turns</span>
        </div>
        <div class="control-row">
          <span class="control-label">Electric Current (I):</span>
          <input type="range" class="sim-slider" id="sliderAmps" min="0.5" max="5.0" step="0.5" value="${amps}">
          <span class="control-value" id="valAmps">${amps} A</span>
        </div>
      `;

      document.getElementById('sliderTurns').oninput = (e) => {
        turns = parseInt(e.target.value);
        document.getElementById('valTurns').textContent = `${turns} turns`;
        updateSim();
      };

      document.getElementById('sliderAmps').oninput = (e) => {
        amps = parseFloat(e.target.value);
        document.getElementById('valAmps').textContent = `${amps} A`;
        updateSim();
      };

      updateSim();
    }

    // 5. INDUSTRIAL SCRAP CRANE ELECTROMAGNET SIMULATOR
    function simScrapCrane(canvas, controls, title, icon) {
      title.textContent = "Scrap Yard Crane Electromagnet";
      icon.textContent = "🏗️";

      let craneStage = 0; // 0: Lowered at pile, 1: Energized & Holding, 2: Lifted over bin, 3: Dropped in bin

      function updateSim() {
        const magnetY = (craneStage === 0 || craneStage === 1) ? 170 : 80;
        const magnetX = (craneStage === 2 || craneStage === 3) ? 380 : 160;
        const isHolding = (craneStage === 1 || craneStage === 2);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Ground Base -->
            <rect x="0" y="270" width="500" height="50" fill="#1e293b"/>
            
            <!-- Sorting Hopper Bin (Right Side) -->
            <polygon points="340,220 440,220 420,270 360,270" fill="#334155" stroke="#64748b" stroke-width="2"/>
            <text x="390" y="250" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Steel Hopper</text>

            <!-- Mixed Scrap Pile (Left Side) -->
            <text x="160" y="260" fill="#94a3b8" font-size="11" text-anchor="middle">Non-Magnetic (Aluminum & Plastic)</text>
            <!-- Yellow plastic bottle & silver aluminum can on ground -->
            <rect x="130" y="245" width="22" height="12" rx="3" fill="#eab308"/>
            <rect x="170" y="242" width="18" height="15" rx="4" fill="#94a3b8"/>

            <!-- Crane Arm Gantry -->
            <line x1="50" y1="20" x2="450" y2="20" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>
            <polygon points="40,280 60,20 80,280" fill="#334155" stroke="#f59e0b" stroke-width="2"/>

            <!-- Crane Cable to Magnet Disk -->
            <line x1="${magnetX}" y1="20" x2="${magnetX}" y2="${magnetY}" stroke="#94a3b8" stroke-width="3"/>

            <!-- Crane Electromagnet Circular Disk -->
            <g transform="translate(${magnetX}, ${magnetY})">
              <ellipse cx="0" cy="0" rx="45" ry="14" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
              <rect x="-35" y="-18" width="70" height="18" fill="#0369a1" rx="4"/>
              
              <!-- Power Indicator LED on Magnet -->
              <circle cx="0" cy="-8" r="4" fill="${isHolding ? '#10b981' : '#f43f5e'}" />

              <!-- Magnetic Flux Sparkle when Energized -->
              ${isHolding ? `
                <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2">
                  <line x1="-30" y1="15" x2="-30" y2="30"/>
                  <line x1="0" y1="16" x2="0" y2="35"/>
                  <line x1="30" y1="15" x2="30" y2="30"/>
                </g>
              ` : ''}

              <!-- Heavy Scrap Car Body / Steel Beams attached -->
              ${isHolding ? `
                <rect x="-40" y="14" width="80" height="35" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
                <text x="0" y="36" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">5-Ton Steel Beam</text>
              ` : ''}
            </g>

            <!-- Dropped Scrap in Bin -->
            ${craneStage === 3 ? `
              <rect x="360" y="200" width="60" height="25" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
              <text x="390" y="217" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Delivered!</text>
            ` : ''}

            <!-- Status Banner -->
            <rect x="15" y="45" width="220" height="30" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
            <text x="25" y="65" fill="#38bdf8" font-size="11" font-weight="bold">
              ${craneStage === 0 ? '1. Lowered over scrap pile' :
                craneStage === 1 ? '2. Current ON: Steel Magnetized!' :
                craneStage === 2 ? '3. Lifted & Moved to Hopper' :
                '4. Current OFF: Heavy Load Dropped!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button class="btn-sim" id="btnStep">▶ Next Operational Step</button>
          <button class="btn-sim" id="btnReset">🔄 Reset Crane</button>
        </div>
      `;

      document.getElementById('btnStep').onclick = () => {
        craneStage = (craneStage + 1) % 4;
        updateSim();
      };

      document.getElementById('btnReset').onclick = () => {
        craneStage = 0;
        updateSim();
      };

      updateSim();
    }

    // 6. EARTH'S GEOMAGNETIC SHIELD SIMULATOR
    function simEarthMagnetism(canvas, controls, title, icon) {
      title.textContent = "Earth's Geodynamo & Magnetosphere Shield";
      icon.textContent = "🌍";

      let shieldActive = true;
      let solarFlare = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Outer Space Deep Darkness -->
            <rect x="0" y="0" width="500" height="320" fill="#070d18"/>

            <!-- Solar Wind Cosmic Rays (Streaming from Left) -->
            <g stroke="#f59e0b" stroke-width="${solarFlare ? 3.5 : 1.5}" stroke-linecap="round">
              ${Array.from({length: 12}).map((_, i) => {
                const y = 30 + i * 22;
                return shieldActive ? `
                  <path d="M 0 ${y} Q 180 ${y} ${y < 160 ? 250 : 250} ${y < 160 ? y - 45 : y + 45}" fill="none" opacity="0.8"/>
                ` : `
                  <line x1="0" y1="${y}" x2="500" y2="${y}" opacity="0.9" stroke="#ef4444"/>
                `;
              }).join('')}
            </g>

            <!-- Earth Magnetosphere Magnetic Field Lines -->
            ${shieldActive ? `
              <g fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.75">
                <ellipse cx="320" cy="160" rx="140" ry="90"/>
                <ellipse cx="320" cy="160" rx="100" ry="60"/>
              </g>
            ` : ''}

            <!-- Rotating Earth -->
            <g transform="translate(320, 160)">
              <!-- Blue Ocean Globe -->
              <circle r="55" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <!-- Green Continents -->
              <path d="M -35 -20 Q -10 -40 20 -20 Q 30 10 10 35 Q -30 20 -35 -20 Z" fill="#10b981"/>
              <!-- Molten Outer Core Cutaway Indicator -->
              <circle r="22" fill="#f59e0b" stroke="#ef4444" stroke-width="2" opacity="0.9"/>
              <circle r="10" fill="#ef4444"/>
              <text x="0" y="4" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">Liquid Core</text>

              <!-- North & South Geomagnetic Poles -->
              <text x="0" y="-62" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">N (Geomagnetic)</text>
              <text x="0" y="74" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">S (Geomagnetic)</text>
            </g>

            <!-- Migratory Birds Group Navigating -->
            <g transform="translate(390, 80)" fill="#f8fafc">
              <path d="M 0 0 L 8 -5 L 16 0 L 8 -2 Z" />
              <path d="M 12 15 L 20 10 L 28 15 L 20 13 Z" />
              <text x="-5" y="35" fill="#38bdf8" font-size="10">Bird Magnetoreception</text>
            </g>

            <!-- Status Banner -->
            <rect x="20" y="270" width="460" height="35" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
            <text x="250" y="292" fill="${shieldActive ? '#34d399' : '#f43f5e'}" font-size="12" font-weight="bold" text-anchor="middle">
              ${shieldActive ? '✔ Magnetosphere Active: Deflecting Lethal Cosmic Radiation' : '✖ SHIELD DISABLED: Solar Wind Bombards Planetary Atmosphere!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn-sim ${shieldActive ? 'active' : ''}" id="btnShield">
            🛡️ Magnetosphere Shield: ${shieldActive ? 'ON' : 'OFF'}
          </button>
          <button class="btn-sim" id="btnSolar">
            ☀️ Solar Storm Flare Burst!
          </button>
        </div>
      `;

      document.getElementById('btnShield').onclick = () => {
        shieldActive = !shieldActive;
        document.getElementById('btnShield').classList.toggle('active', shieldActive);
        updateSim();
      };

      document.getElementById('btnSolar').onclick = () => {
        solarFlare = true;
        updateSim();
        setTimeout(() => { solarFlare = false; updateSim(); }, 1500);
      };

      updateSim();
    }

    // 7. ELECTRON COLLISION & RESISTANCE SIMULATOR
    function simElectronCollision(canvas, controls, title, icon) {
      title.textContent = "Microscopic Resistance & Joule Heat";
      icon.textContent = "⚛️";

      let voltage = 6;

      function updateSim() {
        const tempC = Math.round(25 + voltage * voltage * 1.5);
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Wire Outer Cylinder Boundaries -->
            <rect x="40" y="60" width="420" height="180" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            
            <!-- Fixed Metal Lattice Positive Ions (Vibrating) -->
            ${Array.from({length: 4}).map((_, r) => {
              return Array.from({length: 7}).map((_, c) => {
                const cx = 80 + c * 52;
                const cy = 90 + r * 42;
                return `
                  <g transform="translate(${cx}, ${cy})">
                    <circle r="14" fill="#ef4444" opacity="0.85">
                      <animateTransform attributeName="transform" type="translate" 
                        values="0,0; ${voltage*0.4},${-voltage*0.3}; ${-voltage*0.4},${voltage*0.3}; 0,0" 
                        dur="${0.8 / (voltage*0.3)}s" repeatCount="indefinite"/>
                    </circle>
                    <text x="0" y="5" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">+</text>
                  </g>
                `;
              }).join('');
            }).join('')}

            <!-- Drifting Electrons with Collision Zig-Zags -->
            <g fill="#38bdf8" filter="drop-shadow(0 0 4px #38bdf8)">
              ${Array.from({length: 8}).map((_, i) => `
                <circle cx="${60 + i * 45}" cy="${100 + (i%3)*35}" r="5">
                  <animate attributeName="cx" from="50" to="440" dur="${3.0 / (voltage*0.5)}s" repeatCount="indefinite"/>
                </circle>
              `).join('')}
            </g>

            <!-- Thermometer Display -->
            <rect x="40" y="255" width="420" height="50" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="60" y="285" fill="#cbd5e1" font-size="12">
              Applied Voltage: <strong>${voltage} V</strong> | Lattice Collisions: <strong>High Friction</strong>
            </text>
            <text x="320" y="285" fill="#f59e0b" font-size="14" font-weight="bold">
              Wire Temp: ${tempC} °C
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Driving Voltage (Pushing Electrons):</span>
          <input type="range" class="sim-slider" id="sliderVolt" min="2" max="12" step="1" value="${voltage}">
          <span class="control-value" id="valVolt">${voltage} V</span>
        </div>
      `;

      document.getElementById('sliderVolt').oninput = (e) => {
        voltage = parseInt(e.target.value);
        document.getElementById('valVolt').textContent = `${voltage} V`;
        updateSim();
      };

      updateSim();
    }

    // 8. NICHROME VS COPPER COMPARISON SIMULATOR
    function simNichromeCopper(canvas, controls, title, icon) {
      title.textContent = "Material Duel: Copper vs. Nichrome Wire";
      icon.textContent = "🔥";

      let amps = 3.0;

      function updateSim() {
        const nichromeTemp = Math.round(25 + amps * amps * 22);
        const copperTemp = Math.round(25 + amps * 1.2);
        
        // Color transition for glowing nichrome
        let nichromeColor = '#94a3b8';
        if (nichromeTemp > 100) nichromeColor = '#b45309';
        if (nichromeTemp > 300) nichromeColor = '#ef4444';
        if (nichromeTemp > 600) nichromeColor = '#f59e0b';
        if (nichromeTemp > 900) nichromeColor = '#fef08a';

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Wire Track A: Copper -->
            <rect x="40" y="50" width="420" height="90" rx="10" fill="#1e293b" stroke="#334155"/>
            <text x="60" y="75" fill="#38bdf8" font-size="13" font-weight="bold">Wire A: Pure Copper (Low Resistance ≈ 0.05 Ω)</text>
            <line x1="60" y1="105" x2="380" y2="105" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
            <text x="400" y="110" fill="#34d399" font-size="13" font-weight="bold">${copperTemp} °C (Cool)</text>

            <!-- Wire Track B: Nichrome Alloy -->
            <rect x="40" y="165" width="420" height="90" rx="10" fill="#1e293b" stroke="#334155"/>
            <text x="60" y="190" fill="#f59e0b" font-size="13" font-weight="bold">Wire B: Nichrome Alloy (High Resistance ≈ 3.2 Ω)</text>
            <!-- Coiled Heating Element Shape -->
            <path d="M 60 220 Q 80 200 100 220 T 140 220 T 180 220 T 220 220 T 260 220 T 300 220 T 340 220 T 380 220" 
                  fill="none" stroke="${nichromeColor}" stroke-width="7" stroke-linecap="round"
                  filter="drop-shadow(0 0 8px ${nichromeColor})"/>
            <text x="400" y="225" fill="#f43f5e" font-size="13" font-weight="bold">${nichromeTemp} °C</text>

            <!-- Comparative Summary Bar -->
            <rect x="40" y="270" width="420" height="35" rx="6" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
            <text x="250" y="292" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Same Current (${amps} A) flowing through both: <strong>Nichrome produces 60× more heat!</strong>
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Electric Current (I):</span>
          <input type="range" class="sim-slider" id="sliderAmps" min="1.0" max="6.0" step="0.5" value="${amps}">
          <span class="control-value" id="valAmps">${amps} A</span>
        </div>
      `;

      document.getElementById('sliderAmps').oninput = (e) => {
        amps = parseFloat(e.target.value);
        document.getElementById('valAmps').textContent = `${amps} A`;
        updateSim();
      };

      updateSim();
    }

    // 9. JOULE HEATING & BULB FILAMENT SIMULATOR
    function simJouleHeating(canvas, controls, title, icon) {
      title.textContent = "Joule's Law Calculator ($H = I^2 R t$)";
      icon.textContent = "💡";

      let amps = 2.0;
      let ohms = 10;
      let secs = 5;

      function updateSim() {
        const joules = Math.round(amps * amps * ohms * secs);
        const bulbBrightness = Math.min(1.0, (amps * amps * ohms) / 300);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Incandescent Bulb Contour -->
            <g transform="translate(140, 140)">
              <!-- Glass Bulb Glow -->
              <circle r="60" fill="rgba(254, 240, 138, ${bulbBrightness * 0.4})" />
              <path d="M -45 -35 C -60 10 -35 50 -20 60 L 20 60 C 35 50 60 10 45 -35 C 30 -70 -30 -70 -45 -35 Z" 
                    fill="rgba(255,255,255,0.06)" stroke="#cbd5e1" stroke-width="2"/>
              <!-- Metal Screw Base -->
              <rect x="-20" y="60" width="40" height="25" fill="#94a3b8" rx="2"/>
              <!-- Tungsten Filament Coils -->
              <path d="M -15 10 L -10 -20 L 0 -15 L 10 -20 L 15 10" fill="none" 
                    stroke="${bulbBrightness > 0.3 ? '#fef08a' : '#ef4444'}" stroke-width="4" stroke-linecap="round"
                    filter="drop-shadow(0 0 ${bulbBrightness * 12}px #fef08a)"/>
              <text x="0" y="-35" fill="#f8fafc" font-size="10" text-anchor="middle">Tungsten (3,422°C MP)</text>
            </g>

            <!-- Mathematical Calculation Card -->
            <rect x="250" y="40" width="220" height="240" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="70" fill="#38bdf8" font-size="14" font-weight="bold">Joule's Law ($H = I^2 R t$):</text>
            
            <text x="270" y="105" fill="#cbd5e1" font-size="12">Current ($I$): <strong>${amps} A</strong></text>
            <text x="270" y="130" fill="#cbd5e1" font-size="12">Resistance ($R$): <strong>${ohms} Ω</strong></text>
            <text x="270" y="155" fill="#cbd5e1" font-size="12">Time ($t$): <strong>${secs} s</strong></text>
            
            <line x1="270" y1="175" x2="450" y2="175" stroke="rgba(255,255,255,0.15)"/>
            
            <text x="270" y="200" fill="#94a3b8" font-size="11">Total Heat Generated:</text>
            <text x="270" y="235" fill="#f59e0b" font-size="22" font-weight="bold">
              ${joules.toLocaleString()} Joules
            </text>
            <text x="270" y="260" fill="#34d399" font-size="10">
              ≈ ${(joules / 4.184).toFixed(1)} Calories
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Current (I):</span>
          <input type="range" class="sim-slider" id="sliderI" min="0.5" max="5.0" step="0.5" value="${amps}">
          <span class="control-value" id="valI">${amps} A</span>
        </div>
        <div class="control-row">
          <span class="control-label">Resistance (R):</span>
          <input type="range" class="sim-slider" id="sliderR" min="2" max="25" step="1" value="${ohms}">
          <span class="control-value" id="valR">${ohms} Ω</span>
        </div>
        <div class="control-row">
          <span class="control-label">Duration (t):</span>
          <input type="range" class="sim-slider" id="sliderT" min="1" max="20" step="1" value="${secs}">
          <span class="control-value" id="valT">${secs} s</span>
        </div>
      `;

      document.getElementById('sliderI').oninput = (e) => { amps = parseFloat(e.target.value); document.getElementById('valI').textContent = `${amps} A`; updateSim(); };
      document.getElementById('sliderR').oninput = (e) => { ohms = parseInt(e.target.value); document.getElementById('valR').textContent = `${ohms} Ω`; updateSim(); };
      document.getElementById('sliderT').oninput = (e) => { secs = parseInt(e.target.value); document.getElementById('valT').textContent = `${secs} s`; updateSim(); };

      updateSim();
    }

    // 10. DOMESTIC APPLIANCE & SAFETY FUSE SIMULATOR
    function simApplianceFuse(canvas, controls, title, icon) {
      title.textContent = "Appliance Circuit & Safety Fuse Lab";
      icon.textContent = "🛡️";

      let loadTotal = 5; // Amps
      const fuseRating = 10; // Amps
      let isBlown = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Circuit Board -->
            <rect x="30" y="30" width="440" height="260" rx="14" fill="#1e293b" stroke="#334155" stroke-width="2"/>
            
            <!-- Live Wire Loop with Fuse Cartridge -->
            <path d="M 60 160 L 130 160" stroke="#ef4444" stroke-width="4"/>
            
            <!-- Glass Fuse Cartridge -->
            <g transform="translate(130, 140)">
              <rect x="0" y="0" width="80" height="40" rx="6" fill="rgba(255,255,255,0.08)" stroke="#cbd5e1" stroke-width="1.5"/>
              <rect x="-6" y="5" width="10" height="30" fill="#94a3b8" rx="2"/>
              <rect x="76" y="5" width="10" height="30" fill="#94a3b8" rx="2"/>
              <!-- Fuse Thin Wire Inside -->
              ${!isBlown ? `
                <line x1="5" y1="20" x2="75" y2="20" stroke="#f59e0b" stroke-width="${loadTotal > fuseRating ? 4 : 2}"/>
              ` : `
                <!-- Melted Broken Wire -->
                <line x1="5" y1="20" x2="30" y2="20" stroke="#f43f5e" stroke-width="2"/>
                <line x1="50" y1="20" x2="75" y2="20" stroke="#f43f5e" stroke-width="2"/>
                <circle cx="40" cy="20" r="4" fill="#f43f5e"/>
              `}
              <text x="40" y="32" fill="#cbd5e1" font-size="9" text-anchor="middle">10A Fuse</text>
            </g>

            <path d="M 216 160 L 320 160" stroke="${!isBlown ? '#ef4444' : '#64748b'}" stroke-width="4"/>

            <!-- Connected Domestic Appliance -->
            <g transform="translate(320, 100)">
              <rect x="0" y="0" width="120" height="120" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
              <text x="60" y="30" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Household Load</text>
              <text x="60" y="60" fill="#f8fafc" font-size="18" font-weight="bold" text-anchor="middle">${loadTotal} A</text>
              <text x="60" y="85" fill="#94a3b8" font-size="11" text-anchor="middle">
                ${loadTotal <= 5 ? 'TV & Laptop' : loadTotal <= 10 ? 'Electric Kettle' : 'Overload Geyser!'}
              </text>
            </g>

            <!-- Status Box -->
            <rect x="50" y="220" width="400" height="50" rx="8" fill="#0f172a" stroke="${isBlown ? '#f43f5e' : '#34d399'}"/>
            <text x="250" y="250" fill="${isBlown ? '#fb7185' : '#34d399'}" font-size="13" font-weight="bold" text-anchor="middle">
              ${isBlown ? '⚡ FUSE BLOWN! Excessive Current Melted Wire • House Fire Prevented!' : '✔ Circuit Safe: Current is within 10A fuse capacity.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button class="btn-sim" id="btnLow">Connect TV (3A)</button>
          <button class="btn-sim" id="btnMed">Connect Kettle (8A)</button>
          <button class="btn-sim" id="btnHigh">⚡ Overload Surge (16A)!</button>
          <button class="btn-sim" id="btnResetFuse">🔄 Replace Fuse</button>
        </div>
      `;

      document.getElementById('btnLow').onclick = () => { if (!isBlown) { loadTotal = 3; updateSim(); } };
      document.getElementById('btnMed').onclick = () => { if (!isBlown) { loadTotal = 8; updateSim(); } };
      document.getElementById('btnHigh').onclick = () => {
        loadTotal = 16;
        if (loadTotal > fuseRating) isBlown = true;
        updateSim();
      };
      document.getElementById('btnResetFuse').onclick = () => { isBlown = false; loadTotal = 5; updateSim(); };

      updateSim();
    }

    // 11. INDUSTRIAL ELECTRIC ARC FURNACE & SAFETY SIMULATOR
    function simArcFurnaceSafety(canvas, controls, title, icon) {
      title.textContent = "Electric Arc Furnace & Industrial Metallurgy";
      icon.textContent = "🏭";

      let arcOn = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Heavy Refractory Furnace Vessel -->
            <path d="M 80 140 L 100 270 Q 250 290 400 270 L 420 140 Z" fill="#334155" stroke="#64748b" stroke-width="3"/>
            
            <!-- Molten Steel Pool -->
            <path d="M 110 240 Q 250 260 390 240 Q 250 280 110 240 Z" fill="${arcOn ? '#f59e0b' : '#64748b'}" 
                  filter="drop-shadow(0 0 10px #f59e0b)"/>
            <text x="250" y="260" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">
              ${arcOn ? 'Molten Recycled Scrap Steel (> 3,000°C)' : 'Solid Cold Scrap Metal'}
            </text>

            <!-- Massive Carbon Graphite Electrodes -->
            <rect x="160" y="30" width="35" height="150" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <rect x="232" y="30" width="35" height="150" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <rect x="305" y="30" width="35" height="150" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
            <text x="250" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">Graphite Electrodes (100,000 Amperes)</text>

            <!-- Electric Plasma Arcs (Sparking when ON) -->
            ${arcOn ? `
              <g stroke="#a855f7" stroke-width="4" stroke-linecap="round" filter="drop-shadow(0 0 8px #c084fc)">
                <path d="M 177 180 L 165 200 L 185 220 L 175 240" fill="none"/>
                <path d="M 250 180 L 260 200 L 240 220 L 250 240" fill="none"/>
                <path d="M 322 180 L 310 200 L 330 220 L 320 240" fill="none"/>
              </g>
            ` : ''}
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${arcOn ? 'active' : ''}" id="btnArc">
          ⚡ Plasma Arc Power: ${arcOn ? 'Turn OFF' : 'Ignite Arc'}
        </button>
      `;

      document.getElementById('btnArc').onclick = () => {
        arcOn = !arcOn;
        document.getElementById('btnArc').textContent = `⚡ Plasma Arc Power: ${arcOn ? 'Turn OFF' : 'Ignite Arc'}`;
        document.getElementById('btnArc').classList.toggle('active', arcOn);
        updateSim();
      };

      updateSim();
    }

    // 12. GALVANI VS. VOLTAIC PILE SIMULATOR
    function simGalvaniVolta(canvas, controls, title, icon) {
      title.textContent = "Historic Dispute: Galvani vs. Volta (1800)";
      icon.textContent = "⚡";

      let mode = 'volta'; // 'galvani' or 'volta'

      function updateSim() {
        if (mode === 'galvani') {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="30" y="30" width="440" height="260" rx="12" fill="#1e293b" stroke="#334155"/>
              <text x="250" y="60" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">
                Luigi Galvani: "Animal Electricity" Experiment (1780s)
              </text>
              
              <!-- Frog Leg on Brass Hook & Iron Trellis -->
              <g transform="translate(250, 150)">
                <path d="M -80 -40 Q 0 -50 0 0 Q 30 50 50 10" fill="none" stroke="#22c55e" stroke-width="12" stroke-linecap="round"/>
                <line x1="-80" y1="-40" x2="-80" y2="40" stroke="#f59e0b" stroke-width="4"/>
                <text x="-80" y="60" fill="#f59e0b" font-size="11" text-anchor="middle">Brass Hook</text>
                <line x1="50" y1="10" x2="100" y2="40" stroke="#94a3b8" stroke-width="4"/>
                <text x="100" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Iron Scalpel</text>
              </g>

              <text x="250" y="260" fill="#cbd5e1" font-size="11" text-anchor="middle">
                Galvani thought the muscle produced electricity. Volta proved dissimilar metals did!
              </text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="30" y="30" width="440" height="260" rx="12" fill="#1e293b" stroke="#334155"/>
              <text x="250" y="55" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">
                Alessandro Volta: The Voltaic Pile (1800)
              </text>

              <!-- Alternating Zinc & Copper Discs with Brine Cardboard -->
              <g transform="translate(180, 80)">
                ${Array.from({length: 6}).map((_, i) => `
                  <!-- Copper Disc (Cathode +) -->
                  <rect x="0" y="${i * 26}" width="140" height="8" rx="2" fill="#b45309" stroke="#f59e0b"/>
                  <!-- Cardboard in Brine Acid -->
                  <rect x="10" y="${i * 26 + 8}" width="120" height="6" rx="1" fill="#cbd5e1"/>
                  <!-- Zinc Disc (Anode -) -->
                  <rect x="0" y="${i * 26 + 14}" width="140" height="8" rx="2" fill="#64748b" stroke="#94a3b8"/>
                `).join('')}
              </g>

              <!-- Output Meter -->
              <g transform="translate(360, 160)">
                <circle r="40" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                <text x="0" y="5" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">5.4 V</text>
                <text x="0" y="22" fill="#94a3b8" font-size="9" text-anchor="middle">DC Current</text>
              </g>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn-sim ${mode === 'volta' ? 'active' : ''}" id="btnVolta">Alessandro Volta's Pile (1800)</button>
          <button class="btn-sim ${mode === 'galvani' ? 'active' : ''}" id="btnGalvani">Luigi Galvani's Frog (1780)</button>
        </div>
      `;

      document.getElementById('btnVolta').onclick = () => { mode = 'volta'; updateSim(); };
      document.getElementById('btnGalvani').onclick = () => { mode = 'galvani'; updateSim(); };

      updateSim();
    }

    // 13. CITRUS LEMON CELL SIMULATOR
    function simLemonCell(canvas, controls, title, icon) {
      title.textContent = "Kitchen Science: Citrus Lemon Battery";
      icon.textContent = "🍋";

      let lemons = 3;

      function updateSim() {
        const totalV = (lemons * 0.9).toFixed(1);
        const ledLit = lemons >= 3;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Lemon Battery Units in Series -->
            ${Array.from({length: lemons}).map((_, i) => {
              const lx = 60 + i * (340 / lemons);
              return `
                <g transform="translate(${lx}, 130)">
                  <!-- Juicy Yellow Lemon Shape -->
                  <ellipse cx="40" cy="40" rx="36" ry="46" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
                  <!-- Copper Strip (+) -->
                  <rect x="18" y="-10" width="10" height="35" rx="2" fill="#b45309" stroke="#f59e0b"/>
                  <text x="23" y="-14" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Cu (+)</text>
                  <!-- Zinc Galvanized Nail (-) -->
                  <rect x="52" y="-10" width="8" height="40" rx="2" fill="#94a3b8" stroke="#cbd5e1"/>
                  <text x="56" y="-14" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">Zn (-)</text>
                </g>
              `;
            }).join('')}

            <!-- LED Indicator Load -->
            <g transform="translate(420, 150)">
              <circle r="25" fill="${ledLit ? 'rgba(239, 68, 68, 0.4)' : '#1e293b'}" stroke="#ef4444" stroke-width="2"/>
              <text x="0" y="5" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">
                ${ledLit ? 'LED ON!' : 'LED OFF'}
              </text>
            </g>

            <!-- Voltage Stats -->
            <rect x="40" y="250" width="420" height="45" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="60" y="278" fill="#cbd5e1" font-size="12">
              Series Count: <strong>${lemons} Lemons</strong> | Citric Acid Electrolyte (H⁺ ions)
            </text>
            <text x="360" y="278" fill="#38bdf8" font-size="16" font-weight="bold">
              ${totalV} Volts
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Lemons Connected in Series:</span>
          <input type="range" class="sim-slider" id="sliderLemons" min="1" max="4" step="1" value="${lemons}">
          <span class="control-value" id="valLemons">${lemons} Lemon${lemons > 1 ? 's' : ''}</span>
        </div>
      `;

      document.getElementById('sliderLemons').oninput = (e) => {
        lemons = parseInt(e.target.value);
        document.getElementById('valLemons').textContent = `${lemons} Lemon${lemons > 1 ? 's' : ''}`;
        updateSim();
      };

      updateSim();
    }

    // 14. DRY CELL CUTAWAY INSPECTOR SIMULATOR
    function simDryCellCutaway(canvas, controls, title, icon) {
      title.textContent = "Zinc-Carbon Dry Cell Cutaway Inspector";
      icon.textContent = "🔋";

      let activePart = 'zinc';

      const partsInfo = {
        zinc: { name: "Outer Zinc Canister (- Anode)", desc: "Serves as the structural casing and oxidizes: Zn → Zn²⁺ + 2e⁻, releasing electrons at the negative terminal." },
        carbon: { name: "Central Carbon Graphite Rod (+ Cathode)", desc: "Inert conductive rod with metal top cap collecting electrons to complete the positive circuit." },
        mno2: { name: "Manganese Dioxide (MnO₂) Depolarizer", desc: "Dense black powder that oxidizes insulating hydrogen gas bubbles into water, keeping current steady." },
        paste: { name: "Ammonium Chloride (NH₄Cl) Moist Paste", desc: "Immobilized electrolyte providing mobile chloride and ammonium ions without spilling liquids." }
      };

      function updateSim() {
        const info = partsInfo[activePart];
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Outer Zinc Container -->
            <rect x="80" y="50" width="160" height="210" rx="8" fill="#64748b" stroke="${activePart === 'zinc' ? '#38bdf8' : '#475569'}" stroke-width="${activePart === 'zinc' ? 4 : 2}"/>
            
            <!-- Moist NH4Cl Paste Layer -->
            <rect x="95" y="60" width="130" height="190" fill="#cbd5e1" stroke="${activePart === 'paste' ? '#38bdf8' : 'none'}" stroke-width="3"/>
            
            <!-- MnO2 Black Mixture -->
            <rect x="115" y="60" width="90" height="190" fill="#1e293b" stroke="${activePart === 'mno2' ? '#38bdf8' : 'none'}" stroke-width="3"/>
            
            <!-- Central Carbon Rod -->
            <rect x="145" y="40" width="30" height="200" rx="4" fill="#0f172a" stroke="${activePart === 'carbon' ? '#f59e0b' : '#334155'}" stroke-width="3"/>
            <!-- Metal Top Positive Cap -->
            <rect x="150" y="30" width="20" height="12" rx="2" fill="#fbbf24"/>
            <text x="160" y="24" fill="#fbbf24" font-weight="bold" font-size="12" text-anchor="middle">+ 1.5V</text>

            <!-- Flat Bottom Negative Terminal -->
            <text x="160" y="280" fill="#cbd5e1" font-weight="bold" font-size="12" text-anchor="middle">- Terminal</text>

            <!-- Component Detail Callout -->
            <rect x="260" y="60" width="210" height="190" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="275" y="90" fill="#38bdf8" font-size="13" font-weight="bold">${info.name}</text>
            <foreignObject x="275" y="105" width="180" height="130">
              <div xmlns="http://www.w3.org/1999/xhtml" style="color: #cbd5e1; font-size: 11px; line-height: 1.5;">
                ${info.desc}
              </div>
            </foreignObject>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
          <button class="btn-sim ${activePart === 'zinc' ? 'active' : ''}" id="btnZinc">1. Zinc Can (-)</button>
          <button class="btn-sim ${activePart === 'carbon' ? 'active' : ''}" id="btnCarbon">2. Carbon Rod (+)</button>
          <button class="btn-sim ${activePart === 'mno2' ? 'active' : ''}" id="btnMno2">3. MnO₂ Depolarizer</button>
          <button class="btn-sim ${activePart === 'paste' ? 'active' : ''}" id="btnPaste">4. NH₄Cl Paste</button>
        </div>
      `;

      document.getElementById('btnZinc').onclick = () => { activePart = 'zinc'; updateSim(); };
      document.getElementById('btnCarbon').onclick = () => { activePart = 'carbon'; updateSim(); };
      document.getElementById('btnMno2').onclick = () => { activePart = 'mno2'; updateSim(); };
      document.getElementById('btnPaste').onclick = () => { activePart = 'paste'; updateSim(); };

      updateSim();
    }

    // 15. LITHIUM-ION BATTERY SHUTTLE SIMULATOR
    function simLithiumIon(canvas, controls, title, icon) {
      title.textContent = "Lithium-Ion 'Rocking Chair' Shuttle";
      icon.textContent = "📱";

      let isCharging = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="30" y="40" width="440" height="220" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
            
            <!-- Graphite Anode (Left) -->
            <rect x="50" y="60" width="90" height="180" rx="6" fill="#334155" stroke="#64748b"/>
            <text x="95" y="90" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Graphite Anode</text>
            
            <!-- Separator Membrane (Middle) -->
            <rect x="235" y="60" width="30" height="180" fill="rgba(255,255,255,0.08)" stroke="#94a3b8" stroke-dasharray="4,4"/>
            <text x="250" y="155" fill="#94a3b8" font-size="9" text-anchor="middle" transform="rotate(-90 250 155)">Separator</text>

            <!-- Metal Oxide Cathode (Right) -->
            <rect x="360" y="60" width="90" height="180" rx="6" fill="#475569" stroke="#94a3b8"/>
            <text x="405" y="90" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">LiCoO₂ Cathode</text>

            <!-- Shuttling Lithium Ions (Li+) -->
            <g fill="#10b981" filter="drop-shadow(0 0 4px #10b981)">
              ${Array.from({length: 6}).map((_, i) => {
                const y = 110 + i * 22;
                return `
                  <circle cx="200" cy="${y}" r="8">
                    <animate attributeName="cx" 
                             from="${isCharging ? 380 : 100}" 
                             to="${isCharging ? 100 : 380}" 
                             dur="2s" repeatCount="indefinite"/>
                  </circle>
                  <text x="200" y="${y+3}" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">Li⁺</text>
                `;
              }).join('')}
            </g>

            <!-- Status Banner -->
            <rect x="40" y="270" width="420" height="35" rx="6" fill="#0f172a" stroke="#38bdf8"/>
            <text x="250" y="292" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
              ${isCharging ? '🔌 CHARGING: Li⁺ ions shuttle into Graphite Anode' : '📱 DISCHARGING: Li⁺ ions power your phone (3.7V - 4.2V)'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isCharging ? 'active' : ''}" id="btnCharge">
          ${isCharging ? '📱 Switch to Discharging (Phone Mode)' : '🔌 Plug in Wall Charger'}
        </button>
      `;

      document.getElementById('btnCharge').onclick = () => {
        isCharging = !isCharging;
        document.getElementById('btnCharge').classList.toggle('active', isCharging);
        updateSim();
      };

      updateSim();
    }

    // 16. SOLID-STATE BATTERY & E-WASTE RECYCLING SIMULATOR
    function simSolidStateEwaste(canvas, controls, title, icon) {
      title.textContent = "Solid-State Innovation & E-Waste Recovery";
      icon.textContent = "♻️";

      let viewMode = 'solid_state'; // 'solid_state' or 'ewaste'

      function updateSim() {
        if (viewMode === 'solid_state') {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="30" y="30" width="440" height="260" rx="12" fill="#1e293b" stroke="#334155"/>
              <text x="250" y="60" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">
                Next-Gen Solid-State Battery (Non-Flammable Ceramic)
              </text>

              <!-- Solid Electrolyte Layer -->
              <rect x="80" y="100" width="100" height="120" rx="4" fill="#0284c7"/>
              <text x="130" y="165" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Lithium Anode</text>
              
              <rect x="180" y="90" width="140" height="140" rx="6" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="250" y="155" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">Solid Ceramic</text>
              <text x="250" y="175" fill="#0f172a" font-size="10" text-anchor="middle">Non-Flammable</text>

              <rect x="320" y="100" width="100" height="120" rx="4" fill="#f59e0b"/>
              <text x="370" y="165" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Cathode</text>

              <text x="250" y="260" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">
                ✔ Zero Fire Risk • 10-Minute Ultra-Fast Charging • High Driving Range
              </text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="30" y="30" width="440" height="260" rx="12" fill="#1e293b" stroke="#334155"/>
              <text x="250" y="60" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">
                Certified E-Waste Hydrometallurgical Recycling
              </text>

              <!-- Recovery Vats -->
              <rect x="60" y="110" width="80" height="100" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
              <text x="100" y="155" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">95% Li</text>
              <text x="100" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Purified Lithium</text>

              <rect x="160" y="110" width="80" height="100" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
              <text x="200" y="155" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">95% Co</text>
              <text x="200" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Purified Cobalt</text>

              <rect x="260" y="110" width="80" height="100" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
              <text x="300" y="155" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">98% Cu</text>
              <text x="300" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Pure Copper</text>

              <rect x="360" y="110" width="80" height="100" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
              <text x="400" y="155" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Neutralized</text>
              <text x="400" y="175" fill="#94a3b8" font-size="10" text-anchor="middle">Zero Acid Leak</text>

              <text x="250" y="260" fill="#cbd5e1" font-size="11" text-anchor="middle">
                Always deposit spent batteries at e-waste centers to protect soil & groundwater!
              </text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn-sim ${viewMode === 'solid_state' ? 'active' : ''}" id="btnSS">Solid-State Battery Tech</button>
          <button class="btn-sim ${viewMode === 'ewaste' ? 'active' : ''}" id="btnEW">E-Waste Closed-Loop Facility</button>
        </div>
      `;

      document.getElementById('btnSS').onclick = () => { viewMode = 'solid_state'; updateSim(); };
      document.getElementById('btnEW').onclick = () => { viewMode = 'ewaste'; updateSim(); };

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-electric-current.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

