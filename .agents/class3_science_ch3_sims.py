#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 3: Celebrating Festivals
Assembled Simulators File: Simulators 1 to 16
"""

import sys
sys.path.append(".agents")

from make_c3s_ch3_sims_part1 import simulators_part1
from make_c3s_ch3_sims_part2 import simulators_part2

simulators = {}
simulators.update(simulators_part1)
simulators.update(simulators_part2)

if __name__ == "__main__":
    print(f"Total simulators assembled: {len(simulators)}")
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    for sid in range(1, 17):
        assert sid in simulators, f"Missing simulator for slide {sid}"
        assert len(simulators[sid]) > 100, f"Simulator {sid} content too short"
    print("ALL 16 SIMULATORS STRICTLY VALIDATED!")
