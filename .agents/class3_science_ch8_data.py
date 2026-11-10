#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 8: Food We Eat
Combined Slides Data (Slides 1 to 20)
"""

import sys
import os
import json
import re

sys.path.append(os.path.join(os.path.dirname(__file__)))

from generate_c3s_ch8_part1 import slides_part1
from generate_c3s_ch8_part2 import slides_part2
from generate_c3s_ch8_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

FORBIDDEN_CHARACTERS = [
    'Shirin', 'Raghav', 'Shambhu', 'Gopu', 'Simmi', 'Raj',
    'Rishi', 'Chiya', 'Nonikaa', 'Unni', 'Mama', 'Mami',
    'Nita', 'Radha', 'Sneha', 'Rohit', 'Mohan', 'Chacha', 'Dadiji', 'Dadaji',
    'Bela', 'Banku', 'Bishu', 'Munni', 'Kusum', 'Ronnie',
    'Kishan', 'Peter', 'Ritu', 'Monu', 'Chintu', 'Leena',
    'Adi', 'Shelly', 'Akbar', 'Birbal', 'Shabnam', 'Mukta', 'Gopal', 'Dhara',
    'Atya', 'Jagannath', 'Mithu', 'Dhruv', 'Roro', 'Toto', 'Ajji', 'Teji',
    'Jojo', 'Farooq', 'Arvind', 'Amma', 'Chirag', 'Nandini', 'Deba',
    'Meera', 'Pihu', 'Soni', 'Avi'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

if __name__ == "__main__":
    print(f"Combined slides total: {len(slides)}")
    assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"
    for i, s in enumerate(slides, start=1):
        assert s["id"] == i, f"Slide index mismatch: expected {i}, got {s['id']}"
        twc = len(s["title"].split())
        assert 1 <= twc <= 3, f"Slide {i} title '{s['title']}' has {twc} words (must be 1-3)"

        raw_str = json.dumps(s)
        for ch in FORBIDDEN_CHARACTERS:
            assert not re.search(r'\b' + re.escape(ch) + r"'?s?\b", raw_str, re.IGNORECASE), f"Slide {i} contains forbidden character '{ch}'"
        for p in FORBIDDEN_PERSONAS:
            assert not re.search(p, raw_str, re.IGNORECASE), f"Slide {i} contains forbidden persona matching '{p}'"

        if i <= 16:
            wc = len(s["speech"].split())
            assert 195 <= wc <= 215, f"Slide {i} speech word count {wc} not in 195-215"
            assert len(s["checkpoints"]) == 2
        else:
            assert len(s["questions"]) == 10
    print("All 20 slides for Chapter 8 assembled and strictly validated!")
