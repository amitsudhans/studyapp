# -*- coding: utf-8 -*-
"""
Data generator for NCERT Class 6 Mathematics Chapter 7: Fractions
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, etc.).
All math rendered in clean Unicode (1/2, 3/4, 5/2, 1 1/2, ×, ÷, +, −, etc.).
"""

CHAPTER_META = {
    "title": "NCERT Class 6 Mathematics • Chapter 7 • Fractions",
    "mentors": "Acharya Brahmagupta & Abu Bakr al-Hassar (Pioneers of Fractional Arithmetic & The Fraction Bar)",
    "description": "Comprehensive 20-slide interactive master lab covering equal shares, unit fractions, parts of a whole, paper strip folding, numerator and denominator, number line plotting, density of fractions, proper and improper fractions, mixed numbers, fraction walls, equivalent fractions, simplest form, comparing fractions, addition and subtraction with Brahmagupta's method, and ancient historical origins."
}

SLIDES = [
    # Slide 1: Equal Shares
    {
        "id": 1,
        "badge": "Core Concept",
        "title": "Equal Shares",
        "subtitle": "Quantifying Fair Portions from a Shared Whole",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When a single whole item (like a round roti or a candy bar) is divided equally among multiple people, whole numbers (0, 1, 2, 3...) cannot describe the size of each share. A <span class='text-amber-400 font-semibold'>fraction</span> quantifies equal portions of a whole.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='flex items-center gap-2 font-mono text-cyan-300'>
                    <span class='w-2 h-2 rounded-full bg-cyan-400'></span>
                    <span>1 roti divided equally between 2 children = 1/2 roti each ("one half").</span>
                </div>
                <div class='flex items-center gap-2 font-mono text-amber-300'>
                    <span class='w-2 h-2 rounded-full bg-amber-400'></span>
                    <span>1 roti divided equally among 4 children = 1/4 roti each ("one quarter").</span>
                </div>
                <div class='flex items-center gap-2 font-mono text-emerald-300'>
                    <span class='w-2 h-2 rounded-full bg-emerald-400'></span>
                    <span>General Rule: 1 whole divided into n equal parts produces fractional units of 1/n.</span>
                </div>
            </div>
            <p class='text-xs text-slate-400 leading-relaxed'>
                A fraction strictly requires that all parts are exactly equal in size. If a roti is split into two unequal pieces, neither piece is truly 1/2.
            </p>
        """,
        "summary": "Fractions represent equal shares of a whole. When 1 item is divided into n equal pieces, each piece is 1/n.",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "If 1 paratha is shared equally among 3 friends, what fraction does each friend get?",
                "options": ["1/2", "1/3", "3/1", "2/3"],
                "correct": 1,
                "explanation": "Sharing 1 whole equally among 3 people gives each person exactly 1/3 of the paratha."
            },
            {
                "id": "cp1_2",
                "question": "Why can an unequal slice of pizza NOT be called 1/4, even if the pizza was cut into 4 pieces?",
                "options": [
                    "A pizza cannot be divided into quarters",
                    "Fractions require every share to be strictly equal in size",
                    "Only square items can have fractions",
                    "The crust is thicker than the center"
                ],
                "correct": 1,
                "explanation": "A fraction requires all divided parts to be identical in measure. 4 unequal parts do not represent quarters."
            }
        ]
    },

    # Slide 2: Comparing Unit Fractions
    {
        "id": 2,
        "badge": "Core Concept",
        "title": "Comparing Unit Fractions",
        "subtitle": "As Denominator Increases, Share Size Decreases",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A <span class='text-amber-400 font-semibold'>unit fraction</span> has a numerator of 1 (such as 1/2, 1/3, 1/4, 1/5, ..., 1/100). The bottom number (the <span class='text-cyan-300 font-semibold'>denominator</span>) indicates how many equal parts the whole is partitioned into.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 text-xs space-y-1.5'>
                <p class='font-bold text-slate-200'>The Sharing Principle:</p>
                <p class='text-slate-300'>• Sharing 1 cake among 2 people gives huge slices: <span class='text-amber-300 font-mono font-bold'>1/2</span>.</p>
                <p class='text-slate-300'>• Sharing 1 cake among 5 people gives smaller slices: <span class='text-amber-300 font-mono font-bold'>1/5</span>.</p>
                <p class='text-slate-300'>• Sharing 1 cake among 9 people gives even tinier slices: <span class='text-amber-300 font-mono font-bold'>1/9</span>.</p>
                <div class='mt-2 p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 font-bold'>
                    1/2 > 1/3 > 1/4 > 1/5 > 1/6 > ... > 1/100
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Ancient Knowledge: In the Rig Veda, 3/4 was called 'tri-pada', reflecting modern Indian terms like 'teen paav' (three quarters) or 'mukkaal'.
            </p>
        """,
        "summary": "As the denominator of a unit fraction grows, the size of each slice shrinks: 1/2 is much bigger than 1/10.",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "Which fraction represents a LARGER portion of a chocolate bar: 1/5 or 1/8?",
                "options": ["1/8 because 8 is bigger than 5", "1/5 because sharing among 5 gives bigger pieces", "Both are equal", "Cannot be determined"],
                "correct": 1,
                "explanation": "Dividing 1 whole into fewer pieces (5 instead of 8) means each piece is larger: 1/5 > 1/8."
            },
            {
                "id": "cp2_2",
                "question": "What is the correct order of unit fractions from smallest to largest?",
                "options": ["1/2, 1/4, 1/7, 1/10", "1/10, 1/7, 1/4, 1/2", "1/4, 1/2, 1/10, 1/7", "1/7, 1/10, 1/2, 1/4"],
                "correct": 1,
                "explanation": "As denominator grows, the fraction shrinks. In ascending order: 1/10 < 1/7 < 1/4 < 1/2."
            }
        ]
    },

    # Slide 3: Parts of a Whole
    {
        "id": 3,
        "badge": "Core Concept",
        "title": "Parts of a Whole",
        "subtitle": "Combining Unit Fractions to Form Non-Unit Quantities",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When you gather multiple unit fractions together, you build general fractions. For example, if you take 3 pieces of a chikki bar that was cut into 4 equal quarters, you possess <span class='text-amber-400 font-bold'>3/4</span> of the chikki.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-cyan-300'>
                    1/4 + 1/4 + 1/4 = 3/4 ("three quarters" or "three fourths")
                </div>
                <p class='text-slate-300'>
                    • The whole contains 4 equal units (4/4 = 1 whole).<br>
                    • The selected portion contains 3 of those units.<br>
                    • The unshaded remaining part is 1/4, because 3/4 + 1/4 = 4/4 = 1.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                A fraction represents two distinct numbers: the count of parts chosen (3) and the total equal parts making up the whole (4).
            </p>
        """,
        "summary": "Combining multiple unit fractions forms general fractions. 3 pieces of 1/4 equal 3/4 of the whole.",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "A chocolate bar is divided into 6 equal squares. If Priya eats 5 squares, what fraction has she eaten?",
                "options": ["1/6", "5/6", "6/5", "5/1"],
                "correct": 1,
                "explanation": "She ate 5 parts out of 6 equal total parts, which is 5/6 of the chocolate bar."
            },
            {
                "id": "cp3_2",
                "question": "What fraction of the chocolate bar remains uneaten if Priya ate 5/6?",
                "options": ["1/6", "2/6", "5/6", "0/6"],
                "correct": 0,
                "explanation": "The entire bar is 6/6. Uneaten part = 6/6 − 5/6 = 1/6."
            }
        ]
    },

    # Slide 4: Different Shapes, Same Share
    {
        "id": 4,
        "badge": "Core Concept",
        "title": "Different Shapes, Same Share",
        "subtitle": "Equal Fractional Area in Diverse Geometric Cuts",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Equal shares do not need to look identical in shape to represent the same fraction! As long as each piece covers the exact same area, it is a valid equal share.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Ways to cut a square into 4 equal quarters (1/4 each):</p>
                <div class='grid grid-cols-1 sm:grid-cols-3 gap-2 text-center font-mono'>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-amber-300'>4 Vertical Columns<br>(Stripes)</div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-cyan-300'>2×2 Square Grid<br>(Four Corners)</div>
                    <div class='p-2 rounded bg-slate-900 border border-slate-700 text-emerald-300'>2 Diagonals<br>(Four Triangles)</div>
                </div>
                <p class='text-slate-300 text-xs mt-1'>
                    All three partitioning methods yield pieces with an area of exactly 1/4 of the original square, despite their differing shapes.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Conservation of Area: A triangular quarter and a rectangular quarter have different perimeters, but represent the exact same fraction (1/4) of the square's area.
            </p>
        """,
        "summary": "Equal shares can have different visual shapes. A square cut into 4 strips, 4 corner squares, or 4 triangles each has pieces of area 1/4.",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "A square paper is cut along its two diagonals into 4 triangles. What fraction of the square is each triangle?",
                "options": ["1/2", "1/4", "1/8", "4/1"],
                "correct": 1,
                "explanation": "Cutting along both diagonals divides the square into 4 congruent triangles of equal area, so each is 1/4."
            },
            {
                "id": "cp4_2",
                "question": "Can two pieces of a cake have different shapes but still both be 1/6 of the cake?",
                "options": [
                    "No, identical fractions must have identical shapes",
                    "Yes, provided both pieces enclose the exact same amount of area",
                    "Only if the cake is round",
                    "No, because geometry dictates fraction equality"
                ],
                "correct": 1,
                "explanation": "Fractional equality depends on the magnitude of the measure (area), not on visual shape congruence."
            }
        ]
    },

    # Slide 5: Paper Strip Folding
    {
        "id": 5,
        "badge": "Core Concept",
        "title": "Paper Strip Folding",
        "subtitle": "Generating Halves, Quarters, Eighths & Thirds by Folding",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Paper folding provides a tactile and visual proof of how fractional units arise naturally:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>1st Fold in Half:</span> Divides the strip into 2 equal parts. Crease marks <span class='font-mono text-cyan-300'>1/2</span>.<br>
                    • <span class='text-amber-300 font-bold'>2nd Fold in Half:</span> Doubling the creases creates 4 equal parts: <span class='font-mono text-cyan-300'>1/4, 2/4, 3/4, 4/4</span>.<br>
                    • <span class='text-amber-300 font-bold'>3rd Fold in Half:</span> Doubling again creates 8 equal parts: <span class='font-mono text-cyan-300'>1/8, 2/8, 3/8, ..., 8/8</span>.<br>
                    • <span class='text-emerald-300 font-bold'>Folding into Thirds:</span> Creating an S-shape or Z-fold produces 3 equal parts (<span class='font-mono text-emerald-300'>1/3, 2/3</span>), and folding each in half produces sixths (<span class='font-mono text-emerald-300'>1/6</span>).
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Every fold in half multiplies the total number of parts by 2, halving the width of each fractional unit: 1/2 → 1/4 → 1/8 → 1/16.
            </p>
        """,
        "summary": "Folding paper strips repeatedly in half generates powers-of-two fractions: 1/2, 1/4, 1/8. Folding into thirds yields 1/3 and 1/6.",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "If you fold a paper strip in half, and then fold it in half again, how many equal sections are created?",
                "options": ["2", "3", "4", "6"],
                "correct": 2,
                "explanation": "Folding once creates 2 sections; folding again doubles that to 2 × 2 = 4 equal sections (quarters)."
            },
            {
                "id": "cp5_2",
                "question": "If a strip folded into 3 equal parts (thirds) is then folded in half, what unit fraction is produced?",
                "options": ["1/4", "1/5", "1/6", "1/8"],
                "correct": 2,
                "explanation": "Halving each of the 3 thirds gives 3 × 2 = 6 equal parts, producing unit fractions of 1/6."
            }
        ]
    },

    # Slide 6: Numerator & Denominator
    {
        "id": 6,
        "badge": "Core Concept",
        "title": "Numerator & Denominator",
        "subtitle": "Anatomy of a Fraction: Count vs Type",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Any fraction can be understood as a repeated count of a unit fraction. For example, 5 times 1/2 equals:
            </p>
            <div class='p-3 rounded-xl bg-slate-900 border border-slate-700 mb-3 text-center font-mono text-xs text-amber-300'>
                1/2 + 1/2 + 1/2 + 1/2 + 1/2 = 5/2 ("five halves")
            </div>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 text-xs space-y-2'>
                <div class='flex items-start gap-2'>
                    <span class='px-2 py-0.5 rounded font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0'>Numerator</span>
                    <span class='text-slate-300'>The top number. It counts <em>how many</em> fractional units are being considered (from Latin <em>numerator</em>, "numberer/counter").</span>
                </div>
                <div class='flex items-start gap-2'>
                    <span class='px-2 py-0.5 rounded font-mono font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0'>Denominator</span>
                    <span class='text-slate-300'>The bottom number. It names the <em>size or type</em> of the unit by telling how many parts make 1 whole (from Latin <em>nomen</em>, "namer").</span>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                In 5/2: The denominator 2 tells us the unit is 'halves'. The numerator 5 tells us we have 5 of those halves.
            </p>
        """,
        "summary": "Numerator counts the units taken; denominator names how many parts make up 1 whole. 5 times 1/2 is 5/2.",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "In the fraction 7/8, what is the numerator and what does it represent?",
                "options": [
                    "8, the total parts in the whole",
                    "7, the count of eighths taken",
                    "7/8, the whole number",
                    "1, the unit fraction"
                ],
                "correct": 1,
                "explanation": "The numerator is 7 (top number), which counts that we have 7 units of size 1/8."
            },
            {
                "id": "cp6_2",
                "question": "Express 4 times 1/3 as a single fraction:",
                "options": ["1/12", "4/3", "4/12", "3/4"],
                "correct": 1,
                "explanation": "4 times 1/3 = 1/3 + 1/3 + 1/3 + 1/3 = 4/3."
            }
        ]
    },

    # Slide 7: Fractions on Number Line
    {
        "id": 7,
        "badge": "Core Concept",
        "title": "Fractions on Number Line",
        "subtitle": "Mapping Fractional Distances Between Whole Integers",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Just like whole numbers 0, 1, 2, 3 occupy fixed points on a number line, fractions represent precise lengths and locations along that continuous line:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Protocol for plotting a fraction a/b:</p>
                <p class='text-slate-300'>1. Look at the denominator <span class='font-mono text-amber-300'>b</span>. Divide every unit interval (0 to 1, 1 to 2) into <span class='font-mono text-amber-300'>b</span> equal segments.</p>
                <p class='text-slate-300'>2. Each segment step has length <span class='font-mono text-cyan-300'>1/b</span>.</p>
                <p class='text-slate-300'>3. Starting from 0, count <span class='font-mono text-emerald-300'>a</span> steps to the right. The <span class='font-mono text-emerald-300'>a-th</span> tick mark marks the location of <span class='font-mono text-emerald-300'>a/b</span>.</p>
            </div>
            <p class='text-xs text-slate-400'>
                Example: To mark 3/5, divide the interval from 0 to 1 into 5 equal parts: 1/5, 2/5, 3/5, 4/5, 5/5 (= 1). 3/5 is at the third tick mark.
            </p>
        """,
        "summary": "To plot a/b on the number line, partition each unit gap into b equal segments and step a times from 0.",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "To plot 5/6 on the number line, into how many equal segments must the interval between 0 and 1 be split?",
                "options": ["5", "6", "11", "1"],
                "correct": 1,
                "explanation": "The denominator is 6, so the unit interval between 0 and 1 must be divided into 6 equal parts."
            },
            {
                "id": "cp7_2",
                "question": "Where does the fraction 7/4 lie on the number line?",
                "options": [
                    "Between 0 and 1",
                    "Between 1 and 2",
                    "Between 2 and 3",
                    "Exactly on 7"
                ],
                "correct": 1,
                "explanation": "4/4 = 1 and 8/4 = 2. Since 7/4 is between 4/4 and 8/4 (specifically 1 + 3/4), it lies between 1 and 2."
            }
        ]
    },

    # Slide 8: Density of Fractions
    {
        "id": 8,
        "badge": "Core Concept",
        "title": "Density of Fractions",
        "subtitle": "Infinitely Many Fractions Exist Between Any Two Numbers",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Unlike integers where there is no whole number between 2 and 3, fractions are <span class='text-amber-400 font-semibold'>infinitely dense</span>. Between ANY two fractions on the number line, you can always find another fraction!
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Zooming between 0 and 1:</p>
                <p class='text-slate-300'>• Halving gives: <span class='font-mono text-cyan-300'>1/2</span>.</p>
                <p class='text-slate-300'>• Halving between 0 and 1/2 gives: <span class='font-mono text-cyan-300'>1/4</span>.</p>
                <p class='text-slate-300'>• Halving between 0 and 1/4 gives: <span class='font-mono text-cyan-300'>1/8, 1/16, 1/32, 1/64, ...</span></p>
                <p class='text-emerald-300 font-bold'>
                    No matter how close two fractions are, their midpoint (their average) is a new fraction strictly between them.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                There are infinitely many fractions between 0 and 1, between 0 and 1/100, and even between 99/100 and 1.
            </p>
        """,
        "summary": "Fractions are infinitely dense. Between any two distinct fractions, there exist an infinite number of other fractions.",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "Which fraction lies exactly halfway between 0 and 1/2?",
                "options": ["1/3", "1/4", "1/8", "2/3"],
                "correct": 1,
                "explanation": "Half of 1/2 is 1/4 (1/2 ÷ 2 = 1/4). It sits precisely midway between 0 and 1/2."
            },
            {
                "id": "cp8_2",
                "question": "How many fractions exist between 1/4 and 1/2?",
                "options": ["Only one (1/3)", "Exactly two", "Ten", "Infinitely many"],
                "correct": 3,
                "explanation": "By choosing larger denominators (e.g. 5/16, 6/16, 7/16, 30/100, etc.), infinitely many fractions exist between any two points."
            }
        ]
    },

    # Slide 9: Proper vs Improper
    {
        "id": 9,
        "badge": "Core Concept",
        "title": "Proper vs Improper",
        "subtitle": "Fractions Less Than One vs Fractions Greater Than One",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Depending on whether a fraction represents less than, equal to, or more than one whole, mathematicians categorize it into distinct families:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-emerald-500/30 text-emerald-300'>
                    <span class='font-bold font-mono'>Proper Fraction:</span> Numerator &lt; Denominator (Value &lt; 1).<br>
                    <span class='text-slate-300'>Examples: 1/2, 3/4, 5/6, 99/100. It is genuinely a "part" of a single whole.</span>
                </div>
                <div class='p-2 rounded bg-slate-900 border border-amber-500/30 text-amber-300'>
                    <span class='font-bold font-mono'>Fraction Equal to One:</span> Numerator = Denominator (Value = 1).<br>
                    <span class='text-slate-300'>Examples: 2/2 = 1, 4/4 = 1, 7/7 = 1.</span>
                </div>
                <div class='p-2 rounded bg-slate-900 border border-rose-500/30 text-rose-300'>
                    <span class='font-bold font-mono'>Improper Fraction:</span> Numerator &gt; Denominator (Value &gt; 1).<br>
                    <span class='text-slate-300'>Examples: 5/2, 7/4, 9/5. It represents more than one complete whole.</span>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Historically, the word 'fraction' meant broken piece (less than 1). When quantities exceeded 1, early mathematicians labeled them 'improper'.
            </p>
        """,
        "summary": "Proper fractions have numerator < denominator and value < 1. Improper fractions have numerator > denominator and value > 1.",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "Which of the following is a PROPER fraction?",
                "options": ["7/5", "8/8", "3/7", "9/2"],
                "correct": 2,
                "explanation": "In 3/7, the numerator (3) is smaller than the denominator (7), so its value is less than 1."
            },
            {
                "id": "cp9_2",
                "question": "What is the category of the fraction 11/4?",
                "options": [
                    "Proper fraction",
                    "Improper fraction",
                    "Unit fraction",
                    "Zero fraction"
                ],
                "correct": 1,
                "explanation": "The numerator 11 is strictly greater than the denominator 4, so 11/4 is an improper fraction (value > 1)."
            }
        ]
    },

    # Slide 10: Mixed Numbers
    {
        "id": 10,
        "badge": "Core Concept",
        "title": "Mixed Numbers",
        "subtitle": "Combining Whole Integers with Proper Fractional Parts",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When you have more than 1 whole, an improper fraction can be rewritten as a <span class='text-amber-400 font-semibold'>mixed fraction</span> (or mixed number), showing whole units and remaining parts:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Converting Improper to Mixed (e.g., 9/2):</p>
                <p class='text-slate-300'>• Divide 9 by 2: <span class='font-mono text-cyan-300'>9 ÷ 2 = 4 with a remainder of 1</span>.<br>
                • Whole part = 4, fractional part = 1/2.<br>
                • Therefore, <span class='font-mono text-amber-300 font-bold'>9/2 = 4 1/2</span> ("four and a half").</p>
                <div class='border-t border-slate-700 pt-2'>
                    <p class='font-bold text-slate-200'>Converting Mixed to Improper (e.g., 3 3/4):</p>
                    <p class='text-slate-300'>• 3 wholes have 3 × 4 = 12 quarters.<br>
                    • Add the 3 remaining quarters: 12 + 3 = 15 quarters.<br>
                    • Formula: <span class='font-mono text-emerald-300 font-bold'>3 3/4 = (3 × 4 + 3) / 4 = 15/4</span>.</p>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Mixed numbers are intuitive in everyday speech: "I ran 2 1/2 kilometers" or "I bought 1 3/4 kg of apples".
            </p>
        """,
        "summary": "Mixed numbers combine a whole number and a fraction: 9/2 = 4 1/2. Conversely, 3 3/4 = (3×4+3)/4 = 15/4.",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "Convert 13/4 into a mixed number:",
                "options": ["3 1/4", "4 1/3", "2 3/4", "3 3/4"],
                "correct": 0,
                "explanation": "13 ÷ 4 = 3 with remainder 1. So 13/4 = 3 1/4."
            },
            {
                "id": "cp10_2",
                "question": "Convert the mixed number 2 3/5 into an improper fraction:",
                "options": ["11/5", "13/5", "10/5", "6/5"],
                "correct": 1,
                "explanation": "(2 × 5 + 3) / 5 = (10 + 3) / 5 = 13/5."
            }
        ]
    },

    # Slide 11: The Fraction Wall
    {
        "id": 11,
        "badge": "Core Concept",
        "title": "The Fraction Wall",
        "subtitle": "Visualizing Equivalent Strips from 1 to 1/10",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A <span class='text-amber-400 font-semibold'>fraction wall</span> aligns identical strips of equal total length, each divided into progressively smaller fractional units (halves, thirds, quarters, fifths, sixths, etc.):
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Reading Vertically Down the Wall:</p>
                <p class='text-slate-300'>Notice which partition lines match up perfectly in vertical alignment:</p>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300'>
                    1/2 line aligns with: 2/4, 3/6, 4/8, 5/10<br>
                    1/3 line aligns with: 2/6, 3/9<br>
                    1/4 line aligns with: 2/8
                </div>
                <p class='text-slate-300 text-xs'>
                    Even though 1/2, 2/4, 3/6, and 4/8 use different numbers of pieces and different slice sizes, they occupy the exact same physical length!
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                A fraction wall turns abstract algebraic equality into an undeniable visual fact.
            </p>
        """,
        "summary": "A fraction wall shows that 1/2, 2/4, 3/6, 4/8, and 5/10 have identical horizontal lengths, proving they are equivalent.",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "Looking down a fraction wall, how many sixths (1/6) align with 1/2?",
                "options": ["2", "3", "4", "1"],
                "correct": 1,
                "explanation": "3 pieces of 1/6 cover the exact same distance as 1 piece of 1/2, so 3/6 = 1/2."
            },
            {
                "id": "cp11_2",
                "question": "Which fraction does NOT align with 1/2 on a fraction wall?",
                "options": ["2/4", "3/6", "3/5", "4/8"],
                "correct": 2,
                "explanation": "Half of 5 is 2.5, not 3. 3/5 is greater than 1/2 (since 3/5 = 6/10 > 5/10), so it does not align."
            }
        ]
    },

    # Slide 12: Equivalent Fractions
    {
        "id": 12,
        "badge": "Core Concept",
        "title": "Equivalent Fractions",
        "subtitle": "Scaling Numerator & Denominator by the Same Factor",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                Two fractions are <span class='text-amber-400 font-semibold'>equivalent</span> if they represent the exact same value or share.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Real-World Roti Sharing:</p>
                <p class='text-slate-300'>
                    • 1 roti shared by 2 children = <span class='font-mono text-cyan-300'>1/2 roti each</span>.<br>
                    • 2 rotis shared by 4 children = 2/4 = <span class='font-mono text-cyan-300'>1/2 roti each</span>.<br>
                    • 3 rotis shared by 6 children = 3/6 = <span class='font-mono text-cyan-300'>1/2 roti each</span>.
                </p>
                <div class='border-t border-slate-700 pt-2'>
                    <p class='font-bold text-slate-200'>The Golden Rule of Equivalence:</p>
                    <p class='text-slate-300'>
                        Multiplying or dividing both the numerator and denominator by the <em>same non-zero number k</em> does not change the fraction's value:
                    </p>
                    <div class='p-1.5 rounded bg-slate-900 border border-slate-700 font-mono text-center text-amber-300 font-bold'>
                        (a × k) / (b × k) = a / b
                    </div>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Example: 2/3 = (2×4)/(3×4) = 8/12. Cutting each third into 4 sub-pieces yields 8 twelfths.
            </p>
        """,
        "summary": "Equivalent fractions share the same value. Multiplying or dividing top and bottom by k preserves the value: (a×k)/(b×k) = a/b.",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "Find the missing number to make the fractions equivalent: 3/5 = ? / 20",
                "options": ["9", "12", "15", "18"],
                "correct": 1,
                "explanation": "The denominator 5 was multiplied by 4 to get 20. Multiplying numerator 3 by 4 gives 12. So 3/5 = 12/20."
            },
            {
                "id": "cp12_2",
                "question": "Which of the following is NOT equivalent to 2/3?",
                "options": ["4/6", "6/9", "10/15", "8/15"],
                "correct": 3,
                "explanation": "2/3 = 4/6 (×2) = 6/9 (×3) = 10/15 (×5). But 8/15 is not equivalent to 2/3 (which would be 10/15)."
            }
        ]
    },

    # Slide 13: Simplest Form
    {
        "id": 13,
        "badge": "Core Concept",
        "title": "Simplest Form",
        "subtitle": "Cancelling Common Factors to Reach Lowest Terms",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                A fraction is in its <span class='text-amber-400 font-semibold'>simplest form</span> (or lowest terms) when its numerator and denominator share NO common factor other than 1 (meaning they are co-prime).
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Two Methods to Simplify (e.g., 24/36):</p>
                <p class='text-slate-300'>
                    • <span class='text-cyan-300 font-bold'>Step-by-Step Division:</span> Divide top and bottom by common factors:<br>
                    &nbsp;&nbsp;24/36 ÷ 2 = 12/18 ÷ 2 = 6/9 ÷ 3 = <span class='font-mono text-amber-300 font-bold'>2/3</span>.<br>
                    • <span class='text-emerald-300 font-bold'>Direct HCF Division:</span> Find HCF(24, 36) = 12.<br>
                    &nbsp;&nbsp;Divide directly by 12: (24÷12) / (36÷12) = <span class='font-mono text-amber-300 font-bold'>2/3</span>.
                </p>
            </div>
            <p class='text-xs text-slate-400'>
                Once a fraction is in simplest form, it cannot be reduced any further without introducing non-integer decimals.
            </p>
        """,
        "summary": "A fraction is in simplest form when numerator and denominator have HCF = 1. Divide both by their HCF to reduce in one step.",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "What is 15/25 expressed in its simplest form?",
                "options": ["3/5", "5/3", "1/2", "3/10"],
                "correct": 0,
                "explanation": "HCF of 15 and 25 is 5. Dividing top and bottom by 5 yields 3/5."
            },
            {
                "id": "cp13_2",
                "question": "Is the fraction 8/9 already in simplest form?",
                "options": [
                    "No, both 8 and 9 are composite numbers",
                    "Yes, because 8 and 9 share no common factors other than 1",
                    "No, it can be divided by 2",
                    "No, it can be divided by 3"
                ],
                "correct": 1,
                "explanation": "Although 8 and 9 are both composite, they are co-prime (HCF = 1). Therefore, 8/9 is in simplest form."
            }
        ]
    },

    # Slide 14: Comparing Fractions
    {
        "id": 14,
        "badge": "Core Concept",
        "title": "Comparing Fractions",
        "subtitle": "Common Denominators & Cross-Multiplication",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                To compare two fractions with different denominators (like 3/4 and 5/6), you cannot simply look at the numbers. You must express them in the <span class='text-amber-400 font-semibold'>same fractional unit</span>.
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Method 1: Common Denominator (LCM):</p>
                <p class='text-slate-300'>• Denominators are 4 and 6. LCM(4, 6) = 12.<br>
                • Convert 3/4 = (3×3)/(4×3) = <span class='font-mono text-cyan-300 font-bold'>9/12</span>.<br>
                • Convert 5/6 = (5×2)/(6×2) = <span class='font-mono text-cyan-300 font-bold'>10/12</span>.<br>
                • Since 10/12 &gt; 9/12, we conclude <span class='font-mono text-amber-300 font-bold'>5/6 &gt; 3/4</span>.</p>
                <div class='border-t border-slate-700 pt-2'>
                    <p class='font-bold text-slate-200'>Method 2: Cross-Multiplication Shortcut:</p>
                    <p class='text-slate-300'>Compare a/b with c/d by computing (a × d) vs (b × c):<br>
                    3 × 6 = 18 vs 4 × 5 = 20. Since 18 &lt; 20, 3/4 &lt; 5/6!</p>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                This common-denominator technique also allows arranging long lists of fractions in ascending or descending order.
            </p>
        """,
        "summary": "To compare fractions, convert them to a common denominator using the LCM, or cross-multiply a×d vs b×c.",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "Which fraction is larger: 2/3 or 3/5?",
                "options": ["2/3", "3/5", "Both are equal", "Cannot be determined"],
                "correct": 0,
                "explanation": "Common denominator is 15: 2/3 = 10/15 while 3/5 = 9/15. Since 10 > 9, 2/3 is larger."
            },
            {
                "id": "cp14_2",
                "question": "Using cross-multiplication, compare 4/7 and 5/9:",
                "options": [
                    "4/7 is larger because 4×9 (36) > 7×5 (35)",
                    "5/9 is larger because 35 > 36",
                    "They are equal",
                    "5/9 is larger because 5 > 4"
                ],
                "correct": 0,
                "explanation": "4 × 9 = 36 and 7 × 5 = 35. Since 36 > 35, 4/7 > 5/9."
            }
        ]
    },

    # Slide 15: Adding Like Fractions
    {
        "id": 15,
        "badge": "Core Concept",
        "title": "Adding Like Fractions",
        "subtitle": "Combining Fractions with Identical Denominators",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                When fractions have the <span class='text-amber-400 font-semibold'>same denominator</span>, they share the identical fractional unit. You simply add or subtract the numerators while keeping the denominator unchanged:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <div class='p-2 rounded bg-slate-900 border border-slate-700 font-mono text-center text-cyan-300 font-bold'>
                    a/d + b/d = (a + b) / d &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; a/d − b/d = (a − b) / d
                </div>
                <p class='text-slate-300'>
                    • <span class='text-amber-300 font-bold'>Addition Example:</span> 2/5 + 1/5 = (2 + 1) / 5 = <span class='font-mono text-amber-300'>3/5</span>.<br>
                    • <span class='text-amber-300 font-bold'>Subtraction Example:</span> 6/7 − 4/7 = (6 − 4) / 7 = <span class='font-mono text-amber-300'>2/7</span>.
                </p>
                <div class='p-2 rounded bg-rose-950/40 border border-rose-800/60 text-rose-300'>
                    <span class='font-bold'>Common Trap:</span> NEVER add the denominators! 1/4 + 1/4 is 2/4 (which is 1/2), NOT 2/8. Adding denominators shrinks the unit instead of combining counts!
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Think of it like objects: 2 fifths + 1 fifth = 3 fifths, just as 2 apples + 1 apple = 3 apples.
            </p>
        """,
        "summary": "For like fractions, add or subtract numerators and keep the denominator: a/d + b/d = (a+b)/d. Never add denominators!",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "What is 3/8 + 2/8?",
                "options": ["5/16", "5/8", "6/8", "1/8"],
                "correct": 1,
                "explanation": "Add the numerators: 3 + 2 = 5, and keep denominator 8. The answer is 5/8."
            },
            {
                "id": "cp15_2",
                "question": "What is 7/10 − 3/10 expressed in simplest form?",
                "options": ["4/10", "2/5", "4/0", "1/2"],
                "correct": 1,
                "explanation": "7/10 − 3/10 = 4/10. Simplifying by dividing top and bottom by 2 gives 2/5."
            }
        ]
    },

    # Slide 16: Brahmagupta's Method
    {
        "id": 16,
        "badge": "Core Concept",
        "title": "Brahmagupta's Method",
        "subtitle": "Unlike Denominators & Ancient Fraction History",
        "theory": """
            <p class='text-sm text-slate-300 leading-relaxed mb-3'>
                In 628 CE, the legendary Indian mathematician <span class='text-amber-400 font-semibold'>Brahmagupta</span> formulated the universal rule for adding and subtracting fractions with unlike denominators in his treatise <em>Brahmasphutasiddhanta</em>:
            </p>
            <div class='p-3 rounded-xl bg-slate-800/80 border border-slate-700/80 mb-3 space-y-2 text-xs'>
                <p class='font-bold text-slate-200'>Brahmagupta's 3-Step Algorithm:</p>
                <p class='text-slate-300'>1. Multiply cross-wise to express both fractions with a common denominator (b × d):<br>
                &nbsp;&nbsp;&nbsp;<span class='font-mono text-cyan-300'>a/b = (a × d) / (b × d)</span> and <span class='font-mono text-cyan-300'>c/d = (c × b) / (b × d)</span>.</p>
                <p class='text-slate-300'>2. Add or subtract the numerators: <span class='font-mono text-amber-300 font-bold'>(a×d ± b×c) / (b×d)</span>.</p>
                <p class='text-slate-300'>3. Reduce the result to its simplest form by dividing by the common factor.</p>
                <div class='border-t border-slate-700 pt-2'>
                    <p class='font-bold text-slate-200'>Historical Note on Notation:</p>
                    <p class='text-slate-300'>
                        Writing the numerator directly over the denominator originated in India (Bakhshali Manuscript ~300 CE). The horizontal dividing bar was introduced in the 12th century by Moroccan mathematician Abu Bakr al-Hassar.
                    </p>
                </div>
            </div>
            <p class='text-xs text-slate-400'>
                Egyptian Fraction Challenge: Ancient Egyptians only used unit fractions. Can you write 1 as the sum of 3 distinct unit fractions? 1/2 + 1/3 + 1/6 = 1!
            </p>
        """,
        "summary": "Brahmagupta unified fraction addition: a/b + c/d = (ad + bc)/bd. Numerators over denominators originated in India; Al-Hassar added the bar.",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "Use Brahmagupta's method to compute 1/3 + 1/4:",
                "options": ["2/7", "7/12", "1/12", "5/12"],
                "correct": 1,
                "explanation": "(1×4 + 1×3) / (3×4) = (4 + 3) / 12 = 7/12."
            },
            {
                "id": "cp16_2",
                "question": "Which ancient mathematician first introduced the horizontal fraction bar separating numerator and denominator?",
                "options": ["Euclid", "Brahmagupta", "Abu Bakr al-Hassar", "Eratosthenes"],
                "correct": 2,
                "explanation": "Abu Bakr al-Hassar, a 12th-century mathematician from Morocco, first introduced the horizontal bar."
            }
        ]
    },

    # Quiz Slide 1: Questions 1 to 10
    {
        "id": 17,
        "badge": "Mastery Challenge",
        "title": "Quiz 1",
        "subtitle": "Unit Fractions, Equal Shares & Folding",
        "is_quiz": True,
        "quiz_range": (1, 10)
    },

    # Quiz Slide 2: Questions 11 to 20
    {
        "id": 18,
        "badge": "Mastery Challenge",
        "title": "Quiz 2",
        "subtitle": "Number Line, Proper, Improper & Mixed Numbers",
        "is_quiz": True,
        "quiz_range": (11, 20)
    },

    # Quiz Slide 3: Questions 21 to 30
    {
        "id": 19,
        "badge": "Mastery Challenge",
        "title": "Quiz 3",
        "subtitle": "Fraction Walls, Equivalence & Simplest Form",
        "is_quiz": True,
        "quiz_range": (21, 30)
    },

    # Quiz Slide 4: Questions 31 to 40
    {
        "id": 20,
        "badge": "Mastery Challenge",
        "title": "Quiz 4",
        "subtitle": "Comparing, Addition, Subtraction & History",
        "is_quiz": True,
        "quiz_range": (31, 40)
    }
]

QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "If 1 cake is divided equally among 6 children, what fraction does each child receive?",
        "options": ["6/1", "1/6", "1/5", "6/6"],
        "correct": 1,
        "solution": "When 1 whole item is partitioned equally among n people, each person gets 1/n. Dividing 1 cake among 6 children gives 1/6 of the cake to each."
    },
    # Q2
    {
        "id": 2,
        "question": "Which of the following unit fractions is the SMALLEST?",
        "options": ["1/3", "1/5", "1/12", "1/8"],
        "correct": 2,
        "solution": "In unit fractions, as the denominator increases, the size of each share decreases. Since 12 is the largest denominator, 1/12 is the smallest fraction."
    },
    # Q3
    {
        "id": 3,
        "question": "A strip is folded in half 3 times consecutively. Into how many equal parts is the strip divided?",
        "options": ["6", "8", "12", "16"],
        "correct": 1,
        "solution": "Each fold doubles the number of sections: 1st fold gives 2, 2nd fold gives 4, and 3rd fold gives 2 × 2 × 2 = 8 equal parts."
    },
    # Q4
    {
        "id": 4,
        "question": "In the fraction 5/9, what does the denominator 9 represent?",
        "options": [
            "The number of parts selected",
            "The total number of equal parts that make up 1 whole",
            "The whole number part",
            "The remainder"
        ],
        "correct": 1,
        "solution": "The denominator (bottom number) specifies the total number of equal parts into which the whole has been divided."
    },
    # Q5
    {
        "id": 5,
        "question": "What fraction of an hour is 20 minutes?",
        "options": ["1/2", "1/3", "1/4", "2/5"],
        "correct": 1,
        "solution": "1 hour = 60 minutes. The fraction is 20/60. Dividing numerator and denominator by 20 gives 1/3 of an hour."
    },
    # Q6
    {
        "id": 6,
        "question": "A rectangle is divided into 8 equal parts, and 3 are shaded. What fraction represents the UNSHADED portion?",
        "options": ["3/8", "5/8", "8/3", "5/5"],
        "correct": 1,
        "solution": "Total parts = 8. Shaded parts = 3. Unshaded parts = 8 − 3 = 5. Therefore, the unshaded fraction is 5/8."
    },
    # Q7
    {
        "id": 7,
        "question": "What is 7 times 1/4 expressed as a single fraction?",
        "options": ["7/28", "1/28", "7/4", "4/7"],
        "correct": 2,
        "solution": "7 times 1/4 means adding 1/4 seven times: 1/4 + 1/4 + ... + 1/4 = 7/4."
    },
    # Q8
    {
        "id": 8,
        "question": "In the Rig Veda, 3/4 was called by what ancient term?",
        "options": ["Eka-pada", "Dvi-pada", "Tri-pada", "Chatur-pada"],
        "correct": 2,
        "solution": "In ancient Indian texts including the Rig Veda, 3/4 was named 'tri-pada' (three parts out of four), corresponding to modern Hindi 'teen paav'."
    },
    # Q9
    {
        "id": 9,
        "question": "If a square is cut along both diagonals, each of the 4 resulting triangles has an area equal to what fraction of the square?",
        "options": ["1/2", "1/4", "1/8", "1/3"],
        "correct": 1,
        "solution": "The two diagonals divide the square into 4 congruent triangles of equal area, so each triangle has area equal to 1/4 of the square."
    },
    # Q10
    {
        "id": 10,
        "question": "What fraction of a day is 8 hours?",
        "options": ["1/2", "1/3", "1/4", "1/8"],
        "correct": 1,
        "solution": "1 day = 24 hours. The fraction is 8/24. Dividing numerator and denominator by 8 yields 1/3 of a day."
    },

    # Q11
    {
        "id": 11,
        "question": "Where does the fraction 4/5 lie on the number line?",
        "options": [
            "To the left of 0",
            "Between 0 and 1",
            "Between 1 and 2",
            "To the right of 4"
        ],
        "correct": 1,
        "solution": "Since 4/5 is a proper fraction (numerator 4 < denominator 5), its value is strictly between 0 and 1."
    },
    # Q12
    {
        "id": 12,
        "question": "Which of the following fractions is an IMPROPER fraction?",
        "options": ["2/3", "5/7", "9/4", "1/10"],
        "correct": 2,
        "solution": "An improper fraction has a numerator greater than or equal to its denominator. In 9/4, 9 > 4, so it is improper."
    },
    # Q13
    {
        "id": 13,
        "question": "Convert the improper fraction 17/5 into a mixed number:",
        "options": ["3 2/5", "2 3/5", "3 1/5", "4 2/5"],
        "correct": 0,
        "solution": "Divide 17 by 5: 17 ÷ 5 = 3 with remainder 2. Thus, 17/5 = 3 2/5."
    },
    # Q14
    {
        "id": 14,
        "question": "Convert the mixed number 4 2/3 into an improper fraction:",
        "options": ["14/3", "11/3", "10/3", "8/3"],
        "correct": 0,
        "solution": "Multiply whole number by denominator and add numerator: (4 × 3 + 2) / 3 = (12 + 2) / 3 = 14/3."
    },
    # Q15
    {
        "id": 15,
        "question": "How many fractions lie between 0 and 1 on the number line?",
        "options": ["None", "Exactly 9", "Exactly 100", "Infinitely many"],
        "correct": 3,
        "solution": "Fractions are infinitely dense. You can divide the distance between 0 and 1 into any number of parts, producing infinitely many distinct fractions."
    },
    # Q16
    {
        "id": 16,
        "question": "What is the midpoint between 0 and 1/4 on the number line?",
        "options": ["1/2", "1/6", "1/8", "1/16"],
        "correct": 2,
        "solution": "The midpoint is half of 1/4: (1/4) ÷ 2 = 1/8."
    },
    # Q17
    {
        "id": 17,
        "question": "Which fraction represents exactly 1 whole?",
        "options": ["7/8", "9/9", "10/9", "0/1"],
        "correct": 1,
        "solution": "When numerator equals denominator (n/n), the value is exactly 1 whole. 9/9 = 1."
    },
    # Q18
    {
        "id": 18,
        "question": "Between which two consecutive whole numbers does 11/3 lie?",
        "options": ["1 and 2", "2 and 3", "3 and 4", "4 and 5"],
        "correct": 2,
        "solution": "11 ÷ 3 = 3 with remainder 2, so 11/3 = 3 2/3. This lies between whole numbers 3 and 4."
    },
    # Q19
    {
        "id": 19,
        "question": "Which of the following is equivalent to 1?",
        "options": ["5/6", "12/12", "1/12", "12/1"],
        "correct": 1,
        "solution": "Any non-zero number divided by itself equals 1. So 12/12 = 1."
    },
    # Q20
    {
        "id": 20,
        "question": "If you have 7 halves of an orange, how many whole oranges and extra halves do you have?",
        "options": ["3 wholes and 1 half (3 1/2)", "4 wholes", "2 wholes and 3 halves", "7 wholes"],
        "correct": 0,
        "solution": "7 halves = 7/2. 7 ÷ 2 = 3 with remainder 1, meaning 3 whole oranges and 1 half orange (3 1/2)."
    },

    # Q21
    {
        "id": 21,
        "question": "Which fraction is equivalent to 3/4 with denominator 24?",
        "options": ["15/24", "18/24", "20/24", "21/24"],
        "correct": 1,
        "solution": "To get denominator 24 from 4, multiply by 6: 4 × 6 = 24. Multiply numerator by 6: 3 × 6 = 18. So 3/4 = 18/24."
    },
    # Q22
    {
        "id": 22,
        "question": "What is 18/48 reduced to its simplest form?",
        "options": ["9/24", "6/16", "3/8", "1/3"],
        "correct": 2,
        "solution": "HCF of 18 and 48 is 6. Dividing top and bottom by 6: (18 ÷ 6) / (48 ÷ 6) = 3/8."
    },
    # Q23
    {
        "id": 23,
        "question": "On a fraction wall, how many eighths (1/8) equal 3/4?",
        "options": ["4", "5", "6", "7"],
        "correct": 2,
        "solution": "3/4 = (3 × 2) / (4 × 2) = 6/8. Exactly 6 eighths line up with 3/4."
    },
    # Q24
    {
        "id": 24,
        "question": "A fraction is in simplest form when the HCF of its numerator and denominator is:",
        "options": ["0", "1", "2", "Any prime number"],
        "correct": 1,
        "solution": "A fraction is in lowest terms (simplest form) if and only if numerator and denominator share no common factor other than 1 (HCF = 1)."
    },
    # Q25
    {
        "id": 25,
        "question": "Which of the following fractions is NOT in simplest form?",
        "options": ["7/9", "11/15", "14/21", "25/36"],
        "correct": 2,
        "solution": "In 14/21, both 14 and 21 are divisible by 7: 14/21 = 2/3. Thus it is not in simplest form."
    },
    # Q26
    {
        "id": 26,
        "question": "Find the value of x such that 5/8 = x/40:",
        "options": ["20", "25", "30", "35"],
        "correct": 1,
        "solution": "The denominator 8 was multiplied by 5 to become 40. Therefore, multiply the numerator by 5: x = 5 × 5 = 25."
    },
    # Q27
    {
        "id": 27,
        "question": "If 3 rotis are shared equally among 6 children, what is each child's share in simplest form?",
        "options": ["3/6 roti", "1/2 roti", "2/3 roti", "1/3 roti"],
        "correct": 1,
        "solution": "3 rotis for 6 children gives 3/6. Dividing top and bottom by 3 yields 1/2 roti each."
    },
    # Q28
    {
        "id": 28,
        "question": "Which of the following is equivalent to 5/6?",
        "options": ["10/12", "15/20", "20/30", "25/36"],
        "correct": 0,
        "solution": "Multiplying numerator and denominator of 5/6 by 2 yields 10/12. (15/20 = 3/4; 20/30 = 2/3; 25/36 cannot be simplified to 5/6)."
    },
    # Q29
    {
        "id": 29,
        "question": "What is the simplest form of 36/54?",
        "options": ["6/9", "4/6", "2/3", "18/27"],
        "correct": 2,
        "solution": "HCF of 36 and 54 is 18. (36 ÷ 18) / (54 ÷ 18) = 2/3."
    },
    # Q30
    {
        "id": 30,
        "question": "Can multiplying only the numerator of 2/5 by 3 create an equivalent fraction?",
        "options": [
            "Yes, as long as it is multiplied by a whole number",
            "No, an equivalent fraction requires multiplying BOTH numerator and denominator by the same number",
            "Yes, because 6/5 is equivalent to 2/5",
            "Only if 2/5 is a proper fraction"
        ],
        "correct": 1,
        "solution": "Multiplying only the numerator triples the value (6/5 ≠ 2/5). Both numerator and denominator must be multiplied by the same non-zero number to preserve equivalence."
    },

    # Q31
    {
        "id": 31,
        "question": "Which fraction is greater: 5/7 or 3/7?",
        "options": ["3/7", "5/7", "Both are equal", "Cannot be determined"],
        "correct": 1,
        "solution": "When denominators are identical, the fraction with the larger numerator is larger. Since 5 > 3, 5/7 > 3/7."
    },
    # Q32
    {
        "id": 32,
        "question": "Compare 2/3 and 3/4. Which statement is true?",
        "options": ["2/3 > 3/4", "3/4 > 2/3", "2/3 = 3/4", "3/4 < 1/2"],
        "correct": 1,
        "solution": "Using common denominator 12: 2/3 = 8/12 and 3/4 = 9/12. Since 9/12 > 8/12, 3/4 > 2/3."
    },
    # Q33
    {
        "id": 33,
        "question": "Compute the sum: 3/11 + 5/11",
        "options": ["8/22", "8/11", "15/11", "2/11"],
        "correct": 1,
        "solution": "For like fractions, add the numerators and keep the common denominator: (3 + 5) / 11 = 8/11."
    },
    # Q34
    {
        "id": 34,
        "question": "Compute: 7/9 − 2/9",
        "options": ["5/0", "5/9", "5/18", "9/9"],
        "correct": 1,
        "solution": "Subtract numerators while keeping denominator: (7 − 2) / 9 = 5/9."
    },
    # Q35
    {
        "id": 35,
        "question": "What is 1/2 + 1/3 according to Brahmagupta's method?",
        "options": ["2/5", "5/6", "1/6", "5/12"],
        "correct": 1,
        "solution": "(1 × 3 + 1 × 2) / (2 × 3) = (3 + 2) / 6 = 5/6."
    },
    # Q36
    {
        "id": 36,
        "question": "Compute: 3/4 − 1/6",
        "options": ["2/2", "7/12", "5/12", "2/12"],
        "correct": 1,
        "solution": "Common denominator is 12: 3/4 = 9/12 and 1/6 = 2/12. 9/12 − 2/12 = 7/12."
    },
    # Q37
    {
        "id": 37,
        "question": "Which sum of three distinct unit fractions equals 1 whole (Egyptian fraction puzzle)?",
        "options": [
            "1/2 + 1/3 + 1/4",
            "1/2 + 1/3 + 1/6",
            "1/3 + 1/3 + 1/3",
            "1/4 + 1/4 + 1/2"
        ],
        "correct": 1,
        "solution": "1/2 + 1/3 + 1/6 = 3/6 + 2/6 + 1/6 = (3 + 2 + 1) / 6 = 6/6 = 1. All three are distinct unit fractions."
    },
    # Q38
    {
        "id": 38,
        "question": "In which ancient Indian document do we find numerators written directly over denominators without a bar?",
        "options": ["Sulba Sutras", "Bakhshali Manuscript", "Surya Siddhanta", "Lilavati"],
        "correct": 1,
        "solution": "The Bakhshali Manuscript (~300 CE) contains early mathematical notation where numerators were placed directly above denominators."
    },
    # Q39
    {
        "id": 39,
        "question": "A painter paints 2/7 of a wall on Monday and 3/7 on Tuesday. What fraction of the wall remains unpainted?",
        "options": ["5/7", "2/7", "1/7", "4/7"],
        "correct": 1,
        "solution": "Total painted = 2/7 + 3/7 = 5/7. Remaining unpainted = 1 − 5/7 = 7/7 − 5/7 = 2/7."
    },
    # Q40
    {
        "id": 40,
        "question": "Solve: 1 − 3/8",
        "options": ["5/8", "2/8", "4/8", "1/8"],
        "correct": 0,
        "solution": "Write 1 as 8/8. Then 8/8 − 3/8 = (8 − 3) / 8 = 5/8."
    }
]

def verify_data():
    import json
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    data_str = json.dumps(SLIDES) + json.dumps(QUIZ_QUESTIONS) + json.dumps(CHAPTER_META)
    for word in forbidden:
        if word in data_str:
            raise ValueError(f"Found forbidden LaTeX token: {word}")
    for ch in data_str:
        if 0xD800 <= ord(ch) <= 0xDFFF:
            raise ValueError(f"Found surrogate character: {ch}")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in Fractions data!")

if __name__ == "__main__":
    verify_data()
    # Write self to file
    with open(".agents/class6_math_fractions_data.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch7_fractions_data.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_fractions_data.py")

