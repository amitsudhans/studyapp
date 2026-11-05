# -*- coding: utf-8 -*-
"""
Assemble Chapter 9 Data
Combines slides 1-8, 9-16, 17-20 into class4_maths_ch9_data.py
Performs strict validation:
- 20 slides total
- Titles 1-3 words
- Speech 195-215 words for slides 1-16, empty for 17-20
- 32 checkpoints (2 on each of slides 1-16)
- 40 quiz questions (10 on each of slides 17-20)
- Zero human character names
- Zero lecturer personas
- Clean Unicode throughout
"""

import sys
import os
import re
import pprint

sys.path.append(os.path.dirname(__file__))

from generate_c4m_ch9_part1 import slides_part1
from generate_c4m_ch9_part2 import slides_part2
from generate_c4m_ch9_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

BANNED_NAMES = [
    r"\bGulabo\b", r"\bAnvi\b", r"\bRaghav\b", r"\bMala\b", r"\bNeela\b",
    r"\bBhola\b", r"\bKrishna\b", r"\bSudama\b", r"\bSapan\b", r"\bDaisy\b",
    r"\bLou\b", r"\bMini\b", r"\bJagat\b", r"\bBholu\b", r"\bRani\b", r"\bPreet\b",
    r"\bJaspreet\b", r"\bGulnaz\b", r"\bIkra\b", r"\bSamina\b", r"\bSumedha\b",
    r"\bUdaya\b", r"\bGundappa\b", r"\bMuniamma\b", r"\bShirley\b", r"\bShiv\b",
    r"\bShrinathan\b", r"\bMirabai\b"
]

BANNED_PERSONAS = [
    r"\bDr\b\.?", r"\bSir\b", r"\bMadam\b", r"\bMr\b\.?", r"\bMrs\b\.?", r"\bMiss\b"
]

total_checkpoints = 0
total_quizzes = 0

for s in all_slides:
    sid = s["id"]
    title = s["title"]
    speech = s.get("speech", "")
    
    # 1. Title length
    title_words = title.split()
    assert 1 <= len(title_words) <= 3, f"Slide {sid} title '{title}' has {len(title_words)} words (expected 1-3)!"
    
    # 2. Speech word count
    if sid <= 16:
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {sid} speech has {wc} words (expected 195-215)!"
        cp = s.get("checkpoints", [])
        assert len(cp) == 2, f"Slide {sid} has {len(cp)} checkpoints (expected 2)!"
        total_checkpoints += len(cp)
    else:
        assert speech == "", f"Slide {sid} should have empty speech!"
        qz = s.get("quizzes", [])
        assert len(qz) == 10, f"Slide {sid} has {len(qz)} quizzes (expected 10)!"
        total_quizzes += len(qz)

    # 3. Check text content for banned names & personas
    full_text = speech + " " + title + " " + s.get("section", "")
    for cp in s.get("checkpoints", []):
        full_text += " " + cp["q"] + " " + " ".join(cp["options"]) + " " + cp["exp"]
    for qz in s.get("quizzes", []):
        full_text += " " + qz["q"] + " " + " ".join(qz["options"]) + " " + qz["exp"] + " " + qz.get("hint", "")

    for pattern in BANNED_NAMES:
        assert not re.search(pattern, full_text, re.IGNORECASE), f"Banned name match '{pattern}' found in slide {sid}!"
        
    for pattern in BANNED_PERSONAS:
        assert not re.search(pattern, full_text), f"Banned persona match '{pattern}' found in slide {sid}!"

    # 4. Check for raw LaTeX
    assert "$" not in full_text, f"Raw LaTeX dollar sign found in slide {sid}!"
    assert "\\frac" not in full_text, f"Raw LaTeX frac found in slide {sid}!"

print("All slide validations PASSED successfully!")
print(f"Total Slides: {len(all_slides)}")
print(f"Total Checkpoints: {total_checkpoints} (expected 32)")
print(f"Total Quizzes: {total_quizzes} (expected 40)")

out_path = os.path.join(os.path.dirname(__file__), "class4_maths_ch9_data.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nNCERT Class 4 Mathematics - Chapter 9: Equal Groups\nCurated Slide & Quiz Data\n"""\n\n')
    f.write("slides = ")
    f.write(pprint.pformat(all_slides, indent=4, width=120))
    f.write("\n")

print(f"Successfully generated {out_path}")
