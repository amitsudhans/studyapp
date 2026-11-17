"""Assemble and validate all 20 slides for Class 10 Science Chapter 3: Metals and Non-metals
"""

import sys
import re

sys.path.insert(0, ".agents")

import generate_c10s_ch3_part1 as p1
import generate_c10s_ch3_part2 as p2
import generate_c10s_ch3_part3 as p3

all_slides = p1.slides + p2.slides + p3.slides

assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

forbidden = [r"\braghav\b", r"\bdr\b", r"\bsir\b", r"\bmadam\b", r"\bmr\b", r"\bmrs\b", r"\bprof\b"]

for idx, slide in enumerate(all_slides, 1):
    assert slide["id"] == idx, f"Slide index mismatch: {slide['id']} vs {idx}"
    title_words = len(slide["title"].split())
    assert title_words <= 3, f"Slide {idx} title '{slide['title']}' has {title_words} words (>3)"
    
    if idx <= 16:
        words = len(slide["speech"].split())
        assert 195 <= words <= 215, f"Slide {idx} speech word count {words} out of range [195, 215]"
        assert "checkpoints" in slide and len(slide["checkpoints"]) == 2, f"Slide {idx} missing 2 checkpoints"
    else:
        assert slide["speech"] == "", f"Slide {idx} speech must be empty, got {len(slide['speech'])}"
        assert "questions" in slide and len(slide["questions"]) == 10, f"Slide {idx} must have 10 quiz questions"

    # Check forbidden names/personas in text
    slide_text = str(slide)
    for pat in forbidden:
        match = re.search(pat, slide_text, re.IGNORECASE)
        assert not match, f"Forbidden persona or name pattern '{pat}' found in slide {idx}: {match.group()}"

print(f"Verified all 20 slides for Class 10 Science Chapter 3 successfully!")

# Write out class10_science_ch3_data.py
with open(".agents/class10_science_ch3_data.py", "w") as f:
    f.write("# Class 10 Science Chapter 3: Metals and Non-metals Data\n")
    f.write("slides = " + repr(all_slides) + "\n")

print("Successfully written .agents/class10_science_ch3_data.py")
