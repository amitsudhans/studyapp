# assemble_c4s_ch8_data.py
import json
import re
from generate_c4s_ch8_part1 import slides_part1
from generate_c4s_ch8_part2 import slides_part2
from generate_c4s_ch8_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

FORBIDDEN_NAMES = ["Pihu", "Raghav", "Meera", "Dhruv", "Chandan", "Navya", "Amit", "Reena", "Dr.", "Sir", "Madam", "Mr.", "Mrs.", "Miss"]

for i, slide in enumerate(all_slides, 1):
    assert slide["id"] == i, f"Slide {i} has mismatched id {slide['id']}"
    # Verify title word count (1 to 3 words)
    title_words = slide["title"].strip().split()
    assert 1 <= len(title_words) <= 3, f"Slide {i} title '{slide['title']}' has {len(title_words)} words (must be 1-3)"
    
    # Check for forbidden names in all text fields
    slide_str = json.dumps(slide)
    for name in FORBIDDEN_NAMES:
        pattern = r'\b' + re.escape(name) + r'\b' if not name.endswith('.') else re.escape(name)
        assert not re.search(pattern, slide_str, re.IGNORECASE), f"Forbidden name/persona '{name}' detected in slide {i}"

    if i <= 16:
        # Teaching slides
        speech = slide.get("speech", "")
        speech_words = speech.strip().split()
        assert 195 <= len(speech_words) <= 215, f"Slide {i} speech has {len(speech_words)} words (expected 195-215)"
        assert len(slide.get("checkpoints", [])) == 2, f"Slide {i} must have exactly 2 checkpoints"
        for cp in slide["checkpoints"]:
            assert "q" in cp and "options" in cp and "ans" in cp and "explanation" in cp
            assert len(cp["options"]) == 4
            assert cp["ans"] in cp["options"]
    else:
        # Challenge slides
        assert len(slide.get("questions", [])) == 10, f"Slide {i} must have 10 quiz questions"
        for q in slide["questions"]:
            assert "id" in q and "q" in q and "options" in q and "ans" in q and "hint" in q and "explanation" in q and "solution_steps" in q
            assert len(q["options"]) == 4
            assert q["ans"] in q["options"]
            assert len(q["solution_steps"]) == 3

print("All 20 slides passed strict validation!")

# Write data to class4_science_ch8_data.py
with open(".agents/class4_science_ch8_data.py", "w", encoding="utf-8") as f:
    f.write("# Class 4 Science Chapter 8: How Things are Made - Full 20 Slides Data\n")
    f.write("slides = " + repr(all_slides) + "\n")

print("Saved class4_science_ch8_data.py successfully!")

