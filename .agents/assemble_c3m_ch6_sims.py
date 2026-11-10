# -*- coding: utf-8 -*-
"""Assembles all 16 simulators for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from make_c3m_ch6_sims_part1 import simulators_part1
from make_c3m_ch6_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

assert len(all_sims) == 16, f"Expected 16 simulators, found {len(all_sims)}"

out_path = os.path.join(os.path.dirname(__file__), "class3_maths_ch6_sims.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Complete set of 16 simulators for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""\n\n')
    f.write("simulators = {\n")
    for k, v in all_sims.items():
        f.write(f"    {repr(k)}: {repr(v)},\n")
    f.write("}\n")

print(f"Successfully assembled all 16 simulators into {out_path}!")
