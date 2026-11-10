#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 3: Celebrating Festivals
Assembled Data File: Slides 1 to 20
"""

import sys
sys.path.append(".agents")

from generate_c3s_ch3_part1 import slides_part1
from generate_c3s_ch3_part2 import slides_part2
from generate_c3s_ch3_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    import re, json
    print(f"Total slides assembled: {len(slides)}")
    assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"

    # Check titles (strictly 1-3 words)
    for s in slides:
        tw = len(s["title"].split())
        assert 1 <= tw <= 3, f"Title length violation on slide {s['id']}: '{s['title']}' ({tw} words)"

    # Check speech word counts for slides 1-16 (strictly 195-215 words)
    for s in slides[:16]:
        wc = len(s["speech"].split())
        assert 195 <= wc <= 215, f"Speech word count violation on slide {s['id']}: {wc} words"
        assert len(s["checkpoints"]) == 2, f"Checkpoints count violation on slide {s['id']}"

    # Check challenge slides 17-20 (strictly 10 questions each)
    for s in slides[16:]:
        assert len(s["questions"]) == 10, f"Questions count violation on slide {s['id']}"

    # Check forbidden human character names
    forbidden_names = ['Rishi', 'Chiya', 'Nonikaa', 'Unni', 'Mama', 'Mami', 'Raghav', 'Bela', 'Banku', 'Bishu', 'Dadiji', 'Sneha', 'Rohit', 'Mohan', 'Radha', 'Nita', 'Monu', 'Ritu', 'Mukta', 'Shabnam', 'Akbar', 'Birbal', 'Leena', 'Adi', 'Soni', 'Avi']
    personas = [r'\bDr\.', r'\bDr ', r'\bSir\b', r'\bMadam\b', r'\bMr\.', r'\bMr ', r'\bMrs\.', r'\bMrs ', r'\bMiss\b']

    text_corpus = json.dumps(slides)
    for name in forbidden_names:
        matches = re.findall(r'\b' + name + r'\b', text_corpus, re.IGNORECASE)
        assert len(matches) == 0, f"Forbidden name '{name}' found: {matches}"

    for persona in personas:
        matches = re.findall(persona, text_corpus)
        assert len(matches) == 0, f"Lecturer persona '{persona}' found: {matches}"

    print("ALL 20 SLIDES STRICTLY VALIDATED! ZERO CHARACTER NAMES! ZERO PERSONAS!")
