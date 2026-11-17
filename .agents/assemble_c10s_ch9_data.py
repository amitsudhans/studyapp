# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 9: Light - Reflection and Refraction
Assemble all 20 slides into class10_science_ch9_data.py
Verify:
- Exactly 20 slides
- Title: 1 to 3 words
- Speech: 195 to 215 words on slides 1-16; empty on 17-20
- Checkpoints: 2 per slide on 1-16
- Questions: 10 per slide on 17-20
- Zero forbidden character names, zero persona titles
"""

import json
import re

with open('.agents/c10s_ch9_part1.json', 'r', encoding='utf-8') as f:
    slides1 = json.load(f)

with open('.agents/c10s_ch9_part2.json', 'r', encoding='utf-8') as f:
    slides2 = json.load(f)

with open('.agents/c10s_ch9_part3.json', 'r', encoding='utf-8') as f:
    slides3 = json.load(f)

all_slides = slides1 + slides2 + slides3

FORBIDDEN_CHARACTERS = [
    'Reiaan', 'Shalini', 'Sonia', 'Niharika', 'Preet', 'Champa', 'Chameli', 'Rashmi',
    'Ramkali', 'John', 'Jivanti', 'Ravi', 'Akhila', 'Appooppan', 'Ammu', 'Khushi', 'Chhotu',
    'Shirin', 'Raghav', 'Shambhu', 'Gopu', 'Simmi', 'Raj', 'Rishi', 'Chiya', 'Nonika',
    'Nita', 'Radha', 'Sneha', 'Rohit', 'Mohan', 'Chacha', 'Dadiji', 'Dadaji', 'Bela',
    'Kusum', 'Ronnie', 'Kishan', 'Peter', 'Ritu', 'Monu', 'Chintu', 'Leena', 'Adi',
    'Shabnam', 'Mukta', 'Gopal', 'Dhara', 'Atya', 'Jagannath', 'Mithu', 'Dhruv', 'Rohan',
    'Jojo', 'Farooq', 'Arvind', 'Amma', 'Chirag', 'Nandini', 'Deba', 'Meera', 'Pihu',
    'Shanta', 'Mayank', 'Rachel', 'Hanif', 'Savita', 'Hamida', 'Gopi', 'Sangeeta', 'Tara', 'Sophia'
]
FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bProf\b', r'\bProf\.\b'
]

print(f"Total slides loaded: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

for s in all_slides:
    sid = s['id']
    tw = len(s['title'].split())
    assert 1 <= tw <= 3, f"Slide {sid} title '{s['title']}' must be 1-3 words (got {tw})"

    s_str = json.dumps(s)
    for name in FORBIDDEN_CHARACTERS:
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", s_str, re.IGNORECASE), f"Slide {sid} contains character '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str), f"Slide {sid} contains persona '{persona}'"

    if sid <= 16:
        wc = len(s['speech'].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc}"
        assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
    else:
        assert s['speech'] == "", f"Slide {sid} speech must be empty string"
        assert len(s['questions']) == 10, f"Slide {sid} must have 10 challenge questions"

with open('.agents/class10_science_ch9_data.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(f"slides = {repr(all_slides)}\n")

print("Saved .agents/class10_science_ch9_data.py successfully! All 20 slides validated perfectly.")
