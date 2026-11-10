import sys
sys.path.insert(0, '.agents')
from generate_c3m_ch3_part1 import slides_part1
from generate_c3m_ch3_part2 import slides_part2
from generate_c3m_ch3_part3 import slides_part3

all_slides = slides_part1 + slides_part2 + slides_part3

print(f"Total slides assembled: {len(all_slides)}")
assert len(all_slides) == 20, f"Expected 20 slides, got {len(all_slides)}"

# Check IDs and titles
for i, s in enumerate(all_slides):
    assert s['id'] == i + 1, f"Slide index mismatch at {i}: {s['id']}"
    words = s['title'].strip().split()
    assert 1 <= len(words) <= 3, f"Title length violation on slide {s['id']}: '{s['title']}' ({len(words)} words)"
    if s['id'] <= 16:
        spoken_words = len(s['speech'].strip().split())
        assert 195 <= spoken_words <= 215, f"Spoken word count violation on slide {s['id']}: {spoken_words} words"
        assert len(s['checkpoints']) == 2, f"Slide {s['id']} must have 2 checkpoints"
    else:
        assert len(s['questions']) == 10, f"Slide {s['id']} must have 10 quiz questions"

print("All 20 slides passed validation!")

with open(".agents/class3_maths_ch3_data.py", "w") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 3 Mathematics Chapter 3: Double Century - Complete Slide Data."""\n\n')
    f.write("SLIDES = " + repr(all_slides) + "\n")

print("Successfully written to .agents/class3_maths_ch3_data.py")
