# -*- coding: utf-8 -*-
"""
Assemble and Validate Class 4 Mathematics Chapter 14 Simulators
Produces .agents/class4_maths_ch14_sims.py
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))
from make_c4m_ch14_sims_part1 import simulators_part1
from make_c4m_ch14_sims_part2 import simulators_part2

simulators = {}
simulators.update(simulators_part1)
simulators.update(simulators_part2)

assert len(simulators) == 16, f"Expected 16 simulators, found {len(simulators)}"
print(f"Successfully assembled {len(simulators)} simulators.")

# Check for banned words in simulators
BANNED_NAMES = ['rohan', 'anjali', 'raju', 'rani', 'roja', 'raghav', 'diya', 'anvi', 'gulabo', 'shrinathan', 'mirabai', 'gundappa', 'muniamma', 'jaspreet', 'gulnaz', 'lou', 'daisy', 'sapan', 'udaya', 'sumitha', 'ikra', 'samina', 'shirley', 'shiv', 'sumedha', 'parv', 'chinnu']
BANNED_PERSONAS = ['mr.', 'mrs.', 'miss', 'dr.']

for idx, html in simulators.items():
    lower_html = html.lower()
    for name in BANNED_NAMES:
        assert f" {name} " not in lower_html, f"Banned name '{name}' found in simulator {idx}!"
    for p in BANNED_PERSONAS:
        assert f" {p} " not in lower_html, f"Banned persona '{p}' found in simulator {idx}!"
    assert "$" not in html, f"Raw LaTeX dollar sign found in simulator {idx}!"

with open('.agents/class4_maths_ch14_sims.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 14 Simulators Dictionary"""\n\n')
    f.write("SIMULATORS = {\n")
    for idx in sorted(simulators.keys()):
        f.write(f"    {idx}: '''{simulators[idx]}''',\n")
    f.write("}\n")

print("Generated .agents/class4_maths_ch14_sims.py successfully!")

