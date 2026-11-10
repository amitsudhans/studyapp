# -*- coding: utf-8 -*-
"""Part 3 (Slides 17-20: 4 Challenges × 10 Questions = 40 Questions) for Class 3 Mathematics Chapter 5: Fun with Shapes."""

import json
import re

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Mastery Quiz 1",
        "description": "Test your mastery of dot grid rangoli patterns, straight versus curved lines, and basic shape cutouts.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "How many straight sides and sharp corners does a square drawn on a dot grid have?",
                "options": ["4 sides and 4 corners", "3 sides and 3 corners", "4 sides and 2 corners", "5 sides and 4 corners"],
                "ans": "4 sides and 4 corners",
                "hint": "Recall the geometric definition of a square.",
                "explanation": "A square is a four-sided regular polygon with four equal straight edges meeting at four 90-degree corners.",
                "solution_steps": [
                    "Step 1: Count the straight boundary line segments connecting four adjacent grid dots, which equals 4 sides.",
                    "Step 2: Count the corner vertices where these perpendicular segments meet, which equals 4 corners.",
                    "Step 3: Combine both properties to conclude that a square has 4 sides and 4 corners."
                ]
            },
            {
                "id": "c1_q2",
                "q": "Which of the following objects has a boundary made purely of a curved line?",
                "options": ["A silver rupee coin", "A wooden ruler", "A rectangular door", "A triangular flag"],
                "ans": "A silver rupee coin",
                "hint": "Look for an object that rolls smoothly without any sharp vertices.",
                "explanation": "A coin is circular and bounded entirely by a continuous smooth curve without corners.",
                "solution_steps": [
                    "Step 1: Examine the boundaries of a ruler, door, and flag; all three are bounded by straight line segments meeting at vertices.",
                    "Step 2: Examine a round rupee coin; its rim forms a smooth circular contour with zero vertices.",
                    "Step 3: Confirm that the silver rupee coin is bounded purely by a curved line."
                ]
            },
            {
                "id": "c1_q3",
                "q": "If a craft picture of a boat uses 1 large triangle for the sail, 1 rectangle for the deck, and 2 circles for portholes, how many total shapes are used?",
                "options": ["4 shapes", "3 shapes", "5 shapes", "2 shapes"],
                "ans": "4 shapes",
                "hint": "Add the counts of all the shape cutouts together.",
                "explanation": "Adding 1 sail triangle + 1 deck rectangle + 2 porthole circles equals 4 shapes.",
                "solution_steps": [
                    "Step 1: Identify the triangular pieces: 1 triangle.",
                    "Step 2: Identify the quadrilaterals and circular pieces: 1 rectangle + 2 circles = 3 pieces.",
                    "Step 3: Calculate the grand total: 1 + 3 = 4 geometric shape cutouts."
                ]
            },
            {
                "id": "c1_q4",
                "q": "What happens when a taut piece of string is loosened and laid gently on a table?",
                "options": ["It bends into curved lines", "It turns into a straight line", "It forms a perfect square", "It disappears"],
                "ans": "It bends into curved lines",
                "hint": "Think about what happens when tension is released from a flexible thread.",
                "explanation": "A loose string naturally bends and forms flowing, wavy curves rather than a rigid straight line.",
                "solution_steps": [
                    "Step 1: Recall that pulling string tightly between two points forms a straight line.",
                    "Step 2: Observe that releasing tension allows the string to bend flexibly.",
                    "Step 3: Conclude that the relaxed string bends into curved lines."
                ]
            },
            {
                "id": "c1_q5",
                "q": "How many straight edges meet at each corner of a triangle drawn in a rangoli pattern?",
                "options": ["2 edges", "3 edges", "1 edge", "4 edges"],
                "ans": "2 edges",
                "hint": "Count how many sides intersect at a single vertex.",
                "explanation": "At any vertex or corner of a polygon, exactly two adjacent edges meet.",
                "solution_steps": [
                    "Step 1: Look at any single corner point of a triangle.",
                    "Step 2: Trace the boundary paths that start from that point; there are exactly two straight line segments.",
                    "Step 3: Confirm that exactly 2 straight edges meet at each corner."
                ]
            },
            {
                "id": "c1_q6",
                "q": "Which shape cutout cannot roll across a flat floor in a straight path?",
                "options": ["A square cutout", "A circular disc", "A round wheel", "A circular ring"],
                "ans": "A square cutout",
                "hint": "Flat sides and sharp corners prevent smooth rolling.",
                "explanation": "A square has four straight sides and corners that bump against the floor, preventing smooth rolling.",
                "solution_steps": [
                    "Step 1: Identify objects that roll: circular discs, wheels, and rings roll smoothly due to curved edges.",
                    "Step 2: Examine the square cutout; it has four flat edges and sharp right-angled corners.",
                    "Step 3: Conclude that the square cutout cannot roll smoothly across a flat floor."
                ]
            },
            {
                "id": "c1_q7",
                "q": "If you connect three non-collinear dots on a dot grid with straight lines, what shape is formed?",
                "options": ["A triangle", "A rectangle", "A circle", "A cylinder"],
                "ans": "A triangle",
                "hint": "Three dots joined by three straight segments produce this classic 3-sided figure.",
                "explanation": "Connecting three non-collinear dots with three straight segments encloses a 3-sided triangle.",
                "solution_steps": [
                    "Step 1: Plot three non-collinear dots on the grid.",
                    "Step 2: Draw straight line segments from dot 1 to dot 2, dot 2 to dot 3, and dot 3 back to dot 1.",
                    "Step 3: Observe that the resulting enclosed three-sided polygon is a triangle."
                ]
            },
            {
                "id": "c1_q8",
                "q": "Which of these everyday objects combines both straight edges and curved boundaries?",
                "options": ["An ice cream cone", "A closed rectangular book", "A standard wooden cube", "A flat square tile"],
                "ans": "An ice cream cone",
                "hint": "Look for an object with a round top and slanted straight sides.",
                "explanation": "An ice cream cone has straight conical sides tapering to a point and a curved circular top opening.",
                "solution_steps": [
                    "Step 1: Check the book, cube, and tile; each is bounded exclusively by straight edges.",
                    "Step 2: Check the ice cream cone; it features a curved scoop opening and straight tapering side profiles.",
                    "Step 3: Conclude that an ice cream cone combines both straight edges and curved contours."
                ]
            },
            {
                "id": "c1_q9",
                "q": "How many dots on a square dot grid are needed to outline a single unit square?",
                "options": ["4 dots", "3 dots", "6 dots", "2 dots"],
                "ans": "4 dots",
                "hint": "Each corner of the unit square sits on one dot.",
                "explanation": "A single unit square is defined by four corner dots arranged in a 2-by-2 square block.",
                "solution_steps": [
                    "Step 1: A square has 4 corners (vertices).",
                    "Step 2: On a dot grid, each vertex of the unit square aligns with one grid dot.",
                    "Step 3: Therefore, exactly 4 dots mark the vertices of a unit square."
                ]
            },
            {
                "id": "c1_q10",
                "q": "Why do traditional rangoli artists use dot grids to draw symmetrical geometric patterns?",
                "options": ["Dots maintain equal spacing and balance", "Dots make lines disappear", "Dots turn straight lines into circles", "Dots erase chalk powder"],
                "ans": "Dots maintain equal spacing and balance",
                "hint": "Think about how regular grid points help keep shapes neat and proportional.",
                "explanation": "Evenly spaced grid dots guide the hand to draw equal lengths, parallel paths, and balanced geometric motifs.",
                "solution_steps": [
                    "Step 1: Consider the challenge of drawing freehand symmetrical shapes.",
                    "Step 2: Recognize that a grid of evenly spaced dots provides fixed reference coordinates.",
                    "Step 3: Conclude that dot grids ensure equal spacing, precise proportions, and visual harmony."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Mastery Quiz 2",
        "description": "Evaluate your understanding of unfolded box nets, origami envelopes, and tracing cuboid faces.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "When a solid cuboid cardboard box is unfolded completely flat, how many faces are visible in its net?",
                "options": ["6 faces", "4 faces", "8 faces", "5 faces"],
                "ans": "6 faces",
                "hint": "Think about top, bottom, and four surrounding walls.",
                "explanation": "A standard cuboid box has six distinct faces: top, bottom, front, back, left, and right.",
                "solution_steps": [
                    "Step 1: Count the top and bottom faces of the box: 2 faces.",
                    "Step 2: Count the four surrounding side walls: 4 faces.",
                    "Step 3: Add them together: 2 + 4 = 6 flat rectangular faces in the unfolded net."
                ]
            },
            {
                "id": "c2_q2",
                "q": "When tracing around all faces of a standard rectangular matchbox, what shapes are drawn on paper?",
                "options": ["Rectangles (and possibly squares)", "Circles and ovals", "Triangles and hexagons", "Only circles"],
                "ans": "Rectangles (and possibly squares)",
                "hint": "Matchboxes are cuboids with flat rectangular boundaries.",
                "explanation": "All faces of a standard cuboid are planar rectangles, some of which may have equal sides as squares.",
                "solution_steps": [
                    "Step 1: Inspect the top and bottom of a matchbox; they are rectangles.",
                    "Step 2: Inspect the long side walls and end caps; they are narrower rectangles or squares.",
                    "Step 3: Conclude that tracing produces exclusively rectangles and possible square variations."
                ]
            },
            {
                "id": "c2_q3",
                "q": "If a baking tray contains 4 horizontal rows of biscuits with 6 biscuits in each row, what is the total biscuit count?",
                "options": ["24 biscuits", "20 biscuits", "10 biscuits", "18 biscuits"],
                "ans": "24 biscuits",
                "hint": "Multiply the number of rows by the number of biscuits per row.",
                "explanation": "Multiplying the 4 rows by 6 biscuits per row gives 4 × 6 = 24 biscuits.",
                "solution_steps": [
                    "Step 1: Identify the number of rows: 4 rows.",
                    "Step 2: Identify the count per row: 6 biscuits.",
                    "Step 3: Multiply row count by column count: 4 × 6 = 24 total biscuits."
                ]
            },
            {
                "id": "c2_q4",
                "q": "In an origami envelope made from a square sheet, what shape is the top fold-down closing flap?",
                "options": ["An inverted triangle", "A complete circle", "A long rectangle", "A pentagon"],
                "ans": "An inverted triangle",
                "hint": "Folding down a corner point creates a 3-sided shape pointing downward.",
                "explanation": "Folding down the top corner of the paper produces a triangular flap that overlaps the rectangular pocket.",
                "solution_steps": [
                    "Step 1: Recall the final step of envelope folding where the top pointed corner folds downward.",
                    "Step 2: Observe the boundary of this flap: two slanted folded creases meeting at a bottom point.",
                    "Step 3: Conclude that the closing flap forms an inverted triangle."
                ]
            },
            {
                "id": "c2_q5",
                "q": "How many matching pairs of identical opposite faces does every standard cuboid have?",
                "options": ["3 pairs", "2 pairs", "4 pairs", "6 pairs"],
                "ans": "3 pairs",
                "hint": "Six faces are divided equally into opposite pairs.",
                "explanation": "A cuboid has 6 faces grouped into 3 matching opposite pairs: top-bottom, front-back, and left-right.",
                "solution_steps": [
                    "Step 1: Identify pair 1: top and bottom faces have identical dimensions.",
                    "Step 2: Identify pair 2: front and back faces have identical dimensions.",
                    "Step 3: Identify pair 3: left and right end faces have identical dimensions, giving 3 matching pairs."
                ]
            },
            {
                "id": "c2_q6",
                "q": "If you unfold a cuboid box, what geometric elements do the straight fold lines correspond to in the 3D box?",
                "options": ["The 3D edges of the box", "The corners of the room", "The holes inside", "The thickness of paper"],
                "ans": "The 3D edges of the box",
                "hint": "When flaps bend up to make a box, fold lines become outer seams.",
                "explanation": "When the flat 2D net is folded up, each crease line bends at 90 degrees to form a 3D edge.",
                "solution_steps": [
                    "Step 1: Note that a flat net is folded along straight crease lines.",
                    "Step 2: When two adjacent faces are folded upward, their meeting line creates an edge.",
                    "Step 3: Conclude that the crease lines directly become the 3D edges of the box."
                ]
            },
            {
                "id": "c2_q7",
                "q": "A baker places biscuits in a 5-by-5 square tray. How many total biscuits are resting on the tray?",
                "options": ["25 biscuits", "20 biscuits", "10 biscuits", "30 biscuits"],
                "ans": "25 biscuits",
                "hint": "Multiply 5 rows by 5 biscuits per row.",
                "explanation": "A 5-by-5 array contains 5 rows of 5 biscuits: 5 × 5 = 25 biscuits.",
                "solution_steps": [
                    "Step 1: Count rows: 5 rows.",
                    "Step 2: Count items per row: 5 biscuits.",
                    "Step 3: Calculate the product: 5 × 5 = 25 total biscuits."
                ]
            },
            {
                "id": "c2_q8",
                "q": "When tracing around a round coin onto paper, what 2D shape is generated?",
                "options": ["A circle", "A triangle", "A rectangle", "A square"],
                "ans": "A circle",
                "hint": "The flat face of a coin has a circular perimeter.",
                "explanation": "The boundary of a cylindrical coin's base is a circle, producing a 2D circle when traced.",
                "solution_steps": [
                    "Step 1: Place a round coin flat on a sheet of paper.",
                    "Step 2: Trace along its perimeter with a pencil.",
                    "Step 3: The pencil marks a continuous curved boundary forming a 2D circle."
                ]
            },
            {
                "id": "c2_q9",
                "q": "Which 3D solid produces exclusively identical square outlines when traced across every single face?",
                "options": ["A cube", "A cuboid", "A cylinder", "A cone"],
                "ans": "A cube",
                "hint": "Think of a playing die with 6 identical faces.",
                "explanation": "A cube is a special cuboid where all 6 faces are identical squares of equal side length.",
                "solution_steps": [
                    "Step 1: Check a cuboid: faces can be varied rectangles.",
                    "Step 2: Check a cylinder: circular bases and curved side.",
                    "Step 3: Check a cube: all 6 faces are congruent squares, producing identical square outlines in all orientations."
                ]
            },
            {
                "id": "c2_q10",
                "q": "Why does folding a square paper corner-to-corner along its diagonal divide it into two equal triangles?",
                "options": ["The diagonal line serves as an axis of symmetry", "Triangles are smaller than squares", "Paper stretches diagonally", "Opposite edges are unequal"],
                "ans": "The diagonal line serves as an axis of symmetry",
                "hint": "Consider how the diagonal cuts the four equal sides and right angles in half evenly.",
                "explanation": "The diagonal connects opposite vertices and forms a line of reflective symmetry, splitting the square into two congruent right triangles.",
                "solution_steps": [
                    "Step 1: Draw a diagonal line connecting two opposite corners of a square.",
                    "Step 2: Observe that the diagonal bisects two 90-degree angles into 45-degree angles while sharing the hypotenuse.",
                    "Step 3: Conclude that the diagonal acts as an axis of symmetry, creating two identical right-angled triangles."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Mastery Quiz 3",
        "description": "Assess your understanding of rectangle properties, nested counts, square versus rectangle rules, and matchstick tiling.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "What is the defining rule that distinguishes a square from an ordinary rectangle?",
                "options": ["A square has all 4 sides equal; a rectangle only needs opposite sides equal", "A square has 3 sides; a rectangle has 4 sides", "A square has curved corners; a rectangle has sharp corners", "A square has no right angles"],
                "ans": "A square has all 4 sides equal; a rectangle only needs opposite sides equal",
                "hint": "Consider side lengths versus corner angles.",
                "explanation": "Both shapes have four right angles, but a square requires all four sides to be equal in length.",
                "solution_steps": [
                    "Step 1: Recall that both rectangles and squares have four straight sides and four 90-degree corners.",
                    "Step 2: In a general rectangle, opposite sides are equal (length and width can differ).",
                    "Step 3: In a square, all four sides must be strictly equal in length."
                ]
            },
            {
                "id": "c3_q2",
                "q": "How many matchsticks are required to build a single standalone square?",
                "options": ["4 matchsticks", "3 matchsticks", "5 matchsticks", "6 matchsticks"],
                "ans": "4 matchsticks",
                "hint": "Count the perimeter edges of one square.",
                "explanation": "Each side of a standalone square corresponds to one matchstick, requiring 4 sticks.",
                "solution_steps": [
                    "Step 1: A square has 4 boundary sides.",
                    "Step 2: Lay one matchstick per side to enclose the square.",
                    "Step 3: Conclude that 4 matchsticks are needed for a standalone square."
                ]
            },
            {
                "id": "c3_q3",
                "q": "If three identical squares are built in a straight connected row sharing internal walls, how many matchsticks are used?",
                "options": ["10 matchsticks", "12 matchsticks", "9 matchsticks", "11 matchsticks"],
                "ans": "10 matchsticks",
                "hint": "The first square needs 4 sticks, and each subsequent attached square needs 3 more sticks.",
                "explanation": "First square = 4 sticks; second square adds 3 sticks; third square adds 3 sticks: 4 + 3 + 3 = 10 sticks.",
                "solution_steps": [
                    "Step 1: Build the first square with 4 matchsticks.",
                    "Step 2: Add the second square sharing one existing stick, adding 3 new sticks (total 7).",
                    "Step 3: Add the third square sharing another existing stick, adding 3 more sticks: 7 + 3 = 10 sticks."
                ]
            },
            {
                "id": "c3_q4",
                "q": "In a 2-by-2 grid of square panes, how many total squares can you count (small and large)?",
                "options": ["5 squares", "4 squares", "6 squares", "8 squares"],
                "ans": "5 squares",
                "hint": "Count the 4 small individual squares plus the 1 large overarching square.",
                "explanation": "There are 4 small 1×1 squares and 1 large 2×2 square, totaling 4 + 1 = 5 squares.",
                "solution_steps": [
                    "Step 1: Count the individual 1-by-1 unit squares: 4 squares.",
                    "Step 2: Count the combined 2-by-2 outer boundary square: 1 square.",
                    "Step 3: Add the counts together: 4 + 1 = 5 total squares."
                ]
            },
            {
                "id": "c3_q5",
                "q": "If an angle tested with a folded paper tester opens wider than 90 degrees, it is:",
                "options": ["Greater than a square corner", "Less than a square corner", "Equal to a square corner", "A straight line"],
                "ans": "Greater than a square corner",
                "hint": "The tester represents an exact square corner (90 degrees).",
                "explanation": "An angle whose opening is broader than the 90-degree tester is greater than a square corner (obtuse angle).",
                "solution_steps": [
                    "Step 1: Place the 90-degree paper corner tester at the vertex of the angle.",
                    "Step 2: Notice that the rays of the tested angle spread beyond the edges of the tester.",
                    "Step 3: Classify the angle as greater than a square corner."
                ]
            },
            {
                "id": "c3_q6",
                "q": "Which everyday household item displays perfect square corners at every intersection?",
                "options": ["A rectangular picture frame", "A round tea coaster", "An oval mirror", "A circular clock face"],
                "ans": "A rectangular picture frame",
                "hint": "Look for perpendicular straight edges meeting at 90-degree angles.",
                "explanation": "A rectangular picture frame is constructed with perpendicular corner joints that form exact 90-degree square corners.",
                "solution_steps": [
                    "Step 1: Inspect coasters, mirrors, and clock faces; their rims are curved with no vertices.",
                    "Step 2: Inspect a picture frame; its four corners form perpendicular 90-degree joints.",
                    "Step 3: Confirm that the rectangular picture frame displays perfect square corners."
                ]
            },
            {
                "id": "c3_q7",
                "q": "How many matchsticks are needed to form two separate, disconnected equilateral triangles?",
                "options": ["6 matchsticks", "5 matchsticks", "4 matchsticks", "7 matchsticks"],
                "ans": "6 matchsticks",
                "hint": "Each disconnected triangle requires 3 sticks.",
                "explanation": "Each triangle requires 3 sticks; for 2 disconnected triangles: 3 + 3 = 6 matchsticks.",
                "solution_steps": [
                    "Step 1: Calculate sticks for triangle 1: 3 matchsticks.",
                    "Step 2: Calculate sticks for triangle 2: 3 matchsticks.",
                    "Step 3: Sum both counts: 3 + 3 = 6 matchsticks."
                ]
            },
            {
                "id": "c3_q8",
                "q": "If two equilateral triangles are joined along one shared side, how many matchsticks are used in total?",
                "options": ["5 matchsticks", "6 matchsticks", "4 matchsticks", "7 matchsticks"],
                "ans": "5 matchsticks",
                "hint": "One stick is shared as the common boundary seam.",
                "explanation": "First triangle = 3 sticks; attached triangle adds 2 sticks sharing the middle seam: 3 + 2 = 5 matchsticks.",
                "solution_steps": [
                    "Step 1: Lay 3 sticks to form the first triangle.",
                    "Step 2: Attach the second triangle using one existing side as the base, requiring only 2 new sticks.",
                    "Step 3: Sum the total sticks: 3 + 2 = 5 matchsticks."
                ]
            },
            {
                "id": "c3_q9",
                "q": "How many corners in a regular rectangle are square corners (90 degrees)?",
                "options": ["All 4 corners", "Only 2 corners", "3 corners", "0 corners"],
                "ans": "All 4 corners",
                "hint": "Every corner in a rectangle is a right angle.",
                "explanation": "By definition, a rectangle has four interior angles that are all right angles (square corners).",
                "solution_steps": [
                    "Step 1: Recall the definition of a rectangle.",
                    "Step 2: Verify that each pair of adjacent edges meets perpendicularly.",
                    "Step 3: Conclude that all 4 corners are square corners."
                ]
            },
            {
                "id": "c3_q10",
                "q": "Is a chessboard made up of squares or rectangles?",
                "options": ["Both: each tile is a square, which is also a special rectangle", "Only rectangles, not squares", "Neither, they are diamonds", "Only triangles"],
                "ans": "Both: each tile is a square, which is also a special rectangle",
                "hint": "Every square is mathematically a special rectangle.",
                "explanation": "The 64 tiles on a chessboard are squares (all four sides equal), and since every square is a rectangle, both terms are correct.",
                "solution_steps": [
                    "Step 1: Note that each tile has four equal sides and four right angles, making it a square.",
                    "Step 2: Recognize that any shape with four right angles and opposite equal sides is also a rectangle.",
                    "Step 3: Conclude that the tiles are squares, which are also special rectangles."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Mastery Quiz 4",
        "description": "Master circle center folding, polygon hierarchy, tangram dissection puzzles, and geometric borders.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "When you fold a circular paper plate in half twice along different directions, what is the point where the creases cross?",
                "options": ["The center of the circle", "A corner of the circle", "A vertex of a square", "An outer edge"],
                "ans": "The center of the circle",
                "hint": "Each fold creates a diameter crease.",
                "explanation": "Any two distinct diameter lines of a circle intersect at its exact geometric center.",
                "solution_steps": [
                    "Step 1: The first fold creates a straight crease through the center (a diameter).",
                    "Step 2: The second fold along another direction creates another diameter crease.",
                    "Step 3: The intersection point where two diameters cross is the exact center of the circle."
                ]
            },
            {
                "id": "c4_q2",
                "q": "How many pieces (tans) are in a standard classic Chinese tangram puzzle set?",
                "options": ["7 pieces", "6 pieces", "8 pieces", "5 pieces"],
                "ans": "7 pieces",
                "hint": "It includes 5 triangles, 1 square, and 1 parallelogram.",
                "explanation": "A classic tangram set is composed of exactly 7 geometric pieces dissected from a single square.",
                "solution_steps": [
                    "Step 1: Count the triangular pieces: 2 large + 1 medium + 2 small = 5 triangles.",
                    "Step 2: Count the four-sided pieces: 1 square + 1 parallelogram = 2 pieces.",
                    "Step 3: Add them together: 5 + 2 = 7 total tangram pieces."
                ]
            },
            {
                "id": "c4_q3",
                "q": "What is the name of an 8-sided polygon commonly seen on crimson street STOP signs?",
                "options": ["An octagon", "A hexagon", "A pentagon", "A decagon"],
                "ans": "An octagon",
                "hint": "The prefix 'octa-' means eight.",
                "explanation": "An octagon is an eight-sided polygon with eight vertices, standard for road stop signs.",
                "solution_steps": [
                    "Step 1: Count the sides of a stop sign: 8 straight sides.",
                    "Step 2: Recall Greek numerical prefixes: penta = 5, hexa = 6, octa = 8, deca = 10.",
                    "Step 3: Conclude that an 8-sided polygon is an octagon."
                ]
            },
            {
                "id": "c4_q4",
                "q": "How many triangles are among the seven pieces of a standard tangram puzzle?",
                "options": ["5 triangles", "3 triangles", "4 triangles", "6 triangles"],
                "ans": "5 triangles",
                "hint": "2 large, 1 medium, and 2 small triangles.",
                "explanation": "A tangram contains 5 triangles (2 large, 1 medium, 2 small), 1 square, and 1 parallelogram.",
                "solution_steps": [
                    "Step 1: Identify the two large triangles.",
                    "Step 2: Identify the one medium triangle and two small triangles.",
                    "Step 3: Sum them: 2 + 1 + 2 = 5 triangular pieces."
                ]
            },
            {
                "id": "c4_q5",
                "q": "How many straight sides and corners does a honeycomb hexagon have?",
                "options": ["6 sides and 6 corners", "5 sides and 5 corners", "7 sides and 7 corners", "8 sides and 8 corners"],
                "ans": "6 sides and 6 corners",
                "hint": "The prefix 'hexa-' indicates six.",
                "explanation": "A hexagon has 6 straight sides meeting at 6 vertices, as seen in bee honeycomb cells.",
                "solution_steps": [
                    "Step 1: Recall the polygon naming rule where 'hexa' means six.",
                    "Step 2: In any regular polygon, the number of sides equals the number of corners.",
                    "Step 3: Conclude that a hexagon has 6 sides and 6 corners."
                ]
            },
            {
                "id": "c4_q6",
                "q": "If you cut a rectangle diagonally from one corner to the opposite corner, what two shapes are formed?",
                "options": ["Two right-angled triangles", "Two squares", "Two smaller rectangles", "Two circles"],
                "ans": "Two right-angled triangles",
                "hint": "A diagonal cut across opposite corners splits the four right angles into triangles.",
                "explanation": "Drawing a diagonal across a rectangle divides it into two congruent right-angled triangles.",
                "solution_steps": [
                    "Step 1: Take a rectangle with four 90-degree corners.",
                    "Step 2: Cut straight from one corner to the diagonally opposite corner.",
                    "Step 3: Observe that each half has three straight sides and one 90-degree corner, forming two right-angled triangles."
                ]
            },
            {
                "id": "c4_q7",
                "q": "What is the name of a 5-sided polygon with 5 sharp corners?",
                "options": ["A pentagon", "A hexagon", "An octagon", "A triangle"],
                "ans": "A pentagon",
                "hint": "The prefix 'penta-' means five.",
                "explanation": "A polygon with exactly 5 sides and 5 corners is called a pentagon.",
                "solution_steps": [
                    "Step 1: Check the side count: 5 straight sides.",
                    "Step 2: Match with Greek numerical prefix 'penta' meaning five.",
                    "Step 3: Identify the shape as a pentagon."
                ]
            },
            {
                "id": "c4_q8",
                "q": "Can you assemble the two small tangram triangles together along their shortest sides to form a square?",
                "options": ["Yes, they fit together along their hypotenuses or legs to form a square", "No, triangles can never make a square", "Only if cut with scissors", "Only if stretched"],
                "ans": "Yes, they fit together along their hypotenuses or legs to form a square",
                "hint": "Try placing two identical right-angled triangles against each other along their long edges.",
                "explanation": "Joining two congruent right-angled isosceles triangles along their hypotenuses forms a perfect square equal in area to the tangram square piece.",
                "solution_steps": [
                    "Step 1: The two small tangram pieces are identical 45-45-90 degree right-angled triangles.",
                    "Step 2: Place them face-to-face along their longest edge (hypotenuse).",
                    "Step 3: Observe that the four outer edges are equal and all four corners are 90 degrees, forming a square."
                ]
            },
            {
                "id": "c4_q9",
                "q": "How many straight sides does a decagon have?",
                "options": ["10 sides", "12 sides", "8 sides", "9 sides"],
                "ans": "10 sides",
                "hint": "The prefix 'deca-' means ten.",
                "explanation": "A decagon is a ten-sided polygon with 10 vertices.",
                "solution_steps": [
                    "Step 1: Recall the prefix 'deca-' which stands for 10 (as in decade = 10 years).",
                    "Step 2: Relate prefix to polygon sides.",
                    "Step 3: Conclude that a decagon has exactly 10 sides."
                ]
            },
            {
                "id": "c4_q10",
                "q": "Why do decorative border patterns often repeat identical geometric shapes like triangles and diamonds?",
                "options": ["Repeating patterns create visual rhythm, symmetry, and balance", "Because only one shape is allowed in art", "To make the border crooked", "To hide the cloth underneath"],
                "ans": "Repeating patterns create visual rhythm, symmetry, and balance",
                "hint": "Think about why repetitive tiles and textile borders look appealing and structured.",
                "explanation": "Repetition of uniform geometric elements establishes rhythmic balance, continuous symmetry, and aesthetic harmony along borders.",
                "solution_steps": [
                    "Step 1: Consider how identical geometric units line up along an edge.",
                    "Step 2: Observe that consistent repetition creates predictable spatial intervals.",
                    "Step 3: Conclude that repeating shapes produce visual rhythm, symmetry, and balance."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Amma']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 3 (Slides 17-20 Challenges)...")
    assert len(slides_part3) == 4, "Must have 4 challenge slides"
    total_q = 0
    for s in slides_part3:
        sid = s["id"]
        title = s["title"]
        words = len(title.split())
        assert 1 <= words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {words})"
        
        slide_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
        qs = s["questions"]
        assert len(qs) == 10, f"Slide {sid} must have 10 questions, found {len(qs)}"
        total_q += len(qs)
        for q in qs:
            qid = q["id"]
            assert len(q["options"]) == 4, f"Question {qid} must have 4 options"
            assert q["ans"] in q["options"], f"Question {qid} answer '{q['ans']}' not in options"
            assert len(q["solution_steps"]) == 3, f"Question {qid} must have 3 solution steps"
    print(f"Part 3 validation successful! Total questions: {total_q}")
