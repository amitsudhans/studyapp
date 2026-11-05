"""
Assemble class6_science_ch11_data.py and verify zero raw LaTeX.
"""
import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from generate_ch11_part1 import CHAPTER_META, SLIDES_PART1
from generate_ch11_part2 import SLIDES_PART2
from generate_ch11_part3 import QUIZ_QUESTIONS

SLIDES = SLIDES_PART1 + SLIDES_PART2

# Validate lengths
assert len(SLIDES) == 16, f"Expected 16 slides, got {len(SLIDES)}"
assert len(QUIZ_QUESTIONS) == 40, f"Expected 40 quiz questions, got {len(QUIZ_QUESTIONS)}"

# Verify zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def check_latex(obj, path=""):
    if isinstance(obj, str):
        matches = raw_latex_pattern.findall(obj)
        if matches:
            raise ValueError(f"Found raw LaTeX at {path}: {set(matches)}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            check_latex(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            check_latex(item, f"{path}[{idx}]")

check_latex(CHAPTER_META, "CHAPTER_META")
check_latex(SLIDES, "SLIDES")
check_latex(QUIZ_QUESTIONS, "QUIZ_QUESTIONS")

print("VERIFIED PASS: 16 slides and 40 quiz questions verified with ZERO raw LaTeX!")

# Write out class6_science_ch11_data.py
out_file = ".agents/class6_science_ch11_data.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write('"""Class 6 Science Chapter 11 Data Module"""\n\n')
    f.write(f"CHAPTER_META = {repr(CHAPTER_META)}\n\n")
    f.write(f"SLIDES = {repr(SLIDES)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n")

print(f"Wrote {out_file} successfully.")

