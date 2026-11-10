#!/usr/bin/env python3
import sys
sys.path.append(".agents")
from generate_c3m_ch14_part1 import slides_part1
from generate_c3m_ch14_part2 import slides_part2
from generate_c3m_ch14_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

# Strict verification of all slides
for i, slide in enumerate(all_slides, 1):
    assert slide["id"] == i, f"Slide ID mismatch on index {i}: {slide['id']}"
    title_words = len(slide["title"].strip().split())
    assert 1 <= title_words <= 3, f"Slide {i} title '{slide['title']}' has {title_words} words (must be 1-3)!"
    
    if i <= 16:
        spoken = slide.get("speech", "")
        words = len(spoken.strip().split())
        assert 195 <= words <= 215, f"Slide {i} spoken words {words} outside 195-215!"
        assert len(slide["checkpoints"]) == 2, f"Slide {i} checkpoints count {len(slide['checkpoints'])} != 2!"
        for cp_idx, cp in enumerate(slide["checkpoints"]):
            assert "question" in cp and "options" in cp and "answer" in cp and "explanation" in cp
            assert cp["answer"] in [0, 1, 2, 3], f"Slide {i} CP {cp_idx} correct option invalid: {cp['answer']}"
    else:
        assert "questions" in slide, f"Slide {i} missing questions!"
        assert len(slide["questions"]) == 10, f"Slide {i} questions count {len(slide['questions'])} != 10!"
        for q_idx, q in enumerate(slide["questions"]):
            assert "question" in q and "options" in q and "answer" in q and "hint" in q and "explanation" in q and "solution_steps" in q
            assert len(q["options"]) == 4, f"Slide {i} Q {q_idx} options count != 4"
            assert q["answer"] in [0, 1, 2, 3], f"Slide {i} Q {q_idx} correct option invalid: {q['answer']}"
            assert len(q["solution_steps"]) == 3, f"Slide {i} Q {q_idx} solution steps != 3"

print("All 20 slides verified successfully! Writing .agents/class3_maths_ch14_data.py...")

with open(".agents/class3_maths_ch14_data.py", "w", encoding="utf-8") as f:
    f.write('"""NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair full slides dataset"""\n\n')
    f.write("slides = " + repr(all_slides) + "\n")

print("Saved .agents/class3_maths_ch14_data.py")
