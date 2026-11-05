"""
Assemble all 16 simulators into class5_science_ch6_sims.py
Validate zero raw LaTeX patterns.
"""
import sys
import re

sys.path.append(".agents")
from make_sims_part1 import SIMS as SIMS1
from make_sims_part2 import SIMS as SIMS2

SIMULATORS = {}
for k, v in SIMS1.items():
    SIMULATORS[k] = v
for k, v in SIMS2.items():
    SIMULATORS[k] = v

assert len(SIMULATORS) == 16, f"Expected 16 simulators, got {len(SIMULATORS)}"

# Check for raw LaTeX patterns
latex_patterns = [
    r'\\frac', r'\\text', r'\\times', r'\\div', r'\\circ', r'\\theta', r'\\le', r'\\ge',
    r'\\approx', r'\\pm', r'\\degree', r'\$', r'\\sqrt'
]

combined_text = str(SIMULATORS)
for pat in latex_patterns:
    matches = re.findall(pat, combined_text)
    if matches:
        print(f"WARNING: Found LaTeX pattern {pat}: {matches}")
        sys.exit(1)

print("Zero raw LaTeX check passed for all 16 simulators!")

out_file = ".agents/class5_science_ch6_sims.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write('"""\n16 Bespoke SVG/HTML Interactive Simulators for NCERT Class 5 Science Chapter 6: Some Unique Places\nZero raw LaTeX! Clean Unicode symbols.\n"""\n\n')
    f.write(f"SIMULATORS = {repr(SIMULATORS)}\n")

print(f"Successfully generated {out_file} with 16 simulators.")
