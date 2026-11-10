# assemble_c4s_ch7_sims.py
from make_c4s_ch7_sims_part1 import simulators_part1
from make_c4s_ch7_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"
for i in range(1, 17):
    sim_id = f"sim-{i}"
    assert sim_id in all_sims, f"Missing {sim_id}"

with open(".agents/class4_science_ch7_sims.py", "w", encoding="utf-8") as f:
    f.write("# Class 4 Science Chapter 7 Simulators (1 to 16)\n")
    f.write("simulators = " + repr(all_sims) + "\n")

print("Assembled all 16 simulators into class4_science_ch7_sims.py successfully!")

