"""
Assemble simulators 1 to 16 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Checks for zero raw LaTeX and compiles .agents/class5_science_ch10_sims.py
"""

import sys
import re

from make_c5ch10_sims_part1 import SIMS as S1
from make_c5ch10_sims_part2 import SIMS as S2

SIMS = {}
SIMS.update(S1)
SIMS.update(S2)

print(f"Total simulators collected: {len(SIMS)}")
assert len(SIMS) == 16, f"Expected 16 simulators, got {len(SIMS)}"

raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')
found_latex = False

out_lines = [
    '"""\nSimulators 1 to 16 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home\nZero raw LaTeX! Clean Unicode symbols.\n"""\n',
    'SIMS = {}\n'
]

for idx in range(1, 17):
    sim_content = SIMS[idx]
    matches = raw_latex_pattern.findall(sim_content)
    math_cmds = [m for m in matches if m in ['frac', 'times', 'sqrt', 'cdot', 'text', 'le', 'ge', 'pm', 'circ', 'degree']]
    if math_cmds:
        print(f"ERROR: Raw LaTeX found in SIM {idx}: {math_cmds}")
        found_latex = True
    out_lines.append(f'SIMS[{idx}] = """{sim_content}"""\n\n')

if found_latex:
    sys.exit(1)

with open('.agents/class5_science_ch10_sims.py', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print("Successfully written .agents/class5_science_ch10_sims.py with 16 simulators!")

