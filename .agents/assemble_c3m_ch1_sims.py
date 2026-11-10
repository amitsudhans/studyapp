# -*- coding: utf-8 -*-
"""
Assemble Simulators for Class 3 Mathematics Chapter 1: What's in a Name?
Combines simulators_part1 and simulators_part2 into class3_maths_ch1_sims.py.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from make_c3m_ch1_sims_part1 import simulators_part1
from make_c3m_ch1_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16

out_file = os.path.join(os.path.dirname(__file__), "class3_maths_ch1_sims.py")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Assembled Simulators for Class 3 Mathematics Chapter 1"""\n\n')
    f.write("simulators = {\n")
    for k, v in all_sims.items():
        f.write(f"    {repr(k)}: {repr(v)},\n")
    f.write("}\n")

print(f"Simulators written to {out_file} ({os.path.getsize(out_file)} bytes)")

