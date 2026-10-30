"""NCERT Class 6 Mathematics Chapter 3: Number Play Data Module."""

CHAPTER_META = {
    "chapter_num": 3,
    "title": "Numbers",
    "subtitle": "NCERT Class 6 Mathematics • Chapter 3 Interactive Master Laboratory",
    "mentors": "D. R. Kaprekar & Shakuntala Devi",
    "mentors_title": "Pioneers of Recreational Number Theory & Mental Arithmetic",
    "badge": "Ganita Prakash • Playful Mathematics",
    "total_slides": 20,
    "checkpoints_count": 32,
    "quiz_questions_count": 40
}

SLIDES = [
    {
        "id": 1,
        "slide_num": 1,
        "title": "Number Clues",
        "subtitle": "Deducing Line Positions",
        "badge": "Number Logic",
        "summary": "Numbers are not just for counting; they encode rich real-world information. Through logical line puzzles where children report how many taller neighbors stand beside them, we decode order, heights, and spatial arrangements.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Numbers do far more than label quantities: they <strong class=\"text-amber-300\">tell stories</strong>! A single number can reveal position, ranking, relationships, and hidden clues about the world around us.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧍</span> The Line of Friends Puzzle\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Five friends stand in a straight line from left to right.</li>\n                <li>• Each person states the <strong class=\"text-amber-300\">number of taller neighbors</strong> standing immediately next to them (at most 2 neighbors).</li>\n                <li>• A person at the end of the line has only 1 neighbor; a person in the middle has 2 neighbors.</li>\n                <li>• If someone says \"0\", it means neither adjacent neighbor is taller than them!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧩</span> Deductive Reasoning\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-cyan-300\">The Tallest Friend:</strong> Always says \"0\" regardless of where they stand, because nobody is taller!</li>\n                <li>• <strong class=\"text-emerald-300\">The Shortest Friend:</strong> If standing in the middle, always says \"2\" because both neighbors are taller!</li>\n                <li>• By comparing reported numbers, we reconstruct the complete height order without measuring tape!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>Key Takeaway:</strong> Numbers serve as mathematical clues. In science, medicine, and computing, structured numbers allow algorithms to reconstruct complex 3D shapes from simple scan data.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "If the shortest person in a group stands between two taller friends, what number of taller immediate neighbors will they report?",
                "options": [
                    "0 taller neighbors",
                    "1 taller neighbor",
                    "2 taller neighbors",
                    "3 taller neighbors"
                ],
                "correct": 2,
                "explanation": "Because they have two immediate neighbors (left and right) and both are taller, they report exactly 2."
            },
            {
                "id": "cp1_2",
                "question": "What number of taller neighbors does the tallest person in the entire line always report?",
                "options": [
                    "Always 0",
                    "Always 1",
                    "Always 2",
                    "It depends on their position"
                ],
                "correct": 0,
                "explanation": "No person is taller than the tallest person, so regardless of position, they always report 0 taller neighbors."
            }
        ]
    },
    {
        "id": 2,
        "slide_num": 2,
        "title": "Grid Supercells",
        "subtitle": "Adjacent Cell Maxima",
        "badge": "Grid Puzzles",
        "summary": "In a grid of numbers, a cell is called a supercell if its number is strictly greater than all its immediately adjacent neighboring cells (top, bottom, left, and right). We explore how to maximize supercells under constraints.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Imagine a rectangular grid filled with distinct whole numbers. A cell is crowned a <strong class=\"text-amber-300\">supercell</strong> if the number inside it is strictly larger than each of its immediate adjacent neighbors (sharing an edge: North, South, East, West).\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏰</span> Supercell Criteria\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Interior Cell (4 neighbors):</strong> Must be strictly greater than Top, Bottom, Left, and Right.</li>\n                <li>• <strong class=\"text-slate-100\">Edge Cell (3 neighbors):</strong> Must be greater than its 3 adjacent neighbors.</li>\n                <li>• <strong class=\"text-slate-100\">Corner Cell (2 neighbors):</strong> Needs only to exceed its 2 adjacent neighbors!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🎯</span> Strategic Optimization\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Can two adjacent cells both be supercells? <strong class=\"text-rose-400\">Never!</strong> One must be larger than the other.</li>\n                <li>• To maximize supercells in a 3 × 3 grid, place large numbers in a checkerboard pattern!</li>\n                <li>• The absolute largest number in the grid is <strong class=\"text-emerald-300\">guaranteed to be a supercell</strong>.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Maximum Supercells in a 3 × 3 Grid:</strong> Since no two supercells can share an edge, the maximum number of supercells in a 3 × 3 grid is <strong>5</strong> (the 4 corners plus the center cell, forming an 'X' pattern).\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "Can two cells that share a common edge both be supercells simultaneously?",
                "options": [
                    "Yes, if both numbers are even",
                    "No, because if number A is in one cell and B in the neighbor, A > B and B > A cannot both be true",
                    "Yes, if they are corner cells",
                    "Only in 4 × 4 grids"
                ],
                "correct": 1,
                "explanation": "If two cells are adjacent, one must be larger; both cannot be strictly larger than each other."
            },
            {
                "id": "cp2_2",
                "question": "What is the maximum number of supercells possible in a 3 × 3 grid?",
                "options": [
                    "9",
                    "7",
                    "5",
                    "3"
                ],
                "correct": 2,
                "explanation": "In a 3 × 3 checkerboard pattern, the 4 corners and the center cell can all be supercells (total 5)."
            }
        ]
    },
    {
        "id": 3,
        "slide_num": 3,
        "title": "Number Line Jumps",
        "subtitle": "Predicting Intervals",
        "badge": "Number Line",
        "summary": "The number line gives a spatial map of numbers where equal steps represent equal increments. By observing marked intervals, step sizes, and jump patterns, students learn to locate and predict any missing value.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        The <strong class=\"text-amber-300\">number line</strong> transforms arithmetic into geometry! It is a continuous straight line where every point corresponds to a number, and distance between marks represents step sizes.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📏</span> Equal Interval Principle\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• On a standard number line, the distance between consecutive whole numbers (0 to 1, 1 to 2) is always constant.</li>\n                <li>• Scaled lines: marks can represent jumps of 2, 5, 10, 50, or 100!</li>\n                <li>• Moving to the <strong class=\"text-cyan-300\">right</strong> represents addition (increasing values).</li>\n                <li>• Moving to the <strong class=\"text-rose-300\">left</strong> represents subtraction (decreasing values).</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔍</span> Finding Unknown Marks\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Step 1: Count the number of equal sub-divisions between two known numbers.</li>\n                <li>• Step 2: Compute step size = <span class=\"font-mono text-amber-300\">(End − Start) ÷ Number of Steps</span>.</li>\n                <li>• Step 3: Add step size repeatedly to label intermediate ticks.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Example:</strong> If 0 is at mark 0 and 20 is at the 4th mark to the right, each mark is 20 ÷ 4 = <strong>5 units</strong>. The marks are 0, 5, 10, 15, and 20!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "If there are 5 equal spaces between 100 and 150 on a number line, what does each mark increase by?",
                "options": [
                    "5 units",
                    "10 units (since (150 − 100) ÷ 5 = 10)",
                    "20 units",
                    "50 units"
                ],
                "correct": 1,
                "explanation": "The distance of 50 is divided into 5 equal steps: 50 ÷ 5 = 10 units per mark."
            },
            {
                "id": "cp3_2",
                "question": "On a number line, which direction always indicates increasing numerical value?",
                "options": [
                    "Moving to the left",
                    "Moving to the right",
                    "Staying at the origin",
                    "Moving vertically"
                ],
                "correct": 1,
                "explanation": "Standard number lines increase in value from left to right."
            }
        ]
    },
    {
        "id": 4,
        "slide_num": 4,
        "title": "Digit Populations",
        "subtitle": "Powers of Ten Totals",
        "badge": "Combinatorics",
        "summary": "Discover the beautiful geometric pattern governing how many numbers exist with n digits. There are 9 one-digit positive numbers, 90 two-digit numbers, 900 three-digit numbers, 9000 four-digit numbers, and 90,000 five-digit numbers.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        How many numbers exist with 1 digit? With 2 digits? With 5 digits? By examining upper and lower boundaries, an extraordinary <strong class=\"text-amber-300\">powers-of-10 pattern</strong> emerges.\n    </p>\n\n    <div class=\"overflow-x-auto my-3\">\n        <table class=\"w-full text-xs text-left border-collapse border border-slate-700 bg-slate-900/90 rounded-xl overflow-hidden\">\n            <thead>\n                <tr class=\"bg-slate-800 text-amber-300 border-b border-slate-700\">\n                    <th class=\"p-2.5\">Category</th>\n                    <th class=\"p-2.5\">Smallest</th>\n                    <th class=\"p-2.5\">Largest</th>\n                    <th class=\"p-2.5\">Calculation</th>\n                    <th class=\"p-2.5\">Total Count</th>\n                </tr>\n            </thead>\n            <tbody class=\"divide-y divide-slate-800 text-slate-300\">\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">1-Digit (non-zero)</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">1</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">9</td>\n                    <td class=\"p-2.5\">9 − 1 + 1</td>\n                    <td class=\"p-2.5 font-bold text-amber-300 font-mono\">9</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">2-Digit</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">10</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">99</td>\n                    <td class=\"p-2.5\">99 − 10 + 1</td>\n                    <td class=\"p-2.5 font-bold text-amber-300 font-mono\">90</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">3-Digit</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">100</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">999</td>\n                    <td class=\"p-2.5\">999 − 100 + 1</td>\n                    <td class=\"p-2.5 font-bold text-amber-300 font-mono\">900</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">4-Digit</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">1000</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">9999</td>\n                    <td class=\"p-2.5\">9999 − 1000 + 1</td>\n                    <td class=\"p-2.5 font-bold text-amber-300 font-mono\">9,000</td>\n                </tr>\n                <tr>\n                    <td class=\"p-2.5 font-bold text-slate-100\">5-Digit</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">10000</td>\n                    <td class=\"p-2.5 font-mono text-cyan-300\">99999</td>\n                    <td class=\"p-2.5\">99999 − 10000 + 1</td>\n                    <td class=\"p-2.5 font-bold text-amber-300 font-mono\">90,000</td>\n                </tr>\n            </tbody>\n        </table>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200\">\n        💡 <strong>The General Rule:</strong> For any n digits, the total count of n-digit numbers is always <strong class=\"text-amber-300\">9 × 10^(n−1)</strong>! The first digit has 9 choices (1 to 9), and each subsequent digit has 10 choices (0 to 9).\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "How many total 4-digit whole numbers exist in our base-10 number system?",
                "options": [
                    "1,000",
                    "9,000 (from 1000 to 9999)",
                    "9,999",
                    "10,000"
                ],
                "correct": 1,
                "explanation": "The 4-digit numbers run from 1000 to 9999: 9999 − 1000 + 1 = 9,000."
            },
            {
                "id": "cp4_2",
                "question": "Why are there 9 choices for the first digit of a 3-digit number instead of 10?",
                "options": [
                    "Because 9 is the largest digit",
                    "Because the first digit cannot be 0 (otherwise it would be a 2-digit number)",
                    "Because odd numbers are not allowed",
                    "Because 10 is too large"
                ],
                "correct": 1,
                "explanation": "A leading zero reduces the digit count, so the first digit must be one of 1, 2, ..., 9 (9 choices)."
            }
        ]
    },
    {
        "id": 5,
        "slide_num": 5,
        "title": "Sum of Digits",
        "subtitle": "Digit Frequencies & Sums",
        "badge": "Digit Mysteries",
        "summary": "Adding the digits of a number reveals hidden divisibility rules and patterns. We also become digit detectives, discovering how many times a particular digit like '7' appears between 1 and 100.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        What happens when you add up the individual digits of a number? This operation, called the <strong class=\"text-amber-300\">digit sum</strong>, is one of the most powerful diagnostic tools in number theory.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>➕</span> Numbers with Digit Sum = 14\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• For 2-digit numbers: digits a + b = 14.</li>\n                <li>• Possibilities: <strong class=\"text-amber-300\">59, 68, 77, 86, 95</strong> (exactly 5 numbers!).</li>\n                <li>• Notice the pattern: as the tens digit increases by 1, the units digit decreases by 1!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🕵️</span> Digit Detective: Counting '7's\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• How many times does digit '7' appear from 1 to 100?</li>\n                <li>• <strong class=\"text-cyan-300\">In units place:</strong> 7, 17, 27, 37, 47, 57, 67, 77, 87, 97 (10 times).</li>\n                <li>• <strong class=\"text-emerald-300\">In tens place:</strong> 70, 71, 72, 73, 74, 75, 76, 77, 78, 79 (10 times).</li>\n                <li>• Total appearances = 10 + 10 = <strong class=\"text-amber-300\">20 times</strong>! (Notice 77 counts twice).</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>The Magic of 9:</strong> If you subtract a number's digit sum from the number itself (e.g. 54 − (5+4) = 45), the result is ALWAYS a multiple of 9!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "How many total 2-digit numbers have a digit sum equal to 14?",
                "options": [
                    "3",
                    "4",
                    "5 (59, 68, 77, 86, 95)",
                    "6"
                ],
                "correct": 2,
                "explanation": "The valid pairs of single digits summing to 14 are (5,9), (6,8), (7,7), (8,6), and (9,5): exactly 5 numbers."
            },
            {
                "id": "cp5_2",
                "question": "How many times does the digit '7' appear when writing all whole numbers from 1 to 100?",
                "options": [
                    "10 times",
                    "19 times",
                    "20 times (10 in units place + 10 in tens place)",
                    "21 times"
                ],
                "correct": 2,
                "explanation": "There are 10 sevens in the units place and 10 sevens in the tens place (70–79), totaling 20."
            }
        ]
    },
    {
        "id": 6,
        "slide_num": 6,
        "title": "Mirror Numbers",
        "subtitle": "Palindromic Symmetry",
        "badge": "Symmetry",
        "summary": "Palindromic numbers are numerical mirrors that read identically forwards and backwards (e.g., 66, 848, 575, 1111). We explore single-digit, two-digit, and three-digit palindromes and their remarkable symmetry.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Just as words like <em class=\"text-amber-300\">MADAM</em>, <em class=\"text-amber-300\">RADAR</em>, and <em class=\"text-amber-300\">LEVEL</em> read identically backwards and forwards, numbers with this reflective symmetry are called <strong class=\"text-cyan-300\">palindromic numbers</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-3 gap-3 my-3\">\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-xs mb-1\">2-Digit Palindromes</h5>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Both digits must match: aa.<br>\n                <span class=\"font-mono text-amber-300 font-bold\">11, 22, 33, 44, 55, 66, 77, 88, 99</span>.<br>\n                <em>Total: exactly 9 numbers.</em>\n            </p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-xs mb-1\">3-Digit Palindromes</h5>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Form: aba (first = last).<br>\n                Examples: <span class=\"font-mono text-cyan-300\">101, 121, 353, 575, 848</span>.<br>\n                <em>Total: 9 × 10 = 90 numbers.</em>\n            </p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-xs mb-1\">4-Digit Palindromes</h5>\n            <p class=\"text-[11px] text-slate-300 leading-snug\">\n                Form: abba.<br>\n                Examples: <span class=\"font-mono text-emerald-300\">1001, 1221, 2442, 9889</span>.<br>\n                <em>Total: 9 × 10 = 90 numbers.</em>\n            </p>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>All 2-Digit Palindromes are Divisible by 11:</strong> Notice that 11, 22, 33, 44... are all multiples of 11. In fact, ANY palindrome with an even number of digits (like 1221 or 5885) is divisible by 11!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "Which of the following numbers is a true palindromic number?",
                "options": [
                    "1231",
                    "848 (reads 8-4-8 in both directions)",
                    "572",
                    "1020"
                ],
                "correct": 1,
                "explanation": "848 reversed is 848, so it is a palindrome."
            },
            {
                "id": "cp6_2",
                "question": "How many total 2-digit palindromes exist?",
                "options": [
                    "5",
                    "9 (11, 22, 33, 44, 55, 66, 77, 88, 99)",
                    "10",
                    "11"
                ],
                "correct": 1,
                "explanation": "The 2-digit palindromes are 11, 22, 33, 44, 55, 66, 77, 88, 99 (9 numbers)."
            }
        ]
    },
    {
        "id": 7,
        "slide_num": 7,
        "title": "Palindrome Engine",
        "subtitle": "Reverse & Add Process",
        "badge": "Algorithm",
        "summary": "Take almost any positive number, reverse its digits, and add the two numbers together. Repeat this procedure with each new sum. Remarkably, most numbers produce a palindrome within a few quick steps!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Can non-palindromic numbers be turned into palindromes? Yes! Mathematicians discovered an elegant iterative recipe known as the <strong class=\"text-amber-300\">Reverse-and-Add Algorithm</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔄</span> The 3-Step Routine\n            </h5>\n            <ol class=\"text-xs space-y-1.5 text-slate-300 list-decimal list-inside\">\n                <li>Start with any whole number (e.g., <strong class=\"text-amber-300\">57</strong>).</li>\n                <li>Reverse its digits (<strong class=\"text-cyan-300\">75</strong>).</li>\n                <li>Add them: 57 + 75 = <strong class=\"text-emerald-300\">132</strong>.</li>\n                <li>If not a palindrome, repeat: 132 + 231 = <strong class=\"text-yellow-300\">363</strong> (Palindrome formed in 2 steps!).</li>\n            </ol>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>✨</span> Quick Convergence Examples\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Start with 34:</strong> 34 + 43 = <strong class=\"text-emerald-300\">77</strong> (1 step!).</li>\n                <li>• <strong class=\"text-slate-100\">Start with 68:</strong> 68 + 86 = 154 → 154 + 451 = 605 → 605 + 506 = <strong class=\"text-emerald-300\">1111</strong> (3 steps!).</li>\n                <li>• <strong class=\"text-rose-400\">The 196 Mystery:</strong> The number 196 has been tested through millions of additions by computers and has never yet yielded a palindrome (Lychrel number candidate)!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Try this in class:</strong> Choose your favorite 2-digit number and run the reverse-and-add machine. Over 80% of 2-digit numbers become palindromes in 4 steps or fewer!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "What is the result of applying one step of reverse-and-add to the number 42?",
                "options": [
                    "42 + 24 = 66 (a palindrome in 1 step)",
                    "42 + 42 = 84",
                    "42 − 24 = 18",
                    "24"
                ],
                "correct": 0,
                "explanation": "Reverse of 42 is 24; 42 + 24 = 66, which is already a palindrome."
            },
            {
                "id": "cp7_2",
                "question": "Starting with 75, what is the first sum in the reverse-and-add process?",
                "options": [
                    "120",
                    "132 (75 + 57 = 132)",
                    "150",
                    "147"
                ],
                "correct": 1,
                "explanation": "75 + 57 = 132."
            }
        ]
    },
    {
        "id": 8,
        "slide_num": 8,
        "title": "Kaprekar Mystery",
        "subtitle": "Constant 6174 Black Hole",
        "badge": "Indian Mathematics",
        "summary": "Discovered in 1949 by Indian school teacher D. R. Kaprekar of Devlali: Take any 4-digit number with at least two distinct digits, form the largest and smallest numbers, and subtract. Within at most 7 steps, you always reach 6174!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        In 1949, <strong class=\"text-amber-300\">Dattathreya Ramachandra Kaprekar</strong>, a brilliant Indian mathematics teacher from Maharashtra, stunned the world by revealing a mysterious 'number black hole' for 4-digit numbers: <strong class=\"text-cyan-300 font-mono text-lg\">6174</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🪄</span> Kaprekar's Routine\n            </h5>\n            <ol class=\"text-xs space-y-1.5 text-slate-300 list-decimal list-inside\">\n                <li>Choose any 4-digit number with at least two different digits (e.g. <strong class=\"text-amber-300\">3524</strong>).</li>\n                <li>Arrange digits descending for the largest number: <strong class=\"text-emerald-300\">5432</strong>.</li>\n                <li>Arrange digits ascending for the smallest number: <strong class=\"text-cyan-300\">2345</strong>.</li>\n                <li>Subtract: 5432 − 2345 = <strong class=\"text-amber-200\">3087</strong>.</li>\n                <li>Repeat with 3087: 8730 − 0378 = 8352 → 8532 − 2358 = <strong class=\"text-cyan-300 font-bold\">6174</strong>!</li>\n            </ol>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🕳️</span> The Universal Constant\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Once 6174 is reached, applying the routine again yields:<br>\n                    <span class=\"font-mono text-cyan-200 font-bold\">7641 − 1467 = 6174</span> (trapped forever!).</li>\n                <li>• <strong class=\"text-amber-300\">Guaranteed Convergence:</strong> Every eligible 4-digit number reaches 6174 in <strong class=\"text-slate-100\">at most 7 iterations</strong>!</li>\n                <li>• Only numbers with identical digits (1111, 2222...) fail, yielding 0000.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>Teacher Kaprekar's Legacy:</strong> Kaprekar had no university post or research grant; he taught at a secondary school in Devlali, India. He pursued mathematical patterns out of pure joy, inventing Kaprekar numbers, Harshad numbers, and self numbers!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "What is Kaprekar's constant for 4-digit numbers?",
                "options": [
                    "1089",
                    "6174",
                    "9999",
                    "3141"
                ],
                "correct": 1,
                "explanation": "6174 is the famous Kaprekar constant discovered in 1949."
            },
            {
                "id": "cp8_2",
                "question": "What is the maximum number of steps needed for any eligible 4-digit number to reach 6174?",
                "options": [
                    "3 steps",
                    "5 steps",
                    "7 steps",
                    "10 steps"
                ],
                "correct": 2,
                "explanation": "Every 4-digit number with at least two distinct digits converges to 6174 in at most 7 steps."
            }
        ]
    },
    {
        "id": 9,
        "slide_num": 9,
        "title": "Time Symmetries",
        "subtitle": "Clock & Calendar Loops",
        "badge": "Time Patterns",
        "summary": "Digital clocks display fascinating palindromes (such as 1:01, 4:44, 10:01, 12:21) and repeating digit sets. Calendars reveal cyclical patterns where regular years repeat after 6 or 11 years, and leap years after 28 years.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Timekeeping devices surround us with constantly shifting numbers. By paying close attention to digital clocks and calendars, we uncover surprising symmetry and cyclical rhythms.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⏰</span> Palindromic Clock Times\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Single-digit hour palindromes: <strong class=\"text-amber-300\">1:01, 2:22, 3:33, 4:44, 5:55</strong>.</li>\n                <li>• Double-digit hour palindromes: <strong class=\"text-cyan-300\">10:01, 11:11, 12:21</strong>.</li>\n                <li>• Repunit times: <strong class=\"text-emerald-300\">11:11</strong> is a 4-digit repunit!</li>\n                <li>• Symmetrical matching pairs: <span class=\"font-mono text-amber-200\">10:10, 12:12, 05:05</span>.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📅</span> Calendar Year Repetition\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• A regular year has 365 days = 52 weeks + <strong class=\"text-amber-300\">1 extra day</strong>.</li>\n                <li>• A leap year has 366 days = 52 weeks + <strong class=\"text-cyan-300\">2 extra days</strong>.</li>\n                <li>• A full calendar repeats when the cumulative extra days sum to a multiple of 7.</li>\n                <li>• Regular years repeat every <strong class=\"text-slate-100\">6 or 11 years</strong>; leap years repeat every <strong class=\"text-emerald-300\">28 years</strong>!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>Date Palindromes:</strong> In the date format DD-MM-YYYY, the date <strong>22-02-2022</strong> is a remarkable global palindrome (22022022) reading identical backwards and forwards!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "Which of the following digital clock times forms a palindrome?",
                "options": [
                    "12:15",
                    "12:21",
                    "10:20",
                    "11:22"
                ],
                "correct": 1,
                "explanation": "12:21 reads 1-2-2-1 forwards and backwards, making it a palindrome."
            },
            {
                "id": "cp9_2",
                "question": "How many extra odd days does a standard non-leap year (365 days) contribute beyond complete 7-day weeks?",
                "options": [
                    "0 extra days",
                    "1 extra day (365 = 52 × 7 + 1)",
                    "2 extra days",
                    "7 extra days"
                ],
                "correct": 1,
                "explanation": "365 ÷ 7 = 52 weeks with a remainder of 1 day."
            }
        ]
    },
    {
        "id": 10,
        "slide_num": 10,
        "title": "Mental Arithmetic",
        "subtitle": "Landmarks & Logic",
        "badge": "Mental Computation",
        "summary": "Mental arithmetic is an art of creative grouping. By decomposing numbers into tens and units, bridging to round numbers, and evaluating statements as Always, Sometimes, or Never true, students develop deep mathematical intuition.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        World-renowned Indian mental calculator <strong class=\"text-amber-300\">Shakuntala Devi</strong> taught that mental calculation is not about memorizing raw tables, but seeing <strong class=\"text-cyan-300\">shortcuts, compensations, and number friendliness</strong>!\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧠</span> Friendly Landmark Numbers\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Add 99:</strong> Add 100, then subtract 1! (e.g. 456 + 99 = 456 + 100 − 1 = 555).</li>\n                <li>• <strong class=\"text-slate-100\">Multiply by 25:</strong> Multiply by 100, then divide by 4! (e.g. 16 × 25 = 1600 ÷ 4 = 400).</li>\n                <li>• <strong class=\"text-slate-100\">Pairing to 100:</strong> 37 pairs with 63; 28 pairs with 72; 45 pairs with 55.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⚖️</span> Always, Sometimes, Never True\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <em>\"The sum of two 2-digit numbers is a 3-digit number.\"</em> → <strong class=\"text-amber-300\">Sometimes</strong> (10 + 15 = 25 [2 digits], but 60 + 50 = 110 [3 digits]).</li>\n                <li>• <em>\"The sum of two odd numbers is even.\"</em> → <strong class=\"text-emerald-300\">Always</strong> true!</li>\n                <li>• <em>\"A prime number is divisible by 4.\"</em> → <strong class=\"text-rose-400\">Never</strong> true!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200\">\n        💡 <strong>Target Number Challenge:</strong> Using the pool [2, 3, 5, 7] with addition and subtraction, can you reach 11? Yes: 7 + 5 + 2 − 3 = 11!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "What is the fastest mental math shortcut to add 98 to 345?",
                "options": [
                    "Add 100, then add 2",
                    "Add 100 to get 445, then subtract 2 to get 443",
                    "Add 90, then add 8 with carrying",
                    "Multiply 98 by 2"
                ],
                "correct": 1,
                "explanation": "Since 98 = 100 − 2, adding 100 and then subtracting 2 gives 345 + 100 − 2 = 443."
            },
            {
                "id": "cp10_2",
                "question": "Is the statement 'The product of two odd numbers is odd' Always, Sometimes, or Never true?",
                "options": [
                    "Sometimes true",
                    "Never true",
                    "Always true (e.g. 3 × 5 = 15, 7 × 9 = 63)",
                    "Cannot be determined"
                ],
                "correct": 2,
                "explanation": "Odd × Odd is Always odd because neither factor contributes a factor of 2."
            }
        ]
    },
    {
        "id": 11,
        "slide_num": 11,
        "title": "Smart Summation",
        "subtitle": "Gauss Pairing Method",
        "badge": "Summation Secrets",
        "summary": "Instead of adding numbers one by one, structure them into matching complementary pairs! The famous young Gauss technique allows adding 1 to 100 or summing arithmetic grids in seconds.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        When 10-year-old <strong class=\"text-amber-300\">Carl Friedrich Gauss</strong> was asked by his schoolmaster to add all numbers from 1 to 100, he wrote down the answer in seconds! How? By spotting a <strong class=\"text-cyan-300\">pairing pattern</strong>.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⚡</span> The Gauss Rainbow Pairing\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Pair the first and last numbers: 1 + 100 = <strong class=\"text-amber-300\">101</strong>.</li>\n                <li>• Pair the second and second-last: 2 + 99 = <strong class=\"text-amber-300\">101</strong>.</li>\n                <li>• Pair 3 + 98 = <strong class=\"text-amber-300\">101</strong> ... all 50 pairs equal 101!</li>\n                <li>• Total = 50 pairs × 101 = <strong class=\"text-emerald-300 font-bold font-mono\">5,050</strong>!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧱</span> Grid Sum Shortcuts\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• In a 10 × 10 hundreds chart (1 to 100):</li>\n                <li>• Sum of Row 1 (1 to 10) = 55.</li>\n                <li>• Sum of Row 2 (11 to 20) = 55 + 100 = 155.</li>\n                <li>• Sum of Row 3 (21 to 30) = 155 + 100 = 255.</li>\n                <li>• Adding all rows: 55 + 155 + 255 + ... + 955 = <strong class=\"text-amber-300 font-mono\">5,050</strong>!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>General Triangular Formula:</strong> The sum of the first n counting numbers is given by: <strong>Sum = n × (n + 1) ÷ 2</strong>. For n = 10: 10 × 11 ÷ 2 = 55!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "Using Gauss's pairing technique, what is the sum of all numbers from 1 to 20?",
                "options": [
                    "190",
                    "200",
                    "210 (10 pairs of 21 = 210)",
                    "220"
                ],
                "correct": 2,
                "explanation": "1 + 20 = 21, 2 + 19 = 21... there are 10 pairs of 21: 10 × 21 = 210."
            },
            {
                "id": "cp11_2",
                "question": "What is the sum of the first row (1 + 2 + 3 + ... + 10) on a hundreds chart?",
                "options": [
                    "45",
                    "50",
                    "55 (5 pairs of 11 = 55)",
                    "60"
                ],
                "correct": 2,
                "explanation": "10 × 11 ÷ 2 = 55."
            }
        ]
    },
    {
        "id": 12,
        "slide_num": 12,
        "title": "Collatz Sequence",
        "subtitle": "Hailstone 3n+1 Mystery",
        "badge": "Unsolved Mystery",
        "summary": "Proposed by Lothar Collatz in 1937: If even, divide by 2. If odd, multiply by 3 and add 1. Repeat. Does every positive number eventually collapse down to 1? Despite testing trillions of numbers, no human or supercomputer has proved it!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Mathematics has many grand unsolved mysteries. The most famous and accessible of all is the <strong class=\"text-amber-300\">Collatz Conjecture</strong> (also called the 3n + 1 problem or <em class=\"text-cyan-300\">Hailstone Numbers</em>).\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⚙️</span> The Two Simple Rules\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Take any positive whole number n:</li>\n                <li>• If n is <strong class=\"text-emerald-300\">EVEN</strong>: divide by 2 (<span class=\"font-mono text-emerald-200\">n → n ÷ 2</span>).</li>\n                <li>• If n is <strong class=\"text-rose-300\">ODD</strong>: triple it and add 1 (<span class=\"font-mono text-rose-200\">n → 3n + 1</span>).</li>\n                <li>• Repeat with the new number!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧗</span> The Rollercoaster of 7\n            </h5>\n            <div class=\"text-[11px] font-mono text-cyan-200 leading-relaxed bg-slate-950 p-2 rounded border border-cyan-800/40\">\n                7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1!\n            </div>\n            <p class=\"text-[11px] text-slate-300 mt-1\">\n                Notice: from 1, it enters the infinite 3-step loop: 1 → 4 → 2 → 1!\n            </p>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200\">\n        💡 <strong>The Hailstone Analogy:</strong> Numbers shoot up into cloud altitudes like hailstones caught in storm updrafts (multiplying by 3) and then plummet down as they freeze (halving by 2), before eventually falling to the ground (reaching 1).\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "If you start with the odd number 5, what is the next number under Collatz rules?",
                "options": [
                    "10",
                    "16 (3 × 5 + 1 = 16)",
                    "15",
                    "8"
                ],
                "correct": 1,
                "explanation": "Since 5 is odd, apply 3n + 1: 3 × 5 + 1 = 16."
            },
            {
                "id": "cp12_2",
                "question": "What 3-number loop does every tested Collatz sequence enter upon reaching 1?",
                "options": [
                    "1 → 2 → 3 → 1",
                    "1 → 4 → 2 → 1 (since 1 is odd: 3(1)+1=4, then 4/2=2, then 2/2=1)",
                    "1 → 3 → 5 → 1",
                    "1 → 0 → 1"
                ],
                "correct": 1,
                "explanation": "From 1: 3(1)+1 = 4 → 4/2 = 2 → 2/2 = 1, creating the eternal 4-2-1 loop."
            }
        ]
    },
    {
        "id": 13,
        "slide_num": 13,
        "title": "Practical Estimates",
        "subtitle": "Sensible Rounding",
        "badge": "Practical Math",
        "summary": "In real life, exact counts are often impossible or unnecessary. We use estimation to compute sensible answers for steps taken per day, lifetime heartbeats, crowd counts, and travel distances.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Is it always necessary to count down to the exact single digit? In practical life, engineers, doctors, and planners rely on <strong class=\"text-amber-300\">estimation</strong>—the skill of finding a close, sensible approximation.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🚶</span> Daily Life Estimation: Steps\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• An active student takes about <strong class=\"text-amber-300\">8,000 steps</strong> per day.</li>\n                <li>• In 1 year (365 days): ~8,000 × 365 ≈ 8,000 × 400 = <strong class=\"text-cyan-300\">~3 million steps</strong>!</li>\n                <li>• Average stride = ~0.6 meters → 3,000,000 × 0.6 m ≈ <strong class=\"text-emerald-300\">1,800 kilometers</strong> walked each year!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🫀</span> Heartbeat Estimation\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Resting human heart rate: ~70 beats per minute.</li>\n                <li>• In 1 hour: 70 × 60 = 4,200 beats.</li>\n                <li>• In 1 day (24 hours): 4,200 × 24 ≈ <strong class=\"text-amber-300\">100,000 beats</strong>!</li>\n                <li>• In 1 year: 100,000 × 365 ≈ <strong class=\"text-emerald-300\">36.5 million beats</strong>!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200\">\n        💡 <strong>The Golden Rule of Estimation:</strong> Round numbers to the nearest friendly ten, hundred, or thousand before performing arithmetic, keeping track of whether you rounded up or down.\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "Approximately how many times does an average human heart beat in a single day?",
                "options": [
                    "1,000 times",
                    "10,000 times",
                    "About 100,000 times (~70 bpm × 60 min × 24 hr ≈ 100,800)",
                    "10,000,000 times"
                ],
                "correct": 2,
                "explanation": "70 beats/min × 60 min/hr × 24 hr/day ≈ 100,800 beats, approximately 100,000."
            },
            {
                "id": "cp13_2",
                "question": "To quickly estimate 49 × 31, which rounded calculation gives the best quick mental estimate?",
                "options": [
                    "50 × 30 = 1,500",
                    "40 × 30 = 1,200",
                    "50 × 40 = 2,000",
                    "100 × 30 = 3,000"
                ],
                "correct": 0,
                "explanation": "Rounding 49 to 50 and 31 to 30 gives a rapid and close estimate of 50 × 30 = 1,500 (exact is 1,519)."
            }
        ]
    },
    {
        "id": 14,
        "slide_num": 14,
        "title": "The 21 Contest",
        "subtitle": "Multiples of 4 Strategy",
        "badge": "Game Theory 1",
        "summary": "Two players count upward starting from 1. On each turn, a player may call out 1, 2, or 3 consecutive numbers. The player forced to say '21' loses! Discover the mathematical secret that guarantees a win every single time.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Can mathematics guarantee you victory in a game? Welcome to <strong class=\"text-amber-300\">The Game of 21</strong>, a classic subtraction game rooted in <strong class=\"text-cyan-300\">modular arithmetic</strong> and backward induction!\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>📜</span> Official Rules\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Player A begins counting at 1, saying 1, 2, or 3 numbers (e.g. \"1, 2\").</li>\n                <li>• Player B continues with 1, 2, or 3 numbers (e.g. \"3, 4, 5\").</li>\n                <li>• The game continues in turns.</li>\n                <li>• <strong class=\"text-rose-400\">The Loser:</strong> The player who is forced to say <strong class=\"text-rose-400\">21</strong> loses the game!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏆</span> The Unbeatable Strategy\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Work backwards from 21: To make your opponent say 21, you MUST say <strong class=\"text-emerald-300\">20</strong>!</li>\n                <li>• If you say 20, they can say 21 (1 number), 21-22, etc. They are forced onto 21!</li>\n                <li>• Since turns allow 1 to 3 numbers (span = 1 + 3 = 4), key stepping stones are multiples of 4:</li>\n                <li>• Key milestones: <strong class=\"text-amber-300 font-mono\">4, 8, 12, 16, 20</strong>!</li>\n                <li>• If your opponent says k numbers, you say <span class=\"font-mono text-cyan-200\">4 − k</span> numbers to always land on these milestones!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        💡 <strong>Winning Secret:</strong> Let your friend go first! If they say 1, you say 2, 3, 4 (landing on 4). Whatever they play, complement their move to 4. You will hit 8, 12, 16, and 20, guaranteeing your victory!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "In the Game of 21, what is the critical milestone number you must say to guarantee your opponent is forced to say 21?",
                "options": [
                    "15",
                    "18",
                    "20",
                    "19"
                ],
                "correct": 2,
                "explanation": "If you end your turn on 20, your opponent must start with 21 on the next turn, losing the game."
            },
            {
                "id": "cp14_2",
                "question": "What is the key increment sum (complement) used to maintain control of milestones in the Game of 21?",
                "options": [
                    "Sum of 2",
                    "Sum of 3",
                    "Sum of 4 (min choice 1 + max choice 3 = 4)",
                    "Sum of 5"
                ],
                "correct": 2,
                "explanation": "Because each player can pick 1, 2, or 3 numbers, pairing choices to total 1 + 3 = 4 keeps you in control."
            }
        ]
    },
    {
        "id": 15,
        "slide_num": 15,
        "title": "The 99 Race",
        "subtitle": "Multiples of 11 Highway",
        "badge": "Game Theory 2",
        "summary": "In Game #2, players take turns adding any number from 1 to 10 to a running total, starting at 0. The player who pushes the total to exactly 99 (or over) wins! Master the key stepping stones: 11, 22, 33, 44, 55, 66, 77, 88.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Our second mathematical contest is the <strong class=\"text-amber-300\">Race to 99</strong>. Two players start at 0 and take turns adding any whole number from <strong class=\"text-cyan-300\">1 to 10</strong>. The first player to reach exactly 99 wins!\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏁</span> Game Rules\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Running total starts at 0.</li>\n                <li>• Player on turn adds any integer x where <span class=\"font-mono text-cyan-200\">1 ≤ x ≤ 10</span>.</li>\n                <li>• The player who hits <strong class=\"text-emerald-300\">99</strong> wins the match!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30\">\n            <h5 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🎯</span> The Multiples of 11 Highway\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• Notice that min add (1) + max add (10) = <strong class=\"text-amber-300\">11</strong>.</li>\n                <li>• To guarantee hitting 99, you must first hit <strong class=\"text-slate-100\">88</strong> (since 99 − 11 = 88).</li>\n                <li>• To hit 88, you must first hit 77, 66, 55, 44, 33, 22, and <strong class=\"text-cyan-300\">11</strong>!</li>\n                <li>• Winning Strategy: Land on multiples of 11. Whenever opponent adds n, you add <span class=\"font-mono text-emerald-300\">11 − n</span>!</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200\">\n        💡 <strong>First Mover vs Second Mover:</strong> If Player 1 starts by adding any number from 1 to 10, Player 2 can immediately add enough to reach 11! Thus, Player 2 has a guaranteed winning strategy in this game!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "What is the key complement number in the Race to 99 where players can add 1 to 10 on each turn?",
                "options": [
                    "9",
                    "10",
                    "11 (1 + 10 = 11)",
                    "12"
                ],
                "correct": 2,
                "explanation": "Because choices range from 1 to 10, any opponent move x can be countered with 11 − x so each round adds exactly 11."
            },
            {
                "id": "cp15_2",
                "question": "If your opponent is at 77 and adds 4 (bringing total to 81), how much should you add to seize the next winning milestone?",
                "options": [
                    "6",
                    "7 (bringing total to 81 + 7 = 88)",
                    "8",
                    "10"
                ],
                "correct": 1,
                "explanation": "Adding 7 brings the total to 88 (a multiple of 11), putting you 11 units away from the final goal of 99."
            }
        ]
    },
    {
        "id": 16,
        "slide_num": 16,
        "title": "Grand Synthesis",
        "subtitle": "Connecting Play Patterns",
        "badge": "Chapter Synthesis",
        "summary": "Review the full landscape of Chapter 3: How numbers convey spatial data, supercell grid layouts, palindromic symmetry, Kaprekar's 6174, Collatz's 3n+1 hailstone journey, estimation, and mathematical game strategies.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        You have explored the wonderland of <strong class=\"text-amber-300\">Number Play</strong>! From everyday clues to unsolved international mathematical conjectures, numbers are playful, creative, and predictable.\n    </p>\n\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30\">\n            <h5 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🗺️</span> The Explorers of Ganita Prakash\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-amber-300\">D. R. Kaprekar:</strong> Discovered the 6174 black hole constant through playful digit sorting.</li>\n                <li>• <strong class=\"text-cyan-300\">Carl Friedrich Gauss:</strong> Paired numbers symmetrically to sum 1 to 100 in seconds.</li>\n                <li>• <strong class=\"text-emerald-300\">Lothar Collatz:</strong> Created the 3n + 1 hailstone sequence that still baffles modern mathematics!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔑</span> Lifelong Number Habits\n            </h5>\n            <ul class=\"text-xs space-y-1.5 text-slate-300\">\n                <li>• <strong class=\"text-slate-100\">Look for Symmetry:</strong> Palindromes reflect structure in time and calendars.</li>\n                <li>• <strong class=\"text-slate-100\">Think Backwards:</strong> Game theory solves races to 21 and 99 from target to start.</li>\n                <li>• <strong class=\"text-slate-100\">Estimate Sensibly:</strong> Round before multiplying to make everyday decisions with ease.</li>\n            </ul>\n        </div>\n    </div>\n\n    <div class=\"p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200\">\n        🎉 <strong>Ready for the Mastery Challenge?</strong> Put your skills to the test across 40 interactive questions in the four challenge arenas that follow!\n    </div>\n</div>\n",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "Which Indian mathematician discovered the universal 4-digit routine that converges to 6174?",
                "options": [
                    "Srinivasa Ramanujan",
                    "D. R. Kaprekar",
                    "Aryabhata",
                    "Baudhāyana"
                ],
                "correct": 1,
                "explanation": "Dattathreya Ramachandra Kaprekar discovered the constant 6174 in 1949."
            },
            {
                "id": "cp16_2",
                "question": "What is the defining rule of a mathematical supercell in a numerical grid?",
                "options": [
                    "It must be equal to 100",
                    "It must be strictly larger than all its immediately adjacent neighbor cells",
                    "It must be an odd number",
                    "It must be in the top-left corner"
                ],
                "correct": 1,
                "explanation": "A supercell contains a number strictly greater than all cells sharing an edge with it."
            }
        ]
    },
    {
        "id": 17,
        "slide_num": 17,
        "title": "Challenge Round 1",
        "subtitle": "Questions 1 to 10",
        "badge": "Quiz Arena 1",
        "is_quiz": True,
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": 18,
        "slide_num": 18,
        "title": "Challenge Round 2",
        "subtitle": "Questions 11 to 20",
        "badge": "Quiz Arena 2",
        "is_quiz": True,
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": 19,
        "slide_num": 19,
        "title": "Challenge Round 3",
        "subtitle": "Questions 21 to 30",
        "badge": "Quiz Arena 3",
        "is_quiz": True,
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": 20,
        "slide_num": 20,
        "title": "Challenge Round 4",
        "subtitle": "Questions 31 to 40",
        "badge": "Quiz Arena 4",
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
        "question": "In the Line of Friends puzzle, if 4 friends stand in order from shortest to tallest, what does the person on the far right say?",
        "options": [
            "0 (because they are the tallest, so 0 neighbors are taller)",
            "1",
            "2",
            "3"
        ],
        "correct": 0,
        "explanation": "The person on the far right is the tallest in the group; none of their neighbors are taller, so they report 0."
    },
    {
        "id": 2,
        "challenge": 1,
        "question": "What is the maximum number of neighbors an interior cell in a 2D grid can share an edge with?",
        "options": [
            "2",
            "3",
            "4 (top, bottom, left, right)",
            "8"
        ],
        "correct": 2,
        "explanation": "An interior cell shares an edge with exactly 4 adjacent cells (North, South, East, West)."
    },
    {
        "id": 3,
        "challenge": 1,
        "question": "Can the smallest number in a grid of distinct numbers ever be a supercell?",
        "options": [
            "Yes, if it is in the corner",
            "No, because every neighbor is larger than it",
            "Yes, if all numbers are negative",
            "Only in a 2 × 2 grid"
        ],
        "correct": 1,
        "explanation": "To be a supercell, a cell must exceed all neighbors. The absolute smallest number cannot exceed any neighbor."
    },
    {
        "id": 4,
        "challenge": 1,
        "question": "On a number line, if 0 is at mark A and 60 is at mark D with 3 equal segments between them, what is the value of mark B?",
        "options": [
            "15",
            "20 (60 ÷ 3 = 20 per step)",
            "25",
            "30"
        ],
        "correct": 1,
        "explanation": "Distance 60 ÷ 3 equal intervals = 20 per interval. Mark B is 0 + 20 = 20."
    },
    {
        "id": 5,
        "challenge": 1,
        "question": "How many total 2-digit numbers exist in our base-10 number system?",
        "options": [
            "89",
            "90 (from 10 to 99: 99 − 10 + 1 = 90)",
            "99",
            "100"
        ],
        "correct": 1,
        "explanation": "From 10 through 99 inclusive, there are 99 − 10 + 1 = 90 two-digit numbers."
    },
    {
        "id": 6,
        "challenge": 1,
        "question": "How many total 3-digit numbers exist?",
        "options": [
            "899",
            "900 (from 100 to 999: 999 − 100 + 1 = 900)",
            "999",
            "1000"
        ],
        "correct": 1,
        "explanation": "From 100 to 999 inclusive: 999 − 100 + 1 = 900 numbers."
    },
    {
        "id": 7,
        "challenge": 1,
        "question": "What is the digit sum of the number 789?",
        "options": [
            "21",
            "24 (7 + 8 + 9 = 24)",
            "27",
            "28"
        ],
        "correct": 1,
        "explanation": "7 + 8 + 9 = 24."
    },
    {
        "id": 8,
        "challenge": 1,
        "question": "Which of the following numbers has a digit sum of 10?",
        "options": [
            "342",
            "451 (4 + 5 + 1 = 10)",
            "560",
            "281"
        ],
        "correct": 1,
        "explanation": "4 + 5 + 1 = 10."
    },
    {
        "id": 9,
        "challenge": 1,
        "question": "In a 3 × 3 grid with numbers 1 to 9, is the number 9 guaranteed to be a supercell?",
        "options": [
            "Yes, because 9 is strictly larger than all other numbers in the grid",
            "No, only if it is in the center",
            "No, only if it is in the corner",
            "It depends on the other numbers"
        ],
        "correct": 0,
        "explanation": "Since 9 is the largest number in the entire grid, any cells adjacent to it will be strictly smaller than 9."
    },
    {
        "id": 10,
        "challenge": 1,
        "question": "If you subtract any number's digit sum from the number itself, what is the result always divisible by?",
        "options": [
            "2",
            "5",
            "9",
            "11"
        ],
        "correct": 2,
        "explanation": "In base 10, N − digit_sum(N) is always a multiple of 9."
    },
    {
        "id": 11,
        "challenge": 2,
        "question": "Which of the following is a palindromic number?",
        "options": [
            "1232",
            "5445 (reads same forwards and backwards)",
            "6786",
            "9890"
        ],
        "correct": 1,
        "explanation": "5445 reversed is 5445, making it a true palindrome."
    },
    {
        "id": 12,
        "challenge": 2,
        "question": "How many total 3-digit palindromes exist?",
        "options": [
            "10",
            "45",
            "90 (9 choices for outer digit × 10 choices for middle digit)",
            "100"
        ],
        "correct": 2,
        "explanation": "A 3-digit palindrome has the form aba. There are 9 choices for 'a' (1–9) and 10 choices for 'b' (0–9), giving 9 × 10 = 90."
    },
    {
        "id": 13,
        "challenge": 2,
        "question": "What is the smallest 3-digit palindromic number?",
        "options": [
            "100",
            "101",
            "111",
            "121"
        ],
        "correct": 1,
        "explanation": "101 is the smallest 3-digit palindrome."
    },
    {
        "id": 14,
        "challenge": 2,
        "question": "What is the largest 3-digit palindromic number?",
        "options": [
            "989",
            "990",
            "999",
            "1001"
        ],
        "correct": 2,
        "explanation": "999 reads identically in both directions."
    },
    {
        "id": 15,
        "challenge": 2,
        "question": "Applying the reverse-and-add algorithm to 47 gives:",
        "options": [
            "47 + 74 = 121 (a palindrome in 1 step)",
            "47 + 47 = 94",
            "74 − 47 = 27",
            "118"
        ],
        "correct": 0,
        "explanation": "47 + 74 = 121, which is a palindrome."
    },
    {
        "id": 16,
        "challenge": 2,
        "question": "Applying the reverse-and-add algorithm to 65 gives 65 + 56 = 121. What is the next step if 121 were not already a palindrome?",
        "options": [
            "121 + 121",
            "121 + 121 = 242",
            "121 is already a palindrome!",
            "Subtract 11"
        ],
        "correct": 2,
        "explanation": "121 reversed is 121, so it is already a palindrome and the process stops."
    },
    {
        "id": 17,
        "challenge": 2,
        "question": "How many times does the digit '3' appear in writing numbers from 1 to 100?",
        "options": [
            "10 times",
            "19 times",
            "20 times (10 in units place, 10 in tens place)",
            "21 times"
        ],
        "correct": 2,
        "explanation": "Units place: 3, 13, 23, 33, 43, 53, 63, 73, 83, 93 (10). Tens place: 30–39 (10). Total = 20."
    },
    {
        "id": 18,
        "challenge": 2,
        "question": "What is true about any palindromic number with an even number of digits (like 44 or 1221)?",
        "options": [
            "It is always odd",
            "It is always divisible by 11",
            "It is always a prime number",
            "It is always divisible by 5"
        ],
        "correct": 1,
        "explanation": "Any even-length palindrome is divisible by 11 due to alternating digit sum rules."
    },
    {
        "id": 19,
        "challenge": 2,
        "question": "What is the famous candidate number that has never produced a palindrome under reverse-and-add?",
        "options": [
            "196",
            "121",
            "343",
            "454"
        ],
        "correct": 0,
        "explanation": "196 is the most famous suspected Lychrel number."
    },
    {
        "id": 20,
        "challenge": 2,
        "question": "How many 2-digit numbers have a digit sum equal to 9?",
        "options": [
            "8",
            "9 (18, 27, 36, 45, 54, 63, 72, 81, 90)",
            "10",
            "11"
        ],
        "correct": 1,
        "explanation": "The numbers 18, 27, 36, 45, 54, 63, 72, 81, and 90 all have digit sums of 9 (total 9 numbers)."
    },
    {
        "id": 21,
        "challenge": 3,
        "question": "What is Kaprekar's constant for 4-digit numbers?",
        "options": [
            "1089",
            "6174",
            "9999",
            "495"
        ],
        "correct": 1,
        "explanation": "6174 is Kaprekar's universal 4-digit constant."
    },
    {
        "id": 22,
        "challenge": 3,
        "question": "What is Kaprekar's constant for 3-digit numbers?",
        "options": [
            "108",
            "495",
            "617",
            "999"
        ],
        "correct": 1,
        "explanation": "For 3-digit numbers, Kaprekar's routine always leads to 495 (e.g. 954 − 459 = 495)."
    },
    {
        "id": 23,
        "challenge": 3,
        "question": "Which of the following 4-digit numbers will NOT reach 6174 under Kaprekar's routine?",
        "options": [
            "1234",
            "8532",
            "4444 (all 4 digits identical)",
            "2002"
        ],
        "correct": 2,
        "explanation": "Numbers with all identical digits yield 4444 − 4444 = 0000, so they are excluded."
    },
    {
        "id": 24,
        "challenge": 3,
        "question": "If you apply Kaprekar's routine directly to 6174, what is the result?",
        "options": [
            "0000",
            "6174 (7641 − 1467 = 6174)",
            "9999",
            "1089"
        ],
        "correct": 1,
        "explanation": "7641 − 1467 = 6174, so 6174 reproduces itself endlessly."
    },
    {
        "id": 25,
        "challenge": 3,
        "question": "Which time on a 12-hour digital clock represents a repunit time (all digits identical)?",
        "options": [
            "10:10",
            "11:11",
            "12:12",
            "01:01"
        ],
        "correct": 1,
        "explanation": "11:11 uses the single repeated digit 1."
    },
    {
        "id": 26,
        "challenge": 3,
        "question": "How many extra odd days does a leap year (366 days) have beyond complete 52 weeks?",
        "options": [
            "0",
            "1",
            "2 (366 = 52 × 7 + 2)",
            "4"
        ],
        "correct": 2,
        "explanation": "366 ÷ 7 = 52 weeks with 2 extra days."
    },
    {
        "id": 27,
        "challenge": 3,
        "question": "What is the quickest mental math shortcut to calculate 18 × 25?",
        "options": [
            "Multiply 18 × 100 (= 1800), then divide by 4 (= 450)",
            "Add 25 eighteen times",
            "Multiply 18 × 5, then multiply by 5",
            "Round 18 to 20"
        ],
        "correct": 0,
        "explanation": "Since 25 = 100 ÷ 4, 18 × 100 ÷ 4 = 1800 ÷ 4 = 450."
    },
    {
        "id": 28,
        "challenge": 3,
        "question": "Using Carl Friedrich Gauss's pairing method, what is the sum of numbers from 1 to 100?",
        "options": [
            "5,000",
            "5,050 (50 pairs of 101)",
            "5,500",
            "10,100"
        ],
        "correct": 1,
        "explanation": "50 pairs of 101 = 5,050."
    },
    {
        "id": 29,
        "challenge": 3,
        "question": "Is the statement 'The sum of three consecutive whole numbers is divisible by 3' Always, Sometimes, or Never true?",
        "options": [
            "Sometimes true",
            "Never true",
            "Always true (e.g. (n−1) + n + (n+1) = 3n)",
            "Only for even numbers"
        ],
        "correct": 2,
        "explanation": "The sum is always 3n, which is inherently divisible by 3."
    },
    {
        "id": 30,
        "challenge": 3,
        "question": "What is the sum of the numbers in the third row (21 to 30) of a hundreds grid?",
        "options": [
            "245",
            "255 (55 + 200 = 255)",
            "265",
            "275"
        ],
        "correct": 1,
        "explanation": "Sum of 1 to 10 is 55; adding 20 to each of the 10 numbers adds 200: 55 + 200 = 255."
    },
    {
        "id": 31,
        "challenge": 4,
        "question": "What are the two operations in the Collatz rule for n?",
        "options": [
            "If even: n ÷ 2; If odd: 3n + 1",
            "If even: n + 2; If odd: n − 1",
            "If even: n × 2; If odd: n ÷ 3",
            "If even: n ÷ 4; If odd: 2n + 1"
        ],
        "correct": 0,
        "explanation": "The Collatz rule divides even numbers by 2, and maps odd numbers to 3n + 1."
    },
    {
        "id": 32,
        "challenge": 4,
        "question": "Starting with 6, what is the Collatz sequence generated?",
        "options": [
            "6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1",
            "6 → 12 → 4 → 2 → 1",
            "6 → 18 → 9 → 1",
            "6 → 3 → 1"
        ],
        "correct": 0,
        "explanation": "6/2 = 3 → 3(3)+1 = 10 → 10/2 = 5 → 3(5)+1 = 16 → 8 → 4 → 2 → 1."
    },
    {
        "id": 33,
        "challenge": 4,
        "question": "Has any counter-example ever been discovered to disprove the Collatz Conjecture?",
        "options": [
            "Yes, computers found one in 2020",
            "No, every tested number reaches 1, but a rigorous general proof remains unsolved",
            "Yes, negative numbers disprove it",
            "It was disproved by Gauss"
        ],
        "correct": 1,
        "explanation": "The conjecture has been verified for numbers up to 2^68, but remains unproven generally."
    },
    {
        "id": 34,
        "challenge": 4,
        "question": "To estimate the total cost of 19 textbooks priced at ₹48 each, what is the best mental rounding?",
        "options": [
            "20 × ₹50 = ₹1,000 (close to exact ₹912)",
            "10 × ₹40 = ₹400",
            "20 × ₹40 = ₹800",
            "15 × ₹50 = ₹750"
        ],
        "correct": 0,
        "explanation": "Rounding 19 to 20 and 48 to 50 gives a quick mental estimate of 20 × 50 = ₹1,000."
    },
    {
        "id": 35,
        "challenge": 4,
        "question": "In the Game of 21 (where saying 21 loses and players can say 1 to 3 numbers), what sequence of numbers must you control to guarantee a win?",
        "options": [
            "Multiples of 3: 3, 6, 9, 12, 15, 18",
            "Multiples of 4: 4, 8, 12, 16, 20",
            "Multiples of 5: 5, 10, 15, 20",
            "Odd numbers: 1, 3, 5, 7, 9"
        ],
        "correct": 1,
        "explanation": "Because min choice + max choice = 1 + 3 = 4, controlling 4, 8, 12, 16, and 20 guarantees victory."
    },
    {
        "id": 36,
        "challenge": 4,
        "question": "In the Game of 21, if your opponent says '1, 2', how many numbers should you say to land on the first key milestone 4?",
        "options": [
            "1 number",
            "2 numbers ('3, 4', landing on 4)",
            "3 numbers",
            "Pass your turn"
        ],
        "correct": 1,
        "explanation": "Opponent said 2 numbers; you say 4 − 2 = 2 numbers ('3, 4') to reach milestone 4."
    },
    {
        "id": 37,
        "challenge": 4,
        "question": "In the Race to 99 (where players can add 1 to 10 each turn), what are the key milestone numbers?",
        "options": [
            "Multiples of 10: 10, 20, 30... 90",
            "Multiples of 11: 11, 22, 33, 44, 55, 66, 77, 88",
            "Multiples of 9: 9, 18, 27... 90",
            "Multiples of 12"
        ],
        "correct": 1,
        "explanation": "1 + 10 = 11, so keeping the running total at multiples of 11 leads directly to 88 and 99."
    },
    {
        "id": 38,
        "challenge": 4,
        "question": "If you are at 88 in the Race to 99, and your opponent adds 3 (reaching 91), what must you add to win?",
        "options": [
            "6",
            "7",
            "8 (since 91 + 8 = 99)",
            "9"
        ],
        "correct": 2,
        "explanation": "99 − 91 = 8. Adding 8 wins the game immediately!"
    },
    {
        "id": 39,
        "challenge": 4,
        "question": "Why do Collatz sequences earn the nickname 'Hailstone Numbers'?",
        "options": [
            "Because they are cold",
            "Because their values rise and fall erratically like hailstones in cloud currents before falling to 1",
            "Because they were discovered in winter",
            "Because they only work with solid numbers"
        ],
        "correct": 1,
        "explanation": "Like hailstones bouncing up and down in storm updrafts, numbers climb and fall before hitting 1."
    },
    {
        "id": 40,
        "challenge": 4,
        "question": "What is the primary secret to mastering mathematical games?",
        "options": [
            "Guessing randomly",
            "Working backwards from the target using modular complements to find invariant winning states",
            "Moving as fast as possible",
            "Memorizing the entire board"
        ],
        "correct": 1,
        "explanation": "Backward induction identifies the key positions that leave your opponent no winning options."
    }
]
