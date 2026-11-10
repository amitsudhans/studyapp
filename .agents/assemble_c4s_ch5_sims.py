# -*- coding: utf-8 -*-
"""Class 4 Science Chapter 5: Food for Health - Simulators Assembler"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from make_c4s_ch5_sims_part1 import sims_part1
from make_c4s_ch5_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16, f"Expected 16 simulators, found {len(all_sims)}"

output_file = os.path.join(os.path.dirname(__file__), "class4_science_ch5_sims.py")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Science Chapter 5: Food for Health - Assembled Simulators HTML"""\n\n')
    f.write(f"simulators = {repr(all_sims)}\n")

print(f"Wrote all 16 simulators to {output_file} successfully!")

