# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 (4 Challenges x 10 Questions = 40 Questions)
Class 3 Mathematics - Chapter 2: Toy Joy
Strict requirements:
- Titles: 'Challenge 1', 'Challenge 2', 'Challenge 3', 'Challenge 4' (all 2 words)
- Zero human character names (no Meera, Dhruv, Teji, Jojo, Raghav, Deba, Deep, Pihu, etc.)
- Zero lecturer personas (no Dr., Sir, Madam, Mr., Mrs., Miss)
- Each question has id, q, 4 options, ans, hint, explanation, and 3-step solution_steps
"""

slides_part3 = [
    # Slide 17: Challenge 1 (3D Shapes Identification & Toy Shop Models)
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Shape Identification",
        "description": "Test your ability to identify 3D solid shapes, recognize real-world objects, and analyze toy assemblies.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "Which 3D solid shape does a cylindrical drinking can resemble?",
                "options": [
                    "A cylinder",
                    "A cube",
                    "A sphere",
                    "A cone"
                ],
                "ans": "A cylinder",
                "hint": "Think about a shape with two circular flat ends and a smooth curved side.",
                "explanation": "A drinking can has two identical parallel circular faces and a curved wall, making it a cylinder.",
                "solution_steps": {
                    "step1": "Observe the physical characteristics of a metal beverage can.",
                    "step2": "Identify its two circular flat ends and rounded lateral surface.",
                    "step3": "Conclude that this matches the geometric definition of a cylinder."
                }
            },
            {
                "id": "c1_q2",
                "q": "What 3D shape is formed by a sharp birthday party hat?",
                "options": [
                    "A cone",
                    "A cylinder",
                    "A cuboid",
                    "A sphere"
                ],
                "ans": "A cone",
                "hint": "It has one circular flat base and tapers up to a sharp pointed tip.",
                "explanation": "A party hat has a circular opening at the base and tapers to a single pointed vertex (apex), which defines a cone.",
                "solution_steps": {
                    "step1": "Examine the outline of a celebratory party hat.",
                    "step2": "Note that it narrows smoothly to a sharp point at the top.",
                    "step3": "Recognize that a 3D solid with one circular base and a pointed apex is a cone."
                }
            },
            {
                "id": "c1_q3",
                "q": "In a toy rocket model, which shape is placed at the very top as the nose cone?",
                "options": [
                    "A cone",
                    "A cube",
                    "A cylinder",
                    "A sphere"
                ],
                "ans": "A cone",
                "hint": "The aerodynamic tip of a rocket is pointed to pierce through the air.",
                "explanation": "The aerodynamic nose of a toy rocket is shaped like a cone to point upwards.",
                "solution_steps": {
                    "step1": "Recall the structural assembly of the toy rocket.",
                    "step2": "Identify the topmost pointed component.",
                    "step3": "Confirm that a pointed solid with a circular base is a cone."
                }
            },
            {
                "id": "c1_q4",
                "q": "In a wooden toy locomotive, which 3D shape is used to represent the horizontal steam boiler?",
                "options": [
                    "A long cylinder",
                    "A flat square cube",
                    "A pointed cone",
                    "A round sphere"
                ],
                "ans": "A long cylinder",
                "hint": "Boilers on steam trains are cylindrical pressurized tanks.",
                "explanation": "The long, rounded central body of a steam train locomotive is modeled using a horizontal cylinder.",
                "solution_steps": {
                    "step1": "Look at the parts making up the toy railway locomotive.",
                    "step2": "Locate the long red central body holding steam.",
                    "step3": "Conclude that this horizontally placed tube is a cylinder."
                }
            },
            {
                "id": "c1_q5",
                "q": "A rectangular shoe box or cereal carton is an everyday example of which 3D solid?",
                "options": [
                    "A cuboid",
                    "A sphere",
                    "A cone",
                    "A cylinder"
                ],
                "ans": "A cuboid",
                "hint": "It has six flat rectangular faces with length, width, and height.",
                "explanation": "A box with six rectangular faces where opposite faces are equal is a rectangular cuboid.",
                "solution_steps": {
                    "step1": "Analyze the faces of a standard shoe box.",
                    "step2": "Observe that all 6 faces are rectangles meeting at right angles.",
                    "step3": "Classify this shape as a cuboid."
                }
            },
            {
                "id": "c1_q6",
                "q": "Which toy train component is typically shaped as a cone?",
                "options": [
                    "The puffing smokestack chimney",
                    "The flat railway tracks",
                    "The rectangular driver's cabin",
                    "The circular wheels"
                ],
                "ans": "The puffing smokestack chimney",
                "hint": "It sits upright on top of the boiler to let steam escape.",
                "explanation": "The smokestack atop the boiler tapers upward, which is modeled as a small yellow cone.",
                "solution_steps": {
                    "step1": "Identify the chimney pipe on the toy train.",
                    "step2": "Observe that it is shaped like an inverted or upright cone.",
                    "step3": "Match it with the smokestack component."
                }
            },
            {
                "id": "c1_q7",
                "q": "Which everyday classroom item has the exact 3D geometric shape of a sphere?",
                "options": [
                    "A world globe",
                    "A chalkboard duster",
                    "A flat notebook",
                    "A triangular ruler"
                ],
                "ans": "A world globe",
                "hint": "It is completely round and can roll in all directions.",
                "explanation": "A world globe is completely round and symmetrical from every angle, representing a sphere.",
                "solution_steps": {
                    "step1": "Check the geometry of each listed classroom object.",
                    "step2": "A duster is a cuboid; a notebook is flat; a globe is a 3D ball.",
                    "step3": "Confirm that a globe represents a sphere."
                }
            },
            {
                "id": "c1_q8",
                "q": "If a toy rocket body has 1 cone top, 1 cylinder fuselage, and 1 cuboid launch base, how many total 3D parts are used?",
                "options": [
                    "3 parts",
                    "5 parts",
                    "2 parts",
                    "4 parts"
                ],
                "ans": "3 parts",
                "hint": "Add the counts: 1 + 1 + 1.",
                "explanation": "1 cone + 1 cylinder + 1 cuboid = 3 total parts.",
                "solution_steps": {
                    "step1": "Count each shape: 1 cone, 1 cylinder, 1 cuboid.",
                    "step2": "Calculate 1 + 1 + 1 = 3.",
                    "step3": "Select 3 parts as the total count."
                }
            },
            {
                "id": "c1_q9",
                "q": "What 3D shape is formed by six equal square wooden blocks glued together to form a solid box?",
                "options": [
                    "A cube",
                    "A sphere",
                    "A cylinder",
                    "A cone"
                ],
                "ans": "A cube",
                "hint": "All six faces are identical squares.",
                "explanation": "A solid with six identical square faces is a cube.",
                "solution_steps": {
                    "step1": "Note that all 6 faces are equal squares.",
                    "step2": "Recall that when length = width = height, a cuboid is a cube.",
                    "step3": "Conclude the shape is a cube."
                }
            },
            {
                "id": "c1_q10",
                "q": "Which part of a newly sharpened pencil resembles a cone?",
                "options": [
                    "The sharpened writing tip",
                    "The long wooden barrel",
                    "The flat circular eraser base",
                    "The hexagonal grip"
                ],
                "ans": "The sharpened writing tip",
                "hint": "The tip is shaved down to a sharp point for writing.",
                "explanation": "The shaved writing point of a pencil tapers to a vertex, forming a conical tip.",
                "solution_steps": {
                    "step1": "Inspect a sharpened pencil from eraser to tip.",
                    "step2": "The wooden shaft is a cylinder/prism, while the tip tapers to a point.",
                    "step3": "Identify the sharpened point as a cone."
                }
            }
        ]
    },

    # Slide 18: Challenge 2 (Faces, Edges, Corners & Surface Properties)
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Anatomy & Motion",
        "description": "Demonstrate your understanding of faces, edges, corners, and the dynamic laws of rolling and sliding.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "How many flat faces, straight edges, and sharp corners does a standard cube have?",
                "options": [
                    "6 faces, 12 edges, 8 corners",
                    "8 faces, 12 edges, 6 corners",
                    "6 faces, 8 edges, 12 corners",
                    "4 faces, 6 edges, 4 corners"
                ],
                "ans": "6 faces, 12 edges, 8 corners",
                "hint": "A cube has 6 square faces, 12 boundary edges, and 8 corner points.",
                "explanation": "A cube has 6 flat square faces, 12 straight edges, and 8 vertices (corners).",
                "solution_steps": {
                    "step1": "Count the flat square faces of a cube (6).",
                    "step2": "Count the straight edges where faces meet (12).",
                    "step3": "Count the corner points where edges meet (8)."
                }
            },
            {
                "id": "c2_q2",
                "q": "How many corners (vertices) does a solid sphere have?",
                "options": [
                    "0 corners",
                    "1 corner",
                    "4 corners",
                    "8 corners"
                ],
                "ans": "0 corners",
                "hint": "A sphere is completely round with no sharp points anywhere.",
                "explanation": "A sphere consists of a continuous curved surface with zero flat faces, zero edges, and zero corners.",
                "solution_steps": {
                    "step1": "Recall the geometric definition of a vertex (a sharp point where edges meet).",
                    "step2": "Observe that a sphere has no edges or flat planes.",
                    "step3": "Conclude that a sphere has 0 corners."
                }
            },
            {
                "id": "c2_q3",
                "q": "How many circular edges does a solid cylinder possess?",
                "options": [
                    "2 circular edges",
                    "0 edges",
                    "4 straight edges",
                    "1 circular edge"
                ],
                "ans": "2 circular edges",
                "hint": "Count the rims where the top and bottom circular faces meet the curved side.",
                "explanation": "A cylinder has 2 circular edges where its top and bottom flat faces meet the curved body.",
                "solution_steps": {
                    "step1": "Look at where the flat circular ends join the curved cylindrical side.",
                    "step2": "Each end creates one curved boundary rim.",
                    "step3": "Total curved edges = 2."
                }
            },
            {
                "id": "c2_q4",
                "q": "Why does a marble roll down a ramp while a wooden block slides?",
                "options": [
                    "A marble has a curved surface, while a block has flat faces",
                    "A marble is heavier than a wooden block",
                    "A block has wheels hidden underneath",
                    "A marble is made of liquid"
                ],
                "ans": "A marble has a curved surface, while a block has flat faces",
                "hint": "Curved surfaces roll continuously; flat faces slide along the plane.",
                "explanation": "Curved surfaces turn smoothly over a slope to roll, whereas flat surfaces slide along the incline.",
                "solution_steps": {
                    "step1": "Compare the surfaces of a marble (curved) and a block (flat).",
                    "step2": "Curved surfaces rotate continuously during motion (rolling).",
                    "step3": "Flat surfaces stay in planar contact while sliding."
                }
            },
            {
                "id": "c2_q5",
                "q": "Which of these 3D shapes can both roll and slide?",
                "options": [
                    "A cylinder",
                    "A cube",
                    "A cuboid",
                    "A world globe"
                ],
                "ans": "A cylinder",
                "hint": "It can roll on its curved side and slide on its flat circular base.",
                "explanation": "A cylinder rolls when placed on its curved wall and slides when placed on either flat circular face.",
                "solution_steps": {
                    "step1": "Identify shapes possessing both flat faces and curved surfaces.",
                    "step2": "A cylinder has 2 flat faces (slides) and 1 curved surface (rolls).",
                    "step3": "Confirm that a cylinder can both roll and slide."
                }
            },
            {
                "id": "c2_q6",
                "q": "What is the sharp pointed top of a cone called?",
                "options": [
                    "The apex or top corner",
                    "The perimeter",
                    "The flat diameter",
                    "The curved edge"
                ],
                "ans": "The apex or top corner",
                "hint": "It is the single sharp point at the pinnacle of the cone.",
                "explanation": "The single vertex at the tip of a cone opposite its circular base is called the apex.",
                "solution_steps": {
                    "step1": "Examine the components of a cone: 1 circular base, 1 curved surface, 1 vertex.",
                    "step2": "The vertex at the pointed tip opposite the base is the apex.",
                    "step3": "Select 'The apex or top corner'."
                }
            },
            {
                "id": "c2_q7",
                "q": "How many flat faces does a solid cone have?",
                "options": [
                    "1 flat circular face",
                    "2 flat faces",
                    "0 flat faces",
                    "3 triangular faces"
                ],
                "ans": "1 flat circular face",
                "hint": "Check the bottom base of the cone.",
                "explanation": "A cone has exactly 1 flat face, which is its circular base.",
                "solution_steps": {
                    "step1": "Analyze the surface parts of a cone.",
                    "step2": "The base is a flat circle; the remaining body is a curved lateral surface.",
                    "step3": "Conclude that it has exactly 1 flat face."
                }
            },
            {
                "id": "c2_q8",
                "q": "Which statement correctly describes the relationship between a cube and a cuboid?",
                "options": [
                    "Every cube is a special cuboid with all equal square faces",
                    "Every cuboid is always a cube",
                    "Cubes and cuboids have completely different numbers of corners",
                    "A cube has no flat faces"
                ],
                "ans": "Every cube is a special cuboid with all equal square faces",
                "hint": "A cube satisfies all cuboid rules, with the extra condition that all sides are equal.",
                "explanation": "A cube is a special cuboid where length, width, and height are identical, making all six faces equal squares.",
                "solution_steps": {
                    "step1": "Recall the definitions of cube and cuboid (both have 6 faces, 12 edges, 8 vertices).",
                    "step2": "A square is a special rectangle; thus, equal-sided boxes are special cuboids.",
                    "step3": "Conclude that every cube is a cuboid."
                }
            },
            {
                "id": "c2_q9",
                "q": "Why can you NOT stack spheres on top of each other to make a tall stable tower?",
                "options": [
                    "Spheres have zero flat faces to rest stably upon",
                    "Spheres are too soft and squash flat",
                    "Spheres have sharp corners that push them apart",
                    "Spheres are magnetic and repel each other"
                ],
                "ans": "Spheres have zero flat faces to rest stably upon",
                "hint": "Stacking requires flat surfaces to distribute weight without rolling off.",
                "explanation": "Because spheres have only a curved surface with zero flat faces, they roll off each other when stacked without support.",
                "solution_steps": {
                    "step1": "Consider what makes stacked objects stable: flat horizontal contact planes.",
                    "step2": "Observe that spheres touch only at a single point and easily roll.",
                    "step3": "Conclude that the lack of flat faces prevents stacking."
                }
            },
            {
                "id": "c2_q10",
                "q": "What is the line where two flat faces of a solid meet called?",
                "options": [
                    "An edge",
                    "A vertex",
                    "A perimeter circle",
                    "A diagonal"
                ],
                "ans": "An edge",
                "hint": "It is the straight boundary segment joining two adjacent faces.",
                "explanation": "An edge is the line segment where two faces of a three-dimensional solid intersect.",
                "solution_steps": {
                    "step1": "Recall the anatomical definitions of solid geometry.",
                    "step2": "Faces are flat surfaces; edges are lines where faces meet; corners are points where edges meet.",
                    "step3": "Select 'An edge'."
                }
            }
        ]
    },

    # Slide 19: Challenge 3 (Clay Skeletons & Dice Dot Arithmetic)
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Frames & Dice Rules",
        "description": "Master wireframe skeleton construction with clay balls and sticks, and apply the opposite-sum rule of standard dice.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "When building a skeleton frame of a cube using toothpicks and clay balls, how many clay balls are needed?",
                "options": [
                    "8 clay balls",
                    "6 clay balls",
                    "12 clay balls",
                    "4 clay balls"
                ],
                "ans": "8 clay balls",
                "hint": "Each clay ball forms a corner (vertex). A cube has 8 corners.",
                "explanation": "Clay balls represent vertices. Because a cube has 8 vertices, exactly 8 clay balls are required.",
                "solution_steps": {
                    "step1": "Recall that clay balls correspond to the corners (vertices) of the 3D solid.",
                    "step2": "Determine the number of corners on a cube (8).",
                    "step3": "Conclude that 8 clay balls are needed."
                }
            },
            {
                "id": "c3_q2",
                "q": "How many toothpicks of equal length are needed to construct the complete skeleton of a cube?",
                "options": [
                    "12 toothpicks",
                    "8 toothpicks",
                    "6 toothpicks",
                    "10 toothpicks"
                ],
                "ans": "12 toothpicks",
                "hint": "Toothpicks represent edges. A cube has 12 edges.",
                "explanation": "Toothpicks represent edges. A cube has 12 edges, so 12 identical toothpicks are needed.",
                "solution_steps": {
                    "step1": "Recall that toothpicks correspond to the straight edges of the shape.",
                    "step2": "Count the edges of a cube: 4 at the base, 4 vertical pillars, 4 at the top = 12.",
                    "step3": "Conclude that 12 toothpicks are required."
                }
            },
            {
                "id": "c3_q3",
                "q": "What is the constant sum of numbers on opposite faces of any standard die?",
                "options": [
                    "7",
                    "6",
                    "10",
                    "12"
                ],
                "ans": "7",
                "hint": "Pair the numbers: 1 and 6, 2 and 5, 3 and 4.",
                "explanation": "Standard dice are manufactured so that opposite faces always add up to exactly 7.",
                "solution_steps": {
                    "step1": "Recall the universal standard dice dot rule.",
                    "step2": "Check pairs: 1+6=7, 2+5=7, 3+4=7.",
                    "step3": "Confirm that the constant opposite sum is 7."
                }
            },
            {
                "id": "c3_q4",
                "q": "If a standard die shows 3 dots on top, how many dots are on the bottom face touching the table?",
                "options": [
                    "4 dots",
                    "2 dots",
                    "5 dots",
                    "1 dot"
                ],
                "ans": "4 dots",
                "hint": "Subtract 3 from the total sum of 7.",
                "explanation": "Opposite faces sum to 7. Therefore, 7 - 3 = 4 dots on the opposite bottom face.",
                "solution_steps": {
                    "step1": "Identify the top face number (3).",
                    "step2": "Apply the rule: Top + Bottom = 7.",
                    "step3": "Compute Bottom = 7 - 3 = 4 dots."
                }
            },
            {
                "id": "c3_q5",
                "q": "If a standard die shows 1 dot on its front face, what number is on the hidden back face?",
                "options": [
                    "6 dots",
                    "5 dots",
                    "4 dots",
                    "3 dots"
                ],
                "ans": "6 dots",
                "hint": "Subtract 1 from 7.",
                "explanation": "Opposite faces sum to 7: 7 - 1 = 6 dots on the back face.",
                "solution_steps": {
                    "step1": "Identify the visible face: 1 dot.",
                    "step2": "Subtract from 7: 7 - 1 = 6.",
                    "step3": "The opposite back face has 6 dots."
                }
            },
            {
                "id": "c3_q6",
                "q": "If the bottom face of a standard die has 5 dots, what number is facing upwards?",
                "options": [
                    "2 dots",
                    "3 dots",
                    "1 dot",
                    "4 dots"
                ],
                "ans": "2 dots",
                "hint": "What number added to 5 makes 7?",
                "explanation": "Because opposite faces add up to 7, the top face must show 7 - 5 = 2 dots.",
                "solution_steps": {
                    "step1": "Given bottom face = 5 dots.",
                    "step2": "Calculate top face = 7 - 5 = 2 dots.",
                    "step3": "Select 2 dots as the answer."
                }
            },
            {
                "id": "c3_q7",
                "q": "To build a skeleton frame of a cuboid, how many sets of different length sticks are typically needed?",
                "options": [
                    "3 sets of 4 sticks each (length, width, height)",
                    "12 sticks of completely random lengths",
                    "Only 1 stick length for all 12 edges",
                    "2 sticks total"
                ],
                "ans": "3 sets of 4 sticks each (length, width, height)",
                "hint": "A cuboid has 3 dimensions: length, width, and height, each with 4 parallel edges.",
                "explanation": "A general cuboid has 3 dimensions (length, width, height), each requiring 4 parallel equal sticks (4 + 4 + 4 = 12).",
                "solution_steps": {
                    "step1": "A cuboid has 12 edges divided into 3 sets of 4 parallel edges.",
                    "step2": "Each dimension (length, width, height) has 4 identical edges.",
                    "step3": "Conclude that 3 sets of 4 sticks each are needed."
                }
            },
            {
                "id": "c3_q8",
                "q": "Can you build a skeleton frame of a sphere using straight toothpicks and clay balls?",
                "options": [
                    "No, because a sphere has no straight edges or corner points",
                    "Yes, by using 100 toothpicks in a straight line",
                    "Yes, a sphere needs exactly 4 toothpicks",
                    "Yes, using 1 toothpick bent in half"
                ],
                "ans": "No, because a sphere has no straight edges or corner points",
                "hint": "Skeleton models require straight edges and sharp vertices.",
                "explanation": "A sphere has a continuous curved surface with zero straight edges and zero corners, so it cannot be built from sticks and vertex balls.",
                "solution_steps": {
                    "step1": "Recall that stick skeletons represent straight edges meeting at sharp vertices.",
                    "step2": "A sphere has 0 straight edges and 0 vertices.",
                    "step3": "Conclude that a sphere cannot be built with straight sticks and vertex balls."
                }
            },
            {
                "id": "c3_q9",
                "q": "In the Toy Joy board game, if your token is on tile 14 and you roll a 5, which tile do you land on?",
                "options": [
                    "Tile 19",
                    "Tile 18",
                    "Tile 20",
                    "Tile 17"
                ],
                "ans": "Tile 19",
                "hint": "Add the die roll to your current position: 14 + 5.",
                "explanation": "Starting at tile 14 and moving forward 5 spaces lands you on tile 14 + 5 = 19.",
                "solution_steps": {
                    "step1": "Identify current position: 14.",
                    "step2": "Add the rolled distance: 14 + 5.",
                    "step3": "The token lands on tile 19."
                }
            },
            {
                "id": "c3_q10",
                "q": "On a standard die, which two numbers are placed opposite each other?",
                "options": [
                    "2 and 5",
                    "1 and 5",
                    "3 and 6",
                    "4 and 2"
                ],
                "ans": "2 and 5",
                "hint": "Check which pair adds up to 7.",
                "explanation": "2 + 5 = 7, making them an opposite face pair on standard dice.",
                "solution_steps": {
                    "step1": "Check the sums of each pair: 2+5=7, 1+5=6, 3+6=9, 4+2=6.",
                    "step2": "Only the pair 2 and 5 sums to 7.",
                    "step3": "Conclude that 2 and 5 are placed on opposite faces."
                }
            }
        ]
    },

    # Slide 20: Challenge 4 (Composite Cubes, Stacking & Master Matrix)
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Composite Stacks",
        "description": "Solve advanced multi-cube spatial puzzles, calculate joined face counts, and master hidden block deductions.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "When two identical cubes are joined side-by-side along one face, what new shape is formed?",
                "options": [
                    "A rectangular cuboid",
                    "A single larger cube",
                    "A round cylinder",
                    "A sphere"
                ],
                "ans": "A rectangular cuboid",
                "hint": "The length doubles while width and height stay the same.",
                "explanation": "Because the length is doubled while width and height remain unchanged, the resulting solid is a cuboid.",
                "solution_steps": {
                    "step1": "Combine two cubes of side length 1.",
                    "step2": "Dimensions become length = 2, width = 1, height = 1.",
                    "step3": "Since dimensions are not all equal, it is a cuboid."
                }
            },
            {
                "id": "c4_q2",
                "q": "Two cubes each have 6 faces. When joined together face-to-face, how many total exposed outer faces does the new cuboid have?",
                "options": [
                    "10 unit square faces (or 6 cuboid faces)",
                    "12 unit square faces",
                    "8 unit square faces",
                    "6 unit square faces total"
                ],
                "ans": "10 unit square faces (or 6 cuboid faces)",
                "hint": "Two faces touch inside the seam and disappear: 6 + 6 - 2 = 10.",
                "explanation": "Before joining, there are 6 + 6 = 12 square faces. Joining hides 2 faces in the seam: 12 - 2 = 10 exposed unit square faces.",
                "solution_steps": {
                    "step1": "Total individual faces before joining = 6 + 6 = 12.",
                    "step2": "Touching faces hidden inside the seam = 2.",
                    "step3": "Exposed outer square faces = 12 - 2 = 10."
                }
            },
            {
                "id": "c4_q3",
                "q": "If three unit cubes are joined in a single straight line, what are the dimensions of the resulting cuboid?",
                "options": [
                    "Length 3, Width 1, Height 1",
                    "Length 3, Width 3, Height 3",
                    "Length 1, Width 1, Height 1",
                    "Length 2, Width 2, Height 1"
                ],
                "ans": "Length 3, Width 1, Height 1",
                "hint": "Three unit blocks placed end-to-end triple the length.",
                "explanation": "Three unit cubes placed in a line make a solid of length 3 units, width 1 unit, and height 1 unit.",
                "solution_steps": {
                    "step1": "Place 3 unit cubes of side 1 end-to-end.",
                    "step2": "Length = 1 + 1 + 1 = 3; width = 1; height = 1.",
                    "step3": "Select 'Length 3, Width 1, Height 1'."
                }
            },
            {
                "id": "c4_q4",
                "q": "A staircase is built using 3 columns of cubes: column 1 has 1 cube, column 2 has 2 cubes, and column 3 has 3 cubes. How many cubes were used?",
                "options": [
                    "6 cubes",
                    "5 cubes",
                    "8 cubes",
                    "9 cubes"
                ],
                "ans": "6 cubes",
                "hint": "Add the cubes in each vertical column: 1 + 2 + 3.",
                "explanation": "Adding the columns: 1 + 2 + 3 = 6 unit cubes in total.",
                "solution_steps": {
                    "step1": "List the cubes in each column: 1, 2, 3.",
                    "step2": "Sum the numbers: 1 + 2 + 3 = 6.",
                    "step3": "Conclude that exactly 6 cubes were used."
                }
            },
            {
                "id": "c4_q5",
                "q": "Why must there be a hidden cube under the top step of a 2-cube high tower?",
                "options": [
                    "A block cannot float in empty air and needs a foundation block under it",
                    "It is made of magnetic glue",
                    "To hide secret toys inside",
                    "Because top blocks are always invisible"
                ],
                "ans": "A block cannot float in empty air and needs a foundation block under it",
                "hint": "Gravity requires physical support beneath elevated objects.",
                "explanation": "In physical construction, an elevated block must rest upon a solid foundation block beneath it.",
                "solution_steps": {
                    "step1": "Observe the height of the column (2 cubes high).",
                    "step2": "Recognize that the upper block must be supported from below.",
                    "step3": "Conclude that a foundation cube exists beneath the visible top block."
                }
            },
            {
                "id": "c4_q6",
                "q": "How many total unit cubes are in a 4-step staircase with columns of heights 1, 2, 3, and 4 cubes?",
                "options": [
                    "10 cubes",
                    "12 cubes",
                    "8 cubes",
                    "15 cubes"
                ],
                "ans": "10 cubes",
                "hint": "Add 1 + 2 + 3 + 4.",
                "explanation": "1 + 2 + 3 + 4 = 10 cubes in total.",
                "solution_steps": {
                    "step1": "List the column heights: 1, 2, 3, 4.",
                    "step2": "Add them: 1 + 2 = 3; 3 + 3 = 6; 6 + 4 = 10.",
                    "step3": "Select 10 cubes."
                }
            },
            {
                "id": "c4_q7",
                "q": "How many flat faces, curved surfaces, and corners does a cylinder have?",
                "options": [
                    "2 flat faces, 1 curved surface, 0 corners",
                    "1 flat face, 2 curved surfaces, 1 corner",
                    "6 flat faces, 0 curved surfaces, 8 corners",
                    "0 flat faces, 1 curved surface, 0 corners"
                ],
                "ans": "2 flat faces, 1 curved surface, 0 corners",
                "hint": "Top and bottom are flat circles; side is curved; there are no sharp points.",
                "explanation": "A cylinder has 2 flat circular faces, 1 curved lateral surface, 2 curved edges, and zero corners.",
                "solution_steps": {
                    "step1": "Identify top and bottom circles (2 flat faces).",
                    "step2": "Identify the rounded lateral wall (1 curved surface).",
                    "step3": "Note that no edges meet at a sharp point, so corners = 0."
                }
            },
            {
                "id": "c4_q8",
                "q": "Which 3D shape has 1 flat circular face, 1 curved surface, 1 circular edge, and 1 pointed corner (apex)?",
                "options": [
                    "A cone",
                    "A cylinder",
                    "A sphere",
                    "A cuboid"
                ],
                "ans": "A cone",
                "hint": "Think of an ice cream cone or birthday hat.",
                "explanation": "A cone has 1 flat circular base, 1 curved surface, 1 circular edge, and 1 vertex (apex).",
                "solution_steps": {
                    "step1": "Review the properties: 1 circular face, 1 curved surface, 1 apex.",
                    "step2": "Match these properties with solid shapes.",
                    "step3": "Confirm that this defines a cone."
                }
            },
            {
                "id": "c4_q9",
                "q": "If you stack three identical cubes vertically in a single tower, how tall is the tower if each cube is 4 cm high?",
                "options": [
                    "12 cm",
                    "8 cm",
                    "16 cm",
                    "4 cm"
                ],
                "ans": "12 cm",
                "hint": "Multiply 3 cubes by 4 cm each.",
                "explanation": "Three cubes stacked vertically have a combined height of 3 * 4 cm = 12 cm.",
                "solution_steps": {
                    "step1": "Identify the height of each cube (4 cm).",
                    "step2": "Multiply by the number of cubes in the stack (3).",
                    "step3": "Calculate 3 * 4 cm = 12 cm."
                }
            },
            {
                "id": "c4_q10",
                "q": "Which shape from the Master Geometry Matrix has zero flat faces, zero straight edges, and zero corners?",
                "options": [
                    "A sphere",
                    "A cube",
                    "A cylinder",
                    "A cone"
                ],
                "ans": "A sphere",
                "hint": "It is completely round all over like a cricket ball.",
                "explanation": "A sphere is completely bounded by a single continuous curved surface, having 0 flat faces, 0 edges, and 0 corners.",
                "solution_steps": {
                    "step1": "Look at the master geometry matrix row with all zeros for faces, edges, and corners.",
                    "step2": "Identify the completely round solid.",
                    "step3": "Confirm the shape is a sphere."
                }
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 17 TO 20 (CHALLENGES) ===")
    assert len(slides_part3) == 4, f"Expected 4 challenge slides, got {len(slides_part3)}"
    
    total_q = 0
    for s in slides_part3:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        questions = s["questions"]
        assert len(questions) == 10, f"Slide {sid} must have exactly 10 questions, got {len(questions)}"
        total_q += len(questions)
        
        for q in questions:
            qid = q["id"]
            assert len(q["options"]) == 4, f"Question {qid} options != 4"
            assert q["ans"] in q["options"], f"Question {qid} ans '{q['ans']}' not in options!"
            assert "hint" in q and len(q["hint"]) > 5, f"Question {qid} missing hint!"
            assert "explanation" in q and len(q["explanation"]) > 5, f"Question {qid} missing explanation!"
            assert "solution_steps" in q, f"Question {qid} missing solution_steps!"
            steps = q["solution_steps"]
            assert "step1" in steps and "step2" in steps and "step3" in steps, f"Question {qid} missing steps 1-3!"
            
    print(f"Verified {len(slides_part3)} challenge slides with {total_q} questions successfully!")
