SLIDES_DATA = [
    {
        "id": "slide-1",
        "slide_num": 1,
        "section": "8.0",
        "title": "Working with Fractions: Everyday Quantities & Visual Foundations",
        "badge": "Foundations",
        "narration": "Greetings, keen minds of mathematics! I am Acharya Brahmagupta. In everyday life, whole numbers alone cannot measure the journey of the wind, the share of sweet milk, or the speed of a chariot. We need fractions: parts of a harmonious whole!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>What is a Fraction?</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    A fraction $\\frac{a}{b}$ represents $a$ equal parts out of a whole that has been partitioned into $b$ equal parts.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold text-sm block mb-1'>Numerator ($a$)</span>\n                        <p class='text-slate-300'>The counting number above the bar: tells how many equal parts are chosen or considered.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold text-sm block mb-1'>Denominator ($b$)</span>\n                        <p class='text-slate-300'>The dividing number below the bar: tells how many total equal parts make up one whole ($b \\ne 0$).</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold text-sm block mb-1'>Types of Fractions</span>\n                        <p class='text-slate-300'><strong>Proper:</strong> $a < b$ (less than 1).<br><strong>Improper:</strong> $a \\ge b$ (1 or more).<br><strong>Mixed:</strong> Whole + fraction ($2\\frac{1}{3}$).</p>\n                    </div>\n                </div>\n                <p class='text-slate-400 text-xs italic mt-2'>\n                    💡 Historical Note: In ancient India, fractions were written with the numerator directly above the denominator without a horizontal bar (e.g., $3$ over $4$ meant $\\frac{3}{4}$). The dividing bar was later introduced by Moroccan mathematician al-Hass\u0101r.\n                </p>\n            </div>\n        ",
        "sim_id": "sim-fraction-visualizer",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "In the fraction $\\frac{5}{8}$, what does the denominator 8 signify?",
                "options": [
                    "5 parts are taken",
                    "The whole is divided into 8 equal parts",
                    "The fraction equals 8 wholes",
                    "The fraction is improper"
                ],
                "correct": 1,
                "explanation": "The denominator indicates the total number of equal parts into which the unit whole has been partitioned."
            },
            {
                "id": "cp1_2",
                "question": "Which of the following is an improper fraction?",
                "options": [
                    "$\\frac{3}{5}$",
                    "$\\frac{7}{8}$",
                    "$\\frac{9}{4}$",
                    "$\\frac{1}{2}$"
                ],
                "correct": 2,
                "explanation": "In an improper fraction, the numerator is greater than or equal to the denominator (here, 9 > 4)."
            }
        ]
    },
    {
        "id": "slide-2",
        "slide_num": 2,
        "section": "8.1",
        "title": "Multiplying a Fraction by a Whole Number: Repeated Addition",
        "badge": "Multiplication Basics",
        "narration": "Just as three times four means adding four three times, three times two-sevenths means making three jumps of two-sevenths along our number line! Multiplication by a whole number scales only the numerator.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Repeated Addition of Fractions</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Multiplying a whole number $n$ by a fraction $\\frac{a}{b}$ is equivalent to repeatedly adding $\\frac{a}{b}$ a total of $n$ times:\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base tracking-wide font-mono'>\n                        $$n \\times \\frac{a}{b} = \\underbrace{\\frac{a}{b} + \\frac{a}{b} + \\dots + \\frac{a}{b}}_{n \\text{ times}} = \\frac{n \\times a}{b}$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>Concrete Example:</h5>\n                        <p class='text-slate-300'>$4 \\times \\frac{2}{9} = \\frac{2}{9} + \\frac{2}{9} + \\frac{2}{9} + \\frac{2}{9} = \\frac{4 \\times 2}{9} = \\frac{8}{9}$.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <h5 class='text-emerald-300 font-bold mb-1'>Converting to Mixed Fractions:</h5>\n                        <p class='text-slate-300'>If the product is improper, convert: $5 \\times \\frac{3}{4} = \\frac{15}{4} = 3\\frac{3}{4}$.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-repeated-addition",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "What is the product of $3 \\times \\frac{2}{5}$?",
                "options": [
                    "$\\frac{6}{15}$",
                    "$\\frac{6}{5}$",
                    "$\\frac{5}{6}$",
                    "$\\frac{2}{15}$"
                ],
                "correct": 1,
                "explanation": "Multiply the whole number by the numerator: 3 \u00d7 2 / 5 = 6/5 = 1 1/5."
            },
            {
                "id": "cp2_2",
                "question": "Why does multiplying a fraction by a whole number leave the denominator unchanged?",
                "options": [
                    "Because denominators cannot change",
                    "Because the size of each slice remains the same, only the number of slices increases",
                    "Because denominators are zero",
                    "Because whole numbers have no value"
                ],
                "correct": 1,
                "explanation": "The denominator defines the partition size of each piece; multiplying by a whole number merely takes more of those same-sized pieces."
            }
        ]
    },
    {
        "id": "slide-3",
        "slide_num": 3,
        "section": "8.1",
        "title": "Fraction of a Fraction: The 'Of' Operator",
        "badge": "Fraction of a Quantity",
        "narration": "What does it mean to take half of three-quarters? In mathematics, the word 'of' represents multiplication. Taking a fraction of another fraction subdivides existing portions into even finer pieces!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Connecting 'Of' with Multiplication</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    When we say $\\frac{1}{2}$ <em>of</em> $\\frac{3}{4}$, we first obtain $\\frac{3}{4}$ of a whole, and then cut that shaded portion into $2$ equal parts and keep $1$ of those parts.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\frac{1}{2} \\text{ of } \\frac{3}{4} = \\frac{1}{2} \\times \\frac{3}{4} = \\frac{1 \\times 3}{2 \\times 4} = \\frac{3}{8}$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>Two-Step Visual Sub-partitioning:</span>\n                        <p class='text-slate-300'>Step 1: Divide the unit into 4 columns, shade 3.<br>Step 2: Cut across horizontally into 2 rows, take the top half of the 3 columns &rarr; exactly 3 out of 8 total cells!</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Real-World Parallel:</span>\n                        <p class='text-slate-300'>If a bottle has $\\frac{3}{4}$ liter of juice, and you drink $\\frac{1}{2}$ of it, you drink $\\frac{3}{8}$ liter.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-fraction-of-fraction",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "What is $\\frac{1}{3}$ of $\\frac{3}{5}$?",
                "options": [
                    "$\\frac{1}{5}$",
                    "$\\frac{3}{15}$ (which simplifies to $\\frac{1}{5}$)",
                    "$\\frac{4}{8}$",
                    "Both A and B are correct"
                ],
                "correct": 3,
                "explanation": "1/3 \u00d7 3/5 = 3/15, which reduces by dividing numerator and denominator by 3 to 1/5. Thus both A and B are correct."
            },
            {
                "id": "cp3_2",
                "question": "In fraction arithmetic, what operation does the word 'of' represent?",
                "options": [
                    "Addition",
                    "Subtraction",
                    "Multiplication",
                    "Division"
                ],
                "correct": 2,
                "explanation": "In mathematical phrasing, 'fraction of a quantity' translates directly to multiplication."
            }
        ]
    },
    {
        "id": "slide-4",
        "slide_num": 4,
        "section": "8.1",
        "title": "The Unit Square Area Model for Fraction Multiplication",
        "badge": "Geometric Proof",
        "narration": "Geometry gives us the clearest window into fraction multiplication! Imagine a unit square of area one. Split its width into equal columns and its height into equal rows. The overlapping rectangle reveals the product with crystal clarity.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Area of a Rectangle = Length \u00d7 Breadth</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Consider a unit square with side length $1$ unit (Area $= 1 \\times 1 = 1$). Inside it, construct a rectangle with side lengths $\\frac{a}{b}$ and $\\frac{c}{d}$.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>1. Total Grid Cells</span>\n                        <p class='text-slate-300'>The unit square is partitioned into $b$ columns and $d$ rows, creating $b \\times d$ identical micro-rectangles.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>2. Overlap Shaded Cells</span>\n                        <p class='text-slate-300'>The rectangle spans $a$ columns and $c$ rows, covering exactly $a \\times c$ micro-rectangles.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>3. Geometric Formula</span>\n                        <p class='text-slate-300'>$$\\text{Area} = \\frac{\\text{Shaded Cells}}{\\text{Total Cells}} = \\frac{a \\times c}{b \\times d}$$</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-unit-square-grid",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "If a unit square is divided into 5 vertical columns and 4 horizontal rows, how many total grid cells are formed?",
                "options": [
                    "9",
                    "20",
                    "25",
                    "16"
                ],
                "correct": 1,
                "explanation": "5 columns \u00d7 4 rows = 20 equal grid cells in total."
            },
            {
                "id": "cp4_2",
                "question": "If 3 out of 5 columns and 2 out of 4 rows are shaded, what fraction of the unit square is double-shaded?",
                "options": [
                    "$\\frac{5}{9}$",
                    "$\\frac{6}{20} = \\frac{3}{10}$",
                    "$\\frac{1}{2}$",
                    "$\\frac{6}{9}$"
                ],
                "correct": 1,
                "explanation": "Overlap cells = 3 \u00d7 2 = 6 cells out of 20 total cells, giving 6/20 = 3/10."
            }
        ]
    },
    {
        "id": "slide-5",
        "slide_num": 5,
        "section": "8.1",
        "title": "Brahmagupta's Product Law: Universal Fraction Multiplication",
        "badge": "Classical Theorem",
        "narration": "In the year 628 of the Common Era, in his great treatise Br\u0101hmasphu\u1e6dasiddh\u0101nta, I codified the universal law for multiplying fractions: multiply the numerators together, and multiply the denominators together!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Master Multiplication Rule</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    To multiply any two fractions, multiply their numerators to get the product's numerator, and multiply their denominators to get the product's denominator.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-lg font-mono'>\n                        $$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d}$$\n                    </span>\n                </div>\n                <div class='p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl text-xs text-amber-200 my-2'>\n                    <strong>Original Sanskrit Rule from Br\u0101hmasphu\u1e6dasiddh\u0101nta (Ch. 12, v. 3):</strong><br>\n                    <em>\"r\u016bp\u0101rdh\u0101dipratyayena vadha\u1e25 sa\u1e43gu\u1e47ya h\u0101ra-h\u0101r\u0101bhy\u0101\u1e43 | chinnayo\u1e25 chhedabadha\u1e25 sy\u0101t...\"</em><br>\n                    <span class='text-slate-300'>The product of the numerators divided by the product of the denominators is the multiplication of two fractions.</span>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-brahmagupta-product",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "Compute $\\frac{3}{7} \\times \\frac{5}{8}$ using Brahmagupta's formula:",
                "options": [
                    "$\\frac{8}{15}$",
                    "$\\frac{15}{56}$",
                    "$\\frac{24}{35}$",
                    "$\\frac{15}{15}$"
                ],
                "correct": 1,
                "explanation": "Numerator: 3 \u00d7 5 = 15; Denominator: 7 \u00d7 8 = 56. Thus, 15/56."
            },
            {
                "id": "cp5_2",
                "question": "What is the product of $\\frac{4}{9} \\times \\frac{9}{4}$?",
                "options": [
                    "$\\frac{36}{36} = 1$",
                    "$\\frac{16}{81}$",
                    "$\\frac{8}{13}$",
                    "0"
                ],
                "correct": 0,
                "explanation": "(4 \u00d7 9) / (9 \u00d7 4) = 36/36 = 1."
            }
        ]
    },
    {
        "id": "slide-6",
        "slide_num": 6,
        "section": "8.1",
        "title": "Simplifying Terms: The Art of Cross-Cancelling",
        "badge": "Efficient Computation",
        "narration": "A wise mathematician simplifies before calculating! Rather than multiplying large numbers into monstrous fractions and then struggling to reduce them, divide out common factors across numerators and denominators beforehand.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Cross-Cancelling Strategy</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Because multiplication is associative and commutative, any factor in any numerator can cancel with any common factor in any denominator before performing the multiplication.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-rose-950/30 border border-rose-500/30 rounded-xl'>\n                        <span class='text-rose-300 font-bold block mb-1'>The Clumsy Way (Multiply First):</span>\n                        <p class='text-slate-300'>$$\\frac{14}{25} \\times \\frac{15}{28} = \\frac{14 \\times 15}{25 \\times 28} = \\frac{210}{700}$$ Now you must divide 210 and 700 by 70 to get $\\frac{3}{10}$. Tedious!</p>\n                    </div>\n                    <div class='p-3 bg-emerald-950/30 border border-emerald-500/30 rounded-xl'>\n                        <span class='text-emerald-300 font-bold block mb-1'>The Master Way (Cross-Cancel First):</span>\n                        <p class='text-slate-300'>Cancel 14 and 28 by $14$ &rarr; gives $1$ and $2$.<br>Cancel 15 and 25 by $5$ &rarr; gives $3$ and $5$.<br>$$\\frac{1 \\times 3}{5 \\times 2} = \\frac{3}{10}$$ Instant and error-free!</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-cross-cancelling",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "Simplify $\\frac{5}{12} \\times \\frac{8}{15}$ by cross-cancelling:",
                "options": [
                    "$\\frac{40}{180}$",
                    "$\\frac{2}{9}$",
                    "$\\frac{1}{3}$",
                    "$\\frac{5}{8}$"
                ],
                "correct": 1,
                "explanation": "Divide 5 and 15 by 5 (gives 1 and 3). Divide 8 and 12 by 4 (gives 2 and 3). Product = (1 \u00d7 2) / (3 \u00d7 3) = 2/9."
            },
            {
                "id": "cp6_2",
                "question": "What is the Greatest Common Factor of 14 and 28 used to cross-cancel in $\\frac{14}{25} \\times \\frac{15}{28}$?",
                "options": [
                    "2",
                    "7",
                    "14",
                    "28"
                ],
                "correct": 2,
                "explanation": "14 is a direct divisor of both 14 and 28 (14/14 = 1, 28/14 = 2)."
            }
        ]
    },
    {
        "id": "slide-7",
        "slide_num": 7,
        "section": "8.1",
        "title": "Value of the Product: Does Multiplication Always Magnify?",
        "badge": "Size Behavior",
        "narration": "In childhood, we learn that multiplication makes numbers bigger. But in the land of fractions, this rule is shattered! When you multiply by a proper fraction less than one, the product shrinks!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>How Product Size Compares with Factors</h4>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Proper \u00d7 Proper</span>\n                        <p class='text-slate-300 mb-1'>Product is <strong>smaller</strong> than BOTH factors!</p>\n                        <p class='text-slate-400 font-mono'>$\\frac{2}{3} \\times \\frac{4}{5} = \\frac{8}{15}$<br>($\\frac{8}{15} < \\frac{2}{3}$ and $\\frac{8}{15} < \\frac{4}{5}$)</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>Proper \u00d7 Improper</span>\n                        <p class='text-slate-300 mb-1'>Product lies <strong>between</strong> the two factors!</p>\n                        <p class='text-slate-400 font-mono'>$\\frac{2}{3} \\times \\frac{5}{2} = \\frac{5}{3}$<br>($\\frac{2}{3} < \\frac{5}{3} < \\frac{5}{2}$)</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Improper \u00d7 Improper</span>\n                        <p class='text-slate-300 mb-1'>Product is <strong>greater</strong> than BOTH factors!</p>\n                        <p class='text-slate-400 font-mono'>$\\frac{3}{2} \\times \\frac{5}{4} = \\frac{15}{8}$<br>($\\frac{15}{8} > \\frac{3}{2}$ and $\\frac{15}{8} > \\frac{5}{4}$)</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-product-size-comparator",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "Which statement is true for the product $\\frac{3}{5} \\times \\frac{4}{7} = \\frac{12}{35}$?",
                "options": [
                    "It is greater than 3/5",
                    "It is smaller than both 3/5 and 4/7",
                    "It equals 1",
                    "It is greater than 1"
                ],
                "correct": 1,
                "explanation": "Because both 3/5 and 4/7 are proper fractions (less than 1), their product is strictly smaller than both factors."
            },
            {
                "id": "cp7_2",
                "question": "If you multiply a number by $\\frac{5}{3}$, what happens to its magnitude?",
                "options": [
                    "It increases (magnifies)",
                    "It decreases (shrinks)",
                    "It remains the same",
                    "It becomes zero"
                ],
                "correct": 0,
                "explanation": "Because 5/3 is an improper fraction greater than 1, multiplying by it scales the number up."
            }
        ]
    },
    {
        "id": "slide-8",
        "slide_num": 8,
        "section": "8.1",
        "title": "Commutativity: Order Does Not Alter the Product",
        "badge": "Algebraic Laws",
        "narration": "Does three-fourths of two-fifths equal two-fifths of three-fourths? Verily! Rotating our rectangular area grid by ninety degrees demonstrates that the order of multiplication never alters the product.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Commutative Property of Fraction Multiplication</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    For any two fractions $\\frac{a}{b}$ and $\\frac{c}{d}$:\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d} = \\frac{c \\times a}{d \\times b} = \\frac{c}{d} \\times \\frac{a}{b}$$\n                    </span>\n                </div>\n                <p class='text-slate-300 text-xs mt-2'>\n                    Since ordinary whole-number multiplication is commutative ($a \\times c = c \\times a$ and $b \\times d = d \\times b$), fraction multiplication inherits this symmetry perfectly.\n                </p>\n            </div>\n        ",
        "sim_id": "sim-commutativity-rotator",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "Does $\\frac{2}{7} \\times \\frac{5}{9} = \\frac{5}{9} \\times \\frac{2}{7}$?",
                "options": [
                    "Yes, by the commutative property",
                    "No, order matters in fractions",
                    "Only if denominators are equal",
                    "Only for proper fractions"
                ],
                "correct": 0,
                "explanation": "Multiplication of fractions is strictly commutative; swapping the order of factors produces the exact same product."
            },
            {
                "id": "cp8_2",
                "question": "Why does a 90\u00b0 rotation of the unit square prove commutativity geometrically?",
                "options": [
                    "It changes the perimeter",
                    "The length and breadth swap roles, but the area of the overlapping rectangle remains unchanged",
                    "It turns a square into a circle",
                    "It cancels the denominator"
                ],
                "correct": 1,
                "explanation": "Rotating 90\u00b0 swaps horizontal and vertical dimensions without changing the total area of the overlapping shaded region."
            }
        ]
    },
    {
        "id": "slide-9",
        "slide_num": 9,
        "section": "8.2",
        "title": "Reciprocals: The Secret of Multiplicative Inverses",
        "badge": "Division Foundation",
        "narration": "To divide fractions, we must first meet the reciprocal! Turn any non-zero fraction upside down, swapping its numerator and denominator. When you multiply a fraction by its reciprocal, they dissolve into the perfect unity of one!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Defining the Reciprocal (Multiplicative Inverse)</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Two non-zero numbers are called <strong>reciprocals</strong> of each other if their product is exactly $1$.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\frac{a}{b} \\times \\frac{b}{a} = \\frac{a \\times b}{b \\times a} = 1$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Proper Fraction</span>\n                        <p class='text-slate-300'>Reciprocal of $\\frac{3}{7}$ is $\\frac{7}{3}$ (an improper fraction $> 1$).</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Whole Number</span>\n                        <p class='text-slate-300'>Since $5 = \\frac{5}{1}$, its reciprocal is $\\frac{1}{5}$.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>\n                        <span class='text-rose-300 font-bold block mb-1'>The Zero Exception</span>\n                        <p class='text-slate-300'><strong>Zero has NO reciprocal!</strong> Division by zero is undefined ($0 \\times \\text{anything} = 0 \\ne 1$).</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-reciprocal-flip",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "What is the reciprocal of the mixed fraction $2\\frac{1}{3}$?",
                "options": [
                    "$2\\frac{3}{1}$",
                    "$\\frac{3}{7}$",
                    "$\\frac{7}{3}$",
                    "$\\frac{1}{2}$"
                ],
                "correct": 1,
                "explanation": "Convert to improper fraction: 2 1/3 = 7/3. Its reciprocal is obtained by flipping: 3/7."
            },
            {
                "id": "cp9_2",
                "question": "Why does the number 0 have no reciprocal?",
                "options": [
                    "Because 0 is negative",
                    "Because no number multiplied by 0 can ever equal 1",
                    "Because 0 is not a fraction",
                    "Because ancient scholars disliked 0"
                ],
                "correct": 1,
                "explanation": "By definition, a number and its reciprocal multiply to 1. But 0 multiplied by any real number is always 0, never 1."
            }
        ]
    },
    {
        "id": "slide-10",
        "slide_num": 10,
        "section": "8.2",
        "title": "Understanding Fraction Division: Slicing & Grouping",
        "badge": "Intuitive Models",
        "narration": "What does dividing by a fraction mean? When we compute three divided by one-half, we are asking: how many half-slices can be carved from three whole flatbreads? Each whole yields two halves, so three wholes give six slices!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Meaning of Division: 'How Many Fit?'</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Division $A \\div B$ asks: <em>\"How many groups of size $B$ are contained in quantity $A$?\"</em>\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$3 \\div \\frac{1}{2} = 3 \\times 2 = 6 \\text{ slices}$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Whole by Unit Fraction:</span>\n                        <p class='text-slate-300'>$4 \\div \\frac{1}{3} = 4 \\times 3 = 12$. Four wholes carved into thirds give 12 pieces.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Fraction by Fraction:</span>\n                        <p class='text-slate-300'>$\\frac{6}{7} \\div \\frac{2}{7} = 3$. How many two-sevenths fit into six-sevenths? Exactly 3 groups!</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-division-grouping",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "How many $\\frac{1}{4}$-meter strips of ribbon can be cut from a 2-meter long ribbon?",
                "options": [
                    "2",
                    "4",
                    "8",
                    "6"
                ],
                "correct": 2,
                "explanation": "2 \u00f7 (1/4) = 2 \u00d7 4 = 8 strips."
            },
            {
                "id": "cp10_2",
                "question": "Evaluate $\\frac{8}{9} \\div \\frac{2}{9}$:",
                "options": [
                    "4",
                    "$\\frac{16}{81}$",
                    "$\\frac{4}{9}$",
                    "2"
                ],
                "correct": 0,
                "explanation": "Since denominators are identical, 8 parts \u00f7 2 parts = 4."
            }
        ]
    },
    {
        "id": "slide-11",
        "slide_num": 11,
        "section": "8.2",
        "title": "Brahmagupta's Division Law: Invert & Multiply!",
        "badge": "Classical Algorithm",
        "narration": "Here is the golden key to fraction division, established in ancient India: division by a fraction is identical to multiplication by its reciprocal! Invert the divisor, and multiply across.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Universal Division Algorithm</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    To divide by any fraction, multiply the dividend by the <strong>reciprocal</strong> of the divisor:\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-lg font-mono'>\n                        $$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c} = \\frac{a \\times d}{b \\times c}$$\n                    </span>\n                </div>\n                <div class='p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl text-xs text-amber-200 my-2'>\n                    <strong>\u015ar\u012bdhar\u0101ch\u0101rya's P\u0101\u1e6d\u012bga\u1e47ita Rule (c. 800 CE):</strong><br>\n                    <em>\"bh\u0101gah\u0101re vipar\u012bte k\u1e5bte sa\u1e43gu\u1e47ya...\"</em><br>\n                    <span class='text-slate-300'>Having inverted the divisor, perform multiplication with the dividend.</span>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-division-inverter",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "Evaluate $\\frac{3}{5} \\div \\frac{2}{7}$:",
                "options": [
                    "$\\frac{6}{35}$",
                    "$\\frac{21}{10}$",
                    "$\\frac{10}{21}$",
                    "$\\frac{5}{9}$"
                ],
                "correct": 1,
                "explanation": "Invert the divisor 2/7 to 7/2 and multiply: 3/5 \u00d7 7/2 = 21/10 = 2 1/10."
            },
            {
                "id": "cp11_2",
                "question": "Which fraction must be inverted when computing $\\frac{4}{9} \\div \\frac{5}{6}$?",
                "options": [
                    "$\\frac{4}{9}$ (the dividend)",
                    "$\\frac{5}{6}$ (the divisor)",
                    "Both fractions",
                    "Neither fraction"
                ],
                "correct": 1,
                "explanation": "Only the divisor (the fraction doing the dividing, here 5/6) is inverted."
            }
        ]
    },
    {
        "id": "slide-12",
        "slide_num": 12,
        "section": "8.2",
        "title": "Behavior of the Quotient: When Division Magnifies",
        "badge": "Quotient Dynamics",
        "narration": "In whole-number arithmetic, division always produces a quotient smaller than or equal to the dividend. But when you divide by a proper fraction less than one, the quotient surges larger than the dividend!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>How Quotient Compares to Dividend</h4>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Dividing by a Proper Fraction ($< 1$):</span>\n                        <p class='text-slate-300 mb-1'>The quotient is <strong>greater</strong> than the dividend!</p>\n                        <p class='text-slate-400 font-mono'>$6 \\div \\frac{1}{3} = 6 \\times 3 = 18$ &nbsp;($18 > 6$)<br>$\\frac{2}{5} \\div \\frac{1}{2} = \\frac{2}{5} \\times 2 = \\frac{4}{5}$ &nbsp;($\\frac{4}{5} > \\frac{2}{5}$)</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>\n                        <span class='text-rose-300 font-bold block mb-1'>Dividing by an Improper Fraction ($> 1$):</span>\n                        <p class='text-slate-300 mb-1'>The quotient is <strong>smaller</strong> than the dividend!</p>\n                        <p class='text-slate-400 font-mono'>$6 \\div \\frac{3}{2} = 6 \\times \\frac{2}{3} = 4$ &nbsp;($4 < 6$)</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-quotient-magnifier",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "Is $10 \\div \\frac{2}{5}$ greater than or less than 10?",
                "options": [
                    "Greater than 10 (it equals 25)",
                    "Less than 10 (it equals 4)",
                    "Equal to 10",
                    "Zero"
                ],
                "correct": 0,
                "explanation": "10 \u00f7 2/5 = 10 \u00d7 5/2 = 25, which is much greater than 10 because divisor 2/5 < 1."
            },
            {
                "id": "cp12_2",
                "question": "Under what condition is the quotient of $A \\div B$ strictly greater than $A$ (where $A > 0$)?",
                "options": [
                    "When $B > 1$",
                    "When $0 < B < 1$ (proper fraction divisor)",
                    "When $B = 1$",
                    "Never"
                ],
                "correct": 1,
                "explanation": "Dividing by a positive fraction strictly less than 1 always produces a quotient larger than the original dividend."
            }
        ]
    },
    {
        "id": "slide-13",
        "slide_num": 13,
        "section": "8.3",
        "title": "Practical Word Problems: Milk Sharing & Speed Rates",
        "badge": "Everyday Applications",
        "narration": "Let us take fractions into our markets and travels! Whether pouring measured portions of milk into cups or calculating the uniform speed of a bullock cart over a fractional time, fraction arithmetic is our everyday compass.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Everyday Rates & Fractional Sharing</h4>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>1. Milk Sharing Problem:</h5>\n                        <p class='text-slate-300'>A vessel contains $3\\frac{1}{2}$ liters of milk. If each cup holds $\\frac{1}{4}$ liter, how many full cups can be poured?<br>\n                        $$\\text{Cups} = 3\\frac{1}{2} \\div \\frac{1}{4} = \\frac{7}{2} \\times \\frac{4}{1} = \\frac{28}{2} = 14 \\text{ cups}$$</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <h5 class='text-amber-300 font-bold mb-1'>2. Speed & Distance Rate:</h5>\n                        <p class='text-slate-300'>A traveler covers $32\\frac{1}{2}$ km in $2\\frac{1}{2}$ hours. What is the average speed?<br>\n                        $$\\text{Speed} = \\frac{65}{2} \\div \\frac{5}{2} = \\frac{65}{2} \\times \\frac{2}{5} = 13 \\text{ km/h}$$</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-milk-sharing-speed",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "How many $\\frac{3}{4}$-liter bottles can be filled from 6 liters of water?",
                "options": [
                    "4",
                    "8",
                    "6",
                    "18"
                ],
                "correct": 1,
                "explanation": "6 \u00f7 (3/4) = 6 \u00d7 (4/3) = 24 / 3 = 8 bottles."
            },
            {
                "id": "cp13_2",
                "question": "If a car travels $105$ km using $3\\frac{1}{2}$ liters of fuel, how many km does it travel per liter?",
                "options": [
                    "30 km",
                    "35 km",
                    "25 km",
                    "40 km"
                ],
                "correct": 0,
                "explanation": "105 \u00f7 (7/2) = 105 \u00d7 (2/7) = 15 \u00d7 2 = 30 km/liter."
            }
        ]
    },
    {
        "id": "slide-14",
        "slide_num": 14,
        "section": "8.3",
        "title": "Sacred Geometry: Fractional Bricks of the \u015aulbas\u016btras",
        "badge": "Vedic Architecture",
        "narration": "Over two thousand five hundred years ago, in the Baudhayana and Apastamba \u015aulbas\u016btras, Vedic architects designed complex altars using custom bricks shaped to fractional dimensions: half-bricks, quarter-bricks, and eighth-bricks!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Fractional Paving of Fire Altars (Agni-chiti)</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    The *\u015ayena-chiti* (Falcon Altar) required an exact prescribed area of $7\\frac{1}{2}$ square *puru\u1e63as*, constructed across 5 layered courses of precisely 200 bricks each.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>Ardhe\u1e63\u1e6dak\u0101 (Half-Brick)</span>\n                        <p class='text-slate-300'>Area $= \\frac{1}{2}$ unit. Two half-bricks combine to replace one standard unit brick.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>P\u0101de\u1e63\u1e6dak\u0101 (Quarter-Brick)</span>\n                        <p class='text-slate-300'>Area $= \\frac{1}{4}$ unit. Four quarter-bricks pave the area of one full brick.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>A\u1e63\u1e6dam\u012b (Eighth-Brick)</span>\n                        <p class='text-slate-300'>Area $= \\frac{1}{8}$ unit. Used for triangular wing tips and beak detailing.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-sulbasutra-bricks",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "How many quarter-bricks (p\u0101de\u1e63\u1e6dak\u0101) are required to pave an altar area equal to $3\\frac{1}{2}$ full bricks?",
                "options": [
                    "7",
                    "14",
                    "12",
                    "16"
                ],
                "correct": 1,
                "explanation": "3 1/2 \u00f7 (1/4) = (7/2) \u00d7 4 = 14 quarter-bricks."
            },
            {
                "id": "cp14_2",
                "question": "If an altar section uses 6 half-bricks and 8 quarter-bricks, what is the total area in terms of full bricks?",
                "options": [
                    "3 bricks",
                    "4 bricks",
                    "5 bricks",
                    "6 bricks"
                ],
                "correct": 2,
                "explanation": "6 \u00d7 (1/2) = 3 full bricks; 8 \u00d7 (1/4) = 2 full bricks; Total = 3 + 2 = 5 full bricks."
            }
        ]
    },
    {
        "id": "slide-15",
        "slide_num": 15,
        "section": "8.3",
        "title": "The Cistern-Filling Fountain of P\u1e5bth\u016bdakasv\u0101m\u012b",
        "badge": "Harmonic Rates",
        "narration": "In the 9th century, the scholar Chaturveda P\u1e5bth\u016bdakasv\u0101m\u012b gave a celebrated problem: four fountains flow into a reservoir with different fractional filling rates. When all four flow together, how quickly will the reservoir fill?",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Harmonic Addition of Work Rates</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    If Fountain 1 fills a tank in $\\frac{1}{2}$ day, Fountain 2 in $\\frac{1}{3}$ day, and Fountain 3 in $\\frac{1}{4}$ day:\n                </p>\n                <div class='space-y-2 text-xs'>\n                    <div class='p-2 bg-slate-800/80 rounded border border-cyan-500/30'>\n                        <strong>Step 1 (Find rates per day by taking reciprocals):</strong><br>\n                        \u2022 Rate 1 = $1 \\div \\frac{1}{2} = 2$ tanks per day.<br>\n                        \u2022 Rate 2 = $1 \\div \\frac{1}{3} = 3$ tanks per day.<br>\n                        \u2022 Rate 3 = $1 \\div \\frac{1}{4} = 4$ tanks per day.\n                    </div>\n                    <div class='p-2 bg-slate-800/80 rounded border border-emerald-500/30'>\n                        <strong>Step 2 (Combine flow rates):</strong><br>\n                        Combined Rate = $2 + 3 + 4 = 9$ tanks per day.\n                    </div>\n                    <div class='p-2 bg-slate-800/80 rounded border border-amber-500/30'>\n                        <strong>Step 3 (Calculate time by taking reciprocal of combined rate):</strong><br>\n                        $$\\text{Total Time} = 1 \\div 9 = \\frac{1}{9} \\text{ of a day!}$$\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-cistern-fountain",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "If Pipe A fills a tank in 2 hours and Pipe B fills it in 3 hours, what fraction of the tank do they fill together in 1 hour?",
                "options": [
                    "$\\frac{5}{6}$",
                    "$\\frac{1}{5}$",
                    "$\\frac{2}{3}$",
                    "$\\frac{1}{6}$"
                ],
                "correct": 0,
                "explanation": "Rate A = 1/2 tank/hr, Rate B = 1/3 tank/hr. Combined = 1/2 + 1/3 = 3/6 + 2/6 = 5/6 of the tank per hour."
            },
            {
                "id": "cp15_2",
                "question": "Continuing the above problem, how many hours will Pipe A and Pipe B take to completely fill the tank together?",
                "options": [
                    "$\\frac{5}{6}$ hours",
                    "$1\\frac{1}{5}$ hours ($\\frac{6}{5}$ hours)",
                    "5 hours",
                    "2.5 hours"
                ],
                "correct": 1,
                "explanation": "Time = 1 \u00f7 (5/6) = 6/5 = 1 1/5 hours (or 1 hour 12 minutes)."
            }
        ]
    },
    {
        "id": "slide-16",
        "slide_num": 16,
        "section": "8.3",
        "title": "Bh\u0101skar\u0101ch\u0101rya's L\u012bl\u0101vat\u012b & The Global Legacy",
        "badge": "Heritage & Synthesis",
        "narration": "In 1150 CE, Bh\u0101skar\u0101ch\u0101rya composed his immortal masterpiece L\u012bl\u0101vat\u012b, framing profound mathematics as poetic riddles. Let us solve his famous Alms Riddle and trace how Indian fraction algorithms traveled across the globe to transform the modern world!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Classic Alms Riddle of L\u012bl\u0101vat\u012b</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    <em>\"O beautiful maiden with playful eyes, a traveler gave $\\frac{1}{2}$ of his coins in Pray\u0101ga, $\\frac{2}{9}$ of the remainder in K\u0101\u015b\u012b, and $\\frac{1}{4}$ of what still remained in Gay\u0101. Returning home, he found 63 coins left in his purse. Tell me, what was his original wealth?\"</em>\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl space-y-1 text-xs text-slate-300 my-2'>\n                    <p>\u2022 After Pray\u0101ga: Remainder = $1 - \\frac{1}{2} = \\frac{1}{2}$.</p>\n                    <p>\u2022 In K\u0101\u015b\u012b: Donates $\\frac{2}{9}$ of $\\frac{1}{2} = \\frac{1}{9}$. Remainder = $\\frac{1}{2} - \\frac{1}{9} = \\frac{7}{18}$.</p>\n                    <p>\u2022 In Gay\u0101: Donates $\\frac{1}{4}$ of $\\frac{7}{18}$. Remainder = $\\frac{3}{4} \\times \\frac{7}{18} = \\frac{7}{24}$.</p>\n                    <p>\u2022 If $\\frac{7}{24}$ of total $= 63$ coins &rarr; <strong>$\\text{Total} = 63 \\div \\frac{7}{24} = 63 \\times \\frac{24}{7} = 9 \\times 24 = 216\\text{ coins!}$</strong></p>\n                </div>\n                <div class='p-2 bg-amber-950/30 border border-amber-500/30 rounded-lg text-xs text-amber-200 mt-2'>\n                    <strong>Global Lineage:</strong> Indian fraction arithmetic was translated into Arabic in 8th-century Baghdad, studied by al-Khwarizmi, and transmitted to Europe through Leonardo of Pisa (Fibonacci) in his 1202 book <em>Liber Abaci</em>!\n                </div>\n            </div>\n        ",
        "sim_id": "sim-lilavati-donation",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "In Bh\u0101skara's alms riddle, what was the traveler's total coin purse initially?",
                "options": [
                    "120 coins",
                    "216 coins",
                    "180 coins",
                    "240 coins"
                ],
                "correct": 1,
                "explanation": "The final remaining fraction was 7/24. Since 7/24 of Total = 63, Total = 63 \u00d7 24 / 7 = 9 \u00d7 24 = 216 coins."
            },
            {
                "id": "cp16_2",
                "question": "Which European mathematician introduced Indian fractional algorithms and numerals to Europe in his 1202 text Liber Abaci?",
                "options": [
                    "Isaac Newton",
                    "Ren\u00e9 Descartes",
                    "Fibonacci (Leonardo of Pisa)",
                    "Archimedes"
                ],
                "correct": 2,
                "explanation": "Fibonacci learned Indian-Arabic arithmetic in North Africa and published Liber Abaci in 1202, introducing modern fraction methods to Europe."
            }
        ]
    },
    {
        "id": "slide-17",
        "slide_num": 17,
        "section": "Review",
        "title": "Mastery Challenge Part 1: Fraction Multiplication & Area Models",
        "badge": "Mastery Challenge I",
        "narration": "Outstanding work! Now test your intellect against 10 rigorous challenges examining fraction multiplication, repeated addition, and unit square area models.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena \u2014 Part 1</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Select your answers below and click <strong>Submit Answer</strong>. Click <strong>💡 View Step-by-Step Solution</strong> to see full algebraic derivations.\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": "slide-18",
        "slide_num": 18,
        "section": "Review",
        "title": "Mastery Challenge Part 2: Brahmagupta's Product Law & Cancelling",
        "badge": "Mastery Challenge II",
        "narration": "Onward! These 10 questions test your mastery of Brahmagupta's multiplication rule, cross-cancelling techniques, and analyzing whether products shrink or expand.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena \u2014 Part 2</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Apply cross-cancelling shortcuts and compare products against factors!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": "slide-19",
        "slide_num": 19,
        "section": "Review",
        "title": "Mastery Challenge Part 3: Reciprocals & Fraction Division",
        "badge": "Mastery Challenge III",
        "narration": "Now we test reciprocals, division grouping, and the ancient Indian rule of inverting and multiplying!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena \u2014 Part 3</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Remember: dividing by a fraction less than 1 always produces a quotient larger than the dividend!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": "slide-20",
        "slide_num": 20,
        "section": "Review",
        "title": "Mastery Challenge Part 4: Practical Word Problems, Cisterns & Heritage",
        "badge": "Mastery Challenge IV",
        "narration": "The final capstone challenge! Solve real-world rate problems, Vedic altar brick paving, Prithudakasvami's cistern fountains, and Bhaskaracharya's Lilavati riddle.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Final Capstone Examination</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Complete the final 10 questions to complete your mastery of Working with Fractions!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            31,
            40
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "slide_num": 17,
        "question": "What is the result of multiplying $5 \\times \\frac{3}{7}$?",
        "options": [
            "$\\frac{15}{35}$",
            "$\\frac{15}{7}$",
            "$\\frac{8}{7}$",
            "$\\frac{3}{35}$"
        ],
        "correct": 1,
        "solution": "Multiply the whole number by the numerator: 5 \u00d7 3 / 7 = 15/7 = 2 1/7."
    },
    {
        "id": 2,
        "slide_num": 17,
        "question": "Which of the following represents $\\frac{1}{4}$ of 16?",
        "options": [
            "4",
            "8",
            "64",
            "12"
        ],
        "correct": 0,
        "solution": "1/4 of 16 = 1/4 \u00d7 16 = 16 / 4 = 4."
    },
    {
        "id": 3,
        "slide_num": 17,
        "question": "In a unit square area model, if a rectangle has dimensions $\\frac{2}{3}$ and $\\frac{3}{4}$, what fraction of the unit square does it cover?",
        "options": [
            "$\\frac{5}{7}$",
            "$\\frac{6}{12} = \\frac{1}{2}$",
            "$\\frac{5}{12}$",
            "$\\frac{8}{9}$"
        ],
        "correct": 1,
        "solution": "Area = (2/3) \u00d7 (3/4) = (2 \u00d7 3) / (3 \u00d7 4) = 6/12 = 1/2."
    },
    {
        "id": 4,
        "slide_num": 17,
        "question": "What is $\\frac{2}{5}$ of $\\frac{5}{8}$?",
        "options": [
            "$\\frac{1}{4}$",
            "$\\frac{7}{13}$",
            "$\\frac{10}{13}$",
            "$\\frac{1}{2}$"
        ],
        "correct": 0,
        "solution": "(2/5) \u00d7 (5/8) = (2 \u00d7 5) / (5 \u00d7 8) = 10/40 = 1/4."
    },
    {
        "id": 5,
        "slide_num": 17,
        "question": "If each side of an equilateral triangle measures $\\frac{4}{5}\\text{ cm}$, what is its perimeter?",
        "options": [
            "$\\frac{12}{15}\\text{ cm}$",
            "$\\frac{7}{5}\\text{ cm}$",
            "$\\frac{12}{5}\\text{ cm} = 2\\frac{2}{5}\\text{ cm}$",
            "$\\frac{16}{25}\\text{ cm}$"
        ],
        "correct": 2,
        "solution": "Perimeter = 3 \u00d7 (4/5) = 12/5 = 2 2/5 cm."
    },
    {
        "id": 6,
        "slide_num": 17,
        "question": "A recipe requires $\\frac{3}{4}$ cup of sugar per cake. How much sugar is needed for 6 cakes?",
        "options": [
            "$4\\frac{1}{2}$ cups",
            "3 cups",
            "$6\\frac{3}{4}$ cups",
            "5 cups"
        ],
        "correct": 0,
        "solution": "6 \u00d7 (3/4) = 18/4 = 9/2 = 4 1/2 cups."
    },
    {
        "id": 7,
        "slide_num": 17,
        "question": "What is $\\frac{3}{10} \\times 5$ in simplest form?",
        "options": [
            "$\\frac{15}{10}$",
            "$1\\frac{1}{2}$ (or $\\frac{3}{2}$)",
            "$\\frac{3}{50}$",
            "$\\frac{8}{10}$"
        ],
        "correct": 1,
        "solution": "(3 \u00d7 5) / 10 = 15/10 = 3/2 = 1 1/2."
    },
    {
        "id": 8,
        "slide_num": 17,
        "question": "If you shade $\\frac{3}{5}$ of a circle, and then erase $\\frac{1}{3}$ of the shaded portion, what fraction of the whole circle was erased?",
        "options": [
            "$\\frac{2}{5}$",
            "$\\frac{1}{5}$",
            "$\\frac{3}{15}$ (which is $\\frac{1}{5}$)",
            "Both B and C"
        ],
        "correct": 3,
        "solution": "Erased = 1/3 of 3/5 = (1 \u00d7 3) / (3 \u00d7 5) = 3/15 = 1/5. Both B and C are correct."
    },
    {
        "id": 9,
        "slide_num": 17,
        "question": "What is the area of a rectangular cardboard piece of length $2\\frac{1}{2}\\text{ cm}$ and width $\\frac{4}{5}\\text{ cm}$?",
        "options": [
            "2 sq cm",
            "$2\\frac{4}{10}$ sq cm",
            "$3\\frac{3}{10}$ sq cm",
            "1.5 sq cm"
        ],
        "correct": 0,
        "solution": "Length = 5/2 cm, Width = 4/5 cm. Area = (5/2) \u00d7 (4/5) = 20/10 = 2 sq cm."
    },
    {
        "id": 10,
        "slide_num": 17,
        "question": "Why does $\\frac{1}{a} \\times a = 1$ for any non-zero whole number $a$?",
        "options": [
            "Because a / a = 1",
            "Because whole numbers cancel",
            "Because 1 is the multiplicative identity",
            "All of the above"
        ],
        "correct": 3,
        "solution": "(1/a) \u00d7 (a/1) = a/a = 1, reflecting the definition of a multiplicative inverse."
    },
    {
        "id": 11,
        "slide_num": 18,
        "question": "According to Brahmagupta's formula, $\\frac{a}{b} \\times \\frac{c}{d}$ equals:",
        "options": [
            "$\\frac{a+c}{b+d}$",
            "$\\frac{a \\times d}{b \\times c}$",
            "$\\frac{a \\times c}{b \\times d}$",
            "$\\frac{a \\times b}{c \\times d}$"
        ],
        "correct": 2,
        "solution": "Brahmagupta's product formula states: (a/b) \u00d7 (c/d) = (a \u00d7 c) / (b \u00d7 d)."
    },
    {
        "id": 12,
        "slide_num": 18,
        "question": "Compute $\\frac{7}{11} \\times \\frac{22}{21}$ in simplest terms:",
        "options": [
            "$\\frac{154}{231}$",
            "$\\frac{2}{3}$",
            "$\\frac{3}{2}$",
            "$\\frac{1}{3}$"
        ],
        "correct": 1,
        "solution": "Cross-cancel: 7 and 21 divide by 7 (gives 1 and 3); 11 and 22 divide by 11 (gives 1 and 2). Product = (1 \u00d7 2) / (1 \u00d7 3) = 2/3."
    },
    {
        "id": 13,
        "slide_num": 18,
        "question": "When multiplying two proper fractions, the product is always:",
        "options": [
            "Greater than 1",
            "Equal to 1",
            "Less than both given fractions",
            "Greater than both given fractions"
        ],
        "correct": 2,
        "solution": "Since both proper fractions are positive and less than 1, multiplying shrinks both factors: Product < Factor 1 and Product < Factor 2."
    },
    {
        "id": 14,
        "slide_num": 18,
        "question": "Compute $3\\frac{1}{3} \\times 2\\frac{2}{5}$:",
        "options": [
            "$6\\frac{2}{15}$",
            "8",
            "$7\\frac{1}{2}$",
            "10"
        ],
        "correct": 1,
        "solution": "Convert to improper fractions: 3 1/3 = 10/3, 2 2/5 = 12/5. Product = (10/3) \u00d7 (12/5) = (2 \u00d7 4) = 8."
    },
    {
        "id": 15,
        "slide_num": 18,
        "question": "Which product is strictly greater than 1?",
        "options": [
            "$\\frac{4}{5} \\times \\frac{3}{4}$",
            "$\\frac{7}{6} \\times \\frac{8}{7}$",
            "$\\frac{2}{3} \\times \\frac{3}{2}$",
            "$\\frac{1}{2} \\times \\frac{1}{3}$"
        ],
        "correct": 1,
        "solution": "(7/6) \u00d7 (8/7) = 8/6 = 4/3 = 1 1/3, which is strictly greater than 1 because both factors are improper fractions (> 1)."
    },
    {
        "id": 16,
        "slide_num": 18,
        "question": "Simplify $\\frac{9}{16} \\times \\frac{8}{27}$:",
        "options": [
            "$\\frac{1}{6}$",
            "$\\frac{72}{432}$",
            "$\\frac{3}{8}$",
            "Both A and B"
        ],
        "correct": 3,
        "solution": "9 cancels with 27 (gives 1/3); 8 cancels with 16 (gives 1/2). Product = (1 \u00d7 1) / (2 \u00d7 3) = 1/6 (which equals 72/432)."
    },
    {
        "id": 17,
        "slide_num": 18,
        "question": "If $\\frac{a}{b} \\times \\frac{c}{d} = \\frac{c}{d} \\times \\frac{a}{b}$, which mathematical property is verified?",
        "options": [
            "Closure property",
            "Commutative property",
            "Associative property",
            "Distributive property"
        ],
        "correct": 1,
        "solution": "The commutative property of multiplication states that the order of the factors does not change the result."
    },
    {
        "id": 18,
        "slide_num": 18,
        "question": "What is the product of $\\frac{5}{9} \\times 0$?",
        "options": [
            "$\\frac{5}{9}$",
            "0",
            "1",
            "Undefined"
        ],
        "correct": 1,
        "solution": "Zero multiplied by any fraction equals zero."
    },
    {
        "id": 19,
        "slide_num": 18,
        "question": "Calculate $\\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{4}{5}$:",
        "options": [
            "$\\frac{1}{5}$",
            "$\\frac{24}{120}$",
            "$\\frac{1}{4}$",
            "Both A and B"
        ],
        "correct": 3,
        "solution": "Telescoping cross-cancellation: all intermediate numerators and denominators cancel, leaving 1/5 (which equals 24/120)."
    },
    {
        "id": 20,
        "slide_num": 18,
        "question": "In the Br\u0101hmasphu\u1e6dasiddh\u0101nta (628 CE), who formulated the general fraction multiplication rule?",
        "options": [
            "Varahamihira",
            "Brahmagupta",
            "Aryabhata",
            "Madhava"
        ],
        "correct": 1,
        "solution": "Acharya Brahmagupta codified the universal fraction multiplication rule in chapter 12 of his Br\u0101hmasphu\u1e6dasiddh\u0101nta."
    },
    {
        "id": 21,
        "slide_num": 19,
        "question": "What is the reciprocal of $\\frac{5}{9}$?",
        "options": [
            "$\\frac{5}{9}$",
            "$\\frac{9}{5}$",
            "$-\\frac{5}{9}$",
            "1"
        ],
        "correct": 1,
        "solution": "The reciprocal of a/b is b/a; flipping 5/9 gives 9/5 = 1 4/5."
    },
    {
        "id": 22,
        "slide_num": 19,
        "question": "What is the reciprocal of the whole number 7?",
        "options": [
            "7",
            "$\\frac{1}{7}$",
            "$\\frac{7}{1}$",
            "0"
        ],
        "correct": 1,
        "solution": "7 can be written as 7/1. Its reciprocal is 1/7."
    },
    {
        "id": 23,
        "slide_num": 19,
        "question": "Divide: $8 \\div \\frac{2}{3}$:",
        "options": [
            "$\\frac{16}{3}$",
            "12",
            "$\\frac{8}{3}$",
            "6"
        ],
        "correct": 1,
        "solution": "8 \u00f7 (2/3) = 8 \u00d7 (3/2) = 24 / 2 = 12."
    },
    {
        "id": 24,
        "slide_num": 19,
        "question": "Evaluate $\\frac{5}{6} \\div \\frac{5}{6}$:",
        "options": [
            "0",
            "1",
            "$\\frac{25}{36}$",
            "$\\frac{10}{12}$"
        ],
        "correct": 1,
        "solution": "Any non-zero quantity divided by itself equals 1."
    },
    {
        "id": 25,
        "slide_num": 19,
        "question": "Compute $\\frac{4}{9} \\div 2$:",
        "options": [
            "$\\frac{8}{9}$",
            "$\\frac{2}{9}$",
            "$\\frac{4}{18}$",
            "Both B and C"
        ],
        "correct": 3,
        "solution": "(4/9) \u00f7 2 = (4/9) \u00d7 (1/2) = 4/18 = 2/9. Both B and C are correct."
    },
    {
        "id": 26,
        "slide_num": 19,
        "question": "Evaluate $\\frac{7}{12} \\div \\frac{14}{15}$ in simplest form:",
        "options": [
            "$\\frac{5}{8}$",
            "$\\frac{98}{180}$",
            "$\\frac{8}{5}$",
            "$\\frac{1}{2}$"
        ],
        "correct": 0,
        "solution": "(7/12) \u00d7 (15/14) = (1/4) \u00d7 (5/2) = 5/8."
    },
    {
        "id": 27,
        "slide_num": 19,
        "question": "Which of the following numbers does NOT have a reciprocal?",
        "options": [
            "1",
            "-1",
            "0",
            "100"
        ],
        "correct": 2,
        "solution": "Zero has no reciprocal because division by zero is undefined."
    },
    {
        "id": 28,
        "slide_num": 19,
        "question": "Why is $12 \\div \\frac{1}{4} = 48$ greater than 12?",
        "options": [
            "Because dividing by a number less than 1 asks how many small parts fit into the whole, which is always more parts",
            "Because multiplication was used",
            "Because 48 is an even number",
            "It is an error"
        ],
        "correct": 0,
        "explanation": "Dividing by 1/4 determines how many quarter-units fit inside 12 whole units: 12 \u00d7 4 = 48."
    },
    {
        "id": 29,
        "slide_num": 19,
        "question": "Compute $4\\frac{2}{5} \\div 2\\frac{1}{5}$:",
        "options": [
            "1",
            "2",
            "3",
            "$\\frac{1}{2}$"
        ],
        "correct": 1,
        "solution": "4 2/5 = 22/5; 2 1/5 = 11/5. (22/5) \u00f7 (11/5) = (22/5) \u00d7 (5/11) = 2."
    },
    {
        "id": 30,
        "slide_num": 19,
        "question": "Which medieval Indian mathematician stated the rule: 'Having inverted the divisor, multiply with the dividend'?",
        "options": [
            "\u015ar\u012bdhar\u0101ch\u0101rya (in P\u0101\u1e6d\u012bga\u1e47ita)",
            "Aryabhata",
            "Varahamihira",
            "Pingala"
        ],
        "correct": 0,
        "solution": "Acharya \u015ar\u012bdhar\u0101ch\u0101rya explicitly recorded the 'invert the divisor and multiply' rule in his text P\u0101\u1e6d\u012bga\u1e47ita."
    },
    {
        "id": 31,
        "slide_num": 20,
        "question": "A tailor needs $\\frac{7}{4}$ meters of cloth to stitch one shirt. How many shirts can be made from 21 meters of cloth?",
        "options": [
            "12 shirts",
            "14 shirts",
            "10 shirts",
            "16 shirts"
        ],
        "correct": 0,
        "solution": "21 \u00f7 (7/4) = 21 \u00d7 (4/7) = 3 \u00d7 4 = 12 shirts."
    },
    {
        "id": 32,
        "slide_num": 20,
        "question": "A car runs 16 km using 1 liter of petrol. How much distance will it cover using $2\\frac{3}{4}$ liters of petrol?",
        "options": [
            "40 km",
            "44 km",
            "48 km",
            "32 km"
        ],
        "correct": 1,
        "solution": "16 \u00d7 (11/4) = 4 \u00d7 11 = 44 km."
    },
    {
        "id": 33,
        "slide_num": 20,
        "question": "In the ancient \u015aulbas\u016btra, an altar section of area 5 units is paved with bricks of area $\\frac{1}{4}$ unit each. How many bricks are needed?",
        "options": [
            "10",
            "15",
            "20",
            "25"
        ],
        "correct": 2,
        "solution": "5 \u00f7 (1/4) = 5 \u00d7 4 = 20 bricks."
    },
    {
        "id": 34,
        "slide_num": 20,
        "question": "Fountain A fills a tank in $\\frac{1}{3}$ day, and Fountain B in $\\frac{1}{6}$ day. Flowing together, what fraction of a day will they take to fill the tank?",
        "options": [
            "$\\frac{1}{9}$ day",
            "$\\frac{1}{2}$ day",
            "$\\frac{1}{4}$ day",
            "$\\frac{2}{9}$ day"
        ],
        "correct": 0,
        "solution": "Rate A = 3 tanks/day; Rate B = 6 tanks/day. Combined = 9 tanks/day. Time = 1/9 day."
    },
    {
        "id": 35,
        "slide_num": 20,
        "question": "In Bh\u0101skara's alms riddle, the remaining fraction of coins after all donations was $\\frac{7}{24}$. If this remaining portion equaled 49 coins, what was the initial amount?",
        "options": [
            "144 coins",
            "168 coins",
            "196 coins",
            "216 coins"
        ],
        "correct": 1,
        "solution": "Total = 49 \u00f7 (7/24) = 49 \u00d7 (24/7) = 7 \u00d7 24 = 168 coins."
    },
    {
        "id": 36,
        "slide_num": 20,
        "question": "A container holds $5\\frac{1}{4}$ liters of cooking oil. If small bottles hold $\\frac{3}{8}$ liter each, how many bottles can be filled completely?",
        "options": [
            "12",
            "14",
            "16",
            "18"
        ],
        "correct": 1,
        "solution": "5 1/4 = 21/4 liters. 21/4 \u00f7 3/8 = (21/4) \u00d7 (8/3) = 7 \u00d7 2 = 14 bottles."
    },
    {
        "id": 37,
        "slide_num": 20,
        "question": "A cyclist covers $12\\frac{1}{2}$ km in $\\frac{5}{6}$ of an hour. What is the average speed in km/h?",
        "options": [
            "15 km/h",
            "12 km/h",
            "10 km/h",
            "18 km/h"
        ],
        "correct": 0,
        "solution": "Speed = (25/2) \u00f7 (5/6) = (25/2) \u00d7 (6/5) = 5 \u00d7 3 = 15 km/h."
    },
    {
        "id": 38,
        "slide_num": 20,
        "question": "What is the title of Bh\u0101skar\u0101ch\u0101rya's 1150 CE mathematical treatise dedicated to his daughter, famous for poetic fraction problems?",
        "options": [
            "Siddh\u0101nta \u015airoma\u1e47i (L\u012bl\u0101vat\u012b)",
            "Aryabhatiya",
            "Br\u0101hmasphu\u1e6dasiddh\u0101nta",
            "B\u012bjaga\u1e47ita"
        ],
        "correct": 0,
        "solution": "Bh\u0101skar\u0101ch\u0101rya's L\u012bl\u0101vat\u012b (the arithmetic section of his master treatise Siddh\u0101nta \u015airoma\u1e47i, 1150 CE) contains these poetic problems."
    },
    {
        "id": 39,
        "slide_num": 20,
        "question": "If $\\frac{3}{4}$ of a number is 27, what is the number?",
        "options": [
            "36",
            "32",
            "24",
            "40"
        ],
        "correct": 0,
        "solution": "Number = 27 \u00f7 (3/4) = 27 \u00d7 (4/3) = 9 \u00d7 4 = 36."
    },
    {
        "id": 40,
        "slide_num": 20,
        "question": "In the historical transmission of fraction arithmetic, which Italian book published in 1202 introduced Indian fraction methods to Western Europe?",
        "options": [
            "Principia Mathematica",
            "Liber Abaci by Leonardo of Pisa (Fibonacci)",
            "Elements of Geometry",
            "Almagest"
        ],
        "correct": 1,
        "solution": "Fibonacci's Liber Abaci (1202 CE) introduced Indian-Arabic numerals and fractional arithmetic to Western Europe."
    }
]
