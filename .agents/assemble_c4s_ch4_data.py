# -*- coding: utf-8 -*-
"""
Assemble and validate Class 4 Science Chapter 4 dataset.
Outputs .agents/class4_science_ch4_data.py with master slides array.
"""

import sys
import os
import json
import re

sys.path.append(os.path.dirname(__file__))

from generate_c4s_ch4_part1 import slides_part1
from generate_c4s_ch4_part2 import slides_part2
from generate_c4s_ch4_part3 import slides_part3

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

print("=== VALIDATING ALL 20 SLIDES FOR CHAPTER 4 ===")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

for idx, slide in enumerate(all_slides):
    sid = slide["id"]
    title = slide["title"]
    title_words = len(title.split())
    print(f"Slide {sid}: '{title}' ({title_words} words)")
    assert 1 <= title_words <= 3, f"Title length violation in slide {sid}: '{title}'"
    assert sid == idx + 1, f"Slide id mismatch: expected {idx + 1}, got {sid}"

    if sid <= 16:
        lecture = slide.get("speech", "")
        wc = len(lecture.split())
        print(f"  Theory lecture: {wc} words")
        assert 195 <= wc <= 215, f"Word count violation in slide {sid}: {wc} words"
        assert len(slide.get("checkpoints", [])) == 2, f"Slide {sid} must have 2 checkpoints"
    else:
        quizzes = slide.get("quizzes", [])
        print(f"  Challenge quiz: {len(quizzes)} questions")
        assert len(quizzes) == 10, f"Slide {sid} must have 10 quiz questions"

    slide_str = json.dumps(slide)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + name + r'\b', slide_str, re.IGNORECASE), f"Banned human name '{name}' in slide {sid}!"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_str), f"Banned persona '{persona}' in slide {sid}!"

out_path = os.path.join(os.path.dirname(__file__), "class4_science_ch4_data.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nClass 4 Science Chapter 4: Growing up with Nature\nMaster Slide Data File.\n"""\n\n')
    f.write(f"slides = {json.dumps(all_slides, indent=4, ensure_ascii=False)}\n")

print(f"Master slide data successfully written to {out_path} ({len(json.dumps(all_slides))} bytes)")

