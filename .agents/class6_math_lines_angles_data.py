"""NCERT Class 6 Mathematics Chapter 2: Lines and Angles Data Module."""

CHAPTER_META = {
    "chapter_num": 2,
    "title": "Lines and Angles",
    "subtitle": "NCERT Class 6 Mathematics • Chapter 2 Interactive Master Laboratory",
    "mentors": "Acharya Baudhāyana & Euclid",
    "mentors_title": "Pioneers of Sacred Sulba Sutras & Plane Geometry",
    "badge": "Ganita Prakash • Foundations of Geometry",
    "total_slides": 20,
    "checkpoints_count": 32,
    "quiz_questions_count": 40
}

SLIDES = [
    {
        "id": 1,
        "slide_num": 1,
        "title": "Point",
        "subtitle": "Exact Spatial Location",
        "badge": "Geometry Basics",
        "summary": "A point is a tiny dot marked by the sharp tip of a pencil. It represents a precise location in space and has zero length, zero breadth, and zero thickness. Points are denoted by single capital letters like P, Q, Z, or T.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Geometry begins with the simplest concept: a <strong class=\"text-amber-300\">point</strong>. Imagine sharpening your pencil to the finest possible tip and gently pressing it onto a smooth sheet of paper. The tiny dot you create gives an intuitive idea of a point.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📍</span> Definitive Characteristics\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Zero Dimensions:</strong> A point has no length, no breadth, and no height.</li>\n                <li>• <strong class=\"text-slate-100\">Exact Position:</strong> It merely determines an exact, motionless location in space.</li>\n                <li>• <strong class=\"text-slate-100\">Theoretical vs Physical:</strong> While a pencil dot has microscopic size, a true mathematical point has size zero!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏷️</span> Standard Naming Notation\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Always labeled using a <strong class=\"text-cyan-300\">single capital English letter</strong>.</li>\n                <li>• Written as: <span class=\"font-mono text-cyan-200 font-bold\">Point A, Point P, Point Z, Point T</span>.</li>\n                <li>• Multiple points in space determine geometric figures like triangles, squares, and lines.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>Did You Know?</strong> Euclid of Alexandria defined a point as: <em>\"A point is that which has no part.\"</em> In the ancient Indian Sulba Sutras, Baudhāyana used tiny peg-holes in the ground as reference points to orient sacred fire altars toward the cardinal directions!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "What are the dimensions (length, breadth, and height) of a true mathematical point?",
                "options": [
                    "Length only, but no width",
                    "Zero dimensions: no length, breadth, or height",
                    "Very small length of 0.1 mm",
                    "Equal length and breadth"
                ],
                "correct": 1,
                "explanation": "A point only marks an exact position; it has strictly zero dimensions (no length, no breadth, and no height)."
            },
            {
                "id": "cp1_2",
                "question": "How do mathematicians denote and read points in geometric diagrams?",
                "options": [
                    "Using Roman numerals like I, II, III",
                    "Using single lowercase letters like a, b, c",
                    "Using single capital letters like Point P or Point Z",
                    "Using Greek letters like α, β"
                ],
                "correct": 2,
                "explanation": "Points are always denoted by single capital English letters (such as Point P, Point Q, Point T)."
            }
        ]
    },
    {
        "id": 2,
        "slide_num": 2,
        "title": "Segment",
        "subtitle": "Direct Bound Path",
        "badge": "1D Geometry",
        "summary": "A line segment is the straight path connecting two distinct endpoints A and B. It has a definite measurable length and is modeled by a tight thread or paper crease. It is denoted by AB or BA with a bar above.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Take a sheet of paper and fold it in half. Press your thumb along the fold and open the sheet back up. The straight crease left on the paper gives the model of a <strong class=\"text-amber-300\">line segment</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📏</span> Key Properties\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Two Endpoints:</strong> Begins at point A and terminates at point B.</li>\n                <li>• <strong class=\"text-slate-100\">Shortest Distance:</strong> Among all possible curved or zigzag paths between A and B, the line segment is the shortest!</li>\n                <li>• <strong class=\"text-slate-100\">Measurable Length:</strong> Because it has two fixed ends, its length can be measured with a ruler (e.g., 5 cm).</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>✍️</span> Notation & Symmetry\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Denoted by writing the two endpoints with a bar on top: <strong class=\"text-cyan-200\">AB</strong> or <strong class=\"text-cyan-200\">BA</strong>.</li>\n                <li>• The order of letters does not matter: segment <strong class=\"text-cyan-200\">AB</strong> is identical to segment <strong class=\"text-cyan-200\">BA</strong>.</li>\n                <li>• Physical models: edge of a postcard, stretched rubber band, pencil body, or tube light.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Try this experiment:</strong> Pull a piece of string loosely between your two hands. It curves downward due to gravity. Now pull both hands apart tightly! The string straightens instantly into the shortest direct distance: a true line segment.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "How many endpoints does a line segment have?",
                "options": [
                    "Exactly two endpoints",
                    "Only one endpoint",
                    "No endpoints at all",
                    "Infinitely many endpoints"
                ],
                "correct": 0,
                "explanation": "A line segment has exactly two fixed endpoints that bound its length."
            },
            {
                "id": "cp2_2",
                "question": "If a line segment connects points X and Y, which of the following is true?",
                "options": [
                    "Segment XY is different from segment YX",
                    "Segment XY has infinite length",
                    "Segment XY and segment YX represent the exact same line segment",
                    "Segment XY cannot be measured with a ruler"
                ],
                "correct": 2,
                "explanation": "Order of endpoint letters does not change the segment; segment XY and segment YX are identical."
            }
        ]
    },
    {
        "id": 3,
        "slide_num": 3,
        "title": "Infinite Line",
        "subtitle": "Two-Way Extension",
        "badge": "1D Infinity",
        "summary": "When a line segment AB is extended endlessly without end in both opposite directions, it forms a straight line. It has no endpoints, cannot be measured, and is denoted by AB with a double arrow above or a single lowercase letter like l.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Imagine taking a line segment AB and extending it past point A forever to the left, and past point B forever to the right. This endless, infinite straight pathway is called a <strong class=\"text-amber-300\">line</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>↔️</span> Core Characteristics\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">No Endpoints:</strong> A line continues endlessly in both directions without stopping.</li>\n                <li>• <strong class=\"text-slate-100\">Cannot Be Measured:</strong> Because it is infinitely long, we cannot measure the length of a line!</li>\n                <li>• <strong class=\"text-slate-100\">Arrows on Both Ends:</strong> Diagrams always include arrowhead tips at both ends to indicate endless continuation.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📝</span> Naming Conventions\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• By any two points on the line with a double-headed arrow: <strong class=\"text-emerald-300\">Line AB</strong> or <strong class=\"text-emerald-300\">Line BA</strong>.</li>\n                <li>• Or by a single lowercase English letter: <strong class=\"text-emerald-300\">Line l, Line m, Line n</strong>.</li>\n                <li>• <strong class=\"text-amber-300\">Fundamental Axiom:</strong> Given any two distinct points in space, exactly <em>one unique line</em> passes through them!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Key Geometric Fact:</strong> While an infinite number of lines can pass through a single point P, once you specify a second point Q, only <strong>one single line</strong> can pass through both P and Q!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "How many endpoints does a line have?",
                "options": [
                    "Two endpoints",
                    "One endpoint",
                    "Zero endpoints (it extends endlessly in both directions)",
                    "Three endpoints"
                ],
                "correct": 2,
                "explanation": "A line has zero endpoints because it continues infinitely without stopping in both directions."
            },
            {
                "id": "cp3_2",
                "question": "How many unique straight lines can pass through two given distinct points?",
                "options": [
                    "Infinitely many lines",
                    "Exactly one unique line",
                    "Two different lines",
                    "Zero lines"
                ],
                "correct": 1,
                "explanation": "Two distinct points determine exactly one unique straight line in Euclidean geometry."
            }
        ]
    },
    {
        "id": 4,
        "slide_num": 4,
        "title": "Ray",
        "subtitle": "One-Way Beam",
        "badge": "1D Beam",
        "summary": "A ray is a portion of a line that begins at a fixed starting point (the initial point or origin) and extends endlessly in one direction. It is denoted by an arrow above two letters pointing from the start, such as Ray AP.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Switch on a torch in a dark room. The beam of light emerges from the bulb and travels outward endlessly through space. This real-life phenomenon gives us the concept of a <strong class=\"text-amber-300\">ray</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔦</span> Structure of a Ray\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Initial Point (Origin):</strong> The single fixed point where the ray starts (e.g., Point A).</li>\n                <li>• <strong class=\"text-slate-100\">Endless in One Direction:</strong> It passes through another point P and travels infinitely outward.</li>\n                <li>• <strong class=\"text-slate-100\">One Arrowhead:</strong> Shown with an arrow at only one end to indicate which way it extends.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⚠️</span> Critical Naming Rule\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Always write the <strong class=\"text-amber-300\">starting point first</strong>!</li>\n                <li>• <strong class=\"text-cyan-200\">Ray AP</strong> starts at A and goes through P.</li>\n                <li>• <strong class=\"text-rose-400\">Ray PA is NOT the same as Ray AP!</strong> Ray PA starts at P and travels through A in the opposite direction.</li>\n                <li>• Physical models: sun rays originating at the Sun, laser pointer beam, lighthouse beam.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>Notice the Difference:</strong> For segments, Segment AB = Segment BA. For lines, Line AB = Line BA. But for rays, <strong>Ray AB ≠ Ray BA</strong> because their starting points and directions are completely opposite!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "How many endpoints does a ray possess?",
                "options": [
                    "Exactly one endpoint (its initial starting point)",
                    "Two endpoints",
                    "Zero endpoints",
                    "Infinitely many"
                ],
                "correct": 0,
                "explanation": "A ray has exactly one endpoint called its initial starting point, extending endlessly in the other direction."
            },
            {
                "id": "cp4_2",
                "question": "Why is Ray AB NOT the same as Ray BA?",
                "options": [
                    "Because Ray AB is longer than Ray BA",
                    "Because Ray AB starts at A and goes toward B, while Ray BA starts at B and goes toward A",
                    "Because letters cannot be reversed in mathematics",
                    "Because one is curved and the other is straight"
                ],
                "correct": 1,
                "explanation": "The first letter indicates the fixed initial point; Ray AB begins at A, whereas Ray BA begins at B."
            }
        ]
    },
    {
        "id": 5,
        "slide_num": 5,
        "title": "Basic Shapes",
        "subtitle": "Core Elements Compared",
        "badge": "Comparison Lab",
        "summary": "Master the fundamental distinctions among geometric primitives: endpoints count, measurable length, notation, and physical models. This comparison forms the bedrock of all plane geometry.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us synthesize the four basic building blocks of geometry. Understanding their exact differences prevents common errors when constructing and measuring geometric figures.\n    </p>\n\n    <div class=\"overflow-x-auto my-3\">\n        <table class=\"w-full text-xs text-left border-collapse border border-slate-700 bg-slate-900/90 rounded-xl overflow-hidden\">\n            <thead>\n                <tr class=\"bg-slate-800 text-amber-300 border-b border-slate-700\">\n                    <th class=\"p-2.5\">Feature</th>\n                    <th class=\"p-2.5\">Point</th>\n                    <th class=\"p-2.5\">Line Segment</th>\n                    <th class=\"p-2.5\">Line</th>\n                    <th class=\"p-2.5\">Ray</th>\n                </tr>\n            </thead>\n            <tbody class=\"divide-y divide-slate-800 text-slate-300\">\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">Endpoints</td>\n                    <td class=\"p-2.5 text-cyan-300 font-mono\">0 (location only)</td>\n                    <td class=\"p-2.5 text-emerald-300 font-mono\">2 fixed ends</td>\n                    <td class=\"p-2.5 text-rose-300 font-mono\">0 ends</td>\n                    <td class=\"p-2.5 text-amber-300 font-mono\">1 starting end</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">Length</td>\n                    <td class=\"p-2.5\">Zero (no size)</td>\n                    <td class=\"p-2.5 text-emerald-300 font-bold\">Definite (measurable)</td>\n                    <td class=\"p-2.5 text-slate-400\">Infinite (unmeasurable)</td>\n                    <td class=\"p-2.5 text-slate-400\">Infinite (unmeasurable)</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">Symbolic Notation</td>\n                    <td class=\"p-2.5 font-mono text-cyan-200\">Point P</td>\n                    <td class=\"p-2.5 font-mono text-emerald-200\">AB or BA</td>\n                    <td class=\"p-2.5 font-mono text-rose-200\">Line AB or line l</td>\n                    <td class=\"p-2.5 font-mono text-amber-200\">Ray AP (start at A)</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">Physical Model</td>\n                    <td class=\"p-2.5\">Pencil prick, needle tip</td>\n                    <td class=\"p-2.5\">Ruler edge, tight string</td>\n                    <td class=\"p-2.5\">Railway track to horizons</td>\n                    <td class=\"p-2.5\">Laser beam, sunbeam</td>\n                </tr>\n            </tbody>\n        </table>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200\">\n        💡 <strong>Summary Rule:</strong> Only a <strong>line segment</strong> can be measured with a ruler! Lines and rays are infinitely long and can never be measured with a physical instrument.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "Which of the four geometric primitives can be measured with a ruler to give a finite length?",
                "options": [
                    "Only a line segment",
                    "Both a line and a ray",
                    "Only a ray",
                    "A point"
                ],
                "correct": 0,
                "explanation": "Only a line segment has two fixed endpoints, giving it a definite, measurable length."
            },
            {
                "id": "cp5_2",
                "question": "If you are given a geometric figure with exactly one starting point and extending endlessly in one direction, what is it?",
                "options": [
                    "A line segment",
                    "A line",
                    "A ray",
                    "A vertex"
                ],
                "correct": 2,
                "explanation": "A figure starting at a single initial point and continuing forever in one direction is a ray."
            }
        ]
    },
    {
        "id": 6,
        "slide_num": 6,
        "title": "Angle Formation",
        "subtitle": "Vertex & Rays",
        "badge": "Angle Formation",
        "summary": "An angle is formed when two rays originate from a common starting point called the vertex. The two rays are called the arms of the angle. It is named using the vertex in the middle, such as Angle DBE or Angle EBD.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Look around your classroom or home: the corner where two walls meet, the opening of a pair of scissors, the hands of a clock. All of these exhibit an <strong class=\"text-amber-300\">angle</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📐</span> Parts of an Angle\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-amber-300\">Vertex:</strong> The common initial starting point shared by both rays (e.g., Point B).</li>\n                <li>• <strong class=\"text-cyan-300\">Arms (Sides):</strong> The two rays that branch outward from the vertex (e.g., Ray BD and Ray BE).</li>\n                <li>• <strong class=\"text-slate-100\">Interior & Exterior:</strong> The region between the arms is called the interior of the angle.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏷️</span> Correct Naming Rule\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Represented by the angle symbol: <strong class=\"text-cyan-300\">∠</strong>.</li>\n                <li>• Three-letter name: Put one point on each arm, with the <strong class=\"text-amber-300\">vertex strictly in the middle</strong>!</li>\n                <li>• Example: <span class=\"font-mono text-cyan-200 font-bold\">∠DBE</span> or <span class=\"font-mono text-cyan-200 font-bold\">∠EBD</span>.</li>\n                <li>• If no confusion exists at the vertex, it can be named simply as <strong class=\"text-cyan-200\">∠B</strong>.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        ⚠️ <strong>Common Mistake:</strong> Never place the vertex first or last when using three letters! For an angle at vertex B with arms to D and E, ∠BDE is a completely different angle located at vertex D!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "In the angle denoted as ∠PQR, which point is the vertex?",
                "options": [
                    "Point P",
                    "Point Q (the middle letter)",
                    "Point R",
                    "Both P and R"
                ],
                "correct": 1,
                "explanation": "In standard three-letter angle notation, the vertex is always placed in the middle: Point Q."
            },
            {
                "id": "cp6_2",
                "question": "Which of the following represents the exact same angle as ∠ABC?",
                "options": [
                    "∠BAC",
                    "∠ACB",
                    "∠CBA",
                    "∠CAB"
                ],
                "correct": 2,
                "explanation": "Reversing the outer arm letters keeps the vertex B in the middle: ∠CBA is identical to ∠ABC."
            }
        ]
    },
    {
        "id": 7,
        "slide_num": 7,
        "title": "Rotational Turn",
        "subtitle": "Opening Degree",
        "badge": "Core Insight",
        "summary": "The size of an angle is the amount of turning or rotation needed to move one arm about the vertex until it lies along the other arm. Angle size depends purely on rotation, never on the physical length of the drawn arms!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        What makes one angle 'bigger' than another? Many beginners mistakenly look at the length of the arrows drawn on paper. But rays are infinite! An angle's size is determined solely by the <strong class=\"text-amber-300\">amount of rotation</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔄</span> The Dynamic Turn\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Imagine Ray 1 is lying flat along a horizontal line.</li>\n                <li>• Fix the vertex in place and rotate the ray upward like the hand of a clock.</li>\n                <li>• The degree of opening or 'spread' between the two arms measures the size of the angle.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-rose-500/30\">\n            <h5 class=\"font-bold text-rose-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🚫</span> Arm Length Invariance\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Drawing longer arms on paper <strong class=\"text-rose-300\">does NOT</strong> make the angle larger!</li>\n                <li>• A 30° angle drawn with 2 cm arms has the <strong class=\"text-slate-100\">exact same measure</strong> as a 30° angle drawn with 10-meter arms.</li>\n                <li>• Like opening a door: opening it 45 degrees creates the same angle whether the door is tiny or massive.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Clock Analogy:</strong> Think of a minute hand moving from 12 to 3. It sweeps out a quarter-turn regardless of whether it is a small wristwatch or the massive tower clock of Big Ben!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "If you double the length of the lines drawn to represent the arms of a 40° angle, what happens to the angle measure?",
                "options": [
                    "It doubles to 80°",
                    "It remains exactly 40° (arm length does not change angle size)",
                    "It halves to 20°",
                    "It becomes a straight angle"
                ],
                "correct": 1,
                "explanation": "Angle size measures the amount of turn between the arms; changing arm length has zero effect on the angle."
            },
            {
                "id": "cp7_2",
                "question": "What fundamental physical concept defines the size of an angle?",
                "options": [
                    "The distance between the two arrowheads",
                    "The amount of rotation around the vertex needed to turn one arm onto the other",
                    "The thickness of the drawn pencil lines",
                    "The area of the paper surrounding the vertex"
                ],
                "correct": 1,
                "explanation": "The size of an angle is defined mathematically as the amount of rotation about the vertex from one arm to the other."
            }
        ]
    },
    {
        "id": 8,
        "slide_num": 8,
        "title": "Overlay Comparison",
        "subtitle": "Matching Vertices & Arms",
        "badge": "Comparison Method 1",
        "summary": "To compare two angles directly by superimposition, trace one angle onto transparent paper and place it on top of the other, perfectly aligning their vertices and one arm. The position of the second arm reveals which angle is larger.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        When two angles look very close in size, how can we be certain which one is larger? The first direct geometric method is called <strong class=\"text-amber-300\">superimposition</strong> (placing one figure directly over another).\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📑</span> Step-by-Step Procedure\n            </h5>\n            <ol class=\"text-xs space-y-1.5 text-slate-300 list-decimal list-inside\">\n                <li>Trace angle ∠ABC onto a piece of thin tracing paper.</li>\n                <li>Pick up the tracing paper and place it over the second angle ∠DEF.</li>\n                <li><strong class=\"text-amber-300\">Align Vertices:</strong> Place vertex B directly on top of vertex E.</li>\n                <li><strong class=\"text-cyan-300\">Align Base Arm:</strong> Rotate the tracing paper so that ray BC lies perfectly along ray EF.</li>\n            </ol>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔍</span> Reading the Outcome\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-emerald-300\">Arm BA lies inside ∠DEF:</strong> Angle ∠ABC is smaller than ∠DEF.</li>\n                <li>• <strong class=\"text-cyan-300\">Arm BA coincides with ED:</strong> Both angles are equal in size (congruent).</li>\n                <li>• <strong class=\"text-amber-300\">Arm BA lies outside ∠DEF:</strong> Angle ∠ABC is larger than ∠DEF.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Key Requirement:</strong> Superimposition only works if the two vertices AND one pair of arms match up perfectly! If the vertices do not overlap, no valid comparison can be made.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "What two parts must be perfectly aligned when comparing two angles by superimposition?",
                "options": [
                    "The two arrowheads",
                    "The common vertices and one pair of corresponding arms",
                    "The lengths of both pairs of arms",
                    "The midpoint of both rays"
                ],
                "correct": 1,
                "explanation": "You must place vertex on vertex and align one arm along the other arm to test where the second arm falls."
            },
            {
                "id": "cp8_2",
                "question": "If arm BA falls strictly in the interior of ∠DEF after aligning vertex B on E and arm BC on EF, which angle is larger?",
                "options": [
                    "∠ABC is larger",
                    "∠DEF is larger",
                    "Both angles are equal",
                    "It cannot be determined"
                ],
                "correct": 1,
                "explanation": "Since arm BA lies inside ∠DEF, ∠DEF has a wider opening and is therefore the larger angle."
            }
        ]
    },
    {
        "id": 9,
        "slide_num": 9,
        "title": "Arc Comparison",
        "subtitle": "Equal Radius Testing",
        "badge": "Comparison Method 2",
        "summary": "When angles cannot be moved or traced, we compare them using circular arc templates. Draw a circle of equal radius centered at each vertex; the angle that intercepts a longer circular arc has the greater degree of turn.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        What if the two angles are drawn on heavy wooden tables or walls where you cannot superimpose them? We use a <strong class=\"text-amber-300\">circular arc template</strong> centered at each vertex.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⭕</span> Equal-Radius Principle\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Take a compass and set it to a fixed radius (e.g., 4 cm).</li>\n                <li>• Place the needle at vertex B and draw a circular arc cutting both arms at P and Q.</li>\n                <li>• Keeping the <strong class=\"text-amber-300\">exact same compass radius</strong>, draw an arc centered at vertex E cutting its arms at X and Y.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📏</span> Comparing Arc Distances\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Measure the curved arc distance between P and Q along the circle using a strip of paper.</li>\n                <li>• Measure the curved arc distance between X and Y.</li>\n                <li>• <strong class=\"text-emerald-300\">Theorem:</strong> For equal radii, the angle with the <strong class=\"text-slate-100\">longer intercepted arc</strong> is strictly the larger angle!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        ⚠️ <strong>Crucial Condition:</strong> The compass opening (radius) MUST be identical for both angles! If you draw a large radius on one angle and a tiny radius on the other, the arc lengths cannot be compared directly.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "When comparing two angles using circular arcs without superimposition, what condition is mandatory?",
                "options": [
                    "The arms must be of equal drawn length",
                    "The circular arcs must be drawn with the exact same radius from their respective vertices",
                    "Both angles must point to the right",
                    "The angles must be right angles"
                ],
                "correct": 1,
                "explanation": "Arc length comparison is valid only when both arcs are drawn with identical radii from their vertices."
            },
            {
                "id": "cp9_2",
                "question": "If arc PQ on Angle 1 has length 3.2 cm and arc XY on Angle 2 has length 4.8 cm (both with 5 cm radius), which angle is larger?",
                "options": [
                    "Angle 1",
                    "Angle 2",
                    "They are equal",
                    "Cannot be determined without a protractor"
                ],
                "correct": 1,
                "explanation": "At equal radius, a longer intercepted arc directly corresponds to a greater angle of rotation; Angle 2 is larger."
            }
        ]
    },
    {
        "id": 10,
        "slide_num": 10,
        "title": "Slit Test",
        "subtitle": "Passage by Degree",
        "badge": "Hands-On Science",
        "summary": "By joining two paper straws with a paper clip, we create rotating arms. Testing whether these arms can pass through a narrow slit in cardboard proves that an angle's passage depends solely on its degree of turn, not on the length of its arms.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us perform the famous NCERT <strong class=\"text-amber-300\">Slit-Passing Activity</strong>. Take two paper straws and link them at one end using a brass paper fastener or paper clip so they can pivot freely like a pair of compasses.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>✂️</span> Cardboard Slit Setup\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Cut a V-shaped triangular slit into a sheet of stiff cardboard.</li>\n                <li>• The slit has a fixed opening angle of, say, <strong class=\"text-amber-300\">30°</strong>.</li>\n                <li>• Try sliding your rotating straw arms into the slit.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🎯</span> Experimental Discovery\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• If you open the straws to <strong class=\"text-rose-400\">45°</strong>, they will jam and refuse to pass into the 30° slit, even if you cut the straws very short!</li>\n                <li>• If you set the straws to <strong class=\"text-emerald-400\">30°</strong>, they slip through effortlessly, even if the straws are two meters long!</li>\n                <li>• <strong class=\"text-slate-100\">Conclusion:</strong> Fitting into an angular opening depends 100% on degree of turn and 0% on arm length!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Engineering Application:</strong> Scissors, pliers, door hinges, and aircraft wings all operate on this exact rotational principle. Mechanical clearances depend on angle of rotation rather than arm size!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "What determines whether a pair of rotating straw arms can pass smoothly into a V-shaped slit?",
                "options": [
                    "The color of the straws",
                    "The physical length of the straws",
                    "The angle of opening between the straws matching or being smaller than the slit angle",
                    "The thickness of the cardboard"
                ],
                "correct": 2,
                "explanation": "Passing through an angular slit depends strictly on the degree of rotation (opening angle) between the arms."
            },
            {
                "id": "cp10_2",
                "question": "Will a 60° angle with very short 1 cm arms pass into a 40° slit without jamming?",
                "options": [
                    "Yes, because the arms are very short",
                    "No, because its angle of opening (60°) is wider than the slit (40°)",
                    "Yes, if pushed hard enough",
                    "It depends on the time of day"
                ],
                "correct": 1,
                "explanation": "Since 60° is wider than 40°, the arms will jam against the slit walls regardless of how short they are."
            }
        ]
    },
    {
        "id": 11,
        "slide_num": 11,
        "title": "Right & Straight",
        "subtitle": "Quarter & Half Turns",
        "badge": "Special Benchmarks",
        "summary": "A straight angle is formed by a half-turn where both arms lie along a single straight line in opposite directions. Bisecting a straight angle into two equal parts yields a right angle (quarter-turn, 90°). Lines meeting at 90° are perpendicular.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Two benchmark angles form the foundation of geometry, construction, and architecture: the <strong class=\"text-amber-300\">straight angle</strong> and the <strong class=\"text-cyan-300\">right angle</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>↔️</span> Straight Angle (Half-Turn)\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Formed when one arm rotates through half of a complete circle.</li>\n                <li>• Both arms lie along the <strong class=\"text-amber-300\">same straight line</strong> pointing in directly opposite directions (e.g., Ray OA and Ray OB).</li>\n                <li>• Measure: exactly <strong class=\"text-slate-100\">180°</strong> (half-turn).</li>\n                <li>• Clock example: Hands at 6:00 show a straight angle!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📐</span> Right Angle & Perpendiculars\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Bisect a straight angle into two equal halves: each half is a <strong class=\"text-cyan-300\">right angle</strong>.</li>\n                <li>• Represents a <strong class=\"text-slate-100\">quarter-turn</strong> and measures exactly <strong class=\"text-cyan-300\">90°</strong>.</li>\n                <li>• Forms an 'L' shape; marked in diagrams with a small square corner symbol: <strong class=\"text-cyan-300\">∟</strong>.</li>\n                <li>• Two lines that meet at right angles are called <strong class=\"text-emerald-300\">perpendicular lines</strong> (symbol: <strong class=\"text-emerald-300\">⊥</strong>).</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Baudhāyana's Sulba Sutra:</strong> Ancient Indian temple architects used cords and peg triangles (with ratios like 3:4:5 and 5:12:13) to construct perfectly perpendicular right angles for sacred Vedic fire altars!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "How many right angles are needed to make one straight angle?",
                "options": [
                    "Exactly two right angles (90° + 90° = 180°)",
                    "One right angle",
                    "Three right angles",
                    "Four right angles"
                ],
                "correct": 0,
                "explanation": "A straight angle is 180°, which equals exactly two right angles (90° each) side by side."
            },
            {
                "id": "cp11_2",
                "question": "What are two lines called when they intersect at an angle of 90 degrees?",
                "options": [
                    "Parallel lines",
                    "Perpendicular lines",
                    "Collinear lines",
                    "Curved lines"
                ],
                "correct": 1,
                "explanation": "Lines that intersect at a right angle (90°) are defined as perpendicular lines (denoted AB ⊥ CD)."
            }
        ]
    },
    {
        "id": 12,
        "slide_num": 12,
        "title": "Degree Measure",
        "subtitle": "360-Part Circle",
        "badge": "Number Assignment",
        "summary": "To assign numbers to angles, a complete circle turn is divided into 360 equal parts, where each unit part is 1 degree (1°). The number 360 was chosen historically due to ancient 360-day solar calendars, the Rigveda, and its high divisibility.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Just as we use centimeters to measure length and grams to measure mass, we need a standard unit to measure rotation. Mathematicians divide a full-turn circle into <strong class=\"text-amber-300\">360 equal parts</strong>. Each part is called <strong class=\"text-cyan-300\">one degree</strong>, written as <strong class=\"text-cyan-300\">1°</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>☀️</span> Historical Origins: Astronomy & Rigveda\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Ancient astronomers observed that the Sun takes roughly <strong class=\"text-amber-300\">365 days</strong> to complete a full cycle through the constellations (roughly 1° per day).</li>\n                <li>• The ancient Indian text <strong class=\"text-slate-100\">Rigveda (1.164.48)</strong> poetically describes the cosmic wheel of time as having <strong class=\"text-amber-300\">360 spokes</strong> (days of the solar year).</li>\n                <li>• Babylonian astronomers rounded the year to 360 days for convenient calculations.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔢</span> Mathematical Power: Divisibility\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• 360 is an exceptionally composite number with <strong class=\"text-emerald-300\">24 whole-number factors</strong>!</li>\n                <li>• It divides cleanly by 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180.</li>\n                <li>• Half-turn = 360° ÷ 2 = <strong class=\"text-amber-300\">180°</strong>.</li>\n                <li>• Quarter-turn = 360° ÷ 4 = <strong class=\"text-cyan-300\">90°</strong>.</li>\n                <li>• One-third turn = 360° ÷ 3 = <strong class=\"text-emerald-300\">120°</strong>.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200\">\n        💡 <strong>Think About It:</strong> If the circle had 100 degrees, dividing it into thirds would give an awkward 33.333... degrees! With 360, one-third is a crisp, clean 120°.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "How many degrees are in one complete full rotation (circle)?",
                "options": [
                    "100°",
                    "180°",
                    "360°",
                    "720°"
                ],
                "correct": 2,
                "explanation": "A full-circle turn is divided by definition into exactly 360 degrees (360°)."
            },
            {
                "id": "cp12_2",
                "question": "Why is 360 preferred over 100 for dividing a circle?",
                "options": [
                    "Because 360 has 24 factors, dividing evenly into halves, thirds, quarters, fifths, sixths, and twelfths",
                    "Because 100 was only invented recently",
                    "Because 360 is an odd number",
                    "Because protractors cannot fit 100 marks"
                ],
                "correct": 0,
                "explanation": "360 is highly divisible by 2, 3, 4, 5, 6, 8, 9, 10, 12, making fractions of turns whole numbers."
            }
        ]
    },
    {
        "id": 13,
        "slide_num": 13,
        "title": "Protractor Tool",
        "subtitle": "Dual Scales & Folds",
        "badge": "Measuring Tool",
        "summary": "A protractor is a semicircular instrument divided into 180 equal degrees. It features dual scales (inner and outer) running in opposite directions, a center mark, and a base line. Students can construct a paper protractor through successive paper folds.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        The tool in your geometry box used to measure and draw angles is the <strong class=\"text-amber-300\">protractor</strong>. It is a semicircle spanning from 0° to 180°.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧭</span> Anatomical Parts of a Protractor\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-amber-300\">Center Mark:</strong> The midpoint along the straight bottom edge, placed directly onto the angle's vertex.</li>\n                <li>• <strong class=\"text-cyan-300\">Baseline (0°–180° line):</strong> The straight reference edge aligned along the base arm of the angle.</li>\n                <li>• <strong class=\"text-emerald-300\">Dual Scales:</strong> Two sets of degree markings from 0° to 180° (Inner scale reads counter-clockwise; Outer scale reads clockwise).</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📄</span> Making a Paper Protractor\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Cut out a circular disc of paper (360° full circle).</li>\n                <li>• <strong class=\"text-slate-100\">Fold 1 in half:</strong> The straight edge gives a <strong class=\"text-amber-300\">180° straight angle</strong>.</li>\n                <li>• <strong class=\"text-slate-100\">Fold 2 in quarters:</strong> Crease gives a <strong class=\"text-cyan-300\">90° right angle</strong>.</li>\n                <li>• <strong class=\"text-slate-100\">Fold 3 in eighths:</strong> Crease gives a <strong class=\"text-emerald-300\">45° angle</strong>.</li>\n                <li>• <strong class=\"text-slate-100\">Fold 3-way:</strong> Folding into thirds yields <strong class=\"text-violet-300\">30° and 60°</strong> benchmarks!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Scale Reading Rule:</strong> Always start reading from the scale whose <strong class=\"text-amber-300\">0° mark lies on your base arm</strong>! If the base ray points right, read the inner scale starting at 0°; if it points left, read the outer scale starting at 0°.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "Why do protractors have two sets of scales (inner and outer)?",
                "options": [
                    "One for centimeters and one for inches",
                    "To allow convenient measurement of angles opening either from the right or from the left",
                    "One for acute angles and one for reflex angles",
                    "One is a backup in case the first fades"
                ],
                "correct": 1,
                "explanation": "Dual scales allow you to read from 0° regardless of whether the base arm extends to the right or to the left."
            },
            {
                "id": "cp13_2",
                "question": "If you fold a paper circle in half (180°) and then fold that semicircle in half again, what angle does the corner crease form?",
                "options": [
                    "45°",
                    "60°",
                    "90° (a right angle)",
                    "120°"
                ],
                "correct": 2,
                "explanation": "Halving a 180° straight angle yields 180° ÷ 2 = 90°, creating a perfect right angle corner."
            }
        ]
    },
    {
        "id": 14,
        "slide_num": 14,
        "title": "Angle Drafting",
        "subtitle": "Step Construction Protocol",
        "badge": "Drafting Skill",
        "summary": "Constructing an angle of given degree measure (e.g. Angle TIN = 30°) involves 4 sequential steps: drawing a base ray, aligning the protractor's center and baseline, placing a pencil mark at the target degree, and drawing the second ray.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us master the four-step protocol for accurately constructing any specified angle, such as drawing <strong class=\"text-amber-300\">∠TIN = 30°</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>1️⃣ & 2️⃣</span> Steps 1 & 2: Base Ray & Alignment\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Step 1: Draw Reference Ray:</strong> Using a ruler, draw a straight ray <strong class=\"text-amber-300\">Ray IT</strong> with initial point I (the future vertex) and arrowhead at T.</li>\n                <li>• <strong class=\"text-slate-100\">Step 2: Position Protractor:</strong> Place the protractor's center mark directly on vertex I, and rotate until the baseline rests precisely along Ray IT.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>3️⃣ & 4️⃣</span> Steps 3 & 4: Marking & Connecting\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Step 3: Mark the Degree:</strong> Find 0° on Ray IT. Follow the scale up to <strong class=\"text-emerald-300\">30°</strong>. With a sharp pencil, make a small dot <strong class=\"text-cyan-300\">N</strong> directly beside the 30° mark.</li>\n                <li>• <strong class=\"text-slate-100\">Step 4: Draw Second Ray:</strong> Remove the protractor. Using a ruler, draw a ray starting at vertex I passing through point N. Label the result: <strong class=\"text-slate-100\">∠TIN = 30°</strong>!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Quick Reality Check:</strong> Before removing your protractor, ask yourself: <em>\"Is 30° smaller than an 'L' shape?\"</em> Yes! If your drawn ray looks wider than a right angle, you accidentally read from the wrong 150° scale.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "When drawing ∠TIN = 30°, where must the center mark of the protractor be placed?",
                "options": [
                    "At point T",
                    "At point I (the vertex in the middle)",
                    "At point N",
                    "Anywhere along the ray"
                ],
                "correct": 1,
                "explanation": "The center mark must always be aligned precisely over the vertex of the angle: Point I."
            },
            {
                "id": "cp14_2",
                "question": "If you intend to draw an acute angle of 40° but your drawn angle looks wider than a right angle (looking like 140°), what mistake happened?",
                "options": [
                    "The ruler was crooked",
                    "You read from the outer scale instead of the inner scale starting at 0° on the base ray",
                    "40° is an obtuse angle",
                    "The pencil tip was too blunt"
                ],
                "correct": 1,
                "explanation": "Reading from the wrong scale reads the supplement (180° - 40° = 140°) instead of the target 40°."
            }
        ]
    },
    {
        "id": 15,
        "slide_num": 15,
        "title": "Angle Categories",
        "subtitle": "Sharp, Square & Wide",
        "badge": "Angle Taxonomy",
        "summary": "Angles are formally categorized into standard classes by their degree measures: Acute angles measure between 0° and 90°, Right angles measure exactly 90°, and Obtuse angles measure between 90° and 180°.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Just as biologists classify animals into families, mathematicians classify angles into clear families based on their degree measures compared against the <strong class=\"text-cyan-300\">90° right angle</strong> benchmark.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-3 gap-3 my-3\">\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <div class=\"flex items-center justify-between mb-1\">\n                <h5 class=\"font-bold text-amber-300 text-xs\">Acute Angle</h5>\n                <span class=\"text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300\">0° &lt; θ &lt; 90°</span>\n            </div>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Smaller than a quarter-turn. Narrow, sharp, and pointed like a beak.<br>\n                <em>Examples:</em> 15°, 30°, 45°, 60°, 89°.\n            </p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <div class=\"flex items-center justify-between mb-1\">\n                <h5 class=\"font-bold text-cyan-300 text-xs\">Right Angle</h5>\n                <span class=\"text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300\">θ = 90°</span>\n            </div>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Exactly a quarter-turn. Forms a sharp 'L' corner where arms are perpendicular.<br>\n                <em>Examples:</em> Page corners, window frames.\n            </p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <div class=\"flex items-center justify-between mb-1\">\n                <h5 class=\"font-bold text-emerald-300 text-xs\">Obtuse Angle</h5>\n                <span class=\"text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300\">90° &lt; θ &lt; 180°</span>\n            </div>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Wider than a right angle but smaller than a straight line.<br>\n                <em>Examples:</em> 95°, 120°, 135°, 150°, 179°.\n            </p>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>Memory Tip:</strong> In Latin, <em>acutus</em> means 'sharp' (like a needle tip), while <em>obtusus</em> means 'blunt' or 'dull'. A right angle stands upright and perpendicular!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "An angle measures 89.5 degrees. What type of angle is it?",
                "options": [
                    "Acute angle (since it is strictly less than 90°)",
                    "Right angle",
                    "Obtuse angle",
                    "Straight angle"
                ],
                "correct": 0,
                "explanation": "Any angle greater than 0° and strictly less than 90° is an acute angle, even at 89.5°."
            },
            {
                "id": "cp15_2",
                "question": "Which of the following angles is an obtuse angle?",
                "options": [
                    "45°",
                    "90°",
                    "135°",
                    "180°"
                ],
                "correct": 2,
                "explanation": "135° is strictly between 90° and 180°, making it an obtuse angle."
            }
        ]
    },
    {
        "id": 16,
        "slide_num": 16,
        "title": "Reflex Turns",
        "subtitle": "Beyond Straight Angles",
        "badge": "Advanced Classification",
        "summary": "A straight angle measures exactly 180°. An angle measuring greater than 180° and less than 360° is called a reflex angle. A full complete turn measures 360°.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        What happens when rotation continues past a straight line? Rotating beyond 180° brings us into the realm of <strong class=\"text-violet-300\">reflex angles</strong> and complete turns.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>↔️</span> Straight Angle (Exact 180°)\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Exactly half of a complete rotation (<strong class=\"text-amber-300\">θ = 180°</strong>).</li>\n                <li>• The arms point in diametrically opposite directions along a single line.</li>\n                <li>• Contains exactly 2 right angles (<span class=\"font-mono text-cyan-300\">90° + 90° = 180°</span>).</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-violet-500/30\">\n            <h5 class=\"font-bold text-violet-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔄</span> Reflex Angle (180° &lt; θ &lt; 360°)\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Greater than a half-turn but less than a full turn.</li>\n                <li>• Represents the <strong class=\"text-violet-300\">outer 'reflex' opening</strong> of an angle.</li>\n                <li>• For any inner angle θ, its outer reflex partner is <strong class=\"text-slate-100\">360° − θ</strong>!</li>\n                <li>• Complete Turn (<strong class=\"text-emerald-300\">360°</strong>): The ray rotates full circle back onto itself.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-violet-950/20 border border-violet-500/20 text-xs text-violet-200\">\n        💡 <strong>Reflex Pair Example:</strong> When a clock shows 9:00, the hands form an inner right angle of 90°. The reflex angle on the outer side is 360° − 90° = <strong>270°</strong> (three quarter-turns)!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "An angle measures 250 degrees. How is it classified?",
                "options": [
                    "Obtuse angle",
                    "Straight angle",
                    "Reflex angle",
                    "Acute angle"
                ],
                "correct": 2,
                "explanation": "Because 250° is strictly between 180° and 360°, it is classified as a reflex angle."
            },
            {
                "id": "cp16_2",
                "question": "If the inner acute angle between two rays is 60°, what is the measure of the outer reflex angle?",
                "options": [
                    "120°",
                    "180°",
                    "300° (since 360° − 60° = 300°)",
                    "240°"
                ],
                "correct": 2,
                "explanation": "The inner angle and outer reflex angle always sum to a full 360°: 360° − 60° = 300°."
            }
        ]
    },
    {
        "id": 17,
        "slide_num": 17,
        "title": "Quiz Challenge 1",
        "subtitle": "Questions 1 to 10",
        "badge": "Quiz Challenge 1",
        "is_quiz": True,
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": 18,
        "slide_num": 18,
        "title": "Quiz Challenge 2",
        "subtitle": "Questions 11 to 20",
        "badge": "Quiz Challenge 2",
        "is_quiz": True,
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": 19,
        "slide_num": 19,
        "title": "Quiz Challenge 3",
        "subtitle": "Questions 21 to 30",
        "badge": "Quiz Challenge 3",
        "is_quiz": True,
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": 20,
        "slide_num": 20,
        "title": "Quiz Challenge 4",
        "subtitle": "Questions 31 to 40",
        "badge": "Quiz Challenge 4",
        "is_quiz": True,
        "quiz_range": [
            31,
            40
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "challenge": 1,
        "question": "What is the primary geometric purpose of a mathematical point?",
        "options": [
            "To measure the length of a line",
            "To determine an exact location in space without size or dimensions",
            "To create a circular boundary",
            "To calculate area"
        ],
        "correct": 1,
        "explanation": "A point only marks a precise, dimensionless location in space; it has zero length, width, or thickness."
    },
    {
        "id": 2,
        "challenge": 1,
        "question": "How many endpoints does a line segment have?",
        "options": [
            "Zero",
            "One",
            "Two",
            "Infinitely many"
        ],
        "correct": 2,
        "explanation": "A line segment is bounded by exactly two endpoints."
    },
    {
        "id": 3,
        "challenge": 1,
        "question": "Which of the following correctly denotes a line passing through points P and Q?",
        "options": [
            "Line segment PQ",
            "Line PQ (or Line QP, with double-headed arrow)",
            "Ray PQ only",
            "Point PQ"
        ],
        "correct": 1,
        "explanation": "A line extends endlessly both ways through P and Q, written as Line PQ or Line QP."
    },
    {
        "id": 4,
        "challenge": 1,
        "question": "How many distinct straight lines can pass through two given points in a plane?",
        "options": [
            "Zero",
            "Exactly one",
            "Two",
            "Infinitely many"
        ],
        "correct": 1,
        "explanation": "In Euclidean geometry, two distinct points determine exactly one unique straight line."
    },
    {
        "id": 5,
        "challenge": 1,
        "question": "Which of the following is a real-world physical model of a ray?",
        "options": [
            "The edge of a ruler",
            "A beam of light emitted from a lighthouse",
            "A tightly stretched jump rope",
            "The surface of a dining table"
        ],
        "correct": 1,
        "explanation": "A lighthouse light beam starts at a fixed source bulb (initial point) and extends endlessly outward."
    },
    {
        "id": 6,
        "challenge": 1,
        "question": "Which geometric primitive has a measurable, definite physical length?",
        "options": [
            "A line",
            "A ray",
            "A line segment",
            "A point"
        ],
        "correct": 2,
        "explanation": "Only a line segment has two fixed endpoints, making its length measurable with a ruler."
    },
    {
        "id": 7,
        "challenge": 1,
        "question": "Why is Ray AB not identical to Ray BA?",
        "options": [
            "They have different colors",
            "Ray AB starts at A and extends through B, while Ray BA starts at B and extends through A",
            "Ray AB is longer than Ray BA",
            "Ray BA is a curved line"
        ],
        "correct": 1,
        "explanation": "The first letter specifies the fixed initial starting point; thus Ray AB and Ray BA point in opposite directions."
    },
    {
        "id": 8,
        "challenge": 1,
        "question": "How many lines can pass through a single given point in a plane?",
        "options": [
            "Only one",
            "Only two",
            "Infinitely many",
            "Zero"
        ],
        "correct": 2,
        "explanation": "An infinite number of lines can radiate out in all directions through a single point."
    },
    {
        "id": 9,
        "challenge": 1,
        "question": "A crease formed by folding a sheet of paper tightly represents:",
        "options": [
            "A ray",
            "A line segment",
            "An angle vertex only",
            "A circle"
        ],
        "correct": 1,
        "explanation": "The straight crease terminating at the paper's edges is a physical model of a line segment."
    },
    {
        "id": 10,
        "challenge": 1,
        "question": "If points A, B, and C lie in that order on a single line, what is the intersection of Ray BA and Ray BC?",
        "options": [
            "Line AC",
            "Only the initial point B",
            "Segment AC",
            "An empty set"
        ],
        "correct": 1,
        "explanation": "Ray BA goes left from B and Ray BC goes right from B; their only common point is vertex B."
    },
    {
        "id": 11,
        "challenge": 2,
        "question": "What geometric figure is formed by two rays sharing a common initial point?",
        "options": [
            "A line segment",
            "An angle",
            "A triangle",
            "A parallel pair"
        ],
        "correct": 1,
        "explanation": "An angle is formed when two rays originate from a common starting point called the vertex."
    },
    {
        "id": 12,
        "challenge": 2,
        "question": "In the angle denoted as ∠XYZ, what are the names of the two arms?",
        "options": [
            "Ray XY and Ray ZY",
            "Ray YX and Ray YZ",
            "Ray XZ and Ray ZX",
            "Line segment XZ"
        ],
        "correct": 1,
        "explanation": "The arms originate from vertex Y, so they are Ray YX and Ray YZ."
    },
    {
        "id": 13,
        "challenge": 2,
        "question": "If you double the length of the lines drawn to represent the arms of an angle, what happens to the size of the angle?",
        "options": [
            "It doubles",
            "It halves",
            "It remains unchanged",
            "It becomes 90 degrees"
        ],
        "correct": 2,
        "explanation": "Angle size depends purely on the degree of rotation between the rays, completely independent of arm length."
    },
    {
        "id": 14,
        "challenge": 2,
        "question": "Which method compares two angles by tracing one onto paper and placing it over the other?",
        "options": [
            "Superimposition",
            "Extrapolation",
            "Trigonometry",
            "Bisecting"
        ],
        "correct": 0,
        "explanation": "Superimposition is placing one geometric figure directly over another to compare shape and size."
    },
    {
        "id": 15,
        "challenge": 2,
        "question": "When superimposing angle ∠1 onto angle ∠2, what must be aligned?",
        "options": [
            "Only the arrowheads",
            "The vertices and one pair of corresponding arms",
            "The midpoints of the rays",
            "The outer boundary of the paper"
        ],
        "correct": 1,
        "explanation": "Superimposition requires matching the vertex and one arm so that the relative position of the second arm can be checked."
    },
    {
        "id": 16,
        "challenge": 2,
        "question": "In the circular arc template comparison method, why must both arcs have the same radius?",
        "options": [
            "To ensure the paper does not tear",
            "Because arc length is proportional to angle only when the radius is held constant",
            "Because protractors only have one radius",
            "To make the drawing look neat"
        ],
        "correct": 1,
        "explanation": "At equal radius, arc length is directly proportional to angle opening. Changing the radius would distort comparison."
    },
    {
        "id": 17,
        "challenge": 2,
        "question": "In the straw slit-passing experiment, why could a 60° straw angle not pass into a 40° slit even when trimmed very short?",
        "options": [
            "Because straws are too soft",
            "Because its angle of opening (60°) was wider than the slit opening (40°)",
            "Because the slit was too long",
            "Because of air resistance"
        ],
        "correct": 1,
        "explanation": "Passing through an angular slit depends on angle opening; an opening of 60° cannot clear a 40° aperture."
    },
    {
        "id": 18,
        "challenge": 2,
        "question": "Which of the following points lies in the interior of ∠ABC?",
        "options": [
            "A point lying on ray BA",
            "A point lying between the two arms inside the opening",
            "A point located behind vertex B",
            "A point on ray BC"
        ],
        "correct": 1,
        "explanation": "The interior of an angle consists of all points situated between the two branching arms."
    },
    {
        "id": 19,
        "challenge": 2,
        "question": "If angle ∠DEF is equal in size to angle ∠PQR, they are described geometrically as:",
        "options": [
            "Perpendicular",
            "Congruent (equal)",
            "Supplementary",
            "Collinear"
        ],
        "correct": 1,
        "explanation": "Angles having the identical measure of rotation are called congruent or equal angles."
    },
    {
        "id": 20,
        "challenge": 2,
        "question": "Can an angle be named simply by its vertex letter, such as ∠B?",
        "options": [
            "Never, it is strictly forbidden",
            "Yes, provided only one single angle exists at vertex B so there is no ambiguity",
            "Only if it is a right angle",
            "Only if the arms are horizontal"
        ],
        "correct": 1,
        "explanation": "A single letter naming (e.g. ∠B) is acceptable whenever only one angle exists at that vertex."
    },
    {
        "id": 21,
        "challenge": 3,
        "question": "How many degrees are there in one complete full rotation?",
        "options": [
            "100°",
            "180°",
            "360°",
            "720°"
        ],
        "correct": 2,
        "explanation": "One full circular turn is divided into exactly 360 degrees."
    },
    {
        "id": 22,
        "challenge": 3,
        "question": "How many degrees does a right angle measure?",
        "options": [
            "45°",
            "90°",
            "180°",
            "360°"
        ],
        "correct": 1,
        "explanation": "A right angle is exactly one quarter of a full turn: 360° ÷ 4 = 90°."
    },
    {
        "id": 23,
        "challenge": 3,
        "question": "Why did ancient astronomers and mathematicians select 360 parts for a circle?",
        "options": [
            "It matches the approximate 365-day solar calendar and has 24 whole-number factors",
            "It was the largest number known at the time",
            "It is a prime number",
            "To make angles harder to calculate"
        ],
        "correct": 0,
        "explanation": "360 is close to the solar year and is highly composite, dividing evenly by 2, 3, 4, 5, 6, 8, 9, 10, 12, etc."
    },
    {
        "id": 24,
        "challenge": 3,
        "question": "What is the degree measure of a straight angle?",
        "options": [
            "90°",
            "180°",
            "270°",
            "360°"
        ],
        "correct": 1,
        "explanation": "A straight angle is a half-turn: 360° ÷ 2 = 180°."
    },
    {
        "id": 25,
        "challenge": 3,
        "question": "On a standard protractor, what do the inner and outer scales represent?",
        "options": [
            "One scale measures clockwise and the other counter-clockwise, each from 0° to 180°",
            "One scale is metric and the other is imperial",
            "One scale is for acute angles and the other is for reflex angles",
            "One scale is for children and the other for adults"
        ],
        "correct": 0,
        "explanation": "The dual scales allow measuring from 0° whether the base arm points to the right or to the left."
    },
    {
        "id": 26,
        "challenge": 3,
        "question": "If the base ray of an angle points to the right along the 0° mark of the inner scale, which scale should you read?",
        "options": [
            "The outer scale starting at 180°",
            "The inner scale starting at 0°",
            "Either scale randomly",
            "Subtract 90 from the reading"
        ],
        "correct": 1,
        "explanation": "Always read the scale that begins at 0° along your baseline reference ray."
    },
    {
        "id": 27,
        "challenge": 3,
        "question": "When folding a paper circle in half (180°) and then in half again, the resulting corner crease measures:",
        "options": [
            "45°",
            "60°",
            "90°",
            "120°"
        ],
        "correct": 2,
        "explanation": "Halving 180° produces 90°, which is a right angle."
    },
    {
        "id": 28,
        "challenge": 3,
        "question": "What is the measure of the angle formed when folding a 90° corner crease in half once more?",
        "options": [
            "30°",
            "45°",
            "60°",
            "75°"
        ],
        "correct": 1,
        "explanation": "Halving 90° gives 90° ÷ 2 = 45°."
    },
    {
        "id": 29,
        "challenge": 3,
        "question": "What symbol is used in diagrams to denote perpendicular lines meeting at a right angle?",
        "options": [
            "A small circle at the vertex",
            "A small square corner symbol ∟",
            "A double arrow",
            "A dashed wavy line"
        ],
        "correct": 1,
        "explanation": "A small square box in the corner denotes a right angle (90°)."
    },
    {
        "id": 30,
        "challenge": 3,
        "question": "When constructing an angle of 35° using a protractor, what is the first step?",
        "options": [
            "Place a dot at 35° on blank paper",
            "Draw a straight base reference ray using a ruler",
            "Cut the paper into a circle",
            "Draw an arc with a compass"
        ],
        "correct": 1,
        "explanation": "Step 1 is always drawing a clean straight base reference ray with a designated vertex point."
    },
    {
        "id": 31,
        "challenge": 4,
        "question": "An angle measuring 72° is classified as:",
        "options": [
            "An acute angle (since 0° < 72° < 90°)",
            "A right angle",
            "An obtuse angle",
            "A reflex angle"
        ],
        "correct": 0,
        "explanation": "Any angle between 0° and 90° is an acute angle."
    },
    {
        "id": 32,
        "challenge": 4,
        "question": "An angle measuring 115° is classified as:",
        "options": [
            "An acute angle",
            "A right angle",
            "An obtuse angle (since 90° < 115° < 180°)",
            "A reflex angle"
        ],
        "correct": 2,
        "explanation": "Any angle between 90° and 180° is an obtuse angle."
    },
    {
        "id": 33,
        "challenge": 4,
        "question": "What is an angle measuring greater than 180° and less than 360° called?",
        "options": [
            "An obtuse angle",
            "A straight angle",
            "A reflex angle",
            "A supplementary angle"
        ],
        "correct": 2,
        "explanation": "Angles strictly between 180° and 360° are classified as reflex angles."
    },
    {
        "id": 34,
        "challenge": 4,
        "question": "At 3:00 on an analog clock, the minute hand and hour hand form an angle of:",
        "options": [
            "45°",
            "60°",
            "90° (a right angle)",
            "180°"
        ],
        "correct": 2,
        "explanation": "At 3:00, the hands are 3 hours apart: 3 × (360° ÷ 12) = 3 × 30° = 90°."
    },
    {
        "id": 35,
        "challenge": 4,
        "question": "At 6:00 on an analog clock, the hands point in opposite directions forming:",
        "options": [
            "A right angle",
            "A straight angle of 180°",
            "An acute angle",
            "A reflex angle"
        ],
        "correct": 1,
        "explanation": "At 6:00, the hands form a straight line: 6 × 30° = 180° (a straight angle)."
    },
    {
        "id": 36,
        "challenge": 4,
        "question": "If the inner angle between two rays is an obtuse angle of 110°, what is the measure of the outer reflex angle?",
        "options": [
            "70°",
            "180°",
            "250° (since 360° − 110° = 250°)",
            "290°"
        ],
        "correct": 2,
        "explanation": "The inner angle and outer reflex angle sum to 360°: 360° − 110° = 250°."
    },
    {
        "id": 37,
        "challenge": 4,
        "question": "Which of the following is true regarding acute, right, and obtuse angles?",
        "options": [
            "Acute angle < Right angle < Obtuse angle < Straight angle",
            "Right angle < Acute angle < Obtuse angle",
            "Obtuse angle < Acute angle < Straight angle",
            "Straight angle < Obtuse angle < Right angle"
        ],
        "correct": 0,
        "explanation": "In order of measure: Acute (<90°) < Right (90°) < Obtuse (90°–180°) < Straight (180°)."
    },
    {
        "id": 38,
        "challenge": 4,
        "question": "How many degrees does the hour hand of a clock turn through in 4 hours?",
        "options": [
            "90°",
            "120° (4 × 30° = 120°)",
            "150°",
            "180°"
        ],
        "correct": 1,
        "explanation": "Each hour on a clock face corresponds to 360° ÷ 12 = 30°; thus 4 hours = 4 × 30° = 120°."
    },
    {
        "id": 39,
        "challenge": 4,
        "question": "An angle measuring exactly 90.1° is technically classified as:",
        "options": [
            "An acute angle",
            "A right angle",
            "An obtuse angle (since it exceeds 90°)",
            "A reflex angle"
        ],
        "correct": 2,
        "explanation": "Because 90.1° is strictly greater than 90° and less than 180°, it is classified as obtuse."
    },
    {
        "id": 40,
        "challenge": 4,
        "question": "What is the measure of the angle formed when you turn from facing North to facing South-West clockwise?",
        "options": [
            "135° (obtuse angle)",
            "180° (straight angle)",
            "225° (reflex angle)",
            "270°"
        ],
        "correct": 2,
        "explanation": "North (0°) to East (90°) to South (180°) to South-West (180° + 45° = 225°), which is a reflex angle!"
    }
]
