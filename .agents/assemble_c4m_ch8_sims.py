# -*- coding: utf-8 -*-
"""
Assemble and Validate Class 4 Mathematics Chapter 8 Simulators
Produces .agents/class4_maths_ch8_sims.py
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from make_c4m_ch8_sims_part1 import simulators_part1
from make_c4m_ch8_sims_part2 import simulators_part2

simulators = {}
simulators.update(simulators_part1)
simulators.update(simulators_part2)

assert len(simulators) == 16, f"Expected 16 simulators, found {len(simulators)}"
print(f"Successfully assembled {len(simulators)} simulators for Chapter 8.")

output_file = os.path.join(os.path.dirname(__file__), "class4_maths_ch8_sims.py")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 8 Simulators"""\n\n')
    f.write("simulators = {\n")
    for k in sorted(simulators.keys()):
        content = simulators[k].replace("'''", "\\'\\'\\'")
        f.write(f"    {k}: '''{content}''',\n")
    f.write("}\n")

print(f"Wrote {output_file} ({os.path.getsize(output_file)} bytes).")

