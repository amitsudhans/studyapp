import sys

slides_part2 = [
    {
        "id": 9,
        "title": "Sorting Solid Shapes",
        "badge": "Property Sorting",
        "sim_id": "sim_shape_property_sorter",
        "description": "Classify diverse solid shapes into distinct categories based on their dynamic rolling, sliding, and stacking capabilities.",
        "speech": (
            "Now that we have discovered various geometric solids, let us organize them through systematic mathematical classification! "
            "In this sorting investigation, solid shapes are grouped into three distinct categories based on how they move across flat surfaces: "
            "shapes that only roll, shapes that only slide, and versatile shapes that can both roll and slide! "
            "Objects with exclusively curved surfaces, like a round cricket ball or a smooth glass marble, belong to the rolling group. "
            "Because a sphere lacks flat faces, it rolls effortlessly in any direction but cannot slide or stack securely. "
            "Conversely, objects bounded purely by flat polygonal faces—such as wooden cubes, rectangular gift boxes, and geometric cuboids—belong "
            "to the sliding group. "
            "When pushed, they glide steadily across table surfaces without rotating, and their flat horizontal tops allow multiple boxes to stack "
            "into tall, stable towers! "
            "Finally, cylinders and cones form the extraordinary dual-action category. "
            "Place a cylindrical tin on its round curved side, and it rolls briskly down the ramp; "
            "place it upright on its flat circular face, and it slides smoothly or acts as a sturdy building pedestal! "
            "Sorting shapes by mechanical behavior helps us select optimal structural components when designing real engineering marvels."
        ),
        "checkpoints": [
            {
                "q": "Which group of solid shapes can both roll and slide depending on how they are positioned?",
                "options": [
                    "Cylinders and cones",
                    "Cubes and cuboids",
                    "Only spherical balls",
                    "Only flat square tiles"
                ],
                "ans": "Cylinders and cones",
                "explanation": "Cylinders and cones have flat circular faces for sliding and curved lateral surfaces for rolling."
            },
            {
                "q": "Why can multiple rectangular cuboids and cubes be easily stacked into tall, sturdy towers?",
                "options": [
                    "They possess flat planar faces that rest firmly against one another",
                    "They have magnetic curved sides that attract each other",
                    "They are lighter than air and float upwards",
                    "They possess zero straight edges or corners"
                ],
                "ans": "They possess flat planar faces that rest firmly against one another",
                "explanation": "Flat faces provide stable, level contact areas that prevent stacked blocks from toppling over."
            }
        ]
    },
    {
        "id": 10,
        "title": "Clay Stick Skeletons",
        "badge": "Skeleton Frames",
        "sim_id": "sim_clay_stick_builder",
        "description": "Construct hollow wireframe skeleton models of 3D solids using small clay balls for corners and wooden sticks for edges.",
        "speech": (
            "To truly master the internal geometry of solid figures, nothing equals the joy of building three-dimensional skeleton frames! "
            "In this tactile craftwork laboratory, we assemble hollow geometric skeletons using two simple materials: "
            "small molded clay balls and straight wooden matchsticks or toothpicks. "
            "This hands-on modeling reveals an essential structural correspondence in solid geometry: "
            "every straight wooden stick represents an edge, and every moist clay ball that joins sticks together represents a corner or vertex! "
            "To construct the skeleton frame of a cube, we first roll eight equal spherical balls of soft modeling clay. "
            "Next, we take twelve straight matchsticks of identical length. "
            "By inserting four sticks into four clay balls, we build a flat square base. "
            "We erect four vertical sticks from these corners, and finally cap them with four more sticks and four top clay balls. "
            "The completed open cube stands firm, displaying its eight clay corners and twelve straight stick edges in clear three-dimensional space! "
            "If we build a rectangular cuboid instead, we still require exactly eight clay corner balls and twelve straight boundary sticks, "
            "though the sticks must come in three differing length sets for length, breadth, and height. "
            "Crafting these skeleton models provides an unforgettable physical demonstration of mathematical vertices, edges, and internal spatial architecture."
        ),
        "checkpoints": [
            {
                "q": "In a clay and matchstick skeleton model of a cube, what do the clay balls represent?",
                "options": [
                    "The sharp corners or vertices",
                    "The flat exterior faces",
                    "The straight boundary edges",
                    "The hollow internal volume"
                ],
                "ans": "The sharp corners or vertices",
                "explanation": "Clay balls connect intersecting sticks, physically representing the vertices or corners of the shape."
            },
            {
                "q": "How many matchsticks and clay balls are needed to build the complete skeleton frame of a cuboid?",
                "options": [
                    "12 matchsticks (edges) and 8 clay balls (vertices)",
                    "6 matchsticks and 6 clay balls",
                    "8 matchsticks and 12 clay balls",
                    "10 matchsticks and 5 clay balls"
                ],
                "ans": "12 matchsticks (edges) and 8 clay balls (vertices)",
                "explanation": "A cuboid has 12 straight edges (matchsticks) meeting at 8 corners (clay balls)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Toy Joy Board",
        "badge": "Mathematical Journey",
        "sim_id": "sim_toy_joy_board_game",
        "description": "Navigate a colorful geometric board game where rolling dice and identifying shape attributes advance player tokens.",
        "speech": (
            "Welcome to the vibrant Toy Joy Board Game, an interactive mathematical journey where geometric mastery leads to victory! "
            "The board is laid out as a meandering winding pathway of numbered tiles, each marked with colorful geometric solid illustrations. "
            "Players begin at the toy workshop starting gate and take turns casting a six-sided dotted wooden cube: the game die! "
            "As tokens advance along the path, players land on diverse property checkpoint squares that challenge their geometric reasoning. "
            "For instance, stepping onto a 'Cylinder Square' prompts the player to state how many flat faces a water bottle possesses. "
            "Landing on an 'Edge Bridge' asks the player to count the twelve edges of a wooden storage chest to earn a forward boost! "
            "Special bonus tiles reward students who can spot real-life shapes: identify a cone on a celebration banner to skip ahead three spaces, "
            "or name a spherical sport ball to take an express shortcut! "
            "However, landing on a 'Curved Slip' requires demonstrating why a rolling sphere cannot stack, sliding the token back one space. "
            "By weaving core geometric definitions directly into thrilling board game rules, mathematics transforms into an engaging, interactive adventure for all young learners. "
            "Every turn reinforces shape properties, edge counting, and spatial orientation through joyful friendly competition."
        ),
        "checkpoints": [
            {
                "q": "What geometric shape is the dotted playing die used in the Toy Joy board game?",
                "options": [
                    "A symmetrical cube",
                    "A long cylinder",
                    "A pointed cone",
                    "A flat triangle"
                ],
                "ans": "A symmetrical cube",
                "explanation": "A standard game die is a symmetrical six-faced solid cube."
            },
            {
                "q": "If a board tile asks how many flat faces a solid cylinder possesses, what is the correct answer?",
                "options": [
                    "2 flat circular faces",
                    "6 flat rectangular faces",
                    "0 flat faces",
                    "4 triangular faces"
                ],
                "ans": "2 flat circular faces",
                "explanation": "A cylinder has 2 flat parallel circular faces (top and bottom) joined by one curved surface."
            }
        ]
    },
    {
        "id": 12,
        "title": "Standard Dice Dots",
        "badge": "Opposite Sum Rule",
        "sim_id": "sim_dice_opposite_faces",
        "description": "Uncover the universal arithmetic secret of standard dot dice: opposite faces always add up to exactly seven.",
        "speech": (
            "Take a close look at a standard game die, and you will uncover one of arithmetic's most delightful hidden secrets! "
            "A standard die is a cube whose six square faces are marked with small black dots called pips, representing numbers from one to six. "
            "At first glance, the placement of these dots might appear completely random. "
            "However, dice makers throughout centuries have followed a strict mathematical convention: "
            "the numbers on opposite faces of a standard die always add up to exactly seven! "
            "Let us verify this universal opposite sum rule by pairing each face with the face directly on the reverse side. "
            "The face with one dot is positioned directly opposite the face with six dots: one plus six equals seven! "
            "The face showing two dots sits directly opposite the face showing five dots: two plus five equals seven! "
            "Finally, the face showing three dots is positioned opposite the face showing four dots: three plus four equals seven! "
            "This elegant rule means that if you know the number showing on the top face of a standard die, "
            "you can instantly deduce the hidden number on the bottom face by subtracting from seven! "
            "Exploring dice patterns bridges spatial geometry with rapid mental arithmetic."
        ),
        "checkpoints": [
            {
                "q": "According to the standard dice rule, what is the constant sum of numbers on opposite faces?",
                "options": [
                    "7",
                    "6",
                    "10",
                    "12"
                ],
                "ans": "7",
                "explanation": "Opposite faces on any standard die always sum to 7: 1+6=7, 2+5=7, and 3+4=7."
            },
            {
                "q": "If a standard die resting on a table shows 5 dots on its top face, how many dots are on the hidden bottom face?",
                "options": [
                    "2 dots",
                    "1 dot",
                    "3 dots",
                    "4 dots"
                ],
                "ans": "2 dots",
                "explanation": "Because opposite faces add up to 7, the bottom face has 7 - 5 = 2 dots."
            }
        ]
    },
    {
        "id": 13,
        "title": "Joining Identical Cubes",
        "badge": "Composite Cuboid",
        "sim_id": "sim_two_cubes_join",
        "description": "Discover what happens when two identical wooden cubes are joined face-to-face to create a brand new composite cuboid.",
        "speech": (
            "What fascinating new geometric structure emerges when two identical wooden cubes are glued together along their square faces? "
            "Let us perform this classic geometric experiment step by step to observe how dimensions and surface properties transform. "
            "Begin with two separate wooden cubes of identical side length, say five centimeters each. "
            "Separately, each cube has six flat square faces, giving twelve individual faces in total. "
            "Now, press one square face of the first cube against a matching square face of the second cube. "
            "When these two faces touch, they become glued together inside the seam and disappear from the exterior surface! "
            "The two joined faces are no longer exposed to the outside. "
            "What shape have we constructed? "
            "The resulting combined solid is no longer a cube because its length has doubled to ten centimeters, "
            "while its width and height remain five centimeters! "
            "Because its three dimensions are no longer all equal, the new single solid is a rectangular cuboid! "
            "Looking at the exterior of this composite cuboid, we count six outer faces: "
            "two square ends and four elongated rectangular side faces. "
            "Joining modular blocks clearly illustrates how simple elementary units combine into sophisticated three-dimensional solid geometric architectures throughout design and engineering."
        ),
        "checkpoints": [
            {
                "q": "When two identical cubes are joined side-by-side along one face, what new solid geometric shape is formed?",
                "options": [
                    "A rectangular cuboid",
                    "A larger single cube",
                    "A round cylinder",
                    "A pointed cone"
                ],
                "ans": "A rectangular cuboid",
                "explanation": "The length doubles while width and height stay the same, creating a cuboid with unequal side dimensions."
            },
            {
                "q": "How many individual square faces become hidden inside the contact seam when two cubes are glued together?",
                "options": [
                    "2 square faces (one from each cube)",
                    "4 square faces",
                    "1 square face",
                    "6 square faces"
                ],
                "ans": "2 square faces (one from each cube)",
                "explanation": "The two touching faces meet inside the seam, hiding exactly 2 faces from the outside."
            }
        ]
    },
    {
        "id": 14,
        "title": "Three Cube Arrangements",
        "badge": "Spatial Configurations",
        "sim_id": "sim_three_cube_variations",
        "description": "Explore and compare the different spatial configurations possible when connecting three identical unit cubes.",
        "speech": (
            "Building upon our twin-cube experiment, let us now investigate the intriguing possibilities of connecting three identical unit cubes! "
            "When we have three unit cubes, how many distinctly different spatial structures can we assemble? "
            "The first and most direct configuration is to join all three cubes in a straight, continuous line. "
            "In this linear arrangement, the cubes form an elongated rectangular cuboid whose length is three times the unit width. "
            "Here, two internal contact seams hide four square faces, leaving fourteen unit squares exposed on the outer surface. "
            "Now, let us rearrange the blocks! "
            "Instead of a straight line, attach the third cube to the side of the second cube at a right angle. "
            "This creates an eye-catching L-shaped composite figure, often called a corner block or triomino solid! "
            "Notice something remarkable about this L-shaped block: "
            "although it still uses exactly three unit cubes and hides four interior faces, it is no longer a simple rectangular cuboid! "
            "It has indented inner corners and protruding arms. "
            "Comparing the straight cuboid with the bent L-shape teaches students that identical volume can yield entirely different geometric shapes. "
            "Spatial reasoning flourishes as children visualize rotations and rearrangements of multi-cube assemblies."
        ),
        "checkpoints": [
            {
                "q": "When three identical cubes are placed in a single straight row, what geometric shape is created?",
                "options": [
                    "An elongated cuboid",
                    "A perfect single cube",
                    "A round sphere",
                    "A triangular pyramid"
                ],
                "ans": "An elongated cuboid",
                "explanation": "Connecting three cubes in a straight line produces an elongated box shape, which is a rectangular cuboid."
            },
            {
                "q": "How many total unit cubes are used in making an L-shaped corner arrangement of three blocks?",
                "options": [
                    "3 cubes",
                    "4 cubes",
                    "6 cubes",
                    "2 cubes"
                ],
                "ans": "3 cubes",
                "explanation": "Both the straight bar and the L-shaped corner are constructed using exactly 3 identical unit cubes."
            }
        ]
    },
    {
        "id": 15,
        "title": "Composite Model Stacks",
        "badge": "Hidden Block Counting",
        "sim_id": "sim_cube_block_counter",
        "description": "Master 3D spatial visualization by counting visible and hidden unit cubes in complex stacked block towers and staircases.",
        "speech": (
            "One of the most thrilling challenges in three-dimensional geometry is counting unit cubes in multi-layer composite structures! "
            "When children build steps, towers, or miniature castles from wooden blocks, some blocks remain clearly visible from the front, "
            "while other blocks are hidden underneath upper tiers to support the weight above. "
            "Consider a three-step wooden staircase. "
            "The bottom front step consists of one cube resting on the table. "
            "The middle step stands two cubes high. "
            "The top back step rises three cubes high. "
            "If an untrained viewer only glances from the front, they might mistakenly count only the top visible surfaces: one plus one plus one! "
            "However, a thoughtful mathematician understands gravity and structural support: "
            "a block cannot float in empty mid-air! "
            "To support the top step at height three, there must be a vertical column of three cubes resting on the ground. "
            "Under the second step, there must be a column of two cubes. "
            "Under the first step, there is one single foundation cube. "
            "Adding column heights systematically—one plus two plus three—reveals that the staircase contains exactly six unit cubes! "
            "Mastering hidden cube deduction transforms flat two-dimensional textbook drawings into vibrant three-dimensional spatial reality in young mathematical minds."
        ),
        "checkpoints": [
            {
                "q": "In a 3-step staircase with columns of heights 1, 2, and 3 cubes, how many total unit cubes are used?",
                "options": [
                    "6 cubes (1 + 2 + 3 = 6)",
                    "3 cubes",
                    "5 cubes",
                    "9 cubes"
                ],
                "ans": "6 cubes (1 + 2 + 3 = 6)",
                "explanation": "Summing the vertical cube columns: 1 + 2 + 3 = 6 unit cubes in total."
            },
            {
                "q": "Why must there be hidden blocks beneath the elevated top tier of a stacked block tower?",
                "options": [
                    "Blocks cannot float in mid-air and need solid support cubes underneath",
                    "The wind blows them away otherwise",
                    "Because all cubes are transparent like glass",
                    "Because top cubes are twice as heavy"
                ],
                "ans": "Blocks cannot float in mid-air and need solid support cubes underneath",
                "explanation": "Physical structures require supporting blocks below elevated tiers so they don't fall."
            }
        ]
    },
    {
        "id": 16,
        "title": "Master Geometry Matrix",
        "badge": "Comprehensive Synthesis",
        "sim_id": "sim_master_geometry_table",
        "description": "Synthesize all solid geometric shapes across faces, edges, vertices, and mechanical behaviors in a master comparison matrix.",
        "speech": (
            "Congratulations on journeying through the wonderland of three-dimensional shapes in Chapter 2, Toy Joy! "
            "To consolidate our geometric mastery, let us unite all our discoveries into one grand Master Geometry Matrix. "
            "This comprehensive synthesis table compares our five core solids across every critical mathematical property. "
            "First, the cube: six equal square faces, twelve straight edges, eight sharp corners; it slides and stacks perfectly! "
            "Second, the cuboid: six rectangular faces, twelve straight edges, eight corners; it slides smoothly and stacks with great stability. "
            "Third, the cylinder: two flat circular faces, one curved surface, two curved edges, zero corners; it can roll, slide, and stack! "
            "Fourth, the cone: one flat circular base, one curved surface, one circular edge, and one pointed apex; it rolls in arcs and slides on its base. "
            "Fifth, the sphere: zero flat faces, one continuous curved surface, zero edges, and zero corners; it rolls smoothly in every direction! "
            "Notice the remarkable mathematical harmony: as flat faces give way to curved surfaces, sliding behavior transitions into rotational rolling! "
            "Every single three-dimensional solid around us follows these universal geometric principles of faces, edges, and corners. "
            "With this master matrix at your command, you possess the geometric insight to analyze and build toys, buildings, and machines throughout our physical world."
        ),
        "checkpoints": [
            {
                "q": "Which 3D solid possesses 2 flat circular faces, 1 curved surface, 2 curved edges, and 0 corners?",
                "options": [
                    "A cylinder",
                    "A sphere",
                    "A cube",
                    "A cuboid"
                ],
                "ans": "A cylinder",
                "explanation": "A cylinder has 2 flat circular bases, 1 curved lateral surface, 2 curved rims, and zero corners."
            },
            {
                "q": "How many flat faces and corners does a perfect sphere possess?",
                "options": [
                    "0 flat faces and 0 corners",
                    "1 flat face and 1 corner",
                    "6 flat faces and 8 corners",
                    "2 flat faces and 0 corners"
                ],
                "ans": "0 flat faces and 0 corners",
                "explanation": "A sphere is completely curved all around; it has zero flat faces, zero edges, and zero corners."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 9 TO 16 ===")
    assert len(slides_part2) == 8

    for s in slides_part2:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        speech = s["speech"]
        wc = len(speech.split())
        print(f"Slide {sid}: '{title}' -> {wc} words")
        assert 195 <= wc <= 215, f"Slide {sid} word count {wc} out of range 195-215!"
        
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint options != 4"
            assert cp["ans"] in cp["options"], f"Slide {sid} ans not in options"

    print("Part 2 verified successfully!")
