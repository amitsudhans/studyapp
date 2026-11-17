# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 8: Heredity
Merge simulators 1-16 into class10_science_ch8_sims.py
"""

import json

with open('.agents/c10s_ch8_sims_part1.json', 'r', encoding='utf-8') as f:
    sims1 = json.load(f)

with open('.agents/c10s_ch8_sims_part2.json', 'r', encoding='utf-8') as f:
    sims2 = json.load(f)

sims = {}
for k, v in sims1.items():
    sims[int(k)] = v
for k, v in sims2.items():
    sims[int(k)] = v

print(f"Total simulators loaded: {len(sims)}")
print(f"Keys: {sorted(sims.keys())}")
assert len(sims) == 16, f"Expected 16 simulators, found {len(sims)}"

with open('.agents/class10_science_ch8_sims.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write(f"simulators = {repr(sims)}\n")

print("Saved .agents/class10_science_ch8_sims.py successfully!")
