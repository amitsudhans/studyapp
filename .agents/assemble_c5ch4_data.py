"""
Assembler for NCERT Class 5 Science Chapter 4: Our School - A Happy Place
Combines Part 1, Part 2, and Part 3 into class5_science_ch4_data.py and validates zero raw LaTeX.
"""

import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from generate_c5ch4_part1 import CHAPTER_META, SLIDES_PART1
from generate_c5ch4_part2 import SLIDES_PART2
from generate_c5ch4_part3 import QUIZ_QUESTIONS

ALL_SLIDES = SLIDES_PART1 + SLIDES_PART2
assert len(ALL_SLIDES) == 16, f"Expected 16 slides, got {len(ALL_SLIDES)}"
assert len(QUIZ_QUESTIONS) == 40, f"Expected 40 quiz questions, got {len(QUIZ_QUESTIONS)}"

# Check for zero raw LaTeX in all components
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def check_no_latex(data, path=""):
    if isinstance(data, str):
        matches = raw_latex_pattern.findall(data)
        if matches:
            raise ValueError(f"Found raw LaTeX in {path}: {set(matches)}")
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            check_no_latex(item, f"{path}[{idx}]")
    elif isinstance(data, dict):
        for k, v in data.items():
            check_no_latex(v, f"{path}.{k}")

check_no_latex(CHAPTER_META, "CHAPTER_META")
check_no_latex(ALL_SLIDES, "ALL_SLIDES")
check_no_latex(QUIZ_QUESTIONS, "QUIZ_QUESTIONS")

print("PASSED: Zero raw LaTeX verified in Chapter 4 data!")

# Write to class5_science_ch4_data.py
output_path = ".agents/class5_science_ch4_data.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write('"""NCERT Class 5 Science Chapter 4: Our School - A Happy Place Data Module"""\n\n')
    f.write(f"CHAPTER_META = {repr(CHAPTER_META)}\n\n")
    f.write(f"SLIDES = {repr(ALL_SLIDES)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n")

print(f"Successfully generated {output_path}")

