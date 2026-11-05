#!/usr/bin/env python3
"""
Assemble all 20 slides data for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""
import re
from generate_c5m_ch3_part1 import slides_1_to_8
from generate_c5m_ch3_part2 import slides_9_to_16
from generate_c5m_ch3_part3 import slides_17_to_20

all_slides = slides_1_to_8 + slides_9_to_16 + slides_17_to_20

# Zero raw LaTeX and heading checks
for s in all_slides:
    words = s["heading"].split()
    assert 1 <= len(words) <= 3, f"Heading '{s['heading']}' on Slide {s['id']} has {len(words)} words, must be 1 to 3 words!"
    
    # Check text for raw LaTeX
    text_corpus = s["heading"] + " " + s["tagline"] + " " + s["audio_text"]
    for tb in s.get("theory_blocks", []):
        text_corpus += " " + tb["title"] + " " + tb["content"]
    for cp in s.get("checkpoints", []):
        text_corpus += " " + cp["question"] + " " + " ".join(cp["options"]) + " " + cp["feedback"]
    for q in s.get("quizzes", []):
        text_corpus += " " + q["question"] + " " + " ".join(q["options"]) + " " + q["solution_html"]
        
    latex_matches = re.findall(r"\\(?:frac|times|div|pm|text|cdot|\$)|(?<!\\)\$[^$]+\$", text_corpus)
    if latex_matches:
        raise ValueError(f"Raw LaTeX detected on Slide {s['id']}: {latex_matches}")

print(f"VERIFIED: All {len(all_slides)} slides passed short heading and zero raw LaTeX checks!")

# Write to class5_maths_ch3_data.py
with open(".agents/class5_maths_ch3_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 5 Mathematics - Chapter 3: Angles as Turns Data\n"""\n\n')
    f.write(f"slides_data = {repr(all_slides)}\n")

print("Successfully written .agents/class5_maths_ch3_data.py")

