#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 11: Making Things
Combined Simulators Assembler (Simulators 1 to 16)
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))

from make_c3s_ch11_sims_part1 import simulators_part1
from make_c3s_ch11_sims_part2 import simulators_part2

simulators = {**simulators_part1, **simulators_part2}

if __name__ == "__main__":
    print(f"Combined simulators count: {len(simulators)}")
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    for i in range(1, 17):
        assert i in simulators, f"Missing simulator {i}"
        assert len(simulators[i].strip()) > 300, f"Simulator {i} looks too short"
    print("All 16 interactive simulators for Chapter 11 verified!")
