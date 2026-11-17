#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assemble all 20 slides for NCERT Class 10 Science Chapter 6: Control and Coordination.
Writes to .agents/class10_science_ch6_data.py.
"""

import json
import re

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

with open('.agents/c10s_ch6_part1.json', 'r', encoding='utf-8') as f:
    part1 = json.load(f)
with open('.agents/c10s_ch6_part2.json', 'r', encoding='utf-8') as f:
    part2 = json.load(f)
with open('.agents/c10s_ch6_part3.json', 'r', encoding='utf-8') as f:
    part3 = json.load(f)

all_slides = part1 + part2 + part3
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

print("=== VALIDATING ALL 20 SLIDES FOR CLASS 10 SCIENCE CH 6 ===")

for s in all_slides:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"

    s_str = json.dumps(s)
    for name in FORBIDDEN_CHARACTERS:
        assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", s_str, re.IGNORECASE), f"Slide {sid} contains forbidden character '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str), f"Slide {sid} contains forbidden persona '{persona}'"

    if sid <= 16:
        wc = len(s['speech'].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count {wc} out of range (195-215)!"
        assert len(s.get('checkpoints', [])) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s['checkpoints']:
            assert len(cp['options']) == 4
            assert 'hint' in cp
            assert 'explanation' in cp
            assert 0 <= cp['answer'] <= 3
        print(f"Slide {sid:2d}: '{title}' ({title_words} words) - Lecture speech: {wc} words, 2 checkpoints OK")
    else:
        assert s['speech'] == "", f"Slide {sid} must be silent!"
        assert len(s.get('questions', [])) == 10, f"Slide {sid} must have 10 questions"
        for q in s['questions']:
            assert len(q['options']) == 4
            assert 'hint' in q
            assert 'explanation' in q
            assert len(q['solution_steps']) == 3
            assert 0 <= q['answer'] <= 3
        print(f"Slide {sid:2d}: '{title}' ({title_words} words) - Silent review: 10 challenge questions, 3 solution steps each OK")

out_py = f'''# -*- coding: utf-8 -*-
"""
NCERT Class 10 Science Chapter 6: Control and Coordination Slide Data
20 Slides:
- Slides 1-16: Pure UK Male sound lecture (195-215 words each), 2 checkpoints each
- Slides 17-20: Silent comprehensive review (40 questions total), 10 questions each with 3-step walkthroughs
- Short headings (1-3 words) across all 20 slides
- Zero persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and zero fictional character names
"""

slides = {json.dumps(all_slides, indent=2)}
'''

with open('.agents/class10_science_ch6_data.py', 'w', encoding='utf-8') as f:
    f.write(out_py)

print("\nSuccessfully assembled .agents/class10_science_ch6_data.py!")
