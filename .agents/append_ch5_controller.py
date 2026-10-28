with open("app/Http/Controllers/MultimediaController.php", "r", encoding="utf-8") as f:
    text = f.read()

target = """                        'Heritage Algebra: Acharya Bhaskara II\\'s Lilavati & Bijaganita Poetic Riddles',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

ch5_code = """                        'Heritage Algebra: Acharya Bhaskara II\\'s Lilavati & Bijaganita Poetic Riddles',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                [
                    'chapter_num' => 5,
                    'name' => 'Parallel and Intersecting Lines',
                    'has_multimedia' => true,
                    'media_key' => 'class7-math-parallel-intersecting-lines',
                    'media_title' => 'NCERT Class 7 Mathematics • Chapter 5 • Parallel and Intersecting Lines Master Lab',
                    'media_url' => asset('animations/class7-math-parallel-intersecting-lines.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 7 Mathematics Chapter 5: Parallel and Intersecting Lines with animated mentor avatar Acharya Baudhayana (Master of Sulba Sutra Geometry & Cord-Constructions), Web Speech API narration, and 16 bespoke SVG laboratory simulators covering Intersecting Lines on a plane (scissoring lines, vertically opposite angles equality theorem), Linear Pairs and Supplementary Adjacent Angles (180° straight angle balance), Perpendicular Lines (the 90° right angle cross, inverted-T notation and corner square symbols), Parallel Lines (railway tracks and invariant equidistant property), Origami Paper Folding Perpendicular Creases (symmetric folding of straight angle), Paper Folding Parallel Creases (double-perpendicular principle and chevron arrow notations), Transversals (8 angles formed at double crossings, interior vs exterior classifications), Corresponding Angles (the iconic F-shape explorer and parallel equality rule), Testing for Parallel Lines (converse detector: when corresponding angles match, lines are parallel), Drawing Parallel Lines (ruler and set square sliding construction through external point P), Alternate Interior Angles (the iconic Z-shape explorer and deductive proof), Alternate Exterior Angles (outer zigzag balance and transitive equality), Co-Interior Angles (the C-shape explorer, consecutive interior angles summing to 180°), The Café Wall Illusion (staggered black-and-white tiles distorting straight mortar lines), The Hering and Zöllner Space-Warping Illusions (acute angle expansion and background stripping), Acharya Baudhayana\\'s Vedic Cord & Peg (Sanku-Rajju) sacred altar geometry, 32 interactive checkpoints, and 4 dedicated mastery quiz challenge slides (40 questions) with step-by-step pop-up solution derivations.',
                    'topics' => [
                        'Across the Line: Coplanar Lines, Point of Intersection & Scissors Geometry',
                        'Vertically Opposite Angles Equality Theorem: Deductive Proof',
                        'Linear Pairs of Angles: Adjacent Angles Summing to 180° on a Straight Line',
                        'Perpendicular Lines: The Universal 90° Right Angle Cross ($AB \\\\perp CD$)',
                        'Between Lines: Parallel Lines, Non-Intersection & Invariant Equidistance',
                        'Paper Folding I: Constructing 90° Perpendicular Creases by Symmetry',
                        'Paper Folding II: Double-Perpendicular Principle & Chevron Arrow Notations (\\\\rangle, \\\\gg)',
                        'Transversals: Double Intersection Systems, Interior & Exterior Angle Regions',
                        'Corresponding Angles: The Iconic \\'F-Shape\\' Pattern & Parallel Postulate',
                        'Testing for Parallel Lines: The Converse Corresponding Angle Detector',
                        'Practical Drafting: Drawing Parallel Lines with Ruler and Sliding Set Square',
                        'Alternate Interior Angles: The Famous \\'Z-Shape\\' Pattern & Deductive Proof',
                        'Alternate Exterior Angles: Outer Zigzag Balance & Transitive Proof',
                        'Interior Angles on the Same Side of Transversal: The \\'C-Shape\\' 180° Rule',
                        'Optical Illusions I: The Bristol Café Wall Illusion & Luminance Shearing',
                        'Optical Illusions II: The Hering and Zöllner Acute-Angle Warp Illusions',
                        'Heritage Geometry: Acharya Baudhayana\\'s Vedic Cord & Peg (Sanku-Rajju) Altars',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

assert target in text, "target not found in MultimediaController.php"
text = text.replace(target, ch5_code, 1)

with open("app/Http/Controllers/MultimediaController.php", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully appended Chapter 5 to MultimediaController.php")
