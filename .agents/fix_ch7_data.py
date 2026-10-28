import re

with open('.agents/class7_math_tale_of_three_intersecting_lines_data.py', 'r') as f:
    content = f.read()

# Replace JSON null, true, false with Python None, True, False
content = re.sub(r'\bnull\b', 'None', content)
content = re.sub(r'\btrue\b', 'True', content)
content = re.sub(r'\bfalse\b', 'False', content)

with open('.agents/class7_math_tale_of_three_intersecting_lines_data.py', 'w') as f:
    f.write(content)

print("Fixed null/true/false in class7_math_tale_of_three_intersecting_lines_data.py")
