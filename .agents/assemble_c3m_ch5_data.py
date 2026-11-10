# -*- coding: utf-8 -*-
"""Assembles all 20 slides for Class 3 Mathematics Chapter 5: Fun with Shapes."""

import os
import sys
import json
import re

sys.path.append(os.path.dirname(__file__))

from generate_c3m_ch5_part1 import slides_part1
from generate_c3m_ch5_part2 import slides_part2
from generate_c3m_ch5_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Amma']
FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']

for s in all_slides:
    sid = s["id"]
    title = s["title"]
    words = len(title.split())
    assert 1 <= words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {words})"
    
    slide_str = json.dumps(s)
    for name in FORBIDDEN_CHARACTERS:
        if name.lower() == 'deep':
            assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
        else:
            assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
    
    if sid <= 16:
        wc = len(s["speech"].split())
        assert 195 <= wc <= 215, f"Slide {sid} word count out of range: {wc}"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
    else:
        assert len(s["questions"]) == 10, f"Slide {sid} must have 10 questions"

out_path = os.path.join(os.path.dirname(__file__), "class3_maths_ch5_data.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Complete 20-slide dataset for Class 3 Mathematics Chapter 5: Fun with Shapes."""\n\n')
    f.write("SLIDES = " + json.dumps(all_slides, indent=4, ensure_ascii=False) + "\n")

print(f"Successfully assembled all 20 slides into {out_path}!")
