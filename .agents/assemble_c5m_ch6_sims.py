# -*- coding: utf-8 -*-
"""
Assemble and verify Class 5 Maths Chapter 6 simulators module.
"""

import re
from make_c5m_ch6_sims_part1 import SIMULATORS_PART1
from make_c5m_ch6_sims_part2 import SIMULATORS_PART2

ALL_SIMULATORS = {}
ALL_SIMULATORS.update(SIMULATORS_PART1)
ALL_SIMULATORS.update(SIMULATORS_PART2)

assert len(ALL_SIMULATORS) == 16, f"Expected 16 simulators, got {len(ALL_SIMULATORS)}"
for i in range(1, 17):
    sim_id = f"sim_slide_{i}"
    assert sim_id in ALL_SIMULATORS, f"Missing simulator: {sim_id}"

output_code = f'''# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: The Dairy Farm
NEP 2020 / Joyful Mathematics
Compiled Simulators Module (16 Simulators)
"""

ALL_SIMULATORS = {repr(ALL_SIMULATORS)}
'''

# Raw LaTeX check
raw_latex_patterns = [r'\\frac', r'\\times', r'\\cdot', r'\\div', r'\\pm', r'\\le', r'\\ge']
for pattern in raw_latex_patterns:
    matches = re.findall(pattern, output_code)
    assert not matches, f"Raw LaTeX pattern {pattern} found in assembled simulators!"

with open(".agents/class5_maths_ch6_sims.py", "w", encoding="utf-8") as f:
    f.write(output_code)

print("VERIFIED PASS: .agents/class5_maths_ch6_sims.py successfully created! (16 simulators verified)")

