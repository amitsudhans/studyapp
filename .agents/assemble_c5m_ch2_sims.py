# assemble_c5m_ch2_sims.py
"""Assemble all 16 simulators for Class 5 Maths Chapter 2: Fractions."""

import sys
import re
from make_c5m_ch2_sims_part1 import SIMS_PART1
from make_c5m_ch2_sims_part2 import SIMS_PART2

ALL_SIMS = {}
ALL_SIMS.update(SIMS_PART1)
ALL_SIMS.update(SIMS_PART2)

print(f"Total simulators assembled: {len(ALL_SIMS)}")
assert len(ALL_SIMS) == 16, f"Expected 16 simulators, got {len(ALL_SIMS)}"

# Verify no raw LaTeX
latex_pat = re.compile(r'(\\\([^\)]+\\\)|\\\[[^\]]+\\\]|\$[^$]+\$)')
errors = 0
for i in range(1, 17):
    sim_html = ALL_SIMS[i]
    matches = latex_pat.findall(sim_html)
    if matches:
        print(f"ERROR: Raw LaTeX found in Simulator {i}: {matches}")
        errors += 1

if errors > 0:
    print(f"Verification failed with {errors} errors.")
    sys.exit(1)

print("Zero raw LaTeX verified across all 16 simulators!")

# Write to class5_maths_ch2_sims.py
with open('/home/lead-programmer/study-app/.agents/class5_maths_ch2_sims.py', 'w', encoding='utf-8') as f:
    f.write('"""All 16 bespoke simulators for Class 5 Maths Chapter 2: Fractions."""\n\n')
    f.write('SIMULATORS = {\n')
    for i in range(1, 17):
        f.write(f'    {i}: {repr(ALL_SIMS[i])},\n')
    f.write('}\n')

print("Successfully generated .agents/class5_maths_ch2_sims.py")

