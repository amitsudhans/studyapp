#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 6: Measuring Space: Perimeter and Area
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly covers 6.8 to 6.10.1, Exercises & Summary with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Triangle Median Area",
        "subtitle": "Section 6.8 Area of a Triangle: Formula ½bh & Proof That Every Median Divides a Triangle into Two Equal-Area Halves",
        "speech": (
            "Now halve a parallelogram cleanly across one diagonal in Section Six Point Eight to unlock AREA OF A TRIANGLE! "
            "Take ANY triangle with horizontal base b and perpendicular altitude h! Clone an identical rotated upside-down copy of your triangle and snap their corresponding slanted edges together—forming a crisp parallelogram of base b and perpendicular height h! Because two congruent triangles fill that whole parallelogram without overlap, ONE triangle holds strictly HALF that area: ONE-HALF BASE TIMES HEIGHT! Even acute or obtuse triangles neatly confirm this inside rectangular enclosures! "
            "Now witness a breathtaking median property! Draw median AD connecting top vertex A straight down to the EXACT MIDPOINT D of opposite base BC! Inspect the two newborn sub-triangles sitting side by side: triangle ABD on the left and triangle ACD on the right! "
            "Notice they often appear completely DIFFERENT in shape—one wide and obtuse, the other narrow and acute! Yet compare BOTH ingredients of their area formula! Base BD strictly EQUALS base CD (because midpoint D bisects BC), AND BOTH sub-triangles share the EXACT SAME apex A and perpendicular altitude h! Equal bases plus identical perpendicular height prove EVERY MEDIAN splits a triangle into TWO EQUAL-AREA HALVES!"
        ),
        "checkpoints": [
            {
                "question": "In triangle PQR, PS is a median drawn from vertex P to midpoint S of side QR. If Area(ΔPQR) = 54 cm², what is Area(ΔPQS)?",
                "options": [
                    "27 cm² (half of 54 cm², equal to Area(ΔPSR))",
                    "18 cm²",
                    "54 cm²",
                    "Cannot be found without knowing ∠P"
                ],
                "answer": 0,
                "hint": "Triangles PQS and PSR share equal bases QS = SR and the exact same perpendicular height from vertex P!",
                "explanation": "A median always divides any triangle into two triangles of equal area: 54 / 2 = 27 cm²."
            },
            {
                "question": "What geometric shape forms when you combine any triangle with an identical congruent rotated copy along one shared edge?",
                "options": [
                    "A parallelogram of area b × h (proving triangle area = ½bh)",
                    "Always a square",
                    "Always a circle",
                    "A trapezoid with unequal parallel heights"
                ],
                "answer": 0,
                "hint": "Opposite sides of the joined rotated copies run equal and parallel!",
                "explanation": "Joining two congruent triangles gives a parallelogram of area bh, directly proving Area(Δ) = ½bh."
            }
        ]
    },
    {
        "id": 10,
        "title": "Heron Formula Triangle",
        "subtitle": "Section 6.8.1 Heron's Formula: Computing Triangle Area √(s(s−a)(s−b)(s−c)) Directly from Three Side Lengths a, b, c",
        "speech": (
            "What happens when a land surveyor measures all THREE boundary fence edges a, b, and c of a triangular plot using a measuring tape—but NO perpendicular height h inside the field is convenient to drop? Enter Section Six Point Eight Point One: HERON'S FORMULA! "
            "Greek mathematician Heron of Alexandria derived an extraordinary direct equation requiring ZERO altitude or angle measurements—ONLY the three boundary side lengths a, b, and c! "
            "Follow Heron's crystal-clear two-step recipe cleanly! Step One: calculate HALF the triangle's full perimeter—called SEMI-PERIMETER s—by computing s equals open a plus b plus c close divided by two! "
            "Step Two: multiply semi-perimeter s together with all three remaining side differences smoothly under one square root: AREA EQUALS SQUARE ROOT OF s TIMES open s minus a close TIMES open s minus b close TIMES open s minus c close! "
            "Verify Heron's Formula immediately on a famous thirteen-fourteen-fifteen centimetre triangle! Semi-perimeter s equals open thirteen plus fourteen plus fifteen close over two equals twenty-one! Differences give twenty-one minus thirteen equals eight, twenty-one minus fourteen equals seven, twenty-one minus fifteen equals six! Multiplying twenty-one times eight times seven times six gives seven thousand fifty-six—whose exact square root equals EIGHTY-FOUR square centimetres!"
        ),
        "checkpoints": [
            {
                "question": "Using Heron's formula, find the area of a triangle with side lengths 5 cm, 12 cm, and 13 cm.",
                "options": [
                    "30 cm²",
                    "60 cm²",
                    "15 cm²",
                    "32.5 cm²"
                ],
                "answer": 0,
                "hint": "Compute s = (5 + 12 + 13)/2 = 15, then √(15 × 10 × 3 × 2)!",
                "explanation": "s = 15 ⇒ Area = √(15 × (15−5) × (15−12) × (15−13)) = √(15 × 10 × 3 × 2) = √900 = 30 cm² (matching right triangle ½(5)(12)!)."
            },
            {
                "question": "What does variable s strictly represent inside Heron's formula √[s(s − a)(s − b)(s − c)]?",
                "options": [
                    "The semi-perimeter: s = (a + b + c) / 2",
                    "The full perimeter: a + b + c",
                    "The shortest side of the triangle",
                    "The perpendicular altitude height"
                ],
                "answer": 0,
                "hint": "'Semi' means half!",
                "explanation": "s denotes semi-perimeter, half of total perimeter a + b + c."
            }
        ]
    },
    {
        "id": 11,
        "title": "Circles Brahmagupta Formula",
        "subtitle": "Section 6.8.1 Circle Radii & Brahmagupta: Triangle Area via R & r (abc/4R, r(a+b+c)/2) & Cyclic Quadrilateral Area",
        "speech": (
            "Now marvel at two breathtaking extensions inside Section Six Point Eight Point One linking triangle areas directly to inscribed circles, circumcircles, and cyclic quadrilaterals! "
            "First, examine TWO circle-radius area formulas for ANY triangle with sides a, b, c! Fit an inscribed circle of inradius r tangent to all three triangle edges! Connecting the incentre straight to all three vertices splits the triangle into three thin sub-triangles each carrying perpendicular height r, summing cleanly to AREA EQUALS r TIMES open a plus b plus c close OVER TWO—simply inradius r TIMES semi-perimeter s! And linking outer circumcircle radius R produces AREA EQUALS PRODUCT a b c DIVIDED BY FOUR CAPITAL R! "
            "Second, watch seventh-century Indian genius BRAHMAGUPTA generalize Heron's triangle formula up to FOUR-SIDED CYCLIC QUADRILATERALS inscribed cleanly inside a circle! "
            "For cyclic sides a, b, c, d and semi-perimeter s equals open a plus b plus c plus d close over two: BRAHMAGUPTA'S AREA EQUALS SQUARE ROOT OF open s minus a close open s minus b close open s minus c close open s minus d close! Notice when side d shrinks smoothly to ZERO, the cyclic quadrilateral turns into a triangle—and Brahmagupta's formula effortlessly collapses RIGHT BACK into Heron's formula!"
        ),
        "checkpoints": [
            {
                "question": "A triangle has sides 13, 14, 15 and area 84 sq. units. Find its incircle radius r using Area = r(a + b + c)/2.",
                "options": [
                    "r = 4 units (since s = 21 and 84 = r × 21 ⇒ r = 4)",
                    "r = 2 units",
                    "r = 7 units",
                    "r = 12 units"
                ],
                "answer": 0,
                "hint": "Recall semi-perimeter s = (a + b + c)/2 = 21, and Area = r × s!",
                "explanation": "Area = r(13 + 14 + 15)/2 = 21r. Setting 21r = 84 gives inradius r = 4 units."
            },
            {
                "question": "What special geometric result occurs inside Brahmagupta's cyclic quadrilateral formula √[(s − a)(s − b)(s − c)(s − d)] when side length d shrinks to 0?",
                "options": [
                    "It reduces directly to Heron's formula √[s(s − a)(s − b)(s − c)] for triangles",
                    "It collapses to zero area always",
                    "It converts into circle area πr²",
                    "It only works for squares"
                ],
                "answer": 0,
                "hint": "Check what factor (s − d) becomes when d = 0!",
                "explanation": "When d = 0, s becomes (a+b+c)/2 and (s − 0) = s, transforming Brahmagupta's formula cleanly into Heron's triangle area formula!"
            }
        ]
    },
    {
        "id": 12,
        "title": "Squaring A Rectangle",
        "subtitle": "Section 6.9 Squaring a Rectangle: Baudhāyana's Śhulbasūtra (c. 800 BCE) Geometric Construction of Square Equal in Area to Rectangle ab",
        "speech": (
            "Step back twenty-eight hundred years to ancient India inside Section Six Point Nine: BAUDHĀYANA'S GEOMETRIC SQUARING OF A RECTANGLE! "
            "Around eight hundred BCE, skilled Vedic altar builders in Baudhāyana's Śhulbasūtras had to transform a rectangular brick altar measuring unequal sides a and b into an exact SQUARE altar holding the EXACT SAME SURFACE AREA a b—using ONLY measuring ropes and wooden pegs, zero algebraic calculators! "
            "Follow Baudhāyana's ingenious geometric transformation step by step! Begin with rectangle ABCD where length a exceeds breadth b! First mark off an exact inner square of side b inside the left portion, leaving one narrow leftover rectangle of width open a minus b close and height b! "
            "Next split that leftover vertical strip lengthwise into TWO identical thinner strips, each measuring width half of open a minus b close! Swing one half-strip cleanly around and attach it along the bottom edge—forming an L-shaped gnomon missing one tiny corner square! Fill that small missing corner virtually to complete one large outer square of side open a plus b close OVER TWO! Applying Baudhāyana's right-triangle rope construction subtracts that corner square's area cleanly, constructing the EXACT equal-area square whose side equals square root a b!"
        ),
        "checkpoints": [
            {
                "question": "What exact mathematical problem does Baudhāyana's Śhulbasūtra (c. 800 BCE) geometric 'squaring of a rectangle' solve?",
                "options": [
                    "Constructing a square whose area is strictly equal to the area ab of any given a × b rectangle (side √(ab))",
                    "Making the perimeter of a square equal to the area of a circle",
                    "Cutting a rectangle into 3 circles",
                    "Proving π = 3.125"
                ],
                "answer": 0,
                "hint": "Think: reshaping an a × b altar into a square of equal surface area!",
                "explanation": "Baudhāyana's compass/rope method transforms an a × b rectangle into an equal-area square of side √(ab)."
            },
            {
                "question": "Algebraically, why does Baudhāyana's gnomon subtraction identity [(a + b)/2]² − [(a − b)/2]² confirm equal area for the constructed square?",
                "options": [
                    "Because [(a + b)/2]² − [(a − b)/2]² simplifies identically to ab (the rectangle's exact area!)",
                    "Because (a + b)² − (a − b)² equals a² + b²",
                    "Because it adds the areas of two circles",
                    "Because a − b always equals 1"
                ],
                "answer": 0,
                "hint": "Divide the Chapter 4 identity (a + b)² − (a − b)² = 4ab by 4!",
                "explanation": "By difference of squares, [(a+b)/2]² − [(a−b)/2]² = 4ab / 4 = ab, yielding target side √(ab) via a right triangle!"
            }
        ]
    },
    {
        "id": 13,
        "title": "Circle Area Proofs",
        "subtitle": "Section 6.10 Area of a Circle: Babylonian/Egyptian Estimates, Archimedes' Proof & Nilakantha Somayājī's Slice Parallelogram (πr²)",
        "speech": (
            "How did ancient mathematicians unlock the curved interior space inside a round circle? Explore Section Six Point Ten: AREA OF A CIRCLE! "
            "Early Babylonian scribes estimated circle area roughly as three times radius squared, while ancient Egyptians used open sixteen-ninths radius close squared (closely approximating three point one six times radius squared)! "
            "Then Greek master Archimedes delivered a rock-solid geometric proof! Inscribe a regular n-sided polygon inside circle radius r! Slicing radially from Centre O splits the polygon into n identical triangles of apothem height h and combined base perimeter P! Total polygon area equals ONE-HALF PERIMETER TIMES APOTHEM HEIGHT! As sides n grow endlessly toward infinity, apothem height converges to radius r and polygon perimeter converges smoothly to circumference two Pi r—yielding ONE-HALF TIMES TWO PI r TIMES r EQUALS PI R SQUARED! "
            "Even better, behold Kerala scholar NILAKANTHA SOMAYĀJĪ'S unforgettable pizza-slice visual proof! Slice a round circular disc radially into thirty-two thin equal wedge sectors, alternate them pointing alternately straight up and straight down, and slide them gently together teeth-to-teeth into a near-RECTANGLE / PARALLELOGRAM of horizontal base HALF-CIRCUMFERENCE PI R and vertical height RADIUS R—immediately revealing exact circle AREA EQUALS PI R SQUARED cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In Nilakantha Somayājī's visual slice-and-rearrange proof of circle area = πr², what base length and height form the rearranged parallelogram-like strip?",
                "options": [
                    "Base = half the circumference (πr) and Height = radius (r), giving πr × r = πr²",
                    "Base = 2πr and Height = r",
                    "Base = πr² and Height = 2r",
                    "Base = diameter 2r and Height = r"
                ],
                "answer": 0,
                "hint": "Half the curved pizza crusts line up along the top edge and half line up along the bottom edge!",
                "explanation": "Interleaving alternating circular wedges places half the circumference (πr) along the base with radial height r: Area = πr × r = πr²."
            },
            {
                "question": "In Archimedes' polygon proof, how does the triangle sum ½ × Perimeter × Height converge to the exact area of a circle?",
                "options": [
                    "As polygon sides n → ∞, perimeter → circumference 2πr and apothem height → radius r, so ½(2πr)(r) = πr²",
                    "As n → ∞, perimeter approaches zero",
                    "Every triangle turns into a square",
                    "Height shrinks to 0"
                ],
                "answer": 0,
                "hint": "Substitute Perimeter = 2πr and Height = r into ½ × P × h!",
                "explanation": "Summing n triangles gives Area = ½ × P_n × h_n → ½ × (2πr) × r = πr²."
            }
        ]
    },
    {
        "id": 14,
        "title": "Sector Segment Area",
        "subtitle": "Section 6.10.1 Area of Sector & Segment: Sector Formula πr²(θ°/360°) & Chord-Bounded Circular Segments",
        "speech": (
            "Now slice crisp pizza wedges and chord caps straight out of circular discs in Section Six Point One Zero Point One: AREA OF A SECTOR AND SEGMENT! "
            "First distinguish the two curved sub-regions unmistakably! A SECTOR looks just like a classic pizza wedge bounded cleanly by TWO straight radii OA, OB meeting at Centre O and ONE curved circular arc AB! Because a full three-hundred-sixty-degree disc spans complete area Pi r squared, any sector sweeping central angle theta degrees claims the exact proportional fraction: SECTOR AREA EQUALS PI R SQUARED TIMES THETA OVER THREE HUNDRED SIXTY! Notice a sleek shortcut too: Sector Area ALSO equals ONE-HALF TIMES ARC LENGTH TIMES RADIUS! "
            "Now contrast that with a CIRCULAR SEGMENT! Connect endpoints A and B of arc AB straight across with one straight chord AB without returning back to Centre O! That D-shaped outer cap trapped strictly between straight CHORD AB and curved ARC AB forms a MINOR CIRCULAR SEGMENT! "
            "How do we calculate its exact area cleanly? Simply evaluate full Sector OAB area first, then SUBTRACT the central isosceles triangle OAB area formed by the two radii and chord—and remember a major segment subtracts the minor segment from total circle area Pi r squared!"
        ),
        "checkpoints": [
            {
                "question": "Calculate the area of a circular sector of radius r = 6 cm with central angle θ = 60° (express in terms of π).",
                "options": [
                    "6π cm²",
                    "36π cm²",
                    "12π cm²",
                    "2π cm²"
                ],
                "answer": 0,
                "hint": "Compute π × 6² × (60° / 360°) = 36π × (1/6)!",
                "explanation": "Area of sector = πr²(θ/360°) = π(36)(60/360) = 6π cm²."
            },
            {
                "question": "What exact two boundary pieces enclose a minor CIRCULAR SEGMENT, and how is its area computed from a central sector?",
                "options": [
                    "Bounded by a chord and an arc; Area(minor segment) = Area(sector OAB) − Area(ΔOAB)",
                    "Bounded by two radii and an arc; Area = Area(sector) + Area(ΔOAB)",
                    "Bounded by three diameters; Area = πr² / 3",
                    "Bounded by a tangent and a diameter"
                ],
                "answer": 0,
                "hint": "Think of slicing the triangle out of a pizza wedge to leave just the outer crust cap!",
                "explanation": "A circular segment lies between a chord and its arc; subtracting inner ΔOAB from sector OAB leaves the minor segment."
            }
        ]
    },
    {
        "id": 15,
        "title": "Multi-Shape Mensuration Strategies",
        "subtitle": "End-of-Chapter Exercise Strategies: Wheel Revolutions, Algebraic Identity Areas, Inscribed Polygon Ratios & Composite Shapes",
        "speech": (
            "Master high-scoring End-of-Chapter Exercise strategies uniting algebraic identities, circular rotations, and composite geometry across NCERT Chapter Six problems! "
            "Strategy One—ROLLING WHEEL REVOLUTIONS! Whenever a bicycle, cart, or road-roller wheel of radius r completes ONE full turn along the ground without slipping, it rolls forward across one exact outer circumference two Pi r! Therefore, TOTAL REVOLUTIONS EQUALS TOTAL DISTANCE COVERED DIVIDED BY TWO PI r! Always convert kilometres or metres cleanly into matching centimetres before dividing! "
            "Strategy Two—ALGEBRAIC IDENTITY AREA DIFFERENCES! Surrounding a rectangular park by a uniform paved walkway, or finding a circular track ring between outer radius R and inner radius r? Rather than computing giant squares separately, factor differences using Chapter Four's difference-of-squares identity a squared minus b squared equals open a plus b close open a minus b close—calculating concentric ring area Pi times open R plus r close open R minus r close almost mentally! "
            "Strategy Three—INSCRIBED POLYGON RATIOS AND COMPOSITE SHAPED FIGURES! Compare inner inscribed squares versus outer circumscribed squares cleanly via common circle diameter two r and Baudhāyana-Pythagoras—while leaf, curved petal, and architectural composite shaded regions combine crisp quarter-circle quadrants smoothly or neatly subtract central triangles and inner rectangles!"
        ),
        "checkpoints": [
            {
                "question": "How many complete revolutions will a bicycle wheel of radius 35 cm make while traveling 1.1 km (110,000 cm)? (Use π ≈ 22/7).",
                "options": [
                    "500 revolutions",
                    "1000 revolutions",
                    "250 revolutions",
                    "50 revolutions"
                ],
                "answer": 0,
                "hint": "Circumference = 2 × (22/7) × 35 = 220 cm; divide 110,000 cm by 220 cm!",
                "explanation": "C = 2 × (22/7) × 35 = 220 cm. Revolutions = 110,000 / 220 = 500 turns."
            },
            {
                "question": "A square is inscribed inside a circle of radius r, and a larger square circumscribes the outside of the exact same circle. What is the exact ratio Area(outer square) : Area(inner square)?",
                "options": [
                    "2 : 1 (since outer side = 2r ⇒ 4r², while inner diagonal = 2r ⇒ area = (2r)²/2 = 2r²)",
                    "4 : 1",
                    "π : 2",
                    "3 : 2"
                ],
                "answer": 0,
                "hint": "Outer square side equals diameter 2r; inner square diagonal equals diameter 2r!",
                "explanation": "Outer square area = (2r)² = 4r². Inner square has side r√2, giving area 2r². Ratio = 4r² : 2r² = 2 : 1."
            }
        ]
    },
    {
        "id": 16,
        "title": "Perimeter Area Synthesis",
        "subtitle": "Chapter Summary: Consolidated Reference of Border Formulas, π History, Arcs, Polygons, Heron, Brahmagupta, Baudhāyana & Sectors",
        "speech": (
            "Congratulations on reaching Slide Sixteen—your master mensuration synthesis uniting every formula and historical milestone of Chapter Six! "
            "Review all four grand pillars clearly! Pillar One—PERIMETERS AND PI: polygon borders sum edge lengths (three a, four a, two open a plus b close), while circle circumference equals two Pi r—where universal irrational constant Pi (proven by Lambert in seventeen sixty-one) was bounded by Archimedes (ninety-six-gon), refined by Zu Chongzhi (three fifty-five over one thirteen) and Āryabhaṭa (three point one four one six), and expressed cleanly via Mādhava's infinite series! "
            "Pillar Two—ARCS AND TRACKS: arc length scales as two Pi r times theta over three sixty, governing four-hundred-metre track staggers and semicircle-path equivalence! "
            "Pillar Three—POLYGON AREAS AND ANCIENT PROOFS: rectangle a b shears to parallelogram b h and halves to triangle one-half b h (equal-area medians), extends via Heron's formula root s open s minus a close open s minus b close open s minus c close and Brahmagupta's cyclic quadrilateral formula, and squares geometrically via Baudhāyana! "
            "Pillar Four—CIRCLES AND SECTORS: Archimedes and Nilakantha prove circle area Pi r squared, scaling to sector area Pi r squared theta over three sixty and segments! Now conquer all four silent mastery quizzes!"
        ),
        "checkpoints": [
            {
                "question": "Which summary statement matches ALL THREE historical mathematicians cleanly to their landmark Chapter 6 discoveries?",
                "options": [
                    "Baudhāyana (~800 BCE): geometric squaring of rectangle; Brahmagupta: cyclic quad area √[(s−a)(s−b)(s−c)(s−d)]; Nilakantha: slice-rearrange visual proof of πr²",
                    "Lambert: 96-gon bounds; Archimedes: cyclic quad area; Mādhava: rectangle squaring",
                    "Zu Chongzhi: 1761 irrationality proof; Heron: infinite π/4 series",
                    "Āryabhaṭa: parallelogram bh cut; Babylonians: 355/113"
                ],
                "answer": 0,
                "hint": "Check Sections 6.2, 6.8.1, 6.9, and 6.10!",
                "explanation": "Baudhāyana squared rectangles in the Śhulbasūtras, Brahmagupta generalized Heron to cyclic quads, and Nilakantha illustrated πr² via slice rearrangement."
            },
            {
                "question": "Compare a sector of central angle θ° and a minor segment on chord AB in a circle of radius r. Which pair of formulas is strictly accurate?",
                "options": [
                    "Arc = 2πr(θ°/360°), Sector Area = πr²(θ°/360°), and Minor Segment = Sector Area − Area(ΔOAB)",
                    "Arc = πr²(θ°/360°) and Sector Area = 2πr(θ°/360°)",
                    "Segment Area = Sector Area + Area(ΔOAB)",
                    "Semicircle Perimeter (closed) = πr without adding diameter 2r"
                ],
                "answer": 0,
                "hint": "Watch out for swapped perimeter/area formulas and subtraction vs addition in segments!",
                "explanation": "Arc scales circumference 2πr, Sector scales area πr², and Minor Segment subtracts central triangle OAB from the sector."
            }
        ]
    }
]
