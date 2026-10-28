# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-pressure-winds.html
Class 8 Science - Chapter 6: Pressure, Winds, Storms, and Cyclones
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar
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
from class8_science_pressure_winds_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 6: Pressure, Winds, Storms & Cyclones Master Lab</title>
  
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
        radial-gradient(circle at 85% 80%, rgba(14, 165, 233, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(245, 158, 11, 0.05) 0%, transparent 60%);
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
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }

    .header-text h1 {
      font-size: 1.1rem;
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
      background: linear-gradient(90deg, #38bdf8, #f59e0b);
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
      background: rgba(30, 41, 59, 0.7);
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
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      position: relative;
      flex-shrink: 0;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--accent-sky);
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
      background: linear-gradient(135deg, #ffffff, #67e8f9);
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
      <div class="lab-icon">🌪️</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 6</div>
        <h1>Pressure, Winds, Storms & Cyclones</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Defining Pressure & Area</span>
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
        <span class="avatar-name">Dr. Pawan • Atmospheric Physicist</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Welcome to the Atmospheric Physics Lab! Let us explore the profound connections between force, pressure, winds, and cyclonic systems.
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
          <span class="slide-tag" id="slideBadge">Pressure Fundamentals</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Defining Pressure & Area</h2>

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
            <span id="simIcon">📌</span>
            <span id="simTitle">Interactive Physics Simulator</span>
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
        chip.innerHTML = `<span class="vocab-word">🌪️ ${item.word}:</span><span class="vocab-def">${item.definition}</span>`;
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

      currentUtterance.onerror = () => {
        isSpeaking = false;
        pulse.style.display = 'none';
        pill.style.display = 'none';
        document.getElementById('btnAudioToggle').textContent = '🔊';
      };

      synth.speak(currentUtterance);
    }

    function toggleSpeech() {
      if (!('speechSynthesis' in window)) return;
      if (isSpeaking) {
        synth.cancel();
        isSpeaking = false;
        document.getElementById('avatarPulse').style.display = 'none';
        document.getElementById('speechStatusPill').style.display = 'none';
        document.getElementById('btnAudioToggle').textContent = '🔊';
      } else {
        const text = document.getElementById('avatarSpeechText').textContent;
        speakText(text);
      }
    }

    function replaySpeech() {
      const text = document.getElementById('avatarSpeechText').textContent;
      speakText(text);
    }

    // ==========================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS
    // ==========================================

    function renderSimulator(simId) {
      const canvas = document.getElementById('simCanvas');
      const controls = document.getElementById('simControls');
      const title = document.getElementById('simTitle');
      const icon = document.getElementById('simIcon');

      canvas.innerHTML = '';
      controls.innerHTML = '';

      switch (simId) {
        case 'pressure_area_sim':
          simPressureArea(canvas, controls, title, icon);
          break;
        case 'bag_strap_pressure_sim':
          simBagStrapPressure(canvas, controls, title, icon);
          break;
        case 'liquid_pressure_directions_sim':
          simLiquidPressureDirections(canvas, controls, title, icon);
          break;
        case 'depth_dam_architecture_sim':
          simDepthDamArchitecture(canvas, controls, title, icon);
          break;
        case 'atmospheric_pressure_mercury_sim':
          simAtmosphericPressureMercury(canvas, controls, title, icon);
          break;
        case 'body_fluid_balance_sim':
          simBodyFluidBalance(canvas, controls, title, icon);
          break;
        case 'bernoulli_balloons_roof_sim':
          simBernoulliBalloonsRoof(canvas, controls, title, icon);
          break;
        case 'pressure_gradient_wind_sim':
          simPressureGradientWind(canvas, controls, title, icon);
          break;
        case 'land_sea_breeze_cycle_sim':
          simLandSeaBreezeCycle(canvas, controls, title, icon);
          break;
        case 'storm_convection_cloud_sim':
          simStormConvectionCloud(canvas, controls, title, icon);
          break;
        case 'lightning_charge_breakdown_sim':
          simLightningChargeBreakdown(canvas, controls, title, icon);
          break;
        case 'thunder_sound_distance_sim':
          simThunderSoundDistance(canvas, controls, title, icon);
          break;
        case 'lightning_conductor_earthing_sim':
          simLightningConductorEarthing(canvas, controls, title, icon);
          break;
        case 'cyclone_vortex_coriolis_sim':
          simCycloneVortexCoriolis(canvas, controls, title, icon);
          break;
        case 'cyclone_eye_storm_surge_sim':
          simCycloneEyeStormSurge(canvas, controls, title, icon);
          break;
        case 'imd_satellite_tracking_sim':
          simImdSatelliteTracking(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = `<div style="color: #94a3b8; font-size: 0.9rem;">Select a valid simulator.</div>`;
      }
    }

    // 1. PRESSURE & CONTACT AREA SIMULATOR
    function simPressureArea(canvas, controls, title, icon) {
      title.textContent = "Pointed Nail vs. Blunt Head: P = F / A";
      icon.textContent = "📌";

      let forceN = 50;
      let isPointed = true;

      function updateSim() {
        const areaCm2 = isPointed ? 0.01 : 2.0;
        const pressureKPa = Math.round((forceN / (areaCm2 * 0.0001)) / 1000);
        const depthPx = isPointed ? Math.min(100, Math.round(forceN * 1.1)) : Math.min(12, Math.round(forceN * 0.12));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Wooden Block -->
            <rect x="50" y="170" width="220" height="110" fill="#78350f" stroke="#b45309" stroke-width="2" rx="4"/>
            <text x="160" y="240" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Wooden Plank</text>
            <line x1="50" y1="170" x2="270" y2="170" stroke="#f59e0b" stroke-width="3"/>

            <!-- Nail / Rod Assembly -->
            <g transform="translate(160, ${60 + depthPx})">
              <!-- Hammer Head above -->
              <rect x="-35" y="-35" width="70" height="25" fill="#475569" stroke="#94a3b8" stroke-width="2" rx="3"/>
              <text x="0" y="-18" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Hammer (${forceN} N)</text>
              <line x1="0" y1="-10" x2="0" y2="0" stroke="#ef4444" stroke-width="4"/>

              <!-- Nail Shaft -->
              <rect x="${isPointed ? -4 : -25}" y="0" width="${isPointed ? 8 : 50}" height="70" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
              
              ${isPointed ? `
                <!-- Sharp Point -->
                <polygon points="-4,70 4,70 0,90" fill="#cbd5e1" stroke="#94a3b8"/>
              ` : `
                <!-- Flat Broad End -->
                <rect x="-25" y="70" width="50" height="6" fill="#64748b" stroke="#cbd5e1"/>
              `}
            </g>

            <!-- Results Dashboard -->
            <rect x="290" y="50" width="175" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="305" y="80" fill="#38bdf8" font-size="13" font-weight="bold">Pressure Calculus:</text>
            
            <text x="305" y="110" fill="#94a3b8" font-size="11">Applied Thrust (F):</text>
            <text x="305" y="128" fill="#f8fafc" font-size="13" font-weight="bold">${forceN} N</text>

            <text x="305" y="152" fill="#94a3b8" font-size="11">Contact Area (A):</text>
            <text x="305" y="170" fill="#f59e0b" font-size="13" font-weight="bold">${areaCm2} cm² (${isPointed ? 'Tiny' : 'Broad'})</text>

            <text x="305" y="196" fill="#94a3b8" font-size="11">Resulting Pressure (P):</text>
            <text x="305" y="222" fill="${isPointed ? '#f43f5e' : '#10b981'}" font-size="18" font-weight="800">${pressureKPa} kPa</text>

            <text x="305" y="248" fill="#cbd5e1" font-size="10">
              ${isPointed ? '📌 Penetrates deeply into wood!' : '🛡️ Tiny pressure, wood resists.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Hammer Force (N):</span>
          <input type="range" class="sim-slider" id="sliderForce" min="10" max="100" step="5" value="${forceN}">
          <span class="control-value" id="valForce">${forceN} N</span>
        </div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
          <button class="btn-sim ${isPointed ? 'active' : ''}" id="btnPointed">📌 Sharp Pointed Tip</button>
          <button class="btn-sim ${!isPointed ? 'active' : ''}" id="btnBlunt">🔨 Flat Blunt Head</button>
        </div>
      `;

      document.getElementById('sliderForce').oninput = (e) => {
        forceN = parseInt(e.target.value);
        document.getElementById('valForce').textContent = `${forceN} N`;
        updateSim();
      };

      document.getElementById('btnPointed').onclick = () => {
        isPointed = true;
        document.getElementById('btnPointed').classList.add('active');
        document.getElementById('btnBlunt').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnBlunt').onclick = () => {
        isPointed = false;
        document.getElementById('btnBlunt').classList.add('active');
        document.getElementById('btnPointed').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 2. BACKPACK STRAP PRESSURE SIMULATOR
    function simBagStrapPressure(canvas, controls, title, icon) {
      title.textContent = "Shoulder Load: Thin Cord vs. Broad Padded Strap";
      icon.textContent = "🎒";

      let bagWeight = 60; // N
      let strapType = 'broad'; // 'thin' or 'broad'

      function updateSim() {
        const isThin = (strapType === 'thin');
        const strapWidth = isThin ? 0.5 : 6.0; // cm
        const contactArea = Math.round(strapWidth * 15); // cm^2
        const pressureKPa = Math.round((bagWeight / (contactArea * 0.0001)) / 1000);
        const indentY = isThin ? Math.min(25, Math.round(bagWeight * 0.3)) : Math.min(6, Math.round(bagWeight * 0.08));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Human Shoulder Contour -->
            <path d="M 60 260 C 80 160 140 140 220 160 C 260 170 280 200 290 260 Z" fill="#334155" stroke="#64748b" stroke-width="2"/>
            <text x="175" y="240" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Student Shoulder</text>

            <!-- Strap Resting and Cutting In -->
            <g transform="translate(160, ${142 + indentY})">
              <!-- Indentation mark -->
              ${isThin ? `
                <ellipse cx="0" cy="0" rx="6" ry="12" fill="#ef4444" opacity="0.8"/>
                <!-- Thin string strap -->
                <rect x="-3" y="-50" width="6" height="50" fill="#f87171" stroke="#dc2626"/>
                <text x="15" y="-20" fill="#fb7185" font-size="11" font-weight="bold">Thin Cord (0.5 cm)</text>
              ` : `
                <ellipse cx="0" cy="0" rx="35" ry="4" fill="#10b981" opacity="0.6"/>
                <!-- Broad padded strap -->
                <rect x="-35" y="-50" width="70" height="50" fill="#0284c7" stroke="#38bdf8" rx="4"/>
                <text x="45" y="-20" fill="#38bdf8" font-size="11" font-weight="bold">Broad Padded (6.0 cm)</text>
              `}
            </g>

            <!-- Heavy Backpack Vector -->
            <rect x="250" y="160" width="40" height="70" rx="6" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
            <text x="270" y="200" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Bag (${bagWeight}N)</text>
            <line x1="270" y1="230" x2="270" y2="260" stroke="#f59e0b" stroke-width="3"/>

            <!-- Metrics Panel -->
            <rect x="310" y="50" width="155" height="220" rx="10" fill="#1e293b" stroke="${isThin ? '#f43f5e' : '#10b981'}" stroke-width="1.5"/>
            <text x="325" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Comfort Assessment:</text>
            
            <text x="325" y="110" fill="#94a3b8" font-size="10">Shoulder Contact Area:</text>
            <text x="325" y="128" fill="#f8fafc" font-size="13" font-weight="bold">${contactArea} cm²</text>

            <text x="325" y="155" fill="#94a3b8" font-size="10">Pressure on Tissue:</text>
            <text x="325" y="180" fill="${isThin ? '#fb7185' : '#34d399'}" font-size="18" font-weight="800">${pressureKPa} kPa</text>

            <text x="325" y="210" fill="#cbd5e1" font-size="10">
              ${isThin ? '⚠️ Severe pain, tissue crushing!' : '🌿 Comfortable, force spread evenly.'}
            </text>
            <text x="325" y="240" fill="#f59e0b" font-size="9">
              Rule: Larger Area = Lower Pressure
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">School Bag Weight (N):</span>
          <input type="range" class="sim-slider" id="sliderBag" min="20" max="100" step="10" value="${bagWeight}">
          <span class="control-value" id="valBag">${bagWeight} N</span>
        </div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
          <button class="btn-sim ${strapType === 'thin' ? 'active' : ''}" id="btnThin">🧵 Thin Cord (Severe Pressure)</button>
          <button class="btn-sim ${strapType === 'broad' ? 'active' : ''}" id="btnBroad">🎒 Broad Padded Strap (Low Pressure)</button>
        </div>
      `;

      document.getElementById('sliderBag').oninput = (e) => {
        bagWeight = parseInt(e.target.value);
        document.getElementById('valBag').textContent = `${bagWeight} N`;
        updateSim();
      };

      document.getElementById('btnThin').onclick = () => {
        strapType = 'thin';
        document.getElementById('btnThin').classList.add('active');
        document.getElementById('btnBroad').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnBroad').onclick = () => {
        strapType = 'broad';
        document.getElementById('btnBroad').classList.add('active');
        document.getElementById('btnThin').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 3. LIQUID PRESSURE: EQUAL IN ALL DIRECTIONS SIMULATOR
    function simLiquidPressureDirections(canvas, controls, title, icon) {
      title.textContent = "Liquid Pressure: Equal Sideways and Downward";
      icon.textContent = "💧";

      let depthCm = 15;

      function updateSim() {
        const spurtingLength = Math.round(depthCm * 3.2);
        const hydroPressure = Math.round(depthCm * 0.98); // kPa approx (rho * g * h)

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Central Transparent Cylinder -->
            <rect x="180" y="60" width="140" height="200" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="2"/>
            
            <!-- Water filling inside cylinder -->
            <rect x="182" y="${260 - depthCm * 8}" width="136" height="${depthCm * 8}" fill="#0284c7" opacity="0.6"/>
            <line x1="180" y1="${260 - depthCm * 8}" x2="320" y2="${260 - depthCm * 8}" stroke="#67e8f9" stroke-width="2" stroke-dasharray="4,2"/>
            <text x="250" y="${250 - depthCm * 8}" fill="#67e8f9" font-size="10" font-weight="bold" text-anchor="middle">Water Height = ${depthCm} cm</text>

            <!-- Left Spout at bottom -->
            <circle cx="180" cy="240" r="4" fill="#38bdf8"/>
            <!-- Left Water Jet Parabola -->
            <path d="M 180 240 Q ${180 - spurtingLength * 0.6} 240 ${180 - spurtingLength} 280" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
            <text x="${160 - spurtingLength * 0.5}" y="232" fill="#7dd3fc" font-size="10">L = ${spurtingLength} mm</text>

            <!-- Right Spout at bottom (Same depth) -->
            <circle cx="320" cy="240" r="4" fill="#38bdf8"/>
            <!-- Right Water Jet Parabola -->
            <path d="M 320 240 Q ${320 + spurtingLength * 0.6} 240 ${320 + spurtingLength} 280" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
            <text x="${340 + spurtingLength * 0.5}" y="232" fill="#7dd3fc" font-size="10">L = ${spurtingLength} mm</text>

            <!-- Downward Bottom Spout -->
            <circle cx="250" cy="260" r="4" fill="#38bdf8"/>
            <line x1="250" y1="260" x2="250" y2="295" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>

            <!-- Ground Tray -->
            <rect x="40" y="280" width="420" height="15" fill="#1e293b" stroke="#475569" rx="3"/>

            <!-- Law Card -->
            <rect x="30" y="40" width="135" height="110" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="40" y="65" fill="#f59e0b" font-size="11" font-weight="bold">Fluid Law:</text>
            <text x="40" y="85" fill="#cbd5e1" font-size="10">At depth h = ${depthCm} cm:</text>
            <text x="40" y="105" fill="#38bdf8" font-size="13" font-weight="bold">P = ${hydroPressure} hPa</text>
            <text x="40" y="130" fill="#34d399" font-size="9">Equal in ALL directions!</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Water Column Height (h):</span>
          <input type="range" class="sim-slider" id="sliderWater" min="5" max="22" step="1" value="${depthCm}">
          <span class="control-value" id="valWater">${depthCm} cm</span>
        </div>
      `;

      document.getElementById('sliderWater').oninput = (e) => {
        depthCm = parseInt(e.target.value);
        document.getElementById('valWater').textContent = `${depthCm} cm`;
        updateSim();
      };

      updateSim();
    }

    // 4. DEPTH & DAM ARCHITECTURE SIMULATOR
    function simDepthDamArchitecture(canvas, controls, title, icon) {
      title.textContent = "Liquid Depth vs. Pressure: Dam Architecture";
      icon.textContent = "🌊";

      let viewMode = 'cylinder'; // 'cylinder' or 'dam'

      function updateSim() {
        if (viewMode === 'cylinder') {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- Tall Canister -->
              <rect x="80" y="50" width="90" height="210" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
              <rect x="82" y="55" width="86" height="200" fill="#0284c7" opacity="0.6"/>

              <!-- 3 Vertical Holes -->
              <!-- Hole A: Top (shallow) -->
              <circle cx="170" cy="90" r="4" fill="#fb7185"/>
              <path d="M 170 90 Q 210 90 230 260" fill="none" stroke="#fb7185" stroke-width="2.5"/>
              <text x="180" y="85" fill="#fb7185" font-size="10">Hole A: Low P (Short jet)</text>

              <!-- Hole B: Middle -->
              <circle cx="170" cy="160" r="4" fill="#facc15"/>
              <path d="M 170 160 Q 260 160 310 260" fill="none" stroke="#facc15" stroke-width="2.5"/>
              <text x="180" y="155" fill="#facc15" font-size="10">Hole B: Med P</text>

              <!-- Hole C: Deep bottom -->
              <circle cx="170" cy="230" r="4" fill="#34d399"/>
              <path d="M 170 230 Q 320 230 420 260" fill="none" stroke="#34d399" stroke-width="3"/>
              <text x="180" y="225" fill="#34d399" font-size="10" font-weight="bold">Hole C: High P (Furthest jet!)</text>

              <!-- Base ground -->
              <line x1="40" y1="260" x2="460" y2="260" stroke="#475569" stroke-width="3"/>
              
              <text x="250" y="295" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
                Liquid Pressure Formula: P = ρ · g · h (Increases linearly with depth)
              </text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- Reservoir Water on Left -->
              <polygon points="40,90 240,90 240,250 40,250" fill="#0284c7" opacity="0.6"/>
              <text x="120" y="120" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">Water Reservoir</text>

              <!-- Hydrostatic Pressure Triangle Vectors -->
              <line x1="230" y1="100" x2="200" y2="100" stroke="#facc15" stroke-width="2"/>
              <line x1="230" y1="150" x2="170" y2="150" stroke="#facc15" stroke-width="3"/>
              <line x1="230" y1="200" x2="130" y2="200" stroke="#facc15" stroke-width="4"/>
              <line x1="230" y1="240" x2="70" y2="240" stroke="#ef4444" stroke-width="6"/>
              <text x="140" y="230" fill="#fb7185" font-size="11" font-weight="bold">Massive Lateral Pressure at Base!</text>

              <!-- Trapezoidal Concrete Dam Cross-Section -->
              <!-- Narrow crest at top (240 to 270 = 30 wide), Broad base at bottom (240 to 420 = 180 wide) -->
              <polygon points="240,90 270,90 420,250 240,250" fill="#475569" stroke="#94a3b8" stroke-width="3"/>
              <line x1="240" y1="85" x2="270" y2="85" stroke="#38bdf8" stroke-width="2"/>
              <text x="255" y="78" fill="#38bdf8" font-size="10" text-anchor="middle">Narrow Top</text>

              <line x1="240" y1="265" x2="420" y2="265" stroke="#f59e0b" stroke-width="3"/>
              <text x="330" y="280" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Broad Reinforcement Base</text>

              <!-- Engineering Label -->
              <rect x="290" y="110" width="160" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="300" y="132" fill="#38bdf8" font-size="11" font-weight="bold">Dam Engineering Rule:</text>
              <text x="300" y="152" fill="#cbd5e1" font-size="9">• Water pressure = ρ·g·h</text>
              <text x="300" y="168" fill="#cbd5e1" font-size="9">• Peak load at reservoir floor</text>
              <text x="300" y="184" fill="#34d399" font-size="9">• Thick base resists shear burst</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${viewMode === 'cylinder' ? 'active' : ''}" id="btnCyl">🧪 3-Spout Cylinder Experiment</button>
          <button class="btn-sim ${viewMode === 'dam' ? 'active' : ''}" id="btnDam">🏗️ Hydroelectric Dam Architecture</button>
        </div>
      `;

      document.getElementById('btnCyl').onclick = () => {
        viewMode = 'cylinder';
        document.getElementById('btnCyl').classList.add('active');
        document.getElementById('btnDam').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnDam').onclick = () => {
        viewMode = 'dam';
        document.getElementById('btnDam').classList.add('active');
        document.getElementById('btnCyl').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 5. ATMOSPHERIC PRESSURE MERCURY BAROMETER SIMULATOR
    function simAtmosphericPressureMercury(canvas, controls, title, icon) {
      title.textContent = "Torricelli Barometer: Measuring 1013 hPa";
      icon.textContent = "🌡️";

      let altitudeM = 0;

      function updateSim() {
        // Barometric formula approx: P = 1013 * exp(-h/8400)
        const pressureHPa = Math.round(1013 * Math.exp(-altitudeM / 8400));
        const columnCm = (pressureHPa * 0.075).toFixed(1);
        const columnPx = Math.round(columnCm * 2.2);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Mercury Trough at Bottom -->
            <rect x="100" y="210" width="180" height="50" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
            <rect x="105" y="220" width="170" height="35" fill="#94a3b8" opacity="0.8"/>
            <text x="190" y="245" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">Liquid Mercury (Hg)</text>

            <!-- Atmospheric Pressure Arrows pressing down on trough -->
            <line x1="125" y1="180" x2="125" y2="215" stroke="#ef4444" stroke-width="3"/>
            <polygon points="121,210 125,220 129,210" fill="#ef4444"/>
            <line x1="255" y1="180" x2="255" y2="215" stroke="#ef4444" stroke-width="3"/>
            <polygon points="251,210 255,220 259,210" fill="#ef4444"/>
            <text x="190" y="195" fill="#fb7185" font-size="10" font-weight="bold" text-anchor="middle">P_atm pushes DOWN</text>

            <!-- Vertical Glass Tube -->
            <rect x="175" y="40" width="30" height="200" fill="rgba(255, 255, 255, 0.1)" stroke="#38bdf8" stroke-width="2" rx="2"/>
            
            <!-- Torricellian Vacuum Space at Top -->
            <rect x="177" y="42" width="26" height="${200 - columnPx}" fill="#0f172a"/>
            <text x="190" y="${50 + Math.max(10, (200 - columnPx)/2)}" fill="#38bdf8" font-size="8" text-anchor="middle">Vacuum</text>

            <!-- Mercury Column Inside Tube -->
            <rect x="177" y="${242 - columnPx}" width="26" height="${columnPx}" fill="#94a3b8"/>
            <line x1="210" y1="${242 - columnPx}" x2="235" y2="${242 - columnPx}" stroke="#facc15" stroke-width="2"/>
            <line x1="210" y1="242" x2="235" y2="242" stroke="#facc15" stroke-width="2"/>
            <line x1="230" y1="${242 - columnPx}" x2="230" y2="242" stroke="#facc15" stroke-width="1.5"/>
            <text x="240" y="${242 - columnPx/2}" fill="#facc15" font-size="11" font-weight="bold">${columnCm} cm Hg</text>

            <!-- Digital Readout Card -->
            <rect x="300" y="50" width="165" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="315" y="80" fill="#38bdf8" font-size="13" font-weight="bold">Atmosphere Gauge:</text>
            
            <text x="315" y="110" fill="#94a3b8" font-size="11">Current Altitude:</text>
            <text x="315" y="128" fill="#f8fafc" font-size="14" font-weight="bold">${altitudeM} metres</text>

            <text x="315" y="155" fill="#94a3b8" font-size="11">Barometric Pressure:</text>
            <text x="315" y="180" fill="#34d399" font-size="18" font-weight="800">${pressureHPa} hPa</text>
            <text x="315" y="196" fill="#cbd5e1" font-size="10">(= ${pressureHPa} mb)</text>

            <text x="315" y="225" fill="#f59e0b" font-size="10">
              ${altitudeM === 0 ? '🌊 Standard Sea Level (760 mm Hg)' : '🏔️ Thinner air aloft: Column falls!'}
            </text>
            <text x="315" y="250" fill="#94a3b8" font-size="9">1 hPa = 100 Pa = 100 N/m²</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Altitude Above Sea Level:</span>
          <input type="range" class="sim-slider" id="sliderAlt" min="0" max="4000" step="250" value="${altitudeM}">
          <span class="control-value" id="valAlt">${altitudeM} m</span>
        </div>
      `;

      document.getElementById('sliderAlt').oninput = (e) => {
        altitudeM = parseInt(e.target.value);
        document.getElementById('valAlt').textContent = `${altitudeM} m`;
        updateSim();
      };

      updateSim();
    }

    // 6. BODY FLUID PRESSURE EQUILIBRIUM SIMULATOR
    function simBodyFluidBalance(canvas, controls, title, icon) {
      title.textContent = "Body Fluid Pressure: High-Altitude Equilibrium";
      icon.textContent = "🫀";

      let altM = 0;

      function updateSim() {
        const pAtm = Math.round(101.3 * Math.exp(-altM / 8400));
        const pInternal = 101.3;
        const deltaP = (pInternal - pAtm).toFixed(1);
        const isDistended = (altM > 2500);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Human Capillary / Tissue Cross Section -->
            <g transform="translate(170, 150)">
              <!-- Capillary Tube Wall -->
              <ellipse cx="0" cy="0" rx="${55 + altM * 0.005}" ry="${55 + altM * 0.005}" fill="#450a0a" stroke="${isDistended ? '#f43f5e' : '#e11d48'}" stroke-width="${isDistended ? 5 : 3}"/>
              
              <!-- Blood Cells Flowing Inside -->
              <circle cx="-15" cy="-10" r="12" fill="#ef4444"/>
              <circle cx="18" cy="8" r="14" fill="#ef4444"/>
              <circle cx="0" cy="22" r="10" fill="#b91c1c"/>
              <text x="0" y="4" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Blood Vessel</text>

              <!-- Internal Pressure Arrows (Pointing Outwards) -->
              <line x1="-35" y1="0" x2="-55" y2="0" stroke="#facc15" stroke-width="3"/>
              <line x1="35" y1="0" x2="55" y2="0" stroke="#facc15" stroke-width="3"/>
              <line x1="0" y1="-35" x2="0" y2="-55" stroke="#facc15" stroke-width="3"/>
              <line x1="0" y1="35" x2="0" y2="55" stroke="#facc15" stroke-width="3"/>

              <!-- External Atmospheric Pressure Arrows (Pointing Inwards) -->
              <line x1="-85" y1="0" x2="${-60 - altM * 0.003}" y2="0" stroke="#38bdf8" stroke-width="${Math.max(1, pAtm * 0.04)}"/>
              <line x1="85" y1="0" x2="${60 + altM * 0.003}" y2="0" stroke="#38bdf8" stroke-width="${Math.max(1, pAtm * 0.04)}"/>
              <line x1="0" y1="-85" x2="0" y2="${-60 - altM * 0.003}" stroke="#38bdf8" stroke-width="${Math.max(1, pAtm * 0.04)}"/>
              <line x1="0" y1="85" x2="0" y2="${60 + altM * 0.003}" stroke="#38bdf8" stroke-width="${Math.max(1, pAtm * 0.04)}"/>
            </g>

            <!-- Physiological Status Panel -->
            <rect x="295" y="45" width="170" height="230" rx="10" fill="#1e293b" stroke="${isDistended ? '#f43f5e' : '#10b981'}" stroke-width="1.5"/>
            <text x="310" y="72" fill="#38bdf8" font-size="12" font-weight="bold">Altitude Equilibrium:</text>
            
            <text x="310" y="98" fill="#94a3b8" font-size="10">Elevation: <strong>${altM} m</strong></text>
            <text x="310" y="118" fill="#38bdf8" font-size="10">P_atm (Inward): <strong>${pAtm} kPa</strong></text>
            <text x="310" y="138" fill="#facc15" font-size="10">P_blood (Outward): <strong>${pInternal} kPa</strong></text>
            
            <line x1="310" y1="150" x2="450" y2="150" stroke="rgba(255,255,255,0.1)"/>
            <text x="310" y="170" fill="#cbd5e1" font-size="10">Net Outward Stress:</text>
            <text x="310" y="195" fill="${isDistended ? '#fb7185' : '#34d399'}" font-size="18" font-weight="800">+${deltaP} kPa</text>

            <text x="310" y="225" fill="#cbd5e1" font-size="9">
              ${isDistended ? '⚠️ Capillaries burst in delicate nasal mucosa: High altitude nosebleed!' : '⚖️ Balanced! Blood pressure exactly matches atmospheric envelope.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Ascent Altitude:</span>
          <input type="range" class="sim-slider" id="sliderBodyAlt" min="0" max="6000" step="500" value="${altM}">
          <span class="control-value" id="valBodyAlt">${altM} m</span>
        </div>
      `;

      document.getElementById('sliderBodyAlt').oninput = (e) => {
        altM = parseInt(e.target.value);
        document.getElementById('valBodyAlt').textContent = `${altM} m`;
        updateSim();
      };

      updateSim();
    }

    // 7. BERNOULLI EFFECT: BALLOONS & TIN ROOF LIFT SIMULATOR
    function simBernoulliBalloonsRoof(canvas, controls, title, icon) {
      title.textContent = "Wind Speed & Pressure Drop: Bernoulli's Principle";
      icon.textContent = "🎈";

      let windSpeed = 60; // km/h
      let simMode = 'balloons'; // 'balloons' or 'roof'

      function updateSim() {
        if (simMode === 'balloons') {
          const separation = Math.max(10, Math.round(90 - windSpeed * 0.7));
          const dropKPa = (windSpeed * 0.05).toFixed(1);

          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- Ceiling Support -->
              <line x1="80" y1="50" x2="320" y2="50" stroke="#64748b" stroke-width="4"/>
              
              <!-- Left Balloon -->
              <line x1="160" y1="50" x2="${200 - separation/2}" y2="150" stroke="#94a3b8" stroke-width="1.5"/>
              <circle cx="${200 - separation/2}" cy="160" r="32" fill="#ef4444" opacity="0.85"/>
              <text x="${200 - separation/2}" y="165" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">A</text>

              <!-- Right Balloon -->
              <line x1="240" y1="50" x2="${200 + separation/2}" y2="150" stroke="#94a3b8" stroke-width="1.5"/>
              <circle cx="${200 + separation/2}" cy="160" r="32" fill="#3b82f6" opacity="0.85"/>
              <text x="${200 + separation/2}" y="165" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">B</text>

              <!-- Wind Jet in between -->
              <line x1="200" y1="80" x2="200" y2="230" stroke="#38bdf8" stroke-width="${Math.max(2, windSpeed * 0.08)}" stroke-dasharray="6,4"/>
              <text x="200" y="250" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Air Blast: ${windSpeed} km/h</text>
              <text x="200" y="130" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Low P</text>

              <!-- Outer High Atmospheric Pressure Arrows -->
              <line x1="90" y1="160" x2="135" y2="160" stroke="#10b981" stroke-width="3"/>
              <polygon points="135,156 145,160 135,164" fill="#10b981"/>
              <text x="110" y="150" fill="#34d399" font-size="9">P_atm</text>

              <line x1="310" y1="160" x2="265" y2="160" stroke="#10b981" stroke-width="3"/>
              <polygon points="265,156 255,160 265,164" fill="#10b981"/>
              <text x="285" y="150" fill="#34d399" font-size="9">P_atm</text>

              <!-- Explanatory Box -->
              <rect x="330" y="50" width="135" height="220" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="340" y="75" fill="#38bdf8" font-size="11" font-weight="bold">Bernoulli Law:</text>
              <text x="340" y="100" fill="#cbd5e1" font-size="9">Fast air between balloons creates low pressure:</text>
              <text x="340" y="130" fill="#facc15" font-size="13" font-weight="bold">ΔP = -${dropKPa} kPa</text>
              <text x="340" y="160" fill="#cbd5e1" font-size="9">Outer atmospheric pressure pushes balloons together!</text>
              <text x="340" y="200" fill="#34d399" font-size="11" font-weight="bold">Balloons Collide!</text>
            </svg>
          `;
        } else {
          const liftPx = Math.min(45, Math.round(windSpeed * 0.45));
          const isBlownOff = (windSpeed > 80);

          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- House Walls -->
              <rect x="90" y="170" width="160" height="90" fill="#334155" stroke="#64748b" stroke-width="2"/>
              <rect x="150" y="200" width="40" height="60" fill="#1e293b"/>
              <text x="170" y="195" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Indoor P_atm (Calm)</text>

              <!-- Upward Force Arrows from Inside House -->
              <line x1="120" y1="170" x2="120" y2="135" stroke="#34d399" stroke-width="4"/>
              <line x1="220" y1="170" x2="220" y2="135" stroke="#34d399" stroke-width="4"/>

              <!-- Tin Roof (Lifting or Blown Away) -->
              <g transform="translate(${isBlownOff ? 40 : 0}, ${-liftPx}) rotate(${isBlownOff ? 15 : 0}, 170, 130)">
                <polygon points="70,170 170,110 270,170" fill="#b45309" stroke="#f59e0b" stroke-width="3"/>
                <text x="170" y="145" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Tin Roof</text>
              </g>

              <!-- Fast Gale Winds Rushing Over Roof -->
              <path d="M 40 100 Q 170 80 320 100" fill="none" stroke="#38bdf8" stroke-width="5" stroke-dasharray="10,5"/>
              <text x="170" y="70" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
                Gale Wind (${windSpeed} km/h) = LOW PRESSURE
              </text>

              <!-- Readout -->
              <rect x="300" y="50" width="165" height="220" rx="8" fill="#1e293b" stroke="${isBlownOff ? '#f43f5e' : '#38bdf8'}" stroke-width="1.5"/>
              <text x="315" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Storm Roof Lift:</text>
              <text x="315" y="110" fill="#cbd5e1" font-size="10">Speed above: <strong>${windSpeed} km/h</strong></text>
              <text x="315" y="135" fill="#facc15" font-size="10">Pressure above: <strong>REDUCED</strong></text>
              <text x="315" y="160" fill="#34d399" font-size="10">Pressure below: <strong>HIGH</strong></text>
              
              <text x="315" y="195" fill="${isBlownOff ? '#fb7185' : '#f59e0b'}" font-size="13" font-weight="bold">
                ${isBlownOff ? '💥 ROOF BLOWN OFF!' : '🔼 Net Upward Lift Force!'}
              </text>
              <text x="315" y="230" fill="#cbd5e1" font-size="9">Wind does NOT push down; internal pressure lifts roof!</text>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Wind Velocity:</span>
          <input type="range" class="sim-slider" id="sliderWind" min="0" max="120" step="5" value="${windSpeed}">
          <span class="control-value" id="valWind">${windSpeed} km/h</span>
        </div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
          <button class="btn-sim ${simMode === 'balloons' ? 'active' : ''}" id="btnBal">🎈 Two Suspended Balloons</button>
          <button class="btn-sim ${simMode === 'roof' ? 'active' : ''}" id="btnRoof">🏠 House Tin Roof in Storm</button>
        </div>
      `;

      document.getElementById('sliderWind').oninput = (e) => {
        windSpeed = parseInt(e.target.value);
        document.getElementById('valWind').textContent = `${windSpeed} km/h`;
        updateSim();
      };

      document.getElementById('btnBal').onclick = () => {
        simMode = 'balloons';
        document.getElementById('btnBal').classList.add('active');
        document.getElementById('btnRoof').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnRoof').onclick = () => {
        simMode = 'roof';
        document.getElementById('btnRoof').classList.add('active');
        document.getElementById('btnBal').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 8. PRESSURE GRADIENT & WIND GENERATION SIMULATOR
    function simPressureGradientWind(canvas, controls, title, icon) {
      title.textContent = "Pressure Gradient Force: Driving the Wind";
      icon.textContent = "💨";

      let deltaP = 24; // hPa difference

      function updateSim() {
        const windKmh = Math.round(deltaP * 3.8);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- High Pressure Region on Left -->
            <rect x="40" y="50" width="120" height="210" rx="8" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2"/>
            <text x="100" y="85" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">HIGH (H)</text>
            <text x="100" y="115" fill="#a7f3d0" font-size="18" font-weight="800" text-anchor="middle">${1008 + deltaP} hPa</text>
            <text x="100" y="145" fill="#cbd5e1" font-size="10" text-anchor="middle">Cool, Dense, Subsiding</text>

            <!-- Low Pressure Region on Right -->
            <rect x="340" y="50" width="120" height="210" rx="8" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="2"/>
            <text x="400" y="85" fill="#fb7185" font-size="14" font-weight="bold" text-anchor="middle">LOW (L)</text>
            <text x="400" y="115" fill="#fecdd3" font-size="18" font-weight="800" text-anchor="middle">1008 hPa</text>
            <text x="400" y="145" fill="#cbd5e1" font-size="10" text-anchor="middle">Warm, Rising Air</text>

            <!-- Central Wind Acceleration Pathway -->
            <line x1="165" y1="155" x2="335" y2="155" stroke="#38bdf8" stroke-width="${Math.max(3, deltaP * 0.3)}" stroke-dasharray="8,4"/>
            <polygon points="325,145 340,155 325,165" fill="#38bdf8"/>
            
            <text x="250" y="125" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">
              Pressure Gradient Force (PGF)
            </text>
            <text x="250" y="145" fill="#38bdf8" font-size="18" font-weight="800" text-anchor="middle">
              ${windKmh} km/h
            </text>
            <text x="250" y="180" fill="#94a3b8" font-size="10" text-anchor="middle">
              ΔP = ${deltaP} hPa across 100 km
            </text>

            <!-- Bottom Insight -->
            <rect x="40" y="270" width="420" height="25" rx="4" fill="#1e293b"/>
            <text x="250" y="287" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">
              Fundamental Rule: Air ALWAYS accelerates from HIGH pressure to LOW pressure!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Pressure Difference (ΔP):</span>
          <input type="range" class="sim-slider" id="sliderGrad" min="4" max="40" step="2" value="${deltaP}">
          <span class="control-value" id="valGrad">${deltaP} hPa</span>
        </div>
      `;

      document.getElementById('sliderGrad').oninput = (e) => {
        deltaP = parseInt(e.target.value);
        document.getElementById('valGrad').textContent = `${deltaP} hPa`;
        updateSim();
      };

      updateSim();
    }

    // 9. COASTAL LAND AND SEA BREEZE CYCLE SIMULATOR
    function simLandSeaBreezeCycle(canvas, controls, title, icon) {
      title.textContent = "Coastal Diurnal Breeze Cycle (Day vs. Night)";
      icon.textContent = "🏖️";

      let timeOfDay = 'day'; // 'day' or 'night'

      function updateSim() {
        const isDay = (timeOfDay === 'day');

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="${isDay ? '#0c2238' : '#030712'}" stroke="#38bdf8"/>
            
            <!-- Sun or Moon in Sky -->
            ${isDay ? `
              <circle cx="250" cy="55" r="20" fill="#facc15"/>
              <text x="250" y="90" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Daytime: Solar Heating</text>
            ` : `
              <circle cx="250" cy="55" r="16" fill="#cbd5e1"/>
              <text x="250" y="90" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Nighttime: Radiational Cooling</text>
            `}

            <!-- Coastal Land (Left Half) -->
            <path d="M 40 250 L 240 250 L 240 200 L 40 200 Z" fill="${isDay ? '#b45309' : '#334155'}"/>
            <text x="140" y="230" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">Land (Low Specific Heat)</text>
            <text x="140" y="246" fill="#facc15" font-size="11" text-anchor="middle">
              Temp: ${isDay ? '35°C (Rapid Heat)' : '18°C (Rapid Cool)'}
            </text>

            <!-- Ocean Sea (Right Half) -->
            <path d="M 240 250 L 460 250 L 460 200 L 240 200 Z" fill="#0284c7" opacity="0.75"/>
            <text x="350" y="230" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">Sea (High Specific Heat)</text>
            <text x="350" y="246" fill="#67e8f9" font-size="11" text-anchor="middle">
              Temp: ${isDay ? '26°C (Slow Heat)' : '25°C (Retains Heat)'}
            </text>

            <!-- Convection Circulation Loop -->
            ${isDay ? `
              <!-- Day: Warm air rises over Land, cool sea breeze blows Sea -> Land -->
              <line x1="140" y1="190" x2="140" y2="120" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,3"/>
              <polygon points="136,125 140,115 144,125" fill="#f43f5e"/>
              <text x="140" y="110" fill="#fb7185" font-size="9" font-weight="bold" text-anchor="middle">WARM AIR RISES (LOW P)</text>

              <!-- Sea Breeze blowing low level right to left -->
              <line x1="340" y1="180" x2="160" y2="180" stroke="#38bdf8" stroke-width="4"/>
              <polygon points="170,175 155,180 170,185" fill="#38bdf8"/>
              <text x="250" y="172" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">🌊 SEA BREEZE (Cool Air Inflow)</text>
            ` : `
              <!-- Night: Warm air rises over Sea, cool land breeze blows Land -> Sea -->
              <line x1="350" y1="190" x2="350" y2="120" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,3"/>
              <polygon points="346,125 350,115 354,125" fill="#f43f5e"/>
              <text x="350" y="110" fill="#fb7185" font-size="9" font-weight="bold" text-anchor="middle">WARM AIR RISES (LOW P)</text>

              <!-- Land Breeze blowing low level left to right -->
              <line x1="150" y1="180" x2="330" y2="180" stroke="#34d399" stroke-width="4"/>
              <polygon points="320,175 335,180 320,185" fill="#34d399"/>
              <text x="240" y="172" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">🍃 LAND BREEZE (Offshore Cool Wind)</text>
            `}

            <!-- Footer Badge -->
            <rect x="50" y="265" width="400" height="25" rx="4" fill="#1e293b"/>
            <text x="250" y="282" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">
              ${isDay ? 'Daytime Cycle: Sea Breeze keeps coastal stations cool during afternoons.' : 'Nighttime Cycle: Land Breeze flows offshore until sunrise.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${timeOfDay === 'day' ? 'active' : ''}" id="btnDay">☀️ Daytime: Sea Breeze</button>
          <button class="btn-sim ${timeOfDay === 'night' ? 'active' : ''}" id="btnNight">🌙 Nighttime: Land Breeze</button>
        </div>
      `;

      document.getElementById('btnDay').onclick = () => {
        timeOfDay = 'day';
        document.getElementById('btnDay').classList.add('active');
        document.getElementById('btnNight').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnNight').onclick = () => {
        timeOfDay = 'night';
        document.getElementById('btnNight').classList.add('active');
        document.getElementById('btnDay').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 10. STORM CONVECTION & CUMULONIMBUS CLOUD SIMULATOR
    function simStormConvectionCloud(canvas, controls, title, icon) {
      title.textContent = "Convection Updraft & Cumulonimbus Tower";
      icon.textContent = "⛈️";

      let groundTemp = 38; // °C

      function updateSim() {
        const updraftSpeed = Math.round((groundTemp - 20) * 1.8);
        const cloudHeight = Math.min(14, 6 + Math.round((groundTemp - 25) * 0.6));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0b1329" stroke="#38bdf8"/>
            
            <!-- Ground Level -->
            <rect x="40" y="250" width="420" height="30" fill="#78350f" stroke="#b45309"/>
            <text x="250" y="270" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">
              Sun-Baked Ground Surface (${groundTemp}°C)
            </text>

            <!-- Convective Thermal Updraft Arrows -->
            <line x1="200" y1="245" x2="200" y2="140" stroke="#ef4444" stroke-width="4" stroke-dasharray="6,3"/>
            <polygon points="196,145 200,135 204,145" fill="#ef4444"/>
            <line x1="230" y1="245" x2="230" y2="130" stroke="#f59e0b" stroke-width="5" stroke-dasharray="8,4"/>
            <polygon points="226,135 230,125 234,135" fill="#f59e0b"/>
            <text x="215" y="195" fill="#facc15" font-size="10" font-weight="bold">Thermal Updraft (${updraftSpeed} m/s)</text>

            <!-- Towering Cumulonimbus Cloud with Anvil Top -->
            <g transform="translate(180, 50)">
              <!-- Anvil Top at Tropopause -->
              <ellipse cx="60" cy="20" rx="150" ry="22" fill="#475569" opacity="0.9"/>
              <text x="60" y="24" fill="#e2e8f0" font-size="10" font-weight="bold" text-anchor="middle">Anvil Top (${cloudHeight} km - Tropopause)</text>

              <!-- Central Cloud Column -->
              <ellipse cx="60" cy="70" rx="70" ry="45" fill="#334155" opacity="0.95"/>
              <ellipse cx="30" cy="110" rx="55" ry="35" fill="#1e293b"/>
              <ellipse cx="90" cy="110" rx="60" ry="40" fill="#1e293b"/>
            </g>

            <!-- Cold Downdraft & Torrential Rain -->
            <line x1="280" y1="180" x2="280" y2="245" stroke="#38bdf8" stroke-width="4" stroke-dasharray="5,5"/>
            <polygon points="276,240 280,248 284,240" fill="#38bdf8"/>
            <text x="320" y="215" fill="#67e8f9" font-size="10" font-weight="bold">Cold Downdraft & Deluge</text>

            <!-- Scientific Metric Overlay -->
            <rect x="40" y="40" width="130" height="90" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="50" y="60" fill="#f59e0b" font-size="10" font-weight="bold">Genesis Metric:</text>
            <text x="50" y="80" fill="#cbd5e1" font-size="9">Updraft: <strong>${updraftSpeed} m/s</strong></text>
            <text x="50" y="98" fill="#cbd5e1" font-size="9">Altitude: <strong>${cloudHeight} km</strong></text>
            <text x="50" y="116" fill="#fb7185" font-size="9">Severity: ${groundTemp > 35 ? 'Severe Storm' : 'Moderate'}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Ground Surface Heat:</span>
          <input type="range" class="sim-slider" id="sliderHeat" min="25" max="45" step="1" value="${groundTemp}">
          <span class="control-value" id="valHeat">${groundTemp}°C</span>
        </div>
      `;

      document.getElementById('sliderHeat').oninput = (e) => {
        groundTemp = parseInt(e.target.value);
        document.getElementById('valHeat').textContent = `${groundTemp}°C`;
        updateSim();
      };

      updateSim();
    }

    // 11. LIGHTNING: CLOUD CHARGE & DIELECTRIC BREAKDOWN SIMULATOR
    function simLightningChargeBreakdown(canvas, controls, title, icon) {
      title.textContent = "Cloud Charge Separation & Lightning Discharge";
      icon.textContent = "⚡";

      let isDischarging = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="${isDischarging ? '#1e293b' : '#070b19'}" stroke="#38bdf8"/>
            
            <!-- Cumulonimbus Cloud Silhouette -->
            <ellipse cx="250" cy="80" rx="170" ry="45" fill="#334155" stroke="#64748b" stroke-width="2"/>
            
            <!-- Positive Charges (+) at Upper Cloud Top -->
            <g transform="translate(140, 55)">
              <text x="0" y="0" fill="#38bdf8" font-size="16" font-weight="800">+</text>
              <text x="50" y="-8" fill="#38bdf8" font-size="16" font-weight="800">+</text>
              <text x="110" y="-5" fill="#38bdf8" font-size="16" font-weight="800">+</text>
              <text x="170" y="2" fill="#38bdf8" font-size="16" font-weight="800">+</text>
              <text x="110" y="16" fill="#7dd3fc" font-size="9" text-anchor="middle">Light Ice Crystals (+)</text>
            </g>

            <!-- Negative Charges (-) at Lower Cloud Base -->
            <g transform="translate(140, 105)">
              <text x="10" y="0" fill="#f43f5e" font-size="20" font-weight="800">-</text>
              <text x="60" y="5" fill="#f43f5e" font-size="20" font-weight="800">-</text>
              <text x="120" y="2" fill="#f43f5e" font-size="20" font-weight="800">-</text>
              <text x="180" y="-2" fill="#f43f5e" font-size="20" font-weight="800">-</text>
              <text x="110" y="16" fill="#fca5a5" font-size="9" text-anchor="middle">Heavy Water Droplets / Graupel (-)</text>
            </g>

            <!-- Ground with Induced Positive Charge (+) -->
            <rect x="40" y="260" width="420" height="25" fill="#15803d"/>
            <g transform="translate(150, 255)">
              <text x="0" y="0" fill="#34d399" font-size="16" font-weight="800">+</text>
              <text x="60" y="0" fill="#34d399" font-size="16" font-weight="800">+</text>
              <text x="120" y="0" fill="#34d399" font-size="16" font-weight="800">+</text>
              <text x="180" y="0" fill="#34d399" font-size="16" font-weight="800">+</text>
            </g>
            <text x="250" y="278" fill="#dcfce7" font-size="10" font-weight="bold" text-anchor="middle">Induced Positive Ground Shadow (+)</text>

            <!-- Lightning Bolt Discharge -->
            ${isDischarging ? `
              <path d="M 250 115 L 235 150 L 260 175 L 240 215 L 265 235 L 250 260" 
                    fill="none" stroke="#facc15" stroke-width="5" stroke-linecap="round"/>
              <path d="M 250 115 L 235 150 L 260 175 L 240 215 L 265 235 L 250 260" 
                    fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
              <!-- Flashes -->
              <rect x="20" y="20" width="460" height="280" rx="12" fill="rgba(254, 240, 138, 0.25)"/>
              <text x="250" y="190" fill="#fff" font-size="16" font-weight="800" text-anchor="middle">
                ⚡ DIELECTRIC BREAKDOWN: 30,000°C RETURN STROKE!
              </text>
            ` : `
              <!-- Stepped leader initiating -->
              <line x1="250" y1="120" x2="245" y2="150" stroke="#facc15" stroke-width="2" stroke-dasharray="4,4"/>
              <text x="250" y="180" fill="#94a3b8" font-size="11" text-anchor="middle">
                Electric Field &gt; 3,000,000 V/m initiates air breakdown
              </text>
            `}
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isDischarging ? 'active' : ''}" id="btnDischarge">
          ${isDischarging ? '🔄 Reset Charges' : '⚡ Trigger Dielectric Breakdown (Lightning Stroke)'}
        </button>
      `;

      document.getElementById('btnDischarge').onclick = () => {
        isDischarging = !isDischarging;
        updateSim();
      };

      updateSim();
    }

    // 12. THUNDER SOUND & DISTANCE CALCULATOR SIMULATOR
    function simThunderSoundDistance(canvas, controls, title, icon) {
      title.textContent = "Supersonic Thunder Expansion & 3-Second Rule";
      icon.textContent = "⏱️";

      let delaySec = 6;

      function updateSim() {
        const distanceMetres = delaySec * 340;
        const distanceKm = (distanceMetres / 1000).toFixed(2);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Lightning Flash Location on Left -->
            <g transform="translate(80, 80)">
              <polygon points="0,0 -8,30 2,30 -6,65 14,25 4,25" fill="#facc15"/>
              <text x="0" y="85" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Lightning Flash</text>
              <text x="0" y="100" fill="#94a3b8" font-size="9" text-anchor="middle">Speed = 300,000 km/s</text>
              <text x="0" y="112" fill="#38bdf8" font-size="9" text-anchor="middle">(Instant Sight!)</text>
            </g>

            <!-- Expanding Acoustic Wavefronts -->
            <g transform="translate(80, 110)">
              <circle cx="0" cy="0" r="40" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
              <circle cx="0" cy="0" r="85" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
              <circle cx="0" cy="0" r="140" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="8,4"/>
            </g>

            <!-- Observer with Stopwatch on Right -->
            <g transform="translate(340, 180)">
              <!-- Human Figure -->
              <circle cx="0" cy="-30" r="12" fill="#f59e0b"/>
              <line x1="0" y1="-18" x2="0" y2="20" stroke="#f59e0b" stroke-width="4"/>
              <line x1="0" y1="20" x2="-12" y2="55" stroke="#f59e0b" stroke-width="4"/>
              <line x1="0" y1="20" x2="12" y2="55" stroke="#f59e0b" stroke-width="4"/>
              
              <!-- Stopwatch in Hand -->
              <rect x="15" y="-10" width="22" height="26" rx="4" fill="#1e293b" stroke="#38bdf8"/>
              <text x="26" y="8" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">${delaySec}s</text>
              <text x="0" y="75" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Student Observer</text>
            </g>

            <!-- Computational Card -->
            <rect x="160" y="40" width="160" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="170" y="65" fill="#38bdf8" font-size="11" font-weight="bold">Flash-to-Bang Calculus:</text>
            <text x="170" y="85" fill="#cbd5e1" font-size="10">Flash-to-Rumble Gap: <strong>${delaySec} s</strong></text>
            <text x="170" y="105" fill="#facc15" font-size="10">Distance = Time × 340 m/s</text>
            <text x="170" y="132" fill="#34d399" font-size="16" font-weight="800">${distanceKm} km away</text>

            <rect x="40" y="255" width="420" height="25" rx="4" fill="#1e293b"/>
            <text x="250" y="272" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">
              Quick Rule of Thumb: Every 3 seconds of delay ≈ 1 kilometre of storm distance!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Time Delay (Flash to Bang):</span>
          <input type="range" class="sim-slider" id="sliderDelay" min="1" max="15" step="1" value="${delaySec}">
          <span class="control-value" id="valDelay">${delaySec} seconds</span>
        </div>
      `;

      document.getElementById('sliderDelay').oninput = (e) => {
        delaySec = parseInt(e.target.value);
        document.getElementById('valDelay').textContent = `${delaySec} seconds`;
        updateSim();
      };

      updateSim();
    }

    // 13. LIGHTNING CONDUCTOR & EARTHING SIMULATOR
    function simLightningConductorEarthing(canvas, controls, title, icon) {
      title.textContent = "Lightning Rod Earthing & Human Lightning Crouch";
      icon.textContent = "🛡️";

      let stanceMode = 'conductor'; // 'conductor' or 'crouch'

      function updateSim() {
        if (stanceMode === 'conductor') {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- Multi-Story Building -->
              <rect x="150" y="100" width="160" height="150" fill="#334155" stroke="#475569" stroke-width="2"/>
              <!-- Windows -->
              <rect x="170" y="120" width="25" height="30" fill="#0284c7" opacity="0.7"/>
              <rect x="220" y="120" width="25" height="30" fill="#0284c7" opacity="0.7"/>
              <rect x="270" y="120" width="25" height="30" fill="#0284c7" opacity="0.7"/>
              <rect x="170" y="170" width="25" height="30" fill="#0284c7" opacity="0.7"/>
              <rect x="220" y="170" width="25" height="30" fill="#0284c7" opacity="0.7"/>
              <rect x="270" y="170" width="25" height="30" fill="#0284c7" opacity="0.7"/>

              <!-- Copper Spike Conductor on Roof -->
              <line x1="230" y1="100" x2="230" y2="50" stroke="#f59e0b" stroke-width="4"/>
              <polygon points="226,55 230,40 234,55" fill="#f59e0b"/>
              <text x="230" y="35" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Sharp Copper Spikes</text>

              <!-- Heavy Copper Grounding Strap along outer wall -->
              <path d="M 230 100 L 310 100 L 310 275" fill="none" stroke="#f59e0b" stroke-width="4"/>

              <!-- Buried Earthing Plate in Soil -->
              <rect x="280" y="275" width="60" height="12" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
              <text x="310" y="300" fill="#d97706" font-size="9" font-weight="bold" text-anchor="middle">Buried Metal Earthing Plate</text>

              <!-- Simulated Lightning Strike Diverted harmlessly -->
              <path d="M 230 40 L 230 100 L 310 100 L 310 275" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6,3"/>

              <!-- Explanatory Box -->
              <rect x="30" y="50" width="110" height="120" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
              <text x="40" y="75" fill="#34d399" font-size="10" font-weight="bold">Safety Principle:</text>
              <text x="40" y="95" fill="#cbd5e1" font-size="8">• Sharp points induce discharge</text>
              <text x="40" y="115" fill="#cbd5e1" font-size="8">• Pure copper: lowest resistance</text>
              <text x="40" y="135" fill="#cbd5e1" font-size="8">• Bypasses building structure safely into earth</text>
            </svg>
          `;
        } else {
          canvas.innerHTML = `
            <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
              <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
              
              <!-- Bad Stance: Under Tall Tree -->
              <g transform="translate(100, 240)">
                <!-- Tall Tree -->
                <rect x="15" y="-140" width="14" height="140" fill="#78350f"/>
                <circle cx="22" cy="-150" r="45" fill="#15803d" opacity="0.8"/>
                <text x="22" y="-200" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">❌ DEADLY: Under Tall Tree</text>

                <!-- Standing Person -->
                <circle cx="65" cy="-70" r="10" fill="#f87171"/>
                <line x1="65" y1="-60" x2="65" y2="-20" stroke="#f87171" stroke-width="4"/>
                <line x1="65" y1="-20" x2="55" y2="0" stroke="#f87171" stroke-width="4"/>
                <line x1="65" y1="-20" x2="75" y2="0" stroke="#f87171" stroke-width="4"/>
                <text x="65" y="15" fill="#fb7185" font-size="9" text-anchor="middle">Side Flashover!</text>
              </g>

              <!-- Good Stance: Lightning Crouch in Open Ground -->
              <g transform="translate(340, 240)">
                <!-- Squatting Silhouette -->
                <circle cx="0" cy="-35" r="10" fill="#34d399"/>
                <!-- Body tucked low -->
                <ellipse cx="0" cy="-18" rx="14" ry="12" fill="#10b981"/>
                <!-- Heels touching -->
                <circle cx="-4" cy="0" r="4" fill="#34d399"/>
                <circle cx="4" cy="0" r="4" fill="#34d399"/>
                <text x="0" y="-55" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">✔ SAFE: Lightning Crouch</text>
                <text x="0" y="18" fill="#a7f3d0" font-size="9" text-anchor="middle">Squat low, heels together</text>
                <text x="0" y="30" fill="#a7f3d0" font-size="9" text-anchor="middle">Hands over ears, tuck head</text>
              </g>

              <line x1="30" y1="240" x2="470" y2="240" stroke="#475569" stroke-width="2"/>
            </svg>
          `;
        }
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${stanceMode === 'conductor' ? 'active' : ''}" id="btnRod">🏛️ Building Lightning Conductor Rod</button>
          <button class="btn-sim ${stanceMode === 'crouch' ? 'active' : ''}" id="btnCrouch">🏃 Outdoors: Lightning Crouch Stance</button>
        </div>
      `;

      document.getElementById('btnRod').onclick = () => {
        stanceMode = 'conductor';
        document.getElementById('btnRod').classList.add('active');
        document.getElementById('btnCrouch').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnCrouch').onclick = () => {
        stanceMode = 'crouch';
        document.getElementById('btnCrouch').classList.add('active');
        document.getElementById('btnRod').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 14. CYCLONE GENESIS & CORIOLIS VORTEX SIMULATOR
    function simCycloneVortexCoriolis(canvas, controls, title, icon) {
      title.textContent = "Cyclone Genesis: Warm Ocean & Coriolis Vorticity";
      icon.textContent = "🌀";

      let seaTemp = 28; // °C
      let hemisphere = 'north'; // 'north' or 'south'

      function updateSim() {
        const isFavorable = (seaTemp >= 26.5);
        const spinDirection = (hemisphere === 'north') ? 'Counter-Clockwise ↺' : 'Clockwise ↻';

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#091322" stroke="#38bdf8"/>
            
            <!-- Warm Ocean Surface -->
            <rect x="40" y="210" width="420" height="70" fill="rgba(2, 132, 199, 0.4)"/>
            <line x1="40" y1="210" x2="460" y2="210" stroke="#38bdf8" stroke-width="2"/>
            <text x="250" y="235" fill="#67e8f9" font-size="12" font-weight="bold" text-anchor="middle">
              Tropical Ocean Surface: ${seaTemp}°C (Threshold: &gt; 26.5°C)
            </text>

            <!-- Massive Moisture Evaporation & Latent Heat Chimney -->
            <line x1="180" y1="205" x2="180" y2="120" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
            <line x1="250" y1="205" x2="250" y2="90" stroke="#ef4444" stroke-width="4" stroke-dasharray="5,3"/>
            <line x1="320" y1="205" x2="320" y2="120" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4"/>
            <text x="250" y="160" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Latent Heat Release Fuels Low Core</text>

            <!-- Coriolis Deflection Spiral Vortex -->
            <g transform="translate(250, 100)">
              <circle cx="0" cy="0" r="22" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
              <text x="0" y="4" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">EYE</text>

              <!-- Spiral Arms -->
              <path d="M 0 -22 C 30 -40 70 -20 80 20 C 85 45 60 70 20 80" fill="none" stroke="#38bdf8" stroke-width="3"/>
              <path d="M 0 22 C -30 40 -70 20 -80 -20 C -85 -45 -60 -70 -20 -80" fill="none" stroke="#38bdf8" stroke-width="3"/>
            </g>

            <!-- Status Banner -->
            <rect x="50" y="40" width="170" height="60" rx="8" fill="#1e293b" stroke="${isFavorable ? '#10b981' : '#f43f5e'}" stroke-width="1.5"/>
            <text x="60" y="62" fill="#38bdf8" font-size="10" font-weight="bold">Thermal Status:</text>
            <text x="60" y="82" fill="${isFavorable ? '#34d399' : '#fb7185'}" font-size="11" font-weight="bold">
              ${isFavorable ? '✔ Cyclone Formation Possible!' : '✖ Too Cool (&lt; 26.5°C)'}
            </text>

            <rect x="290" y="40" width="165" height="60" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="300" y="62" fill="#f59e0b" font-size="10" font-weight="bold">Coriolis Rotation:</text>
            <text x="300" y="82" fill="#f8fafc" font-size="11" font-weight="bold">${spinDirection}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Sea Surface Temperature:</span>
          <input type="range" class="sim-slider" id="sliderSST" min="24" max="31" step="0.5" value="${seaTemp}">
          <span class="control-value" id="valSST">${seaTemp}°C</span>
        </div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.25rem;">
          <button class="btn-sim ${hemisphere === 'north' ? 'active' : ''}" id="btnNorth">🌐 Northern Hemisphere (Counter-Clockwise)</button>
          <button class="btn-sim ${hemisphere === 'south' ? 'active' : ''}" id="btnSouth">🌐 Southern Hemisphere (Clockwise)</button>
        </div>
      `;

      document.getElementById('sliderSST').oninput = (e) => {
        seaTemp = parseFloat(e.target.value);
        document.getElementById('valSST').textContent = `${seaTemp}°C`;
        updateSim();
      };

      document.getElementById('btnNorth').onclick = () => {
        hemisphere = 'north';
        document.getElementById('btnNorth').classList.add('active');
        document.getElementById('btnSouth').classList.remove('active');
        updateSim();
      };

      document.getElementById('btnSouth').onclick = () => {
        hemisphere = 'south';
        document.getElementById('btnSouth').classList.add('active');
        document.getElementById('btnNorth').classList.remove('active');
        updateSim();
      };

      updateSim();
    }

    // 15. CYCLONE ANATOMY: CALM EYE & STORM SURGE SIMULATOR
    function simCycloneEyeStormSurge(canvas, controls, title, icon) {
      title.textContent = "Cyclone Anatomy: The Calm Eye & 6m Storm Surge";
      icon.textContent = "🌊";

      let surgeM = 6;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#07111e" stroke="#38bdf8"/>
            
            <!-- Atmospheric Cross Section of Mature Tropical Cyclone -->
            <!-- Eyewall Clouds on Left & Right of Center -->
            <ellipse cx="140" cy="110" rx="60" ry="70" fill="#334155" opacity="0.95"/>
            <ellipse cx="320" cy="110" rx="60" ry="70" fill="#334155" opacity="0.95"/>
            <text x="140" y="80" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">EYEWALL</text>
            <text x="140" y="95" fill="#fca5a5" font-size="8" text-anchor="middle">&gt; 200 km/h Gales</text>

            <text x="320" y="80" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">EYEWALL</text>
            <text x="320" y="95" fill="#fca5a5" font-size="8" text-anchor="middle">Maximum Destruction</text>

            <!-- Central Eye (Calm & Clear) -->
            <rect x="200" y="40" width="60" height="150" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,2"/>
            <text x="230" y="85" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">THE EYE</text>
            <text x="230" y="105" fill="#cbd5e1" font-size="8" text-anchor="middle">20-50 km wide</text>
            <text x="230" y="120" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Calm Winds</text>
            <text x="230" y="135" fill="#fbbf24" font-size="8" text-anchor="middle">Lowest P (920 hPa)</text>

            <!-- Ocean Basin & Storm Surge Inundation -->
            <rect x="40" y="220" width="260" height="60" fill="#0284c7" opacity="0.6"/>
            <text x="120" y="245" fill="#67e8f9" font-size="10">Normal Sea Level</text>

            <!-- Coastal Land with Storm Surge Wall -->
            <polygon points="300,220 300,${220 - surgeM * 7} 460,${220 - surgeM * 7} 460,280 300,280" fill="#0369a1" opacity="0.85"/>
            <line x1="300" y1="${220 - surgeM * 7}" x2="460" y2="${220 - surgeM * 7}" stroke="#ef4444" stroke-width="3"/>
            
            <text x="380" y="${205 - surgeM * 7}" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">
              🌊 ${surgeM}m Storm Surge Wall Overrunning Coast!
            </text>

            <!-- Inundated Houses -->
            <polygon points="360,${220 - surgeM * 4} 380,${195 - surgeM * 4} 400,${220 - surgeM * 4}" fill="#78350f"/>
            <rect x="365" y="${220 - surgeM * 4}" width="30" height="20" fill="#451a03"/>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Storm Surge Height:</span>
          <input type="range" class="sim-slider" id="sliderSurge" min="2" max="10" step="1" value="${surgeM}">
          <span class="control-value" id="valSurge">${surgeM} metres</span>
        </div>
      `;

      document.getElementById('sliderSurge').oninput = (e) => {
        surgeM = parseInt(e.target.value);
        document.getElementById('valSurge').textContent = `${surgeM} metres`;
        updateSim();
      };

      updateSim();
    }

    // 16. IMD SATELLITE RADAR TRACKING & SHELTERS SIMULATOR
    function simImdSatelliteTracking(canvas, controls, title, icon) {
      title.textContent = "IMD Early Warning & Disaster Shelters";
      icon.textContent = "🛰️";

      let warningStage = 3; // 1 to 4

      const STAGES = {
        1: { name: "Stage 1: Pre-Cyclone Watch", color: "#38bdf8", time: "72 hrs prior", action: "Fishermen advised not to venture into deep sea" },
        2: { name: "Stage 2: Cyclone Alert (Yellow)", color: "#facc15", time: "48 hrs prior", action: "Disaster machinery alerted, target districts identified" },
        3: { name: "Stage 3: Cyclone Warning (Orange)", color: "#fb923c", time: "24 hrs prior", action: "Evacuation of coastal kutcha houses to concrete shelters" },
        4: { name: "Stage 4: Post-Landfall Outlook (Red)", color: "#f43f5e", time: "12 hrs prior & Landfall", action: "Total suspension of road/rail traffic, emergency NDRF relief" }
      };

      function updateSim() {
        const stage = STAGES[warningStage];

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0a1424" stroke="#38bdf8"/>
            
            <!-- Map Outline: Eastern India Coast (Odisha & West Bengal) -->
            <path d="M 60 40 Q 120 120 180 200 Q 230 250 250 280 L 40 280 L 40 40 Z" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <text x="110" y="150" fill="#94a3b8" font-size="12" font-weight="bold">Indian Coast</text>
            <text x="110" y="168" fill="#64748b" font-size="9">Odisha / W. Bengal</text>

            <!-- Bay of Bengal Waters on Right -->
            <rect x="250" y="40" width="210" height="240" fill="rgba(2, 132, 199, 0.2)"/>
            <text x="350" y="70" fill="#0284c7" font-size="12" font-weight="bold" text-anchor="middle">Bay of Bengal</text>

            <!-- Cyclone Position along track -->
            <g transform="translate(${380 - warningStage * 45}, ${110 + warningStage * 25})">
              <!-- Doppler Radar Reflectivity concentric rings -->
              <circle cx="0" cy="0" r="35" fill="none" stroke="${stage.color}" stroke-width="2" stroke-dasharray="5,3"/>
              <circle cx="0" cy="0" r="18" fill="rgba(239, 68, 68, 0.3)" stroke="#ef4444" stroke-width="2"/>
              <text x="0" y="4" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">AMPHAN</text>
            </g>

            <!-- Reinforced Cyclone Shelter on Coast -->
            <g transform="translate(140, 210)">
              <!-- Concrete Pillars -->
              <rect x="0" y="20" width="8" height="25" fill="#94a3b8"/>
              <rect x="32" y="20" width="8" height="25" fill="#94a3b8"/>
              <!-- Elevated Platform -->
              <rect x="-5" y="0" width="50" height="20" fill="#10b981" rx="3"/>
              <text x="20" y="13" fill="#064e3b" font-size="8" font-weight="bold" text-anchor="middle">SHELTER</text>
            </g>

            <!-- IMD Warning Status Bulletin -->
            <rect x="230" y="170" width="220" height="105" rx="8" fill="#0f172a" stroke="${stage.color}" stroke-width="2"/>
            <text x="240" y="192" fill="${stage.color}" font-size="12" font-weight="bold">${stage.name}</text>
            <text x="240" y="210" fill="#cbd5e1" font-size="10">Lead Time: <strong>${stage.time}</strong></text>
            <text x="240" y="230" fill="#cbd5e1" font-size="9">Protocol:</text>
            <text x="240" y="248" fill="#e2e8f0" font-size="9">${stage.action}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">IMD 4-Stage Warning Protocol:</span>
          <input type="range" class="sim-slider" id="sliderStage" min="1" max="4" step="1" value="${warningStage}">
          <span class="control-value" id="valStage">Stage ${warningStage}</span>
        </div>
      `;

      document.getElementById('sliderStage').oninput = (e) => {
        warningStage = parseInt(e.target.value);
        document.getElementById('valStage').textContent = `Stage ${warningStage}`;
        updateSim();
      };

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-pressure-winds.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

