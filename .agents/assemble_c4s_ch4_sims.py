# -*- coding: utf-8 -*-
"""
Assemble Chapter 4 Simulators (1 to 16) into class4_science_ch4_sims.py
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from class4_science_ch4_sims_part1 import simulators_part1
from class4_science_ch4_sims_part2 import simulators_part2

simulators = {}
simulators.update(simulators_part1)
simulators.update(simulators_part2)

assert len(simulators) == 16, f"Expected 16 simulators, found {len(simulators)}"

out_path = os.path.join(os.path.dirname(__file__), "class4_science_ch4_sims.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nClass 4 Science Chapter 4 Simulators Master File (1 to 16)\n"""\n\n')
    f.write(f"simulators = {repr(simulators)}\n")

print(f"Master simulators written to {out_path} ({len(simulators)} simulators)")

