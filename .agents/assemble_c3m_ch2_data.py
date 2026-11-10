# -*- coding: utf-8 -*-
"""
Assemble Slides Data for Class 3 Mathematics Chapter 2: Toy Joy
Combines parts 1, 2, and 3 into class3_maths_ch2_data.py with strict validation.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from generate_c3m_ch2_part1 import slides_part1
from generate_c3m_ch2_part2 import slides_part2
from generate_c3m_ch2_part3 import slides_part3

all_slides = []
all_slides.extend(slides_part1)
all_slides.extend(slides_part2)
all_slides.extend(slides_part3)

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20

# Strict verification of all 20 slides
for i, s in enumerate(all_slides):
    sid = s["id"]
    assert sid == i + 1, f"Slide index mismatch: expected {i+1}, got {sid}"
    title = s["title"]
    tw = len(title.split())
    assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
    
    if sid <= 16:
        speech = s["speech"]
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count {wc} out of range 195-215!"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint options != 4"
            assert cp["ans"] in cp["options"], f"Slide {sid} ans not in options"
    else:
        questions = s["questions"]
        assert len(questions) == 10, f"Challenge slide {sid} must have 10 questions"
        for q in questions:
            assert len(q["options"]) == 4, f"Question {q['id']} options != 4"
            assert q["ans"] in q["options"], f"Question {q['id']} ans not in options"
            assert "hint" in q and "explanation" in q and "solution_steps" in q

out_file = os.path.join(os.path.dirname(__file__), "class3_maths_ch2_data.py")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""NCERT Class 3 Mathematics - Chapter 2: Toy Joy Slide Data"""\n\n')
    f.write("slides = [\n")
    for s in all_slides:
        f.write(f"    {repr(s)},\n")
    f.write("]\n")

print(f"Slide data written to {out_file} ({os.path.getsize(out_file)} bytes)")

