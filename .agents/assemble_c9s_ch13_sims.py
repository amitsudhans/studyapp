from make_c9s_ch13_sims_part1 import sims_part1
from make_c9s_ch13_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

print(f"Total simulators assembled: {len(all_sims)} (expected 16)")

with open(".agents/class9_science_ch13_sims.py", "w") as f:
    f.write("# NCERT Class 9 Science - Chapter 13: Earth as a System: Energy, Matter, and Life Simulators\n")
    f.write("from make_c9s_ch13_sims_part1 import sims_part1\n")
    f.write("from make_c9s_ch13_sims_part2 import sims_part2\n\n")
    f.write("sims = {}\n")
    f.write("sims.update(sims_part1)\n")
    f.write("sims.update(sims_part2)\n")
