# -*- coding: utf-8 -*-
"""
Master Builder Script: Generates public/animations/class7-math-another-peek-beyond-the-point.html
NCERT Class 7 Mathematics - Chapter 12: Another Peek Beyond the Point (Decimals)
Features:
- 20 animated slides with Web Speech API audio narration and virtual teacher avatar (Acharya Madhava of Sangamagrama)
- 16 bespoke interactive SVG simulators
- Prominent Key Technical Vocabulary Badges on every content slide
- 32 in-slide checkpoints with instant feedback
- 4 dedicated mastery quiz challenge slides (40 questions total)
- Step-by-step solution pop-up modal (#solutionModal style="display: none;" with z-index: 99999 !important;)
- Slide 20 completion banner ("🎉 You have reached the last slide of this chapter!") hiding nextBtn
- Strictly zero occurrences of prohibited textbook titles
"""

import json
import os
import sys

sys.path.insert(0, '.agents')
from class7_math_another_peek_beyond_the_point_data import SLIDES_DATA, QUIZ_QUESTIONS
from class7_math_another_peek_beyond_the_point_sims import SIMULATORS
from class7_math_another_peek_beyond_the_point_js import SIMULATORS_JS

# Assemble full slides data
full_slides = []
for slide in SLIDES_DATA:
    s = dict(slide)
    if s.get("quiz_range"):
        start_q, end_q = s["quiz_range"]
        s["questions"] = QUIZ_QUESTIONS[start_q - 1:end_q]
        s["is_quiz"] = True
    else:
        s["is_quiz"] = False
    full_slides.append(s)

SLIDES_JSON = json.dumps(full_slides, ensure_ascii=False)
QUIZ_QUESTIONS_JSON = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)
SIMULATORS_JSON = json.dumps(SIMULATORS, ensure_ascii=False)

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT Class 7 Mathematics • Chapter 12: Decimal Operations Master Lab</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script>
    function triggerMathRender(el) {{
      const target = el || document.body;
      if (typeof renderMathInElement === 'function') {{
        try {{
          renderMathInElement(target, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}},
              {{left: '\\\\[', right: '\\\\]', display: true}},
              {{left: '\\\\(', right: '\\\\)', display: false}}
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
          }});
        }} catch (e) {{
          console.warn('KaTeX render error:', e);
        }}
      }} else {{
        setTimeout(() => triggerMathRender(target), 50);
      }}
    }}
    window.triggerMathRender = triggerMathRender;

    // Fallback Pure-JavaScript Math Beautifier (if KaTeX is delayed or blocked)
    function formatSimpleMath(tex) {{
      let s = tex.trim();
      s = s.replace(/\\\\textbf\\{{([^}}]+)\\}}/g, '<b>$1</b>');
      s = s.replace(/\\\\mathbf\\{{([^}}]+)\\}}/g, '<b>$1</b>');
      s = s.replace(/\\\\text\\{{([^}}]+)\\}}/g, '$1');
      s = s.replace(/\\\\frac\\{{([^}}]+)\\}}\\{{([^}}]+)\\}}/g, '<span style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.1;margin:0 2px;"><span style="display:block;border-bottom:1px solid currentColor;padding:0 2px;">$1</span><span style="display:block;padding:0 2px;">$2</span></span>');
      s = s.replace(/\\\\times/g, '×');
      s = s.replace(/\\\\div/g, '÷');
      s = s.replace(/\\\\cdot/g, '·');
      s = s.replace(/\\\\dots/g, '…');
      s = s.replace(/\\\\cdots/g, '…');
      s = s.replace(/\\\\implies/g, '⇒');
      s = s.replace(/\\\\rightarrow/g, '→');
      s = s.replace(/\\\\leftarrow/g, '←');
      s = s.replace(/\\\\approx/g, '≈');
      s = s.replace(/\\\\le/g, '≤');
      s = s.replace(/\\\\ge/g, '≥');
      s = s.replace(/\\\\lt/g, '&lt;');
      s = s.replace(/\\\\gt/g, '&gt;');
      s = s.replace(/\\\\pi/g, 'π');
      s = s.replace(/\\\\overline\\{{([^}}]+)\\}}/g, '<span style="text-decoration:overline;">$1</span>');
      s = s.replace(/\\\\quad/g, '&nbsp;&nbsp;');
      s = s.replace(/\\\\qquad/g, '&nbsp;&nbsp;&nbsp;&nbsp;');
      return `<span class="math-fallback" style="font-family:'Cambria Math', 'Times New Roman', serif;font-style:italic;">${{s}}</span>`;
    }}

    function fallbackMathBeautify(root) {{
      if (typeof renderMathInElement === 'function') return;
      const target = root || document.body;
      const walker = document.createTreeWalker(target, NodeFilter.SHOW_TEXT, null, false);
      const textNodes = [];
      let node;
      while (node = walker.nextNode()) {{
        if (node.parentElement && ['SCRIPT', 'STYLE', 'TEXTAREA', 'CODE'].includes(node.parentElement.tagName)) continue;
        if (node.nodeValue && node.nodeValue.includes('$')) {{
          textNodes.push(node);
        }}
      }}
      textNodes.forEach(tn => {{
        let text = tn.nodeValue;
        text = text.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m, eq) => formatSimpleMath(eq));
        text = text.replace(/\\$([\\s\\S]*?)\\$/g, (m, eq) => formatSimpleMath(eq));
        if (text !== tn.nodeValue) {{
          const span = document.createElement('span');
          span.innerHTML = text;
          tn.parentNode.replaceChild(span, tn);
        }}
      }});
    }}

    // MutationObserver to auto-render KaTeX on dynamic simulator updates
    let mathObserverTimeout = null;
    const mathObserver = new MutationObserver((mutations) => {{
      let hasMath = false;
      for (const m of mutations) {{
        const el = (m.target && m.target.nodeType === 1) ? m.target : (m.target ? m.target.parentElement : null);
        if (el) {{
          if (el.closest && el.closest('.katex')) continue;
          const txt = el.textContent || '';
          if (txt.includes('$') && !el.querySelector('.katex')) {{
            hasMath = true;
            break;
          }}
        }}
      }}
      if (hasMath) {{
        clearTimeout(mathObserverTimeout);
        mathObserverTimeout = setTimeout(() => {{
          triggerMathRender(document.body);
        }}, 30);
      }}
    }});

    window.addEventListener('DOMContentLoaded', () => {{
      mathObserver.observe(document.body, {{ childList: true, subtree: true, characterData: true }});
      setTimeout(() => fallbackMathBeautify(document.body), 2000);
    }});
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            slate: {{
              850: '#0f172a',
              900: '#0b1120',
              950: '#060a12'
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
      --bg-dark: #070d19;
      --card-bg: rgba(15, 23, 42, 0.85);
      --accent-cyan: #06b6d4;
      --accent-teal: #14b8a6;
      --accent-amber: #f59e0b;
      --accent-indigo: #6366f1;
    }}

    body {{
      background: radial-gradient(circle at 50% 0%, #0d1b2a, var(--bg-dark));
      color: #f1f5f9;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    /* Custom Glassmorphism */
    .glass-panel {{
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }}

    .glass-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
    }}

    /* Header Bar */
    .header-bar {{
      background: rgba(11, 17, 32, 0.95);
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 0;
      z-index: 50;
    }}

    /* Main Container */
    .main-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    /* Teacher Avatar & Speech Bar */
    .avatar-speech-bar {{
      background: linear-gradient(135deg, rgba(12, 21, 39, 0.95), rgba(30, 58, 138, 0.35));
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 16px;
      padding: 0.85rem 1.25rem;
      display: flex;
      align-items: center;
      gap: 1.2rem;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
    }}

    .avatar-wrapper {{
      position: relative;
      flex-shrink: 0;
    }}

    .avatar-img-circle {{
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
    }}

    .avatar-speaking-pulse {{
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 2px solid #38bdf8;
      animation: avatarPulse 1.5s infinite;
      opacity: 0;
      pointer-events: none;
    }}

    .is-speaking .avatar-speaking-pulse {{
      opacity: 1;
    }}

    @keyframes avatarPulse {{
      0% {{ transform: scale(1); opacity: 0.8; }}
      100% {{ transform: scale(1.25); opacity: 0; }}
    }}

    .teacher-meta {{
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      min-width: 170px;
    }}

    .teacher-name {{
      font-weight: 800;
      font-size: 0.95rem;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .teacher-title {{
      font-size: 0.72rem;
      color: #94a3b8;
    }}

    .speech-bubble {{
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 12px;
      padding: 0.65rem 1rem;
      flex-grow: 1;
      font-size: 0.88rem;
      line-height: 1.45;
      color: #e2e8f0;
      position: relative;
    }}

    .speech-bubble::before {{
      content: '';
      position: absolute;
      left: -8px;
      top: 50%;
      transform: translateY(-50%);
      border-width: 6px 8px 6px 0;
      border-style: solid;
      border-color: transparent rgba(56, 189, 248, 0.2) transparent transparent;
    }}

    .voice-toggle-btn {{
      padding: 0.5rem 0.85rem;
      border-radius: 10px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #38bdf8;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
      flex-shrink: 0;
    }}

    .voice-toggle-btn:hover {{
      background: rgba(56, 189, 248, 0.3);
      transform: translateY(-1px);
    }}

    /* Slide Grid Layout */
    .slide-content-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      min-height: 520px;
    }}

    @media (max-width: 1024px) {{
      .slide-content-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Theory Column */
    .theory-col {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      overflow-y: auto;
      max-height: 640px;
    }}

    .slide-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: rgba(20, 184, 166, 0.15);
      color: #2dd4bf;
      border: 1px solid rgba(20, 184, 166, 0.35);
      width: fit-content;
    }}

    .slide-heading {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #f8fafc;
      line-height: 1.35;
    }}

    .theory-body {{
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.6;
    }}

    /* Interactive Checkpoints */
    .checkpoint-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 12px;
      padding: 0.85rem 1rem;
      margin-top: 0.5rem;
    }}

    .checkpoint-title {{
      font-size: 0.78rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      margin-bottom: 0.4rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .checkpoint-question {{
      font-size: 0.85rem;
      font-weight: 600;
      color: #f1f5f9;
      margin-bottom: 0.6rem;
    }}

    .checkpoint-options {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.4rem;
    }}

    @media (max-width: 640px) {{
      .checkpoint-options {{
        grid-template-columns: 1fr;
      }}
    }}

    .checkpoint-btn {{
      padding: 0.45rem 0.75rem;
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      font-size: 0.8rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .checkpoint-btn:hover:not(:disabled) {{
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      color: #f8fafc;
    }}

    .checkpoint-btn.is-correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
    }}

    .checkpoint-btn.is-wrong {{
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fda4af !important;
    }}

    .checkpoint-feedback {{
      margin-top: 0.5rem;
      font-size: 0.78rem;
      line-height: 1.4;
      padding: 0.45rem 0.65rem;
      border-radius: 6px;
      display: none;
    }}

    .checkpoint-feedback.is-correct {{
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }}

    .checkpoint-feedback.is-wrong {{
      display: block;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.3);
      color: #fda4af;
    }}

    /* Laboratory Simulator Column */
    .lab-col {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      overflow-y: auto;
      max-height: 640px;
    }}

    .sim-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }}

    .sim-title {{
      font-size: 0.92rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* Quiz Challenge Cards */
    .quiz-container {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      min-height: 520px;
    }}

    .quiz-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
    }}

    .quiz-score-pill {{
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
      font-weight: 800;
      font-size: 0.85rem;
    }}

    .quiz-items-list {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-height: 540px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .quiz-item-card {{
      background: rgba(30, 41, 59, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}

    .quiz-item-q {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #f1f5f9;
      line-height: 1.4;
    }}

    .quiz-opt-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }}

    @media (max-width: 640px) {{
      .quiz-opt-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .quiz-opt-btn {{
      padding: 0.5rem 0.75rem;
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #cbd5e1;
      font-size: 0.82rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .quiz-opt-btn:hover:not(:disabled) {{
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.4);
      color: #f8fafc;
    }}

    .quiz-opt-btn.is-correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
    }}

    .quiz-opt-btn.is-wrong {{
      background: rgba(244, 63, 94, 0.25) !important;
      border-color: #f43f5e !important;
      color: #fda4af !important;
    }}

    .btn-show-solution {{
      align-self: flex-start;
      margin-top: 0.35rem;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}

    .btn-show-solution:hover {{
      background: rgba(245, 158, 11, 0.28);
      transform: translateY(-1px);
    }}

    /* Step-by-Step Solution Pop-Up Modal (#solutionModal) */
    #solutionModal {{
      position: fixed;
      inset: 0;
      z-index: 99999 !important;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }}

    #solutionModal.is-active {{
      display: flex !important;
    }}

    .modal-content-card {{
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 20px;
      max-width: 680px;
      width: 100%;
      padding: 1.5rem;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      position: relative;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 0.75rem;
      margin-bottom: 1rem;
    }}

    .modal-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .btn-close-modal {{
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #94a3b8;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-close-modal:hover {{
      background: rgba(244, 63, 94, 0.2);
      color: #f43f5e;
    }}

    /* Bottom Navigation Bar */
    .nav-bar {{
      background: rgba(11, 17, 32, 0.95);
      border-top: 1px solid rgba(56, 189, 248, 0.2);
      backdrop-filter: blur(10px);
      position: sticky;
      bottom: 0;
      z-index: 50;
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .nav-btn {{
      padding: 0.55rem 1.25rem;
      border-radius: 10px;
      font-weight: 700;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      cursor: pointer;
      transition: all 0.2s;
      background: #0284c7;
      color: white;
      border: none;
    }}

    .nav-btn:hover:not(:disabled) {{
      background: #0369a1;
      transform: translateY(-1px);
    }}

    .nav-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      background: #334155;
    }}

    .jump-select {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #e2e8f0;
      border-radius: 8px;
      padding: 0.45rem 0.85rem;
      font-size: 0.82rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }}

    .jump-select option {{
      background: #0f172a;
      color: #f8fafc;
    }}

    #lastSlideNotice {{
      display: none;
      align-items: center;
      gap: 0.4rem;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.45rem 1rem;
      border-radius: 10px;
    }}
  </style>
</head>
<body class="dark">

  <!-- Top Header Bar -->
  <header class="header-bar">
    <div class="max-w-[1440px] mx-auto px-6 py-3 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 to-teal-500 flex items-center justify-center font-black text-white text-base shadow-lg shadow-teal-500/20">
          7
        </div>
        <div>
          <div class="text-xs font-bold text-amber-400 uppercase tracking-wider">NCERT Class 7 Mathematics • Chapter 12</div>
          <h1 class="text-sm font-black text-slate-100 tracking-tight sm:text-base">Decimal Operations Master Lab</h1>
        </div>
      </div>
      
      <div class="flex items-center gap-3">
        <div id="slideCounter" class="px-3 py-1 rounded-full bg-slate-800/80 border border-slate-700 text-xs font-bold text-slate-300">
          Slide 1 / 20
        </div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-container">
    
    <!-- Virtual Avatar & Narration Speech Bar -->
    <section class="avatar-speech-bar" id="avatarSpeechBar">
      <div class="avatar-wrapper">
        <div id="avatarCircle" class="avatar-img-circle">
          <!-- Stylized Ancient Indian Scholar Avatar SVG for Acharya Madhava of Sangamagrama -->
          <svg width="48" height="48" viewBox="0 0 100 100" fill="none">
            <!-- Aura Background Circle -->
            <circle cx="50" cy="50" r="44" fill="#d97706" opacity="0.3"/>
            <!-- Golden Radiance Glow -->
            <circle cx="50" cy="50" r="40" fill="url(#madhavaAura)"/>
            <defs>
              <radialGradient id="madhavaAura" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#b45309" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#78350f" stop-opacity="0.95"/>
              </radialGradient>
            </defs>
            <!-- Shoulders & Traditional Kerala Kasavu Robe -->
            <path d="M 20,88 Q 50,72 80,88 L 84,100 L 16,100 Z" fill="#fef3c7"/>
            <path d="M 30,82 Q 50,74 70,82" stroke="#ca8a04" stroke-width="2.5" fill="none"/>
            <path d="M 26,86 L 74,86" stroke="#ca8a04" stroke-width="1.5" fill="none"/>
            <!-- Rudraksha mala -->
            <path d="M 34,78 Q 50,90 66,78" stroke="#78350f" stroke-width="2.5" stroke-dasharray="3,3" fill="none"/>
            <!-- Neck -->
            <rect x="44" y="58" width="12" height="18" fill="#d97706" rx="3"/>
            <!-- Head / Face -->
            <ellipse cx="50" cy="42" rx="19" ry="22" fill="#f59e0b"/>
            <!-- Kuduma / Kerala Scholar Hair Topknot -->
            <circle cx="66" cy="24" r="8" fill="#1e293b"/>
            <ellipse cx="50" cy="23" rx="16" ry="6" fill="#1e293b"/>
            <!-- Forehead Sandalwood Chandan Tilak & Kumkum -->
            <path d="M 44,28 Q 50,33 56,28" stroke="#fef3c7" stroke-width="2" fill="none"/>
            <circle cx="50" cy="29" r="1.5" fill="#dc2626"/>
            <!-- Eyebrows -->
            <path d="M 37,34 Q 43,32 47,34" stroke="#451a03" stroke-width="1.8" fill="none"/>
            <path d="M 53,34 Q 57,32 63,34" stroke="#451a03" stroke-width="1.8" fill="none"/>
            <!-- Eyes -->
            <ellipse cx="42" cy="38" rx="2.5" ry="1.8" fill="#0f172a"/>
            <ellipse cx="58" cy="38" rx="2.5" ry="1.8" fill="#0f172a"/>
            <circle cx="43" cy="37.5" r="0.6" fill="#ffffff"/>
            <circle cx="59" cy="37.5" r="0.6" fill="#ffffff"/>
            <!-- Nose -->
            <path d="M 50,37 L 48,46 L 52,46" stroke="#92400e" stroke-width="1.5" fill="none"/>
            <!-- Gentle Smile Mouth -->
            <path id="avatarMouth" d="M 45,52 Q 50,56 55,52" stroke="#78350f" stroke-width="1.8" fill="none"/>
            <!-- Palm Leaf Manuscript / Astrolabe -->
            <rect x="68" y="58" width="18" height="12" rx="2" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
            <line x1="71" y1="62" x2="83" y2="62" stroke="#854d0e" stroke-width="1"/>
            <line x1="71" y1="66" x2="81" y2="66" stroke="#854d0e" stroke-width="1"/>
          </svg>
        </div>
        <div class="avatar-speaking-pulse"></div>
      </div>

      <div class="teacher-meta">
        <div class="teacher-name">
          <span>Acharya Madhava</span>
          <span class="text-xs">📜</span>
        </div>
        <div class="teacher-title">Pioneer of Decimal Series & Kerala Astronomy</div>
      </div>

      <div class="speech-bubble" id="speechBubbleText">
        <!-- Spoken text injected here -->
      </div>

      <button id="btnVoiceToggle" class="voice-toggle-btn" title="Toggle voice narration">
        <svg id="iconVoicePlay" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <polygon points="5 3 19 12 5 21 5 3"/>
        </svg>
        <svg id="iconVoicePause" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="display:none;">
          <rect x="6" y="4" width="4" height="16"/>
          <rect x="14" y="4" width="4" height="16"/>
        </svg>
        <span>Narration</span>
      </button>
    </section>

    <!-- Standard Slide Grid (Slides 1 to 16) -->
    <section id="slideContentGrid" class="slide-content-grid">
      <!-- Left: Theory & Checkpoints -->
      <div class="theory-col" id="theoryCol">
        <div class="flex items-center justify-between">
          <span id="slideBadge" class="slide-badge-pill">Section 4.1</span>
          <span id="slideSectionTitle" class="text-xs text-slate-400 font-semibold">Decimals</span>
        </div>

        <h2 id="slideTitle" class="slide-heading">Slide Title</h2>

        <div id="theoryBody" class="theory-body">
          <!-- Injected Theory HTML -->
        </div>

        <!-- 2 In-Slide Checkpoint Inquiries -->
        <div id="checkpointsWrapper" class="space-y-3 mt-auto pt-2">
          <!-- Checkpoints injected here -->
        </div>
      </div>

      <!-- Right: Interactive Laboratory Simulator -->
      <div class="lab-col" id="labCol">
        <div class="sim-header">
          <div class="sim-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2">
              <path d="M10 2v7.31L4.69 16.5A4 4 0 0 0 8 22h8a4 4 0 0 0 3.31-5.5L14 9.31V2"/>
              <line x1="8" y1="2" x2="16" y2="2"/>
            </svg>
            <span id="simHeaderTitle">Interactive Simulator</span>
          </div>
          <span class="text-[10px] text-slate-400 uppercase tracking-wider font-bold">Hands-On Laboratory</span>
        </div>

        <div id="simContainer" class="flex-grow flex flex-col justify-center">
          <!-- Simulator injected here -->
        </div>
      </div>
    </section>

    <!-- Dedicated Quiz Slides (Slides 17 to 20) -->
    <section id="quizContainer" class="quiz-container" style="display: none;">
      <div class="quiz-header">
        <div>
          <span id="quizBadge" class="slide-badge-pill">Mastery Challenge</span>
          <h2 id="quizTitle" class="text-xl font-extrabold text-slate-100 mt-1">Mastery Challenge</h2>
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
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 16v-4"/>
            <path d="M12 8h.01"/>
          </svg>
          <span id="modalTitleText">Step-by-Step Solution</span>
        </div>
        <button id="btnCloseModal" class="btn-close-modal" title="Close Solution Modal">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>
      
      <div id="modalQuestionText" class="text-sm font-semibold text-slate-300 mb-3 p-3 bg-slate-900 rounded-lg border border-slate-800">
        <!-- Question injected here -->
      </div>

      <div id="modalSolutionSteps" class="text-sm text-slate-200 space-y-3 font-sans">
        <!-- KaTeX Math steps injected here -->
      </div>
    </div>
  </div>

  <!-- Bottom Navigation Bar -->
  <footer class="nav-bar">
    <button id="prevBtn" class="nav-btn">
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

  <!-- Application Script -->
  <script>
    // Injected Data
    const SLIDES_DATA = {SLIDES_JSON};
    const QUIZ_QUESTIONS = {QUIZ_QUESTIONS_JSON};
    const SIMULATORS = {SIMULATORS_JSON};

    let currentSlideIdx = 0;
    let isSpeaking = false;
    let voiceEnabled = true;
    let speechSynth = window.speechSynthesis;
    let speechUtterance = null;

    // Web Audio API Sound Effects
    class SoundFX {{
      constructor() {{
        this.ctx = null;
      }}
      init() {{
        if (!this.ctx) {{
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }}
      }}
      playCorrect() {{
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
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      }}
      playWrong() {{
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now); // A3
        osc.frequency.setValueAtTime(196, now + 0.1); // G3
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        osc.start(now);
        osc.stop(now + 0.25);
      }}
      playClick() {{
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, now);
        gain.gain.setValueAtTime(0.1, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.05);
      }}
    }}
    const sfx = new SoundFX();

    // DOM Elements
    const slideCounter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastSlideNotice = document.getElementById('lastSlideNotice');
    const slideJumpSelect = document.getElementById('slideJumpSelect');

    const avatarCircle = document.getElementById('avatarCircle');
    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const slideBadge = document.getElementById('slideBadge');
    const slideSectionTitle = document.getElementById('slideSectionTitle');
    const slideTitle = document.getElementById('slideTitle');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsWrapper = document.getElementById('checkpointsWrapper');

    const labCol = document.getElementById('labCol');
    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simContainer = document.getElementById('simContainer');

    const quizContainer = document.getElementById('quizContainer');
    const quizBadge = document.getElementById('quizBadge');
    const quizTitle = document.getElementById('quizTitle');
    const quizScorePill = document.getElementById('quizScorePill');
    const quizItemsList = document.getElementById('quizItemsList');

    const solutionModal = document.getElementById('solutionModal');
    const btnCloseModal = document.getElementById('btnCloseModal');
    const modalTitleText = document.getElementById('modalTitleText');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');

    // Populate Jump Select
    SLIDES_DATA.forEach((s, idx) => {{
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${{s.slide_num}}. ${{s.title}}`;
      slideJumpSelect.appendChild(opt);
    }});

    // Narration Engine
    function stopNarration() {{
      if (speechSynth && speechSynth.speaking) {{
        speechSynth.cancel();
      }}
      isSpeaking = false;
      avatarSpeechBar.classList.remove('is-speaking');
      iconVoicePlay.style.display = 'block';
      iconVoicePause.style.display = 'none';
    }}

    function speakNarration(text) {{
      stopNarration();
      if (!voiceEnabled || !speechSynth) return;

      const cleanText = text.replace(/\\$[^\\$]*\\$/g, ' '); // remove raw LaTeX from speech
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 0.95;
      speechUtterance.pitch = 1.0;

      speechUtterance.onstart = () => {{
        isSpeaking = true;
        avatarSpeechBar.classList.add('is-speaking');
        iconVoicePlay.style.display = 'none';
        iconVoicePause.style.display = 'block';
      }};

      speechUtterance.onend = () => {{
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      }};

      speechUtterance.onerror = () => {{
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      }};

      speechSynth.speak(speechUtterance);
    }}

    btnVoiceToggle.addEventListener('click', () => {{
      sfx.playClick();
      if (isSpeaking) {{
        stopNarration();
        voiceEnabled = false;
      }} else {{
        voiceEnabled = true;
        const currentSlide = SLIDES_DATA[currentSlideIdx];
        if (currentSlide && currentSlide.narration) {{
          speakNarration(currentSlide.narration);
        }}
      }}
    }});

    // Render In-Slide Checkpoints
    function renderCheckpoints(checkpoints) {{
      checkpointsWrapper.innerHTML = '';
      if (!checkpoints || !checkpoints.length) return;

      checkpoints.forEach((cp, cpIdx) => {{
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const title = document.createElement('div');
        title.className = 'checkpoint-title';
        title.innerHTML = `<span>⚡</span> Concept Checkpoint ${{cpIdx + 1}}`;

        const q = document.createElement('div');
        q.className = 'checkpoint-question';
        q.textContent = cp.question;

        const optsGrid = document.createElement('div');
        optsGrid.className = 'checkpoint-options';

        const fb = document.createElement('div');
        fb.className = 'checkpoint-feedback';

        cp.options.forEach((optText, optIdx) => {{
          const btn = document.createElement('button');
          btn.className = 'checkpoint-btn';
          btn.textContent = `${{String.fromCharCode(65 + optIdx)}}. ${{optText}}`;

          btn.addEventListener('click', () => {{
            const btns = optsGrid.querySelectorAll('.checkpoint-btn');
            btns.forEach(b => b.disabled = true);

            if (optIdx === cp.correct) {{
              btn.classList.add('is-correct');
              sfx.playCorrect();
              fb.className = 'checkpoint-feedback is-correct';
              fb.innerHTML = `<b>✓ Correct!</b> ${{cp.explanation}}`;
            }} else {{
              btn.classList.add('is-wrong');
              btns[cp.correct].classList.add('is-correct');
              sfx.playWrong();
              fb.className = 'checkpoint-feedback is-wrong';
              fb.innerHTML = `<b>✗ Not quite.</b> ${{cp.explanation}}`;
            }}
            if (window.triggerMathRender) triggerMathRender(fb);
          }});

          optsGrid.appendChild(btn);
        }});

        card.appendChild(title);
        card.appendChild(q);
        card.appendChild(optsGrid);
        card.appendChild(fb);
        checkpointsWrapper.appendChild(card);
      }});
    }}

    // Solution Modal Controller
    function openSolutionModal(qId) {{
      sfx.playClick();
      const q = QUIZ_QUESTIONS.find(item => item.id === qId);
      if (!q) return;

      if (modalTitleText) modalTitleText.textContent = `Question ${{q.id}} • Step-by-Step Solution`;
      if (modalQuestionText) modalQuestionText.textContent = q.question;
      
      const correctOptText = q.options[q.correct];
      const solutionContent = q.solution.trim();

      if (modalSolutionSteps) {{
        modalSolutionSteps.innerHTML = `
          <div style="font-weight:800; color:#34d399; margin-bottom:0.6rem; font-size:0.95rem;">
            ✓ Correct Answer: Option ${{String.fromCharCode(65 + q.correct)}} (${{correctOptText}})
          </div>
          <div style="color:#e2e8f0; line-height:1.6; white-space:pre-wrap;">${{solutionContent}}</div>
        `;
      }}

      if (solutionModal) {{
        solutionModal.style.setProperty('display', 'flex', 'important');
        solutionModal.classList.add('is-active');
      }}
      if (window.triggerMathRender) {{
        triggerMathRender(solutionModal);
        setTimeout(() => triggerMathRender(solutionModal), 60);
      }}
    }}
    window.openSolutionModal = openSolutionModal;

    function closeSolutionModal() {{
      sfx.playClick();
      if (solutionModal) {{
        solutionModal.style.setProperty('display', 'none', 'important');
        solutionModal.classList.remove('is-active');
      }}
    }}
    window.closeSolutionModal = closeSolutionModal;

    if (btnCloseModal) btnCloseModal.addEventListener('click', closeSolutionModal);
    if (solutionModal) {{
      solutionModal.addEventListener('click', (e) => {{
        if (e.target === solutionModal) {{
          closeSolutionModal();
        }}
      }});
    }}

    // Render Quiz Slide
    function renderQuizSlide(slide) {{
      slideContentGrid.style.display = 'none';
      quizContainer.style.display = 'flex';

      quizBadge.textContent = slide.badge;
      quizTitle.textContent = slide.title;

      quizItemsList.innerHTML = '';
      let answeredCount = 0;
      let scoreCount = 0;

      slide.questions.forEach((q, idx) => {{
        const itemCard = document.createElement('div');
        itemCard.className = 'quiz-item-card';

        const qTitle = document.createElement('div');
        qTitle.className = 'quiz-item-q';
        qTitle.innerHTML = `<span style="color:#38bdf8; font-weight:800;">Q${{q.id}}.</span> ${{q.question}}`;

        const optGrid = document.createElement('div');
        optGrid.className = 'quiz-opt-grid';

        q.options.forEach((optText, oIdx) => {{
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.textContent = `${{String.fromCharCode(65 + oIdx)}}. ${{optText}}`;

          btn.addEventListener('click', () => {{
            const btns = optGrid.querySelectorAll('.quiz-opt-btn');
            btns.forEach(b => b.disabled = true);

            answeredCount++;
            if (oIdx === q.correct) {{
              btn.classList.add('is-correct');
              sfx.playCorrect();
              scoreCount++;
            }} else {{
              btn.classList.add('is-wrong');
              btns[q.correct].classList.add('is-correct');
              sfx.playWrong();
            }}

            quizScorePill.textContent = `Score: ${{scoreCount}} / ${{slide.questions.length}}`;
          }});

          optGrid.appendChild(btn);
        }});

        const solBtn = document.createElement('button');
        solBtn.className = 'btn-show-solution';
        solBtn.innerHTML = `
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
            <circle cx="12" cy="12" r="3"/>
          </svg>
          <span>View Step-by-Step Solution</span>
        `;
        solBtn.onclick = () => openSolutionModal(q.id);

        itemCard.appendChild(qTitle);
        itemCard.appendChild(optGrid);
        itemCard.appendChild(solBtn);
        quizItemsList.appendChild(itemCard);
      }});

      quizScorePill.textContent = `Score: 0 / ${{slide.questions.length}}`;
      if (window.triggerMathRender) {{
        triggerMathRender(quizContainer);
        setTimeout(() => triggerMathRender(quizContainer), 60);
        setTimeout(() => triggerMathRender(quizContainer), 250);
      }}
    }}

    // Master Slide Renderer
    function renderSlide(idx) {{
      if (idx < 0 || idx >= SLIDES_DATA.length) return;
      currentSlideIdx = idx;
      const slide = SLIDES_DATA[idx];

      slideCounter.textContent = `Slide ${{slide.slide_num}} / ${{SLIDES_DATA.length}}`;
      slideJumpSelect.value = idx;

      // Update Navigation Buttons & Slide 20 Terminal Rule
      prevBtn.disabled = (idx === 0);
      
      if (currentSlideIdx === SLIDES_DATA.length - 1) {{
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'inline-flex';
      }} else {{
        nextBtn.style.display = 'inline-flex';
        lastSlideNotice.style.display = 'none';
      }}

      speechBubbleText.textContent = slide.narration || '';
      speakNarration(slide.narration || '');

      if (slide.is_quiz) {{
        renderQuizSlide(slide);
      }} else {{
        slideContentGrid.style.display = 'grid';
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideBadge.textContent = slide.badge;
        slideSectionTitle.textContent = slide.section;
        slideTitle.textContent = slide.title;
        theoryBody.innerHTML = slide.theory;

        renderCheckpoints(slide.checkpoints);

        // Simulator injection
        if (slide.sim_id && SIMULATORS[slide.sim_id]) {{
          simHeaderTitle.textContent = slide.title;
          simContainer.innerHTML = SIMULATORS[slide.sim_id];
          
          // Re-init simulator JS engines
          if (window.initSimulators) {{
            window.initSimulators();
          }}
        }} else {{
          simContainer.innerHTML = '<div class="text-xs text-slate-400 p-4 text-center">Interactive simulator ready.</div>';
        }}

        if (window.triggerMathRender) {{
          triggerMathRender(slideContentGrid);
          setTimeout(() => triggerMathRender(slideContentGrid), 60);
          setTimeout(() => triggerMathRender(slideContentGrid), 250);
        }}
      }}
    }}

    // Navigation Click Listeners
    prevBtn.addEventListener('click', () => {{
      sfx.playClick();
      if (currentSlideIdx > 0) renderSlide(currentSlideIdx - 1);
    }});

    nextBtn.addEventListener('click', () => {{
      sfx.playClick();
      if (currentSlideIdx < SLIDES_DATA.length - 1) renderSlide(currentSlideIdx + 1);
    }});

    slideJumpSelect.addEventListener('change', (e) => {{
      sfx.playClick();
      renderSlide(parseInt(e.target.value));
    }});

    // Keyboard Arrow Navigation & Modal Esc Key
    window.addEventListener('keydown', (e) => {{
      if (solutionModal && (solutionModal.classList.contains('is-active') || solutionModal.style.display !== 'none')) {{
        if (e.key === 'Escape') {{
          closeSolutionModal();
        }}
        return;
      }}
      if (e.key === 'ArrowRight' && currentSlideIdx < SLIDES_DATA.length - 1) {{
        sfx.playClick();
        renderSlide(currentSlideIdx + 1);
      }} else if (e.key === 'ArrowLeft' && currentSlideIdx > 0) {{
        sfx.playClick();
        renderSlide(currentSlideIdx - 1);
      }}
    }});

    // Embedded Simulator Engines
    {SIMULATORS_JS}

    // Startup Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      renderSlide(0);
      if (window.triggerMathRender) {{
        triggerMathRender(document.body);
        setTimeout(() => triggerMathRender(document.body), 100);
        setTimeout(() => triggerMathRender(document.body), 400);
      }}
    }});
    window.addEventListener('load', () => {{
      if (window.triggerMathRender) triggerMathRender(document.body);
    }});
  </script>
</body>
</html>
"""

output_path = 'public/animations/class7-math-another-peek-beyond-the_point.html'.replace('the_point', 'the-point')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Generated {output_path} successfully!")
print(f"File size: {os.path.getsize(output_path)} bytes")

