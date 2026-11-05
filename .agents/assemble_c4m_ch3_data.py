# -*- coding: utf-8 -*-
"""
Assembles all 20 slides for Class 4 Maths Chapter 3: Patterns Around Us
Outputs: .agents/class4_maths_ch3_data.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from generate_c4m_ch3_part1 import get_part1_slides
from generate_c4m_ch3_part2 import get_part2_slides
from generate_c4m_ch3_part3 import get_part3_slides

slides = get_part1_slides() + get_part2_slides() + get_part3_slides()

assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"

# Verification of word counts and invariants
HUMAN_NAMES = [
    'gundappa', 'muniamma', 'shirley', 'shiv', 'raghav', 'raman', 'sheela',
    'sunita', 'mary', 'akira', 'preetha', 'adrit', 'rohan', 'aarav', 'ananya',
    'diya', 'priya', 'rahul', 'amit', 'neha', 'sanjay', 'vikram'
]

for s in slides:
    sid = s['id']
    title = s['title']
    print(f"Slide {sid}: {title}")

    # Heading length: 1 to 3 words
    words_in_title = len(title.split())
    assert 1 <= words_in_title <= 3, f"Slide {sid} title '{title}' has {words_in_title} words (must be 1-3)!"

    # Speech word count for slides 1-16: 195-215 words
    if 1 <= sid <= 16:
        w_speech = len(s['speech'].split())
        assert 195 <= w_speech <= 215, f"Slide {sid} speech has {w_speech} words (must be 195-215)!"
        assert len(s.get('checkpoints', [])) == 2, f"Slide {sid} must have 2 checkpoints!"

    # Challenges 17-20: 10 questions each
    if 17 <= sid <= 20:
        assert len(s.get('quiz', [])) == 10, f"Slide {sid} must have 10 quiz questions!"

    # Check for human names
    full_text = s.get('speech', '') + ' ' + str(s.get('checkpoints', '')) + ' ' + str(s.get('quiz', ''))
    for name in HUMAN_NAMES:
        assert name not in full_text.lower(), f"Slide {sid} contains prohibited human name: {name}!"

with open('.agents/class4_maths_ch3_data.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Maths Chapter 3: Patterns Around Us - 20 Slides Data"""\n\n')
    f.write(f"slides = {repr(slides)}\n")

print("Successfully written .agents/class4_maths_ch3_data.py!")
