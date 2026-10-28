# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class8-science-particles-matter.html
Class 8 Science - Chapter 7: Particles and Matter: Nature, States, Diffusion, Atoms and Molecules
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Acharya Dr. Kanad)
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
from class8_science_particles_matter_data import SLIDES, QUIZ_QUESTIONS

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
  <title>NCERT Class 8 Science • Chapter 7: Particles and Matter Master Lab</title>
  
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
        radial-gradient(circle at 85% 80%, rgba(168, 85, 247, 0.1) 0%, transparent 40%),
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
      background: linear-gradient(135deg, #0284c7, #a855f7);
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
      background: linear-gradient(90deg, #38bdf8, #a855f7);
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
      background: linear-gradient(135deg, #0284c7, #a855f7);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      position: relative;
      flex-shrink: 0;
      box-shadow: 0 0 12px rgba(168, 85, 247, 0.4);
    }

    .avatar-speaking-pulse {
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      border: 2px solid var(--accent-purple);
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
      background: linear-gradient(135deg, #ffffff, #c084fc);
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
      <div class="lab-icon">⚛️</div>
      <div class="header-text">
        <div class="sub-badge">NCERT Class 8 Science • Chapter 7</div>
        <h1>Particles and Matter</h1>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-bar-container">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
      <div class="progress-stats">
        <span id="slideIndicator">Slide 1 of 20</span>
        <span id="slideTagIndicator">Matter & Particulate Nature</span>
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
        <span class="avatar-name">Acharya Dr. Kanad • Natural Philosopher & Chemist</span>
        <span class="speech-status-pill" id="speechStatusPill">Speaking...</span>
      </div>
      <div class="avatar-speech-text" id="avatarSpeechText">
        Welcome to the Molecular & Particulate Physics Laboratory! Let us peer into the sub-microscopic world of atoms, molecules, forces, and diffusion.
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
          <span class="slide-tag" id="slideBadge">Particulate Nature</span>
          <span class="slide-number-pill" id="slideNumberPill">Slide 1 of 20</span>
        </div>

        <h2 class="slide-title" id="slideHeading">Matter & Particulate Nature</h2>

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
            <span id="simIcon">🧊</span>
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
        chip.innerHTML = `<span class="vocab-word">⚛️ ${item.word}:</span><span class="vocab-def">${item.definition}</span>`;
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
        case 'matter_sugar_dissolve_sim':
          simMatterSugarDissolve(canvas, controls, title, icon);
          break;
        case 'kanad_parmanu_concept_sim':
          simKanadParmanuConcept(canvas, controls, title, icon);
          break;
        case 'interparticle_voids_sim':
          simInterparticleVoids(canvas, controls, title, icon);
          break;
        case 'interparticle_force_distance_sim':
          simInterparticleForceDistance(canvas, controls, title, icon);
          break;
        case 'thermal_energy_vibration_sim':
          simThermalEnergyVibration(canvas, controls, title, icon);
          break;
        case 'solid_lattice_vibration_sim':
          simSolidLatticeVibration(canvas, controls, title, icon);
          break;
        case 'solid_melting_threshold_sim':
          simSolidMeltingThreshold(canvas, controls, title, icon);
          break;
        case 'liquid_fluid_flow_sim':
          simLiquidFluidFlow(canvas, controls, title, icon);
          break;
        case 'boiling_vs_evaporation_sim':
          simBoilingVsEvaporation(canvas, controls, title, icon);
          break;
        case 'gas_expansion_pressure_sim':
          simGasExpansionPressure(canvas, controls, title, icon);
          break;
        case 'syringe_compressibility_sim':
          simSyringeCompressibility(canvas, controls, title, icon);
          break;
        case 'potassium_permanganate_sim':
          simPotassiumPermanganate(canvas, controls, title, icon);
          break;
        case 'temp_diffusion_rate_sim':
          simTempDiffusionRate(canvas, controls, title, icon);
          break;
        case 'incense_gas_diffusion_sim':
          simIncenseGasDiffusion(canvas, controls, title, icon);
          break;
        case 'elemental_atoms_sim':
          simElementalAtoms(canvas, controls, title, icon);
          break;
        case 'molecules_diatomic_water_sim':
          simMoleculesDiatomicWater(canvas, controls, title, icon);
          break;
        default:
          canvas.innerHTML = `<div style="color: #94a3b8; font-size: 0.9rem;">Select a valid simulator.</div>`;
      }
    }

    // 1. SUGAR DISSOLUTION & VOLUME CONSERVATION SIMULATOR
    function simMatterSugarDissolve(canvas, controls, title, icon) {
      title.textContent = "Sugar Dissolution: Voids & Volume Conservation";
      icon.textContent = "🧊";

      let sugarState = 'crystal'; // 'crystal', 'dissolving', 'dissolved'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Glass Beaker with 100 mL Mark -->
            <rect x="80" y="70" width="160" height="190" rx="4" fill="rgba(14, 165, 233, 0.15)" stroke="#38bdf8" stroke-width="2"/>
            <line x1="70" y1="120" x2="90" y2="120" stroke="#facc15" stroke-width="2"/>
            <text x="65" y="124" fill="#facc15" font-size="10" font-weight="bold" text-anchor="end">100 mL</text>

            <!-- Water Liquid Level (Fixed at 100 mL) -->
            <rect x="82" y="120" width="156" height="138" fill="#0284c7" opacity="0.45"/>

            <!-- Water Particles (Blue Spheres) -->
            <g fill="#38bdf8" opacity="0.8">
              <circle cx="105" cy="145" r="9"/> <circle cx="135" cy="145" r="9"/> <circle cx="165" cy="145" r="9"/> <circle cx="195" cy="145" r="9"/>
              <circle cx="120" cy="175" r="9"/> <circle cx="150" cy="175" r="9"/> <circle cx="180" cy="175" r="9"/> <circle cx="210" cy="175" r="9"/>
              <circle cx="105" cy="205" r="9"/> <circle cx="135" cy="205" r="9"/> <circle cx="165" cy="205" r="9"/> <circle cx="195" cy="205" r="9"/>
              <circle cx="120" cy="235" r="9"/> <circle cx="150" cy="235" r="9"/> <circle cx="180" cy="235" r="9"/> <circle cx="210" cy="235" r="9"/>
            </g>

            <!-- Sugar Particles (Yellow Spheres) -->
            ${sugarState === 'crystal' ? `
              <!-- Compact Sugar Crystal at Bottom -->
              <rect x="140" y="240" width="40" height="18" fill="#facc15" rx="2" stroke="#eab308"/>
              <text x="160" y="252" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Sugar</text>
            ` : sugarState === 'dissolving' ? `
              <!-- Breaking into individual pieces -->
              <circle cx="120" cy="205" r="5" fill="#facc15"/>
              <circle cx="150" cy="235" r="5" fill="#facc15"/>
              <circle cx="180" cy="205" r="5" fill="#facc15"/>
              <circle cx="150" cy="175" r="5" fill="#facc15"/>
              <rect x="150" y="244" width="20" height="12" fill="#facc15" rx="2"/>
            ` : `
              <!-- Fully Dispersed into Interstitial Voids -->
              <circle cx="120" cy="145" r="5" fill="#facc15"/>
              <circle cx="150" cy="145" r="5" fill="#facc15"/>
              <circle cx="180" cy="145" r="5" fill="#facc15"/>
              <circle cx="105" cy="175" r="5" fill="#facc15"/>
              <circle cx="135" cy="175" r="5" fill="#facc15"/>
              <circle cx="165" cy="175" r="5" fill="#facc15"/>
              <circle cx="195" cy="175" r="5" fill="#facc15"/>
              <circle cx="120" cy="205" r="5" fill="#facc15"/>
              <circle cx="150" cy="205" r="5" fill="#facc15"/>
              <circle cx="180" cy="205" r="5" fill="#facc15"/>
              <circle cx="135" cy="235" r="5" fill="#facc15"/>
              <circle cx="165" cy="235" r="5" fill="#facc15"/>
            `}

            <!-- Right Dashboard Panel -->
            <rect x="270" y="50" width="190" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="285" y="80" fill="#38bdf8" font-size="13" font-weight="bold">Solution Dynamics:</text>
            
            <text x="285" y="110" fill="#94a3b8" font-size="11">Beaker Volume:</text>
            <text x="285" y="128" fill="#facc15" font-size="15" font-weight="bold">100 mL (Unchanged!)</text>

            <text x="285" y="155" fill="#94a3b8" font-size="11">State of Solute:</text>
            <text x="285" y="175" fill="${sugarState === 'dissolved' ? '#34d399' : '#f59e0b'}" font-size="13" font-weight="bold">
              ${sugarState === 'crystal' ? 'Solid Crystal at base' : sugarState === 'dissolving' ? 'Dissolving into ions' : 'Occupying Voids!'}
            </text>

            <text x="285" y="205" fill="#cbd5e1" font-size="10">
              ${sugarState === 'dissolved' ? '✔ Sugar particles fit into existing interparticle spaces of water.' : 'Click "Stir & Dissolve" to disperse particles.'}
            </text>
            <text x="285" y="245" fill="#38bdf8" font-size="9">Mass is conserved: Mass_total = M_w + M_s</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${sugarState === 'crystal' ? 'active' : ''}" id="btnCryst">1. Solid Sugar Crystal</button>
          <button class="btn-sim ${sugarState === 'dissolving' ? 'active' : ''}" id="btnDiss">2. Stirring / Dispersing</button>
          <button class="btn-sim ${sugarState === 'dissolved' ? 'active' : ''}" id="btnDone">3. Completely Dissolved</button>
        </div>
      `;

      document.getElementById('btnCryst').onclick = () => { sugarState = 'crystal'; updateSim(); };
      document.getElementById('btnDiss').onclick = () => { sugarState = 'dissolving'; updateSim(); };
      document.getElementById('btnDone').onclick = () => { sugarState = 'dissolved'; updateSim(); };

      updateSim();
    }

    // 2. KANAD'S PARMANU CONCEPT SIMULATOR
    function simKanadParmanuConcept(canvas, controls, title, icon) {
      title.textContent = "Acharya Kanad's Sub-division to Parmanu";
      icon.textContent = "📜";

      let stage = 6; // 1 to 6

      const STAGES = {
        1: { name: "Macro Matter Block", size: "10 cm", desc: "Visible rock piece (Sthula Dravya)", scale: 80, color: "#78350f" },
        2: { name: "Small Chip", size: "1 cm", desc: "Chipped stone flake", scale: 45, color: "#92400e" },
        3: { name: "Fine Sand Grain", size: "1 mm", desc: "Grain of sand or chalk dust", scale: 24, color: "#b45309" },
        4: { name: "Microscopic Mote", size: "10 μm", desc: "Barely visible under light microscope", scale: 12, color: "#d97706" },
        5: { name: "Colloidal Cluster (Anu)", size: "100 nm", desc: "Cluster of multiple atoms", scale: 6, color: "#f59e0b" },
        6: { name: "The Parmanu", size: "0.1 nm (1 Å)", desc: "Eternal, indivisible building block", scale: 20, color: "#facc15" }
      };

      function updateSim() {
        const info = STAGES[stage];

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Central Display Window -->
            <rect x="50" y="50" width="210" height="210" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
            <text x="155" y="80" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">
              Magnification Chamber
            </text>

            <!-- Matter Object at current stage -->
            <g transform="translate(155, 160)">
              ${stage === 6 ? `
                <circle cx="0" cy="0" r="22" fill="#facc15" filter="drop-shadow(0 0 15px #f59e0b)"/>
                <circle cx="0" cy="0" r="28" fill="none" stroke="#facc15" stroke-dasharray="4,4"/>
                <text x="0" y="5" fill="#0f172a" font-size="9" font-weight="800" text-anchor="middle">PARMANU</text>
              ` : `
                <rect x="${-info.scale/2}" y="${-info.scale/2}" width="${info.scale}" height="${info.scale}" rx="4" fill="${info.color}"/>
              `}
            </g>

            <!-- Right Philosophy Banner -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="78" fill="#38bdf8" font-size="12" font-weight="bold">Vaisheshika Philosophy:</text>
            
            <text x="295" y="105" fill="#94a3b8" font-size="10">Stage ${stage} of 6:</text>
            <text x="295" y="125" fill="#facc15" font-size="13" font-weight="bold">${info.name}</text>

            <text x="295" y="150" fill="#94a3b8" font-size="10">Physical Dimension:</text>
            <text x="295" y="168" fill="#34d399" font-size="14" font-weight="bold">${info.size}</text>

            <text x="295" y="195" fill="#cbd5e1" font-size="10">${info.desc}</text>
            
            <text x="295" y="240" fill="#a855f7" font-size="9" font-style="italic">
              "Divide matter endlessly, and you must arrive at the indivisible Parmanu."
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Sub-division Level:</span>
          <input type="range" class="sim-slider" id="sliderKanad" min="1" max="6" step="1" value="${stage}">
          <span class="control-value" id="valKanad">Stage ${stage}: ${STAGES[stage].name}</span>
        </div>
      `;

      document.getElementById('sliderKanad').oninput = (e) => {
        stage = parseInt(e.target.value);
        document.getElementById('valKanad').textContent = `Stage ${stage}: ${STAGES[stage].name}`;
        updateSim();
      };

      updateSim();
    }

    // 3. INTERPARTICLE VOIDS SIMULATOR
    function simInterparticleVoids(canvas, controls, title, icon) {
      title.textContent = "Interparticle Voids in Liquids & Solids";
      icon.textContent = "🔬";

      let highlightVoids = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Microscope Viewfinder -->
            <circle cx="170" cy="160" r="110" fill="#021024" stroke="#38bdf8" stroke-width="3"/>
            
            <!-- Interstitial Voids highlighted in yellow/neon -->
            ${highlightVoids ? `
              <rect x="135" y="125" width="20" height="20" fill="#facc15" opacity="0.6"/>
              <rect x="185" y="125" width="20" height="20" fill="#facc15" opacity="0.6"/>
              <rect x="135" y="175" width="20" height="20" fill="#facc15" opacity="0.6"/>
              <rect x="185" y="175" width="20" height="20" fill="#facc15" opacity="0.6"/>
              <text x="170" y="145" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">VOID</text>
            ` : ''}

            <!-- Spherical Particles -->
            <g fill="#0284c7" stroke="#38bdf8" stroke-width="1.5">
              <circle cx="120" cy="110" r="22"/> <circle cx="170" cy="110" r="22"/> <circle cx="220" cy="110" r="22"/>
              <circle cx="120" cy="160" r="22"/> <circle cx="170" cy="160" r="22"/> <circle cx="220" cy="160" r="22"/>
              <circle cx="120" cy="210" r="22"/> <circle cx="170" cy="210" r="22"/> <circle cx="220" cy="210" r="22"/>
            </g>

            <!-- Metrics Panel -->
            <rect x="300" y="50" width="160" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="315" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Void Geometry:</text>
            
            <text x="315" y="110" fill="#94a3b8" font-size="10">Particle Diameter:</text>
            <text x="315" y="128" fill="#f8fafc" font-size="14" font-weight="bold">~0.28 nm (H₂O)</text>

            <text x="315" y="155" fill="#94a3b8" font-size="10">Liquid Void Fraction:</text>
            <text x="315" y="178" fill="#facc15" font-size="18" font-weight="800">~36% to 42%</text>

            <text x="315" y="210" fill="#cbd5e1" font-size="9">
              ${highlightVoids ? 'Yellow zones show the empty space available for dissolved solute particles.' : 'Spheres represent constituent liquid molecules.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${highlightVoids ? 'active' : ''}" id="btnToggleVoid">
          ${highlightVoids ? '👁️ Hide Interstitial Voids' : '✨ Highlight Interstitial Voids (Yellow)'}
        </button>
      `;

      document.getElementById('btnToggleVoid').onclick = () => {
        highlightVoids = !highlightVoids;
        updateSim();
      };

      updateSim();
    }

    // 4. INTERPARTICLE FORCE VS DISTANCE SIMULATOR
    function simInterparticleForceDistance(canvas, controls, title, icon) {
      title.textContent = "Interparticle Cohesion vs. Distance";
      icon.textContent = "🧲";

      let distNm = 0.3; // nm

      function updateSim() {
        // Force drops steeply: F ~ (0.3 / dist)^4
        const forcePct = Math.min(100, Math.round(100 * Math.pow(0.3 / distNm, 4)));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Two Particles with Elastic Bond Spring -->
            <g transform="translate(180, 130)">
              <!-- Particle A -->
              <circle cx="${-distNm * 90}" cy="0" r="25" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="${-distNm * 90}" y="4" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">A</text>

              <!-- Cohesion Spring Vector -->
              <line x1="${-distNm * 90 + 25}" y1="0" x2="${distNm * 90 - 25}" y2="0" stroke="${forcePct > 40 ? '#10b981' : '#f43f5e'}" stroke-width="${Math.max(1, forcePct * 0.08)}" stroke-dasharray="6,3"/>

              <!-- Particle B -->
              <circle cx="${distNm * 90}" cy="0" r="25" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="${distNm * 90}" y="4" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">B</text>

              <!-- Separation Dimension Line -->
              <line x1="${-distNm * 90}" y1="45" x2="${distNm * 90}" y2="45" stroke="#facc15" stroke-width="1.5"/>
              <text x="0" y="60" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">r = ${distNm.toFixed(2)} nm</text>
            </g>

            <!-- Force Gauge Readout -->
            <rect x="290" y="50" width="170" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="305" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Cohesive Bond Calculus:</text>
            
            <text x="305" y="110" fill="#94a3b8" font-size="10">Particle Separation (r):</text>
            <text x="305" y="128" fill="#facc15" font-size="14" font-weight="bold">${distNm.toFixed(2)} nm</text>

            <text x="305" y="155" fill="#94a3b8" font-size="10">Attractive Force:</text>
            <text x="305" y="180" fill="${forcePct > 50 ? '#34d399' : '#fb7185'}" font-size="20" font-weight="800">${forcePct}%</text>

            <text x="305" y="210" fill="#cbd5e1" font-size="9">
              ${forcePct > 50 ? 'Strong bond: Particles locked tightly!' : 'Drastic drop: Attractive grip nearly zero!'}
            </text>
            <text x="305" y="245" fill="#38bdf8" font-size="8">Law: Small increase in r = Massive drop in F</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Particle Separation (r):</span>
          <input type="range" class="sim-slider" id="sliderDist" min="0.25" max="0.80" step="0.05" value="${distNm}">
          <span class="control-value" id="valDist">${distNm} nm</span>
        </div>
      `;

      document.getElementById('sliderDist').oninput = (e) => {
        distNm = parseFloat(e.target.value);
        document.getElementById('valDist').textContent = `${distNm.toFixed(2)} nm`;
        updateSim();
      };

      updateSim();
    }

    // 5. THERMAL ENERGY VS COHESION TUG-OF-WAR SIMULATOR
    function simThermalEnergyVibration(canvas, controls, title, icon) {
      title.textContent = "Thermal Energy vs. Cohesion Tug-of-War";
      icon.textContent = "🔥";

      let tempC = 25; // °C

      function updateSim() {
        const isSolid = (tempC < 0);
        const isGas = (tempC >= 100);
        const stateName = isSolid ? "SOLID (ICE)" : isGas ? "GAS (STEAM)" : "LIQUID (WATER)";
        const stateColor = isSolid ? "#38bdf8" : isGas ? "#f43f5e" : "#10b981";

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Tug of War Balance Scale Graphic -->
            <g transform="translate(160, 140)">
              <!-- Container Box -->
              <rect x="-90" y="-70" width="180" height="150" rx="8" fill="#1e293b" stroke="${stateColor}" stroke-width="2"/>
              
              ${isSolid ? `
                <!-- Rigid Grid of Particles vibrating slightly -->
                <g fill="#38bdf8">
                  <circle cx="-50" cy="-30" r="10"/> <circle cx="0" cy="-30" r="10"/> <circle cx="50" cy="-30" r="10"/>
                  <circle cx="-50" cy="10" r="10"/> <circle cx="0" cy="10" r="10"/> <circle cx="50" cy="10" r="10"/>
                  <circle cx="-50" cy="50" r="10"/> <circle cx="0" cy="50" r="10"/> <circle cx="50" cy="50" r="10"/>
                </g>
                <text x="0" y="70" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Locked in Lattice Grid</text>
              ` : isGas ? `
                <!-- Dispersed particles flying wildly -->
                <g fill="#f43f5e">
                  <circle cx="-60" cy="-40" r="7"/> <circle cx="40" cy="-50" r="7"/> <circle cx="-10" cy="0" r="7"/>
                  <circle cx="65" cy="20" r="7"/> <circle cx="-55" cy="45" r="7"/> <circle cx="30" cy="55" r="7"/>
                </g>
                <line x1="-60" y1="-40" x2="-35" y2="-20" stroke="#f43f5e" stroke-width="1.5"/>
                <line x1="40" y1="-50" x2="65" y2="-30" stroke="#f43f5e" stroke-width="1.5"/>
                <text x="0" y="70" fill="#fb7185" font-size="10" font-weight="bold" text-anchor="middle">Vast Spaces & Chaos</text>
              ` : `
                <!-- Liquid sliding clusters -->
                <g fill="#34d399">
                  <circle cx="-40" cy="20" r="9"/> <circle cx="-15" cy="30" r="9"/> <circle cx="15" cy="25" r="9"/> <circle cx="45" cy="35" r="9"/>
                  <circle cx="-30" cy="50" r="9"/> <circle cx="0" cy="55" r="9"/> <circle cx="30" cy="52" r="9"/>
                </g>
                <text x="0" y="-40" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Fluids Slide Freely</text>
              `}
            </g>

            <!-- Thermostat Readout -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="${stateColor}" stroke-width="1.5"/>
            <text x="295" y="78" fill="#38bdf8" font-size="12" font-weight="bold">State Equilibrium:</text>
            
            <text x="295" y="105" fill="#94a3b8" font-size="10">Current Temperature:</text>
            <text x="295" y="125" fill="#f8fafc" font-size="15" font-weight="bold">${tempC}°C</text>

            <text x="295" y="152" fill="#94a3b8" font-size="10">Dominant Factor:</text>
            <text x="295" y="172" fill="#facc15" font-size="11" font-weight="bold">
              ${isSolid ? 'Interparticle Attraction Wins' : isGas ? 'Thermal Energy Overwhelms' : 'Forces in Balance'}
            </text>

            <text x="295" y="205" fill="#94a3b8" font-size="10">Resulting Phase:</text>
            <text x="295" y="230" fill="${stateColor}" font-size="16" font-weight="800">${stateName}</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Temperature (°C):</span>
          <input type="range" class="sim-slider" id="sliderTemp" min="-30" max="150" step="5" value="${tempC}">
          <span class="control-value" id="valTemp">${tempC}°C</span>
        </div>
      `;

      document.getElementById('sliderTemp').oninput = (e) => {
        tempC = parseInt(e.target.value);
        document.getElementById('valTemp').textContent = `${tempC}°C`;
        updateSim();
      };

      updateSim();
    }

    // 6. SOLID STATE LATTICE & FIXED-SITE VIBRATIONS
    function simSolidLatticeVibration(canvas, controls, title, icon) {
      title.textContent = "Solid Lattice: Fixed-Site Vibrations";
      icon.textContent = "🧱";

      let heatAmp = 3; // px vibration

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Fixed Lattice Grid with Anchor Dots -->
            <g transform="translate(140, 150)">
              <!-- Lattice Connectors -->
              <line x1="-60" y1="-60" x2="60" y2="-60" stroke="#475569" stroke-width="2"/>
              <line x1="-60" y1="0" x2="60" y2="0" stroke="#475569" stroke-width="2"/>
              <line x1="-60" y1="60" x2="60" y2="60" stroke="#475569" stroke-width="2"/>
              <line x1="-60" y1="-60" x2="-60" y2="60" stroke="#475569" stroke-width="2"/>
              <line x1="0" y1="-60" x2="0" y2="60" stroke="#475569" stroke-width="2"/>
              <line x1="60" y1="-60" x2="60" y2="60" stroke="#475569" stroke-width="2"/>

              <!-- Vibrating Particles with motion blurs -->
              ${[-60, 0, 60].map(x => [-60, 0, 60].map(y => `
                <circle cx="${x}" cy="${y}" r="2" fill="#64748b"/>
                <ellipse cx="${x + (x*y % 3) * heatAmp * 0.2}" cy="${y}" rx="${12 + heatAmp*0.5}" ry="${12}" fill="#0284c7" stroke="#38bdf8" opacity="0.9"/>
              `)).flat().join('')}
            </g>

            <!-- Metrics Panel -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Solid Architecture:</text>
            
            <text x="295" y="110" fill="#94a3b8" font-size="10">Arrangement:</text>
            <text x="295" y="128" fill="#f8fafc" font-size="13" font-weight="bold">Orderly 3D Lattice</text>

            <text x="295" y="155" fill="#94a3b8" font-size="10">Translational Motion:</text>
            <text x="295" y="175" fill="#f43f5e" font-size="14" font-weight="bold">ZERO (Locked)</text>

            <text x="295" y="205" fill="#94a3b8" font-size="10">Oscillatory Vibration:</text>
            <text x="295" y="225" fill="#34d399" font-size="13" font-weight="bold">± ${heatAmp} nm Amplitude</text>
            <text x="295" y="250" fill="#38bdf8" font-size="8">Result: Definite Shape & Definite Volume</text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Thermal Vibration Amplitude:</span>
          <input type="range" class="sim-slider" id="sliderAmp" min="1" max="8" step="1" value="${heatAmp}">
          <span class="control-value" id="valAmp">${heatAmp} units</span>
        </div>
      `;

      document.getElementById('sliderAmp').oninput = (e) => {
        heatAmp = parseInt(e.target.value);
        document.getElementById('valAmp').textContent = `${heatAmp} units`;
        updateSim();
      };

      updateSim();
    }

    // 7. SOLID MELTING POINT PHASE TRANSITION
    function simSolidMeltingThreshold(canvas, controls, title, icon) {
      title.textContent = "Melting Point: Overcoming Fixed Attractions";
      icon.textContent = "🌡️";

      let heatLevel = 0; // 0 to 100

      function updateSim() {
        const isMelted = (heatLevel >= 50);

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Hot Plate Heater -->
            <rect x="80" y="230" width="160" height="20" rx="4" fill="#334155" stroke="#64748b"/>
            ${heatLevel > 20 ? `<rect x="85" y="232" width="150" height="16" fill="#ef4444" opacity="${heatLevel/100}"/>` : ''}
            <text x="160" y="265" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Heating Element</text>

            <!-- Ice Cube or Liquid Puddle -->
            <g transform="translate(160, 180)">
              ${!isMelted ? `
                <!-- Solid Ice Block -->
                <rect x="-40" y="-45" width="80" height="80" rx="6" fill="rgba(56, 189, 248, 0.4)" stroke="#38bdf8" stroke-width="2"/>
                <text x="0" y="0" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">Solid Ice</text>
                <text x="0" y="16" fill="#7dd3fc" font-size="9" text-anchor="middle">T ≤ 0°C</text>
              ` : `
                <!-- Melted Liquid Puddle -->
                <ellipse cx="0" cy="30" rx="65" ry="15" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="0" y="34" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Liquid Water</text>
              `}
            </g>

            <!-- Melting Calculus -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Phase Transition:</text>
            
            <text x="295" y="110" fill="#94a3b8" font-size="10">Applied Thermal Heat:</text>
            <text x="295" y="128" fill="#facc15" font-size="14" font-weight="bold">${heatLevel} kJ / kg</text>

            <text x="295" y="155" fill="#94a3b8" font-size="10">Melting Point:</text>
            <text x="295" y="178" fill="#38bdf8" font-size="16" font-weight="800">0°C (273.15 K)</text>

            <text x="295" y="210" fill="#cbd5e1" font-size="10">
              ${isMelted ? '✔ Thermal vibrations exceed lattice binding forces: Solid collapses to fluid!' : 'Solid absorbs sensible heat until reaching 0°C.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Heat Energy Added:</span>
          <input type="range" class="sim-slider" id="sliderMelt" min="0" max="100" step="5" value="${heatLevel}">
          <span class="control-value" id="valMelt">${heatLevel}%</span>
        </div>
      `;

      document.getElementById('sliderMelt').oninput = (e) => {
        heatLevel = parseInt(e.target.value);
        document.getElementById('valMelt').textContent = `${heatLevel}%`;
        updateSim();
      };

      updateSim();
    }

    // 8. LIQUID STATE: CONTAINER CONFORMITY & FLUIDITY
    function simLiquidFluidFlow(canvas, controls, title, icon) {
      title.textContent = "Liquid State: Container Conformity & Fluidity";
      icon.textContent = "🌊";

      let vessel = 'cylinder'; // 'cylinder', 'flask', 'bowl'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Vessel Geometry -->
            <g transform="translate(160, 160)">
              ${vessel === 'cylinder' ? `
                <rect x="-40" y="-80" width="80" height="150" fill="none" stroke="#38bdf8" stroke-width="3" rx="4"/>
                <rect x="-38" y="-10" width="76" height="78" fill="#0284c7" opacity="0.6"/>
                <text x="0" y="100" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Tall Cylinder</text>
              ` : vessel === 'flask' ? `
                <path d="M -15 -80 L -15 -40 L -60 70 L 60 70 L 15 -40 L 15 -80 Z" fill="none" stroke="#38bdf8" stroke-width="3"/>
                <polygon points="-42,30 -60,68 60,68 42,30" fill="#0284c7" opacity="0.6"/>
                <text x="0" y="100" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Conical Flask</text>
              ` : `
                <path d="M -80 -20 C -80 70 80 70 80 -20" fill="none" stroke="#38bdf8" stroke-width="3"/>
                <path d="M -70 10 C -70 65 70 65 70 10 Z" fill="#0284c7" opacity="0.6"/>
                <text x="0" y="100" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Wide Bowl</text>
              `}
            </g>

            <!-- Metrics Panel -->
            <rect x="290" y="50" width="170" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="305" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Fluidity Properties:</text>
            
            <text x="305" y="110" fill="#94a3b8" font-size="10">Liquid Volume:</text>
            <text x="305" y="128" fill="#34d399" font-size="14" font-weight="bold">150 mL (CONSTANT)</text>

            <text x="305" y="155" fill="#94a3b8" font-size="10">Geometric Shape:</text>
            <text x="305" y="175" fill="#facc15" font-size="12" font-weight="bold">Matches Container</text>

            <text x="305" y="210" fill="#cbd5e1" font-size="9">
              Particles slide over one another easily, allowing liquid to take any vessel contour.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${vessel === 'cylinder' ? 'active' : ''}" id="btnCyl">🍶 Tall Cylinder</button>
          <button class="btn-sim ${vessel === 'flask' ? 'active' : ''}" id="btnFlask">🧪 Conical Flask</button>
          <button class="btn-sim ${vessel === 'bowl' ? 'active' : ''}" id="btnBowl">🥣 Wide Bowl</button>
        </div>
      `;

      document.getElementById('btnCyl').onclick = () => { vessel = 'cylinder'; updateSim(); };
      document.getElementById('btnFlask').onclick = () => { vessel = 'flask'; updateSim(); };
      document.getElementById('btnBowl').onclick = () => { vessel = 'bowl'; updateSim(); };

      updateSim();
    }

    // 9. BOILING VS SURFACE EVAPORATION
    function simBoilingVsEvaporation(canvas, controls, title, icon) {
      title.textContent = "Boiling (Bulk) vs. Evaporation (Surface)";
      icon.textContent = "💨";

      let mode = 'evaporation'; // 'evaporation' or 'boiling'

      function updateSim() {
        const isBoil = (mode === 'boiling');

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Beaker Container -->
            <rect x="70" y="70" width="170" height="170" fill="none" stroke="#38bdf8" stroke-width="2" rx="4"/>
            <rect x="72" y="120" width="166" height="118" fill="#0284c7" opacity="0.4"/>

            ${isBoil ? `
              <!-- Boiling: Bunsen burner flame beneath -->
              <polygon points="140,270 155,242 170,270" fill="#f59e0b"/>
              <polygon points="148,270 155,250 162,270" fill="#ef4444"/>
              
              <!-- Bubbles forming inside bulk liquid -->
              <circle cx="110" cy="200" r="8" fill="#fff" opacity="0.8"/>
              <circle cx="170" cy="180" r="12" fill="#fff" opacity="0.8"/>
              <circle cx="140" cy="140" r="15" fill="#fff" opacity="0.8"/>
              <text x="155" y="225" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Bulk Bubbling Throughout!</text>
            ` : `
              <!-- Evaporation: Gentle quiet surface escape -->
              <path d="M 100 110 Q 110 90 100 70" fill="none" stroke="#38bdf8" stroke-width="2"/>
              <path d="M 150 110 Q 160 90 150 70" fill="none" stroke="#38bdf8" stroke-width="2"/>
              <path d="M 200 110 Q 210 90 200 70" fill="none" stroke="#38bdf8" stroke-width="2"/>
              <text x="155" y="150" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Quiet Surface Escape</text>
            `}

            <!-- Comparison Dashboard -->
            <rect x="270" y="50" width="190" height="220" rx="10" fill="#1e293b" stroke="${isBoil ? '#f43f5e' : '#38bdf8'}" stroke-width="1.5"/>
            <text x="285" y="80" fill="#38bdf8" font-size="12" font-weight="bold">${isBoil ? 'Boiling Phenomenon:' : 'Evaporation Phenomenon:'}</text>
            
            <text x="285" y="110" fill="#94a3b8" font-size="10">Operating Temperature:</text>
            <text x="285" y="130" fill="${isBoil ? '#f43f5e' : '#34d399'}" font-size="14" font-weight="bold">
              ${isBoil ? 'Fixed at 100°C (Boiling Point)' : 'Any Temp below 100°C'}
            </text>

            <text x="285" y="160" fill="#94a3b8" font-size="10">Site of Vaporization:</text>
            <text x="285" y="180" fill="#facc15" font-size="12" font-weight="bold">
              ${isBoil ? 'Entire Bulk Liquid' : 'Only Exposed Surface'}
            </text>

            <text x="285" y="215" fill="#cbd5e1" font-size="9">
              ${isBoil ? 'Vigorous bubbling as vapour pressure equals atmospheric pressure.' : 'Higher-kinetic particles break surface tension quietly, cooling the liquid.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${mode === 'evaporation' ? 'active' : ''}" id="btnEvap">🌊 Surface Evaporation (&lt; 100°C)</button>
          <button class="btn-sim ${mode === 'boiling' ? 'active' : ''}" id="btnBoil">🔥 Bulk Boiling (at 100°C)</button>
        </div>
      `;

      document.getElementById('btnEvap').onclick = () => { mode = 'evaporation'; updateSim(); };
      document.getElementById('btnBoil').onclick = () => { mode = 'boiling'; updateSim(); };

      updateSim();
    }

    // 10. GAS EXPANSION & RANDOM MOTION
    function simGasExpansionPressure(canvas, controls, title, icon) {
      title.textContent = "Gas State: Chaotic Velocity & Container Expansion";
      icon.textContent = "🎈";

      let hasLid = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Chamber Walls -->
            <rect x="60" y="60" width="180" height="180" fill="none" stroke="#38bdf8" stroke-width="3" rx="4"/>
            
            <!-- Chamber Lid (removable) -->
            ${hasLid ? `
              <rect x="55" y="54" width="190" height="12" fill="#f59e0b" rx="3"/>
              <text x="150" y="48" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">LID CLOSED</text>
            ` : `
              <text x="150" y="48" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">LID REMOVED: GAS ESCAPING!</text>
            `}

            <!-- Gas Particles flying -->
            ${hasLid ? `
              <circle cx="80" cy="90" r="5" fill="#f43f5e"/> <line x1="80" y1="90" x2="105" y2="110" stroke="#f43f5e"/>
              <circle cx="130" cy="150" r="5" fill="#f43f5e"/> <line x1="130" y1="150" x2="160" y2="130" stroke="#f43f5e"/>
              <circle cx="190" cy="80" r="5" fill="#f43f5e"/> <line x1="190" y1="80" x2="210" y2="110" stroke="#f43f5e"/>
              <circle cx="100" cy="200" r="5" fill="#f43f5e"/> <line x1="100" y1="200" x2="80" y2="170" stroke="#f43f5e"/>
              <circle cx="180" cy="210" r="5" fill="#f43f5e"/> <line x1="180" y1="210" x2="150" y2="220" stroke="#f43f5e"/>
            ` : `
              <!-- Flying outside chamber -->
              <circle cx="40" cy="40" r="5" fill="#f43f5e"/>
              <circle cx="150" cy="20" r="5" fill="#f43f5e"/>
              <circle cx="280" cy="40" r="5" fill="#f43f5e"/>
              <circle cx="100" cy="180" r="5" fill="#f43f5e"/>
              <circle cx="190" cy="120" r="5" fill="#f43f5e"/>
            `}

            <!-- Metrics Panel -->
            <rect x="270" y="50" width="190" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="285" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Gaseous Dynamics:</text>
            
            <text x="285" y="110" fill="#94a3b8" font-size="10">Particle Velocity:</text>
            <text x="285" y="130" fill="#34d399" font-size="15" font-weight="bold">~400 to 500 m/s</text>

            <text x="285" y="160" fill="#94a3b8" font-size="10">Interparticle Spaces:</text>
            <text x="285" y="180" fill="#facc15" font-size="13" font-weight="bold">Maximum (99.9% Void)</text>

            <text x="285" y="215" fill="#cbd5e1" font-size="9">
              ${hasLid ? 'Continuous collisions with walls produce measurable gas pressure.' : 'Without boundaries, gas expands infinitely into available space!'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${hasLid ? 'active' : ''}" id="btnLid">
          ${hasLid ? '🚪 Remove Container Lid (Release Gas)' : '🔒 Seal Container Lid'}
        </button>
      `;

      document.getElementById('btnLid').onclick = () => {
        hasLid = !hasLid;
        updateSim();
      };

      updateSim();
    }

    // 11. THREE SYRINGES COMPRESSIBILITY
    function simSyringeCompressibility(canvas, controls, title, icon) {
      title.textContent = "Syringe Compressibility: Solids vs. Liquids vs. Gases";
      icon.textContent = "💉";

      let material = 'gas'; // 'solid', 'liquid', 'gas'

      function updateSim() {
        const pistonY = (material === 'solid') ? 70 : (material === 'liquid') ? 72 : 150;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Medical Syringe Barrel -->
            <rect x="120" y="70" width="80" height="150" fill="none" stroke="#38bdf8" stroke-width="2"/>
            <!-- Sealed Nozzle -->
            <rect x="150" y="220" width="20" height="30" fill="#334155" stroke="#38bdf8"/>
            <rect x="140" y="250" width="40" height="15" fill="#ef4444" rx="3"/>
            <text x="160" y="262" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">SEALED</text>

            <!-- Contents inside syringe -->
            <rect x="122" y="${pistonY}" width="76" height="${220 - pistonY}" fill="${material === 'solid' ? '#78350f' : material === 'liquid' ? '#0284c7' : 'rgba(244, 63, 94, 0.2)'}"/>

            <!-- Piston Assembly -->
            <rect x="110" y="${pistonY - 14}" width="100" height="14" fill="#64748b" stroke="#cbd5e1" rx="2"/>
            <rect x="150" y="${pistonY - 60}" width="20" height="50" fill="#94a3b8"/>
            <rect x="130" y="${pistonY - 70}" width="60" height="12" fill="#cbd5e1" rx="3"/>
            <text x="160" y="${pistonY - 40}" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Thumb</text>

            <!-- Metrics Panel -->
            <rect x="270" y="50" width="190" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="285" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Compressibility Test:</text>
            
            <text x="285" y="110" fill="#94a3b8" font-size="10">Test Medium:</text>
            <text x="285" y="130" fill="#facc15" font-size="13" font-weight="bold">
              ${material === 'solid' ? 'Solid Chalk Pieces' : material === 'liquid' ? 'Liquid Water' : 'Gaseous Air'}
            </text>

            <text x="285" y="160" fill="#94a3b8" font-size="10">Volume Reduction:</text>
            <text x="285" y="185" fill="${material === 'gas' ? '#34d399' : '#f43f5e'}" font-size="18" font-weight="800">
              ${material === 'solid' ? '0% (Incompressible)' : material === 'liquid' ? '< 0.1% (Incompressible)' : '65% (Highly Compressible!)'}
            </text>

            <text x="285" y="220" fill="#cbd5e1" font-size="9">
              ${material === 'gas' ? 'Vast empty space between gas particles is easily squeezed.' : 'Particles already touch; cannot be squeezed closer.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${material === 'solid' ? 'active' : ''}" id="btnChalk">🧱 Syringe 1: Chalk (Solid)</button>
          <button class="btn-sim ${material === 'liquid' ? 'active' : ''}" id="btnWater">💧 Syringe 2: Water (Liquid)</button>
          <button class="btn-sim ${material === 'gas' ? 'active' : ''}" id="btnAir">💨 Syringe 3: Air (Gas)</button>
        </div>
      `;

      document.getElementById('btnChalk').onclick = () => { material = 'solid'; updateSim(); };
      document.getElementById('btnWater').onclick = () => { material = 'liquid'; updateSim(); };
      document.getElementById('btnAir').onclick = () => { material = 'gas'; updateSim(); };

      updateSim();
    }

    // 12. POTASSIUM PERMANGANATE DIFFUSION
    function simPotassiumPermanganate(canvas, controls, title, icon) {
      title.textContent = "Liquid Diffusion: KMnO₄ Crystal Dissolution";
      icon.textContent = "🧪";

      let diffProgress = 40; // 0 to 100

      function updateSim() {
        const opacity = (diffProgress / 100) * 0.7;

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Glass Beaker of Still Water -->
            <rect x="70" y="70" width="170" height="170" rx="4" fill="none" stroke="#38bdf8" stroke-width="2"/>
            <rect x="72" y="90" width="166" height="148" fill="#0284c7" opacity="0.25"/>

            <!-- Diffusing Purple Clouds -->
            <rect x="72" y="90" width="166" height="148" fill="#a855f7" opacity="${opacity}"/>

            <!-- KMnO4 Crystal at bottom -->
            <polygon points="150,235 155,225 160,235" fill="#581c87" stroke="#7e22ce"/>

            <!-- Purple Trails spreading -->
            <path d="M 155 225 Q 130 180 120 140" fill="none" stroke="#a855f7" stroke-width="4" opacity="0.8"/>
            <path d="M 155 225 Q 170 170 190 130" fill="none" stroke="#a855f7" stroke-width="4" opacity="0.8"/>

            <!-- Dashboard -->
            <rect x="270" y="50" width="190" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="285" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Spontaneous Diffusion:</text>
            
            <text x="285" y="110" fill="#94a3b8" font-size="10">Dispersion Progress:</text>
            <text x="285" y="130" fill="#c084fc" font-size="15" font-weight="bold">${diffProgress}% Homogeneous</text>

            <text x="285" y="160" fill="#94a3b8" font-size="10">Driving Mechanism:</text>
            <text x="285" y="180" fill="#facc15" font-size="11" font-weight="bold">Water Particle Collisions</text>

            <text x="285" y="215" fill="#cbd5e1" font-size="9">
              Water particles continuously strike KMnO₄ crystal, dislodging particles that weave into voids.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Diffusion Time Elapsed:</span>
          <input type="range" class="sim-slider" id="sliderDiff" min="0" max="100" step="5" value="${diffProgress}">
          <span class="control-value" id="valDiff">${diffProgress}%</span>
        </div>
      `;

      document.getElementById('sliderDiff').oninput = (e) => {
        diffProgress = parseInt(e.target.value);
        document.getElementById('valDiff').textContent = `${diffProgress}%`;
        updateSim();
      };

      updateSim();
    }

    // 13. THERMAL INFLUENCE ON DIFFUSION
    function simTempDiffusionRate(canvas, controls, title, icon) {
      title.textContent = "Thermal Rate of Diffusion: 5°C vs. 25°C vs. 80°C";
      icon.textContent = "⏱️";

      let timeS = 10; // seconds

      function updateSim() {
        const iceOp = Math.min(0.7, (timeS * 0.01));
        const roomOp = Math.min(0.7, (timeS * 0.035));
        const hotOp = Math.min(0.7, (timeS * 0.08));

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Beaker 1: Ice Cold (5°C) -->
            <g transform="translate(60, 80)">
              <rect x="0" y="0" width="90" height="120" fill="none" stroke="#38bdf8" stroke-width="2" rx="3"/>
              <rect x="2" y="30" width="86" height="88" fill="#0284c7" opacity="0.3"/>
              <rect x="2" y="30" width="86" height="88" fill="#a855f7" opacity="${iceOp}"/>
              <polygon points="40,116 45,108 50,116" fill="#581c87"/>
              <text x="45" y="140" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Ice-Cold (5°C)</text>
              <text x="45" y="155" fill="#94a3b8" font-size="8" text-anchor="middle">Sluggish Diffusion</text>
            </g>

            <!-- Beaker 2: Room Temp (25°C) -->
            <g transform="translate(180, 80)">
              <rect x="0" y="0" width="90" height="120" fill="none" stroke="#38bdf8" stroke-width="2" rx="3"/>
              <rect x="2" y="30" width="86" height="88" fill="#0284c7" opacity="0.3"/>
              <rect x="2" y="30" width="86" height="88" fill="#a855f7" opacity="${roomOp}"/>
              <polygon points="40,116 45,108 50,116" fill="#581c87"/>
              <text x="45" y="140" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Room (25°C)</text>
              <text x="45" y="155" fill="#94a3b8" font-size="8" text-anchor="middle">Moderate Spreading</text>
            </g>

            <!-- Beaker 3: Hot Water (80°C) -->
            <g transform="translate(300, 80)">
              <rect x="0" y="0" width="90" height="120" fill="none" stroke="#f43f5e" stroke-width="2" rx="3"/>
              <rect x="2" y="30" width="86" height="88" fill="#0284c7" opacity="0.3"/>
              <rect x="2" y="30" width="86" height="88" fill="#a855f7" opacity="${hotOp}"/>
              <polygon points="40,116 45,108 50,116" fill="#581c87"/>
              <text x="45" y="140" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">Hot (80°C)</text>
              <text x="45" y="155" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Rapid Diffusion!</text>
            </g>

            <!-- Bottom Summary -->
            <rect x="40" y="260" width="420" height="30" rx="4" fill="#1e293b"/>
            <text x="250" y="280" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">
              Rule: Higher Temperature ⟹ Greater Kinetic Energy ⟹ Faster Rate of Diffusion
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div class="control-row">
          <span class="control-label">Time Elapsed (seconds):</span>
          <input type="range" class="sim-slider" id="sliderTime" min="1" max="25" step="1" value="${timeS}">
          <span class="control-value" id="valTime">${timeS} s</span>
        </div>
      `;

      document.getElementById('sliderTime').oninput = (e) => {
        timeS = parseInt(e.target.value);
        document.getElementById('valTime').textContent = `${timeS} s`;
        updateSim();
      };

      updateSim();
    }

    // 14. GASEOUS DIFFUSION & INCENSE AROMA
    function simIncenseGasDiffusion(canvas, controls, title, icon) {
      title.textContent = "Gaseous Diffusion: Incense Stick in Room";
      icon.textContent = "🪔";

      let isLit = true;

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Room Layout -->
            <rect x="40" y="40" width="420" height="230" fill="none" stroke="#475569" stroke-width="2" rx="4"/>
            <text x="250" y="65" fill="#64748b" font-size="11" text-anchor="middle">Large Classroom (Air: N₂ & O₂)</text>

            <!-- Incense Stick in Left Corner -->
            <g transform="translate(80, 220)">
              <!-- Stand -->
              <rect x="-15" y="0" width="30" height="8" fill="#78350f" rx="2"/>
              <!-- Slanted Stick -->
              <line x1="0" y1="0" x2="30" y2="-60" stroke="#b45309" stroke-width="3"/>
              
              ${isLit ? `
                <!-- Glowing Red Tip -->
                <circle cx="30" cy="-60" r="4" fill="#ef4444" filter="drop-shadow(0 0 6px #f59e0b)"/>
                
                <!-- Expanding Aroma Wave Trails across room -->
                <path d="M 30 -60 Q 90 -100 180 -80 Q 280 -60 380 -80" fill="none" stroke="#a855f7" stroke-width="4" opacity="0.6" stroke-dasharray="8,4"/>
                <path d="M 30 -60 Q 120 -40 220 -30 Q 320 -20 400 -10" fill="none" stroke="#a855f7" stroke-width="3" opacity="0.5" stroke-dasharray="6,4"/>
              ` : ''}
              <text x="0" y="20" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">Incense Stick</text>
            </g>

            <!-- Student Observer in Opposite Right Corner -->
            <g transform="translate(420, 180)">
              <circle cx="0" cy="-25" r="10" fill="#38bdf8"/>
              <line x1="0" y1="-15" x2="0" y2="15" stroke="#38bdf8" stroke-width="3"/>
              <line x1="0" y1="15" x2="-8" y2="35" stroke="#38bdf8" stroke-width="3"/>
              <line x1="0" y1="15" x2="8" y2="35" stroke="#38bdf8" stroke-width="3"/>
              
              <text x="0" y="50" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Student</text>
              ${isLit ? `
                <text x="0" y="-42" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">👃 Smells Aroma!</text>
              ` : `
                <text x="0" y="-42" fill="#94a3b8" font-size="9" text-anchor="middle">No scent detected</text>
              `}
            </g>

            <!-- Banner -->
            <rect x="40" y="240" width="420" height="25" fill="#1e293b"/>
            <text x="250" y="257" fill="#cbd5e1" font-size="9" font-weight="bold" text-anchor="middle">
              ${isLit ? 'Aroma particles travel at ~400 m/s, diffusing via billions of air collisions to reach the nose!' : 'Unlit incense aroma remains localized within centimetres.'}
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <button class="btn-sim ${isLit ? 'active' : ''}" id="btnIncense">
          ${isLit ? '💨 Extinguish Incense Stick' : '🔥 Light Incense Stick (Agarbatti)'}
        </button>
      `;

      document.getElementById('btnIncense').onclick = () => {
        isLit = !isLit;
        updateSim();
      };

      updateSim();
    }

    // 15. ATOMS: ELEMENTAL CONSTITUENTS
    function simElementalAtoms(canvas, controls, title, icon) {
      title.textContent = "Elemental Constituents: Pure Atomic Structure";
      icon.textContent = "⚛️";

      let element = 'gold'; // 'gold', 'iron', 'helium'

      function updateSim() {
        const color = (element === 'gold') ? "#facc15" : (element === 'iron') ? "#94a3b8" : "#38bdf8";
        const sym = (element === 'gold') ? "Au" : (element === 'iron') ? "Fe" : "He";
        const name = (element === 'gold') ? "24-Karat Pure Gold (Au)" : (element === 'iron') ? "Pure Iron Lattice (Fe)" : "Helium Gas (He)";

        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Atomic Lattice / Free Atoms View -->
            <g transform="translate(160, 150)">
              ${element === 'helium' ? `
                <!-- Free monoatomic spheres -->
                <circle cx="-60" cy="-40" r="14" fill="${color}"/> <text x="-60" y="-36" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="40" cy="-20" r="14" fill="${color}"/> <text x="40" y="-16" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="-20" cy="40" r="14" fill="${color}"/> <text x="-20" y="44" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="50" cy="50" r="14" fill="${color}"/> <text x="50" y="54" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">${sym}</text>
              ` : `
                <!-- Tightly packed metal atoms -->
                <circle cx="-40" cy="-40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="-40" y="-36" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="0" cy="-40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="0" y="-36" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="40" cy="-40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="40" y="-36" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>

                <circle cx="-40" cy="0" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="-40" y="4" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="0" cy="0" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="0" y="4" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="40" cy="0" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="40" y="4" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>

                <circle cx="-40" cy="40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="-40" y="44" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="0" cy="40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="0" y="44" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
                <circle cx="40" cy="40" r="18" fill="${color}" stroke="#fff" stroke-width="1.5"/> <text x="40" y="44" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">${sym}</text>
              `}
            </g>

            <!-- Information Panel -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Atomic Element:</text>
            
            <text x="295" y="110" fill="#94a3b8" font-size="10">Substance Name:</text>
            <text x="295" y="128" fill="${color}" font-size="13" font-weight="bold">${name}</text>

            <text x="295" y="155" fill="#94a3b8" font-size="10">Constituent Nature:</text>
            <text x="295" y="175" fill="#34d399" font-size="12" font-weight="bold">Identical Atoms Only</text>

            <text x="295" y="210" fill="#cbd5e1" font-size="9">
              An element cannot be broken into simpler substances by ordinary chemical means because it consists of one atomic species.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${element === 'gold' ? 'active' : ''}" id="btnGold">🥇 Gold (Au)</button>
          <button class="btn-sim ${element === 'iron' ? 'active' : ''}" id="btnIron">🔩 Iron (Fe)</button>
          <button class="btn-sim ${element === 'helium' ? 'active' : ''}" id="btnHe">🎈 Helium (He)</button>
        </div>
      `;

      document.getElementById('btnGold').onclick = () => { element = 'gold'; updateSim(); };
      document.getElementById('btnIron').onclick = () => { element = 'iron'; updateSim(); };
      document.getElementById('btnHe').onclick = () => { element = 'helium'; updateSim(); };

      updateSim();
    }

    // 16. MOLECULES: DIATOMIC GASES & WATER COMPOUND
    function simMoleculesDiatomicWater(canvas, controls, title, icon) {
      title.textContent = "Molecules: Diatomic Elements & Water Compound";
      icon.textContent = "🔬";

      let molType = 'water'; // 'hydrogen', 'oxygen', 'water'

      function updateSim() {
        canvas.innerHTML = `
          <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; max-height: 340px;">
            <rect x="20" y="20" width="460" height="280" rx="12" fill="#0f172a" stroke="#38bdf8"/>
            
            <!-- Molecular Model Display -->
            <g transform="translate(160, 150)">
              ${molType === 'water' ? `
                <!-- Water Molecule (H2O): Bent Mickey-Mouse Geometry -->
                <circle cx="0" cy="0" r="28" fill="#ef4444" stroke="#fca5a5" stroke-width="2"/>
                <text x="0" y="5" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">O</text>

                <!-- Hydrogen 1 -->
                <line x1="-15" y1="-15" x2="-35" y2="-35" stroke="#94a3b8" stroke-width="5"/>
                <circle cx="-35" cy="-35" r="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <text x="-35" y="-31" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">H</text>

                <!-- Hydrogen 2 -->
                <line x1="15" y1="-15" x2="35" y2="-35" stroke="#94a3b8" stroke-width="5"/>
                <circle cx="35" cy="-35" r="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <text x="35" y="-31" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">H</text>

                <text x="0" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Water Molecule (H₂O)</text>
              ` : molType === 'hydrogen' ? `
                <!-- Diatomic Hydrogen (H2) -->
                <line x1="-25" y1="0" x2="25" y2="0" stroke="#94a3b8" stroke-width="6"/>
                <circle cx="-25" cy="0" r="18" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <text x="-25" y="4" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">H</text>

                <circle cx="25" cy="0" r="18" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                <text x="25" y="4" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">H</text>

                <text x="0" y="45" fill="#facc15" font-size="12" font-weight="bold" text-anchor="middle">Hydrogen Gas (H₂)</text>
              ` : `
                <!-- Diatomic Oxygen (O2) -->
                <line x1="-28" y1="-5" x2="28" y2="-5" stroke="#ef4444" stroke-width="4"/>
                <line x1="-28" y1="5" x2="28" y2="5" stroke="#ef4444" stroke-width="4"/>
                <circle cx="-28" cy="0" r="22" fill="#ef4444" stroke="#fca5a5" stroke-width="2"/>
                <text x="-28" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">O</text>

                <circle cx="28" cy="0" r="22" fill="#ef4444" stroke="#fca5a5" stroke-width="2"/>
                <text x="28" y="4" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">O</text>

                <text x="0" y="45" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Oxygen Gas (O₂)</text>
              `}
            </g>

            <!-- Molecular Details Panel -->
            <rect x="280" y="50" width="180" height="220" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Molecular Structure:</text>
            
            <text x="295" y="110" fill="#94a3b8" font-size="10">Classification:</text>
            <text x="295" y="128" fill="#facc15" font-size="13" font-weight="bold">
              ${molType === 'water' ? 'Chemical Compound' : 'Diatomic Element'}
            </text>

            <text x="295" y="155" fill="#94a3b8" font-size="10">Formula & Ratio:</text>
            <text x="295" y="175" fill="#34d399" font-size="14" font-weight="bold">
              ${molType === 'water' ? 'H₂O (2 H : 1 O)' : molType === 'hydrogen' ? 'H₂ (2 H atoms)' : 'O₂ (2 O atoms)'}
            </text>

            <text x="295" y="210" fill="#cbd5e1" font-size="9">
              Atoms bond chemically to achieve stable electron configurations, forming stable molecules.
            </text>
          </svg>
        `;
      }

      controls.innerHTML = `
        <div style="display: flex; gap: 0.5rem; justify-content: center;">
          <button class="btn-sim ${molType === 'water' ? 'active' : ''}" id="btnH2O">💧 Water (H₂O)</button>
          <button class="btn-sim ${molType === 'hydrogen' ? 'active' : ''}" id="btnH2">🎈 Hydrogen (H₂)</button>
          <button class="btn-sim ${molType === 'oxygen' ? 'active' : ''}" id="btnO2">💨 Oxygen (O₂)</button>
        </div>
      `;

      document.getElementById('btnH2O').onclick = () => { molType = 'water'; updateSim(); };
      document.getElementById('btnH2').onclick = () => { molType = 'hydrogen'; updateSim(); };
      document.getElementById('btnO2').onclick = () => { molType = 'oxygen'; updateSim(); };

      updateSim();
    }
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_TEMPLATE.replace('__SLIDES_JSON__', SLIDES_JSON).replace('__QUIZ_QUESTIONS_JSON__', QUIZ_QUESTIONS_JSON)

output_path = 'public/animations/class8-science-particles-matter.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {output_path} ({len(final_html)} bytes).")

