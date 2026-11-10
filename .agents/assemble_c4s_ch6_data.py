# assemble_c4s_ch6_data.py
import sys
import os
import json
import re

sys.path.append(os.path.abspath('.agents'))
from generate_c4s_ch6_part1 import slides_part1
from generate_c4s_ch6_part2 import slides_part2
from generate_c4s_ch6_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

forbidden_names = [
    r'\bRaghav\b', r'\bReena\b', r'\bAmit\b', r'\bChandan\b', r'\bNavya\b', 
    r'\bRadha\b', r'\bSuresh\b', r'\bRohan\b', r'\bAnjali\b', r'\bMohan\b',
    r'\bDr\.\b', r'\bDoctor\s+[A-Z]', r'\bSir\b', r'\bMadam\b', r'\bMr\.\b', r'\bMrs\.\b', r'\bMiss\b'
]

for idx, s in enumerate(all_slides, start=1):
    assert s['id'] == idx, f"Slide index mismatch: {s['id']} != {idx}"
    title_words = len(s['title'].split())
    assert 1 <= title_words <= 3, f"Slide {idx} title length invalid ({title_words} words): '{s['title']}'"
    
    # Check forbidden names across all text in the slide
    slide_text = json.dumps(s)
    for pat in forbidden_names:
        matches = re.findall(pat, slide_text)
        assert not matches, f"Slide {idx} contains forbidden persona or human name pattern '{pat}': {matches}"

    if idx <= 16:
        wc = len(s['speech'].split())
        assert 195 <= wc <= 215, f"Slide {idx} speech word count out of range: {wc} words"
        assert len(s.get('checkpoints', [])) == 2, f"Slide {idx} must have exactly 2 checkpoints"
        for cp in s['checkpoints']:
            assert cp['ans'] in cp['options'], f"Slide {idx} checkpoint answer missing from options"
            assert len(cp['options']) == 4, f"Slide {idx} checkpoint must have 4 options"
    else:
        assert s['speech'] == "", f"Challenge slide {idx} speech must be empty"
        assert len(s.get('questions', [])) == 10, f"Challenge slide {idx} must have exactly 10 questions"
        for q in s['questions']:
            assert q['ans'] in q['options'], f"Question {q['id']} answer missing from options"
            assert len(q['options']) == 4, f"Question {q['id']} must have 4 options"
            assert 'step1' in q['solution_steps'] and 'step2' in q['solution_steps'] and 'step3' in q['solution_steps'], f"Question {q['id']} missing 3-step solution"

print("All 20 slides passed validation checks!")

# Write to .agents/class4_science_ch6_data.py
output_path = os.path.join('.agents', 'class4_science_ch6_data.py')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# Class 4 Science Chapter 6 Data: Happy and Healthy Living\n")
    f.write("# Generated automatically - 20 slides\n\n")
    f.write("slides = " + json.dumps(all_slides, indent=4) + "\n")

print(f"Successfully wrote {output_path}")

