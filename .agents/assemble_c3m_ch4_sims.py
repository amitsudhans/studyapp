import sys
sys.path.insert(0, '.agents')
from make_c3m_ch4_sims_part1 import simulators_part1
from make_c3m_ch4_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"

with open(".agents/class3_maths_ch4_sims.py", "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 3 Mathematics Chapter 4: Vacation with My Nani Maa - Complete Interactive Simulators."""\n\n')
    f.write("simulators = " + repr(all_sims) + "\n")

print("Successfully written to .agents/class3_maths_ch4_sims.py")

