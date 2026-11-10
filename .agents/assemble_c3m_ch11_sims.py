#!/usr/bin/env python3
"""
Assemble all 16 simulators for NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting
Outputs: .agents/class3_maths_ch11_sims.py
"""

import sys
sys.path.insert(0, ".agents")

from make_c3m_ch11_sims_part1 import sims_part1
from make_c3m_ch11_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16
for i in range(1, 17):
    assert i in all_sims, f"Missing simulator for slide {i}"

with open(".agents/class3_maths_ch11_sims.py", "w") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""NCERT Class 3 Mathematics - Chapter 11: Filling and Lifting Simulators"""\n\n')
    f.write("simulators = {\n")
    for k in sorted(all_sims.keys()):
        content = all_sims[k].replace("'''", "\\'\\'\\'")
        f.write(f"    {k}: '''{content}''',\n")
    f.write("}\n")

print("Successfully written .agents/class3_maths_ch11_sims.py")
