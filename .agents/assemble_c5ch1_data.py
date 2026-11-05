"""
Assemble class5_science_ch1_data.py and verify zero raw LaTeX.
"""
import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from generate_c5ch1_part1 import CHAPTER_META, SLIDES_PART1
from generate_c5ch1_part2 import SLIDES_PART2
from generate_c5ch1_part3 import QUIZ_QUESTIONS

SLIDES = SLIDES_PART1 + SLIDES_PART2

# Validate lengths
assert len(SLIDES) == 16, f"Expected 16 slides, got {len(SLIDES)}"
assert len(QUIZ_QUESTIONS) == 40, f"Expected 40 quiz questions, got {len(QUIZ_QUESTIONS)}"

# Check checkpoints count
for s in SLIDES:
    assert len(s.get('checkpoints', [])) == 2, f"Slide {s.get('id')} checkpoints != 2: {len(s.get('checkpoints', []))}"

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

# Check for forbidden lecturer personas
forbidden_names = ['Madam Vidya', 'Dr. Raghu', 'Dr Raghu', 'Teacher', 'lecturer']
for s in SLIDES:
    text = s['spoken_text'] + s['title'] + s['subtitle'] + s['concept_html']
    for fn in forbidden_names:
        if fn.lower() in text.lower():
            print(f"Warning: forbidden name '{fn}' found in slide {s['id']}")

print("VERIFIED PASS: 16 slides, 32 checkpoints, and 40 quiz questions verified with ZERO raw LaTeX!")

# Write out class5_science_ch1_data.py
out_file = ".agents/class5_science_ch1_data.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write('"""Class 5 Science Chapter 1: Water - The Essence of Life Data Module"""\n\n')
    f.write(f"CHAPTER_META = {repr(CHAPTER_META)}\n\n")
    f.write(f"SLIDES = {repr(SLIDES)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n")

print(f"Wrote {out_file} successfully.")

