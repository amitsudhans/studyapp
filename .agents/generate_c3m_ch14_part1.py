#!/usr/bin/env python3
"""
NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair
Part 1: Slides 1 to 8 (Teaching Content + Checkpoints)
Strict spoken word count: 195 to 215 words per slide.
Strict titles: 1 to 3 words.
Zero human character names, zero lecturer personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Craft Fair Symmetry",
        "subtitle": "Discovering Balanced Beauty in Artisan Handicrafts",
        "speech": (
            "Welcome young mathematicians to our vibrant journey through the famous craft fair in Faridabad, Haryana. "
            "As we step into this magnificent festival of traditional art and folk culture, our eyes are immediately greeted "
            "by decorated stalls, colorful fabric canopies, and intricate terracotta pottery. Look closely at the handicrafts "
            "displayed by master artisans from every corner of our nation. Notice how many decorative objects possess a special "
            "visual balance called symmetry. When an object is symmetrical, one half is the exact mirror reflection of the other "
            "half. Consider a hanging wooden bird, a hand-carved floral wall hanging, or a pair of traditional brass lamps flanking "
            "a doorway. If you imagine drawing a straight line down the center, the left side matches the right side in size, shape, "
            "and color placement. Symmetry creates harmony, stability, and aesthetic beauty that naturally delights our eyes wherever we "
            "look. Throughout the fairgrounds, we also observe symmetry underfoot in repeating stone floor pavements and painted shop borders. "
            "In this chapter, we will learn how mathematics unlocks the secrets of symmetry through colorful beads, traditional floor rangolis, "
            "folded paper crafts, reflection mirrors, and geometric tiling pathways that decorate our communities with timeless wonder."
        ),
        "checkpoints": [
            {
                "question": "What mathematical property describes an object where one half matches the other half exactly?",
                "options": ["Roughness", "Symmetry", "Perimeter", "Capacity"],
                "answer": 1,
                "hint": "It describes balanced mirror reflection across a dividing line.",
                "explanation": "Symmetry means both halves of an object match identically in shape and proportion."
            },
            {
                "question": "Where is the famous annual crafts fair celebrated in Haryana?",
                "options": ["Jaipur", "Faridabad", "Bhopal", "Lucknow"],
                "answer": 1,
                "hint": "It is located in the Surajkund area of this district.",
                "explanation": "The Surajkund crafts fair is located in Faridabad district, Haryana."
            }
        ]
    },
    {
        "id": 2,
        "title": "Bead Mala Symmetry",
        "subtitle": "Linear Color Patterns & Bilateral Balance",
        "speech": (
            "At the artisan jewelry pavilion, craftspeople create traditional decorative necklaces called malas using wooden and clay beads. "
            "Let us explore symmetry in bead arrangements using eight beads in two distinct colors, such as bright red and golden yellow. "
            "Suppose we string four red beads and four yellow beads with careful artistic intent. How can we arrange them symmetrically? "
            "To achieve bilateral symmetry, the pattern must look identical when read from either end toward the center point. For example, "
            "if we string two red beads, then four yellow beads, and finally two red beads, our mala reads red, red, yellow, yellow on the "
            "left half, and yellow, yellow, red, red on the right half. Folding this necklace at its exact midpoint causes each bead on the "
            "left to align perfectly with an identical bead on the right. Now consider a non-symmetrical arrangement: stringing four red beads "
            "followed by four yellow beads. If we fold this mala, the red beads land on yellow beads, meaning the two halves do not match. "
            "Symmetry requires equal balance from the center outwards. Designing symmetrical necklaces trains our mathematical intuition to "
            "recognize harmonious color sequences and balanced arrangements in everyday art across our rich artisan culture."
        ),
        "checkpoints": [
            {
                "question": "Which bead sequence forms a symmetrical 8-bead mala using Red (R) and Yellow (Y)?",
                "options": ["R-R-R-R-Y-Y-Y-Y", "R-Y-Y-R-R-Y-Y-R", "R-R-Y-Y-Y-Y-Y-R", "Y-Y-Y-R-R-R-R-R"],
                "answer": 1,
                "hint": "The sequence must read the same forward and backward.",
                "explanation": "R-Y-Y-R | R-Y-Y-R reads identically from both ends, forming a symmetrical design."
            },
            {
                "question": "What must happen when a symmetrical bead mala is folded at its central midpoint?",
                "options": ["The beads change color", "Matching beads align perfectly on both halves", "The thread snaps in half", "One side becomes longer"],
                "answer": 1,
                "hint": "Symmetry requires superimposition of matching components.",
                "explanation": "In a symmetrical mala, folding at the center superimposes identical beads on both sides."
            }
        ]
    },
    {
        "id": 3,
        "title": "Kolam Dot Rangoli",
        "subtitle": "Traditional Grid-Based Line Art of Tamil Nadu",
        "speech": (
            "Outside the state craft pavilions, artists from Tamil Nadu demonstrate the sacred folk art of kolam with mesmerizing skill. "
            "In southern India, families welcome guests and bring auspicious prosperity each morning by drawing kolams at their doorsteps using fine "
            "white rice flour. Kolam begins with a systematic grid of evenly spaced dots, called pulli. An artist might place a five-by-five "
            "square grid of dots or an isometric diamond pattern on the freshly swept ground. Next, graceful straight or looping curved lines "
            "are drawn, either connecting the dots or weaving smoothly around them without lifting the hand from the canvas. What makes kolam "
            "deeply mathematical is its rigorous symmetry. Many traditional kolam patterns have four-way symmetry, meaning the top, bottom, "
            "left, and right quarters are mirror reflections of each other. If you fold a kolam along a central vertical axis, both halves "
            "superimpose flawlessly. If you fold it horizontally across the middle, the top half covers the bottom half exactly. Some kolams "
            "even look identical when rotated by a quarter turn. Creating kolams on dot grids helps young students understand how systematic "
            "geometric rules transform simple dots into breathtaking artistic masterpieces recognized and celebrated across the entire world."
        ),
        "checkpoints": [
            {
                "question": "In which Indian state is the traditional grid-based dot art called kolam widely practiced?",
                "options": ["Punjab", "Tamil Nadu", "Gujarat", "Assam"],
                "answer": 1,
                "hint": "This southern state greets mornings with doorstep rice flour designs.",
                "explanation": "Kolam is a traditional floor art of Tamil Nadu, drawn with rice flour on dot grids."
            },
            {
                "question": "What serves as the starting foundation when drawing a traditional kolam design?",
                "options": ["A ruler and compass", "A systematic grid of dots (pulli)", "Stencils and glue", "Random splashes of paint"],
                "answer": 1,
                "hint": "Artists place these regular markers first before drawing lines.",
                "explanation": "Kolams begin with a grid of regular dots around which looping curves are drawn."
            }
        ]
    },
    {
        "id": 4,
        "title": "Fold Line Symmetry",
        "subtitle": "Testing Superimposition & Mirror Axes",
        "speech": (
            "How do we prove whether a shape possesses true mathematical symmetry? The most direct and convincing test is the fold test. "
            "Imagine drawing a shape on translucent tracing paper, such as a paper leaf, a star, or a decorative festival lamp. If you can fold "
            "the paper along a straight crease so that the left half completely covers the right half without any overhang, then that crease line "
            "is an authentic line of symmetry, also known as a mirror line or axis of symmetry. Let us test different geometric figures with careful "
            "investigation. A standard rectangle has two lines of symmetry: one vertical line through the center and one horizontal line through the "
            "center. However, if you attempt to fold a rectangle diagonally, the corners do not align, proving that a diagonal is not a line of symmetry "
            "for a rectangle. In contrast, a perfect square has four lines of symmetry: vertical, horizontal, and both diagonals. Some shapes, like an "
            "irregular cloud or a scalene triangle, have zero lines of symmetry because no fold can produce two matching halves. Testing symmetry "
            "through physical folding builds concrete spatial reasoning, turning abstract geometric concepts into hands-on discoveries of geometric harmony."
        ),
        "checkpoints": [
            {
                "question": "How many lines of symmetry does a standard rectangle have?",
                "options": ["1 line", "2 lines", "4 lines", "8 lines"],
                "answer": 1,
                "hint": "Think about folding vertically and horizontally, but not diagonally.",
                "explanation": "A rectangle has exactly 2 lines of symmetry: one vertical and one horizontal."
            },
            {
                "question": "What must happen during a fold test for a crease line to be a true line of symmetry?",
                "options": ["The paper tears along the crease", "Both halves overlap and match completely without overhang", "The shape changes color", "One half remains twice as large"],
                "answer": 1,
                "hint": "Exact superimposition is required.",
                "explanation": "A true line of symmetry folds the shape so both halves cover each other perfectly."
            }
        ]
    },
    {
        "id": 5,
        "title": "Regional Rangoli Traditions",
        "subtitle": "Pookalam of Kerala & Aipan of Uttarakhand",
        "speech": (
            "Symmetry is celebrated across diverse regional folk arts throughout every corner of India. At the cultural pavilions, we admire "
            "stunning traditional floor decorations from different states with deep appreciation and mathematical curiosity. From the southern state of Kerala, "
            "we discover Pookalam, a magnificent floral carpet designed during the joyful harvest festival of Onam. Pookalam is crafted using "
            "concentric circular rings filled with colorful fresh flower petals. Notice the radial symmetry of a Pookalam: vibrant petals radiate "
            "outward from the central circle like the spokes of a decorative wheel, creating multiple lines of symmetry in every direction. Next, "
            "we visit the Uttarakhand pavilion to admire ancient Aipan art. Aipan is painted on red clay floors using white rice paste called biswar. "
            "Traditional Aipan motifs feature geometric chowkis with central lotus flowers surrounded by symmetrical linear borders. Both Pookalam and "
            "Aipan demonstrate how folk artists utilize line symmetry to evoke sacredness, peace, and natural order. Whether using fresh flower petals "
            "in the southern coastal state of Kerala or white rice paste in the northern Himalayan state of Uttarakhand, Indian artisans intuitively "
            "apply geometric reflections to transform ordinary courtyards into breathtaking canvases of cultural pride, heritage, and mathematical balance."
        ),
        "checkpoints": [
            {
                "question": "Which festival in Kerala is celebrated by crafting concentric floral carpets called Pookalam?",
                "options": ["Bihu", "Onam", "Pongal", "Baisakhi"],
                "answer": 1,
                "hint": "This harvest festival welcomes the mythical King Mahabali.",
                "explanation": "Pookalam floral carpets are created during the Onam festival in Kerala."
            },
            {
                "question": "What natural ingredients are traditionally used to paint Aipan art in Uttarakhand?",
                "options": ["Oil paints and canvas", "Red clay base and white rice paste", "Charcoal and sand", "Synthetic dyes"],
                "answer": 1,
                "hint": "A red background painted with white liquid made from rice.",
                "explanation": "Aipan is traditionally drawn using white rice paste (biswar) over a red ochre clay background."
            }
        ]
    },
    {
        "id": 6,
        "title": "Completing Symmetrical Patterns",
        "subtitle": "Grid Reflection & Boundary Drawing",
        "speech": (
            "A fascinating mathematical challenge involves completing the missing half of a symmetrical design on a square grid. "
            "Suppose an artist has drawn only the left half of a festival lamp or butterfly on grid paper, alongside a bold vertical center line. "
            "Your task is to draw the right half so that the entire figure becomes perfectly symmetrical. How do we accomplish this systematically? "
            "We treat the vertical line as a mirror boundary. First, identify key vertex corner points on the existing left half. For every point, "
            "count its exact distance in grid squares from the central mirror line. If a corner point lies three grid squares to the left of the line, "
            "mark the corresponding point exactly three grid squares to the right of the line at the identical height. Repeat this process for all "
            "corners and boundary curves, and finally connect the mirrored points with straight lines or smooth curves. By maintaining equal horizontal "
            "distances from the mirror line while preserving identical vertical heights, the completed figure emerges as a flawless mirror reflection. "
            "Practicing this technique trains precision, spatial estimation, and deep understanding of coordinate reflections on structured grids "
            "used in modern computer graphics and architecture."
        ),
        "checkpoints": [
            {
                "question": "If a point on a drawing is 4 squares to the left of the mirror line, where must its reflection be placed?",
                "options": ["2 squares to the left", "4 squares to the right at the same height", "4 squares above the line", "8 squares to the right"],
                "answer": 1,
                "hint": "Reflected points maintain the exact same distance on the opposite side.",
                "explanation": "Mirror symmetry requires the corresponding point to be 4 squares to the right at equal height."
            },
            {
                "question": "What happens to the vertical height of a point when reflecting across a vertical mirror line?",
                "options": ["It moves up by 2 squares", "It stays at the exact same vertical height", "It flips upside down", "It doubles"],
                "answer": 1,
                "hint": "Horizontal reflection across a vertical line only changes horizontal position.",
                "explanation": "Across a vertical mirror line, only the horizontal distance flips; vertical height remains identical."
            }
        ]
    },
    {
        "id": 7,
        "title": "Folded Paper Masks",
        "subtitle": "Bilateral Paper Crafting & Cutout Geometry",
        "speech": (
            "At the children's activity corner in the fair, young visitors learn to craft animal face masks using colorful card paper with great joy. "
            "Let us observe the brilliant shortcut that paper folding provides when crafting a symmetrical cat mask. Instead of drawing and cutting "
            "two separate ears and two separate eyes freehand, we first fold a square sheet of paper cleanly in half down the center. Along the folded "
            "crease, we draw only one half of the cat's face: one pointed ear, one cheek contour with whiskers, and half of the nose. Carefully, "
            "we cut along the drawn outline through both layers of folded paper simultaneously. When we unfold the paper, a complete, perfectly "
            "symmetrical cat face opens up before our eyes! Both ears are identical in size and shape, and both eyeholes sit at the exact same distance "
            "from the nose. If a child cuts the mask without folding along the center line, the eyeholes often end up uneven, causing awkward vision "
            "problems when worn. The fold crease acts as a physical mirror line, ensuring that every single cut is duplicated with flawless symmetry across "
            "both matching halves of the finished decorative animal face."
        ),
        "checkpoints": [
            {
                "question": "Why is folding paper in half a smart technique when crafting animal masks?",
                "options": ["It uses more paper", "One cut creates two identical, perfectly symmetrical halves", "It makes the paper heavier", "It changes the color of the mask"],
                "answer": 1,
                "hint": "Cutting folded paper duplicates the shape on both sides.",
                "explanation": "Cutting once through folded paper creates identical, symmetrical features on both sides automatically."
            },
            {
                "question": "What serves as the line of symmetry when unfolding a paper-crafted mask?",
                "options": ["The outer paper border", "The central fold crease", "The pencil outline", "The string tied to the ears"],
                "answer": 1,
                "hint": "The crease where the paper was folded in half.",
                "explanation": "The central fold crease forms the mirror axis dividing the two matching halves."
            }
        ]
    },
    {
        "id": 8,
        "title": "Painter Mirror Trick",
        "subtitle": "The Mathematics of Reflection & Asymmetry",
        "speech": (
            "Now let us enjoy a clever story from the fair about a tricky portrait painter. A painter at a craft stall promised to paint a child's "
            "portrait for one hundred rupees. But when the child returned, the painter presented a canvas containing only the left half of the face, "
            "claiming, 'Hold a mirror along the edge, and you will see the full portrait! Now pay me my one hundred rupees!' The clever child thought "
            "for a moment, handed the painter a single fifty-rupee note, placed a small mirror next to it, and said, 'Look into the mirror; you can see "
            "another fifty-rupee note! Fifty plus fifty equals one hundred rupees!' This amusing tale teaches an essential mathematical principle: "
            "a mirror reflection only completes an object correctly if the original object is truly symmetrical. While a human face possesses rough "
            "bilateral symmetry, many everyday objects do not. Consider a tea kettle with a handle on the left and a spout on the right. If you place a "
            "mirror down the middle, you get a kettle with two handles and no spout! Only genuinely symmetrical shapes produce valid complete images "
            "when reflected along their dividing center axis."
        ),
        "checkpoints": [
            {
                "question": "Why does placing a mirror against half of a tea kettle fail to show a normal kettle?",
                "options": ["Kettles are transparent", "A kettle is asymmetrical with a handle on one side and a spout on the other", "Mirrors cannot reflect metal", "The mirror is too small"],
                "answer": 1,
                "hint": "The handle and spout do not match each other across the middle.",
                "explanation": "Because a kettle is asymmetrical, reflecting half of it produces two handles or two spouts, not a real kettle."
            },
            {
                "question": "How did the clever child pay the painter who delivered only half a portrait?",
                "options": ["With a full 100-rupee note", "With a 50-rupee note placed beside a mirror reflection", "With a bag of marbles", "By refusing to talk"],
                "answer": 1,
                "hint": "The child used the painter's own mirror trick in reverse.",
                "explanation": "The child cleverly placed a 50-rupee note by a mirror so the painter could see the other half of the payment."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        words = len(s["speech"].strip().split())
        title_words = len(s["title"].strip().split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_words} words) -> Speech: {words} words")
        assert 1 <= title_words <= 3, f"Title length violation on slide {s['id']}"
        assert 195 <= words <= 215, f"Speech word count {words} out of range (195-215) on slide {s['id']}"
    print("Part 1 passed all strict validation checks!")
