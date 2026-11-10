# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 3 Mathematics - Chapter 2: Toy Joy
Strict requirements:
- Titles: 1 to 3 words each
- Spoken text: strictly 195 to 215 words each
- Tone: Pure Indian male teacher academic, encouraging, didactic narration
- Zero human character names (no Raghav, Meera, Dhruv, etc.)
- Zero lecturer personas (no Dr., Sir, Madam, Mr., Mrs., Miss)
- 2 checkpoints per slide with 4 options each, correct answer, and explanation
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Crafting 3D Shapes",
        "badge": "Creative Geometry",
        "sim_id": "sim_box_bottle_craft",
        "description": "Discover how everyday discarded containers, cardboard boxes, and bottles transform into animal faces while introducing 3D geometric shapes.",
        "speech": (
            "Welcome young mathematicians and creative inventors to our fascinating exploration of solid geometric shapes in Chapter 2, Toy Joy. "
            "Look around your home or classroom, and you will notice that our world is brimming with three-dimensional containers. "
            "Instead of throwing away empty discarded cartons, tin cans, and plastic bottles, "
            "curious young crafters can transform these everyday objects into playful animal and bird faces! "
            "Consider a square cardboard carton: by pasting paper ears, button eyes, and a button nose, "
            "it turns into an adorable puppy face while embodying the mathematical geometry of a solid cube. "
            "Next, take an elongated shoebox: adding a pink snout and floppy ears transforms it into a cheerful pig, "
            "demonstrating the rectangular structure of a cuboid. "
            "Now examine a round metal soup can or beverage container: painting whiskers and triangular ears creates a charming cat, "
            "revealing the curved elegance of a cylinder with two flat circular bases. "
            "Finally, rolling stiff chart paper into a pointed party hat crafts the sharp beak of a bird, "
            "exemplifying the conical geometry of a cone. "
            "Through creative toy crafting, children discover that geometric solids are not distant textbook abstractions, "
            "but tangible, functional building blocks that shape the joyful physical world all around us every single day."
        ),
        "checkpoints": [
            {
                "q": "Which 3D geometric shape is represented by a round tin can with two flat circular ends?",
                "options": [
                    "A cylinder",
                    "A cube",
                    "A cone",
                    "A triangular prism"
                ],
                "ans": "A cylinder",
                "explanation": "A tin can has a curved side surface and two parallel flat circular bases, which defines a cylinder."
            },
            {
                "q": "What geometric shape does a rolled pointed paper party hat resemble?",
                "options": [
                    "A cone",
                    "A cuboid",
                    "A cylinder",
                    "A sphere"
                ],
                "ans": "A cone",
                "explanation": "A pointed party hat has a circular flat base tapering smoothly to a sharp top apex, defining a cone."
            }
        ]
    },
    {
        "id": 2,
        "title": "Anatomy Of 3D",
        "badge": "Structural Features",
        "sim_id": "sim_cube_anatomy",
        "description": "Identify and count the foundational structural parts of solid shapes: flat faces, straight edges, and sharp corners.",
        "speech": (
            "To understand three-dimensional geometry like true mathematical architects, "
            "we must investigate the precise anatomical parts that construct every solid object in space. "
            "Let us hold a solid wooden cube in our hands and examine its three fundamental anatomical features: "
            "faces, edges, and corners, which mathematicians also formally call vertices in higher geometry. "
            "First, run your palm smoothly across the flat exterior surfaces of the wooden cube. "
            "Each flat surface is called a face; a standard cube possesses exactly six identical square faces: "
            "top, bottom, front, back, left, and right. "
            "Next, trace your index finger along the boundary lines where two flat faces meet together. "
            "These straight boundary lines are called edges; a cube has exactly twelve straight edges of equal length. "
            "Finally, gently touch the sharp, pointed tips where three distinct edges intersect together at a single point. "
            "These pointed meeting points are called corners or vertices; a cube has exactly eight sharp corners. "
            "Remember this essential anatomical triad: six flat faces, twelve straight edges, and eight pointed corners! "
            "Recognizing these three foundational geometric properties enables young students to analyze, compare, and construct "
            "all varieties of polyhedra and geometric figures across mathematics and architectural engineering with complete scientific confidence."
        ),
        "checkpoints": [
            {
                "q": "How many flat faces does a standard solid cube have?",
                "options": [
                    "6 flat faces",
                    "8 flat faces",
                    "12 flat faces",
                    "4 flat faces"
                ],
                "ans": "6 flat faces",
                "explanation": "A cube has six flat square faces: top, bottom, front, back, left, and right."
            },
            {
                "q": "What is the mathematical name for the sharp pointed tips where three edges meet on a cube?",
                "options": [
                    "Corners or vertices",
                    "Curved surfaces",
                    "Perimeters",
                    "Diagonal planes"
                ],
                "ans": "Corners or vertices",
                "explanation": "The sharp points where three edges meet are called corners, or vertices in formal mathematics."
            }
        ]
    },
    {
        "id": 3,
        "title": "Rocket Shape Assembly",
        "badge": "Spatial Models",
        "sim_id": "sim_rocket_assembly",
        "description": "Analyze a multi-shape space rocket model by identifying, counting, and describing the relative positions of its geometric components.",
        "speech": (
            "One of the most thrilling hands-on activities in our geometric toy laboratory is assembling and analyzing a space rocket model! "
            "Imagine building a magnificent toy spacecraft by combining several different three-dimensional blocks together on the classroom table. "
            "At the very top of the rocket sits a bright yellow cone, serving as the aerodynamic nose cone that pierces through the air. "
            "Directly beneath the cone rests a tall, sturdy blue cylinder, forming the central fuselage body and payload chamber of the rocket. "
            "At the base of the rocket sits a solid red cube, anchoring the core engine structure to ensure stability during launch. "
            "Attached to the lateral sides of this central core are two slender grey cuboids, functioning as aerodynamic booster fins to maintain flight balance. "
            "When young mathematicians inspect this assembled spacecraft, they practice both precise numerical counting and spatial positioning. "
            "They record: one cone at the apex, one cylinder in the middle, one cube at the base, and two cuboid stabilizer fins, "
            "making a grand total of five geometric components combined into a single unified flying machine! "
            "Analyzing how basic geometric blocks stack and lock together reveals how complex real-world aerospace vehicles are designed and engineered."
        ),
        "checkpoints": [
            {
                "q": "Which geometric shape is used as the top nose cone of the assembled toy space rocket?",
                "options": [
                    "A cone",
                    "A cylinder",
                    "A cuboid",
                    "A sphere"
                ],
                "ans": "A cone",
                "explanation": "The pointed, tapering shape at the apex of the rocket model is a cone."
            },
            {
                "q": "How many total geometric blocks are combined to build the rocket model (1 cone, 1 cylinder, 1 cube, 2 cuboids)?",
                "options": [
                    "5 blocks",
                    "4 blocks",
                    "6 blocks",
                    "7 blocks"
                ],
                "ans": "5 blocks",
                "explanation": "Adding all components: 1 cone + 1 cylinder + 1 cube + 2 cuboids = 5 geometric blocks."
            }
        ]
    },
    {
        "id": 4,
        "title": "Toy Engine Components",
        "badge": "Component Counting",
        "sim_id": "sim_toy_engine",
        "description": "Examine a colorful toy railway engine to count and categorize specific component shapes and their functional roles.",
        "speech": (
            "Let us now travel to the toy shop to inspect another delightful mechanical marvel: a colorful wooden toy railway engine! "
            "A toy locomotive is an intricate composite structure assembled from diverse geometric shapes painted in bright primary colors. "
            "When young observers analyze the train engine carefully, they can decompose its complex body into distinct geometric parts. "
            "The main steam boiler is constructed from a long, smooth red cylinder that lies horizontally along the chassis. "
            "Perched atop the boiler is a small yellow cone that functions as the puffing smokestack chimney. "
            "Behind the boiler sits a tall grey cuboid that forms the sheltered driver's cabin, complete with rectangular window cutouts. "
            "Beneath the cabin rests a solid blue cube that serves as the sturdy coal tender storage box. "
            "Finally, supporting the entire locomotive chassis are six small, flat black cylinders that rotate smoothly as train wheels on the railway track. "
            "By systematically sorting and tallying these parts, students count one horizontal cylinder, one cone smokestack, "
            "one cuboid driver cabin, one cube tender, and six wheel cylinders. "
            "Overall, carefully analyzing toy train components trains young inquisitive observers to recognize elementary geometric solids inside complex everyday machinery and real-world vehicles."
        ),
        "checkpoints": [
            {
                "q": "What 3D geometric shape forms the rotating wheels of the toy railway locomotive?",
                "options": [
                    "Flat circular cylinders",
                    "Sharp square cubes",
                    "Pointed cones",
                    "Rectangular cuboids"
                ],
                "ans": "Flat circular cylinders",
                "explanation": "Wheels are circular discs with depth, which mathematically represents short flat cylinders."
            },
            {
                "q": "Which shape serves as the tall driver's cabin on the toy train engine?",
                "options": [
                    "A grey cuboid",
                    "A round sphere",
                    "A yellow cone",
                    "A wooden pyramid"
                ],
                "ans": "A grey cuboid",
                "explanation": "The driver's cabin is constructed from an upright rectangular box, representing a cuboid."
            }
        ]
    },
    {
        "id": 5,
        "title": "Cube Versus Cuboid",
        "badge": "Special Relationship",
        "sim_id": "sim_cube_is_cuboid",
        "description": "Explore the foundational geometric principle that reveals why every cube is a special, perfectly balanced type of cuboid.",
        "speech": (
            "One of the most profound and elegant discoveries in primary school geometry is the special relationship between cubes and cuboids. "
            "Many young learners initially think that a cube and a cuboid are completely unrelated shapes. "
            "However, careful mathematical analysis reveals a beautiful truth: a cube is actually a special type of cuboid! "
            "Let us investigate why this is true by examining their shared geometric definitions. "
            "Both a cube and a cuboid have exactly six flat faces, twelve straight edges, and eight sharp corners. "
            "In a general cuboid, such as a rectangular cereal box or a textbook, opposite faces are equal rectangles. "
            "The length, width, and height of a general cuboid can all have completely different measurements. "
            "Now, imagine shrinking the longer length and expanding the shorter width until all three dimensions become perfectly equal: "
            "length equals width, which equals height! "
            "When this happens, every single one of the six rectangular faces becomes an identical square. "
            "The shape is now called a cube! "
            "Because a square is a special type of rectangle, a cube satisfies every single rule required of a cuboid. "
            "Understanding that every cube is a cuboid—but not every cuboid is a cube—deepens mathematical classification skills."
        ),
        "checkpoints": [
            {
                "q": "Why is a cube considered a special type of cuboid?",
                "options": [
                    "All of its six rectangular faces are equal squares with identical lengths",
                    "It has completely round curved edges with no corners",
                    "It can roll like a ball across a flat surface",
                    "It has only three faces instead of six"
                ],
                "ans": "All of its six rectangular faces are equal squares with identical lengths",
                "explanation": "A cube satisfies all cuboid rules, with the special property that length = width = height, making all 6 faces squares."
            },
            {
                "q": "Is every cuboid also a cube?",
                "options": [
                    "No, a cuboid is only a cube when all its faces are equal squares",
                    "Yes, every single rectangular box is always an exact cube",
                    "Yes, all geometric shapes are cubes",
                    "No, cuboids have zero flat faces"
                ],
                "ans": "No, a cuboid is only a cube when all its faces are equal squares",
                "explanation": "A general cuboid can have unequal rectangular faces; it only becomes a cube when all sides are equal."
            }
        ]
    },
    {
        "id": 6,
        "title": "Flat Curved Faces",
        "badge": "Surface Properties",
        "sim_id": "sim_flat_curved_surfaces",
        "description": "Distinguish between flat faces that slide smoothly and curved surfaces that roll continuously across inclined surfaces.",
        "speech": (
            "When solid geometric shapes interact with flat surfaces or ramps, their physical behavior is determined entirely by surface curvature! "
            "Solid shapes possess two fundamentally different kinds of surfaces: flat faces and curved surfaces. "
            "A flat face is completely plane, level, and straight, like the cover of a hardcover book or the tabletop. "
            "When you push an object with flat faces—such as a wooden cube or a rectangular matchbox—down an inclined wooden ramp, "
            "it slides smoothly along its base without rotating. "
            "In sharp contrast, a curved surface is continuously rounded and bent, like the outer skin of an orange or a cricket ball. "
            "When you place a sphere on a ramp, it rolls rapidly down the slope because it has zero flat faces and zero straight edges! "
            "Even more fascinating are shapes that possess both types of surfaces simultaneously. "
            "Consider a cylinder: its rounded side allows it to roll smoothly like a rolling pin, "
            "yet its two flat circular ends allow it to slide or stack securely like a coin! "
            "Similarly, a cone rolls in circular loops on its curved flank, but stands upright on its flat circular base. "
            "Observing rolling and sliding reveals how surface geometry governs mechanical motion in physical toys."
        ),
        "checkpoints": [
            {
                "q": "Which of the following geometric shapes has both flat circular faces and a curved surface?",
                "options": [
                    "A cylinder",
                    "A cube",
                    "A sphere",
                    "A cuboid"
                ],
                "ans": "A cylinder",
                "explanation": "A cylinder has two flat circular faces (top and bottom) and one smoothly curved side surface."
            },
            {
                "q": "Why does a sphere roll effortlessly down an inclined ramp in any direction?",
                "options": [
                    "It has a continuously curved surface with zero flat faces and zero edges",
                    "It is filled with magnetic liquid inside",
                    "It has eight sharp corners that grip the ground",
                    "It is made of light transparent paper"
                ],
                "ans": "It has a continuously curved surface with zero flat faces and zero edges",
                "explanation": "A sphere consists solely of a continuous curved surface, allowing it to roll smoothly in all directions."
            }
        ]
    },
    {
        "id": 7,
        "title": "Shape Mystery Descriptions",
        "badge": "Spatial Communication",
        "sim_id": "sim_mystery_shape_describer",
        "description": "Play a collaborative spatial construction game where precise verbal descriptions enable partners to duplicate models blindly.",
        "speech": (
            "Mathematics is not only about numbers and formulas; it is also a powerful language of precise spatial communication! "
            "In Chapter 2, students engage in an exhilarating classroom challenge called the Collaborative Construction Game. "
            "In this game, two student partners sit back-to-back so they cannot see each other's desk. "
            "The first student, acting as the architect, selects three geometric shapes and builds a secret multi-tier structure behind a cardboard screen. "
            "For example, the architect places a wide wooden cuboid flat on the table, stacks a wooden cylinder vertically on top of it, "
            "and crowns the cylinder with a pointed yellow cone. "
            "Now comes the true mathematical challenge: the architect must verbally describe this construction to the partner "
            "using clear geometric terminology and precise spatial position words! "
            "The architect says: 'First, lay a rectangular cuboid flat as the foundation. "
            "Next, place a cylinder upright on the center of the cuboid's top face. "
            "Finally, balance a cone on top of the cylinder with its sharp apex pointing upward.' "
            "By listening carefully and interpreting spatial terms like 'base', 'center', and 'apex', "
            "the partner replicates the exact structure without ever seeing the original model! "
            "This activity proves how clear mathematical vocabulary enables flawless cooperative problem-solving."
        ),
        "checkpoints": [
            {
                "q": "What is the primary skill developed by playing the back-to-back shape construction game?",
                "options": [
                    "Precise spatial vocabulary and verbal geometric communication",
                    "Running faster during outdoor sports races",
                    "Memorizing long lists of multiplication tables",
                    "Painting pictures with watercolor paints"
                ],
                "ans": "Precise spatial vocabulary and verbal geometric communication",
                "explanation": "The game trains students to describe 3D positions and shapes clearly so partners can replicate them sight unseen."
            },
            {
                "q": "If a cone is balanced on top of a cylinder with its sharp tip facing the ceiling, what is the tip called?",
                "options": [
                    "The apex or top corner",
                    "The circular base",
                    "The horizontal perimeter",
                    "The rectangular side"
                ],
                "ans": "The apex or top corner",
                "explanation": "The pointed sharp tip of a cone opposite its circular base is called the apex."
            }
        ]
    },
    {
        "id": 8,
        "title": "Classroom Shape Hunt",
        "badge": "Environmental Data",
        "sim_id": "sim_classroom_shape_hunt",
        "description": "Embark on an interactive shape safari around the classroom to discover and record real-world 3D geometric figures.",
        "speech": (
            "Armed with our knowledge of solid geometric anatomy, let us now embark on an exciting Classroom Shape Hunt! "
            "Every classroom is an extraordinary treasure trove of geometric forms waiting to be discovered by observant young detectives. "
            "Carrying tally clipboards, students survey the room to identify items that correspond to our core 3D shapes: "
            "cubes, cuboids, cylinders, cones, and spheres. "
            "Look at the teacher's desk: a rectangular chalk box and thick dictionary represent cuboids. "
            "Inspect the writing board: colorful spherical marbles and a world globe on the bookshelf represent perfect spheres. "
            "Glance toward the stationery stand: wooden pencils, glue sticks, and cylindrical drinking water bottles display round cylindrical barrels. "
            "Notice the party decorations or sharpened pencil tips: pointed cones catch our eye. "
            "Students also discover fascinating composite objects constructed from multiple shapes: "
            "a flashlight combines a cylindrical handle with a conical lamp head; "
            "a sharpened pencil combines a hexagonal cylinder body with a conical graphite point! "
            "By tallying their discoveries, students record which shapes appear most frequently—usually cuboids and cylinders—and which appear least often. "
            "Conducting an active classroom shape hunt demonstrates vividly that solid geometry is alive, useful, and thriving in every corner of our daily environment."
        ),
        "checkpoints": [
            {
                "q": "Which 3D shape is typically represented by a standard classroom world globe?",
                "options": [
                    "A sphere",
                    "A cylinder",
                    "A cube",
                    "A cone"
                ],
                "ans": "A sphere",
                "explanation": "A world globe is a completely round, symmetrical 3D ball, which is a sphere."
            },
            {
                "q": "What two 3D shapes combine to form a newly sharpened wooden pencil?",
                "options": [
                    "A cylinder (body) and a cone (sharpened tip)",
                    "A cube and a sphere",
                    "Two cuboids stacked together",
                    "A pyramid and a sphere"
                ],
                "ans": "A cylinder (body) and a cone (sharpened tip)",
                "explanation": "The main wooden shaft of a pencil is a cylinder, while the sharpened writing tip forms a cone."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 1 TO 8 ===")
    assert len(slides_part1) == 8

    for s in slides_part1:
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

    print("Part 1 verified successfully!")
