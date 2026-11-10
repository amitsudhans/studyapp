#!/usr/bin/env python3
"""
Assemble all 20 slides data for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Validates all word counts (195-215 words for slides 1-16), titles (1-3 words), checkpoints (2 per teaching slide),
and challenges (10 questions each with 4 options, hint, explanation, and 3-step solutions).
Outputs: .agents/class3_maths_ch9_data.py
"""

import sys
sys.path.insert(0, ".agents")

from generate_c3m_ch9_part1 import slides_part1
from generate_c3m_ch9_part2 import slides_part2
from generate_c3m_ch9_part3 import challenges

all_slides = slides_part1 + slides_part2 + challenges

print(f"Total slides loaded: {len(all_slides)}")
assert len(all_slides) == 20

for s in all_slides:
    title_words = len(s["title"].split())
    assert title_words <= 3, f"Slide {s['id']} title has {title_words} words: '{s['title']}'"
    if s["id"] <= 16:
        wc = len(s["speech"].split())
        assert 195 <= wc <= 215, f"Slide {s['id']} speech word count {wc} out of range (195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} checkpoints count != 2"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4
            assert 0 <= cp["answer"] <= 3
            assert len(cp["hint"]) > 0
            assert len(cp["explanation"]) > 0
    else:
        assert len(s["questions"]) == 10
        for q in s["questions"]:
            assert len(q["options"]) == 4
            assert 0 <= q["answer"] <= 3
            assert len(q["hint"]) > 0
            assert len(q["explanation"]) > 0
            assert len(q["solution_steps"]) == 3

print("All 20 slides strictly verified!")

import pprint

with open(".agents/class3_maths_ch9_data.py", "w") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II Slides Data"""\n\n')
    f.write("slides_data = ")
    pprint.pprint(all_slides, stream=f, indent=4, width=120)
    f.write("\n")

print("Successfully written .agents/class3_maths_ch9_data.py")
