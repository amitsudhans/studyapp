"""Assemble all 16 simulators for Class 10 Science Chapter 2 into class10_science_ch2_sims.py
"""

import sys

sys.path.insert(0, ".agents")

import make_c10s_ch2_sims_part1 as p1
import make_c10s_ch2_sims_part2 as p2

all_sims = {}
all_sims.update(p1.simulators)
all_sims.update(p2.simulators)

assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"
for i in range(1, 17):
    assert i in all_sims, f"Missing simulator {i}"
    assert len(all_sims[i]) > 100, f"Simulator {i} is too short"

with open(".agents/class10_science_ch2_sims.py", "w") as f:
    f.write("# Class 10 Science Chapter 2: Acids, Bases and Salts Simulators\n")
    f.write("simulators = " + repr(all_sims) + "\n")

print("Successfully written .agents/class10_science_ch2_sims.py with all 16 simulators!")
