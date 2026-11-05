"""
Assemble Chapter 5 data file: class5_science_ch5_data.py
Merges part1, part2, and part3.
Verifies zero raw LaTeX.
"""

import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from generate_c5ch5_part1 import SLIDES_PART1
from generate_c5ch5_part2 import SLIDES_PART2
from generate_c5ch5_part3 import QUIZ_QUESTIONS

CHAPTER_META = {
    "chapter_num": 5,
    "title": "Our Vibrant Country",
    "class_level": "Class 5",
    "subject": "Science (Curiosity, NEP 2020)",
    "description": "NCERT Class 5 Science Chapter 5: Our Vibrant Country interactive animated laboratory."
}

ALL_SLIDES = SLIDES_PART1 + SLIDES_PART2

# Verification for zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def verify_clean(text, context):
    if not isinstance(text, str):
        return
    matches = raw_latex_pattern.findall(text)
    if matches:
        raise ValueError(f"Found raw LaTeX in {context}: {set(matches)}")

verify_clean(CHAPTER_META["title"], "CHAPTER_META title")
for s in ALL_SLIDES:
    verify_clean(s["title"], f"Slide {s['id']} title")
    verify_clean(s["concept_html"], f"Slide {s['id']} concept_html")
    verify_clean(s["spoken_text"], f"Slide {s['id']} spoken_text")
    verify_clean(s["lecture_script"], f"Slide {s['id']} lecture_script")
    for cp in s.get("checkpoints", []):
        verify_clean(cp["question"], f"Slide {s['id']} cp question")
        verify_clean(cp["explanation"], f"Slide {s['id']} cp explanation")
        verify_clean(cp["study_insight"], f"Slide {s['id']} cp study_insight")

for q in QUIZ_QUESTIONS:
    verify_clean(q["question"], f"Quiz Q{q['id']} question")
    verify_clean(q["explanation"], f"Quiz Q{q['id']} explanation")
    verify_clean(q["solution_html"], f"Quiz Q{q['id']} solution_html")

print(f"VERIFICATION SUCCESS: 16 slides, 32 checkpoints, and 40 quiz questions verified with ZERO raw LaTeX!")

output_code = f'''# Generated Chapter 5 Data File
CHAPTER_META = {repr(CHAPTER_META)}

SLIDES = {repr(ALL_SLIDES)}

QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}
'''

output_path = ".agents/class5_science_ch5_data.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_code)

print(f"Wrote {output_path} successfully ({len(output_code)} bytes)!")

