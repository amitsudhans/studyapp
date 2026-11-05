# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 7: Shapes and Patterns - Part 3 (Slides 17 to 20: 40 Mastery Quiz Questions)
NEP 2020 / Joyful Mathematics
"""

MASTERY_CHALLENGES = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tag": "Mastery Challenge 1 • Weaving Patterns & Plane Tessellations",
        "questions": [
            {
                "id": 1,
                "question": "What happens if both Row 1 and Row 2 of a woven paper mat follow the exact same '1 over, 1 under' sequence without inverting?",
                "options": [
                    "The strips do not interlace and easily slide out without tension",
                    "The mat becomes twice as strong",
                    "It automatically creates a diamond pattern",
                    "The paper cuts itself"
                ],
                "correct": 0,
                "solution_html": "<p>Inverting the sequence on alternating rows is essential for <strong>interlacing tension</strong>. Without alternating, the weft strips sit on the same side and slide out freely.</p>"
            },
            {
                "id": 2,
                "question": "What must the sum of angles meeting at any vertex equal for tiles to tessellate without gaps or overlaps?",
                "options": ["Exactly 360°", "180°", "540°", "90°"],
                "correct": 0,
                "solution_html": "<p>A full revolution around any point in a flat 2D plane is <strong>360°</strong>. For tiles to fit without gaps or overlap, the corner angles meeting at the vertex must sum to exactly 360°.</p>"
            },
            {
                "id": 3,
                "question": "How many squares meet at each vertex in a standard square tessellation?",
                "options": ["4 squares (4 × 90° = 360°)", "3 squares", "5 squares", "6 squares"],
                "correct": 0,
                "solution_html": "<p>Each square corner is 90°. Since 360° ÷ 90° = 4, exactly <strong>4 squares</strong> meet at each vertex.</p>"
            },
            {
                "id": 4,
                "question": "Why can regular hexagons tessellate the plane by themselves?",
                "options": [
                    "Each corner is 120°, and 3 × 120° = 360°",
                    "Because they have 6 equal sides",
                    "Because 6 × 60° = 360°",
                    "Because they fit inside circles"
                ],
                "correct": 0,
                "solution_html": "<p>A regular hexagon has interior angles of 120°. Exactly 3 hexagons meet at each vertex: 3 × 120° = <strong>360°</strong>.</p>"
            },
            {
                "id": 5,
                "question": "Why do regular pentagons fail to tessellate a flat floor?",
                "options": [
                    "Each corner is 108°, and 108° does not evenly divide 360°",
                    "Because pentagons have an odd number of sides",
                    "Because 5 × 108° = 540°",
                    "Because pentagons are 3D solids"
                ],
                "correct": 0,
                "solution_html": "<p>In a regular pentagon, each angle is 108°. 3 pentagons take 324° (leaving a 36° gap), while 4 pentagons take 432° (overlapping). Thus, 108° cannot divide 360° evenly.</p>"
            },
            {
                "id": 6,
                "question": "In a semi-regular tessellation of octagons and squares, how many octagons and squares meet at each vertex?",
                "options": [
                    "2 octagons and 1 square (135° + 135° + 90° = 360°)",
                    "1 octagon and 2 squares",
                    "3 octagons and 1 square",
                    "2 octagons and 2 squares"
                ],
                "correct": 0,
                "solution_html": "<p>Each octagon angle is 135°, and each square angle is 90°. 135° + 135° + 90° = <strong>360°</strong>.</p>"
            },
            {
                "id": 7,
                "question": "How many regular polygons are capable of monohedral (single-shape) regular tessellation?",
                "options": [
                    "Only 3 (Equilateral Triangle, Square, Regular Hexagon)",
                    "Only 2 (Square and Rectangle)",
                    "5 regular polygons",
                    "All regular polygons"
                ],
                "correct": 0,
                "explanation": "Only equilateral triangles (60°), squares (90°), and regular hexagons (120°) have interior angles that divide 360° evenly.",
                "solution_html": "<p>Only <strong>3 regular polygons</strong> can tile the plane by themselves: the equilateral triangle, the square, and the regular hexagon.</p>"
            },
            {
                "id": 8,
                "question": "What is the angle measure of each interior corner of an equilateral triangle?",
                "options": ["60°", "90°", "45°", "120°"],
                "correct": 0,
                "solution_html": "<p>An equilateral triangle has 3 equal angles summing to 180°: 180° ÷ 3 = <strong>60°</strong>.</p>"
            },
            {
                "id": 9,
                "question": "What type of weave pattern is created by '2 over, 1 under' with a one-unit shift each row?",
                "options": ["Twill weave (diagonal staircases)", "Plain weave", "Square weave", "Hexagonal weave"],
                "correct": 0,
                "solution_html": "<p>The '2 over, 1 under' pattern with row shifts produces a diagonal ridge texture known as a <strong>twill weave</strong> (like denim fabric).</p>"
            },
            {
                "id": 10,
                "question": "How many equilateral triangles meet at a vertex to tile the plane?",
                "options": ["6 triangles (6 × 60° = 360°)", "4 triangles", "8 triangles", "3 triangles"],
                "correct": 0,
                "solution_html": "<p>Each angle of an equilateral triangle is 60°. 360° ÷ 60° = <strong>6 triangles</strong>.</p>"
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tag": "Mastery Challenge 2 • Triangle Classification & Kite Geometry",
        "questions": [
            {
                "id": 11,
                "question": "A triangle has side lengths of 8 cm, 8 cm, and 5 cm. What type of triangle is it?",
                "options": ["Isosceles triangle", "Equilateral triangle", "Scalene triangle", "Right triangle"],
                "correct": 0,
                "solution_html": "<p>A triangle with at least two equal sides (8 cm and 8 cm) is an <strong>isosceles triangle</strong>.</p>"
            },
            {
                "id": 12,
                "question": "If an isosceles triangle has a vertex angle of 40°, what is the measure of each of its two equal base angles?",
                "options": ["70° each", "60° each", "80° each", "50° each"],
                "correct": 0,
                "solution_html": "<p>Sum of angles = 180°. Remaining for the 2 base angles = 180° - 40° = 140°. Each base angle = 140° ÷ 2 = <strong>70°</strong>.</p>"
            },
            {
                "id": 13,
                "question": "A triangle has angle measures of 35°, 65°, and 80°. How is it classified by its sides?",
                "options": ["Scalene triangle", "Isosceles triangle", "Equilateral triangle", "Right-angled triangle"],
                "correct": 0,
                "solution_html": "<p>Since all three angles are different (35°, 65°, 80°), all three side lengths must be different: a <strong>scalene triangle</strong>.</p>"
            },
            {
                "id": 14,
                "question": "Cutting a rhombus along both of its diagonals yields which four shapes?",
                "options": [
                    "Four identical right-angled triangles",
                    "Four equilateral triangles",
                    "Four squares",
                    "Two triangles and two rectangles"
                ],
                "correct": 0,
                "solution_html": "<p>The diagonals of a rhombus are perpendicular bisectors, cutting it into <strong>4 congruent right-angled triangles</strong>.</p>"
            },
            {
                "id": 15,
                "question": "Which of the following defines a kite quadrilateral?",
                "options": [
                    "Two pairs of adjacent equal sides",
                    "Two pairs of opposite equal sides",
                    "All four sides equal",
                    "Two pairs of parallel sides"
                ],
                "correct": 0,
                "solution_html": "<p>A <strong>kite</strong> is defined by having two pairs of adjacent (neighboring) sides of equal length.</p>"
            },
            {
                "id": 16,
                "question": "What is the angle of intersection between the two diagonals of a kite?",
                "options": ["90° (Perpendicular)", "45°", "60°", "120°"],
                "correct": 0,
                "solution_html": "<p>In every kite, the two diagonals intersect at <strong>90° right angles</strong>.</p>"
            },
            {
                "id": 17,
                "question": "How many lines of reflective symmetry does a non-rhombus kite possess?",
                "options": ["Exactly 1 line (down its main diagonal)", "2 lines", "4 lines", "0 lines"],
                "correct": 0,
                "solution_html": "<p>A standard kite has <strong>exactly 1 line of symmetry</strong> passing through the vertices between the equal adjacent sides.</p>"
            },
            {
                "id": 18,
                "question": "If a triangle has sides of 6 cm, 6 cm, and 6 cm, what are its three angle measures?",
                "options": ["60°, 60°, 60°", "90°, 45°, 45°", "50°, 60°, 70°", "30°, 60°, 90°"],
                "correct": 0,
                "solution_html": "<p>An equilateral triangle with 3 equal sides always has 3 equal angles of <strong>60° each</strong>.</p>"
            },
            {
                "id": 19,
                "question": "In a kite ABCD where AB = AD = 5 cm and CB = CD = 9 cm, which pair of angles are equal?",
                "options": ["Angle B and Angle D", "Angle A and Angle C", "All four angles", "None of the angles"],
                "correct": 0,
                "solution_html": "<p>In a kite, the angles between the unequal sides (∠ B and ∠ D) are <strong>equal</strong>.</p>"
            },
            {
                "id": 20,
                "question": "What is the sum of the four interior angles of any quadrilateral (including a kite or rhombus)?",
                "options": ["360°", "180°", "540°", "720°"],
                "correct": 0,
                "solution_html": "<p>Any quadrilateral can be split into 2 triangles: 2 × 180° = <strong>360°</strong>.</p>"
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tag": "Mastery Challenge 3 • Quadrilateral Taxonomy, Tangrams & Deductions",
        "questions": [
            {
                "id": 21,
                "question": "Which property is shared by BOTH a rectangle and a parallelogram?",
                "options": [
                    "Opposite sides are parallel and equal in length",
                    "All four angles must be 90°",
                    "Diagonals must be equal in length",
                    "All four sides must be equal"
                ],
                "correct": 0,
                "solution_html": "<p>Both shapes have <strong>opposite sides that are parallel and equal in length</strong>. Right angles and equal diagonals belong specifically to rectangles.</p>"
            },
            {
                "id": 22,
                "question": "A quadrilateral has 4 equal sides and diagonals that cross at 90°, but its angles are NOT 90°. What shape is it?",
                "options": ["Rhombus", "Square", "Rectangle", "Trapezoid"],
                "correct": 0,
                "solution_html": "<p>A shape with 4 equal sides and non-right angles is a <strong>rhombus</strong>.</p>"
            },
            {
                "id": 23,
                "question": "Which shape is simultaneously a rectangle, a rhombus, and a parallelogram?",
                "options": ["A square", "A kite", "A trapezium", "An equilateral triangle"],
                "correct": 0,
                "solution_html": "<p>A <strong>square</strong> has 4 right angles (rectangle), 4 equal sides (rhombus), and parallel opposite sides (parallelogram).</p>"
            },
            {
                "id": 24,
                "question": "How many pieces are in a standard tangram puzzle, and how many of them are triangles?",
                "options": [
                    "7 pieces total, with 5 triangles",
                    "6 pieces total, with 4 triangles",
                    "8 pieces total, with 6 triangles",
                    "7 pieces total, with 3 triangles"
                ],
                "correct": 0,
                "solution_html": "<p>A standard tangram has <strong>7 pieces</strong>: 2 large triangles, 1 medium triangle, 2 small triangles, 1 square, and 1 parallelogram (5 triangles in all).</p>"
            },
            {
                "id": 25,
                "question": "What type of triangles are the 5 triangles in a tangram puzzle set?",
                "options": [
                    "45°-45°-90° isosceles right-angled triangles",
                    "Equilateral triangles (60°-60°-60°)",
                    "Scalene right-angled triangles",
                    "Obtuse triangles"
                ],
                "correct": 0,
                "solution_html": "<p>All 5 tangram triangles are <strong>45°-45°-90° isosceles right triangles</strong>.</p>"
            },
            {
                "id": 26,
                "question": "Which shape can be formed by joining the two small tangram triangles along their matching legs?",
                "options": [
                    "The medium triangle or the parallelogram",
                    "The large square",
                    "A circle",
                    "A pentagon"
                ],
                "correct": 0,
                "solution_html": "<p>Joining the two small triangles along their legs can form either the <strong>medium triangle</strong> or the <strong>parallelogram</strong> (or the small square if joined along hypotenuses).</p>"
            },
            {
                "id": 27,
                "question": "Riddle: 'I have four sides. My opposite sides are equal, all four of my angles are 90°, and my diagonals are equal in length.' Which shape am I?",
                "options": ["Rectangle", "Rhombus", "Kite", "Parallelogram"],
                "correct": 0,
                "solution_html": "<p>Opposite sides equal, four 90° angles, and equal diagonals uniquely identify a <strong>rectangle</strong>.</p>"
            },
            {
                "id": 28,
                "question": "Riddle: 'I have four sides. Two adjacent pairs of sides are equal, my diagonals meet at 90°, and I have only 1 line of symmetry.' Which shape am I?",
                "options": ["Kite", "Square", "Rectangle", "Rhombus"],
                "correct": 0,
                "solution_html": "<p>Two adjacent equal pairs, perpendicular diagonals, and 1 symmetry line uniquely identify a <strong>kite</strong>.</p>"
            },
            {
                "id": 29,
                "question": "When folding a square paper diagonally corner-to-corner to start an origami kite, what does the crease represent?",
                "options": [
                    "The central line of symmetry of the kite",
                    "The perimeter of the square",
                    "A curved arc",
                    "The shortest side"
                ],
                "correct": 0,
                "solution_html": "<p>The diagonal crease forms the <strong>line of reflective symmetry</strong> for the folded kite wings.</p>"
            },
            {
                "id": 30,
                "question": "If you rearrange all 7 tangram pieces into the shape of a running person, how does the total area compare to the original square?",
                "options": [
                    "The area is exactly the same",
                    "The area increases",
                    "The area decreases by half",
                    "It depends on how pieces are arranged"
                ],
                "correct": 0,
                "solution_html": "<p>By the <strong>Conservation of Area</strong> principle, rearranging pieces without overlap preserves the exact total area.</p>"
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tag": "Mastery Challenge 4 • Circle Constructions, 3D Solids & Platonic Geometry",
        "questions": [
            {
                "id": 31,
                "question": "If two diameters of a circle are drawn perpendicular (at 90°) to each other, connecting their 4 endpoints creates which shape?",
                "options": ["A square", "A general rectangle", "A trapezoid", "A rhombus with non-right angles"],
                "correct": 0,
                "solution_html": "<p>Because the diameters are equal, bisect each other, and cross at 90°, connecting their endpoints produces a <strong>square</strong>.</p>"
            },
            {
                "id": 32,
                "question": "On a circle with 24 evenly spaced points, what is the angle between point 1 and point 7?",
                "options": [
                    "90° (6 steps × 15°)",
                    "105°",
                    "60°",
                    "75°"
                ],
                "correct": 0,
                "solution_html": "<p>Each step is 360° ÷ 24 = 15°. From point 1 to 7 is 6 steps: 6 × 15° = <strong>90°</strong> (a right angle!).</p>"
            },
            {
                "id": 33,
                "question": "How many valid unfolded hexomino nets can fold into a closed 3-D cube?",
                "options": ["11 nets", "6 nets", "12 nets", "8 nets"],
                "correct": 0,
                "solution_html": "<p>There are mathematically exactly <strong>11 valid nets</strong> that can fold into a closed cube.</p>"
            },
            {
                "id": 34,
                "question": "In a 3×3×3 painted cube cut into 27 small 1cm cubes, how many cubes have exactly TWO painted faces?",
                "options": ["12 cubes (along the edges)", "8 cubes", "6 cubes", "1 cube"],
                "correct": 0,
                "solution_html": "<p>A cube has 12 edges. Each edge has 1 middle cube with 2 painted faces: 12 × 1 = <strong>12 cubes</strong>.</p>"
            },
            {
                "id": 35,
                "question": "In the same 3×3×3 painted cube, how many small cubes have exactly ONE painted face?",
                "options": ["6 cubes (one at the center of each face)", "12 cubes", "8 cubes", "0 cubes"],
                "correct": 0,
                "solution_html": "<p>A cube has 6 faces. Each face center has 1 cube with 1 painted face: 6 × 1 = <strong>6 cubes</strong>.</p>"
            },
            {
                "id": 36,
                "question": "What regular polygon forms all 20 faces of an icosahedron?",
                "options": ["Equilateral triangle", "Regular pentagon", "Square", "Hexagon"],
                "correct": 0,
                "solution_html": "<p>An icosahedron has 20 congruent <strong>equilateral triangular faces</strong>.</p>"
            },
            {
                "id": 37,
                "question": "How many regular pentagonal faces does a dodecahedron have?",
                "options": ["12 faces", "20 faces", "10 faces", "30 faces"],
                "correct": 0,
                "solution_html": "<p>'Dodeca' means 12. A dodecahedron has <strong>12 regular pentagonal faces</strong>.</p>"
            },
            {
                "id": 38,
                "question": "According to Euler's formula V - E + F = 2, if a dodecahedron has 12 faces and 30 edges, how many vertices must it have?",
                "options": ["20 vertices", "12 vertices", "24 vertices", "18 vertices"],
                "correct": 0,
                "solution_html": "<p>V - 30 + 12 = 2 ➔ V - 18 = 2 ➔ V = <strong>20 vertices</strong>.</p>"
            },
            {
                "id": 39,
                "question": "Why does a 4-sided square frame made of straws and clay wobble and collapse, while a triangular frame remains rigid?",
                "options": [
                    "A triangle's side lengths uniquely fix its three angles, making it inherently rigid",
                    "Squares have weaker clay balls",
                    "Straws are only strong in odd numbers",
                    "Squares cannot hold vertical weight"
                ],
                "correct": 0,
                "solution_html": "<p>A triangle is <strong>structurally rigid</strong> because its 3 edge lengths uniquely fix all 3 angles; a square frame can deform into a rhombus without changing side lengths.</p>"
            },
            {
                "id": 40,
                "question": "How many straws (edges) and clay balls (vertices) are needed to build a skeletal square pyramid?",
                "options": [
                    "8 straws and 5 clay balls",
                    "6 straws and 4 clay balls",
                    "12 straws and 8 clay balls",
                    "8 straws and 6 clay balls"
                ],
                "correct": 0,
                "solution_html": "<p>A square pyramid has 4 base edges + 4 slant edges = <strong>8 straws</strong>, and 4 base vertices + 1 apex vertex = <strong>5 clay balls</strong>.</p>"
            }
        ]
    }
]
