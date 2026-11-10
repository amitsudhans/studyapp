# -*- coding: utf-8 -*-
import re

with open('/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/.system_generated/steps/27268/output.txt') as f:
    diff = f.read()

hunks = re.split(r'\n@@ ', diff)

def extract_added(hunk_text):
    return '\n'.join([l[1:] for l in hunk_text.split('\n') if l.startswith('+') and not l.startswith('+++')])

hunk1 = extract_added(hunks[1]).strip()
hunk2 = extract_added(hunks[2])
hunk3 = extract_added(hunks[3])

# Clean Hunk 2 (Class 4 Maths chapters 12, 13, 14)
h2_lines = hunk2.split('\n')
h2_clean_lines = []
for l in h2_lines:
    if "'name' => 'Toy Joy'" in l:
        while h2_clean_lines and not h2_clean_lines[-1].strip().startswith('['):
            h2_clean_lines.pop()
        if h2_clean_lines:
            h2_clean_lines.pop()
        break
    h2_clean_lines.append(l)
h2_clean = '\n'.join(h2_clean_lines).strip()

# Clean Hunk 3 (Class 4 Science chapters 1 to 10)
h3_lines = hunk3.split('\n')
h3_clean_lines = []
in_sci4 = False
for l in h3_lines:
    if "'ncert-science-class4'" in l:
        in_sci4 = True
    if in_sci4:
        if "'name' => 'Toy Joy'" in l:
            while h3_clean_lines and not h3_clean_lines[-1].strip().startswith('['):
                h3_clean_lines.pop()
            if h3_clean_lines:
                h3_clean_lines.pop()
            break
        h3_clean_lines.append(l)

h3_clean = "            // NCERT Science Class 4\n            " + '\n'.join(h3_clean_lines).strip() + "\n            ],\n"

with open('/tmp/MultimediaController.php.clean', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert hunk1 (Class 3 Maths) right before // NCERT Mathematics Class 4
target1 = "            // NCERT Mathematics Class 4\n            'ncert-mathematics-class4' => ["
assert target1 in content, "Target 1 not found!"
replacement1 = hunk1 + "\n\n" + target1
content = content.replace(target1, replacement1, 1)

# 2. Insert h2_clean (Class 4 Maths ch 12, 13, 14) right after Chapter 11
target2 = """                        'Symmetry Project Art: Bilateral Leaf-Imprint Stamping, Radial Mandalas & Botanical Portfolios',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Mathematics Class 5"""
assert target2 in content, "Target 2 not found!"
replacement2 = """                        'Symmetry Project Art: Bilateral Leaf-Imprint Stamping, Radial Mandalas & Botanical Portfolios',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                """ + h2_clean + """
            ],

            // NCERT Mathematics Class 5"""
content = content.replace(target2, replacement2, 1)

# 3. Insert h3_clean (Class 4 Science) right before // NCERT Science Class 5
target3 = "            // NCERT Science Class 5\n            'ncert-science-class5' => ["
assert target3 in content, "Target 3 not found!"
replacement3 = h3_clean + "\n" + target3
content = content.replace(target3, replacement3, 1)

with open('app/Http/Controllers/MultimediaController.php', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully reconstructed MultimediaController.php!")

