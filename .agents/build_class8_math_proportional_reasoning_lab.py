import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from class8_math_proportional_reasoning_data import slides_data, quiz_questions

def generate_html():
    slides_json = json.dumps(slides_data, ensure_ascii=False)
    quiz_json = json.dumps(quiz_questions, ensure_ascii=False)

    template_path = os.path.join(os.path.dirname(__file__), "template_class8_math_proportional_reasoning.html")
    with open(template_path, "r", encoding="utf-8") as tf:
        template = tf.read()

    html = template.replace("__SLIDES_JSON__", slides_json).replace("__QUIZ_JSON__", quiz_json)
    return html

if __name__ == "__main__":
    html_output = generate_html()
    output_path = os.path.join(os.path.dirname(__file__), "..", "public", "animations", "class8-math-proportional-reasoning.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Generated {output_path} ({len(html_output)} bytes)")
