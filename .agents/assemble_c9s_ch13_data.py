import json
import re
from generate_c9s_ch13_part1 import slides_part1
from generate_c9s_ch13_part2 import slides_part2
from generate_c9s_ch13_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides: {len(all_slides)}")

forbidden_titles = ["Dr.", "Dr ", "Sir ", "Madam ", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof.", "Prof "]
forbidden_names = ["Raghav", "Reiaan", "Aarav", "Priya", "Ananya", "Rohan"]

for idx, s in enumerate(all_slides):
    slide_num = idx + 1
    title = s["title"]
    title_words = len(title.split())
    if title_words < 1 or title_words > 3:
        print(f"WARNING: Slide {slide_num} title '{title}' has {title_words} words (expected 1-3)!")
    
    speech = s.get("speech", "")
    words = speech.split()
    wc = len(words)
    if slide_num <= 16:
        if wc < 195 or wc > 215:
            print(f"ERROR: Slide {slide_num} speech word count is {wc} (expected 195-215)!")
    else:
        if wc != 0:
            print(f"ERROR: Slide {slide_num} speech word count is {wc} (expected 0)!")
    
    # Check forbidden personas
    for fp in forbidden_titles:
        if fp.lower() in speech.lower() or fp.lower() in json.dumps(s).lower():
            print(f"WARNING: Slide {slide_num} contains forbidden title: '{fp}'")
            
    for fn in forbidden_names:
        if fn.lower() in speech.lower() or fn.lower() in json.dumps(s).lower():
            print(f"WARNING: Slide {slide_num} contains forbidden name: '{fn}'")

print("Verification complete.")

# Write to class9_science_ch13_data.py
with open(".agents/class9_science_ch13_data.py", "w") as f:
    f.write("# NCERT Class 9 Science - Chapter 13: Earth as a System: Energy, Matter, and Life\n")
    f.write("from generate_c9s_ch13_part1 import slides_part1\n")
    f.write("from generate_c9s_ch13_part2 import slides_part2\n")
    f.write("from generate_c9s_ch13_part3 import slides_part3\n\n")
    f.write("slides_data = slides_part1 + slides_part2 + slides_part3\n")
