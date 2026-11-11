#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for NCERT Class 8 Mathematics - Chapter 9: The Baudhāyana-Pythagoras Theorem
Combines slides 1-8 (part1), 9-16 (part2), and 17-20 (part3) into `slides`.
"""

from generate_c8m_ch9_part1 import slides_part1
from generate_c8m_ch9_part2 import slides_part2
from generate_c8m_ch9_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    print(f"Total slides loaded: {len(slides)}")
    assert len(slides) == 20, "Must have exactly 20 slides!"
    for i, s in enumerate(slides):
        assert s["id"] == i + 1, f"Slide ID mismatch at {i}"
        title_wc = len(s["title"].split())
        assert 1 <= title_wc <= 3, f"Slide {s['id']} title '{s['title']}' exceeds 3 words"
        if s["id"] <= 16:
            wc = len(s["speech"].split())
            assert 195 <= wc <= 215, f"Slide {s['id']} speech out of range: {wc}w"
            assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
        else:
            assert len(s["questions"]) == 10, f"Slide {s['id']} must have 10 questions"
    print("All 20 slides for Class 8 Maths Chapter 9 passed strict data checks!")
