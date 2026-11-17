#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 11 Simulators Combiner
"""

from make_c9s_ch11_sims_part1 import sims_part1
from make_c9s_ch11_sims_part2 import sims_part2

simulators = {}
simulators.update(sims_part1)
simulators.update(sims_part2)

if __name__ == "__main__":
    print(f"Total simulators assembled: {len(simulators)}")
    assert len(simulators) == 16, f"Expected 16 simulators, got {len(simulators)}"
    print("Keys:", sorted(simulators.keys()))
