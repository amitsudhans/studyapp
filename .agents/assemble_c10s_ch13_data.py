# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 13: Assemble all 20 slides into class10_science_ch13_data.py
"""

import json

with open(".agents/c10s_ch13_part1.json", "r", encoding="utf-8") as f:
    p1 = json.load(f)

with open(".agents/c10s_ch13_part2.json", "r", encoding="utf-8") as f:
    p2 = json.load(f)

with open(".agents/c10s_ch13_part3.json", "r", encoding="utf-8") as f:
    p3 = json.load(f)

all_slides = p1 + p2 + p3
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

for i, s in enumerate(all_slides):
    sid = s["id"]
    assert sid == i + 1, f"Slide index mismatch: id={sid}, index={i+1}"
    title_words = len(s["title"].split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{s['title']}' must have 1-3 words, got {title_words}"
    if sid <= 16:
        wc = len(s["speech"].split())
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
    else:
        assert s["speech"] == "", f"Slide {sid} must be silent"
        assert len(s["questions"]) == 10, f"Slide {sid} must have 10 challenge questions"

    slide_str = json.dumps(s, ensure_ascii=False)
    for forbidden in ["Raghav", "Dr.", "Dr ", "Sir", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof."]:
        assert forbidden not in slide_str, f"Forbidden term '{forbidden}' in slide {sid}"

with open(".agents/class10_science_ch13_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 10 Science Chapter 13 Slide Data Dictionary"""\n\n')
    f.write("slides = " + json.dumps(all_slides, indent=2, ensure_ascii=False) + "\n")

print(f"Successfully validated and wrote .agents/class10_science_ch13_data.py with all {len(all_slides)} slides!")
