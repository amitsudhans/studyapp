#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assemble simulators 1 to 16 into .agents/class10_science_ch5_sims.py.
"""

import json

with open('.agents/c10s_ch5_sims_part1.json', 'r', encoding='utf-8') as f:
    part1 = json.load(f)
with open('.agents/c10s_ch5_sims_part2.json', 'r', encoding='utf-8') as f:
    part2 = json.load(f)

sims = {}
for k, v in part1.items():
    sims[int(k)] = v
for k, v in part2.items():
    sims[int(k)] = v

assert len(sims) == 16, f"Expected 16 simulators, got {len(sims)}"

out_py = f'''# -*- coding: utf-8 -*-
"""
Simulators 1 to 16 HTML markup for NCERT Class 10 Science Chapter 5: Life Processes.
"""

simulators = {repr(sims)}
'''

with open('.agents/class10_science_ch5_sims.py', 'w', encoding='utf-8') as f:
    f.write(out_py)

print("Successfully generated .agents/class10_science_ch5_sims.py with integer keys 1..16!")
