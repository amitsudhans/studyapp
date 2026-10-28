import re

with open('app/Http/Controllers/MultimediaController.php', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

replacement = """                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                [
                    'chapter_num' => 7,
                    'name' => 'A Tale of Three Intersecting Lines',
                    'has_multimedia' => true,
                    'media_key' => 'class7-math-tale-of-three-intersecting-lines',
                    'media_title' => 'NCERT Class 7 Mathematics • Chapter 7 • A Tale of Three Intersecting Lines Master Lab',
                    'media_url' => asset('animations/class7-math-tale-of-three-intersecting-lines.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 7 Mathematics Chapter 7: A Tale of Three Intersecting Lines with animated mentor avatar Acharya Baudhāyana (Pioneer of Indian Geometry & the Śulba Sūtras), Web Speech API narration, and 16 bespoke SVG laboratory simulators covering Triangle Anatomy (vertices, sides, interior angles, and three non-concurrent lines enclosing a 2D plane), Equilateral Triangles (total 3-fold rotational and reflectional symmetry, 60° equiangular property, compass and intersecting arc construction superiority over ruler trial-and-error), The Triangle Inequality Theorem (existence condition: sum of any two sides strictly greater than third side, flat-line collapse a+b=c, and impossible gap a+b<c), Circle Intersections (geometric locus of distance, non-intersecting, tangent, and two mirror-congruent intersection points), SSS Construction (step-by-step ruler-compass protocol for scalene and isosceles triangles), SAS Triangle Construction (the power of the included angle locking the opening between two sides), ASA Triangle Construction (base ray convergence law: B+C < 180°, parallel rays B+C=180°, and divergent rays B+C>180°), The Angle Sum Property (formal deductive proof using auxiliary line parallel to base and alternate interior angles, plus paper tear-off corner assembly into a 180° straight angle), The Exterior Angle Theorem (exterior angle equals sum of two interior opposite angles, deductive proof via linear pair), Altitudes of a Triangle (perpendicular height dropped to opposite base, foot of perpendicular, 90° symbol, and area connection), Drafting Altitudes with Ruler and Set Square (sliding set square along ruler track to drop true perpendiculars), Altitudes in Special Triangles (all 3 altitudes inside for acute, legs doubling as altitudes for right triangles, and altitudes falling outside onto extended base lines for obtuse triangles), The Orthocenter H (point of concurrency of three altitudes, tracked moving from inside to right vertex to outside), Classification by Sides (equilateral with 3 symmetry axes, isosceles with 1 symmetry axis, and scalene with 0 symmetry axes), Classification by Angles (acute-angled, right-angled with hypotenuse and Baudhāyana\\\'s theorem, and obtuse-angled), The Master 3x3 Classification Matrix & Ancient Vedic Śulba Sūtras (cord knotting geometry: 3:4:5, 5:12:13, and 8:15:17 right triangles for sacrificial altars), 32 interactive checkpoints, and 4 dedicated mastery quiz challenge slides (40 questions) with step-by-step pop-up solution derivations.',
                    'topics' => [
                        'A Tale of Three Intersecting Lines: Triangle Anatomy, Vertices, Sides & Interior Angles',
                        'Equilateral Triangles: 3-Fold Symmetry, 60° Equiangular Property & Compass Arcs',
                        'The Triangle Inequality Theorem: Why $a + b > c, b + c > a, c + a > b$',
                        'Circle Intersections: Locus Geometry of Distance & Two Mirror Intersection Points',
                        'Constructing SSS Triangles: Precision Ruler-and-Compass Drafting Protocol',
                        'SAS Triangle Construction: The Locking Power of the Included Angle',
                        'ASA Triangle Construction: Ray Convergence Law & Why $\\\\angle B + \\\\angle C < 180^\\\\circ$',
                        'The Angle Sum Property: Deductive Parallel-Line Proof & Corner Tear-Off Assembly',
                        'The Exterior Angle Theorem: Exterior Angle Equals Sum of Interior Opposite Angles',
                        'Altitudes of a Triangle: Perpendicular Heights, Foot of Perpendicular & Area Connection',
                        'Precision Drafting: Drawing Altitudes Using a Sliding Set Square along a Ruler',
                        'Altitudes in Special Triangles: Inside (Acute), On Legs (Right), and Outside (Obtuse)',
                        'The Orthocenter ($H$): Point of Concurrency of Three Altitudes & Spatial Trajectory',
                        'Classification by Sides: Equilateral (3 Symmetries), Isosceles (1 Symmetry), Scalene (0)',
                        'Classification by Angles: Acute ($< 90^\\\\circ$), Right ($90^\\\\circ$, Hypotenuse), Obtuse ($> 90^\\\\circ$)',
                        'The Master 3x3 Classification Matrix: Valid Triangles vs Geometrical Impossibilities',
                        'Heritage Geometry: Acharya Baudhāyana\\\'s Śulba Sūtras & Knotted Cord Right Triangles',
                        'Interactive Checkpoints with Immediate Sound & Visual Feedback (32 Checks)',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 8"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open('app/Http/Controllers/MultimediaController.php', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully appended Chapter 7 to MultimediaController.php")
else:
    print("ERROR: Target block not found in MultimediaController.php")
    exit(1)
