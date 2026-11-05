# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 11: Fun with Symmetry
Part 2: Slides 9 to 16 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Rani, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Polygon Symmetry Lines",
        "section": "Geometric Polygons & Symmetry Classification",
        "speech": (
            "Every geometric polygon has unique symmetry properties that can be systematically uncovered through careful tracing, measuring, "
            "and folding. Let us examine the family of triangles first. An equilateral triangle, having three equal sides and three equal sixty-degree "
            "angles, possesses exactly three lines of symmetry, each running from a vertex directly through the midpoint of the opposite side. An "
            "isosceles triangle, having only two equal sides, possesses just one single line of symmetry bisecting the vertex between the equal sides. "
            "A scalene triangle, with three completely unequal sides, has zero lines of symmetry; no matter how you fold it, the sides never align! "
            "Now consider quadrilaterals: a rectangle has two lines of symmetry connecting opposite side midpoints, while a square boasts four lines "
            "of symmetry: two connecting opposite side midpoints and two running diagonally from opposite corners! For regular polygons where all "
            "sides and angles are equal, a delightful mathematical rule emerges: the number of lines of symmetry always matches the number of sides! "
            "A regular pentagon has five lines of symmetry, and a regular hexagon possesses six! Counting lines of symmetry provides deep insights "
            "into geometric regularity, proving that polygons with equal sides enjoy rich, multi-directional reflectional balance."
        ),
        "checkpoints": [
            {
                "q": "How many lines of symmetry does a regular hexagon (6 equal sides) possess?",
                "options": ["3 lines", "4 lines", "6 lines", "12 lines"],
                "ans": 2,
                "exp": "A regular polygon with n equal sides always has exactly n lines of symmetry; a regular hexagon has 6."
            },
            {
                "q": "How many lines of symmetry does a scalene triangle have?",
                "options": ["0 lines", "1 line", "2 lines", "3 lines"],
                "ans": 0,
                "exp": "A scalene triangle has all sides and angles unequal, so it has zero lines of symmetry."
            }
        ]
    },
    {
        "id": 10,
        "title": "Tessellation Repeating Units",
        "section": "Periodic Tilings & Planar Coverage",
        "speech": (
            "Have you ever looked closely at an intricately tiled floor in a heritage monument, courtyard, or modern railway station? When identical "
            "geometric shapes fit together repeatedly to cover an entire two-dimensional flat surface without leaving any gaps or creating overlaps, "
            "mathematicians call this arrangement a tessellation or tiling pattern. The single fundamental building block that repeats continuously "
            "across the floor is termed the repeating unit or tile. Regular shapes like equilateral triangles, squares, and regular hexagons "
            "tessellate naturally because their interior corner angles fit together snugly around any shared vertex to form a complete three "
            "hundred sixty degrees! For example, four identical squares with ninety-degree corners meet at every joint, four times ninety equaling "
            "three hundred sixty degrees. In contrast, regular pentagons cannot tessellate alone because three interior angles equal three hundred "
            "twenty-four degrees, leaving an awkward thirty-six-degree gap that prevents complete closure! In traditional Indian architecture, master "
            "craftsmen designed breathtaking tessellations using interlocking stars, octagons, and crosses. Exploring these repeating units teaches "
            "us how simple geometric polygons assemble into infinite, seamless mosaic surfaces, combining computational angular precision with "
            "timeless aesthetic craftsmanship across human history, architecture, and everyday modern living spaces in our communities and neighborhoods."
        ),
        "checkpoints": [
            {
                "q": "What is a pattern called where shapes cover a flat surface without any gaps or overlaps?",
                "options": ["Tessellation (tiling)", "Perimeter loop", "Asymmetrical border", "Radial fracture"],
                "ans": 0,
                "exp": "A tessellation is an arrangement of repeating shapes that completely covers a plane with no gaps and no overlaps."
            },
            {
                "q": "Why do squares tessellate effortlessly on a flat floor?",
                "options": ["They are made of wood", "Their 90° corner angles sum to 360° when four corners meet at a vertex", "They have 3 sides", "They are curved"],
                "ans": 1,
                "exp": "Four 90° angles equal 360°, completely filling the space around a shared vertex without gaps."
            }
        ]
    },
    {
        "id": 11,
        "title": "Tile Motion Geometry",
        "section": "Transformations: Slides, Flips & Rotations",
        "speech": (
            "To understand how repeating tile patterns are constructed across large architectural surfaces, mathematicians classify the geometric "
            "motions used to position each tile. These fundamental motions include sliding, flipping, and rotating, along with visual orientations "
            "described as standing or sleeping. A slide, known formally as a translation, means moving a tile smoothly in a straight line along a "
            "horizontal, vertical, or diagonal direction without turning or flipping it. A flip, or reflection, turns the tile over across an edge "
            "like a page in a book, creating a mirror-reversed image. A rotation means turning a tile around a fixed pivot point by a quarter-turn "
            "of ninety degrees or a half-turn of one hundred eighty degrees. Craftsmen also describe tile orientations colloquially: an oblong "
            "rectangular tile laid horizontally is called sleeping, while one oriented vertically is called standing! In classic herringbone "
            "pavement patterns, pairs of standing and sleeping rectangular bricks alternate continuously, locking together in interlocking "
            "zigzags. By mastering sliding, flipping, and rotating, skilled designers and floor masons can easily create hundreds of dazzling "
            "decorative floor patterns from a single basic tile, demonstrating how simple rigid geometric motions govern rich planar artistry across "
            "diverse cultural traditions and architectural landscapes worldwide."
        ),
        "checkpoints": [
            {
                "q": "What geometric motion moves a tile smoothly from one spot to another without turning or flipping it?",
                "options": ["Sliding (translation)", "Flipping (reflection)", "Rotating (turn)", "Shrinking"],
                "ans": 0,
                "exp": "Sliding (translation) shifts an object along a vector without altering its orientation or flipping it."
            },
            {
                "q": "In a herringbone pavement pattern, how do the rectangular tiles alternate?",
                "options": ["All standing vertically", "Alternating standing (vertical) and sleeping (horizontal) orientations", "All upside down", "Randomly angled"],
                "ans": 1,
                "exp": "Herringbone patterns alternate vertical (standing) and horizontal (sleeping) rectangular units to lock tightly together."
            }
        ]
    },
    {
        "id": 12,
        "title": "Custom Tile Crafting",
        "section": "Rangometry Kits & Area Preservation",
        "speech": (
            "Rather than using standard store-bought squares or rectangles, creative artisans and mathematicians love designing custom tiles that "
            "possess imaginative, irregular shapes while still tessellating perfectly! The secret to crafting a custom tessellating tile lies in a "
            "brilliant mathematical principle called area conservation. Begin with a sturdy square card cut from heavy paper or cardboard. On one "
            "side of the square, draw a creative shape, such as a gentle curve, a jagged zigzag, or a triangular tooth. Carefully cut this shape "
            "out using scissors. Instead of throwing the cutout away, slide it straight across to the opposite parallel side of the square and "
            "tape it firmly in place! Because you removed an area from one side and added the exact same area to the opposing side, the total "
            "surface area of your tile remains completely unchanged! More importantly, whenever two of your custom tiles meet, the jutting piece "
            "of one tile fits snugly into the matching hollow cavity of its neighbor, like interlocking puzzle pieces! Tracing this custom tile "
            "repeatedly onto paper produces a mesmerizing, seamless mosaic with zero gaps and zero overlaps, turning simple geometry into enchanting "
            "artistic creations for home decoration and classroom craft displays."
        ),
        "checkpoints": [
            {
                "q": "In custom tile crafting, why is the cut piece from one side taped to the opposite parallel side?",
                "options": ["To make the tile heavier", "So the jutting edge perfectly fills the matching hollow cavity of adjacent tiles", "To change its color", "To make it a circle"],
                "ans": 1,
                "exp": "Translating a cut shape to the opposite edge creates interlocking puzzle edges that tessellate seamlessly."
            },
            {
                "q": "What happens to the total surface area of a square tile after cutting a shape from one side and attaching it to the opposite side?",
                "options": ["The area increases by double", "The area decreases by half", "The total area remains exactly the same", "The area becomes zero"],
                "ans": 2,
                "exp": "Area is conserved because the piece subtracted from one side is added to the other side."
            }
        ]
    },
    {
        "id": 13,
        "title": "Seamless Floor Patterns",
        "section": "Grid Tessellations & Pavement Layouts",
        "speech": (
            "Creating seamless floor patterns requires combining geometric precision with artistic flair to ensure every single tile joins flush with "
            "its neighbors across entire architectural spaces. Professional tile layers and masons rely on rigorous alignment rules when paving "
            "floors in school auditoriums, home verandas, and bustling railway concourses. When ceramic or stone tiles are laid out, they form "
            "distinct networks of seams known as grout lines. If square tiles are laid directly with their corners meeting at four-way intersections, "
            "they form a classic checkerboard grid. However, if each row is systematically shifted by half a tile length, it forms a staggered running "
            "bond pattern, where each vertical seam ends right at the solid center of the tile below, significantly increasing structural strength and "
            "crack resistance! Designers also alternate contrasting colors, such as white and charcoal tiles, creating vibrant optical rhythms. Notice "
            "how every complete floor pattern satisfies the two golden laws of tessellation: no empty gaps between tiles, and absolutely no overlapping "
            "edges. Practicing seamless floor design helps observant young students connect geometric area measurement with structural construction, "
            "showing how mathematics transforms raw stone and clay into durable, beautiful surfaces throughout our built environment across modern "
            "towns, villages, and cities."
        ),
        "checkpoints": [
            {
                "q": "What are the two fundamental golden rules of every valid floor tessellation?",
                "options": ["No empty gaps and no overlapping edges", "Must use only red paint", "Tiles must be curved", "Gaps must be 5 cm wide"],
                "ans": 0,
                "exp": "A valid tessellation must completely cover the surface without any gaps or overlapping shapes."
            },
            {
                "q": "Why do builders frequently use a staggered running bond pattern (shifting each row by half a tile)?",
                "options": ["It looks messy", "It increases structural strength and prevents continuous vertical cracking seams", "It requires zero mortar", "It makes tiles float"],
                "ans": 1,
                "exp": "Staggering vertical seams distributes stress across adjacent tiles, preventing cracks from running straight down the floor."
            }
        ]
    },
    {
        "id": 14,
        "title": "Catty Wall Tessellation",
        "section": "Novelty Tiles & Creative Wall Art",
        "speech": (
            "One of the most delightful craft projects in joyful mathematics is constructing a catty wall using repeating cat-head tiles! This charming "
            "activity demonstrates how even whimsical animal shapes can tessellate across a wall when crafted using rigorous transformation geometry. "
            "To build a cat-head tile, take a square piece of paper. Along the top edge, draw a curved downward crescent between the two upper corners "
            "to form the space between two pointy cat ears. Cut out this top crescent piece, slide it straight down to the bottom edge, and tape it "
            "securely in place, creating the curved chin of the cat! Next, make a triangular inward cut on the left side to represent a cheek whisker "
            "notch, and tape that triangular cutout onto the right edge. Now, draw cute eyes and whiskers on your cutout card. When you trace this "
            "unique cat-head tile repeatedly onto a large poster board, an enchanting phenomenon occurs: every cat chin nestles perfectly between the "
            "pointed ears of the cat below it, and every left cheek notch locks into the right cheek of its neighbor! A whole parade of friendly "
            "cats covers the wall seamlessly, proving that geometry can be playful, expressive, and mathematically rigorous simultaneously."
        ),
        "checkpoints": [
            {
                "q": "In the catty wall craft project, where is the curved crescent cut from the top edge taped?",
                "options": ["At the bottom edge to form the matching chin", "In the center of the card", "On the back of the paper", "Nowhere, it is discarded"],
                "ans": 0,
                "exp": "Sliding the top cut straight down to the bottom edge ensures that the chin of one tile interlocks with the ears of the tile below."
            },
            {
                "q": "Why do the cat-head tiles fit together across the poster board without any gaps?",
                "options": ["They are made of rubber", "Every cut on one edge has a matching identical addition on the opposite parallel edge", "They overlap each other", "They are tiny"],
                "ans": 1,
                "exp": "Translational area modifications on opposite edges ensure perfect interlocking planar coverage without gaps."
            }
        ]
    },
    {
        "id": 15,
        "title": "Nature Walk Symmetry",
        "section": "Biological Bilateral Symmetry & Botanicals",
        "speech": (
            "Nature is the supreme master architect of symmetry. Taking an exploratory nature walk through a local school garden, community park, "
            "or forest trail reveals that symmetry is woven into the very fabric of living organisms. As you stroll beneath shady trees, observe "
            "the fluttering wings of a vibrant butterfly resting on a blossom. A butterfly exhibits exquisite bilateral symmetry: its left wing and "
            "right wing display identical contours, matching veins, and mirrored spots of colour. If the butterfly folds its wings closed vertically "
            "above its back, both wings superimpose with flawless precision! Now, gaze at the fallen leaves beneath a peepal or mango tree. Pick up "
            "a fresh peepal leaf and observe its strong central vein, called the midrib. The midrib acts as an organic line of symmetry, with leaf "
            "veins branching outward at matching angles on both sides. Look closely at flower petals: lilies, hibiscus, and sunflowers exhibit radiant "
            "radial symmetry, where identical petals radiate gracefully around a central core like spokes on a wheel. Observing symmetry in nature "
            "cultivates profound reverence for biological design, showing that mathematical balance is essential for aerodynamic flight, efficient "
            "plant photosynthesis, and natural organic beauty everywhere in the wild outdoor world."
        ),
        "checkpoints": [
            {
                "q": "What part of a peepal or mango leaf functions as an organic line of symmetry?",
                "options": ["The tip", "The central midrib vein", "The outer jagged edge", "The stalk base"],
                "ans": 1,
                "exp": "The central midrib divides the leaf blade into matching left and right halves with symmetrical branching veins."
            },
            {
                "q": "What type of symmetry is displayed when a butterfly folds its wings closed over its back?",
                "options": ["Bilateral symmetry (mirror reflection across the central body axis)", "Asymmetry", "Spherical curvature", "Linear progression"],
                "ans": 0,
                "exp": "Butterflies exhibit bilateral symmetry, where the left and right wings are mirror reflections of each other."
            }
        ]
    },
    {
        "id": 16,
        "title": "Symmetry Project Art",
        "section": "Botanical Imprints & Creative Portfolios",
        "speech": (
            "Following your inspiring nature walk, you can channel your outdoor discoveries into a magnificent symmetry project portfolio using "
            "fallen botanicals, paper folding, and water paints. Gathering naturally shed leaves, flower petals, and slender twigs allows you to "
            "create sustainable artwork without harming living plants. One classic technique is leaf-imprint printing: fold a sheet of thick handmade "
            "paper in half to create a central line of symmetry. Paint the textured underside of a leaf with vibrant poster paint, press it firmly "
            "onto the paper on one side of the crease, and fold the opposite half over to stamp a mirror imprint! Alternatively, students can create "
            "botanical collages by slicing symmetrical leaves along their midrib, pasting one half onto paper, and using a pencil to sketch the missing "
            "mirror half with scientific precision. You can also craft symmetrical greeting cards with pressed flower petals arranged in radiant radial "
            "mandala rings. Completing a symmetry art project synthesizes geometry, fine motor craftsmanship, and biological appreciation, cementing "
            "the timeless truth that mathematics is not just an abstract subject in a school textbook, but a joyful practical lens through which we "
            "appreciate the living natural world around us every single day."
        ),
        "checkpoints": [
            {
                "q": "How can you create a symmetrical leaf-imprint print on paper?",
                "options": ["Crumple the paper into a ball", "Paint a leaf, press it on one side of a folded crease, and fold over to stamp the mirror half", "Throw the leaf away", "Cut the paper into 100 strips"],
                "ans": 1,
                "exp": "Folding painted materials along a central crease stamps a mirror reflection across the crease line."
            },
            {
                "q": "When creating a botanical symmetry study, what does sketching the missing half of a sliced leaf reinforce?",
                "options": ["Color blending only", "Accurate spatial observation, coordinate mirroring, and proportional geometric reconstruction", "Random doodling", "Speed typing"],
                "ans": 1,
                "exp": "Reconstructing the mirror half of a biological specimen trains observational precision and reflectional geometry."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 2 slide constraints validated successfully!")
