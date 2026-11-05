# -*- coding: utf-8 -*-
"""
Assemble Chapter 12 Master Slides Data
Combines Part 1, Part 2, and Part 3 into class5_maths_ch12_data.py
"""

import sys
sys.path.append('.agents')
from generate_c5m_ch12_part1 import slides_part1
from generate_c5m_ch12_part2 import slides_part2
from generate_c5m_ch12_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

# Check all IDs and word counts
for s in all_slides:
    words = len(s['lecture'].split())
    if s['id'] <= 16:
        assert 195 <= words <= 215, f"Slide {s['id']} lecture words {words} out of range [195, 215]!"
        assert len(s.get('checkpoints', [])) == 2, f"Slide {s['id']} does not have 2 checkpoints!"
    else:
        assert len(s.get('questions', [])) == 10, f"Slide {s['id']} does not have 10 quiz questions!"

print("All slide rules verified! Writing class5_maths_ch12_data.py...")

with open('.agents/class5_maths_ch12_data.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""NCERT Class 5 Mathematics — Chapter 12: Racing Seconds Master Data"""\n\n')
    import pprint
    f.write("slides = " + pprint.pformat(all_slides, width=120, sort_dicts=False) + "\n")

print("Successfully written .agents/class5_maths_ch12_data.py!")
