# -*- coding: utf-8 -*-
"""
Assemble and verify Class 5 Maths Chapter 6 data module.
"""

import re
from generate_c5m_ch6_part1 import SLIDES_PART1
from generate_c5m_ch6_part2 import SLIDES_PART2
from generate_c5m_ch6_part3 import MASTERY_CHALLENGES

ALL_SLIDES = SLIDES_PART1 + SLIDES_PART2 + MASTERY_CHALLENGES

# Sanity checks
assert len(ALL_SLIDES) == 20, f"Expected 20 slides, got {len(ALL_SLIDES)}"
for idx, s in enumerate(ALL_SLIDES):
    assert s["id"] == idx + 1, f"Slide ID mismatch at index {idx}: {s['id']}"
    words = s["title"].strip().split()
    assert 1 <= len(words) <= 3, f"Slide title '{s['title']}' must be 1 to 3 words!"

total_checkpoints = sum(len(s.get("checkpoints", [])) for s in ALL_SLIDES)
assert total_checkpoints == 32, f"Expected 32 checkpoints across slides 1-16, got {total_checkpoints}"

total_quiz = sum(len(s.get("questions", [])) for s in ALL_SLIDES)
assert total_quiz == 40, f"Expected 40 quiz questions across slides 17-20, got {total_quiz}"

output_code = f'''# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: The Dairy Farm
NEP 2020 / Joyful Mathematics
Compiled Data Module
"""

ALL_SLIDES = {repr(ALL_SLIDES)}
'''

# Raw LaTeX check
raw_latex_patterns = [r'\\frac', r'\\times', r'\\cdot', r'\\div', r'\\pm', r'\\le', r'\\ge']
for pattern in raw_latex_patterns:
    matches = re.findall(pattern, output_code)
    assert not matches, f"Raw LaTeX pattern {pattern} found in assembled data!"

with open(".agents/class5_maths_ch6_data.py", "w", encoding="utf-8") as f:
    f.write(output_code)

print("VERIFIED PASS: .agents/class5_maths_ch6_data.py successfully created! (20 slides, 32 checkpoints, 40 quizzes)")

