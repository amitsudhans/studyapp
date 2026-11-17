#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 11 Data Aggregator
Combines Part 1 (Slides 1-8), Part 2 (Slides 9-16), and Part 3 (Slides 17-20).
"""

from generate_c9s_ch11_part1 import slides_part1
from generate_c9s_ch11_part2 import slides_part2
from generate_c9s_ch11_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3

if __name__ == "__main__":
    print(f"Total slides aggregated: {len(slides)}")
    for i, s in enumerate(slides):
        sw = len(s["speech"].split()) if s.get("speech") else 0
        tw = len(s["title"].split())
        print(f"Slide {i+1}: title='{s['title']}' ({tw} words), speech={sw} words")
        assert 1 <= tw <= 3, f"Slide {i+1} title length {tw} not 1-3 words"
        if i < 16:
            assert 195 <= sw <= 215, f"Slide {i+1} speech word count {sw} not 195-215"
            assert len(s["checkpoints"]) == 2, f"Slide {i+1} must have 2 checkpoints"
        else:
            assert sw == 0, f"Slide {i+1} speech word count must be 0"
            assert len(s["questions"]) == 10, f"Slide {i+1} must have 10 challenge questions"
    print("ALL 20 SLIDES VERIFIED SUCCESSFULLY!")
