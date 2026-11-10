# -*- coding: utf-8 -*-

with open('/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/.system_generated/steps/25526/output.txt') as f:
    diff_text = f.read()

lines = diff_text.split('\n')

# Maths ch 12, 13, 14 block (lines 11 to 98)
maths_block_lines = [l[1:] if l.startswith('+') else l for l in lines[11:98]]
maths_block = '\n'.join(maths_block_lines)

# Science ch 1, 2, 3 block (lines 167 to 254)
science_block_lines = [l[1:] if l.startswith('+') else l for l in lines[167:254]]
science_block = "            // NCERT Science Class 4\n            'ncert-science-class4' => [\n" + '\n'.join(science_block_lines) + "\n            ],\n\n"

with open('app/Http/Controllers/MultimediaController.php', 'r', encoding='utf-8') as f:
    controller_content = f.read()

# 1. Target for Maths ch 11 end
maths_target = """                        'Symmetry Project Art: Bilateral Leaf-Imprint Stamping, Radial Mandalas & Botanical Portfolios',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Mathematics Class 5"""

assert maths_target in controller_content, "Maths target not found in MultimediaController.php!"

maths_replacement = """                        'Symmetry Project Art: Bilateral Leaf-Imprint Stamping, Radial Mandalas & Botanical Portfolios',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
""" + maths_block + """
            ],

            // NCERT Mathematics Class 5"""

controller_content = controller_content.replace(maths_target, maths_replacement, 1)

# 2. Target for Science Class 5 start
science_target = "            // NCERT Science Class 5\n            'ncert-science-class5' => ["
assert science_target in controller_content, "Science target not found in MultimediaController.php!"

science_replacement = science_block + science_target
controller_content = controller_content.replace(science_target, science_replacement, 1)

with open('app/Http/Controllers/MultimediaController.php', 'w', encoding='utf-8') as f:
    f.write(controller_content)

print("Successfully patched MultimediaController.php!")
