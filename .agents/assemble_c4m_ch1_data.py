# -*- coding: utf-8 -*-
"""
Assemble all 20 slides into class4_maths_ch1_data.py
"""
import sys
sys.path.append('.agents')

from generate_c4m_ch1_part1 import slides_part1
from generate_c4m_ch1_part2 import slides_part2
from generate_c4m_ch1_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

with open('.agents/class4_maths_ch1_data.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 1: Shapes Around Us Slides Data"""\n\n')
    f.write("slides = " + repr(all_slides) + "\n")

print(f"Successfully assembled {len(all_slides)} slides into .agents/class4_maths_ch1_data.py")
