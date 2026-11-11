#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Combined Slides Data Assembler (Slides 1 to 20)
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))

from generate_c8m_ch6_part1 import slides_part1
from generate_c8m_ch6_part2 import slides_part2
from generate_c8m_ch6_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    print(f"Combined slides total: {len(slides)}")
    assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"
    ids = [s["id"] for s in slides]
    assert ids == list(range(1, 21)), f"Slide IDs mismatch: {ids}"
    for s in slides:
        wc = len(s["title"].split())
        assert 1 <= wc <= 3, f"Slide {s['id']} title {s['title']!r} must be 1-3 words"
        if s["id"] <= 16:
            swc = len(s["speech"].split())
            assert 195 <= swc <= 215, f"Slide {s['id']} speech words {swc} not in 195-215"
            assert len(s["checkpoints"]) == 2
        else:
            assert len(s["questions"]) == 10
    print("All 20 slides for Class 8 Maths Chapter 6 assembled and strictly validated!")
