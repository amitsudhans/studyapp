# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 13: Animal Jumps - Part 3 (Slides 17 to 20)
Syllabus: Joyful Mathematics (NEP 2020)
40 Comprehensive Quiz Questions (10 per challenge slide)
- Zero human names
- Zero raw LaTeX
- Full solution_html with step-by-step derivation
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Multiplier Magic Box, Factors, Array Models & Prime Numbers",
        "questions": [
            {
                "question": "If input 7 produces 28 and input 9 produces 36 in the magic box, what will input 14 produce?",
                "options": ["42", "56", "64", "70"],
                "answer": 1,
                "explanation": "The secret multiplier is 4 (28 ÷ 7 = 4). Therefore, 14 × 4 = 56.",
                "hint": "Multiply the input 14 by the secret multiplier 4.",
                "solution_html": "<div class='space-y-2'><p>1. Secret Multiplier = 28 ÷ 7 = 4.</p><p>2. Output = 14 × 4 = <strong>56</strong>.</p></div>"
            },
            {
                "question": "Which of the following multiplication equations shows that 15 is a multiple of both 3 and 5?",
                "options": ["3 + 5 = 8", "15 − 5 = 10", "3 × 5 = 15", "15 ÷ 3 = 5"],
                "answer": 2,
                "explanation": "3 × 5 = 15 directly demonstrates that 15 is the product (multiple) of factors 3 and 5.",
                "hint": "Look for the multiplication sentence linking 3, 5, and 15.",
                "solution_html": "<div class='space-y-2'><p>1. Product of factors: 3 × 5 = 15.</p><p>2. Therefore, 15 is a multiple of 3 and 5.</p></div>"
            },
            {
                "question": "How many different rectangular arrays can be constructed using 12 square tiles?",
                "options": ["2 arrays", "3 arrays", "4 arrays", "6 arrays"],
                "answer": 1,
                "explanation": "12 tiles can form 1×12, 2×6, and 3×4. That makes 3 distinct rectangular arrays.",
                "hint": "Find how many unique factor pairs 12 has.",
                "solution_html": "<div class='space-y-2'><p>1. Rectangles: 1 × 12, 2 × 6, 3 × 4.</p><p>2. Total distinct rectangles = <strong>3</strong>.</p></div>"
            },
            {
                "question": "What is the complete set of factors for the number 10?",
                "options": ["{1, 10}", "{2, 5}", "{1, 2, 5, 10}", "{1, 2, 4, 5, 10}"],
                "answer": 2,
                "explanation": "10 can be factored as 1 × 10 and 2 × 5. Its complete set of factors is {1, 2, 5, 10}.",
                "hint": "List all whole numbers that divide 10 with zero remainder.",
                "solution_html": "<div class='space-y-2'><p>1. 10 ÷ 1 = 10, 10 ÷ 2 = 5.</p><p>2. Factors are <strong>1, 2, 5, 10</strong>.</p></div>"
            },
            {
                "question": "Which of the following numbers is a prime number?",
                "options": ["9", "13", "15", "21"],
                "answer": 1,
                "explanation": "13 has exactly two factors: 1 and 13. Numbers 9, 15, and 21 have more than two factors.",
                "hint": "A prime number cannot be divided evenly by any number other than 1 and itself.",
                "solution_html": "<div class='space-y-2'><p>1. 13 has only factors 1 and 13.</p><p>2. <strong>13 is prime</strong>.</p></div>"
            },
            {
                "question": "Why is the number 14 classified as a composite number?",
                "options": [
                    "It is an even number",
                    "It has more than two factors: 1, 2, 7, and 14",
                    "It can be divided by 3",
                    "It has only two factors"
                ],
                "answer": 1,
                "explanation": "Any whole number with more than two factors is composite. 14 has 4 factors: 1, 2, 7, 14.",
                "hint": "Check how many factors 14 has.",
                "solution_html": "<div class='space-y-2'><p>1. Factors of 14: 1, 2, 7, 14.</p><p>2. Having 4 factors makes it <strong>composite</strong>.</p></div>"
            },
            {
                "question": "Why is the number 1 neither prime nor composite?",
                "options": [
                    "Because 1 is an odd number",
                    "Because it has only one factor (1 itself)",
                    "Because 1 is the smallest number",
                    "Because it cannot be multiplied"
                ],
                "answer": 1,
                "explanation": "Primes need exactly 2 factors and composites need more than 2. 1 has only 1 factor.",
                "hint": "A prime must have exactly two distinct factors.",
                "solution_html": "<div class='space-y-2'><p>1. Factors of 1 = {1} (only 1 factor).</p><p>2. Therefore, 1 is <strong>neither prime nor composite</strong>.</p></div>"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "answer": 2,
                "explanation": "2 is the smallest prime number, and it is the only even prime number.",
                "hint": "Recall that 1 is not prime.",
                "solution_html": "<div class='space-y-2'><p>1. 0 and 1 are not prime.</p><p>2. 2 has factors {1, 2}, so <strong>2 is the smallest prime</strong>.</p></div>"
            },
            {
                "question": "If a magic box multiplies every input by 5, what output rolls out when 16 enters?",
                "options": ["65", "75", "80", "85"],
                "answer": 2,
                "explanation": "16 × 5 = 80.",
                "hint": "Multiply 16 by 5.",
                "solution_html": "<div class='space-y-2'><p>1. Output = 16 × 5.</p><p>2. 16 × 5 = <strong>80</strong>.</p></div>"
            },
            {
                "question": "Why do square numbers like 16 and 25 have an ODD number of factors?",
                "options": [
                    "Because they are odd numbers",
                    "Because their middle factor pair consists of the same number multiplied by itself",
                    "Because they are prime numbers",
                    "Because they cannot form rectangles"
                ],
                "answer": 1,
                "explanation": "In 16, the factor pair 4×4 uses the same number twice, so 4 is listed only once, giving 5 factors.",
                "hint": "Think about 4 × 4 = 16." ,
                "solution_html": "<div class='space-y-2'><p>1. Factors of 16: 1, 2, 4, 8, 16 (5 factors).</p><p>2. The repeated factor 4 creates an <strong>odd count</strong>.</p></div>"
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Animal Number Line Jumps, Common Multiples & Trail Puzzles",
        "questions": [
            {
                "question": "A rabbit leaps in steps of 4 and a frog hops in steps of 3 from 0. What is their first shared landing tile?",
                "options": ["6", "7", "12", "24"],
                "answer": 2,
                "explanation": "The least common multiple of 4 and 3 is 12 (4×3 = 12).",
                "hint": "Find the smallest number divisible by both 3 and 4.",
                "solution_html": "<div class='space-y-2'><p>1. Multiples of 4: 4, 8, 12, 16...</p><p>2. Multiples of 3: 3, 6, 9, 12...</p><p>3. First common tile = <strong>12</strong>.</p></div>"
            },
            {
                "question": "What is the second common tile where both the rabbit (step 4) and frog (step 3) will land?",
                "options": ["18", "20", "24", "36"],
                "answer": 2,
                "explanation": "Common multiples of 3 and 4 are multiples of 12: 12, 24, 36... The second is 24.",
                "hint": "Double the least common multiple 12.",
                "solution_html": "<div class='space-y-2'><p>1. 1st common = 12.</p><p>2. 2nd common = 12 × 2 = <strong>24</strong>.</p></div>"
            },
            {
                "question": "A spider leaps in steps of 3 and a grasshopper leaps in steps of 6. What is their least common multiple?",
                "options": ["3", "6", "9", "18"],
                "answer": 1,
                "explanation": "Since 6 is a multiple of 3 (3 × 2 = 6), 6 is their least common multiple.",
                "hint": "When one number divides another, the larger is their LCM.",
                "solution_html": "<div class='space-y-2'><p>1. 6 is divisible by 3.</p><p>2. LCM(3, 6) = <strong>6</strong>.</p></div>"
            },
            {
                "question": "What is the least common multiple (LCM) of 6 and 8?",
                "options": ["14", "18", "24", "48"],
                "answer": 2,
                "explanation": "Multiples of 6: 6, 12, 18, 24... Multiples of 8: 8, 16, 24... LCM = 24.",
                "hint": "Check the smallest multiple of 8 that is divisible by 6.",
                "solution_html": "<div class='space-y-2'><p>1. 8 × 1 = 8 (no), 8 × 2 = 16 (no), 8 × 3 = 24 (24 ÷ 6 = 4).</p><p>2. LCM = <strong>24</strong>.</p></div>"
            },
            {
                "question": "What is the least common multiple of 4 and 6?",
                "options": ["10", "12", "18", "24"],
                "answer": 1,
                "explanation": "Multiples of 4: 4, 8, 12... Multiples of 6: 6, 12... LCM = 12.",
                "hint": "Find the smallest number that 4 and 6 divide into evenly.",
                "solution_html": "<div class='space-y-2'><p>1. Multiples of 4: 4, 8, 12.</p><p>2. Multiples of 6: 6, 12.</p><p>3. LCM = <strong>12</strong>.</p></div>"
            },
            {
                "question": "What is the least common multiple of 8 and 12?",
                "options": ["16", "24", "32", "96"],
                "answer": 1,
                "explanation": "Multiples of 8: 8, 16, 24... Multiples of 12: 12, 24... LCM = 24.",
                "hint": "Check 12 × 2 = 24.",
                "solution_html": "<div class='space-y-2'><p>1. 12 × 2 = 24.</p><p>2. 24 ÷ 8 = 3. LCM = <strong>24</strong>.</p></div>"
            },
            {
                "question": "What is the least common multiple of 9 and 12?",
                "options": ["18", "27", "36", "72"],
                "answer": 2,
                "explanation": "Multiples of 9: 9, 18, 27, 36... Multiples of 12: 12, 24, 36... LCM = 36.",
                "hint": "Look for a shared multiple in the 30s.",
                "solution_html": "<div class='space-y-2'><p>1. 12 × 3 = 36.</p><p>2. 36 ÷ 9 = 4. LCM = <strong>36</strong>.</p></div>"
            },
            {
                "question": "If the LCM of two numbers is 20, which of the following is NOT a common multiple?",
                "options": ["40", "60", "70", "100"],
                "answer": 2,
                "explanation": "All common multiples must be multiples of the LCM 20. 70 is not a multiple of 20.",
                "hint": "Check which option is not divisible by 20.",
                "solution_html": "<div class='space-y-2'><p>1. Multiples of 20: 20, 40, 60, 80, 100...</p><p>2. <strong>70</strong> is not a multiple of 20.</p></div>"
            },
            {
                "question": "In the cobbled road race, how many leaps does a rabbit taking 4-step jumps need to reach tile 64?",
                "options": ["12 leaps", "14 leaps", "16 leaps", "18 leaps"],
                "answer": 2,
                "explanation": "64 ÷ 4 = 16 leaps.",
                "hint": "Divide 64 by 4.",
                "solution_html": "<div class='space-y-2'><p>1. Jumps = 64 ÷ 4.</p><p>2. 64 ÷ 4 = <strong>16 leaps</strong>.</p></div>"
            },
            {
                "question": "Why does a deer taking 6-step jumps miss tile 64 in the cobbled road race?",
                "options": [
                    "Because the deer jumps too fast",
                    "Because 64 is not divisible by 6 (64 ÷ 6 = 10 remainder 4)",
                    "Because 64 is an odd number",
                    "Because 6 is a prime number"
                ],
                "answer": 1,
                "explanation": "6 × 10 = 60 and 6 × 11 = 66. The deer lands on 60 and then 66, completely missing 64.",
                "hint": "Check the remainder when 64 is divided by 6.",
                "solution_html": "<div class='space-y-2'><p>1. 6 × 10 = 60, 6 × 11 = 66.</p><p>2. 64 is not a multiple of 6 (remainder 4).</p></div>"
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Common Factors, Divisibility Trails & Highest Common Factor",
        "questions": [
            {
                "question": "In the jungle trail, 2-step jumps touch stones 4, 12, 14, and 50. What is 2 called for this set of numbers?",
                "options": ["A multiple", "A common factor", "A prime multiple", "A composite factor"],
                "answer": 1,
                "explanation": "Because 2 divides each number completely without remainder, 2 is their common factor.",
                "hint": "A divisor shared by several numbers is their common factor.",
                "solution_html": "<div class='space-y-2'><p>1. 2 divides 4, 12, 14, and 50 evenly.</p><p>2. Therefore, 2 is a <strong>common factor</strong>.</p></div>"
            },
            {
                "question": "Which of the following numbers is a common factor of 9, 21, 39, and 57?",
                "options": ["2", "3", "5", "9"],
                "answer": 1,
                "explanation": "3 divides 9 (3), 21 (7), 39 (13), and 57 (19). 3 is their common factor.",
                "hint": "Find the number that divides all four numbers.",
                "solution_html": "<div class='space-y-2'><p>1. 9÷3=3, 21÷3=7, 39÷3=13, 57÷3=19.</p><p>2. Common factor = <strong>3</strong>.</p></div>"
            },
            {
                "question": "What is the mathematical definition of a common factor?",
                "options": [
                    "A number that multiplies to give zero",
                    "A number that divides two or more numbers completely without leaving a remainder",
                    "The sum of two numbers",
                    "A number with only one factor"
                ],
                "answer": 1,
                "explanation": "A common factor divides each number in the set with zero remainder.",
                "hint": "Think about exact division without remainders.",
                "solution_html": "<div class='space-y-2'><p>1. A common factor divides two or more numbers with remainder = 0.</p></div>"
            },
            {
                "question": "What are all the common factors of 8 and 12?",
                "options": ["{1, 2}", "{1, 2, 4}", "{2, 4, 8}", "{1, 2, 3, 4, 6, 8, 12}"],
                "answer": 1,
                "explanation": "Factors of 8 are {1, 2, 4, 8}. Factors of 12 are {1, 2, 3, 4, 6, 12}. Common factors are {1, 2, 4}.",
                "hint": "List factors of both and circle the matches.",
                "solution_html": "<div class='space-y-2'><p>1. Factors of 8: 1, 2, 4, 8.</p><p>2. Factors of 12: 1, 2, 3, 4, 6, 12.</p><p>3. Common = <strong>{1, 2, 4}</strong>.</p></div>"
            },
            {
                "question": "What is the highest common factor (HCF) of 8 and 12?",
                "options": ["2", "4", "8", "12"],
                "answer": 1,
                "explanation": "The common factors of 8 and 12 are 1, 2, and 4. The greatest is 4.",
                "hint": "Identify the largest number in {1, 2, 4}.",
                "solution_html": "<div class='space-y-2'><p>1. Common factors: 1, 2, 4.</p><p>2. Highest Common Factor = <strong>4</strong>.</p></div>"
            },
            {
                "question": "How many common factors do 24 and 36 share?",
                "options": ["3 factors", "4 factors", "5 factors", "6 factors"],
                "answer": 3,
                "explanation": "Common factors of 24 and 36 are 1, 2, 3, 4, 6, and 12 (6 factors total).",
                "hint": "Count {1, 2, 3, 4, 6, 12}.",
                "solution_html": "<div class='space-y-2'><p>1. Shared factors: 1, 2, 3, 4, 6, 12.</p><p>2. Total count = <strong>6 factors</strong>.</p></div>"
            },
            {
                "question": "What is the common factor of any two consecutive numbers, such as 12 and 13?",
                "options": ["Only 1", "1 and 2", "1 and 3", "There are none"],
                "answer": 0,
                "explanation": "Consecutive numbers differ by 1, so no number greater than 1 can divide both. Their only common factor is 1.",
                "hint": "Consecutive numbers are always co-prime.",
                "solution_html": "<div class='space-y-2'><p>1. Consecutive numbers have difference = 1.</p><p>2. Only <strong>1</strong> can divide both.</p></div>"
            },
            {
                "question": "What are all the common factors of 12 and 16?",
                "options": ["{1, 2}", "{1, 2, 4}", "{1, 4}", "{2, 4}"],
                "answer": 1,
                "explanation": "Factors of 12: {1,2,3,4,6,12}. Factors of 16: {1,2,4,8,16}. Common: {1, 2, 4}.",
                "hint": "Check numbers dividing both 12 and 16.",
                "solution_html": "<div class='space-y-2'><p>1. 12: 1, 2, 3, 4, 6, 12.</p><p>2. 16: 1, 2, 4, 8, 16.</p><p>3. Common: <strong>{1, 2, 4}</strong>.</p></div>"
            },
            {
                "question": "What is the only common factor of 2 and 9?",
                "options": ["0", "1", "2", "3"],
                "answer": 1,
                "explanation": "Factors of 2: {1, 2}. Factors of 9: {1, 3, 9}. Their only shared factor is 1.",
                "hint": "2 is prime and does not divide 9.",
                "solution_html": "<div class='space-y-2'><p>1. Factors of 2: 1, 2.</p><p>2. Factors of 9: 1, 3, 9.</p><p>3. Common factor = <strong>1</strong>.</p></div>"
            },
            {
                "question": "What is the highest common factor (HCF) of 9 and 21?",
                "options": ["1", "3", "7", "9"],
                "answer": 1,
                "explanation": "Factors of 9: {1, 3, 9}. Factors of 21: {1, 3, 7, 21}. Common factors: {1, 3}. HCF = 3.",
                "hint": "Find the largest number that divides both 9 and 21.",
                "solution_html": "<div class='space-y-2'><p>1. Common factors of 9 and 21: 1, 3.</p><p>2. HCF = <strong>3</strong>.</p></div>"
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Divisibility Logic, Animal Story Scenarios & Venn Diagram Sorting",
        "questions": [
            {
                "question": "Which statement about factors and multiples is TRUE?",
                "options": [
                    "Factors of even numbers must always be even",
                    "Multiples of odd numbers cannot be even",
                    "Factors of odd numbers cannot be even",
                    "0 can be a factor of any number"
                ],
                "answer": 2,
                "explanation": "If an odd number had an even factor, it would be divisible by 2 and thus even, which is impossible.",
                "hint": "Any multiple of an even number is always even.",
                "solution_html": "<div class='space-y-2'><p>1. Even factor × any integer = Even product.</p><p>2. An odd number can NEVER have an even factor.</p><p>3. <strong>Factors of odd numbers cannot be even</strong> is TRUE.</p></div>"
            },
            {
                "question": "Why is the statement 'Factors of even numbers must be even' FALSE?",
                "options": [
                    "Because 1 is a factor of every even number and 1 is odd",
                    "Because all even numbers are prime",
                    "Because even numbers have no factors",
                    "Because 0 divides all numbers"
                ],
                "answer": 0,
                "explanation": "1 is an odd factor of all even numbers. Also, 10 has factor 5, which is odd.",
                "hint": "Think about the factor 1 or 5 for the number 10.",
                "solution_html": "<div class='space-y-2'><p>1. 10 is even, but its factors include 1 and 5 (odd).</p><p>2. The statement is <strong>FALSE</strong>.</p></div>"
            },
            {
                "question": "Why can 0 NEVER be a factor of any whole number?",
                "options": [
                    "Because 0 is an even number",
                    "Because division by 0 is undefined in mathematics",
                    "Because 0 is too small",
                    "Because 0 is not on the number line"
                ],
                "answer": 1,
                "explanation": "A factor divides a number with zero remainder, but division by zero is mathematically undefined.",
                "hint": "Recall the rule about division by zero.",
                "solution_html": "<div class='space-y-2'><p>1. Division by 0 is undefined.</p><p>2. <strong>0 cannot be a factor</strong> of any number.</p></div>"
            },
            {
                "question": "A tiger hunts every 3 days and a panther hunts every 5 days. After how many days will both hunt together?",
                "options": ["8 days", "10 days", "15 days", "30 days"],
                "answer": 2,
                "explanation": "The least common multiple of 3 and 5 is 15 days.",
                "hint": "Calculate the LCM of 3 and 5.",
                "solution_html": "<div class='space-y-2'><p>1. LCM(3, 5) = 3 × 5 = 15.</p><p>2. They hunt together every <strong>15 days</strong>.</p></div>"
            },
            {
                "question": "Which jump size allows a traveler to visit Bear at stone 30 while avoiding Tiger at stone 25?",
                "options": ["Step size 2", "Step size 5", "Step size 6", "Step size 10"],
                "answer": 2,
                "explanation": "Step 6 touches 6, 12, 18, 24, 30. It lands on 30 and misses 25. Step 5 lands on 25.",
                "hint": "Find a factor of 30 that does not divide 25.",
                "solution_html": "<div class='space-y-2'><p>1. Steps of 6: 6, 12, 18, 24, 30.</p><p>2. Lands on 30 and avoids 25.</p></div>"
            },
            {
                "question": "Which single jump size allows an explorer to visit BOTH Snake at stone 21 and Wolf at stone 35?",
                "options": ["Step size 3", "Step size 5", "Step size 7", "Step size 11"],
                "answer": 2,
                "explanation": "7 is a common factor of 21 (7 × 3 = 21) and 35 (7 × 5 = 35).",
                "hint": "Find a common factor of 21 and 35.",
                "solution_html": "<div class='space-y-2'><p>1. 21 ÷ 7 = 3 (touches 21).</p><p>2. 35 ÷ 7 = 5 (touches 35).</p><p>3. Common step size = <strong>7</strong>.</p></div>"
            },
            {
                "question": "In the divisibility Venn diagram, which region does the number 38 belong to?",
                "options": [
                    "Divisible by 2 only",
                    "Divisible by 5 only",
                    "Divisible by 2, 5, and 10",
                    "None of the circles"
                ],
                "answer": 0,
                "explanation": "38 is even (38 ÷ 2 = 19) but does not end in 0 or 5, so it is divisible by 2 only.",
                "hint": "Check the last digit of 38.",
                "solution_html": "<div class='space-y-2'><p>1. 38 ends in 8 ➔ Divisible by 2.</p><p>2. Does not end in 0 or 5 ➔ Not divisible by 5 or 10.</p><p>3. Belongs to <strong>Divisible by 2 only</strong>.</p></div>"
            },
            {
                "question": "In the divisibility Venn diagram, which region does the number 75 belong to?",
                "options": [
                    "Divisible by 2 only",
                    "Divisible by 5 only",
                    "Divisible by 2, 5, and 10",
                    "Divisible by 10 only"
                ],
                "answer": 1,
                "explanation": "75 is odd (not divisible by 2) and ends in 5, so it is divisible by 5 only.",
                "hint": "75 ends in 5 and is not even.",
                "solution_html": "<div class='space-y-2'><p>1. 75 ends in 5 ➔ Divisible by 5.</p><p>2. 75 is odd ➔ Not divisible by 2.</p><p>3. Belongs to <strong>Divisible by 5 only</strong>.</p></div>"
            },
            {
                "question": "Which of the following numbers belongs in the central overlap region (divisible by 2, 5, and 10 simultaneously)?",
                "options": ["45", "62", "90", "95"],
                "answer": 2,
                "explanation": "90 ends in 0: 90 ÷ 2 = 45, 90 ÷ 5 = 18, and 90 ÷ 10 = 9.",
                "hint": "A number divisible by both 2 and 5 must end in 0.",
                "solution_html": "<div class='space-y-2'><p>1. 90 ends in 0.</p><p>2. Divisible by 2, 5, and 10.</p><p>3. Belongs in the <strong>central overlap</strong>.</p></div>"
            },
            {
                "question": "Why is it mathematically impossible for a number to be divisible by 10 without also being divisible by 2 and 5?",
                "options": [
                    "Because 10 is an even number",
                    "Because 2 and 5 are factors of 10 (10 = 2 × 5)",
                    "Because 10 has no multiples",
                    "Because 10 is smaller than 2 and 5"
                ],
                "answer": 1,
                "explanation": "Since 10 = 2 × 5, any number that has 10 as a factor must automatically have 2 and 5 as factors as well.",
                "hint": "Think about the prime factorization of 10.",
                "solution_html": "<div class='space-y-2'><p>1. 10 = 2 × 5.</p><p>2. Every multiple of 10 contains factors 2 and 5.</p><p>3. Therefore, it is <strong>always divisible by 2 and 5</strong>.</p></div>"
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part3:
        print(f"Slide {s['id']} ({s['title']}): {len(s['questions'])} questions")
