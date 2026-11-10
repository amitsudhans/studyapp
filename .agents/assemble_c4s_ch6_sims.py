# assemble_c4s_ch6_sims.py
import sys
import os

sys.path.append(os.path.abspath('.agents'))
from make_c4s_ch6_sims_part1 import simulators_part1
from make_c4s_ch6_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"
for i in range(1, 17):
    sim_id = f"sim-{i}"
    assert sim_id in all_sims, f"Missing {sim_id}"
    assert len(all_sims[sim_id]) > 50, f"Simulator {sim_id} is too short"

output_path = os.path.join('.agents', 'class4_science_ch6_sims.py')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# Class 4 Science Chapter 6 Simulators\n")
    f.write("simulators = {\n")
    for k, v in all_sims.items():
        f.write(f"    {repr(k)}: {repr(v)},\n")
    f.write("}\n")

print(f"Successfully wrote {output_path} with 16 simulators!")

