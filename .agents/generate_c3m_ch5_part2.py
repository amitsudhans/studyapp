# -*- coding: utf-8 -*-
"""Part 2 (Slides 9-16) for Class 3 Mathematics Chapter 5: Fun with Shapes."""

import json
import re

slides_part2 = [
    {
        "id": 9,
        "title": "Counting Nested Rectangles",
        "badge": "Rectangle Counting",
        "sim_id": "sim_counting_nested_rectangles",
        "description": "Discover systematic strategies to identify and count overlapping or composite rectangles embedded within grid figures.",
        "speech": (
            "When rectangles intersect or sit nested inside larger geometric boundaries, counting them requires a keen, systematic eye! Look at this "
            "window frame divided into smaller glass panes. At first glance, a casual observer might simply count the four small individual panes "
            "resting in each quadrant. But in geometry, combined regions also form valid rectangles! Two adjacent vertical panes joined together create "
            "a taller combined rectangle, and there are two such tall pairs. Similarly, two neighboring horizontal panes merge to form a wider combined "
            "rectangle, yielding two wide pairs. Finally, stepping back to take in the entire outer boundary reveals one master overarching rectangle! "
            "Adding all these distinct categories together—four individual unit panes, two tall horizontal pairs, two wide vertical pairs, plus the grand "
            "outer frame—yields a grand total of nine unique rectangles within this single simple window! This counting investigation teaches us an "
            "essential mathematical lesson: shapes do not merely exist in isolation; they combine dynamically to create new composite figures. Each "
            "identified rectangle faithfully preserves four straight boundary sides and four crisp ninety-degree corners. Use the interactive highlight "
            "tool on screen to uncover every hidden composite rectangle nestled inside our geometric grid puzzles with complete confidence!"
        ),
        "checkpoints": [
            {
                "q": "In a 2-by-2 pane window, how many total rectangles exist when counting single panes and combined pairs?",
                "options": ["9 rectangles", "4 rectangles", "5 rectangles", "8 rectangles"],
                "ans": "9 rectangles",
                "explanation": "There are 4 single panes, 2 horizontal pairs, 2 vertical pairs, and 1 large outer frame, making 4 + 2 + 2 + 1 = 9 rectangles."
            },
            {
                "q": "What rule ensures that a combined pair of smaller rectangles is still a rectangle?",
                "options": ["It has 4 straight sides meeting at 4 square corners", "It must have curved corners", "It must have 5 sides", "It must be a perfect square"],
                "ans": "It has 4 straight sides meeting at 4 square corners",
                "explanation": "Any closed four-sided polygon with straight edges meeting at four right angles is mathematically a rectangle."
            }
        ]
    },
    {
        "id": 10,
        "title": "Squares Versus Rectangles",
        "badge": "Square vs Rectangle",
        "sim_id": "sim_squares_versus_rectangles",
        "description": "Compare geometric properties of squares and rectangles across chessboards, ludo boards, and floor tiling.",
        "speech": (
            "Step into our game parlor to explore a famous geometric debate: what makes a square special compared to a rectangle? Take a close look at "
            "our classic wooden chessboard with its alternating dark and light tiles. Every single playing tile on this board has four straight edges "
            "that measure exactly identical in length, alongside four neat square corners. This balanced figure is a square! Now examine the rectangular "
            "scorecard lying nearby on the table. It also boasts four straight sides and four square corners, yet its length is noticeably longer than its "
            "width. Here lies the golden mathematical distinction: while both shapes possess four sides and four right angles, a rectangle only requires "
            "its opposite sides to be equal in length. A square, on the other hand, obeys a much stricter condition: all four of its sides must be strictly "
            "equal! Therefore, every square is actually a special type of rectangle with equal sides, but not every rectangle can be called a square. "
            "Observe tiles, board games, and wall posters to spot this elegant relationship. Use our interactive side-length slider to stretch a square "
            "into an elongated rectangle and watch how their geometric properties transform!"
        ),
        "checkpoints": [
            {
                "q": "Which property must be true for a shape to be classified as a square?",
                "options": ["All 4 sides must be equal in length", "Only 2 sides must be equal", "It must have 3 corners", "Opposite sides must have different lengths"],
                "ans": "All 4 sides must be equal in length",
                "explanation": "A square is a special rectangle where all four boundary sides are of identical length."
            },
            {
                "q": "Is every square mathematically a rectangle?",
                "options": ["Yes, because it has 4 straight sides and 4 square corners", "No, squares are triangles", "No, rectangles must have unequal sides", "Only if it is painted blue"],
                "ans": "Yes, because it has 4 straight sides and 4 square corners",
                "explanation": "A rectangle is defined by four right angles and opposite equal sides, which every square fully satisfies."
            }
        ]
    },
    {
        "id": 11,
        "title": "Matchstick Shape Tiling",
        "badge": "Matchstick Geometry",
        "sim_id": "sim_matchstick_shape_tiling",
        "description": "Build, share edges, and tile composite geometric figures using identical wooden matchsticks.",
        "speech": (
            "Slender wooden matchsticks provide an ideal hands-on tool for constructing polygons and discovering how geometric shapes share boundaries. "
            "To build a single freestanding square, you naturally need four identical matchsticks laid head to tail. But what happens if you wish to construct "
            "two identical squares joined side by side? You might guess you need eight sticks, but clever geometry saves resources! Because the two squares "
            "share one common internal boundary wall, you only need seven matchsticks in total! The shared wall serves both squares simultaneously. If you "
            "add a third connected square in a neat row, you share another common edge, requiring just ten matchsticks instead of twelve. We can also "
            "combine matchsticks to form equilateral triangles using three sticks. By pairing two triangles along a shared seam, we produce a handsome "
            "four-sided diamond called a rhombus. Tiling surfaces with matchsticks illustrates how shared edges economize perimeter lengths while building "
            "sturdy, interconnected spatial structures in our everyday architecture. Notice how adding each new enclosed cell requires fewer sticks than "
            "starting completely anew! Experiment with our interactive matchstick bench to drag, connect, and remove sticks, solving delightful shape-building "
            "puzzles and mastering boundary sharing principles in practical geometry!"
        ),
        "checkpoints": [
            {
                "q": "How many matchsticks are needed to build two connected squares that share one common wall?",
                "options": ["7 matchsticks", "8 matchsticks", "6 matchsticks", "9 matchsticks"],
                "ans": "7 matchsticks",
                "explanation": "The first square needs 4 sticks, and the second attached square needs only 3 additional sticks: 4 + 3 = 7 sticks."
            },
            {
                "q": "When two identical triangles share one complete side edge, what type of shape do they form together?",
                "options": ["A 4-sided quadrilateral", "A 6-sided hexagon", "A single large triangle", "A round circle"],
                "ans": "A 4-sided quadrilateral",
                "explanation": "Joining two triangles along one edge leaves four outer straight edges, forming a 4-sided quadrilateral (rhombus)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Square Corner Angles",
        "badge": "Square Corner Angles",
        "sim_id": "sim_square_corner_angles",
        "description": "Identify right angles using folded paper testers and compare corners that are smaller or larger than a square corner.",
        "speech": (
            "Look around the corners of doors, window panes, picture frames, and textbook covers. They all exhibit a crisp, sharp turn known in geometry "
            "as a square corner, or a right angle. We can construct an ingenious tool to test any corner using an ordinary scrap of paper! Fold the paper "
            "neatly in half once, creating a straight crease. Now, fold that creased edge onto itself so that the folded line lies perfectly flat along its "
            "own edge. Unfold nothing: the sharp ninety-degree corner of your folded paper tester is an exact standard square corner! Hold this tester against "
            "the corner of a wooden ruler, picture frame, or tile. It fits snugly with zero gap, proving beyond doubt it is a perfect square corner. Now test "
            "the sharp tip of a pair of partially opened scissors on your desk. The opening is narrower than our tester, showing it is smaller than a square "
            "corner. Next, inspect a reclining chair or wide clock hands at four o'clock: the angle opens much wider than our tester, proving it is larger "
            "than a square corner. Use our interactive angle tester to classify corners across everyday objects into equal, less, or greater than a square corner!"
        ),
        "checkpoints": [
            {
                "q": "What is the everyday geometric name for a sharp ninety-degree angle found on book covers and doors?",
                "options": ["A square corner (right angle)", "A round curve", "A wavy line", "A zero corner"],
                "ans": "A square corner (right angle)",
                "explanation": "A perpendicular corner where horizontal and vertical lines meet evenly is called a square corner or right angle."
            },
            {
                "q": "If an angle opens narrower than the folded paper tester, how is it described?",
                "options": ["Less than a square corner", "Greater than a square corner", "Equal to a square corner", "A straight line"],
                "ans": "Less than a square corner",
                "explanation": "An angle whose opening is sharper and tighter than a ninety-degree right angle is less than a square corner (acute)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Triangle Pattern Counts",
        "badge": "Triangular Tessellations",
        "sim_id": "sim_triangle_pattern_counts",
        "description": "Identify triangles across culinary shapes like samosas and count nested triangles within intricate geometric stars.",
        "speech": (
            "Triangles are the strongest, most stable polygons in the world of mathematics. Characterized by exactly three straight boundary edges and "
            "three sharp corners, triangles make frequent appearances on our dining plates and in architectural structures. Consider a warm golden samosa "
            "or a sandwich sliced diagonally from corner to corner: both display unmistakable triangular profiles! But when multiple triangles nestle "
            "together within decorative rangoli stars or geometric tessellations, counting them challenges our deductive reasoning. Consider a large "
            "equilateral triangle divided by internal lines into smaller upright and inverted triangles. To count them all without missing a single one, "
            "we group our count by scale! First, count all small, single-unit triangles pointing upwards and downwards across the figure. Next, look for "
            "medium composite triangles formed by grouping four smaller units together into a larger triangular frame. Finally, include the grand master "
            "triangle enclosing the entire assembly! This structured tiered counting technique ensures no hidden shape escapes detection. Whether analyzing "
            "bridge trusses or decorative wall paintings, triangular geometries bring both structural strength and aesthetic symmetry. Explore our interactive "
            "triangle star in the simulator to locate every hidden triangular region and record your findings with complete accuracy and sharp geometric insight!"
        ),
        "checkpoints": [
            {
                "q": "How many sides and corners does every triangle possess?",
                "options": ["3 sides and 3 corners", "4 sides and 4 corners", "3 sides and 4 corners", "2 sides and 3 corners"],
                "ans": "3 sides and 3 corners",
                "explanation": "By mathematical definition, every triangle is bounded by exactly 3 straight edges and 3 vertices."
            },
            {
                "q": "When cutting a square sandwich diagonally from one corner to the opposite corner, what shapes result?",
                "options": ["Two equal triangles", "Two small squares", "Two rectangles", "One circle and one triangle"],
                "ans": "Two equal triangles",
                "explanation": "A diagonal cut across a square splits it into two congruent right-angled isosceles triangles."
            }
        ]
    },
    {
        "id": 14,
        "title": "Paper Circle Center",
        "badge": "Folding Circle Center",
        "sim_id": "sim_paper_circle_center",
        "description": "Discover the exact center of a circular paper disc through sequential perpendicular crease folds.",
        "speech": (
            "Unlike polygons with straight edges and sharp corners, a circle is a completely smooth, continuous curved loop. How can we locate the exact "
            "heart or central balance point of a circle without using a ruler or compass? We can solve this elegant puzzle using simple paper folding! "
            "Cut a neat circular disc from a sheet of colored paper or use a flat round paper plate. First, fold the circular disc exactly in half, "
            "matching its curved curved perimeter edges together until they align flawlessly. Press down firmly to create a sharp straight crease, then unfold "
            "the disc. This straight crease line running directly across the circle from one edge to the other is called a diameter. Next, fold the circle in "
            "half once again, but this time along a completely different direction, pressing another crisp diameter crease into the paper. When you open the "
            "disc flat, look at where those two straight crease lines intersect! They cross each other at one single, undeniable point. That exact crossing "
            "intersection is the precise geometric center of your circle! Try balancing the unfolded disc on your pencil tip right at that crossing point to "
            "witness true rotational balance in action!"
        ),
        "checkpoints": [
            {
                "q": "What geometric feature is revealed where two fold creases intersect on a circular paper disc?",
                "options": ["The exact center of the circle", "A sharp corner", "A straight boundary edge", "A rectangular border"],
                "ans": "The exact center of the circle",
                "explanation": "Two diameter creases folded in different directions intersect at the circle's exact geometric center."
            },
            {
                "q": "What is the straight crease line called that divides a circle into two equal semicircular halves?",
                "options": ["A diameter", "A corner", "A side edge", "A perimeter"],
                "ans": "A diameter",
                "explanation": "A straight line segment passing through the center of a circle and touching both opposite edges is a diameter."
            }
        ]
    },
    {
        "id": 15,
        "title": "Polygon Side Counters",
        "badge": "Polygon Hierarchy",
        "sim_id": "sim_polygon_side_counters",
        "description": "Explore the multi-sided polygon family comparing sides and corners from 3-sided triangles up to 10-sided decagons.",
        "speech": (
            "As we explore geometry beyond basic shapes, we encounter an entire majestic family of closed straight-edged figures known as polygons! "
            "A polygon's identity is defined by the number of straight sides and corners it possesses. The simplest polygon is the classic three-sided triangle. "
            "Add one more straight side, and you enter the vast four-sided realm of quadrilaterals, which includes squares and rectangles. If we add a fifth side, "
            "we create a pentagon, resembling a sturdy school banner or home signpost with five sides and five corners. Add a sixth side, and you get a "
            "hexagon, the exact six-sided shape bees use to engineer honeycombs! A seven-sided figure is a heptagon, while an eight-sided figure is an "
            "octagon, instantly recognizable as a crimson road stop sign standing by a zebra crossing. Moving further, a nine-sided polygon is a nonagon, "
            "and a magnificent ten-sided figure is a decagon. Notice the universal mathematical rule linking all regular polygons: the number of straight "
            "boundary sides always equals the exact total number of sharp corners! Use our polygon transformer tool to dial the side counter from three to ten, watching "
            "how polygons gradually resemble smooth circles as their side count multiplies endlessly!"
        ),
        "checkpoints": [
            {
                "q": "How many straight sides and corners does a honeycomb hexagon have?",
                "options": ["6 sides and 6 corners", "5 sides and 5 corners", "8 sides and 8 corners", "7 sides and 7 corners"],
                "ans": "6 sides and 6 corners",
                "explanation": "A hexagon is a polygon with exactly 6 straight boundary sides and 6 vertices."
            },
            {
                "q": "What is the common mathematical property shared by all regular polygons?",
                "options": ["The number of sides equals the number of corners", "They have no corners", "They only have curved sides", "They all have 4 sides"],
                "ans": "The number of sides equals the number of corners",
                "explanation": "In any polygon, the number of straight boundary edges matches the number of vertices."
            }
        ]
    },
    {
        "id": 16,
        "title": "Tangram Puzzle Assembly",
        "badge": "Tangram Geometry",
        "sim_id": "sim_tangram_puzzle_assembly",
        "description": "Dissect a square into classic seven tangram tans to solve spatial silhouette puzzles and repeating border patterns.",
        "speech": (
            "To conclude our journey through foundational geometry, let us explore the legendary seven-piece dissection puzzle called the tangram! "
            "Originating centuries ago, a tangram begins as a single master square sliced into exactly seven geometric pieces known as tans. These seven "
            "pieces include two large triangles, one medium triangle, two small triangles, one square, and one slanted parallelogram. Every single piece "
            "has flat straight edges that can align smoothly against any other piece. The enchanting challenge of a tangram is to arrange all seven tans "
            "without any overlapping to recreate intricate silhouettes of sailing boats, leaping rabbits, graceful birds, and soaring rockets! In addition, "
            "examining each piece reveals how smaller triangles combine seamlessly to construct the square, the parallelogram, and even larger triangles. "
            "Furthermore, by alternating triangles and parallelograms in repeating sequences, we can construct striking geometric borders along the edges of rugs, "
            "curtains, and palace doorways. The tangram teaches us that boundless creativity and intricate spatial configurations arise from a simple, "
            "disciplined set of geometric shapes. Rotate, slide, and snap the seven colorful tangram pieces on your workspace in our simulator to bring "
            "playful geometric silhouettes to life, celebrating your remarkable mastery of shapes, edges, and corners!"
        ),
        "checkpoints": [
            {
                "q": "How many total geometric pieces (tans) comprise a standard classic tangram puzzle?",
                "options": ["7 pieces", "5 pieces", "8 pieces", "6 pieces"],
                "ans": "7 pieces",
                "explanation": "A standard tangram puzzle consists of exactly 7 pieces: 5 triangles, 1 square, and 1 parallelogram."
            },
            {
                "q": "How many of the seven tangram pieces are triangles?",
                "options": ["5 triangles", "3 triangles", "4 triangles", "2 triangles"],
                "ans": "5 triangles",
                "explanation": "The seven tans include 2 large triangles, 1 medium triangle, and 2 small triangles, totaling 5 triangles."
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Amma']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 2 (Slides 9-16)...")
    for s in slides_part2:
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
        
        wc = len(s["speech"].split())
        print(f"Slide {sid}: '{title}' -> Speech Word Count: {wc}")
        assert 195 <= wc <= 215, f"Slide {sid} word count out of range: {wc} (must be 195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint must have 4 options"
            assert cp["ans"] in cp["options"], f"Slide {sid} checkpoint answer '{cp['ans']}' not in options"
    print("Part 2 validation successful!")
