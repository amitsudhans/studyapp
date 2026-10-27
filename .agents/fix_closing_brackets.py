with open('app/Http/Controllers/MultimediaController.php', 'r') as f:
    text = f.read()

# Notice that after Atoms and Molecules there is an extra '            ],\n\n'
bad_str = """                        '32 In-Slide Checkpoints with Professor Sophia Explanations',
                        '4 Dedicated Mastery Quiz Slides (40 Questions with Pop-up Solutions)',
                    ],
                ],
            ],

                [
                    'chapter_num' => 8,"""

good_str = """                        '32 In-Slide Checkpoints with Professor Sophia Explanations',
                        '4 Dedicated Mastery Quiz Slides (40 Questions with Pop-up Solutions)',
                    ],
                ],
                [
                    'chapter_num' => 8,"""

text = text.replace(bad_str, good_str)

with open('app/Http/Controllers/MultimediaController.php', 'w') as f:
    f.write(text)
print('Fixed bracket syntax!')
