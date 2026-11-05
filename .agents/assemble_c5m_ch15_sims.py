# -*- coding: utf-8 -*-
"""Assemble all 16 simulators for Chapter 15: Data Through Pictures"""

import sys
sys.path.append('.agents')

from make_c5m_ch15_sims_part1 import sims_part1
from make_c5m_ch15_sims_part2 import sims_part2

simulators = {}
simulators.update(sims_part1)
simulators.update(sims_part2)

print(f"Total simulators assembled: {len(simulators)}")
assert len(simulators) == 16, f"Expected 16 simulators, found {len(simulators)}"
for i in range(1, 17):
    assert i in simulators, f"Missing simulator {i}"

with open('.agents/class5_maths_ch15_sims.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""All 16 Simulators for Chapter 15: Data Through Pictures"""\n\n')
    f.write("simulators = {\n")
    for k, v in simulators.items():
        f.write(f"    {k}: '''{v}''',\n")
    f.write("}\n")

print("Successfully wrote .agents/class5_maths_ch15_sims.py!")

