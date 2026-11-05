"""
Generate Slides 1 to 8 for NCERT Class 5 Mathematics Chapter 2: Fractions
Joyful Mathematics curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols throughout.
Rich full spoken classroom lectures by Indian Male Teacher (200-240 words per slide).
"""

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Equal Wholes",
        "subtitle": "Why Comparing Fractions Requires Identical Wholes (Chocolates & Parathas)",
        "concept_html": """
            <p class="mb-3">A fraction represents a part of a whole. But here is the fundamental rule of fractions: <strong>to compare two fractions fairly, the whole items from which they are taken must be identical in size!</strong></p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">The Paratha Dilemma</span>
                    <p class="text-xs text-slate-300">If Kabir eats 1/2 of a small baby paratha and Ananya eats 1/2 of a large family paratha, do they eat the same amount? <strong>No!</strong> Ananya eats much more, even though both fractions say 1/2, because the whole parathas were different sizes!</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-sky-400 block mb-1">Chocolate Bar Sharing</span>
                    <p class="text-xs text-slate-300">When two friends share from the <em>same</em> identical chocolate bar, 1/4 of that bar is truly equal for both, and 1/2 is always bigger than 1/4.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Always remember: a fraction is a relative comparison. Always check the size of the whole before comparing fractional shares!</p>
        """,
        "spoken_text": (
            "Welcome young mathematicians to the wonderful world of fractions! Every single day in our homes, we share food: "
            "we break a chocolate bar into equal squares, slice a round paratha for lunch, or pour half a glass of milk. "
            "A fraction simply tells us how many equal parts we take out of a whole. But before we begin calculating, there is "
            "one golden rule you must lock in your memory: to compare any two fractions, the wholes they come from must be "
            "completely identical in size! Imagine two friends having lunch. One friend eats half of a tiny baby paratha, while "
            "another friend eats half of a giant family-sized paratha. Both say they ate one-half, but did they eat the same "
            "amount of food? Certainly not! Half of a giant paratha is much larger than half of a tiny one. Fractions are relative "
            "to their whole. Only when the original whole shapes are identical can we say that one-half is greater than one-fourth. "
            "Look at the interactive paratha comparison simulator on your screen, switch between different whole sizes, and see "
            "why identical wholes are the bedrock of mathematical fairness!"
        ),
        "checkpoints": [
            {
                "question": "Rohit eats 1/2 of a small chocolate bar and Priya eats 1/2 of a mega chocolate bar. Did they eat the same amount of chocolate?",
                "options": [
                    "Yes, because both ate 1/2",
                    "No, because Priya's whole chocolate bar was larger",
                    "No, because Rohit's chocolate was darker",
                    "Yes, fractions always mean equal quantities"
                ],
                "correct": 1,
                "explanation": "Fractions can only be compared directly when the wholes are identical. 1/2 of a larger chocolate is more chocolate than 1/2 of a smaller bar.",
                "study_insight": "A fraction is always a portion of a specific whole; if the wholes differ, the amounts differ."
            },
            {
                "question": "When can we strictly say that 3/4 of a pizza is greater than 1/2 of a pizza?",
                "options": [
                    "Only when the two pizzas are identical in size",
                    "Whenever we like, regardless of pizza sizes",
                    "Only if the pizza has round slices",
                    "Only when eating in a restaurant"
                ],
                "correct": 0,
                "explanation": "To compare fractions mathematically, both fractions must refer to the exact same whole or identical wholes.",
                "study_insight": "Fairness and accuracy in fractions always begin with identical reference wholes."
            }
        ]
    },
    {
        "id": 2,
        "title": "Grid Shading",
        "subtitle": "Visualizing Fractions on Square Grids (Grids A, B, and C)",
        "concept_html": """
            <p class="mb-3">Square grids are wonderful geometric tools for visualizing fractions. When a square grid is divided into equal smaller squares, each tiny square is a unit fraction of the whole grid.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 my-3 text-center">
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-red-500/30">
                    <span class="text-xs font-bold text-red-400 block mb-1">Grid A (16 Squares)</span>
                    <p class="text-[11px] text-slate-300">Shade <strong>1/8</strong> in Red:<br>1/8 of 16 = <strong>2 squares</strong></p>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-400 block mb-1">Grid B (24 Squares)</span>
                    <p class="text-[11px] text-slate-300">Shade <strong>1/6</strong> in Blue:<br>1/6 of 24 = <strong>4 squares</strong></p>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-amber-500/30">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Grid C (36 Squares)</span>
                    <p class="text-[11px] text-slate-300">Shade <strong>1/12</strong> in Yellow:<br>1/12 of 36 = <strong>3 squares</strong></p>
                </div>
            </div>
            <p class="text-xs text-slate-300">To find a fraction of a grid: multiply the total number of squares by the numerator, then divide by the denominator. Notice how different patterns can represent the same fraction!</p>
        """,
        "spoken_text": (
            "Now let us play with square grids! Square grids allow us to see fractions with our own eyes. Imagine you have a square "
            "sheet divided into sixteen identical smaller squares, which we call Grid A. If you want to color one-eighth of this grid in red, "
            "how many squares should you color? We divide the total sixteen squares by eight, which gives two squares! So coloring any "
            "two squares out of sixteen gives exactly one-eighth. Next, take Grid B, which has twenty-four equal squares. To shade "
            "one-sixth in blue, we divide twenty-four by six, which gives four squares. And on Grid C with thirty-six squares, shading "
            "one-twelfth in bright yellow requires thirty-six divided by twelve, which equals three squares! What makes grid shading "
            "truly fascinating is that it does not matter which specific squares you shade: they can be in a straight line, grouped in a "
            "block, or scattered across the grid. As long as the count of shaded squares is correct, the total fractional area remains "
            "identical! Use the interactive grid canvas on your screen to click and shade squares, and watch the fraction counter update!"
        ),
        "checkpoints": [
            {
                "question": "A square grid has 24 equal squares. How many squares must you shade to cover 1/3 of the grid?",
                "options": [
                    "6 squares",
                    "8 squares",
                    "12 squares",
                    "4 squares"
                ],
                "correct": 1,
                "explanation": "To find 1/3 of 24 squares, divide 24 by 3: 24 ÷ 3 = 8 squares.",
                "study_insight": "1/3 of any total is found by dividing the total into 3 equal groups."
            },
            {
                "question": "If 6 squares out of 18 equal squares in a grid are shaded green, what fraction of the grid is shaded?",
                "options": [
                    "1/2",
                    "1/3",
                    "1/6",
                    "1/4"
                ],
                "correct": 1,
                "explanation": "6 out of 18 is 6/18. Dividing numerator and denominator by 6 gives 1/3.",
                "study_insight": "Grouping 18 squares into 3 equal sets of 6 proves that 6/18 equals 1/3."
            }
        ]
    },
    {
        "id": 3,
        "title": "Fraction Kit",
        "subtitle": "Exploring Physical Fraction Strips and Building Wholes",
        "concept_html": """
            <p class="mb-3">A <strong>Fraction Kit</strong> consists of colorful rectangular strips of identical total length, each cut into different equal fractional pieces: 1 (whole), 1/2 (halves), 1/4 (fourths), 1/8 (eighths), and 1/16 (sixteenths).</p>
            <div class="space-y-2 my-3 font-mono text-xs">
                <div class="p-2 rounded bg-amber-500/20 border border-amber-500/40 text-amber-300 text-center font-bold">1 Whole Strip</div>
                <div class="grid grid-cols-2 gap-1 text-center">
                    <div class="p-1.5 rounded bg-blue-500/20 border border-blue-500/40 text-blue-300 font-bold">1/2</div>
                    <div class="p-1.5 rounded bg-blue-500/20 border border-blue-500/40 text-blue-300 font-bold">1/2</div>
                </div>
                <div class="grid grid-cols-4 gap-1 text-center">
                    <div class="p-1.5 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold">1/4</div>
                    <div class="p-1.5 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold">1/4</div>
                    <div class="p-1.5 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold">1/4</div>
                    <div class="p-1.5 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold">1/4</div>
                </div>
            </div>
            <p class="text-xs text-slate-300">By aligning pieces side-by-side, students physically experience how smaller fractional parts combine to match the length of larger pieces and recreate the complete whole strip.</p>
        """,
        "spoken_text": (
            "In your mathematics classroom, one of the most exciting tools you will use is the Fraction Kit! Imagine taking long, "
            "colorful strips of paper that all have the exact same length. The first strip is left whole, colored in warm amber, representing "
            "the number one. The second strip is folded precisely in the middle and cut into two equal pieces, giving two blue pieces labeled "
            "one-half. The third strip is folded in half and in half again, creating four equal green pieces labeled one-fourth. And if you fold "
            "further, you get eight purple pieces labeled one-eighth! When you place these strips next to each other on your desk, "
            "mathematical relationships become crystal clear. You can physically see that two one-half pieces stretch out to match the full "
            "length of the whole strip. Four one-fourth pieces fit snugly together to make one whole, and eight one-eighth pieces do the "
            "exact same thing! The fraction kit transforms abstract numbers into touchable, visual building blocks. Use the interactive "
            "strip builder on your screen to drag and snap pieces together, and watch how fractions combine to create perfect wholes!"
        ),
        "checkpoints": [
            {
                "question": "How many 1/4 strips from the fraction kit are needed to equal the length of one 1/2 strip?",
                "options": [
                    "1 piece",
                    "2 pieces",
                    "4 pieces",
                    "3 pieces"
                ],
                "correct": 1,
                "explanation": "1/4 + 1/4 = 2/4 = 1/2. Exactly two 1/4 pieces match the length of one 1/2 piece.",
                "study_insight": "Because 4 is twice 2, each fourth is half the size of a half, so two fourths make one half."
            },
            {
                "question": "How many 1/8 pieces are needed to make one complete whole strip?",
                "options": [
                    "4 pieces",
                    "6 pieces",
                    "8 pieces",
                    "16 pieces"
                ],
                "correct": 2,
                "explanation": "The denominator 8 means the whole is divided into 8 equal parts. So 8 pieces of 1/8 make 8/8 = 1 whole.",
                "study_insight": "The denominator tells you exactly how many equal parts make the whole."
            }
        ]
    },
    {
        "id": 4,
        "title": "Piece Relations",
        "subtitle": "Discovering Equivalence and Part-to-Part Proportions",
        "concept_html": """
            <p class="mb-3">By comparing different pieces from our Fraction Kit, we uncover precise mathematical relationships connecting halves, fourths, eighths, and sixteenths.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Fitting Halves and Fourths</span>
                    <p class="text-xs text-slate-300">• Two 1/4 pieces = <strong>1/2</strong> (2/4 = 1/2)<br>• Four 1/4 pieces = <strong>1 Whole</strong> (4/4 = 1)<br>• Four 1/8 pieces = <strong>1/2</strong> (4/8 = 1/2)</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">Fitting Eighths and Sixteenths</span>
                    <p class="text-xs text-slate-300">• Two 1/8 pieces = <strong>1/4</strong> (2/8 = 1/4)<br>• Two 1/16 pieces = <strong>1/8</strong> (2/16 = 1/8)<br>• Eight 1/8 pieces = <strong>1 Whole</strong> (8/8 = 1)</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Notice the pattern: as the denominator doubles, the size of each piece is halved. Therefore, you need twice as many pieces to cover the same length!</p>
        """,
        "spoken_text": (
            "Now let us examine how the different pieces of our fraction kit relate to one another like members of a mathematical family! "
            "When you lay down a one-half strip, take two one-fourth pieces and place them directly on top. They match edge to edge! "
            "This proves visually that two-fourths is exactly equal to one-half. Now, take one-eighth pieces. How many one-eighth pieces "
            "do you think will cover one-fourth? Two one-eighth pieces cover one-fourth perfectly! And how many one-eighth pieces cover "
            "one-half? Exactly four one-eighth pieces! Do you see the marvelous pattern unfolding here? Whenever the denominator doubles—"
            "from two to four, or four to eight—the size of each individual piece becomes half as wide. Because each piece is cut in half, "
            "you need twice as many pieces to cover the exact same distance! That is why two-fourths, four-eighths, and eight-sixteenths "
            "all represent the exact same half of the strip. Use the interactive comparison bench on your screen to snap pieces together "
            "and watch how smaller parts combine into larger equivalents!"
        ),
        "checkpoints": [
            {
                "question": "If you have three 1/4 pieces and two 1/8 pieces, what total fraction of the whole strip do you have?",
                "options": [
                    "3/4",
                    "7/8",
                    "1 Whole",
                    "5/8"
                ],
                "correct": 2,
                "explanation": "Two 1/8 pieces equal 1/4 (2/8 = 1/4). So three 1/4 pieces + one 1/4 piece = four 1/4 pieces = 4/4 = 1 Whole!",
                "study_insight": "Converting 2/8 to 1/4 makes addition of like parts effortless."
            },
            {
                "question": "How many 1/8 pieces are needed to match the length of three 1/4 pieces?",
                "options": [
                    "3 pieces",
                    "4 pieces",
                    "6 pieces",
                    "8 pieces"
                ],
                "correct": 2,
                "explanation": "Each 1/4 piece equals two 1/8 pieces. So three 1/4 pieces = 3 × 2 = six 1/8 pieces (6/8 = 3/4).",
                "study_insight": "Multiplying the numerator and denominator by 2 reveals that 3/4 = 6/8."
            }
        ]
    },
    {
        "id": 5,
        "title": "Building Wholes",
        "subtitle": "Combining Unlike Fraction Pieces to Reconstruct the Whole",
        "concept_html": """
            <p class="mb-3">In our textbook exercises, we practice puzzle grouping to build a complete whole using creative mixtures of different fraction pieces, such as combining thirds, sixths, and twelfths, or halves and fourths.</p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-amber-400 block mb-2">Sample Whole-Building Recipes</span>
                <ul class="text-xs text-slate-300 space-y-1.5 list-disc list-inside">
                    <li><strong>Recipe 1:</strong> 1/2 + 1/4 + 1/4 = <strong>1 Whole</strong></li>
                    <li><strong>Recipe 2:</strong> 1/2 + 1/4 + 1/8 + 1/8 = <strong>1 Whole</strong></li>
                    <li><strong>Recipe 3:</strong> 1/3 + 2/6 + 4/12 = 1/3 + 1/3 + 1/3 = <strong>1 Whole</strong></li>
                    <li><strong>Recipe 4:</strong> 1/2 + 3/6 = 1/2 + 1/2 = <strong>1 Whole</strong></li>
                </ul>
            </div>
            <p class="text-xs text-slate-300">Just like preparing a recipe in the kitchen with half cups and quarter spoons, different fractional portions sum together harmoniously to form complete units.</p>
        """,
        "spoken_text": (
            "Building a complete whole using a combination of different fraction pieces is just like solving a jigsaw puzzle! "
            "You do not always have to use pieces of the same color. Suppose you have one blue strip of one-half. To complete the whole, "
            "you still need another half. But what if you do not have another one-half piece? You can use two green one-fourth pieces instead! "
            "One-half plus one-fourth plus one-fourth gives one complete whole. What if you only have one one-fourth piece and some eighths? "
            "You can take one-half, add one-fourth, and then add two one-eighth pieces! One-half plus one-fourth plus two-eighths equals "
            "one whole. We can even do this with thirds, sixths, and twelfths. One-third plus two-sixths plus four-twelfths is really "
            "one-third plus one-third plus one-third, which equals three-thirds, or one whole! In daily life, a chef in the kitchen often "
            "combines a half-cup of milk, a quarter-cup of curd, and two one-eighth cups of water to fill a measuring jar. Test your puzzle "
            "skills on the interactive whole builder on your screen: select different piece combinations and verify if they fill the whole bar completely!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following combinations of fraction pieces equals exactly 1 Whole?",
                "options": [
                    "1/2 + 1/4 + 1/8",
                    "1/2 + 1/4 + 2/8",
                    "1/4 + 1/4 + 1/4",
                    "1/2 + 1/3"
                ],
                "correct": 1,
                "explanation": "2/8 = 1/4. So 1/2 + 1/4 + 2/8 = 1/2 + 1/4 + 1/4 = 1/2 + 1/2 = 1 Whole.",
                "study_insight": "Simplify smaller pieces to like denominators to quickly check if they reach 1."
            },
            {
                "question": "If you already have 2/3 of a cake, what fraction piece must you add to make 1 Whole cake?",
                "options": [
                    "1/2",
                    "1/3",
                    "1/4",
                    "2/6"
                ],
                "correct": 1,
                "explanation": "1 Whole = 3/3. 3/3 - 2/3 = 1/3. Note that 2/6 is also equivalent to 1/3, but 1/3 is the direct unit piece.",
                "study_insight": "3 parts out of 3 make the whole, so 2 parts need 1 more part."
            }
        ]
    },
    {
        "id": 6,
        "title": "Equivalent Fractions",
        "subtitle": "Visualizing Different Names for the Exact Same Shaded Region",
        "concept_html": """
            <p class="mb-3">Imagine a chocolate bar divided into 3 equal columns. If you shade 1 column, you have shaded <strong>1/3</strong>. Now draw a horizontal cut dividing the bar into 2 equal rows: you now have 6 smaller rectangles, and 2 are shaded! The shaded region has not changed at all, but its name is now <strong>2/6</strong>.</p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3 text-center">
                <span class="text-xs font-bold text-sky-400 block mb-2">The Equivalence Chain</span>
                <div class="flex items-center justify-center space-x-2 font-mono text-sm text-amber-300 font-bold">
                    <span>1/3</span>
                    <span>=</span>
                    <span>2/6</span>
                    <span>=</span>
                    <span>3/9</span>
                    <span>=</span>
                    <span>4/12</span>
                    <span>=</span>
                    <span>5/15</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-2">Rule: Multiply or divide both numerator and denominator by the <em>same non-zero number</em> to generate equivalent fractions.</p>
            </div>
            <p class="text-xs text-slate-300">Equivalent fractions look different because they have different numbers, but they represent the <strong>exact same value and area</strong>.</p>
        """,
        "spoken_text": (
            "Let us explore one of the most powerful concepts in all of mathematics: Equivalent Fractions! The word equivalent comes "
            "from equal value. Equivalent fractions are simply different names for the exact same amount! Picture a chocolate bar divided "
            "into three long vertical strips. If you eat one strip, you have eaten one-third of the chocolate. Now, imagine taking a knife "
            "and cutting the entire chocolate bar horizontally across the middle. Each of the three strips is sliced into two pieces, making "
            "six pieces in total. How many pieces do you have now? You have two pieces out of six! Notice that the amount of chocolate "
            "on your plate has not changed by even a single crumb! You still have the exact same chocolate, but now its name is two-sixths. "
            "If we cut the original bar into three rows, we get three-ninths. If we cut it into four rows, we get four-twelfths! All of these—"
            "one-third, two-sixths, three-ninths, and four-twelfths—are equivalent fractions. Mathematically, whenever you multiply both "
            "the numerator and the denominator by the same number, you are simply cutting the parts into smaller pieces without changing "
            "the total amount! Use the horizontal cutter simulator on your screen to slice rectangles and watch equivalent fractions appear!"
        ),
        "checkpoints": [
            {
                "question": "Which fraction is equivalent to 1/3?",
                "options": [
                    "2/5",
                    "3/9",
                    "2/8",
                    "3/6"
                ],
                "correct": 1,
                "explanation": "Multiplying numerator and denominator of 1/3 by 3 gives (1 × 3) / (3 × 3) = 3/9.",
                "study_insight": "Multiplying top and bottom by the same number preserves the fractional value."
            },
            {
                "question": "If you multiply both the numerator and denominator of 3/5 by 4, what equivalent fraction do you get?",
                "options": [
                    "12/20",
                    "7/9",
                    "12/15",
                    "9/20"
                ],
                "correct": 0,
                "explanation": "(3 × 4) / (5 × 4) = 12/20. Both 3/5 and 12/20 represent the exact same portion.",
                "study_insight": "Multiplying numerator and denominator by 4 divides each fifth into 4 smaller twentieths."
            }
        ]
    },
    {
        "id": 7,
        "title": "Equal Names",
        "subtitle": "Finding Missing Numerators and Denominators in Equivalence Equations",
        "concept_html": """
            <p class="mb-3">To find a missing numerator or denominator in an equivalent fraction statement, find the multiplier connecting the known terms and apply it to the other term.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Example 1: 2/5 = ?/10</span>
                    <p class="text-xs text-slate-300">Look at the denominators: from 5 to 10, we multiplied by 2 (5 × 2 = 10).<br>
                    Therefore, multiply the numerator by 2 as well:<br>
                    2 × 2 = <strong>4</strong>.<br>
                    So, <strong>2/5 = 4/10</strong>!</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Example 2: 3/4 = 9/?</span>
                    <p class="text-xs text-slate-300">Look at the numerators: from 3 to 9, we multiplied by 3 (3 × 3 = 9).<br>
                    Therefore, multiply the denominator by 3 as well:<br>
                    4 × 3 = <strong>12</strong>.<br>
                    So, <strong>3/4 = 9/12</strong>!</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Cross-multiplication check: in any true equivalent fraction pair a/b = c/d, the cross products are equal: a × d = b × c!</p>
        """,
        "spoken_text": (
            "Now let us master the skill of solving equivalent fraction puzzles by finding missing numerators and denominators! "
            "Think of an equivalence statement as a balanced scale: whatever operation happens to the denominator must also happen "
            "to the numerator. Suppose you are given the puzzle: two-fifths equals box over ten. How do you find the missing number in the box? "
            "First, look at the known pair: the denominators five and ten. How did five become ten? We multiplied five by two! To keep "
            "the fraction balanced and equivalent, we must do the exact same thing to the numerator: multiply two by two. Two multiplied "
            "by two is four! Therefore, the missing numerator is four, and two-fifths equals four-tenths! Now consider another puzzle: "
            "three-fourths equals nine over box. Here, we look at the numerators: three became nine by multiplying by three. So we multiply "
            "the denominator four by three, which gives twelve! Three-fourths equals nine-twelfths. You can always check your answer "
            "using cross-multiplication: three multiplied by twelve is thirty-six, and four multiplied by nine is thirty-six! Test your "
            "skills on the interactive equivalence balance on your screen by filling in the missing boxes!"
        ),
        "checkpoints": [
            {
                "question": "Find the missing numerator: 3/7 = ?/21",
                "options": [
                    "6",
                    "9",
                    "12",
                    "15"
                ],
                "correct": 1,
                "explanation": "From 7 to 21, we multiplied by 3 (7 × 3 = 21). So multiply the numerator by 3: 3 × 3 = 9. Thus 3/7 = 9/21.",
                "study_insight": "Whatever scale factor is applied to the denominator must be applied to the numerator."
            },
            {
                "question": "Find the missing denominator: 4/5 = 16/?",
                "options": [
                    "15",
                    "20",
                    "25",
                    "18"
                ],
                "correct": 1,
                "explanation": "From 4 to 16, we multiplied by 4 (4 × 4 = 16). So multiply the denominator by 4: 5 × 4 = 20. Thus 4/5 = 16/20.",
                "study_insight": "Checking with cross multiplication: 4 × 20 = 80, and 5 × 16 = 80."
            }
        ]
    },
    {
        "id": 8,
        "title": "Same Denominator",
        "subtitle": "Comparing Fractions When Part Sizes are Equal (Chikki Slices)",
        "concept_html": """
            <p class="mb-3">When two fractions have the <strong>same denominator</strong>, it means the whole has been divided into parts of the <strong>exact same size</strong>.</p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-amber-400 block mb-1">Comparing 1/3 and 2/3 of a Chikki</span>
                <p class="text-xs text-slate-300">Imagine a crunchy peanut chikki divided into 3 equal pieces. Each piece is 1/3.<br>
                • Aarav gets 1 piece = <strong>1/3</strong><br>
                • Meera gets 2 pieces = <strong>2/3</strong><br>
                Since each piece is identical in size, having 2 pieces is clearly more than having 1 piece!<br>
                Therefore: <strong>2/3 > 1/3</strong> (or <strong>1/3 < 2/3</strong>).</p>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-300">
                <strong>Golden Rule for Same Denominator:</strong> Simply compare the numerators! The fraction with the greater numerator is the larger fraction. (e.g., 5/8 > 3/8 because 5 > 3).
            </div>
        """,
        "spoken_text": (
            "Now let us learn how to compare fractions! The easiest comparison in fractions happens when both fractions share the "
            "exact same denominator. Remember what the denominator tells us: it tells us how many equal parts the whole is divided into. "
            "So if two fractions have the same denominator, every single piece in both fractions has the exact same size! Picture a rectangular "
            "peanut chikki bar broken into three equal pieces. Each piece is one-third of the chikki. If your friend takes one piece, they have "
            "one-third. If you take two pieces, you have two-thirds. Who has more chikki? You do, of course! Two pieces of the same size are "
            "naturally more than one piece. Therefore, two-thirds is greater than one-third. The golden rule is delightfully simple: "
            "when denominators are identical, just look at the numerators! The fraction with the larger numerator is always greater. "
            "For example, five-eighths is greater than three-eighths because five pieces are more than three pieces. Seven-tenths is greater "
            "than four-tenths. Use the chikki sharing simulator on your screen to adjust the numerators and observe how inequality signs "
            "change with the number of slices!"
        ),
        "checkpoints": [
            {
                "question": "Which sign correctly compares 5/7 and 3/7?",
                "options": [
                    "5/7 < 3/7",
                    "5/7 > 3/7",
                    "5/7 = 3/7",
                    "Cannot be determined"
                ],
                "correct": 1,
                "explanation": "Both fractions have the same denominator (7). Comparing numerators: 5 > 3, so 5/7 > 3/7.",
                "study_insight": "With like denominators, more parts mean a larger total portion."
            },
            {
                "question": "Arrange in increasing (ascending) order: 5/9, 2/9, 7/9, 1/9.",
                "options": [
                    "7/9, 5/9, 2/9, 1/9",
                    "1/9, 2/9, 5/9, 7/9",
                    "2/9, 1/9, 5/9, 7/9",
                    "1/9, 5/9, 2/9, 7/9"
                ],
                "correct": 1,
                "explanation": "Since all denominators are 9, we sort by numerators: 1 < 2 < 5 < 7. So: 1/9 < 2/9 < 5/9 < 7/9.",
                "study_insight": "When denominators match, ascending order corresponds directly to ascending numerators."
            }
        ]
    }
]

print("Slides 1 to 8 authored successfully.")

