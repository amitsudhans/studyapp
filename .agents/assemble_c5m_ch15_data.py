# -*- coding: utf-8 -*-
"""Assemble all 20 slides for Chapter 15: Data Through Pictures"""

import sys
sys.path.append('.agents')

from generate_c5m_ch15_part1 import slides_part1
from generate_c5m_ch15_part2 import slides_part2
from generate_c5m_ch15_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

# Check IDs 1 to 20
for idx, s in enumerate(all_slides, 1):
    assert s['id'] == idx, f"Slide index mismatch at {idx}: found {s['id']}"

import json
with open('.agents/class5_maths_ch15_data.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Full Slides Data for Chapter 15: Data Through Pictures"""\n\n')
    f.write("slides = " + repr(all_slides) + "\n")

print("Successfully generated .agents/class5_maths_ch15_data.py!")

