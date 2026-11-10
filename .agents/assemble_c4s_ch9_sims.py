# -*- coding: utf-8 -*-
"""
Assemble all 16 simulators into class4_science_ch9_sims.py
Class 4 Science Chapter 9: Different Lands, Different Lives
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))

from make_c4s_ch9_sims_part1 import simulators_part1
from make_c4s_ch9_sims_part2 import simulators_part2

all_simulators = {}
all_simulators.update(simulators_part1)
all_simulators.update(simulators_part2)

assert len(all_simulators) == 16, f"Expected 16 simulators, got {len(all_simulators)}"

output_path = os.path.join(os.path.dirname(__file__), "class4_science_ch9_sims.py")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nNCERT Class 4 Science - Chapter 9: Different Lands, Different Lives\nInteractive SVG/HTML Simulators (16 Simulators)\n"""\n\n')
    f.write("simulators = {\n")
    for key, val in all_simulators.items():
        clean_val = val.strip().replace('"""', '\\"\\"\\"')
        f.write(f'    "{key}": """{clean_val}""",\n\n')
    f.write("}\n")

print(f"Successfully assembled {len(all_simulators)} simulators into {output_path}")

