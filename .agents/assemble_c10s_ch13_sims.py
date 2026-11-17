# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 13: Assemble all 16 simulators into class10_science_ch13_sims.py
"""

import json

with open(".agents/c10s_ch13_sims_part1.json", "r", encoding="utf-8") as f:
    s1 = json.load(f)

with open(".agents/c10s_ch13_sims_part2.json", "r", encoding="utf-8") as f:
    s2 = json.load(f)

simulators = {}
for k, v in s1.items():
    simulators[int(k)] = v

for k, v in s2.items():
    simulators[int(k)] = v

assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
for i in range(1, 17):
    assert i in simulators, f"Missing simulator {i}"

with open(".agents/class10_science_ch13_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 10 Science Chapter 13 Simulators Dictionary"""\n\n')
    f.write("simulators = " + json.dumps(simulators, indent=2, ensure_ascii=False) + "\n")

print(f"Successfully assembled all {len(simulators)} simulators into .agents/class10_science_ch13_sims.py!")
