# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class7-math-parallel-intersecting-lines.html
Class 7 Mathematics - Chapter 5: Parallel and Intersecting Lines
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Acharya Baudhayana)
- 16 bespoke interactive SVG simulators
- Prominent Key Technical Vocabulary Badges on every content slide
- 32 in-slide checkpoints with instant feedback
- 4 dedicated mastery quiz challenge slides (40 questions total)
- Step-by-step solution pop-up modal (#solutionModal style="display: none;")
- Slide 20 completion banner ("🎉 You have reached the last slide of this chapter!") hiding nextBtn
- Strictly zero occurrences of prohibited textbook titles
"""

import json
import os
import sys

sys.path.insert(0, '.agents')
from class7_math_parallel_intersecting_lines_data import SLIDES_DATA, QUIZ_QUESTIONS
from class7_math_parallel_intersecting_lines_sims import SIMULATORS_JS

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
  <title>NCERT Class 7 Mathematics • Chapter 5: Parallel and Intersecting Lines Master Lab</title>
  
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
      --bg-primary: #070d19;
      --bg-secondary: #0c1527;
      --card-bg: rgba(12, 21, 39, 0.94);
      --card-border: rgba(56, 189, 248, 0.28);
      --accent-blue: #3b82f6;
      --accent-cyan: #38bdf8;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-gold: #fbbf24;
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
      background: radial-gradient(circle at 50% 15%, #0f1f38 0%, var(--bg-primary) 85%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Top Navigation Header */
    .header {
      background: rgba(7, 13, 25, 0.9);
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
      background: linear-gradient(135deg, #1d4ed8, #0284c7);
      color: #eff6ff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.3rem 0.7rem;
      border-radius: 999px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }

    .header-title-box h1 {
      font-size: 1.15rem;
      font-weight: 800;
      color: #f8fafc;
      letter-spacing: -0.01em;
    }

    .header-title-box p {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .slide-counter-pill {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
    }

    /* Main Container */
    .main-container {
      flex: 1;
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      padding: 1.25rem 1.5rem;
      gap: 1rem;
    }

    /* Teacher Avatar & Speech Bar */
    .avatar-speech-bar {
      background: linear-gradient(135deg, rgba(12, 21, 39, 0.95), rgba(30, 58, 138, 0.35));
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
      background: radial-gradient(circle at 35% 35%, #1e3a8a, #070d19);
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
      background: rgba(12, 21, 39, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.65rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .speech-bubble-text {
      font-size: 0.9rem;
      line-height: 1.45;
      color: #e2e8f0;
      font-style: italic;
    }

    .voice-ctrl-btn {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      border-radius: 8px;
      padding: 0.45rem 0.65rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.75rem;
      font-weight: 700;
      transition: all 0.2s;
      flex-shrink: 0;
    }

    .voice-ctrl-btn:hover {
      background: rgba(56, 189, 248, 0.25);
      transform: translateY(-1px);
    }

    /* Content Layout Grid */
    .slide-content-grid {
      display: grid;
      grid-template-columns: 1fr 1.05fr;
      gap: 1.25rem;
      min-height: 570px;
    }

    @media (max-width: 1024px) {
      .slide-content-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Left Card: Theory & Checkpoints */
    .theory-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.35rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      overflow-y: auto;
      max-height: 600px;
    }

    .section-tag {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      margin-bottom: 0.4rem;
    }

    .slide-main-title {
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.3;
      color: #ffffff;
    }

    /* Vocabulary Badges Row */
    .vocab-badges-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-top: 0.3rem;
    }

    .vocab-badge {
      background: rgba(30, 41, 59, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #7dd3fc;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    .theory-body {
      font-size: 0.92rem;
      line-height: 1.6;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .theory-body p {
      margin-bottom: 0;
    }

    .fact-box {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(15, 23, 42, 0.7));
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 12px;
      padding: 0.75rem 1rem;
      font-size: 0.85rem;
      line-height: 1.45;
      color: #fde047;
      display: flex;
      gap: 0.6rem;
      align-items: flex-start;
    }

    .fact-icon {
      font-size: 1.15rem;
      flex-shrink: 0;
    }

    /* In-Slide Checkpoints Section */
    .checkpoints-section {
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 1rem;
      margin-top: auto;
    }

    .checkpoints-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .checkpoint-card {
      background: rgba(12, 21, 39, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 0.75rem;
      margin-bottom: 0.6rem;
    }

    .checkpoint-card:last-child {
      margin-bottom: 0;
    }

    .checkpoint-question {
      font-size: 0.88rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 0.6rem;
      line-height: 1.4;
    }

    .checkpoint-options {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }

    @media (max-width: 600px) {
      .checkpoint-options {
        grid-template-columns: 1fr;
      }
    }

    .chk-btn {
      background: rgba(30, 41, 59, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #e2e8f0;
      border-radius: 8px;
      padding: 0.5rem 0.65rem;
      font-size: 0.82rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .chk-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-1px);
    }

    .chk-btn.correct {
      background: rgba(16, 185, 129, 0.28) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .chk-btn.incorrect {
      background: rgba(239, 68, 68, 0.25) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }

    .checkpoint-feedback {
      margin-top: 0.45rem;
      font-size: 0.78rem;
      line-height: 1.35;
      padding: 0.4rem 0.65rem;
      border-radius: 6px;
      display: none;
    }

    .checkpoint-feedback.visible {
      display: block;
    }

    .checkpoint-feedback.success {
      background: rgba(16, 185, 129, 0.15);
      color: #6ee7b7;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .checkpoint-feedback.error {
      background: rgba(239, 68, 68, 0.15);
      color: #fca5a5;
      border: 1px solid rgba(239, 68, 68, 0.3);
    }

    /* Right Card: Interactive Laboratory Simulator */
    .lab-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 1.35rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      min-height: 570px;
    }

    .lab-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.75rem;
    }

    .lab-header-left {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .lab-badge {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.25rem 0.55rem;
      border-radius: 6px;
    }

    .sim-header-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: #f1f5f9;
    }

    .sim-canvas-area {
      flex: 1;
      background: rgba(7, 13, 25, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.15);
      border-radius: 14px;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 330px;
    }

    .sim-controls-area {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 0.75rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .sim-btn {
      background: rgba(30, 41, 59, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #f8fafc;
      border-radius: 8px;
      padding: 0.45rem 0.85rem;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sim-btn:hover {
      background: rgba(56, 189, 248, 0.25);
      transform: translateY(-1px);
    }

    .sim-btn.active {
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }

    /* Mastery Quiz View (Slides 17 to 20) */
    .quiz-container {
      display: none;
      flex-direction: column;
      gap: 1.25rem;
      max-width: 960px;
      margin: 0 auto;
      width: 100%;
    }

    .quiz-header-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.25rem 1.75rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .quiz-title-area h2 {
      font-size: 1.35rem;
      font-weight: 800;
      color: #ffffff;
    }

    .quiz-score-pill {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 0.45rem 1rem;
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
      padding: 1.25rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .quiz-q-header {
      display: flex;
      align-items: baseline;
      gap: 0.6rem;
    }

    .quiz-q-num {
      background: #0284c7;
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: 6px;
    }

    .quiz-q-text {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f1f5f9;
      line-height: 1.45;
    }

    .quiz-options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
    }

    @media (max-width: 640px) {
      .quiz-options-grid {
        grid-template-columns: 1fr;
      }
    }

    .quiz-opt-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
      border-radius: 8px;
      padding: 0.6rem 0.85rem;
      font-size: 0.85rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.18);
      border-color: rgba(56, 189, 248, 0.4);
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
      font-weight: 700;
    }

    .quiz-opt-btn.incorrect {
      background: rgba(239, 68, 68, 0.25) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }

    .quiz-footer-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 0.6rem;
    }

    .quiz-status-feedback {
      font-size: 0.82rem;
      font-weight: 700;
    }

    .btn-solution-modal {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-solution-modal:hover {
      background: rgba(245, 158, 11, 0.28);
      transform: translateY(-1px);
    }

    /* Step-by-Step Solution Pop-Up Modal */
    #solutionModal {
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }

    .modal-content-card {
      background: #0f172a;
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 18px;
      max-width: 650px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.5rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
    }

    .modal-title {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 1.15rem;
      font-weight: 800;
      color: #fbbf24;
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
      font-size: 1.1rem;
      transition: all 0.2s;
    }

    .btn-close-modal:hover {
      background: rgba(239, 68, 68, 0.3);
      color: #fca5a5;
    }

    .modal-question {
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
      background: rgba(30, 41, 59, 0.6);
      padding: 0.75rem 1rem;
      border-radius: 10px;
      border-left: 3px solid #38bdf8;
    }

    .modal-solution-steps {
      font-size: 0.9rem;
      line-height: 1.6;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .modal-solution-step {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 0.65rem 0.9rem;
      border-radius: 8px;
    }

    /* Bottom Navigation Footer */
    .footer-nav {
      background: rgba(7, 13, 25, 0.92);
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
      background: linear-gradient(135deg, #0284c7, #1d4ed8);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #ffffff;
      border-radius: 10px;
      padding: 0.55rem 1.15rem;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s;
    }

    .nav-btn:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4);
    }

    .nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none !important;
      box-shadow: none !important;
    }

    .jump-select {
      background: #0f172a;
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #e2e8f0;
      padding: 0.5rem 0.9rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      outline: none;
    }

    /* Terminal Slide 20 Notice Banner */
    #lastSlideNotice {
      display: none;
      align-items: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.3));
      border: 1px solid #10b981;
      color: #a7f3d0;
      font-size: 0.85rem;
      font-weight: 800;
      padding: 0.5rem 1.25rem;
      border-radius: 999px;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
      animation: pulseNotice 2s infinite ease-in-out;
    }

    @keyframes pulseNotice {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.02); }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="header">
    <div class="brand-section">
      <div class="badge-chapter">NCERT Class 7 Maths</div>
      <div class="header-title-box">
        <h1>Chapter 5: Parallel and Intersecting Lines</h1>
        <p>Interactive Numerical Laboratory & Conceptual Reasoning</p>
      </div>
    </div>

    <div class="header-actions">
      <div id="slideCounter" class="slide-counter-pill">Slide 1 / 20</div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-container">
    
    <!-- Virtual Avatar & Narration Speech Bar -->
    <section class="avatar-speech-bar" id="avatarSpeechBar">
      <div class="avatar-wrapper">
        <div id="avatarCircle" class="avatar-img-circle">
          <!-- Stylized Ancient Indian Scholar Avatar SVG for Acharya Baudhayana -->
          <svg width="48" height="48" viewBox="0 0 100 100" fill="none">
            <!-- Aura Background Circle -->
            <circle cx="50" cy="50" r="44" fill="#1e3a8a"/>
            <!-- Golden Radiance Glow -->
            <circle cx="50" cy="50" r="41" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 3"/>
            <!-- Saffron Scholarly Uttariya Robes -->
            <path d="M 22,88 C 22,72 36,66 50,66 C 64,66 78,72 78,88 Z" fill="#b45309"/>
            <path d="M 28,88 Q 38,72 50,66 Q 62,72 72,88" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
            <!-- Upavita / Sacred Thread across chest -->
            <line x1="34" y1="70" x2="66" y2="88" stroke="#fef08a" stroke-width="1.5"/>
            <!-- Head & Neck -->
            <circle cx="50" cy="42" r="18" fill="#fed7aa"/>
            <!-- Traditional Tilak / Chandan on forehead -->
            <path d="M 47,33 L 53,33 L 50,38 Z" fill="#dc2626"/>
            <line x1="46" y1="31" x2="54" y2="31" stroke="#fbbf24" stroke-width="1.5"/>
            <!-- Dignified hair & scholar topknot (ushnisha) -->
            <circle cx="50" cy="22" r="7" fill="#1e293b"/>
            <path d="M 32,42 C 32,24 68,24 68,42 C 68,32 60,26 50,26 C 40,26 32,32 32,42 Z" fill="#1e293b"/>
            <!-- Scholar Beard & Mustache -->
            <path d="M 43,49 Q 50,58 57,49 Q 50,53 43,49 Z" fill="#334155"/>
            <!-- Gentle, serene eyes -->
            <circle cx="43" cy="40" r="1.5" fill="#0f172a"/>
            <circle cx="57" cy="40" r="1.5" fill="#0f172a"/>
            <!-- Subtle smiling mouth -->
            <path id="avatarMouth" d="M 46,50 Q 50,54 54,50" stroke="#b45309" stroke-width="1.5" fill="none"/>
            <!-- Small Palm-Leaf Manuscript in hand -->
            <rect x="68" y="72" width="16" height="8" rx="2" fill="#fde047" stroke="#b45309" stroke-width="1"/>
            <line x1="70" y1="76" x2="82" y2="76" stroke="#92400e" stroke-width="0.8"/>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="teacher-meta">
        <div class="teacher-name">
          <span>Acharya Baudhayana</span>
          <span style="font-size:0.75rem;">📜</span>
        </div>
        <div class="teacher-badge">Master of Sulba Sutra Geometry & Cord-Constructions</div>
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
          <span id="slideTag" class="section-tag">2.1 Simple Expressions • Foundations</span>
          <h2 id="slideTitle" class="slide-main-title">Introduction to Simple Arithmetic Expressions</h2>
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
            <span id="simHeaderTitle" class="sim-header-title">Numerical Scale & Mathematical Models</span>
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
          <h2 id="quizTitle" class="slide-main-title">Mastery Challenge: Parallel and Intersecting Lines</h2>
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
          osc.frequency.setValueAtTime(220, now); // A3
          osc.frequency.setValueAtTime(196, now + 0.12); // G3
          gain.gain.setValueAtTime(0.1, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.3);
        } catch(e) {}
      },
      playCelebration() {
        try {
          this.init();
          if (!this.ctx) return;
          const notes = [523.25, 659.25, 783.99, 1046.50];
          notes.forEach((freq, idx) => {
            setTimeout(() => {
              this.playTone(freq, 'triangle', 0.15, 0.12);
            }, idx * 90);
          });
        } catch(e) {}
      }
    };

    // DOM Elements
    const slideCounter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideJumpSelect = document.getElementById('slideJumpSelect');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const avatarCircle = document.getElementById('avatarCircle');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const slideTag = document.getElementById('slideTag');
    const slideTitle = document.getElementById('slideTitle');
    const vocabBadgesRow = document.getElementById('vocabBadgesRow');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsContainer = document.getElementById('checkpointsContainer');

    const labCol = document.getElementById('labCol');
    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simCanvas = document.getElementById('simCanvas');
    const simControls = document.getElementById('simControls');

    const quizContainer = document.getElementById('quizContainer');
    const quizBadge = document.getElementById('quizBadge');
    const quizTitle = document.getElementById('quizTitle');
    const quizScorePill = document.getElementById('quizScorePill');
    const quizItemsList = document.getElementById('quizItemsList');

    const solutionModal = document.getElementById('solutionModal');
    const modalTitleText = document.getElementById('modalTitleText');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');
    const btnCloseModal = document.getElementById('btnCloseModal');

    // Populate Jump Select
    SLIDES_DATA.forEach((slide, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${slide.id}. ${slide.title}`;
      slideJumpSelect.appendChild(opt);
    });

    // Audio Narration Controller
    function stopNarration() {
      if (speechSynth && speechSynth.speaking) {
        speechSynth.cancel();
      }
      isSpeaking = false;
      avatarSpeechBar.classList.remove('is-speaking');
      iconVoicePlay.style.display = 'block';
      iconVoicePause.style.display = 'none';
    }

    function speakNarration(text) {
      stopNarration();
      if (!speechSynth || !text) return;

      const cleanText = text.replace(/<[^>]+>/g, '').replace(/\$+/g, '').replace(/\\times/g, 'times').replace(/\\div/g, 'divided by');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 0.98;
      speechUtterance.pitch = 1.0;

      const voices = speechSynth.getVoices();
      const indianVoice = voices.find(v => v.lang.includes('en-IN')) || voices.find(v => v.lang.includes('en-GB')) || voices.find(v => v.lang.includes('en'));
      if (indianVoice) speechUtterance.voice = indianVoice;

      speechUtterance.onstart = () => {
        isSpeaking = true;
        avatarSpeechBar.classList.add('is-speaking');
        iconVoicePlay.style.display = 'none';
        iconVoicePause.style.display = 'block';
      };

      speechUtterance.onend = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechUtterance.onerror = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechSynth.speak(speechUtterance);
    }

    btnVoiceToggle.addEventListener('click', () => {
      if (isSpeaking) {
        stopNarration();
      } else {
        const slide = SLIDES_DATA[currentSlideIdx];
        if (slide && slide.narration) {
          speakNarration(slide.narration);
        }
      }
    });

    // Checkpoint Renderer
    function renderCheckpoints(checkpoints) {
      checkpointsContainer.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) return;

      checkpoints.forEach((chk, cIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const qText = document.createElement('div');
        qText.className = 'checkpoint-question';
        qText.textContent = `Q${cIdx + 1}. ${chk.question}`;
        card.appendChild(qText);

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
            else if (oIdx === savedAns) btn.classList.add('incorrect');
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
          fb.innerHTML = `
            <span class="fact-icon">💡</span>
            <div><strong>Baudhayana's Sulba Wisdom:</strong> ${slide.fact_box}</div>
          `;
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
        case 'intersecting_lines_scissors_sim':
          simIntersectingLinesScissors();
          break;
        case 'linear_pair_slider_sim':
          simLinearPairSlider();
          break;
        case 'perpendicular_lines_cross_sim':
          simPerpendicularLinesCross();
          break;
        case 'parallel_railway_tracks_sim':
          simParallelRailwayTracks();
          break;
        case 'paper_folding_perpendicular_sim':
          simPaperFoldingPerpendicular();
          break;
        case 'paper_folding_parallel_sim':
          simPaperFoldingParallel();
          break;
        case 'transversal_eight_angles_sim':
          simTransversalEightAngles();
          break;
        case 'corresponding_angles_f_shape_sim':
          simCorrespondingAnglesFShape();
          break;
        case 'parallelism_detector_sim':
          simParallelismDetector();
          break;
        case 'ruler_set_square_construction_sim':
          simRulerSetSquareConstruction();
          break;
        case 'alternate_interior_z_shape_sim':
          simAlternateInteriorZShape();
          break;
        case 'alternate_exterior_angles_sim':
          simAlternateExteriorAngles();
          break;
        case 'co_interior_c_shape_sim':
          simCoInteriorCShape();
          break;
        case 'cafe_wall_illusion_sim':
          simCafeWallIllusion();
          break;
        case 'hering_zollner_illusions_sim':
          simHeringZollnerIllusions();
          break;
        case 'baudhayana_sulba_ropes_sim':
          simBaudhayanaSulbaRopes();
          break;
        default:
          simCanvas.innerHTML = '<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>';
      }
    }

    // Mastery Quiz Slides Renderer (Slides 17 to 20)
    function renderQuizSlide(slide) {
      theoryCol.style.display = 'none';
      labCol.style.display = 'none';
      quizContainer.style.display = 'flex';

      quizBadge.textContent = slide.tag;
      quizTitle.textContent = slide.title;

      const questions = slide.questions || [];
      const slideQuizKey = `quiz_${slide.id}`;
      if (!quizScores[slideQuizKey]) {
        quizScores[slideQuizKey] = { correct: 0, answered: 0, total: questions.length };
      }

      function updateQuizScoreUI() {
        const s = quizScores[slideQuizKey];
        quizScorePill.textContent = `Score: ${s.correct} / ${s.total}`;
        if (s.answered === s.total && s.correct >= 8) {
          sfx.playCelebration();
        }
      }

      quizItemsList.innerHTML = '';
      questions.forEach((q, qIdx) => {
        const card = document.createElement('div');
        card.className = 'quiz-item-card';

        const qHeader = document.createElement('div');
        qHeader.className = 'quiz-q-header';
        qHeader.innerHTML = `
          <span class="quiz-q-num">Q${q.id}</span>
          <span class="quiz-q-text">${q.question}</span>
        `;
        card.appendChild(qHeader);

        const optGrid = document.createElement('div');
        optGrid.className = 'quiz-options-grid';

        const footerAct = document.createElement('div');
        footerAct.className = 'quiz-footer-actions';

        const statusFeedback = document.createElement('span');
        statusFeedback.className = 'quiz-status-feedback';

        const btnSol = document.createElement('button');
        btnSol.className = 'btn-solution-modal';
        btnSol.textContent = '💡 View Step-by-Step Solution';
        btnSol.addEventListener('click', () => {
          openSolutionModal(q);
        });

        footerAct.appendChild(statusFeedback);
        footerAct.appendChild(btnSol);

        const savedAnsKey = `quiz_ans_${q.id}`;
        const savedAns = checkpointAnswers[savedAnsKey];

        q.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.textContent = optText;

          if (savedAns !== undefined) {
            btn.disabled = true;
            if (oIdx === q.correct) btn.classList.add('correct');
            else if (oIdx === savedAns) btn.classList.add('incorrect');
          }

          btn.addEventListener('click', () => {
            checkpointAnswers[savedAnsKey] = oIdx;
            const allBtns = optGrid.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            quizScores[slideQuizKey].answered++;

            if (oIdx === q.correct) {
              btn.classList.add('correct');
              statusFeedback.style.color = '#34d399';
              statusFeedback.textContent = '✓ Correct Answer!';
              quizScores[slideQuizKey].correct++;
              sfx.playCorrect();
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
              statusFeedback.style.color = '#f87171';
              statusFeedback.textContent = '✕ Incorrect';
              sfx.playIncorrect();
            }
            updateQuizScoreUI();
          });
          optGrid.appendChild(btn);
        });

        card.appendChild(optGrid);
        card.appendChild(footerAct);

        if (savedAns !== undefined) {
          if (savedAns === q.correct) {
            statusFeedback.style.color = '#34d399';
            statusFeedback.textContent = '✓ Correct Answer!';
          } else {
            statusFeedback.style.color = '#f87171';
            statusFeedback.textContent = '✕ Incorrect';
          }
        }

        quizItemsList.appendChild(card);
      });

      updateQuizScoreUI();
      if (window.triggerMathRender) triggerMathRender(quizContainer);
    }

    // Modal Solution Opener
    function openSolutionModal(q) {
      modalTitleText.textContent = `Question ${q.id} Detailed Derivation`;
      modalQuestionText.textContent = q.question;
      modalSolutionSteps.innerHTML = '';

      if (q.solution_steps && q.solution_steps.length > 0) {
        q.solution_steps.forEach((step, sIdx) => {
          const sBox = document.createElement('div');
          sBox.className = 'modal-solution-step';
          sBox.innerHTML = `<strong>Step ${sIdx + 1}:</strong> ${step}`;
          modalSolutionSteps.appendChild(sBox);
        });
      } else {
        const sBox = document.createElement('div');
        sBox.className = 'modal-solution-step';
        sBox.textContent = "Full step-by-step arithmetic derivation shown above.";
        modalSolutionSteps.appendChild(sBox);
      }

      solutionModal.style.display = 'flex';
      if (window.triggerMathRender) triggerMathRender(solutionModal);
      sfx.playClick();
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
output_path = 'public/animations/class7-math-parallel-intersecting-lines.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully compiled {output_path} (File size: {os.path.getsize(output_path):,} bytes)")


