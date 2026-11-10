#!/usr/bin/env python3
"""
NCERT Class 3 Science - Chapter 4: Getting to Know Plants
Combined Simulators (Slides 1 to 16)
"""

import sys
sys.path.append(".agents")

from make_c3s_ch4_sims_part1 import simulators_part1
from make_c3s_ch4_sims_part2 import simulators_part2

simulators = {**simulators_part1, **simulators_part2}

if __name__ == "__main__":
    print(f"Total simulators combined: {len(simulators)}")
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    for i in range(1, 17):
        assert i in simulators, f"Simulator {i} missing"
        sim = simulators[i]
        assert isinstance(sim, str) and len(sim) > 100, f"Simulator {i} is invalid or too short"
        print(f"Simulator {i} verified: {len(sim)} chars")
    print("All 16 simulators verified successfully!")
