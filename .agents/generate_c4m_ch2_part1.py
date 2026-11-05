# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 2: Hide and Seek - Part 1 (Slides 1 to 8)
Generates slides 1 to 8 with strict word counts (195-215 words), 2 checkpoints each, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Vantage Point Perspectives",
        "lecture": (
            "Spatial awareness begins with understanding how our physical vantage point changes what we can observe in the surrounding "
            "environment. Imagine a lively afternoon game of hide and seek played across a school playground garden. Five young classmates "
            "scatter in different directions to find clever concealing spots, while one designated seeker closes their eyes by a central "
            "tree trunk. One young explorer climbs high up into the leafy branches of a tall banyan tree, while another hider ducks "
            "low behind a wide brick boundary wall, and a third child squeezes under a wooden park bench. From high up in the tree, "
            "the climbing observer enjoys an elevated bird's-eye vantage point looking straight down. From this superior height, "
            "hidden areas that are completely invisible to someone standing on the flat ground suddenly become fully exposed. The "
            "seeker standing down on the grass cannot look through opaque brick walls or around solid pillars because light travels in "
            "straight lines, creating blocked lines of sight called blind spots. However, the high-perched climber can easily spot who "
            "is crouching behind the low shrubs below. Understanding line-of-sight perspectives helps young mathematicians visualize "
            "how physical position, elevation, and solid obstacles govern what observers can see in three-dimensional space."
        ),
        "checkpoints": [
            {
                "question": "Why can an observer perched high in a tree see someone hiding behind a low garden wall?",
                "options": ["Because tree leaves are transparent", "Because the elevated vantage point provides a clear line of sight over the wall", "Because sound travels faster from trees", "Because low walls disappear from above"],
                "answer": 1,
                "explanation": "An elevated vantage point allows the observer's straight line of sight to look over the top of low obstacles."
            },
            {
                "question": "What creates a blind spot for an observer standing on flat ground during hide and seek?",
                "options": ["Open grassy lawns", "Opaque solid obstacles that block straight lines of sight", "Bright sunlight shining overhead", "Clear glass windows"],
                "answer": 1,
                "explanation": "Light travels in straight lines; solid, opaque obstacles block sight lines, creating invisible blind spots behind them."
            }
        ]
    },
    {
        "id": 2,
        "title": "Object View Angles",
        "lecture": (
            "Every three-dimensional solid object in our everyday physical world presents dramatically different appearances depending "
            "on the exact angle from which it is viewed. To understand this fundamental geometric principle, let us examine a standard "
            "rectangular construction brick resting flat on a classroom table. When young architects sit around the sturdy wooden table "
            "and sketch the brick without moving the brick itself, each person draws an entirely different picture based on their viewing "
            "position. An observer standing directly in front of the long rectangular face views the front view, which shows a wide, low "
            "rectangular surface with horizontal mortar joints. Another student seated at the narrow end looks at the side view, observing "
            "a smaller, nearly square rectangle with different proportions. Meanwhile, a third observer looking directly down from above "
            "observes the top view, revealing the wide upper face often featuring a shallow indentation called a frog. None of these "
            "individual two-dimensional drawings captures the complete solid brick by itself. Instead, true three-dimensional spatial "
            "understanding requires combining all three orthogonal projections: the top view, the front view, and the side view. By "
            "systematically comparing multiple view angles and projections, young learners master how flat two-dimensional profiles "
            "combine to define solid, three-dimensional physical objects in the real world."
        ),
        "checkpoints": [
            {
                "question": "How many primary orthogonal view angles are standardly used to represent a 3D object?",
                "options": ["1 view only", "2 views (left and right)", "3 views (top, front, and side)", "8 views"],
                "answer": 2,
                "explanation": "Engineers and architects rely on 3 primary orthogonal views: top view, front view, and side view."
            },
            {
                "question": "When looking directly down at a brick resting flat on a table, which view are you observing?",
                "options": ["The front view", "The side view", "The top view (bird's-eye view)", "The internal view"],
                "answer": 2,
                "explanation": "Looking perpendicularly downward from directly above an object reveals its top view."
            }
        ]
    },
    {
        "id": 3,
        "title": "Identifying Common Views",
        "lecture": (
            "Now let us apply our sharp observational skills to classify the view angles of familiar everyday household and school "
            "objects in detail. Consider a modern television set: looking straight at its luminous flat screen displays the front view, "
            "whereas looking from directly overhead reveals a very thin, narrow rectangular strip representing its top view. Next, "
            "examine a comfortable upholstered living room sofa. The front view clearly shows the soft seating cushions, armrests, and "
            "decorative pillows; looking at it from the side reveals an L-shaped silhouette showing the slanted backrest and arm thickness; "
            "and looking from directly above presents a wide rectangular boundary divided into cushion segments. Similarly, carefully "
            "examine a bright yellow school bus parked outside. The side view reveals a long yellow rectangle featuring a row of square "
            "passenger windows and two black rubber wheels. The front view shows the wide windshield, dual headlights, front bumper, "
            "and rearview mirrors. The top view displays a long smooth roof often marked with emergency exit hatches. Whether inspecting "
            "a protective motorcycle helmet, a round pencil top, a rotary pizza cutter, or a wooden chair, identifying whether a drawing "
            "depicts the top, front, or side view trains our visual deduction and spatial reasoning skills immensely."
        ),
        "checkpoints": [
            {
                "question": "Which view of a school bus reveals the long line of passenger windows and two wheels along the ground?",
                "options": ["The top view", "The front view", "The side view", "The bottom view"],
                "answer": 2,
                "explanation": "The side view of a bus stretches horizontally, showing the entire row of side passenger windows and wheels."
            },
            {
                "question": "Looking directly down at an unsharpened wooden pencil resting vertically on its eraser reveals which shape?",
                "options": ["A long rectangle", "A small circle or regular hexagon (top view)", "A triangle", "A curved arch"],
                "answer": 1,
                "explanation": "Viewed directly from above, a vertical pencil shows only its circular or hexagonal cross-section top view."
            }
        ]
    },
    {
        "id": 4,
        "title": "Matching Geometric Views",
        "lecture": (
            "Once we can identify views of familiar everyday objects, we can advance to geometric projections of pure mathematical "
            "solids in space. Every regular three-dimensional shape produces characteristic two-dimensional silhouette shadows depending "
            "on the direction of observation. Consider a standard solid cube: every single face is an identical square, so its top view, "
            "front view, and side view all appear as congruent squares of equal dimensions without any variation. Next, examine a "
            "triangular prism resting on one of its flat rectangular faces on a flat surface. Looking at it directly from the front "
            "end shows an upright triangle. Looking from the side reveals a broad rectangle, and looking from directly above also presents "
            "a rectangle divided down the middle by the top ridge edge. Now examine a square pyramid standing upright on its square base. "
            "Its front view and side view both appear as identical isosceles triangles tapering to a sharp top apex. However, its top "
            "view reveals a flat square perimeter containing diagonal crease lines meeting at a central point where the sloping triangular "
            "faces converge. Matching flat two-dimensional profiles to their solid parents helps young mathematicians decode blueprints, "
            "technical schematics, and geometric engineering drawings with remarkable confidence, clarity, and speed."
        ),
        "checkpoints": [
            {
                "question": "What 2D shape is observed when looking at the front view and side view of an upright square pyramid?",
                "options": ["A square", "A circle", "An isosceles triangle", "A hexagon"],
                "answer": 2,
                "explanation": "The triangular sloping faces of a square pyramid appear as flat triangles from both front and side views."
            },
            {
                "question": "Which 3D solid produces identical square silhouettes from its top, front, and side views?",
                "options": ["A cylinder", "A cube", "A triangular prism", "A cone"],
                "answer": 1,
                "explanation": "Because all six faces of a cube are identical squares, its top, front, and side projections are all squares."
            }
        ]
    },
    {
        "id": 5,
        "title": "Matchbox Block Buildings",
        "lecture": (
            "Hands-on architectural construction provides a wonderful creative laboratory for exploring three-dimensional architectural "
            "space in the classroom. In the classroom workshop, young builders collect empty cardboard matchboxes to construct miniature "
            "multi-tiered buildings, bridges, and tower complexes. Each matchbox serves as an identical rectangular cuboid unit with "
            "distinct dimensions: a broad top face, a long narrow side edge, and a short rectangular end face. When stacking matchboxes "
            "together, young architects can orient them in various creative directions to create stepped terrace towers, castle "
            "battlements, arched gateways, or cantilevered balconies with ease. Sturdy foundation bases support vertical columns effectively. "
            "For example, placing four matchboxes flat in a two-by-two square forms a wide, stable foundation podium. Stacking two "
            "matchboxes on the second level and a single matchbox on the third tier creates a magnificent stepped pyramid structure. "
            "Every upper block must rest securely upon the solid surfaces of the blocks situated beneath it. Furthermore, building composite "
            "block models prepares young minds for real architectural engineering, where complex skyscrapers and civic monuments are "
            "assembled by combining standardized modular rectangular units into sturdy, harmonious three-dimensional designs that inspire "
            "our imagination. This hands-on geometric modeling brings physical principles of stability and form alive."
        ),
        "checkpoints": [
            {
                "question": "What standard 3D geometric solid is an individual matchbox shaped like?",
                "options": ["A sphere", "A rectangular cuboid", "A triangular pyramid", "A cylinder"],
                "answer": 1,
                "explanation": "A matchbox has 6 flat rectangular faces, 12 straight edges, and 8 vertices, making it a classic cuboid."
            },
            {
                "question": "Why must upper matchboxes in a stepped tower rest upon solid blocks beneath them?",
                "options": ["To make the tower transparent", "To ensure physical balance and structural stability under gravity", "To change their rectangular shape", "To reduce the total number of faces"],
                "answer": 1,
                "explanation": "Gravity requires elevated blocks to be physically supported by lower foundation blocks to prevent tipping."
            }
        ]
    },
    {
        "id": 6,
        "title": "Multi-Angle Building Views",
        "lecture": (
            "After constructing a matchbox building, how can young architects share their structural design with someone located far away "
            "across the globe? They draw multi-angle perspective projections! When viewing a composite block building from the front, certain "
            "tiers and vertical columns line up directly behind one another. Looking directly at eye level from the front produces the front "
            "elevation, showing which columns rise one, two, or three blocks high. Walking around to the opposite side yields the back view, "
            "which often reverses the left-to-right arrangement of the columns while maintaining their true vertical heights. Moving ninety "
            "degrees to the left or right side reveals the side elevation, showing the building's depth and staircase profile with clarity. "
            "Finally, climbing above to look directly downward produces the plan or top view. In the top view, all vertical height completely "
            "disappears from sight, and we observe only the horizontal footprint grid indicating which floor tiles are occupied by blocks. "
            "A clever classmate can take these three flat drawings and successfully reconstruct the exact physical model without ever seeing "
            "the original structure in person. Translating between 3D solid blocks and 2D orthogonal drawings is the core universal language "
            "of global architecture, manufacturing, and mechanical engineering everywhere."
        ),
        "checkpoints": [
            {
                "question": "What information about a 3D block building disappears when drawing its overhead top view?",
                "options": ["Its horizontal width", "Its vertical height", "Its color", "Its footprint boundaries"],
                "answer": 1,
                "explanation": "In an overhead top view (plan view), all vertical elevations flatten, showing only horizontal footprints."
            },
            {
                "question": "How does the back view of an asymmetrical stepped building compare to its front view?",
                "options": ["It becomes completely round", "Its left-to-right column order is horizontally reversed", "Its height doubles", "It shows the roof only"],
                "answer": 1,
                "explanation": "Viewing a structure from the opposite side reverses the left and right positions of asymmetrical columns."
            }
        ]
    },
    {
        "id": 7,
        "title": "Classroom Spatial Mapping",
        "lecture": (
            "Let us now bring our observational perspective inside our own daily learning environment: the lively school classroom. "
            "Imagine a curious garden cat leaping up onto an open classroom window sill on a bright, sunny morning. Perched up high on "
            "the window ledge, the feline looks inward across the entire room to locate a familiar smiling face among the students. From "
            "this elevated window perch, the cat's sight line surveys the room like an aerial map laid out on a table. The classroom "
            "floor is neatly organized into regular rows and columns of wooden desks, with the teacher's podium at the front, a wide "
            "green chalkboard mounted on the north wall, and a colorful library bookshelf situated near the rear doorway. To describe "
            "where any specific student sits in the room, observers cannot just point their fingers randomly; they need clear, precise "
            "spatial language that everyone understands. Is the student seated near the front row or toward the back? Are they positioned "
            "by the sunny window side or along the door aisle? Converting the physical layout of desks into a structured two-dimensional "
            "floor plan allows young mathematicians to connect real three-dimensional living spaces with systematic navigational maps, "
            "architectural blueprints, and coordinate systems with immense confidence."
        ),
        "checkpoints": [
            {
                "question": "What does a classroom floor plan represent when drawn on a flat sheet of paper?",
                "options": ["A side view of the ceiling", "A top-down 2D map showing the arrangement of desks, doors, and boards", "A picture of the playground outside", "A list of textbook chapters"],
                "answer": 1,
                "explanation": "A classroom floor plan is an overhead top-down map showing the spatial layout of furniture and pathways."
            },
            {
                "question": "Why is an elevated window sill a useful vantage point for surveying an entire classroom?",
                "options": ["Because windows make desks invisible", "Because the elevated height provides an unobstructed sight line over rows of desks", "Because it is darker near windows", "Because the room appears upside down"],
                "answer": 1,
                "explanation": "An elevated perch looks over the tops of desks and chairs, reducing visual obstructions across the room."
            }
        ]
    },
    {
        "id": 8,
        "title": "Desk Positional Terms",
        "lecture": (
            "To navigate and locate objects within structured spaces with clarity, mathematicians use standardized, systematic positional "
            "language. In our classroom seating arrangement, desks are arranged in orderly horizontal rows running across from left to right, "
            "and straight vertical columns running from the front of the room to the back. We identify rows using ordinal numbers: the row "
            "nearest to the chalkboard is the first row, followed by the second row, third row, and fourth row stretching toward the back "
            "wall. Similarly, we number columns from left to right across the classroom: column one on the left, column two in the middle, "
            "and column three on the right. Using this systematic framework, we can pinpoint any desk without ambiguity. For instance, the "
            "phrase 'the third desk in the first row' guides us immediately to the front of the classroom, counting three desks inward from "
            "the left side. Describing another seat as 'the middle desk of the second row' highlights both row depth and central horizontal "
            "alignment perfectly. Positional terms like 'front', 'back', 'left', 'right', 'between', and 'adjacent' eliminate confusion "
            "and form the essential verbal foundation for coordinate geometry, grid navigation, and digital mapping systems used throughout "
            "modern science and everyday life."
        ),
        "checkpoints": [
            {
                "question": "Which desk is located at 'the third desk in the first row'?",
                "options": ["A desk in the back corner", "The third desk from the left in the row closest to the front board", "A desk outside the door", "The middle desk in the third row"],
                "answer": 1,
                "explanation": "The first row is at the front, and the third desk is counted along that row from the left."
            },
            {
                "question": "Why do mathematicians use formal row and column numbers instead of vague directions like 'over there'?",
                "options": ["To make the room look larger", "To specify exact, unambiguous locations that anyone can find reliably", "To use more words", "To keep secrets"],
                "answer": 1,
                "explanation": "Standardized row and column coordinates provide unique, unambiguous locations that eliminate confusion."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part1:
        wc = len(s['lecture'].split())
        title_wc = len(s['title'].split())
        print(f"Slide {s['id']}: '{s['title']}' (Title: {title_wc} words, Lecture: {wc} words)")
        assert 1 <= title_wc <= 3, f"Title length violation in slide {s['id']}"
        assert 195 <= wc <= 215, f"Lecture word count {wc} out of range in slide {s['id']}"
    print("Part 1: All 8 slides verified successfully!")
