"""
Generate 40 Mastery Quiz Questions (10 per slide for Slides 17 to 20)
for NCERT Class 5 Mathematics Chapter 2: Fractions.
Zero raw LaTeX! Clean Unicode symbols throughout.
"""

QUIZ_QUESTIONS = [
    # Challenge 1: Questions 1 to 10 (Slides 1-4 scope: Equal Wholes, Grids, Fraction Kits, Piece Relations)
    {
        "id": 1,
        "question": "Why is 1/2 of a small paratha NOT equal to 1/2 of a large paratha?",
        "options": [
            "Because half always equals one quarter",
            "Because the wholes from which the halves are taken have different sizes",
            "Because parathas cannot be cut into equal halves",
            "Because fractions only apply to rectangular shapes"
        ],
        "answer": 1,
        "explanation": "To compare fractions accurately, the wholes must be identical. Half of a large whole contains more area than half of a small whole.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. A fraction represents a relative portion of a specific whole.<br>2. If Whole A has an area of 50 sq cm, 1/2 of A = 25 sq cm.<br>3. If Whole B has an area of 100 sq cm, 1/2 of B = 50 sq cm.<br>4. Even though both are '1/2', 50 sq cm > 25 sq cm. Wholes must be identical to compare fractions directly."
    },
    {
        "id": 2,
        "question": "A square grid contains 16 identical smaller squares. How many squares represent 1/4 of the grid?",
        "options": [
            "2 squares",
            "4 squares",
            "8 squares",
            "6 squares"
        ],
        "answer": 1,
        "explanation": "To find 1/4 of 16 squares, divide 16 by 4: 16 ÷ 4 = 4 squares.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Total squares in grid = 16.<br>2. Required fraction = 1/4.<br>3. 16 × (1/4) = 16 ÷ 4 = <strong>4 squares</strong>."
    },
    {
        "id": 3,
        "question": "In Grid B with 24 equal squares, 1/6 is shaded in blue. How many blue squares are there?",
        "options": [
            "3 squares",
            "4 squares",
            "6 squares",
            "8 squares"
        ],
        "answer": 1,
        "explanation": "1/6 of 24 = 24 ÷ 6 = 4 squares.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Total squares = 24.<br>2. Fraction shaded = 1/6.<br>3. 24 ÷ 6 = <strong>4 squares</strong>."
    },
    {
        "id": 4,
        "question": "In Grid C with 36 equal squares, 3 squares are shaded yellow. What fraction of Grid C is shaded?",
        "options": [
            "1/6",
            "1/8",
            "1/12",
            "1/9"
        ],
        "answer": 2,
        "explanation": "3 out of 36 is 3/36. Dividing numerator and denominator by 3 gives 1/12.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Shaded squares = 3; Total squares = 36.<br>2. Fraction = 3/36.<br>3. Divide top and bottom by 3: (3 ÷ 3) / (36 ÷ 3) = <strong>1/12</strong>."
    },
    {
        "id": 5,
        "question": "How many 1/8 pieces from the fraction kit equal one 1/2 piece?",
        "options": [
            "2 pieces",
            "4 pieces",
            "6 pieces",
            "8 pieces"
        ],
        "answer": 1,
        "explanation": "4/8 = 1/2. Exactly four 1/8 pieces match the length of one 1/2 piece.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. We want: ? × 1/8 = 1/2.<br>2. Convert 1/2 to eighths: (1 × 4) / (2 × 4) = 4/8.<br>3. Therefore, <strong>4 pieces</strong> of 1/8 are needed."
    },
    {
        "id": 6,
        "question": "How many 1/4 pieces are needed to make one complete whole strip?",
        "options": [
            "2 pieces",
            "3 pieces",
            "4 pieces",
            "8 pieces"
        ],
        "answer": 2,
        "explanation": "4/4 = 1 Whole. Four 1/4 pieces make 1 whole strip.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Whole = 1.<br>2. 1 ÷ (1/4) = 1 × 4 = <strong>4 pieces</strong>."
    },
    {
        "id": 7,
        "question": "If you combine two 1/4 pieces and four 1/8 pieces, what total fraction of the strip do you have?",
        "options": [
            "1/2",
            "3/4",
            "1 Whole",
            "5/8"
        ],
        "answer": 2,
        "explanation": "Two 1/4 pieces = 2/4 = 1/2. Four 1/8 pieces = 4/8 = 1/2. 1/2 + 1/2 = 1 Whole!",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Two 1/4 pieces = 2/4 = 1/2.<br>2. Four 1/8 pieces = 4/8 = 1/2.<br>3. 1/2 + 1/2 = <strong>1 Whole</strong>."
    },
    {
        "id": 8,
        "question": "Which piece relationship is TRUE in the fraction kit?",
        "options": [
            "Two 1/8 pieces = 1/2",
            "Two 1/8 pieces = 1/4",
            "Two 1/4 pieces = 1 Whole",
            "Four 1/8 pieces = 1/4"
        ],
        "answer": 1,
        "explanation": "2/8 simplifies to 1/4 by dividing numerator and denominator by 2.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 1/8 + 1/8 = 2/8.<br>2. (2 ÷ 2) / (8 ÷ 2) = <strong>1/4</strong>.<br>3. Thus, two 1/8 pieces equal 1/4."
    },
    {
        "id": 9,
        "question": "How many 1/16 pieces equal one 1/4 piece?",
        "options": [
            "2 pieces",
            "4 pieces",
            "8 pieces",
            "16 pieces"
        ],
        "answer": 1,
        "explanation": "4/16 = 1/4. Four 1/16 pieces match the length of one 1/4 piece.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Convert 1/4 to sixteenths: (1 × 4) / (4 × 4) = 4/16.<br>2. So exactly <strong>4 pieces</strong> of 1/16 equal 1/4."
    },
    {
        "id": 10,
        "question": "In a fraction a/b, what does the denominator 'b' represent?",
        "options": [
            "The number of parts we are taking",
            "The total number of equal parts into which the whole is divided",
            "The size of the whole in kilograms",
            "The number of people sharing the food"
        ],
        "answer": 1,
        "explanation": "The denominator tells us the total number of equal parts that constitute one whole unit.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. In any fraction a/b:<br>• <strong>b (Denominator)</strong> = total equal parts dividing the whole.<br>• <strong>a (Numerator)</strong> = number of equal parts taken or considered."
    },

    # Challenge 2: Questions 11 to 20 (Slides 5-7 scope: Building Wholes, Equivalent Fractions, Missing Terms)
    {
        "id": 11,
        "question": "Which combination of fraction pieces equals exactly 1 Whole?",
        "options": [
            "1/2 + 1/4 + 1/8",
            "1/2 + 1/4 + 1/4",
            "1/4 + 1/4 + 1/4",
            "1/3 + 1/3"
        ],
        "answer": 1,
        "explanation": "1/2 + 1/4 + 1/4 = 1/2 + 2/4 = 1/2 + 1/2 = 1 Whole.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 1/4 + 1/4 = 2/4 = 1/2.<br>2. 1/2 + 1/2 = 2/2 = <strong>1 Whole</strong>."
    },
    {
        "id": 12,
        "question": "If you have 1/3 and 2/6, how much more do you need to complete 1 Whole?",
        "options": [
            "1/2",
            "1/3",
            "1/6",
            "1/4"
        ],
        "answer": 1,
        "explanation": "2/6 = 1/3. So 1/3 + 2/6 = 1/3 + 1/3 = 2/3. To reach 3/3 (1 Whole), you need 1/3 more.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Simplify 2/6 = 1/3.<br>2. Current sum = 1/3 + 1/3 = 2/3.<br>3. Needed = 1 - 2/3 = 3/3 - 2/3 = <strong>1/3</strong>."
    },
    {
        "id": 13,
        "question": "Which fraction is NOT equivalent to 1/2?",
        "options": [
            "2/4",
            "3/6",
            "4/8",
            "5/12"
        ],
        "answer": 3,
        "explanation": "In 5/12, half of 12 is 6, not 5. So 5/12 is less than 1/2, not equivalent to 1/2.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 2/4 = 1/2 (divide by 2).<br>2. 3/6 = 1/2 (divide by 3).<br>3. 4/8 = 1/2 (divide by 4).<br>4. 5/12 ≠ 1/2 (since 6/12 = 1/2). So <strong>5/12</strong> is not equivalent to 1/2."
    },
    {
        "id": 14,
        "question": "Find the missing number in: 2/5 = ?/15",
        "options": [
            "4",
            "5",
            "6",
            "8"
        ],
        "answer": 2,
        "explanation": "5 × 3 = 15. So 2 × 3 = 6. 2/5 = 6/15.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Compare denominators: 15 ÷ 5 = 3 (scale factor = 3).<br>2. Multiply numerator by 3: 2 × 3 = <strong>6</strong>.<br>3. Therefore, 2/5 = 6/15."
    },
    {
        "id": 15,
        "question": "Find the missing denominator: 3/4 = 12/?",
        "options": [
            "14",
            "15",
            "16",
            "18"
        ],
        "answer": 2,
        "explanation": "3 × 4 = 12. So 4 × 4 = 16. 3/4 = 12/16.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Compare numerators: 12 ÷ 3 = 4 (scale factor = 4).<br>2. Multiply denominator by 4: 4 × 4 = <strong>16</strong>.<br>3. Therefore, 3/4 = 12/16."
    },
    {
        "id": 16,
        "question": "What is the simplest (lowest terms) form of 8/12?",
        "options": [
            "4/6",
            "2/3",
            "1/2",
            "3/4"
        ],
        "answer": 1,
        "explanation": "Divide both 8 and 12 by their greatest common factor, 4: 8 ÷ 4 = 2, and 12 ÷ 4 = 3. The simplest form is 2/3.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Factors of 8: 1, 2, 4, 8.<br>2. Factors of 12: 1, 2, 3, 4, 6, 12.<br>3. Highest common factor = 4.<br>4. (8 ÷ 4) / (12 ÷ 4) = <strong>2/3</strong>."
    },
    {
        "id": 17,
        "question": "If you multiply the numerator and denominator of 4/7 by 5, what equivalent fraction do you get?",
        "options": [
            "20/35",
            "9/12",
            "20/28",
            "16/35"
        ],
        "answer": 0,
        "explanation": "(4 × 5) / (7 × 5) = 20/35.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Numerator: 4 × 5 = 20.<br>2. Denominator: 7 × 5 = 35.<br>3. Result = <strong>20/35</strong>."
    },
    {
        "id": 18,
        "question": "Which two fractions are equivalent?",
        "options": [
            "2/3 and 4/9",
            "3/5 and 6/10",
            "1/4 and 2/6",
            "3/4 and 6/12"
        ],
        "answer": 1,
        "explanation": "3/5 = (3 × 2) / (5 × 2) = 6/10. Cross multiplication: 3 × 10 = 30 and 5 × 6 = 30.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. For 3/5 and 6/10: 3 × 2 = 6, and 5 × 2 = 10.<br>2. Cross check: 3 × 10 = 30; 5 × 6 = 30 (Equal!).<br>3. So <strong>3/5 and 6/10</strong> are equivalent."
    },
    {
        "id": 19,
        "question": "Find the missing value: 5/8 = 25/?",
        "options": [
            "35",
            "40",
            "45",
            "30"
        ],
        "answer": 1,
        "explanation": "5 × 5 = 25. So 8 × 5 = 40. 5/8 = 25/40.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 25 ÷ 5 = 5.<br>2. 8 × 5 = <strong>40</strong>.<br>3. Therefore, 5/8 = 25/40."
    },
    {
        "id": 20,
        "question": "What happens to the value of a fraction if you multiply both numerator and denominator by 10?",
        "options": [
            "The value becomes 10 times larger",
            "The value becomes 10 times smaller",
            "The value stays exactly the same",
            "The fraction becomes improper"
        ],
        "answer": 2,
        "explanation": "Multiplying both numerator and denominator by the same non-zero number produces an equivalent fraction with the exact same value.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Multiplying top and bottom by 10 is equivalent to multiplying by 10/10, which equals 1.<br>2. Any number multiplied by 1 <strong>stays exactly the same</strong> in value."
    },

    # Challenge 3: Questions 21 to 30 (Slides 8-10 scope: Same Denominator, Same Numerator, Fractions > 1)
    {
        "id": 21,
        "question": "Compare: 4/9 ___ 7/9",
        "options": [
            ">",
            "<",
            "=",
            "Cannot be compared"
        ],
        "answer": 1,
        "explanation": "Since denominators are identical (9), compare numerators: 4 < 7. So 4/9 < 7/9.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Denominators match: both are 9.<br>2. Compare numerators: 4 < 7.<br>3. Therefore, <strong>4/9 < 7/9</strong>."
    },
    {
        "id": 22,
        "question": "Compare: 5/7 ___ 5/9",
        "options": [
            ">",
            "<",
            "=",
            "None of these"
        ],
        "answer": 0,
        "explanation": "When numerators match, the smaller denominator has larger pieces. Since 7 < 9, sevenths are bigger than ninths: 5/7 > 5/9.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Numerators match: both are 5.<br>2. Compare denominators: 7 < 9.<br>3. Smaller denominator means larger piece size: 1/7 > 1/9.<br>4. Therefore, <strong>5/7 > 5/9</strong>."
    },
    {
        "id": 23,
        "question": "Which of these fractions is the LARGEST?",
        "options": [
            "2/9",
            "2/7",
            "2/5",
            "2/3"
        ],
        "answer": 3,
        "explanation": "All numerators are 2. The smallest denominator (3) produces the largest individual pieces. So 2/3 is the largest.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. All numerators = 2.<br>2. Smallest denominator = 3 (thirds are larger than fifths, sevenths, or ninths).<br>3. Therefore, <strong>2/3</strong> is the largest fraction."
    },
    {
        "id": 24,
        "question": "Which of these fractions is the SMALLEST?",
        "options": [
            "5/6",
            "3/6",
            "1/6",
            "4/6"
        ],
        "answer": 2,
        "explanation": "All denominators are 6. The smallest numerator (1) represents the fewest slices: 1/6 is the smallest.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. All denominators = 6.<br>2. Compare numerators: 1 < 3 < 4 < 5.<br>3. Therefore, <strong>1/6</strong> is the smallest."
    },
    {
        "id": 25,
        "question": "Which of the following is an improper fraction (greater than 1)?",
        "options": [
            "5/6",
            "3/4",
            "8/5",
            "7/9"
        ],
        "answer": 2,
        "explanation": "In 8/5, the numerator 8 is greater than the denominator 5, making it an improper fraction greater than 1.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. A fraction is improper if numerator ≥ denominator.<br>2. For 8/5: 8 > 5.<br>3. 8/5 = 1 3/5, which is <strong>greater than 1</strong>."
    },
    {
        "id": 26,
        "question": "If you have 7 half-parathas (7 × 1/2), how many whole parathas and leftover halves do you have?",
        "options": [
            "2 whole parathas and 1 half",
            "3 whole parathas and 1 half",
            "4 whole parathas",
            "3 whole parathas and no halves"
        ],
        "answer": 1,
        "explanation": "7 ÷ 2 = 3 with remainder 1. So 7 halves = 3 whole parathas and 1/2 paratha.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Every 2 halves make 1 whole.<br>2. 7 ÷ 2 = 3 with remainder 1.<br>3. So 7/2 = <strong>3 wholes and 1/2</strong> (3 1/2)."
    },
    {
        "id": 27,
        "question": "What is 10/4 simplified and expressed as a mixed number?",
        "options": [
            "2 1/4",
            "2 1/2",
            "2 3/4",
            "3 1/4"
        ],
        "answer": 1,
        "explanation": "10 ÷ 4 = 2 with remainder 2, which gives 2 2/4. Simplifying 2/4 gives 2 1/2.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 10 ÷ 4 = 2 with remainder 2 &rarr; 2 2/4.<br>2. Simplify 2/4 by dividing by 2 &rarr; 1/2.<br>3. Result = <strong>2 1/2</strong>."
    },
    {
        "id": 28,
        "question": "Which symbol makes this statement true: 7/8 ___ 7/10?",
        "options": [
            ">",
            "<",
            "=",
            "+"
        ],
        "answer": 0,
        "explanation": "Same numerator (7). Denominator 8 < 10, so eighths are larger than tenths: 7/8 > 7/10.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Numerators are equal: 7 = 7.<br>2. Denominators: 8 < 10 &rarr; 1/8 > 1/10.<br>3. Therefore, <strong>7/8 > 7/10</strong>."
    },
    {
        "id": 29,
        "question": "How many whole units are in 15/5?",
        "options": [
            "2",
            "3",
            "4",
            "5"
        ],
        "answer": 1,
        "explanation": "15 ÷ 5 = 3 exactly, with zero remainder. So 15/5 = 3 whole units.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 15 ÷ 5 = <strong>3</strong>.<br>2. There is no fractional remainder; 15/5 is equal to the whole number 3."
    },
    {
        "id": 30,
        "question": "If Kabir eats 3/8 of a pizza and Ananya eats 5/8 of the same pizza, who ate more?",
        "options": [
            "Kabir ate more",
            "Ananya ate more",
            "Both ate the same amount",
            "Cannot be determined"
        ],
        "answer": 1,
        "explanation": "5/8 > 3/8 because denominators are identical and 5 > 3. Ananya ate more.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Compare 5/8 and 3/8.<br>2. 5/8 > 3/8.<br>3. Therefore, <strong>Ananya ate more</strong>."
    },

    # Challenge 4: Questions 31 to 40 (Slides 11-16 scope: Mixed Numbers, Benchmarks, Ant Parade, Family Riddle)
    {
        "id": 31,
        "question": "Convert the improper fraction 13/4 to a mixed number:",
        "options": [
            "3 1/4",
            "3 3/4",
            "2 3/4",
            "4 1/4"
        ],
        "answer": 0,
        "explanation": "13 ÷ 4 = 3 with remainder 1. So 13/4 = 3 1/4.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Divide 13 by 4: 13 ÷ 4 = 3 (whole number).<br>2. Remainder = 13 - (4 × 3) = 1.<br>3. Mixed number = <strong>3 1/4</strong>."
    },
    {
        "id": 32,
        "question": "Convert the mixed number 2 3/5 back to an improper fraction:",
        "options": [
            "11/5",
            "13/5",
            "15/5",
            "10/5"
        ],
        "answer": 1,
        "explanation": "(2 × 5) + 3 = 10 + 3 = 13. So 2 3/5 = 13/5.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Multiply whole number by denominator: 2 × 5 = 10.<br>2. Add numerator: 10 + 3 = 13.<br>3. Keep denominator: <strong>13/5</strong>."
    },
    {
        "id": 33,
        "question": "Compare 6/7 and 8/5 using 1 as a benchmark:",
        "options": [
            "6/7 > 8/5",
            "6/7 < 8/5",
            "6/7 = 8/5",
            "Cannot be compared"
        ],
        "answer": 1,
        "explanation": "6/7 < 1 (proper fraction). 8/5 > 1 (improper fraction). Therefore, 6/7 < 8/5.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Benchmark check against 1:<br>• 6/7 < 1 (since 6 < 7).<br>• 8/5 > 1 (since 8 > 5).<br>2. Since 6/7 < 1 < 8/5, we know <strong>6/7 < 8/5</strong>."
    },
    {
        "id": 34,
        "question": "Which of these fractions is strictly LESS than 1/2?",
        "options": [
            "4/8",
            "5/8",
            "3/8",
            "7/12"
        ],
        "answer": 2,
        "explanation": "Half of 8 is 4. In 3/8, the numerator 3 is less than 4, so 3/8 < 1/2.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Benchmark 1/2 of 8 = 4/8.<br>2. Comparing: 3/8 < 4/8.<br>3. Therefore, <strong>3/8</strong> is less than 1/2."
    },
    {
        "id": 35,
        "question": "Which of these fractions is strictly GREATER than 1/2?",
        "options": [
            "4/10",
            "5/10",
            "7/10",
            "3/10"
        ],
        "answer": 2,
        "explanation": "Half of 10 is 5. In 7/10, the numerator 7 is greater than 5, so 7/10 > 1/2.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Benchmark 1/2 of 10 = 5/10.<br>2. 7/10 > 5/10.<br>3. Therefore, <strong>7/10</strong> is greater than 1/2."
    },
    {
        "id": 36,
        "question": "A line of 16 ants marches in a line. Each ant is 1/4 cm long. What is the total length of the line?",
        "options": [
            "2 cm",
            "3 cm",
            "4 cm",
            "8 cm"
        ],
        "answer": 2,
        "explanation": "Total length = 16 × 1/4 = 16/4 = 4 cm.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Length of 1 ant = 1/4 cm.<br>2. Number of ants = 16.<br>3. Total length = 16 × 1/4 = 16/4 = <strong>4 cm</strong>."
    },
    {
        "id": 37,
        "question": "If 20 ants each measure 1/4 cm, what is the total length of the parade?",
        "options": [
            "4 cm",
            "5 cm",
            "6 cm",
            "10 cm"
        ],
        "answer": 1,
        "explanation": "20 × 1/4 = 20/4 = 5 cm.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 20 × (1/4) = 20/4 cm.<br>2. 20 ÷ 4 = <strong>5 cm</strong>."
    },
    {
        "id": 38,
        "question": "In the Family Riddle: 'If the only brother of your father's sister had a child, what would be the child's relationship with you?'",
        "options": [
            "Uncle",
            "Cousin",
            "Your sibling (or yourself)",
            "Grandfather"
        ],
        "answer": 2,
        "explanation": "Father's sister is your aunt. Her ONLY brother is your father. A child of your father is your sibling (or yourself).",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Father's sister = Aunt (Bua).<br>2. Only brother of Aunt = Your Father.<br>3. Child of your Father = <strong>Your sibling (brother/sister) or yourself</strong>."
    },
    {
        "id": 39,
        "question": "Between which two numbers on a number line does 9/2 lie?",
        "options": [
            "Between 3 and 4",
            "Between 4 and 5",
            "Between 5 and 6",
            "Between 2 and 3"
        ],
        "answer": 1,
        "explanation": "9 ÷ 2 = 4 1/2. 4 1/2 lies exactly halfway between 4 and 5.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. 9 ÷ 2 = 4 with remainder 1 &rarr; 4 1/2.<br>2. 4 1/2 is greater than 4 and less than 5.<br>3. So it lies <strong>between 4 and 5</strong>."
    },
    {
        "id": 40,
        "question": "Which fraction is equivalent to 3/4 AND has a denominator of 20?",
        "options": [
            "12/20",
            "15/20",
            "16/20",
            "18/20"
        ],
        "answer": 1,
        "explanation": "From 4 to 20, multiply by 5. (3 × 5) / (4 × 5) = 15/20.",
        "solution_html": "<strong>Step-by-Step Solution:</strong><br>1. Target denominator = 20.<br>2. Scale factor: 20 ÷ 4 = 5.<br>3. Multiply numerator by 5: 3 × 5 = 15.<br>4. Result = <strong>15/20</strong>."
    }
]

print("Mastery Quiz Questions (40 questions) authored successfully.")

