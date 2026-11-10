# -*- coding: utf-8 -*-
"""
Assemble simulators for Class 4 Science Chapter 10: Our Sky
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from make_c4s_ch10_sims_part1 import simulators_part1
from make_c4s_ch10_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

print(f"Total simulators assembled: {len(all_sims)}")

out_path = os.path.join(os.path.dirname(__file__), "class4_science_ch10_sims.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Assembled Simulators for Class 4 Science Chapter 10"""\n\n')
    f.write("simulators = {\n")
    for k, v in all_sims.items():
        f.write(f"    {repr(k)}: {repr(v)},\n")
    f.write("}\n")

print(f"Wrote {out_path} ({os.path.getsize(out_path)} bytes)")

