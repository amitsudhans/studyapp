# -*- coding: utf-8 -*-
"""
Assemble Slides 1 to 20 into class4_science_ch9_data.py
Class 4 Science Chapter 9: Different Lands, Different Lives
"""

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__)))

from generate_c4s_ch9_part1 import slides_part1
from generate_c4s_ch9_part2 import slides_part2
from generate_c4s_ch9_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

output_path = os.path.join(os.path.dirname(__file__), "class4_science_ch9_data.py")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nNCERT Class 4 Science - Chapter 9: Different Lands, Different Lives\nCurriculum Slide Data (20 Slides)\n"""\n\n')
    f.write(f"slides = {json.dumps(all_slides, indent=4, ensure_ascii=False)}\n")

print(f"Successfully assembled {len(all_slides)} slides into {output_path}")

