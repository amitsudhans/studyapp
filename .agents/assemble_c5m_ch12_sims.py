# -*- coding: utf-8 -*-
"""
Assemble Chapter 12 Simulators
Combines Simulators 1-8 and 9-16 into class5_maths_ch12_sims.py
"""

import sys
sys.path.append('.agents')
from make_c5m_ch12_sims_part1 import simulators_part1
from make_c5m_ch12_sims_part2 import simulators_part2

simulators = {}
simulators.update(simulators_part1)
simulators.update(simulators_part2)

print(f"Total simulators assembled: {len(simulators)}")
assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"

with open('.agents/class5_maths_ch12_sims.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""NCERT Class 5 Mathematics — Chapter 12: Racing Seconds Simulators 1 to 16"""\n\n')
    import pprint
    f.write("simulators = " + pprint.pformat(simulators, width=120, sort_dicts=False) + "\n")

print("Successfully written .agents/class5_maths_ch12_sims.py!")
