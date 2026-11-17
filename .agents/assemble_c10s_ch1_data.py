import json
import re
import sys
sys.path.append(".agents")

from generate_c10s_ch1_part1 import slides_part1
from generate_c10s_ch1_part2 import slides_part2
from generate_c10s_ch1_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

forbidden_titles = ["Dr.", "Dr ", "Sir ", "Madam ", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof.", "Prof "]
forbidden_names = ["Raghav", "Reiaan", "Aarav", "Priya", "Ananya", "Rohan"]

for idx, s in enumerate(all_slides):
    slide_num = idx + 1
    title = s["title"]
    title_words = len(title.split())
    if title_words < 1 or title_words > 3:
        raise ValueError(f"Slide {slide_num} title '{title}' has {title_words} words (expected 1-3)!")

    speech = s.get("speech", "")
    words = speech.split()
    wc = len(words)
    if slide_num <= 16:
        if wc < 195 or wc > 215:
            raise ValueError(f"Slide {slide_num} speech word count is {wc} (expected 195-215)!")
        if len(s.get("checkpoints", [])) != 2:
            raise ValueError(f"Slide {slide_num} must have 2 checkpoints!")
    else:
        if wc != 0:
            raise ValueError(f"Slide {slide_num} speech word count is {wc} (expected 0)!")
        if len(s.get("questions", [])) != 10:
            raise ValueError(f"Slide {slide_num} must have 10 questions!")

    # Check forbidden personas & names
    slide_json = json.dumps(s).lower()
    for fp in forbidden_titles:
        if fp.lower() in slide_json:
            raise ValueError(f"Slide {slide_num} contains forbidden title: '{fp}'")

    for fn in forbidden_names:
        if fn.lower() in slide_json:
            raise ValueError(f"Slide {slide_num} contains forbidden name: '{fn}'")

print("All 20 slides passed strict validation!")

with open(".agents/class10_science_ch1_data.py", "w") as f:
    f.write("# NCERT Class 10 Science - Chapter 1: Chemical Reactions and Equations\n")
    f.write("from generate_c10s_ch1_part1 import slides_part1\n")
    f.write("from generate_c10s_ch1_part2 import slides_part2\n")
    f.write("from generate_c10s_ch1_part3 import slides_part3\n\n")
    f.write("slides_data = slides_part1 + slides_part2 + slides_part3\n")

print("Successfully written .agents/class10_science_ch1_data.py")
