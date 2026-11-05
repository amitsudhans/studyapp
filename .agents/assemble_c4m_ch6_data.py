# -*- coding: utf-8 -*-
"""
Assemble and Validate Class 4 Mathematics Chapter 6 Data
Produces .agents/class4_maths_ch6_data.py
"""

import sys
import os
import json
import re

sys.path.append(os.path.dirname(__file__))
from generate_c4m_ch6_part1 import slides_part1
from generate_c4m_ch6_part2 import slides_part2
from generate_c4m_ch6_part3 import slides_part3

HUMAN_NAMES = [
    'Bhola', 'Raghav', 'Diya', 'Raziya', 'Rukhsana', 'Simran', 'Sunil', 'Bablu',
    'Ikra', 'Samina', 'Sumedha', 'Vinayak', 'Kumar', 'Paridhi', 'Idha', 'Karan',
    'Jaspreet', 'Gulnaz', 'Zoltán', 'Dienes', 'Mithali', 'Suzie', 'Bates',
    'Gundappa', 'Muniamma', 'Shirley', 'Shiv',
    'Mini', 'Jagat', 'Bholu', 'Rani', 'Preet',
    'Diksha', 'Raman', 'Sheela', 'Sunita', 'Mary', 'Akira', 'Preetha', 'Adrit',
    'Rohan', 'Aarav', 'Ananya', 'Priya', 'Rahul', 'Amit', 'Neha', 'Sanjay', 'Vikram'
]

LECTURER_PERSONAS = [
    r'\bDr\.', r'\bDr\b', r'\bProf\.', r'\bProf\b', r'\bSir\b', r'\bMadam\b', r'\bMr\.', r'\bMrs\.', r'\bMiss\b'
]

slides = slides_part1 + slides_part2 + slides_part3

print("=== VERIFYING ALL 20 SLIDES FOR CHAPTER 6 ===")
assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"

EXPECTED_TITLES = [
    "Health Checkup Measures",
    "Classroom Metre Benchmark",
    "Rope Fraction Lengths",
    "Walking Jumping Lines",
    "Long Jump Estimates",
    "Animal Length Scales",
    "Length Ratio Puzzles",
    "Small Centimetre Units",
    "Metre Scale Division",
    "Estimation Versus Measurement",
    "Toy Car Distances",
    "Treasure Grid Routes",
    "Broken Ruler Challenges",
    "Sticker Border Math",
    "Metre Centimetre Conversions",
    "Fencing Garden Perimeter",
    "Challenge 1",
    "Challenge 2",
    "Challenge 3",
    "Challenge 4",
]

for idx, slide in enumerate(slides):
    sid = slide['id']
    title = slide['title']
    title_words = len(title.split())
    print(f"Slide {sid:2d}: {title} ({title_words} words)")
    assert title == EXPECTED_TITLES[idx], f"Slide {sid} title '{title}' != expected '{EXPECTED_TITLES[idx]}'"
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1 to 3 words!"

    if sid <= 16:
        speech = slide.get('speech') or slide.get('lecture')
        wc = len(speech.split())
        print(f"  Speech words: {wc}")
        assert 195 <= wc <= 215, f"Slide {sid} speech word count {wc} out of bounds (195-215)!"
        assert len(slide['checkpoints']) == 2, f"Slide {sid} checkpoints must be 2!"
    else:
        quiz = slide.get('quiz')
        assert len(quiz) == 10, f"Slide {sid} quiz must have 10 questions!"

    slide_str = json.dumps(slide)
    for name in HUMAN_NAMES:
        match = re.search(r'\b' + name + r'\b', slide_str, re.IGNORECASE)
        assert not match, f"Prohibited human name '{name}' found in slide {sid}!"

    for persona in LECTURER_PERSONAS:
        match = re.search(persona, slide_str)
        assert not match, f"Prohibited persona '{persona}' found in slide {sid}!"

print("ALL CHAPTER 6 SLIDES VALIDATED PERFECTLY!")

output_file = os.path.join(os.path.dirname(__file__), "class4_maths_ch6_data.py")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 6: Measuring Length Data"""\n\n')
    f.write(f"slides = {json.dumps(slides, indent=2, ensure_ascii=False)}\n")

print(f"Successfully wrote {output_file} ({os.path.getsize(output_file)} bytes).")

