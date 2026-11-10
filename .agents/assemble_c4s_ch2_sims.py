# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Simulator Assembler: Combines Sims Part 1 and Part 2 into class4_science_ch2_sims.py.
"""

import pprint
import re
from make_c4s_ch2_sims_part1 import sims_part1
from make_c4s_ch2_sims_part2 import sims_part2

all_sims = {}
all_sims.update(sims_part1)
all_sims.update(sims_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"

BANNED_NAMES = [
    r'\bnavya\b', r'\bdada\s*ji\b', r'\bdada\b', r'\bdadaji\b', r'\braghav\b', r'\braju\b',
    r'\bchandan\b', r'\brani\b', r'\broja\b', r'\bdiya\b', r'\banvi\b',
    r'\bgulabo\b', r'\bshrinathan\b', r'\bmirabai\b', r'\bgundappa\b', r'\bmuniamma\b',
    r'\bjaspreet\b', r'\bgulnaz\b', r'\blou\b', r'\bdaisy\b', r'\bsapan\b', r'\budaya\b',
    r'\bsumitha\b', r'\bikra\b', r'\bsamina\b', r'\bshirley\b', r'\bshiv\b', r'\bsumedha\b',
    r'\bparv\b', r'\bchinnu\b', r'\brohan\b', r'\banjali\b', r'\bamit\b', r'\bpriya\b'
]

BANNED_PERSONAS = [
    r'\bdr\b', r'\bdr\.\b', r'\bsir\b', r'\bmadam\b', r'\bmr\b', r'\bmr\.\b',
    r'\bmrs\b', r'\bmrs\.\b', r'\bmiss\b'
]

for s_id, html in all_sims.items():
    html_lower = html.lower()
    for name_pat in BANNED_NAMES:
        m = re.search(name_pat, html_lower)
        assert not m, f"Sim {s_id} contains banned name '{m.group(0)}': {name_pat}"
    for persona_pat in BANNED_PERSONAS:
        m = re.search(persona_pat, html_lower)
        assert not m, f"Sim {s_id} contains banned persona '{m.group(0)}': {persona_pat}"

print("All 16 simulators passed validation checks!")

output_code = f"""# -*- coding: utf-8 -*-
\"\"\"
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Master Simulators File
Generated automatically by assemble_c4s_ch2_sims.py
\"\"\"

simulators = {pprint.pformat(all_sims, width=120, sort_dicts=False)}
"""

with open(".agents/class4_science_ch2_sims.py", "w", encoding="utf-8") as f:
    f.write(output_code)

print("Master simulators saved to .agents/class4_science_ch2_sims.py successfully!")

