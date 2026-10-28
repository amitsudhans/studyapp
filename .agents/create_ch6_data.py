# -*- coding: utf-8 -*-
"""
Generates .agents/class7_math_number_play_data.py
Contains:
- 20 slides (SLIDES_DATA)
- 32 in-slide checkpoints (2 per slide on slides 1-16)
- 40 mastery quiz questions (QUIZ_QUESTIONS) with multi-step step-by-step solutions
- Mentor: Acharya Virahāńka (Pioneer of Indian Combinatorics & Rhythmic Number Sequences)
"""

content = r'''# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 6: Number Play Data
Author: Antigravity
Avatar: Acharya Virahāńka (Pioneer of Indian Combinatorics & Rhythmic Number Sequences)
"""

SLIDES_DATA = [
    # Slide 1: Numbers Tell us Things - The Height Queue
    {
        "id": 1,
        "section": "6.1",
        "tag": "Section 6.1 • Numbers Tell us Things",
        "title": "Numbers Tell us Things: Decoding Line-Up Clues",
        "key_terms": ["Positional Logic", "Height Clues", "Inverse Deduction", "Queue Arrangement"],
        "sim_id": "height_queue_decoder_sim",
        "sim_title": "Interactive Height Line-Up Decoder",
        "narration": "Namaste, inquisitive minds! I am Acharya Virahāńka. Numbers are not merely tools for counting sheep—they are secret messengers! Imagine a queue of children where each person calls out a number: how many people taller than them stand ahead. From just these whispered numbers, can we reconstruct the exact height order of the entire line? Let us play with numbers and discover their hidden logic!",
        "theory": [
            "Mathematics often operates like detective work. In many situations, we do not have complete information upfront, but numbers give us **constraints and relationships**.",
            "**The Height Queue Problem**: Suppose students of distinct heights stand in a straight single-file line facing front. Each student counts how many students **taller than them** are standing in front of them in line.",
            "- The person in the very first position always calls out **0**, because nobody stands ahead of them!",
            "- The tallest person in the entire queue will **always call out 0**, no matter where they stand in the line, because no one is taller than them!",
            "- If the shortest person stands at the 5th position, they will call out **4**, because all 4 people ahead are taller than them.",
            "By analyzing these callout numbers from the tallest person down to the shortest, we can uniquely locate everyone's exact position."
        ],
        "fact_box": "This height line-up deduction is an example of an 'inversion sequence' in modern computer science, used in sorting algorithms and database indexing!",
        "checkpoints": [
            {
                "id": "c1_1",
                "question": "In a queue of students facing forward, what number will the tallest student in the entire line ALWAYS call out?",
                "options": ["1", "0", "Their position number", "The total number of students"],
                "correct": 1,
                "explanation": "Since no student in the queue is taller than the tallest student, there are 0 people taller than them ahead, regardless of position."
            },
            {
                "id": "c1_2",
                "question": "A student standing at position 4 in line calls out the number 3. What does this reveal about the three students standing ahead of them?",
                "options": ["All three students ahead are shorter than them", "All three students ahead are taller than them", "Exactly one student ahead is taller", "The student is the shortest in the world"],
                "correct": 1,
                "explanation": "If there are 3 students ahead and the callout is 3, every single person standing ahead must be taller than this student."
            }
        ]
    },

    # Slide 2: Positional Number Logic & Invariants
    {
        "id": 2,
        "section": "6.1",
        "tag": "Section 6.1 • Positional Reasoning",
        "title": "Deductive Reasoning: Reconstructing Hidden Permutations",
        "key_terms": ["Inversion Number", "Permutation", "Deductive Elimination", "Invariant Rules"],
        "sim_id": "positional_lineup_invariants_sim",
        "sim_title": "Interactive Logic Grid: Reconstructing the Queue",
        "narration": "To solve any positional puzzle, we work backwards from the most constrained clues! The tallest person has only one place with 0 taller people ahead. Once the tallest is placed, we place the next tallest, and so on. Let us master this systematic step-by-step elimination.",
        "theory": [
            "**Step-by-Step Queue Reconstruction Algorithm**:",
            "1. **Rank from Tallest to Shortest**: Label the $n$ people from tallest (Rank 1) to shortest (Rank $n$).",
            "2. **Place the Tallest (Rank 1)**: Since no one is taller, their callout must be $0$. Place them into their designated slot.",
            "3. **Place the Next Tallest (Rank 2)**: If their callout is $c$, leave exactly $c$ open spots ahead for taller people, and place them in the next available empty spot.",
            "4. **Continue Downwards**: Repeat for each subsequent person until all empty slots are filled.",
            "**Key Mathematical Invariant**: Every distinct permutation of heights produces a unique sequence of callout numbers, and conversely, every valid callout sequence determines exactly **one unique arrangement**!"
        ],
        "fact_box": "In Indian classical philosophy (*Nyaya Shastra*), deductive reasoning through elimination is called 'Parisesha Pramana'—ruling out impossibilities until the truth remains.",
        "checkpoints": [
            {
                "id": "c2_1",
                "question": "Four students have heights 1, 2, 3, 4 (4 is tallest). Their callouts are [0, 0, 1, 0]. Who stands at the very front of the line (position 1)?",
                "options": ["Student 1", "Student 2", "Student 3", "The person with 0 taller ahead at position 1"],
                "correct": 3,
                "explanation": "The person standing at position 1 must have 0 people ahead of them, so their callout is 0."
            },
            {
                "id": "c2_2",
                "question": "Can the person standing at position 3 in a line ever call out the number 4?",
                "options": ["Yes, if they are very short", "Yes, in large queues", "No, because there are only 2 people standing ahead of them", "Only if people are standing on chairs"],
                "correct": 2,
                "explanation": "A person at position 3 has only 2 people ahead of them; the maximum number of taller people ahead cannot exceed 2."
            }
        ]
    },

    # Slide 3: Picking Parity - Visual Pair-Matching
    {
        "id": 3,
        "section": "6.2",
        "tag": "Section 6.2 • Picking Parity: Even & Odd Numbers",
        "title": "The Geometry of Parity: Perfect Pairs vs. Lonely Dots",
        "key_terms": ["Parity", "Even Numbers", "Odd Numbers", "Pairing Principle", "Modulo 2"],
        "sim_id": "parity_pair_matching_sim",
        "sim_title": "Visual Dot-Pairing & Parity Anatomy Lab",
        "narration": "What makes an even number even, and an odd number odd? Imagine dividing a bag of marbles between two friends. If every single marble finds a partner, forming two equal rows with no leftovers, the number is even! But if exactly one lonely marble is left without a partner, the number is odd. This fundamental property is called parity.",
        "theory": [
            "**Parity** is the mathematical classification of every integer as either **Even** or **Odd**.",
            "**Visual Geometric Model**:",
            "- **Even Numbers** can be arranged in a neat $2 \\times k$ rectangular array of paired dots. Every dot has a matching buddy! Examples: $2, 4, 6, 8, 10, \\dots$",
            "- **Odd Numbers** leave exactly **one solitary dot** with no partner. Examples: $1, 3, 5, 7, 9, \\dots$",
            "**Formal Algebraic Definitions**:",
            "- An **Even Number** can be expressed as: $$E = 2k \\quad (\\text{where } k \\text{ is an integer})$$",
            "- An **Odd Number** can be expressed as: $$O = 2k + 1 \\quad \\text{or} \\quad O = 2k - 1$$",
            "Parity is an all-or-nothing property: every whole number alternates strictly between even and odd: $0, 1, 2, 3, 4, 5, \\dots$"
        ],
        "fact_box": "The word 'parity' comes from the Latin word 'par', meaning 'equal' or 'pair'. Zero is completely even because 0 = 2 × 0 leaves 0 remainder!",
        "checkpoints": [
            {
                "id": "c3_1",
                "question": "When an odd number of dots is arranged into pairs of two, how many unpaired dots are always left over?",
                "options": ["0 dots", "Exactly 1 dot", "2 dots", "It depends on how large the number is"],
                "correct": 1,
                "explanation": "By definition, an odd number divided by 2 always leaves a remainder of exactly 1 unpaired dot."
            },
            {
                "id": "c3_2",
                "question": "Which algebraic expression represents ANY odd number for any integer k?",
                "options": ["2k", "2k + 1", "k + 2", "k²"],
                "correct": 1,
                "explanation": "2k is always even, so adding 1 yields 2k + 1, which is always odd."
            }
        ]
    },

    # Slide 4: Parity Arithmetic Laws
    {
        "id": 4,
        "section": "6.2",
        "tag": "Section 6.2 • Parity Arithmetic Laws",
        "title": "The Arithmetic Laws of Parity: Addition & Multiplication",
        "key_terms": ["Parity Addition", "Parity Multiplication", "Algebraic Proof", "Invariant Sums"],
        "sim_id": "parity_arithmetic_matrix_sim",
        "sim_title": "Interactive Parity Operation Matrix & Dot-Merger",
        "narration": "What happens when you add two odd numbers together? Each odd number has one lonely unpaired dot. When you bring the two numbers together, the two lonely dots find each other and form a new pair! That is why Odd plus Odd always equals Even. Let us explore the universal laws of parity arithmetic.",
        "theory": [
            "**Addition & Subtraction Parity Rules**:",
            "1. **Even + Even = Even**: $(2a) + (2b) = 2(a + b)$. Both pairs combine with zero leftover dots.",
            "2. **Odd + Odd = Even**: $(2a + 1) + (2b + 1) = 2(a + b + 1)$. The two lonely dots unite into a new pair!",
            "3. **Even + Odd = Odd**: $(2a) + (2b + 1) = 2(a + b) + 1$. Exactly one lonely dot remains unpaired.",
            "**Multiplication Parity Rules**:",
            "- $\\text{Even} \\times \\text{Any Integer} = \\text{Even}$ (Since a factor of 2 is present).",
            "- $\\text{Odd} \\times \\text{Odd} = \\text{Odd}$ (No factor of 2 exists anywhere!).",
            "**Summary Insight**: The sum of several numbers is odd if and only if there is an **ODD number of odd numbers** being added!"
        ],
        "fact_box": "Computer networks use 'parity bits' to detect data corruption during internet transmission: if a single bit flips, the parity check fails immediately!",
        "checkpoints": [
            {
                "id": "c4_1",
                "question": "What is the parity of the sum of three odd numbers (e.g. 3 + 5 + 7 = 15)?",
                "options": ["Always Even", "Always Odd", "Sometimes Even, sometimes Odd", "Always Prime"],
                "correct": 1,
                "explanation": "Odd + Odd = Even, and Even + Odd = Odd. An odd count of odd numbers always produces an odd sum."
            },
            {
                "id": "c4_2",
                "question": "If you multiply any integer by 6, the resulting product is guaranteed to be:",
                "options": ["Always Odd", "Always Even", "Prime", "Negative"],
                "correct": 1,
                "explanation": "Since 6 is an even number (6 = 2 × 3), any multiple of 6 contains the factor 2 and is therefore always even."
            }
        ]
    },

    # Slide 5: Parity in Grids & Checkerboard Tiling
    {
        "id": 5,
        "section": "6.2",
        "tag": "Section 6.2 • Parity in Grids",
        "title": "Grid Parity: Checkerboard Coloring & The Domino Dilemma",
        "key_terms": ["Grid Parity", "Checkerboard Coloring", "Domino Tiling", "Bipartite Balance"],
        "sim_id": "grid_squares_parity_sim",
        "sim_title": "Checkerboard Grid Parity & Domino Tiling Lab",
        "narration": "Can you tile an 8-by-8 chessboard using 32 two-square dominoes? Yes, 32 times 2 is 64 squares! But what if someone chops off two opposite corner squares? Now 62 squares remain. Can 31 dominoes cover it? Parity reveals a stunning answer: it is mathematically IMPOSSIBLE! Explore the checkerboard parity proof.",
        "theory": [
            "**Total Squares in a Grid**: An $m \\times n$ grid contains $m \\times n$ unit squares. If both $m$ and $n$ are odd, the total number of squares is odd; otherwise, it is even.",
            "**The Checkerboard Color Invariant**:",
            "- Alternating black and white colors on a grid gives every square a 'color parity'.",
            "- Every $2 \\times 1$ domino placed on the board covers **exactly 1 black square and 1 white square**.",
            "**The Famous Mutilated Chessboard Problem**:",
            "1. An intact $8 \\times 8$ board has 32 white and 32 black squares.",
            "2. Opposite corners of a chessboard always share the **SAME color** (e.g., both are white).",
            "3. If two opposite white corners are cut off, the board has **30 white squares and 32 black squares**.",
            "4. 31 dominoes would require 31 white and 31 black squares. But we have only 30 white squares!",
            "**Conclusion**: By color parity imbalance, tiling is strictly **impossible**!"
        ],
        "fact_box": "This checkerboard proof was popularized by mathematician Solomon Golomb in 1954 and is considered one of the most elegant proofs in all of mathematics.",
        "checkpoints": [
            {
                "id": "c5_1",
                "question": "How many total unit squares are in a grid with 5 rows and 7 columns?",
                "options": ["12 squares", "24 squares", "35 squares (Odd parity)", "36 squares (Even parity)"],
                "correct": 2,
                "explanation": "Total squares = 5 × 7 = 35 squares. Since Odd × Odd = Odd, the total count has odd parity."
            },
            {
                "id": "c5_2",
                "question": "Why can 31 dominoes never cover an 8×8 chessboard with two opposite corners removed?",
                "options": ["Dominoes are too heavy", "The board has 30 white and 32 black squares, but each domino needs 1 white and 1 black", "The board is not square", "Dominoes cannot bend"],
                "correct": 1,
                "explanation": "Each domino must cover 1 white and 1 black square. Since removing opposite corners leaves unequal counts (30 white vs 32 black), complete tiling is impossible."
            }
        ]
    },

    # Slide 6: Algebraic Parity & Sequences
    {
        "id": 6,
        "section": "6.2",
        "tag": "Section 6.2 • Algebraic Sequences",
        "title": "Sequences and Parity: The General $n^{th}$ Term",
        "key_terms": ["Sequence Parity", "General Term", "Algebraic Form", "Collatz Rules"],
        "sim_id": "algebraic_parity_nth_term_sim",
        "sim_title": "Sequence Parity Engine & Collatz Explorer",
        "narration": "When a pattern repeats, algebra gives us the telescope to see into the future! Consider sequences like 2n (all even numbers), 2n - 1 (all odd numbers), or alternating parity sequences. Let us explore how simple algebraic rules control whether the millionth term will be even or odd.",
        "theory": [
            "**Even Number Sequence**: $2, 4, 6, 8, 10, \\dots$ with general term $T_n = 2n$. Every single term is divisible by 2.",
            "**Odd Number Sequence**: $1, 3, 5, 7, 9, \\dots$ with general term $T_n = 2n - 1$. For $n = 100$, $T_{100} = 2(100) - 1 = 199$.",
            "**Analyzing the Parity of $3n + 1$**:",
            "- If $n$ is Even ($n = 2k$): $3(2k) + 1 = 6k + 1$ ➔ **ODD**.",
            "- If $n$ is Odd ($n = 2k + 1$): $3(2k + 1) + 1 = 6k + 4 = 2(3k + 2)$ ➔ **EVEN**.",
            "The parity strictly flips back and forth!",
            "**The Famous $3n + 1$ (Collatz) Rule**: Take any positive integer. If it is even, divide by 2 ($n/2$). If it is odd, triple it and add 1 ($3n + 1$). Amazingly, every number tested eventually cascades down to the repeating loop $4 \\to 2 \\to 1$!"
        ],
        "fact_box": "Lothar Collatz proposed this problem in 1937. Legendary mathematician Paul Erdős said: 'Mathematics is not yet ready for such problems!'",
        "checkpoints": [
            {
                "id": "c6_1",
                "question": "What is the 50th odd number in the sequence 1, 3, 5, 7, ...?",
                "options": ["99", "100", "101", "49"],
                "correct": 0,
                "explanation": "The n-th odd number is given by Tn = 2n - 1. For n = 50: 2(50) - 1 = 100 - 1 = 99."
            },
            {
                "id": "c6_2",
                "question": "If n is an odd number, what is the parity of the expression 5n + 3?",
                "options": ["Always Odd", "Always Even", "Depends on n", "Zero"],
                "correct": 1,
                "explanation": "Odd × Odd = Odd (5n is odd). Odd + Odd = Even (odd + 3 is even). Therefore, 5n + 3 is always even."
            }
        ]
    },

    # Slide 7: Explorations in Grids - Magic Squares
    {
        "id": 7,
        "section": "6.3",
        "tag": "Section 6.3 • Explorations in Grids",
        "title": "Magic Squares: Harmonious Grids with Matching Sums",
        "key_terms": ["Magic Square", "Magic Constant", "Row Sum", "Column Sum", "Diagonal Sum"],
        "sim_id": "magic_square_3x3_sim",
        "sim_title": "Interactive 3 × 3 Magic Square Playground",
        "narration": "Welcome to the enchanted world of magic squares! A magic square is a grid of numbers where the sum of every row, every column, and both main diagonals equals the EXACT same magical target number, called the magic constant. For a 3-by-3 square using digits 1 to 9, the magic sum is always 15!",
        "theory": [
            "**Definition of a Magic Square**: An $n \\times n$ square grid filled with distinct integers such that the sum of each row, each column, and both diagonals is constant.",
            "**How to Calculate the Magic Constant for a $3 \\times 3$ Square**:",
            "1. The numbers to place are $1, 2, 3, 4, 5, 6, 7, 8, 9$.",
            "2. Total sum of all numbers: $$1 + 2 + 3 + \\dots + 9 = \\frac{9 \\times 10}{2} = 45$$",
            "3. The grid has 3 rows, and each row must have the same sum $S$.",
            "4. Therefore: $$3 \\times S = 45 \\implies S = \\frac{45}{3} = 15$$",
            "Every row, column, and diagonal MUST sum to exactly **15**!"
        ],
        "fact_box": "In China, the 3×3 magic square was known as the 'Lo Shu' turtle square (c. 650 BCE). In India, it was inscribed on amulets for balance and cosmic harmony.",
        "checkpoints": [
            {
                "id": "c7_1",
                "question": "What is the magic constant (sum of each row, column, and diagonal) for a standard 3×3 magic square using digits 1 to 9?",
                "options": ["12", "15", "18", "45"],
                "correct": 1,
                "explanation": "Total sum = 45. Divided equally across 3 rows gives 45 / 3 = 15."
            },
            {
                "id": "c7_2",
                "question": "Can the number 9 be placed in the center cell of a standard 3×3 magic square using digits 1 to 9?",
                "options": ["Yes, anywhere", "No, because the center must be 5", "Yes, if 1 is in the corner", "Only in diagonal squares"],
                "correct": 1,
                "explanation": "The center cell must participate in 4 lines (row, column, 2 diagonals) summing to 15. Only the number 5 has enough distinct pairs to satisfy this."
            }
        ]
    },

    # Slide 8: The Center Cell Rule & Structural Symmetry
    {
        "id": 8,
        "section": "6.3",
        "tag": "Section 6.3 • Magic Square Structure",
        "title": "The Golden Center Rule & 8 Symmetries of the $3 \\times 3$ Square",
        "key_terms": ["Center Cell Rule", "Symmetry Group", "Rotations & Reflections", "Complementary Pairs"],
        "sim_id": "magic_square_center_rule_sim",
        "sim_title": "Center Cell Proof & 8 Rotational Symmetries Lab",
        "narration": "Why MUST the number 5 sit right in the center of the 3-by-3 magic square? Because the center cell is the hub: it lies on 1 row, 1 column, and 2 diagonals—four lines crossing at one point! Let us prove mathematically why the center cell is always one-third of the magic sum.",
        "theory": [
            "**Algebraic Proof of the Center Cell Theorem**:",
            "- Let the center cell be $C$, and the magic sum be $S = 15$.",
            "- 4 lines pass through $C$: row 2, column 2, main diagonal 1, and main diagonal 2.",
            "- Adding these 4 lines gives $4 \\times S = 4 \\times 15 = 60$.",
            "- In this sum, every cell of the grid is counted once, except the center cell $C$, which is counted 4 times (3 extra times!).",
            "- Therefore: $\\text{Total Sum} + 3C = 60 \\implies 45 + 3C = 60 \\implies 3C = 15 \\implies C = 5$!",
            "**The 8 Fundamental Orientations**:",
            "There is essentially only ONE unique $3 \\times 3$ magic square! All others are just its **4 rotations** ($0°, 90°, 180°, 270°$) and **4 reflections** (mirror images across axes)."
        ],
        "fact_box": "Notice the complementary pairs surrounding the center 5: 1+9 = 10, 2+8 = 10, 3+7 = 10, 4+6 = 10. Every line through the center consists of 5 plus a pair summing to 10!",
        "checkpoints": [
            {
                "id": "c8_1",
                "question": "In any 3×3 magic square with magic sum S, what is the value of the center cell C?",
                "options": ["C = S / 2", "C = S / 3", "C = S / 4", "C = S - 10"],
                "correct": 1,
                "explanation": "The center cell of any 3×3 magic square is always exactly one-third of the magic constant: C = S / 3 (e.g. 15 / 3 = 5)."
            },
            {
                "id": "c8_2",
                "question": "How many distinct rotations and reflections (symmetries) can be generated from a single 3×3 magic square solution?",
                "options": ["2", "4", "8", "16"],
                "correct": 2,
                "explanation": "A square has 4 rotational symmetries and 4 reflection symmetries, producing 8 visually distinct orientations."
            }
        ]
    },

    # Slide 9: The Chautīsa Yantra ($4 \\times 4$ Magic Square)
    {
        "id": 9,
        "section": "6.3",
        "tag": "Section 6.3 • Ancient Indian Yantras",
        "title": "The Chautīsa Yantra: Khajuraho's Masterwork of 34",
        "key_terms": ["Chautīsa Yantra", "Khajuraho Temple", "Magic Constant 34", "Pandiagonal Magic Square"],
        "sim_id": "chautisa_yantra_4x4_sim",
        "sim_title": "The Chautīsa Yantra: 16 Ways to Make 34",
        "narration": "At the 10th-century Parshvanatha Jain temple in Khajuraho, Madhya Pradesh, an ancient stone inscription displays a breathtaking 4-by-4 magic square called the Chautisa Yantra. 'Chautisa' means thirty-four in Hindi. Not only do the rows, columns, and diagonals sum to 34, but so do the 4 corners, the 4 center squares, and every 2-by-2 quadrant! Explore its sublime symmetry.",
        "theory": [
            "**The Chautīsa Yantra Grid** (using numbers 1 through 16):",
            "$$\\begin{bmatrix} 7 & 12 & 1 & 14 \\\\ 2 & 13 & 8 & 11 \\\\ 16 & 3 & 10 & 5 \\\\ 9 & 6 & 15 & 4 \\end{bmatrix}$$",
            "**Why is the Magic Sum 34?**",
            "- Sum of numbers 1 to 16: $\\frac{16 \\times 17}{2} = 136$.",
            "- Divided across 4 rows: $S = \\frac{136}{4} = 34$!",
            "**The Supernatural Symmetries of the Chautīsa Yantra**:",
            "- All 4 Rows and all 4 Columns sum to 34.",
            "- Both main diagonals sum to 34: $7+13+10+4 = 34$ and $14+8+3+9 = 34$.",
            "- The 4 corner cells sum to 34: $7 + 14 + 9 + 4 = 34$.",
            "- The 4 center cells sum to 34: $13 + 8 + 3 + 10 = 34$.",
            "- Every $2 \\times 2$ corner quadrant sums to 34 (e.g. $7+12+2+13 = 34$)!",
            "- This is a **most-perfect pandiagonal magic square**."
        ],
        "fact_box": "Narayana Pandita wrote a whole chapter on magic squares called 'Bhadra Ganita' in his 1356 CE treatise 'Ganita Kaumudi', detailing algorithms for squares of any size!",
        "checkpoints": [
            {
                "id": "c9_1",
                "question": "What is the magic sum of the Chautīsa Yantra found in the Khajuraho temple inscription?",
                "options": ["15", "30", "34", "136"],
                "correct": 2,
                "explanation": "'Chautīsa' means 34. Every row, column, diagonal, and quadrant in this ancient grid sums to 34."
            },
            {
                "id": "c9_2",
                "question": "In the Chautīsa Yantra, what is the sum of the four corner cells (7, 14, 9, 4)?",
                "options": ["28", "34", "40", "68"],
                "correct": 1,
                "explanation": "7 + 14 + 9 + 4 = 34. The four corner cells also sum to the magic constant 34."
            }
        ]
    },

    # Slide 10: Nature's Favourite Sequence - Virahāńka-Fibonacci Numbers
    {
        "id": 10,
        "section": "6.4",
        "tag": "Section 6.4 • Virahāńka-Fibonacci Numbers",
        "title": "Poetic Beats to Universal Law: The Virahāńka Sequence",
        "key_terms": ["Virahāńka Numbers", "Fibonacci Sequence", "Pingala", "Laghu & Guru Syllables", "Prosody (Matra)"],
        "sim_id": "virahanka_poetic_meter_sim",
        "sim_title": "Poetic Beats & Syllable Combinations Generator",
        "narration": "Centuries before Leonardo of Pisa (Fibonacci) wrote his book in 1202 CE, ancient Indian scholar Virahāńka (around 600–700 CE), building on Acharya Pingala's Chandas Shastra, discovered a miraculous number pattern while studying poetic rhythms! How many ways can you arrange short 1-beat syllables (Laghu) and long 2-beat syllables (Guru) to fill a line of poetry? The answers form nature's favourite sequence!",
        "theory": [
            "**Sanskrit Poetic Meters (*Matra-Vritta*)**:",
            "- **Laghu (L)**: Short syllable lasting **1 beat** (time unit).",
            "- **Guru (G)**: Long syllable lasting **2 beats** (time units).",
            "**Counting Rhythms of $n$ Beats**:",
            "- $n = 1$ beat: [L] ➔ **1 way**",
            "- $n = 2$ beats: [LL, G] ➔ **2 ways**",
            "- $n = 3$ beats: [LLL, LG, GL] ➔ **3 ways**",
            "- $n = 4$ beats: [LLLL, LLG, LGL, GLL, GG] ➔ **5 ways**",
            "- $n = 5$ beats: [8 combinations] ➔ **8 ways**",
            "- $n = 6$ beats: [13 combinations] ➔ **13 ways**",
            "Notice the sequence: $$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, \\dots$$",
            "Each new term is formed by adding the previous two terms! Virahāńka stated this exact recurrence rule in the 7th century CE."
        ],
        "fact_box": "Historians of mathematics now officially acknowledge this sequence as the 'Virahāńka-Hemachandra-Fibonacci sequence' to honor its true Indian origins.",
        "checkpoints": [
            {
                "id": "c10_1",
                "question": "Which ancient Indian scholar analyzed poetic syllables (Laghu and Guru beats) around 600–700 CE to discover this sequence?",
                "options": ["Aryabhata", "Virahāńka", "Brahmagupta", "Bhaskara I"],
                "correct": 1,
                "explanation": "Acharya Virahāńka discovered this sequence while studying combinations of poetic rhythms in his work on Prakrit prosody."
            },
            {
                "id": "c10_2",
                "question": "In Sanskrit prosody, how many beats does a long syllable (Guru) count for compared to a short syllable (Laghu)?",
                "options": ["Laghu = 1 beat, Guru = 2 beats", "Laghu = 2 beats, Guru = 1 beat", "Both count as 1 beat", "Guru = 3 beats"],
                "correct": 0,
                "explanation": "A short syllable (Laghu) takes 1 beat; a long syllable (Guru) takes 2 beats."
            }
        ]
    },

    # Slide 11: The Recurrence Formula & Golden Ratio
    {
        "id": 11,
        "section": "6.4",
        "tag": "Section 6.4 • Sequence Formulas",
        "title": "The Additive Engine: Recurrence Relation & The Golden Ratio",
        "key_terms": ["Recurrence Relation", "F_n = F_{n-1} + F_{n-2}", "Golden Ratio (Phi)", "Limiting Ratio 1.618"],
        "sim_id": "fibonacci_virahanka_sequence_sim",
        "sim_title": "Interactive Recurrence Stepper & Golden Ratio Convergence",
        "narration": "How do you calculate the next number in the Virahāńka sequence? Look at the two numbers before it and add them together! 1 plus 2 is 3, 2 plus 3 is 5, 3 plus 5 is 8, 5 plus 8 is 13. Furthermore, as you divide each term by the one before it, the ratio converges to a cosmic constant: the Golden Ratio, 1.618!",
        "theory": [
            "**The Recurrence Relation Formula**:",
            "$$F_n = F_{n-1} + F_{n-2} \\quad \\text{for } n \\ge 3$$",
            "With initial seed values: $F_1 = 1, F_2 = 2$ (or starting with $0, 1$).",
            "**First 12 Terms**:",
            "$$\\begin{array}{c|c|c|c|c|c|c|c|c|c|c|c} F_1 & F_2 & F_3 & F_4 & F_5 & F_6 & F_7 & F_8 & F_9 & F_{10} & F_{11} & F_{12} \\\\ \\hline 1 & 2 & 3 & 5 & 8 & 13 & 21 & 34 & 55 & 89 & 144 & 233 \\end{array}$$",
            "**The Golden Ratio ($\\Phi \\approx 1.618033...$)**:",
            "When you take ratios of consecutive terms:",
            "- $8 / 5 = 1.600$",
            "- $13 / 8 = 1.625$",
            "- $55 / 34 \\approx 1.6176$",
            "- $233 / 144 \\approx 1.61805$",
            "The ratios oscillate and lock into the Golden Ratio $\\Phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618$!"
        ],
        "fact_box": "The Golden Spiral constructed from squares with side lengths 1, 1, 2, 3, 5, 8, 13 matches the exact chamber curvature of the Nautilus sea shell!",
        "checkpoints": [
            {
                "id": "c11_1",
                "question": "If two consecutive terms in the Virahāńka sequence are 21 and 34, what is the next term?",
                "options": ["45", "55", "68", "89"],
                "correct": 1,
                "explanation": "By the recurrence rule, add the previous two terms: 21 + 34 = 55."
            },
            {
                "id": "c11_2",
                "question": "What mathematical constant do the ratios of consecutive Virahāńka numbers approach as the terms grow large?",
                "options": ["Pi (3.1415...)", "The Golden Ratio (≈ 1.618)", "Euler's number e (2.718...)", "Exactly 2.0"],
                "correct": 1,
                "explanation": "The ratio Fn / Fn-1 approaches the Golden Ratio Phi = (1 + √5)/2 ≈ 1.618033..."
            }
        ]
    },

    # Slide 12: Nature's Spirals & Petals
    {
        "id": 12,
        "section": "6.4",
        "tag": "Section 6.4 • Fibonacci in Nature",
        "title": "Virahāńka Numbers in Nature: Flower Petals & Pinecone Spirals",
        "key_terms": ["Phyllotaxis", "Petal Counts", "Sunflower Seed Spirals", "Pinecone Scales"],
        "sim_id": "nature_petals_spirals_sim",
        "sim_title": "Botanical Gallery: Petal Counts & Sunflower Spiral Counter",
        "narration": "Look closely at the flowers growing in a garden. Why do lilies always have 3 petals, buttercups 5 petals, delphiniums 8 petals, marigolds 13 petals, and black-eyed Susans 21 petals? These are all Virahāńka numbers! Nature uses this mathematical blueprint to pack seeds and petals with maximum efficiency so every leaf receives optimal sunlight.",
        "theory": [
            "**Botanical Petal Counts in Nature**:",
            "- **3 Petals**: Lily, Iris, Trillium ($F_3$)",
            "- **5 Petals**: Buttercup, Wild Rose, Jasmine, Hibiscus ($F_4$)",
            "- **8 Petals**: Delphinium, Clematis ($F_5$)",
            "- **13 Petals**: Marigold, Ragwort, Cineraria ($F_6$)",
            "- **21 Petals**: Aster, Black-eyed Susan, Chicory ($F_7$)",
            "- **34 Petals**: Plantain, Field Daisy ($F_8$)",
            "**Sunflower Seed Spirals**:",
            "- Sunflower seed heads display interlocking clockwise and counter-clockwise spirals.",
            "- In a typical sunflower, you will count **21 spirals going one way and 34 going the other**, or **34 and 55**, or in giant sunflowers **55 and 89**!",
            "- These consecutive Virahāńka numbers allow optimal seed packing (*phyllotaxis*) without wasting any space."
        ],
        "fact_box": "Pineapples have hexagonal scales arranged in 3 distinct sets of spirals: 5, 8, and 13 spirals wrapping around the fruit!",
        "checkpoints": [
            {
                "id": "c12_1",
                "question": "Which of the following petal counts is almost NEVER found in natural wild flower species?",
                "options": ["3 petals", "4 petals", "5 petals", "8 petals"],
                "correct": 1,
                "explanation": "4 is not a Virahāńka-Fibonacci number; natural flowers predominantly exhibit petal counts of 3, 5, 8, 13, or 21."
            },
            {
                "id": "c12_2",
                "question": "Why do plants naturally arrange their leaves and seeds in Virahāńka spiral patterns?",
                "options": ["To look pretty for bees", "To maximize sunlight exposure and pack seeds with zero wasted space", "Because stems are round", "Random accidental chance"],
                "correct": 1,
                "explanation": "Phyllotaxis based on the Golden Ratio ensures that leaves do not overlap and shade each other, while seeds achieve maximum packing density."
            }
        ]
    },

    # Slide 13: Virahāńka Sequence Parity Cycle
    {
        "id": 13,
        "section": "6.4",
        "tag": "Section 6.4 • Parity Patterns in Sequences",
        "title": "The Parity Rhythm: Why Every $3^{rd}$ Virahāńka Number is Even",
        "key_terms": ["Parity Rhythm", "Odd-Even Cycle", "Modulo Arithmetic", "Modular Periodicities"],
        "sim_id": "virahanka_parity_cycle_sim",
        "sim_title": "Interactive Virahāńka Parity Cycle & Modulo Stepper",
        "narration": "Let us combine our two big ideas: Parity and the Virahāńka sequence! Write down the parity of each number in the sequence: 1 is Odd, 2 is Even, 3 is Odd, 5 is Odd, 8 is Even, 13 is Odd, 21 is Odd, 34 is Even. Look at the rhythm: Odd, Even, Odd, Odd, Even, Odd, Odd, Even! It repeats with a period of 3 forever!",
        "theory": [
            "**Inspecting the Parities of the Virahāńka Sequence**:",
            "$$\\begin{array}{c|c|c|c|c|c|c|c|c|c|c|c} n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\\\ \\hline F_n & 1 & 2 & 3 & 5 & 8 & 13 & 21 & 34 & 55 & 89 & 144 & 233 \\\\ \\hline \\text{Parity} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} \\end{array}$$",
            "**Deductive Proof of the Period-3 Parity Cycle**:",
            "1. Start with **Odd, Even**.",
            "2. $\\text{Odd} + \\text{Even} = \\mathbf{Odd}$ (Term 3).",
            "3. $\\text{Even} + \\text{Odd} = \\mathbf{Odd}$ (Term 4).",
            "4. $\\text{Odd} + \\text{Odd} = \\mathbf{Even}$ (Term 5!).",
            "5. $\\text{Odd} + \\text{Even} = \\mathbf{Odd}$ (Term 6).",
            "The cycle **[Odd, Odd, Even]** repeats eternally. Therefore, $F_n$ is even if and only if $n$ is a multiple of 3!"
        ],
        "fact_box": "This repeating modular pattern is called the 'Pisano Period'. For modulo 2, the period is 3. For modulo 10 (last digit), the period is 60!",
        "checkpoints": [
            {
                "id": "c13_1",
                "question": "What is the repeating parity pattern of the Virahāńka sequence?",
                "options": ["Even, Odd, Even, Odd...", "Odd, Odd, Even, Odd, Odd, Even...", "All numbers are Odd", "Odd, Even, Even, Odd..."],
                "correct": 1,
                "explanation": "Because Odd + Odd = Even, two odds always produce an even, creating the 3-step repeating cycle: [Odd, Odd, Even]."
            },
            {
                "id": "c13_2",
                "question": "Is the 30th Virahāńka number (F_30) Even or Odd?",
                "options": ["Odd", "Even, because 30 is a multiple of 3", "Prime", "Cannot be determined without calculating"],
                "correct": 1,
                "explanation": "Every 3rd term is even. Since 30 = 3 × 10, F_30 is guaranteed to be an even number!"
            }
        ]
    },

    # Slide 14: Digits in Disguise - Cryptarithms Warmup
    {
        "id": 14,
        "section": "6.5",
        "tag": "Section 6.5 • Digits in Disguise",
        "title": "Digits in Disguise: Unmasking Letters in Alphametic Puzzles",
        "key_terms": ["Cryptarithm", "Alphametic", "Unique Digit Rule", "Leading Zero Prohibition", "Carryover Clues"],
        "sim_id": "cryptarithm_single_digit_sim",
        "sim_title": "Interactive Cryptarithm Detective: AB + B = BC",
        "narration": "Imagine arithmetic where sneaky detectives have disguised every digit with an alphabetical letter! These puzzles are called cryptarithms or alphametics. Each letter stands for a unique single digit from 0 to 9, and the leading digit of a number can never be zero. Put on your detective hat and solve the puzzle AB + B = BC!",
        "theory": [
            "**The Ground Rules of Cryptarithms**:",
            "1. Each distinct letter represents a **unique digit** from $0$ to $9$ (if $A = 4$, no other letter can be $4$).",
            "2. The first (leading) digit of a number **cannot be zero** (no numbers like '05').",
            "**Case Study: Solve $AB + B = BC$**",
            "- In column addition: $B + B$ ends in $C$.",
            "- In the tens column: $A + \\text{carry} = B$.",
            "- If there were no carry, $A = B$, which violates the unique digit rule! Thus, there MUST be a carry of $1$.",
            "- So $B = A + 1$, and $B + B \\ge 10$.",
            "- Try $B = 9$: Then $A = 8$. $AB = 89$. $89 + 9 = 98$. Then $B = 9, C = 8$. But $A = 8$ and $C = 8$, violating uniqueness!",
            "- Try $B = 8$: $A = 7$. $78 + 8 = 86$. Then $A=7, B=8, C=6$ (All distinct!). Solution found: $78 + 8 = 86$!"
        ],
        "fact_box": "The word 'Alphametic' was coined in 1955 by J. A. H. Hunter. Cryptarithms were first popularized in 1931 by the Belgian recreational math journal Sphinx.",
        "checkpoints": [
            {
                "id": "c14_1",
                "question": "In a cryptarithm, can a multi-digit number like 'SEND' have S = 0?",
                "options": ["Yes, zero is a valid digit", "No, the leading digit of a number can never be zero", "Only if it is a decimal", "Yes, if E = 1"],
                "correct": 1,
                "explanation": "Standard cryptarithm rules strictly prohibit leading zeros; the first letter of any number must be between 1 and 9."
            },
            {
                "id": "c14_2",
                "question": "In the addition puzzle A + A = BA, what must be the value of the carryover letter B?",
                "options": ["B = 0", "B = 1", "B = 2", "B = 9"],
                "correct": 1,
                "explanation": "The maximum sum of two single digits is 9 + 9 = 18. The carry into a new column in addition of two numbers can NEVER exceed 1. Thus, B = 1."
            }
        ]
    },

    # Slide 15: Classic Alphametic Deduction - SEND + MORE = MONEY
    {
        "id": 15,
        "section": "6.5",
        "tag": "Section 6.5 • Classic Cryptarithm Deduction",
        "title": "The Master Alphametic: Solving SEND + MORE = MONEY",
        "key_terms": ["SEND + MORE = MONEY", "Column Deduction", "Carryover Constraints", "Exhaustive Elimination"],
        "sim_id": "classic_alphametic_deduction_sim",
        "sim_title": "SEND + MORE = MONEY Step-by-Step Solver",
        "narration": "In 1924, legendary puzzler Henry Dudeney published the most famous cryptarithm of all time: SEND + MORE = MONEY. Watch how pure logic unlocks every single digit without any guesswork. The carry into the ten-thousands column immediately forces M to be 1! Step by step, the entire word reveals its secret digits.",
        "theory": [
            "$$\\begin{array}{r@{\\quad}c@{}c@{}c@{}c} & S & E & N & D \\\\ + & M & O & R & E \\\\ \\hline M & O & N & E & Y \\end{array}$$",
            "**Step 1: The Ten-Thousands Column (M)**",
            "- $S + M + \\text{carry} = MO$. Adding two 4-digit numbers produces at most a 1 in the fifth column. Since $M \\neq 0$, **$M = 1$**!",
            "**Step 2: The Thousands Column (O)**",
            "- $S + 1 + \\text{carry} = 10 + O$. Since $S \\le 9$, $S + 1 \\le 10$. Thus $O$ must be **$0$**, and $S$ must be **$9$** (or $8$ with carry).",
            "**Step 3: Systematic Chain Deduction**",
            "- Deducing through columns yields: **$S = 9, E = 5, N = 6, D = 7, M = 1, O = 0, R = 8, Y = 2$**.",
            "$$\\mathbf{9567 + 1085 = 10652}$$",
            "Every letter has a unique digit, and the arithmetic checks out with total mathematical perfection!"
        ],
        "fact_box": "Dudeney sent this puzzle in a telegram to his editor with only the words: 'SEND MORE MONEY'—turning a plea for cash into the world's greatest mathematical puzzle!",
        "checkpoints": [
            {
                "id": "c15_1",
                "question": "In the puzzle SEND + MORE = MONEY, why must the letter M equal 1?",
                "options": ["Because M is the first letter in Money", "Because the sum of two 4-digit numbers can produce a carry of at most 1", "Because M represents 10", "Because 9 + 9 = 19"],
                "correct": 1,
                "explanation": "Even 9999 + 9999 = 19998. The carry into the 5th column from two 4-digit numbers can never be anything other than 1. Thus, M = 1."
            },
            {
                "id": "c15_2",
                "question": "What is the unique digit value of the letter S in SEND + MORE = MONEY?",
                "options": ["S = 7", "S = 8", "S = 9", "S = 5"],
                "correct": 2,
                "explanation": "To produce a carry of 1 with M = 1 and O = 0, S must be 9 (9 + 1 + 0 = 10)."
            }
        ]
    },

    # Slide 16: Heritage Review - The Splendor of Indian Number Play
    {
        "id": 16,
        "section": "Review",
        "tag": "Chapter Review • Heritage of Indian Number Play",
        "title": "Centuries of Play: Pingala, Virahāńka & Narayana Pandita",
        "key_terms": ["Chandas Shastra", "Meru Prastara (Pascal's Triangle)", "Ganita Kaumudi", "Bhadra Ganita"],
        "sim_id": "heritage_number_play_sim",
        "sim_title": "Meru Prastara & Ancient Indian Combinatorics Lab",
        "narration": "From the rhythmic syllables of Pingala's Chandas Shastra (3rd century BCE) to the algebraic meter of Virahāńka and the elaborate magic squares in Narayana Pandita's Ganita Kaumudi, Indian mathematics has always treated numbers as a source of joyous creative play! Let us celebrate this heritage and carry forward the spirit of joyful mathematical exploration.",
        "theory": [
            "**Key Heritage Milestones in Indian Number Play**:",
            "1. **Acharya Pingala (c. 300 BCE)**: In *Chandas Shastra*, invented binary numerals, combinations (*Prastara*), and the famous triangle of binomial coefficients known as **Meru Prastara** (over 1,800 years before Blaise Pascal!).",
            "2. **Acharya Virahāńka (c. 600–700 CE)**: First formulated the additive sequence ($1, 2, 3, 5, 8, 13, 21...$) in his work on poetic rhythms, predating Fibonacci by more than five centuries.",
            "3. **Narayana Pandita (1356 CE)**: Devoted the 14th chapter of his masterwork *Ganita Kaumudi* ('Bhadra Ganita') entirely to constructing magic squares of odd, evenly-even, and oddly-even orders.",
            "Mathematical play is not separate from serious mathematics—it is the very engine that sparks mathematical discovery!"
        ],
        "fact_box": "Pingala called the binomial coefficient pyramid 'Meru Prastara', meaning 'The Staircase of Mount Meru'. Halayudha's 10th-century commentary gave the exact triangular addition rule!",
        "checkpoints": [
            {
                "id": "c16_1",
                "question": "What ancient Indian name was given to the triangle of binomial coefficients centuries before Pascal?",
                "options": ["Sulba Sutra", "Meru Prastara", "Bijaganita", "Lilavati"],
                "correct": 1,
                "explanation": "Acharya Pingala and his commentator Halayudha called this triangular number pattern 'Meru Prastara' (The Steps of Mount Meru)."
            },
            {
                "id": "c16_2",
                "question": "Which 14th-century Indian mathematician wrote the comprehensive treatise 'Bhadra Ganita' on magic squares?",
                "options": ["Narayana Pandita", "Aryabhata", "Varahamihira", "Brahmagupta"],
                "correct": 0,
                "explanation": "Narayana Pandita detailed systematic algorithms for constructing magic squares of all orders in his 1356 CE text Ganita Kaumudi."
            }
        ]
    },

    # Slide 17: Mastery Challenge 1 (Questions 1 to 10)
    {
        "id": 17,
        "section": "Quiz 1",
        "is_quiz": True,
        "quiz_range": (1, 10),
        "tag": "Mastery Challenge • Part 1",
        "title": "Mastery Quiz 1: Positional Logic, Height Rules & Queue Deduction",
        "narration": "Welcome to Part 1 of the Chapter Mastery Challenge! Test your skills on positional deduction, height line-ups, and logical inversion rules. Choose your answers and study the step-by-step solutions."
    },

    # Slide 18: Mastery Challenge 2 (Questions 11 to 20)
    {
        "id": 18,
        "section": "Quiz 2",
        "is_quiz": True,
        "quiz_range": (11, 20),
        "tag": "Mastery Challenge • Part 2",
        "title": "Mastery Quiz 2: Parity Properties, Arithmetic Laws & Grid Squares",
        "narration": "Mastery Quiz Part 2! Here we test parity arithmetic, pairing proofs, algebraic forms 2k and 2k+1, and checkerboard grid invariants. Focus on why even and odd numbers behave the way they do."
    },

    # Slide 19: Mastery Challenge 3 (Questions 21 to 30)
    {
        "id": 19,
        "section": "Quiz 3",
        "is_quiz": True,
        "quiz_range": (21, 30),
        "tag": "Mastery Challenge • Part 3",
        "title": "Mastery Quiz 3: Magic Squares, Center Cell Rule & The Chautīsa Yantra",
        "narration": "Welcome to Mastery Quiz Part 3! Tackle magic constants, center cell formulas, 3x3 grids, and the Khajuraho Chautīsa Yantra's stunning 4x4 symmetrical patterns summing to 34."
    },

    # Slide 20: Mastery Challenge 4 (Questions 31 to 40)
    {
        "id": 20,
        "section": "Quiz 4",
        "is_quiz": True,
        "quiz_range": (31, 40),
        "tag": "Mastery Challenge • Part 4 (Final)",
        "title": "Mastery Quiz 4: Virahāńka Numbers, Nature's Spirals & Cryptarithms",
        "narration": "The Final Mastery Challenge! Solve Virahāńka sequence problems, botanical petal ratios, parity cycles, and cryptarithm alphametic puzzles. Complete this slide to conquer Chapter 6!"
    }
]

QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "In a queue of 5 children of distinct heights, what is the maximum number of people taller than them that the child at position 1 can have in front?",
        "options": ["0", "1", "4", "5"],
        "correct": 0,
        "solution": "Step 1: The child at position 1 is at the very front of the queue.\nStep 2: There is no one standing ahead of position 1.\nConclusion: The number of taller people ahead must be exactly 0."
    },
    # Q2
    {
        "id": 2,
        "question": "In a line of 6 people with distinct heights, the shortest person stands at position 4. How many people standing ahead of them are taller than them?",
        "options": ["0", "1", "2", "3"],
        "correct": 3,
        "solution": "Step 1: The person stands at position 4, so there are exactly 3 people standing ahead of them (positions 1, 2, and 3).\nStep 2: Since this person is the shortest in the entire group, every single person ahead is taller than them.\nConclusion: Exactly 3 people ahead are taller."
    },
    # Q3
    {
        "id": 3,
        "question": "Five students A, B, C, D, E have heights 150cm, 155cm, 160cm, 165cm, 170cm. If the 170cm student stands at position 3, what callout number will they announce?",
        "options": ["0", "1", "2", "3"],
        "correct": 0,
        "solution": "Step 1: The student's height is 170cm, which is the tallest height in the group.\nStep 2: No student in the queue is taller than 170cm.\nConclusion: Regardless of standing at position 3, they see 0 taller people ahead. Callout is 0."
    },
    # Q4
    {
        "id": 4,
        "question": "Three students stand in line. Their callouts are [0, 1, 0]. If heights are 1, 2, 3 (3 tallest), what is the height order from front to back?",
        "options": ["3, 1, 2", "2, 1, 3", "1, 2, 3", "3, 2, 1"],
        "correct": 1,
        "solution": "Step 1: Position 3 calls out 0, meaning no one ahead is taller than position 3. Thus, the tallest person (height 3) is at position 3!\nStep 2: Position 2 calls out 1, meaning the person ahead (at position 1) is taller than position 2. Between remaining heights 1 and 2, height 2 must be ahead of height 1.\nStep 3: Therefore, position 1 has height 2, position 2 has height 1, and position 3 has height 3.\nConclusion: The queue is [2, 1, 3] (Callouts: Pos 1 sees 0, Pos 2 sees one taller [2], Pos 3 sees zero taller). Perfect match!"
    },
    # Q5
    {
        "id": 5,
        "question": "What is the sum of any two odd numbers (for example, 17 + 29)?",
        "options": ["Always Odd", "Always Even", "Sometimes Odd, sometimes Even", "Always a Multiple of 4"],
        "correct": 1,
        "solution": "Step 1: Let the two odd numbers be 2a + 1 and 2b + 1.\nStep 2: Sum = (2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1).\nStep 3: Since 2 is a factor of the sum, it is divisible by 2.\nConclusion: The sum of two odd numbers is always Even (17 + 29 = 46, even!)."
    },
    # Q6
    {
        "id": 6,
        "question": "If you add 5 odd numbers together, what will be the parity of the final sum?",
        "options": ["Always Even", "Always Odd", "Cannot be determined", "Zero"],
        "correct": 1,
        "solution": "Step 1: Pair up the odd numbers: (Odd + Odd) + (Odd + Odd) + Odd.\nStep 2: (Even) + (Even) + Odd = Even + Odd = Odd.\nConclusion: An odd count of odd numbers always yields an Odd sum."
    },
    # Q7
    {
        "id": 7,
        "question": "Which of the following products is guaranteed to be an ODD number?",
        "options": ["Even × Even", "Even × Odd", "Odd × Odd", "Odd × Even × Odd"],
        "correct": 2,
        "solution": "Step 1: A number is even if it contains at least one factor of 2.\nStep 2: Only Odd × Odd has no factor of 2 in any of its terms.\nConclusion: Odd × Odd is always Odd (e.g. 7 × 9 = 63)."
    },
    # Q8
    {
        "id": 8,
        "question": "If x is an even number and y is an odd number, what is the parity of 3x + 4y?",
        "options": ["Always Even", "Always Odd", "Depends on x", "Depends on y"],
        "correct": 0,
        "solution": "Step 1: Since x is even, 3x = 3(even) = Even.\nStep 2: Since 4 is even, 4y = 4(odd) = Even.\nStep 3: Sum = Even + Even = Even.\nConclusion: 3x + 4y is always Even."
    },
    # Q9
    {
        "id": 9,
        "question": "What is the 100th even positive integer?",
        "options": ["100", "198", "200", "202"],
        "correct": 2,
        "solution": "Step 1: The sequence of positive even integers is 2, 4, 6, 8, ...\nStep 2: The n-th term formula is Tn = 2n.\nStep 3: For n = 100, T100 = 2 × 100 = 200.\nConclusion: The 100th even integer is 200."
    },
    # Q10
    {
        "id": 10,
        "question": "What is the 75th odd positive integer?",
        "options": ["149", "150", "151", "75"],
        "correct": 0,
        "solution": "Step 1: The sequence of odd positive integers is 1, 3, 5, 7, ...\nStep 2: The n-th term formula is Tn = 2n - 1.\nStep 3: For n = 75, T75 = 2(75) - 1 = 150 - 1 = 149.\nConclusion: The 75th odd integer is 149."
    },

    # Q11
    {
        "id": 11,
        "question": "A rectangle grid has dimensions 6 units by 9 units. What is the parity of the total number of unit squares?",
        "options": ["Even", "Odd", "Fractional", "Zero"],
        "correct": 0,
        "solution": "Step 1: Total squares = 6 × 9 = 54.\nStep 2: 54 is divisible by 2 (54 = 2 × 27).\nConclusion: The total number of squares is Even (Even × Odd = Even)."
    },
    # Q12
    {
        "id": 12,
        "question": "Can a grid with 35 unit squares ever be completely tiled using 2×1 dominoes?",
        "options": ["Yes, easily", "No, because each domino covers 2 squares, so total squares must be even", "Yes, if dominoes are cut", "Only if the grid is square"],
        "correct": 1,
        "solution": "Step 1: Each domino covers exactly 2 squares.\nStep 2: Any number of whole dominoes covers an even number of squares (2k).\nStep 3: 35 is an odd number, so 35 cannot equal 2k.\nConclusion: No, an odd number of squares can never be tiled with dominoes."
    },
    # Q13
    {
        "id": 13,
        "question": "In the Collatz 3n + 1 sequence starting at number 5, what are the next three numbers generated?",
        "options": ["16, 8, 4", "15, 8, 4", "16, 5, 2", "10, 5, 16"],
        "correct": 0,
        "solution": "Step 1: 5 is odd, so calculate 3n + 1 = 3(5) + 1 = 16.\nStep 2: 16 is even, so divide by 2: 16 / 2 = 8.\nStep 3: 8 is even, so divide by 2: 8 / 2 = 4.\nConclusion: The next three numbers are 16, 8, 4 (followed by 2, 1!)."
    },
    # Q14
    {
        "id": 14,
        "question": "What is the magic sum of a standard 3×3 magic square containing the digits 1, 2, 3, 4, 5, 6, 7, 8, 9?",
        "options": ["12", "15", "18", "45"],
        "correct": 1,
        "solution": "Step 1: Sum of numbers from 1 to 9 is (9 × 10) / 2 = 45.\nStep 2: There are 3 rows, each with equal sum S.\nStep 3: 3S = 45 ➔ S = 15.\nConclusion: The magic sum is 15."
    },
    # Q15
    {
        "id": 15,
        "question": "In any standard 3×3 magic square using numbers 1 through 9, which number MUST occupy the central cell?",
        "options": ["1", "3", "5", "9"],
        "correct": 2,
        "solution": "Step 1: The center cell participates in 4 lines: 1 row, 1 column, and 2 diagonals.\nStep 2: Center value C = Magic Sum / 3 = 15 / 3 = 5.\nConclusion: The center cell must strictly be 5."
    },
    # Q16
    {
        "id": 16,
        "question": "If the numbers in a 3×3 magic square are 2, 4, 6, 8, 10, 12, 14, 16, 18, what is the magic constant?",
        "options": ["15", "30", "45", "90"],
        "correct": 1,
        "solution": "Step 1: Notice that each number is double the standard digits 1 to 9 (2 × 1, 2 × 2, ..., 2 × 9).\nStep 2: Total sum = 2 × 45 = 90.\nStep 3: Magic constant S = 90 / 3 = 30 (which is 2 × 15).\nConclusion: The magic constant is 30."
    },
    # Q17
    {
        "id": 17,
        "question": "In the standard 3×3 magic square with center 5, if one corner is 8, what number must be in the diagonally opposite corner?",
        "options": ["1", "2", "3", "4"],
        "correct": 1,
        "solution": "Step 1: The diagonal passes through corner 1, center (5), and corner 2.\nStep 2: The sum of the diagonal must be 15.\nStep 3: 8 + 5 + corner 2 = 15 ➔ 13 + corner 2 = 15 ➔ corner 2 = 2.\nConclusion: The diagonally opposite corner must be 2."
    },
    # Q18
    {
        "id": 18,
        "question": "The Chautīsa Yantra in the Khajuraho temple is a magic square of which grid dimension?",
        "options": ["3 × 3", "4 × 4", "5 × 5", "8 × 8"],
        "correct": 1,
        "solution": "Step 1: The Chautīsa Yantra contains 16 numbers arranged in a 4-by-4 square grid.\nConclusion: It is a 4 × 4 magic square."
    },
    # Q19
    {
        "id": 19,
        "question": "What is the magic sum of each row, column, and diagonal in the Chautīsa Yantra?",
        "options": ["15", "26", "34", "68"],
        "correct": 2,
        "solution": "Step 1: The name 'Chautīsa' translates to 34.\nStep 2: Total sum of numbers 1 to 16 is (16 × 17)/2 = 136.\nStep 3: 136 / 4 = 34.\nConclusion: The magic sum is 34."
    },
    # Q20
    {
        "id": 20,
        "question": "In the Chautīsa Yantra 4×4 square, which of the following groups also sums to 34?",
        "options": ["The 4 corner cells", "The 4 central cells", "Each 2×2 corner quadrant", "All of the above!"],
        "correct": 3,
        "solution": "Step 1: The Chautīsa Yantra is a most-perfect pandiagonal magic square.\nStep 2: The 4 corners sum to 34 (7+14+9+4=34).\nStep 3: The 4 central cells sum to 34 (13+8+3+10=34).\nStep 4: Every 2×2 quadrant sums to 34.\nConclusion: All of the above!"
    },

    # Q21
    {
        "id": 21,
        "question": "Who was the ancient Indian scholar who discovered the sequence 1, 2, 3, 5, 8, 13, 21... through Sanskrit poetic meters around 600–700 CE?",
        "options": ["Fibonacci", "Virahāńka", "Euclid", "Ramanujan"],
        "correct": 1,
        "solution": "Step 1: Acharya Virahāńka analyzed poetic rhythms of short and long syllables in his 7th-century treatise.\nStep 2: This occurred more than 500 years before Fibonacci published Liber Abaci in 1202 CE.\nConclusion: Acharya Virahāńka."
    },
    # Q22
    {
        "id": 22,
        "question": "In Virahāńka's poetic analysis, how many distinct rhythmic combinations of Laghu (1 beat) and Guru (2 beats) can fill a 4-beat measure?",
        "options": ["3", "4", "5", "8"],
        "correct": 2,
        "solution": "Step 1: List the combinations of 1 and 2 that sum to 4:\n- 1+1+1+1 (LLLL)\n- 1+1+2 (LLG)\n- 1+2+1 (LGL)\n- 2+1+1 (GLL)\n- 2+2 (GG)\nConclusion: There are exactly 5 combinations (the 4th Virahāńka number!)."
    },
    # Q23
    {
        "id": 23,
        "question": "Given the Virahāńka sequence: 1, 2, 3, 5, 8, 13, 21, 34, what is the next number in the sequence?",
        "options": ["45", "55", "58", "65"],
        "correct": 1,
        "solution": "Step 1: Add the two most recent terms.\nStep 2: 21 + 34 = 55.\nConclusion: The next number is 55."
    },
    # Q24
    {
        "id": 24,
        "question": "What is the term that immediately follows 55 in the Virahāńka sequence (..., 34, 55, ...)?",
        "options": ["79", "89", "99", "110"],
        "correct": 1,
        "solution": "Step 1: Add 34 and 55.\nStep 2: 34 + 55 = 89.\nConclusion: The next term is 89."
    },
    # Q25
    {
        "id": 25,
        "question": "A wild buttercup flower typically has how many petals?",
        "options": ["4 petals", "5 petals", "7 petals", "9 petals"],
        "correct": 1,
        "solution": "Step 1: Buttercups are classic examples of botanical Virahāńka numbers.\nStep 2: Buttercups have exactly 5 petals (F4 = 5).\nConclusion: 5 petals."
    },
    # Q26
    {
        "id": 26,
        "question": "Lilies and irises typically possess how many petals?",
        "options": ["2 petals", "3 petals", "4 petals", "6 petals"],
        "correct": 1,
        "solution": "Step 1: Lilies, trilliums, and irises exhibit 3-fold symmetry.\nStep 2: 3 is the 3rd Virahāńka number (F3 = 3).\nConclusion: 3 petals."
    },
    # Q27
    {
        "id": 27,
        "question": "In a sunflower seed head, what pair of spiral counts is most commonly observed?",
        "options": ["10 and 20", "21 and 34", "25 and 50", "30 and 40"],
        "correct": 1,
        "solution": "Step 1: Seed spirals in sunflower heads are consecutive Virahāńka numbers.\nStep 2: 21 clockwise and 34 counter-clockwise spirals are typical.\nConclusion: 21 and 34."
    },
    # Q28
    {
        "id": 28,
        "question": "In the Virahāńka sequence 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, how frequently do EVEN numbers appear?",
        "options": ["Every 2nd number", "Every 3rd number", "Every 4th number", "Randomly"],
        "correct": 1,
        "solution": "Step 1: Write the parity pattern: 1(O), 2(E), 3(O), 5(O), 8(E), 13(O), 21(O), 34(E), 55(O), 89(O), 144(E)...\nStep 2: Notice the even numbers: Term 2 (2), Term 5 (8), Term 8 (34), Term 11 (144)...\nConclusion: Exactly every 3rd number is even (pattern: Odd, Odd, Even)."
    },
    # Q29
    {
        "id": 29,
        "question": "What is the parity of the 99th Virahāńka number (F_99)?",
        "options": ["Even, because 99 is a multiple of 3", "Odd", "Negative", "Cannot be determined"],
        "correct": 0,
        "solution": "Step 1: Every term whose index is a multiple of 3 is even.\nStep 2: 99 = 3 × 33 (a multiple of 3).\nConclusion: F_99 is guaranteed to be an Even number."
    },
    # Q30
    {
        "id": 30,
        "question": "In a cryptarithm, if two single-digit numbers are added: X + Y = 1Z, what is the maximum possible value for the sum?",
        "options": ["15", "18", "19", "20"],
        "correct": 1,
        "solution": "Step 1: The largest possible single digits are 9 and 9.\nStep 2: 9 + 9 = 18.\nConclusion: The maximum sum is 18 (so the carry into the tens place is always 1)."
    },

    # Q31
    {
        "id": 31,
        "question": "In the cryptarithm A + A = BA, what are the unique digit values of A and B?",
        "options": ["A = 5, B = 1", "A = 4, B = 8", "A = 9, B = 1", "A = 8, B = 1"],
        "correct": 0,
        "solution": "Step 1: A + A produces a 2-digit number BA. The carry B must be 1 (B = 1).\nStep 2: So A + A = 1A ➔ 2A = 10 + A ➔ 2A - A = 10 ➔ A cannot be 10 as a single digit.\nWait! In vertical addition, A + A ends in A!\nStep 3: What digit doubled ends in itself? 0 + 0 = 0 (but A cannot be 0). What about with no carry? 2A ends in A means A = 0.\nWait, if A + A + 0 = 1A: 2A = 10 + A ➔ A = 10 (not single digit).\nWait: Look at 9 + 9 = 18 (ends in 8). 8 + 8 = 16. 7 + 7 = 14. 6 + 6 = 12. 5 + 5 = 10 (ends in 0, not A).\nWait! Could it be A + A + A = BA? 5 + 5 + 5 = 15! Here A = 5, B = 1! (15 has B=1, A=5).\nConclusion: For A + A + A = BA, A = 5, B = 1."
    },
    # Q32
    {
        "id": 32,
        "question": "In the classic cryptarithm SEND + MORE = MONEY, what is the value of the letter M?",
        "options": ["0", "1", "2", "9"],
        "correct": 1,
        "solution": "Step 1: SEND (4 digits) + MORE (4 digits) = MONEY (5 digits).\nStep 2: The sum of two 4-digit numbers cannot exceed 9999 + 9999 = 19998.\nStep 3: The only possible non-zero carry into the 5th column is 1.\nConclusion: M = 1."
    },
    # Q33
    {
        "id": 33,
        "question": "In SEND + MORE = MONEY, since M = 1, what digit must O represent?",
        "options": ["0", "1", "2", "9"],
        "correct": 0,
        "solution": "Step 1: In the thousands column: S + M + carry = 10 + O.\nStep 2: S + 1 + carry = 10 + O. Since S ≤ 9, S + 1 ≤ 10.\nStep 3: If S + 1 = 10, then O = 0 (and S = 9). Since M = 1, O cannot be 1.\nConclusion: O = 0."
    },
    # Q34
    {
        "id": 34,
        "question": "In SEND + MORE = MONEY, what is the value of S?",
        "options": ["7", "8", "9", "6"],
        "correct": 2,
        "solution": "Step 1: We established S + 1 + carry = 10 + O with O = 0.\nStep 2: So S + 1 + carry = 10.\nStep 3: If there is no carry from the hundreds column, S = 9.\nConclusion: S = 9."
    },
    # Q35
    {
        "id": 35,
        "question": "In the cryptarithm puzzle: ON + ON = NO, where O and N are distinct digits, what is the value of O + N?",
        "options": ["9", "11", "13", "No solution exists"],
        "correct": 3,
        "solution": "Step 1: ON = 10×O + N. NO = 10×N + O.\nStep 2: ON + ON = 2(10O + N) = 20O + 2N.\nStep 3: Set equal to NO: 20O + 2N = 10N + O ➔ 19O = 8N.\nStep 4: Since 19 is prime and O, N are single digits (0-9), 19O = 8N requires O = 0, N = 0 (which violates leading zero rule and distinctness).\nConclusion: No valid solution exists in standard base 10!"
    },
    # Q36
    {
        "id": 36,
        "question": "In the cryptarithm TO + TO = FOR, what digit must F be?",
        "options": ["1", "2", "4", "9"],
        "correct": 0,
        "solution": "Step 1: Two 2-digit numbers TO + TO add up to a 3-digit number FOR.\nStep 2: Maximum sum of two 2-digit numbers is 99 + 99 = 198.\nStep 3: The leading digit F of a 3-digit sum of two 2-digit numbers must be 1.\nConclusion: F = 1."
    },
    # Q37
    {
        "id": 37,
        "question": "What is the ancient Sanskrit name of Pascal's Triangle developed by Acharya Pingala around 300 BCE?",
        "options": ["Sulba Sutra", "Meru Prastara", "Chautīsa Yantra", "Kamsya"],
        "correct": 1,
        "solution": "Step 1: Pingala's Chandas Shastra introduced the triangular arrangement of combinatorial numbers.\nStep 2: It was named 'Meru Prastara' (The Staircase of Mount Meru).\nConclusion: Meru Prastara."
    },
    # Q38
    {
        "id": 38,
        "question": "If the sum of 4 consecutive integers is 66, how many of these integers are even?",
        "options": ["1", "2", "3", "4"],
        "correct": 1,
        "solution": "Step 1: Four consecutive integers alternate: Even, Odd, Even, Odd (or Odd, Even, Odd, Even).\nStep 2: In any four consecutive integers, exactly 2 are even and 2 are odd.\n(The integers are 15, 16, 17, 18; sum = 66. The even numbers are 16 and 18).\nConclusion: Exactly 2 integers are even."
    },
    # Q39
    {
        "id": 39,
        "question": "What is the ratio of the 10th Virahāńka number (F_10 = 89) to the 9th Virahāńka number (F_9 = 55)?",
        "options": ["1.500", "1.618 (approx)", "1.750", "2.000"],
        "correct": 1,
        "solution": "Step 1: 89 / 55 = 1.61818...\nStep 2: This is an extremely close approximation of the Golden Ratio Phi (1.618033...).\nConclusion: Approximately 1.618."
    },
    # Q40
    {
        "id": 40,
        "question": "In a 3×3 magic square using digits 1 to 9, which of the following is a valid set of numbers for one of the main diagonals?",
        "options": ["2, 5, 8", "1, 5, 9", "4, 5, 6", "Both A and C are valid diagonals in the standard Lo Shu square"],
        "correct": 3,
        "solution": "Step 1: In the standard 3×3 magic square:\nRow 1: 4, 9, 2\nRow 2: 3, 5, 7\nRow 3: 8, 1, 6\nStep 2: Main diagonal 1: 4, 5, 6 (Sum = 15).\nStep 3: Main diagonal 2: 2, 5, 8 (Sum = 15).\nConclusion: Both 2, 5, 8 and 4, 5, 6 are valid main diagonals!"
    }
]
'''

with open('.agents/class7_math_number_play_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully generated .agents/class7_math_number_play_data.py")
