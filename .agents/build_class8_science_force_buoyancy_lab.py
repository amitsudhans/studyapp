# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-force-buoyancy.html
Class 8 Science - Chapter 5: Force, Types of Forces, Weight, and Buoyancy
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
from class8_science_force_buoyancy_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 5: Force, Types of Forces & Buoyancy Master Lab</title>
  
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
        radial-gradient(circle at 20% 25%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 80% 75%, rgba(16, 185, 129, 0.1) 0%, transparent 40%),
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
      border-radius: 10px;
      background: linear-gradient(135deg, #38bdf8, #10b981);
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
      background: linear-gradient(135deg, #38bdf8, #10b981);
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
      <div class="lab-icon">⚖️</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 5</div>
        <h1>Force, Types of Forces & Buoyancy</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Defining Force & Interaction</span>
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
        <span class="avatar-name">Sir Isaac • Virtual Mentor</span>
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
          <span class="slide-tag" id="slideBadge">Definition & Interaction</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Defining Force & Interaction</h2>

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
            <span id="simIcon">⚖️</span>
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
        chip.innerHTML = `<span class="vocab-word">⚖️ ${item.word}:</span><span class="vocab-def">${item.definition}</span>`;
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
        case 'force_interaction_sim':
          simForceInteraction(canvas, controls, title, icon);
          break;
        case 'effects_of_force_sim':
          simEffectsOfForce(canvas, controls, title, icon);
          break;
        case 'contact_noncontact_sorter_sim':
          simContactNoncontactSorter(canvas, controls, title, icon);
          break;
        case 'muscular_force_sim':
          simMuscularForce(canvas, controls, title, icon);
          break;
        case 'friction_microscopic_sim':
          simFrictionMicroscopic(canvas, controls, title, icon);
          break;
        case 'fluid_drag_streamlining_sim':
          simFluidDragStreamlining(canvas, controls, title, icon);
          break;
        case 'magnetic_force_poles_sim':
          simMagneticForcePoles(canvas, controls, title, icon);
          break;
        case 'electrostatic_charge_sim':
          simElectrostaticCharge(canvas, controls, title, icon);
          break;
        case 'gravitational_pull_sim':
          simGravitationalPull(canvas, controls, title, icon);
          break;
        case 'mass_vs_weight_sim':
          simMassVsWeight(canvas, controls, title, icon);
          break;
        case 'spring_balance_sim':
          simSpringBalance(canvas, controls, title, icon);
          break;
        case 'liquid_upthrust_sim':
          simLiquidUpthrust(canvas, controls, title, icon);
          break;
        case 'floating_sinking_sim':
          simFloatingSinking(canvas, controls, title, icon);
          break;
        case 'archimedes_principle_sim':
          simArchimedesPrinciple(canvas, controls, title, icon);
          break;
        case 'ship_submarine_density_sim':
          simShipSubmarineDensity(canvas, controls, title, icon);
          break;
        case 'force_matrix_synthesis_sim':
          simForceMatrixSynthesis(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = `<div style="color: #94a3b8;">Simulator ready.</div>`;
      }
    }

    // 1. FORCE & INTERACTION SIMULATOR
    function simForceInteraction(canvas, controls, title, icon) {
      title.textContent = "Two-Body Force Interaction Lab";
      icon.textContent = "🤝";

      let isTouching = true;
      let forceMag = 30; // Newtons

      function updateSim() {
        const cartX = isTouching ? 230 : 270;
        const arrowLen = isTouching ? forceMag * 2 : 0;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <!-- Ground Level -->
            <line x1="20" y1="240" x2="480" y2="240" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
            <rect x="20" y="242" width="460" height="20" fill="#1e293b"/>

            <!-- Person Figure (Pusher) -->
            <g transform="translate(130, 150)">
              <!-- Head -->
              <circle cx="0" cy="0" r="14" fill="#f59e0b"/>
              <!-- Torso leaning -->
              <line x1="0" y1="14" x2="${isTouching ? 15 : 0}" y2="55" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
              <!-- Arms pushing / resting -->
              <line x1="${isTouching ? 8 : 0}" y1="25" x2="${isTouching ? 55 : 20}" y2="${isTouching ? 30 : 45}" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
              <!-- Legs -->
              <line x1="${isTouching ? 15 : 0}" y1="55" x2="-15" y2="90" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
              <line x1="${isTouching ? 15 : 0}" y1="55" x2="25" y2="90" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
              <text x="0" y="105" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Person (Agent)</text>
            </g>

            <!-- Heavy Cart (Receiver Object) -->
            <g transform="translate(${cartX}, 135)">
              <rect x="0" y="0" width="130" height="80" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="65" y="45" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">Heavy Cart (50 kg)</text>
              <!-- Wheels -->
              <circle cx="25" cy="90" r="15" fill="#334155" stroke="#94a3b8" stroke-width="3"/>
              <circle cx="105" cy="90" r="15" fill="#334155" stroke="#94a3b8" stroke-width="3"/>
            </g>

            <!-- Applied Force Vector Arrow -->
            ${isTouching && forceMag > 0 ? `
              <g transform="translate(195, 165)">
                <line x1="0" y1="0" x2="${arrowLen}" y2="0" stroke="#10b981" stroke-width="5" stroke-linecap="round"/>
                <polygon points="${arrowLen}, -6 ${arrowLen + 12}, 0 ${arrowLen}, 6" fill="#10b981"/>
                <text x="${arrowLen / 2}" y="-12" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">
                  F = +${forceMag} N (Push)
                </text>
              </g>
            ` : ''}

            <!-- Status Banner -->
            <rect x="30" y="30" width="440" height="40" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="250" y="55" fill="${isTouching ? '#34d399' : '#f43f5e'}" font-size="12" font-weight="bold" text-anchor="middle">
              ${isTouching ? `✔ Interaction Active: Person pushes Cart with ${forceMag} N force!` : '✖ No Physical Interaction: Distance = 1 meter • Net Force = 0 N (Cart at Rest)'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button class="btn-sim ${isTouching ? 'active' : ''}" id="btnInteract">
            ${isTouching ? '🚶 Step Away (Zero Contact)' : '🤝 Make Contact & Push Cart'}
          </button>
        </div>
        <div class="control-row" style="margin-top: 0.5rem;">
          <span class="control-label">Pushing Force (N):</span>
          <input type="range" class="sim-slider" id="sliderForce" min="10" max="80" step="5" value="${forceMag}">
          <span class="control-value" id="valForce">${forceMag} N</span>
        </div>
      `;

      document.getElementById('btnInteract').onclick = () => {
        isTouching = !isTouching;
        document.getElementById('btnInteract').classList.toggle('active', isTouching);
        document.getElementById('btnInteract').textContent = isTouching ? '🚶 Step Away (Zero Contact)' : '🤝 Make Contact & Push Cart';
        updateSim();
      };

      document.getElementById('sliderForce').oninput = (e) => {
        forceMag = parseInt(e.target.value);
        document.getElementById('valForce').textContent = `${forceMag} N`;
        updateSim();
      };

      updateSim();
    }

    // 2. FOUR EFFECTS OF FORCE SIMULATOR
    function simEffectsOfForce(canvas, controls, title, icon) {
      title.textContent = "The Four Observable Effects of Force";
      icon.textContent = "⚽";

      let effectMode = 1; // 1: Move from Rest, 2: Speed Up/Down, 3: Change Direction, 4: Change Shape

      function updateSim() {
        let contentHtml = '';

        if (effectMode === 1) {
          // Effect 1: Rest to Motion
          contentHtml = `
            <g transform="translate(120, 160)">
              <circle cx="0" cy="0" r="28" fill="#f59e0b" stroke="#fff" stroke-width="2"/>
              <text x="0" y="5" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">Soccer Ball</text>
              <line x1="35" y1="0" x2="160" y2="0" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,4"/>
              <polygon points="160,-6 172,0 160,6" fill="#38bdf8"/>
            </g>
            <text x="250" y="240" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">
              Effect 1: A forward kick accelerates the ball from Rest ($v=0$) to Motion ($v=15\\text{ m/s}$)!
            </text>
          `;
        } else if (effectMode === 2) {
          // Effect 2: Speed Change
          contentHtml = `
            <g transform="translate(250, 150)">
              <rect x="-80" y="-30" width="160" height="60" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="0" y="5" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">Bicycle (Moving)</text>
              <line x1="-120" y1="0" x2="-85" y2="0" stroke="#10b981" stroke-width="6"/>
              <polygon points="-85,-7 -70,0 -85,7" fill="#10b981"/>
              <text x="-105" y="-14" fill="#34d399" font-size="11" font-weight="bold">Push: Speed Up</text>
              <line x1="85" y1="0" x2="120" y2="0" stroke="#f43f5e" stroke-width="6"/>
              <polygon points="85,-7 70,0 85,7" fill="#f43f5e"/>
              <text x="105" y="-14" fill="#fb7185" font-size="11" font-weight="bold">Brake: Slow Down</text>
            </g>
            <text x="250" y="240" fill="#cbd5e1" font-size="13" font-weight="bold" text-anchor="middle">
              Effect 2: Force in motion direction speeds up; force opposite slows down or halts motion.
            </text>
          `;
        } else if (effectMode === 3) {
          // Effect 3: Direction Change
          contentHtml = `
            <g transform="translate(100, 160)">
              <circle cx="0" cy="0" r="16" fill="#ef4444"/>
              <path d="M 0 0 L 150 0 L 250 -60" fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="4,4"/>
              <polygon points="250,-60 235,-55 240,-70" fill="#f59e0b"/>
              <!-- Cricket Bat Surface -->
              <rect x="145" y="-30" width="12" height="60" rx="2" fill="#b45309" stroke="#f59e0b" transform="rotate(25 150 0)"/>
            </g>
            <text x="250" y="240" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">
              Effect 3: Cricket bat strikes incoming ball, changing its trajectory angle across the field!
            </text>
          `;
        } else {
          // Effect 4: Shape Change
          contentHtml = `
            <g transform="translate(250, 150)">
              <!-- Squeezed Sponge -->
              <ellipse cx="0" cy="0" rx="80" ry="25" fill="#facc15" stroke="#ca8a04" stroke-width="3"/>
              <text x="0" y="5" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">Deformed Rubber Sponge</text>
              <!-- Opposing Hands Compression -->
              <line x1="0" y1="-65" x2="0" y2="-30" stroke="#ef4444" stroke-width="6"/>
              <polygon points="-7,-30 0,-18 7,-30" fill="#ef4444"/>
              <line x1="0" y1="65" x2="0" y2="30" stroke="#ef4444" stroke-width="6"/>
              <polygon points="-7,30 0,18 7,30" fill="#ef4444"/>
            </g>
            <text x="250" y="240" fill="#facc15" font-size="13" font-weight="bold" text-anchor="middle">
              Effect 4: Compressive force squashes the sponge, altering its physical shape and volume.
            </text>
          `;
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#334155" stroke-width="2"/>
            ${contentHtml}
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
          <button class="btn-sim ${effectMode === 1 ? 'active' : ''}" id="btnE1">1. Rest to Motion</button>
          <button class="btn-sim ${effectMode === 2 ? 'active' : ''}" id="btnE2">2. Change Speed</button>
          <button class="btn-sim ${effectMode === 3 ? 'active' : ''}" id="btnE3">3. Change Direction</button>
          <button class="btn-sim ${effectMode === 4 ? 'active' : ''}" id="btnE4">4. Change Shape</button>
        </div>
      `;

      document.getElementById('btnE1').onclick = () => { effectMode = 1; updateBtnStates(); updateSim(); };
      document.getElementById('btnE2').onclick = () => { effectMode = 2; updateBtnStates(); updateSim(); };
      document.getElementById('btnE3').onclick = () => { effectMode = 3; updateBtnStates(); updateSim(); };
      document.getElementById('btnE4').onclick = () => { effectMode = 4; updateBtnStates(); updateSim(); };

      function updateBtnStates() {
        document.getElementById('btnE1').classList.toggle('active', effectMode === 1);
        document.getElementById('btnE2').classList.toggle('active', effectMode === 2);
        document.getElementById('btnE3').classList.toggle('active', effectMode === 3);
        document.getElementById('btnE4').classList.toggle('active', effectMode === 4);
      }

      updateSim();
    }

    // 3. CONTACT VS NON-CONTACT SORTER SIMULATOR
    function simContactNoncontactSorter(canvas, controls, title, icon) {
      title.textContent = "Contact vs. Non-Contact Distance Tester";
      icon.textContent = "🔍";

      let dist = 80; // Distance in mm

      function updateSim() {
        const isTouching = dist <= 10;
        const magForce = Math.round(5000 / (dist * dist));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#334155"/>
            
            <!-- Left Fixed Magnet -->
            <g transform="translate(120, 140)">
              <rect x="-60" y="-35" width="60" height="70" fill="#ef4444" rx="4"/>
              <text x="-30" y="8" fill="#fff" font-weight="bold" font-size="18" text-anchor="middle">N</text>
              <rect x="0" y="-35" width="60" height="70" fill="#0284c7" rx="4"/>
              <text x="30" y="8" fill="#fff" font-weight="bold" font-size="18" text-anchor="middle">S</text>
              <text x="0" y="55" fill="#cbd5e1" font-size="11" text-anchor="middle">Magnet A</text>
            </g>

            <!-- Right Movable Iron Block -->
            <g transform="translate(${180 + dist * 2}, 140)">
              <rect x="0" y="-35" width="70" height="70" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2" rx="4"/>
              <text x="35" y="8" fill="#0f172a" font-weight="bold" font-size="13" text-anchor="middle">Iron Block</text>
            </g>

            <!-- Invisible Magnetic Force Lines -->
            <g stroke="#38bdf8" stroke-width="${Math.min(5, magForce * 0.4)}" stroke-dasharray="4,4">
              <line x1="180" y1="125" x2="${180 + dist * 2}" y2="125" opacity="0.8"/>
              <line x1="180" y1="140" x2="${180 + dist * 2}" y2="140" opacity="0.9"/>
              <line x1="180" y1="155" x2="${180 + dist * 2}" y2="155" opacity="0.8"/>
            </g>

            <!-- Data Callout -->
            <rect x="40" y="220" width="420" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="60" y="245" fill="#cbd5e1" font-size="12">
              Separation Gap: <strong>${dist} mm</strong> | Physical Contact: <strong>${isTouching ? 'YES (Surfaces Touch)' : 'NO (Empty Space)'}</strong>
            </text>
            <text x="60" y="265" fill="#38bdf8" font-size="13" font-weight="bold">
              Magnetic Force (Non-Contact): ${magForce} N • Acts directly through empty space!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Distance Gap (mm):</span>
          <input type="range" class="sim-slider" id="sliderDist" min="5" max="100" step="5" value="${dist}">
          <span class="control-value" id="valDist">${dist} mm</span>
        </div>
      `;

      document.getElementById('sliderDist').oninput = (e) => {
        dist = parseInt(e.target.value);
        document.getElementById('valDist').textContent = `${dist} mm`;
        updateSim();
      };

      updateSim();
    }

    // 4. MUSCULAR FORCE & ANATOMY SIMULATOR
    function simMuscularForce(canvas, controls, title, icon) {
      title.textContent = "Muscular Force: External Labor & Internal Organs";
      icon.textContent = "💪";

      let organView = 'arm'; // 'arm', 'heart', 'peristalsis'

      function updateSim() {
        let viewHtml = '';

        if (organView === 'arm') {
          viewHtml = `
            <g transform="translate(200, 150)">
              <!-- Arm Bones & Biceps Contraction -->
              <line x1="-80" y1="40" x2="0" y2="40" stroke="#cbd5e1" stroke-width="10" stroke-linecap="round"/>
              <line x1="0" y1="40" x2="60" y2="-30" stroke="#cbd5e1" stroke-width="10" stroke-linecap="round"/>
              <!-- Swollen Biceps Muscle -->
              <ellipse cx="25" cy="0" rx="35" ry="18" fill="#ef4444" stroke="#f8fafc" stroke-width="2"/>
              <text x="25" y="4" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Biceps Muscle</text>
              <!-- Heavy Dumbbell in Hand -->
              <rect x="55" y="-55" width="25" height="15" fill="#334155" rx="2"/>
              <text x="68" y="-60" fill="#f59e0b" font-weight="bold" font-size="12" text-anchor="middle">10 kg Dumbbell</text>
            </g>
            <text x="250" y="250" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">
              External Muscular Force: Contracting biceps muscle pulls forearm to lift heavy weights!
            </text>
          `;
        } else if (organView === 'heart') {
          viewHtml = `
            <g transform="translate(250, 140)">
              <path d="M 0 30 C -60 -40 -30 -80 0 -40 C 30 -80 60 -40 0 30 Z" fill="#ef4444" stroke="#f43f5e" stroke-width="3">
                <animateTransform attributeName="transform" type="scale" values="1; 1.15; 1" dur="0.8s" repeatCount="indefinite"/>
              </path>
              <text x="0" y="-85" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Cardiac Muscle Pump</text>
            </g>
            <text x="250" y="250" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="middle">
              Internal Vital Muscular Force: Involuntary cardiac muscle contracts 72 times/min to pump blood.
            </text>
          `;
        } else {
          viewHtml = `
            <g transform="translate(120, 150)">
              <!-- Alimentary Canal Tube -->
              <path d="M 0 0 Q 70 -30 140 0 T 260 0" fill="none" stroke="#f59e0b" stroke-width="35" stroke-linecap="round"/>
              <!-- Food Bolus passing through -->
              <circle cx="140" cy="0" r="14" fill="#10b981">
                <animate attributeName="cx" from="20" to="240" dur="3s" repeatCount="indefinite"/>
              </circle>
              <text x="130" y="-30" fill="#cbd5e1" font-size="11" text-anchor="middle">Wave-like Peristalsis</text>
            </g>
            <text x="250" y="250" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">
              Internal Digestive Muscular Force: Smooth muscles contract in waves to push food along the gut.
            </text>
          `;
        }

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#334155"/>
            ${viewHtml}
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
          <button class="btn-sim ${organView === 'arm' ? 'active' : ''}" id="btnArm">1. Biceps Lifting (External)</button>
          <button class="btn-sim ${organView === 'heart' ? 'active' : ''}" id="btnHeart">2. Heart Cardiac Pump (Internal)</button>
          <button class="btn-sim ${organView === 'peristalsis' ? 'active' : ''}" id="btnPeristalsis">3. Peristalsis Digestion (Internal)</button>
        </div>
      `;

      document.getElementById('btnArm').onclick = () => { organView = 'arm'; updateBtnStates(); updateSim(); };
      document.getElementById('btnHeart').onclick = () => { organView = 'heart'; updateBtnStates(); updateSim(); };
      document.getElementById('btnPeristalsis').onclick = () => { organView = 'peristalsis'; updateBtnStates(); updateSim(); };

      function updateBtnStates() {
        document.getElementById('btnArm').classList.toggle('active', organView === 'arm');
        document.getElementById('btnHeart').classList.toggle('active', organView === 'heart');
        document.getElementById('btnPeristalsis').classList.toggle('active', organView === 'peristalsis');
      }

      updateSim();
    }

    // 5. MICROSCOPIC FRICTION & ASPERITIES SIMULATOR
    function simFrictionMicroscopic(canvas, controls, title, icon) {
      title.textContent = "Microscopic Surface Asperities & Friction";
      icon.textContent = "🔬";

      let roughness = 0.5;

      function updateSim() {
        const peakHeight = Math.round(roughness * 25);
        const frictionN = Math.round(roughness * 60);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            
            <!-- Zoom Circle Border -->
            <circle cx="250" cy="130" r="85" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
            <text x="250" y="38" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
              10,000× Microscopic Cross-Section View
            </text>

            <!-- Upper Sliding Body Asperities (Teeth pointing down) -->
            <g transform="translate(175, 120)">
              <rect x="0" y="-40" width="150" height="40" fill="#0284c7" opacity="0.8"/>
              <path d="M 0 0 L 15 ${peakHeight} L 30 0 L 45 ${peakHeight} L 60 0 L 75 ${peakHeight} L 90 0 L 105 ${peakHeight} L 120 0 L 135 ${peakHeight} L 150 0" 
                    fill="none" stroke="#38bdf8" stroke-width="4"/>
              <text x="75" y="-15" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Top Moving Block</text>
            </g>

            <!-- Lower Stationary Floor Asperities (Teeth pointing up) -->
            <g transform="translate(175, ${120 + peakHeight})">
              <path d="M 0 0 L 15 ${-peakHeight} L 30 0 L 45 ${-peakHeight} L 60 0 L 75 ${-peakHeight} L 90 0 L 105 ${-peakHeight} L 120 0 L 135 ${-peakHeight} L 150 0" 
                    fill="none" stroke="#f59e0b" stroke-width="4"/>
              <rect x="0" y="0" width="150" height="40" fill="#334155" opacity="0.8"/>
              <text x="75" y="25" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Bottom Floor</text>
            </g>

            <!-- Force Readout -->
            <rect x="40" y="235" width="420" height="50" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="60" y="258" fill="#cbd5e1" font-size="12">
              Surface Roughness: <strong>${Math.round(roughness * 100)}%</strong> | Asperity Depth: <strong>${peakHeight} μm</strong>
            </text>
            <text x="60" y="276" fill="#f59e0b" font-size="13" font-weight="bold">
              Opposing Frictional Force: ${frictionN} N (Increases as jagged peaks lock tighter)
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Surface Roughness:</span>
          <input type="range" class="sim-slider" id="sliderRough" min="0.1" max="0.9" step="0.1" value="${roughness}">
          <span class="control-value" id="valRough">${Math.round(roughness * 100)}%</span>
        </div>
      `;

      document.getElementById('sliderRough').oninput = (e) => {
        roughness = parseFloat(e.target.value);
        document.getElementById('valRough').textContent = `${Math.round(roughness * 100)}%`;
        updateSim();
      };

      updateSim();
    }

    // 6. FLUID DRAG & STREAMLINING SIMULATOR
    function simFluidDragStreamlining(canvas, controls, title, icon) {
      title.textContent = "Wind Tunnel: Blunt Box vs. Streamlined Body";
      icon.textContent = "✈️";

      let isStreamlined = false;

      function updateSim() {
        const dragN = isStreamlined ? 25 : 120;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#070d18" stroke="#38bdf8"/>
            
            <!-- Wind Tunnel Streamlines -->
            <g stroke="#38bdf8" stroke-width="1.5" opacity="0.6">
              ${Array.from({length: 8}).map((_, i) => {
                const y = 60 + i * 25;
                if (!isStreamlined) {
                  return `
                    <path d="M 30 ${y} L 180 ${y} Q 210 ${y - 15} 250 ${y < 150 ? y - 40 : y + 40} L 470 ${y < 150 ? y - 40 : y + 40}" fill="none"/>
                  `;
                } else {
                  return `
                    <path d="M 30 ${y} Q 200 ${y} 250 ${y < 150 ? y - 10 : y + 10} Q 350 ${y} 470 ${y}" fill="none"/>
                  `;
                }
              }).join('')}
            </g>

            <!-- Test Object in Center of Wind Tunnel -->
            <g transform="translate(250, 150)">
              ${!isStreamlined ? `
                <!-- Flat Blunt Box -->
                <rect x="-45" y="-45" width="90" height="90" rx="4" fill="#ef4444" stroke="#f8fafc" stroke-width="2"/>
                <text x="0" y="5" fill="#fff" font-weight="bold" font-size="12" text-anchor="middle">Flat Box</text>
                <!-- Chaotic Turbulent Eddies behind box -->
                <circle cx="65" cy="-20" r="10" fill="none" stroke="#ef4444" stroke-dasharray="3,3"/>
                <circle cx="70" cy="20" r="12" fill="none" stroke="#ef4444" stroke-dasharray="3,3"/>
              ` : `
                <!-- Streamlined Teardrop Airfoil -->
                <path d="M -60 0 C -60 -35 20 -30 70 0 C 20 30 -60 35 -60 0 Z" fill="#10b981" stroke="#f8fafc" stroke-width="2"/>
                <text x="-10" y="4" fill="#fff" font-weight="bold" font-size="11" text-anchor="middle">Streamlined Airfoil</text>
              `}
            </g>

            <!-- Drag Readout -->
            <rect x="40" y="240" width="420" height="45" rx="8" fill="#1e293b" stroke="${isStreamlined ? '#10b981' : '#ef4444'}"/>
            <text x="60" y="268" fill="#cbd5e1" font-size="12">
              Body Profile: <strong>${isStreamlined ? 'Streamlined (Aerodynamic)' : 'Blunt Block (High Turbulence)'}</strong>
            </text>
            <text x="340" y="268" fill="${isStreamlined ? '#34d399' : '#f87171'}" font-size="14" font-weight="bold">
              Fluid Drag: ${dragN} N
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isStreamlined ? 'active' : ''}" id="btnShape">
          ${isStreamlined ? '📦 Switch to Flat Blunt Box' : '✈️ Switch to Streamlined Airfoil Shape'}
        </button>
      `;

      document.getElementById('btnShape').onclick = () => {
        isStreamlined = !isStreamlined;
        document.getElementById('btnShape').classList.toggle('active', isStreamlined);
        document.getElementById('btnShape').textContent = isStreamlined ? '📦 Switch to Flat Blunt Box' : '✈️ Switch to Streamlined Airfoil Shape';
        updateSim();
      };

      updateSim();
    }

    // 7. MAGNETIC FORCE & POLES SIMULATOR
    function simMagneticForcePoles(canvas, controls, title, icon) {
      title.textContent = "Magnetic Attraction & Repulsion Poles";
      icon.textContent = "🧲";

      let poleMode = 'unlike'; // 'unlike' (attract) or 'like' (repel)

      function updateSim() {
        const isAttract = poleMode === 'unlike';
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#334155"/>
            
            <!-- Left Magnet -->
            <g transform="translate(140, 140)">
              <rect x="-60" y="-30" width="60" height="60" fill="#0284c7" rx="4"/>
              <text x="-30" y="6" fill="#fff" font-weight="bold" font-size="16" text-anchor="middle">S</text>
              <rect x="0" y="-30" width="60" height="60" fill="#ef4444" rx="4"/>
              <text x="30" y="6" fill="#fff" font-weight="bold" font-size="16" text-anchor="middle">N</text>
            </g>

            <!-- Right Magnet -->
            <g transform="translate(300, 140)">
              <rect x="0" y="-30" width="60" height="60" fill="${isAttract ? '#0284c7' : '#ef4444'}" rx="4"/>
              <text x="30" y="6" fill="#fff" font-weight="bold" font-size="16" text-anchor="middle">${isAttract ? 'S' : 'N'}</text>
              <rect x="60" y="-30" width="60" height="60" fill="${isAttract ? '#ef4444' : '#0284c7'}" rx="4"/>
              <text x="90" y="6" fill="#fff" font-weight="bold" font-size="16" text-anchor="middle">${isAttract ? 'N' : 'S'}</text>
            </g>

            <!-- Force Vector Arrows between Poles -->
            <g transform="translate(250, 140)">
              ${isAttract ? `
                <!-- Attractive Pulling inward -->
                <line x1="-35" y1="0" x2="0" y2="0" stroke="#10b981" stroke-width="5"/>
                <polygon points="0,-6 10,0 0,6" fill="#10b981"/>
                <line x1="35" y1="0" x2="0" y2="0" stroke="#10b981" stroke-width="5"/>
                <polygon points="0,-6 -10,0 0,6" fill="#10b981"/>
                <text x="0" y="-18" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">ATTRACT (Unlike Poles)</text>
              ` : `
                <!-- Repulsive Pushing outward -->
                <line x1="-15" y1="0" x2="-45" y2="0" stroke="#f43f5e" stroke-width="5"/>
                <polygon points="-45,-6 -55,0 -45,6" fill="#f43f5e"/>
                <line x1="15" y1="0" x2="45" y2="0" stroke="#f43f5e" stroke-width="5"/>
                <polygon points="45,-6 55,0 45,6" fill="#f43f5e"/>
                <text x="0" y="-18" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">REPEL (Like Poles)</text>
              `}
            </g>

            <!-- Summary Text -->
            <rect x="40" y="235" width="420" height="45" rx="8" fill="#0f172a" stroke="#38bdf8"/>
            <text x="250" y="262" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">
              ${isAttract ? 'North attracts South: Unlike magnetic poles attract across space!' : 'North repels North: Like magnetic poles push each other away!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn-sim ${poleMode === 'unlike' ? 'active' : ''}" id="btnUnlike">North facing South (Unlike - Attract)</button>
          <button class="btn-sim ${poleMode === 'like' ? 'active' : ''}" id="btnLike">North facing North (Like - Repel)</button>
        </div>
      `;

      document.getElementById('btnUnlike').onclick = () => { poleMode = 'unlike'; updateSim(); };
      document.getElementById('btnLike').onclick = () => { poleMode = 'like'; updateSim(); };

      updateSim();
    }

    // 8. ELECTROSTATIC STATIC CHARGE SIMULATOR
    function simElectrostaticCharge(canvas, controls, title, icon) {
      title.textContent = "Electrostatic Charge & Paper Attraction";
      icon.textContent = "⚡";

      let isCharged = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
            
            <!-- Rubber Balloon -->
            <g transform="translate(180, 130)">
              <ellipse cx="0" cy="0" rx="45" ry="60" fill="#f43f5e" stroke="#fb7185" stroke-width="2"/>
              <!-- Negative Charges along edge if charged -->
              ${isCharged ? `
                <text x="35" y="-20" fill="#fff" font-weight="bold" font-size="14">-</text>
                <text x="38" y="5" fill="#fff" font-weight="bold" font-size="14">-</text>
                <text x="35" y="30" fill="#fff" font-weight="bold" font-size="14">-</text>
              ` : ''}
              <text x="0" y="85" fill="#cbd5e1" font-size="11" text-anchor="middle">
                ${isCharged ? 'Rubbed Balloon (- Charge)' : 'Neutral Balloon'}
              </text>
            </g>

            <!-- Paper Scraps on Table -->
            <g transform="translate(320, 180)">
              <!-- Neutral Table Line -->
              <line x1="-30" y1="20" x2="100" y2="20" stroke="#475569" stroke-width="3"/>
              
              <!-- Paper Scraps (Lifting toward balloon if charged) -->
              ${isCharged ? `
                <g fill="#f8fafc">
                  <rect x="-10" y="-40" width="14" height="8" rx="2" transform="rotate(-35 -10 -40)"/>
                  <rect x="10" y="-30" width="16" height="8" rx="2" transform="rotate(20 10 -30)"/>
                  <rect x="35" y="-15" width="15" height="7" rx="2" transform="rotate(-15 35 -15)"/>
                </g>
                <text x="35" y="-60" fill="#a855f7" font-weight="bold" font-size="11">Paper Scraps Fly Up!</text>
              ` : `
                <g fill="#94a3b8">
                  <rect x="-10" y="10" width="14" height="8" rx="2"/>
                  <rect x="20" y="10" width="16" height="8" rx="2"/>
                  <rect x="50" y="10" width="15" height="7" rx="2"/>
                </g>
                <text x="35" y="-10" fill="#64748b" font-size="10">Paper Rest on Table</text>
              `}
            </g>

            <!-- Status Banner -->
            <rect x="40" y="245" width="420" height="40" rx="8" fill="#1e293b" stroke="#a855f7"/>
            <text x="250" y="270" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">
              ${isCharged ? 'Non-Contact Electrostatic Attraction: Static charges polarize and lift neutral paper!' : 'Neutral: Without static charge rubbing, zero electrostatic attraction occurs.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isCharged ? 'active' : ''}" id="btnRub">
          ${isCharged ? '🧼 Discharge Balloon (Make Neutral)' : '🧶 Rub Balloon against Wool (Charge It!)'}
        </button>
      `;

      document.getElementById('btnRub').onclick = () => {
        isCharged = !isCharged;
        document.getElementById('btnRub').classList.toggle('active', isCharged);
        document.getElementById('btnRub').textContent = isCharged ? '🧼 Discharge Balloon (Make Neutral)' : '🧶 Rub Balloon against Wool (Charge It!)';
        updateSim();
      };

      updateSim();
    }

    // 9. GRAVITATIONAL ATTRACTION & FREE FALL SIMULATOR
    function simGravitationalPull(canvas, controls, title, icon) {
      title.textContent = "Earth's Gravitational Pull & Free Fall";
      icon.textContent = "🍎";

      let dropTime = 1.0;

      function updateSim() {
        const fallDist = Math.min(180, Math.round(0.5 * 9.8 * dropTime * dropTime * 15));
        const speed = (9.8 * dropTime).toFixed(1);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Tall Tower Platform -->
            <rect x="60" y="50" width="70" height="220" fill="#334155" stroke="#475569"/>
            <text x="95" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">Tower</text>

            <!-- Dropped Red Apple -->
            <g transform="translate(170, ${60 + fallDist})">
              <circle cx="0" cy="0" r="14" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
              <path d="M 0 -14 Q 4 -22 10 -20" stroke="#b45309" stroke-width="3" fill="none"/>
              <!-- Downward Gravity Force Vector -->
              <line x1="0" y1="16" x2="0" y2="45" stroke="#10b981" stroke-width="4"/>
              <polygon points="-5,45 0,55 5,45" fill="#10b981"/>
              <text x="25" y="35" fill="#34d399" font-size="11" font-weight="bold">W = mg</text>
            </g>

            <!-- Trajectory Dot Trail -->
            <g fill="#38bdf8" opacity="0.5">
              ${Array.from({length: 6}).map((_, i) => `
                <circle cx="170" cy="${60 + i * 30}" r="3"/>
              `).join('')}
            </g>

            <!-- Live Physics Meter -->
            <rect x="260" y="60" width="200" height="180" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="280" y="90" fill="#38bdf8" font-size="13" font-weight="bold">Free Fall Dynamics:</text>
            <text x="280" y="125" fill="#cbd5e1" font-size="12">Elapsed Time ($t$): <strong>${dropTime.toFixed(1)} s</strong></text>
            <text x="280" y="155" fill="#cbd5e1" font-size="12">Acceleration ($g$): <strong>9.8 m/s²</strong></text>
            <text x="280" y="185" fill="#f59e0b" font-size="14" font-weight="bold">
              Down Speed ($v$): ${speed} m/s
            </text>
            <text x="280" y="215" fill="#34d399" font-size="11">Gravity is strictly attractive!</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Fall Time (seconds):</span>
          <input type="range" class="sim-slider" id="sliderTime" min="0.2" max="1.5" step="0.1" value="${dropTime}">
          <span class="control-value" id="valTime">${dropTime.toFixed(1)} s</span>
        </div>
      `;

      document.getElementById('sliderTime').oninput = (e) => {
        dropTime = parseFloat(e.target.value);
        document.getElementById('valTime').textContent = `${dropTime.toFixed(1)} s`;
        updateSim();
      };

      updateSim();
    }

    // 10. MASS VS WEIGHT PLANETARY SIMULATOR
    function simMassVsWeight(canvas, controls, title, icon) {
      title.textContent = "Mass vs. Weight Across the Solar System";
      icon.textContent = "🪐";

      let planet = 'earth';
      const massKg = 60; // Constant mass

      const planetData = {
        earth: { name: "Earth", g: 9.8, color: "#38bdf8" },
        moon: { name: "Moon", g: 1.63, color: "#94a3b8" },
        mars: { name: "Mars", g: 3.71, color: "#ef4444" },
        jupiter: { name: "Jupiter", g: 24.79, color: "#f59e0b" }
      };

      function updateSim() {
        const p = planetData[planet];
        const weightN = Math.round(massKg * p.g);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#070d18" stroke="${p.color}" stroke-width="2"/>
            
            <!-- Planet Graphic -->
            <g transform="translate(130, 140)">
              <circle r="60" fill="${p.color}" opacity="0.3"/>
              <circle r="50" fill="${p.color}" opacity="0.8"/>
              <text x="0" y="5" fill="#fff" font-weight="bold" font-size="14" text-anchor="middle">${p.name}</text>
              <text x="0" y="24" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">g = ${p.g} m/s²</text>
            </g>

            <!-- Astronaut on Scale -->
            <g transform="translate(320, 140)">
              <rect x="-60" y="-80" width="120" height="150" rx="12" fill="#1e293b" stroke="#475569" stroke-width="2"/>
              <text x="0" y="-55" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Cosmic Balance Scale</text>
              
              <text x="0" y="-20" fill="#cbd5e1" font-size="12" text-anchor="middle">Mass (Matter Content):</text>
              <text x="0" y="5" fill="#34d399" font-size="18" font-weight="bold" text-anchor="middle">${massKg} kg (CONSTANT)</text>

              <line x1="-40" y1="20" x2="40" y2="20" stroke="rgba(255,255,255,0.1)"/>

              <text x="0" y="40" fill="#cbd5e1" font-size="12" text-anchor="middle">Weight ($W = mg$):</text>
              <text x="0" y="65" fill="#f59e0b" font-size="20" font-weight="bold" text-anchor="middle">${weightN} N</text>
            </g>

            <text x="250" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">
              Mass is constant everywhere in space; Weight varies with local gravity!
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
          <button class="btn-sim ${planet === 'earth' ? 'active' : ''}" id="btnEarth">Earth (9.8 N/kg)</button>
          <button class="btn-sim ${planet === 'moon' ? 'active' : ''}" id="btnMoon">Moon (1.6 N/kg)</button>
          <button class="btn-sim ${planet === 'mars' ? 'active' : ''}" id="btnMars">Mars (3.7 N/kg)</button>
          <button class="btn-sim ${planet === 'jupiter' ? 'active' : ''}" id="btnJup">Jupiter (24.8 N/kg)</button>
        </div>
      `;

      document.getElementById('btnEarth').onclick = () => { planet = 'earth'; updateBtnStates(); updateSim(); };
      document.getElementById('btnMoon').onclick = () => { planet = 'moon'; updateBtnStates(); updateSim(); };
      document.getElementById('btnMars').onclick = () => { planet = 'mars'; updateBtnStates(); updateSim(); };
      document.getElementById('btnJup').onclick = () => { planet = 'jupiter'; updateBtnStates(); updateSim(); };

      function updateBtnStates() {
        document.getElementById('btnEarth').classList.toggle('active', planet === 'earth');
        document.getElementById('btnMoon').classList.toggle('active', planet === 'moon');
        document.getElementById('btnMars').classList.toggle('active', planet === 'mars');
        document.getElementById('btnJup').classList.toggle('active', planet === 'jupiter');
      }

      updateSim();
    }

    // 11. SPRING BALANCE SIMULATOR
    function simSpringBalance(canvas, controls, title, icon) {
      title.textContent = "Spring Balance & Hooke's Elasticity";
      icon.textContent = "📏";

      let loadN = 4; // Newtons

      function updateSim() {
        const stretchY = loadN * 18;
        const massG = Math.round(loadN * 102);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#334155"/>
            
            <!-- Spring Balance Casing -->
            <g transform="translate(160, 40)">
              <rect x="0" y="0" width="70" height="200" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
              <!-- Central Slot -->
              <rect x="28" y="20" width="14" height="150" fill="#1e293b"/>
              
              <!-- Graduated Scale Markings -->
              ${Array.from({length: 9}).map((_, i) => `
                <line x1="8" y1="${25 + i * 18}" x2="24" y2="${25 + i * 18}" stroke="#cbd5e1" stroke-width="1.5"/>
                <text x="5" y="${28 + i * 18}" fill="#94a3b8" font-size="8" text-anchor="end">${i}N</text>
              `).join('')}

              <!-- Coiled Spring -->
              <path d="M 35 20 Q 25 35 35 50 Q 45 65 35 80 Q 25 ${95 + stretchY*0.3} 35 ${110 + stretchY*0.5} L 35 ${25 + stretchY}" 
                    fill="none" stroke="#f59e0b" stroke-width="3"/>

              <!-- Pointer Indicator -->
              <polygon points="20,${25 + stretchY} 28,${22 + stretchY} 28,${28 + stretchY}" fill="#ef4444"/>

              <!-- Hanging Hook -->
              <path d="M 35 ${25 + stretchY} L 35 ${50 + stretchY} Q 35 ${65 + stretchY} 22 ${60 + stretchY}" 
                    fill="none" stroke="#cbd5e1" stroke-width="3"/>

              <!-- Attached Load Mass -->
              <rect x="10" y="${60 + stretchY}" width="50" height="40" rx="4" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
              <text x="35" y="${85 + stretchY}" fill="#fff" font-weight="bold" font-size="11" text-anchor="middle">${loadN} N</text>
            </g>

            <!-- Measurement Readout -->
            <rect x="270" y="70" width="180" height="150" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="290" y="100" fill="#38bdf8" font-size="13" font-weight="bold">Balance Reading:</text>
            <text x="290" y="130" fill="#cbd5e1" font-size="12">Force / Weight:</text>
            <text x="290" y="155" fill="#f59e0b" font-size="20" font-weight="bold">${loadN}.0 Newtons</text>
            <text x="290" y="180" fill="#cbd5e1" font-size="12">Corresponding Mass:</text>
            <text x="290" y="205" fill="#34d399" font-size="16" font-weight="bold">≈ ${massG} grams</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Suspended Weight (N):</span>
          <input type="range" class="sim-slider" id="sliderLoad" min="1" max="8" step="1" value="${loadN}">
          <span class="control-value" id="valLoad">${loadN} N</span>
        </div>
      `;

      document.getElementById('sliderLoad').oninput = (e) => {
        loadN = parseInt(e.target.value);
        document.getElementById('valLoad').textContent = `${loadN} N`;
        updateSim();
      };

      updateSim();
    }

    // 12. LIQUID PRESSURE & UPTHRUST SIMULATOR
    function simLiquidUpthrust(canvas, controls, title, icon) {
      title.textContent = "Liquid Hydrostatic Pressure & Upthrust";
      icon.textContent = "🌊";

      let depth = 60; // mm

      function updateSim() {
        const topPressure = Math.round(depth * 0.1);
        const bottomPressure = Math.round((depth + 50) * 0.1);
        const netUpthrust = bottomPressure - topPressure;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Glass Water Tank -->
            <rect x="60" y="50" width="220" height="220" rx="6" fill="rgba(14, 165, 233, 0.2)" stroke="#38bdf8" stroke-width="2"/>
            <text x="170" y="75" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Water Tank (ρ = 1.0 g/cm³)</text>

            <!-- Submerged Cylinder -->
            <g transform="translate(130, ${70 + depth})">
              <rect x="0" y="0" width="80" height="50" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
              <text x="40" y="30" fill="#fff" font-weight="bold" font-size="11" text-anchor="middle">Cylinder</text>
              
              <!-- Downward Pressure Arrows on Top -->
              <line x1="20" y1="-15" x2="20" y2="-2" stroke="#ef4444" stroke-width="3"/>
              <line x1="60" y1="-15" x2="60" y2="-2" stroke="#ef4444" stroke-width="3"/>
              <text x="40" y="-18" fill="#fb7185" font-size="9" text-anchor="middle">P_top = ${topPressure} kPa</text>

              <!-- Upward Pressure Arrows on Bottom (Larger) -->
              <line x1="20" y1="65" x2="20" y2="52" stroke="#10b981" stroke-width="5"/>
              <line x1="60" y1="65" x2="60" y2="52" stroke="#10b981" stroke-width="5"/>
              <text x="40" y="78" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">P_bottom = ${bottomPressure} kPa</text>
            </g>

            <!-- Mathematical Explanation -->
            <rect x="300" y="60" width="165" height="180" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="315" y="90" fill="#38bdf8" font-size="13" font-weight="bold">Origin of Upthrust:</text>
            <text x="315" y="120" fill="#cbd5e1" font-size="11">Bottom pressure exceeds top pressure due to depth:</text>
            <text x="315" y="145" fill="#34d399" font-size="12" font-weight="bold">F_up > F_down</text>
            <text x="315" y="175" fill="#cbd5e1" font-size="11">Resultant Net Force:</text>
            <text x="315" y="205" fill="#f59e0b" font-size="16" font-weight="bold">Upthrust ($F_b$)</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Immersion Depth (mm):</span>
          <input type="range" class="sim-slider" id="sliderDepth" min="20" max="110" step="10" value="${depth}">
          <span class="control-value" id="valDepth">${depth} mm</span>
        </div>
      `;

      document.getElementById('sliderDepth').oninput = (e) => {
        depth = parseInt(e.target.value);
        document.getElementById('valDepth').textContent = `${depth} mm`;
        updateSim();
      };

      updateSim();
    }

    // 13. FLOATING & SINKING CONDITIONS SIMULATOR
    function simFloatingSinking(canvas, controls, title, icon) {
      title.textContent = "Equilibrium: Weight vs. Buoyant Force";
      icon.textContent = "⚖️";

      let density = 0.6; // g/cm3

      function updateSim() {
        const isFloat = density <= 1.0;
        const blockY = isFloat ? (120 - (1.0 - density) * 40) : 200;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Water Tank with Waterline at Y=140 -->
            <rect x="60" y="140" width="220" height="130" fill="rgba(14, 165, 233, 0.3)" stroke="#38bdf8" stroke-width="2"/>
            <line x1="60" y1="140" x2="280" y2="140" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>
            <text x="70" y="160" fill="#38bdf8" font-size="10">Waterline (ρ = 1.0 g/cm³)</text>

            <!-- Test Block -->
            <g transform="translate(140, ${blockY})">
              <rect x="0" y="0" width="70" height="60" rx="4" fill="${isFloat ? '#f59e0b' : '#64748b'}" stroke="#fff" stroke-width="2"/>
              <text x="35" y="35" fill="#0f172a" font-weight="bold" font-size="11" text-anchor="middle">
                ${density} g/cm³
              </text>
            </g>

            <!-- Readout Panel -->
            <rect x="300" y="60" width="165" height="190" rx="10" fill="#1e293b" stroke="${isFloat ? '#10b981' : '#f43f5e'}" stroke-width="2"/>
            <text x="315" y="90" fill="#38bdf8" font-size="13" font-weight="bold">State: ${isFloat ? 'FLOATING' : 'SINKING'}</text>
            <text x="315" y="120" fill="#cbd5e1" font-size="12">Block Density:</text>
            <text x="315" y="140" fill="${isFloat ? '#f59e0b' : '#f87171'}" font-size="16" font-weight="bold">${density} g/cm³</text>
            
            <text x="315" y="170" fill="#cbd5e1" font-size="12">Force Balance:</text>
            <text x="315" y="195" fill="${isFloat ? '#34d399' : '#fb7185'}" font-size="13" font-weight="bold">
              ${isFloat ? 'F_buoyant = Weight' : 'Weight > F_buoyant'}
            </text>
            <text x="315" y="225" fill="#94a3b8" font-size="10">
              ${isFloat ? 'Displaces equal weight' : 'Accelerates to bottom!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Material Density:</span>
          <input type="range" class="sim-slider" id="sliderDens" min="0.3" max="2.0" step="0.1" value="${density}">
          <span class="control-value" id="valDens">${density} g/cm³</span>
        </div>
      `;

      document.getElementById('sliderDens').oninput = (e) => {
        density = parseFloat(e.target.value);
        document.getElementById('valDens').textContent = `${density} g/cm³`;
        updateSim();
      };

      updateSim();
    }

    // 14. ARCHIMEDES' PRINCIPLE OVERFLOW SIMULATOR
    function simArchimedesPrinciple(canvas, controls, title, icon) {
      title.textContent = "Archimedes' Overflow Can Experiment";
      icon.textContent = "🧪";

      let isSubmerged = false;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Eureka Overflow Can with Spout -->
            <path d="M 80 80 L 80 230 L 200 230 L 200 110 L 230 140 L 230 150 L 200 125 L 200 80 Z" 
                  fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <!-- Water inside can -->
            <rect x="85" y="110" width="110" height="115" fill="rgba(14, 165, 233, 0.3)"/>

            <!-- Suspended Heavy Rock -->
            <g transform="translate(140, ${isSubmerged ? 160 : 70})">
              <circle r="22" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
              <text x="0" y="4" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Rock</text>
            </g>

            <!-- Measuring Cylinder Collecting Overflow -->
            <rect x="235" y="160" width="55" height="90" rx="4" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
            ${isSubmerged ? `
              <!-- Water in beaker -->
              <rect x="238" y="200" width="49" height="48" fill="#0284c7" opacity="0.8"/>
              <text x="262" y="190" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">200 mL</text>
            ` : ''}

            <!-- Mathematical Identity Box -->
            <rect x="310" y="60" width="155" height="190" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="325" y="90" fill="#f59e0b" font-size="13" font-weight="bold">Archimedes' Law:</text>
            <text x="325" y="120" fill="#cbd5e1" font-size="11">Rock in Air: <strong>5.0 N</strong></text>
            <text x="325" y="145" fill="#cbd5e1" font-size="11">Apparent in Water: <strong>${isSubmerged ? '3.04 N' : '5.0 N'}</strong></text>
            <line x1="325" y1="160" x2="450" y2="160" stroke="rgba(255,255,255,0.1)"/>
            <text x="325" y="180" fill="#38bdf8" font-size="11">Displaced Water Wt:</text>
            <text x="325" y="205" fill="#34d399" font-size="16" font-weight="bold">${isSubmerged ? '1.96 N' : '0.0 N'}</text>
            <text x="325" y="230" fill="#38bdf8" font-size="10">Buoyant Force = Displaced Wt</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isSubmerged ? 'active' : ''}" id="btnSubmerge">
          ${isSubmerged ? '🔼 Lift Rock Out of Can' : '🔽 Lower Rock into Full Can (Eureka!)'}
        </button>
      `;

      document.getElementById('btnSubmerge').onclick = () => {
        isSubmerged = !isSubmerged;
        document.getElementById('btnSubmerge').classList.toggle('active', isSubmerged);
        document.getElementById('btnSubmerge').textContent = isSubmerged ? '🔼 Lift Rock Out of Can' : '🔽 Lower Rock into Full Can (Eureka!)';
        updateSim();
      };

      updateSim();
    }

    // 15. SUBMARINE BALLAST TANK SIMULATOR
    function simShipSubmarineDensity(canvas, controls, title, icon) {
      title.textContent = "Submarine Ballast Tanks: Dive & Surface";
      icon.textContent = "🚢";

      let isDiving = false;

      function updateSim() {
        const subY = isDiving ? 190 : 130;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#070d18" stroke="#38bdf8"/>
            
            <!-- Ocean Surface & Deep Water -->
            <rect x="30" y="120" width="440" height="170" fill="rgba(2, 132, 199, 0.25)"/>
            <line x1="30" y1="120" x2="470" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,4"/>
            <text x="50" y="140" fill="#38bdf8" font-size="10">Sea Level</text>

            <!-- Submarine Body -->
            <g transform="translate(180, ${subY})">
              <!-- Hull -->
              <ellipse cx="60" cy="0" rx="90" ry="30" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
              <rect x="40" y="-45" width="35" height="20" fill="#475569" rx="2"/>
              
              <!-- Ballast Tanks -->
              <rect x="0" y="-12" width="35" height="24" rx="2" fill="${isDiving ? '#0284c7' : '#f8fafc'}" stroke="#38bdf8"/>
              <text x="17" y="4" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">${isDiving ? 'H₂O' : 'AIR'}</text>
              
              <rect x="85" y="-12" width="35" height="24" rx="2" fill="${isDiving ? '#0284c7' : '#f8fafc'}" stroke="#38bdf8"/>
              <text x="102" y="4" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">${isDiving ? 'H₂O' : 'AIR'}</text>
            </g>

            <!-- Status Banner -->
            <rect x="40" y="40" width="420" height="45" rx="8" fill="#1e293b" stroke="#38bdf8"/>
            <text x="250" y="67" fill="${isDiving ? '#fb7185' : '#34d399'}" font-size="13" font-weight="bold" text-anchor="middle">
              ${isDiving ? '⚓ BALLAST FLOODED WITH SEAWATER: Average density > Seawater • Submarine Dives!' : '🌊 COMPRESSED AIR BLOWS WATER OUT: Average density < Seawater • Submarine Surfaces!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isDiving ? 'active' : ''}" id="btnDive">
          ${isDiving ? '💨 Blow Compressed Air (Surface to Top)' : '🌊 Flood Ballast Tanks with Seawater (Dive Deep)'}
        </button>
      `;

      document.getElementById('btnDive').onclick = () => {
        isDiving = !isDiving;
        document.getElementById('btnDive').classList.toggle('active', isDiving);
        document.getElementById('btnDive').textContent = isDiving ? '💨 Blow Compressed Air (Surface to Top)' : '🌊 Flood Ballast Tanks with Seawater (Dive Deep)';
        updateSim();
      };

      updateSim();
    }

    // 16. MASTER FORCE MATRIX SYNTHESIS SIMULATOR
    function simForceMatrixSynthesis(canvas, controls, title, icon) {
      title.textContent = "Grand Force Classification & Balance Matrix";
      icon.textContent = "📊";

      let activeRow = 'all';

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#1e293b" stroke="#38bdf8"/>
            
            <text x="250" y="50" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">
              Master Synthesis: Contact vs. Non-Contact Taxonomy
            </text>

            <!-- Category Columns -->
            <g transform="translate(40, 80)">
              <!-- Contact Column -->
              <rect x="0" y="0" width="200" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="100" y="25" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Contact Forces (Touch)</text>
              <text x="20" y="55" fill="#cbd5e1" font-size="11">• Muscular Force (Skeletal/Gut)</text>
              <text x="20" y="80" fill="#cbd5e1" font-size="11">• Surface Friction ($f_{\\text{oppose}}$)</text>
              <text x="20" y="105" fill="#cbd5e1" font-size="11">• Fluid Drag & Streamlining</text>
              <text x="20" y="130" fill="#cbd5e1" font-size="11">• Fluid Upthrust ($F_b$)</text>

              <!-- Non-Contact Column -->
              <rect x="220" y="0" width="200" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
              <text x="320" y="25" fill="#a855f7" font-size="12" font-weight="bold" text-anchor="middle">Non-Contact Forces (Field)</text>
              <text x="240" y="55" fill="#cbd5e1" font-size="11">• Magnetic Force (Poles)</text>
              <text x="240" y="80" fill="#cbd5e1" font-size="11">• Electrostatic Force (Charges)</text>
              <text x="240" y="105" fill="#cbd5e1" font-size="11">• Gravitational Force ($W=mg$)</text>
              <text x="240" y="130" fill="#34d399" font-size="11">Strictly Attractive Nature!</text>
            </g>

            <!-- Bottom Formula Recap -->
            <rect x="40" y="245" width="420" height="40" rx="8" fill="#0f172a" stroke="rgba(255,255,255,0.1)"/>
            <text x="250" y="270" fill="#f8fafc" font-size="11" text-anchor="middle">
              SI Unit: <strong>Newton (N)</strong> | Mass: Invariant (kg) | Archimedes: <strong>F_b = Wt of displaced fluid</strong>
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; justify-content: center;">
          <span style="color: #38bdf8; font-size: 0.82rem; font-weight: 600;">
            ✔ Complete 16-Topic Curriculum Synthesized
          </span>
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

output_path = 'public/animations/class8-science-force-buoyancy.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

