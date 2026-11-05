# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 11: Fun with Symmetry
Part 1: Slides 1 to 8 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Rani, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Ink Blot Symmetry",
        "section": "Crease Lines & Bilateral Mirror Reflection",
        "speech": (
            "Welcome to the captivating world of symmetry, where balance, beauty, and geometric harmony unite across art and nature. "
            "To begin exploring symmetry firsthand, take a clean sheet of stiff drawing paper and fold it precisely down the middle, "
            "creating a crisp vertical crease. Unfold the paper, place a few vibrant drops of liquid watercolour or ink directly onto "
            "one half near the center, and fold the paper back along the original crease line. Press firmly across the surface with your "
            "palms so the wet ink spreads outwards. When you gently open the folded paper, a breathtaking, symmetrical design emerges! "
            "Look closely at the central crease: it divides the entire artwork into two identical halves that mirror each other perfectly. "
            "In mathematics, this central dividing crease is known as the line of symmetry or mirror line. If you imagine placing a vertical "
            "mirror along this crease, the reflection of the left half matches the right half seamlessly! Every droplet of colour on the left "
            "has an identical counterpart on the right, positioned at the exact same distance from the fold. Practicing bilateral ink blot "
            "symmetry teaches us that geometric symmetry is fundamentally about balanced, congruent reflection across a dividing line."
        ),
        "checkpoints": [
            {
                "q": "What is the crease line called in an ink blot design that divides the picture into two identical matching halves?",
                "options": ["Line of symmetry (mirror line)", "Perimeter border", "Diagonal hypouse", "Curved tangent"],
                "ans": 0,
                "exp": "The central fold dividing the figure into identical mirror halves is the line of symmetry."
            },
            {
                "q": "If an ink drop is placed 3 cm to the left of the fold crease, where will its mirrored impression appear?",
                "options": ["1 cm to the left", "3 cm to the right of the fold crease", "6 cm below the bottom", "At the corner"],
                "ans": 1,
                "exp": "In bilateral symmetry, corresponding points appear at identical perpendicular distances on opposite sides of the fold line."
            }
        ]
    },
    {
        "id": 2,
        "title": "Paper Airplane Fold",
        "section": "Aerodynamic Balance & Flight Mechanics",
        "speech": (
            "Paper airplanes offer an exhilarating practical demonstration of how symmetry directly influences physical balance, aerodynamic "
            "stability, and flight performance. When carefully folding a standard aerodynamic paper glider, every single precise crease begins "
            "from a central lengthwise axis. You fold the rectangular paper in half lengthwise, unfold it, and then fold both top corners "
            "downward at identical angles so their edges meet precisely along the center crease. Next, you fold both paper wings downward "
            "using identical dimensions and matching crease angles. Because the left wing and right wing are exact mirror reflections of each "
            "other across the central fuselage, the airplane possesses perfect bilateral symmetry! When launched smoothly into open air, balanced "
            "aerodynamic lift acts equally on both wings, allowing the glider to soar straight, gracefully, and steadily across the room. But "
            "what happens if you intentionally introduce an asymmetrical fold, making one wing narrower or bending one flap upward? The "
            "unbalanced air resistance immediately creates an unequal turning force, causing the airplane to spin sideways, wobble, and crash! "
            "Symmetrical aircraft design ensures perfect aerodynamic equilibrium, proving that structural symmetry in engineering is not merely "
            "decorative, but absolutely vital for balance, stability, and controlled flight dynamics through the air."
        ),
        "checkpoints": [
            {
                "q": "Why does a symmetrically folded paper airplane glide smoothly in a straight path?",
                "options": ["It is heavier than air", "Both wings experience balanced, identical aerodynamic lift and air resistance", "It has no wings", "It uses an electric engine"],
                "ans": 1,
                "exp": "Identical wing shape and crease angles ensure equal lift forces on both sides of the central axis."
            },
            {
                "q": "What happens if one wing of a paper airplane is folded larger and steeper than the other wing?",
                "options": ["It flies completely straight", "It wobbles, tilts, and spirals off course due to asymmetrical air drag", "It flies backwards", "It hovers motionlessly"],
                "ans": 1,
                "exp": "Asymmetry causes uneven aerodynamic forces, resulting in tilting and spiral diving."
            }
        ]
    },
    {
        "id": 3,
        "title": "Holes And Cuts",
        "section": "Spatial Reasoning & Unfolding Predictions",
        "speech": (
            "One of the most intriguing mental challenges in geometry involves predicting what a folded sheet of paper will look like after "
            "holes or shapes are cut into it and then unfolded. Imagine taking a square piece of paper and folding it once along a vertical "
            "midline. Next, you fold it a second time along a horizontal midline, producing a smaller four-layered square. Now, suppose an "
            "imaginative craftsperson cuts a small triangular notch into the folded closed corner, and punches a circular hole near the outer "
            "open edge. Before carefully unfolding the layered paper, can you visualize exactly where all the cutouts will appear? Because "
            "the paper was folded across two perpendicular lines of symmetry, every single cut through all four layers will replicate four "
            "times across the four quadrants of the original square! When opened flat, that single corner notch blossoms into a complete "
            "diamond-shaped window centered right at the intersection of the two fold lines, while the edge punch produces four symmetrically "
            "distributed circular holes across all quadrants! Regularly practicing hole-and-cut visualization trains advanced spatial reasoning, "
            "helping observant young mathematicians mentally manipulate reflected shapes, anticipate multi-layered transformations, and deeply "
            "understand how fold lines multiply geometric features across surfaces."
        ),
        "checkpoints": [
            {
                "q": "If a square paper is folded in half once and a circular hole is punched through both layers, how many holes appear when unfolded?",
                "options": ["1 hole", "2 holes", "4 holes", "8 holes"],
                "ans": 1,
                "exp": "Folding in half creates 2 layers; a single punch through 2 layers creates 2 symmetrical holes."
            },
            {
                "q": "If a square paper is folded twice (into 4 layers) and a single corner cut is made at the central folded apex, what shape appears at the center when opened?",
                "options": ["A single small slit", "A 4-pointed symmetric diamond or square centered on the folds", "A circle at the outer border", "No shape at all"],
                "ans": 1,
                "exp": "The 4 layers meeting at the central folded corner unfold into a 4-fold symmetric polygon centered at the origin."
            }
        ]
    },
    {
        "id": 4,
        "title": "Dot Grid Designs",
        "section": "Coordinate Dot Grids & Line Symmetry",
        "speech": (
            "Dot grids provide an ideal structured mathematical canvas for constructing, verifying, and analyzing symmetrical shapes. On a dot grid, "
            "points are arranged in uniform horizontal rows and vertical columns, creating precise intervals that allow us to measure distances "
            "accurately without needing a physical ruler. Suppose a red vertical line is drawn down the center of a dot grid to represent our line of "
            "symmetry. On the left side of this mirror line, a jagged geometric path connects three dots: starting two units left, moving diagonally "
            "to one unit left, and turning back to four units left. To complete the symmetrical design on the right side, we must plot matching "
            "reflection points that mirror the left path point for point. For every dot located a certain number of spaces to the left of the line of "
            "symmetry, its partner dot must be plotted the exact same perpendicular number of spaces to the right, along the identical horizontal row! "
            "Connecting these reflected dots reveals a perfectly balanced geometric figure, like a butterfly wing, a vase, or an arrowhead. Dot grids "
            "transform symmetry from an abstract visual intuition into an exact, measurable coordinate relationship where left and right distances remain invariant."
        ),
        "checkpoints": [
            {
                "q": "On a dot grid with a vertical line of symmetry, if a vertex is 4 grid units to the left, where must its reflection be placed?",
                "options": ["4 units to the right along the same horizontal line", "2 units above the line", "4 units diagonally downward", "Directly on the mirror line"],
                "ans": 0,
                "exp": "Symmetry requires equal perpendicular distance from the line of symmetry along the same horizontal coordinate row."
            },
            {
                "q": "What happens if a point lies directly on the line of symmetry?",
                "options": ["Its reflection appears at infinity", "Its reflection lies at the exact same location on the line", "It vanishes", "It doubles in size"],
                "ans": 1,
                "exp": "Points lying directly on the mirror line have a distance of zero from the line, so their reflections remain unchanged."
            }
        ]
    },
    {
        "id": 5,
        "title": "Border Shape Symmetry",
        "section": "Decorative Borders & Symmetry Testing",
        "speech": (
            "Decorative borders often adorn traditional Indian textiles, architectural archways, greeting cards, and classroom display boards. When "
            "analyzing border shapes, mathematicians test whether individual decorative units possess lines of symmetry. For instance, consider a "
            "wide variety of border elements: a regular five-pointed star, a pointed arrowhead, a leaf shape, a heart motif, an asymmetrical paisley "
            "droplet, and an oval. To test whether any border shape is symmetrical, we can use two highly reliable methods: physical paper folding "
            "or transparent tracing. If we trace the outline of a heart onto tracing paper and fold it down the center, the left lobe superimposes "
            "completely onto the right lobe, proving it has one vertical line of symmetry. An oval possesses two lines of symmetry: one vertical and "
            "one horizontal! A regular star boasts five distinct lines of symmetry passing through each point. However, when we inspect an organic "
            "paisley motif with its swirling curved tail, no straight line can ever be found that divides the shape into two matching halves. Folding "
            "it anywhere results in mismatched borders and overlapping edges. Systematically categorizing border motifs as symmetrical or asymmetrical "
            "develops keen observational discernment, clearly showing that true symmetry requires complete geometric congruence upon folding."
        ),
        "checkpoints": [
            {
                "q": "How many lines of symmetry does a standard oval (ellipse) border motif possess?",
                "options": ["Zero", "One line", "Two lines (vertical and horizontal)", "Infinite lines"],
                "ans": 2,
                "exp": "An oval possesses two perpendicular lines of symmetry: one along its major axis and one along its minor axis."
            },
            {
                "q": "Why is a traditional paisley motif with a curved curling tail classified as asymmetrical?",
                "options": ["It has no straight line that folds the shape into two perfectly overlapping halves", "It has too many colours", "It is smaller than a square", "It has 4 right angles"],
                "ans": 0,
                "exp": "Because of its curved, one-sided tail, no folding line can divide a paisley into matching congruent halves."
            }
        ]
    },
    {
        "id": 6,
        "title": "Mirror Reflection Games",
        "section": "Physical Mirrors & Visual Invariance",
        "speech": (
            "Playing games with a small pocket mirror provides an enchanting, hands-on way to investigate reflections, mirror lines, and symmetric "
            "transformations. When you place the straight edge of an upright pocket mirror across an illustration, the mirror hides the artwork behind "
            "it while reflecting the artwork in front, producing a brand-new composite image composed half of paper and half of reflection! By angling "
            "and sliding the mirror across a reference drawing, you can produce surprisingly diverse target shapes. Fascinatingly, certain numbers and "
            "letters look completely identical whether viewed directly or through a vertical mirror! For example, consider the three-digit number one "
            "hundred eighty-one: the digit one is vertically symmetrical, and the central digit eight is vertically symmetrical. Because the sequence "
            "reads one, eight, one both forwards and backwards, viewing one hundred eighty-one in a vertical mirror produces the exact same number: "
            "one hundred eighty-one! Similarly, the three-digit number eight hundred eight also remains completely identical. In contrast, consider the "
            "number six hundred eighty-six: in a mirror, the curved tails of the sixes flip outwards, distorting the digits into non-standard symbols. "
            "Mirror reflection games prove that reflection inverses lateral direction while preserving perpendicular distances, transforming abstract "
            "arithmetic symbols into playful optical investigations."
        ),
        "checkpoints": [
            {
                "q": "Which of the following three-digit numbers reads identically when reflected in a vertical mirror?",
                "options": ["181", "121", "686", "252"],
                "ans": 0,
                "exp": "Both '1' and '8' possess vertical symmetry, and the palindromic sequence '1-8-1' reflects without distortion."
            },
            {
                "q": "What happens to the letter 'E' when viewed in a vertical mirror placed along its spine?",
                "options": ["It looks identical", "It faces backwards (forming a reversed 3-like symbol)", "It turns upside down", "It turns into an O"],
                "ans": 1,
                "exp": "A vertical mirror flips left and right, reversing the arms of the letter 'E'."
            }
        ]
    },
    {
        "id": 7,
        "title": "Ambulance Word Mirror",
        "section": "Lateral Inversion & Emergency Vehicles",
        "speech": (
            "Have you ever noticed that emergency ambulances driving on city roads have the word AMBULANCE painted strangely in reverse on their front "
            "hood? This is not a printing mistake; it is a brilliant real-world application of optical physics and lateral inversion! When an ambulance "
            "speeds up behind a car on the road, the driver ahead looks into their rear-view mirror to see what is behind them. Flat mirrors naturally "
            "produce a lateral inversion, swapping the perceived left and right sides of any reflected object. When the driver looks into their "
            "rear-view mirror, the mirror reverses the already-reversed letters on the ambulance, flipping them back into normal, readable orientation! "
            "The driver instantly reads AMBULANCE correctly and clearly, allowing them to pull over safely and let the emergency vehicle pass without "
            "delay. We can explore lateral inversion by writing words on paper and predicting their reflections. Some capital letters with vertical "
            "symmetry, like A, H, I, M, O, T, U, V, W, X, and Y, look identical in a mirror! For example, familiar English words like MOM or WOW "
            "reflect without any distortion! Understanding lateral inversion bridges classroom geometry with practical everyday safety, clearly "
            "demonstrating how mirror mathematics saves precious lives on busy highways."
        ),
        "checkpoints": [
            {
                "q": "Why is the word AMBULANCE painted in reversed lettering on the front of emergency vehicles?",
                "options": ["To confuse pedestrians", "So drivers ahead see it right-side-up and readable in their rear-view mirrors", "It is written in a foreign language", "To save painting ink"],
                "ans": 1,
                "exp": "The rear-view mirror laterally inverts the reversed letters, making the word appear normally oriented to the driver ahead."
            },
            {
                "q": "Which of the following English words reads identically in a vertical mirror reflection?",
                "options": ["MOM", "CAT", "DOG", "SUN"],
                "ans": 0,
                "exp": "Letters M and O have vertical symmetry, and MOM is a palindrome, so its vertical mirror image remains MOM."
            }
        ]
    },
    {
        "id": 8,
        "title": "Completing Symmetric Figures",
        "section": "Geometric Reconstruction & Mirror Halves",
        "speech": (
            "A wonderful puzzle in elementary geometry is completing a symmetrical figure when only one half is drawn along a given line of symmetry. "
            "Imagine looking at an activity sheet showing half of a butterfly, half of a decorative flower, half of a kite, or half of a teapot, with "
            "a dotted mirror line running straight down the center. To complete the drawing, an artist must act like a living mirror, systematically "
            "transferring every contour, angle, and corner to the other side. Begin by identifying key anchor points: the tip of an antenna, the "
            "outermost curve of a wing, or the sharp vertex of a leaf. For each anchor point, measure its perpendicular distance from the line of "
            "symmetry, and plot a corresponding point at that exact same distance on the opposite side. Once all anchor points are plotted, connect "
            "them with matching lines and curves that replicate the original half with faithful precision. If the left side features a circular wing "
            "spot, the right side must receive a matching circle of identical radius and position. Completing symmetric figures develops proportional "
            "reasoning, geometric accuracy, and fine motor drawing skills, transforming partial sketches into magnificent, harmoniously balanced wholes."
        ),
        "checkpoints": [
            {
                "q": "What is the first step in accurately completing a symmetrical figure across a vertical mirror line?",
                "options": ["Erase the mirror line", "Identify key anchor points and measure their perpendicular distance from the line of symmetry", "Color the entire page black", "Draw random circles"],
                "ans": 1,
                "exp": "Measuring anchor points perpendicular to the mirror line ensures that reflected vertices land at correct corresponding coordinates."
            },
            {
                "q": "If the left half of a figure contains a triangle with base 4 cm, what must the reflected right half contain?",
                "options": ["A square of 6 cm", "A matching congruent triangle with base 4 cm", "A circle of radius 2 cm", "Nothing"],
                "ans": 1,
                "exp": "Reflection preserves size and shape, producing an exact congruent mirror copy."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 1 slide constraints validated successfully!")
