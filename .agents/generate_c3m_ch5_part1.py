# -*- coding: utf-8 -*-
"""Part 1 (Slides 1-8) for Class 3 Mathematics Chapter 5: Fun with Shapes."""

import json
import re

slides_part1 = [
    {
        "id": 1,
        "title": "Rangoli Dot Grid",
        "badge": "Dot Grid Rangoli",
        "sim_id": "sim_rangoli_dot_grid",
        "description": "Recreate traditional dot-grid floor patterns using interconnected squares, equilateral triangles, and smooth circular loops.",
        "speech": (
            "Welcome curious young learners to our wonderful geometry laboratory! Traditional festive floor art called rangoli brings math to vibrant "
            "life right before our eyes. Look closely at this pristine dot grid drawn with dry rice flour across the welcoming courtyard floor. By connecting "
            "rows and columns of evenly spaced dots with steady chalk strokes, an intricate dance of classic shapes begins to emerge. Four neighboring dots "
            "joined together by four straight lines form a perfect square. When we connect three dots along slanted pathways, sharp triangular petals "
            "spring up across the grid. Flowing gracefully around these straight figures, gentle sweeping arcs curve smoothly through the open spaces "
            "to create circular floral centers. Notice how each geometric element relies on precise spatial spacing. A square demands four equal line "
            "segments meeting at four neat corners, while a triangle requires exactly three straight boundary edges. Circles flow continuously without "
            "any sharp corners or flat edges whatsoever. By copying and extending these harmonious dot patterns, we discover how basic geometric shapes "
            "combine to construct grand artistic tapestries. Practice connecting the highlighted dots on your interactive canvas to finish the symmetrical "
            "lotus motif, celebrating the timeless beauty of foundational geometry everywhere in our daily world!"
        ),
        "checkpoints": [
            {
                "q": "How many straight boundary segments are needed to form a single square on a dot grid?",
                "options": ["4 straight segments", "3 straight segments", "5 straight segments", "2 curved segments"],
                "ans": "4 straight segments",
                "explanation": "A square is formed by joining four adjacent dots with four equal straight line segments."
            },
            {
                "q": "Which shape in the courtyard rangoli has curved contours rather than straight edges?",
                "options": ["Smooth circular center", "Corner square tile", "Slanted triangle petal", "Straight border line"],
                "ans": "Smooth circular center",
                "explanation": "Circles are bounded entirely by continuous curved lines, unlike squares and triangles which have straight edges."
            }
        ]
    },
    {
        "id": 2,
        "title": "Lines and Curves",
        "badge": "Line Classification",
        "sim_id": "sim_lines_and_curves",
        "description": "Distinguish between straight line segments and curved paths across everyday geometric illustrations.",
        "speech": (
            "Every single shape in our visual world begins with either a straight line or a curved path. When you pull a cotton thread tightly "
            "between both hands, it forms an unwavering, direct path called a straight line. Straight lines can stand perfectly upright as tall vertical "
            "lines, lie flat like calm water as level horizontal lines, or tilt dynamically as diagonal slanted lines. Polygons like triangles, rectangles, "
            "and squares are constructed entirely from straight line segments that meet crisply at sharp corners. However, when that same thread is "
            "allowed to hang loosely, it bends gracefully into a soft, flowing contour known as a curved line. Bangle rims, round dinner plates, "
            "swirling pottery wheels, smooth coins, and sweet round laddoos are defined by curved boundaries that glide smoothly without any corners at all. "
            "Some creative objects, such as arched doorways, smiling crescent moons, and ice cream cones, cleverly combine both straight edges and curved "
            "arcs within a single unified design. Understanding the distinct behavior of straight edges versus curved contours empowers us to analyze "
            "complex diagrams with remarkable mathematical clarity. Experiment with our interactive classifier to sort varied everyday objects into pure "
            "straight, pure curved, or hybrid geometric families right now!"
        ),
        "checkpoints": [
            {
                "q": "What type of line is formed when a piece of string is pulled completely taut between two hands?",
                "options": ["A straight line", "A curved line", "A circular loop", "A zig-zag spiral"],
                "ans": "A straight line",
                "explanation": "Pulling string tightly creates the shortest direct path between two points, which is a straight line."
            },
            {
                "q": "Which of these household items is bounded purely by curved lines with no sharp corners?",
                "options": ["A round glass bangle", "A rectangular notebook", "A triangular sandwich slice", "A wooden matchbox"],
                "ans": "A round glass bangle",
                "explanation": "A glass bangle forms a complete circular ring made entirely of a continuous curved boundary without any vertices."
            }
        ]
    },
    {
        "id": 3,
        "title": "Shape Cutout Art",
        "badge": "Composite Shape Craft",
        "sim_id": "sim_shape_cutout_art",
        "description": "Assemble expressive figures like houses, birds, and locomotives using pre-cut 2D geometric shapes.",
        "speech": (
            "Let us step into our craft workshop where colorful sheets of stiff chart paper have been neatly sliced into assorted geometric cutouts. "
            "We have ruby red squares, emerald green triangles, sapphire blue rectangles, and golden yellow circles waiting on the table. By arranging "
            "these fundamental shapes side by side, we can construct imaginative pictures of familiar objects without drawing a single new line! Place "
            "a large red square down as the sturdy main body of a village cottage. Crown it with a broad green triangle to serve as a sloping rooftop that "
            "lets monsoon rain run off smoothly. Add a tall blue rectangle for a front doorway, two tiny yellow squares for sunlit windows, and a puff of "
            "circular paper for chimney smoke drifting into the sky. You have just transformed four distinct geometric types into an architectural marvel! "
            "Similarly, three slender rectangles and several pairs of circular wheels quickly assemble into a chugging toy railway train. This creative "
            "exercise reveals that even the most complex mechanical wonders and natural creatures can be broken down into elementary geometric building "
            "blocks. Drag and snap the shape cutouts on your workspace to build your own custom composite masterpiece!"
        ),
        "checkpoints": [
            {
                "q": "Which shape cutout is best suited to represent the rolling wheels of a toy train?",
                "options": ["Circular cutouts", "Square cutouts", "Triangular cutouts", "Pentagonal cutouts"],
                "ans": "Circular cutouts",
                "explanation": "Circular cutouts have round edges that roll smoothly without corners, making them ideal representations for wheels."
            },
            {
                "q": "If a craft cottage uses 1 triangle for the roof, 1 large square for the wall, and 1 rectangle for the door, how many shapes were used?",
                "options": ["3 shapes", "4 shapes", "5 shapes", "2 shapes"],
                "ans": "3 shapes",
                "explanation": "Adding 1 triangle + 1 square + 1 rectangle equals exactly 3 geometric shape cutouts in total."
            }
        ]
    },
    {
        "id": 4,
        "title": "Flattened Box Nets",
        "badge": "3D to 2D Unfolding",
        "sim_id": "sim_flattened_box_nets",
        "description": "Unfold solid cardboard boxes along their seams to inspect the underlying two-dimensional net of rectangles and squares.",
        "speech": (
            "Every hollow packaging box you encounter in a pantry, grocery store, or toy shop is actually a three-dimensional solid created from a single flat sheet! "
            "Consider a familiar cardboard carton used to hold fresh toothpaste or sweet mango barfis. In its closed three-dimensional state, it stands "
            "upright, enclosing empty space inside with solid rectangular walls. But what happens if we carefully slit the glued corner edges and gently "
            "unfold the entire box flat against the tabletop? Like magic, the bulky three-dimensional container unfolds into a flat, planar two-dimensional "
            "pattern of connected rectangles known to mathematicians as a geometric net! Count the flat faces exposed in this unfolded layout. You will find exactly "
            "six distinct rectangular regions linked along straight fold creases. Notice that opposite faces in the original box appear separated by one "
            "intervening rectangle in the net. When we fold these flat flaps back along the creases, they wrap neatly around to enclose the interior space "
            "once again. Exploring unfolded nets reveals the vital mathematical bridge between flat planar drawings and hollow three-dimensional spatial "
            "structures. Click the unfold slider in our simulator to peel open cardboard boxes and trace their six rectangular components with complete confidence!"
        ),
        "checkpoints": [
            {
                "q": "How many flat rectangular faces are revealed when a standard cuboid box is completely unfolded?",
                "options": ["6 rectangular faces", "4 rectangular faces", "8 rectangular faces", "5 rectangular faces"],
                "ans": "6 rectangular faces",
                "explanation": "A standard cuboid box has exactly six faces (top, bottom, front, back, left, and right) which all lie flat in its net."
            },
            {
                "q": "What happens to the fold creases of an unfolded box net when the box is assembled?",
                "options": ["They become 3D edges", "They disappear completely", "They turn into circles", "They become inside holes"],
                "ans": "They become 3D edges",
                "explanation": "The straight fold lines of a flat net meet at right angles to become the straight 3D edges of the box."
            }
        ]
    },
    {
        "id": 5,
        "title": "Paper Fold Envelope",
        "badge": "Origami Geometry",
        "sim_id": "sim_paper_fold_envelope",
        "description": "Follow sequential geometric creases on a square sheet of paper to create a functional greeting card envelope.",
        "speech": (
            "Origami, the ancient art of paper folding, is pure practical geometry in action. Take a crisp square sheet of bright craft paper with four equal "
            "sides and four perfect square corners. Our practical goal is to craft a handsome postal envelope to safely hold a holiday greeting card. First, fold "
            "the square in half diagonally by bringing opposite corners together. When you crease and open the paper, a diagonal crease line divides our single "
            "square into two symmetrical right-angled triangles. Next, fold the two side corners inward toward the exact central point of the page, forming two neat "
            "triangular flaps that meet along a vertical centerline. Now, fold the broad bottom edge firmly upward to cover the lower half, creating a secure "
            "rectangular pocket for messages. Finally, fold the remaining top triangular flap downward over the opening to seal the envelope shut! Look at the resulting "
            "envelope: its main body forms a compact rectangle, while its sealing flap presents a crisp inverted triangle. Every fold converted flat geometric "
            "symmetry into functional structural compartments without using scissors or glue. Follow the interactive step-by-step origami guide on screen "
            "to fold your own virtual envelope and master angular creases in our digital studio!"
        ),
        "checkpoints": [
            {
                "q": "What initial shape of paper is used to fold the greeting card envelope?",
                "options": ["A square sheet", "A circular disc", "A long thin strip", "An irregular polygon"],
                "ans": "A square sheet",
                "explanation": "The envelope construction starts with a symmetrical square sheet having four equal sides."
            },
            {
                "q": "When a square sheet is folded corner-to-corner along its diagonal, what shapes are formed?",
                "options": ["Two triangles", "Two circles", "Three small squares", "Four rectangles"],
                "ans": "Two triangles",
                "explanation": "Folding a square corner-to-corner across its diagonal splits the square into two congruent right-angled triangles."
            }
        ]
    },
    {
        "id": 6,
        "title": "Biscuit Tray Arrays",
        "badge": "Rectangular Grid Arrays",
        "sim_id": "sim_biscuit_tray_arrays",
        "description": "Analyze rectangular baking tray layouts where identical circular, square, and rectangular biscuits form organized rows and columns.",
        "speech": (
            "A bustling bakery kitchen provides a delicious, mouthwatering setting for observing geometric regularity and rectangular grid arrangements. Look at "
            "this gleaming metallic baking tray fresh from the warm oven. The baker has arranged identical golden biscuits in tidy, parallel rows and columns. "
            "Notice how the entire rectangular tray is subdivided into a repeating geometric grid of identical sections. If we count across, there are four "
            "biscuits resting in each horizontal row. If we count down, there are three neat vertical columns of biscuits. Rather than counting each biscuit one "
            "by one, our mathematical understanding of arrays allows us to calculate the total swiftly. Three rows containing four biscuits each give three times "
            "four, which equals twelve biscuits in total without counting single items! Furthermore, observe the shapes of the biscuits themselves. Some trays "
            "hold round circular biscuits stamped with radiating spokes, while other trays hold crisp rectangular biscuits with dotted pinholes. Because every biscuit "
            "in a tray shares identical dimensions and consistent thickness, they pack together with uniform spacing, maximizing the available rectangular "
            "baking surface. Use the tray configuration controls on screen to adjust row and column counts, discovering how rectangular arrays make counting both "
            "swift and delightfully enjoyable!"
        ),
        "checkpoints": [
            {
                "q": "If a baking tray has 3 rows of biscuits with 5 biscuits in each row, how many biscuits are there?",
                "options": ["15 biscuits", "12 biscuits", "8 biscuits", "20 biscuits"],
                "ans": "15 biscuits",
                "explanation": "Multiplying the 3 rows by 5 biscuits per row gives 3 × 5 = 15 biscuits."
            },
            {
                "q": "Why do bakers arrange identical rectangular biscuits in neat rows and columns?",
                "options": ["To pack space evenly and count easily", "To make them bake unevenly", "To waste space on the tray", "To change their circular shape"],
                "ans": "To pack space evenly and count easily",
                "explanation": "Uniform rows and columns pack the flat surface efficiently and allow quick total calculation via multiplication."
            }
        ]
    },
    {
        "id": 7,
        "title": "Tracing Cuboid Faces",
        "badge": "Tracing 3D Solids",
        "sim_id": "sim_tracing_cuboid_faces",
        "description": "Trace the outlines of everyday 3D objects like matchboxes and erasers to reveal their 2D rectangular and square faces.",
        "speech": (
            "How do three-dimensional objects communicate with two-dimensional paper? We can discover this fascinating secret by pressing solid household items "
            "against a sheet of paper and tracing their boundaries with a sharp pencil! Pick up a standard wooden matchbox or a clean rectangular eraser. This "
            "three-dimensional solid is called a cuboid, possessing thickness, width, and height. Rest its largest flat surface firmly upon the paper and carefully "
            "guide your pencil around all four perimeter edges. Lift the matchbox away, and what remains behind? A crisp, two-dimensional rectangle appears "
            "permanently on the page! Now, tip the matchbox onto its narrow side edge and trace it once more. You obtain a second, much narrower rectangle with "
            "matching opposite lengths. Finally, stand the matchbox upright upon its smallest end face and trace that contour carefully. You produce a third "
            "rectangle, or perhaps even a square! By systematically tracing all six faces of the matchbox, you reveal that a cuboid is enclosed by three matching "
            "pairs of opposite rectangular faces. This tactile tracing experiment proves that every flat face of a 3D solid is a familiar 2D polygon. Try rotating "
            "and tracing our virtual wooden block in the simulator to collect its full set of rectangular footprints today!"
        ),
        "checkpoints": [
            {
                "q": "What flat shape is produced when you trace around the base of a rectangular wooden block?",
                "options": ["A rectangle", "A circle", "A triangle", "A pentagon"],
                "ans": "A rectangle",
                "explanation": "Tracing the flat rectangular face of a wooden block onto flat paper creates a 2D rectangle."
            },
            {
                "q": "How many total faces does a standard cuboid like a matchbox possess across all orientations?",
                "options": ["6 faces", "4 faces", "8 faces", "12 faces"],
                "ans": "6 faces",
                "explanation": "A cuboid has exactly 6 flat faces arranged as 3 pairs of matching opposite rectangles."
            }
        ]
    },
    {
        "id": 8,
        "title": "Dot Grid Rectangles",
        "badge": "Dot Grid Geometry",
        "sim_id": "sim_dot_grid_rectangles",
        "description": "Construct, stretch, and measure rectangles of various lengths and widths across a regular coordinate dot matrix.",
        "speech": (
            "A regular dot grid is an incredible interactive playground for investigating the geometric rules that govern all rectangles in mathematics. Every "
            "dot represents an equally spaced milestone across the horizontal and vertical directions. To construct a rectangle, choose a starting dot and draw "
            "a horizontal line segment stretching five units to the right side. From that ending dot, turn sharply downward at a ninety-degree angle and draw a "
            "vertical segment measuring three grid units. Now, trace five units back to the left, and finally climb three units upward to meet your original "
            "starting dot securely. Examine your completed figure closely. It has four straight sides and four sharp square corners at every intersection. "
            "Notice a fundamental geometric property: the top and bottom horizontal sides both measure exactly five units, while the left and right vertical "
            "sides both measure exactly three units! In every true rectangle, opposite sides are completely parallel and equal in length to each other. If all four "
            "sides happen to share the exact same length, the rectangle is a special case called a square. Use our interactive dot grid drawing tool to drag "
            "corner handles, building narrow, wide, and square rectangles with precision and artistic flair!"
        ),
        "checkpoints": [
            {
                "q": "In a rectangle, which pairs of sides are always guaranteed to have equal length?",
                "options": ["Opposite sides", "Adjacent perpendicular sides", "Only the diagonal sides", "No sides are equal"],
                "ans": "Opposite sides",
                "explanation": "In every rectangle, the top side equals the bottom side, and the left side equals the right side."
            },
            {
                "q": "How many square corners (right angles) does every rectangle contain?",
                "options": ["4 square corners", "2 square corners", "3 square corners", "6 square corners"],
                "ans": "4 square corners",
                "explanation": "Every rectangle is bounded by four perpendicular line segments meeting at four 90-degree square corners."
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Amma']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 1 (Slides 1-8)...")
    for s in slides_part1:
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
    print("Part 1 validation successful!")
