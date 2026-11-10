#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 8: Introduction to Trigonometry
Combined Data Assembler (Slides 1 to 20)
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))

from generate_c10m_ch8_part1 import slides_part1
from generate_c10m_ch8_part2 import slides_part2
from generate_c10m_ch8_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    print(f"Combined slides total: {len(slides)}")
    assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"
    for idx, s in enumerate(slides, 1):
        assert s["id"] == idx, f"Slide ID mismatch: expected {idx}, got {s['id']}"
        twc = len(s["title"].split())
        assert 1 <= twc <= 3, f"Slide {idx} title '{s['title']}' word count {twc} out of 1-3 bounds"
    print("All 20 slides for Class 10 Maths Chapter 8 assembled and strictly validated!")
