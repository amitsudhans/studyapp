# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 11: Assemble all 20 slides into class10_science_ch11_data.py
"""

import json
import re

with open(".agents/c10s_ch11_part1.json", "r", encoding="utf-8") as f:
    p1 = json.load(f)

with open(".agents/c10s_ch11_part2.json", "r", encoding="utf-8") as f:
    p2 = json.load(f)

with open(".agents/c10s_ch11_part3.json", "r", encoding="utf-8") as f:
    p3 = json.load(f)

all_slides = p1 + p2 + p3
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

forbidden_personas = ["Dr.", "Dr ", "Doctor", "Sir ", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof.", "Professor", "Raghav"]

for s in all_slides:
    sid = s["id"]
    title = s["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' out of range ({title_words} words)"

    slide_str = json.dumps(s)
    for forb in forbidden_personas:
        matches = re.findall(rf"\b{re.escape(forb.strip())}\b", slide_str, re.IGNORECASE)
        if matches:
            raise AssertionError(f"Slide {sid} contains forbidden term '{forb}': {matches}")

    if sid <= 16:
        wc = len(s["speech"].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc}"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
    else:
        assert s["speech"] == "", f"Slide {sid} speech must be empty"
        assert len(s["questions"]) == 10, f"Slide {sid} must have 10 challenge questions"

# Write out python data file
with open(".agents/class10_science_ch11_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 10 Science Chapter 11 Slide Data"""\n\n')
    f.write("slides = " + json.dumps(all_slides, indent=2) + "\n")

print("Successfully validated and wrote .agents/class10_science_ch11_data.py with all 20 slides!")
