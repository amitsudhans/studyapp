"""
Generate Slides 9 to 16 for NCERT Class 5 Mathematics Chapter 2: Fractions
Joyful Mathematics curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols throughout.
Rich full spoken classroom lectures by Indian Male Teacher (200-240 words per slide).
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Same Numerator",
        "subtitle": "Comparing Fractions When Part Counts are Equal but Sizes Differ",
        "concept_html": """
            <p class="mb-3">What happens when two fractions have the <strong>same numerator</strong> but <strong>different denominators</strong>, such as comparing <strong>4/6</strong> and <strong>4/5</strong> of a paratha?</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-sky-400 block mb-1">Part Size Comparison</span>
                    <p class="text-xs text-slate-300">A paratha cut into 5 equal pieces has larger slices than a paratha cut into 6 equal pieces.<br>
                    Therefore, <strong>1/5 piece > 1/6 piece</strong>.</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Taking 4 Pieces of Each</span>
                    <p class="text-xs text-slate-300">Taking 4 pieces of the smaller size (4 × 1/6) is less than taking 4 pieces of the larger size (4 × 1/5).<br>
                    Therefore: <strong>4/6 < 4/5</strong> (or <strong>4/5 > 4/6</strong>)!</p>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-300">
                <strong>Golden Rule for Same Numerator:</strong> The fraction with the <em>smaller denominator</em> has larger individual pieces, making it the <strong>larger fraction</strong>! (e.g., 3/4 > 3/8 because fourths are bigger than eighths).
            </div>
        """,
        "spoken_text": (
            "Now here is a fascinating question that surprises many students: what happens when two fractions have the exact same "
            "numerator, but different denominators? For example, which is bigger: four-sixths of a paratha, or four-fifths of an "
            "identical paratha? Let us think carefully about the meaning of the denominator. If you divide a round paratha among five friends, "
            "each piece is one-fifth. If you divide that same paratha among six friends, you have to cut it into more slices, so each slice "
            "becomes smaller! This means one-fifth is distinctly larger than one-sixth. Now, both fractions have the numerator four, meaning "
            "you are taking four slices of each! Taking four large slices of one-fifth gives you much more food than taking four smaller "
            "slices of one-sixth. Therefore, four-fifths is greater than four-sixths! Notice the surprising rule: when numerators are the "
            "same, the fraction with the smaller denominator is actually the larger fraction! Why? Because fewer cuts make bigger pieces! "
            "Three-fourths is larger than three-eighths. Two-thirds is larger than two-fifths. Use the interactive paratha slice comparator "
            "on your screen to toggle slice sizes and see why smaller denominators give larger shares!"
        ),
        "checkpoints": [
            {
                "question": "Which fraction is larger: 3/5 or 3/7?",
                "options": [
                    "3/7, because 7 is greater than 5",
                    "3/5, because fifths are larger pieces than sevenths",
                    "Both are equal because both numerators are 3",
                    "Cannot be determined without a calculator"
                ],
                "correct": 1,
                "explanation": "When numerators are equal, the fraction with the smaller denominator has larger pieces. Since 5 < 7, 1/5 > 1/7, so 3/5 > 3/7.",
                "study_insight": "Fewer cuts mean bigger slices: fifths are bigger than sevenths."
            },
            {
                "question": "Insert the correct symbol: 5/8 ___ 5/6",
                "options": [
                    ">",
                    "<",
                    "=",
                    "+"
                ],
                "correct": 1,
                "explanation": "Since eighths are smaller than sixths (1/8 < 1/6), 5 eighths is less than 5 sixths: 5/8 < 5/6.",
                "study_insight": "A larger denominator with the same numerator indicates a smaller overall value."
            }
        ]
    },
    {
        "id": 10,
        "title": "Greater Than One",
        "subtitle": "Discovering Fractions Beyond One Whole (5/2, 9/4, and Sharing Parathas)",
        "concept_html": """
            <p class="mb-3">Can a fraction be larger than 1 whole? <strong>Yes!</strong> In everyday life, when we share multiple items, we frequently encounter quantities greater than 1.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-amber-400 block mb-1">Sharing 5 Halves of Paratha</span>
                    <p class="text-xs text-slate-300">Suppose you have 5 half-parathas (5 × 1/2). That is <strong>5/2</strong>.<br>
                    • Two halves make 1 whole paratha.<br>
                    • Another two halves make a 2nd whole paratha.<br>
                    • 1 half is left over.<br>
                    So 5/2 = <strong>2 whole parathas and 1/2</strong>!</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Improper Fractions</span>
                    <p class="text-xs text-slate-300">When the <strong>numerator is greater than or equal to the denominator</strong> (like 5/2, 9/4, 7/3), it is called an <strong>improper fraction</strong>, and its value is <strong>greater than or equal to 1</strong>.</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Fractions where the numerator is smaller than the denominator (like 1/2, 3/4) are called proper fractions, and they are always less than 1.</p>
        """,
        "spoken_text": (
            "Up until now, we have mostly looked at fractions that are smaller than one whole, like half a glass of juice or a quarter "
            "of a pizza. But what happens when you have more than one whole? Suppose your family makes fresh, hot parathas for breakfast. "
            "Each paratha is cut into two equal halves. If you eat five of these half-slices, what fraction have you eaten? You have eaten "
            "five halves, written as five over two! Notice that the top number, five, is greater than the bottom number, two. Whenever "
            "the numerator is larger than the denominator, we call it an improper fraction, and its value is strictly greater than one! "
            "Think about those five half-slices: the first two halves join together to make one whole paratha. The next two halves make a "
            "second whole paratha. And you still have one half-slice left! So eating five-halves is the exact same as eating two whole "
            "parathas plus one-half paratha. That is two and a half! Similarly, if you have nine quarter-slices of pizza, nine over four "
            "gives two whole pizzas and one-fourth left over. Use the paratha assembly simulator on your screen to bundle slices together "
            "and see how fractions naturally extend beyond one whole!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following is a fraction greater than 1 (an improper fraction)?",
                "options": [
                    "3/4",
                    "5/6",
                    "7/4",
                    "2/3"
                ],
                "correct": 2,
                "explanation": "In 7/4, the numerator 7 is greater than the denominator 4. 7/4 = 1 Whole and 3/4, which is greater than 1.",
                "study_insight": "Whenever numerator > denominator, the fraction represents more than 1 whole."
            },
            {
                "question": "If you have 8 quarter-pieces (8 × 1/4) of a sandwich, how many whole sandwiches do you have?",
                "options": [
                    "1 sandwich",
                    "2 sandwiches",
                    "4 sandwiches",
                    "8 sandwiches"
                ],
                "correct": 1,
                "explanation": "Every 4 fourths make 1 whole sandwich. 8/4 = 8 ÷ 4 = 2 whole sandwiches.",
                "study_insight": "Dividing numerator by denominator converts improper fractions to whole units."
            }
        ]
    },
    {
        "id": 11,
        "title": "Mixed Numbers",
        "subtitle": "Plotting Improper Fractions on the Number Line and Converting to Mixed Numbers",
        "concept_html": """
            <p class="mb-3">A <strong>mixed number</strong> combines a whole number and a proper fraction together (e.g., 2 1/2, read as <em>two and a half</em>).</p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-sky-400 block mb-1">Conversion Steps: Improper Fraction to Mixed Number</span>
                <p class="text-xs text-slate-300">Divide the numerator by the denominator:<br>
                • <strong>Quotient</strong> becomes the <em>Whole Number</em>.<br>
                • <strong>Remainder</strong> becomes the new <em>Numerator</em>.<br>
                • <strong>Divisor</strong> remains the <em>Denominator</em>.<br>
                <em>Example:</em> Convert <strong>9/4</strong>:<br>
                9 ÷ 4 = 2 with remainder 1 &rarr; <strong>9/4 = 2 1/4</strong> (two and one-fourth).</p>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-300">
                <strong>Number Line Position:</strong> 2 1/4 lies between 2 and 3 on the number line, exactly one-quarter of the way past 2!
            </div>
        """,
        "spoken_text": (
            "Now let us connect improper fractions to the number line by learning about Mixed Numbers! A mixed number is a happy union "
            "of two mathematical parts: a whole number standing proudly on the left, and a proper fraction sitting beside it. Take the "
            "improper fraction nine-fourths. How do we write nine-fourths as a mixed number? We simply divide the numerator by the denominator! "
            "Divide nine by four. Four goes into nine two times, because four multiplied by two is eight. That quotient of two gives us two "
            "complete whole units! When you subtract eight from nine, you have a remainder of one. That remainder one becomes our new "
            "numerator, sitting over the original denominator four. So nine-fourths is written as two and one-fourth! Now imagine looking at "
            "a number line marked with zero, one, two, and three. Where does two and one-fourth sit? It sits past two, right in the interval "
            "between two and three, exactly one-quarter of the distance towards three! Converting between improper fractions and mixed "
            "numbers allows us to instantly visualize how big a quantity really is. Use the number line slider on your screen to jump "
            "between whole numbers and fractions, and watch the mixed number conversions happen dynamically!"
        ),
        "checkpoints": [
            {
                "question": "What is the improper fraction 11/3 written as a mixed number?",
                "options": [
                    "3 1/3",
                    "3 2/3",
                    "2 2/3",
                    "4 1/3"
                ],
                "correct": 1,
                "explanation": "11 ÷ 3 = 3 with remainder 2. So 11/3 = 3 2/3 (three and two-thirds).",
                "study_insight": "3 × 3 = 9, and 9 + 2 = 11, verifying that 3 2/3 = 11/3."
            },
            {
                "question": "Between which two consecutive whole numbers does 17/5 lie on the number line?",
                "options": [
                    "Between 1 and 2",
                    "Between 2 and 3",
                    "Between 3 and 4",
                    "Between 4 and 5"
                ],
                "correct": 2,
                "explanation": "17 ÷ 5 = 3 with remainder 2 (3 2/5). Since it is 3 plus 2/5, it lies between 3 and 4 on the number line.",
                "study_insight": "The whole number part of a mixed number identifies its preceding whole number on the line."
            }
        ]
    },
    {
        "id": 12,
        "title": "Benchmark One",
        "subtitle": "Using Whole Number 1 as a Benchmark to Compare Fractions",
        "concept_html": """
            <p class="mb-3">When comparing two fractions, you do not always need to calculate common denominators! Often, you can simply compare both fractions to the <strong>benchmark of 1 (a whole)</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-rose-400 block mb-1">Less Than 1 Whole</span>
                    <p class="text-xs text-slate-300">If numerator < denominator, the fraction is <strong>less than 1</strong>.<br>
                    <em>Example:</em> <strong>7/8 < 1</strong> (needs 1/8 more to make a whole).</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Greater Than 1 Whole</span>
                    <p class="text-xs text-slate-300">If numerator > denominator, the fraction is <strong>greater than 1</strong>.<br>
                    <em>Example:</em> <strong>8/6 > 1</strong> (equals 1 2/6, more than a whole).</p>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs text-amber-200">
                <strong>Instant Comparison:</strong> Since 7/8 is less than 1, and 8/6 is greater than 1, we know immediately that <strong>7/8 < 8/6</strong> without any common denominator calculations!
            </div>
        """,
        "spoken_text": (
            "Here is a brilliant mental math shortcut that real mathematicians use every day: benchmark comparisons! Often, when two "
            "fractions look complicated to compare, you do not need to do long calculations or find common denominators. All you need to do "
            "is compare each fraction to the benchmark number one! Ask yourself: is this fraction less than one whole, or greater than one "
            "whole? Consider this comparison: which is larger, seven-eighths or eight-sixths? Look at seven-eighths: the numerator seven is "
            "smaller than eight, which means you have seven slices out of an eight-slice pizza. You still need one more slice to make a whole, "
            "so seven-eighths is strictly less than one. Now look at eight-sixths: the numerator eight is greater than six, which means you have "
            "one whole pizza plus two extra slices! Eight-sixths is greater than one. Since seven-eighths is less than one, and eight-sixths "
            "is greater than one, seven-eighths is unquestionably smaller than eight-sixths! Just by comparing both fractions to the benchmark "
            "of one whole, we solved the problem in two seconds flat. Use the benchmark scale on your screen to test different pairs and "
            "watch how the benchmark one instantly separates smaller from larger fractions!"
        ),
        "checkpoints": [
            {
                "question": "Compare 5/6 and 7/5 using 1 as a benchmark:",
                "options": [
                    "5/6 > 7/5",
                    "5/6 < 7/5",
                    "5/6 = 7/5",
                    "Cannot be compared"
                ],
                "correct": 1,
                "explanation": "5/6 is less than 1 (numerator < denominator). 7/5 is greater than 1 (numerator > denominator). Therefore, 5/6 < 7/5.",
                "study_insight": "Any proper fraction is always smaller than any improper fraction."
            },
            {
                "question": "Which of these fractions is strictly LESS than 1?",
                "options": [
                    "9/8",
                    "4/3",
                    "11/12",
                    "6/5"
                ],
                "correct": 2,
                "explanation": "In 11/12, numerator 11 is less than denominator 12, so 11/12 < 1. All other options have numerator > denominator.",
                "study_insight": "A proper fraction requires more parts to reach 1 whole."
            }
        ]
    },
    {
        "id": 13,
        "title": "Benchmark Half",
        "subtitle": "Using 1/2 as a Benchmark to Evaluate and Compare Fractions",
        "concept_html": """
            <p class="mb-3">Another powerful benchmark is <strong>one-half (1/2)</strong>. To check whether a fraction is less than, equal to, or greater than 1/2, compare its numerator to <strong>half of its denominator</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 my-3 text-center">
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-blue-500/30">
                    <span class="text-xs font-bold text-blue-400 block mb-1">Equal to 1/2</span>
                    <p class="text-[11px] text-slate-300">Numerator = Half of Denominator<br>• <strong>3/6</strong> (3 is half of 6)<br>• <strong>4/8</strong> (4 is half of 8)</p>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-emerald-500/30">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Greater than 1/2</span>
                    <p class="text-[11px] text-slate-300">Numerator > Half of Denominator<br>• <strong>5/8</strong> (5 > 4)<br>• <strong>7/10</strong> (7 > 5)</p>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-rose-500/30">
                    <span class="text-xs font-bold text-rose-400 block mb-1">Less than 1/2</span>
                    <p class="text-[11px] text-slate-300">Numerator < Half of Denominator<br>• <strong>2/6</strong> (2 < 3)<br>• <strong>3/8</strong> (3 < 4)</p>
                </div>
            </div>
            <p class="text-xs text-slate-300">Example: Compare 3/8 and 5/8. Half of 8 is 4. 3/8 is less than 1/2, while 5/8 is greater than 1/2. Thus, <strong>3/8 < 5/8</strong>!</p>
        """,
        "spoken_text": (
            "Just as we used the number one as a benchmark, we can also use one-half as a powerful comparison landmark! "
            "How do you know if a fraction is equal to, greater than, or less than one-half? You simply look at its denominator, find half "
            "of that denominator, and compare it to the numerator! Let us practice. Take the fraction three-sixths. What is half of six? "
            "Half of six is three. Since the numerator is exactly three, three-sixths is equal to one-half! Now take five-eighths. What is half "
            "of eight? Half of eight is four. The numerator five is greater than four, so five-eighths is greater than one-half! Now look at "
            "two-sixths. The numerator two is less than three, so two-sixths is less than one-half. Now imagine you are asked to compare "
            "two-sixths and five-eighths. Instead of cross-multiplying, just glance at the benchmark of one-half: two-sixths is less than "
            "half, and five-eighths is more than half! Therefore, two-sixths is immediately smaller than five-eighths. Using benchmarks "
            "builds strong mathematical intuition and number sense. Test different fractions on the interactive benchmark meter on your "
            "screen to see them sort into less than half, exactly half, and greater than half!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following fractions is strictly GREATER than 1/2?",
                "options": [
                    "3/8",
                    "4/10",
                    "5/8",
                    "2/6"
                ],
                "correct": 2,
                "explanation": "Half of 8 is 4. In 5/8, the numerator 5 is greater than 4, so 5/8 > 1/2. For all other options, numerator < half denominator.",
                "study_insight": "Check numerator against half of denominator: 5 > 4 means greater than 1/2."
            },
            {
                "question": "Which fraction is exactly equal to 1/2?",
                "options": [
                    "5/12",
                    "6/12",
                    "7/12",
                    "8/12"
                ],
                "correct": 1,
                "explanation": "Half of 12 is 6. So 6/12 = 1/2. (Dividing top and bottom by 6 gives 1/2).",
                "study_insight": "When the numerator is exactly half the denominator, the fraction simplifies to 1/2."
            }
        ]
    },
    {
        "id": 14,
        "title": "Ant Parade",
        "subtitle": "Word Problem: Calculating the Total Length of 16 Marching Ants",
        "concept_html": """
            <p class="mb-3">In the <strong>Try This</strong> section of Chapter 2, students encounter a charming nature puzzle: <em>A line of 16 tiny ants is walking one after the other in a straight parade. If each ant measures 1/4 cm in length, what is the total length of the entire ant parade?</em></p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-amber-400 block mb-1">Mathematical Solution Steps</span>
                <p class="text-xs text-slate-300">Each ant = <strong>1/4 cm</strong>.<br>
                Total number of ants = <strong>16</strong>.<br>
                Total parade length = 16 × 1/4 cm = <strong>16/4 cm</strong>.<br>
                Now divide 16 by 4:<br>
                16 ÷ 4 = <strong>4 cm</strong>!</p>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-300">
                <strong>Number Line Hop:</strong> On a centimetre ruler, 4 ants make 1 cm (4 × 1/4 = 1). The next 4 ants make 2 cm, the next 4 make 3 cm, and the final 4 ants reach exactly <strong>4 cm</strong>!
            </div>
        """,
        "spoken_text": (
            "Now let us solve a delightful real-world puzzle from the Try This section of your textbook: The Ant Parade! Imagine looking down "
            "at your garden path and watching a disciplined line of sixteen tiny worker ants marching one right behind the other in a perfect "
            "straight parade. Each little ant measures exactly one-fourth of a centimetre in length. The question asks: what is the total "
            "length of the entire sixteen-ant parade from the head of the first ant to the tail of the last ant? Let us calculate this step by step! "
            "Every single ant contributes one-fourth of a centimetre. So with sixteen ants, the total length is sixteen multiplied by one-fourth, "
            "which gives the improper fraction sixteen over four centimetres. Now, what is sixteen divided by four? Sixteen divided by four is "
            "exactly four! So the entire parade measures four centimetres long! You can also visualize this using groups of four: four ants "
            "join together to make one full centimetre. The next four ants make a second centimetre. The next four make a third centimetre. "
            "And the last four ants complete the fourth centimetre! Sixteen fourths equals four whole centimetres. Watch the interactive "
            "ant parade march across the centimetre ruler on your screen, and see how repeated addition of fractions creates whole centimetres!"
        ),
        "checkpoints": [
            {
                "question": "If 12 ants of length 1/4 cm each walk in a single line, what is the total length of the ant line?",
                "options": [
                    "2 cm",
                    "3 cm",
                    "4 cm",
                    "12 cm"
                ],
                "correct": 1,
                "explanation": "Total length = 12 × 1/4 cm = 12/4 cm = 12 ÷ 4 = 3 cm.",
                "study_insight": "12 fourths equals 3 whole centimetres."
            },
            {
                "question": "How many ants measuring 1/4 cm each are needed to form a line measuring exactly 5 cm?",
                "options": [
                    "10 ants",
                    "15 ants",
                    "20 ants",
                    "25 ants"
                ],
                "correct": 2,
                "explanation": "Each centimetre requires 4 ants. For 5 cm, you need 5 × 4 = 20 ants.",
                "study_insight": "5 ÷ (1/4) = 5 × 4 = 20 ants."
            }
        ]
    },
    {
        "id": 15,
        "title": "Family Riddle",
        "subtitle": "Fun with Relations: Deductive Logic and Relationship Riddles",
        "concept_html": """
            <p class="mb-3">In the <strong>Fun with Relations</strong> section, the textbook presents a classic Indian family logic riddle: <em>“If the only brother of your father's sister had a child, what would be the child's relationship with you?”</em></p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 my-3">
                <span class="text-xs font-bold text-sky-400 block mb-2">Step-by-Step Logical Deduction</span>
                <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside">
                    <li><strong>Step 1:</strong> “Your father's sister” is your paternal aunt (often called <em>Bua</em> in Hindi).</li>
                    <li><strong>Step 2:</strong> Who is the “<em>only brother</em>” of your father's sister? Since your father is her brother, and she has only <em>one</em> brother, that only brother is <strong>your father himself</strong>!</li>
                    <li><strong>Step 3:</strong> Now, the riddle asks about “the child of your father”. Who is your father's child? <strong>You yourself, or your brother/sister (sibling)!</strong></li>
                </ol>
            </div>
            <p class="text-xs text-slate-300">Just like simplifying a fraction step-by-step to its lowest terms, analyzing relationship riddles step-by-step leads directly to an elegant, logical answer.</p>
        """,
        "spoken_text": (
            "To sharpen our logical reasoning, the textbook includes a wonderful family riddle in the Fun with Relations section! "
            "Listen carefully to the clues: If the only brother of your father's sister had a child, what would be the child's relationship "
            "with you? Let us break this puzzle down like true mathematical detectives. First, think about your father's sister. In Indian "
            "families, your father's sister is your aunt, affectionately called Bua in Hindi. Next, who is the only brother of your father's "
            "sister? Since she has only one brother, and your father is her brother, that only brother can be none other than your very own "
            "father! Now the riddle becomes delightfully simple: who is the child of your father? Your father's child is either you yourself, "
            "or your brother, or your sister! That means the child is your sibling, or you! In mathematics, whether we are simplifying "
            "a complex fraction or solving a word puzzle, breaking a problem into clear, deductive steps always turns confusion into clarity. "
            "Use the interactive family tree diagram on your screen to trace the clues and reveal the secret connection!"
        ),
        "checkpoints": [
            {
                "question": "In the family riddle, who is the 'only brother of your father's sister'?",
                "options": [
                    "Your uncle (Chacha)",
                    "Your grandfather",
                    "Your father",
                    "Your cousin"
                ],
                "correct": 2,
                "explanation": "Your father's sister is your aunt. If she has only one brother, that brother must be your father.",
                "study_insight": "Deductive logic breaks down complex statements one phrase at a time."
            },
            {
                "question": "What is the relationship between you and a child of your father?",
                "options": [
                    "Cousin",
                    "Sibling (or yourself)",
                    "Uncle",
                    "Nephew"
                ],
                "correct": 1,
                "explanation": "Your father's children are your brothers, your sisters, or yourself (siblings).",
                "study_insight": "Tracing kinship links mirrors simplifying mathematical expressions."
            }
        ]
    },
    {
        "id": 16,
        "title": "Fraction Lab",
        "subtitle": "Interactive Synthesis: Equivalence, Benchmarks, and Mixed Numbers",
        "concept_html": """
            <p class="mb-3">Welcome to the complete <strong>Fraction Laboratory</strong>! Here we synthesize all the key concepts mastered in Chapter 2 into an interactive mathematical workshop.</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-3 text-center text-xs font-mono">
                <div class="p-2 rounded-xl bg-slate-950/60 border border-amber-500/30">
                    <span class="text-[10px] text-amber-400 font-bold block">Equal Wholes</span>
                    <span class="text-white">Fair Baseline</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-950/60 border border-blue-500/30">
                    <span class="text-[10px] text-blue-400 font-bold block">Equivalence</span>
                    <span class="text-white">1/3 = 2/6 = 4/12</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-950/60 border border-emerald-500/30">
                    <span class="text-[10px] text-emerald-400 font-bold block">Benchmarks</span>
                    <span class="text-white">Compare to 1/2 & 1</span>
                </div>
                <div class="p-2 rounded-xl bg-slate-950/60 border border-purple-500/30">
                    <span class="text-[10px] text-purple-400 font-bold block">Mixed Numbers</span>
                    <span class="text-white">7/3 = 2 1/3</span>
                </div>
            </div>
            <p class="text-xs text-slate-300">You are now equipped with full mastery of fractions—from sharing parathas and shading grids to finding equivalent names, using benchmarks, and converting improper fractions!</p>
        """,
        "spoken_text": (
            "Congratulations young mathematicians! You have completed your exploration of all the core concepts in Chapter Two on Fractions. "
            "Let us take a moment to look back at the grand mathematical toolkit you now possess. First, you learned that fractions can only "
            "be fairly compared when the original reference wholes are identical. Second, you discovered how to visualize fractional parts "
            "by shading square grids and fitting colorful fraction strips together. Third, you mastered equivalent fractions: different names "
            "like one-third, two-sixths, and four-twelfths that describe the exact same shaded region. Fourth, you uncovered the golden rules "
            "of comparison: when denominators are equal, larger numerators win; and when numerators are equal, smaller denominators win! "
            "Fifth, you journeyed beyond one whole into improper fractions and mixed numbers like five-halves and two and a half. And finally, "
            "you learned to use benchmarks like one-half and one whole to evaluate fractions in seconds, and applied your skills to ant parades "
            "and family riddles. Now, you are ready to tackle the four Mastery Challenges on the upcoming slides! Experiment with the "
            "all-in-one Fraction Lab on your screen and celebrate your mathematical success!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following statements summarizes the core rule of equivalent fractions?",
                "options": [
                    "They have the same numbers and different values",
                    "They have different numbers but represent the exact same value",
                    "They can only have 1 as their numerator",
                    "They are always greater than 1"
                ],
                "correct": 1,
                "explanation": "Equivalent fractions (like 1/2, 2/4, 4/8) have different numerators and denominators but equal mathematical value.",
                "study_insight": "Equivalence means equal value despite different numerical representations."
            },
            {
                "question": "If you compare 4/7 and 5/9 using benchmarks, which fraction is greater than 1/2?",
                "options": [
                    "4/7 is greater than 1/2",
                    "5/9 is greater than 1/2",
                    "Both 4/7 and 5/9 are greater than 1/2",
                    "Neither is greater than 1/2"
                ],
                "correct": 2,
                "explanation": "Half of 7 is 3.5; 4 > 3.5, so 4/7 > 1/2. Half of 9 is 4.5; 5 > 4.5, so 5/9 > 1/2 as well! Both are greater than 1/2.",
                "study_insight": "Checking both numerators against half their denominators quickly validates both are above 1/2."
            }
        ]
    }
]

print("Slides 9 to 16 authored successfully.")

