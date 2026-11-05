# assemble_c5m_ch2_data.py
"""Assemble all parts into class5_maths_ch2_data.py and verify zero raw LaTeX."""

import sys
import re
from generate_c5m_ch2_part1 import SLIDES_PART1
from generate_c5m_ch2_part2 import SLIDES_PART2
from generate_c5m_ch2_part3 import QUIZ_QUESTIONS

ALL_SLIDES = SLIDES_PART1 + SLIDES_PART2
print(f"Total slides: {len(ALL_SLIDES)} (Expected: 16)")
print(f"Total quiz questions: {len(QUIZ_QUESTIONS)} (Expected: 40)")
assert len(ALL_SLIDES) == 16, "Must have exactly 16 concept slides"
assert len(QUIZ_QUESTIONS) == 40, "Must have exactly 40 quiz questions"

# Verify Zero Raw LaTeX
latex_pat = re.compile(r'(\\\([^\)]+\\\)|\\\[[^\]]+\\\]|\$[^$]+\$)')
errors = 0

for s in ALL_SLIDES:
    for field in ['title', 'subtitle', 'concept_html', 'spoken_text']:
        val = s.get(field, '')
        matches = latex_pat.findall(val)
        if matches:
            print(f"ERROR: Raw LaTeX in Slide {s['id']} [{field}]: {matches}")
            errors += 1
    for cp in s.get('checkpoints', []):
        for cp_field in ['question', 'explanation', 'study_insight']:
            val = cp.get(cp_field, '')
            matches = latex_pat.findall(val)
            if matches:
                print(f"ERROR: Raw LaTeX in Slide {s['id']} CP [{cp_field}]: {matches}")
                errors += 1
        for opt in cp.get('options', []):
            matches = latex_pat.findall(opt)
            if matches:
                print(f"ERROR: Raw LaTeX in Slide {s['id']} CP option: {matches}")
                errors += 1

for q in QUIZ_QUESTIONS:
    for q_field in ['question', 'explanation', 'solution_html']:
        val = q.get(q_field, '')
        matches = latex_pat.findall(val)
        if matches:
            print(f"ERROR: Raw LaTeX in Quiz Q{q['id']} [{q_field}]: {matches}")
            errors += 1
    for opt in q.get('options', []):
        matches = latex_pat.findall(opt)
        if matches:
            print(f"ERROR: Raw LaTeX in Quiz Q{q['id']} option: {matches}")
            errors += 1

if errors > 0:
    print(f"Found {errors} raw LaTeX occurrences! Fix them before proceeding.")
    sys.exit(1)

print("VERIFIED PASS: Zero raw LaTeX found in all Chapter 2 Maths data!")

# Write to class5_maths_ch2_data.py
CHAPTER_META = {
    "title": "Fractions",
    "class": "Class 5",
    "subject": "Mathematics",
    "chapter": 2,
    "book": "Joyful Mathematics",
    "total_slides": 20,
    "concept_slides": 16,
    "quiz_slides": 4,
    "total_checkpoints": 32,
    "total_quiz_questions": 40
}

with open('/home/lead-programmer/study-app/.agents/class5_maths_ch2_data.py', 'w', encoding='utf-8') as f:
    f.write('"""Master Data File for NCERT Class 5 Mathematics Chapter 2: Fractions."""\n\n')
    f.write(f'CHAPTER_META = {repr(CHAPTER_META)}\n\n')
    f.write(f'SLIDES = {repr(ALL_SLIDES)}\n\n')
    f.write(f'QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n')

print("Successfully written .agents/class5_maths_ch2_data.py!")

