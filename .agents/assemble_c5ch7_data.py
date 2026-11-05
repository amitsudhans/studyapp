"""
Assembler script for NCERT Class 5 Science Chapter 7: Energy - How Things Work data file.
Merges Part 1 (Slides 1-8), Part 2 (Slides 9-16), and Part 3 (Quizzes 1-40) into class5_science_ch7_data.py.
Validates zero raw LaTeX.
"""

import sys
import re

sys.path.append(".agents")
from generate_c5ch7_part1 import SLIDES_PART1
from generate_c5ch7_part2 import SLIDES_PART2
from generate_c5ch7_part3 import QUIZ_QUESTIONS

CHAPTER_META = {
    "chapter_num": 7,
    "title": "Energy - How Things Work",
    "class_level": "Class 5",
    "subject": "Science (Curiosity, NEP 2020)",
    "description": "NCERT Class 5 Science Chapter 7: Energy - How Things Work interactive animated laboratory.",
}

SLIDES = SLIDES_PART1 + SLIDES_PART2

assert len(SLIDES) == 16, f"Expected 16 slides, got {len(SLIDES)}"
assert len(QUIZ_QUESTIONS) == 40, f"Expected 40 quiz questions, got {len(QUIZ_QUESTIONS)}"

# Check for raw LaTeX patterns
latex_patterns = [
    r'\\frac', r'\\text', r'\\times', r'\\div', r'\\circ', r'\\theta', r'\\le', r'\\ge',
    r'\\approx', r'\\pm', r'\\degree', r'\$', r'\\sqrt'
]

combined_text = str(CHAPTER_META) + str(SLIDES) + str(QUIZ_QUESTIONS)
for pat in latex_patterns:
    matches = re.findall(pat, combined_text)
    if matches:
        print(f"WARNING: Found LaTeX pattern {pat}: {matches}")
        sys.exit(1)

print("Zero raw LaTeX check passed successfully for Chapter 7 data!")

out_file = ".agents/class5_science_ch7_data.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 5 Science Chapter 7: Energy - How Things Work Data\n"""\n\n')
    f.write(f"CHAPTER_META = {repr(CHAPTER_META)}\n\n")
    f.write(f"SLIDES = {repr(SLIDES)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n")

print(f"Successfully generated {out_file} with 16 slides and 40 quiz questions.")

