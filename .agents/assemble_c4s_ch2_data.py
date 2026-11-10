# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Data Assembler: Combines parts 1, 2, and 3 into class4_science_ch2_data.py.
Validates all constraints strictly.
"""

import re
import sys
import pprint

from generate_c4s_ch2_part1 import slides_part1
from generate_c4s_ch2_part2 import slides_part2
from generate_c4s_ch2_part3 import slides_part3

# Harmonize dictionary keys
processed_slides = []

for s in slides_part1 + slides_part2:
    cps = []
    for cp in s.get("checkpoints", []):
        cps.append({
            "q": cp.get("q", cp.get("question")),
            "options": cp["options"],
            "ans": cp.get("ans", cp.get("correct")),
            "exp": cp.get("exp", cp.get("explanation"))
        })
    processed_slides.append({
        "id": s.get("id", s.get("slide_num")),
        "title": s["title"],
        "section": s.get("section", "Neighbourhood Science & Living"),
        "speech": s["speech"],
        "bullets": s.get("bullets", []),
        "checkpoints": cps
    })

for s in slides_part3:
    qs = []
    for q in s.get("quizzes", []):
        qs.append({
            "q": q.get("q", q.get("question")),
            "options": q["options"],
            "ans": q.get("ans", q.get("correct")),
            "hint": q.get("hint", "Consider the concepts discussed in this chapter."),
            "exp": q.get("exp", q.get("explanation")),
            "sol": q.get("sol", "")
        })
    processed_slides.append({
        "id": s.get("id", s.get("slide_num")),
        "title": s["title"],
        "section": s.get("section", "Comprehensive Review & Challenge"),
        "speech": "",
        "quizzes": qs
    })

print(f"Total slides assembled: {len(processed_slides)}")
assert len(processed_slides) == 20, f"Expected 20 slides, got {len(processed_slides)}"

BANNED_NAMES = [
    r'\bnavya\b', r'\bdada\s*ji\b', r'\bdada\b', r'\bdadaji\b', r'\braghav\b', r'\braju\b',
    r'\bchandan\b', r'\brani\b', r'\broja\b', r'\bdiya\b', r'\banvi\b',
    r'\bgulabo\b', r'\bshrinathan\b', r'\bmirabai\b', r'\bgundappa\b', r'\bmuniamma\b',
    r'\bjaspreet\b', r'\bgulnaz\b', r'\blou\b', r'\bdaisy\b', r'\bsapan\b', r'\budaya\b',
    r'\bsumitha\b', r'\bikra\b', r'\bsamina\b', r'\bshirley\b', r'\bshiv\b', r'\bsumedha\b',
    r'\bparv\b', r'\bchinnu\b', r'\brohan\b', r'\banjali\b', r'\bamit\b', r'\bpriya\b'
]

BANNED_PERSONAS = [
    r'\bdr\b', r'\bdr\.\b', r'\bsir\b', r'\bmadam\b', r'\bmr\b', r'\bmr\.\b',
    r'\bmrs\b', r'\bmrs\.\b', r'\bmiss\b'
]

for s in processed_slides:
    s_id = s["id"]
    title = s["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {s_id} title '{title}' must be 1 to 3 words, got {title_words}"
    
    if s_id <= 16:
        speech = s["speech"]
        wc = len(speech.split())
        assert 195 <= wc <= 215, f"Slide {s_id} speech has {wc} words (must be 195 to 215)!"
        assert len(s.get("checkpoints", [])) == 2, f"Slide {s_id} must have 2 checkpoints"
    else:
        assert len(s.get("quizzes", [])) == 10, f"Slide {s_id} must have 10 quiz questions"
    
    # Check for banned names and personas
    blob = f"{title} {s.get('section', '')} {s.get('speech', '')}"
    for cp in s.get("checkpoints", []):
        blob += f" {cp['q']} {' '.join(cp['options'])} {cp['exp']}"
    for q in s.get("quizzes", []):
        blob += f" {q['q']} {' '.join(q['options'])} {q.get('hint', '')} {q['exp']} {q.get('sol', '')}"
    
    blob_lower = blob.lower()
    for name_pat in BANNED_NAMES:
        m = re.search(name_pat, blob_lower)
        assert not m, f"Slide {s_id} contains banned name '{m.group(0)}' in content: {name_pat}"
    
    for persona_pat in BANNED_PERSONAS:
        m = re.search(persona_pat, blob_lower)
        assert not m, f"Slide {s_id} contains banned persona '{m.group(0)}' in content: {persona_pat}"

print("All slide metadata, word counts, banned names, and personas passed verification!")

output_code = f"""# -*- coding: utf-8 -*-
\"\"\"
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Master Data File
Generated automatically by assemble_c4s_ch2_data.py
\"\"\"

slides = {pprint.pformat(processed_slides, width=120, sort_dicts=False)}
"""

with open(".agents/class4_science_ch2_data.py", "w", encoding="utf-8") as f:
    f.write(output_code)

print("Master data saved to .agents/class4_science_ch2_data.py successfully!")

