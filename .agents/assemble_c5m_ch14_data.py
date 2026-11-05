import sys
sys.path.insert(0, '.agents')
import re
from generate_c5m_ch14_part1 import slides_part1
from generate_c5m_ch14_part2 import slides_part2
from generate_c5m_ch14_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3
print(f"Total slides: {len(all_slides)}")
assert len(all_slides) == 20, "Must have exactly 20 slides"

# Check human names
names = ['Raghav', 'Akira', 'Sunita', 'Mary', 'Aarav', 'Bhavna', 'Chetan', 'Diya', 'Priya', 'Rohan', 'Adrit', 'Preetha', 'Kabir', 'Meera']
for s in all_slides:
    text = s['title'] + ' ' + s.get('tagline', '') + ' ' + s.get('lecture', '')
    for cp in s.get('checkpoints', []):
        text += ' ' + cp['question'] + ' ' + ' '.join(cp['options']) + ' ' + cp['explanation']
    for q in s.get('questions', []):
        text += ' ' + q['question'] + ' ' + ' '.join(q['options']) + ' ' + q['explanation'] + ' ' + q.get('solution_html', '')
    
    for n in names:
        assert not re.search(rf'\b{n}\b', text, re.IGNORECASE), f"Found name {n} in slide {s['id']}"

# Check word count for slides 1 to 16
for s in all_slides[:16]:
    wc = len(s['lecture'].split())
    assert 195 <= wc <= 215, f"Slide {s['id']} lecture has {wc} words (must be 195-215)"
    assert len(s.get('checkpoints', [])) == 2, f"Slide {s['id']} must have 2 checkpoints"

# Check questions for slides 17 to 20
for s in all_slides[16:]:
    assert len(s.get('questions', [])) == 10, f"Slide {s['id']} must have 10 questions"
    for q in s['questions']:
        assert 'solution_html' in q, f"Slide {s['id']} question missing solution_html"

print("All slide rules verified! Writing class5_maths_ch14_data.py...")

with open('.agents/class5_maths_ch14_data.py', 'w') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 5 Maths Chapter 14: Maps and Locations Data File"""\n\n')
    f.write(f"slides = {repr(all_slides)}\n")

print("Successfully written .agents/class5_maths_ch14_data.py!")
