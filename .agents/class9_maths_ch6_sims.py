#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for NCERT Class 9 Maths Chapter 6 Simulators (Slides 1-16)
"""

from make_c9m_ch6_sims_part1 import simulators_part1
from make_c9m_ch6_sims_part2 import simulators_part2

simulators = {**simulators_part1, **simulators_part2}

if __name__ == "__main__":
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    print("Chapter 6 Simulators assembled cleanly: 16 interactive modules.")
