#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for Class 8 Mathematics Chapter 8 Interactive Simulators (1-16)
"""

from make_c8m_ch8_sims_part1 import simulators_part1
from make_c8m_ch8_sims_part2 import simulators_part2

simulators = {**simulators_part1, **simulators_part2}

if __name__ == "__main__":
    print(f"Combined simulators count: {len(simulators)}")
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    for i in range(1, 17):
        assert i in simulators and len(simulators[i].strip()) > 100
    print("All 16 interactive simulators for Class 8 Maths Chapter 8 verified!")
