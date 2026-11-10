#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
from make_c3s_ch2_sims_part1 import sims_part1
from make_c3s_ch2_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"
for i in range(1, 17):
    assert i in all_sims, f"Missing simulator for slide {i}"
    assert len(all_sims[i].strip()) > 50, f"Simulator {i} content suspiciously short!"

print(f"All 16 simulators verified! Writing .agents/class3_science_ch2_sims.py...")

out_path = os.path.join(os.path.dirname(__file__), "class3_science_ch2_sims.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write('"""NCERT Class 3 Science (Our Wondrous World) - Chapter 2: Going to the Mela full simulators dataset"""\n\n')
    f.write("simulators = " + repr(all_sims) + "\n")

print(f"Saved {out_path} successfully.")
