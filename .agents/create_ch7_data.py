import json

slides = [
    # Slide 1: 7.0 The Anatomy of a Triangle
    {
        "id": "slide-1",
        "slide_num": 1,
        "section": "7.0",
        "title": "A Tale of Three Intersecting Lines: The Anatomy of a Triangle",
        "badge": "Foundations of Geometry",
        "narration": "Welcome, young mathematicians! I am Acharya Baudhāyana. When three straight lines lie in a plane and intersect each other at three distinct points, they enclose a sacred and fundamental geometric form: the triangle. Let us explore its vertices, sides, and interior angles.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>What Happens When Three Lines Intersect?</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    Consider three straight lines drawn on a flat sheet of paper. If no two lines are parallel and all three do not pass through a single common point (non-concurrent), they must cross each other at <strong>three distinct intersection points</strong>.
                </p>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <span class='text-amber-300 font-bold text-sm block mb-1'>1. Three Vertices</span>
                        <p class='text-xs text-slate-300'>The three distinct points where pairs of lines intersect: points $A$, $B$, and $C$.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>
                        <span class='text-cyan-300 font-bold text-sm block mb-1'>2. Three Sides</span>
                        <p class='text-xs text-slate-300'>The line segments joining adjacent vertices: segments $AB$, $BC$, and $CA$ (or lengths $c, a, b$).</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <span class='text-emerald-300 font-bold text-sm block mb-1'>3. Three Interior Angles</span>
                        <p class='text-xs text-slate-300'>The angles formed inside the enclosed boundary at each vertex: $\\angle A$, $\\angle B$, and $\\angle C$.</p>
                    </div>
                </div>
                <p class='text-slate-400 text-xs italic mt-2'>
                    💡 Key Notation: Side $a$ is opposite vertex $A$, side $b$ is opposite vertex $B$, and side $c$ is opposite vertex $C$. A triangle with vertices $A, B, C$ is denoted as $\\Delta ABC$.
                </p>
            </div>
        """,
        "sim_id": "sim-triangle-anatomy",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "What geometric figure is enclosed when three coplanar lines intersect at three distinct points?",
                "options": ["A rectangle", "A triangle", "A straight line", "A circle"],
                "correct": 1,
                "explanation": "Three non-parallel, non-concurrent lines intersecting at three distinct points enclose a three-sided polygon called a triangle."
            },
            {
                "id": "cp1_2",
                "question": "In triangle $ABC$, which side lies directly opposite to vertex $B$?",
                "options": ["Side $AB$", "Side $BC$", "Side $AC$ (or $b$)", "Side $B$"],
                "correct": 2,
                "explanation": "In standard mathematical notation, side $AC$ (often labeled lowercase $b$) lies directly opposite to vertex $B$."
            }
        ]
    },

    # Slide 2: 7.1 Equilateral Triangles
    {
        "id": "slide-2",
        "slide_num": 2,
        "section": "7.1",
        "title": "Equilateral Triangles: The Pinnacle of Symmetry",
        "badge": "Perfect Symmetry",
        "narration": "An equilateral triangle is nature's most balanced polygon! All three of its sides are equal in length, and all three of its angles measure exactly sixty degrees. Trying to find the third vertex with a ruler alone is clumsy, but with compass arcs, the intersection is instantaneous and exact.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Properties & Elegant Construction of Equilateral Triangles</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    An <strong>equilateral triangle</strong> has three sides of equal length: $AB = BC = CA = s$. Because of total rotational and reflectional symmetry:
                </p>
                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <h5 class='text-amber-300 font-bold text-xs uppercase mb-1'>Equiangular Property</h5>
                        <p class='text-xs text-slate-300'>All three interior angles are equal: $\\angle A = \\angle B = \\angle C = 60^\\circ$. The total sum is $60^\\circ + 60^\\circ + 60^\\circ = 180^\\circ$.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>
                        <h5 class='text-cyan-300 font-bold text-xs uppercase mb-1'>Why Compasses Triumph Over Rulers</h5>
                        <p class='text-xs text-slate-300'>Measuring side lengths with a ruler to pinpoint vertex $C$ involves trial-and-error. But a compass preserves distance invariant: sweeping arcs from $A$ and $B$ of radius $s$ guarantees vertex $C$ in one step!</p>
                    </div>
                </div>
                <div class='p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl text-xs text-amber-200'>
                    <strong>Compass Construction Algorithm:</strong><br>
                    1. Draw base segment $AB = s$.<br>
                    2. Open compass to exact width $AB$. Centered at $A$, swing an arc above $AB$.<br>
                    3. Keeping the same radius, centered at $B$, swing a second arc intersecting the first at point $C$.<br>
                    4. Draw segments $AC$ and $BC$. Triangle $ABC$ is guaranteed equilateral!
                </div>
            </div>
        """,
        "sim_id": "sim-equilateral-compass",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "What is the measure of each interior angle in an equilateral triangle?",
                "options": ["45°", "90°", "60°", "120°"],
                "correct": 2,
                "explanation": "Since all three sides are equal, all three angles are equal. Since the angle sum is 180°, each angle is 180° / 3 = 60°."
            },
            {
                "id": "cp2_2",
                "question": "When constructing an equilateral triangle of side 5 cm, what radius must the compass maintain when swinging arcs from both endpoints?",
                "options": ["2.5 cm", "5 cm", "10 cm", "Any random radius"],
                "correct": 1,
                "explanation": "To make all three sides equal to 5 cm, both arcs must be drawn with a radius equal to the base length of 5 cm."
            }
        ]
    },

    # Slide 3: 7.2 The Triangle Inequality
    {
        "id": "slide-3",
        "slide_num": 3,
        "section": "7.2",
        "title": "The Triangle Inequality: The Universal Law of Existence",
        "badge": "Existence Theorem",
        "narration": "Can any three random stick lengths form a triangle? Nay! If two sticks are too short, their ends can never reach across the third side to meet. This eternal geometric truth is known as the Triangle Inequality Theorem.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Triangle Inequality Theorem</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    A triangle can exist if and only if the sum of the lengths of any two sides is <strong>strictly greater</strong> than the length of the third side.
                </p>
                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>
                    <span class='text-amber-300 font-bold text-base tracking-wide font-mono'>
                        a + b > c &nbsp;&nbsp;|&nbsp;&nbsp; b + c > a &nbsp;&nbsp;|&nbsp;&nbsp; c + a > b
                    </span>
                </div>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-xl'>
                        <span class='text-emerald-400 font-bold block mb-1'>Case 1: $a + b > c$ (Triangle Exists)</span>
                        <p class='text-slate-300'>The two sides have enough combined span to hinge upwards and meet at an apex above base $c$.</p>
                    </div>
                    <div class='p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl'>
                        <span class='text-amber-400 font-bold block mb-1'>Case 2: $a + b = c$ (Flat Line Collapse)</span>
                        <p class='text-slate-300'>The sticks meet only when lying completely flat on base $c$. The apex collapses onto the line (zero area).</p>
                    </div>
                    <div class='p-3 bg-rose-950/40 border border-rose-500/30 rounded-xl'>
                        <span class='text-rose-400 font-bold block mb-1'>Case 3: $a + b < c$ (Impossible Gap)</span>
                        <p class='text-slate-300'>The two sticks cannot reach each other; an impassable gap remains, making a triangle impossible!</p>
                    </div>
                </div>
                <p class='text-cyan-300 text-xs mt-2'>
                    💡 Quick Test Shortcut: To test whether three lengths form a triangle, simply check if the sum of the <strong>two smaller sides</strong> is greater than the <strong>largest side</strong>.
                </p>
            </div>
        """,
        "sim_id": "sim-triangle-inequality",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "Can sticks of lengths 3 cm, 4 cm, and 8 cm form a triangle?",
                "options": ["Yes, always", "No, because 3 + 4 = 7, which is less than 8", "Yes, if angles are acute", "Only in 3D space"],
                "correct": 1,
                "explanation": "Here, the sum of the two shorter sides is 3 + 4 = 7 cm, which is less than the third side of 8 cm. Hence, they cannot meet to form a triangle."
            },
            {
                "id": "cp3_2",
                "question": "What happens when three side lengths satisfy $a + b = c$?",
                "options": ["An equilateral triangle forms", "An obtuse triangle forms", "The vertices collapse onto a straight line segment", "An impossible curved triangle forms"],
                "correct": 2,
                "explanation": "When a + b = c, the two arms lie completely flat along the third segment, forming a degenerate straight line with zero height and zero area."
            }
        ]
    },

    # Slide 4: 7.2 Circle Intersections
    {
        "id": "slide-4",
        "slide_num": 4,
        "section": "7.2",
        "title": "Circle Intersections: The Geometric Reality of Triangle Existence",
        "badge": "Locus & Arcs",
        "narration": "When constructing a triangle with side lengths a, b, and c, we draw two circles centered at the endpoints of base c. Whether those circles intersect, touch, or miss each other entirely determines whether our triangle can physically exist!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Why Circle Arcs Reveal Triangle Existence</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    Let base $AB = c$. The locus of all points at distance $b$ from $A$ is a circle $C_A$ of radius $b$. The locus of all points at distance $a$ from $B$ is a circle $C_B$ of radius $a$. Any third vertex $C$ must lie on <strong>both</strong> circles!
                </p>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-rose-950/30 border border-rose-500/30 rounded-xl'>
                        <span class='text-rose-400 font-bold block mb-1'>1. Non-Intersecting ($a + b < c$)</span>
                        <p class='text-slate-300'>The centers are too far apart. The circles never touch. <strong>0 intersection points</strong> = No triangle possible.</p>
                    </div>
                    <div class='p-3 bg-amber-950/30 border border-amber-500/30 rounded-xl'>
                        <span class='text-amber-400 font-bold block mb-1'>2. Tangent Externally ($a + b = c$)</span>
                        <p class='text-slate-300'>The circles touch at exactly <strong>1 point</strong> lying on line $AB$. Degenerate flat line segment.</p>
                    </div>
                    <div class='p-3 bg-emerald-950/30 border border-emerald-500/30 rounded-xl'>
                        <span class='text-emerald-400 font-bold block mb-1'>3. Two Intersections ($|a - b| < c < a + b$)</span>
                        <p class='text-slate-300'>The circles intersect at <strong>2 distinct points</strong>: one above base $AB$, and one below (mirror reflection).</p>
                    </div>
                </div>
                <p class='text-slate-400 text-xs italic mt-2'>
                    💡 Mirror Congruence: The two intersection points $C_1$ (above) and $C_2$ (below) create two congruent triangles $\\Delta ABC_1 \\cong \\Delta ABC_2$ mirrored across line $AB$.
                </p>
            </div>
        """,
        "sim_id": "sim-circle-intersections",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "How many distinct triangle apex points exist when two compass circles intersect normally?",
                "options": ["1 point", "2 points (one above and one below the base)", "3 points", "Infinitely many points"],
                "correct": 1,
                "explanation": "Two circles centered at points A and B intersect at two points: one above line AB and one below line AB, giving two congruent triangles."
            },
            {
                "id": "cp4_2",
                "question": "If center distance $AB = 10\\text{ cm}$, and circle radii are $r_1 = 4\\text{ cm}$ and $r_2 = 5\\text{ cm}$, do the circles intersect?",
                "options": ["Yes, at two points", "Yes, at one point", "No, because 4 + 5 = 9 < 10 (circles do not touch)", "They overlap entirely"],
                "correct": 2,
                "explanation": "Because r1 + r2 = 4 + 5 = 9 cm is less than the distance between centers (10 cm), the circles cannot reach each other and do not intersect."
            }
        ]
    },

    # Slide 5: 7.2 Constructing SSS Triangles
    {
        "id": "slide-5",
        "slide_num": 5,
        "section": "7.2",
        "title": "Constructing SSS Triangles: Scalene & Isosceles",
        "badge": "Drafting Mastery",
        "narration": "Now let us master the art of drafting any triangle when all three sides are known—the Side-Side-Side construction! Whether the sides are all unequal as in a scalene triangle, or two are equal as in an isosceles triangle, our compass guides us flawlessly.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Step-by-Step SSS Construction Protocol</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    To construct $\\Delta ABC$ given side lengths $a, b, c$:
                </p>
                <div class='space-y-2 text-xs'>
                    <div class='flex items-start gap-2 p-2 bg-slate-800/60 rounded-lg'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>1</span>
                        <p class='text-slate-300'><strong>Draw the Base:</strong> Use a ruler to draw line segment $AB$ of length $c$.</p>
                    </div>
                    <div class='flex items-start gap-2 p-2 bg-slate-800/60 rounded-lg'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>2</span>
                        <p class='text-slate-300'><strong>First Arc from $A$:</strong> Open your compass to length $b$ (side $AC$). Place the metal point at $A$ and swing a broad arc above the base.</p>
                    </div>
                    <div class='flex items-start gap-2 p-2 bg-slate-800/60 rounded-lg'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>3</span>
                        <p class='text-slate-300'><strong>Second Arc from $B$:</strong> Open your compass to length $a$ (side $BC$). Place the metal point at $B$ and swing an arc intersecting the first arc at point $C$.</p>
                    </div>
                    <div class='flex items-start gap-2 p-2 bg-slate-800/60 rounded-lg'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>4</span>
                        <p class='text-slate-300'><strong>Complete the Polygon:</strong> Join vertex $C$ to $A$ and to $B$ with straight line segments.</p>
                    </div>
                </div>
                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs'>
                    <div class='p-2 bg-slate-800/80 rounded border border-cyan-500/30'>
                        <span class='text-cyan-300 font-bold block'>Scalene Triangles:</span> All three sides distinct ($a \\ne b \\ne c$).
                    </div>
                    <div class='p-2 bg-slate-800/80 rounded border border-emerald-500/30'>
                        <span class='text-emerald-300 font-bold block'>Isosceles Triangles:</span> Two sides equal ($a = b \\ne c$). Base angles are equal!
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-sss-construction",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "What is the primary tool used to transfer exact side lengths when constructing an SSS triangle?",
                "options": ["A protractor", "A compass", "A set square", "A magnifying glass"],
                "correct": 1,
                "explanation": "A pair of compasses is used to measure and transfer exact lengths from a ruler to swing circular arcs."
            },
            {
                "id": "cp5_2",
                "question": "In an isosceles triangle with sides 6 cm, 6 cm, and 4 cm, what is true about its base angles?",
                "options": ["They must be 90°", "They are unequal", "The angles opposite the equal sides are equal", "All three angles are 60°"],
                "correct": 2,
                "explanation": "In any isosceles triangle, the angles opposite to the two equal sides are always equal in measure."
            }
        ]
    },

    # Slide 6: 7.3 SAS Triangle Construction
    {
        "id": "slide-6",
        "slide_num": 6,
        "section": "7.3",
        "title": "Two Sides and the Included Angle: SAS Construction",
        "badge": "Angular Locking",
        "narration": "What if we do not know all three sides, but know two sides and the angle pinned firmly between them? This is the Side-Angle-Side criterion. The included angle locks the opening like a pair of compass arms, uniquely determining the third side!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Power of the Included Angle (SAS)</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    The term <strong>included angle</strong> means the angle formed directly between the two known sides. For sides $AB$ and $AC$, the included angle is $\\angle A$.
                </p>
                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <span class='text-amber-300 font-bold text-sm block mb-1'>Why SAS Uniquely Fixes the Triangle</span>
                        <p class='text-slate-300'>Once you fix side $c$ along base $AB$ and open ray $AX$ at fixed angle $\\angle A$, vertex $C$ is locked at distance $b$ along that ray. The distance between endpoints $B$ and $C$ is mathematically frozen!</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>
                        <span class='text-rose-300 font-bold text-sm block mb-1'>The Non-Included Angle Trap (SSA)</span>
                        <p class='text-slate-300'>If the angle is NOT included between the two sides, the swinging arm can often hit the base line at <strong>two different points</strong> (the ambiguous case). SAS avoids this ambiguity completely!</p>
                    </div>
                </div>
                <div class='p-3 bg-slate-900 border border-cyan-500/30 rounded-xl text-xs text-cyan-200'>
                    <strong>Construction Sequence:</strong> 1. Draw base $AB = c$. &rarr; 2. Use a protractor to construct ray $AX$ at angle $\\angle A$. &rarr; 3. Use compass to cut off length $b$ along ray $AX$ to locate $C$. &rarr; 4. Join $B$ to $C$.
                </div>
            </div>
        """,
        "sim_id": "sim-sas-construction",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "Which angle is the 'included angle' between sides $PQ$ and $QR$ in triangle $PQR$?",
                "options": ["$\\angle P$", "$\\angle Q$", "$\\angle R$", "$\\angle S$"],
                "correct": 1,
                "explanation": "The letter common to both segments PQ and QR is Q, so the included angle between them is angle Q."
            },
            {
                "id": "cp6_2",
                "question": "Why does SAS guarantee a single unique triangle?",
                "options": ["Because all three angles are given", "Because the angle fixes the direction and the two side lengths freeze all three vertices", "Because all triangles are equilateral", "Because the third side is always 10 cm"],
                "correct": 1,
                "explanation": "Fixing two side lengths and the angle between them fixes the exact positions of all three vertices in the plane."
            }
        ]
    },

    # Slide 7: 7.3 ASA Triangle Construction
    {
        "id": "slide-7",
        "slide_num": 7,
        "section": "7.3",
        "title": "Two Angles and the Included Side: ASA Construction",
        "badge": "Ray Convergence",
        "narration": "In the Angle-Side-Angle construction, we lay down a known base segment and shoot two rays inward from both endpoints. As long as the two base angles sum to less than one hundred and eighty degrees, the rays must converge and meet at the third vertex!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>ASA Construction & The Ray Convergence Law</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    Given base side $BC = a$ and base angles $\\angle B$ and $\\angle C$, we erect rays $BX$ and $CY$ pointing inward towards each other.
                </p>
                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>
                    <span class='text-amber-300 font-bold text-sm font-mono'>
                        Fundamental Existence Condition: &nbsp;&nbsp; $\\angle B + \\angle C < 180^\\circ$
                    </span>
                </div>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-xl'>
                        <span class='text-emerald-400 font-bold block mb-1'>$\\angle B + \\angle C < 180^\\circ$</span>
                        <p class='text-slate-300'>The interior rays tilt towards each other and intersect at a unique vertex $A$. Triangle exists!</p>
                    </div>
                    <div class='p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl'>
                        <span class='text-amber-400 font-bold block mb-1'>$\\angle B + \\angle C = 180^\\circ$</span>
                        <p class='text-slate-300'>The rays are parallel! They extend forever without meeting. No triangle can form.</p>
                    </div>
                    <div class='p-3 bg-rose-950/40 border border-rose-500/30 rounded-xl'>
                        <span class='text-rose-400 font-bold block mb-1'>$\\angle B + \\angle C > 180^\\circ$</span>
                        <p class='text-slate-300'>The rays diverge away from each other on this side of the base. Intersection is impossible.</p>
                    </div>
                </div>
                <p class='text-slate-400 text-xs italic mt-2'>
                    💡 Calculating the Third Angle: Once $\\angle B$ and $\\angle C$ are given, the third angle is automatically fixed as $\\angle A = 180^\\circ - (\\angle B + \\angle C)$.
                </p>
            </div>
        """,
        "sim_id": "sim-asa-construction",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "Can a triangle be constructed with base angles measuring 110° and 80°?",
                "options": ["Yes, using a long base", "No, because 110° + 80° = 190° > 180° (rays diverge)", "Yes, if sides are equal", "Only if it is a right triangle"],
                "correct": 1,
                "explanation": "The sum of the two angles is 190°, which exceeds 180°. Interior rays will diverge and can never intersect."
            },
            {
                "id": "cp7_2",
                "question": "If base $BC = 6\\text{ cm}$, $\\angle B = 70^\\circ$, and $\\angle C = 50^\\circ$, what is the measure of angle $A$?",
                "options": ["60°", "120°", "50°", "70°"],
                "correct": 0,
                "explanation": "By the Angle Sum Property, angle A = 180° - (70° + 50°) = 180° - 120° = 60°."
            }
        ]
    },

    # Slide 8: 7.3 Angle Sum Property
    {
        "id": "slide-8",
        "slide_num": 8,
        "section": "7.3",
        "title": "The Angle Sum Property: The Sacred 180° Theorem",
        "badge": "Universal Law",
        "narration": "In every triangle in the Euclidean plane, whether skinny, wide, small as an atom, or vast as the cosmos, the sum of all three interior angles is always exactly one hundred and eighty degrees! Let us prove this using our trusted tool: parallel lines.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Deductive Proof of the Angle Sum Property</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    Let $\\Delta ABC$ have interior angles $\\angle 1, \\angle 2, \\angle 3$ (where $\\angle 1 = \\angle A, \\angle 2 = \\angle B, \\angle 3 = \\angle C$).
                </p>
                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl space-y-2 text-xs text-slate-300 my-3'>
                    <p><strong>Step 1 (Auxiliary Line):</strong> Through vertex $A$, draw a straight line $XY$ parallel to base $BC$ ($XY \\parallel BC$).</p>
                    <p><strong>Step 2 (Alternate Interior Angles):</strong><br>
                    • Line segment $AB$ acts as a transversal across $XY \\parallel BC$, so $\\angle XAB = \\angle B = \\angle 2$.<br>
                    • Line segment $AC$ acts as a transversal across $XY \\parallel BC$, so $\\angle YAC = \\angle C = \\angle 3$.</p>
                    <p><strong>Step 3 (Angles on a Straight Line):</strong> Points $X, A, Y$ lie on a straight line, so their angles form a straight angle:<br>
                    $$\\angle XAB + \\angle 1 + \\angle YAC = 180^\\circ$$</p>
                    <p><strong>Conclusion:</strong> Substituting the alternate angles gives:<br>
                    $$\\mathbf{\\angle 2 + \\angle 1 + \\angle 3 = 180^\\circ} \\iff \\mathbf{\\angle A + \\angle B + \\angle C = 180^\\circ}$$</p>
                </div>
                <p class='text-cyan-300 text-xs'>
                    💡 Hands-on Paper Tearing Activity: Cut out any triangle from paper, tear off its three corners, and arrange them with vertices touching. They will form a flawless straight line ($180^\\circ$)!
                </p>
            </div>
        """,
        "sim_id": "sim-angle-sum-proof",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "What auxiliary line is constructed to prove that the interior angles of a triangle sum to 180°?",
                "options": ["A perpendicular bisector to the base", "A line through one vertex parallel to the opposite side", "A circle around the triangle", "A line bisecting angle A"],
                "correct": 1,
                "explanation": "Drawing a line through a vertex parallel to the opposite side creates alternate interior angles that lie along a straight line summing to 180°."
            },
            {
                "id": "cp8_2",
                "question": "Can a triangle have two right angles (90° each)?",
                "options": ["Yes, in isosceles triangles", "No, because two 90° angles already sum to 180°, leaving 0° for the third angle", "Yes, if one side is zero", "Only if it is scalene"],
                "correct": 1,
                "explanation": "If two angles were 90°, their sum would be 180°, leaving 0° for the third angle. The lines would be parallel and never close to form a triangle."
            }
        ]
    },

    # Slide 9: 7.3 Exterior Angle Theorem
    {
        "id": "slide-9",
        "slide_num": 9,
        "section": "7.3",
        "title": "The Exterior Angle Theorem: The Window to Outer Angles",
        "badge": "Angle Relationships",
        "narration": "Extend any side of a triangle outwards, and you create an exterior angle. This exterior angle holds an astonishing secret: its measure is always exactly equal to the sum of the two interior opposite angles!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Exterior Angle Theorem</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    When side $BC$ of $\\Delta ABC$ is extended past $C$ to point $D$, $\\angle ACD$ is called an <strong>exterior angle</strong>. The angles $\\angle A$ and $\\angle B$ are its <strong>interior opposite angles</strong>.
                </p>
                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>
                    <span class='text-amber-300 font-bold text-base tracking-wide font-mono'>
                        \\text{Exterior Angle } \\angle ACD = \\angle A + \\angle B
                    </span>
                </div>
                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>
                        <h5 class='text-cyan-300 font-bold uppercase mb-1'>Quick Deductive Proof</h5>
                        <p class='text-slate-300'>
                            1. In $\\Delta ABC$: $\\angle A + \\angle B + \\angle BCA = 180^\\circ$.<br>
                            2. Along line $BCD$: $\\angle ACD + \\angle BCA = 180^\\circ$ (Linear pair).<br>
                            3. Equating both: $\\angle ACD + \\angle BCA = \\angle A + \\angle B + \\angle BCA$.<br>
                            4. Subtract $\\angle BCA$ from both sides: $\\angle ACD = \\angle A + \\angle B$.
                        </p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <h5 class='text-emerald-300 font-bold uppercase mb-1'>Important Corollary</h5>
                        <p class='text-slate-300'>
                            An exterior angle is always <strong>strictly greater</strong> than either of its interior opposite angles: $\\angle ACD > \\angle A$ and $\\angle ACD > \\angle B$.
                        </p>
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-exterior-angle",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "If the exterior angle at vertex $C$ is 125°, and interior opposite angle $A$ is 65°, what is angle $B$?",
                "options": ["60°", "70°", "125°", "55°"],
                "correct": 0,
                "explanation": "By the Exterior Angle Theorem: Ext Angle = Angle A + Angle B. Therefore, 125° = 65° + Angle B, giving Angle B = 125° - 65° = 60°."
            },
            {
                "id": "cp9_2",
                "question": "Is an exterior angle of a triangle ever smaller than either of its interior opposite angles?",
                "options": ["Yes, in acute triangles", "No, it is always strictly greater than each interior opposite angle", "Yes, in obtuse triangles", "Only in right-angled triangles"],
                "correct": 1,
                "explanation": "Because Ext Angle = Angle A + Angle B, and angles of a triangle are positive, Ext Angle must be strictly greater than both Angle A and Angle B."
            }
        ]
    },

    # Slide 10: 7.4 Altitudes of a Triangle
    {
        "id": "slide-10",
        "slide_num": 10,
        "section": "7.4",
        "title": "Altitudes of a Triangle: The Perpendicular Heights",
        "badge": "Geometric Altitudes",
        "narration": "What is the true height of a triangle? It is not the sloped side! The altitude is the perpendicular line segment dropped from a vertex straight down to the opposite side or its extension.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Defining the Altitude of a Triangle</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    An <strong>altitude</strong> of a triangle is the line segment from a vertex drawn perpendicular ($90^\\circ$) to the opposite side (known as the base). The point where it meets the opposite side is called the <strong>foot of the perpendicular</strong>.
                </p>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <span class='text-amber-300 font-bold block mb-1'>Every Triangle Has 3 Altitudes</span>
                        <p class='text-slate-300'>From vertex $A$ to side $BC$, from vertex $B$ to side $CA$, and from vertex $C$ to side $AB$.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>
                        <span class='text-cyan-300 font-bold block mb-1'>Area of a Triangle Connection</span>
                        <p class='text-slate-300'>$$\\text{Area} = \\frac{1}{2} \\times \\text{Base} \\times \\text{Altitude}$$ Choosing any side as base paired with its altitude gives the exact same area!</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <span class='text-emerald-300 font-bold block mb-1'>Altitude vs Median</span>
                        <p class='text-slate-300'>An altitude meets the base at $90^\\circ$. A median connects the vertex to the <em>midpoint</em> of the base (they only coincide in symmetric triangles!).</p>
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-altitude-definition",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "What angle does an altitude make with the side on which it lands?",
                "options": ["45°", "60°", "90°", "180°"],
                "correct": 2,
                "explanation": "By definition, an altitude is a perpendicular line segment dropped from a vertex, so it meets the base at a right angle of 90°."
            },
            {
                "id": "cp10_2",
                "question": "How many altitudes does every triangle possess?",
                "options": ["Only 1", "2", "Exactly 3 (one from each vertex)", "Infinitely many"],
                "correct": 2,
                "explanation": "Every triangle has three vertices, and from each vertex exactly one perpendicular altitude can be drawn to the opposite side."
            }
        ]
    },

    # Slide 11: 7.4 Drafting Altitudes with Ruler and Set Square
    {
        "id": "slide-11",
        "slide_num": 11,
        "section": "7.4",
        "title": "Drafting Altitudes: The Ruler & Set Square Technique",
        "badge": "Precision Craft",
        "narration": "In ancient times, we used cords and pegs. Today, master draftsmen use the brilliant combination of a straightedge ruler and a right-angled set square to slide down the true perpendicular effortlessly!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>How to Draw an Altitude Using a Set Square</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    To draw the altitude from vertex $A$ to base $BC$:
                </p>
                <div class='space-y-2 text-xs'>
                    <div class='p-2 bg-slate-800/70 rounded-lg flex items-start gap-2'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>1</span>
                        <p class='text-slate-300'><strong>Align the Ruler:</strong> Place a straight ruler firmly along base side $BC$ (or line containing $BC$).</p>
                    </div>
                    <div class='p-2 bg-slate-800/70 rounded-lg flex items-start gap-2'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>2</span>
                        <p class='text-slate-300'><strong>Slide the Set Square:</strong> Place one leg of the right-angled set square against the ruler. Slide it along the ruler.</p>
                    </div>
                    <div class='p-2 bg-slate-800/70 rounded-lg flex items-start gap-2'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>3</span>
                        <p class='text-slate-300'><strong>Stop at Vertex $A$:</strong> Stop sliding when the perpendicular upright edge of the set square directly touches vertex $A$.</p>
                    </div>
                    <div class='p-2 bg-slate-800/70 rounded-lg flex items-start gap-2'>
                        <span class='w-5 h-5 flex items-center justify-center rounded-full bg-amber-500/20 text-amber-300 font-bold shrink-0'>4</span>
                        <p class='text-slate-300'><strong>Draw the Altitude:</strong> Draw a straight segment from vertex $A$ down to line $BC$. Mark the $90^\\circ$ corner symbol!</p>
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-set-square-drafting",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "Why is a set square especially suitable for drawing altitudes?",
                "options": ["It has curved edges", "It has a fixed 90° right angle built into its corners", "It measures weight", "It has zero degrees"],
                "correct": 1,
                "explanation": "A set square features an exact factory-machined 90° right angle, guaranteeing true perpendicular lines when guided by a straight ruler."
            },
            {
                "id": "cp11_2",
                "question": "What role does the ruler play during set-square altitude construction?",
                "options": ["It acts as a straight track guiding the base of the set square along the triangle side", "It measures the angle of the apex", "It draws arcs", "It holds the pencil"],
                "correct": 0,
                "explanation": "The ruler is held stationary against the base side to serve as a linear track for the set square to slide without tilting."
            }
        ]
    },

    # Slide 12: 7.4 Altitudes in Special Triangles
    {
        "id": "slide-12",
        "slide_num": 12,
        "section": "7.4",
        "title": "Altitudes in Special Triangles: Inside, On, and Outside!",
        "badge": "Spatial Variations",
        "narration": "Did you assume altitudes always lie neatly inside the triangle? Prepare for a revelation! In right-angled triangles, the altitudes double as the sides themselves. And in obtuse triangles, altitudes plunge outside into the empty plane!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Three Surprising Behaviors of Altitudes</h4>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <span class='text-emerald-300 font-bold block mb-1 text-sm'>1. Acute Triangles</span>
                        <p class='text-slate-300 mb-2'>All three interior angles are acute ($< 90^\\circ$).</p>
                        <div class='p-2 bg-emerald-950/40 rounded text-emerald-200'>
                            <strong>All 3 altitudes lie entirely INSIDE</strong> the interior of the triangle.
                        </div>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <span class='text-amber-300 font-bold block mb-1 text-sm'>2. Right Triangles</span>
                        <p class='text-slate-300 mb-2'>One angle is exactly $90^\\circ$ at vertex $B$.</p>
                        <div class='p-2 bg-amber-950/40 rounded text-amber-200'>
                            <strong>Two altitudes lie ON the sides!</strong> Side $AB$ is the altitude to $BC$, and side $BC$ is the altitude to $AB$. Only the altitude to hypotenuse is inside.
                        </div>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>
                        <span class='text-rose-300 font-bold block mb-1 text-sm'>3. Obtuse Triangles</span>
                        <p class='text-slate-300 mb-2'>One angle is obtuse ($> 90^\\circ$) at vertex $B$.</p>
                        <div class='p-2 bg-rose-950/40 rounded text-rose-200'>
                            <strong>Two altitudes fall OUTSIDE</strong> the triangle! You must extend side $BC$ and side $AB$ backwards to drop the perpendiculars.
                        </div>
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-altitude-cases",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "In a right-angled triangle, where are two of its three altitudes located?",
                "options": ["Outside the triangle", "They coincide with the two perpendicular sides of the triangle", "At the midpoint of the hypotenuse", "They do not exist"],
                "correct": 1,
                "explanation": "Since the two legs meet at 90°, each leg serves as the altitude dropped to the other leg."
            },
            {
                "id": "cp12_2",
                "question": "In an obtuse-angled triangle, where do the two altitudes from the acute vertices land?",
                "options": ["Inside the triangle", "Outside the triangle on the extended base lines", "At the center of mass", "On the obtuse angle vertex"],
                "correct": 1,
                "explanation": "Because the obtuse angle leans back past 90°, perpendiculars dropped from the acute vertices land outside the triangle on the extended side lines."
            }
        ]
    },

    # Slide 13: 7.4 The Orthocenter
    {
        "id": "slide-13",
        "slide_num": 13,
        "section": "7.4",
        "title": "The Orthocenter: Where Three Altitudes Meet",
        "badge": "Point of Concurrency",
        "narration": "Here is one of geometry's most breathtaking miracles. Draw all three altitudes of any triangle, extend their lines, and they will ALWAYS meet at one single, shared intersection point: the Orthocenter, symbolized as H!",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Concurrency & The Location of the Orthocenter ($H$)</h4>
                <p class='text-slate-300 text-sm mb-3'>
                    Lines that pass through a single common point are called <strong>concurrent</strong>. The point of concurrency of the three lines containing the altitudes is called the <strong>Orthocenter</strong> ($H$).
                </p>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <span class='text-emerald-300 font-bold block mb-1'>Acute Triangle</span>
                        <p class='text-slate-300'>The Orthocenter $H$ lies <strong>strictly inside</strong> the triangle interior.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <span class='text-amber-300 font-bold block mb-1'>Right Triangle</span>
                        <p class='text-slate-300'>The Orthocenter $H$ lies <strong>exactly on the right-angled vertex</strong>!</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>
                        <span class='text-rose-300 font-bold block mb-1'>Obtuse Triangle</span>
                        <p class='text-slate-300'>The Orthocenter $H$ lies <strong>completely outside</strong> the triangle, tucked behind the obtuse vertex!</p>
                    </div>
                </div>
                <p class='text-slate-400 text-xs italic mt-2'>
                    💡 Dynamic Observation: As a triangle morphs from acute to right-angled to obtuse, the orthocenter $H$ glides smoothly from inside, touches the vertex, and pops outside into open space!
                </p>
            </div>
        """,
        "sim_id": "sim-orthocenter-concurrency",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "What is the mathematical term for the common intersection point of a triangle's three altitudes?",
                "options": ["Centroid", "Orthocenter ($H$)", "Incenter", "Circumcenter"],
                "correct": 1,
                "explanation": "The point where the three lines containing the altitudes of a triangle concur is called the Orthocenter (denoted by H)."
            },
            {
                "id": "cp13_2",
                "question": "Where does the orthocenter lie in a right-angled triangle?",
                "options": ["Inside the triangle", "At the midpoint of the hypotenuse", "Directly on the vertex containing the 90° right angle", "Outside the triangle"],
                "correct": 2,
                "explanation": "In a right triangle, the two perpendicular legs are themselves altitudes, so their intersection—the right-angled vertex—is the orthocenter."
            }
        ]
    },

    # Slide 14: 7.5 Types of Triangles by Sides
    {
        "id": "slide-14",
        "slide_num": 14,
        "section": "7.5",
        "title": "Classification by Sides: Equilateral, Isosceles, Scalene",
        "badge": "Taxonomy of Sides",
        "narration": "To classify triangles with precision, we first measure their side lengths. This gives us three classic families: Equilateral with three equal sides, Isosceles with two equal sides, and Scalene where no two sides match.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Side-Based Taxonomy & Symmetry Properties</h4>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>
                        <h5 class='text-cyan-300 font-bold text-sm mb-1'>1. Equilateral Triangle</h5>
                        <ul class='text-slate-300 space-y-1 list-disc list-inside'>
                            <li>All 3 sides equal ($a = b = c$)</li>
                            <li>All 3 angles equal ($60^\\circ, 60^\\circ, 60^\\circ$)</li>
                            <li><strong>3 lines of symmetry</strong></li>
                            <li>Rotational symmetry of order 3 ($120^\\circ$)</li>
                        </ul>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <h5 class='text-amber-300 font-bold text-sm mb-1'>2. Isosceles Triangle</h5>
                        <ul class='text-slate-300 space-y-1 list-disc list-inside'>
                            <li>At least 2 sides equal ($a = b \\ne c$)</li>
                            <li>Angles opposite equal sides are equal</li>
                            <li><strong>1 line of symmetry</strong> (down middle)</li>
                            <li>Altitude to base bisects base & vertex angle</li>
                        </ul>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>
                        <h5 class='text-rose-300 font-bold text-sm mb-1'>3. Scalene Triangle</h5>
                        <ul class='text-slate-300 space-y-1 list-disc list-inside'>
                            <li>All 3 sides different ($a \\ne b \\ne c$)</li>
                            <li>All 3 angles different ($\\angle A \\ne \\angle B \\ne \\angle C$)</li>
                            <li><strong>0 lines of symmetry</strong></li>
                            <li>Largest angle is opposite longest side!</li>
                        </ul>
                    </div>
                </div>
            </div>
        """,
        "sim_id": "sim-triangle-by-sides",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "How many lines of reflective symmetry does an equilateral triangle have?",
                "options": ["0", "1", "2", "3"],
                "correct": 3,
                "explanation": "An equilateral triangle has 3 lines of symmetry, each passing through one vertex and the midpoint of the opposite side."
            },
            {
                "id": "cp14_2",
                "question": "In a scalene triangle with side lengths 4 cm, 7 cm, and 9 cm, which interior angle is the largest?",
                "options": ["The angle opposite the 4 cm side", "The angle opposite the 7 cm side", "The angle opposite the 9 cm side", "All angles are equal"],
                "correct": 2,
                "explanation": "In any triangle, the largest angle is always positioned directly opposite to the longest side (here, opposite 9 cm)."
            }
        ]
    },

    # Slide 15: 7.5 Types of Triangles by Angles
    {
        "id": "slide-15",
        "slide_num": 15,
        "section": "7.5",
        "title": "Classification by Angles: Acute, Right, and Obtuse",
        "badge": "Taxonomy of Angles",
        "narration": "Next, we classify triangles by their interior angles! Because the angle sum is strictly locked at one hundred and eighty degrees, a triangle can harbor at most one right or obtuse angle.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Angle-Based Taxonomy</h4>
                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>
                        <h5 class='text-emerald-300 font-bold text-sm mb-1'>1. Acute-Angled Triangle</h5>
                        <p class='text-slate-300 mb-1'><strong>All three</strong> interior angles are strictly acute ($< 90^\\circ$).</p>
                        <p class='text-slate-400 italic'>Example: $50^\\circ, 60^\\circ, 70^\\circ$.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>
                        <h5 class='text-amber-300 font-bold text-sm mb-1'>2. Right-Angled Triangle</h5>
                        <p class='text-slate-300 mb-1'><strong>Exactly one</strong> angle is a right angle ($= 90^\\circ$). The other two are complementary acute angles ($< 90^\\circ$, sum to $90^\\circ$).</p>
                        <p class='text-slate-400 italic'>Side opposite $90^\\circ$ is the <strong>hypotenuse</strong>.</p>
                    </div>
                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>
                        <h5 class='text-rose-300 font-bold text-sm mb-1'>3. Obtuse-Angled Triangle</h5>
                        <p class='text-slate-300 mb-1'><strong>Exactly one</strong> angle is obtuse ($> 90^\\circ$). The other two must be acute with a combined sum $< 90^\\circ$.</p>
                        <p class='text-slate-400 italic'>Example: $120^\\circ, 35^\\circ, 25^\\circ$.</p>
                    </div>
                </div>
                <div class='p-3 bg-slate-900 border border-amber-500/30 rounded-xl text-xs text-amber-200 mt-2'>
                    <strong>Why Can't a Triangle Have Two Obtuse Angles?</strong><br>
                    If two angles were $> 90^\\circ$, their sum would be $> 180^\\circ$, instantly violating the Angle Sum Property before even counting the third angle!
                </div>
            </div>
        """,
        "sim_id": "sim-triangle-by-angles",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "What is the longest side of a right-angled triangle called?",
                "options": ["Altitude", "Hypotenuse", "Base", "Median"],
                "correct": 1,
                "explanation": "The side opposite the 90° right angle is the longest side of a right triangle, known as the hypotenuse."
            },
            {
                "id": "cp15_2",
                "question": "If a triangle has angles measuring 92°, 44°, and 44°, what type of triangle is it by angle classification?",
                "options": ["Acute-angled", "Right-angled", "Obtuse-angled", "Equiangular"],
                "correct": 2,
                "explanation": "Because one angle measures 92° (which is greater than 90°), it is classified as an obtuse-angled triangle."
            }
        ]
    },

    # Slide 16: 7.5 Master Classification Matrix & Sulba Sutra Heritage
    {
        "id": "slide-16",
        "slide_num": 16,
        "section": "7.5",
        "title": "The Master Matrix & Baudhāyana's Śulba Geometry",
        "badge": "Heritage & Synthesis",
        "narration": "Let us unite sides and angles into a grand three-by-three matrix! We will discover which combinations thrive in harmony and which are mathematically impossible. We also celebrate my sacred Śulba Sūtras, where cord knotting pioneered practical right triangles thousands of years ago.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The 3x3 Classification Matrix & Ancient Vedic Geometry</h4>
                <div class='overflow-x-auto my-3'>
                    <table class='w-full text-xs text-left border-collapse border border-slate-700'>
                        <thead class='bg-slate-800 text-amber-300'>
                            <tr>
                                <th class='p-2 border border-slate-700'>Side \\ Angle</th>
                                <th class='p-2 border border-slate-700'>Acute ($< 90^\\circ$)</th>
                                <th class='p-2 border border-slate-700'>Right ($= 90^\\circ$)</th>
                                <th class='p-2 border border-slate-700'>Obtuse ($> 90^\\circ$)</th>
                            </tr>
                        </thead>
                        <tbody class='text-slate-300'>
                            <tr class='bg-slate-900/60'>
                                <td class='p-2 font-bold text-amber-200 border border-slate-700'>Equilateral</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ All ($60^\\circ, 60^\\circ, 60^\\circ$)</td>
                                <td class='p-2 text-rose-400 border border-slate-700'>❌ Impossible ($3 \\times 90^\\circ = 270^\\circ$)</td>
                                <td class='p-2 text-rose-400 border border-slate-700'>❌ Impossible ($3 \\times >90^\\circ > 270^\\circ$)</td>
                            </tr>
                            <tr class='bg-slate-800/40'>
                                <td class='p-2 font-bold text-amber-200 border border-slate-700'>Isosceles</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Acute Isosceles ($70^\\circ, 70^\\circ, 40^\\circ$)</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Right Isosceles ($45^\\circ, 45^\\circ, 90^\\circ$)</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Obtuse Isosceles ($30^\\circ, 30^\\circ, 120^\\circ$)</td>
                            </tr>
                            <tr class='bg-slate-900/60'>
                                <td class='p-2 font-bold text-amber-200 border border-slate-700'>Scalene</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Acute Scalene ($40^\\circ, 60^\\circ, 80^\\circ$)</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Right Scalene ($30^\\circ, 60^\\circ, 90^\\circ$)</td>
                                <td class='p-2 text-emerald-400 border border-slate-700'>✅ Obtuse Scalene ($20^\\circ, 40^\\circ, 120^\\circ$)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class='p-3 bg-amber-950/40 border border-amber-500/40 rounded-xl text-xs text-slate-300'>
                    <span class='text-amber-300 font-bold block mb-1'>Acharya Baudhāyana's Śulba Sūtra (c. 800 BCE):</span>
                    <em>"dīrghasyākṣaṇayā rajjuḥ pārśvamānī tiryaṅmānī ca yatpṛthagbhūte kurutastadubhayaṃ karoti"</em><br>
                    <span class='text-slate-400'>The cord stretched across the diagonal of a rectangle produces by itself what both the horizontal and vertical sides produce separately ($a^2 + b^2 = c^2$). Indian Vedic architects knotted cords into ratios 3:4:5, 5:12:13, and 8:15:17 to construct flawless right angles for sacrificial altars!</span>
                </div>
            </div>
        """,
        "sim_id": "sim-master-matrix-sulba",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "Can an equilateral triangle ever have a right angle or an obtuse angle?",
                "options": ["Yes, if sides are very long", "No, an equilateral triangle must always be acute with three 60° angles", "Only in spherical geometry", "Yes, in right equilateral triangles"],
                "correct": 1,
                "explanation": "Because all three sides are equal, all three angles must be equal: 180° / 3 = 60°. Hence, every equilateral triangle is strictly acute-angled."
            },
            {
                "id": "cp16_2",
                "question": "What are the angle measures of a Right-Angled Isosceles triangle?",
                "options": ["60°, 60°, 60°", "45°, 45°, 90°", "30°, 60°, 90°", "50°, 50°, 80°"],
                "correct": 1,
                "explanation": "A right isosceles triangle has one 90° right angle and two equal acute angles: (180° - 90°) / 2 = 45° each."
            }
        ]
    },

    # Slide 17: Mastery Challenge Part 1
    {
        "id": "slide-17",
        "slide_num": 17,
        "section": "Review",
        "title": "Mastery Challenge Part 1: Triangle Properties & Inequalities",
        "badge": "Mastery Challenge I",
        "narration": "Splendid progress! You have completed the theoretical foundations. Now, test your intellect on 10 rigorous challenges examining triangle anatomy, equilateral symmetries, and the triangle inequality.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Mastery Challenge Instructions</h4>
                <p class='text-slate-300 text-sm mb-2'>
                    Select your answer for each of the 10 questions below. Click <strong>Submit Answer</strong> to verify. Click <strong>💡 View Step-by-Step Solution</strong> for complete mathematical derivations and visual explanations.
                </p>
                <div class='p-2 bg-slate-800/80 rounded-lg text-xs text-amber-300 border border-amber-500/30'>
                    Target: Answer at least 8 out of 10 correctly to achieve Vedic Geometry Scholar status!
                </div>
            </div>
        """,
        "sim_id": None,
        "quiz_range": (1, 10)
    },

    # Slide 18: Mastery Challenge Part 2
    {
        "id": "slide-18",
        "slide_num": 18,
        "section": "Review",
        "title": "Mastery Challenge Part 2: Geometric Constructions (SSS, SAS, ASA)",
        "badge": "Mastery Challenge II",
        "narration": "Onward to the drafting arena! These 10 challenges evaluate your mastery of ruler-and-compass constructions: SSS circle radii, SAS included angles, and ASA ray convergence constraints.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Drafting Criteria & Arc Analysis</h4>
                <p class='text-slate-300 text-sm mb-2'>
                    Work through these construction questions carefully. Pay close attention to included vs non-included angles and base angle convergence conditions!
                </p>
            </div>
        """,
        "sim_id": None,
        "quiz_range": (11, 20)
    },

    # Slide 19: Mastery Challenge Part 3
    {
        "id": "slide-19",
        "slide_num": 19,
        "section": "Review",
        "title": "Mastery Challenge Part 3: Angle Sum Property & Exterior Angles",
        "badge": "Mastery Challenge III",
        "narration": "Now we test your deductive proofs and algebraic prowess on the sacred 180-degree Angle Sum Property and the Exterior Angle Theorem.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Angle Theorems & Linear Deductions</h4>
                <p class='text-slate-300 text-sm mb-2'>
                    Calculate missing angles, verify parallel line proofs, and determine exterior angle equations.
                </p>
            </div>
        """,
        "sim_id": None,
        "quiz_range": (21, 30)
    },

    # Slide 20: Mastery Challenge Part 4
    {
        "id": "slide-20",
        "slide_num": 20,
        "section": "Review",
        "title": "Mastery Challenge Part 4: Altitudes, Orthocenter & Classifications",
        "badge": "Mastery Challenge IV",
        "narration": "The final frontier! Test your mastery on triangle altitudes, set square construction mechanics, orthocenter concurrency locations, the 3x3 classification matrix, and Baudhāyana's ancient Śulba geometry.",
        "theory": """
            <div class='theory-box'>
                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Final Capstone Examination</h4>
                <p class='text-slate-300 text-sm mb-2'>
                    Complete the final 10 questions to complete your journey through A Tale of Three Intersecting Lines!
                </p>
            </div>
        """,
        "sim_id": None,
        "quiz_range": (31, 40)
    }
]

# 40 Mastery Quiz Questions
quiz_questions = [
    # Q1 (Slide 17)
    {
        "id": 1,
        "slide_num": 17,
        "question": "How many line segments bound a triangle?",
        "options": ["2", "3", "4", "6"],
        "correct": 1,
        "solution": "A triangle is a three-sided polygon bounded by exactly 3 line segments connecting its 3 non-collinear vertices."
    },
    # Q2 (Slide 17)
    {
        "id": 2,
        "slide_num": 17,
        "question": "In triangle $PQR$, the side opposite to vertex $R$ is denoted by:",
        "options": ["$QR$", "$PR$", "$PQ$ (or lowercase $r$)", "$P$"],
        "correct": 2,
        "solution": "The side opposite to vertex R joins the other two vertices, P and Q. Hence, it is side PQ (or lowercase r)."
    },
    # Q3 (Slide 17)
    {
        "id": 3,
        "slide_num": 17,
        "question": "Which of the following sets of numbers CANNOT be the side lengths of a triangle?",
        "options": ["3 cm, 4 cm, 5 cm", "6 cm, 7 cm, 8 cm", "2 cm, 5 cm, 7 cm", "5 cm, 12 cm, 13 cm"],
        "correct": 2,
        "solution": "By the Triangle Inequality Theorem, the sum of any two sides must be strictly greater than the third side. For 2, 5, 7: 2 + 5 = 7, which is NOT strictly greater than 7. Hence, no triangle can form."
    },
    # Q4 (Slide 17)
    {
        "id": 4,
        "slide_num": 17,
        "question": "If two sides of a triangle are 4 cm and 9 cm, the length of the third side $x$ must satisfy:",
        "options": ["$x > 13$", "$x < 5$", "$5 < x < 13$", "$x = 13$"],
        "correct": 2,
        "solution": "The third side must be strictly greater than the difference (9 - 4 = 5 cm) and strictly less than the sum (9 + 4 = 13 cm). Thus, 5 cm < x < 13 cm."
    },
    # Q5 (Slide 17)
    {
        "id": 5,
        "slide_num": 17,
        "question": "How many lines of reflective symmetry does an equilateral triangle have?",
        "options": ["1", "2", "3", "Infinite"],
        "correct": 2,
        "solution": "An equilateral triangle has 3 lines of symmetry: each connects one vertex to the midpoint of the opposite side."
    },
    # Q6 (Slide 17)
    {
        "id": 6,
        "slide_num": 17,
        "question": "If base $AB = 8\\text{ cm}$, and circle arcs drawn from $A$ and $B$ have radii $r_1 = 3\\text{ cm}$ and $r_2 = 4\\text{ cm}$, how many points of intersection occur?",
        "options": ["0 (they do not intersect)", "1 (tangent)", "2", "Infinite"],
        "correct": 0,
        "solution": "The sum of radii is 3 + 4 = 7 cm, which is less than the distance between centers AB = 8 cm. Thus, the circles do not touch, giving 0 intersections."
    },
    # Q7 (Slide 17)
    {
        "id": 7,
        "slide_num": 17,
        "question": "When constructing an equilateral triangle of side $6\\text{ cm}$, the compass opening for both arcs must be:",
        "options": ["3 cm", "6 cm", "12 cm", "Any length"],
        "correct": 1,
        "solution": "To make all three sides equal to 6 cm, the compass radius swung from both base endpoints must be exactly 6 cm."
    },
    # Q8 (Slide 17)
    {
        "id": 8,
        "slide_num": 17,
        "question": "A triangle with vertices $A(0,0), B(6,0), C(3, h)$ has two equal sides $AC = BC$. What type of triangle is this by side classification?",
        "options": ["Scalene", "Isosceles", "Right scalene", "Degenerate"],
        "correct": 1,
        "solution": "Since side AC = BC, the triangle has at least two sides of equal length, making it an isosceles triangle."
    },
    # Q9 (Slide 17)
    {
        "id": 9,
        "slide_num": 17,
        "question": "Can a triangle have sides of lengths 10 cm, 10 cm, and 20 cm?",
        "options": ["Yes, it is isosceles", "No, because 10 + 10 = 20 (it collapses into a line)", "Yes, it is right-angled", "Only if drawn on a sphere"],
        "correct": 1,
        "solution": "Since 10 + 10 = 20, the sum of the two shorter sides equals the third side. The vertices collapse into a single straight line segment."
    },
    # Q10 (Slide 17)
    {
        "id": 10,
        "slide_num": 17,
        "question": "Why does a compass arc construction guarantee that vertex $C$ is at the exact desired distance from vertex $A$?",
        "options": ["Because a compass measures angles", "Because all points on a circle are equidistant from its center", "Because compasses are made of steel", "Because circles have 360°"],
        "correct": 1,
        "solution": "By definition, a circle is the locus of all points in a plane that are at a fixed distance (the radius) from a given center point."
    },

    # Q11 (Slide 18)
    {
        "id": 11,
        "slide_num": 18,
        "question": "Which criterion guarantees triangle construction when two sides and the angle between them are known?",
        "options": ["SSS", "SAS", "ASA", "AAA"],
        "correct": 1,
        "solution": "The SAS (Side-Angle-Side) criterion guarantees a unique triangle when two sides and their included angle are given."
    },
    # Q12 (Slide 18)
    {
        "id": 12,
        "slide_num": 18,
        "question": "In triangle $XYZ$, what is the included angle between sides $XY$ and $YZ$?",
        "options": ["$\\angle X$", "$\\angle Y$", "$\\angle Z$", "$\\angle W$"],
        "correct": 1,
        "solution": "Vertex Y is shared by both line segments XY and YZ, so angle Y is the included angle between them."
    },
    # Q13 (Slide 18)
    {
        "id": 13,
        "slide_num": 18,
        "question": "To construct a triangle using the ASA criterion on base $BC$, what must be true about base angles $\\angle B$ and $\\angle C$?",
        "options": ["$\\angle B + \\angle C = 180^\\circ$", "$\\angle B + \\angle C < 180^\\circ$", "$\\angle B + \\angle C > 180^\\circ$", "$\\angle B = \\angle C = 90^\\circ$"],
        "correct": 1,
        "solution": "For the rays from B and C to tilt towards each other and intersect at vertex A, their sum must be strictly less than 180°."
    },
    # Q14 (Slide 18)
    {
        "id": 14,
        "slide_num": 18,
        "question": "If someone attempts to construct a triangle with base angles of $100^\\circ$ and $85^\\circ$, what will happen to the interior rays?",
        "options": ["They will intersect at an acute angle", "They will be parallel", "They will diverge away from each other and never meet", "They will form a circle"],
        "correct": 2,
        "solution": "100° + 85° = 185° > 180°. By Euclid's fifth postulate, the rays diverge on that side of the base and can never intersect."
    },
    # Q15 (Slide 18)
    {
        "id": 15,
        "slide_num": 18,
        "question": "Why is AAA (Angle-Angle-Angle) NOT sufficient to construct a unique triangle?",
        "options": ["Because angles cannot be measured", "Because AAA only fixes shape (similarity), not size; infinitely many magnified triangles share the same angles", "Because angle sum is not 180°", "Because it only works for right triangles"],
        "correct": 1,
        "solution": "Giving three angles fixes the shape of the triangle (similar triangles), but without at least one side length, the triangle can be scaled to any size."
    },
    # Q16 (Slide 18)
    {
        "id": 16,
        "slide_num": 18,
        "question": "In constructing $\\Delta ABC$ with $AB = 5\\text{ cm}, \\angle A = 60^\\circ, AC = 4\\text{ cm}$, what is the first step?",
        "options": ["Draw side $BC$", "Draw base segment $AB = 5\\text{ cm}$ with a ruler", "Draw a circle of radius 4 cm", "Draw altitude from C"],
        "correct": 1,
        "solution": "Standard construction begins by laying down the base segment AB = 5 cm, from which the angle at A can be constructed."
    },
    # Q17 (Slide 18)
    {
        "id": 17,
        "slide_num": 18,
        "question": "When constructing an SSS triangle, why do we draw two arcs rather than using a ruler to find the third vertex?",
        "options": ["Rulers cannot measure centimeters", "The arcs automatically find the exact geometric intersection satisfying both distance requirements without trial and error", "Rulers change length", "Because compasses are cheaper"],
        "correct": 1,
        "solution": "The intersection of the two arcs is the exact unique point that simultaneously satisfies both distance constraints from the two endpoints."
    },
    # Q18 (Slide 18)
    {
        "id": 18,
        "slide_num": 18,
        "question": "If $BC = 7\\text{ cm}, \\angle B = 45^\\circ, \\angle C = 45^\\circ$, what kind of triangle will be constructed?",
        "options": ["Equilateral", "Right-angled Isosceles", "Obtuse Scalene", "Acute Scalene"],
        "correct": 1,
        "solution": "Since angles B and C are each 45°, the sides opposite them are equal (isosceles). Angle A = 180° - (45° + 45°) = 90°, making it a right-angled isosceles triangle."
    },
    # Q19 (Slide 18)
    {
        "id": 19,
        "slide_num": 18,
        "question": "Can you construct a triangle with $AB = 6\\text{ cm}, \\angle B = 90^\\circ, \\angle C = 90^\\circ$?",
        "options": ["Yes, with hypotenuse 10 cm", "No, because the sum of the two angles is 180°, so the rays are parallel and never meet", "Yes, it forms a square", "Only if side BC is given"],
        "correct": 1,
        "solution": "Two 90° angles on base BC are perpendicular to BC. They are parallel lines and therefore never meet to form a third vertex."
    },
    # Q20 (Slide 18)
    {
        "id": 20,
        "slide_num": 18,
        "question": "What happens if you swing compass arcs for an SSS triangle below the base instead of above?",
        "options": ["An impossible shape forms", "You obtain a congruent triangle that is a mirror reflection of the one above", "The triangle becomes obtuse", "The side lengths double"],
        "correct": 1,
        "solution": "The two circles intersect at two symmetrical points: one above the base and one below. Constructing below produces an identical congruent triangle reflected across the base."
    },

    # Q21 (Slide 19)
    {
        "id": 21,
        "slide_num": 19,
        "question": "What is the sum of the three interior angles in ANY planar triangle?",
        "options": ["90°", "180°", "270°", "360°"],
        "correct": 1,
        "solution": "By the Angle Sum Property of Euclidean geometry, the sum of all three interior angles of any triangle is always exactly 180°."
    },
    # Q22 (Slide 19)
    {
        "id": 22,
        "slide_num": 19,
        "question": "In triangle $ABC$, if $\\angle A = 55^\\circ$ and $\\angle B = 65^\\circ$, what is the measure of $\\angle C$?",
        "options": ["50°", "60°", "70°", "120°"],
        "correct": 1,
        "solution": "Angle C = 180° - (Angle A + Angle B) = 180° - (55° + 65°) = 180° - 120° = 60°."
    },
    # Q23 (Slide 19)
    {
        "id": 23,
        "slide_num": 19,
        "question": "According to the Exterior Angle Theorem, an exterior angle of a triangle is equal to:",
        "options": ["The adjacent interior angle", "The sum of its two interior opposite angles", "180° minus the adjacent angle only", "Twice the opposite angle"],
        "correct": 1,
        "solution": "The Exterior Angle Theorem states that the measure of an exterior angle of a triangle is equal to the sum of the measures of its two interior opposite angles."
    },
    # Q24 (Slide 19)
    {
        "id": 24,
        "slide_num": 19,
        "question": "If an exterior angle of a triangle is $110^\\circ$ and one of the interior opposite angles is $40^\\circ$, what is the other interior opposite angle?",
        "options": ["40°", "70°", "110°", "150°"],
        "correct": 1,
        "solution": "Ext Angle = Angle 1 + Angle 2 ==> 110° = 40° + Angle 2 ==> Angle 2 = 110° - 40° = 70°."
    },
    # Q25 (Slide 19)
    {
        "id": 25,
        "slide_num": 19,
        "question": "In the parallel line proof of the angle sum property, which angle relationship is used when transversal $AB$ cuts parallel lines $XY$ and $BC$?",
        "options": ["Vertically opposite angles", "Alternate interior angles", "Corresponding exterior angles", "Linear pair"],
        "correct": 1,
        "solution": "The line segment AB acts as a transversal across XY || BC, creating equal alternate interior angles: angle XAB = angle B."
    },
    # Q26 (Slide 19)
    {
        "id": 26,
        "slide_num": 19,
        "question": "Can a triangle have one right angle and one obtuse angle?",
        "options": ["Yes, in scalene triangles", "No, because 90° plus an angle > 90° already exceeds 180°", "Yes, if the third angle is negative", "Only if sides are curved"],
        "correct": 1,
        "solution": "A right angle (90°) plus an obtuse angle (> 90°) gives a sum strictly greater than 180°, which is impossible in a Euclidean triangle."
    },
    # Q27 (Slide 19)
    {
        "id": 27,
        "slide_num": 19,
        "question": "In an isosceles triangle, if the vertex angle between the two equal sides is $80^\\circ$, what is the measure of each base angle?",
        "options": ["40°", "50°", "80°", "100°"],
        "correct": 1,
        "solution": "The sum of the two base angles is 180° - 80° = 100°. Since the base angles are equal, each measures 100° / 2 = 50°."
    },
    # Q28 (Slide 19)
    {
        "id": 28,
        "slide_num": 19,
        "question": "The three angles of a triangle are in the ratio $1 : 2 : 3$. What are the angle measures?",
        "options": ["20°, 40°, 60°", "30°, 60°, 90°", "15°, 30°, 45°", "40°, 60°, 80°"],
        "correct": 1,
        "solution": "Let the angles be x, 2x, 3x. Then x + 2x + 3x = 6x = 180°, so x = 30°. The angles are 30°, 60°, and 90°."
    },
    # Q29 (Slide 19)
    {
        "id": 29,
        "slide_num": 19,
        "question": "If side $BC$ is extended to $D$, the exterior angle $\\angle ACD$ and interior angle $\\angle ACB$ together form:",
        "options": ["A reflex angle", "A complementary pair (90°)", "A linear pair summing to 180°", "An equilateral pair"],
        "correct": 2,
        "solution": "Since B, C, and D lie on a straight line, angle ACD and angle ACB are adjacent angles on a straight line, forming a linear pair summing to 180°."
    },
    # Q30 (Slide 19)
    {
        "id": 30,
        "slide_num": 19,
        "question": "If all three exterior angles (one at each vertex) of a triangle are added together, what is their total sum?",
        "options": ["180°", "270°", "360°", "540°"],
        "correct": 2,
        "solution": "Each exterior angle is 180° - interior angle. Total sum = 3(180°) - (interior sum) = 540° - 180° = 360°."
    },

    # Q31 (Slide 20)
    {
        "id": 31,
        "slide_num": 20,
        "question": "What is an altitude of a triangle?",
        "options": ["A line joining a vertex to the midpoint of the opposite side", "A perpendicular line segment dropped from a vertex to the opposite side", "A line bisecting an interior angle", "The perimeter of the triangle"],
        "correct": 1,
        "solution": "An altitude is the perpendicular segment dropped from a vertex to the opposite side (or line containing the opposite side)."
    },
    # Q32 (Slide 20)
    {
        "id": 32,
        "slide_num": 20,
        "question": "How many altitudes does a triangle possess?",
        "options": ["1", "2", "3", "Infinitely many"],
        "correct": 2,
        "solution": "A triangle has three vertices, and from each vertex exactly one altitude can be dropped to the opposite side, making 3 altitudes in total."
    },
    # Q33 (Slide 20)
    {
        "id": 33,
        "slide_num": 20,
        "question": "Where does the orthocenter of an acute-angled triangle lie?",
        "options": ["Inside the triangle", "On the boundary", "Outside the triangle", "At infinity"],
        "correct": 0,
        "solution": "In an acute-angled triangle, all three altitudes lie entirely within the interior, so their intersection (the orthocenter) is inside the triangle."
    },
    # Q34 (Slide 20)
    {
        "id": 34,
        "slide_num": 20,
        "question": "Where does the orthocenter of an obtuse-angled triangle lie?",
        "options": ["Inside the triangle", "On the longest side", "Outside the triangle", "At the vertex of the obtuse angle"],
        "correct": 2,
        "solution": "In an obtuse triangle, the two altitudes from the acute vertices fall outside the triangle; their extended lines meet at an orthocenter located outside the triangle."
    },
    # Q35 (Slide 20)
    {
        "id": 35,
        "slide_num": 20,
        "question": "In a right-angled triangle $ABC$ with right angle at $B$, which point is the orthocenter?",
        "options": ["Vertex $A$", "Vertex $B$", "Vertex $C$", "Midpoint of hypotenuse $AC$"],
        "correct": 1,
        "solution": "In a right triangle, sides AB and BC are themselves altitudes, meeting at the right-angled vertex B. Thus, vertex B is the orthocenter."
    },
    # Q36 (Slide 20)
    {
        "id": 36,
        "slide_num": 20,
        "question": "Can an equilateral triangle be a right-angled triangle?",
        "options": ["Yes, if sides are 5 cm", "No, because all angles of an equilateral triangle must be 60°, never 90°", "Yes, in Indian geometry", "Only if it is scalene"],
        "correct": 1,
        "solution": "An equilateral triangle must have three equal angles (180° / 3 = 60°). It can never contain a 90° right angle."
    },
    # Q37 (Slide 20)
    {
        "id": 37,
        "slide_num": 20,
        "question": "A triangle has side lengths 5 cm, 5 cm, and 8 cm. How is it classified by its sides?",
        "options": ["Equilateral", "Isosceles", "Scalene", "Right-angled"],
        "correct": 1,
        "solution": "Because exactly two of its side lengths are equal (5 cm and 5 cm), it is classified as an isosceles triangle."
    },
    # Q38 (Slide 20)
    {
        "id": 38,
        "slide_num": 20,
        "question": "Which ancient Indian text contains geometric cord-rules for constructing right triangles for sacrificial altars?",
        "options": ["Aryabhatiya", "Baudhāyana Śulba Sūtra", "Surya Siddhanta", "Lilavati"],
        "correct": 1,
        "solution": "The Baudhāyana Śulba Sūtra (c. 800 BCE) contains the earliest Indian geometric rules for cord-based constructions of squares and right triangles."
    },
    # Q39 (Slide 20)
    {
        "id": 39,
        "slide_num": 20,
        "question": "Which of the following triples was used by Śulba Sūtra rope-stretchers to construct exact right angles?",
        "options": ["2, 3, 4", "3, 4, 5", "4, 5, 6", "1, 2, 3"],
        "correct": 1,
        "solution": "The triple (3, 4, 5) satisfies 3² + 4² = 9 + 16 = 25 = 5², forming an exact right angle used by Vedic rope-stretchers (rajju-karas)."
    },
    # Q40 (Slide 20)
    {
        "id": 40,
        "slide_num": 20,
        "question": "If a triangle has angles measuring 35°, 55°, and 90°, how is it classified by sides and angles?",
        "options": ["Acute Equilateral", "Right-angled Scalene", "Obtuse Isosceles", "Right-angled Isosceles"],
        "correct": 1,
        "solution": "Since one angle is 90°, it is right-angled. Since all three angles are different (35°, 55°, 90°), all three sides are different, making it a Right-angled Scalene triangle."
    }
]

with open('.agents/class7_math_tale_of_three_intersecting_lines_data.py', 'w') as f:
    f.write(f"SLIDES_DATA = {json.dumps(slides, indent=4)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {json.dumps(quiz_questions, indent=4)}\n")

print("Created .agents/class7_math_tale_of_three_intersecting_lines_data.py successfully!")
