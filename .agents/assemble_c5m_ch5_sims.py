#!/usr/bin/env python3
"""
Assemble Simulators 1 to 16 for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""
import re
from make_c5m_ch5_sims_part1 import sims_1_to_8
from make_c5m_ch5_sims_part2 import sims_9_to_16

all_sims = {}
all_sims.update(sims_1_to_8)
all_sims.update(sims_9_to_16)

assert len(all_sims) == 16, f"Expected 16 simulators, found {len(all_sims)}"

# Check for raw LaTeX in simulators
for sim_id, sim_html in all_sims.items():
    matches = re.findall(r"\\(?:frac|times|div|pm|text|cdot|\$)|(?<!\\)\$[^$]+\$", sim_html)
    if matches:
        raise ValueError(f"Raw LaTeX detected in Simulator {sim_id}: {matches}")

print("VERIFIED: All 16 Simulators passed zero raw LaTeX verification!")

with open(".agents/class5_maths_ch5_sims.py", "w", encoding="utf-8") as f:
    f.write('"""\nSimulators 1 to 16 for NCERT Class 5 Mathematics - Chapter 5: Far and Near\n"""\n\n')
    f.write(f"simulators = {repr(all_sims)}\n")

print("Successfully written .agents/class5_maths_ch5_sims.py")

