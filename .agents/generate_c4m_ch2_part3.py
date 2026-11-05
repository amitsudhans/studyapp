# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 2: Hide and Seek - Part 3 (Slides 17 to 20)
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
                "q": "Why can an observer perched high up in a tree see someone hiding behind a low wall?",
                "options": ["Because tree leaves are transparent", "Because the elevated vantage point provides a clear line of sight over the obstacle", "Because sound travels faster from trees", "Because low walls disappear from above"],
                "ans": 1,
                "hint": "Think about how light travels in straight lines from an elevated position.",
                "explanation": "An elevated vantage point allows the observer's line of sight to travel over the top of low obstacles, eliminating ground blind spots.",
                "solution_html": make_sol_html([
                    "Light travels in straight lines through space.",
                    "An observer on the ground has their horizontal sight line blocked by a vertical wall.",
                    "An elevated observer in a tree looks downward at an angle, creating a line of sight that clears the wall's top edge.",
                    "Therefore, the area behind the low wall becomes directly visible from above."
                ], "An elevated vantage point provides an unobstructed line of sight over low obstacles.")
            },
            {
                "q": "What creates a blind spot for an observer during a game of hide and seek?",
                "options": ["Open flat grass", "Opaque obstacles that block straight lines of sight", "Bright daylight", "Clear glass windows"],
                "ans": 1,
                "hint": "Consider what happens when light cannot pass through an object.",
                "explanation": "Solid, opaque obstacles block the straight path of light, creating an invisible zone behind them called a blind spot.",
                "solution_html": make_sol_html([
                    "Understand how human vision functions: light reflected from an object must reach the observer's eyes in a straight line.",
                    "Opaque materials (like brick walls, wooden fences, and tree trunks) absorb or reflect light and cannot be seen through.",
                    "The geometric region behind the opaque obstacle where light cannot travel directly to the observer is a blind spot."
                ], "Opaque obstacles block straight lines of sight, creating blind spots.")
            },
            {
                "q": "What are the three primary orthogonal view angles used in engineering and design?",
                "options": ["Inside, outside, through", "Top view, front view, side view", "Left diagonal, right diagonal, center", "North, south, east"],
                "ans": 1,
                "hint": "Think of looking from directly above, straight ahead, and from the flank.",
                "explanation": "The three standard orthogonal projections are the top view (plan), front view (front elevation), and side view (side elevation).",
                "solution_html": make_sol_html([
                    "Review 3D orthogonal projection principles in mathematics and engineering.",
                    "To completely describe a 3D solid on 2D planes, observers project views along three mutually perpendicular axes:",
                    "1. Top view: viewed perpendicularly from directly above.",
                    "2. Front view: viewed perpendicularly from the front face.",
                    "3. Side view: viewed perpendicularly from the side profile."
                ], "The 3 standard views are Top view, Front view, and Side view.")
            },
            {
                "q": "When looking directly down at a building brick lying flat on a table, which view is observed?",
                "options": ["Front view", "Side view", "Top view", "Bottom view"],
                "ans": 2,
                "hint": "You are looking from above like a bird flying overhead.",
                "explanation": "Looking directly downward from above onto a horizontal object reveals its top view.",
                "solution_html": make_sol_html([
                    "Identify the observer's viewing orientation relative to the object.",
                    "The observer is positioned directly above the object, looking vertically down at a 90° angle to the table.",
                    "This overhead perspective is defined as the top view (or bird's-eye view)."
                ], "Looking straight down from above reveals the Top View.")
            },
            {
                "q": "Which 2D shape is observed when looking at a flat-screen television from directly overhead (top view)?",
                "options": ["A large square", "A very thin, narrow rectangle", "A circle", "A triangle"],
                "ans": 1,
                "hint": "Modern televisions are very thin in depth compared to their screen width.",
                "explanation": "A modern TV is wide but very thin; viewed from above, it appears as a long, narrow rectangular strip.",
                "solution_html": make_sol_html([
                    "Analyze the 3D dimensions of a modern flat-panel TV:",
                    "Height: tall (visible in front view). Width: wide (visible in front view). Depth/thickness: very thin.",
                    "When viewed directly from above, height is eliminated, showing only width and depth.",
                    "A wide width combined with a very thin depth forms a narrow, slender rectangle."
                ], "The top view of a flat-screen TV is a thin, narrow rectangle.")
            },
            {
                "q": "Which view of a yellow school bus displays the full row of passenger windows and two wheels along the ground?",
                "options": ["Top view", "Front view", "Side view", "Underneath view"],
                "ans": 2,
                "hint": "Think of standing on the sidewalk watching the bus drive past.",
                "explanation": "The side view of a bus stretches horizontally, displaying the entire row of passenger windows and the wheels.",
                "solution_html": make_sol_html([
                    "Examine the features of a bus along different view axes:",
                    "Front view shows headlights, front windshield, and bumper.",
                    "Top view shows the flat roof and emergency escape hatch.",
                    "Side view shows the full length of the vehicle, the line of passenger windows, side doors, and wheels along the ground."
                ], "The side view shows the line of windows and wheels.")
            },
            {
                "q": "Which 3D solid produces identical square silhouettes from its top view, front view, and side view?",
                "options": ["A cylinder", "A cube", "A triangular prism", "A sphere"],
                "ans": 1,
                "hint": "All six faces of this solid are congruent squares.",
                "explanation": "Because a cube has six identical square faces meeting at 90°, all three orthogonal projections are identical squares.",
                "solution_html": make_sol_html([
                    "Evaluate the symmetry of a cube (regular hexahedron):",
                    "Width = Height = Depth = s (equal side lengths).",
                    "Front projection (width × height) = square of side s.",
                    "Side projection (depth × height) = square of side s.",
                    "Top projection (width × depth) = square of side s.",
                    "All three orthogonal views are congruent squares."
                ], "A cube produces identical square silhouettes from all three views.")
            },
            {
                "q": "What 2D shape is seen in the front view of a triangular prism resting on its rectangular face?",
                "options": ["A circle", "A triangle", "A hexagon", "A square"],
                "ans": 1,
                "hint": "Look directly at the triangular base end.",
                "explanation": "The front end face of a triangular prism is an upright triangle.",
                "solution_html": make_sol_html([
                    "A triangular prism consists of 2 identical triangular bases and 3 rectangular lateral faces.",
                    "When positioned with a rectangular face on the ground and viewing directly from the triangular end:",
                    "The projection onto a perpendicular vertical plane is a triangle."
                ], "The front view of a triangular prism is a triangle.")
            },
            {
                "q": "Looking from directly above at an upright square pyramid, what pattern is observed?",
                "options": ["A plain circle", "A square containing diagonal lines meeting at a central point", "A single straight line", "A rectangle with two circles"],
                "ans": 1,
                "hint": "The square base forms the outline, and the 4 sloping triangular faces form diagonal crease lines meeting at the apex.",
                "explanation": "The top view shows the square base boundary with four diagonal edges converging at the central top apex point.",
                "solution_html": make_sol_html([
                    "Examine a square pyramid from directly overhead (top view):",
                    "1. The outer perimeter matches the square base boundary.",
                    "2. The 4 sloping lateral edges converge from the four base corners to the apex situated above the center.",
                    "3. Projecting these edges straight down produces two diagonal lines connecting opposite corners through the center."
                ], "A square containing diagonal lines meeting at the central apex point.")
            },
            {
                "q": "What 2D shape is observed when looking from directly above at an upright solid cylinder?",
                "options": ["A rectangle", "A circle", "A triangle", "An ellipse"],
                "ans": 1,
                "hint": "The top face of a cylinder is a circular lid.",
                "explanation": "Looking directly down at an upright cylinder reveals its flat circular top base.",
                "solution_html": make_sol_html([
                    "An upright cylinder has a circular top base, a circular bottom base, and a vertical curved wall.",
                    "When viewed directly from above, vertical height is eliminated.",
                    "The projection shows only the circular top boundary face: a circle."
                ], "The top view of an upright cylinder is a circle.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "questions": [
            {
                "q": "What standard 3D geometric solid is an individual empty matchbox shaped like?",
                "options": ["A sphere", "A rectangular cuboid", "A cone", "A triangular pyramid"],
                "ans": 1,
                "hint": "It has 6 flat rectangular faces, 12 straight edges, and 8 vertices.",
                "explanation": "A matchbox has six rectangular faces and right-angled corners, making it a classic cuboid.",
                "solution_html": make_sol_html([
                    "Count and analyze the geometric elements of an empty matchbox:",
                    "Faces: 6 flat rectangular surfaces.",
                    "Edges: 12 straight line-segment boundaries.",
                    "Vertices: 8 corner points where three edges meet at 90°.",
                    "This geometric definition precisely characterizes a rectangular cuboid."
                ], "A matchbox is a rectangular cuboid.")
            },
            {
                "q": "Why must every upper matchbox in a stepped tower rest upon solid blocks beneath it?",
                "options": ["To make the tower lighter", "Because gravity requires physical support beneath elevated masses to prevent collapse", "To turn the cuboids into cubes", "To hide the colors"],
                "ans": 1,
                "hint": "Think about why blocks cannot float in mid-air.",
                "explanation": "Under gravity, any unsupported elevated block will tip and fall; stable structures require continuous foundation support beneath.",
                "solution_html": make_sol_html([
                    "Analyze physical structural equilibrium and gravitational load paths:",
                    "Downward gravitational force pulls on every mass in the structure.",
                    "Without a solid reaction surface directly beneath its center of mass, an upper block experiences an unbalanced tipping torque.",
                    "Continuous lower support blocks provide the normal contact force required for equilibrium."
                ], "Gravity requires continuous support beneath elevated blocks to prevent collapse.")
            },
            {
                "q": "What essential geometric dimension of a block building completely disappears in its overhead top view?",
                "options": ["Its horizontal width", "Its vertical height", "Its footprint perimeter", "Its horizontal depth"],
                "ans": 1,
                "hint": "Looking straight down from above compresses the vertical axis.",
                "explanation": "An overhead top view flattens the vertical dimension, showing only horizontal width and depth footprints.",
                "solution_html": make_sol_html([
                    "In orthogonal projection, viewing an object along the z-axis (vertical) projects points onto the horizontal x-y plane.",
                    "Differences in vertical elevation (z-coordinates) are projected onto the exact same planar points.",
                    "Therefore, the vertical height information disappears in a pure top view."
                ], "Vertical height disappears in an overhead top view.")
            },
            {
                "q": "How does the back view of an asymmetrical stepped block structure compare to its front view?",
                "options": ["It looks completely identical in every way", "The left-to-right positions of the vertical columns are reversed", "The building appears twice as high", "All straight edges become curved"],
                "ans": 1,
                "hint": "Imagine walking 180 degrees around to the rear of the building.",
                "explanation": "Viewing a structure from the opposite side reverses the left and right positions of asymmetrical columns.",
                "solution_html": make_sol_html([
                    "Observe an asymmetrical building with a tall column on the left and a short column on the right in front view.",
                    "When the observer walks around to the back (180° rotation around the vertical axis):",
                    "The tall column is now on the observer's right, and the short column is on the observer's left.",
                    "Thus, the left-to-right column order is horizontally reversed."
                ], "Left-to-right column positions are horizontally reversed in the back view.")
            },
            {
                "q": "Why is an elevated classroom window sill a superior vantage point for surveying the room?",
                "options": ["Because windows make desks transparent", "Because the elevated angle provides an unobstructed line of sight over desk rows", "Because sound is quieter near windows", "Because desks turn into circles"],
                "ans": 1,
                "hint": "Consider how looking downward avoids having near desks block far desks.",
                "explanation": "An elevated position looks downward over desk tops, preventing front furniture from blocking the sight line to rear desks.",
                "solution_html": make_sol_html([
                    "When viewing at floor eye level, the first row of desks obstructs the view of the second and third rows.",
                    "An elevated vantage point (like a high window sill or cat perch) angles the line of sight downward.",
                    "This vertical sight angle clears the tops of foreground desks, revealing the entire floor layout."
                ], "The elevated angle provides an unobstructed line of sight over desk rows.")
            },
            {
                "q": "What is a 2D classroom floor plan?",
                "options": ["A painting of the ceiling", "An overhead top-down map showing the arrangement of desks, boards, and doors", "A photograph of the floor tiles only", "A list of homework questions"],
                "ans": 1,
                "hint": "It is a bird's-eye architectural blueprint of the room.",
                "explanation": "A floor plan is a scaled 2D top-down diagram showing the locations of furniture, walkways, and boundaries.",
                "solution_html": make_sol_html([
                    "Define an architectural floor plan:",
                    "It is a 2D orthogonal top-down projection of a room.",
                    "It depicts walls, windows, doorways, desks, chalkboard, and pathways in their correct relative spatial positions."
                ], "An overhead top-down map showing furniture, doors, and pathways.")
            },
            {
                "q": "Why do mathematicians use standardized row and column numbers to describe desk locations?",
                "options": ["To make the classroom look larger", "To specify exact, unambiguous locations that anyone can identify reliably", "To confuse visitors", "To reduce the number of chairs"],
                "ans": 1,
                "hint": "Coordinates leave no room for misunderstanding.",
                "explanation": "Row and column coordinates provide unique, objective spatial addresses that prevent confusion.",
                "solution_html": make_sol_html([
                    "Vague qualitative terms like 'near the front' or 'over there' depend on where the speaker is standing.",
                    "Row numbers (horizontal depth from front) and Column numbers (horizontal position across) establish an invariant coordinate frame.",
                    "Every desk receives a unique, objective address that anyone can locate without ambiguity."
                ], "To specify exact, unambiguous locations that anyone can identify reliably.")
            },
            {
                "q": "In a classroom where the first row is closest to the chalkboard, where is 'the third desk in the first row' located?",
                "options": ["In the back-left corner", "In the row nearest to the board, counting three desks from the left", "In the middle of the third row", "Outside in the hallway"],
                "ans": 1,
                "hint": "Row 1 is at the front; count three desks along that row from the left.",
                "explanation": "The first row is at the front of the room, and the third desk is found by counting three seats inward from the left side.",
                "solution_html": make_sol_html([
                    "Parse the positional descriptor:",
                    "1. 'First row': the horizontal line of desks closest to the front chalkboard.",
                    "2. 'Third desk': starting from the left-hand aisle of that first row, count 1, 2, 3 desks.",
                    "This identifies the third desk from the left in the very front row."
                ], "The third desk from the left in the row closest to the front board.")
            },
            {
                "q": "In a 3×3 desk arrangement (3 rows and 3 columns), which desk sits at the exact center?",
                "options": ["First desk of first row", "Third desk of third row", "Middle desk of second row", "First desk of second row"],
                "ans": 2,
                "hint": "The middle of 3 is 2.",
                "explanation": "The center desk lies in the second row (vertically centered) and second column (horizontally centered).",
                "solution_html": make_sol_html([
                    "In a 3-element sequence (1, 2, 3), the central element is 2.",
                    "Central row = Row 2 (the second row).",
                    "Central column = Column 2 (the middle desk of that row).",
                    "Therefore, the center desk is the middle desk of the second row."
                ], "The middle desk of the second row.")
            },
            {
                "q": "What ordinal numbering term describes the row positioned immediately behind the first row?",
                "options": ["The third row", "The second row", "The fifth row", "The zero row"],
                "ans": 1,
                "hint": "After first comes second.",
                "explanation": "The sequential ordinal following first is second.",
                "solution_html": make_sol_html([
                    "Review standard ordinal number sequence:",
                    "First (1st) ➔ Second (2nd) ➔ Third (3rd) ➔ Fourth (4th).",
                    "The row immediately following the first row is the second row."
                ], "The second row.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "questions": [
            {
                "q": "How many total compartments (cells) are there in a standard 3×3 grid system?",
                "options": ["6 cells", "8 cells", "9 cells", "12 cells"],
                "ans": 2,
                "hint": "Multiply the number of rows by the number of columns: 3 × 3.",
                "explanation": "A 3×3 grid contains 3 rows with 3 cells in each row: 3 × 3 = 9 cells in total.",
                "solution_html": make_sol_html([
                    "Use the multiplication rule for rectangular arrays:",
                    "Number of horizontal rows = 3.",
                    "Number of vertical columns = 3.",
                    "Total cells = Rows × Columns = 3 × 3 = 9 cells."
                ], "A 3×3 grid contains 9 total cells.")
            },
            {
                "q": "What are the exact row and column coordinates of the central cell in a 3×3 grid?",
                "options": ["Row 1, Column 1", "Row 3, Column 3", "Row 2, Column 2", "Row 1, Column 3"],
                "ans": 2,
                "hint": "It is in the second row and second column.",
                "explanation": "Row 2 is the middle horizontal layer, and Column 2 is the middle vertical column; their intersection is the center.",
                "solution_html": make_sol_html([
                    "Identify the central indices of a 3×3 matrix:",
                    "Rows: 1 (top), 2 (middle), 3 (bottom). Center row = 2.",
                    "Columns: 1 (left), 2 (middle), 3 (right). Center column = 2.",
                    "The intersection coordinate is Row 2, Column 2."
                ], "The central cell is Row 2, Column 2.")
            },
            {
                "q": "Which coordinate pair identifies the top-left corner compartment of a 3×3 grid?",
                "options": ["Row 1, Column 1", "Row 1, Column 3", "Row 3, Column 1", "Row 3, Column 3"],
                "ans": 0,
                "hint": "Top row is Row 1; leftmost column is Column 1.",
                "explanation": "Row 1 represents the top horizontal band, and Column 1 represents the leftmost vertical column.",
                "solution_html": make_sol_html([
                    "Locate the top-left boundary of the grid:",
                    "Top row = Row 1.",
                    "Left column = Column 1.",
                    "The top-left corner cell is Row 1, Column 1."
                ], "The top-left corner is Row 1, Column 1.")
            },
            {
                "q": "Which coordinate pair identifies the bottom-right corner compartment of a 3×3 grid?",
                "options": ["Row 1, Column 1", "Row 3, Column 1", "Row 1, Column 3", "Row 3, Column 3"],
                "ans": 3,
                "hint": "Bottom row is Row 3; rightmost column is Column 3.",
                "explanation": "Row 3 represents the bottom row, and Column 3 represents the rightmost column.",
                "solution_html": make_sol_html([
                    "Locate the bottom-right boundary of the grid:",
                    "Bottom row = Row 3.",
                    "Right column = Column 3.",
                    "The bottom-right corner cell is Row 3, Column 3."
                ], "The bottom-right corner is Row 3, Column 3.")
            },
            {
                "q": "If a clue instructs: 'Place a ripe apple at Row 2, Column 2', where should it be drawn?",
                "options": ["In the top-right corner", "At the exact center of the grid", "In the bottom-left corner", "Outside the grid border"],
                "ans": 1,
                "hint": "Row 2 and Column 2 intersect at the middle.",
                "explanation": "Row 2 is the middle row, and Column 2 is the middle column, so Row 2, Column 2 is the exact center.",
                "solution_html": make_sol_html([
                    "Find the intersection of Row 2 and Column 2:",
                    "Row 2 lies between Row 1 (top) and Row 3 (bottom).",
                    "Column 2 lies between Column 1 (left) and Column 3 (right).",
                    "The cell at (2, 2) is the exact center of the 3×3 grid."
                ], "At the exact center of the grid.")
            },
            {
                "q": "What rule governs valid moves in an orthogonal grid treasure hunt game?",
                "options": ["Players may jump diagonally across corners", "Players must move only Up, Down, Left, or Right along grid lines", "Players can teleport anywhere", "Players must only move backward"],
                "ans": 1,
                "hint": "Orthogonal means perpendicular: no diagonal steps allowed.",
                "explanation": "In an orthogonal grid game, movements are strictly confined to perpendicular directions: Up, Down, Left, or Right.",
                "solution_html": make_sol_html([
                    "Review orthogonal motion rules:",
                    "A valid step changes either the row index by ±1 OR the column index by ±1.",
                    "Changing both row and column simultaneously is a diagonal jump, which is disallowed.",
                    "Therefore, only Up, Down, Left, and Right moves are permitted."
                ], "Players must move only Up, Down, Left, or Right along grid lines.")
            },
            {
                "q": "Why are diagonal moves across cell corners prohibited in street grid navigation?",
                "options": ["Because streets are painted green", "Because real buildings, walls, and city blocks block diagonal cutting", "Because diagonal lines are invisible", "Because clocks run clockwise"],
                "ans": 1,
                "hint": "You cannot walk straight through a solid brick building on a city corner.",
                "explanation": "Real streets and hallways are laid out on perpendicular axes; you cannot cut diagonally through solid buildings.",
                "solution_html": make_sol_html([
                    "In physical urban architecture and corridor layouts, blocks of buildings occupy the interior space of corners.",
                    "Pedestrians and vehicles must follow the perimeter sidewalks and roadways along perpendicular axes.",
                    "Cutting diagonally would require walking through solid walls or private property."
                ], "Real buildings, walls, and city blocks block diagonal paths.")
            },
            {
                "q": "Starting at Row 4, Column 1 on a 4×4 grid, moving 2 steps Up and 3 steps Right lands on which cell?",
                "options": ["Row 2, Column 4", "Row 1, Column 3", "Row 3, Column 4", "Row 2, Column 3"],
                "ans": 0,
                "hint": "Subtract 2 from Row 4 (going up); add 3 to Column 1 (going right).",
                "explanation": "Moving Up 2 steps: 4 - 2 = Row 2. Moving Right 3 steps: 1 + 3 = Column 4. Landing cell is Row 2, Column 4.",
                "solution_html": make_sol_html([
                    "Calculate row shift: moving Up decreases row number from bottom to top.",
                    "Starting Row = 4. 2 steps Up: 4 - 2 = Row 2.",
                    "Calculate column shift: moving Right increases column number from left to right.",
                    "Starting Column = 1. 3 steps Right: 1 + 3 = Column 4.",
                    "Final coordinate cell = Row 2, Column 4."
                ], "The explorer lands on Row 2, Column 4.")
            },
            {
                "q": "What is the total Manhattan distance (grid step count) from Row 4, Column 1 to Row 1, Column 3?",
                "options": ["4 steps", "5 steps", "6 steps", "7 steps"],
                "ans": 1,
                "hint": "Count vertical steps (4 to 1) plus horizontal steps (1 to 3).",
                "explanation": "Vertical steps: 4 - 1 = 3 steps Up. Horizontal steps: 3 - 1 = 2 steps Right. Total steps = 3 + 2 = 5 steps.",
                "solution_html": make_sol_html([
                    "State the Manhattan distance formula: d = |Row₁ - Row₂| + |Col₁ - Col₂|.",
                    "Vertical distance = |4 - 1| = 3 steps.",
                    "Horizontal distance = |1 - 3| = 2 steps.",
                    "Total step count = 3 + 2 = 5 steps."
                ], "Total distance is 5 steps.")
            },
            {
                "q": "On a grid path, does walking 2 steps Right then 3 steps Up require the same number of steps as walking 3 steps Up then 2 steps Right?",
                "options": ["No, Right first is longer", "No, Up first is shorter", "Yes, both paths require exactly 5 steps", "It depends on the time of day"],
                "ans": 2,
                "hint": "Addition is commutative: 2 + 3 = 3 + 2.",
                "explanation": "The order of orthogonal movements does not change the total sum: 2 + 3 = 3 + 2 = 5 steps.",
                "solution_html": make_sol_html([
                    "Path A: 2 steps Right + 3 steps Up = 2 + 3 = 5 steps.",
                    "Path B: 3 steps Up + 2 steps Right = 3 + 2 = 5 steps.",
                    "By the commutative property of addition (a + b = b + a), both paths have identical total step counts."
                ], "Yes, both paths require exactly 5 steps.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "questions": [
            {
                "q": "How do sloping pitched roofs of school buildings appear in an overhead top-down drone photograph?",
                "options": ["As pointed pyramids only", "As flat 2D geometric rectangles", "As wavy circular ribbons", "As vertical lines"],
                "ans": 1,
                "hint": "Viewed directly from above, sloping planes project onto horizontal flat rectangles.",
                "explanation": "Looking straight down perpendicularly flattens the slope, projecting the roof slopes as 2D flat rectangles.",
                "solution_html": make_sol_html([
                    "Examine the orthogonal projection of a pitched roof:",
                    "A pitched roof has two inclined rectangular surfaces meeting at a central horizontal ridge line.",
                    "When viewed directly from above (drone camera pointing straight down):",
                    "The inclined surfaces project onto the horizontal plane as adjacent flat 2D rectangles sharing the ridge seam."
                ], "Pitched roofs appear as flat 2D geometric rectangles.")
            },
            {
                "q": "How does a circular concrete flagpole pedestal appear in an aerial top-down drone photograph?",
                "options": ["As a flat circle", "As a tall triangle", "As an irregular hexagon", "As a straight vertical line"],
                "ans": 0,
                "hint": "The top profile of a cylinder or circular pedestal is round.",
                "explanation": "A circular pedestal viewed perpendicularly from directly above appears as a flat, geometric circle.",
                "solution_html": make_sol_html([
                    "A cylindrical pedestal has a circular cross-section.",
                    "An aerial camera looking straight down captures the horizontal perimeter of the pedestal.",
                    "This projection forms a flat, geometric 2D circle."
                ], "A circular flagpole base appears as a flat circle.")
            },
            {
                "q": "Why are vertical building walls mostly invisible in a direct top-down aerial photograph?",
                "options": ["Because walls are made of glass", "Because walls run parallel to the camera's sight line and hide beneath roof eaves", "Because walls shrink in the sun", "Because drones fly too fast"],
                "ans": 1,
                "hint": "Roof edges project outward past the walls, covering them from above.",
                "explanation": "Vertical walls run parallel to a downward sight line and are covered by the building's overhanging roofline.",
                "solution_html": make_sol_html([
                    "The camera sight line is perpendicular to the ground (straight down).",
                    "Vertical walls lie parallel to this sight line, collapsing to negligible projected thickness.",
                    "Furthermore, building roofs typically overhang past the walls (eaves), completely concealing the walls beneath."
                ], "Walls run parallel to the downward sight line and hide beneath roof eaves.")
            },
            {
                "q": "What is the primary purpose of a school campus blueprint?",
                "options": ["To list cafeteria recipes", "To provide a structured 2D map showing the spatial layout of all campus buildings and paths", "To count the number of windows", "To show the color of school uniforms"],
                "ans": 1,
                "hint": "Blueprints help people navigate and understand where rooms are located.",
                "explanation": "A campus blueprint maps out the relative locations, corridors, rooms, and outdoor zones across the school grounds.",
                "solution_html": make_sol_html([
                    "Define a campus blueprint:",
                    "It is a 2D architectural site plan representing the entire school layout.",
                    "It clearly labels classrooms, library, playground, medical room, stage, and corridors so visitors and students can navigate easily."
                ], "To provide a structured 2D map showing the spatial layout of all campus facilities.")
            },
            {
                "q": "Where is the main entrance gate situated on a standard school campus site map?",
                "options": ["On the classroom roof", "At the boundary baseline where visitors enter the grounds", "Inside the library bookshelf", "Under the performance stage"],
                "ans": 1,
                "hint": "It is at the perimeter boundary where access begins.",
                "explanation": "The main entrance gate is located at the perimeter boundary baseline where travelers enter the campus.",
                "solution_html": make_sol_html([
                    "On architectural site plans, the entrance gate represents the point of ingress.",
                    "It is positioned along the outer perimeter boundary baseline, serving as the starting waypoint for campus navigation."
                ], "At the boundary baseline where visitors enter the grounds.")
            },
            {
                "q": "Route A from the classroom to the stage is 60 meters. Route B around the playground is 95 meters. Which route is shorter and by how much?",
                "options": ["Route B is shorter by 35 m", "Route A is shorter by 35 m", "Both routes are equal", "Route A is shorter by 25 m"],
                "ans": 1,
                "hint": "Subtract: 95 m - 60 m = 35 m.",
                "explanation": "Route A (60 m) is shorter than Route B (95 m) by 95 - 60 = 35 meters.",
                "solution_html": make_sol_html([
                    "Compare route distances:",
                    "Distance of Route A = 60 meters.",
                    "Distance of Route B = 95 meters.",
                    "Difference = 95 - 60 = 35 meters.",
                    "Route A is shorter by 35 meters."
                ], "Route A is shorter by 35 meters.")
            },
            {
                "q": "Why is choosing the shortest route between school facilities beneficial?",
                "options": ["It increases walking time", "It minimizes travel distance, saving time and physical effort", "It makes backpacks heavier", "It skips math class"],
                "ans": 1,
                "hint": "Walking less distance saves energy and time.",
                "explanation": "Taking the shortest route minimizes walking distance, conserving time and physical energy during campus transitions.",
                "solution_html": make_sol_html([
                    "Analyze the practical benefits of shortest-path routing:",
                    "Distance is directly proportional to travel time (Time = Distance ÷ Speed).",
                    "Minimizing distance minimizes transit duration and physical energy expended.",
                    "This optimization is fundamental to logistics, emergency response, and daily campus navigation."
                ], "It minimizes travel distance, saving time and physical effort.")
            },
            {
                "q": "What essential information should a student include when drawing a personal campus sight map?",
                "options": ["Drawings of passing airplanes only", "Sequential landmarks, directional turn arrows, and labeled pathways", "Random paint splashes", "Only the names of holidays"],
                "ans": 1,
                "hint": "A navigator needs recognizable waypoints and directions to follow the path.",
                "explanation": "A practical sight map requires recognizable landmark waypoints, turn arrows (left/right), and labeled pathways.",
                "solution_html": make_sol_html([
                    "Identify key cartographic elements of a sight map:",
                    "1. Starting point (e.g., entrance gate) and destination (e.g., classroom desk).",
                    "2. Sequential landmark waypoints (water fountain, ashoka tree, office, stairs).",
                    "3. Directional turn arrows indicating orientation shifts (turn left, turn right, go straight).",
                    "4. Labeled corridors and pathways."
                ], "Sequential landmarks, directional turn arrows, and labeled pathways.")
            },
            {
                "q": "How does creating a personal sight map strengthen spatial intelligence?",
                "options": ["It makes paper thicker", "It bridges physical 3D navigation experiences with structured 2D geometric representations", "It changes the school bell schedule", "It makes desks round"],
                "ans": 1,
                "hint": "You translate what you see while walking into a flat drawing.",
                "explanation": "Mapping translates three-dimensional sensory memories of motion and vision into an organized two-dimensional diagram.",
                "solution_html": make_sol_html([
                    "Spatial intelligence involves mentally manipulating 2D and 3D spatial representations.",
                    "Walking through a space involves 3D egocentric perception (what is in front, left, right).",
                    "Drawing a sight map requires transforming that subjective 3D experience into an allocentric 2D bird's-eye map.",
                    "This cognitive transformation is the foundation of spatial reasoning and mathematical cartography."
                ], "It bridges physical 3D navigation experiences with structured 2D geometric representations.")
            },
            {
                "q": "If an explorer faces North and makes a 90° turn to the right, which cardinal direction are they now facing?",
                "options": ["South", "West", "East", "North-West"],
                "ans": 2,
                "hint": "Think of the compass rose: North at top, East at right.",
                "explanation": "Turning 90° clockwise (to the right) from North faces East.",
                "solution_html": make_sol_html([
                    "Review cardinal directions on a standard compass rose:",
                    "North is at 0° (top).",
                    "A 90° turn to the right (clockwise) rotates from North to East.",
                    "Therefore, the explorer is now facing East."
                ], "The explorer is facing East.")
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
