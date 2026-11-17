#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 6: Measuring Space: Perimeter and Area
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 6.1 to 6.7 with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Border Perimeter Basics",
        "subtitle": "Section 6.1 Perimeter of a Shape: Border Length Definition, Standard Formulas (4a, 3a, 2(a+b)) & Circular Perimeter Question",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Six: Measuring Space—Perimeter and Area! "
            "Whenever builders put fencing around a rectangular garden, painters outline a playground court, or athletes paint white lane lines around a stadium track, what exactly do they measure? In Section Six Point One, PERIMETER means the total boundary distance walked completely around the outer edge of any flat closed two-dimensional shape, returning smoothly to the starting point! "
            "Review three classic straight-edged formulas effortlessly! For an equilateral triangle of side a, adding three equal borders gives perimeter three a! For a square of side a, walking four equal borders gives four a! For a rectangle measuring length a and breadth b, walking opposite pairs twice gives perimeter two times open a plus b close! Notice that even irregular polygons work simply by adding every individual border side length using an ordinary straight ruler! "
            "Wait—what happens when a boundary curves smoothly with zero straight edges at all? Now ask the thrilling Chapter Six question: how can we determine the exact boundary length—the CIRCUMFERENCE—of a perfectly ROUND CIRCLE using just its radius or diameter, without bending fragile rulers or strings around curves, so we can calculate stadium athletic track staggers accurately!"
        ),
        "checkpoints": [
            {
                "question": "What does the perimeter of any two-dimensional shape measure physically?",
                "options": [
                    "The total continuous boundary length around the outer border of the shape",
                    "The flat interior surface enclosed inside the shape",
                    "The thickness of the object in three dimensions",
                    "Only the longest diagonal connecting opposite corners"
                ],
                "answer": 0,
                "hint": "Picture walking all the way around the fence along the outer edge and returning to your start!",
                "explanation": "Perimeter measures total 1D boundary distance around a 2D figure's border."
            },
            {
                "question": "A square garden of side 12 m and a rectangular garden of length 15 m share the exact same perimeter. What is the rectangle's breadth b?",
                "options": [
                    "9 m (since 4 × 12 = 48 = 2(15 + b) ⇒ b = 9 m)",
                    "12 m",
                    "18 m",
                    "6 m"
                ],
                "answer": 0,
                "hint": "Equate square perimeter 4a = 48 m to 2(15 + b)!",
                "explanation": "Perimeter = 4 × 12 = 48 m. Setting 2(15 + b) = 48 gives 15 + b = 24 ⇒ b = 9 m."
            }
        ]
    },
    {
        "id": 2,
        "title": "Constant Pi Ratio",
        "subtitle": "Section 6.2 Perimeter of a Circle: Constant Ratio C/D = π, Mesopotamia (~1900 BCE) & Archimedes' 96-Gon Bounds",
        "speech": (
            "Roll any round bangle, bicycle tyre, bottle cap, or dinner plate across a straight flat floor to uncover Section Six Point Two! Measure each circle's outer circumference C with a thread and divide cleanly by its straight diameter D passing through the centre! "
            "Whether the circle spans two centimetres across a coin, fifty centimetres across a bicycle wheel, or thousands of kilometres around Earth's equator, dividing circumference C by diameter D ALWAYS produces the exact same universal ratio—celebrated worldwide by the Greek symbol PI! Because all circles share identical geometric shape regardless of size, that golden constant yields our famous circumference formula: C equals Pi times D, or equivalently two Pi r! "
            "How did ancient civilizations estimate Pi long before modern computers? Around nineteen hundred BCE in ancient Mesopotamia, clay-tablet scribes inscribed regular hexagons of perimeter six r inside circles and refined the ratio slightly upward, setting Pi approximately equal to three point one two five (three and one-eighth)! "
            "Centuries later around two hundred fifty BCE, Greek genius Archimedes trapped circles tightly between inscribed and circumscribed regular polygons—pushing carefully from hexagons up to NINETY-SIX-SIDED polygons! Archimedes rigorously proved Pi sits strictly squeezed between three and ten seventy-firsts and three and one-seventh!"
        ),
        "checkpoints": [
            {
                "question": "Whenever you divide the circumference C of ANY circle by its diameter D, what constant result always appears?",
                "options": [
                    "The universal mathematical constant π (≈ 3.14159...)",
                    "A number that grows larger for larger circles",
                    "Exactly 4 for every circle",
                    "The circle's radius r"
                ],
                "answer": 0,
                "hint": "Remember all circles are geometrically similar, keeping C / D completely scale-invariant!",
                "explanation": "Every circle maintains the constant circumference-to-diameter ratio C/D = π, yielding C = πD = 2πr."
            },
            {
                "question": "Around 250 BCE, how did Archimedes tightly bound the numerical value of π using polygons up to 96 sides?",
                "options": [
                    "3 10/71 < π < 3 1/7 (i.e., 223/71 < π < 22/7)",
                    "π = 3.125 exactly",
                    "2 < π < 3",
                    "355/113 = π exactly"
                ],
                "answer": 0,
                "hint": "Recall the classic upper bound 3 1/7 = 22/7 paired with the tight 96-gon lower bound 3 10/71!",
                "explanation": "Archimedes sandwiched circular perimeter between inscribed and circumscribed 96-gons to prove 3 10/71 < π < 3 1/7."
            }
        ]
    },
    {
        "id": 3,
        "title": "Global Pi Scholars",
        "subtitle": "Section 6.2 Historical Approximations: Ptolemy, Liu Hui, Zu Chongzhi (355/113), Āryabhaṭa, Brahmagupta, Nilakantha & Mādhava Series",
        "speech": (
            "Follow the thrilling multicultural relay race across centuries to sharpen Pi's decimal digits inside Section Six Point Two! "
            "In Alexandria, astronomer Ptolemy used circle chords in trigonometric tables to estimate Pi around three point one four one six! In third-century China, Liu Hui iteratively doubled polygon sides beyond three thousand sides to refine Pi cleanly! Then in four hundred eighty CE, Chinese mathematician Zu Chongzhi painstakingly computed regular polygons of twenty-four thousand five hundred seventy-six sides—discovering the astonishingly accurate fraction THREE HUNDRED FIFTY-FIVE DIVIDED BY ONE HUNDRED THIRTEEN, matching true Pi cleanly to six full decimal places! "
            "Meanwhile in India, mathematical precision soared remarkably high across generations! Āryabhaṭa gave three point one four one six via the elegant ratio sixty-two thousand eight hundred thirty-two over twenty thousand! Brahmagupta often used square root of ten for rapid astronomical calculations, while Nilakantha Somayājī later pioneered rapidly converging alternating series! "
            "Above all, in fourteenth-century Kerala, Mādhava of Saṅgamagrāma achieved a historic breakthrough bridging circle geometry and infinite analysis—discovering the FIRST EXACT INFINITE SERIES FOR PI: Pi divided by four equals one minus one-third plus one-fifth minus one-seventh continuing endlessly forever—allowing mathematicians to compute Pi cleanly to arbitrarily many digits!"
        ),
        "checkpoints": [
            {
                "question": "Which historical mathematician utilized 24,576-sided polygons in 480 CE to discover the ultra-accurate rational fraction 355/113 for π?",
                "options": [
                    "Zu Chongzhi",
                    "Archimedes",
                    "Brahmagupta",
                    "Mesopotamian scribes"
                ],
                "answer": 0,
                "hint": "Note 355/113 ≈ 3.1415929... stays accurate to 6 decimal places!",
                "explanation": "Zu Chongzhi (480 CE) computed inscribed 24,576-gons to discover 355/113 (Milü)."
            },
            {
                "question": "Who discovered the first exact infinite series formula π/4 = 1 − 1/3 + 1/5 − 1/7 + ... bridging circle geometry and calculus?",
                "options": [
                    "Mādhava of Saṅgamagrāma",
                    "Ptolemy",
                    "Liu Hui",
                    "Johann Lambert"
                ],
                "answer": 0,
                "hint": "Recall the 14th-century founder of the Kerala School of Mathematics!",
                "explanation": "Mādhava of Saṅgamagrāma derived the infinite alternating odd-reciprocal series for π/4 centuries before European calculus."
            }
        ]
    },
    {
        "id": 4,
        "title": "Pi Is Irrational",
        "subtitle": "Section 6.3 π is Irrational: Infinite Non-Repeating Digits, Lambert (1761), Approximations (≈) & Pi Days",
        "speech": (
            "Notice a subtle mathematical misconception right at the heart of Section Six Point Three! Textbooks routinely substitute twenty-two sevenths or three point one four for Pi in school geometry exercises—leading many learners to mistakenly believe Pi EQUALS twenty-two sevenths! "
            "Erase that myth permanently right now! Is twenty-two sevenths actually equal to Pi? NO! Twenty-two divided by seven produces three point one four two eight five seven repeating endlessly in a crisp six-digit rational block! Even Zu Chongzhi's extraordinary fraction three hundred fifty-five over one hundred thirteen—though accurate to six digits—remains a rational ratio of integers, slightly above Pi! "
            "In seventeen hundred sixty-one, Swiss mathematician Johann Heinrich Lambert used continued fractions to rigorously prove that PI IS GENUINELY AN IRRATIONAL NUMBER! Its true decimal expansion—three point one four one five nine two six five three five eight nine seven nine...—continues infinitely with ZERO termination and ZERO repeating pattern! "
            "Therefore ALWAYS read twenty-two sevenths and three point one four with the approximately equal symbol (≈) rather than exact equals! And celebrate two playful annual calendar dates honoring these approximations worldwide: PI DAY every March fourteen (three-one-four) and PI APPROXIMATION DAY every July twenty-two (twenty-two-over-seven in international day-month format)!"
        ),
        "checkpoints": [
            {
                "question": "Why is 22/7 strictly ONLY an approximation (π ≈ 22/7) rather than the exact value of π?",
                "options": [
                    "22/7 is a rational repeating decimal (3.142857̄), whereas Johann Lambert proved in 1761 that π is irrational with infinite non-repeating digits",
                    "22/7 is slightly smaller than 3",
                    "π stops cleanly after 4 decimal places",
                    "22/7 equals Zu Chongzhi's 355/113"
                ],
                "answer": 0,
                "hint": "Every ratio p/q of integers is rational and terminates or repeats; π is irrational!",
                "explanation": "π ≈ 3.14159... is irrational (proven by Lambert, 1761); 22/7 = 3.142857... is merely a convenient rational estimate."
            },
            {
                "question": "Which two calendar dates celebrate Pi Day (decimal digits 3.14) and Pi Approximation Day (fraction 22/7)?",
                "options": [
                    "March 14 (3/14) and July 22 (22/7)",
                    "April 13 and August 22",
                    "January 7 and December 25",
                    "May 14 and June 22"
                ],
                "answer": 0,
                "hint": "Match month/day numbers cleanly to 3.14 and 22/7!",
                "explanation": "March 14 matches 3.14 (Pi Day), while July 22 in day/month format (22/7) marks Pi Approximation Day."
            }
        ]
    },
    {
        "id": 5,
        "title": "Arcs Running Tracks",
        "subtitle": "Section 6.4 Length of an Arc: Semicircles (πr), Quarters (πr/2), General Arc Formula 2πr(θ°/360°) & 400 m Track Staggers",
        "speech": (
            "Now apply circular circumference proportionally to curved arcs and real stadium athletics tracks in Section Six Point Four! "
            "One complete revolution around a circle sweeps three hundred sixty degrees at the centre, tracing full circumference two Pi r! What length does ONE-HALF circle (a semicircle) sweep through one hundred eighty degrees? Half of two Pi r equals PI R! What about a quarter circle sweeping ninety degrees? One-fourth of two Pi r equals PI R DIVIDED BY TWO! "
            "Follow exact direct proportionality for ANY central angle theta degrees: ARC LENGTH EQUALS FULL CIRCUMFERENCE TWO PI R MULTIPLIED BY FRACTION THETA OVER THREE HUNDRED SIXTY! "
            "Now step onto an Olympic four-hundred-metre athletics running track! Every standard stadium oval connects TWO equal straight sections alongside TWO identical semicircular bends forming one combined circle! Wait—why do sprinters in outer lanes start staggered precise metres AHEAD of runners in innermost lane one? "
            "Because each outer lane curve holds a LARGER radius r plus lane width w! Full extra curve distance per full lap around both bends equals two Pi times lane width w—requiring exact forward STAGGER starting marks so every competing athlete runs fairly across exactly four hundred metres!"
        ),
        "checkpoints": [
            {
                "question": "Calculate the arc length of a sector with radius r = 21 cm subtending central angle θ = 60° (use π ≈ 22/7).",
                "options": [
                    "22 cm",
                    "44 cm",
                    "11 cm",
                    "132 cm"
                ],
                "answer": 0,
                "hint": "Apply 2πr × (60° / 360°) = 2 × (22/7) × 21 × (1/6)!",
                "explanation": "Arc length = 2 × (22/7) × 21 × (60/360) = 132 × (1/6) = 22 cm."
            },
            {
                "question": "Why must runners in outer lanes of a 400 m athletics track start staggered ahead of inner-lane runners?",
                "options": [
                    "Outer semicircular bends have larger radii (r + w), making outer curved arc paths longer by 2πw per full lap",
                    "Straight sections are longer in outer lanes",
                    "Outer runners face stronger gravity",
                    "To make outer runners sprint fewer total metres"
                ],
                "answer": 0,
                "hint": "Straight sections keep identical length in every lane; only the two semicircular bends change radius!",
                "explanation": "Increasing radius from r to r + w adds 2πw to the combined semicircular curve length, compensated via stagger starts."
            }
        ]
    },
    {
        "id": 6,
        "title": "Perimeter Path Puzzles",
        "subtitle": "Section 6.5 Problems, Puzzles & Paradoxes: Intersecting Circles, Semicircle Chain Equivalence & Flower Petal Borders",
        "speech": (
            "Ready for mind-bending geometric surprises inside Section Six Point Five: PERIMETER PROBLEMS, PUZZLES AND PARADOXES? "
            "Test the celebrated SEMICIRCLE PATH PARADOX right now! Suppose highway route A travels smoothly from city P to city Q along ONE giant semicircular arc of diameter ten kilometres! Meanwhile, winding curved path B hops from P to Q across FIVE tiny touching semicircles sitting along diameter PQ whose individual diameters add up neatly to ten kilometres! Which route covers fewer kilometres? Wait—calculate BOTH curved lengths carefully! "
            "Giant semicircle length equals Pi times D divided by two equals five Pi kilometres! Winding path B sums five tiny halves: Pi times open d one plus d two plus d three plus d four plus d five close divided by two! Because all small diameters total ten kilometres, Path B equals FIVE PI TOO—BOTH CURVED ROUTES ARE IDENTICALLY EQUAL! Distributivity cancels scale subdivisions completely! "
            "Explore intersecting-circle chains and symmetric four-petal flower borders drawn inside squares and equilateral triangles too: decomposing complex curved borders into clean fractional arcs computes exact total border perimeters effortlessly using central angles and exact radii without guessing!"
            " Try sliding intersecting circles horizontally right now—watching total perimeter stay surprisingly predictable!"
        ),
        "checkpoints": [
            {
                "question": "Route A moves from X to Y along 1 large semicircle of diameter 14 cm, while Route B connects X to Y via 3 touching semicircles of diameters 4 cm, 6 cm, and 4 cm. Which route is longer?",
                "options": [
                    "Both routes have the EXACT SAME length (7π cm each!)",
                    "Route A is longer than Route B",
                    "Route B is 3 times longer than Route A",
                    "Cannot be determined without height"
                ],
                "answer": 0,
                "hint": "Factor out π/2 from Route B: (π/2)(4 + 6 + 4)!",
                "explanation": "Route A = (π/2)(14) = 7π cm. Route B = (π/2)(4 + 6 + 4) = (π/2)(14) = 7π cm. Exact tie!"
            },
            {
                "question": "A decorative 4-petal border inside a square of side 14 cm is formed by 4 semicircles drawn inward using each square edge as a diameter. What is the total curved petal perimeter (use π ≈ 22/7)?",
                "options": [
                    "88 cm (4 semicircles = 2 full circles of diameter 14 cm)",
                    "44 cm",
                    "56 cm",
                    "176 cm"
                ],
                "answer": 0,
                "hint": "4 identical semicircles of diameter 14 cm combine into 2 full circumferences of π × 14!",
                "explanation": "Total curved arc length = 4 × (π × 14 / 2) = 2 × (22/7) × 14 = 88 cm."
            }
        ]
    },
    {
        "id": 7,
        "title": "Rectangle Area Space",
        "subtitle": "Section 6.6 Area of a Rectangle: 2D Space Measurement in Square Units (1 unit²) & Area Formula A = ab",
        "speech": (
            "Now shift smoothly from one-dimensional outer border perimeters to two-dimensional flat interior surfaces in Section Six Point Six: AREA OF A RECTANGLE! "
            "While perimeter wraps a taut measuring tape strictly around a field's outer fence, AREA quantifies how much flat two-dimensional space lies completely enclosed INSIDE the closed figure—representing the exact paint needed to coat a classroom wall or square floor tiles required to pave a hall! "
            "How does geometry standardize area measurement cleanly? Draw one crisp unit square measuring length one unit by width one unit—defining its enclosed flat interior strictly EQUAL TO ONE SQUARE UNIT (such as one square centimetre or one square metre)! "
            "Now align a rectangle measuring height a units by width b units carefully onto a square grid! Count a horizontal rows stacked vertically, each row packed smoothly without gaps or overlaps by b identical unit squares! Multiplying rows times columns immediately reveals total non-overlapping square coverage: RECTANGLE AREA EQUALS LENGTH TIMES BREADTH—A TIMES B SQUARE UNITS! Even fractional edge lengths like three-and-a-half by two-and-a-quarter pack seamlessly by subdividing each unit square into finer equal grid tiles—and observe that shapes sharing identical perimeters can enclose wildly different flat interior areas!"
        ),
        "checkpoints": [
            {
                "question": "If a rectangular classroom floor measures 8.5 m long and 6 m wide, what total floor space (area) does it cover?",
                "options": [
                    "51 m²",
                    "29 m²",
                    "14.5 m²",
                    "51 m"
                ],
                "answer": 0,
                "hint": "Multiply length × breadth and keep squared area units (m²)!",
                "explanation": "Area = a × b = 8.5 m × 6 m = 51 m². (29 m would be its perimeter!)"
            },
            {
                "question": "What happens to the area of a rectangle if BOTH its length a and breadth b are doubled (2a and 2b)?",
                "options": [
                    "The area becomes 4 times larger (4ab)",
                    "The area doubles (2ab)",
                    "The area triples (3ab)",
                    "The area stays unchanged"
                ],
                "answer": 0,
                "hint": "Substitute 2a and 2b into Area = length × breadth!",
                "explanation": "New area = (2a)(2b) = 4ab, quadrupling the enclosed surface space."
            }
        ]
    },
    {
        "id": 8,
        "title": "Parallelogram Transformation Area",
        "subtitle": "Section 6.7 Area of a Parallelogram: Rectangle Shear/Cut Transformation (Area = bh) & Oblique/Thin Parallelograms",
        "speech": (
            "Now unlock the remarkable geometric transformation magic inside Section Six Point Seven: AREA OF A PARALLELOGRAM! "
            "Inspect a tilted parallelogram ABCD resting on horizontal base b with slanted side edge l and vertical perpendicular height h between its parallel opposite sides! Wait—does its interior area equal base times SLANT SIDE l, or base times PERPENDICULAR HEIGHT h? NEVER fall for the slant-side trap—slanting increases slant edge while squashing perpendicular height! "
            "Prove the exact formula using clean scissor geometry! Slice off the projecting right-triangular overhang right along perpendicular height line h on the left side of your parallelogram, slide that exact congruent triangle smoothly across to the matching gap on the right side—and SNAP! What upright figure clicks effortlessly into place? An exact RECTANGLE carrying identical base b and identical vertical height h! Since cutting and rearranging preserves total space, PARALLELOGRAM AREA EQUALS BASE TIMES HEIGHT—b h! "
            "Wait—what about an EXTREME OBLIQUE, razor-thin parallelogram tilted so dramatically that the perpendicular drop from top corner C falls completely OUTSIDE base edge segment AB onto its horizontal extension? Even in that extreme case, slicing and sliding horizontal shear strips preserves exact area BASE TIMES PERPENDICULAR HEIGHT b h!"
        ),
        "checkpoints": [
            {
                "question": "A parallelogram has horizontal base 14 cm, slanted edge 10 cm, and perpendicular vertical height 6 cm between parallel bases. What is its exact area?",
                "options": [
                    "84 cm² (base 14 × height 6)",
                    "140 cm² (base 14 × slant side 10)",
                    "60 cm²",
                    "48 cm²"
                ],
                "answer": 0,
                "hint": "Always use perpendicular altitude h = 6 cm, NOT slanted side 10 cm!",
                "explanation": "Cutting and shifting the triangular overhang forms a 14 cm × 6 cm rectangle of area bh = 84 cm²."
            },
            {
                "question": "In a strongly tilted oblique parallelogram where the perpendicular altitude h from top corner D drops strictly OUTSIDE base edge AB onto extended line AB, how do we compute its area?",
                "options": [
                    "Still base AB × perpendicular height h identically",
                    "Zero because altitude falls outside",
                    "Half of base × height",
                    "Base × slant side instead"
                ],
                "answer": 0,
                "hint": "Area depends solely on the chosen base length and perpendicular gap between the two parallel lines!",
                "explanation": "By shearing/parallelogram decomposition on parallel strips, Area = base × perpendicular height holds even when the altitude foot falls outside the base segment."
            }
        ]
    }
]
