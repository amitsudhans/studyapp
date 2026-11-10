#!/usr/bin/env python3
"""
Assemble all 20 slides for NCERT Class 3 Science (Our Wondrous World) - Chapter 1: Family and Friends
into .agents/class3_science_ch1_data.py with strict validation.
"""

import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))
from generate_c3s_ch1_part1 import slides_part1
from generate_c3s_ch1_part2 import slides_part2
from generate_c3s_ch1_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

# Strict Validations
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

FORBIDDEN_CHARACTERS = [
    'Bela', 'Banku', 'Bishu', 'Munni', 'Kusum', 'Rohit', 'Niku', 'Ronnie',
    'Raghav', 'Kishan', 'Peter', 'Ritu', 'Nita', 'Monu', 'Chintu', 'Leena',
    'Adi', 'Shelly', 'Akbar', 'Birbal', 'Shabnam', 'Mukta', 'Gopal', 'Dhara',
    'Atya', 'Jagannath', 'Mithu', 'Dhruv', 'Roro', 'Toto', 'Ajji', 'Teji',
    'Jojo', 'Farooq', 'Arvind', 'Amma', 'Chirag', 'Nandini', 'Deba',
    'Meera', 'Pihu', 'Soni', 'Avi'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

for idx, slide in enumerate(all_slides):
    sid = slide["id"]
    assert sid == idx + 1, f"Slide id mismatch: expected {idx+1}, got {sid}"
    
    # Title validation
    title = slide["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"
    
    # Text validation for character names & personas
    slide_text = str(slide)
    for name in FORBIDDEN_CHARACTERS:
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_text, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, slide_text, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    if sid <= 16:
        # Teaching slides
        wc = len(slide["speech"].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count {wc} out of range (195-215)"
        assert len(slide["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cidx, cp in enumerate(slide["checkpoints"]):
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint {cidx+1} options != 4"
            assert 0 <= cp["answer"] <= 3, f"Slide {sid} checkpoint {cidx+1} answer index out of bounds"
            assert "hint" in cp and "explanation" in cp
    else:
        # Challenge slides
        assert len(slide["questions"]) == 10, f"Slide {sid} must have 10 challenge questions"
        for qidx, q in enumerate(slide["questions"]):
            assert len(q["options"]) == 4, f"Slide {sid} question {qidx+1} options != 4"
            assert 0 <= q["answer"] <= 3, f"Slide {sid} question {qidx+1} answer index out of bounds"
            assert len(q["solution_steps"]) == 3, f"Slide {sid} question {qidx+1} solution steps != 3"
            assert "hint" in q and "explanation" in q

print("All 20 slides strictly verified against all pedagogical and structural rules!")

out_path = os.path.join(os.path.dirname(__file__), "class3_science_ch1_data.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write('"""NCERT Class 3 Science (Our Wondrous World) - Chapter 1: Family and Friends Curriculum Dataset"""\n\n')
    f.write("slides = " + repr(all_slides) + "\n")

print(f"Successfully generated {out_path} with all 20 slides!")
