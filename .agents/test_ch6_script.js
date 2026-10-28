
    // Injected Data
    const SLIDES_DATA = [{"id": 1, "section": "6.1", "tag": "Section 6.1 • Numbers Tell us Things", "title": "Numbers Tell us Things: Decoding Line-Up Clues", "key_terms": ["Positional Logic", "Height Clues", "Inverse Deduction", "Queue Arrangement"], "sim_id": "height_queue_decoder_sim", "sim_title": "Interactive Height Line-Up Decoder", "narration": "Namaste, inquisitive minds! I am Acharya Virahāńka. Numbers are not merely tools for counting sheep—they are secret messengers! Imagine a queue of children where each person calls out a number: how many people taller than them stand ahead. From just these whispered numbers, can we reconstruct the exact height order of the entire line? Let us play with numbers and discover their hidden logic!", "theory": ["Mathematics often operates like detective work. In many situations, we do not have complete information upfront, but numbers give us **constraints and relationships**.", "**The Height Queue Problem**: Suppose students of distinct heights stand in a straight single-file line facing front. Each student counts how many students **taller than them** are standing in front of them in line.", "- The person in the very first position always calls out **0**, because nobody stands ahead of them!", "- The tallest person in the entire queue will **always call out 0**, no matter where they stand in the line, because no one is taller than them!", "- If the shortest person stands at the 5th position, they will call out **4**, because all 4 people ahead are taller than them.", "By analyzing these callout numbers from the tallest person down to the shortest, we can uniquely locate everyone's exact position."], "fact_box": "This height line-up deduction is an example of an 'inversion sequence' in modern computer science, used in sorting algorithms and database indexing!", "checkpoints": [{"id": "c1_1", "question": "In a queue of students facing forward, what number will the tallest student in the entire line ALWAYS call out?", "options": ["1", "0", "Their position number", "The total number of students"], "correct": 1, "explanation": "Since no student in the queue is taller than the tallest student, there are 0 people taller than them ahead, regardless of position."}, {"id": "c1_2", "question": "A student standing at position 4 in line calls out the number 3. What does this reveal about the three students standing ahead of them?", "options": ["All three students ahead are shorter than them", "All three students ahead are taller than them", "Exactly one student ahead is taller", "The student is the shortest in the world"], "correct": 1, "explanation": "If there are 3 students ahead and the callout is 3, every single person standing ahead must be taller than this student."}]}, {"id": 2, "section": "6.1", "tag": "Section 6.1 • Positional Reasoning", "title": "Deductive Reasoning: Reconstructing Hidden Permutations", "key_terms": ["Inversion Number", "Permutation", "Deductive Elimination", "Invariant Rules"], "sim_id": "positional_lineup_invariants_sim", "sim_title": "Interactive Logic Grid: Reconstructing the Queue", "narration": "To solve any positional puzzle, we work backwards from the most constrained clues! The tallest person has only one place with 0 taller people ahead. Once the tallest is placed, we place the next tallest, and so on. Let us master this systematic step-by-step elimination.", "theory": ["**Step-by-Step Queue Reconstruction Algorithm**:", "1. **Rank from Tallest to Shortest**: Label the $n$ people from tallest (Rank 1) to shortest (Rank $n$).", "2. **Place the Tallest (Rank 1)**: Since no one is taller, their callout must be $0$. Place them into their designated slot.", "3. **Place the Next Tallest (Rank 2)**: If their callout is $c$, leave exactly $c$ open spots ahead for taller people, and place them in the next available empty spot.", "4. **Continue Downwards**: Repeat for each subsequent person until all empty slots are filled.", "**Key Mathematical Invariant**: Every distinct permutation of heights produces a unique sequence of callout numbers, and conversely, every valid callout sequence determines exactly **one unique arrangement**!"], "fact_box": "In Indian classical philosophy (*Nyaya Shastra*), deductive reasoning through elimination is called 'Parisesha Pramana'—ruling out impossibilities until the truth remains.", "checkpoints": [{"id": "c2_1", "question": "Four students have heights 1, 2, 3, 4 (4 is tallest). Their callouts are [0, 0, 1, 0]. Who stands at the very front of the line (position 1)?", "options": ["Student 1", "Student 2", "Student 3", "The person with 0 taller ahead at position 1"], "correct": 3, "explanation": "The person standing at position 1 must have 0 people ahead of them, so their callout is 0."}, {"id": "c2_2", "question": "Can the person standing at position 3 in a line ever call out the number 4?", "options": ["Yes, if they are very short", "Yes, in large queues", "No, because there are only 2 people standing ahead of them", "Only if people are standing on chairs"], "correct": 2, "explanation": "A person at position 3 has only 2 people ahead of them; the maximum number of taller people ahead cannot exceed 2."}]}, {"id": 3, "section": "6.2", "tag": "Section 6.2 • Picking Parity: Even & Odd Numbers", "title": "The Geometry of Parity: Perfect Pairs vs. Lonely Dots", "key_terms": ["Parity", "Even Numbers", "Odd Numbers", "Pairing Principle", "Modulo 2"], "sim_id": "parity_pair_matching_sim", "sim_title": "Visual Dot-Pairing & Parity Anatomy Lab", "narration": "What makes an even number even, and an odd number odd? Imagine dividing a bag of marbles between two friends. If every single marble finds a partner, forming two equal rows with no leftovers, the number is even! But if exactly one lonely marble is left without a partner, the number is odd. This fundamental property is called parity.", "theory": ["**Parity** is the mathematical classification of every integer as either **Even** or **Odd**.", "**Visual Geometric Model**:", "- **Even Numbers** can be arranged in a neat $2 \\times k$ rectangular array of paired dots. Every dot has a matching buddy! Examples: $2, 4, 6, 8, 10, \\dots$", "- **Odd Numbers** leave exactly **one solitary dot** with no partner. Examples: $1, 3, 5, 7, 9, \\dots$", "**Formal Algebraic Definitions**:", "- An **Even Number** can be expressed as: $$E = 2k \\quad (\\text{where } k \\text{ is an integer})$$", "- An **Odd Number** can be expressed as: $$O = 2k + 1 \\quad \\text{or} \\quad O = 2k - 1$$", "Parity is an all-or-nothing property: every whole number alternates strictly between even and odd: $0, 1, 2, 3, 4, 5, \\dots$"], "fact_box": "The word 'parity' comes from the Latin word 'par', meaning 'equal' or 'pair'. Zero is completely even because 0 = 2 × 0 leaves 0 remainder!", "checkpoints": [{"id": "c3_1", "question": "When an odd number of dots is arranged into pairs of two, how many unpaired dots are always left over?", "options": ["0 dots", "Exactly 1 dot", "2 dots", "It depends on how large the number is"], "correct": 1, "explanation": "By definition, an odd number divided by 2 always leaves a remainder of exactly 1 unpaired dot."}, {"id": "c3_2", "question": "Which algebraic expression represents ANY odd number for any integer k?", "options": ["2k", "2k + 1", "k + 2", "k²"], "correct": 1, "explanation": "2k is always even, so adding 1 yields 2k + 1, which is always odd."}]}, {"id": 4, "section": "6.2", "tag": "Section 6.2 • Parity Arithmetic Laws", "title": "The Arithmetic Laws of Parity: Addition & Multiplication", "key_terms": ["Parity Addition", "Parity Multiplication", "Algebraic Proof", "Invariant Sums"], "sim_id": "parity_arithmetic_matrix_sim", "sim_title": "Interactive Parity Operation Matrix & Dot-Merger", "narration": "What happens when you add two odd numbers together? Each odd number has one lonely unpaired dot. When you bring the two numbers together, the two lonely dots find each other and form a new pair! That is why Odd plus Odd always equals Even. Let us explore the universal laws of parity arithmetic.", "theory": ["**Addition & Subtraction Parity Rules**:", "1. **Even + Even = Even**: $(2a) + (2b) = 2(a + b)$. Both pairs combine with zero leftover dots.", "2. **Odd + Odd = Even**: $(2a + 1) + (2b + 1) = 2(a + b + 1)$. The two lonely dots unite into a new pair!", "3. **Even + Odd = Odd**: $(2a) + (2b + 1) = 2(a + b) + 1$. Exactly one lonely dot remains unpaired.", "**Multiplication Parity Rules**:", "- $\\text{Even} \\times \\text{Any Integer} = \\text{Even}$ (Since a factor of 2 is present).", "- $\\text{Odd} \\times \\text{Odd} = \\text{Odd}$ (No factor of 2 exists anywhere!).", "**Summary Insight**: The sum of several numbers is odd if and only if there is an **ODD number of odd numbers** being added!"], "fact_box": "Computer networks use 'parity bits' to detect data corruption during internet transmission: if a single bit flips, the parity check fails immediately!", "checkpoints": [{"id": "c4_1", "question": "What is the parity of the sum of three odd numbers (e.g. 3 + 5 + 7 = 15)?", "options": ["Always Even", "Always Odd", "Sometimes Even, sometimes Odd", "Always Prime"], "correct": 1, "explanation": "Odd + Odd = Even, and Even + Odd = Odd. An odd count of odd numbers always produces an odd sum."}, {"id": "c4_2", "question": "If you multiply any integer by 6, the resulting product is guaranteed to be:", "options": ["Always Odd", "Always Even", "Prime", "Negative"], "correct": 1, "explanation": "Since 6 is an even number (6 = 2 × 3), any multiple of 6 contains the factor 2 and is therefore always even."}]}, {"id": 5, "section": "6.2", "tag": "Section 6.2 • Parity in Grids", "title": "Grid Parity: Checkerboard Coloring & The Domino Dilemma", "key_terms": ["Grid Parity", "Checkerboard Coloring", "Domino Tiling", "Bipartite Balance"], "sim_id": "grid_squares_parity_sim", "sim_title": "Checkerboard Grid Parity & Domino Tiling Lab", "narration": "Can you tile an 8-by-8 chessboard using 32 two-square dominoes? Yes, 32 times 2 is 64 squares! But what if someone chops off two opposite corner squares? Now 62 squares remain. Can 31 dominoes cover it? Parity reveals a stunning answer: it is mathematically IMPOSSIBLE! Explore the checkerboard parity proof.", "theory": ["**Total Squares in a Grid**: An $m \\times n$ grid contains $m \\times n$ unit squares. If both $m$ and $n$ are odd, the total number of squares is odd; otherwise, it is even.", "**The Checkerboard Color Invariant**:", "- Alternating black and white colors on a grid gives every square a 'color parity'.", "- Every $2 \\times 1$ domino placed on the board covers **exactly 1 black square and 1 white square**.", "**The Famous Mutilated Chessboard Problem**:", "1. An intact $8 \\times 8$ board has 32 white and 32 black squares.", "2. Opposite corners of a chessboard always share the **SAME color** (e.g., both are white).", "3. If two opposite white corners are cut off, the board has **30 white squares and 32 black squares**.", "4. 31 dominoes would require 31 white and 31 black squares. But we have only 30 white squares!", "**Conclusion**: By color parity imbalance, tiling is strictly **impossible**!"], "fact_box": "This checkerboard proof was popularized by mathematician Solomon Golomb in 1954 and is considered one of the most elegant proofs in all of mathematics.", "checkpoints": [{"id": "c5_1", "question": "How many total unit squares are in a grid with 5 rows and 7 columns?", "options": ["12 squares", "24 squares", "35 squares (Odd parity)", "36 squares (Even parity)"], "correct": 2, "explanation": "Total squares = 5 × 7 = 35 squares. Since Odd × Odd = Odd, the total count has odd parity."}, {"id": "c5_2", "question": "Why can 31 dominoes never cover an 8×8 chessboard with two opposite corners removed?", "options": ["Dominoes are too heavy", "The board has 30 white and 32 black squares, but each domino needs 1 white and 1 black", "The board is not square", "Dominoes cannot bend"], "correct": 1, "explanation": "Each domino must cover 1 white and 1 black square. Since removing opposite corners leaves unequal counts (30 white vs 32 black), complete tiling is impossible."}]}, {"id": 6, "section": "6.2", "tag": "Section 6.2 • Algebraic Sequences", "title": "Sequences and Parity: The General $n^{th}$ Term", "key_terms": ["Sequence Parity", "General Term", "Algebraic Form", "Collatz Rules"], "sim_id": "algebraic_parity_nth_term_sim", "sim_title": "Sequence Parity Engine & Collatz Explorer", "narration": "When a pattern repeats, algebra gives us the telescope to see into the future! Consider sequences like 2n (all even numbers), 2n - 1 (all odd numbers), or alternating parity sequences. Let us explore how simple algebraic rules control whether the millionth term will be even or odd.", "theory": ["**Even Number Sequence**: $2, 4, 6, 8, 10, \\dots$ with general term $T_n = 2n$. Every single term is divisible by 2.", "**Odd Number Sequence**: $1, 3, 5, 7, 9, \\dots$ with general term $T_n = 2n - 1$. For $n = 100$, $T_{100} = 2(100) - 1 = 199$.", "**Analyzing the Parity of $3n + 1$**:", "- If $n$ is Even ($n = 2k$): $3(2k) + 1 = 6k + 1$ ➔ **ODD**.", "- If $n$ is Odd ($n = 2k + 1$): $3(2k + 1) + 1 = 6k + 4 = 2(3k + 2)$ ➔ **EVEN**.", "The parity strictly flips back and forth!", "**The Famous $3n + 1$ (Collatz) Rule**: Take any positive integer. If it is even, divide by 2 ($n/2$). If it is odd, triple it and add 1 ($3n + 1$). Amazingly, every number tested eventually cascades down to the repeating loop $4 \\to 2 \\to 1$!"], "fact_box": "Lothar Collatz proposed this problem in 1937. Legendary mathematician Paul Erdős said: 'Mathematics is not yet ready for such problems!'", "checkpoints": [{"id": "c6_1", "question": "What is the 50th odd number in the sequence 1, 3, 5, 7, ...?", "options": ["99", "100", "101", "49"], "correct": 0, "explanation": "The n-th odd number is given by Tn = 2n - 1. For n = 50: 2(50) - 1 = 100 - 1 = 99."}, {"id": "c6_2", "question": "If n is an odd number, what is the parity of the expression 5n + 3?", "options": ["Always Odd", "Always Even", "Depends on n", "Zero"], "correct": 1, "explanation": "Odd × Odd = Odd (5n is odd). Odd + Odd = Even (odd + 3 is even). Therefore, 5n + 3 is always even."}]}, {"id": 7, "section": "6.3", "tag": "Section 6.3 • Explorations in Grids", "title": "Magic Squares: Harmonious Grids with Matching Sums", "key_terms": ["Magic Square", "Magic Constant", "Row Sum", "Column Sum", "Diagonal Sum"], "sim_id": "magic_square_3x3_sim", "sim_title": "Interactive 3 × 3 Magic Square Playground", "narration": "Welcome to the enchanted world of magic squares! A magic square is a grid of numbers where the sum of every row, every column, and both main diagonals equals the EXACT same magical target number, called the magic constant. For a 3-by-3 square using digits 1 to 9, the magic sum is always 15!", "theory": ["**Definition of a Magic Square**: An $n \\times n$ square grid filled with distinct integers such that the sum of each row, each column, and both diagonals is constant.", "**How to Calculate the Magic Constant for a $3 \\times 3$ Square**:", "1. The numbers to place are $1, 2, 3, 4, 5, 6, 7, 8, 9$.", "2. Total sum of all numbers: $$1 + 2 + 3 + \\dots + 9 = \\frac{9 \\times 10}{2} = 45$$", "3. The grid has 3 rows, and each row must have the same sum $S$.", "4. Therefore: $$3 \\times S = 45 \\implies S = \\frac{45}{3} = 15$$", "Every row, column, and diagonal MUST sum to exactly **15**!"], "fact_box": "In China, the 3×3 magic square was known as the 'Lo Shu' turtle square (c. 650 BCE). In India, it was inscribed on amulets for balance and cosmic harmony.", "checkpoints": [{"id": "c7_1", "question": "What is the magic constant (sum of each row, column, and diagonal) for a standard 3×3 magic square using digits 1 to 9?", "options": ["12", "15", "18", "45"], "correct": 1, "explanation": "Total sum = 45. Divided equally across 3 rows gives 45 / 3 = 15."}, {"id": "c7_2", "question": "Can the number 9 be placed in the center cell of a standard 3×3 magic square using digits 1 to 9?", "options": ["Yes, anywhere", "No, because the center must be 5", "Yes, if 1 is in the corner", "Only in diagonal squares"], "correct": 1, "explanation": "The center cell must participate in 4 lines (row, column, 2 diagonals) summing to 15. Only the number 5 has enough distinct pairs to satisfy this."}]}, {"id": 8, "section": "6.3", "tag": "Section 6.3 • Magic Square Structure", "title": "The Golden Center Rule & 8 Symmetries of the $3 \\times 3$ Square", "key_terms": ["Center Cell Rule", "Symmetry Group", "Rotations & Reflections", "Complementary Pairs"], "sim_id": "magic_square_center_rule_sim", "sim_title": "Center Cell Proof & 8 Rotational Symmetries Lab", "narration": "Why MUST the number 5 sit right in the center of the 3-by-3 magic square? Because the center cell is the hub: it lies on 1 row, 1 column, and 2 diagonals—four lines crossing at one point! Let us prove mathematically why the center cell is always one-third of the magic sum.", "theory": ["**Algebraic Proof of the Center Cell Theorem**:", "- Let the center cell be $C$, and the magic sum be $S = 15$.", "- 4 lines pass through $C$: row 2, column 2, main diagonal 1, and main diagonal 2.", "- Adding these 4 lines gives $4 \\times S = 4 \\times 15 = 60$.", "- In this sum, every cell of the grid is counted once, except the center cell $C$, which is counted 4 times (3 extra times!).", "- Therefore: $\\text{Total Sum} + 3C = 60 \\implies 45 + 3C = 60 \\implies 3C = 15 \\implies C = 5$!", "**The 8 Fundamental Orientations**:", "There is essentially only ONE unique $3 \\times 3$ magic square! All others are just its **4 rotations** ($0°, 90°, 180°, 270°$) and **4 reflections** (mirror images across axes)."], "fact_box": "Notice the complementary pairs surrounding the center 5: 1+9 = 10, 2+8 = 10, 3+7 = 10, 4+6 = 10. Every line through the center consists of 5 plus a pair summing to 10!", "checkpoints": [{"id": "c8_1", "question": "In any 3×3 magic square with magic sum S, what is the value of the center cell C?", "options": ["C = S / 2", "C = S / 3", "C = S / 4", "C = S - 10"], "correct": 1, "explanation": "The center cell of any 3×3 magic square is always exactly one-third of the magic constant: C = S / 3 (e.g. 15 / 3 = 5)."}, {"id": "c8_2", "question": "How many distinct rotations and reflections (symmetries) can be generated from a single 3×3 magic square solution?", "options": ["2", "4", "8", "16"], "correct": 2, "explanation": "A square has 4 rotational symmetries and 4 reflection symmetries, producing 8 visually distinct orientations."}]}, {"id": 9, "section": "6.3", "tag": "Section 6.3 • Ancient Indian Yantras", "title": "The Chautīsa Yantra: Khajuraho's Masterwork of 34", "key_terms": ["Chautīsa Yantra", "Khajuraho Temple", "Magic Constant 34", "Pandiagonal Magic Square"], "sim_id": "chautisa_yantra_4x4_sim", "sim_title": "The Chautīsa Yantra: 16 Ways to Make 34", "narration": "At the 10th-century Parshvanatha Jain temple in Khajuraho, Madhya Pradesh, an ancient stone inscription displays a breathtaking 4-by-4 magic square called the Chautisa Yantra. 'Chautisa' means thirty-four in Hindi. Not only do the rows, columns, and diagonals sum to 34, but so do the 4 corners, the 4 center squares, and every 2-by-2 quadrant! Explore its sublime symmetry.", "theory": ["**The Chautīsa Yantra Grid** (using numbers 1 through 16):", "$$\\begin{bmatrix} 7 & 12 & 1 & 14 \\\\ 2 & 13 & 8 & 11 \\\\ 16 & 3 & 10 & 5 \\\\ 9 & 6 & 15 & 4 \\end{bmatrix}$$", "**Why is the Magic Sum 34?**", "- Sum of numbers 1 to 16: $\\frac{16 \\times 17}{2} = 136$.", "- Divided across 4 rows: $S = \\frac{136}{4} = 34$!", "**The Supernatural Symmetries of the Chautīsa Yantra**:", "- All 4 Rows and all 4 Columns sum to 34.", "- Both main diagonals sum to 34: $7+13+10+4 = 34$ and $14+8+3+9 = 34$.", "- The 4 corner cells sum to 34: $7 + 14 + 9 + 4 = 34$.", "- The 4 center cells sum to 34: $13 + 8 + 3 + 10 = 34$.", "- Every $2 \\times 2$ corner quadrant sums to 34 (e.g. $7+12+2+13 = 34$)!", "- This is a **most-perfect pandiagonal magic square**."], "fact_box": "Narayana Pandita wrote a whole chapter on magic squares called 'Bhadra Ganita' in his 1356 CE treatise 'Ganita Kaumudi', detailing algorithms for squares of any size!", "checkpoints": [{"id": "c9_1", "question": "What is the magic sum of the Chautīsa Yantra found in the Khajuraho temple inscription?", "options": ["15", "30", "34", "136"], "correct": 2, "explanation": "'Chautīsa' means 34. Every row, column, diagonal, and quadrant in this ancient grid sums to 34."}, {"id": "c9_2", "question": "In the Chautīsa Yantra, what is the sum of the four corner cells (7, 14, 9, 4)?", "options": ["28", "34", "40", "68"], "correct": 1, "explanation": "7 + 14 + 9 + 4 = 34. The four corner cells also sum to the magic constant 34."}]}, {"id": 10, "section": "6.4", "tag": "Section 6.4 • Virahāńka-Fibonacci Numbers", "title": "Poetic Beats to Universal Law: The Virahāńka Sequence", "key_terms": ["Virahāńka Numbers", "Fibonacci Sequence", "Pingala", "Laghu & Guru Syllables", "Prosody (Matra)"], "sim_id": "virahanka_poetic_meter_sim", "sim_title": "Poetic Beats & Syllable Combinations Generator", "narration": "Centuries before Leonardo of Pisa (Fibonacci) wrote his book in 1202 CE, ancient Indian scholar Virahāńka (around 600–700 CE), building on Acharya Pingala's Chandas Shastra, discovered a miraculous number pattern while studying poetic rhythms! How many ways can you arrange short 1-beat syllables (Laghu) and long 2-beat syllables (Guru) to fill a line of poetry? The answers form nature's favourite sequence!", "theory": ["**Sanskrit Poetic Meters (*Matra-Vritta*)**:", "- **Laghu (L)**: Short syllable lasting **1 beat** (time unit).", "- **Guru (G)**: Long syllable lasting **2 beats** (time units).", "**Counting Rhythms of $n$ Beats**:", "- $n = 1$ beat: [L] ➔ **1 way**", "- $n = 2$ beats: [LL, G] ➔ **2 ways**", "- $n = 3$ beats: [LLL, LG, GL] ➔ **3 ways**", "- $n = 4$ beats: [LLLL, LLG, LGL, GLL, GG] ➔ **5 ways**", "- $n = 5$ beats: [8 combinations] ➔ **8 ways**", "- $n = 6$ beats: [13 combinations] ➔ **13 ways**", "Notice the sequence: $$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, \\dots$$", "Each new term is formed by adding the previous two terms! Virahāńka stated this exact recurrence rule in the 7th century CE."], "fact_box": "Historians of mathematics now officially acknowledge this sequence as the 'Virahāńka-Hemachandra-Fibonacci sequence' to honor its true Indian origins.", "checkpoints": [{"id": "c10_1", "question": "Which ancient Indian scholar analyzed poetic syllables (Laghu and Guru beats) around 600–700 CE to discover this sequence?", "options": ["Aryabhata", "Virahāńka", "Brahmagupta", "Bhaskara I"], "correct": 1, "explanation": "Acharya Virahāńka discovered this sequence while studying combinations of poetic rhythms in his work on Prakrit prosody."}, {"id": "c10_2", "question": "In Sanskrit prosody, how many beats does a long syllable (Guru) count for compared to a short syllable (Laghu)?", "options": ["Laghu = 1 beat, Guru = 2 beats", "Laghu = 2 beats, Guru = 1 beat", "Both count as 1 beat", "Guru = 3 beats"], "correct": 0, "explanation": "A short syllable (Laghu) takes 1 beat; a long syllable (Guru) takes 2 beats."}]}, {"id": 11, "section": "6.4", "tag": "Section 6.4 • Sequence Formulas", "title": "The Additive Engine: Recurrence Relation & The Golden Ratio", "key_terms": ["Recurrence Relation", "F_n = F_{n-1} + F_{n-2}", "Golden Ratio (Phi)", "Limiting Ratio 1.618"], "sim_id": "fibonacci_virahanka_sequence_sim", "sim_title": "Interactive Recurrence Stepper & Golden Ratio Convergence", "narration": "How do you calculate the next number in the Virahāńka sequence? Look at the two numbers before it and add them together! 1 plus 2 is 3, 2 plus 3 is 5, 3 plus 5 is 8, 5 plus 8 is 13. Furthermore, as you divide each term by the one before it, the ratio converges to a cosmic constant: the Golden Ratio, 1.618!", "theory": ["**The Recurrence Relation Formula**:", "$$F_n = F_{n-1} + F_{n-2} \\quad \\text{for } n \\ge 3$$", "With initial seed values: $F_1 = 1, F_2 = 2$ (or starting with $0, 1$).", "**First 12 Terms**:", "$$\\begin{array}{c|c|c|c|c|c|c|c|c|c|c|c} F_1 & F_2 & F_3 & F_4 & F_5 & F_6 & F_7 & F_8 & F_9 & F_{10} & F_{11} & F_{12} \\\\ \\hline 1 & 2 & 3 & 5 & 8 & 13 & 21 & 34 & 55 & 89 & 144 & 233 \\end{array}$$", "**The Golden Ratio ($\\Phi \\approx 1.618033...$)**:", "When you take ratios of consecutive terms:", "- $8 / 5 = 1.600$", "- $13 / 8 = 1.625$", "- $55 / 34 \\approx 1.6176$", "- $233 / 144 \\approx 1.61805$", "The ratios oscillate and lock into the Golden Ratio $\\Phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618$!"], "fact_box": "The Golden Spiral constructed from squares with side lengths 1, 1, 2, 3, 5, 8, 13 matches the exact chamber curvature of the Nautilus sea shell!", "checkpoints": [{"id": "c11_1", "question": "If two consecutive terms in the Virahāńka sequence are 21 and 34, what is the next term?", "options": ["45", "55", "68", "89"], "correct": 1, "explanation": "By the recurrence rule, add the previous two terms: 21 + 34 = 55."}, {"id": "c11_2", "question": "What mathematical constant do the ratios of consecutive Virahāńka numbers approach as the terms grow large?", "options": ["Pi (3.1415...)", "The Golden Ratio (≈ 1.618)", "Euler's number e (2.718...)", "Exactly 2.0"], "correct": 1, "explanation": "The ratio Fn / Fn-1 approaches the Golden Ratio Phi = (1 + √5)/2 ≈ 1.618033..."}]}, {"id": 12, "section": "6.4", "tag": "Section 6.4 • Fibonacci in Nature", "title": "Virahāńka Numbers in Nature: Flower Petals & Pinecone Spirals", "key_terms": ["Phyllotaxis", "Petal Counts", "Sunflower Seed Spirals", "Pinecone Scales"], "sim_id": "nature_petals_spirals_sim", "sim_title": "Botanical Gallery: Petal Counts & Sunflower Spiral Counter", "narration": "Look closely at the flowers growing in a garden. Why do lilies always have 3 petals, buttercups 5 petals, delphiniums 8 petals, marigolds 13 petals, and black-eyed Susans 21 petals? These are all Virahāńka numbers! Nature uses this mathematical blueprint to pack seeds and petals with maximum efficiency so every leaf receives optimal sunlight.", "theory": ["**Botanical Petal Counts in Nature**:", "- **3 Petals**: Lily, Iris, Trillium ($F_3$)", "- **5 Petals**: Buttercup, Wild Rose, Jasmine, Hibiscus ($F_4$)", "- **8 Petals**: Delphinium, Clematis ($F_5$)", "- **13 Petals**: Marigold, Ragwort, Cineraria ($F_6$)", "- **21 Petals**: Aster, Black-eyed Susan, Chicory ($F_7$)", "- **34 Petals**: Plantain, Field Daisy ($F_8$)", "**Sunflower Seed Spirals**:", "- Sunflower seed heads display interlocking clockwise and counter-clockwise spirals.", "- In a typical sunflower, you will count **21 spirals going one way and 34 going the other**, or **34 and 55**, or in giant sunflowers **55 and 89**!", "- These consecutive Virahāńka numbers allow optimal seed packing (*phyllotaxis*) without wasting any space."], "fact_box": "Pineapples have hexagonal scales arranged in 3 distinct sets of spirals: 5, 8, and 13 spirals wrapping around the fruit!", "checkpoints": [{"id": "c12_1", "question": "Which of the following petal counts is almost NEVER found in natural wild flower species?", "options": ["3 petals", "4 petals", "5 petals", "8 petals"], "correct": 1, "explanation": "4 is not a Virahāńka-Fibonacci number; natural flowers predominantly exhibit petal counts of 3, 5, 8, 13, or 21."}, {"id": "c12_2", "question": "Why do plants naturally arrange their leaves and seeds in Virahāńka spiral patterns?", "options": ["To look pretty for bees", "To maximize sunlight exposure and pack seeds with zero wasted space", "Because stems are round", "Random accidental chance"], "correct": 1, "explanation": "Phyllotaxis based on the Golden Ratio ensures that leaves do not overlap and shade each other, while seeds achieve maximum packing density."}]}, {"id": 13, "section": "6.4", "tag": "Section 6.4 • Parity Patterns in Sequences", "title": "The Parity Rhythm: Why Every $3^{rd}$ Virahāńka Number is Even", "key_terms": ["Parity Rhythm", "Odd-Even Cycle", "Modulo Arithmetic", "Modular Periodicities"], "sim_id": "virahanka_parity_cycle_sim", "sim_title": "Interactive Virahāńka Parity Cycle & Modulo Stepper", "narration": "Let us combine our two big ideas: Parity and the Virahāńka sequence! Write down the parity of each number in the sequence: 1 is Odd, 2 is Even, 3 is Odd, 5 is Odd, 8 is Even, 13 is Odd, 21 is Odd, 34 is Even. Look at the rhythm: Odd, Even, Odd, Odd, Even, Odd, Odd, Even! It repeats with a period of 3 forever!", "theory": ["**Inspecting the Parities of the Virahāńka Sequence**:", "$$\\begin{array}{c|c|c|c|c|c|c|c|c|c|c|c} n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\\\ \\hline F_n & 1 & 2 & 3 & 5 & 8 & 13 & 21 & 34 & 55 & 89 & 144 & 233 \\\\ \\hline \\text{Parity} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} & \\text{O} & \\mathbf{E} & \\text{O} \\end{array}$$", "**Deductive Proof of the Period-3 Parity Cycle**:", "1. Start with **Odd, Even**.", "2. $\\text{Odd} + \\text{Even} = \\mathbf{Odd}$ (Term 3).", "3. $\\text{Even} + \\text{Odd} = \\mathbf{Odd}$ (Term 4).", "4. $\\text{Odd} + \\text{Odd} = \\mathbf{Even}$ (Term 5!).", "5. $\\text{Odd} + \\text{Even} = \\mathbf{Odd}$ (Term 6).", "The cycle **[Odd, Odd, Even]** repeats eternally. Therefore, $F_n$ is even if and only if $n$ is a multiple of 3!"], "fact_box": "This repeating modular pattern is called the 'Pisano Period'. For modulo 2, the period is 3. For modulo 10 (last digit), the period is 60!", "checkpoints": [{"id": "c13_1", "question": "What is the repeating parity pattern of the Virahāńka sequence?", "options": ["Even, Odd, Even, Odd...", "Odd, Odd, Even, Odd, Odd, Even...", "All numbers are Odd", "Odd, Even, Even, Odd..."], "correct": 1, "explanation": "Because Odd + Odd = Even, two odds always produce an even, creating the 3-step repeating cycle: [Odd, Odd, Even]."}, {"id": "c13_2", "question": "Is the 30th Virahāńka number (F_30) Even or Odd?", "options": ["Odd", "Even, because 30 is a multiple of 3", "Prime", "Cannot be determined without calculating"], "correct": 1, "explanation": "Every 3rd term is even. Since 30 = 3 × 10, F_30 is guaranteed to be an even number!"}]}, {"id": 14, "section": "6.5", "tag": "Section 6.5 • Digits in Disguise", "title": "Digits in Disguise: Unmasking Letters in Alphametic Puzzles", "key_terms": ["Cryptarithm", "Alphametic", "Unique Digit Rule", "Leading Zero Prohibition", "Carryover Clues"], "sim_id": "cryptarithm_single_digit_sim", "sim_title": "Interactive Cryptarithm Detective: AB + B = BC", "narration": "Imagine arithmetic where sneaky detectives have disguised every digit with an alphabetical letter! These puzzles are called cryptarithms or alphametics. Each letter stands for a unique single digit from 0 to 9, and the leading digit of a number can never be zero. Put on your detective hat and solve the puzzle AB + B = BC!", "theory": ["**The Ground Rules of Cryptarithms**:", "1. Each distinct letter represents a **unique digit** from $0$ to $9$ (if $A = 4$, no other letter can be $4$).", "2. The first (leading) digit of a number **cannot be zero** (no numbers like '05').", "**Case Study: Solve $AB + B = BC$**", "- In column addition: $B + B$ ends in $C$.", "- In the tens column: $A + \\text{carry} = B$.", "- If there were no carry, $A = B$, which violates the unique digit rule! Thus, there MUST be a carry of $1$.", "- So $B = A + 1$, and $B + B \\ge 10$.", "- Try $B = 9$: Then $A = 8$. $AB = 89$. $89 + 9 = 98$. Then $B = 9, C = 8$. But $A = 8$ and $C = 8$, violating uniqueness!", "- Try $B = 8$: $A = 7$. $78 + 8 = 86$. Then $A=7, B=8, C=6$ (All distinct!). Solution found: $78 + 8 = 86$!"], "fact_box": "The word 'Alphametic' was coined in 1955 by J. A. H. Hunter. Cryptarithms were first popularized in 1931 by the Belgian recreational math journal Sphinx.", "checkpoints": [{"id": "c14_1", "question": "In a cryptarithm, can a multi-digit number like 'SEND' have S = 0?", "options": ["Yes, zero is a valid digit", "No, the leading digit of a number can never be zero", "Only if it is a decimal", "Yes, if E = 1"], "correct": 1, "explanation": "Standard cryptarithm rules strictly prohibit leading zeros; the first letter of any number must be between 1 and 9."}, {"id": "c14_2", "question": "In the addition puzzle A + A = BA, what must be the value of the carryover letter B?", "options": ["B = 0", "B = 1", "B = 2", "B = 9"], "correct": 1, "explanation": "The maximum sum of two single digits is 9 + 9 = 18. The carry into a new column in addition of two numbers can NEVER exceed 1. Thus, B = 1."}]}, {"id": 15, "section": "6.5", "tag": "Section 6.5 • Classic Cryptarithm Deduction", "title": "The Master Alphametic: Solving SEND + MORE = MONEY", "key_terms": ["SEND + MORE = MONEY", "Column Deduction", "Carryover Constraints", "Exhaustive Elimination"], "sim_id": "classic_alphametic_deduction_sim", "sim_title": "SEND + MORE = MONEY Step-by-Step Solver", "narration": "In 1924, legendary puzzler Henry Dudeney published the most famous cryptarithm of all time: SEND + MORE = MONEY. Watch how pure logic unlocks every single digit without any guesswork. The carry into the ten-thousands column immediately forces M to be 1! Step by step, the entire word reveals its secret digits.", "theory": ["$$\\begin{array}{r@{\\quad}c@{}c@{}c@{}c} & S & E & N & D \\\\ + & M & O & R & E \\\\ \\hline M & O & N & E & Y \\end{array}$$", "**Step 1: The Ten-Thousands Column (M)**", "- $S + M + \\text{carry} = MO$. Adding two 4-digit numbers produces at most a 1 in the fifth column. Since $M \\neq 0$, **$M = 1$**!", "**Step 2: The Thousands Column (O)**", "- $S + 1 + \\text{carry} = 10 + O$. Since $S \\le 9$, $S + 1 \\le 10$. Thus $O$ must be **$0$**, and $S$ must be **$9$** (or $8$ with carry).", "**Step 3: Systematic Chain Deduction**", "- Deducing through columns yields: **$S = 9, E = 5, N = 6, D = 7, M = 1, O = 0, R = 8, Y = 2$**.", "$$\\mathbf{9567 + 1085 = 10652}$$", "Every letter has a unique digit, and the arithmetic checks out with total mathematical perfection!"], "fact_box": "Dudeney sent this puzzle in a telegram to his editor with only the words: 'SEND MORE MONEY'—turning a plea for cash into the world's greatest mathematical puzzle!", "checkpoints": [{"id": "c15_1", "question": "In the puzzle SEND + MORE = MONEY, why must the letter M equal 1?", "options": ["Because M is the first letter in Money", "Because the sum of two 4-digit numbers can produce a carry of at most 1", "Because M represents 10", "Because 9 + 9 = 19"], "correct": 1, "explanation": "Even 9999 + 9999 = 19998. The carry into the 5th column from two 4-digit numbers can never be anything other than 1. Thus, M = 1."}, {"id": "c15_2", "question": "What is the unique digit value of the letter S in SEND + MORE = MONEY?", "options": ["S = 7", "S = 8", "S = 9", "S = 5"], "correct": 2, "explanation": "To produce a carry of 1 with M = 1 and O = 0, S must be 9 (9 + 1 + 0 = 10)."}]}, {"id": 16, "section": "Review", "tag": "Chapter Review • Heritage of Indian Number Play", "title": "Centuries of Play: Pingala, Virahāńka & Narayana Pandita", "key_terms": ["Chandas Shastra", "Meru Prastara (Pascal's Triangle)", "Ganita Kaumudi", "Bhadra Ganita"], "sim_id": "heritage_number_play_sim", "sim_title": "Meru Prastara & Ancient Indian Combinatorics Lab", "narration": "From the rhythmic syllables of Pingala's Chandas Shastra (3rd century BCE) to the algebraic meter of Virahāńka and the elaborate magic squares in Narayana Pandita's Ganita Kaumudi, Indian mathematics has always treated numbers as a source of joyous creative play! Let us celebrate this heritage and carry forward the spirit of joyful mathematical exploration.", "theory": ["**Key Heritage Milestones in Indian Number Play**:", "1. **Acharya Pingala (c. 300 BCE)**: In *Chandas Shastra*, invented binary numerals, combinations (*Prastara*), and the famous triangle of binomial coefficients known as **Meru Prastara** (over 1,800 years before Blaise Pascal!).", "2. **Acharya Virahāńka (c. 600–700 CE)**: First formulated the additive sequence ($1, 2, 3, 5, 8, 13, 21...$) in his work on poetic rhythms, predating Fibonacci by more than five centuries.", "3. **Narayana Pandita (1356 CE)**: Devoted the 14th chapter of his masterwork *Ganita Kaumudi* ('Bhadra Ganita') entirely to constructing magic squares of odd, evenly-even, and oddly-even orders.", "Mathematical play is not separate from serious mathematics—it is the very engine that sparks mathematical discovery!"], "fact_box": "Pingala called the binomial coefficient pyramid 'Meru Prastara', meaning 'The Staircase of Mount Meru'. Halayudha's 10th-century commentary gave the exact triangular addition rule!", "checkpoints": [{"id": "c16_1", "question": "What ancient Indian name was given to the triangle of binomial coefficients centuries before Pascal?", "options": ["Sulba Sutra", "Meru Prastara", "Bijaganita", "Lilavati"], "correct": 1, "explanation": "Acharya Pingala and his commentator Halayudha called this triangular number pattern 'Meru Prastara' (The Steps of Mount Meru)."}, {"id": "c16_2", "question": "Which 14th-century Indian mathematician wrote the comprehensive treatise 'Bhadra Ganita' on magic squares?", "options": ["Narayana Pandita", "Aryabhata", "Varahamihira", "Brahmagupta"], "correct": 0, "explanation": "Narayana Pandita detailed systematic algorithms for constructing magic squares of all orders in his 1356 CE text Ganita Kaumudi."}]}, {"id": 17, "section": "Quiz 1", "is_quiz": true, "quiz_range": [1, 10], "tag": "Mastery Challenge • Part 1", "title": "Mastery Quiz 1: Positional Logic, Height Rules & Queue Deduction", "narration": "Welcome to Part 1 of the Chapter Mastery Challenge! Test your skills on positional deduction, height line-ups, and logical inversion rules. Choose your answers and study the step-by-step solutions.", "questions": [{"id": 1, "question": "In a queue of 5 children of distinct heights, what is the maximum number of people taller than them that the child at position 1 can have in front?", "options": ["0", "1", "4", "5"], "correct": 0, "solution": "Step 1: The child at position 1 is at the very front of the queue.\nStep 2: There is no one standing ahead of position 1.\nConclusion: The number of taller people ahead must be exactly 0."}, {"id": 2, "question": "In a line of 6 people with distinct heights, the shortest person stands at position 4. How many people standing ahead of them are taller than them?", "options": ["0", "1", "2", "3"], "correct": 3, "solution": "Step 1: The person stands at position 4, so there are exactly 3 people standing ahead of them (positions 1, 2, and 3).\nStep 2: Since this person is the shortest in the entire group, every single person ahead is taller than them.\nConclusion: Exactly 3 people ahead are taller."}, {"id": 3, "question": "Five students A, B, C, D, E have heights 150cm, 155cm, 160cm, 165cm, 170cm. If the 170cm student stands at position 3, what callout number will they announce?", "options": ["0", "1", "2", "3"], "correct": 0, "solution": "Step 1: The student's height is 170cm, which is the tallest height in the group.\nStep 2: No student in the queue is taller than 170cm.\nConclusion: Regardless of standing at position 3, they see 0 taller people ahead. Callout is 0."}, {"id": 4, "question": "Three students stand in line. Their callouts are [0, 1, 0]. If heights are 1, 2, 3 (3 tallest), what is the height order from front to back?", "options": ["3, 1, 2", "2, 1, 3", "1, 2, 3", "3, 2, 1"], "correct": 1, "solution": "Step 1: Position 3 calls out 0, meaning no one ahead is taller than position 3. Thus, the tallest person (height 3) is at position 3!\nStep 2: Position 2 calls out 1, meaning the person ahead (at position 1) is taller than position 2. Between remaining heights 1 and 2, height 2 must be ahead of height 1.\nStep 3: Therefore, position 1 has height 2, position 2 has height 1, and position 3 has height 3.\nConclusion: The queue is [2, 1, 3] (Callouts: Pos 1 sees 0, Pos 2 sees one taller [2], Pos 3 sees zero taller). Perfect match!"}, {"id": 5, "question": "What is the sum of any two odd numbers (for example, 17 + 29)?", "options": ["Always Odd", "Always Even", "Sometimes Odd, sometimes Even", "Always a Multiple of 4"], "correct": 1, "solution": "Step 1: Let the two odd numbers be 2a + 1 and 2b + 1.\nStep 2: Sum = (2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1).\nStep 3: Since 2 is a factor of the sum, it is divisible by 2.\nConclusion: The sum of two odd numbers is always Even (17 + 29 = 46, even!)."}, {"id": 6, "question": "If you add 5 odd numbers together, what will be the parity of the final sum?", "options": ["Always Even", "Always Odd", "Cannot be determined", "Zero"], "correct": 1, "solution": "Step 1: Pair up the odd numbers: (Odd + Odd) + (Odd + Odd) + Odd.\nStep 2: (Even) + (Even) + Odd = Even + Odd = Odd.\nConclusion: An odd count of odd numbers always yields an Odd sum."}, {"id": 7, "question": "Which of the following products is guaranteed to be an ODD number?", "options": ["Even × Even", "Even × Odd", "Odd × Odd", "Odd × Even × Odd"], "correct": 2, "solution": "Step 1: A number is even if it contains at least one factor of 2.\nStep 2: Only Odd × Odd has no factor of 2 in any of its terms.\nConclusion: Odd × Odd is always Odd (e.g. 7 × 9 = 63)."}, {"id": 8, "question": "If x is an even number and y is an odd number, what is the parity of 3x + 4y?", "options": ["Always Even", "Always Odd", "Depends on x", "Depends on y"], "correct": 0, "solution": "Step 1: Since x is even, 3x = 3(even) = Even.\nStep 2: Since 4 is even, 4y = 4(odd) = Even.\nStep 3: Sum = Even + Even = Even.\nConclusion: 3x + 4y is always Even."}, {"id": 9, "question": "What is the 100th even positive integer?", "options": ["100", "198", "200", "202"], "correct": 2, "solution": "Step 1: The sequence of positive even integers is 2, 4, 6, 8, ...\nStep 2: The n-th term formula is Tn = 2n.\nStep 3: For n = 100, T100 = 2 × 100 = 200.\nConclusion: The 100th even integer is 200."}, {"id": 10, "question": "What is the 75th odd positive integer?", "options": ["149", "150", "151", "75"], "correct": 0, "solution": "Step 1: The sequence of odd positive integers is 1, 3, 5, 7, ...\nStep 2: The n-th term formula is Tn = 2n - 1.\nStep 3: For n = 75, T75 = 2(75) - 1 = 150 - 1 = 149.\nConclusion: The 75th odd integer is 149."}]}, {"id": 18, "section": "Quiz 2", "is_quiz": true, "quiz_range": [11, 20], "tag": "Mastery Challenge • Part 2", "title": "Mastery Quiz 2: Parity Properties, Arithmetic Laws & Grid Squares", "narration": "Mastery Quiz Part 2! Here we test parity arithmetic, pairing proofs, algebraic forms 2k and 2k+1, and checkerboard grid invariants. Focus on why even and odd numbers behave the way they do.", "questions": [{"id": 11, "question": "A rectangle grid has dimensions 6 units by 9 units. What is the parity of the total number of unit squares?", "options": ["Even", "Odd", "Fractional", "Zero"], "correct": 0, "solution": "Step 1: Total squares = 6 × 9 = 54.\nStep 2: 54 is divisible by 2 (54 = 2 × 27).\nConclusion: The total number of squares is Even (Even × Odd = Even)."}, {"id": 12, "question": "Can a grid with 35 unit squares ever be completely tiled using 2×1 dominoes?", "options": ["Yes, easily", "No, because each domino covers 2 squares, so total squares must be even", "Yes, if dominoes are cut", "Only if the grid is square"], "correct": 1, "solution": "Step 1: Each domino covers exactly 2 squares.\nStep 2: Any number of whole dominoes covers an even number of squares (2k).\nStep 3: 35 is an odd number, so 35 cannot equal 2k.\nConclusion: No, an odd number of squares can never be tiled with dominoes."}, {"id": 13, "question": "In the Collatz 3n + 1 sequence starting at number 5, what are the next three numbers generated?", "options": ["16, 8, 4", "15, 8, 4", "16, 5, 2", "10, 5, 16"], "correct": 0, "solution": "Step 1: 5 is odd, so calculate 3n + 1 = 3(5) + 1 = 16.\nStep 2: 16 is even, so divide by 2: 16 / 2 = 8.\nStep 3: 8 is even, so divide by 2: 8 / 2 = 4.\nConclusion: The next three numbers are 16, 8, 4 (followed by 2, 1!)."}, {"id": 14, "question": "What is the magic sum of a standard 3×3 magic square containing the digits 1, 2, 3, 4, 5, 6, 7, 8, 9?", "options": ["12", "15", "18", "45"], "correct": 1, "solution": "Step 1: Sum of numbers from 1 to 9 is (9 × 10) / 2 = 45.\nStep 2: There are 3 rows, each with equal sum S.\nStep 3: 3S = 45 ➔ S = 15.\nConclusion: The magic sum is 15."}, {"id": 15, "question": "In any standard 3×3 magic square using numbers 1 through 9, which number MUST occupy the central cell?", "options": ["1", "3", "5", "9"], "correct": 2, "solution": "Step 1: The center cell participates in 4 lines: 1 row, 1 column, and 2 diagonals.\nStep 2: Center value C = Magic Sum / 3 = 15 / 3 = 5.\nConclusion: The center cell must strictly be 5."}, {"id": 16, "question": "If the numbers in a 3×3 magic square are 2, 4, 6, 8, 10, 12, 14, 16, 18, what is the magic constant?", "options": ["15", "30", "45", "90"], "correct": 1, "solution": "Step 1: Notice that each number is double the standard digits 1 to 9 (2 × 1, 2 × 2, ..., 2 × 9).\nStep 2: Total sum = 2 × 45 = 90.\nStep 3: Magic constant S = 90 / 3 = 30 (which is 2 × 15).\nConclusion: The magic constant is 30."}, {"id": 17, "question": "In the standard 3×3 magic square with center 5, if one corner is 8, what number must be in the diagonally opposite corner?", "options": ["1", "2", "3", "4"], "correct": 1, "solution": "Step 1: The diagonal passes through corner 1, center (5), and corner 2.\nStep 2: The sum of the diagonal must be 15.\nStep 3: 8 + 5 + corner 2 = 15 ➔ 13 + corner 2 = 15 ➔ corner 2 = 2.\nConclusion: The diagonally opposite corner must be 2."}, {"id": 18, "question": "The Chautīsa Yantra in the Khajuraho temple is a magic square of which grid dimension?", "options": ["3 × 3", "4 × 4", "5 × 5", "8 × 8"], "correct": 1, "solution": "Step 1: The Chautīsa Yantra contains 16 numbers arranged in a 4-by-4 square grid.\nConclusion: It is a 4 × 4 magic square."}, {"id": 19, "question": "What is the magic sum of each row, column, and diagonal in the Chautīsa Yantra?", "options": ["15", "26", "34", "68"], "correct": 2, "solution": "Step 1: The name 'Chautīsa' translates to 34.\nStep 2: Total sum of numbers 1 to 16 is (16 × 17)/2 = 136.\nStep 3: 136 / 4 = 34.\nConclusion: The magic sum is 34."}, {"id": 20, "question": "In the Chautīsa Yantra 4×4 square, which of the following groups also sums to 34?", "options": ["The 4 corner cells", "The 4 central cells", "Each 2×2 corner quadrant", "All of the above!"], "correct": 3, "solution": "Step 1: The Chautīsa Yantra is a most-perfect pandiagonal magic square.\nStep 2: The 4 corners sum to 34 (7+14+9+4=34).\nStep 3: The 4 central cells sum to 34 (13+8+3+10=34).\nStep 4: Every 2×2 quadrant sums to 34.\nConclusion: All of the above!"}]}, {"id": 19, "section": "Quiz 3", "is_quiz": true, "quiz_range": [21, 30], "tag": "Mastery Challenge • Part 3", "title": "Mastery Quiz 3: Magic Squares, Center Cell Rule & The Chautīsa Yantra", "narration": "Welcome to Mastery Quiz Part 3! Tackle magic constants, center cell formulas, 3x3 grids, and the Khajuraho Chautīsa Yantra's stunning 4x4 symmetrical patterns summing to 34.", "questions": [{"id": 21, "question": "Who was the ancient Indian scholar who discovered the sequence 1, 2, 3, 5, 8, 13, 21... through Sanskrit poetic meters around 600–700 CE?", "options": ["Fibonacci", "Virahāńka", "Euclid", "Ramanujan"], "correct": 1, "solution": "Step 1: Acharya Virahāńka analyzed poetic rhythms of short and long syllables in his 7th-century treatise.\nStep 2: This occurred more than 500 years before Fibonacci published Liber Abaci in 1202 CE.\nConclusion: Acharya Virahāńka."}, {"id": 22, "question": "In Virahāńka's poetic analysis, how many distinct rhythmic combinations of Laghu (1 beat) and Guru (2 beats) can fill a 4-beat measure?", "options": ["3", "4", "5", "8"], "correct": 2, "solution": "Step 1: List the combinations of 1 and 2 that sum to 4:\n- 1+1+1+1 (LLLL)\n- 1+1+2 (LLG)\n- 1+2+1 (LGL)\n- 2+1+1 (GLL)\n- 2+2 (GG)\nConclusion: There are exactly 5 combinations (the 4th Virahāńka number!)."}, {"id": 23, "question": "Given the Virahāńka sequence: 1, 2, 3, 5, 8, 13, 21, 34, what is the next number in the sequence?", "options": ["45", "55", "58", "65"], "correct": 1, "solution": "Step 1: Add the two most recent terms.\nStep 2: 21 + 34 = 55.\nConclusion: The next number is 55."}, {"id": 24, "question": "What is the term that immediately follows 55 in the Virahāńka sequence (..., 34, 55, ...)?", "options": ["79", "89", "99", "110"], "correct": 1, "solution": "Step 1: Add 34 and 55.\nStep 2: 34 + 55 = 89.\nConclusion: The next term is 89."}, {"id": 25, "question": "A wild buttercup flower typically has how many petals?", "options": ["4 petals", "5 petals", "7 petals", "9 petals"], "correct": 1, "solution": "Step 1: Buttercups are classic examples of botanical Virahāńka numbers.\nStep 2: Buttercups have exactly 5 petals (F4 = 5).\nConclusion: 5 petals."}, {"id": 26, "question": "Lilies and irises typically possess how many petals?", "options": ["2 petals", "3 petals", "4 petals", "6 petals"], "correct": 1, "solution": "Step 1: Lilies, trilliums, and irises exhibit 3-fold symmetry.\nStep 2: 3 is the 3rd Virahāńka number (F3 = 3).\nConclusion: 3 petals."}, {"id": 27, "question": "In a sunflower seed head, what pair of spiral counts is most commonly observed?", "options": ["10 and 20", "21 and 34", "25 and 50", "30 and 40"], "correct": 1, "solution": "Step 1: Seed spirals in sunflower heads are consecutive Virahāńka numbers.\nStep 2: 21 clockwise and 34 counter-clockwise spirals are typical.\nConclusion: 21 and 34."}, {"id": 28, "question": "In the Virahāńka sequence 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, how frequently do EVEN numbers appear?", "options": ["Every 2nd number", "Every 3rd number", "Every 4th number", "Randomly"], "correct": 1, "solution": "Step 1: Write the parity pattern: 1(O), 2(E), 3(O), 5(O), 8(E), 13(O), 21(O), 34(E), 55(O), 89(O), 144(E)...\nStep 2: Notice the even numbers: Term 2 (2), Term 5 (8), Term 8 (34), Term 11 (144)...\nConclusion: Exactly every 3rd number is even (pattern: Odd, Odd, Even)."}, {"id": 29, "question": "What is the parity of the 99th Virahāńka number (F_99)?", "options": ["Even, because 99 is a multiple of 3", "Odd", "Negative", "Cannot be determined"], "correct": 0, "solution": "Step 1: Every term whose index is a multiple of 3 is even.\nStep 2: 99 = 3 × 33 (a multiple of 3).\nConclusion: F_99 is guaranteed to be an Even number."}, {"id": 30, "question": "In a cryptarithm, if two single-digit numbers are added: X + Y = 1Z, what is the maximum possible value for the sum?", "options": ["15", "18", "19", "20"], "correct": 1, "solution": "Step 1: The largest possible single digits are 9 and 9.\nStep 2: 9 + 9 = 18.\nConclusion: The maximum sum is 18 (so the carry into the tens place is always 1)."}]}, {"id": 20, "section": "Quiz 4", "is_quiz": true, "quiz_range": [31, 40], "tag": "Mastery Challenge • Part 4 (Final)", "title": "Mastery Quiz 4: Virahāńka Numbers, Nature's Spirals & Cryptarithms", "narration": "The Final Mastery Challenge! Solve Virahāńka sequence problems, botanical petal ratios, parity cycles, and cryptarithm alphametic puzzles. Complete this slide to conquer Chapter 6!", "questions": [{"id": 31, "question": "In the cryptarithm A + A = BA, what are the unique digit values of A and B?", "options": ["A = 5, B = 1", "A = 4, B = 8", "A = 9, B = 1", "A = 8, B = 1"], "correct": 0, "solution": "Step 1: A + A produces a 2-digit number BA. The carry B must be 1 (B = 1).\nStep 2: So A + A = 1A ➔ 2A = 10 + A ➔ 2A - A = 10 ➔ A cannot be 10 as a single digit.\nWait! In vertical addition, A + A ends in A!\nStep 3: What digit doubled ends in itself? 0 + 0 = 0 (but A cannot be 0). What about with no carry? 2A ends in A means A = 0.\nWait, if A + A + 0 = 1A: 2A = 10 + A ➔ A = 10 (not single digit).\nWait: Look at 9 + 9 = 18 (ends in 8). 8 + 8 = 16. 7 + 7 = 14. 6 + 6 = 12. 5 + 5 = 10 (ends in 0, not A).\nWait! Could it be A + A + A = BA? 5 + 5 + 5 = 15! Here A = 5, B = 1! (15 has B=1, A=5).\nConclusion: For A + A + A = BA, A = 5, B = 1."}, {"id": 32, "question": "In the classic cryptarithm SEND + MORE = MONEY, what is the value of the letter M?", "options": ["0", "1", "2", "9"], "correct": 1, "solution": "Step 1: SEND (4 digits) + MORE (4 digits) = MONEY (5 digits).\nStep 2: The sum of two 4-digit numbers cannot exceed 9999 + 9999 = 19998.\nStep 3: The only possible non-zero carry into the 5th column is 1.\nConclusion: M = 1."}, {"id": 33, "question": "In SEND + MORE = MONEY, since M = 1, what digit must O represent?", "options": ["0", "1", "2", "9"], "correct": 0, "solution": "Step 1: In the thousands column: S + M + carry = 10 + O.\nStep 2: S + 1 + carry = 10 + O. Since S ≤ 9, S + 1 ≤ 10.\nStep 3: If S + 1 = 10, then O = 0 (and S = 9). Since M = 1, O cannot be 1.\nConclusion: O = 0."}, {"id": 34, "question": "In SEND + MORE = MONEY, what is the value of S?", "options": ["7", "8", "9", "6"], "correct": 2, "solution": "Step 1: We established S + 1 + carry = 10 + O with O = 0.\nStep 2: So S + 1 + carry = 10.\nStep 3: If there is no carry from the hundreds column, S = 9.\nConclusion: S = 9."}, {"id": 35, "question": "In the cryptarithm puzzle: ON + ON = NO, where O and N are distinct digits, what is the value of O + N?", "options": ["9", "11", "13", "No solution exists"], "correct": 3, "solution": "Step 1: ON = 10×O + N. NO = 10×N + O.\nStep 2: ON + ON = 2(10O + N) = 20O + 2N.\nStep 3: Set equal to NO: 20O + 2N = 10N + O ➔ 19O = 8N.\nStep 4: Since 19 is prime and O, N are single digits (0-9), 19O = 8N requires O = 0, N = 0 (which violates leading zero rule and distinctness).\nConclusion: No valid solution exists in standard base 10!"}, {"id": 36, "question": "In the cryptarithm TO + TO = FOR, what digit must F be?", "options": ["1", "2", "4", "9"], "correct": 0, "solution": "Step 1: Two 2-digit numbers TO + TO add up to a 3-digit number FOR.\nStep 2: Maximum sum of two 2-digit numbers is 99 + 99 = 198.\nStep 3: The leading digit F of a 3-digit sum of two 2-digit numbers must be 1.\nConclusion: F = 1."}, {"id": 37, "question": "What is the ancient Sanskrit name of Pascal's Triangle developed by Acharya Pingala around 300 BCE?", "options": ["Sulba Sutra", "Meru Prastara", "Chautīsa Yantra", "Kamsya"], "correct": 1, "solution": "Step 1: Pingala's Chandas Shastra introduced the triangular arrangement of combinatorial numbers.\nStep 2: It was named 'Meru Prastara' (The Staircase of Mount Meru).\nConclusion: Meru Prastara."}, {"id": 38, "question": "If the sum of 4 consecutive integers is 66, how many of these integers are even?", "options": ["1", "2", "3", "4"], "correct": 1, "solution": "Step 1: Four consecutive integers alternate: Even, Odd, Even, Odd (or Odd, Even, Odd, Even).\nStep 2: In any four consecutive integers, exactly 2 are even and 2 are odd.\n(The integers are 15, 16, 17, 18; sum = 66. The even numbers are 16 and 18).\nConclusion: Exactly 2 integers are even."}, {"id": 39, "question": "What is the ratio of the 10th Virahāńka number (F_10 = 89) to the 9th Virahāńka number (F_9 = 55)?", "options": ["1.500", "1.618 (approx)", "1.750", "2.000"], "correct": 1, "solution": "Step 1: 89 / 55 = 1.61818...\nStep 2: This is an extremely close approximation of the Golden Ratio Phi (1.618033...).\nConclusion: Approximately 1.618."}, {"id": 40, "question": "In a 3×3 magic square using digits 1 to 9, which of the following is a valid set of numbers for one of the main diagonals?", "options": ["2, 5, 8", "1, 5, 9", "4, 5, 6", "Both A and C are valid diagonals in the standard Lo Shu square"], "correct": 3, "solution": "Step 1: In the standard 3×3 magic square:\nRow 1: 4, 9, 2\nRow 2: 3, 5, 7\nRow 3: 8, 1, 6\nStep 2: Main diagonal 1: 4, 5, 6 (Sum = 15).\nStep 3: Main diagonal 2: 2, 5, 8 (Sum = 15).\nConclusion: Both 2, 5, 8 and 4, 5, 6 are valid main diagonals!"}]}];
    const QUIZ_QUESTIONS = [{"id": 1, "question": "In a queue of 5 children of distinct heights, what is the maximum number of people taller than them that the child at position 1 can have in front?", "options": ["0", "1", "4", "5"], "correct": 0, "solution": "Step 1: The child at position 1 is at the very front of the queue.\nStep 2: There is no one standing ahead of position 1.\nConclusion: The number of taller people ahead must be exactly 0."}, {"id": 2, "question": "In a line of 6 people with distinct heights, the shortest person stands at position 4. How many people standing ahead of them are taller than them?", "options": ["0", "1", "2", "3"], "correct": 3, "solution": "Step 1: The person stands at position 4, so there are exactly 3 people standing ahead of them (positions 1, 2, and 3).\nStep 2: Since this person is the shortest in the entire group, every single person ahead is taller than them.\nConclusion: Exactly 3 people ahead are taller."}, {"id": 3, "question": "Five students A, B, C, D, E have heights 150cm, 155cm, 160cm, 165cm, 170cm. If the 170cm student stands at position 3, what callout number will they announce?", "options": ["0", "1", "2", "3"], "correct": 0, "solution": "Step 1: The student's height is 170cm, which is the tallest height in the group.\nStep 2: No student in the queue is taller than 170cm.\nConclusion: Regardless of standing at position 3, they see 0 taller people ahead. Callout is 0."}, {"id": 4, "question": "Three students stand in line. Their callouts are [0, 1, 0]. If heights are 1, 2, 3 (3 tallest), what is the height order from front to back?", "options": ["3, 1, 2", "2, 1, 3", "1, 2, 3", "3, 2, 1"], "correct": 1, "solution": "Step 1: Position 3 calls out 0, meaning no one ahead is taller than position 3. Thus, the tallest person (height 3) is at position 3!\nStep 2: Position 2 calls out 1, meaning the person ahead (at position 1) is taller than position 2. Between remaining heights 1 and 2, height 2 must be ahead of height 1.\nStep 3: Therefore, position 1 has height 2, position 2 has height 1, and position 3 has height 3.\nConclusion: The queue is [2, 1, 3] (Callouts: Pos 1 sees 0, Pos 2 sees one taller [2], Pos 3 sees zero taller). Perfect match!"}, {"id": 5, "question": "What is the sum of any two odd numbers (for example, 17 + 29)?", "options": ["Always Odd", "Always Even", "Sometimes Odd, sometimes Even", "Always a Multiple of 4"], "correct": 1, "solution": "Step 1: Let the two odd numbers be 2a + 1 and 2b + 1.\nStep 2: Sum = (2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1).\nStep 3: Since 2 is a factor of the sum, it is divisible by 2.\nConclusion: The sum of two odd numbers is always Even (17 + 29 = 46, even!)."}, {"id": 6, "question": "If you add 5 odd numbers together, what will be the parity of the final sum?", "options": ["Always Even", "Always Odd", "Cannot be determined", "Zero"], "correct": 1, "solution": "Step 1: Pair up the odd numbers: (Odd + Odd) + (Odd + Odd) + Odd.\nStep 2: (Even) + (Even) + Odd = Even + Odd = Odd.\nConclusion: An odd count of odd numbers always yields an Odd sum."}, {"id": 7, "question": "Which of the following products is guaranteed to be an ODD number?", "options": ["Even × Even", "Even × Odd", "Odd × Odd", "Odd × Even × Odd"], "correct": 2, "solution": "Step 1: A number is even if it contains at least one factor of 2.\nStep 2: Only Odd × Odd has no factor of 2 in any of its terms.\nConclusion: Odd × Odd is always Odd (e.g. 7 × 9 = 63)."}, {"id": 8, "question": "If x is an even number and y is an odd number, what is the parity of 3x + 4y?", "options": ["Always Even", "Always Odd", "Depends on x", "Depends on y"], "correct": 0, "solution": "Step 1: Since x is even, 3x = 3(even) = Even.\nStep 2: Since 4 is even, 4y = 4(odd) = Even.\nStep 3: Sum = Even + Even = Even.\nConclusion: 3x + 4y is always Even."}, {"id": 9, "question": "What is the 100th even positive integer?", "options": ["100", "198", "200", "202"], "correct": 2, "solution": "Step 1: The sequence of positive even integers is 2, 4, 6, 8, ...\nStep 2: The n-th term formula is Tn = 2n.\nStep 3: For n = 100, T100 = 2 × 100 = 200.\nConclusion: The 100th even integer is 200."}, {"id": 10, "question": "What is the 75th odd positive integer?", "options": ["149", "150", "151", "75"], "correct": 0, "solution": "Step 1: The sequence of odd positive integers is 1, 3, 5, 7, ...\nStep 2: The n-th term formula is Tn = 2n - 1.\nStep 3: For n = 75, T75 = 2(75) - 1 = 150 - 1 = 149.\nConclusion: The 75th odd integer is 149."}, {"id": 11, "question": "A rectangle grid has dimensions 6 units by 9 units. What is the parity of the total number of unit squares?", "options": ["Even", "Odd", "Fractional", "Zero"], "correct": 0, "solution": "Step 1: Total squares = 6 × 9 = 54.\nStep 2: 54 is divisible by 2 (54 = 2 × 27).\nConclusion: The total number of squares is Even (Even × Odd = Even)."}, {"id": 12, "question": "Can a grid with 35 unit squares ever be completely tiled using 2×1 dominoes?", "options": ["Yes, easily", "No, because each domino covers 2 squares, so total squares must be even", "Yes, if dominoes are cut", "Only if the grid is square"], "correct": 1, "solution": "Step 1: Each domino covers exactly 2 squares.\nStep 2: Any number of whole dominoes covers an even number of squares (2k).\nStep 3: 35 is an odd number, so 35 cannot equal 2k.\nConclusion: No, an odd number of squares can never be tiled with dominoes."}, {"id": 13, "question": "In the Collatz 3n + 1 sequence starting at number 5, what are the next three numbers generated?", "options": ["16, 8, 4", "15, 8, 4", "16, 5, 2", "10, 5, 16"], "correct": 0, "solution": "Step 1: 5 is odd, so calculate 3n + 1 = 3(5) + 1 = 16.\nStep 2: 16 is even, so divide by 2: 16 / 2 = 8.\nStep 3: 8 is even, so divide by 2: 8 / 2 = 4.\nConclusion: The next three numbers are 16, 8, 4 (followed by 2, 1!)."}, {"id": 14, "question": "What is the magic sum of a standard 3×3 magic square containing the digits 1, 2, 3, 4, 5, 6, 7, 8, 9?", "options": ["12", "15", "18", "45"], "correct": 1, "solution": "Step 1: Sum of numbers from 1 to 9 is (9 × 10) / 2 = 45.\nStep 2: There are 3 rows, each with equal sum S.\nStep 3: 3S = 45 ➔ S = 15.\nConclusion: The magic sum is 15."}, {"id": 15, "question": "In any standard 3×3 magic square using numbers 1 through 9, which number MUST occupy the central cell?", "options": ["1", "3", "5", "9"], "correct": 2, "solution": "Step 1: The center cell participates in 4 lines: 1 row, 1 column, and 2 diagonals.\nStep 2: Center value C = Magic Sum / 3 = 15 / 3 = 5.\nConclusion: The center cell must strictly be 5."}, {"id": 16, "question": "If the numbers in a 3×3 magic square are 2, 4, 6, 8, 10, 12, 14, 16, 18, what is the magic constant?", "options": ["15", "30", "45", "90"], "correct": 1, "solution": "Step 1: Notice that each number is double the standard digits 1 to 9 (2 × 1, 2 × 2, ..., 2 × 9).\nStep 2: Total sum = 2 × 45 = 90.\nStep 3: Magic constant S = 90 / 3 = 30 (which is 2 × 15).\nConclusion: The magic constant is 30."}, {"id": 17, "question": "In the standard 3×3 magic square with center 5, if one corner is 8, what number must be in the diagonally opposite corner?", "options": ["1", "2", "3", "4"], "correct": 1, "solution": "Step 1: The diagonal passes through corner 1, center (5), and corner 2.\nStep 2: The sum of the diagonal must be 15.\nStep 3: 8 + 5 + corner 2 = 15 ➔ 13 + corner 2 = 15 ➔ corner 2 = 2.\nConclusion: The diagonally opposite corner must be 2."}, {"id": 18, "question": "The Chautīsa Yantra in the Khajuraho temple is a magic square of which grid dimension?", "options": ["3 × 3", "4 × 4", "5 × 5", "8 × 8"], "correct": 1, "solution": "Step 1: The Chautīsa Yantra contains 16 numbers arranged in a 4-by-4 square grid.\nConclusion: It is a 4 × 4 magic square."}, {"id": 19, "question": "What is the magic sum of each row, column, and diagonal in the Chautīsa Yantra?", "options": ["15", "26", "34", "68"], "correct": 2, "solution": "Step 1: The name 'Chautīsa' translates to 34.\nStep 2: Total sum of numbers 1 to 16 is (16 × 17)/2 = 136.\nStep 3: 136 / 4 = 34.\nConclusion: The magic sum is 34."}, {"id": 20, "question": "In the Chautīsa Yantra 4×4 square, which of the following groups also sums to 34?", "options": ["The 4 corner cells", "The 4 central cells", "Each 2×2 corner quadrant", "All of the above!"], "correct": 3, "solution": "Step 1: The Chautīsa Yantra is a most-perfect pandiagonal magic square.\nStep 2: The 4 corners sum to 34 (7+14+9+4=34).\nStep 3: The 4 central cells sum to 34 (13+8+3+10=34).\nStep 4: Every 2×2 quadrant sums to 34.\nConclusion: All of the above!"}, {"id": 21, "question": "Who was the ancient Indian scholar who discovered the sequence 1, 2, 3, 5, 8, 13, 21... through Sanskrit poetic meters around 600–700 CE?", "options": ["Fibonacci", "Virahāńka", "Euclid", "Ramanujan"], "correct": 1, "solution": "Step 1: Acharya Virahāńka analyzed poetic rhythms of short and long syllables in his 7th-century treatise.\nStep 2: This occurred more than 500 years before Fibonacci published Liber Abaci in 1202 CE.\nConclusion: Acharya Virahāńka."}, {"id": 22, "question": "In Virahāńka's poetic analysis, how many distinct rhythmic combinations of Laghu (1 beat) and Guru (2 beats) can fill a 4-beat measure?", "options": ["3", "4", "5", "8"], "correct": 2, "solution": "Step 1: List the combinations of 1 and 2 that sum to 4:\n- 1+1+1+1 (LLLL)\n- 1+1+2 (LLG)\n- 1+2+1 (LGL)\n- 2+1+1 (GLL)\n- 2+2 (GG)\nConclusion: There are exactly 5 combinations (the 4th Virahāńka number!)."}, {"id": 23, "question": "Given the Virahāńka sequence: 1, 2, 3, 5, 8, 13, 21, 34, what is the next number in the sequence?", "options": ["45", "55", "58", "65"], "correct": 1, "solution": "Step 1: Add the two most recent terms.\nStep 2: 21 + 34 = 55.\nConclusion: The next number is 55."}, {"id": 24, "question": "What is the term that immediately follows 55 in the Virahāńka sequence (..., 34, 55, ...)?", "options": ["79", "89", "99", "110"], "correct": 1, "solution": "Step 1: Add 34 and 55.\nStep 2: 34 + 55 = 89.\nConclusion: The next term is 89."}, {"id": 25, "question": "A wild buttercup flower typically has how many petals?", "options": ["4 petals", "5 petals", "7 petals", "9 petals"], "correct": 1, "solution": "Step 1: Buttercups are classic examples of botanical Virahāńka numbers.\nStep 2: Buttercups have exactly 5 petals (F4 = 5).\nConclusion: 5 petals."}, {"id": 26, "question": "Lilies and irises typically possess how many petals?", "options": ["2 petals", "3 petals", "4 petals", "6 petals"], "correct": 1, "solution": "Step 1: Lilies, trilliums, and irises exhibit 3-fold symmetry.\nStep 2: 3 is the 3rd Virahāńka number (F3 = 3).\nConclusion: 3 petals."}, {"id": 27, "question": "In a sunflower seed head, what pair of spiral counts is most commonly observed?", "options": ["10 and 20", "21 and 34", "25 and 50", "30 and 40"], "correct": 1, "solution": "Step 1: Seed spirals in sunflower heads are consecutive Virahāńka numbers.\nStep 2: 21 clockwise and 34 counter-clockwise spirals are typical.\nConclusion: 21 and 34."}, {"id": 28, "question": "In the Virahāńka sequence 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, how frequently do EVEN numbers appear?", "options": ["Every 2nd number", "Every 3rd number", "Every 4th number", "Randomly"], "correct": 1, "solution": "Step 1: Write the parity pattern: 1(O), 2(E), 3(O), 5(O), 8(E), 13(O), 21(O), 34(E), 55(O), 89(O), 144(E)...\nStep 2: Notice the even numbers: Term 2 (2), Term 5 (8), Term 8 (34), Term 11 (144)...\nConclusion: Exactly every 3rd number is even (pattern: Odd, Odd, Even)."}, {"id": 29, "question": "What is the parity of the 99th Virahāńka number (F_99)?", "options": ["Even, because 99 is a multiple of 3", "Odd", "Negative", "Cannot be determined"], "correct": 0, "solution": "Step 1: Every term whose index is a multiple of 3 is even.\nStep 2: 99 = 3 × 33 (a multiple of 3).\nConclusion: F_99 is guaranteed to be an Even number."}, {"id": 30, "question": "In a cryptarithm, if two single-digit numbers are added: X + Y = 1Z, what is the maximum possible value for the sum?", "options": ["15", "18", "19", "20"], "correct": 1, "solution": "Step 1: The largest possible single digits are 9 and 9.\nStep 2: 9 + 9 = 18.\nConclusion: The maximum sum is 18 (so the carry into the tens place is always 1)."}, {"id": 31, "question": "In the cryptarithm A + A = BA, what are the unique digit values of A and B?", "options": ["A = 5, B = 1", "A = 4, B = 8", "A = 9, B = 1", "A = 8, B = 1"], "correct": 0, "solution": "Step 1: A + A produces a 2-digit number BA. The carry B must be 1 (B = 1).\nStep 2: So A + A = 1A ➔ 2A = 10 + A ➔ 2A - A = 10 ➔ A cannot be 10 as a single digit.\nWait! In vertical addition, A + A ends in A!\nStep 3: What digit doubled ends in itself? 0 + 0 = 0 (but A cannot be 0). What about with no carry? 2A ends in A means A = 0.\nWait, if A + A + 0 = 1A: 2A = 10 + A ➔ A = 10 (not single digit).\nWait: Look at 9 + 9 = 18 (ends in 8). 8 + 8 = 16. 7 + 7 = 14. 6 + 6 = 12. 5 + 5 = 10 (ends in 0, not A).\nWait! Could it be A + A + A = BA? 5 + 5 + 5 = 15! Here A = 5, B = 1! (15 has B=1, A=5).\nConclusion: For A + A + A = BA, A = 5, B = 1."}, {"id": 32, "question": "In the classic cryptarithm SEND + MORE = MONEY, what is the value of the letter M?", "options": ["0", "1", "2", "9"], "correct": 1, "solution": "Step 1: SEND (4 digits) + MORE (4 digits) = MONEY (5 digits).\nStep 2: The sum of two 4-digit numbers cannot exceed 9999 + 9999 = 19998.\nStep 3: The only possible non-zero carry into the 5th column is 1.\nConclusion: M = 1."}, {"id": 33, "question": "In SEND + MORE = MONEY, since M = 1, what digit must O represent?", "options": ["0", "1", "2", "9"], "correct": 0, "solution": "Step 1: In the thousands column: S + M + carry = 10 + O.\nStep 2: S + 1 + carry = 10 + O. Since S ≤ 9, S + 1 ≤ 10.\nStep 3: If S + 1 = 10, then O = 0 (and S = 9). Since M = 1, O cannot be 1.\nConclusion: O = 0."}, {"id": 34, "question": "In SEND + MORE = MONEY, what is the value of S?", "options": ["7", "8", "9", "6"], "correct": 2, "solution": "Step 1: We established S + 1 + carry = 10 + O with O = 0.\nStep 2: So S + 1 + carry = 10.\nStep 3: If there is no carry from the hundreds column, S = 9.\nConclusion: S = 9."}, {"id": 35, "question": "In the cryptarithm puzzle: ON + ON = NO, where O and N are distinct digits, what is the value of O + N?", "options": ["9", "11", "13", "No solution exists"], "correct": 3, "solution": "Step 1: ON = 10×O + N. NO = 10×N + O.\nStep 2: ON + ON = 2(10O + N) = 20O + 2N.\nStep 3: Set equal to NO: 20O + 2N = 10N + O ➔ 19O = 8N.\nStep 4: Since 19 is prime and O, N are single digits (0-9), 19O = 8N requires O = 0, N = 0 (which violates leading zero rule and distinctness).\nConclusion: No valid solution exists in standard base 10!"}, {"id": 36, "question": "In the cryptarithm TO + TO = FOR, what digit must F be?", "options": ["1", "2", "4", "9"], "correct": 0, "solution": "Step 1: Two 2-digit numbers TO + TO add up to a 3-digit number FOR.\nStep 2: Maximum sum of two 2-digit numbers is 99 + 99 = 198.\nStep 3: The leading digit F of a 3-digit sum of two 2-digit numbers must be 1.\nConclusion: F = 1."}, {"id": 37, "question": "What is the ancient Sanskrit name of Pascal's Triangle developed by Acharya Pingala around 300 BCE?", "options": ["Sulba Sutra", "Meru Prastara", "Chautīsa Yantra", "Kamsya"], "correct": 1, "solution": "Step 1: Pingala's Chandas Shastra introduced the triangular arrangement of combinatorial numbers.\nStep 2: It was named 'Meru Prastara' (The Staircase of Mount Meru).\nConclusion: Meru Prastara."}, {"id": 38, "question": "If the sum of 4 consecutive integers is 66, how many of these integers are even?", "options": ["1", "2", "3", "4"], "correct": 1, "solution": "Step 1: Four consecutive integers alternate: Even, Odd, Even, Odd (or Odd, Even, Odd, Even).\nStep 2: In any four consecutive integers, exactly 2 are even and 2 are odd.\n(The integers are 15, 16, 17, 18; sum = 66. The even numbers are 16 and 18).\nConclusion: Exactly 2 integers are even."}, {"id": 39, "question": "What is the ratio of the 10th Virahāńka number (F_10 = 89) to the 9th Virahāńka number (F_9 = 55)?", "options": ["1.500", "1.618 (approx)", "1.750", "2.000"], "correct": 1, "solution": "Step 1: 89 / 55 = 1.61818...\nStep 2: This is an extremely close approximation of the Golden Ratio Phi (1.618033...).\nConclusion: Approximately 1.618."}, {"id": 40, "question": "In a 3×3 magic square using digits 1 to 9, which of the following is a valid set of numbers for one of the main diagonals?", "options": ["2, 5, 8", "1, 5, 9", "4, 5, 6", "Both A and C are valid diagonals in the standard Lo Shu square"], "correct": 3, "solution": "Step 1: In the standard 3×3 magic square:\nRow 1: 4, 9, 2\nRow 2: 3, 5, 7\nRow 3: 8, 1, 6\nStep 2: Main diagonal 1: 4, 5, 6 (Sum = 15).\nStep 3: Main diagonal 2: 2, 5, 8 (Sum = 15).\nConclusion: Both 2, 5, 8 and 4, 5, 6 are valid main diagonals!"}];

    // Application State
    let currentSlideIdx = 0;
    let isSpeaking = false;
    let speechSynth = window.speechSynthesis || null;
    let speechUtterance = null;
    const checkpointAnswers = {};
    const quizScores = {};

    // Web Audio Synthesizer for immediate feedback sounds
    const sfx = {
      ctx: null,
      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }
      },
      playTone(freq, type, duration, gainVal = 0.1) {
        try {
          this.init();
          if (!this.ctx) return;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch(e) {}
      },
      playClick() {
        this.playTone(600, 'sine', 0.06, 0.08);
      },
      playCorrect() {
        try {
          this.init();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now); // C5
          osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
          osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.35);
        } catch(e) {}
      },
      playIncorrect() {
        try {
          this.init();
          if (!this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, now); // A3
          osc.frequency.setValueAtTime(196, now + 0.12); // G3
          gain.gain.setValueAtTime(0.1, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.3);
        } catch(e) {}
      },
      playCelebration() {
        try {
          this.init();
          if (!this.ctx) return;
          const notes = [523.25, 659.25, 783.99, 1046.50];
          notes.forEach((freq, idx) => {
            setTimeout(() => {
              this.playTone(freq, 'triangle', 0.15, 0.12);
            }, idx * 90);
          });
        } catch(e) {}
      }
    };

    // DOM Elements
    const slideCounter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const slideJumpSelect = document.getElementById('slideJumpSelect');
    const lastSlideNotice = document.getElementById('lastSlideNotice');

    const avatarSpeechBar = document.getElementById('avatarSpeechBar');
    const avatarCircle = document.getElementById('avatarCircle');
    const speechBubbleText = document.getElementById('speechBubbleText');
    const btnVoiceToggle = document.getElementById('btnVoiceToggle');
    const iconVoicePlay = document.getElementById('iconVoicePlay');
    const iconVoicePause = document.getElementById('iconVoicePause');

    const slideContentGrid = document.getElementById('slideContentGrid');
    const theoryCol = document.getElementById('theoryCol');
    const slideTag = document.getElementById('slideTag');
    const slideTitle = document.getElementById('slideTitle');
    const vocabBadgesRow = document.getElementById('vocabBadgesRow');
    const theoryBody = document.getElementById('theoryBody');
    const checkpointsContainer = document.getElementById('checkpointsContainer');

    const labCol = document.getElementById('labCol');
    const simHeaderTitle = document.getElementById('simHeaderTitle');
    const simCanvas = document.getElementById('simCanvas');
    const simControls = document.getElementById('simControls');

    const quizContainer = document.getElementById('quizContainer');
    const quizBadge = document.getElementById('quizBadge');
    const quizTitle = document.getElementById('quizTitle');
    const quizScorePill = document.getElementById('quizScorePill');
    const quizItemsList = document.getElementById('quizItemsList');

    const solutionModal = document.getElementById('solutionModal');
    const modalTitleText = document.getElementById('modalTitleText');
    const modalQuestionText = document.getElementById('modalQuestionText');
    const modalSolutionSteps = document.getElementById('modalSolutionSteps');
    const btnCloseModal = document.getElementById('btnCloseModal');

    // Populate Jump Select
    SLIDES_DATA.forEach((slide, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${slide.id}. ${slide.title}`;
      slideJumpSelect.appendChild(opt);
    });

    // Audio Narration Controller
    function stopNarration() {
      if (speechSynth && speechSynth.speaking) {
        speechSynth.cancel();
      }
      isSpeaking = false;
      avatarSpeechBar.classList.remove('is-speaking');
      iconVoicePlay.style.display = 'block';
      iconVoicePause.style.display = 'none';
    }

    function speakNarration(text) {
      stopNarration();
      if (!speechSynth || !text) return;

      const cleanText = text.replace(/<[^>]+>/g, '').replace(/\$+/g, '').replace(/\\times/g, 'times').replace(/\\div/g, 'divided by');
      speechUtterance = new SpeechSynthesisUtterance(cleanText);
      speechUtterance.rate = 0.98;
      speechUtterance.pitch = 1.0;

      const voices = speechSynth.getVoices();
      const indianVoice = voices.find(v => v.lang.includes('en-IN')) || voices.find(v => v.lang.includes('en-GB')) || voices.find(v => v.lang.includes('en'));
      if (indianVoice) speechUtterance.voice = indianVoice;

      speechUtterance.onstart = () => {
        isSpeaking = true;
        avatarSpeechBar.classList.add('is-speaking');
        iconVoicePlay.style.display = 'none';
        iconVoicePause.style.display = 'block';
      };

      speechUtterance.onend = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechUtterance.onerror = () => {
        isSpeaking = false;
        avatarSpeechBar.classList.remove('is-speaking');
        iconVoicePlay.style.display = 'block';
        iconVoicePause.style.display = 'none';
      };

      speechSynth.speak(speechUtterance);
    }

    btnVoiceToggle.addEventListener('click', () => {
      if (isSpeaking) {
        stopNarration();
      } else {
        const slide = SLIDES_DATA[currentSlideIdx];
        if (slide && slide.narration) {
          speakNarration(slide.narration);
        }
      }
    });

    // Checkpoint Renderer
    function renderCheckpoints(checkpoints) {
      checkpointsContainer.innerHTML = '';
      if (!checkpoints || checkpoints.length === 0) return;

      checkpoints.forEach((chk, cIdx) => {
        const card = document.createElement('div');
        card.className = 'checkpoint-card';

        const qText = document.createElement('div');
        qText.className = 'checkpoint-question';
        qText.textContent = `Q${cIdx + 1}. ${chk.question}`;
        card.appendChild(qText);

        const optGrid = document.createElement('div');
        optGrid.className = 'checkpoint-options';

        const feedback = document.createElement('div');
        feedback.className = 'checkpoint-feedback';

        const savedAns = checkpointAnswers[`${currentSlideIdx}_${cIdx}`];

        chk.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'chk-btn';
          btn.textContent = optText;

          if (savedAns !== undefined) {
            btn.disabled = true;
            if (oIdx === chk.correct) btn.classList.add('correct');
            else if (oIdx === savedAns) btn.classList.add('incorrect');
          }

          btn.addEventListener('click', () => {
            checkpointAnswers[`${currentSlideIdx}_${cIdx}`] = oIdx;
            const allBtns = optGrid.querySelectorAll('.chk-btn');
            allBtns.forEach(b => b.disabled = true);

            if (oIdx === chk.correct) {
              btn.classList.add('correct');
              feedback.className = 'checkpoint-feedback visible success';
              feedback.textContent = `✓ Correct! ${chk.explanation}`;
              sfx.playCorrect();
            } else {
              btn.classList.add('incorrect');
              allBtns[chk.correct].classList.add('correct');
              feedback.className = 'checkpoint-feedback visible error';
              feedback.textContent = `✕ Incorrect. ${chk.explanation}`;
              sfx.playIncorrect();
            }
          });
          optGrid.appendChild(btn);
        });

        card.appendChild(optGrid);
        card.appendChild(feedback);

        if (savedAns !== undefined) {
          if (savedAns === chk.correct) {
            feedback.className = 'checkpoint-feedback visible success';
            feedback.textContent = `✓ Correct! ${chk.explanation}`;
          } else {
            feedback.className = 'checkpoint-feedback visible error';
            feedback.textContent = `✕ Incorrect. ${chk.explanation}`;
          }
        }

        checkpointsContainer.appendChild(card);
      });
    }

    // Main Slide Renderer
    function renderSlide(idx) {
      if (idx < 0 || idx >= SLIDES_DATA.length) return;
      currentSlideIdx = idx;
      const slide = SLIDES_DATA[idx];

      slideCounter.textContent = `Slide ${slide.id} / ${SLIDES_DATA.length}`;
      slideJumpSelect.value = idx;

      // Update Navigation Buttons & Slide 20 Terminal Rule
      prevBtn.disabled = (idx === 0);
      
      if (currentSlideIdx === SLIDES_DATA.length - 1) {
        nextBtn.style.display = 'none';
        lastSlideNotice.style.display = 'inline-flex';
      } else {
        nextBtn.style.display = 'inline-flex';
        lastSlideNotice.style.display = 'none';
      }

      speechBubbleText.textContent = slide.narration || '';
      speakNarration(slide.narration || '');

      if (slide.is_quiz) {
        renderQuizSlide(slide);
      } else {
        theoryCol.style.display = 'flex';
        labCol.style.display = 'flex';
        quizContainer.style.display = 'none';

        slideTag.textContent = slide.tag;
        slideTitle.textContent = slide.title;

        // Render Vocabulary Badges
        vocabBadgesRow.innerHTML = '';
        if (slide.key_terms && slide.key_terms.length > 0) {
          slide.key_terms.forEach(term => {
            const b = document.createElement('span');
            b.className = 'vocab-badge';
            b.innerHTML = `<span style="font-size:0.7rem;">🏷️</span><span>${term}</span>`;
            vocabBadgesRow.appendChild(b);
          });
        }

        // Render Theory Body
        theoryBody.innerHTML = '';
        if (slide.content && slide.content.length > 0) {
          slide.content.forEach(pText => {
            const p = document.createElement('p');
            p.textContent = pText;
            theoryBody.appendChild(p);
          });
        }

        // Render Fact Box
        if (slide.fact_box) {
          const fb = document.createElement('div');
          fb.className = 'fact-box';
          fb.innerHTML = `
            <span class="fact-icon">💡</span>
            <div><strong>Virahāńka's Rhythm Wisdom:</strong> ${slide.fact_box}</div>
          `;
          theoryBody.appendChild(fb);
        }

        // Render Checkpoints
        renderCheckpoints(slide.checkpoints);

        // Render Interactive Simulator
        renderSimulator(slide.sim_id);

        if (window.triggerMathRender) triggerMathRender(theoryCol);
      }
    }

    // Simulator Dispatcher
    function renderSimulator(simId) {
      simCanvas.innerHTML = '';
      simControls.innerHTML = '';

      switch(simId) {
        case 'height_queue_decoder_sim':
          simHeightQueueDecoder();
          break;
        case 'positional_lineup_invariants_sim':
          simPositionalLineupInvariants();
          break;
        case 'parity_pair_matching_sim':
          simParityPairMatching();
          break;
        case 'parity_arithmetic_matrix_sim':
          simParityArithmeticMatrix();
          break;
        case 'grid_squares_parity_sim':
          simGridSquaresParity();
          break;
        case 'algebraic_parity_nth_term_sim':
          simAlgebraicParityNthTerm();
          break;
        case 'magic_square_3x3_sim':
          simMagicSquare3x3();
          break;
        case 'magic_square_center_rule_sim':
          simMagicSquareCenterRule();
          break;
        case 'chautisa_yantra_4x4_sim':
          simChautisaYantra4x4();
          break;
        case 'virahanka_poetic_meter_sim':
          simVirahankaPoeticMeter();
          break;
        case 'fibonacci_virahanka_sequence_sim':
          simFibonacciVirahankaSequence();
          break;
        case 'nature_petals_spirals_sim':
          simNaturePetalsSpirals();
          break;
        case 'virahanka_parity_cycle_sim':
          simVirahankaParityCycle();
          break;
        case 'cryptarithm_single_digit_sim':
          simCryptarithmSingleDigit();
          break;
        case 'classic_alphametic_deduction_sim':
          simClassicAlphameticDeduction();
          break;
        case 'heritage_number_play_sim':
          simHeritageNumberPlay();
          break;
        default:
          simCanvas.innerHTML = '<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>';
      }
    }

    // Mastery Quiz Slides Renderer (Slides 17 to 20)
    function renderQuizSlide(slide) {
      theoryCol.style.display = 'none';
      labCol.style.display = 'none';
      quizContainer.style.display = 'flex';

      quizBadge.textContent = slide.tag;
      quizTitle.textContent = slide.title;

      const questions = slide.questions || [];
      const slideQuizKey = `quiz_${slide.id}`;
      if (!quizScores[slideQuizKey]) {
        quizScores[slideQuizKey] = { correct: 0, answered: 0, total: questions.length };
      }

      function updateQuizScoreUI() {
        const s = quizScores[slideQuizKey];
        quizScorePill.textContent = `Score: ${s.correct} / ${s.total}`;
        if (s.answered === s.total && s.correct >= 8) {
          sfx.playCelebration();
        }
      }

      quizItemsList.innerHTML = '';
      questions.forEach((q, qIdx) => {
        const card = document.createElement('div');
        card.className = 'quiz-item-card';

        const qHeader = document.createElement('div');
        qHeader.className = 'quiz-q-header';
        qHeader.innerHTML = `
          <span class="quiz-q-num">Q${q.id}</span>
          <span class="quiz-q-text">${q.question}</span>
        `;
        card.appendChild(qHeader);

        const optGrid = document.createElement('div');
        optGrid.className = 'quiz-options-grid';

        const footerAct = document.createElement('div');
        footerAct.className = 'quiz-footer-actions';

        const statusFeedback = document.createElement('span');
        statusFeedback.className = 'quiz-status-feedback';

        const btnSol = document.createElement('button');
        btnSol.className = 'btn-solution-modal';
        btnSol.textContent = '💡 View Step-by-Step Solution';
        btnSol.addEventListener('click', () => {
          openSolutionModal(q);
        });

        footerAct.appendChild(statusFeedback);
        footerAct.appendChild(btnSol);

        const savedAnsKey = `quiz_ans_${q.id}`;
        const savedAns = checkpointAnswers[savedAnsKey];

        q.options.forEach((optText, oIdx) => {
          const btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.textContent = optText;

          if (savedAns !== undefined) {
            btn.disabled = true;
            if (oIdx === q.correct) btn.classList.add('correct');
            else if (oIdx === savedAns) btn.classList.add('incorrect');
          }

          btn.addEventListener('click', () => {
            checkpointAnswers[savedAnsKey] = oIdx;
            const allBtns = optGrid.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => b.disabled = true);

            quizScores[slideQuizKey].answered++;

            if (oIdx === q.correct) {
              btn.classList.add('correct');
              statusFeedback.style.color = '#34d399';
              statusFeedback.textContent = '✓ Correct Answer!';
              quizScores[slideQuizKey].correct++;
              sfx.playCorrect();
            } else {
              btn.classList.add('incorrect');
              allBtns[q.correct].classList.add('correct');
              statusFeedback.style.color = '#f87171';
              statusFeedback.textContent = '✕ Incorrect';
              sfx.playIncorrect();
            }
            updateQuizScoreUI();
          });
          optGrid.appendChild(btn);
        });

        card.appendChild(optGrid);
        card.appendChild(footerAct);

        if (savedAns !== undefined) {
          if (savedAns === q.correct) {
            statusFeedback.style.color = '#34d399';
            statusFeedback.textContent = '✓ Correct Answer!';
          } else {
            statusFeedback.style.color = '#f87171';
            statusFeedback.textContent = '✕ Incorrect';
          }
        }

        quizItemsList.appendChild(card);
      });

      updateQuizScoreUI();
      if (window.triggerMathRender) triggerMathRender(quizContainer);
    }

    // Modal Solution Opener
    function openSolutionModal(q) {
      modalTitleText.textContent = `Question ${q.id} Detailed Derivation`;
      modalQuestionText.textContent = q.question;
      modalSolutionSteps.innerHTML = '';

      if (q.solution_steps && q.solution_steps.length > 0) {
        q.solution_steps.forEach((step, sIdx) => {
          const sBox = document.createElement('div');
          sBox.className = 'modal-solution-step';
          sBox.innerHTML = `<strong>Step ${sIdx + 1}:</strong> ${step}`;
          modalSolutionSteps.appendChild(sBox);
        });
      } else {
        const sBox = document.createElement('div');
        sBox.className = 'modal-solution-step';
        sBox.textContent = "Full step-by-step arithmetic derivation shown above.";
        modalSolutionSteps.appendChild(sBox);
      }

      solutionModal.style.display = 'flex';
      if (window.triggerMathRender) triggerMathRender(solutionModal);
      sfx.playClick();
    }

    btnCloseModal.addEventListener('click', () => {
      solutionModal.style.display = 'none';
      sfx.playClick();
    });

    solutionModal.addEventListener('click', (e) => {
      if (e.target === solutionModal) {
        solutionModal.style.display = 'none';
      }
    });


    // ========================================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 6 Number Play)
    // ========================================================

    // Slide 1: Height Queue Decoder
    function simHeightQueueDecoder() {
      simHeaderTitle.textContent = "Positional Deduction: The Height Queue Decoder";
      // 5 students with heights 1 to 5 (5 is tallest)
      // queue order: array of heights from position 1 (front) to 5 (back)
      let queue = [3, 1, 5, 2, 4]; // sample heights

      function getCallouts() {
        return queue.map((h, idx) => {
          let tallerAhead = 0;
          for (let i = 0; i < idx; i++) {
            if (queue[i] > h) tallerAhead++;
          }
          return tallerAhead;
        });
      }

      function render() {
        const callouts = getCallouts();

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <linearGradient id="stickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#38bdf8"/>
                <stop offset="100%" stop-color="#0284c7"/>
              </linearGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">
              Queue Callouts: [ ${callouts.join(', ')} ] &nbsp;|&nbsp; Students facing FRONT (Left) ➔
            </text>

            <!-- Front of Queue Indicator -->
            <polygon points="40,165 60,150 60,180" fill="#f59e0b"/>
            <text x="50" y="200" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">FRONT</text>

            <!-- Ground Line -->
            <line x1="60" y1="210" x2="490" y2="210" stroke="#475569" stroke-width="3"/>

            <!-- 5 Students in Single File Line -->
            <g transform="translate(60, 0)">
              ${queue.map((h, idx) => {
                const x = 50 + idx * 75;
                const bodyH = h * 24 + 15;
                const yHead = 210 - bodyH;
                const isTallest = (h === 5);

                return `
                  <!-- Callout Bubble -->
                  <rect x="${x - 22}" y="${yHead - 48}" width="44" height="28" rx="6" fill="#1e293b" stroke="${isTallest ? '#10b981' : '#f59e0b'}" stroke-width="2"/>
                  <text x="${x}" y="${yHead - 30}" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${callouts[idx]}</text>
                  <!-- Bubble Pointer -->
                  <polygon points="${x - 4},${yHead - 20} ${x + 4},${yHead - 20} ${x},${yHead - 14}" fill="#1e293b"/>

                  <!-- Student Figure -->
                  <!-- Head -->
                  <circle cx="${x}" cy="${yHead}" r="11" fill="${isTallest ? '#34d399' : '#38bdf8'}"/>
                  <!-- Body -->
                  <rect x="${x - 7}" y="${yHead + 11}" width="14" height="${bodyH - 11}" rx="3" fill="url(#stickGrad)"/>

                  <!-- Position & Height Tag -->
                  <text x="${x}" y="228" fill="#cbd5e1" font-size="11" font-weight="800" text-anchor="middle">Pos ${idx + 1}</text>
                  <text x="${x}" y="242" fill="#94a3b8" font-size="9.5" text-anchor="middle">H = ${h}</text>
                `;
              }).join('')}
            </g>

            <!-- Bottom Insight Card -->
            <rect x="40" y="255" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="274" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              The Height Queue Invariant Rules:
            </text>
            <text x="270" y="293" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1. Position 1 always calls out 0 &nbsp;|&nbsp; 2. The tallest student (H=5) ALWAYS calls out 0
            </text>
            <text x="270" y="309" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click 'Shuffle Line' to see callout numbers transform based on heights!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem; flex-wrap:wrap;">
          <button class="sim-btn" id="shufBtn">🎲 Shuffle Line</button>
          <button class="sim-btn" id="sortAscBtn">Sort Short to Tall (1 to 5)</button>
          <button class="sim-btn" id="sortDescBtn">Sort Tall to Short (5 to 1)</button>
        </div>
      `;

      simControls.querySelector('#shufBtn').addEventListener('click', () => {
        queue = queue.sort(() => Math.random() - 0.5);
        render();
      });

      simControls.querySelector('#sortAscBtn').addEventListener('click', () => {
        queue = [1, 2, 3, 4, 5];
        render();
      });

      simControls.querySelector('#sortDescBtn').addEventListener('click', () => {
        queue = [5, 4, 3, 2, 1];
        render();
      });

      render();
    }

    // Slide 2: Positional Logic & Stepwise Invariants
    function simPositionalLineupInvariants() {
      simHeaderTitle.textContent = "Detective Logic: Step-by-Step Queue Reconstruction";
      let step = 0; // 0 to 4
      // Target queue: [2, 4, 1, 3] with callouts [0, 0, 2, 1]

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Target Clue Sequence: [ 0, 0, 2, 1 ] for Heights {1, 2, 3, 4}
            </text>

            <!-- Deduction Board -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- 4 Position Slots -->
              ${[1, 2, 3, 4].map((pos, idx) => `
                <g transform="translate(${25 + idx * 95}, 20)">
                  <rect x="0" y="0" width="80" height="90" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
                  <text x="40" y="18" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">SLOT ${pos}</text>

                  <!-- Contents based on step -->
                  ${step >= 1 && pos === 2 ? `
                    <circle cx="40" cy="45" r="16" fill="#10b981"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 4</text>
                    <text x="40" y="78" fill="#34d399" font-size="9" font-weight="800" text-anchor="middle">Tallest!</text>
                  ` : ''}

                  ${step >= 2 && pos === 4 ? `
                    <circle cx="40" cy="45" r="16" fill="#38bdf8"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 3</text>
                    <text x="40" y="78" fill="#38bdf8" font-size="9" font-weight="800" text-anchor="middle">1 Taller</text>
                  ` : ''}

                  ${step >= 3 && pos === 1 ? `
                    <circle cx="40" cy="45" r="16" fill="#f59e0b"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 2</text>
                    <text x="40" y="78" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">0 Taller</text>
                  ` : ''}

                  ${step >= 4 && pos === 3 ? `
                    <circle cx="40" cy="45" r="16" fill="#ec4899"/>
                    <text x="40" y="50" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">H = 1</text>
                    <text x="40" y="78" fill="#f472b6" font-size="9" font-weight="800" text-anchor="middle">2 Taller</text>
                  ` : ''}
                </g>
              `).join('')}

              <!-- Deduction Step Explanation -->
              <rect x="25" y="125" width="370" height="38" rx="6" fill="#0f172a"/>
              <text x="210" y="148" fill="#f8fafc" font-size="11" font-weight="800" text-anchor="middle">
                ${step === 0 ? 'Clue: Start by placing the tallest student (H=4)...' : step === 1 ? 'Step 1: H=4 must have callout 0. Slot 2 has 0, so H=4 fits at Slot 2!' : step === 2 ? 'Step 2: H=3 has callout 1. One taller ahead (H=4 at Slot 2) ➔ Slot 4!' : step === 3 ? 'Step 3: H=2 has callout 0 ➔ Placed in front at Slot 1!' : 'Solved! Slot 3 is the remaining spot for shortest student H=1!'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="250" width="460" height="68" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="270" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              The Backward Elimination Strategy:
            </text>
            <text x="270" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Always place the tallest elements first, because their callouts depend on nobody else!
            </text>
            <text x="270" y="306" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Every set of callout numbers corresponds to exactly ONE unique ordering.
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">Reset</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">Step 1: Place H=4</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">Step 2: Place H=3</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">Step 3: Place H=2</button>
          <button class="sim-btn ${step === 4 ? 'active' : ''}" data-step="4">Step 4: Place H=1 (Done)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-step]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          step = parseInt(e.target.getAttribute('data-step'));
          simControls.querySelectorAll('button[data-step]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 3: Picking Parity - Visual Pair-Matching
    function simParityPairMatching() {
      simHeaderTitle.textContent = "The Geometry of Parity: Perfect Pairs vs Solitary Dots";
      let n = 9; // 1 to 20

      function render() {
        const isEven = (n % 2 === 0);
        const pairs = Math.floor(n / 2);
        const hasLeftover = (n % 2 !== 0);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Status Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="${isEven ? '#064e3b' : '#78350f'}" stroke="${isEven ? '#10b981' : '#f59e0b'}" stroke-width="2"/>
            <text x="270" y="36" fill="${isEven ? '#34d399' : '#fef08a'}" font-size="14" font-weight="900" text-anchor="middle">
              ${n} is ${isEven ? 'EVEN: Exactly ' + pairs + ' Complete Pairs (0 Remainder)' : 'ODD: ' + pairs + ' Pairs + 1 Lonely Unpaired Dot!'}
            </text>

            <!-- 2-Row Dot Pairing Grid -->
            <g transform="translate(60, 75)">
              <rect x="0" y="0" width="420" height="150" rx="12" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Row 1: Top dots -->
              ${Array.from({ length: pairs }).map((_, i) => `
                <!-- Pair box -->
                <rect x="${25 + i * 36}" y="25" width="28" height="85" rx="6" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Top Dot -->
                <circle cx="${39 + i * 36}" cy="45" r="10" fill="#38bdf8"/>
                <!-- Bottom Dot -->
                <circle cx="${39 + i * 36}" cy="90" r="10" fill="#38bdf8"/>
                <text x="${39 + i * 36}" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Pair ${i + 1}</text>
              `).join('')}

              <!-- Solitary Dot if Odd -->
              ${hasLeftover ? `
                <g transform="translate(${25 + pairs * 36}, 25)">
                  <rect x="0" y="0" width="28" height="85" rx="6" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
                  <circle cx="14" cy="45" r="10" fill="#ef4444"/>
                  <!-- Empty Partner Slot -->
                  <circle cx="14" cy="90" r="10" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="14" y="93" fill="#fca5a5" font-size="8" text-anchor="middle">Empty</text>
                  <text x="14" y="125" fill="#f87171" font-size="9" font-weight="900" text-anchor="middle">+1</text>
                </g>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="240" width="460" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Formal Algebraic Definitions of Parity:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              ${isEven ? `Even Number: ${n} = 2 × ${pairs} ➔ General form is 2k (Divisible by 2)` : `Odd Number: ${n} = 2 × ${pairs} + 1 ➔ General form is 2k + 1 (Remainder 1)`}
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Slide the controller below to observe how every number alternates between Even and Odd!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Test Number (n):</span>
          <input type="range" id="paritySlider" min="1" max="20" value="${n}" style="width:200px; accent-color:#38bdf8; cursor:pointer;">
          <span id="parityVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">${n}</span>
          <button class="sim-btn" id="randParityBtn">🎲 Random Number</button>
        </div>
      `;

      const slider = simControls.querySelector('#paritySlider');
      slider.addEventListener('input', (e) => {
        n = parseInt(e.target.value);
        simControls.querySelector('#parityVal').textContent = n;
        render();
      });

      simControls.querySelector('#randParityBtn').addEventListener('click', () => {
        n = Math.floor(Math.random() * 20) + 1;
        slider.value = n;
        simControls.querySelector('#parityVal').textContent = n;
        render();
      });

      render();
    }

    // Slide 4: Parity Arithmetic Laws
    function simParityArithmeticMatrix() {
      simHeaderTitle.textContent = "Parity Arithmetic: Why Odd + Odd Always Equals Even";
      let opType = 'odd_odd'; // 'even_even', 'odd_odd', 'even_odd'

      function render() {
        let titleText = "Odd + Odd = Even (Two Lonely Dots Combine into a Pair!)";
        let num1 = 5, num2 = 3;
        let sum = 8;
        let isResultEven = true;

        if (opType === 'even_even') {
          titleText = "Even + Even = Even (Both sets already paired; 0 leftovers!)";
          num1 = 4; num2 = 6; sum = 10; isResultEven = true;
        } else if (opType === 'even_odd') {
          titleText = "Even + Odd = Odd (One lonely dot remains without a partner!)";
          num1 = 4; num2 = 5; sum = 9; isResultEven = false;
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${titleText}
            </text>

            <!-- Visual Equation Cards -->
            <g transform="translate(40, 65)">
              <!-- Term 1 Card -->
              <rect x="0" y="0" width="130" height="150" rx="10" fill="#111827" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="65" y="24" fill="#38bdf8" font-size="12" font-weight="900" text-anchor="middle">
                ${num1 % 2 === 0 ? 'EVEN' : 'ODD'} (${num1})
              </text>
              <g transform="translate(15, 40)">
                ${Array.from({ length: Math.floor(num1 / 2) }).map((_, i) => `
                  <circle cx="20" cy="${i * 22 + 10}" r="7" fill="#38bdf8"/>
                  <circle cx="45" cy="${i * 22 + 10}" r="7" fill="#38bdf8"/>
                `).join('')}
                ${num1 % 2 !== 0 ? `
                  <circle cx="20" cy="${Math.floor(num1 / 2) * 22 + 10}" r="7" fill="#ef4444"/>
                  <text x="65" y="${Math.floor(num1 / 2) * 22 + 14}" fill="#ef4444" font-size="10" font-weight="800">Lonely!</text>
                ` : ''}
              </g>

              <!-- Plus Sign -->
              <text x="155" y="80" fill="#fbbf24" font-size="28" font-weight="900" text-anchor="middle">+</text>

              <!-- Term 2 Card -->
              <rect x="180" y="0" width="130" height="150" rx="10" fill="#111827" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="245" y="24" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">
                ${num2 % 2 === 0 ? 'EVEN' : 'ODD'} (${num2})
              </text>
              <g transform="translate(195, 40)">
                ${Array.from({ length: Math.floor(num2 / 2) }).map((_, i) => `
                  <circle cx="20" cy="${i * 22 + 10}" r="7" fill="#fbbf24"/>
                  <circle cx="45" cy="${i * 22 + 10}" r="7" fill="#fbbf24"/>
                `).join('')}
                ${num2 % 2 !== 0 ? `
                  <circle cx="20" cy="${Math.floor(num2 / 2) * 22 + 10}" r="7" fill="#ef4444"/>
                  <text x="65" y="${Math.floor(num2 / 2) * 22 + 14}" fill="#ef4444" font-size="10" font-weight="800">Lonely!</text>
                ` : ''}
              </g>

              <!-- Equals Sign -->
              <text x="335" y="80" fill="#10b981" font-size="28" font-weight="900" text-anchor="middle">=</text>

              <!-- Result Card -->
              <rect x="360" y="0" width="100" height="150" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
              <text x="410" y="24" fill="#a7f3d0" font-size="11" font-weight="900" text-anchor="middle">SUM: ${sum}</text>
              <text x="410" y="55" fill="#ffffff" font-size="20" font-weight="900" text-anchor="middle">
                ${isResultEven ? 'EVEN' : 'ODD'}
              </text>
              <text x="410" y="85" fill="#6ee7b7" font-size="10" text-anchor="middle">
                ${opType === 'odd_odd' ? '2 Lonely dots joined into 1 pair!' : opType === 'even_even' ? 'All dots paired!' : '1 Dot remains lonely!'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Universal Parity Arithmetic Table:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              • Even + Even = Even &nbsp;|&nbsp; • Odd + Odd = Even &nbsp;|&nbsp; • Even + Odd = Odd
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              • Odd × Odd = Odd &nbsp;|&nbsp; • Even × Any Integer = ALWAYS Even!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.8rem; flex-wrap:wrap;">
          <button class="sim-btn ${opType === 'odd_odd' ? 'active' : ''}" data-op="odd_odd">Odd + Odd = Even (5 + 3 = 8)</button>
          <button class="sim-btn ${opType === 'even_even' ? 'active' : ''}" data-op="even_even">Even + Even = Even (4 + 6 = 10)</button>
          <button class="sim-btn ${opType === 'even_odd' ? 'active' : ''}" data-op="even_odd">Even + Odd = Odd (4 + 5 = 9)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-op]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          opType = e.target.getAttribute('data-op');
          simControls.querySelectorAll('button[data-op]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 5: Parity in Grids & Chessboard Tiling
    function simGridSquaresParity() {
      simHeaderTitle.textContent = "Grid Parity: Checkerboard Coloring & The Mutilated Board";
      let cornersRemoved = false;

      function render() {
        const whiteCount = cornersRemoved ? 30 : 32;
        const blackCount = 32;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${cornersRemoved ? 'Mutilated Board: 30 White & 32 Black Squares ➔ Tiling is IMPOSSIBLE!' : 'Complete 8×8 Chessboard: 32 White & 32 Black Squares (32 Dominoes Fit)'}
            </text>

            <!-- 8x8 Chessboard Grid -->
            <g transform="translate(60, 60)">
              ${Array.from({ length: 8 }).map((_, r) => {
                return Array.from({ length: 8 }).map((_, c) => {
                  const isWhite = (r + c) % 2 === 0;
                  // check if opposite white corners: (0,0) and (7,7)
                  const isRemoved = cornersRemoved && ((r === 0 && c === 0) || (r === 7 && c === 7));
                  if (isRemoved) {
                    return `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="#ef4444" stroke="#475569" stroke-width="0.5"/>
                            <text x="${c * 20 + 10}" y="${r * 20 + 14}" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">✕</text>`;
                  }
                  return `<rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="${isWhite ? '#f8fafc' : '#334155'}" stroke="#475569" stroke-width="0.5"/>`;
                }).join('');
              }).join('')}
            </g>

            <!-- Domino Card & Statistics -->
            <g transform="translate(260, 60)">
              <rect x="0" y="0" width="220" height="160" rx="10" fill="#111827" stroke="${cornersRemoved ? '#ef4444' : '#10b981'}" stroke-width="2"/>
              <text x="110" y="24" fill="${cornersRemoved ? '#fca5a5' : '#a7f3d0'}" font-size="12" font-weight="900" text-anchor="middle">COLOR PARITY BALANCE</text>

              <!-- Domino sample -->
              <g transform="translate(45, 38)">
                <rect x="0" y="0" width="60" height="26" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <rect x="0" y="0" width="30" height="26" fill="#f8fafc"/>
                <rect x="30" y="0" width="30" height="26" fill="#334155"/>
                <text x="65" y="18" fill="#cbd5e1" font-size="10">1 Domino</text>
              </g>

              <g transform="translate(20, 80)">
                <text x="0" y="16" fill="#cbd5e1" font-size="11">White Squares: <tspan fill="#f8fafc" font-weight="bold">${whiteCount}</tspan></text>
                <text x="0" y="34" fill="#cbd5e1" font-size="11">Black Squares: <tspan fill="#94a3b8" font-weight="bold">${blackCount}</tspan></text>
                <text x="0" y="52" fill="#cbd5e1" font-size="11">Total Squares: <tspan fill="#38bdf8" font-weight="bold">${whiteCount + blackCount}</tspan></text>
                <text x="0" y="70" fill="${cornersRemoved ? '#ef4444' : '#10b981'}" font-size="11" font-weight="900">
                  ${cornersRemoved ? 'IMBALANCE: 30 ≠ 32!' : 'BALANCED: 32 = 32'}
                </text>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Power of Parity Invariants:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Every single 2×1 domino MUST cover exactly 1 white and 1 black square.
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Since 31 dominoes need 31 whites and 31 blacks, 30 whites can NEVER be covered!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn ${!cornersRemoved ? 'active' : ''}" id="fullBoardBtn">Standard 8×8 Board (64 Sq)</button>
          <button class="sim-btn ${cornersRemoved ? 'active' : ''}" id="cutCornersBtn">Cut 2 Opposite Corners (62 Sq)</button>
        </div>
      `;

      simControls.querySelector('#fullBoardBtn').addEventListener('click', () => {
        cornersRemoved = false;
        render();
      });

      simControls.querySelector('#cutCornersBtn').addEventListener('click', () => {
        cornersRemoved = true;
        render();
      });

      render();
    }

    // Slide 6: Algebraic Parity & Collatz 3n+1
    function simAlgebraicParityNthTerm() {
      simHeaderTitle.textContent = "Algebraic Parity & The Famous Collatz 3n + 1 Loop";
      let startNum = 7;

      function getCollatzSequence(start) {
        let seq = [start];
        let cur = start;
        while (cur !== 1 && seq.length < 18) {
          if (cur % 2 === 0) cur = cur / 2;
          else cur = 3 * cur + 1;
          seq.push(cur);
        }
        return seq;
      }

      function render() {
        const seq = getCollatzSequence(startNum);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Collatz Rules: If Even ➔ n/2 &nbsp;|&nbsp; If Odd ➔ 3n + 1 (Start at ${startNum})
            </text>

            <!-- Sequence Stepping Blocks -->
            <g transform="translate(30, 65)">
              <rect x="0" y="0" width="480" height="155" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <g transform="translate(15, 20)">
                ${seq.slice(0, 16).map((num, i) => {
                  const x = (i % 8) * 56;
                  const y = Math.floor(i / 8) * 60;
                  const isEven = (num % 2 === 0);

                  return `
                    <g transform="translate(${x}, ${y})">
                      <rect x="0" y="0" width="50" height="42" rx="6" fill="${isEven ? '#0284c7' : '#d97706'}" stroke="${isEven ? '#38bdf8' : '#fbbf24'}" stroke-width="1.5"/>
                      <text x="25" y="24" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${num}</text>
                      <text x="25" y="36" fill="${isEven ? '#bae6fd' : '#fef08a'}" font-size="8" font-weight="700" text-anchor="middle">${isEven ? 'EVEN' : 'ODD'}</text>
                    </g>
                  `;
                }).join('')}
              </g>

              <text x="240" y="145" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">
                Notice: All numbers eventually plummet into the eternal loop: 4 ➔ 2 ➔ 1!
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="235" width="460" height="80" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="258" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Parity Shifts in 3n + 1:
            </text>
            <text x="270" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">
              When n is odd, 3n is odd, so 3n + 1 is GUARANTEED to be even!
            </text>
            <text x="270" y="298" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Every odd jump is immediately followed by at least one division by 2.
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Choose Starting Number:</span>
          <input type="range" id="collatzSlider" min="2" max="25" value="${startNum}" style="width:160px; accent-color:#38bdf8; cursor:pointer;">
          <span id="collatzVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">${startNum}</span>
          <button class="sim-btn" data-start="7">Try 7</button>
          <button class="sim-btn" data-start="9">Try 9</button>
          <button class="sim-btn" data-start="12">Try 12</button>
        </div>
      `;

      const slider = simControls.querySelector('#collatzSlider');
      slider.addEventListener('input', (e) => {
        startNum = parseInt(e.target.value);
        simControls.querySelector('#collatzVal').textContent = startNum;
        render();
      });

      simControls.querySelectorAll('button[data-start]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          startNum = parseInt(e.target.getAttribute('data-start'));
          slider.value = startNum;
          simControls.querySelector('#collatzVal').textContent = startNum;
          render();
        });
      });

      render();
    }

    // Slide 7: Explorations in Grids - Magic Square Basics
    function simMagicSquare3x3() {
      simHeaderTitle.textContent = "Magic Squares: The Harmonious 3 × 3 Grid with Sum = 15";
      // Standard Lo Shu grid
      const grid = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
      ];

      function render() {
        const rowSums = grid.map(r => r.reduce((a, b) => a + b, 0));
        const colSums = [0, 1, 2].map(c => grid[0][c] + grid[1][c] + grid[2][c]);
        const diag1 = grid[0][0] + grid[1][1] + grid[2][2];
        const diag2 = grid[0][2] + grid[1][1] + grid[2][0];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              Magic Constant S = 15 &nbsp;|&nbsp; Every Row, Column & Diagonal = 15!
            </text>

            <!-- 3x3 Magic Square Canvas -->
            <g transform="translate(150, 65)">
              <!-- Outer Border -->
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

              ${grid.map((row, r) => row.map((val, c) => `
                <rect x="${c * 60}" y="${r * 60}" width="60" height="60" fill="${val === 5 ? '#0284c7' : '#111827'}" stroke="#334155" stroke-width="1.5"/>
                <text x="${c * 60 + 30}" y="${r * 60 + 38}" fill="${val === 5 ? '#ffffff' : '#f8fafc'}" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              `).join('')).join('')}

              <!-- Row Sum Indicators on Right -->
              ${rowSums.map((sum, r) => `
                <text x="195" y="${r * 60 + 38}" fill="#10b981" font-size="13" font-weight="900">➔ ${sum}</text>
              `).join('')}

              <!-- Column Sum Indicators Below -->
              ${colSums.map((sum, c) => `
                <text x="${c * 60 + 30}" y="205" fill="#10b981" font-size="13" font-weight="900" text-anchor="middle">↓ ${sum}</text>
              `).join('')}

              <!-- Diagonal indicators -->
              <text x="-25" y="-8" fill="#fbbf24" font-size="12" font-weight="900">↘ ${diag1}</text>
              <text x="205" y="-8" fill="#fbbf24" font-size="12" font-weight="900">↙ ${diag2}</text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="260" width="460" height="58" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="280" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Total Sum of Digits 1 to 9 = 45 ➔ 45 ÷ 3 Rows = 15 per Line!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Notice: Even numbers (2, 4, 6, 8) sit in the corners; Odd numbers (1, 3, 7, 9) sit on the edges!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn active" id="inspectLoShuBtn">Standard Lo Shu Square (Digits 1–9)</button>
        </div>
      `;

      render();
    }

    // Slide 8: The Center Cell Rule & Structural Symmetry
    function simMagicSquareCenterRule() {
      simHeaderTitle.textContent = "The Center Cell Rule: Why the Center is ALWAYS S / 3 = 5";
      let rotation = 0; // 0, 90, 180, 270

      function getRotatedGrid(deg) {
        if (deg === 90) return [[8, 3, 4], [1, 5, 9], [6, 7, 2]];
        if (deg === 180) return [[6, 1, 8], [7, 5, 3], [2, 9, 4]];
        if (deg === 270) return [[2, 7, 6], [9, 5, 1], [4, 3, 8]];
        return [[4, 9, 2], [3, 5, 7], [8, 1, 6]];
      }

      function render() {
        const curGrid = getRotatedGrid(rotation);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Center Cell Theorem: Center = Magic Sum / 3 = 15 / 3 = 5 (Rotation: ${rotation}°)
            </text>

            <!-- 3x3 Grid Display -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#111827" stroke="#38bdf8" stroke-width="2"/>

              ${curGrid.map((row, r) => row.map((val, c) => `
                <rect x="${c * 60}" y="${r * 60}" width="60" height="60" fill="${val === 5 ? '#0284c7' : '#1e293b'}" stroke="#334155" stroke-width="1.5"/>
                <text x="${c * 60 + 30}" y="${r * 60 + 38}" fill="${val === 5 ? '#ffffff' : '#f8fafc'}" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              `).join('')).join('')}
            </g>

            <!-- Mathematical Proof Diagram Card on Right -->
            <g transform="translate(260, 65)">
              <rect x="0" y="0" width="220" height="180" rx="10" fill="#111827" stroke="#10b981" stroke-width="1.5"/>
              <text x="110" y="24" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">THE 4-LINE CENTER HUB</text>

              <g transform="translate(15, 36)">
                <text x="0" y="18" fill="#cbd5e1" font-size="10.5">4 Lines pass through center (C):</text>
                <text x="0" y="34" fill="#38bdf8" font-size="10.5">• Row 2 &nbsp;• Col 2 &nbsp;• 2 Diagonals</text>
                <text x="0" y="52" fill="#fbbf24" font-size="10.5">Sum of 4 lines = 4 × 15 = 60</text>
                <text x="0" y="70" fill="#cbd5e1" font-size="10">All 9 cells + 3C = 60</text>
                <text x="0" y="88" fill="#cbd5e1" font-size="10">45 + 3C = 60</text>
                <text x="0" y="108" fill="#10b981" font-size="13" font-weight="900">3C = 15 ➔ C = 5!</text>
              </g>

              <text x="110" y="165" fill="#bae6fd" font-size="10" font-weight="800" text-anchor="middle">
                Center is unshakeable under all rotations!
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="260" width="460" height="58" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="280" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Complementary Pairs with 5:
            </text>
            <text x="270" y="298" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1+9 = 10, 2+8 = 10, 3+7 = 10, 4+6 = 10. Opposites across the center always add up to 10!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${rotation === 0 ? 'active' : ''}" data-rot="0">Rotation: 0°</button>
          <button class="sim-btn ${rotation === 90 ? 'active' : ''}" data-rot="90">Rotate 90°</button>
          <button class="sim-btn ${rotation === 180 ? 'active' : ''}" data-rot="180">Rotate 180°</button>
          <button class="sim-btn ${rotation === 270 ? 'active' : ''}" data-rot="270">Rotate 270°</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-rot]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          rotation = parseInt(e.target.getAttribute('data-rot'));
          simControls.querySelectorAll('button[data-rot]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 9: The Chautīsa Yantra (4x4 Magic Square)
    function simChautisaYantra4x4() {
      simHeaderTitle.textContent = "The Chautīsa Yantra: Khajuraho's 4 × 4 Masterwork of 34";
      let activeHighlight = 'corners'; // 'corners', 'center', 'diagonals', 'quadrants'

      const yantra = [
        [7, 12, 1, 14],
        [2, 13, 8, 11],
        [16, 3, 10, 5],
        [9, 6, 15, 4]
      ];

      function isHighlighted(r, c) {
        if (activeHighlight === 'corners') {
          return (r === 0 || r === 3) && (c === 0 || c === 3);
        }
        if (activeHighlight === 'center') {
          return (r === 1 || r === 2) && (c === 1 || c === 2);
        }
        if (activeHighlight === 'diagonals') {
          return (r === c) || (r + c === 3);
        }
        if (activeHighlight === 'quadrants') {
          return (r < 2 && c < 2); // top-left quadrant sample
        }
        return false;
      }

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="270" y="36" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">
              Khajuraho Temple Inscription (c. 10th Century CE) • Magic Constant = 34
            </text>

            <!-- 4x4 Yantra Grid Canvas -->
            <g transform="translate(70, 60)">
              <rect x="0" y="0" width="180" height="180" rx="8" fill="#111827" stroke="#f59e0b" stroke-width="2"/>

              ${yantra.map((row, r) => row.map((val, c) => {
                const hl = isHighlighted(r, c);
                return `
                  <rect x="${c * 45}" y="${r * 45}" width="45" height="45" fill="${hl ? '#b45309' : '#1e293b'}" stroke="#334155" stroke-width="1.5"/>
                  <text x="${c * 45 + 22.5}" y="${r * 45 + 29}" fill="${hl ? '#fef08a' : '#f8fafc'}" font-size="16" font-weight="900" text-anchor="middle">${val}</text>
                `;
              }).join('')).join('')}
            </g>

            <!-- Symmetry Explanation Card -->
            <g transform="translate(270, 60)">
              <rect x="0" y="0" width="220" height="180" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
              <text x="110" y="24" fill="#a5b4fc" font-size="12" font-weight="900" text-anchor="middle">ACTIVE 34 PATTERN</text>

              <g transform="translate(15, 36)">
                ${activeHighlight === 'corners' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">The 4 Corner Cells:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 14 + 9 + 4 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">Even the outer boundary corners balance to 34!</text>
                ` : activeHighlight === 'center' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">The 4 Center Cells:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">13 + 8 + 3 + 10 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">The central 2×2 hub balances to 34!</text>
                ` : activeHighlight === 'diagonals' ? `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">Both Main Diagonals:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 13 + 10 + 4 = 34</text>
                  <text x="0" y="58" fill="#ffffff" font-size="14" font-weight="900">14 + 8 + 3 + 9 = 34</text>
                ` : `
                  <text x="0" y="18" fill="#fef08a" font-size="12" font-weight="800">Each 2×2 Quadrant:</text>
                  <text x="0" y="38" fill="#ffffff" font-size="14" font-weight="900">7 + 12 + 2 + 13 = 34</text>
                  <text x="0" y="60" fill="#cbd5e1" font-size="10">Every 2×2 corner block sums to 34!</text>
                `}
              </g>

              <text x="110" y="165" fill="#fef08a" font-size="10" font-weight="800" text-anchor="middle">
                Total sum of 1 to 16 = 136 = 4 × 34
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="255" width="480" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="274" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Pandiagonal Perfection:
            </text>
            <text x="270" y="293" fill="#cbd5e1" font-size="11" text-anchor="middle">
              In this grid, there are over 16 DIFFERENT sub-combinations of 4 numbers that sum to 34!
            </text>
            <text x="270" y="309" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click the buttons below to illuminate each magical pattern!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${activeHighlight === 'corners' ? 'active' : ''}" data-hl="corners">4 Corners (34)</button>
          <button class="sim-btn ${activeHighlight === 'center' ? 'active' : ''}" data-hl="center">4 Center Cells (34)</button>
          <button class="sim-btn ${activeHighlight === 'diagonals' ? 'active' : ''}" data-hl="diagonals">2 Diagonals (34)</button>
          <button class="sim-btn ${activeHighlight === 'quadrants' ? 'active' : ''}" data-hl="quadrants">2×2 Quadrant (34)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-hl]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activeHighlight = e.target.getAttribute('data-hl');
          simControls.querySelectorAll('button[data-hl]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 10: Virahāńka-Fibonacci - Poetic Syllable Origins
    function simVirahankaPoeticMeter() {
      simHeaderTitle.textContent = "Poetic Prosody Origins: Pingala & Virahāńka's Syllable Beats";
      let beats = 4; // 1 to 5

      const patterns = {
        1: [["L"]],
        2: [["L", "L"], ["G"]],
        3: [["L", "L", "L"], ["L", "G"], ["G", "L"]],
        4: [["L", "L", "L", "L"], ["L", "L", "G"], ["L", "G", "L"], ["G", "L", "L"], ["G", "G"]],
        5: [
          ["L","L","L","L","L"], ["L","L","L","G"], ["L","L","G","L"], ["L","G","L","L"],
          ["G","L","L","L"], ["L","G","G"], ["G","L","G"], ["G","G","L"]
        ]
      };

      function render() {
        const list = patterns[beats] || patterns[4];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Virahāńka Prosody: Beats = ${beats} ➔ Exactly ${list.length} Combinations! (F_${beats} = ${list.length})
            </text>

            <!-- Syllable Blocks Display -->
            <g transform="translate(40, 65)">
              <rect x="0" y="0" width="460" height="165" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Legend -->
              <g transform="translate(20, 15)">
                <rect x="0" y="0" width="30" height="18" rx="3" fill="#0284c7"/>
                <text x="15" y="13" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">L</text>
                <text x="36" y="13" fill="#cbd5e1" font-size="10">Laghu (Short = 1 beat)</text>

                <rect x="180" y="0" width="45" height="18" rx="3" fill="#d97706"/>
                <text x="202" y="13" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">G</text>
                <text x="232" y="13" fill="#cbd5e1" font-size="10">Guru (Long = 2 beats)</text>
              </g>

              <!-- Combinations Grid -->
              <g transform="translate(20, 45)">
                ${list.map((comb, idx) => {
                  const x = (idx % 4) * 110;
                  const y = Math.floor(idx / 4) * 50;

                  return `
                    <g transform="translate(${x}, ${y})">
                      <rect x="0" y="0" width="100" height="36" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                      <text x="8" y="22" fill="#94a3b8" font-size="10" font-weight="700">${idx + 1}.</text>
                      <g transform="translate(24, 8)">
                        ${comb.map((s, si) => `
                          <rect x="${si * 22}" y="0" width="${s === 'L' ? 18 : 20}" height="20" rx="3" fill="${s === 'L' ? '#0284c7' : '#d97706'}"/>
                          <text x="${si * 22 + (s === 'L' ? 9 : 10)}" y="14" fill="#ffffff" font-size="10" font-weight="900" text-anchor="middle">${s}</text>
                        `).join('')}
                      </g>
                    </g>
                  `;
                }).join('')}
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Recurrence Origin (c. 700 CE):
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              To form n beats: End with a Laghu (needs n-1 beats) OR end with a Guru (needs n-2 beats).
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Therefore: Ways(n) = Ways(n-1) + Ways(n-2) ➔ The sequence 1, 2, 3, 5, 8, 13 is born!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${beats === 1 ? 'active' : ''}" data-beats="1">1 Beat (1 way)</button>
          <button class="sim-btn ${beats === 2 ? 'active' : ''}" data-beats="2">2 Beats (2 ways)</button>
          <button class="sim-btn ${beats === 3 ? 'active' : ''}" data-beats="3">3 Beats (3 ways)</button>
          <button class="sim-btn ${beats === 4 ? 'active' : ''}" data-beats="4">4 Beats (5 ways)</button>
          <button class="sim-btn ${beats === 5 ? 'active' : ''}" data-beats="5">5 Beats (8 ways)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-beats]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          beats = parseInt(e.target.getAttribute('data-beats'));
          simControls.querySelectorAll('button[data-beats]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 11: The Recurrence Machine & Golden Ratio
    function simFibonacciVirahankaSequence() {
      simHeaderTitle.textContent = "The Additive Machine: Virahāńka Sequence & Golden Ratio";
      let nTerm = 7;

      const seq = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377];

      function render() {
        const val = seq[nTerm - 1];
        const prevVal = seq[nTerm - 2];
        const ratio = (val / prevVal).toFixed(5);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              F_${nTerm} = ${val} &nbsp;|&nbsp; Ratio F_${nTerm} / F_${nTerm - 1} = ${val} / ${prevVal} = ${ratio}
            </text>

            <!-- Recurrence Stepper Display -->
            <g transform="translate(40, 65)">
              <rect x="0" y="0" width="460" height="160" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Preceding Two Terms Adder -->
              <g transform="translate(40, 25)">
                <rect x="0" y="0" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="50" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">F_${nTerm - 2}</text>
                <text x="50" y="44" fill="#38bdf8" font-size="18" font-weight="900" text-anchor="middle">${seq[nTerm - 3] || 1}</text>

                <text x="125" y="35" fill="#f59e0b" font-size="24" font-weight="900" text-anchor="middle">+</text>

                <rect x="150" y="0" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="200" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">F_${nTerm - 1}</text>
                <text x="200" y="44" fill="#38bdf8" font-size="18" font-weight="900" text-anchor="middle">${prevVal}</text>

                <text x="275" y="35" fill="#10b981" font-size="24" font-weight="900" text-anchor="middle">=</text>

                <rect x="300" y="0" width="100" height="55" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                <text x="350" y="20" fill="#a7f3d0" font-size="10" text-anchor="middle">F_${nTerm}</text>
                <text x="350" y="44" fill="#ffffff" font-size="22" font-weight="900" text-anchor="middle">${val}</text>
              </g>

              <!-- Golden Ratio Meter -->
              <g transform="translate(40, 105)">
                <text x="0" y="16" fill="#cbd5e1" font-size="11" font-weight="700">Golden Ratio Convergence:</text>
                <text x="220" y="16" fill="#fbbf24" font-size="13" font-weight="900">Φ ≈ 1.618033...</text>
                <rect x="0" y="25" width="380" height="14" rx="7" fill="#1e293b"/>
                <rect x="0" y="25" width="${Math.min(380, (parseFloat(ratio) / 2) * 380)}" height="14" rx="7" fill="#10b981"/>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              The Recurrence Formula: F_n = F_{n-1} + F_{n-2}
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              As you calculate larger and larger terms, the ratio of successive numbers locks onto 1.618!
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Use the slider below to step through higher terms and watch the ratio stabilize!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Term Number (n):</span>
          <input type="range" id="fibSlider" min="3" max="12" value="${nTerm}" style="width:180px; accent-color:#38bdf8; cursor:pointer;">
          <span id="fibVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">n = ${nTerm}</span>
        </div>
      `;

      const slider = simControls.querySelector('#fibSlider');
      slider.addEventListener('input', (e) => {
        nTerm = parseInt(e.target.value);
        simControls.querySelector('#fibVal').textContent = `n = ${nTerm}`;
        render();
      });

      render();
    }

    // Slide 12: Nature's Spirals & Petals
    function simNaturePetalsSpirals() {
      simHeaderTitle.textContent = "Botanical Gallery: Flower Petal Counts & Sunflower Spirals";
      let activeItem = 'buttercup'; // 'lily', 'buttercup', 'delphinium', 'sunflower'

      const flowers = {
        lily: { name: "Lily / Iris", petals: 3, virahankaIndex: "F_3", desc: "Lilies exhibit 3-fold floral symmetry with exactly 3 petals." },
        buttercup: { name: "Wild Buttercup", petals: 5, virahankaIndex: "F_4", desc: "Buttercups and wild roses almost universally feature 5 golden petals." },
        delphinium: { name: "Delphinium", petals: 8, virahankaIndex: "F_5", desc: "Delphiniums proudly display 8 distinct blooming petals." },
        sunflower: { name: "Sunflower Head", petals: "21 & 34 Spirals", virahankaIndex: "F_7 & F_8", desc: "Interlocking clockwise (21) and counter-clockwise (34) seed spirals pack with 100% space efficiency!" }
      };

      function render() {
        const item = flowers[activeItem];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">
              ${item.name} ➔ ${item.petals} Petals (${item.virahankaIndex})
            </text>

            <!-- Flower Illustration Display Area -->
            <g transform="translate(60, 60)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Central Flower Canvas -->
              <g transform="translate(140, 85)">
                ${activeItem === 'lily' ? `
                  <!-- 3 Petals at 120 deg -->
                  ${[0, 120, 240].map(deg => `
                    <ellipse cx="0" cy="-35" rx="16" ry="32" fill="#38bdf8" opacity="0.85" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#fbbf24"/>
                ` : activeItem === 'buttercup' ? `
                  <!-- 5 Petals at 72 deg -->
                  ${[0, 72, 144, 216, 288].map(deg => `
                    <ellipse cx="0" cy="-35" rx="18" ry="30" fill="#fbbf24" opacity="0.9" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#f59e0b"/>
                ` : activeItem === 'delphinium' ? `
                  <!-- 8 Petals at 45 deg -->
                  ${[0, 45, 90, 135, 180, 225, 270, 315].map(deg => `
                    <ellipse cx="0" cy="-35" rx="14" ry="28" fill="#818cf8" opacity="0.85" transform="rotate(${deg})"/>
                  `).join('')}
                  <circle cx="0" cy="0" r="14" fill="#fbbf24"/>
                ` : `
                  <!-- Sunflower Spirals -->
                  <circle cx="0" cy="0" r="55" fill="#78350f"/>
                  ${Array.from({ length: 45 }).map((_, i) => {
                    const r = 8 + i * 1.0;
                    const theta = i * 2.39996; // golden angle
                    return `<circle cx="${r * Math.cos(theta)}" cy="${r * Math.sin(theta)}" r="2.5" fill="#fef08a"/>`;
                  }).join('')}
                `}
              </g>

              <!-- Description Box on Right -->
              <g transform="translate(230, 25)">
                <rect x="0" y="0" width="170" height="125" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <text x="85" y="24" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">${item.name}</text>
                <foreignObject x="12" y="32" width="146" height="85">
                  <div xmlns="http://www.w3.org/1999/xhtml" style="color:#cbd5e1; font-size:10.5px; line-height:1.35; text-align:center;">
                    ${item.desc}
                  </div>
                </foreignObject>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              Nature's Mathematical Optimization:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              By rotating each new seed or leaf by the Golden Angle (137.5°), plants avoid overlapping.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              This optimal packing geometry directly generates the Virahāńka sequence in nature!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${activeItem === 'lily' ? 'active' : ''}" data-flower="lily">Lily (3 Petals)</button>
          <button class="sim-btn ${activeItem === 'buttercup' ? 'active' : ''}" data-flower="buttercup">Buttercup (5 Petals)</button>
          <button class="sim-btn ${activeItem === 'delphinium' ? 'active' : ''}" data-flower="delphinium">Delphinium (8 Petals)</button>
          <button class="sim-btn ${activeItem === 'sunflower' ? 'active' : ''}" data-flower="sunflower">Sunflower (21 & 34 Spirals)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-flower]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          activeItem = e.target.getAttribute('data-flower');
          simControls.querySelectorAll('button[data-flower]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 13: Virahāńka Sequence Parity Cycle
    function simVirahankaParityCycle() {
      simHeaderTitle.textContent = "The Parity Rhythm: Why Every 3rd Virahāńka Number is Even";
      let testIndex = 9;

      const seq = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233];

      function render() {
        const val = seq[testIndex - 1];
        const isEven = (val % 2 === 0);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Repeating Period-3 Parity Pattern: [ Odd, Odd, Even ] Forever!
            </text>

            <!-- 12-Term Parity Ribbon -->
            <g transform="translate(30, 65)">
              <rect x="0" y="0" width="480" height="160" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <g transform="translate(10, 20)">
                ${seq.map((num, i) => {
                  const ev = (num % 2 === 0);
                  const isSel = (i + 1 === testIndex);
                  const x = i * 38;

                  return `
                    <g transform="translate(${x}, 0)">
                      <rect x="0" y="0" width="34" height="60" rx="6" fill="${ev ? '#0284c7' : '#d97706'}" stroke="${isSel ? '#ffffff' : '#475569'}" stroke-width="${isSel ? 2.5 : 1}"/>
                      <text x="17" y="16" fill="#ffffff" font-size="9" text-anchor="middle">n=${i + 1}</text>
                      <text x="17" y="36" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">${num}</text>
                      <text x="17" y="52" fill="${ev ? '#bae6fd' : '#fef08a'}" font-size="8" font-weight="800" text-anchor="middle">${ev ? 'E' : 'O'}</text>
                    </g>
                  `;
                }).join('')}
              </g>

              <!-- Inspector Card -->
              <rect x="30" y="95" width="420" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
              <text x="240" y="116" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">
                Selected Term F_${testIndex} = ${val} ➔ Parity is <tspan fill="${isEven ? '#38bdf8' : '#fbbf24'}" font-weight="bold">${isEven ? 'EVEN' : 'ODD'}</tspan>
              </text>
              <text x="240" y="134" fill="#94a3b8" font-size="10.5" text-anchor="middle">
                Index ${testIndex} ${testIndex % 3 === 0 ? 'IS a multiple of 3 ➔ GUARANTEED EVEN!' : 'is NOT a multiple of 3 ➔ ODD'}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="240" width="480" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">
              Why Every 3rd Term is Even:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Odd + Even = Odd ➔ Even + Odd = Odd ➔ Odd + Odd = EVEN!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Therefore, F_30, F_60, and F_3000 are all guaranteed to be even numbers!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:center; gap:1.2rem; flex-wrap:wrap;">
          <span style="font-weight:700; color:#cbd5e1; font-size:0.9rem;">Inspect Term (n):</span>
          <input type="range" id="cycleSlider" min="1" max="12" value="${testIndex}" style="width:180px; accent-color:#38bdf8; cursor:pointer;">
          <span id="cycleVal" style="color:#38bdf8; font-weight:800; font-size:1.1rem; min-width:30px;">n = ${testIndex}</span>
        </div>
      `;

      const slider = simControls.querySelector('#cycleSlider');
      slider.addEventListener('input', (e) => {
        testIndex = parseInt(e.target.value);
        simControls.querySelector('#cycleVal').textContent = `n = ${testIndex}`;
        render();
      });

      render();
    }

    // Slide 14: Digits in Disguise - Cryptarithm Warmup
    function simCryptarithmSingleDigit() {
      simHeaderTitle.textContent = "Cryptarithm Detective: Unmasking AB + B = BC";
      let bVal = 8; // try B = 6, 7, 8, 9

      function render() {
        // A = B - 1 (since carry is 1)
        const aVal = bVal - 1;
        const ab = aVal * 10 + bVal;
        const sum = ab + bVal;
        const cVal = sum % 10;
        const resultBC = bVal * 10 + cVal;

        // check uniqueness: A, B, C distinct
        const isDistinct = (aVal !== bVal) && (bVal !== cVal) && (aVal !== cVal);
        const isValid = isDistinct && (sum === resultBC);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="40" y="12" width="460" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${isValid ? '✔ SOLUTION FOUND: 78 + 8 = 86 (A=7, B=8, C=6 Distinct!)' : `Testing B = ${bVal} ➔ ${ab} + ${bVal} = ${sum} (Check Distinctness)`}
            </text>

            <!-- Column Addition Card -->
            <g transform="translate(100, 60)">
              <rect x="0" y="0" width="340" height="175" rx="10" fill="#111827" stroke="${isValid ? '#10b981' : '#f59e0b'}" stroke-width="2"/>

              <!-- Letters Addition -->
              <g transform="translate(40, 25)">
                <text x="80" y="30" fill="#38bdf8" font-size="28" font-weight="900">A B</text>
                <text x="50" y="65" fill="#f59e0b" font-size="24" font-weight="900">+</text>
                <text x="100" y="65" fill="#f59e0b" font-size="28" font-weight="900">B</text>
                <line x1="40" y1="78" x2="135" y2="78" stroke="#ffffff" stroke-width="2.5"/>
                <text x="80" y="110" fill="#10b981" font-size="28" font-weight="900">B C</text>
              </g>

              <!-- Values Evaluation -->
              <g transform="translate(200, 25)">
                <text x="60" y="30" fill="#cbd5e1" font-size="20" font-weight="800">${aVal} ${bVal}</text>
                <text x="35" y="65" fill="#cbd5e1" font-size="20" font-weight="800">+</text>
                <text x="75" y="65" fill="#cbd5e1" font-size="20" font-weight="800">${bVal}</text>
                <line x1="25" y1="78" x2="105" y2="78" stroke="#94a3b8" stroke-width="2"/>
                <text x="60" y="110" fill="${isValid ? '#34d399' : '#f87171'}" font-size="22" font-weight="900">${sum}</text>
              </g>

              <!-- Status -->
              <text x="170" y="155" fill="${isValid ? '#34d399' : '#fbbf24'}" font-size="11.5" font-weight="800" text-anchor="middle">
                ${isValid ? 'Letters represent unique digits: A=7, B=8, C=6!' : (aVal === cVal ? 'Violation: A and C cannot both be ' + aVal + '!' : 'Testing digits...')}
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="250" width="460" height="65" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="270" fill="#38bdf8" font-size="11.5" font-weight="800" text-anchor="middle">
              Cryptarithm Deduction Rules:
            </text>
            <text x="270" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">
              1. Each letter is a unique digit 0–9 &nbsp;|&nbsp; 2. Leading digits cannot be zero
            </text>
            <text x="270" y="306" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Since A + carry = B, there must be a carry of 1, meaning B = A + 1!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;">
          <button class="sim-btn ${bVal === 7 ? 'active' : ''}" data-b="7">Try B = 7 (67 + 7 = 74)</button>
          <button class="sim-btn ${bVal === 8 ? 'active' : ''}" data-b="8">Try B = 8 (78 + 8 = 86) [Solution!]</button>
          <button class="sim-btn ${bVal === 9 ? 'active' : ''}" data-b="9">Try B = 9 (89 + 9 = 98)</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-b]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          bVal = parseInt(e.target.getAttribute('data-b'));
          simControls.querySelectorAll('button[data-b]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 15: Classic Alphametic Deduction - SEND + MORE = MONEY
    function simClassicAlphameticDeduction() {
      simHeaderTitle.textContent = "The Master Alphametic: Solving SEND + MORE = MONEY";
      let step = 0; // 0 to 4

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0b0f19"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="36" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              ${step === 0 ? 'Dudeney (1924): SEND + MORE = MONEY Puzzle' : step === 1 ? 'Step 1: Carry into 5th column forces M = 1!' : step === 2 ? 'Step 2: S + 1 forces O = 0 and S = 9!' : step === 3 ? 'Step 3: Column carries yield E = 5, N = 6, R = 8!' : 'Solved: 9567 + 1085 = 10652! All digits unique!'}
            </text>

            <!-- Column Addition Display -->
            <g transform="translate(60, 60)">
              <rect x="0" y="0" width="420" height="175" rx="10" fill="#111827" stroke="#334155" stroke-width="1.5"/>

              <!-- Cryptarithm Letters & Substituted Digits -->
              <g transform="translate(60, 25)">
                <!-- Row 1: SEND -->
                <text x="60" y="25" fill="#38bdf8" font-size="20" font-weight="900">
                  ${step >= 2 ? '9' : 'S'} &nbsp;${step >= 3 ? '5' : 'E'} &nbsp;${step >= 3 ? '6' : 'N'} &nbsp;${step >= 4 ? '7' : 'D'}
                </text>

                <!-- Row 2: MORE -->
                <text x="20" y="60" fill="#f59e0b" font-size="20" font-weight="900">+</text>
                <text x="38" y="60" fill="#f59e0b" font-size="20" font-weight="900">
                  ${step >= 1 ? '1' : 'M'} &nbsp;${step >= 2 ? '0' : 'O'} &nbsp;${step >= 3 ? '8' : 'R'} &nbsp;${step >= 3 ? '5' : 'E'}
                </text>

                <line x1="15" y1="72" x2="185" y2="72" stroke="#ffffff" stroke-width="2"/>

                <!-- Row 3: MONEY -->
                <text x="38" y="105" fill="#10b981" font-size="22" font-weight="900">
                  ${step >= 1 ? '1' : 'M'} &nbsp;${step >= 2 ? '0' : 'O'} &nbsp;${step >= 3 ? '6' : 'N'} &nbsp;${step >= 3 ? '5' : 'E'} &nbsp;${step >= 4 ? '2' : 'Y'}
                </text>
              </g>

              <!-- Step Deduction Description Box on Right -->
              <g transform="translate(260, 20)">
                <rect x="0" y="0" width="145" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
                <text x="72" y="22" fill="#38bdf8" font-size="11" font-weight="900" text-anchor="middle">LOGICAL CLUES</text>
                <foreignObject x="8" y="30" width="130" height="95">
                  <div xmlns="http://www.w3.org/1999/xhtml" style="color:#cbd5e1; font-size:9.5px; line-height:1.3;">
                    ${step === 0 ? 'Adding two 4-digit numbers creates a 5-digit number. Start at the fifth column!' : step === 1 ? 'The carry from two 4-digit numbers can only be 1. Since M ≠ 0, M MUST be 1!' : step === 2 ? 'S + 1 = 10 + O. Since S ≤ 9, O must be 0, and S must be 9!' : step === 3 ? 'With M=1, O=0, S=9, columns deduce E=5, N=6, R=8.' : 'D=7, E=5 forces Y=2. Check: 9567 + 1085 = 10652!'}
                  </div>
                </foreignObject>
              </g>
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="245" width="480" height="70" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="267" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              The Art of Mathematical Deduction:
            </text>
            <text x="270" y="287" fill="#cbd5e1" font-size="11" text-anchor="middle">
              No trial-and-error guessing needed! Every digit is forced by carryover constraints.
            </text>
            <text x="270" y="303" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">
              Click the step buttons to watch the puzzle unlock column by column!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;">
          <button class="sim-btn ${step === 0 ? 'active' : ''}" data-step="0">Start</button>
          <button class="sim-btn ${step === 1 ? 'active' : ''}" data-step="1">1. Find M = 1</button>
          <button class="sim-btn ${step === 2 ? 'active' : ''}" data-step="2">2. Find O=0, S=9</button>
          <button class="sim-btn ${step === 3 ? 'active' : ''}" data-step="3">3. Find E, N, R</button>
          <button class="sim-btn ${step === 4 ? 'active' : ''}" data-step="4">4. Complete Solution</button>
        </div>
      `;

      simControls.querySelectorAll('button[data-step]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          step = parseInt(e.target.getAttribute('data-step'));
          simControls.querySelectorAll('button[data-step]').forEach(b => b.classList.remove('active'));
          e.target.classList.add('active');
          render();
        });
      });

      render();
    }

    // Slide 16: Heritage Review - Meru Prastara (Pingala's Triangle)
    function simHeritageNumberPlay() {
      simHeaderTitle.textContent = "Meru Prastara: Pingala's Ancient Combinatorial Mountain";
      let showFibonacci = false;

      function render() {
        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

            <!-- Top Banner -->
            <rect x="30" y="12" width="480" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="270" y="36" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">
              Acharya Pingala's Meru Prastara (The Staircase of Mount Meru, c. 300 BCE)
            </text>

            <!-- Meru Prastara Pyramid (Pascal's Triangle) -->
            <g transform="translate(270, 65)">
              <!-- Row 0: 1 -->
              <circle cx="0" cy="10" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="0" y="14" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 1: 1 1 -->
              <circle cx="-20" cy="36" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-20" y="40" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="20" cy="36" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="20" y="40" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 2: 1 2 1 -->
              <circle cx="-40" cy="62" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-40" y="66" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="0" cy="62" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="0" y="66" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">2</text>
              <circle cx="40" cy="62" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="40" y="66" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 3: 1 3 3 1 -->
              <circle cx="-60" cy="88" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-60" y="92" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-20" cy="88" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-20" y="92" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">3</text>
              <circle cx="20" cy="88" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="20" y="92" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">3</text>
              <circle cx="60" cy="88" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="60" y="92" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 4: 1 4 6 4 1 -->
              <circle cx="-80" cy="114" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-80" y="118" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-40" cy="114" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-40" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">4</text>
              <circle cx="0" cy="114" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="0" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">6</text>
              <circle cx="40" cy="114" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="40" y="118" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">4</text>
              <circle cx="80" cy="114" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="80" y="118" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              <!-- Row 5: 1 5 10 10 5 1 -->
              <circle cx="-100" cy="140" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="-100" y="144" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>
              <circle cx="-60" cy="140" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="-60" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">5</text>
              <circle cx="-20" cy="140" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="-20" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">10</text>
              <circle cx="20" cy="140" r="13" fill="#059669" stroke="#10b981" stroke-width="2"/>
              <text x="20" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">10</text>
              <circle cx="60" cy="140" r="13" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="60" y="144" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">5</text>
              <circle cx="100" cy="140" r="13" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="100" y="144" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">1</text>

              ${showFibonacci ? `
                <!-- Shallow Diagonals showing Virahanka numbers -->
                <line x1="-120" y1="140" x2="30" y2="40" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
                <text x="-135" y="145" fill="#f59e0b" font-size="12" font-weight="900">Sum = 8!</text>
              ` : ''}
            </g>

            <!-- Bottom Insight -->
            <rect x="30" y="240" width="480" height="75" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#475569" stroke-width="1.5"/>
            <text x="270" y="262" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">
              1,800 Years Before Pascal:
            </text>
            <text x="270" y="282" fill="#cbd5e1" font-size="11" text-anchor="middle">
              Halayudha's 10th-century commentary on Pingala gave the rule: add the two numbers above!
            </text>
            <text x="270" y="300" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
              Amazingly, summing the shallow diagonals in Meru Prastara generates the Virahāńka sequence!
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; justify-content:center; gap:1rem;">
          <button class="sim-btn ${showFibonacci ? 'active' : ''}" id="toggleFibDiagBtn">
            ${showFibonacci ? 'Hide Shallow Diagonals' : 'Reveal Virahāńka Numbers in Diagonals'}
          </button>
        </div>
      `;

      simControls.querySelector('#toggleFibDiagBtn').addEventListener('click', () => {
        showFibonacci = !showFibonacci;
        render();
      });

      render();
    }


    // Navigation Event Listeners
    prevBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx > 0) renderSlide(currentSlideIdx - 1);
    });

    nextBtn.addEventListener('click', () => {
      sfx.playClick();
      if (currentSlideIdx < SLIDES_DATA.length - 1) renderSlide(currentSlideIdx + 1);
    });

    slideJumpSelect.addEventListener('change', (e) => {
      sfx.playClick();
      renderSlide(parseInt(e.target.value));
    });

    // Keyboard Arrow Navigation
    window.addEventListener('keydown', (e) => {
      if (solutionModal.style.display !== 'none') {
        if (e.key === 'Escape') {
          solutionModal.style.display = 'none';
        }
        return;
      }
      if (e.key === 'ArrowRight' && currentSlideIdx < SLIDES_DATA.length - 1) {
        sfx.playClick();
        renderSlide(currentSlideIdx + 1);
      } else if (e.key === 'ArrowLeft' && currentSlideIdx > 0) {
        sfx.playClick();
        renderSlide(currentSlideIdx - 1);
      }
    });

    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      renderSlide(0);
    });
  