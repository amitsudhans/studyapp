# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 1: Shapes Around Us - Part 3 (Slides 17 to 20)
40 Quiz questions (10 per challenge slide) with instant grading, hint, explanation, and solution_html.
"""

def make_sol_html(steps, final_ans):
    html = "<div class='space-y-3 p-3 bg-slate-900/80 rounded-xl border border-slate-700/60 font-sans text-sm text-slate-200'>"
    html += "<h4 class='font-bold text-amber-400 text-base border-b border-slate-700 pb-1.5 flex items-center gap-2'><span>📝</span> Step-by-Step Mathematical Solution</h4>"
    html += "<ol class='list-decimal list-inside space-y-2 text-slate-300 leading-relaxed'>"
    for step in steps:
        html += f"<li class='pl-1'><span class='text-slate-100 font-medium'>{step}</span></li>"
    html += "</ol>"
    html += f"<div class='mt-3 pt-2 border-t border-slate-700/60 text-emerald-400 font-semibold flex items-center gap-1.5'><span>✅</span> <span>Conclusion:</span> <span class='text-white font-bold'>{final_ans}</span></div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "questions": [
            {
                "q": "Which 3D geometric shape serves as the most stable base for a monument model?",
                "options": ["Sphere", "Cone", "Cuboid", "Cylinder on side"],
                "ans": 2,
                "hint": "Think of a solid with wide, flat rectangular faces that cannot roll.",
                "explanation": "A cuboid has broad, flat rectangular surfaces that sit securely on the table without tipping.",
                "solution_html": make_sol_html([
                    "Evaluate the physical stability of 3D solids on a horizontal plane.",
                    "Spheres and rolling cylinders have curved surfaces that easily roll away under gravity.",
                    "Cones have a narrow pointed apex when inverted, or a circular base prone to rocking.",
                    "A rectangular cuboid possesses wide, flat perpendicular faces that offer maximum frictional grip and stability."
                ], "A flat-faced cuboid provides the most stable foundation base.")
            },
            {
                "q": "How many storeys and internal spiral stairs are there in the historic Qutub Minar?",
                "options": ["3 storeys, 200 stairs", "5 storeys, 379 stairs", "4 storeys, 300 stairs", "6 storeys, 450 stairs"],
                "ans": 1,
                "hint": "Recall the architectural facts recorded about the tallest brick minaret.",
                "explanation": "The Qutub Minar stands 72.5 meters tall with 5 tapering storeys and 379 internal stairs.",
                "solution_html": make_sol_html([
                    "Recall historical architectural specifications of the Qutub Minar in New Delhi.",
                    "The minaret is constructed from carved red sandstone and marble in 5 distinct storeys.",
                    "Internal ascent is provided by a continuous winding spiral staircase comprising exactly 379 stone steps."
                ], "Qutub Minar has 5 storeys and 379 internal stairs.")
            },
            {
                "q": "How many faces, edges, and vertices does a standard rectangular building brick possess?",
                "options": ["6 faces, 8 edges, 12 vertices", "6 faces, 12 edges, 8 vertices", "8 faces, 12 edges, 6 vertices", "5 faces, 9 edges, 6 vertices"],
                "ans": 1,
                "hint": "A brick is shaped like a cuboid.",
                "explanation": "A standard brick is a rectangular cuboid with 6 rectangular faces, 12 straight edges, and 8 corner vertices.",
                "solution_html": make_sol_html([
                    "Identify the 3D shape of a standard construction brick: it is a rectangular cuboid.",
                    "Count flat faces: top, bottom, front, back, left, right = 6 faces.",
                    "Count straight edges: 4 on top + 4 on bottom + 4 vertical posts = 12 edges.",
                    "Count corner vertices: 4 top corners + 4 bottom corners = 8 vertices."
                ], "A standard brick has 6 faces, 12 edges, and 8 vertices.")
            },
            {
                "q": "Why do bricklayers arrange bricks in overlapping running bonds rather than aligned vertical seams?",
                "options": ["To make the wall lighter", "To distribute weight evenly and prevent continuous cracks", "To allow wind to blow through", "To use less mortar"],
                "ans": 1,
                "hint": "Consider what would happen if a crack started at the top of a straight vertical line.",
                "explanation": "Overlapping bricks distribute downward forces across neighboring bricks and stop cracks from traveling straight down.",
                "solution_html": make_sol_html([
                    "Analyze mechanical load distribution in masonry construction.",
                    "If bricks are stacked in straight columns with aligned vertical mortar joints, any vertical stress causes the joint to split open continuously from top to bottom.",
                    "By staggering bricks so that each upper brick rests across the boundary of two lower bricks, downward loads are distributed diagonally into a stable pyramid of support.",
                    "This interlocking bond locks the wall together securely."
                ], "Overlapping bonds distribute loads evenly and prevent continuous vertical cracking.")
            },
            {
                "q": "What geometric characteristic uniquely identifies all prisms?",
                "options": ["They have a single apex point", "They have two identical, parallel bases joined by rectangular side faces", "They have only curved surfaces", "They always have five faces"],
                "ans": 1,
                "hint": "Prisms have identical polygon ends that face each other.",
                "explanation": "A prism is defined by two congruent, parallel polygon bases connected by rectangular side faces.",
                "solution_html": make_sol_html([
                    "Review the geometric definition of a prism.",
                    "A prism has two opposite end faces that are congruent polygons lying in parallel planes.",
                    "All the lateral side faces connecting the corresponding sides of these bases are rectangles (or parallelograms)."
                ], "Prisms possess two identical parallel bases connected by rectangular side faces.")
            },
            {
                "q": "In a square pyramid, how many triangular side faces slope upward to meet at the apex?",
                "options": ["3 faces", "4 faces", "5 faces", "6 faces"],
                "ans": 1,
                "hint": "The square base has 4 straight edges.",
                "explanation": "Each of the 4 edges of the square base gives rise to one triangular face that ascends to the top apex.",
                "solution_html": make_sol_html([
                    "Examine the anatomy of a pyramid: every edge of the base polygon anchors one triangular lateral face.",
                    "A square base has exactly 4 straight boundary edges.",
                    "Therefore, exactly 4 triangular side faces rise upward to converge at the single shared apex vertex."
                ], "A square pyramid has 4 triangular side faces meeting at its apex.")
            },
            {
                "q": "How many faces (F), vertices (V), and edges (E) does a triangular prism possess?",
                "options": ["F = 4, V = 4, E = 6", "F = 5, V = 6, E = 9", "F = 5, V = 5, E = 8", "F = 6, V = 8, E = 12"],
                "ans": 1,
                "hint": "It has 2 triangular bases and 3 rectangular sides.",
                "explanation": "A triangular prism has 2 triangles + 3 rectangles = 5 faces, 3 + 3 = 6 vertices, and 3 + 3 + 3 = 9 edges.",
                "solution_html": make_sol_html([
                    "Count faces (F): 2 triangular end bases + 3 rectangular lateral faces = 5 faces.",
                    "Count vertices (V): 3 corners on the front triangle + 3 corners on the rear triangle = 6 vertices.",
                    "Count edges (E): 3 edges on front base + 3 edges on rear base + 3 connecting length edges = 9 edges."
                ], "For a triangular prism: F = 5, V = 6, E = 9.")
            },
            {
                "q": "Using Euler's formula F + V - E = 2, if a polyhedron has 6 faces and 8 vertices, how many edges does it have?",
                "options": ["10 edges", "11 edges", "12 edges", "14 edges"],
                "ans": 2,
                "hint": "Substitute F = 6 and V = 8 into F + V - E = 2.",
                "explanation": "6 + 8 - E = 2 → 14 - E = 2 → E = 14 - 2 = 12 edges.",
                "solution_html": make_sol_html([
                    "State Euler's Polyhedral Formula: F + V - E = 2.",
                    "Substitute given values: F = 6 and V = 8.",
                    "Compute: 6 + 8 - E = 2.",
                    "14 - E = 2.",
                    "Solve for E: E = 14 - 2 = 12 edges."
                ], "The polyhedron has 12 edges (this is a cube or rectangular cuboid).")
            },
            {
                "q": "On a standard fair gaming die, what number is located directly opposite to the face with 3 pips?",
                "options": ["2", "4", "5", "6"],
                "ans": 1,
                "hint": "Opposite faces on a standard die always sum to 7.",
                "explanation": "Because opposite faces sum to 7, the face opposite 3 must be 7 - 3 = 4.",
                "solution_html": make_sol_html([
                    "Recall the universal pip rule for standard gaming dice: opposite face numbers always add up to 7.",
                    "The given face is 3.",
                    "Calculate opposite face: 7 - 3 = 4."
                ], "The opposite face has 4 pips.")
            },
            {
                "q": "Can two opposite faces of a 3D cube ever share a common boundary edge?",
                "options": ["Yes, along one edge", "Yes, at two corners", "No, opposite faces are parallel and never touch", "Only in transparent cubes"],
                "ans": 2,
                "hint": "Adjacent faces touch along an edge; opposite faces lie on opposite parallel sides.",
                "explanation": "Opposite faces in a cube lie on parallel planes separated by the cube's interior, so they never touch or share an edge.",
                "solution_html": make_sol_html([
                    "Understand adjacent versus opposite faces in solid polyhedra.",
                    "Adjacent faces share a line-segment boundary edge (e.g., top and front).",
                    "Opposite faces lie on distinct, parallel planes facing away from each other across the solid interior.",
                    "Therefore, opposite faces can never share an edge or corner."
                ], "Opposite faces are parallel and never share any boundary edge.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "questions": [
            {
                "q": "A cube has 6 colored faces. View 1 shows Red, Blue, Green. View 2 shows Red, Green, Yellow. View 3 shows Blue, Green, Purple. What color is opposite Green?",
                "options": ["Red", "Blue", "The 6th remaining color", "Yellow"],
                "ans": 2,
                "hint": "Any color seen adjacent to Green cannot be opposite Green.",
                "explanation": "Green touches Red, Blue, Yellow, and Purple. Thus, none of these can be opposite Green. The remaining 6th color must be opposite.",
                "solution_html": make_sol_html([
                    "List all faces that appear adjacent to Green across the three views:",
                    "View 1 shows Green touching Red and Blue.",
                    "View 2 shows Green touching Red and Yellow.",
                    "View 3 shows Green touching Blue and Purple.",
                    "Thus, Green is adjacent to Red, Blue, Yellow, and Purple (4 distinct colors).",
                    "Since a cube has only 6 faces, the 4 adjacent colors cannot be opposite Green.",
                    "Therefore, only the 6th remaining color can be on the opposite face."
                ], "The 6th remaining color is situated directly opposite Green.")
            },
            {
                "q": "In a Venn diagram of 3D shapes, where does a triangular prism belong if circles represent 'Has rectangular faces' and 'Has triangular faces'?",
                "options": ["Only in the rectangular circle", "Only in the triangular circle", "In the overlapping intersection", "Outside both circles"],
                "ans": 2,
                "hint": "Count the types of faces on a triangular prism.",
                "explanation": "A triangular prism has 3 rectangular faces and 2 triangular bases, placing it directly in the intersection.",
                "solution_html": make_sol_html([
                    "Examine the faces of a triangular prism: it has 2 triangular bases and 3 rectangular lateral sides.",
                    "Since it possesses rectangular faces, it satisfies the first set.",
                    "Since it possesses triangular faces, it satisfies the second set.",
                    "An element belonging to both sets must be placed in their overlapping intersection."
                ], "A triangular prism belongs in the overlapping intersection of both circles.")
            },
            {
                "q": "Which description accurately classifies a solid cylinder?",
                "options": ["6 flat faces and 12 straight edges", "2 flat circular faces and 1 curved surface with 2 curved edges", "1 curved surface and 0 flat faces", "1 flat circular face and 1 apex"],
                "ans": 1,
                "hint": "Think of a tin can with top and bottom lids.",
                "explanation": "A cylinder features two flat circular circular bases and one smooth curved body wall, giving it 2 curved edges.",
                "solution_html": make_sol_html([
                    "Analyze the surfaces of a 3D cylinder:",
                    "Top surface: flat circle (1 flat face).",
                    "Bottom surface: flat circle (1 flat face).",
                    "Lateral boundary: smooth wrapped surface (1 curved surface).",
                    "Edges: where the circular bases meet the curved surface, forming 2 circular curved edges.",
                    "Vertices: 0 corner points."
                ], "A cylinder has 2 flat circular faces, 1 curved surface, and 2 curved edges.")
            },
            {
                "q": "How many flat faces, edges, and vertices does a perfect geometric sphere possess?",
                "options": ["1 flat face, 1 edge, 0 vertices", "0 flat faces, 0 edges, 0 vertices (1 continuous curved surface)", "2 flat faces, 1 curved edge", "6 flat faces, 8 vertices"],
                "ans": 1,
                "hint": "A sphere is completely smooth all around like a ball.",
                "explanation": "A sphere has no flat faces, no straight or curved edges, and no sharp vertices; it is a single continuous curved surface.",
                "solution_html": make_sol_html([
                    "Examine the geometric properties of a sphere.",
                    "Every point on a sphere's surface is equidistant from its center.",
                    "There are no flat polygonal planar regions, so flat faces = 0.",
                    "There are no seams or intersections of distinct planes, so edges = 0.",
                    "There are no pointed intersections of edges, so vertices = 0.",
                    "It consists entirely of 1 smooth, continuous curved surface."
                ], "A sphere has 0 flat faces, 0 edges, and 0 vertices.")
            },
            {
                "q": "A cube tower is built in 3 vertical columns with heights 4, 3, and 2 unit cubes. What is the total volume?",
                "options": ["8 unit cubes", "9 unit cubes", "10 unit cubes", "12 unit cubes"],
                "ans": 1,
                "hint": "Add the number of cubes in each vertical column.",
                "explanation": "Summing the column heights: 4 + 3 + 2 = 9 unit cubes.",
                "solution_html": make_sol_html([
                    "Identify the number of unit cubes in each vertical column:",
                    "Column 1 has height = 4 cubes.",
                    "Column 2 has height = 3 cubes.",
                    "Column 3 has height = 2 cubes.",
                    "Calculate total volume by summing column counts: 4 + 3 + 2 = 9 unit cubes."
                ], "Total volume is 9 unit cubes.")
            },
            {
                "q": "In a 3-layer stepped pyramid tower with 1 cube on top, 4 cubes on the middle layer, and 9 cubes on the bottom layer, how many total cubes are used?",
                "options": ["12 cubes", "13 cubes", "14 cubes", "16 cubes"],
                "ans": 2,
                "hint": "Sum the cubes on each layer: 1 + 4 + 9.",
                "explanation": "Top layer (1) + Middle layer (4) + Bottom layer (9) = 14 unit cubes in total.",
                "solution_html": make_sol_html([
                    "Perform layer-by-layer summation from top to bottom:",
                    "Layer 1 (top): 1 cube (1 × 1 square).",
                    "Layer 2 (middle): 4 cubes (2 × 2 square).",
                    "Layer 3 (bottom): 9 cubes (3 × 3 square).",
                    "Sum all layers: 1 + 4 + 9 = 14 unit cubes."
                ], "The stepped pyramid contains 14 unit cubes.")
            },
            {
                "q": "On isometric dot paper, what geometric shape is formed by any three nearest neighboring dots?",
                "options": ["A square", "An equilateral triangle", "A right-angled triangle", "A regular hexagon"],
                "ans": 1,
                "hint": "All nearest neighbor dots are at the exact same distance from each other.",
                "explanation": "Isometric dot grids are arranged so that every group of three adjacent dots forms an equilateral triangle.",
                "solution_html": make_sol_html([
                    "Examine the lattice structure of isometric dot paper.",
                    "The dots are arranged in staggered triangular rows where the spacing between any two adjacent dots is constant.",
                    "Connecting any three mutually adjacent dots creates three sides of equal length.",
                    "A triangle with three equal sides is an equilateral triangle with 60° internal angles."
                ], "Any three nearest adjacent dots form an equilateral triangle.")
            },
            {
                "q": "How many distinct valid 2D nets composed of 6 squares can fold into a closed 3D cube?",
                "options": ["8 nets", "9 nets", "11 nets", "14 nets"],
                "ans": 2,
                "hint": "Recall the classic hexomino folding theorems in geometry.",
                "explanation": "There are exactly 11 distinct arrangements of 6 connected squares that successfully fold into a complete closed cube.",
                "solution_html": make_sol_html([
                    "There are 35 distinct hexominoes (arrangements of 6 connected squares) in combinatorics.",
                    "When tested for 3D foldability into a hollow cube without overlaps or gaps:",
                    "Exactly 11 of these arrangements fold into a complete closed cube.",
                    "The remaining 24 arrangements produce overlapping faces or open sides."
                ], "There are exactly 11 valid cube nets.")
            },
            {
                "q": "Why does a flat net with two side flaps attached to the exact same edge fail to fold into a cube?",
                "options": ["It becomes too heavy", "The two flaps fold onto the exact same face, leaving an opposite face open", "It folds into a cone", "The paper shrinks"],
                "ans": 1,
                "hint": "Think about where the flaps land when folded 90 degrees.",
                "explanation": "Both flaps will land on the identical side, doubling up on one face while leaving the opposing face completely uncovered.",
                "solution_html": make_sol_html([
                    "Trace the fold sequence of the net along 90° creases.",
                    "If two flaps share the same hinge edge or fold along identical rotational paths, they occupy the exact same spatial plane in 3D.",
                    "This creates a double-layered wall on one face and leaves the opposite face with zero coverage.",
                    "Therefore, the solid cannot be closed."
                ], "The flaps overlap on one face, leaving an opposing face uncovered.")
            },
            {
                "q": "What is formed when two straight lines or rays meet at a shared point?",
                "options": ["A circumference", "An angle", "A diameter", "A perimeter"],
                "ans": 1,
                "hint": "The meeting point is called the vertex.",
                "explanation": "Two straight lines meeting at a common vertex form an angle.",
                "solution_html": make_sol_html([
                    "Review fundamental geometric definitions.",
                    "Two straight rays originating from or meeting at a common endpoint (vertex) define an angle.",
                    "The measure of the angle represents the amount of circular rotation between the two rays."
                ], "Two intersecting lines form an angle.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "questions": [
            {
                "q": "Does extending the drawn length of two rays forming an angle change the angle's measurement?",
                "options": ["Yes, longer rays make larger angles", "No, angle measurement depends only on the spread between rays", "Yes, it doubles the angle", "Only if measured with a ruler"],
                "ans": 1,
                "hint": "Angle is measured in degrees of circular turn, not centimeters of length.",
                "explanation": "The measure of an angle depends exclusively on the angular opening between the rays, completely independent of how long the rays are drawn.",
                "solution_html": make_sol_html([
                    "Understand how angles are quantified.",
                    "Angles measure rotational separation (degrees), not linear distance (centimeters).",
                    "Extending the rays simply extends the sides indefinitely into space without rotating them.",
                    "Since the amount of spread remains unchanged, the angle measure remains strictly identical."
                ], "Angle size depends only on the spread between rays, not line length.")
            },
            {
                "q": "What angle is created by folding a paper sheet in half and then in half again?",
                "options": ["An acute angle of 45°", "A right angle of 90°", "An obtuse angle of 120°", "A straight angle of 180°"],
                "ans": 1,
                "hint": "Think of the corner of a square or capital letter L.",
                "explanation": "Two perpendicular folds divide the 360° circle into four 90° quadrants, creating a right-angle corner.",
                "solution_html": make_sol_html([
                    "A flat unfolded plane around a point equals 360°.",
                    "Folding the sheet in half creates a straight line crease dividing 360° by 2 = 180°.",
                    "Folding the sheet in half a second time along that crease divides 180° by 2 = 90°.",
                    "The resulting folded corner is an exact 90° right angle."
                ], "Two successive perpendicular folds produce a 90° right angle.")
            },
            {
                "q": "Which angle type measures strictly less than 90°?",
                "options": ["Right angle", "Acute angle", "Obtuse angle", "Reflex angle"],
                "ans": 1,
                "hint": "Think of a sharp, pointed beak or letter V.",
                "explanation": "An acute angle is smaller and narrower than a 90° right angle.",
                "solution_html": make_sol_html([
                    "Review angle classification definitions:",
                    "Acute angle: 0° < angle < 90°.",
                    "Right angle: exactly 90°.",
                    "Obtuse angle: 90° < angle < 180°.",
                    "Therefore, an angle measuring strictly less than 90° is an acute angle."
                ], "An angle measuring less than 90° is an acute angle.")
            },
            {
                "q": "Which angle type measures greater than 90° but less than 180°?",
                "options": ["Acute angle", "Right angle", "Obtuse angle", "Zero angle"],
                "ans": 2,
                "hint": "Think of a wide, gently sloping roof or a reclining armchair.",
                "explanation": "An obtuse angle opens wider than a 90° right angle, measuring between 90° and 180°.",
                "solution_html": make_sol_html([
                    "Review angle classifications:",
                    "An angle that is wider and more open than a 90° square corner, but not yet flat (less than 180°), is classified as obtuse.",
                    "Its range is strictly between 90° and 180°."
                ], "An angle greater than 90° and less than 180° is an obtuse angle.")
            },
            {
                "q": "What type of angle is formed at the bottom vertex of the capital letter V?",
                "options": ["Right angle", "Acute angle", "Obtuse angle", "Straight angle"],
                "ans": 1,
                "hint": "Compare the opening of letter V with an L-shaped right angle.",
                "explanation": "The arms of the letter V meet at a sharp point narrower than an L-corner, making it an acute angle.",
                "solution_html": make_sol_html([
                    "Observe the geometry of the uppercase letter V.",
                    "The two slanted line segments converge downward to meet at a sharp bottom corner.",
                    "The opening spread is visibly narrower than a 90° perpendicular corner (letter L).",
                    "An angle narrower than 90° is an acute angle."
                ], "The letter V forms an acute angle at its bottom vertex.")
            },
            {
                "q": "Why does a 3-straw triangle keep its rigid shape when pushed, while a 4-straw quadrilateral wobbles?",
                "options": ["Because straws in triangles become heavier", "Because three side lengths permanently fix the three corner angles", "Because quadrilaterals have curved corners", "Because triangles have right angles"],
                "ans": 1,
                "hint": "Can you change the angles of a triangle without changing its side lengths?",
                "explanation": "By geometric congruence (SSS), three fixed side lengths determine unique fixed angles, making triangles inherently rigid.",
                "solution_html": make_sol_html([
                    "In a four-sided quadrilateral with hinged corners, the sides can pivot and shear into various parallelograms without changing side lengths.",
                    "In contrast, in a triangle, fixing the three side lengths fixes all three interior angles uniquely (SSS congruence theorem).",
                    "No corner can move without stretching or compressing the rigid straws.",
                    "Therefore, a triangle cannot deform and is structurally rigid."
                ], "Three side lengths permanently lock the three corner angles, providing structural rigidity.")
            },
            {
                "q": "How can an engineer make a wobbly rectangular bridge frame completely rigid?",
                "options": ["By making the sides longer", "By adding a diagonal brace that divides the rectangle into two triangles", "By removing two corners", "By heating the metal"],
                "ans": 1,
                "hint": "Turn the wobbly quadrilateral into rigid triangles.",
                "explanation": "Adding a diagonal strut splits the rectangle into two interconnected triangles, locking all angles and preventing distortion.",
                "solution_html": make_sol_html([
                    "A rectangular frame has 4 sides and flexible joints, which shear easily under lateral force.",
                    "Adding a diagonal strut creates two triangles sharing that common diagonal.",
                    "Since triangles are rigid structures that cannot deform without altering edge lengths, the entire assembly becomes completely rigid.",
                    "This principle is widely applied in truss bridges and crane booms."
                ], "Adding a diagonal brace creates two rigid triangles that lock the structure.")
            },
            {
                "q": "What is the curved boundary of a circle where every point is equidistant from a fixed center called?",
                "options": ["The diameter", "The circumference", "The radius", "The chord"],
                "ans": 1,
                "hint": "It is the perimeter or outer rim of the circle.",
                "explanation": "The outer curved boundary path of a circle is known as its circumference.",
                "solution_html": make_sol_html([
                    "Define the primary components of a circle:",
                    "Center: the fixed central anchor point.",
                    "Radius: distance from center to boundary.",
                    "Circumference: the complete outer curved boundary line surrounding the circle.",
                    "Diameter: line passing through center connecting two points on the circumference."
                ], "The outer curved boundary is called the circumference.")
            },
            {
                "q": "What is a straight line segment passing directly through the circle's center with both endpoints on the boundary called?",
                "options": ["Radius", "Diameter", "Arc", "Tangent"],
                "ans": 1,
                "hint": "It divides the circle into two matching semicircles.",
                "explanation": "The diameter is the longest straight line across a circle, passing through the central point.",
                "solution_html": make_sol_html([
                    "Examine lines inside a circle:",
                    "A line segment connecting two points on the circle's boundary that passes directly through the center point is defined as the diameter.",
                    "It divides the circular area into two congruent halves (semicircles)."
                ], "A line through the center connecting boundary points is the diameter.")
            },
            {
                "q": "If a circle has a radius of 15 cm, what is its diameter?",
                "options": ["7.5 cm", "20 cm", "30 cm", "45 cm"],
                "ans": 2,
                "hint": "Remember the formula: Diameter = 2 × Radius.",
                "explanation": "Diameter = 2 × Radius = 2 × 15 cm = 30 cm.",
                "solution_html": make_sol_html([
                    "Recall the relationship: Diameter (d) = 2 × Radius (r).",
                    "Given: r = 15 cm.",
                    "Compute: d = 2 × 15 cm = 30 cm."
                ], "The diameter of the circle is 30 cm.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "questions": [
            {
                "q": "If a circular bicycle wheel has a diameter of 42 cm, what is its radius?",
                "options": ["84 cm", "42 cm", "21 cm", "14 cm"],
                "ans": 2,
                "hint": "Radius is half of the diameter: Radius = Diameter ÷ 2.",
                "explanation": "Radius = Diameter ÷ 2 = 42 cm ÷ 2 = 21 cm.",
                "solution_html": make_sol_html([
                    "State the radius formula: Radius (r) = Diameter (d) ÷ 2.",
                    "Given diameter: d = 42 cm.",
                    "Compute: r = 42 ÷ 2 = 21 cm."
                ], "The radius is 21 cm.")
            },
            {
                "q": "What are multiple circles of different radii that all share the exact same central point called?",
                "options": ["Concentric circles", "Eccentric circles", "Parallel circles", "Intersecting circles"],
                "ans": 0,
                "hint": "They look like archery target rings or ripples on a pond.",
                "explanation": "Circles of different sizes having the same center point are called concentric circles.",
                "solution_html": make_sol_html([
                    "Review circle terminology.",
                    "Circles that share a common center point are termed 'concentric' (meaning having a common center).",
                    "They do not intersect and form nested rings, such as archery targets or tree rings."
                ], "Circles sharing the same center are called concentric circles.")
            },
            {
                "q": "When using a geometric compass to draw a circle, what controls the radius of the drawn circle?",
                "options": ["The sharpness of the pencil", "The spread distance between the metal needle and the pencil tip", "The speed of rotation", "The color of the lead"],
                "ans": 1,
                "hint": "Measure the opening between the needle and pencil with a ruler.",
                "explanation": "The distance between the fixed needle pivot and the pencil point directly sets the radius.",
                "solution_html": make_sol_html([
                    "Understand how a compass operates.",
                    "The metal needle stays fixed at the center point.",
                    "The pencil tip rotates around this pivot, maintaining a constant distance.",
                    "That distance between needle and pencil tip is precisely the radius of the circle."
                ], "The spread distance between the needle and pencil tip sets the radius.")
            },
            {
                "q": "By stepping the compass radius around the circumference of a circle, how many petals are formed in a floral rosette?",
                "options": ["4 petals", "5 petals", "6 petals", "8 petals"],
                "ans": 2,
                "hint": "A circle's radius fits into its circumference exactly 6 times (6 × 60° = 360°).",
                "explanation": "Stepping the radius around a circle divides the 360° circle into six 60° arcs, creating a 6-petalled flower.",
                "solution_html": make_sol_html([
                    "In geometry, the side length of a regular inscribed hexagon equals the radius of the circle.",
                    "Stepping the compass around the boundary with radius unchanged marks exactly 6 points.",
                    "Drawing arcs from these 6 vertices through the center creates a symmetric 6-petalled rosette."
                ], "Exactly 6 petals are formed in the floral rosette.")
            },
            {
                "q": "What happens to the total surface area of a polygon when it is cut apart and rearranged into a new shape?",
                "options": ["It increases", "It decreases", "It remains exactly conserved and unchanged", "It depends on the color"],
                "ans": 2,
                "hint": "No pieces are added or removed during dissection.",
                "explanation": "Geometric dissection rearranges the same surface pieces, so total area is strictly conserved.",
                "solution_html": make_sol_html([
                    "Examine the conservation of area principle in geometry.",
                    "Dissecting a shape cuts it into a finite set of smaller pieces.",
                    "Rearranging these pieces without overlapping them preserves the sum of their individual areas.",
                    "Total area of new shape = Total area of original pieces."
                ], "Total surface area remains strictly conserved and unchanged.")
            },
            {
                "q": "In a geometric dissection puzzle, a large triangle is divided into a central square and how many smaller triangles?",
                "options": ["1 triangle", "2 smaller triangles", "3 smaller triangles", "4 smaller triangles"],
                "ans": 1,
                "hint": "The square sits at the base, leaving one triangle on top and one or two flanking wings.",
                "explanation": "A triangle can be dissected into a central square and 2 smaller right-angled triangles flanking its sides.",
                "solution_html": make_sol_html([
                    "Examine the classic triangle-to-square dissection problem.",
                    "An isosceles or right triangle can have a square inscribed on its base.",
                    "The remaining negative space decomposes into 2 smaller flanking right triangles.",
                    "Together, 1 central square + 2 smaller triangles equal the full original triangle."
                ], "The triangle is divided into 1 square and 2 smaller triangles.")
            },
            {
                "q": "A student sorts 2D polygon cards into groups by number of sides. Which polygon has exactly 6 straight sides?",
                "options": ["Pentagon", "Hexagon", "Heptagon", "Octagon"],
                "ans": 1,
                "hint": "Hexa- is the Greek prefix for six.",
                "explanation": "A polygon with 6 straight sides and 6 vertices is a hexagon.",
                "solution_html": make_sol_html([
                    "Review polygon naming based on side counts:",
                    "3 sides = Triangle.",
                    "4 sides = Quadrilateral.",
                    "5 sides = Pentagon.",
                    "6 sides = Hexagon.",
                    "8 sides = Octagon."
                ], "A hexagon has exactly 6 straight sides.")
            },
            {
                "q": "How many matchsticks (edges) and clay connector balls (vertices) are required to build a triangular pyramid skeleton?",
                "options": ["4 matchsticks, 4 clay balls", "6 matchsticks, 4 clay balls", "8 matchsticks, 5 clay balls", "12 matchsticks, 8 clay balls"],
                "ans": 1,
                "hint": "The base is a triangle (3 matchsticks, 3 balls), and 3 matchsticks rise to 1 top ball.",
                "explanation": "A triangular pyramid (tetrahedron) has 6 edges (matchsticks) and 4 vertices (clay balls).",
                "solution_html": make_sol_html([
                    "Construct the skeleton frame:",
                    "Base: 3 matchsticks joined by 3 clay balls to form a flat triangle.",
                    "Apex: 1 clay ball positioned above the center.",
                    "Lateral edges: 3 matchsticks connecting the 3 base balls to the single apex ball.",
                    "Total matchsticks (edges) = 3 + 3 = 6.",
                    "Total clay balls (vertices) = 3 + 1 = 4."
                ], "A triangular pyramid skeleton requires 6 matchsticks and 4 clay balls.")
            },
            {
                "q": "In a spider web, what are the straight silk lines radiating from the center like wheel spokes called?",
                "options": ["Concentric spiral threads", "Radial threads", "Curved anchor loops", "Zigzag border cords"],
                "ans": 1,
                "hint": "They radiate outward along radii from the center hub.",
                "explanation": "Radial threads provide the structural framework radiating straight outward from the spider web's central hub.",
                "solution_html": make_sol_html([
                    "Analyze the architecture of an orb spider web:",
                    "1. Radial threads: straight structural lines radiating outward from the central hub like wheel spokes.",
                    "2. Spiral threads: concentric or spiraling sticky capture lines linking adjacent radial threads.",
                    "The straight outward lines are radial threads."
                ], "The straight lines radiating from the center are radial threads.")
            },
            {
                "q": "What is the universal relationship between the number of straight sides (n) and the number of interior angles in any polygon?",
                "options": ["Number of angles = n - 2", "Number of angles = n", "Number of angles = 2n", "Number of angles = n + 2"],
                "ans": 1,
                "hint": "A triangle has 3 sides and 3 angles. A quadrilateral has 4 sides and 4 angles.",
                "explanation": "In every closed plane polygon, the number of interior angles is always equal to the number of straight sides: n sides = n angles.",
                "solution_html": make_sol_html([
                    "Examine polygons with varying side counts:",
                    "Triangle: 3 sides, 3 angles.",
                    "Quadrilateral: 4 sides, 4 angles.",
                    "Pentagon: 5 sides, 5 angles.",
                    "Hexagon: 6 sides, 6 angles.",
                    "Decagon: 10 sides, 10 angles.",
                    "In every closed polygon, each pair of adjacent sides meets at exactly one vertex to form one interior angle.",
                    "Therefore, for any n-sided polygon, Number of angles = n."
                ], "In any polygon, the number of interior angles equals the number of sides (n sides = n angles).")
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part3:
        title_wc = len(s['title'].split())
        print(f"Slide {s['id']}: '{s['title']}' ({len(s['questions'])} questions)")
        assert 1 <= title_wc <= 3, f"Title length violation in slide {s['id']}"
        assert len(s['questions']) == 10, f"Expected 10 questions in slide {s['id']}"
        for q in s['questions']:
            assert len(q['options']) == 4
            assert 0 <= q['ans'] <= 3
            assert q['hint']
            assert q['explanation']
            assert q['solution_html']
    print("Part 3: All 4 challenge slides (40 questions) verified successfully!")
