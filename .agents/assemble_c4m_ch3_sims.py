# -*- coding: utf-8 -*-
"""
Assembles all 16 interactive simulators for Class 4 Maths Chapter 3.
Outputs: .agents/class4_maths_ch3_sims.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from make_c4m_ch3_sims_part1 import get_sims_part1
from make_c4m_ch3_sims_part2 import get_sims_part2

simulators = {}
simulators.update(get_sims_part1())
simulators.update(get_sims_part2())

assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"

with open('.agents/class4_maths_ch3_sims.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Maths Chapter 3: 16 Bespoke Simulators Markup"""\n\n')
    f.write(f"simulators = {repr(simulators)}\n")

print(f"Successfully assembled {len(simulators)} simulators into .agents/class4_maths_ch3_sims.py!")
