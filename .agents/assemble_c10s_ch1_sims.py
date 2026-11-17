import sys
sys.path.append(".agents")

from make_c10s_ch1_sims_part1 import sims_part1
from make_c10s_ch1_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

print(f"Total simulators assembled: {len(all_sims)} (expected 16)")
assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"

with open(".agents/class10_science_ch1_sims.py", "w") as f:
    f.write("# NCERT Class 10 Science - Chapter 1: Chemical Reactions and Equations Simulators\n")
    f.write("from make_c10s_ch1_sims_part1 import sims_part1\n")
    f.write("from make_c10s_ch1_sims_part2 import sims_part2\n\n")
    f.write("sims = {}\n")
    f.write("sims.update(sims_part1)\n")
    f.write("sims.update(sims_part2)\n")

print("Successfully written .agents/class10_science_ch1_sims.py")
