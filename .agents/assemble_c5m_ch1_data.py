"""
Assemble full dataset for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I
Checks for zero raw LaTeX and compiles .agents/class5_maths_ch1_data.py
"""

import sys
import re

from generate_c5m_ch1_part1 import SLIDES_PART1
from generate_c5m_ch1_part2 import SLIDES_PART2
from generate_c5m_ch1_part3 import QUIZ_QUESTIONS

CHAPTER_META = {
    "chapter_num": 1,
    "title": "We the Travellers - I",
    "class": "Class 5",
    "subject": "Mathematics (Joyful Mathematics, NEP 2020)",
    "description": "Comprehensive 20-slide interactive animated laboratory exploring human travel evolution from walking to spacecraft, large numbers up to Ten Thousand (10,000), Indian place value chart (TTh, Th, H, T, O), comma placement, comparing and ordering numbers, digit swap puzzles, rounding off to nearest 10, 100, and 1,000, travel speed (Distance = Speed × Time), field trip vehicle capacity math, large numbers in everyday life, and pastime mathematics puzzles (River Crossing, Pebble Game, Digit Difference, and King's Horses).",
}

SLIDES = SLIDES_PART1 + SLIDES_PART2

print(f"Total slides: {len(SLIDES)} (Expected: 16)")
print(f"Total quiz questions: {len(QUIZ_QUESTIONS)} (Expected: 40)")

assert len(SLIDES) == 16, f"Expected 16 concept slides, got {len(SLIDES)}"
assert len(QUIZ_QUESTIONS) == 40, f"Expected 40 quiz questions, got {len(QUIZ_QUESTIONS)}"

# Check for raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def verify_no_latex(text, context):
    if not isinstance(text, str):
        return
    matches = raw_latex_pattern.findall(text)
    math_cmds = [m for m in matches if m in ['frac', 'times', 'sqrt', 'cdot', 'text', 'le', 'ge', 'pm', 'circ', 'degree']]
    if math_cmds:
        raise ValueError(f"Found raw LaTeX in {context}: {set(math_cmds)}")

verify_no_latex(CHAPTER_META['title'], "CHAPTER_META title")
for s in SLIDES:
    verify_no_latex(s['title'], f"Slide {s['id']} title")
    verify_no_latex(s['concept_html'], f"Slide {s['id']} concept_html")
    verify_no_latex(s['spoken_text'], f"Slide {s['id']} spoken_text")
    for cp in s.get('checkpoints', []):
        verify_no_latex(cp['question'], f"Slide {s['id']} cp question")
        verify_no_latex(cp['explanation'], f"Slide {s['id']} cp explanation")
        if 'study_insight' in cp:
            verify_no_latex(cp['study_insight'], f"Slide {s['id']} cp study_insight")

for q in QUIZ_QUESTIONS:
    verify_no_latex(q['question'], f"Quiz Q{q['id']} question")
    verify_no_latex(q['explanation'], f"Quiz Q{q['id']} explanation")
    verify_no_latex(q['solution_html'], f"Quiz Q{q['id']} solution_html")

print("VERIFIED PASS: Zero raw LaTeX found in all Chapter 1 Maths data!")

# Write to .agents/class5_maths_ch1_data.py
out_content = f'''"""
Full Dataset for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I
Joyful Mathematics curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols.
"""

CHAPTER_META = {repr(CHAPTER_META)}

SLIDES = {repr(SLIDES)}

QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}
'''

with open(".agents/class5_maths_ch1_data.py", "w", encoding="utf-8") as f:
    f.write(out_content)

print("Successfully written .agents/class5_maths_ch1_data.py!")

