# -*- coding: utf-8 -*-
"""
Assemble Slides Data for Class 3 Mathematics Chapter 1: What's in a Name?
Combines parts 1, 2, and 3 into class3_maths_ch1_data.py with strict validation.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from generate_c3m_ch1_part1 import slides_part1
from generate_c3m_ch1_part2 import slides_part2
from generate_c3m_ch1_part3 import slides_part3

all_slides = []
all_slides.extend(slides_part1)
all_slides.extend(slides_part2)
all_slides.extend(slides_part3)

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20

out_file = os.path.join(os.path.dirname(__file__), "class3_maths_ch1_data.py")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""NCERT Class 3 Mathematics - Chapter 1: What\'s in a Name? Slide Data"""\n\n')
    f.write("slides = [\n")
    for s in all_slides:
        f.write(f"    {repr(s)},\n")
    f.write("]\n")

print(f"Slide data written to {out_file} ({os.path.getsize(out_file)} bytes)")

