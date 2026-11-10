#!/usr/bin/env python3
"""
Assemble all 20 slides for NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party!
Outputs: .agents/class3_maths_ch10_data.py
"""

import sys
sys.path.insert(0, ".agents")

from generate_c3m_ch10_part1 import slides_part1
from generate_c3m_ch10_part2 import slides_part2
from generate_c3m_ch10_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3
print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20

with open(".agents/class3_maths_ch10_data.py", "w") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""NCERT Class 3 Mathematics - Chapter 10: Fun at Class Party! Data"""\n\n')
    f.write("slides_data = " + repr(all_slides) + "\n")

print("Successfully written .agents/class3_maths_ch10_data.py")
