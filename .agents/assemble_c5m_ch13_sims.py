import sys
sys.path.insert(0, '.agents')
from make_c5m_ch13_sims_part1 import sims_part1
from make_c5m_ch13_sims_part2 import sims_part2

simulators = {}
simulators.update(sims_part1)
simulators.update(sims_part2)

print(f"Total simulators assembled: {len(simulators)}")
assert len(simulators) == 16, "Must have exactly 16 simulators"

with open('.agents/class5_maths_ch13_sims.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 5 Maths Chapter 13: Animal Jumps Simulators File"""\n\n')
    f.write(f"simulators = {repr(simulators)}\n")

print("Successfully written .agents/class5_maths_ch13_sims.py!")
