#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for NCERT Class 9 Maths Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
"""

from generate_c9m_ch8_part1 import slides_part1
from generate_c9m_ch8_part2 import slides_part2
from generate_c9m_ch8_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    assert len(slides) == 20, f"Expected 20 slides, got {len(slides)}"
    print("Chapter 8 Slides Data assembled cleanly: 20 slides total.")
