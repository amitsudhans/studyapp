import re
import sys

with open('.agents/build_ch5_motion_data.py', 'r') as f:
    text_slides = f.read()

with open('.agents/build_ch5_quiz_data.py', 'r') as f:
    text_quiz = f.read()

# Extract slides list
match_slides = re.search(r'slides = \[(.*?)\]\n\n# Verify no latex', text_slides, re.DOTALL)
if not match_slides:
    print("Could not extract slides")
    sys.exit(1)
slides_code = match_slides.group(1)

# Extract quiz list
match_quiz = re.search(r'quiz_questions = \[(.*?)\]\n\n# Verify no latex', text_quiz, re.DOTALL)
if not match_quiz:
    print("Could not extract quiz")
    sys.exit(1)
quiz_code = match_quiz.group(1)

content = f'''"""
NCERT Class 6 Science - Chapter 5: Measurement of Length and Motion
Master Data File
"""

CHAPTER_META = {{
    "chapter_num": 5,
    "title": "Measurement of Length and Motion",
    "subject": "Science",
    "grade": "Class 6",
    "book": "Curiosity (NEP 2020)",
    "total_slides": 20,
    "concept_slides": 16,
    "quiz_slides": 4,
    "checkpoints_count": 32,
    "quiz_questions_count": 40
}}

SLIDES = [
{slides_code}
]

QUIZ_QUESTIONS = [
{quiz_code}
]
'''

with open('.agents/class6_science_ch5_data.py', 'w') as f:
    f.write(content)

print("Created .agents/class6_science_ch5_data.py successfully!")
