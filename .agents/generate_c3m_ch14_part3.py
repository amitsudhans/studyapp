#!/usr/bin/env python3
"""
NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair
Part 3: Slides 17 to 20 (4 Challenge Slides × 10 Multi-Choice Questions = 40 Questions)
Strict titles: 1 to 3 words.
Each question has:
- question, 4 options, answer (0-3), hint, explanation
- solution_steps: strictly 3 steps
Zero human character names, zero lecturer personas.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Mastery Challenge: Lines of Symmetry & Bead Malas",
        "questions": [
            {
                "question": "How many lines of symmetry does a regular square have?",
                "options": ["1 line", "2 lines", "3 lines", "4 lines"],
                "answer": 3,
                "hint": "Consider vertical, horizontal, and both diagonal folds.",
                "explanation": "A square has 4 lines of symmetry: vertical, horizontal, and two diagonals.",
                "solution_steps": [
                    "Step 1: Identify all possible fold lines across a square.",
                    "Step 2: Fold vertically (1), horizontally (1), and along both diagonals (2).",
                    "Step 3: 1 + 1 + 2 = 4 lines of symmetry in total."
                ]
            },
            {
                "question": "Which of the following capital letters possesses horizontal line symmetry?",
                "options": ["Letter A", "Letter B", "Letter M", "Letter V"],
                "answer": 1,
                "hint": "Folding this letter across its horizontal middle divides it into matching top and bottom halves.",
                "explanation": "Capital letter B has a horizontal line of symmetry.",
                "solution_steps": [
                    "Step 1: Examine the candidates: A, B, M, V.",
                    "Step 2: Letters A, M, and V have vertical symmetry.",
                    "Step 3: Letter B can be divided horizontally into matching top and bottom halves."
                ]
            },
            {
                "question": "Which bead arrangement is symmetrical for a 6-bead necklace of Red (R) and Green (G)?",
                "options": ["R-R-R-G-G-G", "R-G-R-R-G-R", "R-G-G-G-R-G", "G-G-R-R-R-R"],
                "answer": 1,
                "hint": "The sequence must read identically from left-to-right and right-to-left.",
                "explanation": "R-G-R-R-G-R is a palindrome; both halves (R-G-R) mirror each other perfectly.",
                "solution_steps": [
                    "Step 1: Test each sequence for palindrome symmetry.",
                    "Step 2: R-G-R-R-G-R: left half is R-G-R, right half backwards is R-G-R.",
                    "Step 3: Both halves match, confirming bilateral symmetry."
                ]
            },
            {
                "question": "How many lines of symmetry does a scalene triangle (with all unequal sides) have?",
                "options": ["0 lines", "1 line", "2 lines", "3 lines"],
                "answer": 0,
                "hint": "No two sides or angles are equal in a scalene triangle.",
                "explanation": "A scalene triangle has no equal sides or angles, resulting in 0 lines of symmetry.",
                "solution_steps": [
                    "Step 1: Recall the definition of a scalene triangle: all sides and angles are unequal.",
                    "Step 2: Attempting to fold along any axis produces overhang without superimposition.",
                    "Step 3: Therefore, it has exactly 0 lines of symmetry."
                ]
            },
            {
                "question": "An equilateral triangle has how many lines of symmetry?",
                "options": ["1 line", "2 lines", "3 lines", "4 lines"],
                "answer": 2,
                "hint": "One line extends from each vertex to the midpoint of the opposite side.",
                "explanation": "An equilateral triangle has 3 equal sides and 3 lines of symmetry.",
                "solution_steps": [
                    "Step 1: Count the vertices of an equilateral triangle: 3 vertices.",
                    "Step 2: A line drawn from each vertex to the opposite side's midpoint creates 2 congruent halves.",
                    "Step 3: Thus, an equilateral triangle has 3 lines of symmetry."
                ]
            },
            {
                "question": "What is the result when an asymmetrical shape is folded in half?",
                "options": ["Both halves match perfectly", "The two halves do not match and create overhangs", "The shape turns into a circle", "The shape doubles in area"],
                "answer": 1,
                "hint": "Asymmetry means lacking balanced proportion.",
                "explanation": "Asymmetrical shapes do not match across any fold line, leaving uneven edges and overhangs.",
                "solution_steps": [
                    "Step 1: Define asymmetry: lack of symmetry or mirror balance.",
                    "Step 2: Folding an asymmetrical shape results in mismatched overlapping parts.",
                    "Step 3: Confirm that the two halves do not match."
                ]
            },
            {
                "question": "Which of these everyday objects typically exhibits bilateral symmetry?",
                "options": ["A natural tree branch with random twigs", "A human hand with distinct thumb and fingers", "A butterfly with spread wings", "A spilled puddle of water"],
                "answer": 2,
                "hint": "The left wing mirrors the right wing in shape and pattern.",
                "explanation": "A butterfly displays classic bilateral symmetry across its central body axis.",
                "solution_steps": [
                    "Step 1: Examine the shape of each object.",
                    "Step 2: A butterfly's left wing and right wing are mirror reflections in shape, size, and spots.",
                    "Step 3: Confirm the butterfly exhibits bilateral symmetry."
                ]
            },
            {
                "question": "If a symmetrical 10-bead mala has 4 blue beads and 6 white beads, what is a valid symmetrical sequence?",
                "options": ["B-B-W-W-W-W-W-W-B-B", "W-B-B-W-W-W-W-B-B-W", "B-W-W-W-B-B-W-W-W-B", "B-B-B-B-W-W-W-W-W-W"],
                "answer": 2,
                "hint": "Check that the sequence is a palindrome containing 4 B's and 6 W's.",
                "explanation": "B-W-W-W-B | B-W-W-W-B contains 4 B's and 6 W's and is perfectly symmetrical.",
                "solution_steps": [
                    "Step 1: Count the beads in B-W-W-W-B-B-W-W-W-B: 4 B and 6 W.",
                    "Step 2: Check symmetry from center: left is B-W-W-W-B, right is B-W-W-W-B in reverse.",
                    "Step 3: Both halves are identical mirror images."
                ]
            },
            {
                "question": "How many lines of symmetry does a circle have?",
                "options": ["1 line", "4 lines", "100 lines", "An infinite number of lines"],
                "answer": 3,
                "hint": "Any straight line passing through the center divides a circle into two equal halves.",
                "explanation": "Any diameter through the center is a line of symmetry, giving infinitely many lines.",
                "solution_steps": [
                    "Step 1: Consider diameters passing through a circle's center point.",
                    "Step 2: Folding along any diameter superimposes both semicircles perfectly.",
                    "Step 3: Since infinite diameters can be drawn, a circle has infinitely many lines of symmetry."
                ]
            },
            {
                "question": "Which of these digits has both vertical and horizontal symmetry in standard font?",
                "options": ["Digit 1", "Digit 8", "Digit 4", "Digit 7"],
                "answer": 1,
                "hint": "Look at the digit made of two symmetrical loops.",
                "explanation": "Digit 8 has both vertical and horizontal lines of symmetry.",
                "solution_steps": [
                    "Step 1: Inspect digit 8: top and bottom loops can be divided vertically and horizontally.",
                    "Step 2: Digits 1, 4, and 7 lack bilateral symmetry.",
                    "Step 3: Confirm digit 8 possesses two lines of symmetry."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Mastery Challenge: Kolam, Aipan & Mirror Reflections",
        "questions": [
            {
                "question": "What is the traditional name for the floral carpet created in Kerala during Onam?",
                "options": ["Alpana", "Pookalam", "Kolam", "Aipan"],
                "answer": 1,
                "hint": "'Poo' means flower in Malayalam.",
                "explanation": "Pookalam is the traditional floral rangoli created during Onam in Kerala.",
                "solution_steps": [
                    "Step 1: Match the floral art with its regional origin in Kerala.",
                    "Step 2: 'Pookalam' is made with fresh flower petals in concentric circular patterns.",
                    "Step 3: Confirm Pookalam is the correct traditional term."
                ]
            },
            {
                "question": "Aipan folk art from Uttarakhand traditionally features what color combination?",
                "options": ["Blue and yellow", "Red ochre base with white rice paste", "Green and black", "Gold and purple"],
                "answer": 1,
                "hint": "Red clay background painted with white paste.",
                "explanation": "Aipan is drawn with white rice paste (biswar) over a red terracotta/ochre base.",
                "solution_steps": [
                    "Step 1: Recall the traditional ingredients of Himalayan Aipan art.",
                    "Step 2: The base is red ochre (geru), and the painting paste is ground white rice (biswar).",
                    "Step 3: Conclude the color scheme is red ochre and white."
                ]
            },
            {
                "question": "When completing a drawing on a grid across a vertical mirror line, what remains identical?",
                "options": ["The horizontal distance", "The vertical height of each point", "The color brightness", "The line thickness"],
                "answer": 1,
                "hint": "Points reflect horizontally, so their vertical height does not change.",
                "explanation": "Vertical height stays identical; only horizontal distance is mirrored across the line.",
                "solution_steps": [
                    "Step 1: Understand reflection across a vertical line $x = c$.",
                    "Step 2: The $y$-coordinate (vertical height) remains constant: $(x, y) \\to (2c - x, y)$.",
                    "Step 3: Confirm vertical height remains identical."
                ]
            },
            {
                "question": "If a point is located at (3, 5) on a grid and reflected across the vertical axis $x = 0$, what are the new coordinates?",
                "options": ["(-3, 5)", "(3, -5)", "(-3, -5)", "(5, 3)"],
                "answer": 0,
                "hint": "Negate the $x$-coordinate while keeping the $y$-coordinate unchanged.",
                "explanation": "Reflecting across the $y$-axis changes $x$ from 3 to -3 while $y$ remains 5.",
                "solution_steps": [
                    "Step 1: Identify the reflection line: the vertical axis $x = 0$.",
                    "Step 2: Rule for vertical axis reflection: $(x, y) \\to (-x, y)$.",
                    "Step 3: Apply rule: $(3, 5) \\to (-3, 5)$."
                ]
            },
            {
                "question": "Why did the painter's trick fail when applied to an asymmetrical object like a tea kettle?",
                "options": ["Kettles absorb light", "A kettle has different features on left and right sides", "Mirrors cannot reflect hot items", "The canvas was too small"],
                "answer": 1,
                "hint": "The handle on one side does not match the spout on the other side.",
                "explanation": "An asymmetrical object does not have matching halves, so reflecting one half creates an invalid shape.",
                "solution_steps": [
                    "Step 1: Identify the anatomy of a kettle: handle on one side, spout on the opposite side.",
                    "Step 2: Reflecting half a kettle duplicates either two handles or two spouts.",
                    "Step 3: This proves reflection only works for genuinely symmetrical objects."
                ]
            },
            {
                "question": "What happens to the word 'MOM' when viewed in a vertical mirror?",
                "options": ["It reads backwards as WOW", "It reads identically as MOM", "It becomes illegible", "The letters turn upside down"],
                "answer": 1,
                "hint": "M and O are vertically symmetrical, and the word is a palindrome.",
                "explanation": "M and O have vertical symmetry, and MOM is symmetrical as a whole, so it reads MOM in a mirror.",
                "solution_steps": [
                    "Step 1: Inspect the individual letters: M and O both have vertical line symmetry.",
                    "Step 2: Inspect the sequence: M-O-M is a palindrome (reads same forward and backward).",
                    "Step 3: Thus, lateral inversion leaves the entire word 'MOM' visually identical."
                ]
            },
            {
                "question": "Which of the following shapes has rotational symmetry of order 4 (looks the same after every quarter turn)?",
                "options": ["Rectangle", "Square", "Scalene Triangle", "Trapezoid"],
                "answer": 1,
                "hint": "It has 4 equal sides and 4 right angles.",
                "explanation": "A square matches itself after every 90° rotation, possessing 4-fold rotational symmetry.",
                "solution_steps": [
                    "Step 1: Calculate rotation angle for order 4: 360° ÷ 4 = 90°.",
                    "Step 2: Test shapes: rotating a square by 90° yields an identical orientation.",
                    "Step 3: Confirm the square has 4-fold rotational symmetry."
                ]
            },
            {
                "question": "A student cuts a folded paper heart along the fold line. How many complete hearts are formed when unfolded?",
                "options": ["Half a heart", "1 complete symmetrical heart", "2 separate hearts", "4 small hearts"],
                "answer": 1,
                "hint": "The fold line is the center line of the single heart.",
                "explanation": "Cutting half a heart along a fold creates one complete symmetrical heart upon unfolding.",
                "solution_steps": [
                    "Step 1: Recognize that the paper is folded once with the heart's center along the crease.",
                    "Step 2: The cut passes through both folded layers simultaneously.",
                    "Step 3: Unfolding opens the two joined halves into 1 complete symmetrical heart."
                ]
            },
            {
                "question": "What is the primary artistic purpose of the dot grid (pulli) in traditional Tamil kolam?",
                "options": ["To count points for games", "To provide an orderly, symmetrical geometric framework", "To absorb water", "To measure distance in meters"],
                "answer": 1,
                "hint": "The dots guide the symmetrical curves and straight lines.",
                "explanation": "The dot grid provides the geometric reference points ensuring symmetry and proportion.",
                "solution_steps": [
                    "Step 1: Understand the technique of drawing pulli kolam.",
                    "Step 2: The dots establish regular spacing and mirror axes for the artist's lines.",
                    "Step 3: Conclude that the dot grid ensures orderly, symmetrical geometric construction."
                ]
            },
            {
                "question": "If an asymmetrical mask is cut without folding the paper in half, what practical problem commonly occurs?",
                "options": ["The mask changes color", "The eyeholes end up at uneven heights, obstructing vision", "The paper becomes indestructible", "The mask grows larger"],
                "answer": 1,
                "hint": "Uneven eyeholes make it difficult to see through both eyes comfortably.",
                "explanation": "Freehand cutting often results in mismatched eyehole heights and uneven spacing.",
                "solution_steps": [
                    "Step 1: Consider freehand cutting of two separate eyeholes without a central fold.",
                    "Step 2: Small human variations produce uneven vertical levels and distances from the nose.",
                    "Step 3: This causes misalignment with the wearer's eyes, obstructing vision."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Mastery Challenge: Tessellations & Rangometry Shapes",
        "questions": [
            {
                "question": "Which of these regular polygons CANNOT tessellate a flat surface by itself?",
                "options": ["Equilateral triangle", "Square", "Regular Pentagon", "Regular Hexagon"],
                "answer": 2,
                "hint": "Its interior angle is 108 degrees, which does not divide 360 degrees evenly.",
                "explanation": "Regular pentagons have 108° angles. 360 ÷ 108 = 3.33, leaving gaps when tiled.",
                "solution_steps": [
                    "Step 1: Check the interior angle of a regular pentagon: 108°.",
                    "Step 2: Calculate sum around a vertex: 3 × 108° = 324° (gap of 36°); 4 × 108° = 432° (overlap).",
                    "Step 3: Since 108 does not divide 360, regular pentagons cannot tessellate alone."
                ]
            },
            {
                "question": "What must the sum of interior angles around any vertex equal for tiles to fit without gaps?",
                "options": ["180 degrees", "270 degrees", "360 degrees", "540 degrees"],
                "answer": 2,
                "hint": "A full circular turn around a point in a plane.",
                "explanation": "A complete unbroken circle around a vertex point equals 360 degrees.",
                "solution_steps": [
                    "Step 1: Recall that the space around any point in a two-dimensional plane is a full circle.",
                    "Step 2: A full circular angle measures exactly 360 degrees.",
                    "Step 3: Thus, corner angles meeting at every vertex must sum to 360° to avoid gaps or overlaps."
                ]
            },
            {
                "question": "How many equilateral triangles meet at each vertex in a regular triangular tessellation?",
                "options": ["3 triangles", "4 triangles", "6 triangles", "8 triangles"],
                "answer": 2,
                "hint": "Each angle of an equilateral triangle is 60 degrees. 360 ÷ 60 = ?",
                "explanation": "6 × 60° = 360°, so 6 equilateral triangles meet at each vertex.",
                "solution_steps": [
                    "Step 1: Find the interior angle of an equilateral triangle: 60°.",
                    "Step 2: Divide 360° by 60°: 360 ÷ 60 = 6.",
                    "Step 3: Exactly 6 equilateral triangles meet at each vertex."
                ]
            },
            {
                "question": "How many regular hexagons meet at each vertex in a honeycomb tiling?",
                "options": ["2 hexagons", "3 hexagons", "4 hexagons", "6 hexagons"],
                "answer": 1,
                "hint": "Each interior angle of a regular hexagon is 120 degrees.",
                "explanation": "3 × 120° = 360°, so 3 hexagons meet at each vertex.",
                "solution_steps": [
                    "Step 1: Calculate the interior angle of a regular hexagon: (6 - 2) × 180° ÷ 6 = 120°.",
                    "Step 2: Divide total vertex angle 360° by 120°: 360 ÷ 120 = 3.",
                    "Step 3: Exactly 3 regular hexagons meet at each joint vertex."
                ]
            },
            {
                "question": "Why do round circular coins fail to tessellate a flat surface?",
                "options": ["Coins are made of metal", "Circles leave curved open gaps between them", "Coins are too small", "Circles have no center"],
                "answer": 1,
                "hint": "Packing circles together always leaves small curved spaces between them.",
                "explanation": "Circles cannot fill 360° completely at contact points, leaving open interstitial gaps.",
                "solution_steps": [
                    "Step 1: Arrange identical circular coins touching edge-to-edge.",
                    "Step 2: Observe the empty triangular-like curved spaces left between touching circles.",
                    "Step 3: Conclude that circles cannot form a gapless tessellation."
                ]
            },
            {
                "question": "If you modify a square by cutting a triangle from the bottom and attaching it to the top, what is preserved?",
                "options": ["Only the perimeter", "The total surface area", "The color of the tile", "The number of right angles"],
                "answer": 1,
                "hint": "Area cut from one place is added to another.",
                "explanation": "The total area remains constant because no material was lost, only translated.",
                "solution_steps": [
                    "Step 1: Start with initial area $A = s^2$.",
                    "Step 2: Subtract area $T$ from bottom edge, add identical area $T$ to top edge: $A - T + T = A$.",
                    "Step 3: Total area is conserved."
                ]
            },
            {
                "question": "In a craft fair tiling project, a worker combines 2 squares and 3 equilateral triangles at a vertex. Do they fit flat?",
                "options": ["Yes, because (2 × 90°) + (3 × 60°) = 360°", "No, because the angles sum to 300°", "No, because triangles cannot touch squares", "Yes, because all shapes have straight lines"],
                "answer": 0,
                "hint": "2 × 90 = 180, and 3 × 60 = 180. 180 + 180 = 360.",
                "explanation": "(2 × 90°) + (3 × 60°) = 180° + 180° = 360°, forming a valid semi-regular tessellation.",
                "solution_steps": [
                    "Step 1: Calculate contribution of 2 squares: 2 × 90° = 180°.",
                    "Step 2: Calculate contribution of 3 triangles: 3 × 60° = 180°.",
                    "Step 3: Sum the angles: 180° + 180° = 360°. They fit together flat without gaps."
                ]
            },
            {
                "question": "What is a major advantage of using interlocking paving bricks on outdoor fairground paths?",
                "options": ["They melt in the rain", "They prevent displacement and create a continuous, stable surface", "They make walking noisier", "They change direction automatically"],
                "answer": 1,
                "hint": "Interlocking shapes lock each other in place against heavy foot traffic.",
                "explanation": "Interlocking tiles resist shifting and eliminate tripping hazards under heavy foot traffic.",
                "solution_steps": [
                    "Step 1: Examine physical forces on pathway bricks from thousands of walking visitors.",
                    "Step 2: Interlocking geometry distributes lateral loads and locks adjacent blocks together.",
                    "Step 3: This prevents tiles from popping out or creating dangerous gaps."
                ]
            },
            {
                "question": "Which of the following geometric tiles can be used alongside regular octagons to create a gapless floor pattern?",
                "options": ["Squares", "Equilateral Triangles", "Circles", "Pentagons"],
                "answer": 0,
                "hint": "An octagon has 135° angles. Two octagons make 270°. What shape provides the remaining 90°?",
                "explanation": "Two octagons (2 × 135° = 270°) leave 90°, which is filled perfectly by a square (270° + 90° = 360°).",
                "solution_steps": [
                    "Step 1: Interior angle of regular octagon = 135°.",
                    "Step 2: Two octagons meeting at a vertex sum to 135° + 135° = 270°.",
                    "Step 3: Remaining angle to reach 360° = 360° - 270° = 90°, exactly matching a square corner."
                ]
            },
            {
                "question": "What name is given to repeating patterns that decorate edges and borders in traditional architecture?",
                "options": ["Frieze patterns", "Random clusters", "Fractions", "Subtractions"],
                "answer": 0,
                "hint": "These linear decorative bands repeat along temple cornices and wall tops.",
                "explanation": "A frieze pattern is an architectural border pattern that repeats infinitely in one direction.",
                "solution_steps": [
                    "Step 1: Identify linear repeating decorative border bands in architecture.",
                    "Step 2: In geometry and art history, these single-direction repeating patterns are called frieze patterns.",
                    "Step 3: Confirm frieze pattern is the correct term."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Mastery Challenge: Fairground Maps & Maze Logic",
        "questions": [
            {
                "question": "What do map symbols represent on a fairground guide map?",
                "options": ["Real-world physical locations and amenities", "Random decorative drawings", "Prices of food items", "The names of visitors"],
                "answer": 0,
                "hint": "Symbols stand for actual places like restrooms, parking, ATMs, and stages.",
                "explanation": "Map symbols represent physical locations and amenities in a simplified, standardized visual form.",
                "solution_steps": [
                    "Step 1: Understand map representation.",
                    "Step 2: Icons such as parking 'P', food plate, or ATM represent real facilities on the grounds.",
                    "Step 3: Confirm symbols represent physical real-world locations."
                ]
            },
            {
                "question": "On a standard fair map, which direction is conventionally oriented toward the top of the page?",
                "options": ["South", "East", "North", "West"],
                "answer": 2,
                "hint": "Remember the compass rose: North is at the top.",
                "explanation": "By cartographic convention, North is oriented toward the top of maps.",
                "solution_steps": [
                    "Step 1: Check standard map orientation conventions.",
                    "Step 2: The compass rose places North at the top, South at bottom, East to right, West to left.",
                    "Step 3: Confirm North is at the top."
                ]
            },
            {
                "question": "A visitor walks along Blue Lane, turns left onto Red Lane, and reaches the Giant Wheel. What type of thinking is used?",
                "options": ["Fractional division", "Sequential route following and spatial navigation", "Weight comparison", "Calendar counting"],
                "answer": 1,
                "hint": "Navigating step-by-step turns along labeled pathways.",
                "explanation": "Following a sequence of turns and paths exercises spatial orientation and navigation.",
                "solution_steps": [
                    "Step 1: Identify the task: following a sequence of lanes and turns.",
                    "Step 2: This involves spatial mental mapping, direction tracking, and route planning.",
                    "Step 3: Confirm this is sequential route following and spatial navigation."
                ]
            },
            {
                "question": "In a maze, what is the mathematical term for a point where a path divides into two or more choices?",
                "options": ["A dead end", "A junction (or intersection)", "A boundary", "A perimeter"],
                "answer": 1,
                "hint": "A fork in the road where you must choose which way to turn.",
                "explanation": "A junction or node is a decision point where a path splits into multiple branches.",
                "solution_steps": [
                    "Step 1: Define maze features: paths, dead ends, and choice points.",
                    "Step 2: A location where a pathway branches into multiple directions is called a junction.",
                    "Step 3: Confirm junction (intersection) is the correct term."
                ]
            },
            {
                "question": "What systematic strategy guarantees escaping any simply connected maze with an entrance and exit on the outer perimeter?",
                "options": ["Running randomly as fast as possible", "The wall-follower rule (keeping your right hand continuously on the wall)", "Closing your eyes and guessing", "Climbing over the hedge"],
                "answer": 1,
                "hint": "Keep one hand touching the wall continuously without letting go.",
                "explanation": "The right-hand (or left-hand) rule guarantees traversal of the entire boundary to the exit in simply connected mazes.",
                "solution_steps": [
                    "Step 1: Recall the classic maze-solving algorithm: the wall-follower rule.",
                    "Step 2: Placing one hand on the wall and walking continuously traces the boundary uninterrupted.",
                    "Step 3: In a simply connected maze, this algorithm is mathematically proven to lead to the exit."
                ]
            },
            {
                "question": "If a visitor starts at the Chaupal (center) and walks North along Golden Lane, in which direction are they moving?",
                "options": ["Toward the top of the map", "Toward the bottom of the map", "Toward the left of the map", "Toward the right of the map"],
                "answer": 0,
                "hint": "North points directly toward the top of a standard map.",
                "explanation": "Moving North corresponds to moving toward the top edge of the map.",
                "solution_steps": [
                    "Step 1: Identify current position: central chaupal.",
                    "Step 2: Direction of travel is North.",
                    "Step 3: On a standard map, North is directly upward toward the top."
                ]
            },
            {
                "question": "Why is recording landmarks (like a fountain or statue) vital during maze navigation?",
                "options": ["To paint them different colors", "To detect if you have looped back to an earlier location", "To sell them to visitors", "To make the maze wider"],
                "answer": 1,
                "hint": "Seeing the same statue twice means you walked in a circle.",
                "explanation": "Landmarks serve as memory anchors, preventing navigators from looping repeatedly.",
                "solution_steps": [
                    "Step 1: Consider what happens when lost in a winding maze: circular paths can look identical.",
                    "Step 2: Spotting a previously noted landmark proves that the current loop is redundant.",
                    "Step 3: This allows the navigator to backtrack and choose an unexplored alternative branch."
                ]
            },
            {
                "question": "A map scale indicates that 1 centimeter on the map equals 50 meters on the ground. How far is a 4 cm path in reality?",
                "options": ["100 meters", "150 meters", "200 meters", "250 meters"],
                "answer": 2,
                "hint": "Multiply 4 by 50 meters.",
                "explanation": "4 × 50 meters = 200 meters.",
                "solution_steps": [
                    "Step 1: Identify scale factor: 1 cm on map = 50 m on ground.",
                    "Step 2: Multiply map distance by scale factor: 4 cm × 50 m/cm.",
                    "Step 3: 4 × 50 = 200 meters on the ground."
                ]
            },
            {
                "question": "If a fairground map shows four color zones: Golden (Center), Red (Food), Blue (Water), Green (Nature), which lane would you take to buy lunch?",
                "options": ["Blue Lane", "Red Lane", "Green Lane", "Golden Lane"],
                "answer": 1,
                "hint": "The food stalls and kulfi carts are located in the Red zone.",
                "explanation": "Red Lane connects the food stalls, refreshment kiosks, and kulfi carts.",
                "solution_steps": [
                    "Step 1: Review map legend descriptions for the color zones.",
                    "Step 2: Red zone is designated for food courts, kulfi carts, and refreshments.",
                    "Step 3: Take Red Lane to buy lunch."
                ]
            },
            {
                "question": "What is the final goal of the Surajkund Fair maze puzzle?",
                "options": ["To collect five heavy stones", "To find a clear, unobstructed path from the entry to the exit gate", "To stay inside the maze overnight", "To count the number of leaves on hedges"],
                "answer": 1,
                "hint": "Successfully navigating from the start to the outside exit.",
                "explanation": "The objective is navigating from the maze entrance through the winding hedges to the exit gate.",
                "solution_steps": [
                    "Step 1: Understand the premise of the fair maze challenge.",
                    "Step 2: Navigators must eliminate dead ends and trace an open route out of the fairgrounds.",
                    "Step 3: Conclude that finding a clear route from entrance to exit gate is the goal."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        title_words = len(s["title"].strip().split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_words} words) -> {len(s['questions'])} questions")
        assert 1 <= title_words <= 3, f"Title violation on slide {s['id']}"
        assert len(s["questions"]) == 10, f"Question count mismatch on slide {s['id']}"
        for qidx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4, f"Slide {s['id']} Q{qidx+1} options count != 4"
            assert q["answer"] in [0, 1, 2, 3], f"Slide {s['id']} Q{qidx+1} answer invalid"
            assert len(q["solution_steps"]) == 3, f"Slide {s['id']} Q{qidx+1} solution steps != 3"
    print("Part 3 passed all strict validation checks!")
