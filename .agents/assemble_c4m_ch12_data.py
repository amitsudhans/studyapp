# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Data Assembler: Combines parts 1, 2, and 3 into class4_maths_ch12_data.py.
Validates all constraints strictly.
"""

import re
import sys
from generate_c4m_ch12_part1 import slides_part1
from generate_c4m_ch12_part2 import slides_part2
from generate_c4m_ch12_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

BANNED_NAMES = [
    r'\braju\b', r'\brani\b', r'\broja\b', r'\braghav\b', r'\bdiya\b', r'\banvi\b',
    r'\bgulabo\b', r'\bshrinathan\b', r'\bmirabai\b', r'\bgundappa\b', r'\bmuniamma\b',
    r'\bjaspreet\b', r'\bgulnaz\b', r'\blou\b', r'\bdaisy\b', r'\bsapan\b', r'\budaya\b',
    r'\bsumitha\b', r'\bikra\b', r'\bsamina\b', r'\bshirley\b', r'\bshiv\b', r'\bsumedha\b',
    r'\bparv\b'
]

BANNED_PERSONAS = [
    r'\bdr\b', r'\bdr\.\b', r'\bsir\b', r'\bmadam\b', r'\bmr\b', r'\bmr\.\b',
    r'\bmrs\b', r'\bmrs\.\b', r'\bmiss\b'
]

for s in all_slides:
    s_id = s["id"]
    title = s["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {s_id} title '{title}' must be 1 to 3 words, got {title_words}"
    
    if s_id <= 16:
        speech = s["speech"]
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {s_id} speech has {wc} words (must be 195 to 215)!"
        assert len(s.get("checkpoints", [])) == 2, f"Slide {s_id} must have 2 checkpoints"
    else:
        assert len(s.get("quizzes", [])) == 10, f"Slide {s_id} must have 10 quiz questions"
    
    # Check for banned names and personas in title, speech, questions, solutions
    blob = f"{title} {s.get('section', '')} {s.get('speech', '')}"
    for cp in s.get("checkpoints", []):
        blob += f" {cp['q']} {' '.join(cp['options'])} {cp['exp']}"
    for qz in s.get("quizzes", []):
        blob += f" {qz['q']} {' '.join(qz['options'])} {qz.get('hint', '')} {qz['exp']} {qz['sol']}"
        
    for pat in BANNED_NAMES:
        assert not re.search(pat, blob, re.IGNORECASE), f"Banned character name matched pattern '{pat}' in slide {s_id}!"
    for pat in BANNED_PERSONAS:
        assert not re.search(pat, blob, re.IGNORECASE), f"Banned persona matched pattern '{pat}' in slide {s_id}!"

    # Clean Unicode check (no raw LaTeX $)
    assert "$" not in blob, f"Raw LaTeX dollar sign found in slide {s_id}!"
    assert "\\frac" not in blob, f"Raw LaTeX frac found in slide {s_id}!"

print("All slide constraints validated successfully!")

# Write out class4_maths_ch12_data.py
import pprint

with open(".agents/class4_maths_ch12_data.py", "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\n')
    f.write("Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar\n")
    f.write("Full 20-slide structured curriculum dataset.\n")
    f.write('"""\n\n')
    f.write("SLIDES_DATA = ")
    f.write(pprint.pformat(all_slides, indent=4, width=120))
    f.write("\n")

print("Generated .agents/class4_maths_ch12_data.py successfully!")
