import sys
import os
import re

sys.path.append(os.path.abspath(".agents"))
from generate_ch9_part1 import SLIDES_PART1
from generate_ch9_part2 import SLIDES_PART2
from generate_ch9_part3 import QUIZ_QUESTIONS

CHAPTER_META = {
    "title": "Methods of Separation in Everyday Life",
    "class": "Class 6",
    "subject": "Science",
    "chapter": 9,
    "book": "Curiosity",
    "total_slides": 20,
    "concept_slides": 16,
    "quiz_slides": 4,
    "total_checkpoints": 32,
    "total_quiz_questions": 40
}

ALL_SLIDES = SLIDES_PART1 + SLIDES_PART2

# Clean raw LaTeX if any (replace with clean Unicode)
latex_pattern = re.compile(r'\\[a-zA-Z]+')

def clean_latex(text):
    if not isinstance(text, str):
        return text
    # Replace math terms
    text = text.replace(r'$a_w$', 'a_w')
    text = text.replace(r'$B \propto I$', 'B ∝ I')
    text = text.replace(r'$$', '')
    text = text.replace(r'$', '')
    matches = latex_pattern.findall(text)
    if matches:
        print(f"Warning: found raw LaTeX {matches} in: {text[:50]}")
    return text

for s in ALL_SLIDES:
    s['title'] = clean_latex(s['title'])
    s['subtitle'] = clean_latex(s['subtitle'])
    s['concept_html'] = clean_latex(s['concept_html'])
    s['lecture_script'] = clean_latex(s['lecture_script'])
    s['spoken_text'] = clean_latex(s['spoken_text'])
    for cp in s['checkpoints']:
        cp['question'] = clean_latex(cp['question'])
        cp['options'] = [clean_latex(opt) for opt in cp['options']]
        cp['explanation'] = clean_latex(cp['explanation'])
        cp['study_insight'] = clean_latex(cp['study_insight'])

for q in QUIZ_QUESTIONS:
    q['question'] = clean_latex(q['question'])
    q['options'] = [clean_latex(opt) for opt in q['options']]
    q['explanation'] = clean_latex(q['explanation'])
    q['solution_html'] = clean_latex(q['solution_html'])

with open('.agents/class6_science_ch9_data.py', 'w', encoding='utf-8') as f:
    f.write('"""\nNCERT Class 6 Science - Chapter 9: Methods of Separation in Everyday Life\nData Module with 16 Concept Slides & 40 Quiz Questions\nZero raw LaTeX. All clean Unicode.\n"""\n\n')
    f.write('CHAPTER_META = ' + repr(CHAPTER_META) + '\n\n')
    f.write('SLIDES = ' + repr(ALL_SLIDES) + '\n\n')
    f.write('QUIZ_QUESTIONS = ' + repr(QUIZ_QUESTIONS) + '\n')

print(f"Successfully assembled .agents/class6_science_ch9_data.py! Slides: {len(ALL_SLIDES)}, Quizzes: {len(QUIZ_QUESTIONS)}")

