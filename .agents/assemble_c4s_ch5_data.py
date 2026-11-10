# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 5: Food for Health - Data Assembler
Validates all 20 slides:
- 1-3 words titles with exact same meaning
- 195-215 words speech for slides 1-16
- 2 checkpoints for slides 1-16
- 10 quiz questions each for slides 17-20
- Zero human character names
- Zero lecturer personas
Writes final slides list to .agents/class4_science_ch5_data.py
"""

import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from generate_c4s_ch5_part1 import slides_part1
from generate_c4s_ch5_part2 import slides_part2
from generate_c4s_ch5_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

HUMAN_NAMES = [
    'Reena', 'Amit', 'Dada', 'Dadaji', 'Chandan', 'Navya', 'Raghav', 'Diya', 'Raziya',
    'Rukhsana', 'Simran', 'Sunil', 'Bablu', 'Ikra', 'Samina', 'Sumedha', 'Vinayak',
    'Kumar', 'Paridhi', 'Idha', 'Karan', 'Jaspreet', 'Gulnaz', 'Mithali', 'Suzie',
    'Bates', 'Gundappa', 'Muniamma', 'Shirley', 'Shiv', 'Jagat', 'Bholu', 'Rani',
    'Preet', 'Diksha', 'Raman', 'Sheela', 'Sunita', 'Mary', 'Akira', 'Preetha',
    'Adrit', 'Rohan', 'Anjali', 'Aarav', 'Ananya', 'Priya', 'Rahul', 'Neha', 'Sanjay',
    'Vikram', 'Shrinathan', 'Mirabai', 'Gulabo', 'Anvi', 'Raju', 'Parv', 'Chinnu',
    'Abha', 'Didi', 'Daisy', 'Lou', 'Sapan', 'Udaya', 'Krishna', 'Sudama', 'Mala', 'Neela', 'Bhola'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== VALIDATING ALL 20 SLIDES FOR CHAPTER 5: FOOD FOR HEALTH ===")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

for s in all_slides:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    # Content string checking
    slide_text = json_str = str(s)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + re.escape(name) + r'\b', slide_text, re.IGNORECASE), f"Slide {sid} contains human name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_text, re.IGNORECASE), f"Slide {sid} contains forbidden persona '{persona}'"

    if sid <= 16:
        speech = s['speech']
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {sid} speech out of bounds: {wc} words"
        assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s['checkpoints']:
            assert cp['ans'] in cp['options'], f"Checkpoint answer not in options in slide {sid}"
        print(f"Slide {sid:02d} [{title}]: {wc} words, 2 checkpoints OK")
    else:
        assert len(s['questions']) == 10, f"Slide {sid} must have 10 questions"
        for q in s['questions']:
            assert len(q['options']) == 4, f"Question {q['id']} must have 4 options"
            assert q['ans'] in q['options'], f"Question {q['id']} answer not in options"
            assert 'step1' in q['solution_steps'] and 'step2' in q['solution_steps'] and 'step3' in q['solution_steps']
        print(f"Slide {sid:02d} [{title}]: 10 challenge questions OK")

output_file = os.path.join(os.path.dirname(__file__), "class4_science_ch5_data.py")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Science Chapter 5: Food for Health - Validated Slides Data"""\n\n')
    f.write(f"slides = {repr(all_slides)}\n")

print(f"\nSuccessfully wrote validated data for all 20 slides to {output_file}!")

