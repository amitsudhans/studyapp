import re

new_titles = {
    1: "Why Measure",
    2: "Shifting Spans",
    3: "Ancient Scales",
    4: "The Metre",
    5: "Metric Powers",
    6: "Tool Choice",
    7: "Eye Angle",
    8: "Broken Zeros",
    9: "Symbol Rules",
    10: "Curved Paths",
    11: "The Origin",
    12: "Rest & Motion",
    13: "Relative Move",
    14: "Straight Path",
    15: "Circle Spin",
    16: "To and Fro"
}

with open('.agents/class6_science_ch5_data.py', 'r') as f:
    content = f.read()

import sys
sys.path.append('.agents')
import class6_science_ch5_data as d

for s in d.SLIDES:
    old_title = s['title']
    new_title = new_titles[s['id']]
    s['title'] = new_title
    # also update spoken text start
    if s['spoken_text'].startswith(f"Slide {s['id']}: {old_title}."):
        s['spoken_text'] = s['spoken_text'].replace(f"Slide {s['id']}: {old_title}.", f"Slide {s['id']}: {new_title}.", 1)

# Write back
import reprlib
out_content = f'''"""
NCERT Class 6 Science - Chapter 5: Measurement of Length and Motion
Master Data File
"""

CHAPTER_META = {repr(d.CHAPTER_META)}

SLIDES = {repr(d.SLIDES)}

QUIZ_QUESTIONS = {repr(d.QUIZ_QUESTIONS)}
'''

with open('.agents/class6_science_ch5_data.py', 'w') as f:
    f.write(out_content)

print("Updated .agents/class6_science_ch5_data.py with short titles successfully!")
