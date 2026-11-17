#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 12: Quadrilaterals
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Planar Quadrilateral Definition",
        "subtitle": "Section 12.1 What Exactly is a Quadrilateral?: Planar, Non-Collinear & Non-Self-Intersecting Rules",
        "speech": (
            "Welcome to Chapter Twelve: Quadrilaterals! You have seen four-sided shapes since primary school—yet in rigorous geometry, defining a quadrilateral precisely requires four strict guardrails inside Section Twelve Point One! "
            "Take four distinct points A, B, C, and D joined in order by segments AB, BC, CD, and DA! Why can't we stop there? Test four failure cases! "
            "Failure One—COLLINEAR POINTS: if three or four vertices lie on a single straight line, the figure collapses into a triangle or flat segment instead of a true four-sided polygon! So NO three vertices may be collinear! "
            "Failure Two—NON-PLANAR OR SKEW QUADRILATERALS: fold a paper quadrilateral along its diagonal into three-dimensional space! Those four points no longer lie in one flat plane, and their interior angle sum drops strictly BELOW three hundred sixty degrees! So all four vertices MUST be coplanar! "
            "Failure Three—SELF-INTERSECTING BOWTIE LINKAGES: if opposite segments cross each other like an X, they break simple interior-exterior separation and create ambiguous regions! Failure Four—OPEN PATHS: the final segment DA MUST close seamlessly back to vertex A instead of leaving an open gap! Putting all four conditions together defines a clean, closed, planar, non-self-intersecting quadrilateral—and guarantees that its four interior angles always add up to exactly three hundred sixty degrees!"
        ),
        "checkpoints": [
            {
                "question": "Which condition MUST hold for four segments AB, BC, CD, DA to form a standard planar quadrilateral?",
                "options": [
                    "All four vertices are coplanar, no three are collinear, segments do not self-intersect, and the path is closed",
                    "Three vertices lie on one straight line",
                    "Opposite sides cross each other in an X-shape",
                    "The four vertices lie in two different 3D planes"
                ],
                "answer": 0,
                "hint": "Recall all four guardrails: closed, coplanar, non-collinear triples, and non-self-intersecting!",
                "explanation": "Eliminating collinear triples, 3D skew vertices, bowtie crossings, and open paths gives a well-defined planar quadrilateral."
            },
            {
                "question": "What happens if three vertices of a 4-point closed figure lie on the exact same straight line?",
                "options": [
                    "Two adjacent edges merge into one straight side, collapsing the figure into a triangle",
                    "It forms a regular square",
                    "Its angle sum becomes 540°",
                    "It becomes a circle"
                ],
                "answer": 0,
                "hint": "Imagine A, B, C collinear with D outside the line: AB + BC is just segment AC!",
                "explanation": "Collinear adjacent vertices reduce the number of true sides from 4 to 3 (a triangle)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Convex Non-Convex Quadrilaterals",
        "subtitle": "Section 12.1 Convexity: Interior Angles (< 180° vs > 180° Dent) & Diagonal Intersection",
        "speech": (
            "Now classify planar quadrilaterals into two fundamental families inside Section Twelve Point One: CONVEX versus NON-CONVEX (also called concave)! "
            "In a CONVEX QUADRILATERAL—such as a square, rectangle, parallelogram, rhombus, or trapezium—EVERY single one of its four interior angles measures STRICTLY LESS than one hundred eighty degrees! Draw both diagonals AC and BD inside any convex quadrilateral: BOTH diagonals lie completely INSIDE the shape and ALWAYS cross each other at an interior point! Furthermore, extending any side into an infinite line leaves the entire quadrilateral on ONE side of that line! "
            "Now push one vertex inward past the opposite diagonal until you create a sharp 'dent'—like an arrowhead or boomerang! That dented interior angle now opens wider than a straight line, measuring STRICTLY GREATER than one hundred eighty degrees (a reflex angle)! "
            "Immediately notice two dramatic consequences in every NON-CONVEX quadrilateral! First, one diagonal lies completely OUTSIDE the dented region, bridging across the inward cavity! Second, the two diagonals NEVER intersect each other anywhere as line segments! Yet remarkably, triangulating from the dented reflex vertex into two non-overlapping triangles proves the four interior angles STILL sum to exactly three hundred sixty degrees—just like every convex quadrilateral!"
        ),
        "checkpoints": [
            {
                "question": "Which property ALWAYS distinguishes a NON-CONVEX (concave) quadrilateral from a convex one?",
                "options": [
                    "It has one reflex interior angle > 180°, one diagonal lies outside the shape, and its two diagonals do not intersect",
                    "All four interior angles are acute (< 90°)",
                    "Its interior angles sum to 180°",
                    "Both diagonals lie completely inside and cross at 90°"
                ],
                "answer": 0,
                "hint": "Think of an arrowhead/boomerang shape with an inward dent!",
                "explanation": "A non-convex quadrilateral has exactly one reflex interior angle (> 180°), forcing one diagonal outside and preventing diagonal intersection."
            },
            {
                "question": "Does the 360° interior angle sum still hold for a planar NON-CONVEX quadrilateral?",
                "options": [
                    "Yes — drawing the internal diagonal from the reflex vertex splits it into two triangles (180° + 180° = 360°)",
                    "No — its angle sum is 540°",
                    "No — its angle sum is 180°",
                    "Only if it is a kite"
                ],
                "answer": 0,
                "hint": "Even with a dent, the internal diagonal divides the region into 2 triangles!",
                "explanation": "Triangulation along the interior diagonal preserves the 360° angle sum for all simple planar quadrilaterals."
            }
        ]
    },
    {
        "id": 3,
        "title": "Opposite Sides Converse",
        "subtitle": "Section 12.2 Theorem 2: Converse of Opposite Sides Equality (SSS Congruence Proof)",
        "speech": (
            "Now turn to Section Twelve Point Two: CONVERSES OF PARALLELOGRAM THEOREMS! Knowing that a parallelogram has equal opposite sides, equal opposite angles, and bisecting diagonals is only half the story—how do we PROVE a mystery quadrilateral IS a parallelogram? By proving the converses as official parallelogram tests! "
            "Begin with THEOREM TWO (Converse of Opposite Sides Equality): If BOTH pairs of opposite sides of a quadrilateral are equal—meaning AB equals CD and BC equals DA—then the quadrilateral MUST be a parallelogram! "
            "Follow this crisp SSS congruence proof! Draw diagonal AC splitting quadrilateral ABCD into two triangles: triangle ABC and triangle CDA! Compare their three side pairs: AB equals CD (given), BC equals DA (given), and AC equals CA (shared common side)! By SSS CONGRUENCE, triangle ABC is congruent to triangle CDA! "
            "By corresponding parts (CPCTC), angle BAC equals angle DCA—forming equal alternate interior angles across transversal AC, which proves side AB is strictly PARALLEL to side CD! Similarly, angle BCA equals angle DAC proves side BC is strictly PARALLEL to side DA! Because BOTH pairs of opposite sides are parallel, ABCD is rigorously proven to be a parallelogram! This gives us our first official side-length test!"
        ),
        "checkpoints": [
            {
                "question": "In Theorem 2 (Given AB = CD and BC = DA in quadrilateral ABCD), which congruence criterion proves △ABC ≅ △CDA after drawing diagonal AC?",
                "options": [
                    "SSS Congruence (AB = CD, BC = DA, and shared side AC = CA)",
                    "AAA Similarity",
                    "SSA Criterion",
                    "RHS Criterion"
                ],
                "answer": 0,
                "hint": "We are only given side-length equalities, plus one shared diagonal!",
                "explanation": "Three pairs of equal sides establish △ABC ≅ △CDA by SSS, yielding equal alternate interior angles to prove parallelism."
            },
            {
                "question": "After proving △ABC ≅ △CDA in Theorem 2, how do we deduce that AB ∥ CD?",
                "options": [
                    "By CPCTC, alternate interior angles ∠BAC and ∠DCA are equal, which proves AB ∥ CD",
                    "Because all four angles are 90°",
                    "Because AC is perpendicular to BD",
                    "By assuming it is a square"
                ],
                "answer": 0,
                "hint": "Recall the Z-pattern alternate interior angles test for parallel lines!",
                "explanation": "Equal alternate interior angles formed by transversal AC force AB ∥ CD (and similarly BC ∥ DA)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Opposite Angles Converse",
        "subtitle": "Section 12.2 Theorem 3: Converse of Opposite Angles Equality (Interior Angle Algebra Proof)",
        "speech": (
            "Now prove THEOREM THREE inside Section Twelve Point Two (Converse of Opposite Angles Equality): If BOTH pairs of opposite angles of a quadrilateral are equal—meaning angle A equals angle C and angle B equals angle D—then ABCD MUST be a parallelogram! "
            "Watch how cleanly algebra replaces triangle congruence here! We know the four interior angles of any planar quadrilateral sum to three hundred sixty degrees: angle A plus angle B plus angle C plus angle D equals three hundred sixty! "
            "Now substitute angle C equals angle A and angle D equals angle B! That turns the equation into TWO TIMES angle A plus TWO TIMES angle B equals three hundred sixty degrees! Divide every term by two: ANGLE A PLUS ANGLE B EQUALS ONE HUNDRED EIGHTY DEGREES! "
            "Look at transversal AB cutting segments AD and BC! Angles A and B are CONSECUTIVE INTERIOR (co-interior) angles summing to one hundred eighty degrees—which proves AD is strictly PARALLEL to BC! Repeating the exact same substitution with angle B and angle C gives angle A plus angle D equals one hundred eighty degrees, proving AB is strictly PARALLEL to DC! Hence ABCD is rigorously proven to be a parallelogram!"
        ),
        "checkpoints": [
            {
                "question": "In Theorem 3 (Given ∠A = ∠C and ∠B = ∠D), what does substituting into ∠A + ∠B + ∠C + ∠D = 360° immediately yield?",
                "options": [
                    "2(∠A + ∠B) = 360° ⇒ ∠A + ∠B = 180°, showing co-interior angles are supplementary so AD ∥ BC",
                    "∠A = ∠B = 90° always",
                    "∠A + ∠C = 180°",
                    "∠A − ∠B = 90°"
                ],
                "answer": 0,
                "hint": "Replace ∠C with ∠A and ∠D with ∠B, then divide by 2!",
                "explanation": "Co-interior angles summing to 180° prove AD ∥ BC (and similarly ∠A + ∠D = 180° proves AB ∥ DC)."
            },
            {
                "question": "If a quadrilateral has angles 70°, 110°, 70°, 110° in cyclic order, is it guaranteed to be a parallelogram?",
                "options": [
                    "Yes — both pairs of opposite angles are equal, satisfying Theorem 3",
                    "No — only rectangles have 360° angle sums",
                    "Only if all sides are 5 cm",
                    "No — it must be a trapezium that is not a parallelogram"
                ],
                "answer": 0,
                "hint": "Check whether opposite angles are equal: 70° = 70° and 110° = 110°!",
                "explanation": "Equal opposite angles satisfy Theorem 3, guaranteeing both pairs of opposite sides are parallel."
            }
        ]
    },
    {
        "id": 5,
        "title": "Diagonals Bisection Converse",
        "subtitle": "Section 12.2 Theorems 4 & 5: Bisecting Diagonals Test (SAS) & Single Equal-Parallel Pair Test",
        "speech": (
            "Now master the remaining two parallelogram identification tests inside Section Twelve Point Two: THEOREM FOUR AND THEOREM FIVE! "
            "THEOREM FOUR (Converse of Bisecting Diagonals): If the diagonals AC and BD of quadrilateral ABCD bisect each other at intersection O—so AO equals OC and BO equals OD—then ABCD MUST be a parallelogram! Look at triangles AOB and COD: AO equals OC (given), BO equals OD (given), and vertically opposite angles AOB and COD are equal! By SAS CONGRUENCE, triangle AOB is congruent to triangle COD! Therefore angle OAB equals angle OCD, proving AB is parallel to CD; similarly triangle AOD congruent to triangle COB proves AD is parallel to BC! "
            "Now inspect THEOREM FIVE (Single-Pair Test): If JUST ONE pair of opposite sides is BOTH EQUAL AND PARALLEL (say AB equals CD AND AB is parallel to CD), is ABCD a parallelogram? YES! Draw diagonal AC: equal alternate interior angles BAC and DCA, plus AB equals CD, plus shared side AC give SAS congruence between triangles ABC and CDA! By CPCTC, BC equals DA and alternate angles prove BC is parallel to DA—making ABCD a parallelogram! Together, Theorems Two through Five give us four complete tests!"
        ),
        "checkpoints": [
            {
                "question": "In Theorem 4 (diagonals bisect each other: AO = OC and BO = OD), which congruence criterion proves △AOB ≅ △COD?",
                "options": [
                    "SAS Congruence (AO = OC, vertically opposite ∠AOB = ∠COD, and BO = OD)",
                    "SSS Congruence",
                    "ASA Congruence",
                    "RHS Congruence"
                ],
                "answer": 0,
                "hint": "Notice the vertically opposite angles right between the two bisected half-diagonals!",
                "explanation": "Two pairs of equal half-diagonals with the included vertically opposite angles give SAS congruence."
            },
            {
                "question": "Which single-pair condition on opposite sides AB and CD is SUFFICIENT (Theorem 5) to prove ABCD is a parallelogram?",
                "options": [
                    "AB = CD AND AB ∥ CD (the SAME pair is both equal and parallel)",
                    "AB = CD and AD = BC is not needed, just AB = CD alone",
                    "AB ∥ CD and AD = BC (one pair parallel, the OTHER pair equal)",
                    "Only AB = BC"
                ],
                "answer": 0,
                "hint": "Beware of an isosceles trapezium where one pair is parallel and the OTHER pair is equal!",
                "explanation": "Theorem 5 requires the SAME pair of opposite sides to be both equal in length and parallel."
            }
        ]
    },
    {
        "id": 6,
        "title": "Linkages Force Vectors",
        "subtitle": "Section 12.3 Applications of Parallelograms: Watt's Linkage, Pantographs & Physics Force Vectors",
        "speech": (
            "Why do mechanical engineers and physicists love parallelograms so much? Discover three real-world marvels inside Section Twelve Point Three: APPLICATIONS OF PARALLELOGRAMS! "
            "Application One—PANTOGRAPHS FOR DRAWING SCALING! A pantograph connects four rigid bars pinned into a flexible parallelogram linkage! When you trace a small map or architectural sketch with one pointer, a pen attached to an extended bar automatically draws a perfectly scaled enlarged or reduced copy—because opposite sides stay strictly parallel throughout every motion! "
            "Application Two—JAMES WATT'S PARALLEL MOTION LINKAGE! During the Industrial Revolution, steam engine pistons moved strictly up and down along a straight line while beam engines rocked in circular arcs! James Watt combined a four-bar linkage with parallelogram geometry so the piston rod stayed nearly straight without jamming! "
            "Application Three—PHYSICS FORCE VECTORS! When two forces F one and F two pull an object simultaneously at an angle from a common point, their combined net resultant force equals the main diagonal of the parallelogram formed by vectors F one and F two—known across physics and engineering as the Parallelogram Law of Vector Addition! Thus simple parallelogram theorems power precision drafting tools, steam engines, and classical mechanics alike in everyday modern engineering today!"
        ),
        "checkpoints": [
            {
                "question": "How does a pantograph linkage accurately enlarge or shrink a drawing as a user traces the original?",
                "options": [
                    "Pinned parallelogram bars keep opposite sides strictly parallel at all angles, preserving similar triangles and a constant scaling ratio",
                    "By locking all four angles at 90° permanently",
                    "By using a circular compass only",
                    "By changing bar lengths continuously"
                ],
                "answer": 0,
                "hint": "Think about flexible parallelogram linkages preserving parallelism while angles change!",
                "explanation": "Parallelism of opposite sides keeps the tracing and drawing points collinear with the pivot in a fixed similarity ratio."
            },
            {
                "question": "In physics, how does the Parallelogram Law determine the combined resultant of two forces F₁ and F₂ acting at a point?",
                "options": [
                    "As the diagonal of the parallelogram whose adjacent sides represent vectors F₁ and F₂",
                    "As the perimeter of the parallelogram",
                    "As the difference of their areas",
                    "By ignoring the angle between F₁ and F₂"
                ],
                "answer": 0,
                "hint": "Draw F₁ and F₂ tail-to-tail as adjacent sides of a parallelogram!",
                "explanation": "The vector sum F₁ + F₂ corresponds geometrically to the main diagonal from the common origin."
            }
        ]
    },
    {
        "id": 7,
        "title": "Triangle Midpoint Theorem",
        "subtitle": "Section 12.3.1 Theorem 6 (Midpoint Theorem): Segment Joining Midpoints is Parallel & Half the Base",
        "speech": (
            "Now unlock one of the crown-jewel theorems of triangle geometry inside Section Twelve Point Three Point One: THEOREM SIX, THE MIDPOINT THEOREM! "
            "Take ANY triangle ABC! Let D be the exact midpoint of side AB, and let E be the exact midpoint of side AC! Connect D to E! Theorem Six proves TWO astonishing facts simultaneously: FIRST, segment DE is strictly PARALLEL to the third side BC; SECOND, length DE equals EXACTLY ONE-HALF of BC! "
            "Watch how Theorem Five (our parallelogram test!) proves this in four crystal-clear lines! Extend segment DE rightward past E to point F so that EF equals DE, and connect C to F! Now compare triangles ADE and CFE: AE equals CE (E is midpoint), vertically opposite angles AED and CEF are equal, and DE equals FE (by construction)! By SAS CONGRUENCE, triangle ADE is congruent to triangle CFE! "
            "Therefore CF equals AD equals BD, AND equal alternate interior angles prove CF is parallel to AB (hence CF is parallel to BD)! By Theorem Five, BCFD IS A PARALLELOGRAM! Thus DF is parallel to BC and DF equals BC—making DE parallel to BC and DE equals half BC in every single triangle!"
        ),
        "checkpoints": [
            {
                "question": "In △ABC, D and E are midpoints of AB and AC respectively. If BC = 18 cm, what is the length of DE and its relationship to BC?",
                "options": [
                    "DE = 9 cm (half of BC) and DE ∥ BC",
                    "DE = 18 cm and DE ⊥ BC",
                    "DE = 6 cm and DE ∥ BC",
                    "DE = 12 cm"
                ],
                "answer": 0,
                "hint": "Apply the Midpoint Theorem: DE = ½ BC and DE ∥ BC!",
                "explanation": "By Theorem 6, DE is parallel to BC and half its length: ½ × 18 = 9 cm."
            },
            {
                "question": "In the proof of the Midpoint Theorem (extending DE to F with EF = DE), why is BCFD proven to be a parallelogram?",
                "options": [
                    "SAS congruence △ADE ≅ △CFE gives CF = AD = BD and CF ∥ BD, so BCFD is a parallelogram by Theorem 5",
                    "Because all angles of BCFD are 90°",
                    "Because BF = CD",
                    "Because D and E are on BC"
                ],
                "answer": 0,
                "hint": "One pair of opposite sides (BD and CF) is shown to be BOTH equal and parallel!",
                "explanation": "△ADE ≅ △CFE (SAS) yields CF = AD = BD and equal alternate interior angles CF ∥ BD, triggering Theorem 5."
            }
        ]
    },
    {
        "id": 8,
        "title": "Converse Midpoint Theorem",
        "subtitle": "Section 12.3.1 Theorem 7: Line Through One Midpoint Parallel to Base Bisects Third Side",
        "speech": (
            "Now inspect the natural partner of Theorem Six inside Section Twelve Point Three Point One: THEOREM SEVEN, THE CONVERSE OF THE MIDPOINT THEOREM! "
            "Suppose in triangle ABC, you start at D—the midpoint of side AB—and draw a line passing through D that is PARALLEL to base BC, meeting side AC at some point E! Must E automatically be the exact midpoint of AC? "
            "YES! Let us prove Theorem Seven cleanly! Draw an auxiliary line through vertex C parallel to side AB, meeting ray DE extended at point F! Look at quadrilateral BCFD! First, DF is parallel to BC (given); second, CF is parallel to BD (by construction)! With both pairs of opposite sides parallel, BCFD IS A PARALLELOGRAM! "
            "Because opposite sides of a parallelogram are equal, CF equals BD—and since D is the midpoint of AB, BD equals AD, so CF equals AD! Now compare triangles ADE and CFE: CF equals AD, and parallel lines AB and CF give TWO pairs of equal alternate interior angles! By AAS (or ASA) CONGRUENCE, triangle ADE is congruent to triangle CFE—forcing AE equals CE! Thus point E is guaranteed to bisect side AC every single time without exception!"
        ),
        "checkpoints": [
            {
                "question": "In △ABC, D is the midpoint of AB and line l through D is drawn parallel to BC, meeting AC at E. If AC = 15 cm, what is AE?",
                "options": ["7.5 cm (since Theorem 7 proves E is the midpoint of AC)", "5 cm", "10 cm", "15 cm"],
                "answer": 0,
                "hint": "Theorem 7 guarantees that a line through one midpoint parallel to the base bisects the third side!",
                "explanation": "By the Converse of the Midpoint Theorem, AE = EC = 15/2 = 7.5 cm."
            },
            {
                "question": "How is the Converse of the Midpoint Theorem (Theorem 7) used to TRISECT a line segment AB using parallel lines?",
                "options": [
                    "Draw a ray from A with 3 equal compass marks P₁, P₂, P₃, connect P₃ to B, and draw parallels through P₁, P₂ to cut AB into 3 equal parts",
                    "Fold the segment in half once",
                    "Draw perpendiculars from the midpoint only",
                    "Use a 60° protractor"
                ],
                "answer": 0,
                "hint": "Equal intercepts on one transversal produce equal intercepts on any other transversal between parallel lines!",
                "explanation": "Repeatedly applying Theorem 7 (the Intercept Theorem) transfers equal segments from the auxiliary ray onto AB."
            }
        ]
    }
]
